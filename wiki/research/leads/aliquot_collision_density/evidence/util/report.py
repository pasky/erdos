"""Build, run and parse the compiled collision census.

``build`` compiles ``census.cpp`` with the system C++ compiler, ``run``
executes it on a list of checkpoints, and ``parse`` turns its line report
into dictionaries keyed like those of ``brute.census``.
"""

from __future__ import annotations

import shutil
import subprocess
from math import isqrt
from pathlib import Path

__all__ = [
    'build',
    'checkpoints',
    'parse',
    'run',
]

_SOURCE = Path(__file__).resolve().parent / 'census.cpp'


def checkpoints(top_exponent: int) -> list[int]:
    """Return the checkpoints floor(10^(3 + j/4)) for j = 0, ..., 4(top - 3)."""
    out = []
    for j in range(4 * (top_exponent - 3) + 1):
        q, r = divmod(j, 4)
        # floor of (10^(4(3 + q) + r))^(1/4), by two exact integer square roots
        out.append(isqrt(isqrt(10 ** (4 * (3 + q) + r))))
    return out


def build(outdir: Path) -> Path:
    """Compile ``census.cpp`` into ``outdir`` and return the executable path."""
    compiler = shutil.which('c++') or shutil.which('clang++') or shutil.which('g++')
    if compiler is None:
        raise RuntimeError('no C++ compiler on PATH')
    outdir.mkdir(parents=True, exist_ok=True)
    exe = outdir / 'census'
    subprocess.run(  # noqa: S603 -- compile the local source with an argv list
        [compiler, '-O2', '-std=c++17', '-o', str(exe), str(_SOURCE)],
        check=True,
    )
    return exe


def run(
    exe: Path, workdir: Path, wbits: int, xs: list[int], hist_js: list[int], mode: int
) -> str:
    """Run the census and return its report text."""
    workdir.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(  # noqa: S603 -- execute the locally built census
        [
            str(exe),
            str(workdir),
            str(wbits),
            ','.join(str(x) for x in xs),
            ','.join(str(j) for j in hist_js),
            str(mode),
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise RuntimeError(
            f'census exited {result.returncode}: {result.stderr.strip()}'
        )
    return result.stdout


def parse(text: str) -> dict[str, object]:
    """Parse a census report into dictionaries keyed like ``brute.census``."""
    out_r: dict[tuple[str, int], int] = {}
    out_c: dict[tuple[str, int], int] = {}
    out_h: dict[tuple[int, str, int], int] = {}
    primes: dict[int, int] = {}
    omega2: dict[int, int] = {}
    meta: dict[str, int] = {}
    xs: list[int] = []
    ended = False
    for line in text.splitlines():
        parts = line.split()
        tag = parts[0]
        if tag == 'X':
            xs = [int(v) for v in parts[2:]]
        elif tag in ('RECORDS', 'MAXS', 'CLIPPED', 'MAXRUN', 'WBITS', 'MODE'):
            meta[tag] = int(parts[1])
        elif tag == 'PRIMES':
            primes[int(parts[1])] = int(parts[2])
        elif tag == 'OMEGA2':
            omega2[int(parts[1])] = int(parts[2])
        elif tag == 'R':
            out_r[parts[1], int(parts[2])] = int(parts[3])
        elif tag == 'C':
            out_c[parts[1], int(parts[2])] = int(parts[3])
        elif tag == 'H':
            out_h[int(parts[1]), parts[2], int(parts[3])] = int(parts[4])
        elif tag == 'END':
            ended = True
        else:
            raise ValueError(f'unknown report line: {line}')
    if not ended:
        raise ValueError('census report has no END line')
    return {
        'X': xs,
        'R': out_r,
        'C': out_c,
        'H': out_h,
        'PRIMES': primes,
        'OMEGA2': omega2,
        'META': meta,
    }
