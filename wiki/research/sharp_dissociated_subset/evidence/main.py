"""Check the exact finite facts recorded in the pivot-certificate note.

Nine groups of checks, all in exact integer arithmetic:

1. For k = 1, ..., 5 the odd progression O_k = {1, 3, ..., 2^(k+1) - 1}
   has largest dissociated subset size 2, 3, 5, 6, 7.  Each retained
   witness is checked to lie in O_k and to have pairwise distinct subset
   sums; maximality is checked by an exhaustive depth-first enumeration of
   all dissociated subsets (dissociation is hereditary, so every
   dissociated set is reached through its increasing prefixes).
2. The set {1, 3, 5, 7, 13} has dissociation number 4, while the largest
   certificate of the graded pivot lemma (one pivot, companions at pairwise
   distinct 2-adic levels, the graded budget hypothesis) has two
   companions; the dependent set {13; 7, 1, 5} meets the lemma's strict
   inequality with equality.
3. The set {3, 14, 17, 24, 41, 43, 58, 107, 289} has dissociation number
   7, while the largest graded-pivot certificate again has two companions;
   the lattice form with modulus 107 certifies the five-element subset
   {3, 14, 24, 107, 289}, whose hypotheses and dissociation are checked.
4. A set of 32 positive integers with largest element below twice the
   smallest has no dominant-pivot certificate with 5 = floor(log_2 32)
   companions (the largest has 4), while a retained graded certificate
   has 8 companions and a retained 6-element subset is dissociated.
5. A set of 9 odd positive integers with largest element below twice the
   smallest has dissociation number 8, while the largest graded-pivot
   certificate has 3 companions, one short of what the stronger odd bound
   |O| <= 2^(d(O)-1) would need from a certificate.
6. A set of 8 integers in which every pivot with at least three levels
   pays more than the diameter for its three cheapest levels.
7. Three explicit certificates using freely chosen archimedean centers:
   six elements of the bounded set, five of the bounded odd set, and four
   of the diameter example. Their level conditions, strict budgets and
   actual subset-sum distinctness are checked. The original graded
   predicate rejects these same pivot/companion choices. A known dependent
   four-set is rejected by the recentered predicate too.
8. A set of 32 positive integers whose five-level stars all have total
   distance from any freely chosen center greater than the diameter.
   Every pivot and every center among the ambient elements is checked,
   choosing the five cheapest levels relative to the center. A median
   of any selected star is one of its elements, so these centers suffice.
   A retained minimizing star is nevertheless dissociated: this is an
   obstruction to the diameter estimate, not to the requested bound.
9. An explicit 65-element odd set of ratio below two has only two pivots
   with seven difference levels. Every seven-level star fails the
   recentered budget with multiplier two: the minimum defect is 892.
   An eight-element dissociated subset and a seven-element graded
   certificate are checked. A translated odd progression is a passing
   control for the centered budget. This is one constructive obstruction,
   not a search over sets or a computation of its dissociation number.

The graded certificate search of groups 2, 3 and 5 enumerates every
pivot, every set of levels and every choice of one companion per level,
so it does not rely on the cheapest-companion reduction.  Groups 4 and 6
use that reduction, which is exact for the dominant-pivot hypothesis and
for a total-cost bound: replacing a companion by a nearer element of the
same level keeps the levels distinct and lowers the total.  Dissociation
of a set of small integers is tested by building its subset sums as an
integer bit mask, and of a set of large integers by collecting its
subset sums.

Run from the repository root:
    uv run --no-sync python wiki/research/sharp_dissociated_subset/evidence/main.py

Dependencies are the standard library and the installed root ``tools``
package.  There are no inputs, outputs, random choices or reduced modes.
Expected runtime is under ten seconds.  The checks concern these specific
finite sets only and prove nothing about Problem 963 in general.
"""

from __future__ import annotations

import itertools
import sys

import tools

__all__ = [
    'cheapest_level_costs',
    'dissociated',
    'dissociation_number',
    'distinct_subset_sums',
    'graded_hypothesis',
    'largest_certificate',
    'largest_dominant_certificate',
    'lattice_hypothesis',
    'main',
    'minimum_centered_cost',
    'recentered_hypothesis',
]

# retained witnesses for the odd progressions, keyed by k
_ODD_WITNESSES = {
    1: (1, 3),
    2: (1, 3, 5),
    3: (1, 7, 11, 13, 15),
    4: (1, 7, 13, 25, 27, 29),
    5: (1, 7, 13, 27, 51, 53, 55),
}

