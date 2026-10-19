"""Exact checks of the rigid split-class example; not a counterexample to Erdos problem 132.

For m = 2..7, A_m is the grid {(i, (1+sqrt2) j) : 0 <= i, j < m} together with
w = (1/2, sqrt3/2). Numbers of Q(sqrt2, sqrt3) are kept as exact coefficient
tuples over the basis 1, sqrt2, sqrt3, sqrt6, which is linearly independent
over Q, so equal tuples are exactly equal squared distances. The probe checks
that the unit class is the only class whose pairs have unequal absolute
horizontal displacements, that the unit equilateral triangle gives two
independent equal-length tensors, and that the exact rare count R(A_m) is at
least (m^2 - 4m - 6)/4. It exits nonzero when any obligation fails.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations

Coeffs = tuple[F, ...]
Point = tuple[Coeffs, Coeffs]

# products of basis elements 1, sqrt2, sqrt3, sqrt6 as (coefficient, index)
_TABLE = {
    (0, 0): (1, 0),
    (0, 1): (1, 1),
    (0, 2): (1, 2),
    (0, 3): (1, 3),
    (1, 1): (2, 0),
    (1, 2): (1, 3),
    (1, 3): (2, 2),
    (2, 2): (3, 0),
    (2, 3): (3, 1),
    (3, 3): (6, 0),
}


def mul(x: Coeffs, y: Coeffs) -> Coeffs:
    """Multiply two coefficient tuples."""
    out = [F(0)] * 4
    for i in range(4):
        for j in range(4):
            if x[i] and y[j]:
                scale, index = _TABLE[(min(i, j), max(i, j))]
                out[index] += scale * x[i] * y[j]
    return tuple(out)


def sub(x: Coeffs, y: Coeffs) -> Coeffs:
    """Subtract two coefficient tuples."""
    return tuple(a - b for a, b in zip(x, y))


def rational(q: int | F) -> Coeffs:
    """Embed a rational number."""
    return (F(q), F(0), F(0), F(0))


def points(m: int) -> list[Point]:
    """Return the points of A_m as pairs of coefficient tuples."""
    grid = [(rational(i), (F(j), F(j), F(0), F(0))) for i in range(m) for j in range(m)]
    w = (rational(F(1, 2)), (F(0), F(0), F(1, 2), F(0)))
    return [*grid, w]


def check(m: int, failures: list[str]) -> tuple[int, int, int]:
    """Check the stated properties of A_m and return its exact rare count."""
    pts = points(m)
    n = len(pts)
    classes = defaultdict(list)
    for p, q in combinations(pts, 2):
        dx = sub(p[0], q[0])
        dy = sub(p[1], q[1])
        # every abscissa is rational, so dx has only a rational coefficient
        if any(dx[1:]):
            failures.append(f'm={m}: irrational horizontal displacement')
        square = tuple(a + b for a, b in zip(mul(dx, dx), mul(dy, dy)))
        classes[square].append(abs(dx[0]))
    unit = rational(1)
    split = [key for key, values in classes.items() if len(set(values)) > 1]
    if split != [unit]:
        failures.append(f'm={m}: split classes {split}')
    if sorted(set(classes[unit])) != [F(1, 2), F(1)]:
        failures.append(f'm={m}: unit class displacements {set(classes[unit])}')
    rare = sum(1 for values in classes.values() if len(values) <= n)
    if 4 * rare < m * m - 4 * m - 6:
        failures.append(f'm={m}: R={rare} below the bound')
    return n, len(classes), rare


def main() -> None:
    """Check the tensor rank and the six exact configurations."""
    failures: list[str] = []
    # the unit triangle's equal-length tensors: traceless parts (dx^2-dy^2, 2dxdy)
    half, root = rational(F(1, 2)), (F(0), F(0), F(1, 2), F(0))
    directions = [
        (rational(1), rational(0)),
        (half, root),
        (sub(rational(0), half), root),
    ]
    parts = [
        (sub(mul(x, x), mul(y, y)), mul(rational(2), mul(x, y))) for x, y in directions
    ]
    first = (sub(parts[0][0], parts[1][0]), sub(parts[0][1], parts[1][1]))
    second = (sub(parts[0][0], parts[2][0]), sub(parts[0][1], parts[2][1]))
    determinant = sub(mul(first[0], second[1]), mul(first[1], second[0]))
    if not any(determinant):
        failures.append('triangle tensors are dependent')
    for m in range(2, 8):
        n, distances, rare = check(m, failures)
        print(f'split-class example m={m}: n={n}, distances={distances}, R={rare}')
    if failures:
        for failure in failures:
            print('FAIL', failure)
        raise SystemExit(1)
    print('split-class example: all checks pass')


if __name__ == '__main__':
    main()
