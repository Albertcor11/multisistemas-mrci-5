#!/usr/bin/env python3
"""Recuperar y verificar el paquete visual PRE-02 desde su ZIP original."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--zip', type=Path, help='ZIP externo opcional; por defecto usar el paquete completo incorporado.')
    args = parser.parse_args()
    manifest = json.loads((ROOT / 'references/inventario-PRE-02.json').read_text())
    if args.zip is None:
        cache = Path(tempfile.mkdtemp(prefix='mrci-pre02-zip-'))
        args.zip = cache / 'PRE02.zip'
        with args.zip.open('wb') as out:
            for row in manifest['embedded_parts']:
                part = PurePosixPath(row['path'])
                if part.is_absolute() or '..' in part.parts:
                    raise ValueError('Ruta de recurso no segura')
                blob = (ROOT / part).read_bytes()
                if len(blob) != row['bytes'] or sha(blob) != row['sha256']:
                    raise ValueError('Parte PRE-02 alterada o incompleta: ' + row['path'])
                out.write(blob)
    payload = args.zip.read_bytes()
    if sha(payload) != manifest['source_sha256']:
        raise ValueError('El ZIP no coincide con el original verificado de PRE-02.')
    expected = {row['path']: row['sha256_original'] for row in manifest['files']}
    entries = {}
    with zipfile.ZipFile(args.zip) as archive:
        for item in archive.infolist():
            if item.is_dir():
                continue
            name = item.filename
            try:
                name = name.encode('cp437').decode('utf-8')
            except UnicodeError:
                pass
            name = unicodedata.normalize('NFC', name)
            parts = PurePosixPath(name).parts
            if len(parts) < 2 or '..' in parts or name.startswith('/'):
                raise ValueError('Ruta insegura en el paquete.')
            path = PurePosixPath(*parts[1:])
            if path.name == 'SKILL.md':
                path = path.with_name('MODULO.md')
            key = path.as_posix()
            data = archive.read(item)
            if key in entries or expected.get(key) != sha(data):
                raise ValueError('Archivo inesperado, duplicado o alterado: ' + key)
            entries[key] = data
    if set(entries) != set(expected):
        raise ValueError('El paquete está incompleto.')
    destination = Path(tempfile.mkdtemp(prefix='MRCI_PRE02_'))
    try:
        for key, data in entries.items():
            target = destination / key
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        validator = destination / 'visuales-diplomado-ia/scripts/validar_sistema_visual.py'
        validator.write_text(validator.read_text().replace('SKILL.md', 'MODULO.md'))
        result = subprocess.run([sys.executable, str(validator)], capture_output=True, text=True)
        if result.returncode:
            raise ValueError(result.stdout + result.stderr)
    except Exception:
        shutil.rmtree(destination)
        raise
    print(f'Verificados {len(entries)} archivos; validación completa APROBADA.', file=sys.stderr)
    print(destination)


if __name__ == '__main__':
    main()
