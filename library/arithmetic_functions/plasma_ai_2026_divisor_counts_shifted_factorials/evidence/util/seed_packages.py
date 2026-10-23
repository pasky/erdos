"""Copy only pinned, clean Mathlib dependencies into a fresh replay workspace."""

from __future__ import annotations

# Git and cp are declared command-line dependencies; all calls use argument lists.
# ruff: noqa: S603, S607
import json
import platform
import shutil
import subprocess
import sys
from pathlib import Path

source, cache = map(Path, sys.argv[1:])
packages = source / '.lake' / 'packages'
packages.mkdir(parents=True, exist_ok=True)
for package in json.loads((source / 'lake-manifest.json').read_text())['packages']:
    origin = cache / package['name']
    revision = subprocess.check_output(
        ['git', '-C', str(origin), 'rev-parse', 'HEAD'], text=True
    ).strip()
    dirty = subprocess.check_output(
        ['git', '-C', str(origin), 'status', '--porcelain'], text=True
    ).strip()
    if revision != package['rev'] or dirty:
        raise SystemExit(
            f'dependency cache is not clean at the pinned revision: {origin}'
        )
    destination = packages / package['name']
    if destination.exists():
        raise SystemExit(f'refusing to replace {destination}')
    if platform.system() == 'Darwin':
        subprocess.run(['cp', '-cR', str(origin), str(destination)], check=True)
    else:
        shutil.copytree(origin, destination, symlinks=True)
    print(f'seeded {package["name"]} at {revision}', flush=True)
