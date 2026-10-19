"""Floating-point linear programs for localized rooted contradiction certificates.

The hypothesis H(a, b) is that W is a triangle-free {0,1}-valued graphon with
a <= p(W) <= b and d_mono(W) >= t. A row is a linear functional of the induced
densities of order L that is nonnegative under H(a, b):

- cut rows: k roots, a cut pair x, y and m = L - 2 - k multiplier vertices
  z1, z2 sample the integrand [type(R) = tau] f(z) ([x ~ y] same(x, y) - t),
  where same(x, y) is the probability that a profile rule puts x and y on one
  side and f is a nonnegative multiplier: 1, a class size, a band factor
  [z1 ~ z2] - a or b - [z1 ~ z2], a degree square, or the square of a
  combination of class sizes;
- band rows p - a, b - p and (p - a)(b - p);
- squares [[F^2]]_sigma of fixed combinations F of sigma-flags, plain or
  multiplied by a band factor;
- optionally, products of two cut rows on the same L - 4 roots, valid
  because both factors are nonnegative under the hypothesis.

A certificate is a nonnegative combination of rows whose coefficient on every
triangle-free graph of order L is negative. The program maximizes eps with
every coefficient at most -eps and the cut-row weights summing to one; every
column is scaled to unit maximum, which changes eps by a positive factor and
not its sign. Cut rows and localizing squares enter by column generation;
squares of eigenvectors of the flag moment matrices at the dual state may be
added in rounds. All arithmetic is floating point: the programs search for
certificates and certify nothing. A positive eps would still need an exact
rational certificate.
"""

from __future__ import annotations

import warnings
from itertools import combinations, permutations

import networkx as nx
import numpy as np
from scipy.optimize import linprog

# OEIS A006785: triangle-free graphs on 7 and 8 vertices
GRAPH_COUNTS = {7: 107, 8: 410}
DEGREE_GRID = (2 / 7, 3 / 10, 4 / 13, 5 / 16, 1 / 4, 1 / 3)
COINS = (0.25, 0.5, 0.75)


def pairs_of(k: int) -> list[tuple[int, int]]:
    """Return the vertex pairs of [k] in the bit order of type codes."""
    return list(combinations(range(k), 2))


def permute_code(code: int, k: int, perm: tuple[int, ...]) -> int:
    """Relabel vertex i as perm[i] in a labeled code."""
    index = {pair: bit for bit, pair in enumerate(pairs_of(k))}
    out = 0
    for bit, (i, j) in enumerate(pairs_of(k)):
        if (code >> bit) & 1:
            out |= 1 << index[tuple(sorted((perm[i], perm[j])))]
    return out


def canonical_types(k: int) -> list[int]:
    """Return the least labeled code of every triangle-free graph on k vertices."""
    out = set()
    for code in range(1 << len(pairs_of(k))):
        edges = {pair for bit, pair in enumerate(pairs_of(k)) if (code >> bit) & 1}
        if any({(i, j), (j, l), (i, l)} <= edges for i, j, l in combinations(range(k), 3)):
            continue
        out.add(min(permute_code(code, k, p) for p in permutations(range(k))))
    return sorted(out)


def independent_sets(code: int, k: int) -> list[int]:
    """Return the independent sets of a labeled type as bit masks: its possible profiles."""
    edges = [pair for bit, pair in enumerate(pairs_of(k)) if (code >> bit) & 1]
    return [s for s in range(1 << k) if not any((s >> i) & 1 and (s >> j) & 1 for i, j in edges)]


