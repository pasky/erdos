"""Check finite Hadamard witnesses and the recursive probe-cut calculation.

Owner: ../sparse_ladder_profiles.md, construction and equations (1)--(2).
Domain: t = 2, 4, 16, 64; --quick omits 64. All arithmetic is integral.
Additional owner: ../recursive_probe_cuts.md, equation (6) and its table.
The cut recurrence runs through k=8 (k=4 with --quick), with independent
explicit-coloring comparisons through k=3 and graph construction through k=4.
Checks: graph simplicity, three-coloring, separated predecessor intervals,
balanced attachment degrees, Hadamard column orthogonality, the block
rounding inequality, and exhaustive small-cut comparisons.
Inputs: none; the displayed deterministic construction regenerates the graph.
Dependencies: Python standard library and the repository tools package.
Command from repository root:
  uv run --no-sync python \
    wiki/research/leads/linear_bipartization_countable_coloring/evidence/main.py
Expected runtime: below one minute on one core.
Limitations: no infinite graph is constructed; the arbitrary-t assertion uses
the owner's proof. The large-t lower bounds are not asserted exact optima.
The independent analytic review in this folder is outside these checks.
"""

from __future__ import annotations

import sys
from itertools import pairwise, product
from math import isqrt

from tools import Checker, evidence_parser


def witness(t: int) -> tuple[list[list[int]], list[tuple[int, int]]]:
    """Use characters 1,...,t of the binary vector space of order t squared."""
    rows = t * t
    matrix = [
        [1 if (row & column).bit_count() % 2 == 0 else -1 for column in range(1, t + 1)]
        for row in range(rows)
    ]
    edges = []
    for block in range(t):
        start = 2 * t * block
        edges.extend((start + a, start + t + b) for a in range(t) for b in range(t))
        counts = {1: 0, -1: 0}
        for row in range(rows):
            sign = matrix[row][block]
            side = 0 if sign == 1 else t
            old = start + side + counts[sign] % t
            counts[sign] += 1
            edges.append((old, 2 * t * t + row))
    return matrix, edges


def separated_order(n: int, edges: list[tuple[int, int]]) -> bool:
    """Compute actual reachable minima, independently of the proposed blocks."""
    earlier: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        earlier[v].append(u)
    least = list(range(n))
    for v, neighbors in enumerate(earlier):
        neighbors.sort()
        if any(u >= least[w] for u, w in pairwise(neighbors)):
            return False
        least[v] = min([v, *(least[u] for u in neighbors)])
    return True


def enumerate_beta(n: int, edges: list[tuple[int, int]]) -> int:
    """Enumerate every cut up to complementation; used only at n=12."""
    return min(
        sum(((mask >> u) & 1) == ((mask >> v) & 1) for u, v in edges)
        for mask in range(1 << (n - 1))
    )


