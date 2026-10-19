"""Check finite host diagnostics of the complete bipartite size Ramsey lead.

Checked clauses:

0. Input scope. The stored witnesses have exactly the stated parameters,
   binary entries of the specified dimensions, and a simple red edge set on
   vertices 0 through 16 for the complete-host witness.
1. Capacities. For n = 2 (a = 3, 4, 5) and n = 3 (a = 5, ..., 14) the
   capacity cap(a, n) of Lemma 2, computed from exact binomials, equals the
   value the lead tabulates.
2. Complete bipartite witnesses. Each stored colouring of K_{a,b} (n = 2:
   (3,6), (4,6); n = 3: (5,40), (6,40), (7,28), (8,28), (9,22), (10,20),
   (11,18), (12,16), (13,15), (14,14)) has no monochromatic K_{n,n}. This is
   checked twice: by the red and blue loads of every n-set of columns
   (Lemma 1), and by the common red and common blue columns of every n-set of
   rows. For n = 3 and a = 5, 6, 7, 8, and for n = 2 and a = 3, 4, the
   witness has cap(a, n) rows, so B(a, n) = cap(a, n).
3. Counting thresholds. K_{3,7} and K_{4,7} (n = 2) and K_{7,29} (n = 3)
   satisfy the inequality of Lemma 2, so each is Ramsey.
4. Complete bipartite minima. Every K_{a,b} with a <= b and ab <= 20 (n = 2),
   or ab <= 202 (n = 3), gets a checked colouring: a general colouring for
   a <= 2 (n = 2) or a <= 4 (n = 3), otherwise the first rows of a stored
   witness. With clause 3, the cheapest complete bipartite Ramsey hosts have
   21 and 203 edges.
5. b(2) = 5. K_{4,4} has a checked colouring, and no five rows of length 5
   are pairwise compatible (two rows sharing at most one red and at most one
   blue column), checked over all sets of five of the 32 rows; so every
   colouring of K_{5,5} has a monochromatic K_{2,2}.
6. All hosts for n = 2. The graphs with minimum degree at least 3 and at
   most 14 edges are generated up to isomorphism (the networkx atlas up to
   7 vertices; one-vertex extensions for 8 and 9 vertices). Completeness is
   checked in every (vertices, edges) cell by the orbit count: the sum of
   v!/|Aut(G)| over the classes equals the number of labelled graphs in the
   cell, counted independently by degree sequences. Each class has a good
   colouring, found by enumeration and checked against every 4-cycle; K_6 is
   Ramsey for C_4 by enumeration of all 2^15 colourings. With the
   degree-reduction lemma on the lead page, Rhat(K_{2,2}) = 15.
7. The K_17 witness has no monochromatic K_{3,3}: every 3-set has at most 2
   common red and at most 2 common blue neighbours, and no pair of disjoint
   3-sets spans a monochromatic K_{3,3}.
8. The 30 affine hyperplanes of F_2^4 form a translation-invariant good
   colouring of K_{16,30} for n = 4. A specified affine plane has red and
   blue loads 3, disproving the proposed divisibility-by-four obstruction.
   The counting capacity is 78; optimality is not claimed.

Not checked here: the solver verdict that K_{9,23} has no good colouring,
the theorem r(K_{3,3}) = 18 that makes K_18 Ramsey, and the propositions of
the lead, whose proofs are on the page.

Run from the repository root:
    uv run --no-sync python wiki/research/leads/complete_bipartite_size_ramsey/evidence/main.py

Dependencies: networkx, numpy and the installed root ``tools`` package. Input:
``assets/witnesses.json`` (solver-found colourings, checked here, not
trusted). Deterministic; no output files. The run takes under a minute. Every
failed obligation exits nonzero, including under ``python -O``. Limitation:
these are finite checks at n = 2, 3 and 4; they say nothing about the
asymptotic order. Clauses 1 and 8 use exact integer arithmetic; the NumPy
uint32 colouring enumeration in clause 6 uses at most 15 bits.
"""

from __future__ import annotations

import itertools
import json
import math
import sys
from collections.abc import Callable
from functools import cache
from pathlib import Path

import networkx as nx
import numpy as np

from tools import Checker, evidence_parser

__all__ = [
    'main',
]

