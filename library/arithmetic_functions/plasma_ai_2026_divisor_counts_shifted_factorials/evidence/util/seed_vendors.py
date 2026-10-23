"""Copy matching vendor caches, leaving every project-owned Lean module unbuilt."""

from __future__ import annotations

# Git and cp are declared dependencies, invoked without a shell.
# ruff: noqa: S603, S607
import json
import platform
import shutil
import subprocess
import sys
from pathlib import Path

source, cache = (Path(arg).resolve() for arg in sys.argv[1:])
for name in ('lean-toolchain', 'lakefile.toml', 'lake-manifest.json'):
    if (source / name).read_bytes() != (cache / name).read_bytes():
        raise SystemExit(f'cache configuration differs: {name}')

expected = {
    p.relative_to(source / 'vendor')
    for p in (source / 'vendor').rglob('*')
    if p.is_file()
}
actual = {
    p.relative_to(cache / 'vendor')
    for p in (cache / 'vendor').rglob('*')
    if p.is_file()
}
if expected != actual:
    raise SystemExit('vendor source file lists differ')
for name in sorted(expected):
    if (source / 'vendor' / name).read_bytes() != (
        cache / 'vendor' / name
    ).read_bytes():
        raise SystemExit(f'vendor source differs: {name}')
print(f'verified {len(expected)} identical vendor source files', flush=True)

# The source cache may use Lake's local dependency overrides. Check their actual
# Git revisions and clean source trees against the held manifest before reuse.
overrides_file = cache / '.lake' / 'package-overrides.json'
overrides = {}
if overrides_file.exists():
    overrides = {
        p['name']: p for p in json.loads(overrides_file.read_text())['packages']
    }
for package in json.loads((source / 'lake-manifest.json').read_text())['packages']:
    override = overrides.get(package['name'])
    origin = (
        cache / override['dir']
        if override and override['type'] == 'path'
        else cache / '.lake' / 'packages' / package['name']
    )
    revision = subprocess.check_output(
        ['git', '-C', str(origin), 'rev-parse', 'HEAD'], text=True
    ).strip()
    dirty = subprocess.check_output(
        ['git', '-C', str(origin), 'status', '--porcelain'], text=True
    ).strip()
    if revision != package['rev'] or dirty:
        raise SystemExit(
            f'vendor cache dependency is not clean at its pinned revision: {origin}'
        )

namespaces = (
    'OAI',
    'PrimeNumberTheoremAnd',
    'RellichKondrachov',
    'PrimeGapsTheory',
    'PrimeGapsCert',
)
modules = {
    Path(*name.parts[1:]).with_suffix('') for name in expected if name.suffix == '.lean'
}
settings = 0
for module in sorted(modules):
    if module.parts[0] not in namespaces:
        raise SystemExit(f'unexpected vendor source namespace: {module}')
    setup = cache / '.lake/build/ir' / f'{module}.setup.json'
    config = json.loads(setup.read_text())
    if config.get('options') != {'autoImplicit': False} or config.get('plugins') != []:
        raise SystemExit(f'vendor cache has unexpected build options: {setup}')
    if config.get('package') != 'Erdos420':
        raise SystemExit(f'vendor cache has unexpected owning package: {setup}')
    if not (cache / '.lake/build/lib/lean' / f'{module}.olean').is_file():
        raise SystemExit(f'missing compiled vendor module: {module}')
    settings += 1
print(f'verified build settings for {settings} cached vendor modules', flush=True)

# Never copy the containing build directory: that would bring in Erdos420,
# Challenge, or Solution artifacts. Only these explicit vendor namespaces qualify.
for area in ('lib/lean', 'ir'):
    for namespace in namespaces:
        origin = cache / '.lake/build' / area / namespace
        if not origin.is_dir():
            raise SystemExit(f'missing vendor artifact namespace: {origin}')
        destination = source / '.lake/build' / area / namespace
        if destination.exists():
            raise SystemExit(f'refusing to replace {destination}')
        destination.parent.mkdir(parents=True, exist_ok=True)
        if platform.system() == 'Darwin':
            subprocess.run(['cp', '-cR', str(origin), str(destination)], check=True)
        else:
            shutil.copytree(origin, destination, symlinks=True)
# Older builds can leave unrelated modules within a vendor namespace. Remove
# every artifact whose source module is absent from the retained vendor tree.
removed = 0
for area in ('lib/lean', 'ir'):
    build_root = source / '.lake/build' / area
    for namespace in namespaces:
        for artifact in (build_root / namespace).rglob('*'):
            if artifact.is_file():
                relative = artifact.relative_to(build_root)
                module = relative.parent / relative.name.split('.', 1)[0]
                if module not in modules:
                    artifact.unlink()
                    removed += 1
print(
    f'removed {removed} stale artifacts outside the retained vendor module set',
    flush=True,
)
print(
    'copied only retained vendor modules; no project proof artifacts copied', flush=True
)