def phase_beta(matrix: list[list[int]]) -> int:
    """Enumerate every proper block bipartition; used only at t<=4."""
    t = len(matrix[0])
    return min(
        sum((t - abs(sum(a * b for a, b in zip(row, signs)))) // 2 for row in matrix)
        for signs in product((-1, 1), repeat=t)
    )


def check_parameter(checker: Checker, t: int) -> None:
    """Check one Hadamard graph and all of its declared finite obligations."""
    matrix, edges = witness(t)
    rows = t * t
    old_count = 2 * rows
    n = 3 * rows
    label = f't={t}'
    checker.check(
        f'{label}: simple graph and exact sizes',
        len(edges) == 2 * t**3
        and len(set(edges)) == len(edges)
        and all(0 <= u < v < n for u, v in edges),
    )
    colors = [(v % (2 * t)) // t for v in range(old_count)] + [2] * rows
    checker.check(
        f'{label}: proper three-coloring', all(colors[u] != colors[v] for u, v in edges)
    )
    checker.check(
        f'{label}: separated predecessor intervals', separated_order(n, edges)
    )
    checker.check(
        f'{label}: balanced orthogonal columns',
        all(sum(row[i] for row in matrix) == 0 for i in range(t))
        and all(
            sum(row[i] * row[j] for row in matrix) == (rows if i == j else 0)
            for i in range(t)
            for j in range(i, t)
        ),
    )
    attachment_degrees = [0] * old_count
    apex_blocks: list[list[int]] = [[] for _ in range(rows)]
    incidence_ok = True
    for u, v in edges:
        if v >= old_count:
            block, within = divmod(u, 2 * t)
            row = v - old_count
            incidence_ok &= (1 if within < t else -1) == matrix[row][block]
            attachment_degrees[u] += 1
            apex_blocks[row].append(block)
    checker.check(
        f'{label}: exact apex attachments and old degrees',
        incidence_ok
        and all(degree == t // 2 for degree in attachment_degrees)
        and all(sorted(blocks) == list(range(t)) for blocks in apex_blocks),
    )
    checker.check(
        f'{label}: every block rounding count',
        all(
            2 * (t * (x + y) - 2 * x * y) >= t * (x + y)
            for x in range(t + 1)
            for y in range(t + 1 - x)
        ),
    )
    if t <= 4:
        exact_phase_cost = phase_beta(matrix)
        # Squared Cauchy--Schwarz, with no numerical square root.
        checker.check(
            f'{label}: exhaustive block phases satisfy the bound',
            (rows * t - 2 * exact_phase_cost) ** 2 <= rows * rows * t,
        )
        if t == 2:
            checker.check(
                't=2: every graph cut agrees with the rounded phase optimum',
                enumerate_beta(n, edges) == exact_phase_cost,
            )
    root = isqrt(t)
    if root * root == t:
        bound = rows * (t - root) // 2
        checker.check(
            f'{label}: integral lower-bound arithmetic', 2 * bound == rows * (t - root)
        )
        if t == 16:
            checker.check(
                't=16: 1536 certified edges on 768 vertices', (bound, n) == (1536, 768)
            )
        if t == 64:
            checker.check(
                't=64: 114688 certified edges on 12288 vertices',
                (bound, n) == (114688, 12288),
            )


def probe_graph(k: int) -> tuple[int, list[tuple[int, int]], list[tuple[int, ...]]]:
    """Explicit graph construction, used only at small levels."""
    if k == 1:
        return 1, [], [(0,)]
    n, edges, probes = probe_graph(k - 1)
    result_edges = list(edges)
    result_probes = []
    count = n
    for base_probe in probes:
        offset = count
        count += n
        result_edges.extend((u + offset, v + offset) for u, v in edges)
        for probe in probes:
            copied = tuple(v + offset for v in probe)
            added = count
            count += 1
            result_edges.extend((v, added) for v in copied)
            result_probes.extend((base_probe + copied, (*base_probe, added)))
    return count, result_edges, result_probes


class ProbeCuts:
    """Integer implementation of the proved cut-potential recurrence."""

    def __init__(self, last: int) -> None:
        """Prepare finite count domains and an instance-owned memo table."""
        self.pairs = {1: ((0, 1), (1, 0))}
        self.counts = {1: (1, 0, 1, 1)}
        self._cache: dict[tuple[int, tuple[int, ...]], int] = {}
        for k in range(2, last + 1):
            n, m, p, s = self.counts[k - 1]
            self.counts[k] = (
                (p + 1) * n + p * p,
                (p + 1) * m + p * s,
                2 * p * p,
                3 * p * s + p * p,
            )
            sizes = {a + b for a, b in self.pairs[k - 1]}
            next_sizes = {s + 1 for s in sizes} | {s + t for s in sizes for t in sizes}
            self.pairs[k] = tuple(
                sorted((a, s - a) for s in next_sizes for a in range(s + 1))
            )

    def evaluate(self, k: int, values: tuple[int, ...]) -> int:
        """Evaluate a potential after constant-shift and complement reduction."""
        least = min(values)
        normalized = tuple(v - least for v in values)
        mapping = dict(zip(self.pairs[k], normalized))
        swapped = tuple(mapping[b, a] for a, b in self.pairs[k])
        # A constant shifts every probe penalty. Complementing the whole cut
        # exchanges the two arguments without changing any edge cost.
        return self.counts[k][2] * least + self.core(k, min(normalized, swapped))

    def core(self, k: int, values: tuple[int, ...]) -> int:
        """Apply equation (6), memoizing only within this finite calculation."""
        key = k, values
        if key in self._cache:
            return self._cache[key]
        if k == 1:
            return min(values)
        f = dict(zip(self.pairs[k], values))
        h = []
        for a, b in self.pairs[k - 1]:
            zero = f[a + 1, b]
            one = f[a, b + 1]
            g = tuple(
                f[a + c, b + d] + min(c + zero, d + one) for c, d in self.pairs[k - 1]
            )
            h.append(self.evaluate(k - 1, g))
        result = self.evaluate(k - 1, tuple(h))
        self._cache[key] = result
        return result


def check_probe_recurrence(checker: Checker, last: int) -> None:
    """Compare the recurrence with explicit small graphs and its finite table."""
    calculation = ProbeCuts(last)
    for k in range(1, 5):
        n, edges, probes = probe_graph(k)
        checker.check(
            f'probe k={k}: explicit construction counts',
            (n, len(edges), len(probes), sum(map(len, probes)))
            == calculation.counts[k],
        )
        augmented = edges + [
            (v, n + i) for i, probe in enumerate(probes) for v in probe
        ]
        checker.check(
            f'probe k={k}: augmented graph has separated order',
            separated_order(n + len(probes), augmented),
        )
        if k <= 3:
            potentials = (
                lambda a, b: min(a, b),
                lambda a, b: 2 * min(a, b),
                lambda a, b: a,
                lambda a, b: 3 * a - b,
            )
            for number, potential in enumerate(potentials, start=1):
                brute = min(
                    sum(colors[u] == colors[v] for u, v in edges)
                    + sum(
                        potential(
                            len(probe) - sum(colors[v] for v in probe),
                            sum(colors[v] for v in probe),
                        )
                        for probe in probes
                    )
                    for colors in product((0, 1), repeat=n)
                )
                computed = calculation.evaluate(
                    k, tuple(potential(a, b) for a, b in calculation.pairs[k])
                )
                checker.check(
                    f'probe k={k}, potential {number}: all colorings', brute == computed
                )
    expected = (
        (2, 0),
        (5, 1),
        (21, 7),
        (309, 163),
        (72501, 45763),
        (4523236149, 3378746051),
        (18936947705250519861, 15470367629841240771),
        (
            344803697388458091777620145336886172469,
            302196315691130900082126676245640090307,
        ),
    )
    for k in range(1, last + 1):
        n, _, p, _ = calculation.counts[k]
        cost = calculation.evaluate(
            k, tuple(min(a, b) for a, b in calculation.pairs[k])
        )
        checker.check(
            f'probe k={k}: exact augmented cut table', (n + p, cost) == expected[k - 1]
        )


def main() -> int:
    """Run the declared checks and return the shared harness exit status."""
    args = evidence_parser(__doc__ or 'Finite cut checks').parse_args()
    checker = Checker()
    for t in (2, 4, 16) if args.quick else (2, 4, 16, 64):
        check_parameter(checker, t)
    check_probe_recurrence(checker, 4 if args.quick else 8)
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