_ASSETS = Path(__file__).resolve().parent / 'assets' / 'witnesses.json'
_DESCRIPTION = (
    'Check finite host diagnostics of the complete bipartite size Ramsey lead.'
)
_BIPARTITE_SHAPES = {
    (2, 3, 6),
    (2, 4, 6),
    (3, 5, 40),
    (3, 6, 40),
    (3, 7, 28),
    (3, 8, 28),
    (3, 9, 22),
    (3, 10, 20),
    (3, 11, 18),
    (3, 12, 16),
    (3, 13, 15),
    (3, 14, 14),
}
# capacities as the lead tabulates them
_CAP = {
    2: {3: 6, 4: 6, 5: 5},
    3: {5: 40, 6: 40, 7: 28, 8: 28, 9: 24, 10: 24, 11: 22, 12: 22, 13: 20, 14: 20},
}
# witnesses that reach the capacity
_AT_CAP = {2: (3, 4), 3: (5, 6, 7, 8)}
# edge counts below which every complete bipartite host is coloured
_BELOW = {2: 20, 3: 202}
# hosts certified Ramsey by Lemma 2
_COUNTED = [(2, 3, 7), (2, 4, 7), (3, 7, 29)]


def check_asset_domain(checker: Checker, data: dict) -> bool:
    """Clause 0; reject missing, duplicate, out-of-domain or mislabelled witnesses."""
    bip = data.get('complete_bipartite', [])
    inventory = [(w.get('n'), w.get('a'), w.get('b')) for w in bip]
    scope = (
        len(inventory) == len(_BIPARTITE_SHAPES) and set(inventory) == _BIPARTITE_SHAPES
    )
    checker.check('complete bipartite witness inventory has the stated scope', scope)
    binary = all(
        isinstance(w.get('rows'), list)
        and isinstance(w.get('a'), int)
        and isinstance(w.get('b'), int)
        and len(w['rows']) == w['b']
        and all(
            isinstance(row, str) and len(row) == w['a'] and set(row) <= {'0', '1'}
            for row in w['rows']
        )
        for w in bip
    )
    checker.check(
        'bipartite witnesses have binary entries and the stated dimensions', binary
    )
    complete = data.get('complete', [])
    target = (
        len(complete) == 1 and complete[0].get('N') == 17 and complete[0].get('n') == 3
    )
    checker.check('complete witness has exactly the target K_17 for K_{3,3}', target)
    edges = complete[0].get('red_edges', []) if target else []
    simple = (
        target
        and isinstance(edges, list)
        and all(
            isinstance(e, list)
            and len(e) == 2
            and all(type(v) is int for v in e)
            and 0 <= e[0] < e[1] < 17
            for e in edges
        )
    )
    if simple:
        simple = len({tuple(e) for e in edges}) == len(edges)
    checker.check('K_17 red edges are distinct simple edges on vertices 0..16', simple)
    return scope and binary and target and simple


def capacity(a: int, n: int) -> int | None:
    """Return cap(a, n) of Lemma 2, or None when m(a, n) = 0."""
    m = min(math.comb(r, n) + math.comb(a - r, n) for r in range(a + 1))
    return None if m == 0 else (2 * (n - 1) * math.comb(a, n)) // m


def counted_ramsey(a: int, b: int, n: int) -> bool:
    """Return whether b m(a, n) > 2(n-1) C(a, n), the inequality of Lemma 2."""
    m = min(math.comb(r, n) + math.comb(a - r, n) for r in range(a + 1))
    return b * m > 2 * (n - 1) * math.comb(a, n)


def masks(rows: list[str]) -> list[int]:
    """Return each 0/1 row string as a bit mask over its columns."""
    return [sum(1 << i for i, ch in enumerate(row) if ch == '1') for row in rows]


def good_by_loads(rows: list[int], a: int, n: int) -> bool:
    """Return whether every n-set of columns has red and blue loads at most n-1."""
    for cols in itertools.combinations(range(a), n):
        s = sum(1 << i for i in cols)
        red = sum(1 for r in rows if r & s == s)
        blue = sum(1 for r in rows if r & s == 0)
        if red >= n or blue >= n:
            return False
    return True


def good_by_rows(rows: list[int], a: int, n: int) -> bool:
    """Return whether every n-set of rows has fewer than n common red and n common blue columns."""
    full = (1 << a) - 1
    for t in itertools.combinations(rows, n):
        red = full
        blue = full
        for r in t:
            red &= r
            blue &= full & ~r
        if red.bit_count() >= n or blue.bit_count() >= n:
            return False
    return True


def general_rows(n: int, b: int) -> list[int]:
    """Return b copies of a row that is constant on no n-set of at most 2n - 2 columns."""
    # first n - 1 columns red, the rest blue: at most n - 1 columns of each colour
    return [sum(1 << i for i in range(n - 1))] * b


