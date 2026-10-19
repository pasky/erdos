"""Check the finite content of L214's lemmas on small exact instances.

Exact rational arithmetic (fractions.Fraction); repository tools harness and
the Python standard library. The program builds every member of each family
it names and checks, by brute force over all nonempty subsets of members:

1. the block family B(rho, m) for (rho, m) in (2,2), (2,3), (2,4), (2,5),
   (3,3), (3,4), (3,5), (4,4): it is intersecting and (m+1)-uniform, has
   rho^m + m rho^(m-rho) distinct members, satisfies
   P[I in A] <= phi rho^(1-|I|) for every nonempty I (phi =
   max(1,kappa)/(1+kappa), kappa = m rho^(-rho)), and attains phi on a
   singleton (Lemma 3 of the proof);
2. the substitution recursion E_{G[H]}(R) = psi_G(E_H(R)) of Lemma 2, for
   five pairs (G, H) of small intersecting families at five rational R,
   together with uniformity, member count and intersection of G[H]
   (Lemma 1);
3. two instances of the spread conclusion: B(2,4), the family of the
   statement at rho = 2, and B(2,2)^2, an instance of the general form
   (phi^h rho <= 1) recorded in the proof; each is normalized 2-spread.

These are finite checks of the lemmas and of small instances. The statement
for general rho, and the thinning part, rest on the written proof; no
asymptotic or probabilistic clause is checked here. Runtime is under five
seconds. Nothing is read from or written to disk.
"""
import itertools
import sys
from collections import Counter
from fractions import Fraction
from tools import Checker, evidence_parser


def block_family(rho, m):
    """B(rho, m) on points 0 (x), 1 (z) and consecutive blocks of rho points."""
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


def containment_counts(family):
    """Map each nonempty subset of a member to the number of members containing it."""
    counts = Counter()
    for member in family:
        ordered = tuple(sorted(member))
        for size in range(1, len(ordered) + 1):
            for subset in itertools.combinations(ordered, size):
                counts[subset] += 1
    return counts


def profile(family):
    """Largest containment probability for each subset size, exactly."""
    total = len(family)
    best = {}
    for t, c in containment_counts(family).items():
        best[len(t)] = max(best.get(len(t), Fraction(0)), Fraction(c, total))
    return best


def excess(best, r):
    """E_F(r) = max over nonempty T of P[T in S] r^|T|, from the profile of F."""
    return max(p * r ** size for size, p in best.items())


def substitute(outer, inner):
    """G[H]: points (i, u) encoded as i * width + index of u."""
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


def uniform(family, size):
    return all(len(member) == size for member in family)


def main():
    evidence_parser(__doc__, quick=False).parse_args()
    checker = Checker()
    # Lemma 3 on small block families
    for rho, m in [(2, 2), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5), (4, 4)]:
        family = block_family(rho, m)
        kappa = Fraction(m, rho ** rho)
        phi = max(Fraction(1), kappa) / (1 + kappa)
        counts = containment_counts(family)
        total = len(family)
        bound_holds = all(Fraction(c, total) <= phi * Fraction(rho) ** (1 - len(t))
                          for t, c in counts.items())
        singleton_max = max(Fraction(c, total) for t, c in counts.items() if len(t) == 1)
        checker.check(f'B({rho},{m}) has rho^m + m rho^(m-rho) distinct members',
                      len(set(family)) == total == rho ** m + m * rho ** (m - rho))
        checker.check(f'B({rho},{m}) is (m+1)-uniform and intersecting',
                      uniform(family, m + 1) and intersecting(family))
        checker.check(f'B({rho},{m}) satisfies P[I in A] <= phi rho^(1-|I|)', bound_holds)
        checker.check(f'B({rho},{m}) attains phi on a singleton', singleton_max == phi)
    # Lemmas 1 and 2 on small substitutions
    point = [frozenset([0])]
    triangle = [frozenset(e) for e in ([0, 1], [0, 2], [1, 2])]
    b22 = block_family(2, 2)
    b23 = block_family(2, 3)
    pairs = [('triangle[triangle]', triangle, triangle),
             ('triangle[B(2,3)]', triangle, b23),
             ('B(2,2)[triangle]', b22, triangle),
             ('B(2,3)[triangle]', b23, triangle),
             ('B(2,2)[B(2,2)]', b22, b22)]
    rates = [Fraction(3, 2), Fraction(2), Fraction(5, 2), Fraction(3), Fraction(7, 2)]
    for name, outer, inner in pairs:
        composed = substitute(outer, inner)
        a = len(outer[0])
        b = len(inner[0])
        outer_best, inner_best, composed_best = profile(outer), profile(inner), profile(composed)
        checker.check(f'{name} is ab-uniform with |G||H|^a distinct members',
                      uniform(composed, a * b)
                      and len(set(composed)) == len(composed) == len(outer) * len(inner) ** a)
        checker.check(f'{name} is intersecting', intersecting(composed))
        checker.check(f'{name} satisfies E_(G[H])(R) = psi_G(E_H(R)) at five rates',
                      all(excess(composed_best, r) == excess(outer_best, excess(inner_best, r))
                          for r in rates))
    checker.check('substitution into the one-point family returns G itself',
                  sorted(map(sorted, substitute(b22, point))) == sorted(map(sorted, b22)))
    # small instances of the spread conclusion
    b24 = block_family(2, 4)
    checker.check('B(2,4), the rho = 2 family of the statement, is normalized 2-spread',
                  excess(profile(b24), Fraction(2)) <= 1 and len(b24) >= 2 ** 5)
    b22_squared = substitute(b22, b22)
    checker.check('B(2,2)^2 (phi^2 rho = 8/9) is normalized 2-spread',
                  excess(profile(b22_squared), Fraction(2)) <= 1 and len(b22_squared) >= 2 ** 9)
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
