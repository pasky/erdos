#!/usr/bin/env python3
"""Exact additional log weights from proper prime powers in BFT intervals.

Keep an existing certified theta lower bound, and add this nonnegative sum
for p^k, k>=2. The prime-power carry lemma permits counting each such power
once with weight log(p). We inherit directed fixed-point log weights from
PrimeLogIntervals. No floating-point arithmetic is used in the sums.
"""
from __future__ import annotations

import hashlib
from math import isqrt
import numpy as np

from erdos_699_bft_prime_bootstrap import SCALE


class PrimePowerAddendum:
    """Proper prime powers through power_limit, using known sieve primes.

    When theta.limit>=sqrt(power_limit), every proper prime power in range
    is included. Otherwise the known-prime subset is still a valid lower
    bound. A 10^12 limit requires fewer than 100,000 entries; 10^16 requires
    about 5.8 million entries when the underlying sieve reaches 10^8.
    """
    def __init__(self, theta, power_limit=10**12):
        assert 4 <= power_limit < 2**63
        self.limit = int(power_limit)
        count = int(np.searchsorted(theta.primes, isqrt(self.limit), side='right'))
        bases = theta.primes[:count].copy()
        weights = (theta.prefix_lo[1:count+1]-theta.prefix_lo[:count]).copy()
        values = bases*bases
        chunks, weight_chunks = [], []
        exponent = 2
        exponent_counts = {}
        while len(values):
            assert np.all(values <= self.limit)
            chunks.append(values)
            weight_chunks.append(weights)
            exponent_counts[str(exponent)] = len(values)
            # Check multiplication before performing it, avoiding overflow.
            keep = values <= self.limit//bases
            bases, weights = bases[keep], weights[keep]
            values = values[keep]*bases
            exponent += 1
        if chunks:
            powers = np.concatenate(chunks)
            all_weights = np.concatenate(weight_chunks)
            order = np.argsort(powers)
            powers, all_weights = powers[order], all_weights[order]
            assert np.all(powers[1:] > powers[:-1])
            assert len(powers)*int(all_weights.max()) < 2**64
            prefix = np.r_[np.uint64(0), np.cumsum(all_weights, dtype=np.uint64)]
        else:
            powers = np.array([], dtype=np.int64)
            prefix = np.array([0], dtype=np.uint64)
        self.powers, self.prefix_lo = powers, prefix
        self.metadata = {
            'power_limit': self.limit,
            'base_sieve_limit': theta.limit,
            'proper_prime_power_count': len(powers),
            'counts_by_exponent': exponent_counts,
            'all_proper_prime_powers_in_range': theta.limit >= isqrt(self.limit),
            'fixed_point_scale': SCALE,
            'source_prime_array_sha256': theta.metadata['prime_array_sha256'],
            'source_lower_prefix_sha256': theta.metadata['lower_prefix_sha256'],
            'power_array_sha256': hashlib.sha256(powers.tobytes()).hexdigest(),
            'lower_prefix_sha256': hashlib.sha256(prefix.tobytes()).hexdigest(),
        }

    def interval_sum_lower(self, uppers, lowers):
        """Fixed-point lower sum over disjoint integer-endpoint intervals."""
        uppers, lowers = np.asarray(uppers), np.asarray(lowers)
        assert uppers.shape == lowers.shape
        keep = uppers > lowers
        uppers, lowers = uppers[keep], lowers[keep]
        if len(uppers) == 0:
            return 0
        # The BFT intervals arrive in decreasing order. Disjointness ensures
        # no prime power is counted twice and the sum cannot exceed prefix[-1].
        assert np.all(uppers[1:] <= lowers[:-1])
        iu = np.searchsorted(self.powers, uppers, side='right')
        il = np.searchsorted(self.powers, lowers, side='right')
        return int(np.sum(self.prefix_lo[iu]-self.prefix_lo[il], dtype=np.uint64))


if __name__ == '__main__':
    import argparse
    import json
    from erdos_699_bft_prime_bootstrap import PrimeLogIntervals
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sieve-limit', type=int, default=10**6)
    parser.add_argument('--power-limit', type=int, default=10**12)
    args = parser.parse_args()
    theta = PrimeLogIntervals(args.sieve_limit)
    powers = PrimePowerAddendum(theta, args.power_limit)
    print(json.dumps(powers.metadata, indent=2))