def c4_masks(g: nx.Graph, eid: dict[frozenset, int]) -> list[int]:
    """Return the edge masks of the 4-cycles of g, each once."""
    out = set()
    for quad in itertools.combinations(sorted(g.nodes()), 4):
        w, x, y, z = quad
        for cyc in ((w, x, y, z), (w, x, z, y), (w, y, x, z)):
            es = [frozenset((cyc[i], cyc[(i + 1) % 4])) for i in range(4)]
            if all(e in eid for e in es):
                out.add(sum(1 << eid[e] for e in es))
    return sorted(out)


def all_colourings_bad(m: int, cycles: list[int]) -> np.ndarray:
    """Return, for each of the 2^m colourings, whether some 4-cycle is monochromatic."""
    cols = np.arange(1 << m, dtype=np.uint32)
    full = np.uint32((1 << m) - 1)
    bad = np.zeros(1 << m, dtype=bool)
    for mk in cycles:
        mk = np.uint32(mk)
        bad |= (cols & mk) == mk
        bad |= ((~cols) & full & mk) == mk
    return bad


def no_mono_c4(g: nx.Graph, red: set[frozenset]) -> bool:
    """Return whether no 4-cycle of g is monochromatic, by direct enumeration."""
    nodes = sorted(g.nodes())
    for w, x, y, z in itertools.permutations(nodes, 4):
        if not (w < x and w < y and w < z and x < z):
            continue
        es = [frozenset(p) for p in ((w, x), (x, y), (y, z), (z, w))]
        if all(g.has_edge(*tuple(e)) for e in es):
            colours = {e in red for e in es}
            if len(colours) == 1:
                return False
    return True


def dedupe(graphs: list[nx.Graph]) -> list[nx.Graph]:
    """Return one representative of each isomorphism class."""
    buckets: dict[tuple, list[nx.Graph]] = {}
    out = []
    for g in graphs:
        key = (
            g.number_of_nodes(),
            g.number_of_edges(),
            tuple(sorted(d for _, d in g.degree())),
        )
        lst = buckets.setdefault(key, [])
        if any(nx.is_isomorphic(g, h) for h in lst):
            continue
        lst.append(g)
        out.append(g)
    return out


def extend(base: list[nx.Graph], keep: Callable[[nx.Graph], bool]) -> list[nx.Graph]:
    """Return the classes of graphs obtained by adding one vertex to a base graph."""
    out = []
    for g in base:
        v = g.number_of_nodes()
        for r in range(v + 1):
            for nbrs in itertools.combinations(range(v), r):
                h = nx.convert_node_labels_to_integers(g)
                h.add_node(v)
                h.add_edges_from((v, u) for u in nbrs)
                if keep(h):
                    out.append(h)
    return dedupe(out)


def mindeg(g: nx.Graph) -> int:
    """Return the minimum degree of a nonempty graph."""
    return min(d for _, d in g.degree())


def host_class() -> list[nx.Graph]:
    """Return the classes with minimum degree >= 3 and at most 14 edges."""
    atlas = nx.graph_atlas_g()
    small = [
        g
        for g in atlas
        if g.number_of_nodes() >= 4 and mindeg(g) >= 3 and g.number_of_edges() <= 14
    ]
    seven = [g for g in atlas if g.number_of_nodes() == 7]
    eight = extend(seven, lambda h: mindeg(h) >= 3 and h.number_of_edges() <= 14)
    # a 9-vertex member has degrees (4, 3^8); deleting a degree-3 vertex leaves 11 edges, degrees 2..4
    seven11 = [g for g in seven if g.number_of_edges() <= 11]
    eight11 = extend(
        seven11,
        lambda h: (
            h.number_of_edges() == 11
            and mindeg(h) >= 2
            and max(d for _, d in h.degree()) <= 4
        ),
    )
    nine = extend(eight11, lambda h: h.number_of_edges() == 14 and mindeg(h) >= 3)
    return small + eight + nine


@cache
def labelled_by_degrees(degs: tuple[int, ...]) -> int:
    """Return the number of labelled simple graphs with this sorted degree sequence."""
    if not degs:
        return 1
    d0, rest = degs[0], degs[1:]
    total = 0
    for nbrs in itertools.combinations(range(len(rest)), d0):
        res = list(rest)
        ok = True
        for j in nbrs:
            res[j] -= 1
            if res[j] < 0:
                ok = False
                break
        if ok:
            total += labelled_by_degrees(tuple(sorted(res)))
    return total


