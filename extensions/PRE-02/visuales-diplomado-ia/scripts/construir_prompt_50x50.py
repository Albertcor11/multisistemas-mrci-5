#!/usr/bin/env python3
"""Construye prompts de la biblioteca escénica 50x50 sin generar imágenes."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
REFERENCES = SKILL_ROOT / "references"
STYLES_PATH = REFERENCES / "catalogo-estilos-50.json"
FAMILIES_PATH = REFERENCES / "catalogo-familias-escenicas-50.json"
LAYOUTS_PATH = REFERENCES / "catalogo-composiciones-50.json"
DENSITIES_PATH = REFERENCES / "catalogo-densidades-texto-6.json"


def load_catalog(path: Path) -> list[dict[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"El catálogo {path.name} no es una lista JSON.")
    return data


def by_id(items: list[dict[str, str]], item_id: str, label: str) -> dict[str, str]:
    for item in items:
        if item.get("id") == item_id:
            return item
    raise ValueError(f"{label} desconocido: {item_id}")


def validate_catalogs(
    families: list[dict[str, str]],
    layouts: list[dict[str, str]],
    styles: list[dict[str, str]],
) -> None:
    if len(families) != 50:
        raise ValueError(f"Se esperaban 50 familias escénicas y existen {len(families)}.")
    if len(styles) != 50:
        raise ValueError(f"Se esperaban 50 estilos y existen {len(styles)}.")
    if len(layouts) != 50:
        raise ValueError(f"Se esperaban 50 composiciones y existen {len(layouts)}.")
    family_ids = [item.get("id") for item in families]
    layout_ids = [item.get("id") for item in layouts]
    style_ids = [item.get("id") for item in styles]
    if len(set(family_ids)) != 50 or any(not value for value in family_ids):
        raise ValueError("Los identificadores de familia escénica deben ser 50 y únicos.")
    if len(set(layout_ids)) != 50 or any(not value for value in layout_ids):
        raise ValueError("Los identificadores de composición deben ser 50 y únicos.")
    if len(set(style_ids)) != 50 or any(not value for value in style_ids):
        raise ValueError("Los identificadores de acabado deben ser 50 y únicos.")
    combinations = {
        f"{family_id}-{layout_id}"
        for family_id in family_ids
        for layout_id in layout_ids
    }
    if len(combinations) != 2500:
        raise ValueError("La matriz no produce 2,500 combinaciones únicas.")


def build_prompt(
    family: dict[str, str],
    style: dict[str, str],
    layout: dict[str, str],
    subject: str,
    variant: str,
    density: dict[str, str] | None = None,
) -> str:
    variant_line = f"\nVariation note: {variant}" if variant else ""
    density_line = ""
    if density:
        density_line = (
            f"\nText density mode: {density['id']} {density['name']}; "
            f"{density['initial_range']}; {density['blocks']}. "
            f"Carrier geometry: {density['geometry']}. "
            f"Reserve {density['carrier_share']} for clean text carriers and only "
            f"{density['scene_share']} for scene and atmosphere. {density['guidance']}."
        )
    return f"""Use case: productivity-visual
