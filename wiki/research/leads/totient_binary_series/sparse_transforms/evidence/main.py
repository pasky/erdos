"""Check exact integer multipliers and finite prime-sieve denominators.

Default coverage is five retained (N, k) pairs, N <= 900, plus six primorials
Q <= 30030 and five nonprimorial squarefree Q <= 70. The quick mode checks
two pairs and three primorials. Totients,
convolutions, rational tail bounds, and denominator decisions are recomputed
with exact arithmetic. Logarithms describe results only. Witness inputs are
relative to this file, and the program writes no files. Dependencies are the
standard library and the repository tools package; lattice discovery is not
rerun. Every failed obligation exits nonzero, including under python -O.

Run from the repository root:
    nice -n 10 uv run --no-sync python wiki/research/leads/totient_binary_series/sparse_transforms/evidence/main.py

Expected runtime is a few seconds. No finite success proves the growing
family criterion or irrationality of the target.
"""

from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import tools

# retain the finite input domain and denominator observations
_PAIRS = ((100, 20), (160, 28), (300, 28), (300, 32), (900, 32))
_SIEVES = (
    ((2,), 3, 4),
    ((2, 3), 5, 12),
    ((2, 3, 5), 7, 59),
    ((2, 3, 5, 7), 11, 417),
    ((2, 3, 5, 7, 11), 13, 4616),
    ((2, 3, 5, 7, 11, 13), 17, 60051),
    ((5,), 2, 10),
    ((2, 5), 3, 19),
    ((3, 5), 2, 30),
    ((3, 7), 2, 42),
    ((2, 5, 7), 3, 137),
)
_TAIL_TERMS = 400


def totients(limit: int) -> list[int]:
    """Compute phi(0..limit) by an integer sieve."""
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:
            for n in range(p, limit + 1, p):
                phi[n] -= phi[n] // p
    return phi


def check_witness(checker: tools.Checker, record: dict) -> None:
    """Check all gap equations and a full infinite-tail certificate."""
    n, k = record['N'], record['k']
    label = f'N={n},k={k}'
    coefficients = record['coefficients']
    valid = (
        3 <= k <= n <= 900
        and all(
            type(i) is int and type(c) is int and 0 <= i <= n and c != 0
            for i, c in coefficients
        )
        and len({i for i, _ in coefficients}) == len(coefficients)
    )
    checker.check(f'{label}: coefficient domain and uniqueness', valid)
    if not valid:
        return
    polynomial = dict(coefficients)
    checker.check(f'{label}: exact degree and normalization', polynomial.get(n) == 2)
    checker.check(
        f'{label}: preceding polynomial gap',
        all(polynomial.get(i, 0) == 0 for i in range(n - k + 1, n)),
    )

    # independently form every coefficient needed by the finite and tail checks
    cutoff = k + _TAIL_TERMS
    phi = totients(n + cutoff)
    checker.check(
        f'{label}: small totient control',
        phi[1:13] == [1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4],
    )
    product = [0] * (n + cutoff + 1)
    for i, c in coefficients:
        for j in range(1, len(product) - i):
            product[i + j] += c * phi[j]
    checker.check(
        f'{label}: both product gaps',
        all(product[j] == 0 for j in range(n - k + 1, n))
        and all(product[j] == 0 for j in range(n + 1, n + k + 1)),
    )
    height = max(abs(c) for _, c in coefficients)
    central = product[n]
    checker.check(f'{label}: declared height', height == record['height'])
    checker.check(
        f'{label}: declared central coefficient',
        central == record['central_coefficient'],
    )

    # verify the integer specialization and its residues directly
    u = sum(c * (1 << (n - i)) for i, c in coefficients)
    v = sum(product[j] * (1 << (n - j)) for j in range(n + 1))
    checker.check(
        f'{label}: specialization residues',
        u % (1 << k) == 2 and (v - central) % (1 << k) == 0,
    )

    # bound every coefficient beyond cutoff, not just the sampled tail
    prefix_numerator = sum(
        product[n + j] * (1 << (cutoff - j)) for j in range(k + 1, cutoff + 1)
    )
    far_numerator = sum(abs(c) * (n + cutoff + 2 - i) for i, c in coefficients)
    error = Fraction(abs(prefix_numerator) + far_numerator, 1 << cutoff)
    crude = Fraction(sum(abs(c) * (n + k + 2 - i) for i, c in coefficients), 1 << k)
    height_bound = Fraction(height * (n + 1) * (n + k + 2), 1 << k)
    checker.check(
        f'{label}: full remainder bounded below the unit lattice',
        0 < error <= crude <= height_bound < 1,
    )
    if error <= 0:
        return
    max_denominator = min(
        (error.denominator - 1) // error.numerator,
        ((1 << k) - 1) // (abs(central) + 3),
    )
    checker.check(
        f'{label}: strict finite denominator certificate',
        max_denominator >= 1
        and max_denominator * error < 1
        and max_denominator * (abs(central) + 3) < (1 << k),
    )
    bits = math.log2(error.denominator) - math.log2(error.numerator)
    crude_bits = math.log2(height_bound.denominator) - math.log2(height_bound.numerator)
    print(
        f'{label}: H={height}, central={central}, '
        f'crude_bits={crude_bits:.3f}, certified_error_bits={bits:.3f}, '
        f'excluded_denominators=1..{max_denominator}'
    )


