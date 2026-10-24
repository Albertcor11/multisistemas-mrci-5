from __future__ import annotations

import argparse
import collections
import hashlib
import json
import posixpath
import re
import statistics
import zipfile
from pathlib import PurePosixPath

from lxml import etree


NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}
R = f"{{{NS['r']}}}"


def natural_key(value: str) -> list[object]:
    return [int(piece) if piece.isdigit() else piece for piece in re.split(r"(\d+)", value)]


def rels_part(part: str) -> str:
    path = PurePosixPath(part)
    return str(path.parent / "_rels" / f"{path.name}.rels")


def resolve_target(base_part: str, target: str) -> str:
    if target.startswith("/"):
        return target.lstrip("/")
    return posixpath.normpath(posixpath.join(posixpath.dirname(base_part), target))


def parse_rels(package: zipfile.ZipFile, part: str) -> dict[str, dict[str, str]]:
    name = rels_part(part)
    if name not in package.namelist():
        return {}
    root = etree.fromstring(package.read(name))
    return {
        rel.get("Id", ""): {
            "type": rel.get("Type", ""),
            "target": resolve_target(part, rel.get("Target", "")),
        }
        for rel in root
    }


def xfrm(node: etree._Element | None) -> dict[str, float | bool]:
    if node is None:
        return {"x": 0, "y": 0, "w": 0, "h": 0, "rotation": 0.0}
    off = node.find("a:off", NS)
    ext = node.find("a:ext", NS)
    return {
        "x": int(off.get("x", "0")) if off is not None else 0,
        "y": int(off.get("y", "0")) if off is not None else 0,
        "w": int(ext.get("cx", "0")) if ext is not None else 0,
        "h": int(ext.get("cy", "0")) if ext is not None else 0,
        "rotation": int(node.get("rot", "0")) / 60000,
    }


def color_from(node: etree._Element | None) -> str | None:
    if node is None:
        return None
    srgb = node.find("a:solidFill/a:srgbClr", NS)
    if srgb is not None:
        return srgb.get("val")
    scheme = node.find("a:solidFill/a:schemeClr", NS)
    if scheme is not None:
        return f"scheme:{scheme.get('val')}"
    return None


def extract_text(shape: etree._Element) -> tuple[list[str], list[dict]]:
    paragraphs: list[str] = []
    runs: list[dict] = []
    for paragraph in shape.xpath(".//a:p", namespaces=NS):
        pieces: list[str] = []
        for run in paragraph.xpath("./a:r|./a:fld", namespaces=NS):
            text_node = run.find("a:t", NS)
            if text_node is None or text_node.text is None:
                continue
            pieces.append(text_node.text)
            props = run.find("a:rPr", NS)
            size = int(props.get("sz")) / 100 if props is not None and props.get("sz") else None
            latin = props.find("a:latin", NS) if props is not None else None
            runs.append(
                {
                    "text": text_node.text,
                    "size_pt": size,
                    "bold": props is not None and props.get("b", "0") in {"1", "true"},
                    "font": latin.get("typeface") if latin is not None else None,
                    "color": color_from(props),
                }
            )
        text = "".join(pieces).strip()
        if text:
            paragraphs.append(text)
    return paragraphs, runs


def box_pct(box: dict, slide_w: int, slide_h: int) -> dict[str, float]:
    return {
        "x": round(100 * box["x"] / slide_w, 3),
        "y": round(100 * box["y"] / slide_h, 3),
        "w": round(100 * box["w"] / slide_w, 3),
        "h": round(100 * box["h"] / slide_h, 3),
        "rotation": round(float(box["rotation"]), 3),
    }


