"""Check the finite statements of the property-P sieve lead on Problem 12.

Property P is read with distinct larger summands: no ``a`` in ``A`` divides
``b + c`` for distinct ``b, c`` in ``A`` with ``b, c > a``. The checks are:

- the worked examples of the lead have property P, in exact integer
  arithmetic: the truncated gcd-one set ``{3} | {2p^2}``, the finite set
  ``{4, 6, 8, 9}``, and every block ``{n = 1 mod L : x < n <= L*x/2}`` on a
  grid of ``(L, x)``, whose class first breaks property P within ``L`` of
  ``(L + 2) * a0 / 2``, where ``a0`` is the block's least element;
- the maximal residue occupancy of the occupancy lemma, by exhaustive search,
  for pairwise coprime moduli and for the non-coprime pair ``{15, 21}``;
- the greedy coprime sequence of the truncated gcd-one set stops at
  ``{3, 98}``, so a finite prime set covers the rest;
- for the greedy property-P set of primes below ``10**6``, the reciprocal
  mass of each region of the pairwise-coprime theorem against that region's
  bound, and the sum against the theorem's constant;
- the greedy property-P set of integers from 3 below ``10**5`` has 72
  elements and reciprocal sum ``1.10816...``;
- the shared-part bound (13) on the greedy sets and the truncated example;
- the maximal reciprocal sum of a property-P subset of ``[3, N]`` for
  ``N = 20, 40, 60, 80, 100``, and of a property-P subset of ``[20, N]``
  inside one admissible half of the classes modulo each of the first two,
  three or four odd primes, by SciPy's mixed-integer solver, with the
  returned set's property P and exact reciprocal sum checked in rationals.

Run from the repository root:
    uv run --no-sync python wiki/research/leads/property_p_sieve_multiplicity/evidence/main.py

Dependencies are the standard library, the installed root ``tools``
package, NumPy and SciPy. The retained above-product witnesses are read from
``assets/above_product.json``; ``assets/two_block.json`` supplies the joint
window witness. There are no random choices or output files. Expected runtime
is about 90 seconds, dominated by the solver and exhaustive matching bounds.
The solver's optimality is floating-point and solver-reported; only the
property P and the reciprocal sum of the returned sets are exact. No check
proves the reciprocal-sum question, and the finite maxima prove no
uniform bound.

The normalization checks in ``util/normalization.py`` additionally verify
exact ownership, descent, inherited exclusions and both telescoping identities,
including nodes containing 1 or 2. They check finite instances of the three
obstruction families, including the semiprime matching and discarded-part
bounds. The prime-number-theorem step in the unbounded obstruction is an
external theorem, not established by these finite checks. Nine retained
solver witnesses start above the moduli product; their feasibility and rational
masses are replayed, without treating their recorded solver maxima as certified.
The two-block check additionally proves four finite upper bounds, each covering
all 16384 early subsets, using disjoint conflict matchings with integer-rounded
weights; its feasible lower witness is checked directly. These bounds are exact
at their stated finite scope and separate from solver-reported optimality.
"""

from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix
from util.normalization import obstruction_checks
from util.two_block import check_two_blocks

import tools

__all__ = [
    'has_property_p',
    'max_occupancy',
    'greedy_coprime',
    'greedy_p_set',
    'max_harmonic_p_subset',
    'main',
]

# retain one solver-reported maximizer over [3, N] for each N
_MAXIMA = {
    20: [3, 5, 6, 8, 11, 20],
    40: [3, 5, 6, 8, 11, 20, 23, 26],
    60: [3, 5, 6, 8, 11, 20, 23, 26, 56],
    80: [3, 5, 6, 8, 11, 20, 23, 26, 56, 71],
    100: [3, 5, 6, 8, 11, 20, 23, 26, 56, 71],
}


# fix one admissible half of the classes modulo each of 3, 5, 7 and 11
_HALVES = {3: {2}, 5: {1, 3}, 7: {3, 5, 6}, 11: {1, 3, 4, 5, 9}}

# retain the solver-reported maxima inside the admissible classes
_ADMISSIBLE = {
    400: {(3, 5): '0.245223', (3, 5, 7): '0.167886', (3, 5, 7, 11): '0.100233'},
    2000: {(3, 5, 7): '0.180201', (3, 5, 7, 11): '0.112996'},
}


