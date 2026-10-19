"""Check the common-span rank of the seven-layer three-coloring of S_3 x S_5 x S_7.

Fixed test only: the explicit seven-layer partition of the 105 tensor
columns into three classes of 35, and the 96-by-105 matrix whose kernel is
the set of coefficient triples with equal signed sums in all three classes.
The checks are the class sizes (35, 35, 35), the matrix shape 96 by 105,
rank 83 and nullity 22. The original design allowed a ternary enumeration
of the free coefficients only when the nullity was at most 12; the nullity
exceeds that gate, so no enumeration runs and this probe decides nothing
about the common signed-span intersection. The algebraic cyclic-sum lemma
on the owning page supersedes this stopped route. Arithmetic is exact
rational elimination; no search runs.

Run from the repository root:
    uv run --no-sync python wiki/research/erdos_774/evidence/prime_reset_span/main.py

Dependencies are the standard library and the installed root ``tools``
package. There are no file inputs, output files, random choices or reduced
modes. Expected runtime is a few seconds. Failed obligations exit nonzero,
including under ``python -O``.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from itertools import product

import tools

__all__ = [
    'main',
]

# fix the enumeration gate the original test declared and the expected numbers
_GATE = 12
_CLASS_SIZES = [35, 35, 35]
_SHAPE = (96, 105)
_RANK = 83
_NULLITY = 22

# fix the S_5 relabeling used in the seven-layer coloring
_T = (0, 1, 2, 4, 3)


def _rref(rows: list[list[int]], n: int) -> tuple[list[list[Fraction]], list[int]]:
    """Return the reduced rows and pivot columns of an integer matrix."""
    a = [[Fraction(x) for x in row] for row in rows]
    pivots: list[int] = []
    k = 0
    for j in range(n):
        z = next((i for i in range(k, len(a)) if a[i][j]), None)
        if z is None:
            continue
        a[k], a[z] = a[z], a[k]
        d = a[k][j]
        a[k] = [x / d for x in a[k]]
        for i in range(len(a)):
            if i != k and a[i][j]:
                d = a[i][j]
                a[i] = [x - d * y for x, y in zip(a[i], a[k])]
        pivots.append(j)
        k += 1
        if k == len(a):
            break
    return a[:k], pivots


def _simplex(p: int) -> list[list[int]]:
    """Return the p simplex columns in dimension p-1."""
    return [[int(i == j) for i in range(p - 1)] for j in range(p - 1)] + [[-1] * (p - 1)]


def _tensor(*factors: list[int]) -> list[int]:
    """Return the tensor product of vectors."""
    out = [1]
    for x in factors:
        out = [a * b for a in out for b in x]
    return out


def main() -> int:
    """Run every finite obligation and return the shared checker's exit code."""
    # parse the fixed-domain interface and build the seven-layer coloring
    parser = tools.evidence_parser('Check the common-span rank of the seven-layer coloring.', quick=False)
    parser.parse_args()
    checker = tools.Checker()
    s3, s5, s7 = map(_simplex, (3, 5, 7))
    vectors: list[list[int]] = []
    classes: list[list[int]] = [[], [], []]
    for r, j, k in product(range(3), range(5), range(7)):
        c = (r + (j if k < 3 or k == 6 else _T[j]) + (k % 3 if k < 6 else 0)) % 3
        classes[c].append(len(vectors))
        vectors.append(_tensor(s3[r], s5[j], s7[k]))
    checker.check('class sizes are (35, 35, 35)', list(map(len, classes)) == _CLASS_SIZES, f'observed {list(map(len, classes))}')

    # form the equality matrix whose kernel has equal signed sums in all classes
    columns = []
    for c in range(3):
        for i in classes[c]:
            v = vectors[i]
            if c == 0:
                columns.append(v + v)
            elif c == 1:
                columns.append([-x for x in v] + [0] * 48)
            else:
                columns.append([0] * 48 + [-x for x in v])
    rows = [list(row) for row in zip(*columns)]
    checker.check('equality matrix is 96 by 105', (len(rows), len(rows[0])) == _SHAPE, f'observed {(len(rows), len(rows[0]))}')
    reduced, pivots = _rref(rows, 105)
    nullity = 105 - len(pivots)
    checker.check('rank is 83', len(pivots) == _RANK, f'observed {len(pivots)}')
    checker.check('nullity is 22', nullity == _NULLITY, f'observed {nullity}')
    checker.check('nullity exceeds the declared enumeration gate, so no enumeration runs', nullity > _GATE)
    print(f'rank {len(pivots)}, nullity {nullity}; ternary enumeration not run (gate {_GATE})')
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
