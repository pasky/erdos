"""Exact, bounded diagnostics for palette and graph-coloring arguments.

No graph census or list-assignment search is performed. The unbounded
arguments are on the owning research page. The palette computation checks necessary
conditions at k=4, v<=26; the Specker check exhausts the C(20,6) edge order
patterns on coordinates 0..19; the Toft check verifies explicit colorings
for s=3,5,7 and every edge deletion. No randomness or floating point is used.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from itertools import combinations
from math import comb

from tools import Checker, evidence_parser


def choose(n: int, k: int) -> int:
    """Return a binomial coefficient, with zero outside the valid lower range."""
    return comb(n, k) if 0 <= k <= n else 0


def palette_checks(checker: Checker) -> None:
    """Recompute the exact palette bounds and necessary order-26 restrictions."""
    expected = [
        70,
        70,
        42,
        42,
        33,
        33,
        Fraction(143, 5),
        Fraction(143, 5),
        26,
        26,
        Fraction(170, 7),
    ]
    actual = []
    for palette in range(7, 18):
        middle = palette // 2
        bound = Fraction(
            2 * comb(palette, middle),
            choose(palette - 4, middle) + choose(palette - 4, middle - 4),
        )
        incidence = (palette * ((palette - 1 + 2) // 3) + 3) // 4
        actual.append(bound)
        checker.check(f'palette N={palette} excludes v<=25', max(bound, incidence) > 25)
        print(f'    N={palette}: midpoint bound={bound}, incidence bound={incidence}')
    checker.check('exact midpoint table N=7..17', actual == expected)
    checker.check('pair coverage excludes N>=18 at v<=25', comb(18, 2) > 6 * 25)

    # At v=26 pair coverage gives N<=18. The degree-incidence condition
    # excludes 18. Cover every layer and forbid an equality that necessarily
    # counts the same bad subset at least twice on a side with >=2 lists.
    candidates = []
    for palette in range(7, 19):
        if palette * ((palette - 1 + 2) // 3) > 4 * 26:
            continue
        for left in range(1, 26):
            right = 26 - left
            possible = True
            for size in range(palette + 1):
                bad_count = left * choose(palette - 4, size) + right * choose(
                    palette - 4, size - 4
                )
                total = comb(palette, size)
                if bad_count < total:
                    possible = False
                # Two 4-lists have union of size at most eight.
                forced_overlap = (left >= 2 and size <= palette - 8) or (
                    right >= 2 and size >= 8
                )
                if bad_count == total and forced_overlap:
                    possible = False
            if possible:
                candidates.append((palette, left, right))
    expected_candidates = [(17, a, 26 - a) for a in range(11, 16)]
    checker.check(
        '26-vertex necessary conditions leave only N=17, sides 11..15',
        candidates == expected_candidates,
        repr(candidates),
    )
    print(f'    surviving necessary-condition triples: {candidates}')


def specker_color(triple: tuple[int, int, int]) -> tuple[int, int]:
    """Color an increasing triple by its outer split and its middle bit."""
    low, middle, high = triple
    position = (low ^ high).bit_length() - 1
    return position, (middle >> position) & 1


def specker_checks(checker: Checker) -> None:
    """Exhaust the explicit six-coordinate edge pattern on coordinates 0 through 19."""
    examined = 0
    first_failure = None
    for a, b, c, d, e, f in combinations(range(20), 6):
        x = (a, b, d)
        y = (c, e, f)
        examined += 1
        if specker_color(x) == specker_color(y) and first_failure is None:
            first_failure = (x, y)
    checker.check(
        'all 38760 Specker edge patterns on coordinates 0..19 covered',
        examined == comb(20, 6) == 38760,
    )
    checker.check(
        'dyadic color separates every tested Specker edge',
        first_failure is None,
        repr(first_failure),
    )
    colors = [specker_color(t) for t in combinations(range(20), 3)]
    checker.check(
        'all tested triple colors lie in five levels times two bits',
        all(0 <= p < 5 and b in (0, 1) for p, b in colors),
    )


def toft_edges(size: int) -> set[tuple[int, int]]:
    """Construct the cycle, matching and complete cross edges of the Toft graph."""
    edges = set()
    for offset in (0, size):
        for i in range(size):
            edges.add(tuple(sorted((offset + i, offset + (i + 1) % size))))
    for i in range(size):
        edges.add((i, 2 * size + i))
        edges.add((size + i, 3 * size + i))
    for i in range(size):
        for j in range(size):
            edges.add((2 * size + i, 3 * size + j))
    return edges


def odd_cycle_coloring(size: int) -> list[int]:
    """Give a proper three-coloring of a cycle of odd size at least three."""
    return [i % 2 + 1 for i in range(size - 1)] + [3]


def path_around_vertex(
    size: int, at: int, single: int, first: int, second: int
) -> list[int]:
    """Color one cycle vertex separately and alternate along the remaining path."""
    colors = [0] * size
    colors[at] = single
    for step in range(1, size):
        colors[(at + step) % size] = first if step % 2 else second
    return colors


def deletion_coloring(size: int, deleted: tuple[int, int]) -> list[int]:
    """Construct a three-coloring after any one Toft edge is deleted."""
    u, v = deleted
    # Use the symmetry (A,X)<->(B,Y) for edges in the second half.
    if (size <= u < 2 * size and size <= v < 2 * size) or (
        size <= u < 2 * size and 3 * size <= v < 4 * size
    ):

        def swap(vertex: int) -> int:
            block, index = divmod(vertex, size)
            return (block ^ 1) * size + index

        switched = tuple(sorted((swap(u), swap(v))))
        base = deletion_coloring(size, switched)
        return [base[swap(vertex)] for vertex in range(4 * size)]

    b = odd_cycle_coloring(size)
    y = [2 if color == 1 else 1 for color in b]
    if u < size and v < size:
        # Deleted cycle edge: start the remaining path at its later endpoint
        # in the cyclic orientation, including the wraparound edge.
        start = v if (u + 1) % size == v else u
        a = [0] * size
        for step in range(size):
            a[(start + step) % size] = step % 2 + 1
        return a + b + [3] * size + y
    if u < size and 2 * size <= v < 3 * size:
        a = path_around_vertex(size, u, 3, 1, 2)
        return a + b + [3] * size + y
    if 2 * size <= u < 3 * size and 3 * size <= v < 4 * size:
        i, j = u - 2 * size, v - 3 * size
        a = path_around_vertex(size, i, 1, 2, 3)
        b = path_around_vertex(size, j, 2, 1, 3)
        x, y = [1] * size, [2] * size
        x[i] = y[j] = 3
        return a + b + x + y
    raise ValueError(f'unclassified edge {deleted}')


def toft_checks(checker: Checker) -> None:
    """Verify graph counts and every supplied deletion coloring at the retained sizes."""
    for size in (3, 5, 7):
        edges = toft_edges(size)
        vertices = range(4 * size)
        degrees = [sum(v in edge for edge in edges) for v in vertices]
        checker.check(
            f'Toft s={size}: exact size, edge count and degree sequence',
            len(edges) == size * size + 4 * size
            and degrees == [3] * (2 * size) + [size + 1] * (2 * size),
        )
        a = b = odd_cycle_coloring(size)
        y = [2 if color == 1 else 1 for color in b]
        colors = a + b + [4] * size + y
        checker.check(
            f'Toft s={size}: supplied four-coloring is proper',
            len(colors) == 4 * size and all(colors[u] != colors[v] for u, v in edges),
        )
        failures = []
        for deleted in sorted(edges):
            colors = deletion_coloring(size, deleted)
            if (
                len(colors) != 4 * size
                or not set(colors) <= {1, 2, 3}
                or any(colors[u] == colors[v] for u, v in edges if (u, v) != deleted)
            ):
                failures.append(deleted)
        checker.check(
            f'Toft s={size}: proper three-coloring after each of {len(edges)} edge deletions',
            not failures,
            repr(failures),
        )
    # Non-three-colorability is proved by disjoint color sets on X,Y in
    # the owning research page; this finite witness driver does not claim a SAT refutation.


def main() -> int:
    """Run the finite diagnostics and return a failing status on disagreement."""
    evidence_parser(__doc__ or 'Graph coloring diagnostics', quick=False).parse_args()
    checker = Checker()
    palette_checks(checker)
    specker_checks(checker)
    toft_checks(checker)
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