def labelled_count(v: int, m: int) -> int:
    """Return the number of labelled graphs on v vertices with m edges and minimum degree >= 3."""
    total = 0
    for degs in itertools.combinations_with_replacement(range(3, v), v):
        if sum(degs) != 2 * m:
            continue
        perms = math.factorial(v)
        for k in set(degs):
            perms //= math.factorial(degs.count(k))
        total += perms * labelled_by_degrees(tuple(sorted(degs)))
    return total


def automorphisms(g: nx.Graph) -> int:
    """Return |Aut(g)|."""
    return sum(
        1 for _ in nx.algorithms.isomorphism.GraphMatcher(g, g).isomorphisms_iter()
    )


def check_capacities(checker: Checker) -> None:
    """Clause 1."""
    for n, table in _CAP.items():
        for a, expected in table.items():
            got = capacity(a, n)
            checker.check(
                f'cap({a},{n}) = {expected}', got == expected, f'computed {got}'
            )


def check_complete_bipartite(
    checker: Checker, data: dict
) -> dict[tuple[int, int], list[int]]:
    """Clauses 2 to 4; return the checked witness rows keyed by (n, a)."""
    found: dict[tuple[int, int], list[int]] = {}
    for w in data['complete_bipartite']:
        n, a, b = w['n'], w['a'], w['b']
        rows = masks(w['rows'])
        shape = len(rows) == b and all(len(r) == a for r in w['rows'])
        checker.check(f'K_{{{a},{b}}} witness shape (n={n})', shape)
        checker.check(
            f'K_{{{a},{b}}} loads at most {n - 1} (n={n})', good_by_loads(rows, a, n)
        )
        checker.check(f'K_{{{a},{b}}} row sets (n={n})', good_by_rows(rows, a, n))
        found[(n, a)] = rows
    for n, cols in _AT_CAP.items():
        for a in cols:
            rows = found.get((n, a), [])
            checker.check(
                f'B({a},{n}) = cap({a},{n}) = {_CAP[n][a]}', len(rows) == _CAP[n][a]
            )
    for n, a, b in _COUNTED:
        checker.check(
            f'K_{{{a},{b}}} Ramsey for K_{{{n},{n}}} by counting',
            counted_ramsey(a, b, n),
        )
    for n, limit in _BELOW.items():
        a = 1
        while a * a <= limit:
            b = limit // a
            if a < n:
                ok = True  # no n-set of columns exists
            elif capacity(a, n) is None:
                ok = good_by_loads(general_rows(n, b), a, n)
            else:
                rows = found.get((n, a), [])
                ok = len(rows) >= b and good_by_loads(rows[:b], a, n)
            checker.check(f'K_{{{a},{b}}} coloured (n={n}, ab <= {limit})', ok)
            a += 1
    return found


def check_b2(checker: Checker, found: dict[tuple[int, int], list[int]]) -> None:
    """Clause 5."""
    rows = found.get((2, 4), [])[:4]
    checker.check(
        'K_{4,4} coloured (n=2)', len(rows) == 4 and good_by_loads(rows, 4, 2)
    )
    full = 31
    ok_pair = [
        [
            (x & y).bit_count() <= 1 and (full & ~x & ~y).bit_count() <= 1
            for y in range(32)
        ]
        for x in range(32)
    ]
    five = any(
        all(ok_pair[x][y] for x, y in itertools.combinations(t, 2))
        for t in itertools.combinations(range(32), 5)
    )
    # equal rows are never compatible: a row shares its own red and blue columns
    repeat = any(ok_pair[x][x] for x in range(32))
    checker.check(
        'every colouring of K_{5,5} has a monochromatic K_{2,2}',
        not five and not repeat,
    )


