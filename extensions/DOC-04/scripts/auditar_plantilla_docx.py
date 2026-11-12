#!/usr/bin/env python3
"""Auditor técnico de plantillas requisitadas y consistencia fáctica (DOC-04).

Verifica sobre un archivo entregable (.docx, .md o .txt):
1. Preservación íntegra de imágenes/logotipos (word/media/* y nodos gráficos)
   y encabezados/pies frente al molde original (--molde).
2. Ausencia de marcadores residuales de plantilla ([1], [Ej. ...], {{campo}},
   <<campo>>, [Insertar ...], XXXX), reconstruyendo párrafos completos aunque
   Word haya fragmentado el texto en múltiples corridas (<w:r>).
3. Control explícito de marcadores [PENDIENTE: ...] (bloquean entrega definitiva,
   o pasan como BORRADOR_PARA_REVISION si se indica --permitir-pendientes).
4. Ausencia de comentarios residuales o control de cambios sin aceptar en .docx
   (salvo --permitir-revisiones).
5. Cotejo opcional contra una Ficha de Datos Maestros en JSON (--ficha-json) con
   listas `valores_obligatorios` y `residuos_prohibidos`, incluyendo verificación
   de paridad sobre archivos adicionales del mismo paquete (--paquete).
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
import zipfile

PATRON_PENDIENTE = re.compile(r'\[\s*PENDIENTE\s*:\s*([^\]]+?)\s*\]', flags=re.IGNORECASE)

PATRONES_MARCADOR_RESIDUAL = [
    ('MARCADOR_NUMERICO', re.compile(r'\[(\d{1,3})\]')),
    ('MARCADOR_EJEMPLO', re.compile(r'\[\s*(?:ej\.?|ejemplo|insertar|colocar|completar|indicar|escribir|nombre|fecha|monto|folio|rfc|domicilio|cargo)\b[^\]]*\]', flags=re.IGNORECASE)),
    ('MARCADOR_DOBLE_LLAVE', re.compile(r'\{\{\s*[^}]+\s*\}\}')),
    ('MARCADOR_ANGULAR', re.compile(r'<<\s*[^>]+\s*>>')),
    ('MARCADOR_BLOQUE_PLANTILLA', re.compile(r'\[\s*(?:BLOQUE\s+CONDICIONAL|TABLA\s+DIN[ÁA]MICA)\b[^\]]*\]', flags=re.IGNORECASE)),
    ('MARCADOR_XXXX', re.compile(r'\bX{4,}\b')),
]

ETIQUETAS_GRAFICAS = {'drawing', 'pict', 'imagedata', 'blip'}


def nfc(texto: str) -> str:
    return unicodedata.normalize('NFC', texto)


def local_name(tag: str) -> str:
    return tag.rsplit('}', 1)[-1] if '}' in tag else tag


def inspeccionar_docx(ruta: Path) -> dict:
    """Extrae párrafos reconstruidos, medios SHA-256, conteo gráfico y revisiones de un .docx."""
    parrafos: list[str] = []
    medios: dict[str, str] = {}
    nodos_graficos = 0
    partes_encabezado_pie: list[str] = []
    tiene_comentarios = False
    cambios_sin_aceptar = 0

    with zipfile.ZipFile(ruta) as zf:
        nombres = sorted(zf.namelist())
        for nombre in nombres:
            if nombre.startswith('word/media/') and not nombre.endswith('/'):
                datos = zf.read(nombre)
                medios[nombre] = hashlib.sha256(datos).hexdigest()
            elif re.match(r'^word/(header|footer)\d*\.xml$', nombre):
                partes_encabezado_pie.append(nombre)

            if nombre == 'word/comments.xml':
                raiz_com = ET.fromstring(zf.read(nombre))
                for elem in raiz_com.iter():
                    if local_name(elem.tag) == 'comment':
                        tiene_comentarios = True
                        break

            if nombre.startswith('word/') and nombre.endswith('.xml') and nombre != 'word/comments.xml':
                raiz = ET.fromstring(zf.read(nombre))
                for elem in raiz.iter():
                    ln = local_name(elem.tag)
                    if ln in ETIQUETAS_GRAFICAS:
                        nodos_graficos += 1
                    elif ln in ('ins', 'del'):
                        cambios_sin_aceptar += 1
                    elif ln == 'p':
                        fragmentos = []
                        for sub in elem.iter():
                            sub_ln = local_name(sub.tag)
                            if sub_ln == 't' and sub.text:
                                fragmentos.append(sub.text)
                            elif sub_ln == 'tab':
                                fragmentos.append('\t')
                            elif sub_ln in ('br', 'cr'):
                                fragmentos.append('\n')
                        texto_p = ''.join(fragmentos).strip()
                        if texto_p:
                            parrafos.append(nfc(texto_p))

    return {
        'texto_completo': '\n'.join(parrafos),
        'parrafos': parrafos,
        'medios': medios,
        'nodos_graficos': nodos_graficos,
        'encabezados_pies': partes_encabezado_pie,
        'tiene_comentarios': tiene_comentarios,
        'cambios_sin_aceptar': cambios_sin_aceptar,
    }


def extraer_info_archivo(ruta: Path) -> dict:
    if ruta.suffix.lower() == '.docx':
        return inspeccionar_docx(ruta)
    texto = nfc(ruta.read_text(encoding='utf-8', errors='replace'))
    lineas = [ln.strip() for ln in texto.splitlines() if ln.strip()]
    return {
        'texto_completo': texto,
        'parrafos': lineas,
        'medios': {},
        'nodos_graficos': 0,
        'encabezados_pies': [],
        'tiene_comentarios': False,
        'cambios_sin_aceptar': 0,
    }


def buscar_marcadores(parrafos: list[str]) -> tuple[list[str], list[dict]]:
    pendientes: list[str] = []
    residuales: list[dict] = []

    for idx, p in enumerate(parrafos, start=1):
        for m_pend in PATRON_PENDIENTE.finditer(p):
            detalle = m_pend.group(1).strip()
            if detalle not in pendientes:
                pendientes.append(detalle)

        p_sin_pendientes = PATRON_PENDIENTE.sub('', p)
        for tipo, patron in PATRONES_MARCADOR_RESIDUAL:
            for match in patron.finditer(p_sin_pendientes):
                valor = match.group(0)
                residuales.append({
                    'tipo': tipo,
                    'marcador': valor,
                    'parrafo_num': idx,
                    'contexto': p[:140],
                })

    return pendientes, residuales


def comparar_con_molde(info_doc: dict, ruta_molde: Path) -> dict:
    info_molde = inspeccionar_docx(ruta_molde)
    medios_molde = info_molde['medios']
    medios_doc = info_doc['medios']

    medios_faltantes = []
    medios_alterados = []
    for ruta_media, sha_molde in medios_molde.items():
        if ruta_media not in medios_doc:
            medios_faltantes.append(ruta_media)
        elif medios_doc[ruta_media] != sha_molde:
            medios_alterados.append(ruta_media)

    encabezados_faltantes = [
        hp for hp in info_molde['encabezados_pies']
        if hp not in info_doc['encabezados_pies']
    ]
    perdida_grafica = info_doc['nodos_graficos'] < info_molde['nodos_graficos']

    preservado = (
        not medios_faltantes
        and not medios_alterados
        and not encabezados_faltantes
        and not perdida_grafica
    )
    return {
        'molde': str(ruta_molde),
        'preservado': preservado,
        'medios_molde_total': len(medios_molde),
        'medios_entregable_total': len(medios_doc),
        'medios_faltantes': medios_faltantes,
        'medios_alterados': medios_alterados,
        'nodos_graficos_molde': info_molde['nodos_graficos'],
        'nodos_graficos_entregable': info_doc['nodos_graficos'],
        'encabezados_pies_faltantes': encabezados_faltantes,
    }


def evaluar_ficha_maestra(
    texto_principal: str,
    ruta_ficha: Path,
    rutas_paquete: list[Path],
) -> dict:
    ficha = json.loads(ruta_ficha.read_text(encoding='utf-8'))
    obligatorios = [nfc(str(v)) for v in ficha.get('valores_obligatorios', [])]
    prohibidos = [nfc(str(v)) for v in ficha.get('residuos_prohibidos', [])]
    atributos_paridad = {
        nfc(str(k)): nfc(str(v))
        for k, v in ficha.get('atributos_transversales', {}).items()
    }

    faltantes = [val for val in obligatorios if val not in texto_principal]
    residuos = [
        val for val in prohibidos
        if val and val.lower() in texto_principal.lower()
    ]

    inconsistencias_paquete = []
    if rutas_paquete and atributos_paridad:
        textos_paquete = {
            str(r): extraer_info_archivo(r)['texto_completo']
            for r in rutas_paquete
        }
        for nombre_attr, valor_esperado in atributos_paridad.items():
            presente_principal = valor_esperado in texto_principal
            if not presente_principal:
                inconsistencias_paquete.append({
                    'atributo': nombre_attr,
                    'valor_maestro': valor_esperado,
                    'archivo': 'principal',
                })
            for ruta_str, txt_extra in textos_paquete.items():
                if valor_esperado not in txt_extra:
                    inconsistencias_paquete.append({
                        'atributo': nombre_attr,
                        'valor_maestro': valor_esperado,
                        'archivo': ruta_str,
                    })

    return {
        'ficha': str(ruta_ficha),
        'faltantes_ficha_maestra': faltantes,
        'residuos_asunto_previo_detectados': residuos,
        'inconsistencias_transversales': inconsistencias_paquete,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('entregable', help='Ruta del archivo requisitado (.docx, .md, .txt).')
    parser.add_argument('--molde', help='Ruta del molde .docx original para verificar preservación de logotipos y encabezados.')
    parser.add_argument('--permitir-pendientes', action='store_true', help='Autorizar modo borrador preliminar con marcadores [PENDIENTE: ...].')
    parser.add_argument('--permitir-revisiones', action='store_true', help='Permitir comentarios o control de cambios activos en .docx.')
    parser.add_argument('--ficha-json', help='Archivo JSON con valores_obligatorios, residuos_prohibidos y atributos_transversales.')
    parser.add_argument('--paquete', nargs='*', default=[], help='Archivos adicionales del mismo paquete multi-destinatario para verificar paridad.')
    args = parser.parse_args()

    ruta_entregable = Path(args.entregable).resolve()
    if not ruta_entregable.is_file():
        raise SystemExit(f'No existe el archivo entregable: {ruta_entregable}')

    info = extraer_info_archivo(ruta_entregable)
    pendientes, residuales = buscar_marcadores(info['parrafos'])

    hallazgos_criticos: list[str] = []
    hallazgos_mayores: list[str] = []

    if residuales:
        hallazgos_criticos.append(
            f'Se detectaron {len(residuales)} marcador(es) residual(es) de plantilla sin requisitar.'
        )

    if pendientes and not args.permitir_pendientes:
        hallazgos_criticos.append(
            f'Existen {len(pendientes)} campo(s) [PENDIENTE: ...] no admisibles en entrega definitiva.'
        )

    resultado_molde = None
    if args.molde:
        ruta_molde = Path(args.molde).resolve()
        if not ruta_molde.is_file():
            raise SystemExit(f'No existe el archivo molde: {ruta_molde}')
        if ruta_entregable.suffix.lower() != '.docx' or ruta_molde.suffix.lower() != '.docx':
            raise SystemExit('La comparación --molde requiere que ambos archivos sean .docx.')
        resultado_molde = comparar_con_molde(info, ruta_molde)
        if not resultado_molde['preservado']:
            hallazgos_criticos.append(
                'El entregable perdió o alteró logotipos/imágenes, nodos gráficos o encabezados/pies respecto del molde.'
            )

    if ruta_entregable.suffix.lower() == '.docx' and not args.permitir_revisiones:
        if info['tiene_comentarios']:
            hallazgos_mayores.append('El archivo .docx conserva comentarios de revisión en word/comments.xml.')
        if info['cambios_sin_aceptar'] > 0:
            hallazgos_mayores.append(
                f"El archivo .docx conserva {info['cambios_sin_aceptar']} marca(s) de control de cambios sin aceptar."
            )

    resultado_ficha = None
    if args.ficha_json:
        ruta_ficha = Path(args.ficha_json).resolve()
        if not ruta_ficha.is_file():
            raise SystemExit(f'No existe el archivo de ficha maestra: {ruta_ficha}')
        rutas_paq = [Path(p).resolve() for p in args.paquete]
        resultado_ficha = evaluar_ficha_maestra(info['texto_completo'], ruta_ficha, rutas_paq)
        if resultado_ficha['faltantes_ficha_maestra']:
            hallazgos_criticos.append(
                'Faltan valores obligatorios o no coinciden exactamente con la Ficha de Datos Maestros.'
            )
        if resultado_ficha['residuos_asunto_previo_detectados']:
            hallazgos_criticos.append(
                'Se detectaron datos residuales prohibidos de un cliente o asunto anterior.'
            )
        if resultado_ficha['inconsistencias_transversales']:
            hallazgos_criticos.append(
                'Inconsistencia transversal detectada entre versiones del paquete multi-destinatario.'
            )

    if hallazgos_criticos:
        ok = False
        severidad_maxima = 'Crítico'
        dictamen = 'NO CONFORME'
        estado_operativo = 'ENTREGA_BLOQUEADA'
    elif pendientes and args.permitir_pendientes:
        ok = True
        severidad_maxima = 'Observación' if not hallazgos_mayores else 'Mayor'
        dictamen = 'CONFORME CON OBSERVACIONES'
        estado_operativo = 'BORRADOR_PARA_REVISION'
    elif hallazgos_mayores:
        ok = False
        severidad_maxima = 'Mayor'
        dictamen = 'NO CONFORME'
        estado_operativo = 'ENTREGA_BLOQUEADA'
    else:
        ok = True
        severidad_maxima = 'Ninguna'
        dictamen = 'CONFORME'
        estado_operativo = 'REQUIERE_VALIDACION_HUMANA'

    salida = {
        'ok': ok,
        'archivo': str(ruta_entregable),
        'estado_operativo': estado_operativo,
        'dictamen_mpro': dictamen,
        'severidad_maxima': severidad_maxima,
        'pendientes_declarados': pendientes,
        'marcadores_residuales': residuales,
        'comparacion_molde': resultado_molde,
        'validacion_ficha_maestra': resultado_ficha,
        'hallazgos_criticos': hallazgos_criticos,
        'hallazgos_mayores': hallazgos_mayores,
    }
    print(json.dumps(salida, ensure_ascii=False, indent=2))
    if not ok:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
