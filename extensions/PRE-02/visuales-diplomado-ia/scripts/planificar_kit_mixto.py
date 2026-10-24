#!/usr/bin/env python3
"""Planifica el enrutamiento E/LT/NATIVA de una presentación con densidades mixtas."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from sugerir_grupos_texto_grande import density_for, normalize, suggest


ROOT = Path(__file__).resolve().parents[1]
REFS = ROOT / "references"


def load(name: str) -> list[dict]:
    return json.loads((REFS / name).read_text(encoding="utf-8"))


def select_kit(slides: list[dict], kits: list[dict], requested: str | None) -> dict:
    if requested:
        for kit in kits:
            if kit["id"] == requested:
                return kit
        raise ValueError(f"Kit desconocido: {requested}")
    corpus = normalize(" ".join(f"{s.get('title', '')} {s.get('text', '')} {s.get('relation', '')}" for s in slides))
    boosts = {
        "KM01": ["direccion", "gobierno", "estrateg", "corporativ", "consultor"],
        "KM02": ["jurid", "ley", "sentencia", "norma", "cumplimiento", "defensa"],
        "KM03": ["financ", "presupuesto", "inversion", "ingreso", "costo", "rendimiento"],
        "KM04": ["tecn", "sistema", "proceso", "arquitectura", "operacion", "innovacion"],
        "KM05": ["municip", "territorio", "infraestructura", "servicio", "cobertura"],
        "KM06": ["academ", "docencia", "investig", "concepto", "diplomado", "evidencia"],
        "KM07": ["riesgo", "auditor", "control", "seguridad", "excepcion", "supervision"],
        "KM08": ["cambio", "equipo", "capacidad", "implementacion", "transformacion", "futuro"],
    }
    scores = {kit["id"]: sum(corpus.count(word) for word in boosts[kit["id"]]) for kit in kits}
    winner = max(kits, key=lambda kit: (scores[kit["id"]], -int(kit["id"][2:])))
    return winner


def detect_relation(slide: dict) -> str:
    given = normalize(str(slide.get("relation", ""))).strip()
    if given:
        return given
    text = normalize(f"{slide.get('title', '')} {slide.get('text', '')}")
    rules = [
        ("juridico", ["jurid", "ley", "norma", "sentencia", "autoridad"]),
        ("finanzas", ["presupuesto", "ingreso", "costo", "inversion", "rendimiento"]),
        ("territorial", ["territorio", "municipio", "region", "cobertura"]),
        ("actores", ["responsable", "actor", "equipo", "institucion"]),
        ("comparacion", ["compar", "versus", "diferencia"]),
        ("proceso", ["paso", "etapa", "proceso", "procedimiento"]),
        ("riesgo", ["riesgo", "control", "excepcion", "detencion"]),
        ("cronologia", ["fecha", "cronologia", "periodo"]),
        ("evidencia", ["evidencia", "prueba", "hallazgo", "auditoria"]),
        ("sistema", ["sistema", "componente", "interdependencia"]),
        ("decision", ["decision", "criterio", "aprobar", "rechazar"]),
    ]
    for relation, words in rules:
        if any(word in text for word in words):
            return relation
    return "sintesis"


SHORT_PREFERENCES = {
    "juridico": ["E18", "E28", "E49", "E43", "E11"],
    "finanzas": ["E03", "E13", "E16", "E38", "E47"],
    "territorial": ["E06", "E09", "E19", "E37", "E39"],
    "actores": ["E27", "E30", "E39", "E43", "E48"],
    "proceso": ["E05", "E23", "E26", "E34", "E04"],
    "comparacion": ["E11", "E15", "E43", "E45"],
    "sistema": ["E01", "E27", "E39", "E48"],
    "riesgo": ["E12", "E25", "E32", "E41", "E46"],
    "evidencia": ["E14", "E16", "E18", "E28", "E49"],
    "decision": ["E11", "E12", "E15", "E43", "E45"],
    "cronologia": ["E07", "E34", "E47", "E50"],
    "sintesis": ["E10", "E27", "E49", "E50"],
}

COMPOSITIONS = {
    "juridico": ["C20", "C36", "C43"],
    "finanzas": ["C16", "C30", "C39"],
    "territorial": ["C21", "C33", "C37"],
    "actores": ["C22", "C24", "C35"],
    "proceso": ["C08", "C10", "C12"],
    "comparacion": ["C15", "C17", "C29"],
    "sistema": ["C20", "C22", "C24"],
    "riesgo": ["C42", "C43", "C46"],
    "evidencia": ["C36", "C38", "C40"],
    "decision": ["C05", "C41", "C45"],
    "cronologia": ["C09", "C14", "C47"],
    "sintesis": ["C07", "C49", "C50"],
}


def route_slide(slide: dict, kit: dict, index: int) -> dict:
    text = str(slide.get("text", ""))
    words = re.findall(r"\b[\wÁÉÍÓÚÜÑáéíóúüñ'-]+\b", text)
    density = density_for(len(words))
    relation = detect_relation(slide)

    if slide.get("native_data"):
        return {"library": "NATIVA", "family_candidates": [], "composition_candidates": [], "reason": "tabla o gráfica editable"}

    paragraphs = [part for part in re.split(r"\n\s*\n", text) if part.strip()]
    bullets = sum(bool(re.match(r"^(?:[-*•·]|\d+[.)])\s+", line.strip())) for line in text.splitlines())
    use_long = density in {"D04", "D05", "D06"} or (density == "D03" and (len(paragraphs) > 1 or bullets >= 3))

    if use_long:
        ranked = suggest(text, 20)["suggestions"]
        allowed = set(kit["long_families"])
        candidates = [item["id"] for item in ranked if item["id"] in allowed][:3]
        candidates += [item for item in kit["long_families"] if item not in candidates][: 3 - len(candidates)]
        return {"library": "LT", "family_candidates": candidates, "composition_candidates": [], "reason": "párrafos o alta densidad"}

    preferred = SHORT_PREFERENCES.get(relation, SHORT_PREFERENCES["sintesis"])
    allowed = kit["short_families"]
    candidates = [item for item in preferred if item in allowed]
    candidates += [item for item in allowed if item not in candidates]
    compositions = COMPOSITIONS.get(relation, COMPOSITIONS["sintesis"])
    shift = index % len(compositions)
    compositions = compositions[shift:] + compositions[:shift]
    return {"library": "E", "family_candidates": candidates[:3], "composition_candidates": compositions, "reason": "bloques breves o medios"}


def plan(slides: list[dict], requested_kit: str | None) -> dict:
    kits = load("catalogo-8-kits-mixtos-profesionales.json")
    kit = select_kit(slides, kits, requested_kit)
    rows = []
    for index, slide in enumerate(slides):
        text = str(slide.get("text", ""))
        route = route_slide(slide, kit, index)
        rows.append({
            "slide": slide.get("slide", index + 1),
            "title": slide.get("title", ""),
            "words": len(re.findall(r"\b[\wÁÉÍÓÚÜÑáéíóúüñ'-]+\b", text)),
            "density": density_for(len(re.findall(r"\b[\wÁÉÍÓÚÜÑáéíóúüñ'-]+\b", text))),
            "relation": detect_relation(slide),
            "finish": kit["primary_finish"],
            **route,
        })
    return {"kit": kit, "slides": rows}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="JSON con una lista de diapositivas")
    parser.add_argument("--kit", help="Kit KM01-KM08; si se omite, se sugiere automáticamente")
    parser.add_argument("--output", type=Path, help="Guarda el plan JSON")
    args = parser.parse_args()
    slides = json.loads(args.input.read_text(encoding="utf-8"))
    if not isinstance(slides, list) or not all(isinstance(item, dict) for item in slides):
        raise ValueError("El archivo debe contener una lista JSON de diapositivas")
    result = plan(slides, args.kit)
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
        print(f"Plan guardado en {args.output}")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    sys.exit(main())
