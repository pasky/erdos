"""Check the retained monochromatic relations against the binary checksum palette.

Over F_2[t], stage m has rows V_m x V_(2m), with V_j the polynomials of
degree at most j, encoded by their binary coefficient strings and numbered
x + 2^(m+1) y. Columns are the cosets of the slope-r lines {(x, r x)} for
every r of degree j <= m, restricted to x in V_j, together with the cosets of
the initial vertical direction {(0, a) : a in F_2}. The palette colors a
slope-r coset with representative (u, v) by L(v - r u) and a vertical coset
by L(u), where L(t^i) is the parity of the i-th Catalan number.

The input is ``assets/checksum_witnesses.json``: four eight-column witnesses,
one per color at stages one and two. The checks are that every listed column
is a genuine coset whose support and color match the palette, that the eight
supports of a witness are distinct, that its coefficients are +1 or -1, and
that the signed sum of its indicator columns is exactly zero. Arithmetic is
exact integer arithmetic; no solver runs. Discovery of the witnesses is the
separate ``produce.py`` beside this script.

Run from the repository root:
    uv run --no-sync python wiki/research/erdos_774/evidence/polynomial_checksum/main.py

Dependencies are the standard library and the installed root ``tools``
package. The only input is the asset beside this script; no output file is
written and there is no reduced mode. Expected runtime is under a second.
Failed obligations exit nonzero, including under ``python -O``. A
monochromatic relation against one palette is not a lower bound for
arbitrary colorings.
"""

from __future__ import annotations

import json
import math
import pathlib
import sys

import tools

__all__ = [
    'main',
]

# locate the retained witnesses relative to this script
_ASSET = pathlib.Path(__file__).with_name('assets') / 'checksum_witnesses.json'

# fix the expected stages, colors and witness size
_EXPECTED = {(1, 0), (1, 1), (2, 0), (2, 1)}
_WITNESS_SIZE = 8


def _mul(a: int, b: int) -> int:
    """Multiply two binary polynomials encoded as integers."""
    z = 0
    while b:
        if b & 1:
            z ^= a
        b >>= 1
        a <<= 1
    return z


def _checksum(a: int) -> int:
    """Return the Catalan-parity checksum of a binary polynomial."""
    z = 0
    j = 0
    while a:
        if a & 1:
            z ^= (math.comb(2 * j, j) // (j + 1)) & 1
        a >>= 1
        j += 1
    return z


def _column(m: int, r: int | None, j: int, rep: list[int]) -> tuple[list[int], int]:
    """Return the support and palette color of the coset with the given representative."""
    nx = 1 << (m + 1)
    u, v = rep
    if r is None:
        subgroup = [(0, a) for a in range(2)]
        color = _checksum(u)
    else:
        subgroup = [(a, _mul(r, a)) for a in range(1 << (j + 1))]
        color = _checksum(v ^ _mul(r, u))
    support = sorted((u ^ a) + nx * (v ^ b) for a, b in subgroup)
    return support, color


def main() -> int:
    """Run every finite obligation and return the shared checker's exit code."""
    # parse the fixed-domain interface and load the retained witnesses
    parser = tools.evidence_parser('Check the retained checksum witnesses.', quick=False)
    parser.parse_args()
    checker = tools.Checker()
    data = json.loads(_ASSET.read_text())
    witnesses = data['witnesses']
    checker.check(
        'one witness per color at stages one and two',
        {(w['m'], w['color']) for w in witnesses} == _EXPECTED and len(witnesses) == 4,
    )
    for witness in witnesses:
        m, color = witness['m'], witness['color']
        nx, ny = 1 << (m + 1), 1 << (2 * m + 1)
        label = f'stage {m} color {color}'
        columns = witness['columns']
        checker.check(f'{label}: eight columns', len(columns) == _WITNESS_SIZE, f'observed {len(columns)}')
        checker.check(f'{label}: row count {nx * ny}', witness['row_count'] == nx * ny)
        # check every column against the coset formula and the palette
        column_failures = 0
        for col in columns:
            r, j = col['r'], col['j']
            if r is not None and j != max(0, r.bit_length() - 1):
                column_failures += 1
                continue
            support, palette = _column(m, r, j, col['rep'])
            if support != col['support'] or palette != color:
                column_failures += 1
        checker.check(f'{label}: every column is a genuine coset of that color', column_failures == 0, f'{column_failures} failures')
        supports = [tuple(col['support']) for col in columns]
        checker.check(f'{label}: the eight supports are distinct', len(set(supports)) == len(supports))
        checker.check(f'{label}: coefficients are +1 or -1', all(col['coefficient'] in (1, -1) for col in columns))
        # check that the signed indicator sum vanishes on every row
        total = [0] * (nx * ny)
        for col in columns:
            for row in col['support']:
                total[row] += col['coefficient']
        checker.check(f'{label}: the signed sum of the columns is zero', not any(total))
    print('four retained eight-column monochromatic relations verified by exact integer sums')
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
