#!/usr/bin/env python3
"""Reempaquetar el corpus de módulos desde una copia extraída y editada.

Flujo: `abrir_corpus.py` extrae a una carpeta temporal, se editan los archivos de
`modulos/` en esa carpeta y este script regenera `assets/corpus/parte-NN.bin` y las
huellas de `references/inventario.json`. Después, verificar con
`abrir_corpus.py --verificar`. No toca PRE-02, que se sella contra su ZIP original.
"""
import argparse
import hashlib
import io
import json
from pathlib import Path
import unicodedata
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PARTE = 16 * 1024 * 1024
IGNORAR = {'.DS_Store', '__pycache__', '.pytest_cache'}


def nfc(ruta):
    # El inventario conserva la forma Unicode original de cada ruta (algunas en NFD);
    # sólo se normaliza para comparar.
    return unicodedata.normalize('NFC', ruta)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('carpeta', type=Path, help='Carpeta devuelta por abrir_corpus.py, con modulos/ editado.')
    parser.add_argument('--version', help='Identificador de la actualización; obligatorio si hay cambios.')
    parser.add_argument('--registro', help='Ruta del registro de cambios dentro de la skill, p. ej. references/registro-...md')
    parser.add_argument('--fecha', default='2026-10-24', help='Fecha AAAA-MM-DD; también fija la fecha interna del ZIP.')
    parser.add_argument('--permitir-borrados', action='store_true', help='Quitar del inventario los archivos eliminados.')
    parser.add_argument('--simular', action='store_true', help='Informar los cambios sin escribir nada.')
    args = parser.parse_args()

    inv_path = ROOT / 'references/inventario.json'
    inv = json.loads(inv_path.read_text())
    paquetes = {p['name']: p['id'] for p in inv['packages']}

    actuales = {}
    for archivo in sorted((args.carpeta / 'modulos').rglob('*')):
        relativa = archivo.relative_to(args.carpeta)
        if archivo.is_file() and not IGNORAR & set(relativa.parts) and archivo.suffix != '.pyc':
            actuales[nfc(relativa.as_posix())] = archivo.read_bytes()
    if not actuales:
        raise SystemExit('La carpeta no contiene modulos/.')

    registradas = {nfc(e['path']) for e in inv['files']}
    borrados = sorted(registradas - set(actuales))
    if borrados and not args.permitir_borrados:
        raise SystemExit('Faltan archivos del inventario (usar --permitir-borrados si es intencional):\n' + '\n'.join(borrados))
    nuevos = sorted(set(actuales) - registradas)
    desconocidos = [r for r in nuevos if r.split('/')[1] not in paquetes]
    if desconocidos:
        raise SystemExit('Carpeta de módulo no registrada en el inventario:\n' + '\n'.join(desconocidos))

    inv['files'] = [e for e in inv['files'] if nfc(e['path']) in actuales]
    modificados = []
    for entrada in inv['files']:
        digest = hashlib.sha256(actuales[nfc(entrada['path'])]).hexdigest()
        if digest != entrada['sha256']:
            entrada['sha256'] = digest
            entrada['storage'] = 'embedded'
            modificados.append(entrada['path'])
    for ruta in nuevos:
        paquete = paquetes[ruta.split('/')[1]]
        ultimo = max(i for i, e in enumerate(inv['files']) if e['package'] == paquete)
        inv['files'].insert(ultimo + 1, {'path': ruta, 'original_path': ruta,
                                         'sha256': hashlib.sha256(actuales[ruta]).hexdigest(),
                                         'package': paquete, 'source': None, 'storage': 'embedded'})

    resumen = {'modificados': modificados, 'nuevos': nuevos, 'borrados': borrados}
    print(json.dumps(resumen, ensure_ascii=False, indent=2))
    if not (modificados or nuevos or borrados):
        print('Sin cambios; no se escribe nada.')
        return
    if args.simular:
        return
    if not args.version:
        raise SystemExit('Indicar --version para registrar la actualización.')

    for paquete in inv['packages']:
        paquete['files'] = sum(1 for e in inv['files'] if e['package'] == paquete['id'])

    # Un miembro por contenido único, nombrado por su SHA-256, con fecha fija para que
    # el mismo contenido produzca siempre los mismos bytes.
    fecha = tuple(int(x) for x in args.fecha.split('-')) + (0, 0, 0)
    buffer = io.BytesIO()
    vistos = set()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as archive:
        for entrada in inv['files']:
            if entrada['sha256'] not in vistos:
                vistos.add(entrada['sha256'])
                info = zipfile.ZipInfo(entrada['sha256'], fecha)
                info.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(info, actuales[nfc(entrada['path'])])
    blob = buffer.getvalue()

    for viejo in (ROOT / 'assets/corpus').glob('parte-*.bin'):
        viejo.unlink()
    partes = []
    for numero, inicio in enumerate(range(0, len(blob), PARTE), start=1):
        datos = blob[inicio:inicio + PARTE]
        ruta = f'assets/corpus/parte-{numero:02d}.bin'
        (ROOT / ruta).write_bytes(datos)
        partes.append({'path': ruta, 'sha256': hashlib.sha256(datos).hexdigest(), 'bytes': len(datos)})
    inv['corpus_parts'] = partes
    inv['corpus_sha256'] = hashlib.sha256(blob).hexdigest()
    inv['actualizacion'][args.version] = {
        'fecha_local': args.fecha,
        'archivos_modificados': len(modificados),
        'archivos_nuevos': len(nuevos),
        'archivos_borrados': len(borrados),
        'registro': args.registro,
    }
    inv_path.write_text(json.dumps(inv, indent=2, ensure_ascii=False))
    print(f'Corpus regenerado: {len(inv["files"])} archivos, {len(partes)} partes. Ejecutar abrir_corpus.py --verificar.')


if __name__ == '__main__':
    main()