# the two certificate examples with their dissociation witnesses
_SMALL = (1, 3, 5, 7, 13)
_SMALL_WITNESS = (1, 3, 5, 13)
_SPREAD = (3, 14, 17, 24, 41, 43, 58, 107, 289)
_SPREAD_WITNESS = (3, 14, 24, 43, 58, 107, 289)

# the lattice certificate in the spread set: modulus and (element, multiple)
_LATTICE_MODULUS = 107
_LATTICE_REPS = ((3, 0), (14, 0), (24, 0), (107, 1), (289, 3))

# A perfect six-level tree with one split leaf. Three sibling subtrees
# along the resulting seven-level path are high; the others are low.
_SPLIT_ODD = tuple(2049 + 2 * c + 1792 * (c % 8 != 0) for c in range(65))
_SPLIT_ODD_WITNESS = (2049, 3843, 3845, 3847, 3851, 3859, 3875, 3907)

# a bounded-ratio set defeating dominant-pivot certificates, a graded
# certificate in it and a dissociated subset of size floor(log_2 32) + 1
_BOUNDED = (
    1000025929,
    1000027225,
    1000028985,
    1000030089,
    1000031897,
    1000032937,
    1000035001,
    1000037225,
    1059324281,
    1059325161,
    1089023257,
    1118931145,
    1163421945,
    1222028073,
    1284134153,
    1464121049,
    1596136281,
    2000038026,
    2000039058,
    2000040078,
    2000041110,
    2000042124,
    2000042644,
    2000043664,
    2000044696,
    2000045707,
    2000046739,
    2000047759,
    2000048791,
    2000049805,
    2000050837,
    2000051857,
)
_BOUNDED_GRADED = (
    1596136281,
    (
        2000045707,
        2000049805,
        2000051857,
        1284134153,
        1163421945,
        1089023257,
        1464121049,
        1000027225,
    ),
)
_BOUNDED_WITNESS = (
    1000028985,
    1059324281,
    2000039058,
    2000044696,
    2000045707,
    2000047759,
)

# a bounded-ratio odd set whose certificates miss the stronger odd bound
_ODD_BOUNDED = (
    1000471,
    1001479,
    1989889,
    1990153,
    1990157,
    1990667,
    1990915,
    1990927,
    1991173,
)
_ODD_BOUNDED_WITNESS = _ODD_BOUNDED[:8]

# a set whose pivots all pay more than the diameter for three levels
_DIAMETER = (272141, 350179, 395247, 536073, 700101, 1000000, 1000034, 1000215)

# (name, ambient set, pivot, companions, center, exact total center cost)
_CENTERED = (
    (
        'bounded set',
        _BOUNDED,
        1464121049,
        (2000045707, 2000044696, 2000049805, 2000051857, 1596136281),
        2000045707,
        939845343,
    ),
    (
        'bounded odd set',
        _ODD_BOUNDED,
        1000471,
        (1001479, 1990915, 1990927, 1991173),
        1990915,
        1980150,
    ),
    (
        'diameter set',
        _DIAMETER,
        536073,
        (1000000, 1000215, 700101),
        1000000,
        764041,
    ),
)

# A binary-tree configuration found by a bounded exploratory search, rounded
# and realized by integer binary codes. Only this exact witness is evidence.
_RECENTERED_DIAMETER = (
    1024000003,
    1024000014,
    1024000015,
    1024000023,
    1024000059,
    1024520720,
    1027426821,
    1028447757,
    1050496524,
    1064518148,
    1110536214,
    1120143366,
    1142529560,
    1217676297,
    1247841793,
    1265661969,
    1272945198,
    1277249049,
    1335652462,
    1403094024,
    1442390048,
    1455246888,
    1476227072,
    1533241371,
    1534553611,
    1535015426,
    1535925269,
    1536000007,
    1536000010,
    1536000030,
    1536000041,
    1536000055,
)
_RECENTERED_DIAMETER_WITNESS = (
    1024000059,
    1024000023,
    1024000014,
    1024000003,
    1027426821,
    1533241371,
)


def _v2(z: int) -> int:
    """Return the exponent of 2 in a nonzero integer."""
    z = abs(z)
    return (z & -z).bit_length() - 1


def dissociated(xs: tuple[int, ...]) -> bool:
    """Return whether distinct subsets of positive integers have distinct sums."""
    # build the subset-sum mask and reject any collision
    mask = 1
    for x in xs:
        if x <= 0 or mask & (mask << x):
            return False
        mask |= mask << x
    return True


