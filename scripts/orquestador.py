#!/usr/bin/env python3
"""Motor Orquestador Unificado para Multisistemas MRCI 5.0.

Gestiona el catálogo de mini-skills, el enrutamiento inteligente por encargo,
la activación selectiva con caché persistente verificada por SHA-256, la creación
modular de nuevas mini-skills en `extensions/` y la auditoría de anonimato y
control léxico sobre archivos entregables (.md, .txt, .docx, .pptx).
"""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile
import unicodedata
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CATALOGO_PATH = ROOT / 'references/catalogo-orquestador.json'
INVENTARIO_PATH = ROOT / 'references/inventario.json'

# Expresiones de veto y control del perfil autoral JAPR (LEXICO_CONTROL_IA)
LEXICO_VETO = [
    ('LEX-001', 'claro, aquí tienes', 'Apertura de asistente sin función autoral'),
    ('LEX-002', 'por supuesto, aquí tienes', 'Apertura de asistente sin función autoral'),
    ('LEX-003', 'a continuación te presento', 'Anuncio de estructura en lugar de contenido'),
    ('LEX-004', 'como modelo de inteligencia artificial', 'Metadiscurso tecnológico'),
    ('LEX-005', 'como inteligencia artificial', 'Metadiscurso tecnológico'),
    ('LEX-006', 'espero que esto te ayude', 'Cierre complaciente de asistente'),
    ('LEX-007', 'adentrémonos en', 'Fórmula estereotipada'),
    ('LEX-008', 'exploremos juntos', 'Fórmula estereotipada'),
    ('LEX-009', 'sumérgete en', 'Fórmula promocional estereotipada'),
    ('LEX-010', 'en un mundo cada vez más', 'Apertura genérica'),
    ('LEX-011', 'hoy más que nunca', 'Intensificación vacía salvo dato demostrable'),
    ('LEX-012', 'marca un antes y un después', 'Grandilocuencia sin medición'),
    ('LEX-013', 'desempeña un papel crucial', 'Fórmula frecuente sin precisión causal'),
    ('LEX-014', 'solución robusta', 'Valoración genérica sin atributo verificable'),
    ('LEX-015', 'panorama integral', 'Fórmula genérica sin delimitación'),
    ('LEX-031', 'sistema mrci', 'Referencia al sistema interno de elaboración'),
    ('LEX-032', 'tes-01', 'Código interno de producto editorial MRCI'),
    ('LEX-033', 'prueba de espejo', 'Terminología de control metodológico interno'),
    ('LEX-034', 'el encargo que dio origen a este documento', 'Referencia al proceso de elaboración'),
    ('LEX-035', 'aparato de citas apa mrci méxico', 'Nombre de herramienta interna de citación'),
    ('LEX-036', 'perfil autoral japr', 'Nombre de motor interno de estilo'),
    ('LEX-037', 'estructura provisional del sistema mrci', 'Referencia al sistema interno de producción'),
    ('LEX-040', 'restricciones de acceso de la herramienta empleada', 'Referencia a la herramienta de elaboración'),
]

LEXICO_CONTROL = [
    ('LEX-038', 'meta interna de', 'Declarar cifra y justificación sin nombrar origen interno'),
    ('LEX-039', 'excepción de saturación material', 'Reformular como limitación metodológica sin nombrar protocolo interno'),
    ('LEX-041', 'registro de correcciones del estudiante', 'Verificar que sea anexo opcional y no cuerpo de investigación'),
    ('LEX-042', 'jurisprudencia consolidada', 'Verificar bajo Ley de Amparo si es jurisprudencia obligatoria o tesis aislada'),
]

MARCAS_INTERNAS_BASE = [
    r'\bMRCI(?:\s+5\.0)?\b',
    r'\bMultisistemas?\s+MRCI\b',
    r'\bANJU\b',
    r'\bINJU\b',
    r'\bESFI\b',
    r'\bOPSY\b',
    r'\bARQE\b',
    r'\bPENO-01\b',
    r'\bDALILA\b',
    r'\bSentencias\s+SOL\b',
    r'\bJAPR\b',
]


def nfc(texto: str) -> str:
    return unicodedata.normalize('NFC', texto)


def cargar_catalogo() -> dict:
    return json.loads(CATALOGO_PATH.read_text(encoding='utf-8'))


def cargar_inventario() -> dict:
    return json.loads(INVENTARIO_PATH.read_text(encoding='utf-8'))


