#!/usr/bin/env python3
"""Pointwise gcd evaluator using the checked compact prime prefix.

Intervals inside the compact sieve use its directed weighted sums. Entire
intervals above it use the retained BFT/Broadbent bounds. At most one
interval crosses the sieve cutoff; its lower theta endpoint uses the exact
compact upper estimate. Proper prime powers are added independently.
"""

from functools import lru_cache
from math import isqrt

import numpy as np
from erdos_699_bft_prime_bootstrap import SCALE
from erdos_699_index_7_gcd_pointwise import PointwiseGcdLower, sharp_prime_sum_lower
from erdos_699_off_diagonal_gcd_sharp import TABLE
from erdos_699_prime_power_addendum import PrimePowerAddendum


def theta_lower_scaled(x):
    """Directed lower theta(x), in SCALE units, for x<=10^19."""
    assert 1 <= x <= 10**19
    root_scale = 64
    root = isqrt(x * root_scale * root_scale)
    if root * root < x * root_scale * root_scale:
        root += 1
    numerator, denominator = (259, 125) if x < 10**11 else (49, 25)
    error = (numerator * root + denominator - 1) // denominator
    for threshold, _up, lo in TABLE:
        if threshold > x:
            break
        error = min(
            error,
            (lo.numerator * x * root_scale + lo.denominator - 1) // lo.denominator,
        )
    return max(0, x * root_scale - error) * (SCALE // root_scale)


def compact_prime_sum_lower(compact, uppers, lowers):
    keep = uppers > lowers
    uppers, lowers = uppers[keep], lowers[keep]
    if not len(uppers):
        return 0
    assert np.all(uppers[1:] <= lowers[:-1])
    inside = uppers <= compact.limit
    total = compact.interval_sum_lower(uppers[inside], lowers[inside])
    above = lowers > compact.limit
    if np.any(above):
        total += sharp_prime_sum_lower(compact.base, uppers[above], lowers[above])
    cross = (uppers > compact.limit) & (lowers <= compact.limit)
    assert np.count_nonzero(cross) <= 1
    for upper, lower in zip(uppers[cross], lowers[cross], strict=False):
        lo = theta_lower_scaled(int(upper))
        hi = compact.theta_upper_integer(int(lower)) * SCALE
        total += max(0, lo - hi)
    return total


class CompactPointwiseGcdLower(PointwiseGcdLower):
    def __init__(self, compact, directions, *, terms=4000, powers=None):
        self.compact = compact
        if powers is None:
            powers = PrimePowerAddendum(compact.base, power_limit=10**14)
        super().__init__(compact, directions, terms=terms, powers=powers)

    @lru_cache(maxsize=512)  # noqa: B019 - evaluator lifetime owns the cache.
    def log_lower(self, m):
        A, B, C = self.directions
        H = A + B + C
        assert isinstance(m, int) and m >= 1 and B * m >= 2 and H * m < 2**62
        uppers = (H * m - 1) // self.ts
        lowers = np.maximum.reduce(
            (
                (A * m + 1) // self.den[:, 0],
                B * m // self.den[:, 1],
                (C * m + 1) // self.den[:, 2],
            )
        )
        return compact_prime_sum_lower(
            self.compact, uppers, lowers
        ) + self.powers.interval_sum_lower(uppers, lowers)
