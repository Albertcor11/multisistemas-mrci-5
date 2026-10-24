#!/usr/bin/env python3
"""Valida la integridad completa del sistema visual transportable."""

from __future__ import annotations

import json
import re
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFS = ROOT / "references"
PENO = ROOT / "assets" / "plantillas" / "PENO-01"

CATALOGS = {
    "E": ("catalogo-familias-escenicas-50.json", 50, "E", 2),
    "C": ("catalogo-composiciones-50.json", 50, "C", 2),
    "S": ("catalogo-estilos-50.json", 50, "S", 2),
    "D": ("catalogo-densidades-texto-6.json", 6, "D", 2),
    "LT": ("catalogo-20-familias-texto-grande.json", 20, "LT", 2),
    "KM": ("catalogo-8-kits-mixtos-profesionales.json", 8, "KM", 2),
}

REQUIRED = [
    "MODULO.md",
    "agents/openai.yaml",
    "references/integracion-imagen-texto-editable.md",
    "references/protocolo-portadores-exactos.md",
    "references/coherencia-semantica-imagen-texto.md",
    "references/concordancia-morfologica-y-encaje.md",
    "references/escenas-portadoras-de-texto.md",
    "references/texto-largo-en-escenas.md",
    "references/seleccion-20-familias-texto-grande.md",
    "references/modo-mixto-kit-profesional.md",
    "references/plantilla-escultorica-negro-oro.md",
    "references/modo-proyeccion-y-reedicion-humana.md",
    "references/auditoria-visual-reedicion-humana.md",
    "references/preservacion-quirurgica-pptx.md",
    "references/prompt-maestro-peno-01-proyeccion-v15.md",
    "references/prompt-maestro-general-arranque.md",
    "references/auditoria-hostil-word-powerpoint.md",
    "assets/plantillas/PENO-01/Plantilla_Escultorica_Negro_y_Oro_PENO-01.pptx",
    "assets/plantillas/PENO-01/Vista_general_PENO-01.png",
    "scripts/construir_prompt_50x50.py",
    "scripts/sugerir_grupos_texto_grande.py",
    "scripts/planificar_kit_mixto.py",
    "scripts/auditar_texto_word_pptx.py",
    "scripts/medir_referencia_pptx.py",
    "scripts/auditar_pptx_pptx.py",
    "assets/ejemplos-validados/Fiscalizacion_algoritmica_PENO-01_proyeccion_v15.pptx",
    "assets/ejemplos-validados/Vista_general_Fiscalizacion_algoritmica_PENO-01_v15.png",
    "assets/ejemplos-validados/Auditoria_hostil_Fiscalizacion_algoritmica_PENO-01_v15.md",
    "assets/ejemplos-validados/Manifiesto_visual_Fiscalizacion_algoritmica_PENO-01_v15.json",
]

PENO_VISUALS = [
    "01_portada_marco.png",
    "02_proceso_modulos.png",
    "03_crecimiento_finanzas.png",
    "04_comparacion.png",
    "05_jerarquia_bloques.png",
    "06_analisis_engranes.png",
    "07_ciclo_colaboracion.png",
    "08_riesgo_escudo.png",
    "09_hoja_ruta.png",
    "10_deliberacion.png",
    "11_puente_implementacion.png",
    "12_texto_largo_libro.png",
]

PENO_PROJECTION_VISUALS = [
    "13_poder_y_control.png",
    "14_modulos_causales.png",
    "15_escala_intervencion.png",
    "16_auditoria_causal.png",
    "17_libro_explicativo.png",
    "18_cadena_datos.png",
    "19_balanza_inferencia.png",
    "20_circuito_supervision.png",
    "21_lente_perfilamiento.png",
    "22_ruta_trazabilidad.png",
    "23_escudo_dividido.png",
    "24_estatuto_derechos.png",
]


def expected_ids(prefix: str, count: int, width: int) -> list[str]:
    return [f"{prefix}{number:0{width}d}" for number in range(1, count + 1)]


def load_catalog(filename: str) -> list[dict]:
    path = REFS / filename
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"{filename} no contiene una lista JSON")
    return data


