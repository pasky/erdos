"""Four-colour sample space for two independent active maximum cuts.

The two bits of a colour are the two cut colours. We quotient only by
vertex permutations, independent global complements of the two cuts and
exchange of the two cuts (eight colour transformations), not arbitrary S4.
All numerical coefficient arrays average every labelled tuple in that orbit.
"""

from __future__ import annotations

import itertools
import time
from collections import OrderedDict
from functools import cache

import numpy as np

START = time.monotonic()


def log(s: str) -> None:
    """Print a discovery progress message with elapsed time."""
    print(f'{time.monotonic() - START:.1f}s {s}', flush=True)


def pairs(n: int) -> list[tuple[int, int]]:
    """List unordered position pairs in the code-bit order."""
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def colour_maps() -> list[np.ndarray]:
    """The eight complements and exchanges of the two cut coordinates."""
    return [
        np.array(
            [
                (((c >> swap) & 1) ^ a) + 2 * (((c >> (1 - swap)) & 1) ^ b)
                for c in range(4)
            ],
            np.uint8,
        )
        for swap, a, b in itertools.product((0, 1), repeat=3)
    ]


@cache
def destinations(n: int) -> np.ndarray:
    """Destinations of edge and colour bits under vertex permutations."""
    pp = pairs(n)
    idx = {p: i for i, p in enumerate(pp)}
    edge = len(pp)
    out = []
    for pi in itertools.permutations(range(n)):
        d = [idx[tuple(sorted((pi[i], pi[j])))] for i, j in pp]
        d += [edge + 2 * pi[i] + b for i in range(n) for b in (0, 1)]
        out.append(d)
    return np.array(out, np.int64)


def permute(
    codes: np.ndarray | tuple[int, ...], n: int, colour_group: bool = True
) -> np.ndarray:
    """Return all permitted relabellings of each graph code."""
    edge = n * (n - 1) // 2
    dest = destinations(n)
    codes = np.asarray(codes, np.int64)
    out = np.zeros((len(codes), len(dest)), np.int64)
    w = np.int64(1) << dest
    for b in range(edge + 2 * n):
        out += ((codes[:, None] >> b) & 1) * w[None, :, b]
    if not colour_group:
        return out
    transforms = []
    for cmap in colour_maps():
        value = out & ((1 << edge) - 1)
        for i in range(n):
            value = value | (
                cmap[(out >> (edge + 2 * i)) & 3].astype(np.int64) << (edge + 2 * i)
            )
        transforms.append(value)
    return np.concatenate(transforms, axis=1)


def decode(code: int, n: int) -> tuple[np.ndarray, np.ndarray]:
    """Decode the adjacency matrix and two-bit vertex colours."""
    a = np.zeros((n, n), np.uint8)
    for b, (i, j) in enumerate(pairs(n)):
        a[i, j] = a[j, i] = (code >> b) & 1
    e = n * (n - 1) // 2
    c = np.array([(code >> (e + 2 * i)) & 3 for i in range(n)], np.uint8)
    return a, c


def encode(a: np.ndarray, c: np.ndarray) -> int:
    """Encode an adjacency matrix and two-bit vertex colours."""
    n = len(c)
    e = n * (n - 1) // 2
    return sum(int(a[i, j]) << b for b, (i, j) in enumerate(pairs(n))) + sum(
        int(c[i]) << (e + 2 * i) for i in range(n)
    )


@cache
def representatives(n: int) -> tuple[int, ...]:
    """Enumerate triangle-free graphs modulo vertex and cut symmetries."""
    if not 0 <= n <= 6:
        raise ValueError('This discovery implementation supports at most six points')
    if n == 0:
        return (0,)
    if n == 1:
        return (0,)
    old = representatives(n - 1)
    candidates = set()
    for code in old:
        a, c = decode(code, n - 1)
        for mask in range(1 << (n - 1)):
            nbr = [i for i in range(n - 1) if mask >> i & 1]
            if any(a[i, j] for i, j in itertools.combinations(nbr, 2)):
                continue
            new = np.zeros((n, n), np.uint8)
            new[:-1, :-1] = a
            new[nbr, n - 1] = new[n - 1, nbr] = 1
            for col in range(4):
                candidates.add(encode(new, np.r_[c, col]))
    out = set()
    codes = np.array(sorted(candidates), np.int64)
    for start in range(0, len(codes), 256):
        out.update(permute(codes[start : start + 256], n).min(axis=1).tolist())
    result = tuple(sorted(out))
    log(f'paired representatives order {n}: {len(result)} from {len(codes)} extensions')
    return result


