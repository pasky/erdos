"""Check the displayed flat multiples of odd squarefree cyclotomic polynomials.

The checks are exact integer polynomial arithmetic on the objects displayed on
the angular-coloring research page: the cyclotomic polynomials of 15, 105 and
1155 are built from the Moebius product of the binomials x^d - 1 and checked
against their degree phi(N) and the minimal-polynomial property at the
divisors; Phi_15 and (1 - x) Phi_105 are flat, Phi_105 and Phi_1155 are not;
the displayed multiplier Q = (1 - x^6) S makes Phi_1155 Q flat of degree 502
with 128 nonzero coefficients and constant term one, and S has no cyclotomic
factor; substituting x^11 in (1 - x) Phi_105 gives a flat multiple of
Phi_1155 of degree 539; the totient-ratio thresholds and the prime sum quoted
on the page hold in exact rational arithmetic; and the Gram determinant of
Phi_1155, x Phi_1155, ..., x^22 Phi_1155 has the quoted logarithm. No search
runs: the least degree D(1155) = 502 is a solver observation that this
checker does not reproduce, and nothing here bounds D(N) for larger N.

Run from the repository root:
    uv run --no-sync python wiki/research/erdos_774/evidence/angular_flat_multiples/main.py

Dependencies are the standard library and the installed root ``tools``
package. There are no file inputs, output files, random choices or reduced
modes. Expected runtime is a few seconds. Failed obligations exit nonzero,
including under ``python -O``. These finite checks prove no coloring theorem.
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction

import tools

__all__ = [
    'main',
]

# fix the displayed second factor of the 1155 multiplier, low degree first
_S_1155 = [1, 1, 1, 0, -1, -2, -1, 0, 1, 0, -1, -2, -1, 0, 1, 1, 1]


def _mul(a: list[int], b: list[int]) -> list[int]:
    """Return the product of two coefficient lists, low degree first."""
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return out


def _divmod(a: list[int], b: list[int]) -> tuple[list[int], list[int]]:
    """Return quotient and remainder of a by a monic or unit-leading b over the integers."""
    a = a[:]
    lead = b[-1]
    if lead not in (1, -1):
        raise ValueError('divisor must have unit leading coefficient')
    q = [0] * max(len(a) - len(b) + 1, 1)
    for k in range(len(a) - len(b), -1, -1):
        c = a[k + len(b) - 1] * lead
        q[k] = c
        if c:
            for j, y in enumerate(b):
                a[k + j] -= c * y
    r = a[: len(b) - 1]
    return q, r


def _trim(a: list[int]) -> list[int]:
    """Return the coefficient list without trailing zeros."""
    a = a[:]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def _primes(n: int) -> list[int]:
    """Return the primes dividing n."""
    out, m, p = [], n, 2
    while p * p <= m:
        if m % p == 0:
            out.append(p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        out.append(m)
    return out


def _mobius(n: int) -> int:
    """Return the Moebius function of n."""
    ps, m = _primes(n), n
    for p in ps:
        m //= p
        if m % p == 0:
            return 0
    return (-1) ** len(ps)


def _cyclotomic(n: int) -> list[int]:
    """Return Phi_n from the Moebius product of the binomials x^d - 1."""
    numerator, denominator = [1], [1]
    for d in range(1, n + 1):
        if n % d:
            continue
        binomial = [-1] + [0] * (d - 1) + [1]
        if _mobius(n // d) == 1:
            numerator = _mul(numerator, binomial)
        elif _mobius(n // d) == -1:
            denominator = _mul(denominator, binomial)
    q, r = _divmod(numerator, denominator)
    if any(r):
        raise ValueError('Moebius quotient is not a polynomial')
    return _trim(q)


def _phi(n: int) -> int:
    """Return Euler's totient of n."""
    out = n
    for p in _primes(n):
        out = out // p * (p - 1)
    return out


def _divides(b: list[int], a: list[int]) -> bool:
    """Decide whether the unit-leading polynomial b divides a."""
    _, r = _divmod(a, b)
    return not any(r)


def _flat(a: list[int]) -> bool:
    """Decide whether every coefficient lies in {-1, 0, 1}."""
    return all(c in (-1, 0, 1) for c in a)