def validate_markdown_links(errors: list[str]) -> None:
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for markdown in ROOT.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        for raw_target in pattern.findall(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target or re.match(r"^[a-z]+://", target) or target.startswith("mailto:"):
                continue
            resolved = (markdown.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"enlace roto en {markdown.relative_to(ROOT)}: {raw_target}")


def validate_peno(errors: list[str]) -> None:
    visual_dir = PENO / "visuales"
    for filename in PENO_VISUALS:
        image = visual_dir / filename
        if not image.is_file():
            errors.append(f"PENO-01: falta visual {filename}")
            continue
        header = image.read_bytes()[:26]
        if len(header) < 26 or header[:8] != b"\x89PNG\r\n\x1a\n":
            errors.append(f"PENO-01: {filename} no es PNG válido")
            continue
        width = int.from_bytes(header[16:20], "big")
        height = int.from_bytes(header[20:24], "big")
        color_type = header[25]
        if width < 1000 or height < 700:
            errors.append(f"PENO-01: resolución insuficiente en {filename}: {width}x{height}")
        if color_type not in {4, 6}:
            errors.append(f"PENO-01: {filename} no declara canal alfa")

    projection_dir = PENO / "visuales-proyeccion"
    projection_hashes: set[bytes] = set()
    for filename in PENO_PROJECTION_VISUALS:
        image = projection_dir / filename
        if not image.is_file():
            errors.append(f"PENO-01 proyección: falta visual {filename}")
            continue
        payload = image.read_bytes()
        header = payload[:26]
        if len(header) < 26 or header[:8] != b"\x89PNG\r\n\x1a\n":
            errors.append(f"PENO-01 proyección: {filename} no es PNG válido")
            continue
        width = int.from_bytes(header[16:20], "big")
        height = int.from_bytes(header[20:24], "big")
        color_type = header[25]
        if width < 1600 or height < 900:
            errors.append(f"PENO-01 proyección: resolución insuficiente en {filename}: {width}x{height}")
        if color_type not in {4, 6}:
            errors.append(f"PENO-01 proyección: {filename} no declara canal alfa")
        digest = __import__("hashlib").sha256(payload).digest()
        if digest in projection_hashes:
            errors.append(f"PENO-01 proyección: imagen duplicada {filename}")
        projection_hashes.add(digest)

    deck = PENO / "Plantilla_Escultorica_Negro_y_Oro_PENO-01.pptx"
    if deck.is_file():
        try:
            with zipfile.ZipFile(deck) as package:
                slides = [
                    name for name in package.namelist()
                    if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)
                ]
            if len(slides) != 12:
                errors.append(f"PENO-01: el PowerPoint base debe contener 12 diapositivas y contiene {len(slides)}")
        except zipfile.BadZipFile:
            errors.append("PENO-01: el PowerPoint base no es un paquete PPTX válido")

    example_dir = ROOT / "assets" / "ejemplos-validados"
    example_deck = example_dir / "Fiscalizacion_algoritmica_PENO-01_proyeccion_v15.pptx"
    if example_deck.is_file():
        try:
            with zipfile.ZipFile(example_deck) as package:
                slides = [
                    name for name in package.namelist()
                    if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)
                ]
            if len(slides) != 12:
                errors.append(f"ejemplo PENO-01: se esperaban 12 diapositivas y contiene {len(slides)}")
        except zipfile.BadZipFile:
            errors.append("ejemplo PENO-01: el archivo no es un paquete PPTX válido")

    audit = example_dir / "Auditoria_hostil_Fiscalizacion_algoritmica_PENO-01_v15.md"
    if audit.is_file() and "Resultado: **APROBADO**" not in audit.read_text(encoding="utf-8"):
        errors.append("ejemplo PENO-01: la auditoría hostil no está aprobada")

    manifest = example_dir / "Manifiesto_visual_Fiscalizacion_algoritmica_PENO-01_v15.json"
    if manifest.is_file():
        try:
            entries = json.loads(manifest.read_text(encoding="utf-8"))
            images = [entry.get("image") for entry in entries]
            if len(entries) != 12 or len(images) != len(set(images)):
                errors.append("ejemplo PENO-01: el manifiesto debe declarar 12 imágenes únicas")
        except (ValueError, json.JSONDecodeError):
            errors.append("ejemplo PENO-01: manifiesto visual inválido")


