"""Build, verify and restore the music-wiki research bundle (Python 3.10+)."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[3]
DESCRIPTOR = Path('local/docs/交接/资料包.json')
MANIFEST = '_handoff/materials-manifest.json'
DIRECTORIES = ('origin_resources', 'resources')
CHUNK = 1024 * 1024


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(CHUNK), b''):
            h.update(block)
    return h.hexdigest()


def target_for(root, name):
    p = PurePosixPath(name)
    if ('\\' in name or ':' in name or p.is_absolute() or '..' in p.parts
            or len(p.parts) < 3 or p.parts[0] != 'local'
            or p.parts[1] not in DIRECTORIES):
        raise ValueError(f'Unsafe or unexpected archive path: {name}')
    target = root.joinpath(*p.parts)
    # Existing junctions/symlinks must not redirect extraction outside the repo.
    if not target.resolve().is_relative_to((root / 'local' / p.parts[1]).absolute()):
        raise ValueError(f'Extraction path escapes its resource directory: {name}')
    return target


def pack(args):
    source = args.source_root.resolve()
    output = args.archive.resolve()
    if output.exists():
        raise FileExistsError(f'Refusing to replace existing bundle: {output}')
    output.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    candidates = []
    for directory in DIRECTORIES:
        base = source / 'local' / directory
        if not base.is_dir():
            raise FileNotFoundError(base)
        for p in sorted(base.rglob('*')):
            if p.is_symlink():
                raise ValueError(f'Symlinks are not supported: {p}')
            if p.is_file():
                candidates.append(p)
    partial = output.with_suffix(output.suffix + '.partial')
    if partial.exists():
        raise FileExistsError(partial)
    stored = {'.zip', '.gz', '.bz2', '.xz', '.7z', '.jpg', '.jpeg', '.png',
              '.pdf', '.mp3', '.mp4', '.woff', '.woff2'}
    with zipfile.ZipFile(partial, 'w', allowZip64=True, compression=zipfile.ZIP_DEFLATED,
                         compresslevel=3) as archive:
        for index, p in enumerate(candidates, 1):
            name = p.relative_to(source).as_posix()
            info = zipfile.ZipInfo.from_file(p, name)
            info.compress_type = zipfile.ZIP_STORED if p.suffix.lower() in stored else zipfile.ZIP_DEFLATED
            info._compresslevel = 3
            before = p.stat()
            h = hashlib.sha256()
            count = 0
            with p.open('rb') as src, archive.open(info, 'w', force_zip64=True) as dst:
                for block in iter(lambda: src.read(CHUNK), b''):
                    h.update(block)
                    count += len(block)
                    dst.write(block)
            after = p.stat()
            if before.st_size != count or before.st_mtime_ns != after.st_mtime_ns:
                raise RuntimeError(f'Source changed while packing: {p}')
            rows.append({'path': name, 'bytes': count, 'sha256': h.hexdigest()})
            if index % 1000 == 0:
                print(f'Packed {index}/{len(candidates)} files', flush=True)
        manifest = {'format': 1, 'files': rows}
        archive.writestr(MANIFEST, json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    os.replace(partial, output)
    descriptor = {
        'format': 1, 'created_date': args.date, 'archive': output.name,
        'archive_bytes': output.stat().st_size, 'archive_sha256': digest(output),
        'manifest_path': MANIFEST, 'manifest_sha256': hashlib.sha256(
            (json.dumps(manifest, ensure_ascii=False, indent=2) + '\n').encode()).hexdigest(),
        'directories': {d: {'files': sum(r['path'].startswith('local/' + d + '/') for r in rows),
                            'bytes': sum(r['bytes'] for r in rows if r['path'].startswith('local/' + d + '/'))}
                        for d in DIRECTORIES},
        'total_files': len(rows), 'total_uncompressed_bytes': sum(r['bytes'] for r in rows),
        'extract_into': 'repository root; preserves local/origin_resources and local/resources',
        'excluded': ['local/.git', 'local/materials', 'local/archive', 'OCR runtime logs', 'credentials'],
        'source_main_commit': args.main_commit, 'source_local_commit': args.local_commit,
    }
    dest = args.descriptor or ROOT / DESCRIPTOR
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(descriptor, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(descriptor, ensure_ascii=False, indent=2), flush=True)


def check(args):
    root = args.repo_root.resolve()
    desc = json.loads((args.descriptor or root / DESCRIPTOR).read_text(encoding='utf-8-sig'))
    archive_path = args.archive.resolve()
    if archive_path.stat().st_size != desc['archive_bytes'] or digest(archive_path) != desc['archive_sha256']:
        raise ValueError('Archive size/SHA-256 mismatch; obtain the matching complete bundle')
    print('Archive SHA-256 verified', flush=True)
    with zipfile.ZipFile(archive_path) as archive:
        manifest_bytes = archive.read(MANIFEST)
        if hashlib.sha256(manifest_bytes).hexdigest() != desc['manifest_sha256']:
            raise ValueError('Manifest SHA-256 mismatch')
        rows = json.loads(manifest_bytes)['files']
        names = [r['path'] for r in rows]
        actual_names = archive.namelist()
        if (len(set(actual_names)) != len(actual_names) or len(set(names)) != len(names)
                or set(actual_names) != set(names) | {MANIFEST}
                or len(rows) != desc['total_files']
                or sum(r['bytes'] for r in rows) != desc['total_uncompressed_bytes']):
            raise ValueError('Archive/manifest inventory mismatch')
        targets = [target_for(root, name) for name in names]
        # Check all collisions before writing any file; retain collaborators' edits.
        if args.command == 'restore':
            for row, target in zip(rows, targets):
                if target.exists() and (not target.is_file() or target.stat().st_size != row['bytes']
                                        or digest(target) != row['sha256']):
                    raise FileExistsError(f'Different local file; refusing to overwrite: {target}')
            needed = sum(r['bytes'] for r, t in zip(rows, targets) if not t.exists())
            if shutil.disk_usage(root).free < needed + 128 * 1024 * 1024:
                raise OSError(f'Insufficient free space; need at least {needed} bytes plus margin')
        restored = skipped = 0
        for index, (row, target) in enumerate(zip(rows, targets), 1):
            if archive.getinfo(row['path']).file_size != row['bytes']:
                raise ValueError(f'Entry size mismatch: {row["path"]}')
            if args.command == 'restore' and target.exists():
                skipped += 1
                continue
            h = hashlib.sha256()
            temp = None
            try:
                if args.command == 'restore':
                    target.parent.mkdir(parents=True, exist_ok=True)
                    fd, temp = tempfile.mkstemp(prefix='.handoff-', dir=target.parent)
                    dst = os.fdopen(fd, 'wb')
                else:
                    dst = None
                with archive.open(row['path']) as src:
                    for block in iter(lambda: src.read(CHUNK), b''):
                        h.update(block)
                        if dst:
                            dst.write(block)
                if dst:
                    dst.close()
                if h.hexdigest() != row['sha256']:
                    raise ValueError(f'Entry SHA-256 mismatch: {row["path"]}')
                if temp:
                    os.replace(temp, target)
                    temp = None
                    restored += 1
            finally:
                if 'dst' in locals() and dst and not dst.closed:
                    dst.close()
                if temp:
                    Path(temp).unlink(missing_ok=True)
            if index % 2000 == 0:
                print(f'Checked {index}/{len(rows)} files', flush=True)
    print(json.dumps({'verified_files': len(rows), 'restored': restored, 'already_identical': skipped,
                      'archive': str(archive_path)}, ensure_ascii=False), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('pack')
    p.add_argument('--source-root', type=Path, required=True)
    p.add_argument('--date', required=True)
    p.add_argument('--main-commit', required=True)
    p.add_argument('--local-commit', required=True)
    for name in ('verify', 'restore'):
        p = sub.add_parser(name)
        p.add_argument('--repo-root', type=Path, default=ROOT)
    for p in sub.choices.values():
        p.add_argument('--archive', type=Path, required=True)
        p.add_argument('--descriptor', type=Path)
    args = parser.parse_args()
    pack(args) if args.command == 'pack' else check(args)


if __name__ == '__main__':
    main()