def reconstruir_zip_corpus(inv: dict) -> bytes:
    """Reconstruye y verifica el ZIP del corpus en memoria desde assets/corpus/parte-*.bin."""
    bloques = []
    complete_hash = hashlib.sha256()
    for part in inv.get('corpus_parts', []):
        relative = PurePosixPath(part['path'])
        if relative.is_absolute() or '..' in relative.parts:
            raise ValueError(f'Ruta de corpus no segura: {part["path"]}')
        data = (ROOT / relative).read_bytes()
        if len(data) != part['bytes'] or hashlib.sha256(data).hexdigest() != part['sha256']:
            raise ValueError(f'Parte de corpus alterada: {part["path"]}')
        bloques.append(data)
        complete_hash.update(data)
    if complete_hash.hexdigest() != inv['corpus_sha256']:
        raise ValueError('El corpus reconstruido no coincide con corpus_sha256.')
    return b''.join(bloques)


def obtener_directorio_cache(inv: dict) -> Path:
    short_hash = inv['corpus_sha256'][:12]
    cache_dir = Path(tempfile.gettempdir()) / f'mrci5-cache-{short_hash}'
    cache_dir.mkdir(parents=True, exist_ok=True)
    return cache_dir


def asegurar_archivos_corpus(codigos_modulos: set[str], rutas_especificas: set[str], forzar: bool = False) -> Path:
    """Extrae bajo demanda y con caché persistente los módulos y rutas del corpus solicitados."""
    inv = cargar_inventario()
    cache_dir = obtener_directorio_cache(inv)
    rutas_especificas_nfc = {nfc(r) for r in rutas_especificas}

    entradas_requeridas = [
        e for e in inv['files']
        if e['package'] in codigos_modulos or nfc(e['path']) in rutas_especificas_nfc
    ]

    faltantes = []
    for entry in entradas_requeridas:
        destino = cache_dir / PurePosixPath(entry['path'])
        if forzar or not destino.is_file():
            faltantes.append(entry)
        else:
            if hashlib.sha256(destino.read_bytes()).hexdigest() != entry['sha256']:
                faltantes.append(entry)

    if faltantes:
        import io
        zip_bytes = reconstruir_zip_corpus(inv)
        with zipfile.ZipFile(io.BytesIO(zip_bytes)) as archive:
            disponibles = set(archive.namelist())
            for entry in faltantes:
                digest = entry['sha256']
                if digest not in disponibles:
                    raise ValueError(f'Hash {digest} no disponible en el corpus para {entry["path"]}')
                data = archive.read(digest)
                if hashlib.sha256(data).hexdigest() != digest:
                    raise ValueError(f'Integridad incorrecta al extraer {entry["path"]}')
                destino = cache_dir / PurePosixPath(entry['path'])
                destino.parent.mkdir(parents=True, exist_ok=True)
                destino.write_bytes(data)

    return cache_dir


def cmd_listar(args):
    cat = cargar_catalogo()
    miniskills = cat['miniskills']
    if args.capa:
        miniskills = [m for m in miniskills if m['capa'] == args.capa]

    if args.json:
        print(json.dumps(miniskills, ensure_ascii=False, indent=2))
        return

    print(f"=== Catálogo del Orquestador MRCI ({cat['version']}) ===")
    print(f"Total de mini-skills registradas: {len(miniskills)}\n")
    for capa in ('sustantivo', 'formato', 'evidencia', 'extension'):
        grupo = [m for m in miniskills if m['capa'] == capa]
        if not grupo:
            continue
        print(f"[{capa.upper()}]")
        for m in grupo:
            apoyos = ', '.join(m.get('apoyos_sugeridos', [])) or '-'
            print(f"  • {m['id']:8s} | {m['titulo']} (Apoyos: {apoyos})")
        print()


