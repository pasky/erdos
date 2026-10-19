"""Probe the 2-adic tail valuations and a certified continued fraction of S.

Here S = sum_{n>=1} phi(n) / 2^n and Phi_N = sum_{n<=N} phi(n) 2^(N-n). The
owning page proves that a rational S = a/b forces v_2(Phi_N) <= log2(b(N+2))
for every N >= 4, and 2^v_2(Phi_N) <= N + 2 for all large N when b is a power
of two. This probe recomputes v_2(Phi_N) for 1 <= N <= X, records where
v_2(Phi_N) - log2 N is large, checks that every record after N = 16 arises
through a carry tie, counts the excess-positive indices 16 <= N <= X, those
with 2^v_2(Phi_N) > N + 2, and lists the excess-positive indices with
2^(v_2(phi(N)) + 2) > N + 2, the necessary condition for delivery by a
whole-progression certificate. It counts the one-large-prime windows: indices
N <= X such that every one of N + 1, ..., N + J with J = ceil(log2(N + 2)) has
exactly one distinct prime factor above J. Finally it certifies a prefix of
the regular continued fraction of S from the two-sided bounds
Phi_M / 2^M <= S <= (Phi_M + M + 2) / 2^M. The common prefix bounds the
denominator of any rational value of S.

Run from the repository root:
    uv run --no-sync python wiki/research/leads/totient_binary_series/evidence/main.py

The default is the full declared domain, X = 10_000_000 and M = 40_000, which
takes about ten seconds on the development machine. ``--quick`` uses
X = 1_000_000 and M = 4_000 with its own reduced expectations. Arithmetic
uses Python integers;
Phi_N is tracked modulo 2^64, so a valuation is exact whenever it is below 64,
and the run checks that the largest observed valuation stays below that cap.
Dependencies are the standard library and the installed root ``tools``
package. There are no file inputs, output files or random choices. Failed
obligations exit nonzero, including under ``python -O``. The finite domain
proves nothing about all N and confers no standing on the target.
"""

from __future__ import annotations

import math
import sys
from array import array
from fractions import Fraction

import tools

__all__ = [
    'totients',
    'tail_valuations',
    'large_prime_factors',
    'one_large_prime_windows',
    'continued_fraction',
    'main',
]

# fix the valuation cap of the 64-bit accumulator
_CAP = 64

# fix the first index at which log2 N is compared with the valuation
_FIRST = 16

# fix the excess thresholds whose hit counts are recorded
_THRESHOLDS = (0, 1, 2, 3)

# fix the first index of the range whose longest one-large-prime run is reported
_BEYOND = (1 << 15) - 1

# fix the expectations of both modes before the enumeration runs
_EXPECTED = {
    'full': {
        'X': 10_000_000,
        'M': 40_000,
        'max_valuation': 29,
        'records': [
            (16, 4),
            (28, 6),
            (64, 10),
            (88, 12),
            (2_146_743, 28),
            (2_786_632, 29),
        ],
        'hits': {0: 72, 1: 45, 2: 21, 3: 9},
        'prefix_length': 11_759,
        'first_terms': [
            1,
            2,
            1,
            2,
            1,
            1,
            2,
            1,
            12,
            1,
            1,
            2,
            1,
            1,
            6,
            6,
            19,
            3,
            54,
            1,
            3,
            1,
            7,
            1,
            1,
            1,
            3,
            4,
            3,
            1,
        ],
        'largest_quotient': (15_531, 7_055),
        'denominator_digits': 6_018,
        'decimal_prefix': 1_367_630_801_985,
        'excess_positive': 71,
        'certifiable': [64, 204, 512, 1_632],
        'windows': (240, 31_790, 20),
    },
    'quick': {
        'X': 1_000_000,
        'M': 4_000,
        'max_valuation': 21,
        'records': [(16, 4), (28, 6), (64, 10), (88, 12)],
        'hits': {0: 45, 1: 28, 2: 12, 3: 4},
        'prefix_length': 1_171,
        'first_terms': [
            1,
            2,
            1,
            2,
            1,
            1,
            2,
            1,
            12,
            1,
            1,
            2,
            1,
            1,
            6,
            6,
            19,
            3,
            54,
            1,
            3,
            1,
            7,
            1,
            1,
            1,
            3,
            4,
            3,
            1,
        ],
        'largest_quotient': (3_281, 911),
        'denominator_digits': 599,
        'decimal_prefix': 1_367_630_801_985,
        'excess_positive': 44,
        'certifiable': [64, 204, 512, 1_632],
        'windows': (240, 31_790, 18),
    },
}

