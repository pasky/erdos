"""Nine-point coefficient tables without a full nine-point labeling table.

Extend every eight-vertex triangle-free graph by every independent
neighborhood, identifying isomorphism classes exactly. Deletion averages
lift order-eight rows. Seven-root cut coefficients count all embeddings
of each canonical labeled root type, with the two remaining endpoints.
New flag-square blocks use one or three roots and complementary extension
sets. All incidence counts are integers; matrices are divided by the
explicit sampling counts only for floating discovery.
"""
from __future__ import annotations

import math
from collections.abc import Callable
from itertools import combinations, permutations

import networkx as nx
import numpy as np
from scipy import sparse
from util.flaglp import pairs_of, triangle_free_graphs


def codes(adjacency: np.ndarray) -> np.ndarray:
    """Encode a batch of labeled adjacency matrices."""
    out = np.zeros(adjacency.shape[:-2], np.int64)
    for bit, (i, j) in enumerate(pairs_of(adjacency.shape[-1])):
        out |= adjacency[..., i, j].astype(np.int64) << bit
    return out


def bucket(graph: nx.Graph) -> tuple:
    """A cheap invariant used only to shortlist exact isomorphism comparisons."""
    degrees = dict(graph.degree())
    return (
        graph.number_of_edges(),
        tuple(sorted((degrees[v], tuple(sorted(degrees[u] for u in graph[v]))) for v in graph)),
    )


