"""Observe the parity-prediction rule on the primes below 2 * 10^7.

For the parity-prediction sketch of Problem 251 in the parent folder. With
h_n = (p_{n+1} - p_n)/2, an odd d, and K = ceil(log2(d log X)) + C, a start
n with X < p_n <= 2X is *mispredicted* when the phase
frac(d * sum_{j<K} h_{n+j} 2^{-j-1}) is below 1/2. The program computes,
for X in {10^6, 10^7}, d in {1, 3, 5, 7, 9, 11, 15} and C in {0, ..., 6},
the exact number of mispredicted starts, and checks three things.

1. Rule (P) of the sketch on every start: the phase test agrees with the
   parity form "h_n is not congruent to beta_{n,K} mod 2", where beta is
   computed separately from the residues of h_{n+1}, ..., h_{n+K-1}.
2. In every cell the mispredicted fraction lies in [0.49, 0.51].
3. The best prediction of the parity of h_n from the residues
   h_{n+j} mod 2^{j+1}, 1 <= j < K, gains less than 0.01 over the
   prediction from no residues at all, for K = 2, 3, 4 at X = 10^7 (the
   total variation delta_0 of the sketch's Theorem F); the K = 1 value, the
   bias |Pr(h_n odd) - Pr(h_n even)|, is reported.

All phases are exact: with M = sum_{j<K} h_{n+j} 2^{K-1-j}, a start is
mispredicted exactly when (d * M) mod 2^K < 2^{K-1}. The primes come from
a sieve of Eratosthenes up to 2 * 10^7 + 10^5. These are finite
observations. They exclude no denominator: this check supplies neither an
explicit threshold X_0 for Theorem C nor a bound on the preperiod of a
hypothetical rational value. Other finite tail-certificate methods are separate.
They show how far the computed range is from the concentration that a
rational sum would force asymptotically (fewer than 2dX/2^K mispredicted
starts).

Run from the repository root:
    uv run --no-sync python wiki/research/prime_binary_new_attack/evidence/main.py

Dependencies: numpy and the root ``tools`` package. The full run takes a
few seconds and well under 1 GiB of memory; ``--quick`` uses X = 10^6
only and skips check 3. There are no input files and no outputs. Every
check goes through the shared ``Checker``, so failures exit nonzero under
``python -O`` as well.
"""

from __future__ import annotations

import math
import sys

import numpy as np

import tools

__all__ = [
    'DENOMINATORS',
    'OFFSETS',
    'check_prediction_gain',
    'check_rule',
    'main',
    'primes_up_to',
]

DENOMINATORS = (1, 3, 5, 7, 9, 11, 15)
OFFSETS = tuple(range(7))
SCALES_FULL = (10**6, 10**7)
SCALES_QUICK = (10**6,)


def primes_up_to(limit: int) -> np.ndarray:
    """Return the primes up to ``limit`` by the sieve of Eratosthenes."""
    # mark composites with a boolean sieve over the odd and even numbers
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    sieve[4::2] = False
    for p in range(3, math.isqrt(limit) + 1, 2):
        if sieve[p]:
            sieve[p * p :: 2 * p] = False
    return np.flatnonzero(sieve)


def _range(primes: np.ndarray, x: int) -> tuple[int, int]:
    """Return the index range of the primes p with x < p <= 2x."""
    # locate the first prime above x and the last prime at most 2x
    low = int(np.searchsorted(primes, x, side='right'))
    high = int(np.searchsorted(primes, 2 * x, side='right'))
    return low, high


