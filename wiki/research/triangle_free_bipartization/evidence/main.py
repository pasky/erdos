"""Check exact profile-rule envelope values on band and control graphons.

For a graph H on n vertices, W_H is its equal-weight step graphon. A k-root
profile rule colours every point by its adjacencies to k i.i.d. roots.
Writing mono(R, c) for the monochromatic density of rule c at placement R:

- V_k = E_R min_c mono(R, c), averaged over all n^k placements;
- U_k = sum over labeled root types of P(type) min_c E[mono | type, c],
  the type-averaged envelope (Ferudun's U_7 at k = 7).

The owning page proves dmono <= V_k <= U_k. Clauses checked, in exact
integer and Fraction arithmetic unless stated:

1. C5, C7, the Petersen graph and the Clebsch graph are triangle-free with
   5, 7, 15 and 40 edges, and for every vertex v an explicit automorphism
   maps vertex 0 to v. Vertex-transitivity justifies summing over placements
   whose first root is vertex 0 and multiplying by n.
2. Every cut is scanned: the bipartization numbers are 1, 1, 3 and 8, and
   the Clebsch graph has exactly five optimal cuts, its coordinate cuts.
3. The edge-cut value p/2 - t(C4)/p equals (d(2K2) + d(P4))/(6p) on each
   graph, with values 2/25, 4/49, 1/10 and 27/256, from all n^4 ordered
   four-tuples.
4. Exhaustive per-placement minima give the stated V_k: Clebsch k <= 7
   (k <= 6 under --quick), Petersen k <= 4, C7 k <= 3, C5 k <= 4. Hence
   U_k >= V_k > 2/25 on Clebsch for k <= 5, on Petersen for k <= 3 and on
   C7 for k = 1, and every Clebsch placement with at most three roots
   leaves at least 12 edges uncut; from four roots on, the stated numbers
   of placements attain the optimum 8 and the others leave at least 11
   uncut. Scanning every rule of every four-root type gives
   U_4(Clebsch) = 24195/262144, and the type of two disjoint root edges is
   the only one with a rule of density 1/16 on all its placements.
5. Stored rules (assets/rules.json), one for every root type class, give
   exact upper bounds: U_k(Clebsch) < 2/25 for k = 6 and 7 (k = 6 under
   --quick), U_4(Petersen) < 2/25, U_2(C7) < 2/25, and U_k(C5) = 2/25 for
   k <= 4. A stored code must be the least code of its class over all root
   relabelings; its rule cost is summed over placements of exactly that
   labeled type and multiplied by the number of labeled versions, which
   preserves U_k, and the classes must account for all n^(k-1) placements.
6. C7, the Petersen graph and the Grotzsch graph have homomorphisms to the
   Clebsch graph (found and checked); the Chvatal graph and the Andrasfai
   graph on eleven vertices have none (exhaustive backtracking).
7. Higman-Sims (skipped under --quick). The Golay code, the Steiner system
   S(3,6,22) and the graph are built and checked (A^2 + 6A - 16I = 6J).
   Two stored automorphisms fixing vertex 0 generate a group of order
   887040 whose orbits are {0}, the neighbours and the non-neighbours; two
   more move 0 to a neighbour and to a non-neighbour, so the graph is
   vertex-transitive. Orbit representatives of seven-root placements with
   first root 0, weighted by orbit size, cover all 100^6 placements. The
   stored rules give U_7 <= 802719381387/9765625000000 exactly. The matching
   lower bound for equality is numerical, not exact: for each of the 107 types,
   scipy's HiGHS mixed-integer solver, run on the integer weights with zero
   relative gap, must report optimality at the stored cost. Then
   a numerical report U_7 > 2/25, and the mixture with the C5 blow-up at edge density
   1243/5000 carries slack (757/900)(U_7 - 2/25) > 1/600. For k <= 6 the
   values U_k and the least per-type value m_k are as stated and m_k > 2/25
   (exhaustive for types with at most 18 profiles, solver-certified
   otherwise), and the graph contains an induced five-cycle. Separately,
   exact integer-Gram branch bounds prove U_7 >= 81/1000 and m_k > 2/25
   for k <= 6. Those bounds alone prove the interior mixture at density
   1/4 forces seven-root envelope slack at least 1/1200. Each branch is
   pruned only by integer and rational arithmetic, regardless of the
   numerical factor proposal. Every
   placement of at most five roots leaves at least 406 of the 1100 edges
   uncut under every rule (exhaustive or solver-certified per placement).
   The cheapest stored rule has density 49/625 < 2/25 on its own type
   (exact), and no map of the seven roots into the five classes of a C5
   blow-up induces that type.
8. C13(1,5), the circulant on Z/13 with connection set {1, 5, 8, 12}, is
   triangle-free and 4-regular with 26 edges, and the rotations are
   automorphisms mapping vertex 0 to every vertex. Every cut is scanned: its
   bipartization number is 6, with exactly 26 optimal cuts having vertex 0 on
   side 0, so d_mono = 12/169 at p = 4/13. Exhaustive per-placement and
   per-type minima give V_k and the least per-type value m_k for k <= 4 as
   stated, with m_3 > 2/25 > m_4, and the stated numbers of placements with
   first root 0 attain an optimal cut. For the mixture of density vectors
   with weight lambda on C13(1,5) and 1 - lambda on the Clebsch graph, both
   of band density, the least unrooted four-root cut row at threshold 2/25
   is computed exactly over every labeled type and every rule: deterministic
   on all profile classes, or with a coin of any probability q in [0, 1] on
   the zero class. At lambda = 2/5, 1/2, 2157/5000 and 3/5 it equals the
   stated positive value, binds on the type of two disjoint root edges, and
   no interior coin is cheaper than the deterministic rules of its type; a
   control table on which the coin q = 1/4 is strictly cheaper checks that
   the coin search finds interior coins. One stored five-root rule on the
   labeled type P4 + K1 (root edges r0r1, r0r3, r1r2) has conditional
   density 140/1859 on C13(1,5) and 1/16 on the Clebsch graph, both below
   2/25, so its row is negative at every mixture of the two.
9. Abelian Cayley graphs. Every symmetric sum-free
   connection set S, with |S|/n in [1243/5000, 3197/10000], in every
   product of cyclic groups of order n <= 24 (these include every abelian
   group of each order) gives a triangle-free Cayley graph of band density.
   Every cut is scanned for n <= 16; above that a seeded local search
   proposes a cut whose uncut edges are recounted exactly. Every one of
   these graphs has a cut of monochromatic density at most 12/169, which
   C13(1,5) attains; the scan must contain the connection sets of C13(1,5)
   and of the Clebsch graph on (Z/2)^4.
10. Two-root switching trap. In the independently 7/8 edge-retained Clebsch
    blow-up with old colouring mask 831, all 32768 ordered-part-pair/switch
    cases up to complementation have positive expected gain on nontrivial
    switches, with minimum 49/65536 in the edges/N^2 convention. The
    three-root move (2,2,4), mask 424, has gain -931/524288. The template,
    vertex slacks, density, negative control, and the rational constants
    for the research page's finite concentration argument are checked.
    The three-root switch of mask 1090, on root type 12, weighted by
    squared common non-neighbour mass, has exact limiting density gain
    -164741871/2**47; it supplies an order-seven row excluding the trap.
    --switching-only runs exactly this clause; it takes about a second.
11. Hereditary comparison. All vertex subsets of C5, C7, Petersen and
    C13(1,5), with maximum cuts obtained exhaustively, satisfy the boundary
    identity and the comparison from the uniform source bound B=4/47.
    B=7/100 is rejected on C5. These are finite implementation controls;
    the general proof and imported source dependence are in the sketch.
    Fractional selections and recursive partial cuts are checked on C5/C7.
    Balanced mixtures of optimal cuts and independent-cut pattern counts
    check the finite formulas of the weighted-extremal route; a single
    cut and a repeated, dependent cut pair supply negative controls.
    --comparison-only runs exactly this clause.

Runtime: under a minute with --quick; the full run takes about five minutes,
most of it in the solver. Clauses 8 and 9 run in both modes and take
seconds.
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path

import networkx as nx
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from util.cayley import (
    abelian_groups,
    band_connection_sets,
    cayley_adjacency,
    proposed_cut,
    uncut_edges,
)
from util.envelopes import (
    aggregated_tables,
    all_cut_costs,
    clebsch,
    cycle,
    edges_of,
    even_subsets,
    exhaustive_minimum,
    four_vertex_densities,
    golay_octads,
    higman_sims,
    homomorphism,
    is_automorphism,
    is_triangle_free,
    labeled_versions,
    least_codes,
    per_placement_minimum,
    petersen,
    placement_blocks,
    profiles,
    rule_cost,
    type_codes,
)
from util.exactcut import certify_lower_bound, gram_bound
from util.groups import closure, orbit_representatives, weighted_placements
from util.hereditary import hereditary_clauses
from util.maxcut import solver_minimum_uncut
from util.mixtures import (
    circulant,
    coin_minimum,
    component_tables,
    conditional_minima,
    deterministic_minimum,
    mixture_minimum,
)
from util.switching_trap import switching_trap_clauses

from tools import Checker, evidence_parser

TARGET = Fraction(2, 25)
HS_U7_LOWER = Fraction(81, 1000)

# exact V_k from exhaustive per-placement minima
EXPECTED_V = {
    'C5': {1: Fraction(2, 25), 2: Fraction(2, 25), 3: Fraction(2, 25), 4: Fraction(2, 25)},
    'C7': {1: Fraction(6, 49), 2: Fraction(26, 343), 3: Fraction(18, 343)},
    'Petersen': {1: Fraction(3, 25), 2: Fraction(12, 125), 3: Fraction(51, 625),
                 4: Fraction(873, 12500)},
    'Clebsch': {
        1: Fraction(15, 128),
        2: Fraction(105, 1024),
        3: Fraction(195, 2048),
        4: Fraction(11955, 131072),
        5: Fraction(175785, 2097152),
        6: Fraction(2552025, 33554432),
        7: Fraction(37685265, 536870912),
    },
}

# placements with first root 0 whose best rule is an optimal Clebsch cut
CLEBSCH_OPTIMAL_PLACEMENTS = {4: 90, 5: 13500, 6: 489690, 7: 11540340}

# least conditional density of a stored seven-root Higman-Sims rule on its type
HS_CHEAPEST_TYPE = Fraction(49, 625)

# edge-cut values p/2 - t(C4)/p
EXPECTED_EDGE_CUT = {'C5': Fraction(2, 25), 'C7': Fraction(4, 49), 'Petersen': Fraction(1, 10),
                     'Clebsch': Fraction(27, 256)}

# exact U_4 on the Clebsch graphon, and the optimum density 1/16
CLEBSCH_U4 = Fraction(24195, 262144)
CLEBSCH_M4 = Fraction(1, 16)

# U_k and least per-type value m_k on the Higman-Sims graphon for k <= 6;
# exhaustive for types with at most 18 profiles, solver-certified otherwise
HS_TABLE = {
    1: (Fraction(77, 625), Fraction(77, 625)),
    2: (Fraction(5643, 62500), Fraction(107, 1250)),
    3: (Fraction(269071, 3125000), Fraction(107, 1250)),
    4: (Fraction(13393589, 156250000), Fraction(6377, 75625)),
    5: (Fraction(20753271, 244140625), Fraction(68257, 831875)),
    6: (Fraction(1634467681, 19531250000), Fraction(101, 1250)),
}

# least number of uncut Higman-Sims edges over placements with k roots and rules
HS_PLACEMENT_MINIMUM = {1: 616, 2: 428, 3: 428, 4: 416, 5: 406}

# exact U_7 of the stored Higman-Sims rules
HS_U7 = Fraction(802719381387, 9765625000000)

# C13(1,5): exact V_k and least per-type value m_k for k <= 4
C13_V = {1: Fraction(20, 169), 2: Fraction(212, 2197), 3: Fraction(2324, 28561),
         4: Fraction(27860, 371293)}
C13_M = {1: Fraction(20, 169), 2: Fraction(44, 507), 3: Fraction(68, 845), 4: Fraction(38, 507)}

# placements with first root 0 whose best rule is an optimal cut of C13(1,5)
C13_OPTIMAL_PLACEMENTS = {1: 0, 2: 4, 3: 108, 4: 1852}

# least unrooted four-root row of the mixture lambda C13(1,5) + (1 - lambda) Clebsch
MIXTURE_MINIMA = {
    Fraction(2, 5): Fraction(2537621, 116985856000),
    Fraction(1, 2): Fraction(27708913, 1216652902400),
    Fraction(2157, 5000): Fraction(3913894461, 116985856000000),
    Fraction(3, 5): Fraction(10931697, 1520816128000),
}

# a five-root rule on the labeled type P4 + K1 (code 21: root edges r0r1, r0r3,
# r1r2), as a mask of profile sides, and its exact conditional densities
FIVE_ROOT_CODE = 21
FIVE_ROOT_RULE = 0x5370006
FIVE_ROOT_DENSITY = {'C13(1,5)': Fraction(140, 1859), 'Clebsch': Fraction(1, 16)}

# band endpoints of the retained tail composition
BAND = (Fraction(1243, 5000), Fraction(3197, 10000))

# abelian Cayley graphs: largest order scanned, and largest order scanned exhaustively
CAYLEY_MAX_ORDER = 24
CAYLEY_EXHAUSTIVE_ORDER = 16

# exact U_k of the stored rules (upper bounds)
EXPECTED_RULE_U = {
    'C5': {1: Fraction(2, 25), 2: Fraction(2, 25), 3: Fraction(2, 25), 4: Fraction(2, 25)},
    'C7': {2: Fraction(26, 343)},
    'Petersen': {4: Fraction(909, 12500)},
    'Clebsch': {6: Fraction(2570745, 33554432), 7: Fraction(37855485, 536870912)},
}


def transitivity_maps(name: str, adjacency: np.ndarray) -> list[np.ndarray]:
    """Return explicit automorphisms g_v with g_v(0) = v for every vertex v."""
    n = len(adjacency)
    if name in ('C5', 'C7'):
        return [np.array([(x + v) % n for x in range(n)]) for v in range(n)]
    if name == 'Clebsch':
        subsets = even_subsets()
        index = {s: i for i, s in enumerate(subsets)}
        return [np.array([index[s ^ subsets[v]] for s in subsets]) for v in range(n)]
    # Petersen: vertex 0 is {0,1}; a permutation of [5] carrying {0,1} to the
    # pair of vertex v induces the map
    pairs = list(combinations(range(5), 2))
    index = {p: i for i, p in enumerate(pairs)}
    maps = []
    for v in range(n):
        for perm in permutations(range(5)):
            if tuple(sorted((perm[0], perm[1]))) == pairs[v]:
                maps.append(np.array([index[tuple(sorted((perm[a], perm[b])))]
                                      for a, b in pairs]))
                break
    return maps


def v_from_histogram(histogram: Counter[int], n: int, k: int) -> Fraction:
    """Return V_k from the histogram of per-placement minima over first-root-0 placements."""
    total = sum(cost * count for cost, count in histogram.items())
    return Fraction(2 * total, n ** (k - 1) * n * n)


def rule_upper_bound(adjacency: np.ndarray, k: int, rules: dict[str, str]) -> tuple[Fraction, bool]:
    """Return U_k of the stored rules and whether they cover every root type class once.

    Each stored code must be the least code of its class, so distinct stored
    codes lie in distinct classes. Coverage is exact when the stored classes
    account for every placement: the sum over stored codes of the number of
    labeled versions times the number of placements of that labeled type is
    n^(k-1).
    """
    n = len(adjacency)
    stored = sorted(int(c) for c in rules)
    stored_array = np.array(stored, dtype=np.int64)
    canonical = bool((least_codes(stored_array, k) == stored_array).all())
    versions = {c: labeled_versions(c, k) for c in stored}
    blocks = ((roots, np.ones(len(roots), dtype=np.int64)) for roots in placement_blocks(n, k))
    tables, totals = aggregated_tables(adjacency, blocks, set(stored))
    coverage = sum(versions[c] * totals[c] for c in stored) == n ** (k - 1)
    total = 0
    for code in stored:
        mask = int(rules[str(code)], 16)
        rule = {p: (mask >> p) & 1 for p in range(1 << k)}
        total += versions[code] * rule_cost(tables[code], rule)
    return Fraction(2 * total, n ** (k - 1) * n * n), canonical and coverage


def edge_cut_clauses(checker: Checker, name: str, adjacency: np.ndarray) -> None:
    """Check the edge-cut value and its induced four-vertex form exactly."""
    n = len(adjacency)
    p = Fraction(2 * len(edges_of(adjacency)), n * n)
    walks = int(np.trace(np.linalg.matrix_power(adjacency, 4)))
    c4 = Fraction(walks, n ** 4)
    value = p / 2 - c4 / p
    counts = four_vertex_densities(adjacency)
    density = {key: Fraction(v, n ** 4) for key, v in counts.items()}
    checker.check(f'{name}: four-vertex induced counts are complete and triangle-free',
                  sum(counts.values()) == n ** 4)
    checker.check(f'{name}: p^2 = (d(2K2) + d(P4) + 2 d(C4))/3 and t(C4) = d(C4)/3',
                  p * p == (density['2K2'] + density['P4'] + 2 * density['C4']) / 3
                  and c4 == density['C4'] / 3)
    checker.check(f'{name}: edge cut p/2 - t(C4)/p = (d(2K2) + d(P4))/(6p) = {EXPECTED_EDGE_CUT[name]}',
                  value == (density['2K2'] + density['P4']) / (6 * p) == EXPECTED_EDGE_CUT[name],
                  f'got {value}')


def exact_envelope(adjacency: np.ndarray, k: int) -> tuple[Fraction, dict[int, Fraction]]:
    """Return U_k and each class's least conditional value, by scanning every rule.

    Classes are keyed by their least labeled code.
    """
    n = len(adjacency)
    codes = set()
    for roots in placement_blocks(n, k):
        codes.update(np.unique(type_codes(adjacency, roots)).tolist())
    stored = sorted(set(least_codes(np.array(sorted(codes), dtype=np.int64), k).tolist()))
    blocks = ((roots, np.ones(len(roots), dtype=np.int64)) for roots in placement_blocks(n, k))
    tables, totals = aggregated_tables(adjacency, blocks, set(stored))
    versions = {c: labeled_versions(c, k) for c in stored}
    if sum(versions[c] * totals[c] for c in stored) != n ** (k - 1):
        raise RuntimeError('type classes do not cover every placement')
    minima = {c: exhaustive_minimum(tables[c]) for c in stored}
    total = sum(versions[c] * minima[c] for c in stored)
    conditional = {c: Fraction(2 * minima[c], totals[c] * n * n) for c in stored}
    return Fraction(2 * total, n ** (k - 1) * n * n), conditional


def homomorphism_clauses(checker: Checker) -> None:
    """Check which small graphs map homomorphically to the Clebsch graph."""
    target = clebsch()
    andrasfai = np.array([[int((u - v) % 11 in (1, 4, 7, 10)) for v in range(11)]
                          for u in range(11)], dtype=np.int64)
    graphs = {
        'C7': (cycle(7), 7, True),
        'Petersen': (petersen(), 15, True),
        'Grotzsch': (nx.to_numpy_array(nx.mycielski_graph(4), dtype=np.int64), 20, True),
        'Chvatal': (nx.to_numpy_array(nx.chvatal_graph(), dtype=np.int64), 24, False),
        'Andrasfai(4)': (andrasfai, 22, False),
    }
    for name, (adjacency, edge_count, expected) in graphs.items():
        checker.check(f'{name}: triangle-free with {edge_count} edges',
                      is_triangle_free(adjacency) and len(edges_of(adjacency)) == edge_count)
        image = homomorphism(adjacency, target)
        valid = image is not None and all(target[image[u], image[v]] for u, v in edges_of(adjacency))
        if expected:
            checker.check(f'{name}: a checked homomorphism to the Clebsch graph exists', valid)
        else:
            checker.check(f'{name}: exhaustive search finds no homomorphism to the Clebsch graph',
                          image is None)


def type_minima(adjacency: np.ndarray, roots: np.ndarray, weights: np.ndarray,
                k: int) -> tuple[Fraction, Fraction, bool, bool]:
    """Return numerical U_k, m_k, optimality reports, and an exact threshold check.

    A type's minimum is exhaustive when it has at most 18 profiles and
    solver-certified otherwise. ``roots`` and ``weights`` cover all n^(k-1)
    placements with first root 0.
    """
    n = len(adjacency)
    codes = np.unique(type_codes(adjacency, roots))
    stored = sorted(set(least_codes(codes, k).tolist()))
    step = 1 << 16
    blocks = ((roots[i:i + step], weights[i:i + step]) for i in range(0, len(roots), step))
    tables, totals = aggregated_tables(adjacency, blocks, set(stored))
    versions = {c: labeled_versions(c, k) for c in stored}
    certified = sum(versions[c] * totals[c] for c in stored) == n ** (k - 1)
    threshold_proved = certified
    total = 0
    least = None
    for code in stored:
        if len({x for pair in tables[code] for x in pair}) <= 18:
            value = exhaustive_minimum(tables[code])
            threshold_proved &= 2 * value > TARGET * totals[code] * n * n
        else:
            rule, optimal = solver_minimum_uncut(tables[code])
            certified &= optimal
            value = rule_cost(tables[code], rule)
            threshold = (totals[code] * n * n) // 25 + 1
            proved, _ = certify_lower_bound(tables[code], threshold)
            threshold_proved &= proved
        total += versions[code] * value
        conditional = Fraction(2 * value, totals[code] * n * n)
        least = conditional if least is None else min(least, conditional)
    return (Fraction(2 * total, n ** (k - 1) * n * n), least or Fraction(0),
            certified, threshold_proved)


def placement_minimum(adjacency: np.ndarray, roots: np.ndarray) -> tuple[int, bool]:
    """Return the least uncut-edge count over placements and rules, and whether it is certified.

    Each placement's minimum is exhaustive when it has at most 18 profile
    classes and solver-certified otherwise.
    """
    edges = edges_of(adjacency)
    prof = profiles(adjacency, roots)
    least = None
    certified = True
    for row in prof:
        low = np.minimum(row[edges[:, 0]], row[edges[:, 1]])
        high = np.maximum(row[edges[:, 0]], row[edges[:, 1]])
        table = Counter(zip(low.tolist(), high.tolist()))
        if len({x for pair in table for x in pair}) <= 18:
            value = exhaustive_minimum(table)
        else:
            rule, optimal = solver_minimum_uncut(table)
            certified &= optimal
            value = rule_cost(table, rule)
        least = value if least is None else min(least, value)
    return least if least is not None else 0, certified


def exact_cut_controls(checker: Checker) -> None:
    """Exercise the exact bounds against exhaustive cuts and false targets."""
    tables = [
        Counter({(0, 1): 1, (0, 2): 1, (1, 2): 1}),
        Counter({(0, 0): 7, (0, 1): 2, (1, 2): 3, (2, 3): 5,
                 (3, 4): 4, (0, 4): 6, (1, 4): 2}),
    ]
    for index, table in enumerate(tables):
        minimum = exhaustive_minimum(table)
        true_target, _ = certify_lower_bound(table, minimum)
        false_target, _ = certify_lower_bound(table, minimum + 1)
        checker.check(f'exact cut control {index}: exhaustive optimum certified and false bound rejected',
                      true_target and not false_target)
    signed = np.array([[0, 3, -5], [3, 0, 4], [-5, 4, 0]], dtype=np.int64)
    lower, _ = gram_bound(signed)
    exact = min(int(np.array(s) @ signed @ np.array(s)) for s in product((-1, 1), repeat=3))
    checker.check('integer Gram bound remains valid with signed linear fields', lower <= exact)


def exact_hs_lower(tables: dict[int, Counter], totals: Counter,
                   versions: dict[int, int], rules: dict[str, str]) -> tuple[Fraction, int]:
    """Certify a lower bound above 81/1000 without relying on MILP optimality.

    For each nonempty type, target its exhibited cost minus 1/1000 of the
    conditional density. For the empty type target 163/2000. Every target is
    proved by exhaustive branching with exact integer-Gram pruning bounds.
    """
    weighted_lower = 0
    visits = 0
    for code in sorted(tables):
        table = tables[code]
        mask = int(rules[str(code)], 16)
        cost = rule_cost(table, {p: (mask >> p) & 1 for p in range(128)})
        if code == 0:
            target = Fraction(163, 2000) * totals[code] * 10000 / 2
        else:
            target = Fraction(cost) - Fraction(totals[code] * 10000, 2000)
        proved, count = certify_lower_bound(table, target)
        if not proved:
            raise RuntimeError(f'type {code}: proposed lower bound has a counterexample')
        visits += count
        # Costs are integers, so rounding up a certified rational bound is safe.
        weighted_lower += versions[code] * -(-target.numerator // target.denominator)
    return Fraction(2 * weighted_lower, 100 ** 8), visits


def higman_sims_clauses(checker: Checker, rules: dict[str, str]) -> None:
    """Check the Higman-Sims construction and its seven-root envelope U_7."""
    octads, words = golay_octads()
    weights = words.sum(axis=1)
    checker.check('Golay code: 4096 distinct words, minimum weight 8, 759 octads',
                  len({w.tobytes() for w in words}) == 4096
                  and int(weights[weights > 0].min()) == 8 and len(octads) == 759)
    adjacency, hexads = higman_sims()
    hexad_sets = [set(h) for h in hexads]
    checker.check('77 hexads form S(3,6,22): every 3 points lie in exactly one',
                  len(hexads) == 77 and all(len(h) == 6 for h in hexad_sets)
                  and all(sum(set(t) <= h for h in hexad_sets) == 1
                          for t in combinations(range(22), 3)))
    n = 100
    square = adjacency @ adjacency
    ones = np.ones((n, n), dtype=np.int64)
    checker.check('HS: A^2 + 6A - 16I = 6J, so srg(100, 22, 0, 6), triangle-free',
                  bool((square + 6 * adjacency - 16 * np.eye(n, dtype=np.int64) == 6 * ones).all()
                       and (adjacency.sum(axis=1) == 22).all() and not adjacency.trace()
                       and (adjacency == adjacency.T).all()))
    data = json.loads((Path(__file__).parent / 'assets/higman_sims_automorphisms.json').read_text())
    generators = [np.array(g) for g in data['stabilizer_generators']]
    checker.check('HS: stored stabilizer generators are automorphisms fixing vertex 0',
                  all(is_automorphism(adjacency, g) and g[0] == 0 for g in generators))
    group = closure(generators)
    checker.check('HS: the generated stabilizer has order 887040', len(group) == 887040)
    orbits = orbit_representatives(group, np.arange(len(group)), n)
    neighbours = set(np.flatnonzero(adjacency[0]).tolist())
    orbit_sets = [set(np.unique(group[:, p]).tolist()) for p, _ in orbits]
    checker.check('HS: stabilizer orbits are {0}, the 22 neighbours and the 77 others',
                  sorted(map(len, orbit_sets)) == [1, 22, 77] and neighbours in orbit_sets)
    moves = data['moves_vertex_0_to']
    checker.check('HS: stored automorphisms move 0 to a neighbour and to a non-neighbour',
                  all(is_automorphism(adjacency, np.array(g)) and g[0] == int(v)
                      and int(v) != 0
                      for v, g in moves.items())
                  and {adjacency[0, int(v)] for v in moves} == {0, 1})
    cycle_found = False
    for b in np.flatnonzero(adjacency[0]).tolist():
        for c in np.flatnonzero(adjacency[b]).tolist():
            for d in np.flatnonzero(adjacency[c]).tolist():
                for e in np.flatnonzero(adjacency[d] & adjacency[0]).tolist():
                    five = [0, b, c, d, e]
                    cycle_found |= len(set(five)) == 5 and all(
                        adjacency[five[i], five[j]] == int((i - j) % 5 in (1, 4))
                        for i, j in combinations(range(5), 2))
    checker.check('HS: contains an induced five-cycle, so every C5 blow-up type has positive '
                  'probability in W_HS', cycle_found)
    for k, (expected_u, expected_m) in HS_TABLE.items():
        roots, leaf_weights = weighted_placements(group, 0, k, n)
        u_k, m_k, certified, threshold_proved = type_minima(adjacency, roots, leaf_weights, k)
        checker.check(f'HS: U_{k} = {expected_u} and m_{k} = {expected_m} (classes cover all '
                      'placements; large types solver-certified)',
                      certified and u_k == expected_u and m_k == expected_m,
                      f'got {u_k}, {m_k}, certified {certified}')
        checker.check(f'HS: every {k}-root type has every rule above 2/25 (exact branch bounds)',
                      threshold_proved)
        if k in HS_PLACEMENT_MINIMUM:
            least, certified = placement_minimum(adjacency, roots)
            checker.check(f'HS: every {k}-root placement leaves at least {HS_PLACEMENT_MINIMUM[k]} '
                          'edges uncut under every rule, more than 2/25 allows',
                          certified and least == HS_PLACEMENT_MINIMUM[k]
                          and 2 * least > TARGET * n * n, f'got {least}, certified {certified}')
    k = 7
    roots, leaf_weights = weighted_placements(group, 0, k, n)
    checker.check('HS: orbit-weighted placements cover all 100^6 with first root 0',
                  int(leaf_weights.sum()) == n ** (k - 1))
    stored = sorted(int(c) for c in rules)
    stored_array = np.array(stored, dtype=np.int64)
    versions = {c: labeled_versions(c, k) for c in stored}
    step = 1 << 16
    blocks = ((roots[i:i + step], leaf_weights[i:i + step]) for i in range(0, len(roots), step))
    tables, totals = aggregated_tables(adjacency, blocks, set(stored))
    checker.check('HS: every stored 7-root code is the least code of its class',
                  bool((least_codes(stored_array, k) == stored_array).all()))
    checker.check('HS: the stored classes cover every placement exactly',
                  sum(versions[c] * totals[c] for c in stored) == n ** (k - 1))
    exact_lower, branch_nodes = exact_hs_lower(tables, totals, versions, rules)
    checker.check('HS: exact integer-Gram branch bounds prove U_7 >= 81/1000 > 2/25',
                  exact_lower >= HS_U7_LOWER > TARGET,
                  f'lower bound {exact_lower}; {branch_nodes} branch nodes')
    mixture = Fraction(5, 6)
    checker.check('HS+C5: mixture density 1/4 lies inside the open band and forces slack >= 1/1200',
                  mixture * Fraction(11, 50) + (1 - mixture) * Fraction(2, 5) == Fraction(1, 4)
                  and Fraction(1243, 5000) < Fraction(1, 4) < Fraction(3197, 10000)
                  and mixture * (exact_lower - TARGET) >= Fraction(1, 1200))
    total = 0
    solver_total = 0
    certified = True
    cheapest = None
    for code in stored:
        mask = int(rules[str(code)], 16)
        cost = rule_cost(tables[code], {p: (mask >> p) & 1 for p in range(1 << k)})
        total += versions[code] * cost
        conditional = Fraction(2 * cost, totals[code] * n * n)
        if cheapest is None or conditional < cheapest[0]:
            cheapest = (conditional, code)
        rule, optimal = solver_minimum_uncut(tables[code])
        certified &= optimal
        solver_total += versions[code] * rule_cost(tables[code], rule)
    value = Fraction(2 * total, n ** (k - 1) * n * n)
    checker.check(f'HS: stored rules give U_7 <= {HS_U7}', value == HS_U7, f'got {value}')
    checker.check('HS: HiGHS reports every type optimal at the stored cost (numerical)',
                  certified and solver_total == total,
                  f'solver total {solver_total}, stored total {total}')
    checker.check('HS: numerical optimality reports agree with the exhibited U_7 value',
                  certified and solver_total == total
                  and value > TARGET)
    checker.check(f'HS: the cheapest stored rule has density {HS_CHEAPEST_TYPE} < 2/25 on its type',
                  cheapest is not None and cheapest[0] == HS_CHEAPEST_TYPE < TARGET, f'got {cheapest}')
    pairs = list(combinations(range(k), 2))
    code = cheapest[1] if cheapest is not None else 0
    realizable = any(
        all(((code >> b) & 1) == int((f[i] - f[j]) % 5 in (1, 4)) for b, (i, j) in enumerate(pairs))
        for f in product(range(5), repeat=k)
    )
    checker.check('HS: that type occurs in no blow-up of C5, so a C5 component cannot offset it',
                  not realizable)
    slack = Fraction(757, 900) * (value - TARGET)
    checker.check('HS: numerical U_7 report would give endpoint-mixture slack above 1/600',
                  slack > Fraction(1, 600), f'slack {slack}')


def inband_mixture_clauses(checker: Checker) -> None:
    """Check C13(1,5) and its in-band density-vector mixture with the Clebsch graph."""
    # control: two zero-class edges and two edges to one nonzero class; every
    # deterministic rule leaves cost 2, the coin q = 1/4 costs 7/4
    control = {(0, 0): 2, (0, 1): 2}
    checker.check('coin control: an interior zero-class coin is found strictly cheaper (7/4 < 2)',
                  deterministic_minimum(control) == 2
                  and coin_minimum(control, 0) == Fraction(7, 4))
    c13 = circulant(13, {1, 5, 8, 12})
    n = len(c13)
    checker.check('C13(1,5): symmetric, loopless, 4-regular with 26 edges',
                  bool((c13 == c13.T).all() and not c13.trace() and (c13.sum(axis=1) == 4).all()
                       and len(edges_of(c13)) == 26))
    checker.check('C13(1,5): triangle-free', is_triangle_free(c13))
    rotations = [np.array([(x + v) % n for x in range(n)]) for v in range(n)]
    checker.check('C13(1,5): the rotations are automorphisms mapping vertex 0 to every vertex',
                  all(is_automorphism(c13, g) and g[0] == v for v, g in enumerate(rotations)))
    _masks, cost = all_cut_costs(c13)
    checker.check('C13(1,5): bipartization number 6, with exactly 26 optimal cuts having vertex 0 '
                  'on side 0, so d_mono = 12/169',
                  int(cost.min()) == 6 and int((cost == 6).sum()) == 26
                  and Fraction(2 * int(cost.min()), n * n) == Fraction(12, 169))
    for k in range(1, 5):
        histogram = per_placement_minimum(c13, placement_blocks(n, k))
        value = v_from_histogram(histogram, n, k)
        checker.check(f'C13(1,5): V_{k} = {C13_V[k]}', value == C13_V[k], f'got {value}')
        checker.check(f'C13(1,5): {C13_OPTIMAL_PLACEMENTS[k]} of the {n ** (k - 1)} {k}-root '
                      'placements with first root 0 attain an optimal cut',
                      histogram[6] == C13_OPTIMAL_PLACEMENTS[k], f'got {histogram[6]}')
        tables, totals = component_tables(c13, k)
        least = min(conditional_minima(n, tables, totals).values())
        checker.check(f'C13(1,5): m_{k} = {C13_M[k]}', least == C13_M[k], f'got {least}')
    checker.check('C13(1,5): m_3 > 2/25 > m_4', C13_M[3] > TARGET > C13_M[4])
    densities = (Fraction(2 * 26, n * n), Fraction(2 * 40, 16 * 16))
    checker.check('C13(1,5) and Clebsch: densities 4/13 and 5/16 lie in the band',
                  densities == (Fraction(4, 13), Fraction(5, 16))
                  and all(BAND[0] <= d <= BAND[1] for d in densities))
    components = [(n, *component_tables(c13, 4)), (16, *component_tables(clebsch(), 4))]
    root_pairs = list(combinations(range(4), 2))
    all_types = set()
    for code in range(1 << len(root_pairs)):
        edges = {pair for bit, pair in enumerate(root_pairs) if (code >> bit) & 1}
        if not any({(i, j), (i, k), (j, k)} <= edges
                   for i, j, k in combinations(range(4), 3)):
            all_types.add(code)
    supported = set().union(*(set(totals) for _, _, totals in components))
    checker.check('mixture components support all 41 labeled triangle-free four-root types',
                  len(all_types) == 41 and supported == all_types)
    for weight, expected in MIXTURE_MINIMA.items():
        value, code, coin_better = mixture_minimum(components, [weight, 1 - weight], 4, TARGET)
        checker.check(f'mixture {weight} C13(1,5) + {1 - weight} Clebsch: every four-root row, '
                      f'deterministic or with a zero-class coin, is at least {expected} > 0 '
                      'at threshold 2/25',
                      value == expected and value > 0, f'got {value}')
        # code 12 is the least labeled code of two disjoint root edges, r0r3 and r1r2
        checker.check(f'mixture {weight}: the least row is on the type of two disjoint root edges, '
                      'and no interior zero-class coin beats the deterministic rules',
                      code == 12 and not coin_better, f'got code {code}, coin {coin_better}')
    rule = {q: (FIVE_ROOT_RULE >> q) & 1 for q in range(32)}
    for name, adjacency in (('C13(1,5)', c13), ('Clebsch', clebsch())):
        size = len(adjacency)
        tables, totals = component_tables(adjacency, 5)
        density = Fraction(2 * rule_cost(tables[FIVE_ROOT_CODE], rule),
                           totals[FIVE_ROOT_CODE] * size * size)
        checker.check(f'{name}: the stored five-root rule on type P4 + K1 has conditional density '
                      f'{FIVE_ROOT_DENSITY[name]} < 2/25',
                      density == FIVE_ROOT_DENSITY[name] and density < TARGET
                      and totals[FIVE_ROOT_CODE] > 0, f'got {density}')


def cayley_clauses(checker: Checker) -> None:
    """Check that no band-density triangle-free abelian Cayley graph of order at most 24 beats 12/169."""
    rng = np.random.default_rng(5)
    count = 0
    triangle_free = True
    largest = Fraction(0)
    # controls: C13(1,5) on Z/13 and the Clebsch graph on (Z/2)^4, whose
    # connection set is the four unit vectors and their sum
    controls = {((13,), (1, 5, 8, 12)), ((2, 2, 2, 2), (1, 2, 4, 8, 15))}
    found = set()
    for n in range(1, CAYLEY_MAX_ORDER + 1):
        for factors in abelian_groups(n):
            for _, connection in band_connection_sets(factors, BAND[0], BAND[1]):
                found |= {(factors, connection)} & controls
                adjacency = cayley_adjacency(factors, connection)
                triangle_free &= is_triangle_free(adjacency)
                if n <= CAYLEY_EXHAUSTIVE_ORDER:
                    uncut = int(all_cut_costs(adjacency)[1].min())
                else:
                    uncut = uncut_edges(adjacency, proposed_cut(adjacency, rng))
                largest = max(largest, Fraction(2 * uncut, n * n))
                count += 1
    checker.check(f'abelian Cayley graphs: all {count} symmetric sum-free connection sets of band '
                  f'density on groups of order at most {CAYLEY_MAX_ORDER} give triangle-free graphs, '
                  'and the scan contains C13(1,5) and the Clebsch graph',
                  triangle_free and count == 5199 and found == controls,
                  f'expected 5199 connection sets, got {count}')
    checker.check('abelian Cayley graphs: each has a cut of monochromatic density at most 12/169 '
                  f'(all cuts scanned up to order {CAYLEY_EXHAUSTIVE_ORDER}, exhibited cuts above), '
                  'and 12/169 is attained', largest == Fraction(12, 169), f'got {largest}')


def main() -> int:
    """Run every clause and return the exit status."""
    parser = evidence_parser(__doc__ or '')
    selected = parser.add_mutually_exclusive_group()
    selected.add_argument('--switching-only', action='store_true',
                          help='run only the exact retained-edge switching-trap clause')
    selected.add_argument('--comparison-only', action='store_true',
                          help='run only the exact hereditary-comparison controls')
    args = parser.parse_args()
    checker = Checker()
    if args.comparison_only:
        hereditary_clauses(checker)
        return checker.finish()
    switching_trap_clauses(checker)
    if args.switching_only:
        return checker.finish()
    hereditary_clauses(checker)
    exact_cut_controls(checker)
    rules = json.loads((Path(__file__).parent / 'assets/rules.json').read_text())
    graphs = {'C5': cycle(5), 'C7': cycle(7), 'Petersen': petersen(), 'Clebsch': clebsch()}
    edge_counts = {'C5': 5, 'C7': 7, 'Petersen': 15, 'Clebsch': 40}
    d2 = {'C5': 1, 'C7': 1, 'Petersen': 3, 'Clebsch': 8}
    v_range = {'C5': range(1, 5), 'C7': range(1, 4), 'Petersen': range(1, 5),
               'Clebsch': range(1, 7 if args.quick else 8)}
    for name, adjacency in graphs.items():
        n = len(adjacency)
        checker.check(f'{name}: symmetric, loopless, {edge_counts[name]} edges',
                      bool((adjacency == adjacency.T).all() and not adjacency.trace()
                           and len(edges_of(adjacency)) == edge_counts[name]))
        checker.check(f'{name}: triangle-free', is_triangle_free(adjacency))
        maps = transitivity_maps(name, adjacency)
        checker.check(f'{name}: an automorphism maps vertex 0 to every vertex',
                      len(maps) == n and all(is_automorphism(adjacency, g) and g[0] == v
                                             for v, g in enumerate(maps)))
        masks, cost = all_cut_costs(adjacency)
        checker.check(f'{name}: bipartization number {d2[name]}', int(cost.min()) == d2[name])
        edge_cut_clauses(checker, name, adjacency)
        if name == 'Clebsch':
            optimal = masks[cost == 8]
            subsets = even_subsets()
            coordinate = set()
            for j in range(5):
                side = sum(1 << i for i, s in enumerate(subsets) if (s >> j) & 1)
                coordinate.add(side if not side & 1 else ((1 << n) - 1) ^ side)
            checker.check('Clebsch: the optimal cuts are exactly the five coordinate cuts',
                          set(optimal.tolist()) == coordinate)
        for k in v_range[name]:
            histogram = per_placement_minimum(adjacency, placement_blocks(n, k))
            value = v_from_histogram(histogram, n, k)
            expected = EXPECTED_V[name].get(k)
            label = f'{name}: V_{k} = {value}'
            if expected is not None:
                checker.check(label + ' as stated', value == expected, f'got {value}')
            if name == 'Clebsch' and k <= 5:
                checker.check(f'Clebsch: V_{k} > 2/25, so U_{k} > 2/25', value > TARGET)
            if name == 'Clebsch' and k <= 3:
                checker.check(f'Clebsch: every {k}-root placement leaves at least 12 edges uncut',
                              min(histogram) >= 12)
            if name == 'Clebsch' and k >= 4:
                checker.check(f'Clebsch: {CLEBSCH_OPTIMAL_PLACEMENTS[k]} of the {n ** (k - 1)} '
                              f'{k}-root placements with first root 0 attain the optimum 8; '
                              'the others leave at least 11 edges uncut',
                              histogram[8] == CLEBSCH_OPTIMAL_PLACEMENTS[k]
                              and min(c for c in histogram if c != 8) >= 11,
                              f'got {sorted(histogram.items())}')
            if name == 'Petersen' and k <= 3:
                checker.check(f'Petersen: V_{k} > 2/25, so U_{k} > 2/25', value > TARGET, f'got {value}')
            if name == 'C7' and k == 1:
                checker.check('C7: V_1 > 2/25, so U_1 > 2/25', value > TARGET)
            if name == 'C5':
                checker.check(f'C5: V_{k} = 2/25', value == TARGET)
        if name == 'Clebsch':
            u4, conditional = exact_envelope(adjacency, 4)
            checker.check(f'Clebsch: U_4 = {CLEBSCH_U4} exactly (every rule scanned)', u4 == CLEBSCH_U4,
                          f'got {u4}')
            # code 12 is the least labeled code of two disjoint root edges, r0r3 and r1r2
            best = sorted(c for c, value in conditional.items() if value == CLEBSCH_M4)
            checker.check('Clebsch: exactly the 4-root type 2K2 has a rule of density 1/16 on all '
                          'its placements', best == [12], f'got {best}')
        for k, expected in EXPECTED_RULE_U[name].items():
            if args.quick and name == 'Clebsch' and k == 7:
                continue
            value, complete = rule_upper_bound(adjacency, k, rules[name][str(k)])
            checker.check(f'{name}: stored rules cover every canonical {k}-root type once', complete)
            checker.check(f'{name}: stored {k}-root rules give U <= {expected}', value == expected,
                          f'got {value}')
            if name == 'C5':
                checker.check(f'C5: U_{k} = 2/25', value == TARGET)
            else:
                checker.check(f'{name}: U_{k} < 2/25', value < TARGET)
    homomorphism_clauses(checker)
    inband_mixture_clauses(checker)
    cayley_clauses(checker)
    if not args.quick:
        higman_sims_clauses(checker, rules['HigmanSims']['7'])
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