def has_property_p(values: list[int]) -> bool:
    """Return whether no element divides a sum of two distinct larger ones."""
    # scan each element against the residues of the larger elements
    ordered = sorted(set(values))
    for index, a in enumerate(ordered):
        seen: set[int] = set()
        for b in ordered[index + 1 :]:
            residue = b % a
            if (-residue) % a in seen:
                return False
            seen.add(residue)
    return True


def max_occupancy(moduli: tuple[int, ...]) -> int:
    """Return the largest antisymmetric residue set modulo the moduli's lcm.

    A residue ``x`` is admissible when no modulus ``a`` has ``2x = 0 mod a``;
    two residues conflict when their sum is ``0`` modulo some modulus. The
    maximum independent set is found by exhaustive branching.
    """
    # build the admissible residues and the conflict graph
    lcm = math.lcm(*moduli)
    vertices = [x for x in range(lcm) if all((2 * x) % a for a in moduli)]
    index = {x: i for i, x in enumerate(vertices)}
    adjacency = [0] * len(vertices)
    for x in vertices:
        for y in vertices:
            if x != y and any((x + y) % a == 0 for a in moduli):
                adjacency[index[x]] |= 1 << index[y]
    # branch on the lowest remaining vertex, bounding by the remaining count
    best = 0

    def search(remaining: int, size: int) -> None:
        nonlocal best
        if size + remaining.bit_count() <= best:
            return
        if remaining == 0:
            best = size
            return
        low = (remaining & -remaining).bit_length() - 1
        search(remaining & ~(1 << low) & ~adjacency[low], size + 1)
        search(remaining & ~(1 << low), size)

    search((1 << len(vertices)) - 1, 0)
    return best


def greedy_coprime(values: list[int]) -> list[int]:
    """Return the greedy coprime sequence: each least element coprime to all before."""
    # take each element coprime to the product of those already taken
    chosen: list[int] = []
    product = 1
    for value in sorted(values):
        if math.gcd(value, product) == 1:
            chosen.append(value)
            product *= value
    return chosen


def greedy_p_set(limit: int, *, primes_only: bool) -> list[int]:
    """Return the greedy property-P set of integers, or of primes, in [3, limit)."""
    # sieve the primes
    sieve = bytearray([1]) * limit
    sieve[0:2] = b'\x00\x00'
    for p in range(2, math.isqrt(limit - 1) + 1):
        if sieve[p]:
            sieve[p * p : limit : p] = bytearray(len(range(p * p, limit, p)))
    # admit a candidate when its residue is not the negative of an earlier one
    chosen: list[int] = []
    forbidden: dict[int, set[int]] = {}
    for c in range(3, limit):
        if (primes_only and not sieve[c]) or any(c % a in forbidden[a] for a in chosen):
            continue
        for a in chosen:
            forbidden[a].add((-c) % a)
        chosen.append(c)
        forbidden[c] = set()
    return chosen


def max_harmonic_p_subset(elements: list[int]) -> tuple[float, list[int]]:
    """Return the solver's maximal reciprocal sum of a P-subset of ``elements``."""
    # list one constraint for each forbidden triple a < b < c with a | b + c
    elements = sorted(elements)
    position = {value: i for i, value in enumerate(elements)}
    top = elements[-1]
    rows: list[int] = []
    cols: list[int] = []
    count = 0
    for a in elements:
        for b in elements:
            if b <= a:
                continue
            c = b + 1 + ((-(2 * b + 1)) % a)
            while c <= top:
                if c in position:
                    rows += [count, count, count]
                    cols += [position[a], position[b], position[c]]
                    count += 1
                c += a
    # forbid all three members of each triple and maximize the reciprocal sum
    constraints = []
    if count:
        matrix = coo_matrix(
            (np.ones(len(rows)), (rows, cols)), shape=(count, len(elements))
        )
        constraints.append(LinearConstraint(matrix.tocsr(), -np.inf, 2))
    result = milp(
        -np.array([1.0 / value for value in elements]),
        constraints=constraints,
        integrality=np.ones(len(elements)),
        bounds=Bounds(0, 1),
        options={'mip_rel_gap': 1e-9, 'threads': 1, 'parallel': False},
    )
    if result.status != 0 or result.x is None or result.fun is None:
        raise RuntimeError(f'solver did not report optimality: {result.message}')
    chosen = [elements[i] for i in range(len(elements)) if result.x[i] > 0.5]
    return -result.fun, chosen


