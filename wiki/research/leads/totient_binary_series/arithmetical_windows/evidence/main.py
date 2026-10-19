"""Check fixed finite witnesses for totient-term isolation and its CRT data.

Run from the repository root:
    nice -n 10 uv run --no-sync python wiki/research/leads/totient_binary_series/arithmetical_windows/evidence/main.py

The full check uses exact integers, trial division through the selected
arguments 418608, 418609, 418610, a totient sieve to 89013, and Phi_N modulo
2048. It checks only the fixed witnesses named below, not
all indices in that sieve domain. It takes under a second, reads and writes
no files, and has no random choices or reduced mode. Dependencies are the
standard library and the installed root tools package. Failed obligations
exit nonzero even under python -O. Infinite statements require the owning
page's proof and Dirichlet's theorem; these checks confer no proof tier.
"""

from __future__ import annotations

import math
import sys

import tools

__all__ = ['main']

# fix both cases of the prime-cofactor construction and their exact totients
_WITNESSES = (
    (15_131, 5, 1, (15_131,), (15_130, 5_632, 9_840), 1),
    (89_013, 8, 5, (3, 29_671), (59_340, 32_640, 79_680), 2),
)

# fix the nine auxiliary primes in the infinite 64p counterfamily
_FRESH_PRIMES = (257, 641, 769, 1_153, 1_409, 2_689, 3_329, 3_457, 4_481)

# retain the CRT residue as data, with no assertion that it is prime
_RESIDUE = 10_902_871_344_717_736_470_074_227_285_488_089_485_531
_MODULUS = 24_316_165_102_496_165_371_645_476_418_278_117_995_580


def _prime(n: int) -> bool:
    """Certify primality by trial division for the fixed small inputs."""
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


def _phi(n: int) -> int:
    """Compute one totient by trial factorization."""
    value = n
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            value -= value // divisor
            while n % divisor == 0:
                n //= divisor
        divisor += 1
    if n > 1:
        value -= value // n
    return value


def main() -> int:
    """Check every declared finite obligation and return a failing exit code."""
    tools.evidence_parser(
        'Check fixed totient isolation witnesses.', quick=False
    ).parse_args()
    checker = tools.Checker()

    # sieve independently of trial factorization and retain selected residues
    limit = 89_013
    phi = list(range(limit + 1))
    for prime in range(2, limit + 1):
        if phi[prime] == prime:
            for multiple in range(prime, limit + 1, prime):
                phi[multiple] -= phi[multiple] // prime
    selected = {64, 125, 3_125, 78_125, 15_131, 89_013}
    residues = {}
    acc = 0
    for n in range(1, limit + 1):
        acc = (2 * acc + phi[n]) % 2_048
        if n in selected:
            residues[n] = acc
    checker.check('seed Phi_64 has exact valuation ten', residues[64] == 1_024)
    checker.check(
        'powers-of-five witnesses have exact valuation two',
        all(residues[n] % 8 == 4 for n in (125, 3_125, 78_125)),
    )
    checker.check(
        'small suppression factors are primes in 1 mod 8',
        all(_prime(q) and q % 8 == 1 for q in (17, 41)),
    )

    # verify actual factors, unwanted-term suppression, and full-prefix residues
    for n, modulus, residue, factors, expected, valuation in _WITNESSES:
        checker.check(
            f'N={n}: reduced prime or semiprime cofactor',
            n % modulus == residue
            and math.prod(factors) == n
            and len(set(factors)) == len(factors)
            and all(_prime(p) and p % 4 == 3 for p in factors),
        )
        observed = tuple(_phi(n - i) for i in range(3))
        checker.check(
            f'N={n}: exact totients agree with independent sieve',
            observed == expected == tuple(phi[n - i] for i in range(3)),
        )
        checker.check(
            f'N={n}: fresh primes suppress the unwanted terms',
            (n - 1) % 17 == 0
            and (n - 2) % 41 == 0
            and observed[1] % 8 == observed[2] % 8 == 0
            and math.gcd(n, modulus * 17 * 41) == 1,
        )
        window = sum((1 << i) * observed[i] for i in range(3))
        checker.check(
            f'N={n}: the full numerator has valuation {valuation}',
            residues[n] % 8 == window % 8
            and residues[n] % (1 << (valuation + 1)) == 1 << valuation,
        )

    # check a prime square with shifts on both sides and a signed coefficient
    square_prime = 647
    square_n = square_prime**2
    square_arguments = (square_n, square_n - 1, square_n + 1)
    square_factors = (
        ((647, 2),),
        ((2, 4), (3, 4), (17, 1), (19, 1)),
        ((2, 1), (5, 1), (41, 1), (1_021, 1)),
    )
    checker.check(
        'prime-square parameter preserves the base class',
        _prime(square_prime) and square_prime % 36 == 35 and square_n % 9 == 1,
    )
    checker.check(
        'prime-square roots suppress both opposite shifts',
        square_prime % 17 == 1
        and square_prime % 41 == 32
        and square_n % 17 == 1
        and square_n % 41 == 40,
    )
    square_totients = tuple(_phi(n) for n in square_arguments)
    checker.check(
        'prime-square totients agree with certified factorizations',
        all(
            math.prod(q**a for q, a in factors) == n
            and all(_prime(q) for q, _ in factors)
            and math.prod((q - 1) * q ** (a - 1) for q, a in factors) == totient
            for n, factors, totient in zip(
                square_arguments, square_factors, square_totients, strict=True
            )
        )
        and square_totients == (417_962, 124_416, 163_200),
    )
    signed_sum = -square_totients[0] + square_totients[1] + square_totients[2]
    checker.check(
        'prime-square signed sum has exact valuation one',
        signed_sum == -130_346
        and signed_sum % 4 == 2
        and all(value % 4 == 0 for value in square_totients[1:]),
    )

    # check the prime progression defining the symbolic infinite counterfamily
    seed_modulus = math.lcm(*range(55, 65))
    checker.check(
        'seed window modulus and its exact power of two',
        seed_modulus == 13_632_589_333_440
        and seed_modulus // 64 == 213_009_208_335
        and seed_modulus % 128 == 64,
    )
    checker.check(
        'the nine fresh factors are distinct primes in 1 mod 128',
        len(set(_FRESH_PRIMES)) == 9
        and all(_prime(q) and q > 64 and q % 128 == 1 for q in _FRESH_PRIMES),
    )
    checker.check(
        'the retained CRT class has the correct modulus and is reduced',
        4 * (seed_modulus // 64) * math.prod(_FRESH_PRIMES) == _MODULUS
        and 0 <= _RESIDUE < _MODULUS
        and math.gcd(_RESIDUE, _MODULUS) == 1,
    )
    checker.check(
        'the CRT class preserves the seed divisors and gives p in 3 mod 4',
        _RESIDUE % (seed_modulus // 64) == 1
        and _RESIDUE % 4 == 3
        and (64 * _RESIDUE - 64) % seed_modulus == 0,
    )
    checker.check(
        'the CRT class puts a fresh prime at each unwanted position',
        all((64 * _RESIDUE - i) % q == 0 for i, q in enumerate(_FRESH_PRIMES, 1)),
    )
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