def inspect(path: str) -> dict:
    with zipfile.ZipFile(path) as package:
        presentation = etree.fromstring(package.read("ppt/presentation.xml"))
        size = presentation.find("p:sldSz", NS)
        slide_w = int(size.get("cx"))
        slide_h = int(size.get("cy"))
        slide_parts = sorted(
            [name for name in package.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)],
            key=natural_key,
        )
        media_hashes = {
            name: hashlib.sha256(package.read(name)).hexdigest()
            for name in package.namelist()
            if name.startswith("ppt/media/") and not name.endswith("/")
        }
        hash_frequency: collections.Counter[str] = collections.Counter()
        global_fonts: collections.Counter[str] = collections.Counter()
        global_sizes: list[float] = []
        global_colors: collections.Counter[str] = collections.Counter()
        slides: list[dict] = []

        for sequence, slide_part in enumerate(slide_parts, start=1):
            root = etree.fromstring(package.read(slide_part))
            rels = parse_rels(package, slide_part)
            text_shapes: list[dict] = []
            pictures: list[dict] = []

            for shape in root.xpath(".//p:sp", namespaces=NS):
                paragraphs, runs = extract_text(shape)
                if not paragraphs:
                    continue
                name_node = shape.find("p:nvSpPr/p:cNvPr", NS)
                box = xfrm(shape.find("p:spPr/a:xfrm", NS))
                sizes = [run["size_pt"] for run in runs if run["size_pt"]]
                fonts = [run["font"] for run in runs if run["font"]]
                colors = [run["color"] for run in runs if run["color"]]
                global_sizes.extend(sizes)
                global_fonts.update(fonts)
                global_colors.update(colors)
                text_shapes.append(
                    {
                        "name": name_node.get("name", "") if name_node is not None else "",
                        "text": "\n".join(paragraphs),
                        "word_count": len(re.findall(r"\b\w+\b", " ".join(paragraphs), re.UNICODE)),
                        "box_pct": box_pct(box, slide_w, slide_h),
                        "font_sizes_pt": sorted(set(round(value, 2) for value in sizes)),
                        "font_median_pt": round(statistics.median(sizes), 2) if sizes else None,
                        "fonts": sorted(set(fonts)),
                        "colors": sorted(set(colors)),
                    }
                )

            for picture in root.xpath(".//p:pic", namespaces=NS):
                name_node = picture.find("p:nvPicPr/p:cNvPr", NS)
                blip = picture.find("p:blipFill/a:blip", NS)
                rid = blip.get(f"{R}embed", "") if blip is not None else ""
                media = rels.get(rid, {}).get("target", "")
                digest = media_hashes.get(media, "")
                if digest:
                    hash_frequency[digest] += 1
                box = xfrm(picture.find("p:spPr/a:xfrm", NS))
                pictures.append(
                    {
                        "name": name_node.get("name", "") if name_node is not None else "",
                        "media": media,
                        "sha256": digest,
                        "box_pct": box_pct(box, slide_w, slide_h),
                        "area_pct": round(100 * box["w"] * box["h"] / (slide_w * slide_h), 3),
                    }
                )

            title_candidate = None
            if text_shapes:
                title_candidate = sorted(
                    text_shapes,
                    key=lambda item: (
                        item["box_pct"]["y"] > 32,
                        -(item["font_median_pt"] or 0),
                        item["box_pct"]["y"],
                    ),
                )[0]
            body_sizes = [
                value
                for shape in text_shapes
                if shape is not title_candidate
                for value in shape["font_sizes_pt"]
                if value > 0
            ]
            slides.append(
                {
                    "slide": sequence,
                    "title": title_candidate["text"].replace("\n", " ") if title_candidate else "",
                    "title_font_pt": title_candidate["font_median_pt"] if title_candidate else None,
                    "title_box_pct": title_candidate["box_pct"] if title_candidate else None,
                    "text_shape_count": len(text_shapes),
                    "word_count": sum(shape["word_count"] for shape in text_shapes),
                    "body_font_min_pt": min(body_sizes) if body_sizes else None,
                    "body_font_median_pt": round(statistics.median(body_sizes), 2) if body_sizes else None,
                    "body_font_max_pt": max(body_sizes) if body_sizes else None,
                    "picture_count": len(pictures),
                    "largest_picture_area_pct": max((pic["area_pct"] for pic in pictures), default=0),
                    "rotated_text_count": sum(abs(shape["box_pct"]["rotation"]) > 0.2 for shape in text_shapes),
                    "text_shapes": text_shapes,
                    "pictures": pictures,
                }
            )

        repeated_media = {digest: count for digest, count in hash_frequency.items() if count > 1}
        body_medians = [slide["body_font_median_pt"] for slide in slides if slide["body_font_median_pt"]]
        title_sizes = [slide["title_font_pt"] for slide in slides if slide["title_font_pt"]]
        return {
            "path": path,
            "slide_count": len(slides),
            "slide_size_emu": [slide_w, slide_h],
            "slide_size_in": [round(slide_w / 914400, 4), round(slide_h / 914400, 4)],
            "fonts": dict(global_fonts.most_common()),
            "font_sizes_summary_pt": {
                "min": min(global_sizes) if global_sizes else None,
                "median": round(statistics.median(global_sizes), 2) if global_sizes else None,
                "max": max(global_sizes) if global_sizes else None,
            },
            "title_sizes_summary_pt": {
                "min": min(title_sizes) if title_sizes else None,
                "median": round(statistics.median(title_sizes), 2) if title_sizes else None,
                "max": max(title_sizes) if title_sizes else None,
            },
            "body_medians_summary_pt": {
                "min": min(body_medians) if body_medians else None,
                "median": round(statistics.median(body_medians), 2) if body_medians else None,
                "max": max(body_medians) if body_medians else None,
            },
            "text_colors": dict(global_colors.most_common()),
            "repeated_media": repeated_media,
            "slides": slides,
        }


def main() -> None:
    parser = argparse.ArgumentParser(description="Mide una reedición humana de PowerPoint.")
    parser.add_argument("pptx")
    parser.add_argument("output")
    args = parser.parse_args()
    result = inspect(args.pptx)
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
    keys = ("slide_count", "slide_size_in", "fonts", "font_sizes_summary_pt", "title_sizes_summary_pt", "body_medians_summary_pt")
    print(json.dumps({key: result[key] for key in keys}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