Asset type: structural image for a professional 16:9 PowerPoint slide
Combination ID: {family['id']}-{layout['id']} / finish {style['id']}
Primary request: Create a complete slide-ready carrier scene about {subject}. This is not a background. The subjects, objects and blank panels must visibly organize the message and be useful after editable PowerPoint text is placed over them.
Scene/backdrop: {style['background']}.
Subject: express {subject} through the family {family['name']}; {family['scene']}.
Style/medium: {style['name']}; {style['medium']}.
Composition/framing: adapt {layout['name']} for {layout['use']}; {layout['composition']}. The scene must occupy the slide as a coherent infographic illustration, not sit behind unrelated copy.
Semantic carriers: {family['carriers']}.
Editable overlay zones: {layout['zones']}. Render those zones as actual physical panels, cards, platforms, steps, circles, frames or object faces belonging to the scene. Keep every zone blank, smooth, high-contrast and large enough for native PowerPoint text boxes.{density_line}
Variation logic: {family['variation_logic']}.
Lighting/mood: {style['lighting']}; authoritative, modern, precise and professional.
Color palette: {style['palette']}.
Materials/textures: {style['materials']}.
Visual motifs: {style['motifs']}.{variant_line}
Constraints: landscape 16:9, high resolution, strong hierarchy, clean edges and readable silhouettes. The carrier objects and their blank text surfaces must be the dominant content of the frame. Use negative space only as breathing room around the constructed scene. The visual must remain usable after editable text is placed over every reserved zone.
NO TEXT IN IMAGE: no words, letters, numbers, formulas, dates, labels, headings, captions, placeholder text, logos, watermarks or typographic marks anywhere.
Avoid: {style['avoid']}; {family['avoid']}; diffuse decorative background, empty scenery, unrelated copy space, generic robots, humanoid AI figures, emojis, mascots, stock-photo poses, childish style, neon, cyberpunk, decorative UI cards, buttons, dashboards, fake charts and rainbow gradients. If the selected narrative composition normally suggests another metaphor, preserve the chosen family and adapt only its information arrangement."""


def write_matrix(
    path: Path,
    families: list[dict[str, str]],
    layouts: list[dict[str, str]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "combination_id",
                "family_id",
                "family",
                "composition_id",
                "composition",
                "use",
                "default_finish",
            ]
        )
        for family in families:
            for layout in layouts:
                writer.writerow(
                    [
                        f"{family['id']}-{layout['id']}",
                        family["id"],
                        family["name"],
                        layout["id"],
                        layout["name"],
                        layout["use"],
                        family["default_style"],
                    ]
                )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Selecciona una combinación de la biblioteca visual 50x50 y construye su prompt."
    )
    parser.add_argument("--family", help="Familia escénica E01-E50")
    parser.add_argument(
        "--style",
        help="Acabado visual opcional S01-S50; si se omite, usa el sugerido por la familia",
    )
    parser.add_argument("--composition", help="Identificador C01-C50")
    parser.add_argument(
        "--density",
        help="Modo opcional de densidad textual D01-D06",
    )
    parser.add_argument("--subject", help="Tema o mensaje que debe representar la imagen")
    parser.add_argument("--variant", default="", help="Matiz opcional para diferenciar la imagen")
    parser.add_argument("--output", type=Path, help="Archivo opcional donde guardar el prompt")
    parser.add_argument("--matrix", type=Path, help="Genera un CSV con las 2,500 combinaciones")
    parser.add_argument("--list-styles", action="store_true")
    parser.add_argument("--list-families", action="store_true")
    parser.add_argument("--list-compositions", action="store_true")
    parser.add_argument("--list-densities", action="store_true")
    parser.add_argument("--validate", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        families = load_catalog(FAMILIES_PATH)
        layouts = load_catalog(LAYOUTS_PATH)
        styles = load_catalog(STYLES_PATH)
        densities = load_catalog(DENSITIES_PATH)
        validate_catalogs(families, layouts, styles)
        if len(densities) != 6 or len({item.get("id") for item in densities}) != 6:
            raise ValueError("Los modos de densidad deben ser seis y tener identificadores únicos.")

        if args.validate:
            print(
                "Biblioteca válida: 50 familias escénicas x 50 composiciones "
                "= 2,500 escenas portadoras; 50 acabados y 6 modos de densidad disponibles."
            )
        if args.list_families:
            for item in families:
                print(f"{item['id']}\t{item['name']}\t{item['best_for']}")
        if args.list_styles:
            for item in styles:
                print(f"{item['id']}\t{item['name']}")
        if args.list_compositions:
            for item in layouts:
                print(f"{item['id']}\t{item['name']}\t{item['use']}")
        if args.list_densities:
            for item in densities:
                print(f"{item['id']}\t{item['name']}\t{item['initial_range']}")
        if args.matrix:
            write_matrix(args.matrix, families, layouts)
            print(f"Matriz guardada en {args.matrix}")

        requested_prompt = any(
            [args.family, args.style, args.composition, args.subject, args.density]
        )
        if requested_prompt:
            if not all([args.family, args.composition, args.subject]):
                raise ValueError(
                    "Para construir un prompt se requieren --family, --composition y --subject."
                )
            family = by_id(families, args.family, "Familia escénica")
            selected_style = args.style or family["default_style"]
            style = by_id(styles, selected_style, "Acabado")
            layout = by_id(layouts, args.composition, "Composición")
            density = by_id(densities, args.density, "Densidad") if args.density else None
            prompt = build_prompt(
                family,
                style,
                layout,
                args.subject,
                args.variant,
                density,
            )
            if args.output:
                args.output.parent.mkdir(parents=True, exist_ok=True)
                args.output.write_text(prompt + "\n", encoding="utf-8")
                print(f"Prompt guardado en {args.output}")
            else:
                print(prompt)

        if not any(
            [
                args.validate,
                args.list_families,
                args.list_styles,
                args.list_compositions,
                args.list_densities,
                args.matrix,
                requested_prompt,
            ]
        ):
            print("Usa --help para ver las opciones.", file=sys.stderr)
            return 2
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
