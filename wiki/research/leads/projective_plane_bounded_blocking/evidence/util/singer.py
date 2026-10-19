"""Singer cycles of PG(2, p) and point sets invariant under their subgroups.

For a prime p and a cubic x^3 = a x^2 + b x + c over F_p, let w be a root.
When the classes of 1, w, w^2, ... modulo F_p^* run through all
N = p^2 + p + 1 points of PG(2, p) before repeating, the vector of w^i in the
basis 1, w, w^2 is a point P_i, and i -> i + 1 is a collineation of order N
(a Singer cycle). The line of points with trace zero is the planar
difference set D = {i : Tr(w^i) = 0}, and every line is D + t. For M | N the
subgroup of order N/M has the residue classes modulo M as point orbits, and
a union of classes r in K meets D + t in sum_{r in K} mu(r - t) points, where
mu(a) counts the elements of D congruent to a modulo M.
"""

from __future__ import annotations

__all__ = [
    'class_union',
    'cover_search',
    'difference_set',
    'histogram',
    'singer_cubic',
    'singer_points',
]


def _step(u: tuple[int, int, int], cubic: tuple[int, int, int], p: int) -> tuple[int, int, int]:
    """Multiply u0 + u1 w + u2 w^2 by w, using w^3 = a w^2 + b w + c."""
    a, b, c = cubic
    u0, u1, u2 = u
    return ((c * u2) % p, (u0 + b * u2) % p, (u1 + a * u2) % p)


def singer_points(p: int, cubic: tuple[int, int, int]) -> list[tuple[int, int, int]] | None:
    """Return P_0, ..., P_{N-1} when the cubic defines a Singer cycle, else None."""
    n = p * p + p + 1
    u = (1, 0, 0)
    seq = [u]
    for i in range(1, n + 1):
        u = _step(u, cubic, p)
        scalar = u[1] == 0 and u[2] == 0
        if scalar != (i == n):
            return None
        if i < n:
            seq.append(u)
    return seq


def singer_cubic(p: int) -> tuple[int, int, int]:
    """Return the first cubic (a, b, c), in lexicographic order with c != 0, giving a Singer cycle."""
    for a in range(p):
        for b in range(p):
            for c in range(1, p):
                if singer_points(p, (a, b, c)) is not None:
                    return (a, b, c)
    raise ValueError('no Singer cubic found')


def difference_set(p: int, cubic: tuple[int, int, int]) -> list[int]:
    """Return D = {i : Tr(w^i) = 0}, with Tr(1) = 3, Tr(w) = a, Tr(w^2) = a^2 + 2b."""
    a, b, _ = cubic
    tr = (3 % p, a % p, (a * a + 2 * b) % p)
    seq = singer_points(p, cubic)
    if seq is None:
        raise ValueError('cubic does not define a Singer cycle')
    return [i for i, u in enumerate(seq) if (tr[0] * u[0] + tr[1] * u[1] + tr[2] * u[2]) % p == 0]


def histogram(diff: list[int], m: int) -> list[int]:
    """Return mu(a) = |{d in D : d = a mod m}|."""
    mu = [0] * m
    for d in diff:
        mu[d % m] += 1
    return mu


def class_union(p: int, cubic: tuple[int, int, int], m: int, classes: list[int]) -> list[tuple[int, int, int]]:
    """Return the points P_i with i mod m in the given classes."""
    seq = singer_points(p, cubic)
    if seq is None:
        raise ValueError('cubic does not define a Singer cycle')
    keep = set(classes)
    return [u for i, u in enumerate(seq) if i % m in keep]


def cover_search(mu: list[int], cap: int, node_limit: int) -> tuple[list[int] | None, bool]:
    """Search exhaustively for K in Z_m, 0 in K, with 1 <= sum_{r in K} mu(r - t) <= cap for all t.

    Returns (K, True) for a solution, (None, True) when the search space is exhausted, and
    (None, False) when the node limit is reached. Fixing 0 in K loses nothing, since translating
    a solution gives a solution. The search branches on an uncovered class t with the fewest
    admissible covering classes r, and excludes each tried r from the later branches.
    """
    m = len(mu)
    sup = [a for a in range(m) if mu[a]]
    load = [0] * m
    state = [0] * m  # 0 undecided, 1 in K, 2 excluded
    nodes = 0

    def admissible(r: int) -> bool:
        return all(load[(r - a) % m] + mu[a] <= cap for a in sup)

    def apply(r: int, sign: int) -> None:
        for a in sup:
            load[(r - a) % m] += sign * mu[a]

    def dfs() -> list[int] | None:
        nonlocal nodes
        nodes += 1
        if nodes > node_limit:
            return None
        best_t, best = -1, None
        for t in range(m):
            if load[t]:
                continue
            cands = [(t + a) % m for a in sup if state[(t + a) % m] == 0 and admissible((t + a) % m)]
            if best is None or len(cands) < len(best):
                best_t, best = t, cands
                if not cands:
                    break
        if best_t < 0:
            return [r for r in range(m) if state[r] == 1]
        if not best:
            return None
        for r in best:
            state[r] = 1
            apply(r, 1)
            found = dfs()
            apply(r, -1)
            state[r] = 2
            if found is not None:
                for s in best:
                    state[s] = 0
                return found
        for s in best:
            state[s] = 0
        return None

    if not admissible(0):
        return None, True
    state[0] = 1
    apply(0, 1)
    found = dfs()
    return found, nodes <= node_limit
