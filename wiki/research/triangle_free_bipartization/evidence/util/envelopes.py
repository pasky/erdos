"""Exact helpers for k-root profile rules on equal-weight step graphons.

A graph H on n vertices gives the step graphon W_H. Roots are i.i.d. points;
a root in part r is recorded as the vertex r, so a placement is a tuple in
V(H)^k. Every point in part v has the profile sum_i 2^i [v ~ r_i]. A rule maps
profiles to sides; its cost is the number of edges of H whose two ends get
the same side, and its graphon monochromatic density is 2 * cost / n^2.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations

import numpy as np


def cycle(n: int) -> np.ndarray:
    """Return the adjacency matrix of the cycle C_n."""
    return np.array(
        [[int((u - v) % n in (1, n - 1)) for v in range(n)] for u in range(n)],
        dtype=np.int64,
    )


def petersen() -> np.ndarray:
    """Return the Petersen graph: 2-subsets of [5], adjacent when disjoint."""
    pairs = list(combinations(range(5), 2))
    return np.array(
        [[int(not set(a) & set(b)) for b in pairs] for a in pairs], dtype=np.int64
    )


def even_subsets() -> list[int]:
    """Return the even subsets of [5] as bit masks, in increasing order."""
    return [v for v in range(32) if bin(v).count('1') % 2 == 0]


def clebsch() -> np.ndarray:
    """Return the Clebsch graph: even subsets of [5], adjacent at distance 4."""
    subsets = even_subsets()
    return np.array(
        [[int(bin(u ^ v).count('1') == 4) for v in subsets] for u in subsets],
        dtype=np.int64,
    )


def golay_octads() -> tuple[list[tuple[int, ...]], np.ndarray]:
    """Return the 759 octads of the extended binary Golay code.

    The cyclic code of length 23 has generator polynomial
    1 + x^2 + x^4 + x^5 + x^6 + x^10 + x^11; a parity coordinate extends it.
    The caller checks dimension, minimum weight and the octad count.
    """
    gen = [0] * 23
    for degree in (0, 2, 4, 5, 6, 10, 11):
        gen[degree] = 1
    rows = []
    for shift in range(12):
        row = [0] * 23
        for degree in range(23):
            if gen[degree]:
                row[(degree + shift) % 23] = 1
        rows.append(row + [sum(row) % 2])
    matrix = np.array(rows, dtype=np.int64)
    coefficients = (np.arange(1 << 12)[:, None] >> np.arange(12)[None, :]) & 1
    words = (coefficients @ matrix) % 2
    return [tuple(np.nonzero(w)[0].tolist()) for w in words if w.sum() == 8], words


def higman_sims() -> tuple[np.ndarray, list[tuple[int, ...]]]:
    """Return the Higman-Sims graph from the Steiner system S(3,6,22).

    Vertex 0 is a point at infinity, vertices 1..22 the points and 23..99
    the 77 hexads (octads through Golay coordinates 22 and 23). Infinity is
    adjacent to every point, a point to the hexads containing it, and two
    hexads when they are disjoint.
    """
    octads, _ = golay_octads()
    hexads = [tuple(x for x in o if x < 22) for o in octads if 22 in o and 23 in o]
    adjacency = np.zeros((100, 100), dtype=np.int64)
    for point in range(22):
        adjacency[0, 1 + point] = adjacency[1 + point, 0] = 1
    for index, hexad in enumerate(hexads):
        for point in hexad:
            adjacency[1 + point, 23 + index] = adjacency[23 + index, 1 + point] = 1
    for i, j in combinations(range(len(hexads)), 2):
        if not set(hexads[i]) & set(hexads[j]):
            adjacency[23 + i, 23 + j] = adjacency[23 + j, 23 + i] = 1
    return adjacency, hexads


def edges_of(adjacency: np.ndarray) -> np.ndarray:
    """Return the edges u < v as an integer array of shape (e, 2)."""
    n = len(adjacency)
    return np.array(
        [(u, v) for u, v in combinations(range(n), 2) if adjacency[u, v]],
        dtype=np.int64,
    )


def is_triangle_free(adjacency: np.ndarray) -> bool:
    """Return whether no edge has a common neighbour."""
    square = adjacency @ adjacency
    return bool((square[adjacency == 1] == 0).all())


def is_automorphism(adjacency: np.ndarray, image: np.ndarray) -> bool:
    """Return whether the vertex map ``image`` is a bijective automorphism."""
    n = len(adjacency)
    return bool(
        sorted(image.tolist()) == list(range(n))
        and (adjacency[np.ix_(image, image)] == adjacency).all()
    )


def all_cut_costs(adjacency: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return every cut with vertex 0 on side 0 and its uncut-edge count."""
    n = len(adjacency)
    masks = np.arange(1 << (n - 1), dtype=np.int64) << 1
    cost = np.zeros(len(masks), dtype=np.int64)
    for u, v in edges_of(adjacency):
        cost += (((masks >> u) ^ (masks >> v)) & 1) == 0
    return masks, cost