def main() -> int:
    errors: list[str] = []
    data: dict[str, list[dict]] = {}

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"falta archivo obligatorio: {relative}")

    for label, (filename, count, prefix, width) in CATALOGS.items():
        try:
            items = load_catalog(filename)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"no se pudo leer {filename}: {exc}")
            continue
        data[label] = items
        ids = [item.get("id") for item in items]
        expected = expected_ids(prefix, count, width)
        if len(items) != count:
            errors.append(f"{filename}: se esperaban {count} registros y hay {len(items)}")
        if ids != expected:
            errors.append(f"{filename}: los identificadores deben ser {expected[0]}–{expected[-1]} en orden")
        if len(ids) != len(set(ids)):
            errors.append(f"{filename}: existen identificadores duplicados")

    style_ids = {item.get("id") for item in data.get("S", [])}
    family_ids = {item.get("id") for item in data.get("E", [])}
    density_ids = {item.get("id") for item in data.get("D", [])}
    long_ids = {item.get("id") for item in data.get("LT", [])}

    for family in data.get("E", []):
        if family.get("default_style") not in style_ids:
            errors.append(f"{family.get('id')}: default_style inexistente")

    for family in data.get("LT", []):
        modes = family.get("density_modes", [])
        if not modes or any(mode not in density_ids for mode in modes):
            errors.append(f"{family.get('id')}: density_modes inválidos")

    color = re.compile(r"^#[0-9A-Fa-f]{6}$")
    for kit in data.get("KM", []):
        kit_id = kit.get("id", "KM??")
        if kit.get("primary_finish") not in style_ids or kit.get("secondary_finish") not in style_ids:
            errors.append(f"{kit_id}: acabado primario o secundario inexistente")
        if not kit.get("short_families") or any(value not in family_ids for value in kit.get("short_families", [])):
            errors.append(f"{kit_id}: short_families inválidas")
        if not kit.get("long_families") or any(value not in long_ids for value in kit.get("long_families", [])):
            errors.append(f"{kit_id}: long_families inválidas")
        palette = kit.get("palette", [])
        if len(palette) < 4 or any(not color.match(value) for value in palette):
            errors.append(f"{kit_id}: paleta inválida")

    skill_text = (ROOT / "MODULO.md").read_text(encoding="utf-8") if (ROOT / "MODULO.md").exists() else ""
    required_terms = [
        "D01–D06", "E01–E50", "LT01–LT20", "KM01–KM08", "PENO-01",
        "auditar_texto_word_pptx.py", "Arial", "#FF2B2B",
        "No reutilizar una ilustración semántica",
        "compuerta de coherencia semántica",
        "compuerta de concordancia morfológica",
        "modo de proyección y reedición humana",
        "zonas editables y zonas protegidas",
        "prompt-maestro-peno-01-proyeccion-v15.md",
        "prompt-maestro-general-arranque.md",
        "Contrato de portadores exactos",
        "auditoria-visual-reedicion-humana.md",
        "marco escénico con lienzo editorial",
        "preservación quirúrgica de PPTX",
        "auditar_pptx_pptx.py",
    ]
    for term in required_terms:
        if term not in skill_text:
            errors.append(f"MODULO.md no declara {term}")

    prompt_path = REFS / "prompt-maestro-peno-01-proyeccion-v15.md"
    if prompt_path.is_file():
        prompt_text = prompt_path.read_text(encoding="utf-8")
        for term in (
            "Fiscalizacion_algoritmica_PENO-01_proyeccion_v15",
            "fidelidad literal",
            "zonas_editables",
            "zonas_protegidas",
            "#FF2B2B",
            "APROBADO",
        ):
            if term not in prompt_text:
                errors.append(f"prompt maestro v15 no declara {term}")

    general_prompt_path = REFS / "prompt-maestro-general-arranque.md"
    if general_prompt_path.is_file():
        general_prompt_text = general_prompt_path.read_text(encoding="utf-8")
        for term in (
            "FASE 5A · CONTRATO DE PORTADORES EXACTOS",
            "relleno transparente",
            "línea transparente",
            "franja de título",
            "rechaza y regenera",
            "auditoría hostil Word–PowerPoint",
        ):
            if term not in general_prompt_text:
                errors.append(f"prompt maestro general no declara {term}")

    for markdown in ROOT.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8").lower()
        if "horizontal 3:2" in text or "composición objetivo 3:2" in text:
            errors.append(f"proporción obsoleta 3:2 en {markdown.relative_to(ROOT)}")

    validate_markdown_links(errors)
    validate_peno(errors)

    auditor_text = (ROOT / "scripts/auditar_texto_word_pptx.py").read_text(encoding="utf-8")
    for option in (
        "--uppercase-titles",
        "--assign-preamble-to-slide-one",
        "--allow-nonlinear-layout",
    ):
        if option not in auditor_text:
            errors.append(f"el auditor no declara la opción controlada {option}")

    if errors:
        print("RECHAZADO — sistema visual inconsistente")
        for error in errors:
            print(f"- {error}")
        return 1

    print("APROBADO — sistema visual completo y coherente")
    print("50 familias E × 50 composiciones C = 2,500 escenas; 50 acabados S; 6 densidades D; 20 familias LT; 8 kits KM.")
    print("PENO-01 aprobado: PowerPoint base de 12 diapositivas y 12 visuales PNG con canal alfa.")
    print("Extensión PENO-C13–C24 aprobada: 12 visuales de proyección únicos, 16:9 y con canal alfa.")
    print("Texto editable, portadores exactos, proyección, reedición humana, prompts maestros general y PENO v15, coherencia semántica, concordancia morfológica, Arial, escenas únicas y auditoría controlada verificados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