def _bareiss(matrix: list[list[int]]) -> int:
    """Return the determinant of an integer matrix by Bareiss elimination."""
    a = [row[:] for row in matrix]
    n, previous, sign = len(a), 1, 1
    for k in range(n - 1):
        pivot_row = next((r for r in range(k, n) if a[r][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                value = a[i][j] * a[k][k] - a[i][k] * a[k][j]
                if value % previous:
                    raise ValueError('Bareiss exact division failed')
                a[i][j] = value // previous
            a[i][k] = 0
        previous = a[k][k]
    return sign * a[-1][-1]


def main() -> int:
    """Run every finite obligation and return the shared checker's exit code."""
    # parse the fixed-domain interface and build the three cyclotomic polynomials
    parser = tools.evidence_parser('Check the displayed flat cyclotomic multiples.', quick=False)
    parser.parse_args()
    checker = tools.Checker()
    phi15, phi105, phi1155 = _cyclotomic(15), _cyclotomic(105), _cyclotomic(1155)
    for n, poly in ((15, phi15), (105, phi105), (1155, phi1155)):
        checker.check(f'Phi_{n} has degree phi({n}) and constant term one', len(poly) - 1 == _phi(n) and poly[0] == 1)
        xn = [-1] + [0] * (n - 1) + [1]
        proper = all(not _divides(poly, [-1] + [0] * (d - 1) + [1]) for d in range(1, n) if n % d == 0)
        checker.check(f'Phi_{n} divides x^{n} - 1 and no x^d - 1 for proper divisors d', _divides(poly, xn) and proper)

    # check the exact values D(15) = 8 and D(105) = 49 from flatness and heights
    checker.check('Phi_15 is flat, so D(15) = phi(15) = 8', _flat(phi15) and len(phi15) - 1 == 8)
    one_minus_x_105 = _trim(_mul([1, -1], phi105))
    checker.check('(1 - x) Phi_105 is flat of degree 49', _flat(one_minus_x_105) and len(one_minus_x_105) - 1 == 49)
    checker.check('(1 - x) Phi_105 has 26 nonzero coefficients', sum(1 for c in one_minus_x_105 if c) == 26)
    checker.check('Phi_105 has height two at x^7 and x^41', max(abs(c) for c in phi105) == 2 and [i for i, c in enumerate(phi105) if abs(c) == 2] == [7, 41])

    # check the displayed 1155 multiplier and its product
    multiplier = _mul([1, 0, 0, 0, 0, 0, -1], _S_1155)
    product = _trim(_mul(phi1155, multiplier))
    checker.check('the 1155 multiplier has degree 22 and constant term one', len(multiplier) - 1 == 22 and multiplier[0] == 1)
    checker.check('Phi_1155 times the multiplier is flat', _flat(product))
    checker.check('the flat 1155 multiple has degree 502', len(product) - 1 == 502)
    checker.check('the flat 1155 multiple has 128 nonzero coefficients', sum(1 for c in product if c) == 128)
    checker.check('Phi_1155 has height three and is not flat', max(abs(c) for c in phi1155) == 3)
    no_cyclotomic = all(not _divides(_cyclotomic(d), _S_1155) for d in range(1, 61) if _phi(d) <= 16)
    checker.check('the degree-16 factor has no cyclotomic factor', no_cyclotomic)

    # check the inflation bound D(1155) <= 11 D(105) through x -> x^11
    inflated = [0] * (11 * 49 + 1)
    for i, c in enumerate(one_minus_x_105):
        inflated[11 * i] = c
    checker.check('(1 - x^11) Phi_105(x^11) is a flat multiple of Phi_1155 of degree 539', _flat(inflated) and _divides(phi1155, inflated))

    # check the totient-ratio thresholds and the prime sum quoted on the page
    odd_primes = [p for p in range(3, 100) if _primes(p) == [p]]
    ratio = {}
    running = Fraction(1)
    for p in odd_primes:
        running *= Fraction(p - 1, p)
        ratio[p] = running
    checker.check('three arcs: prime 19 ratio above 1/3, prime 23 ratio below', ratio[19] > Fraction(1, 3) > ratio[23])
    checker.check('four arcs: prime 73 ratio above 1/4, prime 79 ratio below', ratio[73] > Fraction(1, 4) > ratio[79])
    checker.check('the odd primes up to 23 have sum of (p - 2) equal to 82', sum(p - 2 for p in odd_primes if p <= 23) == 82)
    checker.check('the totient ratio of 1155 is 480/1155', Fraction(_phi(1155), 1155) == ratio[11])

    # check the Gram determinant of the rank-23 lattice of degree-502 multiples
    auto = [sum(phi1155[i] * phi1155[i + t] for i in range(len(phi1155) - t)) for t in range(23)]
    gram = [[auto[abs(i - j)] for j in range(23)] for i in range(23)]
    det = _bareiss(gram)
    log_covolume = 0.5 * math.log(det) if det > 0 else float('nan')
    checker.check('the Gram determinant is positive with half-logarithm 51.39', det > 0 and abs(log_covolume - 51.39) < 0.01, f'observed {log_covolume}')
    ball = 23 * math.log(2) + 11.5 * math.log(503 / 23)
    checker.check('the section bound 2^23 (503/23)^(23/2) has logarithm 51.42', abs(ball - 51.42) < 0.01, f'observed {ball}')
    print(f'D(15) = 8, D(105) = 49, D(1155) <= 502; log covolume {log_covolume:.2f}, section bound {ball:.2f}')
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