def distinct_subset_sums(xs: tuple[int, ...]) -> bool:
    """Return whether distinct subsets have distinct sums, for large integers."""
    # collect every subset sum and compare with the number of subsets
    sums = {0}
    for x in xs:
        sums |= {t + x for t in sums}
    return len(sums) == 2 ** len(xs)


def dissociation_number(xs: tuple[int, ...]) -> int:
    """Return the largest size of a dissociated subset, by exhaustive search."""
    items = sorted(xs)
    best = 0

    def extend(start: int, mask: int, size: int) -> None:
        nonlocal best
        best = max(best, size)
        # a branch that cannot exceed the current best is skipped
        if size + len(items) - start <= best:
            return
        for i in range(start, len(items)):
            x = items[i]
            if not mask & (mask << x):
                extend(i + 1, mask | (mask << x), size + 1)

    extend(0, 1, 0)
    return best


def graded_hypothesis(a: int, companions: tuple[int, ...]) -> bool:
    """Return whether pivot and companions satisfy the graded pivot lemma."""
    # companions must have pairwise distinct levels
    levels = [_v2(b - a) for b in companions]
    if len(set(levels)) != len(levels):
        return False
    u = _v2(a)
    bound = len(companions) + 1
    costs = dict(zip(levels, (abs(b - a) for b in companions), strict=True))
    # check every level of the window against the graded budget
    for j in levels:
        if j >= u and 2 ** (j - u) <= bound:
            total = sum(c for i, c in costs.items() if i >= j)
            if total >= 2 ** (j - u) * abs(a):
                return False
    return True


def lattice_hypothesis(g: int, reps: tuple[tuple[int, int], ...]) -> bool:
    """Return whether elements z = q*g + rho satisfy the lattice lemma."""
    residues = [z - q * g for z, q in reps]
    nonzero = [r for r in residues if r != 0]
    levels = [_v2(r) for r in nonzero]
    return (
        len(set(levels)) == len(levels)
        and len(residues) - len(nonzero) <= 1
        and sum(abs(r) for r in residues) < g
    )


def recentered_hypothesis(a: int, companions: tuple[int, ...]) -> bool:
    """Check every required suffix budget, trying all of its possible centers."""
    values = (a, *companions)
    if min(values) <= 0 or len(set(values)) != len(values):
        return False
    levels = [_v2(b - a) for b in companions]
    if len(set(levels)) != len(levels):
        return False
    u = _v2(a)
    for j in levels:
        if j < u or 2 ** (j - u) > len(values):
            continue
        suffix = (a, *(b for b, i in zip(companions, levels, strict=True) if i >= j))
        q = 2 ** (j - u)
        if not any(sum(abs(x - c) for x in suffix) < q * c for c in suffix):
            return False
    return True


def largest_certificate(xs: tuple[int, ...]) -> int:
    """Return the most companions any graded-pivot certificate in xs has."""
    best = 0
    for a in xs:
        # group the other elements by their level relative to the pivot
        by_level: dict[int, list[int]] = {}
        for x in xs:
            if x != a:
                by_level.setdefault(_v2(x - a), []).append(x)
        levels = sorted(by_level)
        # try every level set and every choice of companions
        for r in range(1, len(levels) + 1):
            for chosen in itertools.combinations(levels, r):
                pools = [by_level[j] for j in chosen]
                if any(
                    graded_hypothesis(a, comps) for comps in itertools.product(*pools)
                ):
                    best = max(best, r)
                    break
    return best


def cheapest_level_costs(a: int, xs: tuple[int, ...]) -> dict[int, int]:
    """Return, for each level v_2(x - a), the least distance |x - a|."""
    costs: dict[int, int] = {}
    for x in xs:
        if x != a:
            j = _v2(x - a)
            costs[j] = min(costs.get(j, abs(x - a)), abs(x - a))
    return costs


def minimum_centered_cost(
    xs: tuple[int, ...], companions: int, *, budget_multiple: int = 0
) -> int | None:
    """Minimize over all pivots, level choices, representatives and centers.

    Return sum(abs(x-center)) - budget_multiple * center. Here the budget
    is nonnegative and strictly below companions+1. A minimizing center
    for a fixed selected set may be chosen among its elements, by the
    piecewise-linear slopes (a median when the budget is zero). For a
    fixed pivot and center, each level is independent, so take its nearest
    representative and the cheapest requested levels.
    """
    best = None
    for a in xs:
        pools: dict[int, list[int]] = {}
        for b in xs:
            if b != a:
                pools.setdefault(_v2(b - a), []).append(b)
        if len(pools) < companions:
            continue
        for center in xs:
            costs = sorted(
                min(abs(b - center) for b in pool) for pool in pools.values()
            )
            total = abs(a - center) + sum(costs[:companions]) - budget_multiple * center
            if best is None or total < best:
                best = total
    return best


