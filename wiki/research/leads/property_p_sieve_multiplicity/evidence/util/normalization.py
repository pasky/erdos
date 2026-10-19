"""Exact finite checks of normalization, Euler weights, and obstruction families.

The infinite conclusions are proved in the lead, not by these samples.
"""

from __future__ import annotations

import math
from collections import defaultdict
from collections.abc import Callable
from fractions import Fraction
from functools import lru_cache

from tools import Checker


@lru_cache(maxsize=100_000)
def prime_factors(value: int) -> tuple[int, ...]:
    """Return the distinct prime factors of a positive integer."""
    found: list[int] = []
    prime = 2
    while prime * prime <= value:
        if value % prime == 0:
            found.append(prime)
            while value % prime == 0:
                value //= prime
        prime += 1
    if value > 1:
        found.append(value)
    return tuple(found)


def harmonic(values: list[int] | tuple[int, ...]) -> Fraction:
    """Sum reciprocals exactly."""
    return sum((Fraction(1, value) for value in values), Fraction())


def density(excluded: set[int] | frozenset[int] | tuple[int, ...]) -> Fraction:
    """Return the density of integers avoiding these distinct primes."""
    return math.prod((Fraction(p - 1, p) for p in excluded), start=Fraction(1))


def partition(values: list[int]) -> tuple[list[int], dict[tuple[int, int], list[int]]]:
    """Select the greedy coprime list and assign each remainder to its first hit."""
    selected: list[int] = []
    owner: dict[int, int] = {}
    children: dict[tuple[int, int], list[int]] = defaultdict(list)
    for value in sorted(values):
        factors = prime_factors(value)
        hits = [(owner[p], p) for p in factors if p in owner]
        if not hits:
            for prime in factors:
                owner[prime] = len(selected)
            selected.append(value)
        else:
            index, prime = min(hits)
            children[index, prime].append(value // prime)
    return selected, dict(children)


def inherited(
    excluded: frozenset[int], selected: list[int], index: int, prime: int
) -> frozenset[int]:
    """Compute exactly the excluded primes in (19)."""
    result = set(excluded)
    for value in selected[:index]:
        result.update(prime_factors(value))
    result.update(q for q in prime_factors(selected[index]) if q < prime)
    return frozenset(result)


def tree_checks(checker: Checker, values: list[int], label: str) -> None:
    """Check ownership, descent, inherited exclusions, and both telescoping sums."""
    stack = [(values, frozenset(), 1)]
    cost = Fraction()
    loss = Fraction()
    nodes = 0
    valid = True
    while stack:
        current, excluded, divisor = stack.pop()
        nodes += 1
        selected, children = partition(current)
        assigned = list(selected)
        child_mass = Fraction()
        child_density = Fraction()
        for (index, prime), child in children.items():
            new_excluded = inherited(excluded, selected, index, prime)
            assigned.extend(prime * value for value in child)
            valid &= max(child) < max(current)
            valid &= all(prime * value > selected[index] for value in child)
            valid &= all(value % q for value in child for q in new_excluded)
            child_mass += harmonic(child) / prime
            child_density += density(new_excluded) / prime
            stack.append((child, new_excluded, divisor * prime))
        all_primes = {p for value in selected for p in prime_factors(value)}
        valid &= sorted(assigned) == sorted(current)
        valid &= harmonic(current) == harmonic(selected) + child_mass
        valid &= not (all_primes & excluded)
        valid &= child_density <= density(excluded) * (1 - density(all_primes))
        cost += harmonic(selected) / divisor
        loss += (density(excluded) - child_density) / divisor
    checker.check(
        f'{label}: ownership, descent, exclusions, and node identities', valid
    )
    checker.check(
        f'{label}: exact mass telescopes over {nodes} nodes', cost == harmonic(values)
    )
    checker.check(f'{label}: exact Euler leftover weights telescope to one', loss == 1)


def primes_up_to(limit: int) -> list[int]:
    """Generate all primes through a fixed finite limit with an integer sieve."""
    sieve = bytearray([1]) * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = bytes(len(range(p * p, limit + 1, p)))
    return [p for p in range(2, limit + 1) if sieve[p]]


def obstruction_checks(
    checker: Checker, property_p: Callable[[list[int]], bool]
) -> None:
    """Check finite instances of (16), (23), and the normalization identities."""
    # The caller supplies the independent residue-scan checker.
    for values in ([1, 2], [2, 3, 4], [4, 6, 8, 9], [6, 9, 10, 12, 22, 34]):
        checker.check(f'boundary witness {values} has property P', property_p(values))
        tree_checks(checker, values, f'boundary witness {values}')

    odd_primes = (3, 5, 7, 11, 13)
    for count, multiplier in ((3, 1), (3, 3), (4, 1), (5, 1)):
        primes = odd_primes[:count]
        product = math.prod(primes)
        base = product * multiplier
        values = [base] + [
            n for n in range(base + 1, (3 * base + 1) // 2) if math.gcd(n, product) > 1
        ]
        selected, branches = partition(values)
        checker.check(
            f'(16), k={count}, M={base}: one coprime witness', selected == [base]
        )
        checker.check(
            f'(16), k={count}, M={base}: every prime branch is present',
            set(branches) == {(0, p) for p in primes},
        )
        checker.check(
            f'(16), k={count}, M={base}: exact branch order',
            all(p * min(branches[0, p]) == base + p for p in primes),
        )
        checker.check(
            f'(16), k={count}, M={base}: automatic-P interval hypotheses',
            all(base <= n and 2 * n < 3 * base for n in values),
        )
        if base <= 1155:
            checker.check(
                f'(16), k={count}, M={base}: direct property P', property_p(values)
            )
            tree_checks(checker, values, f'(16), k={count}, M={base}')
        delta = Fraction(1)
        total_density = Fraction()
        for index, p in enumerate(primes, start=1):
            checker.check(
                f'(17), k={count}, branch={index}: delta >= 1/j',
                delta >= Fraction(1, index),
            )
            total_density += delta / p
            delta *= Fraction(p - 1, p)
        checker.check(
            f'(20), k={count}: full first generation has weight 1-delta',
            total_density == 1 - density(primes),
        )
        if count == 5:
            checker.check(
                '(16): fifth normalized branch exceeds the unscaled 2^(1-j) proposal',
                harmonic(branches[0, 13]) > Fraction(1, 16),
            )

    # A fixed early element defeats charging the current toll to its leftover.
    for factors, exponent in (((5,), 4), ((5, 7), 2)):
        product = math.prod(factors)
        base = product**exponent
        values = [3, base, base + 2] + [
            n
            for n in range(base + 1, (3 * base + 1) // 2)
            if n % 3 == 1 and math.gcd(n, product) > 1
        ]
        selected, branches = partition(values)
        left = Fraction(1) - sum(
            (density(inherited(frozenset(), selected, i, p)) / p for i, p in branches),
            Fraction(),
        )
        checker.check(f'direct toll, M={base}: property P', property_p(values))
        checker.check(
            f'direct toll, M={base}: exact coprime list and every root branch',
            selected == [3, base]
            and set(branches) == {(0, 3)} | {(1, p) for p in factors},
        )
        checker.check(
            f'direct toll, M={base}: Euler leftover and current selected mass',
            left == Fraction(2, 3) * density(factors)
            and harmonic(selected) == Fraction(1, 3) + Fraction(1, base),
        )
        tree_checks(checker, values, f'direct toll, M={base}')

    # Generate semiprimes directly, retaining the exact finite domain in code.
    for cutoff in (7, 13, 31):
        base = cutoff**3
        primes = primes_up_to(3 * base // 4)
        small = [p for p in primes if p <= cutoff]
        values = sorted(
            {
                p * q
                for p in small
                for q in primes
                if base < p * q < Fraction(3 * base, 2)
            }
        )
        selected, branches = partition(values)
        used_large = {max(prime_factors(n)) for n in selected}
        selected_small = {min(prime_factors(n)) for n in selected}
        checker.check(f'(23), y={cutoff}: direct property P', property_p(values))
        checker.check(
            f'(23), y={cutoff}: all small primes matched once',
            selected_small == set(small) and len(selected) == len(small),
        )
        checker.check(
            f'(23), y={cutoff}: every small-prime branch is nonempty',
            all(any(p == edge[1] for edge in branches) for p in small),
        )
        checker.check(
            f'(23), y={cutoff}: small-prime children consist of primes',
            all(
                prime_factors(n) == (n,)
                for (i, p), child in branches.items()
                if p <= cutoff
                for n in child
            ),
        )
        child_mass = sum(
            (harmonic(partition(child)[0]) / p for (i, p), child in branches.items()),
            Fraction(),
        )
        left = Fraction(1) - sum(
            (density(inherited(frozenset(), selected, i, p)) / p for i, p in branches),
            Fraction(),
        )
        checker.check(
            f'(25), y={cutoff}: exact empty-branch upper bound',
            0 < left <= density(tuple(small)) + harmonic(tuple(used_large)),
        )
        checker.check(
            f'(24), y={cutoff}: root toll bound',
            harmonic(selected) <= Fraction(1, cutoff**2),
        )
        available = sum(
            (
                Fraction(1, p)
                * harmonic(
                    tuple(q for q in primes if base < p * q < Fraction(3 * base, 2))
                )
                for p in small
            ),
            Fraction(),
        )
        checker.check(
            f'(24), y={cutoff}: discarded large-prime cost bound',
            child_mass >= available - Fraction(1, cutoff),
        )
        tree_checks(checker, values, f'(23), y={cutoff}')

    small_prime_sum = sum((Fraction(1, p * p) for p in primes_up_to(1000)), Fraction())
    checker.check(
        'Proposition C: explicit prime-square sum upper bound below 0.46',
        small_prime_sum + Fraction(1, 1000) < Fraction(46, 100),
    )
