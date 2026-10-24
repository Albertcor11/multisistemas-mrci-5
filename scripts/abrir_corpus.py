"""Recuperar recursos MRCI con verificación, desde el contenedor y las skills declaradas."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import tempfile
import zipfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--modulo', action='append', help='Código de módulo; repetible. Omitir para recuperar todos.')
    parser.add_argument('--originales', action='store_true', help='Restaurar nombres originales SKILL.md.')
    parser.add_argument('--verificar', action='store_true', help='Sólo verificar; no crear una copia temporal.')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    repo = root.parent
    inv = json.loads((root / 'references/inventario.json').read_text())
    codes = {p['id'] for p in inv['packages']}
    selected = set(args.modulo or codes)
    if selected - codes:
        raise ValueError('Módulo desconocido: ' + ', '.join(sorted(selected - codes)))
    entries = [e for e in inv['files'] if e['package'] in selected]
    target = None if args.verificar else Path(tempfile.mkdtemp(prefix='mrci5-'))
    checked = {}
    source_roots = {}
    failures = []
    embedded = external = 0
    corpus_cache = None
    archive_path = root / 'assets/corpus.zip'
    if inv.get('corpus_parts'):
        corpus_cache = tempfile.TemporaryDirectory(prefix='mrci-corpus-verificado-')
        archive_path = Path(corpus_cache.name) / 'corpus.zip'
        complete_hash = hashlib.sha256()
        with archive_path.open('wb') as output:
            for part in inv['corpus_parts']:
                relative = PurePosixPath(part['path'])
                if relative.is_absolute() or '..' in relative.parts:
                    raise ValueError('Ruta de corpus no segura')
                data = (root / relative).read_bytes()
                if len(data) != part['bytes'] or hashlib.sha256(data).hexdigest() != part['sha256']:
                    raise ValueError('Parte de corpus alterada: ' + part['path'])
                output.write(data)
                complete_hash.update(data)
        if complete_hash.hexdigest() != inv['corpus_sha256']:
            raise ValueError('El corpus reconstruido no coincide')
    with zipfile.ZipFile(archive_path) as archive:
        available = set(archive.namelist())
        for entry in entries:
            digest = entry['sha256']
            if digest not in checked:
                if digest in available:
                    data = archive.read(digest)
                else:
                    source = entry.get('source')
                    if not source:
                        failures.append(entry['path'] + ': Sin fuente disponible')
                        continue
                    part = PurePosixPath(source['relative_path'])
                    directory = PurePosixPath(source['skill_dir'])
                    if part.is_absolute() or '..' in part.parts or len(directory.parts) != 1:
                        raise ValueError('Ruta de dependencia no segura')
                    candidates = [repo / directory / part]
                    if not candidates[0].is_file() or hashlib.sha256(candidates[0].read_bytes()).hexdigest() != digest:
                        name = source['skill_name']
                        if name not in source_roots:
                            source_roots[name] = []
                            for md in repo.glob('*/SKILL.md'):
                                head = md.read_text(errors='replace')[:3000]
                                match = re.search(r'^name:\s*[\'"]?([^\n\'"]+)', head, re.M)
                                if match and match.group(1).strip() == name:
                                    source_roots[name].append(md.parent)
                        candidates.extend(p / part for p in source_roots[name])
                    data = None
                    for candidate in candidates:
                        if candidate.is_file():
                            blob = candidate.read_bytes()
                            if hashlib.sha256(blob).hexdigest() == digest:
                                data = blob
                                break
                    if data is None:
                        failures.append(entry['path'] + ': Dependencia ausente o versión distinta (' + source['skill_name'] + ')')
                        continue
                if hashlib.sha256(data).hexdigest() != digest:
                    failures.append(entry['path'] + ': Integridad incorrecta')
                    continue
                checked[digest] = data
            if digest in available:
                embedded += 1
            else:
                external += 1
            if target:
                part = PurePosixPath(entry['original_path'] if args.originales else entry['path'])
                if part.is_absolute() or '..' in part.parts:
                    raise ValueError('Ruta de salida no segura')
                output = target / part
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_bytes(checked[digest])
    if corpus_cache:
        corpus_cache.cleanup()
    if failures:
        print(json.dumps({'ok': False, 'failures': failures}, ensure_ascii=False, indent=2))
        raise SystemExit(1)
    if target:
        print(target)
    else:
        print(json.dumps({'ok': True, 'modules': len(selected), 'files': len(entries), 'embedded_files': embedded, 'dependency_files': external}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