# retain small exact totient values as a sieve control
_SMALL_TOTIENTS = (1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4)

# retain three factorizations as a control of the large-prime-factor sieve
_SMALL_FACTORS = ((257, 257, 0), (258, 43, 3), (264, 11, 3))


def totients(limit: int) -> array:
    """Return phi(0..limit) by the ordinary prime-by-prime sieve."""
    # initialize the identity and mark composites while dividing out primes
    phi = array('q', range(limit + 1))
    composite = bytearray(limit + 1)
    for p in range(2, limit + 1):
        if composite[p]:
            continue
        if p * p <= limit:
            composite[p * p :: p] = b'\x01' * len(range(p * p, limit + 1, p))
        for k in range(p, limit + 1, p):
            phi[k] -= phi[k] // p
    return phi


def tail_valuations(phi: array, limit: int) -> bytearray:
    """Return v_2(Phi_N) for 0 <= N <= limit, computed modulo 2 ** _CAP."""
    # advance the scaled partial sum and record its trailing zero count
    mask = (1 << _CAP) - 1
    acc = 0
    valuations = bytearray(limit + 1)
    for n in range(1, limit + 1):
        acc = ((acc << 1) + phi[n]) & mask
        valuations[n] = (acc & -acc).bit_length() - 1 if acc else _CAP
    return valuations


def large_prime_factors(limit: int) -> tuple[array, array]:
    """Return the largest and second-largest distinct prime factors of 0..limit.

    An entry without a second distinct prime factor holds zero there.
    """
    # overwrite along multiples in increasing prime order; the last two writes remain
    largest = array('i', [0]) * (limit + 1)
    second = array('i', [0]) * (limit + 1)
    composite = bytearray(limit + 1)
    for p in range(2, limit + 1):
        if composite[p]:
            continue
        if p * p <= limit:
            composite[p * p :: p] = b'\x01' * len(range(p * p, limit + 1, p))
        second[p::p] = largest[p::p]
        largest[p::p] = array('i', [p]) * len(range(p, limit + 1, p))
    return largest, second


def one_large_prime_windows(
    largest: array, second: array, limit: int
) -> tuple[int, int, int]:
    """Return statistics of the one-large-prime windows of every N <= limit.

    An integer is one-large-prime for the threshold J when it has exactly one
    distinct prime factor above J. The window of N is N + 1, ..., N + J with
    J = ceil(log2(N + 2)). Returns the number of N whose whole window is
    one-large-prime, the last such N, and the longest run of one-large-prime
    integers starting at N + 1 over N >= _BEYOND, truncated at the
    dyadic block endpoint plus J. The arrays must extend to
    limit + ceil(log2(limit + 2)).
    """
    # scan each dyadic block of N, on which the window length J is constant
    count = 0
    last = 0
    longest = 0
    for j in range(2, (limit + 1).bit_length() + 1):
        low = max(1, (1 << (j - 1)) - 1)
        high = min(limit, (1 << j) - 2)
        # fill the run lengths of one-large-prime integers from the top down
        runs = array('i', [0]) * (high + j - low + 2)
        for n in range(high + j, low, -1):
            good = largest[n] > j and second[n] <= j
            runs[n - low] = runs[n - low + 1] + 1 if good else 0
        best = 0
        for n in range(low, high + 1):
            run = runs[n + 1 - low]
            best = max(best, run)
            if run >= j:
                count += 1
                last = n
        if low >= _BEYOND:
            longest = max(longest, best)
    return count, last, longest


def continued_fraction(numerator: int, denominator: int) -> list[int]:
    """Return the regular continued fraction of a nonnegative rational."""
    # run Euclid's algorithm and collect the partial quotients
    terms: list[int] = []
    while denominator:
        quotient, remainder = divmod(numerator, denominator)
        terms.append(quotient)
        numerator, denominator = denominator, remainder
    return terms