def placement_blocks(n: int, k: int, first: int = 0, size: int = 1 << 18):
    """Yield, in blocks, every k-tuple of vertices whose first root is ``first``.

    Tuples are listed in base-n order of their last k - 1 roots.
    """
    total = n ** (k - 1)
    powers = n ** np.arange(k - 2, -1, -1, dtype=np.int64)
    for start in range(0, total, size):
        index = np.arange(start, min(total, start + size), dtype=np.int64)
        rest = (index[:, None] // powers[None, :]) % n
        head = np.full((len(index), 1), first, dtype=np.int64)
        yield np.concatenate([head, rest], axis=1)


def root_pairs(k: int) -> list[tuple[int, int]]:
    """Return the root pairs in the bit order of type codes."""
    return list(combinations(range(k), 2))


def type_codes(adjacency: np.ndarray, roots: np.ndarray) -> np.ndarray:
    """Return the labeled induced root type of each placement as a bit code."""
    code = np.zeros(len(roots), dtype=np.int64)
    for bit, (i, j) in enumerate(root_pairs(roots.shape[1])):
        code |= adjacency[roots[:, i], roots[:, j]] << bit
    return code


def profiles(adjacency: np.ndarray, roots: np.ndarray) -> np.ndarray:
    """Return the profile of every vertex for every placement."""
    result = np.zeros((len(roots), len(adjacency)), dtype=np.int64)
    for i in range(roots.shape[1]):
        result |= adjacency[:, roots[:, i]].T << i
    return result


def permuted_codes(codes: np.ndarray, k: int, perm: tuple[int, ...]) -> np.ndarray:
    """Relabel root i as perm[i] in every type code."""
    index = {pair: bit for bit, pair in enumerate(root_pairs(k))}
    out = np.zeros_like(codes)
    for bit, (i, j) in enumerate(root_pairs(k)):
        a, b = sorted((perm[i], perm[j]))
        out |= ((codes >> bit) & 1) << index[(a, b)]
    return out


def least_codes(codes: np.ndarray, k: int) -> np.ndarray:
    """Return the least code over all root relabelings of every code.

    The least code is the canonical labeled type of the type class.
    """
    least = codes.copy()
    for perm in permutations(range(k)):
        np.minimum(least, permuted_codes(codes, k, perm), out=least)
    return least


def labeled_versions(code: int, k: int) -> int:
    """Return the number of distinct labeled codes in the relabeling class of a code."""
    array = np.array([code], dtype=np.int64)
    return len({int(permuted_codes(array, k, perm)[0]) for perm in permutations(range(k))})


def per_placement_minimum(adjacency: np.ndarray, blocks) -> Counter:
    """Return the exact histogram of min over rules of the cost, per placement.

    A rule is a function of the profile, so its cut is constant on the
    classes of equal profile. The minimum is the cheapest cut of H that is
    constant on every class; all cuts of H are scanned in increasing cost.
    """
    n = len(adjacency)
    masks, cost = all_cut_costs(adjacency)
    order = np.argsort(cost, kind='stable')
    sides = ((masks[order][:, None] >> np.arange(n)[None, :]) & 1).astype(np.int8)
    sorted_cost = cost[order]
    classes: Counter = Counter()
    for roots in blocks:
        prof = profiles(adjacency, roots)
        first = (prof[:, :, None] == prof[:, None, :]).argmax(axis=2)
        keys, counts = np.unique(first, axis=0, return_counts=True)
        for key, count in zip(map(tuple, keys.tolist()), counts.tolist()):
            classes[key] += count
    histogram: Counter = Counter()
    for key, count in classes.items():
        compatible = np.all(sides == sides[:, list(key)], axis=1)
        histogram[int(sorted_cost[int(np.argmax(compatible))])] += count
    return histogram


def aggregated_tables(
    adjacency: np.ndarray, blocks, wanted: set[int]
) -> tuple[dict[int, Counter], Counter]:
    """Sum weighted profile-pair edge counts over placements of the wanted labeled types.

    ``blocks`` yields (roots, weights) arrays. Returns, per wanted labeled
    code, a Counter of unordered profile pairs (low, high) and the total
    placement weight of that code.
    """
    edges = edges_of(adjacency)
    tables: dict[int, Counter] = {code: Counter() for code in wanted}
    totals: Counter = Counter()
    wanted_array = np.array(sorted(wanted), dtype=np.int64)
    for roots, weights in blocks:
        k = roots.shape[1]
        code = type_codes(adjacency, roots)
        keep = np.isin(code, wanted_array)
        roots, weights, code = roots[keep], weights[keep], code[keep]
        if not len(roots):
            continue
        prof = profiles(adjacency, roots)
        low = np.minimum(prof[:, edges[:, 0]], prof[:, edges[:, 1]])
        high = np.maximum(prof[:, edges[:, 0]], prof[:, edges[:, 1]])
        key = ((code[:, None] << (2 * k)) | (low << k) | high).reshape(-1)
        key_weights = np.repeat(weights, len(edges))
        order = np.argsort(key, kind='stable')
        key, key_weights = key[order], key_weights[order]
        starts = np.flatnonzero(np.r_[True, key[1:] != key[:-1]])
        sums = np.add.reduceat(key_weights, starts)
        mask = (1 << k) - 1
        for packed, total in zip(key[starts].tolist(), sums.tolist()):
            tables[packed >> (2 * k)][((packed >> k) & mask, packed & mask)] += total
        for c, w in zip(code.tolist(), weights.tolist()):
            totals[c] += w
    return tables, totals


def exhaustive_minimum(table: Counter) -> int:
    """Return the least rule cost on a table by scanning every rule on its profiles."""
    nodes = sorted({x for pair in table for x in pair})
    position = {v: i for i, v in enumerate(nodes)}
    if len(nodes) > 20:
        raise ValueError('too many profiles for an exhaustive scan')
    masks = np.arange(1 << max(0, len(nodes) - 1), dtype=np.int64) << 1
    value = np.zeros(len(masks), dtype=np.int64)
    for (a, b), weight in table.items():
        i, j = position[a], position[b]
        value += weight * ((((masks >> i) ^ (masks >> j)) & 1) == 0)
    return int(value.min())


def four_vertex_densities(adjacency: np.ndarray) -> dict[str, int]:
    """Count ordered 4-tuples of vertices by the induced graph on the four positions.

    Equal vertices are non-adjacent, as two points of one part of the step
    graphon are. Returns counts over all n^4 tuples, keyed by graph name; a
    triangle-free graph induces only the seven names listed.
    """
    n = len(adjacency)
    index = np.indices((n, n, n, n)).reshape(4, -1)
    pairs = list(combinations(range(4), 2))
    present = np.array([adjacency[index[i], index[j]] for i, j in pairs])
    degree = np.zeros((4, present.shape[1]), dtype=np.int64)
    for row, (i, j) in zip(present, pairs):
        degree[i] += row
        degree[j] += row
    edges = present.sum(axis=0)
    top = degree.max(axis=0)
    names = {
        'empty': edges == 0,
        'K2+2K1': edges == 1,
        '2K2': (edges == 2) & (top == 1),
        'P3+K1': (edges == 2) & (top == 2),
        'P4': (edges == 3) & (top == 2),
        'K13': (edges == 3) & (top == 3),
        'C4': (edges == 4) & (top == 2) & (degree.min(axis=0) == 2),
    }
    return {name: int(mask.sum()) for name, mask in names.items()}


def homomorphism(source: np.ndarray, target: np.ndarray) -> list[int] | None:
    """Return a homomorphism from source to target, or None if none exists.

    Exhaustive backtracking: vertices are mapped in breadth-first order and
    each image must be adjacent to the images of the mapped neighbours.
    """
    n = len(source)
    order: list[int] = []
    for start in range(n):
        if start in order:
            continue
        queue = [start]
        order.append(start)
        while queue:
            v = queue.pop(0)
            for w in np.flatnonzero(source[v]).tolist():
                if w not in order:
                    order.append(w)
                    queue.append(w)
    image = [-1] * n

    def extend(position: int) -> bool:
        if position == n:
            return True
        v = order[position]
        mapped = [image[w] for w in np.flatnonzero(source[v]).tolist() if image[w] >= 0]
        for candidate in range(len(target)):
            if all(target[candidate, u] for u in mapped):
                image[v] = candidate
                if extend(position + 1):
                    return True
                image[v] = -1
        return False

    return image if extend(0) else None


def rule_cost(table: Counter, rule: dict[int, int]) -> int:
    """Return the summed cost of a rule: weight of pairs whose profiles share a side."""
    return sum(w for (a, b), w in table.items() if rule[a] == rule[b])
