"""Exact weighted-count certificates for bad list assignments on complete bipartite graphs.

A list assignment on the complete bipartite graph with left lists ``left`` and
right lists ``right`` (subsets of the palette ``{0,...,n-1}``) is bad when every
palette subset ``T`` misses some left list or contains some right list; a proper
list colouring exists exactly when some ``T`` meets every left list and contains
no right list (left vertices take colours in ``T``, right vertices outside it).

The two fixed left lists are ``A1 = {0,...,k-1}`` and ``A2 = {k,...,2k-1}``; the
remaining colours form ``W``. A weighting gives every subset ``T`` meeting both
``A1`` and ``A2`` the integer weight ``w(|T cap A1|, |T cap A2|, |T cap W|)``.
The left event weight of a list ``X`` is the total weight of the subsets
disjoint from ``X``, and its right event weight is the total weight of the
subsets containing ``X``. All sums are exact integers, computed over every
palette subset by subset- and superset-sum transforms.
"""

from __future__ import annotations

import itertools
from math import comb

import numpy as np

__all__ = [
    'assignment_masks',
    'mask',
    'is_bad',
    'colouring_subset',
    'profiles',
    'weight_vector',
    'event_weights',
    'split_bound',
]


def assignment_masks(data: dict) -> tuple[int, int, list[int], list[int]]:
    """Validate a complete bipartite list assignment and return its masks.

    Vertices are list occurrences on the two nonempty sides; repeated lists
    at different vertices are allowed. Each list itself must be a set of k
    distinct colours in the stated palette. This is a finite witness-checking
    domain (at most 20 colours), not a reduction for arbitrary graphs.
    """
    n, k = data['colours'], data['list_size']
    if type(n) is not int or type(k) is not int or not 1 <= k <= n <= 20:
        raise ValueError('require integer palette and list sizes 1 <= k <= n <= 20')
    sides = []
    for side in ('left', 'right'):
        lists = data[side]
        if not isinstance(lists, list) or not lists:
            raise ValueError('each side must be a nonempty list of lists')
        masks = []
        for colours in lists:
            if not isinstance(colours, list) or len(colours) != k:
                raise ValueError('wrong list size')
            if any(type(c) is not int or not 0 <= c < n for c in colours):
                raise ValueError('colour outside the palette or not an integer')
            if len(set(colours)) != k:
                raise ValueError('repeated colour in a list')
            masks.append(mask(colours))
        sides.append(masks)
    return n, k, sides[0], sides[1]


def mask(colours: list[int] | tuple[int, ...]) -> int:
    """Return the bit mask of a list of colours."""
    return sum(1 << c for c in colours)


def colouring_subset(left: list[int], right: list[int], n: int) -> int | None:
    """Return the least subset ``T`` meeting every left mask and containing no right mask, if any."""
    full = (1 << n) - 1
    for T in range(1 << n):
        if all(A & T for A in left) and all(B & ~T & full for B in right):
            return T
    return None


def is_bad(left: list[int], right: list[int], n: int) -> bool:
    """Return whether every palette subset misses a left mask or contains a right mask."""
    return colouring_subset(left, right, n) is None


def profiles(n: int, k: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return the arrays ``|T cap A1|``, ``|T cap A2|``, ``|T cap W|`` indexed by every subset ``T``."""
    a1 = (1 << k) - 1
    a2 = a1 << k
    w = ((1 << n) - 1) & ~(a1 | a2)
    idx = np.arange(1 << n, dtype=np.int64)
    counts = []
    for part in (a1, a2, w):
        bits = idx & part
        c = np.zeros(1 << n, dtype=np.int64)
        for i in range(n):
            c += (bits >> i) & 1
        counts.append(c)
    return counts[0], counts[1], counts[2]


def weight_vector(rows: list[list[int]], n: int, k: int) -> np.ndarray:
    """Return the weight of every subset ``T`` from rows ``[t1, t2, t3, weight]``.

    Raises ``ValueError`` for a row outside the domain: a profile with ``t1`` or
    ``t2`` zero (such a subset misses a fixed left list), a profile that does not
    exist, a repeated profile, or a negative or non-integer weight.
    """
    if not (isinstance(n, int) and isinstance(k, int) and 1 <= k and 2 * k <= n <= 20):
        raise ValueError('require integers 1 <= k, 2*k <= n <= 20')
    seen = set()
    total = 0
    for row in rows:
        if len(row) != 4 or not all(isinstance(x, int) and not isinstance(x, bool) for x in row):
            raise ValueError(f'malformed row {row}')
        p1, p2, p3, wt = row
        if not (1 <= p1 <= k and 1 <= p2 <= k and 0 <= p3 <= n - 2 * k):
            raise ValueError(f'profile {row[:3]} outside t1,t2 in [1,{k}], t3 in [0,{n - 2 * k}]')
        if wt < 0:
            raise ValueError(f'negative weight in {row}')
        if (p1, p2, p3) in seen:
            raise ValueError(f'repeated profile {row[:3]}')
        seen.add((p1, p2, p3))
        # Bound the sum with Python integers BEFORE conversion to int64.
        # Every intermediate of either nonnegative zeta transform is at most
        # this total. Checking wv.sum() after conversion would be too late.
        total += comb(k, p1) * comb(k, p2) * comb(n - 2 * k, p3) * wt
    if total > np.iinfo(np.int64).max:
        raise ValueError('total weight too large for exact int64 sums')
    t1, t2, t3 = profiles(n, k)
    wv = np.zeros(1 << n, dtype=np.int64)
    for p1, p2, p3, wt in rows:
        wv[(t1 == p1) & (t2 == p2) & (t3 == p3)] = wt
    return wv


def event_weights(wv: np.ndarray, n: int, lists: list[int]) -> tuple[list[int], list[int]]:
    """Return the left and right event weights of each mask in ``lists``.

    Left: total weight of subsets disjoint from the mask. Right: total weight of
    subsets containing it. Exact int64 arithmetic; the caller bounds the total.
    """
    full = (1 << n) - 1
    idx = np.arange(1 << n, dtype=np.int64)
    sub = wv.copy()  # sub[S] = sum of wv[T] over T inside S
    sup = wv.copy()  # sup[S] = sum of wv[T] over T containing S
    for i in range(n):
        bit = 1 << i
        on = (idx & bit) != 0
        sub[on] += sub[idx[on] ^ bit]
        off = ~on
        sup[off] += sup[idx[off] | bit]
    return [int(sub[full & ~X]) for X in lists], [int(sup[X]) for X in lists]


def split_bound(rows: list[list[int]], n: int, k: int, left: int, right: int) -> tuple[int, int, int, int]:
    """Return ``(Z, maxL, maxR, bound)`` for one weighting and side split.

    ``Z`` is the total weight; ``maxL`` and ``maxR`` are the largest left and right
    event weights over all ``k``-subsets other than ``A1`` and ``A2``;
    ``bound = (left - 2) * maxL + right * maxR``. The weighting certifies that no
    bad assignment with distinct lists contains ``A1`` and ``A2`` among ``left``
    left lists and ``right`` right lists exactly when ``bound < Z``.
    """
    wv = weight_vector(rows, n, k)
    Z = int(wv.sum())
    if Z * (left + right) >= 2 ** 62:
        raise ValueError('weights too large for exact int64 sums')
    a1 = (1 << k) - 1
    a2 = a1 << k
    others = [mask(c) for c in itertools.combinations(range(n), k) if mask(c) not in (a1, a2)]
    lw, rw = event_weights(wv, n, others)
    maxL, maxR = max(lw), max(rw)
    return Z, maxL, maxR, (left - 2) * maxL + right * maxR
