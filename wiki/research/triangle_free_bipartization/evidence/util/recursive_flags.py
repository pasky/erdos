"""Full flag localizers for weighted-extremal recursive-cut discovery.

These are floating-point coefficient generators, not exact certificates.
Degree blocks localize d(r_i)-4/25. Recursive blocks use one or two roots,
two cut endpoints and two disjoint two-vertex flag extensions. Their
positivity requires the hypothetical weighted counterexample of the sketch.
"""

from __future__ import annotations

from itertools import permutations

import networkx as nx
import numpy as np
from scipy import sparse
from util.flaglp import FlagSystem, canonical_types, pairs_of


def degree_scalar_rows(system: FlagSystem) -> list[tuple[np.ndarray, tuple]]:
    """Multiply the root degree surplus by every one-rooted flag on L-1 points."""
    size = system.order - 1
    flag_perms = np.array(list(permutations(range(size))), np.int16)
    lookup = np.full(1 << (size * (size - 1) // 2), -1, np.int32)
    canonical = {}
    for graph in nx.graph_atlas_g():
        if graph.number_of_nodes() != size or sum(nx.triangles(graph).values()):
            continue
        adjacency = nx.to_numpy_array(graph, dtype=np.int64)
        relabeled = adjacency[flag_perms[:, :, None], flag_perms[:, None, :]]
        codes = np.zeros(len(flag_perms), np.int64)
        for bit, (i, j) in enumerate(pairs_of(size)):
            codes |= relabeled[:, i, j] << bit
        ids = []
        for root in range(size):
            code = int(codes[flag_perms[:, 0] == root].min())
            if code not in canonical:
                canonical[code] = len(canonical)
            ids.append(canonical[code])
        values = np.array(ids, np.int32)[flag_perms[:, 0]]
        old = lookup[codes]
        if np.any((old >= 0) & (old != values)):
            raise RuntimeError('Rooted flag code collision')
        lookup[codes] = values
    count = len(canonical)
    rows = np.zeros((count, system.count))
    perms = np.array(list(permutations(range(system.order))), np.int16)
    positions = (0, *range(2, system.order))
    for h, adjacency in enumerate(system.graphs):
        relabeled = adjacency[perms[:, :, None], perms[:, None, :]]
        codes = np.zeros(system.nperm, np.int64)
        for bit, (i, j) in enumerate(pairs_of(size)):
            codes |= relabeled[:, positions[i], positions[j]] << bit
        flags = lookup[codes]
        if flags.min() < 0:
            raise RuntimeError('A sampled one-rooted flag is missing')
        rows[:, h] = (
            np.bincount(flags, weights=relabeled[:, 0, 1] - 4 / 25, minlength=count)
            / system.nperm
        )
    return [(rows[index], (size, code)) for code, index in canonical.items()]


def degree_blocks(system: FlagSystem) -> list[tuple[sparse.csr_matrix, int, tuple]]:
    """Build degree-localized squares with all specified rooted flag bases."""
    order = system.order
    specs = [
        (s, m, root)
        for m in range(2, order)
        for s in range(1, m)
        if 2 * m - s in (order - 2, order - 1) and m - s <= 3
        for root in range(s)
    ]
    records: dict[tuple, list] = {key: [] for key in specs}
    perms = np.array(list(permutations(range(order))), dtype=np.int16)
    for h, adjacency in enumerate(system.graphs):
        relabeled = adjacency[perms[:, :, None], perms[:, None, :]]
        for s, m, root in specs:
            changed = relabeled.copy()
            # The last vertex is outside both flags. Replacing its edge to
            # the penultimate vertex changes only _square_keys' multiplier
            # bit, leaving both sampled flags and their root type intact.
            changed[:, order - 2, order - 1] = relabeled[:, root, order - 1]
            changed[:, order - 1, order - 2] = relabeled[:, root, order - 1]
            records[(s, m, root)].append(system._square_keys(h, changed, s, m))
    types = {s: canonical_types(s) for s in sorted({s for s, _m, _root in specs})}
    out = []
    for (s, m, root), pieces in records.items():
        h, key, counts = (np.concatenate(part) for part in zip(*pieces))
        multiplier = (key & 1) - 4 / 25
        rest = key >> 1
        second = rest & ((1 << 12) - 1)
        first = (rest >> 12) & ((1 << 12) - 1)
        code = rest >> 24
        for t in types[s]:
            take = code == t
            if not take.any():
                continue
            flags = np.unique(np.r_[first[take], second[take]])
            n = len(flags)
            a = np.searchsorted(flags, first[take])
            b = np.searchsorted(flags, second[take])
            lo, hi = np.minimum(a, b), np.maximum(a, b)
            pos = lo * n - lo * (lo - 1) // 2 + hi - lo
            values = counts[take] * multiplier[take] / system.nperm
            values = values / np.where(lo == hi, 1, np.sqrt(2))
            M = sparse.coo_matrix(
                (values, (pos, h[take])),
                shape=(n * (n + 1) // 2, system.count),
            ).tocsr()
            scale = float(abs(M).max())
            if scale > 0:
                out.append((M / scale, n, (s, m, root, int(t), flags.tolist(), scale)))
    return out


def recursive_blocks(
    system: FlagSystem,
) -> list[tuple[sparse.csr_matrix, int, int, int, tuple]]:
    """Build feature tensors for full two-extension recursive localizers."""
    order = system.order
    roots = order - 6
    cells = 1 << roots
    features = 2 * cells**2
    flag_codes = 2 * cells**2
    specs = []
    perms = np.array(list(permutations(range(order))), dtype=np.int16)
    for h, adjacency in enumerate(system.graphs):
        a = adjacency[perms[:, :, None], perms[:, None, :]]
        rootcode = np.zeros(system.nperm, np.int64)
        for bit, (i, j) in enumerate(pairs_of(roots)):
            rootcode |= a[:, i, j] << bit
        profiles = []
        for v in range(roots, order):
            p = np.zeros(system.nperm, np.int64)
            for i in range(roots):
                p |= a[:, i, v] << i
            profiles.append(p)
        feature = 2 * (profiles[0] * cells + profiles[1]) + a[:, roots, roots + 1]
        flags = []
        for offset in (2, 4):
            first, second = profiles[offset], profiles[offset + 1]
            edge = a[:, roots + offset, roots + offset + 1]
            flags.append(
                2 * np.minimum(first * cells + second, second * cells + first) + edge
            )
        key = (
            (rootcode * features + feature) * flag_codes + flags[0]
        ) * flag_codes + flags[1]
        values, counts = np.unique(key, return_counts=True)
        specs.append((np.full(len(values), h, np.int32), values, counts))
    h, key, counts = (np.concatenate(part) for part in zip(*specs))
    second = key % flag_codes
    key //= flag_codes
    first = key % flag_codes
    key //= flag_codes
    feature = key % features
    rootcode = key // features
    out = []
    for t in canonical_types(roots):
        take = rootcode == t
        flags = np.unique(np.r_[first[take], second[take]])
        n = len(flags)
        a = np.searchsorted(flags, first[take])
        b = np.searchsorted(flags, second[take])
        lo, hi = np.minimum(a, b), np.maximum(a, b)
        width = n * (n + 1) // 2
        pos = feature[take] * width + lo * n - lo * (lo - 1) // 2 + hi - lo
        values = counts[take] / system.nperm / np.where(lo == hi, 1, np.sqrt(2))
        M = sparse.coo_matrix(
            (values, (pos, h[take])), shape=(features * width, system.count)
        ).tocsr()
        scale = float(abs(M).max())
        if scale > 0:
            out.append((M / scale, n, roots, int(t), (flags.tolist(), scale)))
    return out