def largest_dominant_certificate(xs: tuple[int, ...]) -> int:
    """Return the most companions of distinct levels with total cost below the pivot."""
    best = 0
    for a in xs:
        # the m cheapest levels give the least total for m companions
        total = 0
        count = 0
        for c in sorted(cheapest_level_costs(a, xs).values()):
            if total + c >= a:
                break
            total += c
            count += 1
        best = max(best, count)
    return best


def main() -> int:
    """Run every check and return the exit code."""
    parser = tools.evidence_parser(
        'Check the finite facts of the pivot-certificate note (Problem 963).',
        quick=False,
    )
    parser.parse_args()
    checker = tools.Checker()

    # odd progressions: witnesses and exhaustive maxima
    expected = {1: 2, 2: 3, 3: 5, 4: 6, 5: 7}
    for k, value in expected.items():
        odd = tuple(range(1, 2 ** (k + 1), 2))
        witness = _ODD_WITNESSES[k]
        checker.check(
            f'O_{k}: witness of size {value} lies in O_{k} and is dissociated',
            len(witness) == value and set(witness) <= set(odd) and dissociated(witness),
        )
        found = dissociation_number(odd)
        checker.check(
            f'O_{k}: dissociation number is {value}', found == value, str(found)
        )

    # the small example: dimension four, certificate two, tight equality
    checker.check(
        '{1,3,5,7,13}: witness {1,3,5,13} is dissociated',
        dissociated(_SMALL_WITNESS),
    )
    checker.check(
        '{1,3,5,7,13}: dissociation number is 4',
        dissociation_number(_SMALL) == 4,
    )
    checker.check(
        '{1,3,5,7,13}: largest graded-pivot certificate has 2 companions',
        largest_certificate(_SMALL) == 2,
    )
    checker.check(
        '{13; 7, 1, 5}: dependent, and the graded budget fails with equality',
        not dissociated((1, 5, 7, 13))
        and 6 + 12 + 8 == 2 * 13
        and not graded_hypothesis(13, (7, 1, 5)),
    )

    # the spread example: dimension seven, certificate two
    checker.check(
        'spread set: witness of size 7 is dissociated',
        len(_SPREAD_WITNESS) == 7
        and set(_SPREAD_WITNESS) <= set(_SPREAD)
        and dissociated(_SPREAD_WITNESS),
    )
    checker.check(
        'spread set: dissociation number is 7',
        dissociation_number(_SPREAD) == 7,
    )
    checker.check(
        'spread set: largest graded-pivot certificate has 2 companions',
        largest_certificate(_SPREAD) == 2,
    )
    lattice_set = tuple(z for z, _ in _LATTICE_REPS)
    checker.check(
        'spread set: lattice certificate modulo 107 has five elements of the set',
        set(lattice_set) <= set(_SPREAD)
        and len(lattice_set) == 5
        and lattice_hypothesis(_LATTICE_MODULUS, _LATTICE_REPS),
    )
    checker.check(
        'spread set: the lattice-certified five-set is dissociated',
        dissociated(lattice_set),
    )

    # the bounded-ratio set: dominant pivots reach 4 companions, not 5
    checker.check(
        'bounded set: 32 distinct positive integers with max <= 2 min',
        len(set(_BOUNDED)) == 32
        and min(_BOUNDED) > 0
        and max(_BOUNDED) <= 2 * min(_BOUNDED),
    )
    found = largest_dominant_certificate(_BOUNDED)
    checker.check(
        'bounded set: largest dominant-pivot certificate has 4 companions',
        found == 4,
        str(found),
    )
    pivot, companions = _BOUNDED_GRADED
    checker.check(
        'bounded set: retained graded certificate has 8 companions',
        {pivot, *companions} <= set(_BOUNDED)
        and len(set(companions)) == 8
        and graded_hypothesis(pivot, companions)
        and distinct_subset_sums((pivot, *companions)),
    )
    checker.check(
        'bounded set: retained 6-element subset is dissociated',
        len(set(_BOUNDED_WITNESS)) == 6
        and set(_BOUNDED_WITNESS) <= set(_BOUNDED)
        and distinct_subset_sums(_BOUNDED_WITNESS),
    )

    # the bounded odd set: certificates give 4 elements, dimension is 8
    checker.check(
        'bounded odd set: 9 distinct odd integers with max <= 2 min',
        len(set(_ODD_BOUNDED)) == 9
        and all(x % 2 == 1 for x in _ODD_BOUNDED)
        and max(_ODD_BOUNDED) <= 2 * min(_ODD_BOUNDED),
    )
    found = largest_certificate(_ODD_BOUNDED)
    checker.check(
        'bounded odd set: largest graded-pivot certificate has 3 companions',
        found == 3,
        str(found),
    )
    checker.check(
        'bounded odd set: witness of size 8 is dissociated',
        dissociated(_ODD_BOUNDED_WITNESS),
    )
    found = dissociation_number(_ODD_BOUNDED)
    checker.check('bounded odd set: dissociation number is 8', found == 8, str(found))

    # the diameter example: three cheapest levels always cost more
    diameter = max(_DIAMETER) - min(_DIAMETER)
    totals = [
        sum(sorted(costs.values())[:3])
        for costs in (cheapest_level_costs(a, _DIAMETER) for a in _DIAMETER)
        if len(costs) >= 3
    ]
    checker.check(
        'diameter set: every pivot with three levels pays more than the diameter',
        bool(totals) and min(totals) > diameter,
        f'{min(totals)} vs {diameter}',
    )

    # The free center is part of the exact certificate, not an approximation.
    for name, ambient, a, companions, center, expected_cost in _CENTERED:
        selected = (a, *companions)
        levels = [_v2(b - a) for b in companions]
        total = sum(abs(x - center) for x in selected)
        checker.check(
            f'{name}: retained free-center certificate satisfies its hypotheses',
            set(selected) <= set(ambient)
            and len(set(selected)) == len(selected)
            and len(set(levels)) == len(levels)
            and total == expected_cost
            and total < center
            and recentered_hypothesis(a, companions),
            f'cost {total} < center {center}',
        )
        checker.check(
            f'{name}: certified subset sums are distinct; old predicate rejects',
            distinct_subset_sums(selected) and not graded_hypothesis(a, companions),
        )
    checker.check(
        'recentered predicate rejects the dependent set {1,5,7,13}',
        not distinct_subset_sums((1, 5, 7, 13))
        and not recentered_hypothesis(5, (1, 7, 13)),
    )
    xs = _RECENTERED_DIAMETER
    diameter = max(xs) - min(xs)
    best = minimum_centered_cost(xs, 5)
    checker.check(
        'free-center diameter obstruction: every five-level star costs more',
        len(xs) == len(set(xs)) == 32
        and min(xs) > 0
        and diameter == 512000052
        and best == 512668211
        and best > diameter,
        f'minimum cost {best}, diameter {diameter}',
    )
    witness = _RECENTERED_DIAMETER_WITNESS
    pivot, *rest = witness
    checker.check(
        'free-center diameter obstruction: minimizing star is dissociated',
        set(witness) <= set(xs)
        and len({_v2(b - pivot) for b in rest}) == 5
        and sum(abs(b - pivot) for b in witness) == best
        and best < pivot
        and distinct_subset_sums(witness),
    )
    control = minimum_centered_cost(tuple(range(1, 33)), 5)
    checker.check(
        'free-center diameter comparison: consecutive integers satisfy the estimate',
        control is not None and control <= 31,
    )
    xs = _SPLIT_ODD
    depths = [len(cheapest_level_costs(a, xs)) for a in xs]
    checker.check(
        'split-tree odd set: ratio below two and exactly two seven-level pivots',
        len(xs) == len(set(xs)) == 65
        and all(a > 0 and a % 2 == 1 for a in xs)
        and max(xs) < 2 * min(xs)
        and depths[0] == depths[64] == 7
        and all(depth == 6 for depth in depths[1:64]),
    )
    defect = minimum_centered_cost(xs, 7, budget_multiple=2)
    checker.check(
        'split-tree odd set: every seven-level star fails even a free center',
        defect == 892,
        f'minimum centered defect {defect}',
    )
    witness = _SPLIT_ODD_WITNESS
    checker.check(
        'split-tree odd set: eight dissociated elements and a seven-element certificate',
        set(witness) <= set(xs)
        and distinct_subset_sums(witness)
        and graded_hypothesis(witness[1], witness[2:]),
    )
    control = minimum_centered_cost(
        tuple(2049 + 2 * c for c in range(65)), 7, budget_multiple=2
    )
    checker.check(
        'split-tree comparison: the translated odd progression passes',
        control is not None and control < 0,
    )
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