class Nine:
    """The exhaustive nine-vertex universe, projection, and cut records."""

    def __init__(self, log: Callable[[str], None]) -> None:
        """Generate classes by independent-neighborhood extensions and exact isomorphism."""
        self.eight = triangle_free_graphs(8)
        self.graphs = []
        self.buckets: dict[tuple, list[int]] = {}
        self.networks = []
        for a in self.eight:
            for mask in range(256):
                neighbors = [i for i in range(8) if (mask >> i) & 1]
                if any(a[i, j] for i, j in combinations(neighbors, 2)):
                    continue
                g = nx.from_numpy_array(a)
                g.add_node(8)
                g.add_edges_from((8, v) for v in neighbors)
                key = bucket(g)
                indices = self.buckets.setdefault(key, [])
                if any(nx.is_isomorphic(g, self.networks[i]) for i in indices):
                    continue
                indices.append(len(self.graphs))
                self.networks.append(g)
                self.graphs.append(nx.to_numpy_array(g, nodelist=range(9), dtype=np.int8))
        self.count = len(self.graphs)
        log(f'Exhaustive extension generated {self.count} nine-vertex classes')
        if self.count != 1897:
            raise RuntimeError('Unexpected nine-vertex census size')
        perm = np.array(list(permutations(range(8))), np.int16)
        allcodes, owners = [], []
        for h, a in enumerate(self.eight):
            c = np.unique(codes(a[perm[:, :, None], perm[:, None, :]]))
            allcodes.append(c)
            owners.append(np.full(len(c), h, np.int16))
        allcodes = np.concatenate(allcodes)
        owners = np.concatenate(owners)
        order = allcodes.argsort()
        allcodes, owners = allcodes[order], owners[order]
        self.projection_counts = np.zeros((len(self.eight), self.count), np.int16)
        for h, a in enumerate(self.graphs):
            sub = np.array([[v for v in range(9) if v != omit] for omit in range(9)])
            c = codes(a[sub[:, :, None], sub[:, None, :]])
            where = np.searchsorted(allcodes, c)
            if np.any(where == len(allcodes)) or np.any(allcodes[where] != c):
                raise RuntimeError('An eight-vertex deletion is missing')
            self.projection_counts[:, h] = np.bincount(owners[where], minlength=len(self.eight))
        if np.any(self.projection_counts.sum(axis=0) != 9):
            raise RuntimeError('Deletion multiplicities failed')
        self.projection = self.projection_counts.astype(float) / 9
        self.control_counts = self.cycle_counts(5)
        self.control = self.control_counts / 5**9
        self.p = np.array([a.sum() / 72 for a in self.graphs])
        # In an induced sample of nine distinct labels the edge coefficient
        # is 2e/(9*8); repeated underlying vertices are in the sampled state.
        if abs(self.p @ self.control - 0.4) > 1e-12:
            raise RuntimeError('Pentagon edge-density control failed')
        log('Deletion projection and pentagon density control pass')
        self.cut_records = self.root_records(log)

    def cycle_counts(self, size: int) -> np.ndarray:
        """Count every ordered sample from a balanced cycle by its occupancies."""
        out = np.zeros(self.count, np.int64)
        def visit(remaining: int, parts: list[int]) -> None:
            if len(parts) == size - 1:
                counts = [*parts, remaining]
                labels = np.repeat(np.arange(size), counts)
                a = (((labels[:, None] - labels[None, :]) % size == 1)
                     | ((labels[None, :] - labels[:, None]) % size == 1)).astype(np.int8)
                g = nx.from_numpy_array(a)
                for h in self.buckets.get(bucket(g), []):
                    if nx.is_isomorphic(g, self.networks[h]):
                        out[h] += math.factorial(9) // math.prod(math.factorial(c) for c in counts)
                        return
                raise RuntimeError('Cycle sample missing from exhaustive universe')
            for c in range(remaining + 1):
                visit(remaining - c, [*parts, c])
        visit(9, [])
        if int(out.sum()) != size**9:
            raise RuntimeError('Cycle sample multiplicities failed')
        return out

    def root_records(self, log: Callable[[str], None]) -> list[dict]:
        """Count canonical seven-root embeddings and unordered endpoint profiles."""
        perm = np.array(list(permutations(range(7))), np.int16)
        inverse = np.argsort(perm, axis=1).astype(np.int8)
        roots = []
        for g in nx.graph_atlas_g():
            if len(g) != 7 or sum(nx.triangles(g).values()):
                continue
            a = nx.to_numpy_array(g, dtype=np.int8)
            relabeled = a[perm[:, :, None], perm[:, None, :]]
            c = codes(relabeled)
            k = int(c.argmin())
            roots.append((int(c[k]), relabeled[k].copy()))
        roots.sort(key=lambda item: item[0])
        self.root_codes = [code for code, _a in roots]
        automorphisms = [
            int(np.count_nonzero(codes(a[perm[:, :, None], perm[:, None, :]]) == code))
            for code, a in roots
        ]
        self.root_multiplicity = [math.factorial(7) // a for a in automorphisms]
        root_labels = np.concatenate([codes(a[perm[:, :, None], perm[:, None, :]]) for _code, a in roots])
        owner = np.repeat(np.arange(len(roots), dtype=np.int16), len(perm))
        maps = np.tile(inverse, (len(roots), 1))
        order = root_labels.argsort(kind='stable')
        root_labels, owner, maps = root_labels[order], owner[order], maps[order]
        positions = np.array(list(combinations(range(9), 7)), np.int16)
        remaining = np.array([[v for v in range(9) if v not in s] for s in positions], np.int16)
        rows = []
        for h, a in enumerate(self.graphs):
            c = codes(a[positions[:, :, None], positions[:, None, :]])
            lo = np.searchsorted(root_labels, c, side='left')
            hi = np.searchsorted(root_labels, c, side='right')
            keys = []
            for s, ends, left, right in zip(positions, remaining, lo, hi):
                if right == left:
                    raise RuntimeError('Seven-root type missing')
                embeddings = maps[left:right]
                px = (a[ends[0], s[embeddings]] * (1 << np.arange(7))).sum(axis=1)
                py = (a[ends[1], s[embeddings]] * (1 << np.arange(7))).sum(axis=1)
                first, second = np.minimum(px, py), np.maximum(px, py)
                key = 2 * ((int(owner[left]) * 128 + first) * 128 + second) + int(a[ends[0], ends[1]])
                keys.append(key)
            key, multiplicity = np.unique(np.concatenate(keys), return_counts=True)
            rows.append((np.full(len(key), h, np.int16), key, 2 * multiplicity))
        h, key, count = (np.concatenate(part) for part in zip(*rows))
        edge = key & 1
        py = (key >> 1) & 127
        px = (key >> 8) & 127
        types = key >> 15
        result = []
        total_mass = np.zeros(self.count, np.int64)
        total_edges = np.zeros(self.count, np.int64)
        for t, code in enumerate(self.root_codes):
            take = types == t
            factor = math.factorial(7) // automorphisms[t]
            np.add.at(total_mass, h[take], factor * count[take])
            np.add.at(total_edges, h[take], factor * count[take] * edge[take])
            result.append({'h': h[take], 'x': px[take], 'y': py[take],
                           'e': edge[take], 'count': count[take], 'code': code})
        if (
            np.any(total_mass != math.factorial(9))
            or np.any(total_edges != np.array([int(a.sum()) * math.factorial(7) for a in self.graphs]))
        ):
            raise RuntimeError('Seven-root embedding coverage or edge identity failed')
        log(f'Seven-root tables: {len(result)} types, {len(key)} exact incidence records')
        return result


def flag_block(
    nine: Nine, roots: int, log: Callable[[str], None]
) -> list[tuple[sparse.csr_matrix, int, tuple]]:
    """New order-nine full flag squares with one or three fixed roots."""
    if roots not in (1, 3):
        raise ValueError('Declared square bases use one or three roots')
    extension = (9 - roots) // 2
    size = roots + extension
    edges = pairs_of(size)
    flag_codes = np.arange(1 << len(edges), dtype=np.int64)
    adjacency = np.zeros((len(flag_codes), size, size), np.int8)
    for bit, (i, j) in enumerate(edges):
        adjacency[:, i, j] = adjacency[:, j, i] = (flag_codes >> bit) & 1
    valid = np.ones(len(flag_codes), bool)
    for i, j, k in combinations(range(size), 3):
        valid &= ~(adjacency[:, i, j] & adjacency[:, i, k] & adjacency[:, j, k]).astype(bool)
    root_code = codes(adjacency[:, :roots, :roots])
    valid &= np.isin(root_code, [0] if roots == 1 else [0, 1, 3])
    selected = np.flatnonzero(valid)
    canonical = np.full(len(flag_codes), -1, np.int64)
    least = np.full(len(selected), 1 << len(edges), np.int64)
    for tail in permutations(range(roots, size)):
        p = np.array([*range(roots), *tail])
        least = np.minimum(least, codes(adjacency[selected][:, p[:, None], p[None, :]]))
    canonical[selected] = least
    del adjacency
    dictionaries = {}
    lookup = np.full(len(flag_codes), -1, np.int16)
    for t in ([0] if roots == 1 else [0, 1, 3]):
        flagset = np.unique(canonical[(root_code == t) & valid])
        dictionaries[t] = flagset
        use = (root_code == t) & valid
        lookup[use] = np.searchsorted(flagset, canonical[use])
    tuples = []
    for r in permutations(range(9), roots):
        remainder = [v for v in range(9) if v not in r]
        for first in combinations(remainder, extension):
            second = [v for v in remainder if v not in first]
            tuples.append([*r, *first, *second])
    tuples = np.asarray(tuples, np.int16)
    first = tuples[:, :size]
    second = tuples[:, [*range(roots), *range(size, 9)]]
    denominator = len(tuples)
    # At most 10080 labeled root/extension choices contribute to a column,
    # so int16 suffices for these incidence counts. Keep the final matrices sparse.
    if denominator >= 32768:
        raise RuntimeError('Square count exceeds the declared int16 range')
    raw = {t: np.zeros((len(f) * (len(f) + 1) // 2, nine.count), np.int16)
           for t, f in dictionaries.items()}
    log(f'New square basis roots {roots}: dimensions {[len(f) for f in dictionaries.values()]}')
    for h, a in enumerate(nine.graphs):
        ca = codes(a[first[:, :, None], first[:, None, :]])
        cb = codes(a[second[:, :, None], second[:, None, :]])
        for t, flags in dictionaries.items():
            use = (root_code[ca] == t) & (lookup[ca] >= 0)
            x, y = lookup[ca[use]], lookup[cb[use]]
            if np.any(y < 0):
                raise RuntimeError('Missing second flag')
            lo, hi = np.minimum(x, y).astype(np.int64), np.maximum(x, y).astype(np.int64)
            n = len(flags)
            pos = lo * n - lo * (lo - 1) // 2 + hi - lo
            raw[t][:, h] = np.bincount(pos, minlength=n * (n + 1) // 2)
    out = []
    for t, flags in dictionaries.items():
        n = len(flags)
        i, j = np.triu_indices(n)
        M = sparse.csr_matrix(raw[t], dtype=float) / denominator
        del raw[t]
        M = sparse.diags(1 / np.where(i == j, 1, np.sqrt(2))) @ M
        out.append((M.tocsr(), n, ('plain_nine', roots, t, flags.tolist(), denominator)))
    return out


def localizer_blocks(
    nine: Nine, log: Callable[[str], None]
) -> list[tuple[sparse.csr_matrix, int, tuple]]:
    """Nine-point band and recursive matrices on one-rooted four-point flags."""
    adjacency = np.zeros((64, 4, 4), np.int8)
    for bit, (i, j) in enumerate(pairs_of(4)):
        adjacency[:, i, j] = adjacency[:, j, i] = (np.arange(64) >> bit) & 1
    valid = np.ones(64, bool)
    for i, j, k in combinations(range(4), 3):
        valid &= ~(adjacency[:, i, j] & adjacency[:, i, k] & adjacency[:, j, k]).astype(bool)
    canonical = np.full(64, 64, np.int16)
    for tail in permutations((1, 2, 3)):
        p = np.array((0, *tail))
        canonical = np.minimum(canonical, codes(adjacency[:, p[:, None], p[None, :]]))
    flagset = np.unique(canonical[valid])
    lookup = np.full(64, -1, np.int16)
    lookup[valid] = np.searchsorted(flagset, canonical[valid])
    tuples = []
    for root in range(9):
        for ends in combinations([v for v in range(9) if v != root], 2):
            remainder = [v for v in range(9) if v != root and v not in ends]
            for first in combinations(remainder, 3):
                second = [v for v in remainder if v not in first]
                tuples.append((root, *ends, *first, *second))
    tuples = np.asarray(tuples, np.int16)
    denominator = len(tuples)
    if denominator != 5040:
        raise RuntimeError('Wrong one-root two-endpoint extension count')
    n = len(flagset)
    first = tuples[:, (0, 3, 4, 5)]
    second = tuples[:, (0, 6, 7, 8)]
    raw = np.zeros((n * (n + 1) // 2, 8, nine.count), np.int16)
    for h, a in enumerate(nine.graphs):
        x = lookup[codes(a[first[:, :, None], first[:, None, :]])]
        y = lookup[codes(a[second[:, :, None], second[:, None, :]])]
        if min(x.min(), y.min()) < 0:
            raise RuntimeError('Localizer extension flag missing')
        lo, hi = np.minimum(x, y).astype(np.int64), np.maximum(x, y).astype(np.int64)
        pos = lo * n - lo * (lo - 1) // 2 + hi - lo
        kind = (
            4 * a[tuples[:, 0], tuples[:, 1]]
            + 2 * a[tuples[:, 0], tuples[:, 2]]
            + a[tuples[:, 1], tuples[:, 2]]
        )
        raw[:, :, h] = np.bincount(pos * 8 + kind, minlength=raw.shape[0] * 8).reshape(raw.shape[:2])
    if np.any(raw.sum(axis=(0, 1)) != denominator):
        raise RuntimeError('Localizer incidence mass identity failed')
    if np.any(
        (raw[:, 1::2, :].sum(axis=(0, 1)) * 72)
        != denominator * np.array([int(a.sum()) for a in nine.graphs])
    ):
        raise RuntimeError('Localizer endpoint-edge identity failed')
    kinds = np.arange(8)
    edge = kinds & 1
    px, py = kinds >> 2, (kinds >> 1) & 1
    rules = [
        (10000 * edge - 2486, 10000, ('band_lower_nine',)),
        (3197 - 10000 * edge, 10000, ('band_upper_nine',)),
    ]
    # Outside colour biases are 0,1/4,1/2,3/4,1. Labels 5,6 name
    # independently recut parts. Two profile cells need no further parts.
    z = np.array([-2, -1, 0, 1, 2, 0, 0], np.int64)
    seen = set()
    for left in range(7):
        for right in range(7):
            label = np.array([left, right])
            same_part = (label[px] >= 5) & (label[px] == label[py])
            same_part = same_part.astype(np.int64)
            numerator = 25 * edge * (4 + z[label[px]] * z[label[py]] - 4 * same_part) - 16 * (1 - same_part)
            key = numerator.tobytes()
            if key in seen or not np.any(numerator):
                continue
            seen.add(key)
            rules.append((numerator, 200, ('recursive_localizer_nine', [left, right])))
    i, j = np.triu_indices(n)
    scale = sparse.diags(1 / np.where(i == j, 1, np.sqrt(2)))
    out = []
    for numerator, divisor, recipe in rules:
        counts = np.tensordot(raw.astype(np.int64), numerator, axes=(1, 0))
        M = scale @ sparse.csr_matrix(counts / (divisor * denominator))
        out.append((M.tocsr(), n, (*recipe, flagset.tolist(), divisor, denominator)))
    log(f'Nine-point recursive/band localizers: {len(out)} matrices on {n} flags')
    return out
