"""Valuation reconstruction of Harrington's repeated-3 example and kernel bound.

Mathematical specification: support_concentration.md. All arithmetic is exact.
The catalogue and a separate recursive partition are built from formulas;
no PDF, private file, numerical solver, or cached result is read.
"""

from __future__ import annotations

from fractions import Fraction
from math import prod

from tools import Checker

# A clause is a tuple of (prime, exponent, residue) conditions.
Clause = tuple[tuple[int, int, int], ...]
Shape = tuple[tuple[int, int], ...]


def clause(*conditions: tuple[int, int, int]) -> Clause:
    """Normalize a conjunction of prime-power congruences."""
    if len({p for p, _, _ in conditions}) != len(conditions):
        raise ValueError('a prime occurs twice in a clause')
    return tuple(sorted((p, e, a % p**e) for p, e, a in conditions))


def shape(c: Clause) -> Shape:
    """Return the exponent vector specifying the modulus."""
    return tuple((p, e) for p, e, _ in c)


def catalogue() -> dict[Shape, Clause]:
    """Classes covering 3Z; all moduli are distinct and greater than 3."""
    out: dict[Shape, Clause] = {}

    def add(c: Clause) -> None:
        old = out.setdefault(shape(c), c)
        if old != c:
            raise ValueError('two distinct residues with the same modulus')

    for n in range(1, 16):
        add(clause((3, n + 1, 3**n)))
        h3 = (3, n + 1, 2 * 3**n)
        for s in range(12):
            add(clause((5, s + 1, 5**s)))
            add(clause((3, 1, 0), (5, s + 1, 2 * 5**s)))
            add(clause(h3, (5, s + 1, 3 * 5**s)))
            h5 = (5, s + 1, 4 * 5**s)
            for u in range(10):
                add(clause((7, u + 1, 7**u)))
                add(clause((3, 1, 0), (7, u + 1, 2 * 7**u)))
                add(clause(h5, (7, u + 1, 3 * 7**u)))
                add(clause((3, 1, 0), h5, (7, u + 1, 4 * 7**u)))
                add(clause(h3, (7, u + 1, 5 * 7**u)))
                add(clause(h3, h5, (7, u + 1, 6 * 7**u)))
    for p, q, depth in ((7, 11, 10), (5, 13, 12), (3, 17, 16)):
        add(clause((q, 1, 0)))
        for j in range(1, depth + 1):
            add(clause((p, j, 0), (q, 1, j)))
    return out


def partition() -> list[tuple[Clause, Shape]]:
    """Partition 3Z into leaf cylinders, each labelled by a covering shape.

    At each nonterminal node, split into all digits of the next prime-power
    level. At a depth cutoff, split into all residues of the auxiliary prime.
    """
    leaves: list[tuple[Clause, Shape]] = []

    def record(box: dict[int, tuple[int, int]], chosen: Clause) -> None:
        leaves.append(
            (clause(*((p, e, a) for p, (e, a) in box.items())), shape(chosen))
        )

    def close(box: dict[int, tuple[int, int]], p: int, q: int) -> None:
        for j in range(q):
            leaf = {**box, q: (1, j)}
            chosen = clause((q, 1, 0)) if j == 0 else clause((p, j, 0), (q, 1, j))
            record(leaf, chosen)

    def branch7(box: dict[int, tuple[int, int]], n: int, s: int, u: int) -> None:
        if u == 10:
            close(box, 7, 11)
            return
        for digit in range(7):
            h7 = (7, u + 1, digit * 7**u)
            leaf = {**box, 7: (h7[1], h7[2])}
            if digit == 0:
                branch7(leaf, n, s, u + 1)
                continue
            chosen = [h7]
            if digit in (2, 4):
                chosen.append((3, 1, 0))
            if digit in (3, 4, 6):
                chosen.append((5, s + 1, 4 * 5**s))
            if digit in (5, 6):
                chosen.append((3, n + 1, 2 * 3**n))
            record(leaf, clause(*chosen))

    def branch5(box: dict[int, tuple[int, int]], n: int, s: int) -> None:
        if s == 12:
            close(box, 5, 13)
            return
        for digit in range(5):
            h5 = (5, s + 1, digit * 5**s)
            leaf = {**box, 5: (h5[1], h5[2])}
            if digit == 0:
                branch5(leaf, n, s + 1)
            elif digit == 4:
                branch7(leaf, n, s, 0)
            else:
                chosen = [h5]
                if digit == 2:
                    chosen.append((3, 1, 0))
                elif digit == 3:
                    chosen.append((3, n + 1, 2 * 3**n))
                record(leaf, clause(*chosen))

    def branch3(box: dict[int, tuple[int, int]], n: int) -> None:
        if n == 16:
            close(box, 3, 17)
            return
        for digit in range(3):
            h3 = (3, n + 1, digit * 3**n)
            leaf = {**box, 3: (h3[1], h3[2])}
            if digit == 0:
                branch3(leaf, n + 1)
            elif digit == 1:
                record(leaf, clause(h3))
            else:
                branch5(leaf, n, 0)

    branch3({3: (1, 0)}, 1)
    return leaves


def covers(c: Clause, box: Clause) -> bool:
    """Whether a clause contains the entire cylinder box."""
    b = {p: (e, a) for p, e, a in box}
    return all(p in b and b[p][0] >= e and (b[p][1] - a) % p**e == 0 for p, e, a in c)


