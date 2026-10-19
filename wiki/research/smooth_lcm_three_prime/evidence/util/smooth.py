"""Exact integer helpers for running-lcm series over a finite prime set.

Every floor of a logarithm is decided by comparing integer prime powers, so no
floating-point value enters a decision. The running lcm at a smooth cutoff
``m`` is ``D(m) = prod_u u**floor(log_u m)``, which the research page proves and
``main.py`` compares with a brute-force cumulative lcm.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd

__all__ = [
    'flog',
    'running_lcm',
    'smooth_upto',
    'brute_force_mismatches',
    'events_upto',
    'carry',
    'exact_sum_below',
]


def flog(u: int, n: int) -> int:
    """Return the largest k >= 0 with u**k <= n, for integers u >= 2, n >= 1."""
    k, t = 0, u
    while t <= n:
        k += 1
        t *= u
    return k


def running_lcm(primes: tuple[int, ...], m: int) -> int:
    """Return prod_u u**floor(log_u m), the formula for the running lcm at m."""
    d = 1
    for u in primes:
        d *= u ** flog(u, m)
    return d


def smooth_upto(primes: tuple[int, ...], x: int) -> list[int]:
    """Return the sorted smooth integers 1 <= m <= x over the given primes."""
    out = [1]
    for u in primes:
        grown = []
        for m in out:
            t = m
            while t <= x:
                grown.append(t)
                t *= u
        out = grown
    return sorted(out)


def brute_force_mismatches(primes: tuple[int, ...], x: int) -> tuple[int, int]:
    """Compare the cumulative lcm with the formula at every smooth m <= x.

    Returns the number of smooth integers examined and the number of cutoffs
    at which the brute-force lcm of all earlier smooth integers differs from
    ``running_lcm``.
    """
    count, bad, lcm = 0, 0, 1
    for m in smooth_upto(primes, x):
        lcm = lcm * m // gcd(lcm, m)
        count += 1
        if lcm != running_lcm(primes, m):
            bad += 1
    return count, bad


def events_upto(primes: tuple[int, ...], x: int) -> list[tuple[int, int]]:
    """Return the prime powers u**j <= x with j >= 1, increasing, as (value, u)."""
    out = []
    for u in primes:
        t = u
        while t <= x:
            out.append((t, u))
            t *= u
    return sorted(out)


def carry(z: int, n1: int, n2: int) -> int:
    """Return floor(log_z(n1 n2)) - floor(log_z n1) - floor(log_z n2), 0 or 1."""
    return flog(z, n1 * n2) - flog(z, n1) - flog(z, n2)


def exact_sum_below(primes: tuple[int, ...], x: int) -> Fraction:
    """Return the exact sum of 1/D(m) over smooth integers m < x."""
    return sum(
        (Fraction(1, running_lcm(primes, m)) for m in smooth_upto(primes, x - 1)),
        Fraction(0),
    )
