"""Exact rows of unrooted k-root profile rules at mixtures of step graphons.

For a vertex-transitive graph H on n vertices, a labeled k-root type tau and
a rule c, the cut row at threshold t is

    g_H(tau, c) = Pr(tau) (E[mono(R, c) | tau] - t)
                = 2 S(tau, c) / n^(k+1) - t N(tau) / n^(k-1),

where S(tau, c) counts, over placements with first root 0, the edges whose
ends get the same side, and N(tau) counts those placements. A mixture of
density vectors with weights lambda_i has row value sum_i lambda_i g_i.

Rules are deterministic on every profile class or put the zero class (the
points adjacent to no root) on side 1 with probability q, for any q in
[0, 1]. Every other profile class is independent in a triangle-free graph,
so the cost is multilinear in the coins of the nonzero classes and its
minimum over them is attained by deterministic choices. All values are
exact rationals; integer arrays are bounded explicitly before use.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import lcm

import numpy as np

from util.envelopes import aggregated_tables, placement_blocks, type_codes

LIMIT = 1 << 62


def circulant(n: int, connection: set[int]) -> np.ndarray:
    """Return the circulant graph on Z/n with the given symmetric connection set."""
    return np.array([[int((v - u) % n in connection) for v in range(n)] for u in range(n)],
                    dtype=np.int64)


def component_tables(adjacency: np.ndarray, k: int) -> tuple[dict[int, Counter], Counter]:
    """Return profile-pair edge tables and placement counts for every labeled k-root type.

    Placements have first root 0; each table maps an unordered profile pair to
    the number of (placement, edge) incidences of that type.
    """
    n = len(adjacency)
    codes: set[int] = set()
    for roots in placement_blocks(n, k):
        codes.update(np.unique(type_codes(adjacency, roots)).tolist())
    blocks = ((roots, np.ones(len(roots), dtype=np.int64)) for roots in placement_blocks(n, k))
    return aggregated_tables(adjacency, blocks, codes)


def _scaled_type(components, weights, code: int, k: int, t: Fraction):
    """Return integer pair weights, the threshold term and the scale of one type."""
    values: dict[tuple[int, int], Fraction] = {}
    threshold = Fraction(0)
    for (n, tables, totals), weight in zip(components, weights):
        for pair, count in tables.get(code, Counter()).items():
            values[pair] = values.get(pair, Fraction(0)) + weight * Fraction(2 * count, n ** (k + 1))
        threshold += weight * t * Fraction(totals.get(code, 0), n ** (k - 1))
    scale = lcm(threshold.denominator, *(v.denominator for v in values.values()))
    integer = {pair: int(v * scale) for pair, v in values.items()}
    return integer, int(threshold * scale), scale


def deterministic_minimum(pairs: dict[tuple[int, int], int]) -> int:
    """Return the least cost over every deterministic rule on the profiles of the pairs."""
    nodes = sorted({x for pair in pairs for x in pair})
    if not nodes:
        return 0
    if len(nodes) > 20 or sum(pairs.values()) >= LIMIT:
        raise ValueError('table outside the exhaustive integer range')
    position = {v: i for i, v in enumerate(nodes)}
    masks = np.arange(1 << (len(nodes) - 1), dtype=np.int64) << 1
    cost = np.zeros(len(masks), dtype=np.int64)
    for (a, b), weight in pairs.items():
        cost += weight * ((((masks >> position[a]) ^ (masks >> position[b])) & 1) == 0)
    return int(cost.min())


def coin_minimum(pairs: dict[tuple[int, int], int], threshold: int) -> Fraction | None:
    """Return the least row value, times the scale, over rules with an interior zero-class coin.

    For a fixed assignment of the nonzero classes the cost is
    A q^2 + B q + C with A = 2 w(0, 0). Only assignments whose minimizing q
    lies strictly inside (0, 1) are new; the endpoints are deterministic rules.
    Returns None when no assignment has an interior minimizer.
    """
    zero_zero = pairs.get((0, 0), 0)
    if zero_zero == 0:
        return None
    nonzero = sorted({x for pair in pairs for x in pair} - {0})
    if len(nonzero) > 20 or sum(pairs.values()) >= LIMIT:
        raise ValueError('table outside the exhaustive integer range')
    position = {v: i for i, v in enumerate(nonzero)}
    masks = np.arange(1 << len(nonzero), dtype=np.int64)
    mono = np.zeros(len(masks), dtype=np.int64)
    linear = np.zeros(len(masks), dtype=np.int64)
    toward_zero = np.zeros(len(masks), dtype=np.int64)
    for (a, b), weight in pairs.items():
        if a == 0 and b == 0:
            continue
        if a == 0:
            side = (masks >> position[b]) & 1
            linear += weight * (2 * side - 1)
            toward_zero += weight * (1 - side)
        else:
            mono += weight * ((((masks >> position[a]) ^ (masks >> position[b])) & 1) == 0)
    a_term = 2 * zero_zero
    b_term = linear - 2 * zero_zero
    c_term = zero_zero + toward_zero + mono
    interior = (b_term < 0) & (-b_term < 2 * a_term)
    if not interior.any():
        return None
    b_exact = b_term[interior].astype(object)
    c_exact = c_term[interior].astype(object)
    numerator = 4 * a_term * (c_exact - threshold) - b_exact * b_exact
    return Fraction(int(numerator.min()), 4 * a_term)


def mixture_minimum(components, weights, k: int, t: Fraction) -> tuple[Fraction, int, bool]:
    """Return the least mixture row over all labeled k-root types and rules.

    ``components`` lists (n, tables, totals) from ``component_tables``. Returns
    the exact least value, the binding labeled code, and whether some
    interior zero-class coin is strictly cheaper than every deterministic
    rule of its type.
    """
    codes = sorted(set().union(*(set(totals) for _, _, totals in components)))
    best: Fraction | None = None
    best_code = -1
    coin_better = False
    for code in codes:
        pairs, threshold, scale = _scaled_type(components, weights, code, k, t)
        value = Fraction(deterministic_minimum(pairs) - threshold, scale)
        coin = coin_minimum(pairs, threshold)
        if coin is not None and coin / scale < value:
            coin_better = True
            value = coin / scale
        if best is None or value < best:
            best, best_code = value, code
    if best is None:
        raise ValueError('no root types in the mixture')
    return best, best_code, coin_better


def conditional_minima(n: int, tables: dict[int, Counter], totals: Counter) -> dict[int, Fraction]:
    """Return min over deterministic rules of E[mono | tau] for every labeled type."""
    return {code: Fraction(2 * deterministic_minimum(dict(tables[code])), totals[code] * n * n)
            for code in totals}