def partition_valid(
    classes: dict[Shape, Clause], leaves: list[tuple[Clause, Shape]]
) -> bool:
    """Validate each leaf against the separate covering catalogue."""
    return all(s in classes and covers(classes[s], box) for box, s in leaves)


def concentration_floor(primes: list[int], depth3: int, depth_other: int) -> Fraction:
    """Average the point kernel with its centre in one first-digit 3 branch."""
    result = Fraction(1) + sum(
        (Fraction(2 * t + 1, 3 ** (t - 1)) for t in range(1, depth3 + 1)), Fraction(0)
    )
    for p in primes:
        if p != 3:
            result *= Fraction(1) + sum(
                (
                    Fraction(2 * t + 1, (p - 1) * p ** (t - 1))
                    for t in range(1, depth_other + 1)
                ),
                Fraction(0),
            )
    return result


def check_concentration(checker: Checker, primes: list[int]) -> None:
    """Check the finite symbolic cover, surviving point, and rational bounds."""
    classes = catalogue()
    leaves = partition()
    checker.check(
        'repeated-3 construction: 2470 distinct odd moduli greater than 3',
        len(classes) == 2470
        and all(prod(p**e for p, e, _ in c) > 3 for c in classes.values())
        and all(p in (3, 5, 7, 11, 13, 17) for c in classes.values() for p, _, _ in c),
    )
    checker.check(
        'valuation partition: 13547 leaves of total density 1/3, all contained in 3Z',
        len(leaves) == 13547
        and sum(
            (Fraction(1, prod(p**e for p, e, _ in box)) for box, _ in leaves),
            Fraction(0),
        )
        == Fraction(1, 3)
        and all(covers(clause((3, 1, 0)), box) for box, _ in leaves),
    )
    checker.check(
        'every partition leaf lies in its designated covering class',
        partition_valid(classes, leaves),
    )
    damaged = dict(classes)
    damaged.pop(((17, 1),))
    checker.check(
        'negative control: deleting the pure 17-class breaks the partition certificate',
        not partition_valid(damaged, leaves),
    )
    witness = clause(*((p, 16, 2 if p in (3, 5, 7) else 1) for p in primes))
    checker.check(
        'the distinct family with 1 mod 3 leaves the explicit CRT point uncovered',
        not covers(clause((3, 1, 1)), witness)
        and not any(covers(c, witness) for c in classes.values()),
    )
    # A class modulo the full period, at witness+1, realizes depth 16 at
    # every prime while avoiding the witness. Missing prime-modulus classes
    # are chosen at its first digit plus one. No residue enumeration is needed.
    full_shape = tuple((p, 16) for p in primes)
    extended = {**classes, ((3, 1),): clause((3, 1, 1))}
    for p in primes:
        if ((p, 1),) not in extended:
            extended[((p, 1),)] = clause((p, 1, 2))
    extended[full_shape] = clause(*((p, e, a + 1) for p, e, a in witness))
    checker.check(
        'depth-16 period extension has 2486 distinct moduli and retains the witness',
        len(extended) == 2486
        and all(shape(c) == s for s, c in extended.items())
        and not any(covers(c, witness) for c in extended.values())
        and all(e <= 16 for c in extended.values() for _, e, _ in c),
    )
    extra_primes = [p for p in primes if p >= 11 and p != 17]
    density_extension = dict(extended)
    for q in extra_primes:
        c = clause((3, 1, 2), (q, 1, 1))
        if shape(c) in density_extension:
            raise ValueError('the density extension would repeat a modulus')
        density_extension[shape(c)] = c
    new_witness = clause(
        *((p, 16, 2 if p < 17 else 1 if p == 17 else 3) for p in primes)
    )
    checker.check(
        'density extension: 2502 distinct moduli with an explicit surviving CRT point',
        len(extra_primes) == 16
        and len(density_extension) == 2502
        and not any(covers(c, new_witness) for c in density_extension.values()),
    )
    u5 = (1 - Fraction(1, 5**11)) / 16
    u7 = (1 - Fraction(1, 7**9)) / 36
    v5 = Fraction(5, 16) * (1 - Fraction(1, 5**12))
    v7 = Fraction(7, 36) * (1 - Fraction(1, 7**10))
    density_upper = (
        Fraction(1, 2)
        * (1 - u5 - u7 + u5 * u7 - v5 * v7)
        * prod(Fraction(q - 2, q - 1) for q in extra_primes)
    )
    checker.check(
        'density extension: exact upper density below 1/4, original lower density above 1/4',
        0 < density_upper < Fraction(1, 4) < Fraction(773, 1920)
        and Fraction(1, 2)
        * (1 - Fraction(43, 288) - Fraction(7, 360) - Fraction(5, 192))
        == Fraction(773, 1920),
    )
    for d3, dother, low, high in (
        (4, 4, 14680, 14681),
        (16, 4, 15162, 15163),
        (16, 16, 15214, 15215),
    ):
        value = concentration_floor(primes, d3, dother)
        checker.check(
            f'forced first 3-digit: depths {d3}/{dother}, kernel in ({low}/100, {high}/100)',
            Fraction(low, 100) < value < Fraction(high, 100)
            and value > Fraction(138877, 1000),
        )