def check_rule(
    checker: tools.Checker, primes: np.ndarray, scales: tuple[int, ...]
) -> None:
    """Check rule (P) and the mispredicted fractions in every cell."""
    # halved gaps, indexed like the primes; the first entry is unused
    halved = np.diff(primes) // 2
    for x in scales:
        low, high = _range(primes, x)
        count = high - low
        rule_ok = True
        fractions = []
        for d in DENOMINATORS:
            for c in OFFSETS:
                k = math.ceil(math.log2(d * math.log(x))) + c
                modulus = 1 << k
                # M = sum_{j<K} h_{n+j} 2^{K-1-j} and its part without h_n
                tail = np.zeros(count, dtype=np.int64)
                for j in range(1, k):
                    tail += halved[low + j : high + j] * (1 << (k - 1 - j))
                first = halved[low:high]
                total = tail + first * (1 << (k - 1))
                # the phase test and the parity form of rule (P)
                by_phase = (d * total) % modulus < modulus // 2
                beta = ((d * tail) % modulus < modulus // 2).astype(np.int64)
                by_parity = (first % 2) != beta
                rule_ok = rule_ok and bool(np.array_equal(by_phase, by_parity))
                fractions.append((d, c, k, int(by_phase.sum()) / count))
        lowest = min(f for _, _, _, f in fractions)
        highest = max(f for _, _, _, f in fractions)
        # report the observed range and the asymptotic bound at C = 6
        bounds = [
            2 * d * x / 2**k / count for d, c, k, _ in fractions if c == OFFSETS[-1]
        ]
        print(
            f'  X = {x}: {count} starts; mispredicted fractions {lowest:.4f} to '
            f'{highest:.4f}; the bound 2dX/(2^K N) at C = {OFFSETS[-1]} ranges '
            f'{min(bounds):.4f} to {max(bounds):.4f}'
        )
        checker.check(
            f'X = {x}: rule (P) agrees with the phase test on every start and cell',
            rule_ok,
        )
        checker.check(
            f'X = {x}: every mispredicted fraction lies in [0.49, 0.51]',
            lowest >= 0.49 and highest <= 0.51,
            f'{count} starts, fractions {lowest:.4f} to {highest:.4f}',
        )


def _delta0(halved: np.ndarray, low: int, high: int, k: int) -> float:
    """Return delta_0 of the residue law of K consecutive halved gaps."""
    # encode the residues of h_{n+1}, ..., h_{n+K-1} as one key per start
    count = high - low
    key = np.zeros(count, dtype=np.int64)
    shift = 0
    for j in range(1, k):
        key += (halved[low + j : high + j] % (1 << (j + 1))) << shift
        shift += j + 1
    parity = halved[low:high] % 2
    size = 1 << shift
    even = np.bincount(key[parity == 0], minlength=size)
    odd = np.bincount(key[parity == 1], minlength=size)
    return float(np.abs(even - odd).sum()) / count


def check_prediction_gain(checker: tools.Checker, primes: np.ndarray) -> None:
    """Check that later residues add little to the parity prediction."""
    # compare delta_0 at K = 2, 3, 4 with the marginal bias at K = 1
    halved = np.diff(primes) // 2
    low, high = _range(primes, 10**7)
    base = _delta0(halved, low, high, 1)
    gains = [_delta0(halved, low, high, k) - base for k in (2, 3, 4)]
    # report delta_0 for K = 1, ..., 4
    values = ', '.join(f'{base + g:.4f}' for g in [0.0, *gains])
    print(f'  X = 10^7: delta_0 for K = 1, 2, 3, 4 is {values}')
    checker.check(
        'X = 10^7: delta_0 gains less than 0.01 over K = 1 for K = 2, 3, 4',
        all(g < 0.01 for g in gains),
        f'bias at K = 1 is {base:.4f}; gains ' + ', '.join(f'{g:.4f}' for g in gains),
    )


def main() -> int:
    """Run every check and return the exit code."""
    # parse the interface, sieve once, then run the checks
    parser = tools.evidence_parser(
        'Observe the parity-prediction rule on the primes below 2 * 10^7.',
    )
    args = parser.parse_args()
    scales = SCALES_QUICK if args.quick else SCALES_FULL
    primes = primes_up_to(2 * max(scales) + 10**5)
    checker = tools.Checker()
    check_rule(checker, primes, scales)
    if not args.quick:
        check_prediction_gain(checker, primes)
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