def cmd_enrutar(args):
    cat = cargar_catalogo()
    texto = nfc(args.encargo.lower())

    puntuaciones = []
    for m in cat['miniskills']:
        score = 0
        coincidencias = []
        if m['id'].lower() in texto:
            score += 5
            coincidencias.append(m['id'])
        for kw in m.get('palabras_clave', []):
            kw_norm = nfc(kw.lower())
            if kw_norm in texto:
                score += 2 if ' ' in kw_norm else 1
                coincidencias.append(kw)
        if score > 0:
            puntuaciones.append((score, m, coincidencias))

    puntuaciones.sort(key=lambda x: x[0], reverse=True)

    seleccionados = []
    for _, m, _ in puntuaciones:
        if m['id'] not in seleccionados:
            seleccionados.append(m['id'])

    # Reglas de orquestación por defecto
    if not seleccionados:
        seleccionados = ['MRCI-00']

    # Si hay PRE-02 o PRE-01 pero ningún módulo sustantivo, sugerir MRCI-00 como apoyo de fondo
    mapa_ms = {m['id']: m for m in cat['miniskills']}
    capas_presentes = {mapa_ms[cid]['capa'] for cid in seleccionados if cid in mapa_ms}
    if 'sustantivo' not in capas_presentes:
        seleccionados.insert(0, 'MRCI-00')

    # Si se activa EDI-01, asegurar APA-MX
    if 'EDI-01' in seleccionados and 'APA-MX' not in seleccionados:
        seleccionados.append('APA-MX')
    if 'APA-MX' in seleccionados and 'EDI-01' not in seleccionados:
        seleccionados.append('EDI-01')

    advertencias = []
    if 'JUD-01' in seleccionados and 'JUD-02' in seleccionados:
        advertencias.append(
            'Concurrencia SOL (JUD-02) y DALILA (JUD-01): separar estrictamente la investigación '
            'litigiosa de parte de la proyección jurisdiccional imparcial.'
        )
    if 'PRE-02' in seleccionados or 'PRE-01' in seleccionados:
        advertencias.append(
            'Producción de presentaciones: conservar al módulo especialista como responsable del fondo; '
            'no desplazar la especialidad sustantiva por el formato.'
        )
    if 'EDI-01' in seleccionados or 'APA-MX' in seleccionados:
        advertencias.append(
            'Producto académico/editorial: ejecutar las 3 auditorías obligatorias de EDI-01 '
            '(formato Word 1.6.0, voz/metatexto JAPR y render completo) antes de entregar.'
        )

    resultado = {
        'encargo': args.encargo,
        'miniskills_recomendadas': seleccionados,
        'detalle': [
            {
                'id': cid,
                'titulo': mapa_ms[cid]['titulo'],
                'capa': mapa_ms[cid]['capa'],
                'apoyos_sugeridos': mapa_ms[cid].get('apoyos_sugeridos', [])
            }
            for cid in seleccionados if cid in mapa_ms
        ],
        'advertencias_orquestacion': advertencias,
        'comando_activacion': f"python3 scripts/orquestador.py activar {' '.join(seleccionados)}"
    }
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


def cmd_activar(args):
    cat = cargar_catalogo()
    mapa_ms = {m['id']: m for m in cat['miniskills']}

    codigos = []
    for c in args.codigos:
        c_up = c.upper()
        if c_up not in mapa_ms:
            raise SystemExit(f"Mini-skill desconocida: '{c}'. Ejecuta `python3 scripts/orquestador.py listar`.")
        if c_up not in codigos:
            codigos.append(c_up)

    # Identificar qué módulos del corpus .bin se necesitan
    modulos_corpus = {
        cid for cid in codigos
        if mapa_ms[cid]['origen'] == 'corpus'
    }
    archivos_core = set(cat['nucleo_transversal']['archivos'])

    cache_dir = asegurar_archivos_corpus(
        codigos_modulos=modulos_corpus,
        rutas_especificas=archivos_core,
        forzar=args.forzar
    )

    activas = {}
    for cid in codigos:
        ms = mapa_ms[cid]
        origen = ms['origen']
        info = {
            'id': cid,
            'titulo': ms['titulo'],
            'capa': ms['capa'],
            'origen': origen,
            'apoyos_sugeridos': ms.get('apoyos_sugeridos', []),
        }
        if origen == 'corpus':
            info['entrada_absoluta'] = str(cache_dir / PurePosixPath(ms['entrada']))
            info['directorio_modulo'] = str((cache_dir / PurePosixPath(ms['entrada'])).parent)
        elif origen == 'local':
            info['entrada_absoluta'] = str(ROOT / PurePosixPath(ms['entrada']))
            info['archivos_locales'] = [str(ROOT / PurePosixPath(p)) for p in ms.get('archivos_locales', [])]
        elif origen == 'extension_pre02':
            info['entrada_absoluta'] = str(ROOT / PurePosixPath(ms['entrada']))
            info['modulo_pre02'] = str(ROOT / 'extensions/PRE-02/visuales-diplomado-ia/MODULO.md')
            info['archivos_locales'] = [str(ROOT / PurePosixPath(p)) for p in ms.get('archivos_locales', [])]
            if args.incluir_recursos_pre02:
                proc = subprocess.run(
                    [sys.executable, str(ROOT / 'scripts/preparar_PRE02.py')],
                    capture_output=True, text=True, check=True
                )
                info['paquete_visual_128_extraido'] = proc.stdout.strip()
        elif origen == 'extension':
            info['entrada_absoluta'] = str(ROOT / PurePosixPath(ms['entrada']))
            info['directorio_extension'] = str((ROOT / PurePosixPath(ms['entrada'])).parent)
        activas[cid] = info

    salida = {
        'ok': True,
        'cache_corpus_dir': str(cache_dir),
        'nucleo_transversal': [str(cache_dir / PurePosixPath(p)) for p in cat['nucleo_transversal']['archivos']],
        'miniskills_activas': activas,
        'recordatorio_entrega': (
            'Antes de entregar cualquier archivo al usuario, ejecuta: '
            'python3 scripts/orquestador.py auditar <ruta_del_entregable>'
        )
    }
    print(json.dumps(salida, ensure_ascii=False, indent=2))