def triangle_free_graphs(order: int) -> list[np.ndarray]:
    """Return one adjacency matrix for every triangle-free graph on 7 or 8 vertices."""
    seven = [nx.convert_node_labels_to_integers(g) for g in nx.graph_atlas_g()
             if g.number_of_nodes() == 7 and sum(nx.triangles(g).values()) == 0]
    graphs = seven
    if order == 8:
        buckets: dict[str, list[nx.Graph]] = {}
        graphs = []
        for g in seven:
            a = nx.to_numpy_array(g, nodelist=range(7), dtype=int)
            for s in range(1 << 7):
                nb = [i for i in range(7) if (s >> i) & 1]
                if any(a[i, j] for i, j in combinations(nb, 2)):
                    continue
                h = g.copy()
                h.add_node(7)
                h.add_edges_from((7, i) for i in nb)
                with warnings.catch_warnings():
                    # the hash only buckets candidates; isomorphism is tested exactly
                    warnings.simplefilter('ignore', UserWarning)
                    key = nx.weisfeiler_lehman_graph_hash(h, iterations=4)
                bucket = buckets.setdefault(key, [])
                if not any(nx.is_isomorphic(h, other) for other in bucket):
                    bucket.append(h)
                    graphs.append(h)
    if len(graphs) != GRAPH_COUNTS[order]:
        raise RuntimeError(f'found {len(graphs)} triangle-free graphs on {order} vertices')
    return [nx.to_numpy_array(g, nodelist=range(order), dtype=np.int64) for g in graphs]