def check_sieve(
    checker: tools.Checker,
    primes: tuple[int, ...],
    first_missing_prime: int,
    expected_bits: int,
) -> None:
    """Reduce one sieve sum and check the surviving cyclotomic divisor."""
    q = math.prod(primes)
    divisors = [(1, 1)]
    for p in primes:
        divisors += [(d * p, -mu) for d, mu in divisors]
    main_term = sum(
        (Fraction(mu * (1 << d), ((1 << d) - 1) ** 2) for d, mu in divisors),
        Fraction(),
    )
    denominator = main_term.denominator
    checker.check(
        f'Q={q}: reduced denominator bit length',
        denominator.bit_length() == expected_bits,
    )
    checker.check(
        f'Q={q}: common denominator is divisible by the reduced one',
        ((1 << q) - 1) ** 2 % denominator == 0,
    )
    phi = totients(120)
    checker.check(
        f'Q={q}: sieve coefficient identity through 120',
        all(
            sum(mu * (n // d) for d, mu in divisors if n % d == 0)
            == sum(
                phi[n // r]
                for r in range(1, n + 1)
                if n % r == 0 and math.gcd(r, q) == 1
            )
            for n in range(1, 121)
        ),
    )
    largest = primes[-1]
    if largest >= 5:
        # mu(Q/d) equals mu(Q)*mu(d) for this squarefree Q
        mu_q = (-1) ** len(primes)
        cyclotomic = Fraction(1)
        for d, mu in divisors:
            cyclotomic *= Fraction((1 << d) - 1) ** (mu_q * mu)
        checker.check(f'Q={q}: integral cyclotomic value', cyclotomic.denominator == 1)
        value = cyclotomic.numerator
        primitive_part = value // math.gcd(value, largest)
        phi_q = math.prod(p - 1 for p in primes)
        checker.check(
            f'Q={q}: primitive part square survives reduction',
            denominator % (primitive_part * primitive_part) == 0,
        )
        checker.check(
            f'Q={q}: quantitative denominator lower bounds',
            4 * value > (1 << phi_q)
            and denominator * largest * largest > (1 << (2 * phi_q - 4))
            and denominator > (1 << first_missing_prime)
            and denominator * largest * largest
            > (1 << (2 * largest + first_missing_prime - 9)),
        )
        if q == 21:
            checker.check(
                'Q=21: nonprimitive cyclotomic prime occurs and is removed',
                value == 2359
                and math.gcd(value, largest) == 7
                and primitive_part == 337,
            )
    print(f'Q={q}: reduced_denominator_bits={denominator.bit_length()}')


def main() -> int:
    """Run the full default domain or the explicitly reduced quick domain."""
    args = tools.evidence_parser(__doc__.split('\n', 1)[0]).parse_args()
    checker = tools.Checker()
    source = Path(__file__).resolve().parent / 'assets' / 'witnesses.json'
    try:
        records = json.loads(source.read_text())['witnesses']
        records = sorted(records, key=lambda record: (record['N'], record['k']))
        checker.check(
            'exact retained witness domain',
            tuple((record['N'], record['k']) for record in records) == _PAIRS,
        )
        selected = records[:2] if args.quick else records
        sieves = _SIEVES[:3] if args.quick else _SIEVES
        print(
            f'mode={"quick" if args.quick else "full"}; witnesses={len(selected)}; sieves={len(sieves)}'
        )
        for record in selected:
            check_witness(checker, record)
        for primes, first_missing_prime, expected_bits in sieves:
            check_sieve(checker, primes, first_missing_prime, expected_bits)
    except (OSError, ValueError, KeyError, TypeError) as error:
        checker.check('readable, well-formed evidence input', False, str(error))
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