def cmd_crear_miniskill(args):
    cat = cargar_catalogo()
    codigo = args.codigo.upper().strip()
    if not re.match(r'^[A-Z0-9]+-[0-9A-Z]+$', codigo):
        raise SystemExit("El código debe tener formato TIPO-NN (por ejemplo: FIS-01, LAB-01, AUD-02).")

    existentes = {m['id'] for m in cat['miniskills']}
    if codigo in existentes:
        raise SystemExit(f"El código {codigo} ya existe en el catálogo.")

    slug = re.sub(r'[^a-z0-9-]+', '-', args.nombre.lower().strip()).strip('-')
    ext_dir = ROOT / 'extensions' / codigo
    refs_dir = ext_dir / 'references'
    scripts_dir = ext_dir / 'scripts'
    refs_dir.mkdir(parents=True, exist_ok=True)
    scripts_dir.mkdir(parents=True, exist_ok=True)

    modulo_md = ext_dir / 'MODULO.md'
    plantilla = f"""---
name: {slug}
description: {args.descripcion}
---

# {args.titulo} ({codigo})

## 1. Identidad y coordinación en el ecosistema

- **Identificador funcional:** `{codigo}`
- **Nombre interno:** `{slug}`
- **Capa en el orquestador:** `{args.capa}`
- **Función:** Mini-skill modular integrable bajo demanda mediante `python3 scripts/orquestador.py activar {codigo}`.

Antes de resolver un encargo sustantivo, aplica el núcleo transversal del orquestador (`00-protocolo-realidad-fuentes.md`, `01-perfil-humanizacion-japr.md` y `02-citacion-edicion.md`).

## 2. Propósito y alcance

{args.descripcion}

## 3. Cuándo activar esta mini-skill

- Cuando el usuario solicite expresamente tareas vinculadas con **{args.titulo}**.
- Cuando el orquestador principal (`SKILL.md`) asigne a `{codigo}` como módulo rector o de apoyo técnico.

## 4. Método de ejecución

1. **Diagnóstico:** Identificar hechos, documentos aportados, jurisdicción/contexto y producto esperado.
2. **Sustento y trazabilidad:** Separar hechos probados, fuentes verificadas e inferencias.
3. **Producción:** Elaborar el entregable con rigor técnico y claridad expositiva.
4. **Compuerta de calidad:** Ejecutar `python3 scripts/orquestador.py auditar <archivo>` antes de entregar.

## 5. Regla de anonimato en el entregable

El producto final entregado al usuario nunca debe mencionar `{codigo}`, `{slug}`, «MRCI» ni términos de control interno.
"""
    modulo_md.write_text(plantilla, encoding='utf-8')
    (refs_dir / 'README.md').write_text(
        f"# Referencias de {codigo} · {args.titulo}\n\nColoca aquí catálogos, guías y listas de control específicas de esta mini-skill.\n",
        encoding='utf-8'
    )

    palabras = [p.strip() for p in (args.palabras_clave or '').split(',') if p.strip()]
    if not palabras:
        palabras = [slug.replace('-', ' '), args.titulo.lower()]
    apoyos = [a.strip().upper() for a in (args.apoyos or 'DOC-03').split(',') if a.strip()]

    nueva_entrada = {
        'id': codigo,
        'nombre': slug,
        'titulo': args.titulo,
        'capa': args.capa,
        'origen': 'extension',
        'entrada': f'extensions/{codigo}/MODULO.md',
        'apoyos_sugeridos': apoyos,
        'palabras_clave': palabras,
    }
    cat['miniskills'].append(nueva_entrada)
    CATALOGO_PATH.write_text(json.dumps(cat, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

    print(json.dumps({
        'ok': True,
        'mensaje': f'Mini-skill {codigo} creada y registrada en el orquestador.',
        'directorio': str(ext_dir),
        'modulo_md': str(modulo_md),
        'entrada_catalogo': nueva_entrada
    }, ensure_ascii=False, indent=2))


def extraer_texto_archivo(ruta: Path) -> str:
    """Extrae texto plano de archivos .md, .txt, .html, .json, .docx o .pptx."""
    sufijo = ruta.suffix.lower()
    if sufijo in ('.md', '.txt', '.json', '.html', '.csv', '.yaml', '.yml'):
        return ruta.read_text(encoding='utf-8', errors='replace')

    if sufijo == '.docx':
        textos = []
        with zipfile.ZipFile(ruta) as zf:
            for nombre in zf.namelist():
                if nombre.startswith('word/') and nombre.endswith('.xml'):
                    raiz = ET.fromstring(zf.read(nombre))
                    for elem in raiz.iter():
                        if elem.tag.endswith('}t') and elem.text:
                            textos.append(elem.text)
        return '\n'.join(textos)

    if sufijo == '.pptx':
        textos = []
        with zipfile.ZipFile(ruta) as zf:
            for nombre in sorted(zf.namelist()):
                if (nombre.startswith('ppt/slides/slide') or nombre.startswith('ppt/notesSlides/notesSlide')) and nombre.endswith('.xml'):
                    raiz = ET.fromstring(zf.read(nombre))
                    for elem in raiz.iter():
                        if elem.tag.endswith('}t') and elem.text:
                            textos.append(elem.text)
        return '\n'.join(textos)

    return ruta.read_text(encoding='utf-8', errors='replace')


def cmd_auditar(args):
    ruta = Path(args.archivo).resolve()
    if not ruta.is_file():
        raise SystemExit(f"No existe el archivo a auditar: {ruta}")

    cat = cargar_catalogo()
    texto = extraer_texto_archivo(ruta)
    texto_lower = texto.lower()

    # 1. Buscar códigos y marcas internas de la metodología
    codigos_catalogo = [re.escape(m['id']) for m in cat['miniskills']]
    patrones_marcas = MARCAS_INTERNAS_BASE + [rf'\b{c}\b' for c in codigos_catalogo]

    filtraciones_metodologia = []
    for pat in patrones_marcas:
        for match in re.finditer(pat, texto, flags=re.IGNORECASE):
            val = match.group(0)
            if val not in filtraciones_metodologia:
                filtraciones_metodologia.append(val)

    # 2. Buscar expresiones vetadas JAPR (LEXICO_VETO)
    vetos_detectados = []
    for lex_id, expr, motivo in LEXICO_VETO:
        if expr.lower() in texto_lower:
            vetos_detectados.append({'id': lex_id, 'expresion': expr, 'motivo': motivo})

    # 3. Buscar expresiones de control JAPR (LEXICO_CONTROL)
    controles_detectados = []
    for lex_id, expr, criterio in LEXICO_CONTROL:
        if expr.lower() in texto_lower:
            controles_detectados.append({'id': lex_id, 'expresion': expr, 'criterio': criterio})

    bloqueado = bool(filtraciones_metodologia or vetos_detectados or (args.estricto and controles_detectados))
    estado = 'ENTREGA_BLOQUEADA' if bloqueado else 'APROBADO_PARA_ENTREGA'

    reporte = {
        'archivo': str(ruta),
        'estado': estado,
        'ok': not bloqueado,
        'filtraciones_metodologia_interna': filtraciones_metodologia,
        'expresiones_vetadas_japr': vetos_detectados,
        'alertas_control_japr': controles_detectados,
    }
    print(json.dumps(reporte, ensure_ascii=False, indent=2))
    if bloqueado:
        raise SystemExit(1)


def cmd_verificar(args):
    cat = cargar_catalogo()

    # 1. Verificar corpus base mediante abrir_corpus.py --verificar
    proc_corpus = subprocess.run(
        [sys.executable, str(ROOT / 'scripts/abrir_corpus.py'), '--verificar'],
        capture_output=True, text=True
    )
    corpus_info = json.loads(proc_corpus.stdout) if proc_corpus.returncode == 0 else {'ok': False, 'error': proc_corpus.stderr}

    # 2. Verificar entradas locales y extensiones registradas
    faltantes_locales = []
    for m in cat['miniskills']:
        if m['origen'] in ('local', 'extension_pre02', 'extension'):
            ruta_entrada = ROOT / PurePosixPath(m['entrada'])
            if not ruta_entrada.is_file():
                faltantes_locales.append(m['entrada'])
            for extra in m.get('archivos_locales', []):
                if not (ROOT / PurePosixPath(extra)).is_file():
                    faltantes_locales.append(extra)

    ok_global = bool(corpus_info.get('ok')) and not faltantes_locales
    resumen = {
        'ok': ok_global,
        'version_orquestador': cat['version'],
        'total_miniskills': len(cat['miniskills']),
        'corpus_base': corpus_info,
        'archivos_locales_faltantes': faltantes_locales,
    }
    print(json.dumps(resumen, ensure_ascii=False, indent=2))
    if not ok_global:
        raise SystemExit(1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='comando', required=True)

    p_listar = sub.add_parser('listar', help='Listar todas las mini-skills registradas en el orquestador.')
    p_listar.add_argument('--capa', choices=['sustantivo', 'formato', 'evidencia', 'extension'], help='Filtrar por capa.')
    p_listar.add_argument('--json', action='store_true', help='Imprimir en formato JSON.')
    p_listar.set_defaults(func=cmd_listar)

    p_enrutar = sub.add_parser('enrutar', help='Sugerir qué mini-skills activar según la descripción del encargo.')
    p_enrutar.add_argument('encargo', help='Descripción en lenguaje natural del encargo del usuario.')
    p_enrutar.set_defaults(func=cmd_enrutar)

    p_activar = sub.add_parser('activar', help='Preparar y devolver las rutas de las mini-skills solicitadas usando caché.')
    p_activar.add_argument('codigos', nargs='+', help='Códigos de mini-skills a activar (ej. MUN-01 PRE-02 APA-MX).')
    p_activar.add_argument('--forzar', action='store_true', help='Forzar re-extracción en caché.')
    p_activar.add_argument('--incluir-recursos-pre02', action='store_true', help='Extraer y validar también los 128 archivos visuales de PRE-02.')
    p_activar.set_defaults(func=cmd_activar)

    p_crear = sub.add_parser('crear-miniskill', help='Crear una nueva mini-skill en extensions/ y registrarla en el orquestador.')
    p_crear.add_argument('--codigo', required=True, help='Código único, ej. FIS-01 o LAB-01.')
    p_crear.add_argument('--nombre', required=True, help='Nombre corto o slug, ej. defensa-fiscal-mrci.')
    p_crear.add_argument('--titulo', required=True, help='Título descriptivo de la mini-skill.')
    p_crear.add_argument('--descripcion', required=True, help='Descripción clara de qué hace y cuándo se activa.')
    p_crear.add_argument('--capa', default='extension', choices=['sustantivo', 'formato', 'evidencia', 'extension'])
    p_crear.add_argument('--palabras-clave', help='Palabras clave separadas por coma para el enrutador.')
    p_crear.add_argument('--apoyos', default='DOC-03', help='Códigos de apoyo sugeridos separados por coma.')
    p_crear.set_defaults(func=cmd_crear_miniskill)

    p_auditar = sub.add_parser('auditar', help='Auditar un archivo entregable (.md, .txt, .docx, .pptx) contra filtraciones internas y léxico IA.')
    p_auditar.add_argument('archivo', help='Ruta al archivo entregable.')
    p_auditar.add_argument('--estricto', action='store_true', help='Bloquear también ante alertas de control (no sólo vetos).')
    p_auditar.set_defaults(func=cmd_auditar)

    p_verificar = sub.add_parser('verificar', help='Verificar integridad del corpus base y de todas las mini-skills locales.')
    p_verificar.set_defaults(func=cmd_verificar)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