def _v2(value: int) -> int:
    """Return the 2-adic valuation of a positive integer."""
    return (value & -value).bit_length() - 1


def main() -> int:
    """Run every obligation of the selected mode and return the exit code."""
    # select the mode and its fixed expectations
    parser = tools.evidence_parser(
        'Probe tail valuations and a certified continued fraction of S.'
    )
    args = parser.parse_args()
    mode = 'quick' if args.quick else 'full'
    expected = _EXPECTED[mode]
    limit = expected['X']
    depth = expected['M']
    checker = tools.Checker()
    print(f'mode={mode} X={limit} M={depth}')

    # sieve the totients and control them against exact small values
    phi = totients(limit)
    checker.check(
        'sieve reproduces phi(1..12)',
        tuple(phi[1:13]) == _SMALL_TOTIENTS,
        f'observed {tuple(phi[1:13])}',
    )
    checker.check(
        'sieve reproduces phi at the top power of two and at the limit',
        phi[1 << 19] == 1 << 18 and phi[limit] == (limit // 10) * 4,
        f'observed {phi[1 << 19]}, {phi[limit]}',
    )

    # compute the valuations and locate records and threshold hits
    valuations = tail_valuations(phi, limit)
    largest = max(valuations)
    print(f'largest valuation v_2(Phi_N) for N <= X: {largest}')
    checker.check('largest valuation stays below the accumulator cap', largest < _CAP)
    records: list[tuple[int, int]] = []
    best_n = 1
    best_power = 0
    hits = dict.fromkeys(_THRESHOLDS, 0)
    excess_positive: list[int] = []
    for n in range(_FIRST, limit + 1):
        power = 1 << valuations[n]
        if power * best_n > best_power * n:
            best_n, best_power = n, power
            records.append((n, valuations[n]))
        for threshold in _THRESHOLDS:
            if power >= n * (1 << threshold):
                hits[threshold] += 1
        if power > n + 2:
            excess_positive.append(n)
    print('records (N, v_2(Phi_N), excess over log2 N):')
    for n, valuation in records:
        print(f'  {n} {valuation} {valuation - math.log2(n):.3f}')
    print(f'hit counts of excess >= C for N >= {_FIRST}: {hits}')
    ties = [_v2(phi[n]) == 1 + valuations[n - 1] for n, _ in records]
    print(f'records reached through a carry tie: {sum(ties)} of {len(records)}')
    checker.check('every record arises through a carry tie', all(ties))
    if expected['records'] is not None:
        checker.check(
            'exact record list', records == expected['records'], f'observed {records}'
        )
        checker.check(
            'exact largest valuation',
            largest == expected['max_valuation'],
            f'observed {largest}',
        )
        checker.check('exact hit counts', hits == expected['hits'], f'observed {hits}')

    # list the excess-positive indices and those a whole progression could deliver
    certifiable = [n for n in excess_positive if 1 << (_v2(phi[n]) + 2) > n + 2]
    print(
        f'excess-positive indices (2^v_2(Phi_N) > N + 2) for N >= {_FIRST}: '
        f'{len(excess_positive)}'
    )
    print(f'those with 2^(v_2(phi(N)) + 2) > N + 2: {certifiable}')
    checker.check(
        'exact count of excess-positive indices',
        len(excess_positive) == expected['excess_positive'],
        f'observed {len(excess_positive)}',
    )
    checker.check(
        'exact list of excess-positive indices meeting the certificate condition',
        certifiable == expected['certifiable'],
        f'observed {certifiable}',
    )

    # count the one-large-prime windows after controlling the prime-factor sieve
    span = limit + (limit + 1).bit_length()
    largest_factor, second_factor = large_prime_factors(span)
    observed = [(largest_factor[n], second_factor[n]) for n, _, _ in _SMALL_FACTORS]
    checker.check(
        'prime-factor sieve reproduces 257, 258 = 2*3*43 and 264 = 2^3*3*11',
        observed == [(big, next_big) for _, big, next_big in _SMALL_FACTORS],
        f'observed {observed}',
    )
    windows = one_large_prime_windows(largest_factor, second_factor, limit)
    print(
        f'one-large-prime windows of length ceil(log2(N + 2)): {windows[0]}, '
        f'last at N = {windows[1]}, longest truncated run for N >= {_BEYOND}: {windows[2]}'
    )
    checker.check(
        'exact count, last index and truncated-run statistic of one-large-prime windows',
        windows == expected['windows'],
        f'observed {windows}',
    )

    # report the empirical tail of the valuation distribution on [X/2, X]
    counts = [0] * (_CAP + 1)
    for n in range(limit // 2, limit + 1):
        counts[valuations[n]] += 1
    total = sum(counts)
    print('valuation m, count on [X/2, X], count / (total * 2^-m):')
    for m in range(1, largest + 1):
        ratio = counts[m] / (total * 2.0**-m)
        print(f'  {m:2d} {counts[m]:9d} {ratio:8.3f}')

    # certify a continued-fraction prefix of S from two-sided rational bounds
    scaled = 0
    for n in range(1, depth + 1):
        scaled = (scaled << 1) + phi[n]
    lower = continued_fraction(scaled, 1 << depth)
    upper = continued_fraction(scaled + depth + 2, 1 << depth)
    common = 0
    while common < min(len(lower), len(upper)) and lower[common] == upper[common]:
        common += 1
    prefix = lower[:common]
    body = prefix[1:]
    largest_quotient = max(body)
    position = 1 + body.index(largest_quotient)
    decimal_prefix = (scaled * 10**12) >> depth
    checker.check(
        'certified prefix is long enough to use',
        common > 30 and common < len(lower) and common < len(upper),
        f'observed common={common} lengths={len(lower)},{len(upper)}',
    )
    checker.check(
        'decimal prefix of S from the lower bound',
        decimal_prefix == expected['decimal_prefix']
        and ((scaled + depth + 2) * 10**12) >> depth == expected['decimal_prefix'],
        f'observed {decimal_prefix}',
    )
    # compute the last convergent and check the whole enclosure is in its cylinder
    p_prev, p_last = 1, prefix[0]
    q_prev, q_last = 0, 1
    for term in body:
        p_prev, p_last = p_last, term * p_last + p_prev
        q_prev, q_last = q_last, term * q_last + q_prev
    endpoints = sorted(
        (
            Fraction(p_last, q_last),
            Fraction(p_last + p_prev, q_last + q_prev),
        )
    )
    checker.check(
        'continued-fraction endpoints are Farey neighbours',
        abs(p_last * q_prev - p_prev * q_last) == 1,
    )
    checker.check(
        'the rational tail enclosure is strictly inside the common cylinder',
        endpoints[0]
        < Fraction(scaled, 1 << depth)
        < Fraction(scaled + depth + 2, 1 << depth)
        < endpoints[1],
    )
    sys.set_int_max_str_digits(0)
    digits = len(str(q_last))
    ones = sum(1 for term in body if term == 1) / len(body)
    geometric = math.exp(sum(math.log(term) for term in body) / len(body))
    print(f'S = {scaled / 2**depth:.15f}...; certified prefix length {common}')
    print(f'first terms {prefix[:30]}')
    print(f'largest certified partial quotient {largest_quotient} at index {position}')
    print(f'proportion of ones {ones:.3f}; geometric mean {geometric:.3f}')
    print(f'denominator of the last certified convergent has {digits} decimal digits')
    if expected['prefix_length'] is not None:
        checker.check(
            'exact certified prefix length',
            common == expected['prefix_length'],
            f'observed {common}',
        )
        checker.check(
            'exact first thirty partial quotients',
            prefix[:30] == expected['first_terms'],
            f'observed {prefix[:30]}',
        )
        checker.check(
            'exact largest certified partial quotient and index',
            (largest_quotient, position) == expected['largest_quotient'],
            f'observed {(largest_quotient, position)}',
        )
    if expected['denominator_digits'] is not None:
        checker.check(
            'exact digit count of the last certified denominator',
            digits == expected['denominator_digits'],
            f'observed {digits}',
        )
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
