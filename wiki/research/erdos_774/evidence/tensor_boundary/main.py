"""Check the exact bounded certificate for S_3 tensor S_4 tensor S_3.

The checks are: the three base colors of the fixed 3-by-4 layer coloring
have signed-span intersection sizes 81, 7, 1 (twice) and 81, 17, 1 across
the three S_3 layers, so each color is dissociated; the three tensor color
classes have twelve columns each and the third lies in a rational
hyperplane; and the twelve automorphic colorings in the certificate are
proper, move a class off a class of the original coloring, and have
third-class normals of rank twelve. Nine base layers are enumerated with
3**4 = 81 signed sums each; no enumeration of 3**36 tensor coefficients is
used. Arithmetic is exact integer and rational arithmetic; no search runs.

Run from the repository root:
    uv run --no-sync python wiki/research/erdos_774/evidence/tensor_boundary/main.py

Dependencies are the standard library and the installed root ``tools``
package. There are no file inputs, output files, random choices or reduced
modes. Expected runtime is under a second. Failed obligations exit nonzero,
including under ``python -O``. The disjointness-connected hyperplane
argument that turns these checks into the exclusion of anchors after every
exact ternary-relation-preserving encoding is on the owning page.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from itertools import product

import tools

__all__ = [
    'main',
]

# fix the simplex columns and the three-layer coloring of the 3-by-4 base
_S3 = ((1, 0), (0, 1), (-1, -1))
_S4 = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, -1, -1))
_LAYERS = (
    ((2, 1, 3), (3, 1, 2), (3, 2, 1), (1, 3, 2)),
    ((1, 3, 2), (3, 2, 1), (3, 1, 2), (2, 1, 3)),
    ((1, 3, 2), (2, 1, 3), (2, 1, 3), (3, 2, 1)),
)

# retain twelve automorphic colorings; each last pair is (original color, new color)
_CERTIFICATE = (
    ((0, 1, 2), (0, 1, 2, 3), (0, 1, 2), (0, 1)),
    ((0, 1, 2), (0, 3, 2, 1), (0, 2, 1), (0, 1)),
    ((0, 1, 2), (1, 0, 3, 2), (0, 1, 2), (1, 1)),
    ((0, 1, 2), (2, 1, 3, 0), (2, 1, 0), (1, 0)),
    ((0, 1, 2), (3, 1, 0, 2), (2, 1, 0), (0, 1)),
    ((0, 1, 2), (3, 2, 1, 0), (0, 2, 1), (1, 1)),
    ((1, 0, 2), (0, 1, 3, 2), (0, 2, 1), (0, 0)),
    ((1, 0, 2), (0, 1, 3, 2), (2, 1, 0), (2, 2)),
    ((1, 0, 2), (0, 2, 1, 3), (0, 2, 1), (0, 0)),
    ((1, 0, 2), (0, 2, 3, 1), (2, 1, 0), (0, 1)),
    ((1, 0, 2), (1, 0, 2, 3), (2, 1, 0), (1, 2)),
    ((1, 0, 2), (1, 0, 3, 2), (0, 2, 1), (1, 1)),
)

# fix the expected intersection sizes and the third-class normal vector
_SIZES = [[81, 7, 1], [81, 7, 1], [81, 17, 1]]
_NORMAL = (0, 0, 0, 0, 0, 0, 0, 0, 1, -1, -1, 1)


def _dot(a: tuple[int, ...], b: tuple[int, ...]) -> int:
    """Return the integer dot product."""
    return sum(x * y for x, y in zip(a, b))


def _signed_sums(vectors: list[tuple[int, ...]]) -> set[tuple[int, ...]]:
    """Return all signed sums of a vector list."""
    dimension = len(vectors[0])
    return {
        tuple(sum(e[t] * vectors[t][a] for t in range(len(vectors))) for a in range(dimension))
        for e in product((-1, 0, 1), repeat=len(vectors))
    }


def _rank(rows: list[tuple[int, ...]]) -> int:
    """Return the rational rank by exact elimination."""
    matrix = [list(map(Fraction, row)) for row in rows]
    pivot = 0
    for column in range(len(matrix[0])):
        found = next((j for j in range(pivot, len(matrix)) if matrix[j][column]), None)
        if found is None:
            continue
        matrix[pivot], matrix[found] = matrix[found], matrix[pivot]
        divisor = matrix[pivot][column]
        matrix[pivot] = [x / divisor for x in matrix[pivot]]
        for j in range(pivot + 1, len(matrix)):
            multiplier = matrix[j][column]
            matrix[j] = [x - multiplier * y for x, y in zip(matrix[j], matrix[pivot])]
        pivot += 1
        if pivot == len(matrix):
            break
    return pivot


def main() -> int:
    """Run every finite obligation and return the shared checker's exit code."""
    # parse the fixed-domain interface and check the base layer criterion
    parser = tools.evidence_parser('Check the S_3 x S_4 x S_3 boundary certificate.', quick=False)
    parser.parse_args()
    checker = tools.Checker()
    base = {(i, j): tuple(a * b for a in _S3[i] for b in _S4[j]) for i, j in product(range(3), range(4))}
    sizes = []
    layer_failures = 0
    for color in (1, 2, 3):
        intersection = None
        counts = []
        for layer in _LAYERS:
            vectors = [base[i, j] for i, j in base if layer[j][i] == color]
            if len(vectors) != 4:
                layer_failures += 1
            sums = _signed_sums(vectors)
            if len(sums) != 81:
                layer_failures += 1
            intersection = sums if intersection is None else intersection & sums
            counts.append(len(intersection))
        if intersection != {(0,) * 6}:
            layer_failures += 1
        sizes.append(counts)
    checker.check('every base color has four columns per layer with 81 distinct signed sums', layer_failures == 0)
    checker.check('base color intersection sizes are as recorded', sizes == _SIZES, f'observed {sizes}')

    # form the tensor classes and check the rational hyperplane of the third class
    keys = tuple(product(range(3), range(4), range(3)))
    vectors = {(i, j, k): tuple(a * b * c for a in _S3[i] for b in _S4[j] for c in _S3[k]) for i, j, k in keys}
    classes = tuple({(i, j, k) for i, j, k in keys if _LAYERS[k][j][i] == color} for color in (1, 2, 3))
    checker.check('three tensor classes of twelve columns', list(map(len, classes)) == [12, 12, 12])
    checker.check('the third class lies in the recorded hyperplane', all(_dot(_NORMAL, vectors[key]) == 0 for key in classes[2]))
    evaluation = {key: _dot(_NORMAL, vectors[key]) for key in keys}

    # check the twelve automorphic colorings and the rank of their normals
    normals = []
    certificate_failures = 0
    for p, q, r, (original_color, new_color) in _CERTIFICATE:
        transformed = tuple({(p[i], q[j], r[k]) for i, j, k in color} for color in classes)
        if classes[original_color] & transformed[new_color]:
            certificate_failures += 1
        ip = {p[i]: i for i in range(3)}
        iq = {q[j]: j for j in range(4)}
        ir = {r[k]: k for k in range(3)}
        new_normal = tuple(evaluation[ip[i], iq[j], ir[k]] for i, j, k in product(range(2), range(3), range(2)))
        if not all(_dot(new_normal, vectors[key]) == 0 for key in transformed[2]):
            certificate_failures += 1
        normals.append(new_normal)
    checker.check('each automorphic coloring is disjoint from an original class and keeps its hyperplane', certificate_failures == 0)
    normal_rank = _rank(normals)
    checker.check('the twelve third-class normals have rank twelve', normal_rank == 12, f'observed {normal_rank}')
    print(f'base color intersection sizes: {sizes}; third-class normal rank: {normal_rank}')
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
