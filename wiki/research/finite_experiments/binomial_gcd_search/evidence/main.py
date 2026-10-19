"""Check the finite binomial-GCD thresholds described by the owning page.

The full domain is 4 <= n <= 30 and 1 <= i < j <= n // 2. Check the
non-strict prime threshold throughout that domain, the exact strict exception
set, and the exposed integer witnesses. Arithmetic uses Python integers,
``math.comb``, ``math.gcd`` and elementary trial division.

Run from the repository root:
    uv run --no-sync python wiki/research/finite_experiments/binomial_gcd_search/evidence/main.py

Dependencies are the standard library and the installed root ``tools`` package.
There are no file inputs, output files, random choices or reduced modes.
Expected runtime is a few seconds or less. Failed obligations exit nonzero,
including under ``python -O``. This finite check proves no all-order result.
"""

from __future__ import annotations

import math
import sys

import tools

__all__ = [
    'is_prime',
    'classify',
    'main',
]

# bound the complete finite domain stated on the owning page
_MIN_N = 4
_MAX_N = 30

# count pairs at each half-order: 2 * binom(15, 3) + binom(15, 2)
_TRIPLE_COUNT = 1_015

# fix the expected strict failures before the enumeration runs
_STRICT_FAILURES = [(10, 3, 5), (16, 2, 6), (28, 3, 14), (28, 5, 14)]

# retain the owning page's binomial values, gcds and complete prime-divisor sets
_WITNESSES = {
    (4, 1, 2): (4, 6, 2, (2,)),
    (10, 3, 5): (120, 252, 12, (2, 3)),
    (16, 2, 6): (120, 8_008, 8, (2,)),
    (28, 3, 14): (3_276, 40_116_600, 36, (2, 3)),
    (28, 5, 14): (98_280, 40_116_600, 1_080, (2, 3, 5)),
}


def is_prime(value: int) -> bool:
    """Determine primality by trial division through the integer square root."""
    if value < 2:
        return False
    for divisor in range(2, math.isqrt(value) + 1):
        if value % divisor == 0:
            return False
    return True


def classify(common: int, index: int, primes: tuple[int, ...]) -> tuple[bool, bool]:
    """Classify a positive gcd using its complete candidate prime list.

    ``primes`` contains every possible prime divisor of ``common``. Return
    whether a divisor is at least ``index``, then whether one is greater.
    """
    divisors = tuple(prime for prime in primes if common % prime == 0)
    non_strict = any(prime >= index for prime in divisors)
    strict = any(prime > index for prime in divisors)
    return non_strict, strict


def main() -> int:
    """Run every finite obligation and return the shared checker's exit code."""
    # parse the fixed-domain interface and construct all candidate primes
    parser = tools.evidence_parser(
        'Check the full finite binomial-GCD domain.', quick=False
    )
    parser.parse_args()
    checker = tools.Checker()
    primes = tuple(value for value in range(2, _MAX_N + 1) if is_prime(value))
    checker.check(
        'complete prime list through the upper bound',
        primes == (2, 3, 5, 7, 11, 13, 17, 19, 23, 29),
        f'observed {primes}',
    )
    checker.check(
        'reject nonprime witnesses 1 and 6', not is_prime(1) and not is_prime(6)
    )

    # enumerate every admissible pair in every binomial row
    count = 0
    non_strict_failures: list[tuple[int, int, int]] = []
    strict_failures: list[tuple[int, int, int]] = []
    for n in range(_MIN_N, _MAX_N + 1):
        half = n // 2
        row = [math.comb(n, index) for index in range(half + 1)]
        for i in range(1, half):
            for j in range(i + 1, half + 1):
                count += 1
                common = math.gcd(row[i], row[j])
                non_strict, strict = classify(common, i, primes)
                if not non_strict:
                    non_strict_failures.append((n, i, j))
                    print(f'non-strict failure {(n, i, j)}: gcd={common}')
                if not strict:
                    strict_failures.append((n, i, j))
                    print(f'strict failure {(n, i, j)}: gcd={common}')

    # compare fresh coverage and failure sets with the stated finite result
    print(f'checked domain: {_MIN_N} <= n <= {_MAX_N}; triples={count}')
    print(f'non-strict failures: {non_strict_failures}')
    print(f'strict failures: {strict_failures}')
    checker.check('complete triple count', count == _TRIPLE_COUNT, f'observed {count}')
    checker.check('non-strict threshold on every triple', not non_strict_failures)
    checker.check('exact strict exception set', strict_failures == _STRICT_FAILURES)

    # check the exposed arithmetic and both threshold outcomes for each witness
    for triple, expected in _WITNESSES.items():
        n, i, j = triple
        left = math.comb(n, i)
        right = math.comb(n, j)
        common = math.gcd(left, right)
        divisors = tuple(prime for prime in primes if common % prime == 0)
        actual = left, right, common, divisors
        thresholds = classify(common, i, primes)
        expected_thresholds = True, triple not in _STRICT_FAILURES
        checker.check(
            f'exact witness {triple}',
            actual == expected and thresholds == expected_thresholds,
            f'observed {actual}, thresholds={thresholds}',
        )
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
