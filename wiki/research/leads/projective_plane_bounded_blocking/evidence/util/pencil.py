"""Lines missing plane curves in PG(2, p) and the pencil counts N_P.

Points and lines of PG(2, p), p an odd prime, are normalized homogeneous
triples over Z/p: (x, y, 1), (x, 1, 0) and (1, 0, 0). A point (X, Y, Z) lies
on the line [a, b, c] exactly when aX + bY + cZ = 0 mod p. A conic is a
symmetric 3 x 3 matrix A with nonzero determinant, and v lies on it when
v^T A v = 0 mod p. ``curve_pencil_counts`` handles any curve given by a form
evaluated on integer arrays, with exact integer arithmetic reduced mod p;
the index of the point (x, y, 1) is x p + y, of (x, 1, 0) is p^2 + x, and of
(1, 0, 0) is p^2 + p.
"""

from __future__ import annotations

import random
from collections.abc import Callable

import numpy as np

__all__ = [
    'Plane',
    'curve_pencil_counts',
    'diagonal_conic',
    'missed_lines',
    'pencil_counts',
    'random_conics',
]


class Plane:
    """The points of PG(2, p) and, for each line, the indices of its points."""

    def __init__(self: Plane, p: int) -> None:
        """Enumerate the points and the point lists of all lines."""
        # points and lines share the normalized representation
        self.p = p
        self.points = [(x, y, 1) for x in range(p) for y in range(p)] + [(x, 1, 0) for x in range(p)] + [(1, 0, 0)]
        self.lines = list(self.points)
        # incidence lists in both directions
        self.on_line = [[i for i, (x, y, z) in enumerate(self.points) if (a * x + b * y + c * z) % p == 0] for a, b, c in self.lines]
        self.through = [[] for _ in self.points]
        for j, pts in enumerate(self.on_line):
            for i in pts:
                self.through[i].append(j)


def _det(a: list[list[int]], p: int) -> int:
    """Return the determinant of a 3 x 3 matrix modulo p."""
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    ) % p


def _scaled(a: list[list[int]], p: int) -> tuple[int, ...]:
    """Return the matrix entries scaled so that the first nonzero entry is one."""
    flat = [a[i][j] for i in range(3) for j in range(3)]
    lead = next(v for v in flat if v)
    inv = pow(lead, p - 2, p)
    return tuple(v * inv % p for v in flat)


def random_conics(p: int, m: int, seed: int) -> list[list[list[int]]]:
    """Return m distinct nondegenerate conics from a seeded generator."""
    rng = random.Random(seed)
    out, seen = [], set()
    while len(out) < m:
        a = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(i, 3):
                a[i][j] = a[j][i] = rng.randrange(p)
        if _det(a, p) and _scaled(a, p) not in seen:
            seen.add(_scaled(a, p))
            out.append(a)
    return out


def diagonal_conic(p: int, a: int, b: int, c: int) -> list[list[int]]:
    """Return the conic a X^2 + b Y^2 + c Z^2 = 0."""
    return [[a % p, 0, 0], [0, b % p, 0], [0, 0, c % p]]


def _on(a: list[list[int]], v: tuple[int, int, int], p: int) -> bool:
    """Return whether v lies on the conic a."""
    return sum(a[i][j] * v[i] * v[j] for i in range(3) for j in range(3)) % p == 0


def missed_lines(plane: Plane, conics: list[list[list[int]]]) -> tuple[set[int], set[int]]:
    """Return the indices of the points on the union and of the lines missing it."""
    p = plane.p
    on_y = {i for i, v in enumerate(plane.points) if any(_on(a, v, p) for a in conics)}
    missed = {j for j, pts in enumerate(plane.on_line) if not any(i in on_y for i in pts)}
    return on_y, missed


def pencil_counts(plane: Plane, on_y: set[int], missed: set[int]) -> dict[int, int]:
    """Return N_P, the number of missed lines through P, for every point P off the union."""
    return {i: sum(1 for j in plane.through[i] if j in missed) for i in range(len(plane.points)) if i not in on_y}


def _normalized_index(v: np.ndarray, p: int, inv: np.ndarray) -> np.ndarray:
    """Return the point indices of the nonzero homogeneous vectors in the rows of v."""
    x, y, z = v[..., 0] % p, v[..., 1] % p, v[..., 2] % p
    iz, iy = inv[z], inv[y]
    affine = (x * iz % p) * p + y * iz % p
    infinite = np.where(y != 0, p * p + x * iy % p, p * p + p)
    return np.where(z != 0, affine, infinite)


def curve_pencil_counts(p: int, form: Callable[[np.ndarray, np.ndarray, np.ndarray], np.ndarray]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return the points, the mask of points on the curve form = 0, and N_P for every point.

    N_P counts the lines through the point that contain no rational point of
    the curve; it is returned for every point, and is meaningful off the curve.
    """
    # points, which are also the lines, and inverses mod p
    xs, ys = np.meshgrid(np.arange(p), np.arange(p), indexing='ij')
    affine = np.stack([xs.ravel(), ys.ravel(), np.ones(p * p, dtype=np.int64)], axis=1)
    infinite = np.stack([np.arange(p), np.ones(p, dtype=np.int64), np.zeros(p, dtype=np.int64)], axis=1)
    pts = np.concatenate([affine, infinite, np.array([[1, 0, 0]])]).astype(np.int64)
    inv = np.array([0] + [pow(a, p - 2, p) for a in range(1, p)], dtype=np.int64)
    on_y = form(pts[:, 0], pts[:, 1], pts[:, 2]) % p == 0
    # a line is hit when it passes through a rational point of the curve
    hit = np.zeros(len(pts), dtype=bool)
    for q in pts[on_y]:
        hit |= (pts @ q) % p == 0
    lines = pts[~hit]
    # Accumulate the p + 1 points of each missed line in bounded batches;
    # materializing every parametrized line at once uses cubic storage.
    t = np.arange(p)
    counts = np.zeros(len(pts), dtype=np.int64)
    for start in range(0, len(lines), 256):
        batch = lines[start : start + 256]
        a, b, c = batch[:, 0:1], batch[:, 1:2], batch[:, 2:3]
        one, zero = np.ones_like(a * t), np.zeros_like(a * t)
        # type [a, b, 1]: (1, t, -(a + b t)) and (0, 1, -b)
        gen1 = np.stack([one, one * t, -(a + b * t)], axis=-1)
        extra1 = np.stack([zero[:, 0], one[:, 0], -b[:, 0]], axis=-1)
        # type [a, 1, 0]: (1, -a, t) and (0, 0, 1)
        gen2 = np.stack([one, -a * one, one * t], axis=-1)
        extra2 = np.stack([zero[:, 0], zero[:, 0], one[:, 0]], axis=-1)
        # type [1, 0, 0]: (0, 1, t) and (0, 0, 1)
        gen3 = np.stack([zero, one, one * t], axis=-1)
        kind = np.where(c[:, 0] == 1, 1, np.where(b[:, 0] == 1, 2, 3))
        gen = np.where((kind == 1)[:, None, None], gen1, np.where((kind == 2)[:, None, None], gen2, gen3))
        extra = np.where((kind == 1)[:, None], extra1, extra2)
        idx = np.concatenate([_normalized_index(gen, p, inv).ravel(), _normalized_index(extra, p, inv)])
        counts += np.bincount(idx, minlength=len(pts))
    return pts, on_y, counts
