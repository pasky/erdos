"""Triangle-free Cayley graphs on finite abelian groups.

Every finite abelian group is isomorphic to a product of cyclic groups
Z_{d_1} x ... x Z_{d_k} with 2 <= d_1 <= ... <= d_k; listing every such
nondecreasing factorization of n covers every abelian group of order n,
some more than once. For a symmetric connection set S not containing 0, the
Cayley graph joins x and x + s for s in S. It is triangle-free exactly when
S is sum-free: a triangle x, x + a, x + a + b with a, b and -(a + b) in S
needs a + b in -S = S.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product

import numpy as np


def abelian_groups(n: int) -> list[tuple[int, ...]]:
    """Return every nondecreasing factorization of n into factors at least 2."""

    def split(m: int, least: int):
        if m == 1:
            yield ()
            return
        for d in range(least, m + 1):
            if m % d == 0:
                for rest in split(m // d, d):
                    yield (d,) + rest

    return sorted(set(split(n, 2)))


def band_connection_sets(factors: tuple[int, ...], low, high):
    """Yield every symmetric sum-free connection set S with low <= |S| / n <= high.

    Yields (elements, S) with S a sorted tuple of element indices.
    """
    elements = list(product(*[range(f) for f in factors]))
    index = {e: i for i, e in enumerate(elements)}
    n = len(elements)
    zero = tuple(0 for _ in factors)

    def add(a, b):
        return tuple((x + y) % f for x, y, f in zip(a, b, factors))

    def negate(a):
        return tuple((-x) % f for x, f in zip(a, factors))

    classes, seen = [], set()
    for e in elements:
        if e == zero or e in seen:
            continue
        pair = {e, negate(e)}
        seen |= pair
        classes.append(sorted(pair))
    for r in range(1, len(classes) + 1):
        for chosen in combinations(classes, r):
            members = [e for pair in chosen for e in pair]
            if not low <= Fraction(len(members), n) <= high:
                continue
            members_set = set(members)
            if any(add(a, b) in members_set for a in members for b in members):
                continue
            yield elements, tuple(sorted(index[e] for e in members))


def cayley_adjacency(factors: tuple[int, ...], connection: tuple[int, ...]) -> np.ndarray:
    """Return the adjacency matrix of the Cayley graph with a connection set of element indices."""
    elements = list(product(*[range(f) for f in factors]))
    index = {e: i for i, e in enumerate(elements)}
    adjacency = np.zeros((len(elements), len(elements)), dtype=np.int64)
    for x in elements:
        for s in connection:
            y = tuple((a + b) % f for a, b, f in zip(x, elements[s], factors))
            adjacency[index[x], index[y]] = 1
    return adjacency


def proposed_cut(adjacency: np.ndarray, rng: np.random.Generator, restarts: int = 60) -> np.ndarray:
    """Return a cut (side of every vertex) from a seeded local search; only a proposal."""
    n = len(adjacency)
    best, best_cost = None, None
    for _ in range(restarts):
        s = rng.choice([-1, 1], n)
        while True:
            gain = (adjacency @ s) * s
            i = int(np.argmax(gain))
            if gain[i] <= 0:
                break
            s[i] = -s[i]
        cost = uncut_edges(adjacency, (s > 0).astype(np.int64))
        if best_cost is None or cost < best_cost:
            best, best_cost = (s > 0).astype(np.int64), cost
    if best is None:
        raise ValueError('no restarts')
    return best


def uncut_edges(adjacency: np.ndarray, side: np.ndarray) -> int:
    """Return the number of edges whose ends lie on the same side."""
    same = side[:, None] == side[None, :]
    return int((adjacency * same).sum() // 2)
