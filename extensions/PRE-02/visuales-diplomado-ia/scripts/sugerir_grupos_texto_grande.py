#!/usr/bin/env python3
"""Sugiere familias LT01-LT20 para una sección de texto destinada a PowerPoint."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "references" / "catalogo-20-familias-texto-grande.json"


def normalize(value: str) -> str:
    table = str.maketrans("áéíóúüñÁÉÍÓÚÜÑ", "aeiouunAEIOUUN")
    return value.translate(table).lower()


def density_for(word_count: int) -> str:
    if word_count <= 35:
        return "D01"
    if word_count <= 70:
        return "D02"
    if word_count <= 120:
        return "D03"
    if word_count <= 180:
        return "D04"
    if word_count <= 260:
        return "D05"
    return "D06"


def structure_tags(text: str) -> set[str]:
    tags: set[str] = set()
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    bullet_count = sum(bool(re.match(r"^(?:[-*•·]|\d+[.)])\s+", line)) for line in lines)
    paragraphs = [part for part in re.split(r"\n\s*\n", text) if part.strip()]
    norm = normalize(text)

    if bullet_count >= 3:
        tags.add("lista")
    if len(paragraphs) <= 2 and bullet_count < 3:
        tags.update({"prosa_continua", "un_tema"})
    if len(paragraphs) == 2:
        tags.add("dos_partes")
    if len(paragraphs) == 3:
        tags.add("tres_partes")
    if len(paragraphs) >= 4 or bullet_count >= 4:
        tags.add("cuatro_partes")

    tag_keywords = {
        "comparacion": ["compar", "versus", "diferencia", "ventaja", "desventaja"],
        "secuencia": ["paso", "etapa", "fase", "primero", "despues", "finalmente"],
        "proceso": ["proceso", "procedimiento", "tramite", "implementar", "ejecutar"],
        "cronologia": ["fecha", "ano", "historia", "cronologia", "periodo"],
        "juridico": ["articulo", "ley", "jurisprudencia", "autoridad", "resolucion"],
        "finanzas": ["presupuesto", "ingreso", "costo", "inversion", "rendimiento"],
        "datos": ["porcentaje", "indicador", "medicion", "resultado", "%", "$"],
        "riesgos": ["riesgo", "control", "alerta", "amenaza", "mitigacion"],
        "territorial": ["territorio", "municipio", "region", "zona", "cobertura"],
        "actores": ["responsable", "actor", "institucion", "participante", "competencia"],
        "sistema": ["sistema", "integral", "interdependencia", "entorno", "factor"],
        "sintesis": ["resumen", "conclusion", "hallazgo", "recomendacion", "cierre"],
        "transformacion": ["problema", "solucion", "actual", "futuro", "cambio"],
        "monitoreo": ["seguimiento", "supervision", "cumplimiento", "control"],
        "marco": ["principio", "pilar", "criterio", "marco", "fundamento"],
        "tecnico": ["tecnico", "arquitectura", "especificacion", "configuracion"],
    }
    for tag, needles in tag_keywords.items():
        if any(needle in norm for needle in needles):
            tags.add(tag)
    return tags


def suggest(text: str, top: int) -> dict:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    words = re.findall(r"\b[\wÁÉÍÓÚÜÑáéíóúüñ'-]+\b", text)
    density = density_for(len(words))
    tags = structure_tags(text)
    norm = normalize(text)
    ranked = []
    preferred_by_tag = {
        "juridico": {"LT04": 7, "LT05": 3, "LT14": 2},
        "comparacion": {"LT06": 7, "LT12": 4},
        "proceso": {"LT19": 6, "LT07": 4, "LT08": 3},
        "secuencia": {"LT19": 5, "LT08": 5, "LT09": 2},
        "cronologia": {"LT09": 8},
        "monitoreo": {"LT10": 6},
        "tecnico": {"LT11": 8},
        "riesgos": {"LT13": 8},
        "marco": {"LT14": 6},
        "territorial": {"LT15": 8},
        "actores": {"LT16": 7},
        "sistema": {"LT17": 7},
        "finanzas": {"LT18": 9},
        "sintesis": {"LT20": 7, "LT01": 3},
        "transformacion": {"LT12": 6},
    }

    for item in catalog:
        score = 0.0
        reasons = []
        if density in item["density_modes"]:
            score += 8
            reasons.append(f"compatible con {density}")
        elif density == "D03" and "D04" in item["density_modes"]:
            score += 3

        matched_signals = [signal for signal in item["signals"] if normalize(signal) in norm]
        if matched_signals:
            score += min(8, 2 * len(matched_signals))
            reasons.append("señales: " + ", ".join(matched_signals[:4]))

        matched_tags = sorted(tags.intersection(item["structure_tags"]))
        if matched_tags:
            score += 3 * len(matched_tags)
            reasons.append("estructura: " + ", ".join(matched_tags[:3]))

        semantic_boost = sum(
            preferences.get(item["id"], 0)
            for tag, preferences in preferred_by_tag.items()
            if tag in tags
        )
        if semantic_boost:
            score += semantic_boost
            reasons.append("ajuste semántico principal")

        if not reasons and item["id"] in {"LT01", "LT20"}:
            score += 1
            reasons.append("opción editorial general")

        ranked.append((score, item, reasons))

    ranked.sort(key=lambda row: (-row[0], row[1]["id"]))
    selections = []
    for score, item, reasons in ranked[:top]:
        selections.append(
            {
                "id": item["id"],
                "name": item["name"],
                "score": round(score, 1),
                "reason": "; ".join(reasons) or "ajuste visual general",
                "purpose": item["purpose"],
                "blocks": item["blocks"],
                "geometry": item["geometry"],
            }
        )
    return {
        "words": len(words),
        "density": density,
        "detected_structure": sorted(tags),
        "suggestions": selections,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--text", help="Texto que se analizará.")
    source.add_argument("--file", type=Path, help="Archivo UTF-8 con el texto.")
    parser.add_argument("--top", type=int, default=3, help="Número de sugerencias (1-20).")
    parser.add_argument("--json", action="store_true", help="Devuelve JSON en lugar de texto.")
    args = parser.parse_args()

    if not 1 <= args.top <= 20:
        parser.error("--top debe estar entre 1 y 20")
    text = args.text if args.text is not None else args.file.read_text(encoding="utf-8")
    result = suggest(text, args.top)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    print(f"Palabras: {result['words']} | Densidad: {result['density']}")
    if result["detected_structure"]:
        print("Estructura detectada: " + ", ".join(result["detected_structure"]))
    print("Sugerencias:")
    for index, item in enumerate(result["suggestions"], 1):
        print(f"{index}. {item['id']} — {item['name']} ({item['score']} puntos)")
        print(f"   Motivo: {item['reason']}")
        print(f"   Uso: {item['purpose']}")
        print(f"   Geometría: {item['geometry']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
