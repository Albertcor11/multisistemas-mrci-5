#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import posixpath
import re
import unicodedata
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "c": "http://schemas.openxmlformats.org/drawingml/2006/chart",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}
CHART_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/chart"


def normalize(value: str) -> str:
    return unicodedata.normalize("NFC", value.replace("\u00a0", " "))


def slide_numbers(package: zipfile.ZipFile) -> list[int]:
    numbers = []
    for name in package.namelist():
        match = re.fullmatch(r"ppt/slides/slide(\d+)\.xml", name)
        if match:
            numbers.append(int(match.group(1)))
    return sorted(numbers)


def visible_paragraphs(package: zipfile.ZipFile, number: int) -> list[str]:
    root = ET.fromstring(package.read(f"ppt/slides/slide{number}.xml"))
    result = []
    for paragraph in root.findall(".//a:p", NS):
        value = "".join(node.text or "" for node in paragraph.findall(".//a:t", NS))
        if value:
            result.append(normalize(value))
    return result


def resolve_target(base_part: str, target: str) -> str:
    if target.startswith("/"):
        return target.lstrip("/")
    return posixpath.normpath(posixpath.join(posixpath.dirname(base_part), target))


def canonical_chart_value(value: str) -> str:
    value = normalize(value)
    try:
        number = float(value)
    except ValueError:
        return value
    if abs(number - round(number)) < 1e-12:
        return str(int(round(number)))
    return format(number, ".12g")


def chart_values(package: zipfile.ZipFile, number: int) -> list[list[str]]:
    slide_part = f"ppt/slides/slide{number}.xml"
    rels_part = f"ppt/slides/_rels/slide{number}.xml.rels"
    if rels_part not in package.namelist():
        return []
    rels = ET.fromstring(package.read(rels_part))
    targets = [
        resolve_target(slide_part, rel.get("Target", ""))
        for rel in rels.findall("rel:Relationship", NS)
        if rel.get("Type") == CHART_REL
    ]
    result = []
    for target in targets:
        root = ET.fromstring(package.read(target))
        result.append([canonical_chart_value(node.text or "") for node in root.findall(".//c:v", NS)])
    return sorted(result, key=lambda values: json.dumps(values, ensure_ascii=False))


def find_render(directory: Path, number: int) -> Path | None:
    for name in (f"slide-{number}.png", f"{number}.png", f"slide{number}.png"):
        candidate = directory / name
        if candidate.exists():
            return candidate
    return None


def compare_renders(source_dir: Path, output_dir: Path, numbers: list[int]) -> dict:
    try:
        from PIL import Image, ImageChops, ImageStat
    except ImportError as error:
        raise SystemExit("Pillow is required when render directories are supplied") from error

    slides = []
    for number in numbers:
        source_path = find_render(source_dir, number)
        output_path = find_render(output_dir, number)
        if source_path is None or output_path is None:
            slides.append({"slide": number, "status": "missing_render"})
            continue
        source_image = Image.open(source_path).convert("RGB")
        output_image = Image.open(output_path).convert("RGB")
        if source_image.size != output_image.size:
            slides.append({"slide": number, "status": "size_mismatch"})
            continue
        difference = ImageChops.difference(source_image, output_image)
        bounds = difference.getbbox()
        rms = ImageStat.Stat(difference).rms
        slides.append({
            "slide": number,
            "status": "identical" if bounds is None else "different",
            "difference_bbox": list(bounds) if bounds else None,
            "rms": round((sum(value * value for value in rms) / 3) ** 0.5, 6),
        })
    return {
        "performed": True,
        "passed": all(item["status"] == "identical" for item in slides),
        "different_slides": [item["slide"] for item in slides if item["status"] != "identical"],
        "slides": slides,
    }


def audit(args: argparse.Namespace) -> dict:
    with zipfile.ZipFile(args.source) as source, zipfile.ZipFile(args.output) as output:
        source_numbers = slide_numbers(source)
        output_numbers = slide_numbers(output)
        numbers = sorted(set(source_numbers) | set(output_numbers))
        slides = []
        for number in numbers:
            source_text = visible_paragraphs(source, number) if number in source_numbers else []
            output_text = visible_paragraphs(output, number) if number in output_numbers else []
            source_charts = chart_values(source, number) if number in source_numbers else []
            output_charts = chart_values(output, number) if number in output_numbers else []
            slides.append({
                "slide": number,
                "text_exact_order": source_text == output_text,
                "text_exact_multiset": Counter(source_text) == Counter(output_text),
                "chart_values_exact": source_charts == output_charts,
                "missing_text": list((Counter(source_text) - Counter(output_text)).elements()),
                "added_text": list((Counter(output_text) - Counter(source_text)).elements()),
            })
    failed = [
        item["slide"] for item in slides
        if not item["text_exact_multiset"] or not item["chart_values_exact"]
    ]
    render_result = {"performed": False, "passed": None, "different_slides": [], "slides": []}
    if args.source_renders and args.output_renders:
        render_result = compare_renders(args.source_renders, args.output_renders, numbers)
    passed = (
        source_numbers == output_numbers
        and not failed
        and (not render_result["performed"] or render_result["passed"])
    )
    return {
        "source": str(args.source),
        "output": str(args.output),
        "source_slide_count": len(source_numbers),
        "output_slide_count": len(output_numbers),
        "passed": passed,
        "failed_content_slides": failed,
        "render_comparison": render_result,
        "slides": slides,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit exact PPTX content and optional rendered-slide identity")
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("report", type=Path)
    parser.add_argument("--source-renders", type=Path)
    parser.add_argument("--output-renders", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if bool(args.source_renders) != bool(args.output_renders):
        raise SystemExit("Supply both --source-renders and --output-renders, or neither")
    result = audit(args)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "passed": result["passed"],
        "failed_content_slides": result["failed_content_slides"],
        "different_render_slides": result["render_comparison"]["different_slides"],
        "report": str(args.report),
    }, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