def shared_part_bound(values: list[int]) -> tuple[Fraction, Fraction]:
    """Return the reciprocal sum and the sum over shared parts in (13)."""
    # find the primes dividing at least two elements
    counts: dict[int, int] = {}
    for value in values:
        rest, p = value, 2
        while p * p <= rest:
            if rest % p == 0:
                counts[p] = counts.get(p, 0) + 1
                while rest % p == 0:
                    rest //= p
            p += 1
        if rest > 1:
            counts[rest] = counts.get(rest, 0) + 1
    shared = [p for p, count in counts.items() if count >= 2]
    # take the largest divisor of each element composed of shared primes
    parts = set()
    for value in values:
        part = 1
        for p in shared:
            while value % (part * p) == 0:
                part *= p
        parts.add(part)
    return sum(Fraction(1, v) for v in values), sum(Fraction(1, v) for v in parts)


def main() -> int:
    """Run every check and return the exit code."""
    tools.evidence_parser(__doc__ or '', quick=False).parse_args()
    checker = tools.Checker()
    # check the worked examples of the lead
    tail = [
        2 * p * p
        for p in range(5, 10_000)
        if all(p % q for q in range(2, math.isqrt(p) + 1)) and p % 4 == 3
    ]
    checker.check(
        '{3} | {2p^2 : p = 3 mod 4, 3 < p < 10^4} has property P',
        has_property_p([3, *tail]),
    )
    checker.check('{4, 6, 8, 9} has property P', has_property_p([4, 6, 8, 9]))
    for modulus in (3, 4, 5, 6, 7, 10, 12):
        for start in (2 * modulus + 1, 50, 101):
            top = modulus * start // 2
            ladder = [
                v for v in range(start + 1, 10 * modulus * start) if v % modulus == 1
            ]
            block = [v for v in ladder if v <= top]
            checker.check(
                f'block 1 mod {modulus} on ({start}, {top}] has property P',
                has_property_p(block),
            )
            # find the first class element whose admission breaks property P
            breaking = next(
                (
                    ladder[i]
                    for i in range(len(block), len(ladder))
                    if not has_property_p(ladder[: i + 1])
                ),
                None,
            )
            checker.check(
                f'the class 1 mod {modulus} above {start} breaks property P by (L+2)*{block[0]}/2 + L',
                breaking is not None
                and 2 * breaking <= (modulus + 2) * block[0] + 2 * modulus,
                f'first break {breaking}',
            )
    # check the maximal occupancy of the occupancy lemma
    for moduli in ((3, 4), (3, 5), (4, 5), (3, 7), (4, 7), (5, 6)):
        predicted = math.prod((a - math.gcd(a, 2)) // 2 for a in moduli)
        found = max_occupancy(moduli)
        checker.check(
            f'maximal occupancy modulo {moduli} is {predicted}',
            found == predicted,
            f'found {found}',
        )
    found = max_occupancy((15, 21))
    checker.check(
        'maximal occupancy modulo (15, 21) is 41 of 105', found == 41, f'found {found}'
    )
    # check the greedy coprime sequence of the truncated gcd-one example
    chosen = greedy_coprime([3, *tail])
    checker.check(
        'the greedy coprime sequence of {3} | {2p^2} is (3, 98)',
        chosen == [3, 98],
        f'found {chosen}',
    )
    # check the regions of the pairwise-coprime theorem on the greedy prime set
    primes = greedy_p_set(10**6, primes_only=True)
    checker.check('the greedy prime set has property P', has_property_p(primes))
    region_bound = 1 / math.log(9) + math.log(3)
    product = primes[0]
    for m in range(1, len(primes)):
        low, high = product**2, product**2 * primes[m] ** 2
        mass = sum(1 / q for q in primes if max(low, primes[m]) <= q < high)
        if not checker.check(
            f'region {m} of the greedy prime set has mass at most 2^(2-{m}) * 1.556',
            mass <= 2.0 ** (2 - m) * region_bound,
            f'mass {mass}',
        ):
            break
        product *= primes[m]
        if low > primes[-1]:
            break
    total = sum(Fraction(1, q) for q in primes)
    checker.check(
        'the greedy prime set has reciprocal sum below 10',
        total < 10,
        f'sum {float(total)}',
    )
    # check the greedy property-P set of integers
    greedy = greedy_p_set(10**5, primes_only=False)
    mass = sum(Fraction(1, v) for v in greedy)
    checker.check(
        'the greedy integer set below 10^5 has property P', has_property_p(greedy)
    )
    checker.check(
        'the greedy integer set below 10^5 has 72 elements and sum 1.1081636',
        len(greedy) == 72
        and abs(mass - Fraction(11081636, 10**7)) < Fraction(1, 10**7),
        f'{len(greedy)} elements, sum {float(mass)}',
    )
    # check the shared-part bound (13) on the greedy sets and the example (6)
    for label, values in (
        ('greedy integer set', greedy),
        ('greedy prime set', primes),
        ('example (6)', [3, *tail]),
    ):
        mass, parts = shared_part_bound(values)
        checker.check(
            f'the {label} satisfies the shared-part bound (13)',
            mass < Fraction(933, 100) * parts,
            f'sum {float(mass)}, shared parts {float(parts)}',
        )
    # check the solver maxima and the exact property of their maximizers
    previous = Fraction(0)
    for n, recorded in _MAXIMA.items():
        _, chosen = max_harmonic_p_subset(list(range(3, n + 1)))
        exact = sum(Fraction(1, v) for v in chosen)
        checker.check(f'the [3, {n}] maximizer has property P', has_property_p(chosen))
        checker.check(
            f'the [3, {n}] maximizer has the recorded reciprocal sum {float(sum(Fraction(1, v) for v in recorded)):.6f}',
            exact == sum(Fraction(1, v) for v in recorded) and has_property_p(recorded),
            f'found {chosen} with {float(exact)}',
        )
        checker.check(f'the [3, {n}] maximum is nondecreasing in N', exact >= previous)
        previous = exact
    # check the solver maxima inside admissible classes modulo 3, 5, 7, 11
    for top in (400, 2000):
        for moduli, mass in _ADMISSIBLE[top].items():
            admissible = [
                n
                for n in range(20, top + 1)
                if all(n % m in _HALVES[m] for m in moduli)
            ]
            _, chosen = max_harmonic_p_subset(admissible)
            exact = sum(Fraction(1, v) for v in chosen)
            checker.check(
                f'the admissible maximizer modulo {moduli} on [20, {top}] has property P',
                has_property_p(chosen),
            )
            checker.check(
                f'the admissible maximum modulo {moduli} on [20, {top}] is {mass}',
                abs(exact - Fraction(mass)) < Fraction(1, 10**6),
                f'found {float(exact)}',
            )
    obstruction_checks(checker, has_property_p)
    check_two_blocks(checker, has_property_p)
    asset = Path(__file__).resolve().parent / 'assets' / 'above_product.json'
    windows = json.loads(asset.read_text())
    expected = {(k, ratio) for k in (2, 3, 4) for ratio in (2, 4, 8)}
    found = set()
    for row in windows:
        moduli = row['moduli']
        product = math.prod(moduli)
        values = row['selected']
        key = (len(moduli), row['high'] // product)
        found.add(key)
        valid = (
            row['low'] == product + 1
            and row['high'] == key[1] * product
            and moduli == [3, 5, 7, 11][: len(moduli)]
            and len(values) == len(set(values))
            and all(
                row['low'] <= n <= row['high']
                and all(n % m in _HALVES[m] for m in moduli)
                for n in values
            )
        )
        checker.check(
            f'above-product window {key}: exact domain and admissibility', valid
        )
        checker.check(
            f'above-product window {key}: direct property P', has_property_p(values)
        )
        checker.check(
            f'above-product window {key}: retained rational mass',
            sum((Fraction(1, n) for n in values), Fraction()) == Fraction(row['mass']),
        )
    checker.check(
        'all nine above-product witness windows are present exactly once',
        found == expected and len(windows) == len(expected),
    )
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
