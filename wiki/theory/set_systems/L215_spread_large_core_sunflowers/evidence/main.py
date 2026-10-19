"""Check the finite content of L215's lemmas on small exact instances.

Exact integer and rational arithmetic; repository tools harness and the
Python standard library. The program builds every member of each family it
names and checks:

1. the triangle powers D, D^2 and D^3 are intersecting and contain no
   k-sunflower for k = 3 and k = 4 (exhaustive over k-subsets for D and
   D^2; for D^3, by testing every possible core: no petal family of a core
   has k pairwise disjoint members); for D and D^2 only, their excess at
   R = 3, 4, 9/2 equals 3 (R/3)^(2^g) (Lemma A of the proof);
2. the core lemma (Lemma B) on the substitutions B(3,3)[D] and B(2,3)[D]:
   each is intersecting and has no 4-sunflower; the smallest core of a
   3-sunflower has exactly 2 points in B(3,3)[D], where B(3,3) has
   3-sunflowers with a 1-point core, and exactly 4 points in B(2,3)[D],
   where every 3-sunflower of B(2,3) has a 2-point core, as the lemma's
   description of the core as whole fibers over the outer core predicts;
3. the spread recursion of L214's Lemma 2 on B(3,3)[D] at five rates.

A k-sunflower with core C is the same as k members containing C whose
differences with C are pairwise disjoint; the core test enumerates every
candidate core of the given size and looks for k pairwise disjoint petals.
These are finite checks of the lemmas. The statement for general k, g and
R rests on the written proof. Runtime is under a minute. Nothing is read
from or written to disk.
"""
import itertools
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from tools import Checker, evidence_parser


def block_family(rho, m):
    point = 2
    blocks = []
    for _ in range(m):
        blocks.append(tuple(range(point, point + rho)))
        point += rho
    other = []
    for _ in range(m - rho):
        other.append(tuple(range(point, point + rho)))
        point += rho
    family = [frozenset((0,) + t) for t in itertools.product(*blocks)]
    for block in blocks:
        for w in itertools.product(*other):
            family.append(frozenset((1,) + block + w))
    return family


def substitute(outer, inner):
    points = sorted(set().union(*inner))
    index = {u: k for k, u in enumerate(points)}
    width = len(points)
    out = []
    for root in outer:
        root = sorted(root)
        for choice in itertools.product(inner, repeat=len(root)):
            out.append(frozenset(i * width + index[u]
                                 for i, fiber in zip(root, choice) for u in fiber))
    return out


def intersecting(family):
    masks = [sum(1 << v for v in member) for member in family]
    return all(masks[i] & masks[j]
               for i in range(len(masks)) for j in range(i + 1, len(masks)))


def profile(family):
    total = len(family)
    counts = Counter()
    for member in family:
        ordered = tuple(sorted(member))
        for size in range(1, len(ordered) + 1):
            for subset in itertools.combinations(ordered, size):
                counts[subset] += 1
    best = {}
    for t, c in counts.items():
        best[len(t)] = max(best.get(len(t), Fraction(0)), Fraction(c, total))
    return best


def excess(best, r):
    return max(p * r ** size for size, p in best.items())


def has_disjoint(petals, k):
    """Whether k pairwise disjoint sets occur among the bitmasks in petals."""
    n = len(petals)
    adjacency = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if petals[i] & petals[j] == 0:
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i

    def extend(candidates, depth):
        if depth == 0:
            return True
        while candidates:
            low = candidates & -candidates
            i = low.bit_length() - 1
            candidates ^= low
            if extend(candidates & adjacency[i], depth - 1):
                return True
        return False

    return extend((1 << n) - 1, k)


def petal_map(family, size):
    """Map each core of the given size to the petal bitmasks of members containing it."""
    petals = defaultdict(list)
    for member in family:
        mask = sum(1 << v for v in member)
        for core in itertools.combinations(sorted(member), size):
            core_mask = sum(1 << v for v in core)
            petals[core].append(mask & ~core_mask)
    return petals


def min_core_at_least(family, k, bound):
    """No k-sunflower with a core of fewer than bound points (cores of size 0 included)."""
    masks = [sum(1 << v for v in member) for member in family]
    if bound > 0 and has_disjoint(masks, k):
        return False
    for size in range(1, bound):
        for petals in petal_map(family, size).values():
            if len(petals) >= k and has_disjoint(petals, k):
                return False
    return True


def sunflower_with_core_size(family, k, size):
    return any(len(petals) >= k and has_disjoint(petals, k)
               for petals in petal_map(family, size).values())


def no_sunflower_exhaustive(family, k):
    for group in itertools.combinations(family, k):
        cores = {a & b for a, b in itertools.combinations(group, 2)}
        if len(cores) == 1:
            return False
    return True


def no_sunflower_by_cores(family, k):
    width = len(next(iter(family)))
    return min_core_at_least(family, k, width)


def main():
    evidence_parser(__doc__, quick=False).parse_args()
    checker = Checker()
    point = [frozenset([0])]
    triangle = [frozenset(e) for e in ([0, 1], [0, 2], [1, 2])]
    powers = {0: point, 1: triangle}
    for g in (2, 3):
        powers[g] = substitute(triangle, powers[g - 1])
    # Lemma A: triangle powers
    for g in (1, 2, 3):
        family = powers[g]
        checker.check(f'D^{g} has 3^(2^{g}-1) members of size 2^{g} and is intersecting',
                      len(set(family)) == len(family) == 3 ** (2 ** g - 1)
                      and all(len(s) == 2 ** g for s in family) and intersecting(family))
        for k in (3, 4):
            test = no_sunflower_exhaustive if g <= 2 else no_sunflower_by_cores
            checker.check(f'D^{g} has no {k}-sunflower', test(family, k))
        best = profile(family) if g <= 2 else None
        if best is not None:
            checker.check(f'D^{g} has excess 3 (R/3)^(2^{g}) at R = 3, 4, 9/2',
                          all(excess(best, r) == 3 * (r / 3) ** (2 ** g)
                              for r in (Fraction(3), Fraction(4), Fraction(9, 2))))
    # Lemma B: cores of substitutions into the triangle D
    for rho, m, smallest in [(3, 3, 2), (2, 3, 4)]:
        outer = block_family(rho, m)
        family = substitute(outer, triangle)
        name = f'B({rho},{m})[D]'
        checker.check(f'{name} is intersecting', intersecting(family))
        checker.check(f'{name} has no 4-sunflower', no_sunflower_by_cores(family, 4))
        checker.check(f'{name}: every 3-sunflower has a core of at least {smallest} points',
                      min_core_at_least(family, 3, smallest))
        checker.check(f'{name}: some 3-sunflower has a core of exactly {smallest} points',
                      sunflower_with_core_size(family, 3, smallest))
    # spread recursion on B(3,3)[D]
    outer = block_family(3, 3)
    family = substitute(outer, triangle)
    rates = [Fraction(3, 2), Fraction(2), Fraction(5, 2), Fraction(3), Fraction(4)]
    outer_best, inner_best, best = profile(outer), profile(triangle), profile(family)
    checker.check('B(3,3)[D] satisfies E(R) = psi_B(E_D(R)) at five rates',
                  all(excess(best, r) == excess(outer_best, excess(inner_best, r))
                      for r in rates))
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