def check_hosts_n2(checker: Checker) -> None:
    """Clause 6."""
    classes = dedupe(host_class())
    checker.check(
        'the exhaustive host class has 313 distinct representatives',
        len(classes) == 313,
    )
    cells: dict[tuple[int, int], int] = {}
    for g in classes:
        key = (g.number_of_nodes(), g.number_of_edges())
        cells[key] = cells.get(key, 0) + math.factorial(key[0]) // automorphisms(g)
    expected_cells = {
        (v, m)
        for v in range(4, 10)
        for m in range(0, 15)
        if 3 * v <= 2 * m <= v * (v - 1)
    }
    checker.check(
        'every generated host cell satisfies the vertex and edge bounds',
        set(cells) <= expected_cells,
    )
    for v, m in sorted(expected_cells):
        got = cells.get((v, m), 0)
        want = labelled_count(v, m)
        checker.check(
            f'orbit count v={v} m={m}: {want} labelled graphs',
            got == want,
            f'classes give {got}',
        )
    coloured = 0
    for g in classes:
        edges = [frozenset(e) for e in g.edges()]
        eid = {e: k for k, e in enumerate(edges)}
        bad = all_colourings_bad(len(edges), c4_masks(g, eid))
        idx = np.flatnonzero(~bad)
        if len(idx) == 0:
            continue
        red = {e for k, e in enumerate(edges) if (int(idx[0]) >> k) & 1}
        if no_mono_c4(g, red):
            coloured += 1
    checker.check(
        f'all {len(classes)} host classes have a good colouring',
        coloured == len(classes),
        f'{coloured} coloured',
    )
    k6 = nx.complete_graph(6)
    edges = [frozenset(e) for e in k6.edges()]
    eid = {e: k for k, e in enumerate(edges)}
    checker.check(
        'K_6 Ramsey for C_4 over all 2^15 colourings',
        bool(all_colourings_bad(15, c4_masks(k6, eid)).all()),
    )


def check_k17(checker: Checker, data: dict) -> None:
    """Clause 7."""
    w = data['complete'][0]
    N, n = w['N'], w['n']
    red = {frozenset(e) for e in w['red_edges']}
    valid = all(len(e) == 2 and max(e) < N for e in red)
    checker.check(f'K_{N} witness edges valid', valid)
    nbr_red = [
        {u for u in range(N) if u != v and frozenset((u, v)) in red} for v in range(N)
    ]
    nbr_blue = [set(range(N)) - nbr_red[v] - {v} for v in range(N)]
    ok_common = True
    for t in itertools.combinations(range(N), n):
        cr = set.intersection(*(nbr_red[v] for v in t))
        cb = set.intersection(*(nbr_blue[v] for v in t))
        if len(cr) >= n or len(cb) >= n:
            ok_common = False
            break
    checker.check(
        f'K_{N}: every {n}-set has < {n} common red and blue neighbours', ok_common
    )
    ok_pairs = True
    for s in itertools.combinations(range(N), n):
        rest = [x for x in range(N) if x not in s]
        for t in itertools.combinations(rest, n):
            if s > t:
                continue
            colours = {frozenset((x, y)) in red for x in s for y in t}
            if len(colours) == 1:
                ok_pairs = False
                break
        if not ok_pairs:
            break
    checker.check(
        f'K_{N}: no pair of disjoint {n}-sets spans a monochromatic K_{{{n},{n}}}',
        ok_pairs,
    )


def check_affine_hyperplanes(checker: Checker) -> None:
    """Clause 8: explicit construction, with no solver or numerical approximation."""
    rows = [
        sum(1 << x for x in range(16) if (u & x).bit_count() % 2 == c)
        for u in range(1, 16)
        for c in range(2)
    ]
    row_set = set(rows)
    checker.check(
        'F_2^4 has 30 distinct affine hyperplanes, each of size 8',
        len(row_set) == 30 and all(r.bit_count() == 8 for r in rows),
    )
    closed = all(
        sum(1 << (x ^ t) for x in range(16) if r & (1 << x)) in row_set
        for r in rows
        for t in range(16)
    )
    checker.check('the hyperplane family is invariant under every translation', closed)
    checker.check(
        'K_{16,30} hyperplane loads are at most 3', good_by_loads(rows, 16, 4)
    )
    checker.check(
        'K_{16,30} hyperplane row sets avoid K_{4,4}', good_by_rows(rows, 16, 4)
    )
    plane = sum(1 << x for x in (0, 1, 2, 3))
    red = sum(1 for r in rows if r & plane == plane)
    blue = sum(1 for r in rows if r & plane == 0)
    checker.check(
        'the plane {0,1,2,3} has loads (3,3), not divisible by 4', (red, blue) == (3, 3)
    )
    checker.check('cap(16,4) = 78', capacity(16, 4) == 78)


def main() -> int:
    """Run every clause and return the exit code."""
    evidence_parser(_DESCRIPTION, quick=False).parse_args()
    checker = Checker()
    data = json.loads(_ASSETS.read_text())
    if not check_asset_domain(checker, data):
        return checker.finish()
    check_capacities(checker)
    found = check_complete_bipartite(checker, data)
    check_b2(checker, found)
    check_hosts_n2(checker)
    check_k17(checker, data)
    check_affine_hyperplanes(checker)
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