class Table:
    """Every ordering and allowed cut relabelling of each sampled graph."""

    def __init__(self, n: int) -> None:
        """Build the finite table with a bounded cache of rooted flag indices."""
        if not 1 <= n <= 6:
            raise ValueError('The table supports one through six points')
        self.n = n
        self.reps = representatives(n)
        raw = permute(self.reps, n)
        self.count, self.orderings = raw.shape
        self.codes = raw.reshape(-1).astype(np.uint32)
        self.tuples = len(self.codes)
        self.index = {p: i for i, p in enumerate(pairs(n))}
        edge = len(self.index)
        self.colours = np.array(
            [((self.codes >> (edge + 2 * i)) & 3) for i in range(n)], np.uint8
        ).T.copy()
        self.graph = np.repeat(
            np.arange(self.count, dtype=np.int16 if self.count < 32768 else np.int32),
            self.orderings,
        )
        self.cache = OrderedDict()
        log(
            f'paired table {self.count} graphs, {self.tuples} '
            'ordered and colour-transformed tuples'
        )

    def adj(self, i: int, j: int) -> np.ndarray:
        """Read one adjacency bit for every ordered tuple."""
        return ((self.codes >> self.index[tuple(sorted((i, j)))]) & 1).astype(np.uint8)

    def same(self, i: int, j: int, cut: int = 0) -> np.ndarray:
        """Whether two positions have the same colour in the specified cut."""
        return ((self.colours[:, i] >> cut) & 1) == ((self.colours[:, j] >> cut) & 1)

    def flag(
        self, pos: tuple[int, ...], roots: int, mode: str = 'both'
    ) -> tuple[np.ndarray, np.ndarray]:
        """Canonical rooted flags, keeping both, second, or neither cut colour."""
        # For mode='second', retain only the second cut's colour; uncoloured
        # mode retains neither. Both modes keep the graph edges unchanged.
        key = (pos, roots, mode)
        if key in self.cache:
            return self.cache[key]
        q = len(pos)
        pp = pairs(q)
        edge = len(pp)
        bits = 2 if mode == 'both' else int(mode == 'second')
        raw = np.zeros(self.tuples, np.uint32)
        for b, (i, j) in enumerate(pp):
            raw |= self.adj(pos[i], pos[j]).astype(np.uint32) << b
        for i, x in enumerate(pos):
            if mode == 'both':
                raw |= self.colours[:, x].astype(np.uint32) << (edge + 2 * i)
            elif mode == 'second':
                raw |= (self.colours[:, x].astype(np.uint32) >> 1) << (edge + i)
        codes = np.unique(raw)
        best = codes.copy()
        idx = {p: i for i, p in enumerate(pp)}
        for tail in itertools.permutations(range(roots, q)):
            pi = tuple(range(roots)) + tail
            z = np.zeros_like(codes)
            for b, (i, j) in enumerate(pp):
                z |= ((codes >> b) & 1) << idx[tuple(sorted((pi[i], pi[j])))]
            for i in range(q):
                if bits:
                    z |= ((codes >> (edge + bits * i)) & ((1 << bits) - 1)) << (
                        edge + bits * pi[i]
                    )
            np.minimum(best, z, out=best)
        canonical, mp = np.unique(best, return_inverse=True)
        lookup = np.zeros(1 << (edge + bits * q), np.int32)
        lookup[codes] = mp
        result = (lookup[raw], canonical)
        self.cache[key] = result
        if self.n >= 6:
            while len(self.cache) > 2:
                self.cache.popitem(last=False)
        return result

    def row(self, value: np.ndarray) -> np.ndarray:
        """Average a labelled-tuple quantity on every graph class."""
        return (
            np.bincount(self.graph, weights=value, minlength=self.count)
            / self.orderings
        )