class FlagSystem:
    """Row data of the localized rooted system at one order and density interval."""

    def __init__(self, order: int, low: float, high: float) -> None:
        self.order, self.low, self.high = order, low, high
        self.graphs = triangle_free_graphs(order)
        self.count = len(self.graphs)
        perms = np.array(list(permutations(range(order))), dtype=np.int64)
        self.nperm = len(perms)
        self.families = [self._family(order - 2 - m, m) for m in (0, 1, 2)]
        plain = [(s, m) for m in range(1, order) for s in range(m)
                 if 2 * m - s in (order - 1, order) and m - s <= 4 and (s > 0 or m <= 4)]
        local = [(s, m) for m in range(1, order) for s in range(m)
                 if 2 * m - s in (order - 3, order - 2) and m - s <= 4]
        records: dict = {('cut', m): [] for m in (0, 1, 2)}
        records.update({('sq', s, m): [] for s, m in plain + local})
        records['band'] = []
        records['product'] = []
        codes, classes = [], []
        for h, adjacency in enumerate(self.graphs):
            relabeled = adjacency[perms[:, :, None], perms[:, None, :]]
            labeled = np.zeros(self.nperm, dtype=np.int64)
            for bit, (i, j) in enumerate(pairs_of(order)):
                labeled |= relabeled[:, i, j] << bit
            labeled = np.unique(labeled)
            codes.append(labeled)
            classes.append(np.full(len(labeled), h))
            for m, family in zip((0, 1, 2), self.families):
                records[('cut', m)].append(self._cut_keys(h, relabeled, family))
            for s, m in plain + local:
                records[('sq', s, m)].append(self._square_keys(h, relabeled, s, m))
            records['product'].append(self._product_keys(h, relabeled, self.families[2]))
            band = relabeled[:, 0, 1] * 2 + relabeled[:, 2, 3]
            u, c = np.unique(band, return_counts=True)
            records['band'].append((np.full(len(u), h), u, c))
        self.records = {key: tuple(np.concatenate(part) for part in zip(*lists))
                        for key, lists in records.items()}
        codes, classes = np.concatenate(codes), np.concatenate(classes)
        order_codes = np.argsort(codes)
        self.codes, self.classes = codes[order_codes], classes[order_codes]
        for m, family in zip((0, 1, 2), self.families):
            self._split_family(family, self.records[('cut', m)])
        self.p_vector = self._band_vector(lambda e01, e23: e01)
        self.fixed = [('p-a', self._band_vector(lambda e01, e23: e01 - low)),
                      ('b-p', self._band_vector(lambda e01, e23: high - e01)),
                      ('(p-a)(b-p)', self._band_vector(lambda e01, e23: (e01 - low) * (high - e23)))]
        self.blocks = {}
        for s, m in plain + local:
            self._blocks(s, m, (s, m) in local)
        for key, block in self.blocks.items():
            size = block['size']
            if size <= 26:
                for i, j in combinations(range(size), 2):
                    for sign in (1.0, -1.0):
                        v = np.zeros(size)
                        v[i], v[j] = 1.0, sign
                        row = self.block_row(block, v)
                        if row.min() < -1e-13:
                            self.fixed.append((('pair', key, i, j, sign), row))
            if key[3] != 'plain':
                for i in range(size):
                    v = np.zeros(size)
                    v[i] = 1.0
                    self.fixed.append((('local', key, i), self.block_row(block, v)))

    def _family(self, k: int, m: int) -> dict:
        types = canonical_types(k)
        index = np.full(1 << len(pairs_of(k)), -1)
        index[types] = np.arange(len(types))
        return {'k': k, 'm': m, 'types': types, 'index': index,
                'profiles': [independent_sets(code, k) for code in types]}

    def _cut_keys(self, h, relabeled, family):
        k, m = family['k'], family['m']
        roots = list(range(k))
        code = np.zeros(len(relabeled), dtype=np.int64)
        for bit, (i, j) in enumerate(pairs_of(k)):
            code |= relabeled[:, i, j] << bit
        t = family['index'][code]

        def profile(v):
            out = np.zeros(len(relabeled), dtype=np.int64)
            for i in roots:
                out |= relabeled[:, v, i] << i
            return out

        x, y = k, k + 1
        z1 = profile(k + 2) if m >= 1 else np.zeros(len(relabeled), dtype=np.int64)
        z2 = profile(k + 3) if m >= 2 else np.zeros(len(relabeled), dtype=np.int64)
        ez = relabeled[:, k + 2, k + 3] if m >= 2 else np.zeros(len(relabeled), dtype=np.int64)
        key = ((((((t << k | profile(x)) << k | profile(y)) << 1 | relabeled[:, x, y]) << k | z1)
                << k | z2) << 1) | ez
        keep = t >= 0
        u, c = np.unique(key[keep], return_counts=True)
        return np.full(len(u), h), u, c

    def _product_keys(self, h, relabeled, family):
        """Keys (type, first pair, second pair) for products of two cut rows on the same roots."""
        k = family['k']
        n = len(relabeled)
        code = np.zeros(n, dtype=np.int64)
        for bit, (i, j) in enumerate(pairs_of(k)):
            code |= relabeled[:, i, j] << bit
        t = family['index'][code]

        def pair(x):
            px = np.zeros(n, dtype=np.int64)
            py = np.zeros(n, dtype=np.int64)
            for i in range(k):
                px |= relabeled[:, x, i] << i
                py |= relabeled[:, x + 1, i] << i
            return ((px << k) | py) << 1 | relabeled[:, x, x + 1]

        width = 2 * k + 1
        key = ((t << width | pair(k)) << width) | pair(k + 2)
        keep = t >= 0
        u, c = np.unique(key[keep], return_counts=True)
        return np.full(len(u), h), u, c

    def product_tables(self) -> list[dict]:
        """Split the product records by type into first-pair and second-pair keys."""
        k = self.families[2]['k']
        width = 2 * k + 1
        h, key, count = self.records['product']
        second = key & ((1 << width) - 1)
        first = (key >> width) & ((1 << width) - 1)
        t = key >> (2 * width)
        return [{'h': h[t == ti], 'first': first[t == ti], 'second': second[t == ti],
                 'w': count[t == ti] / self.nperm} for ti in range(len(self.families[2]['types']))]

    def _split_family(self, family, records) -> None:
        h, key, count = records
        k = family['k']
        mask = (1 << k) - 1
        fields = {'ez': key & 1}
        key = key >> 1
        fields['z2'] = key & mask
        key = key >> k
        fields['z1'] = key & mask
        key = key >> k
        fields['e'] = key & 1
        key = key >> 1
        fields['py'] = key & mask
        key = key >> k
        fields['px'] = key & mask
        t = key >> k
        family['data'] = []
        for ti in range(len(family['types'])):
            sel = t == ti
            entry = {name: value[sel] for name, value in fields.items()}
            entry['h'] = h[sel]
            entry['w'] = count[sel] / self.nperm
            family['data'].append(entry)

    def _square_keys(self, h, relabeled, s, m):
        e = m - s
        n = len(relabeled)
        code = np.zeros(n, dtype=np.int64)
        for bit, (i, j) in enumerate(pairs_of(s)):
            code |= relabeled[:, i, j] << bit

        def flag(ext):
            best = None
            for perm in permutations(ext):
                c = np.zeros(n, dtype=np.int64)
                shift = 0
                for v in perm:
                    for i in range(s):
                        c |= relabeled[:, v, i] << (shift + i)
                    shift += s
                for i, j in combinations(range(e), 2):
                    c |= relabeled[:, perm[i], perm[j]] << shift
                    shift += 1
                best = c if best is None else np.minimum(best, c)
            return best

        first = flag(list(range(s, m)))
        second = flag(list(range(m, 2 * m - s)))
        band = relabeled[:, self.order - 2, self.order - 1]
        key = (((code << 12 | first) << 12 | second) << 1) | band
        u, c = np.unique(key, return_counts=True)
        return np.full(len(u), h), u, c

    def _band_vector(self, weight) -> np.ndarray:
        h, key, count = self.records['band']
        return np.bincount(h, weights=count * weight(key >> 1, key & 1), minlength=self.count) / self.nperm

    def _blocks(self, s: int, m: int, localized: bool) -> None:
        h, key, count = self.records[('sq', s, m)]
        band = key & 1
        rest = key >> 1
        second = rest & ((1 << 12) - 1)
        first = (rest >> 12) & ((1 << 12) - 1)
        code = rest >> 24
        types = canonical_types(s) if s >= 2 else [0]
        for t in types:
            sel = code == t
            if not sel.any():
                continue
            flags = np.unique(np.concatenate([first[sel], second[sel]]))
            position = {f: i for i, f in enumerate(flags.tolist())}
            i1 = np.array([position[f] for f in first[sel].tolist()])
            i2 = np.array([position[f] for f in second[sel].tolist()])
            weights = [('plain', np.ones(sel.sum()))]
            if localized:
                weights = [('low', band[sel] - self.low), ('high', self.high - band[sel])]
            for label, factor in weights:
                self.blocks[(s, m, int(t), label)] = {
                    'h': h[sel], 'i1': i1, 'i2': i2, 'size': len(flags),
                    'w': count[sel] * factor / self.nperm}

    def density_vector(self, adjacency: np.ndarray, weights=None) -> np.ndarray:
        """Return the induced densities of order L of a step graphon.

        Without weights the graph must be vertex-transitive: tuples fix their
        first vertex at 0. With weights every tuple is weighted by its product.
        """
        n = len(adjacency)
        free = self.order - 1 if weights is None else self.order
        total = n ** free
        powers = n ** np.arange(free - 1, -1, -1, dtype=np.int64)
        out = np.zeros(self.count)
        for start in range(0, total, 1 << 20):
            index = np.arange(start, min(total, start + (1 << 20)), dtype=np.int64)
            tuples = (index[:, None] // powers[None, :]) % n
            if weights is None:
                tuples = np.concatenate([np.zeros((len(index), 1), dtype=np.int64), tuples], axis=1)
            code = np.zeros(len(index), dtype=np.int64)
            for bit, (i, j) in enumerate(pairs_of(self.order)):
                code |= adjacency[tuples[:, i], tuples[:, j]] << bit
            position = np.searchsorted(self.codes, code)
            position = np.minimum(position, len(self.codes) - 1)
            if not (self.codes[position] == code).all():
                raise RuntimeError('a sampled graph is not triangle-free')
            mass = None if weights is None else np.prod(np.asarray(weights)[tuples], axis=1)
            out += np.bincount(self.classes[position], weights=mass, minlength=self.count)
        return out / total if weights is None else out

    def block_matrix(self, block, y: np.ndarray) -> np.ndarray:
        """Return the moment matrix of a square block at a state y."""
        size = block['size']
        flat = np.bincount(block['i1'] * size + block['i2'], weights=block['w'] * y[block['h']],
                           minlength=size * size)
        matrix = flat.reshape(size, size)
        return (matrix + matrix.T) / 2

    def block_row(self, block, v: np.ndarray) -> np.ndarray:
        """Return the coefficients of the square of the flag combination v."""
        return np.bincount(block['h'], weights=block['w'] * v[block['i1']] * v[block['i2']],
                           minlength=self.count)

    def multiplier(self, family, ti: int, g: tuple) -> np.ndarray:
        """Return the multiplier value on every record of one type."""
        d = family['data'][ti]
        kind = g[0]
        if kind == 'one':
            return np.ones(len(d['w']))
        if kind == 'class':
            return (d['z1'] == g[1]).astype(float)
        if kind == 'p-a':
            return d['ez'] - self.low
        if kind == 'b-p':
            return self.high - d['ez']
        if kind == 'degree':
            i, c = g[1], g[2]
            return (((d['z1'] >> i) & 1) - c) * (((d['z2'] >> i) & 1) - c)
        if kind == 'square':
            v = np.zeros(1 << family['k'])
            v[list(g[1])] = g[2]
            return v[d['z1']] * v[d['z2']]
        raise ValueError(g)

    def multipliers(self) -> list[tuple[dict, int, tuple]]:
        """Return the fixed multiplier list of every family and type."""
        out = []
        for family in self.families:
            for ti, profiles in enumerate(family['profiles']):
                if family['m'] == 0:
                    out.append((family, ti, ('one',)))
                    continue
                out += [(family, ti, ('class', r)) for r in profiles]
                if family['m'] == 2:
                    out += [(family, ti, ('p-a',)), (family, ti, ('b-p',))]
                    out += [(family, ti, ('degree', i, c)) for i in range(family['k'])
                            for c in DEGREE_GRID]
        return out

    def aggregate(self, family, ti: int, g: tuple, y: np.ndarray) -> tuple[np.ndarray, float]:
        """Return the edge-weight table over profile pairs and the multiplier mass at y."""
        d = family['data'][ti]
        size = 1 << family['k']
        weight = self.multiplier(family, ti, g) * d['w'] * y[d['h']]
        table = np.bincount(d['px'] * size + d['py'], weights=weight * d['e'], minlength=size * size)
        return table.reshape(size, size), float(weight.sum())

    def row(self, family, ti: int, g: tuple, same: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """Return the coefficient vectors S and N of the row S - t N."""
        d = family['data'][ti]
        weight = self.multiplier(family, ti, g) * d['w']
        s = np.bincount(d['h'], weights=weight * d['e'] * same[d['px'], d['py']], minlength=self.count)
        n = np.bincount(d['h'], weights=weight, minlength=self.count)
        return s, n


def same_side(k: int, profiles: list[int], mask: int, q: float | None = None) -> np.ndarray:
    """Return P(same side) over profile pairs; bit i of mask is the side of profiles[i].

    With q, each point of the zero class goes to side 1 with probability q.
    """
    side = np.zeros(1 << k, dtype=int)
    for i, profile in enumerate(profiles):
        side[profile] = (mask >> i) & 1
    same = (side[:, None] == side[None, :]).astype(float)
    if q is not None:
        same[0, :] = np.where(side == 1, q, 1 - q)
        same[:, 0] = same[0, :]
        same[0, 0] = q * q + (1 - q) ** 2
    return same


def cheapest_rule(table: np.ndarray, profiles: list[int], limit: int = 17,
                  seed: int = 0) -> tuple[float, int]:
    """Return the least cost and its mask: exhaustive up to ``limit`` profiles, else local search."""
    m = len(profiles)
    w = table[np.ix_(profiles, profiles)]
    w = w + w.T
    iu, ju = np.triu_indices(m, 1)
    pair = w[iu, ju]
    diagonal = np.trace(w) / 2
    if m <= limit:
        best = (np.inf, 0)
        masks = np.arange(1 << (m - 1), dtype=np.int64) << 1
        for start in range(0, len(masks), 1 << 13):
            block = masks[start:start + (1 << 13)]
            same = (((block[:, None] >> iu[None, :]) ^ (block[:, None] >> ju[None, :])) & 1) == 0
            cost = same @ pair
            a = int(np.argmin(cost))
            if cost[a] < best[0]:
                best = (float(cost[a]), int(block[a]))
        return best[0] + diagonal, best[1]
    rng = np.random.default_rng(seed)
    full = np.zeros((m, m))
    full[iu, ju] = pair
    full = full + full.T
    best = (np.inf, 0)
    for _ in range(80):
        s = rng.choice([-1, 1], m)
        while True:
            gain = (full @ s) * s
            i = int(np.argmax(gain))
            if gain[i] <= 1e-15:
                break
            s[i] = -s[i]
        if s[0] == 1:
            s = -s
        side = (s > 0).astype(int)
        cost = float(pair[side[iu] == side[ju]].sum())
        if cost < best[0]:
            best = (cost, int(sum(int(side[i]) << i for i in range(m))))
    return best[0] + diagonal, best[1]


def coin_rules(table: np.ndarray, profiles: list[int]) -> list[tuple[float, int, float]]:
    """Return, for each coin probability, the cheapest rule with a coin on the zero class."""
    m = len(profiles)
    if m - 1 > 15:
        return []
    w = table[np.ix_(profiles, profiles)]
    w = w + w.T
    masks = np.arange(1 << (m - 1), dtype=np.int64) << 1
    bits = ((masks[:, None] >> np.arange(1, m)[None, :]) & 1).astype(float)
    upper = np.triu(w[1:, 1:], 1)
    i2, j2 = np.nonzero(upper)
    mono = (bits[:, i2] == bits[:, j2]).astype(float) @ upper[i2, j2]
    out = []
    for q in COINS:
        cost = w[0, 0] / 2 * (q * q + (1 - q) ** 2) + (bits * q + (1 - bits) * (1 - q)) @ w[0, 1:] + mono
        a = int(np.argmin(cost))
        out.append((float(cost[a]), int(masks[a]), q))
    return out


class Program:
    """Column generation for one system at varying thresholds."""

    def __init__(self, system: FlagSystem) -> None:
        self.system = system
        self.mults = system.multipliers()
        self.cut: list[tuple[tuple, np.ndarray, np.ndarray]] = []
        self.squares: list[tuple[tuple, np.ndarray]] = []

    def solve(self, t: float) -> tuple[float, np.ndarray, np.ndarray]:
        """Return eps, the dual state y and the column weights at threshold t."""
        columns = [s - t * n for _, s, n in self.cut] + [v for _, v in self.system.fixed]
        columns += [v for _, v in self.squares]
        scale = np.array([max(np.abs(v).max(), 1e-300) for v in columns])
        matrix = np.column_stack([v / sc for v, sc in zip(columns, scale)] + [np.ones(self.system.count)])
        cost = np.zeros(len(columns) + 1)
        cost[-1] = -1.0
        equality = np.zeros((1, len(columns) + 1))
        equality[0, :len(self.cut)] = 1.0
        bounds = [(0, None)] * len(columns) + [(None, None)]
        res = None
        for method in ('highs-ds', 'highs-ipm', 'highs'):
            res = linprog(cost, A_ub=matrix, b_ub=np.zeros(self.system.count), A_eq=equality, b_eq=[1.0],
                          bounds=bounds, method=method)
            if res.status == 0:
                break
        if res is None or res.status != 0:
            raise RuntimeError(f'linear program failed: {res.message if res is not None else ""}')
        weights = res.x[:-1] / scale
        return -res.fun, -res.ineqlin.marginals, weights

    def price(self, y: np.ndarray, t: float, eps: float) -> int:
        """Add every cut row and localizing square whose scaled value at y is below -eps."""
        added = 0

        def offer(label, s, n):
            nonlocal added
            v = s - t * n
            if not self.cut or float(y @ v) / max(np.abs(v).max(), 1e-300) < -eps - 1e-9:
                self.cut.append((label, s, n))
                added += 1

        for family, ti, g in self.mults:
            table, mass = self.system.aggregate(family, ti, g, y)
            profiles = family['profiles'][ti]
            candidates = [cheapest_rule(table, profiles) + (None,)]
            if family['m'] >= 1:
                candidates += coin_rules(table, profiles)
            for cost, mask, q in candidates:
                if cost - t * mass < 0:
                    same = same_side(family['k'], profiles, mask, q)
                    offer((family['k'], ti, g, mask, q), *self.system.row(family, ti, g, same))
        family = self.system.families[2]
        rules = {(label[1], label[3], label[4]) for label, _, _ in self.cut if label[0] == family['k']}
        for ti, mask, q in sorted(rules, key=str):
            d = family['data'][ti]
            profiles = family['profiles'][ti]
            same = same_side(family['k'], profiles, mask, q)
            weight = d['w'] * y[d['h']] * (d['e'] * same[d['px'], d['py']] - t)
            size = 1 << family['k']
            matrix = np.bincount(d['z1'] * size + d['z2'], weights=weight, minlength=size * size)
            matrix = matrix.reshape(size, size)
            matrix = ((matrix + matrix.T) / 2)[np.ix_(profiles, profiles)]
            values, vectors = np.linalg.eigh(matrix)
            if values[0] < 0:
                g = ('square', tuple(profiles), vectors[:, 0].copy())
                offer((family['k'], ti, ('square', tuple(profiles), tuple(np.round(vectors[:, 0], 6))), mask, q),
                      *self.system.row(family, ti, g, same))
        return added

    def prune(self, weights: np.ndarray, y: np.ndarray, t: float, eps: float) -> None:
        """Drop unused cut columns whose scaled reduced cost is large."""
        keep = []
        for i, (label, s, n) in enumerate(self.cut):
            v = s - t * n
            if weights[i] > 0 or float(y @ v) / max(np.abs(v).max(), 1e-300) + eps < 1e-6:
                keep.append((label, s, n))
        self.cut = keep

    def generate(self, t: float, rounds: int = 30, log=None) -> tuple[float, np.ndarray]:
        """Run column generation at threshold t; stop early once a certificate appears."""
        eps, y = 0.0, np.ones(self.system.count) / self.system.count
        for it in range(rounds):
            if self.cut:
                eps, y, weights = self.solve(t)
                self.prune(weights, y, t, eps)
                eps, y, weights = self.solve(t)
                if eps > 1e-7:
                    return eps, y
            added = self.price(y, t, eps if self.cut else -1.0)
            if log:
                log(f'  t={t:.5f} iteration {it}: eps={eps:.4e}, cut columns {len(self.cut)}, added {added}')
            if added == 0:
                break
        return eps, y

    def products(self, y: np.ndarray, t: float, best: int = 20) -> int:
        """Add products of two cut rows on the same roots whose value at y is negative.

        Under the hypothesis both factors are nonnegative for every root
        tuple, so the integrated product is a valid row. Every pair of
        deterministic rules of each type is scored at y; the most negative
        pairs are added.
        """
        family = self.system.families[2]
        k = family['k']
        if not hasattr(self, '_product_tables'):
            self._product_tables = self.system.product_tables()
        added = 0
        for ti, profiles in enumerate(family['profiles']):
            m = len(profiles)
            if m > 9:
                continue
            masks = np.arange(1 << (m - 1)) << 1
            keys = np.arange(1 << (2 * k + 1))
            px, py, e = keys >> (k + 1), (keys >> 1) & ((1 << k) - 1), keys & 1
            vectors = np.array([e * same_side(k, profiles, int(mask))[px, py] - t for mask in masks])
            d = self._product_tables[ti]
            size = len(keys)
            joint = np.bincount(d['first'] * size + d['second'], weights=d['w'] * y[d['h']],
                                minlength=size * size).reshape(size, size)
            values = vectors @ ((joint + joint.T) / 2) @ vectors.T
            for flat in np.argsort(values, axis=None)[:best]:
                a, b = np.unravel_index(flat, values.shape)
                row = np.bincount(d['h'], weights=d['w'] * vectors[a][d['first']] * vectors[b][d['second']],
                                  minlength=self.system.count)
                if float(y @ row) / max(np.abs(row).max(), 1e-300) < -1e-9:
                    self.squares.append((('product', ti, int(masks[a]), int(masks[b]), t), row))
                    added += 1
        return added

    def eigen_squares(self, y: np.ndarray, label: int) -> float:
        """Add squares of the three least eigenvectors of every negative block; return the least eigenvalue."""
        least = 0.0
        for key, block in self.system.blocks.items():
            values, vectors = np.linalg.eigh(self.system.block_matrix(block, y))
            least = min(least, values[0])
            for j in range(min(3, len(values))):
                if values[j] < -1e-10:
                    self.squares.append((('eigen', key, label, j), self.system.block_row(block, vectors[:, j])))
        return least
