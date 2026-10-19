"""Check one fixed 81-by-27 rational circuit among four-direction axis lines.

The input is ``assets/axis_line_circuit.json``: 27 full axis-parallel lines
of the box [3]^4, each with an integer coefficient. The checks are that the
27 lines are distinct, that the coefficients are nonzero with exactly one of
magnitude two and greatest common divisor one, that the signed combination
of the line indicators vanishes on all 81 points, and that the 81-by-27
incidence matrix has rank 26. Rank and full support prove that the support
is a rational circuit, and the primitive coefficient two proves that it is
dissociated. Arithmetic is exact rational elimination; no search runs.

Run from the repository root:
    uv run --no-sync python wiki/research/erdos_774/evidence/axis_line_circuit/main.py

Dependencies are the standard library and the installed root ``tools``
package. The only input is the asset beside this script; no output file is
written and there is no reduced mode. Expected runtime is under a second.
Failed obligations exit nonzero, including under ``python -O``.
"""

from __future__ import annotations

import json
import pathlib
import sys
from fractions import Fraction
from itertools import product
from math import gcd

import tools

__all__ = [
    'main',
]

# locate the retained certificate relative to this script
_ASSET = pathlib.Path(__file__).with_name('assets') / 'axis_line_circuit.json'


def _rank(rows: list[list[int]]) -> int:
    """Return the rational rank by exact elimination."""
    a = [[Fraction(x) for x in row] for row in rows]
    r = 0
    for j in range(len(a[0])):
        pivot = next((k for k in range(r, len(a)) if a[k][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        scale = a[r][j]
        a[r] = [x / scale for x in a[r]]
        for k in range(r + 1, len(a)):
            scale = a[k][j]
            if scale:
                a[k] = [x - scale * y for x, y in zip(a[k], a[r])]
        r += 1
    return r


def main() -> int:
    """Run every finite obligation and return the shared checker's exit code."""
    # parse the fixed-domain interface and load the retained circuit
    parser = tools.evidence_parser('Check the fixed four-direction axis-line circuit.', quick=False)
    parser.parse_args()
    checker = tools.Checker()
    data = json.loads(_ASSET.read_text())
    dims = data['dimensions']
    cols = data['columns']
    checker.check('the box is [3]^4 with 27 columns', dims == [3, 3, 3, 3] and len(cols) == 27)
    checker.check('the 27 lines are distinct', len({(c['axis'], tuple(c['fixed'])) for c in cols}) == 27)

    # build the incidence matrix and check the relation and its coefficients
    matrix = [
        [int(tuple(x[j] for j in range(4) if j != c['axis']) == tuple(c['fixed'])) for c in cols]
        for x in product(*(range(d) for d in dims))
    ]
    coefficients = [c['coefficient'] for c in cols]
    checker.check('all coefficients are nonzero with height two', all(coefficients) and max(map(abs, coefficients)) == 2)
    checker.check('exactly one coefficient has magnitude two', sum(abs(c) == 2 for c in coefficients) == 1)
    checker.check('the coefficient vector is primitive', gcd(*coefficients) == 1)
    checker.check('the signed combination vanishes on all 81 points', all(sum(a * b for a, b in zip(row, coefficients)) == 0 for row in matrix))
    rank = _rank(matrix)
    checker.check('the 81-by-27 matrix has rank 26', rank == 26, f'observed {rank}')
    print(f'rank {rank}; primitive full-support height-two kernel')
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
