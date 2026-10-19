"""Check the repository-supplied ``i >= 906`` cutoff for E0699.

The full run checks the uncoarsened factorial-product consequence of Lemma 1
for every integer ``906 <= i < 10^6`` and checks the elementary analytic bound
used for the remaining tail.  The finite clauses compare against Table 8 of
Oliveira e Silva--Herzog--Pardi (record prime gaps through ``4*10^18``).  The
tail takes as published premises Rosser--Schoenfeld's prime-counting estimate
and Ramaré--Saouter Theorem 3, including their finite maximum-gap computation.
It does not reverify those external computations or the manuscript's Lemma 1.

Arithmetic is Python integers plus correctly rounded ``Decimal`` logarithms at
50 digits; the smallest accepted logarithmic margin is greater than 0.26.
There are no file inputs, random choices, output files, or reduced modes.

Run from the repository root:
    uv run --no-sync python library/factorials_binomials/van_doorn_rocca_2026_binomial_coefficients_sharing_large_prime_divisor/evidence/main.py

Dependencies are Python 3.11 or later and the installed root ``tools`` package.
Expected runtime is about one minute.  Failed obligations exit nonzero,
including under ``python -O``.  Success proves no case with ``i < 906``.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
import json
import sys

import tools


INDEX_CUTOFF = 906
RECORD_GAP_LIMIT = 1476
FINITE_LIMIT = 1_000_000
PRIME_GAP_LIMIT = 4_000_000_000_000_000_000
RAMARE_SAOUTER_DELTA = 28_314_000
RAMARE_SAOUTER_START = 10_726_905_041
ROSSER_SCHOENFELD_PI_CONSTANT = Decimal('1.25506')
PREVIOUS_RECORD_GAP = (906, 218_209_405_436_543)

# Table 8 of Oliveira e Silva--Herzog--Pardi: successive record gaps
# relevant to 906 <= i < 1476, as (gap, lower prime endpoint).
RECORD_GAPS = (
    (916, 1_189_459_969_825_483),
    (924, 1_686_994_940_955_803),
    (1132, 1_693_182_318_746_371),
    (1184, 43_841_547_845_541_059),
    (1198, 55_350_776_431_903_243),
    (1220, 80_873_624_627_234_849),
    (1224, 203_986_478_517_455_989),
    (1248, 218_034_721_194_214_273),
    (1272, 305_405_826_521_087_869),
    (1328, 352_521_223_451_364_323),
    (1356, 401_429_925_999_153_707),
    (1370, 418_032_645_936_712_127),
    (1442, 804_212_830_686_677_669),
    (1476, 1_425_172_824_437_699_411),
)


def prime_pi_table(limit: int) -> list[int]:
    """Return ``pi(i)`` for every ``0 <= i <= limit``."""

    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for prime in range(2, int(limit**0.5) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start : limit + 1 : prime] = b'\x00' * (
                (limit - start) // prime + 1
            )
    result = [0] * (limit + 1)
    count = 0
    for value in range(limit + 1):
        count += sieve[value]
        result[value] = count
    return result


def superfactorial_logs(limit: int) -> list[Decimal]:
    """Return ``log(prod(r!, r=1..k))`` for ``0 <= k <= limit``."""

    result = [Decimal(0)] * (limit + 1)
    log_factorial = Decimal(0)
    log_superfactorial = Decimal(0)
    for k in range(1, limit + 1):
        log_factorial += Decimal(k).ln()
        log_superfactorial += log_factorial
        result[k] = log_superfactorial
    return result


def log_counterexample_bound(
    i: int, prime_pi: list[int], log_superfactorial: list[Decimal]
) -> Decimal:
    """Return ``log N_i``, where a counterexample would have ``n < N_i``."""

    k = (i + 1) // 2
    exponent_n_numerator = (i - k) + k * (k - 1) // 2
    exponent_two_numerator = (i - k) + k * i - k * (k - 1) // 2
    alpha = Decimal(exponent_n_numerator) / Decimal(k + 1)
    beta = Decimal(exponent_two_numerator) / Decimal(k + 1)
    denominator = alpha - Decimal(prime_pi[i])
    if denominator <= 0:
        raise ValueError(f'nonpositive exponent at i={i}')
    numerator = (
        Decimal('1.04') * Decimal(i)
        + beta * Decimal(2).ln()
        + log_superfactorial[k] / Decimal(k + 1)
    )
    return numerator / denominator


def first_record_gap_above(i: int) -> int:
    """Return the first lower endpoint of a published record gap longer than i."""

    for gap, lower_endpoint in RECORD_GAPS:
        if gap > i:
            return lower_endpoint
    raise ValueError(f'no record threshold supplied for i={i}')


def analytic_tail() -> dict[str, Decimal]:
    """Bound ``log N_i - log i`` uniformly for real ``i >= 10^6``."""

    x = Decimal(FINITE_LIMIT)
    log_x = x.ln()
    # k <= (i+1)/2, alpha >= i/4, beta <= 3(i+1)/4, and
    # log(prod r!)/(k+1) <= (k/2)log k.  After division by i, the
    # non-logarithmic terms decrease, so their value at x is uniform.
    constant = (
        Decimal('1.04')
        + Decimal('0.75') * (1 + 1 / x) * Decimal(2).ln()
        + Decimal('0.25')
        * (1 + 1 / x)
        * ((1 + 1 / x).ln() - Decimal(2).ln())
    )
    a = 4 * constant
    b = 4 * ROSSER_SCHOENFELD_PI_CONSTANT
    # Rosser--Schoenfeld gives pi(i) < 1.25506*i/log(i).  Thus the next
    # expression is an upper bound, decreasing with L=log(i).
    excess_bound = (a + b) * log_x / (log_x - b)
    return {
        'numerator_constant_C': constant,
        'upper_bound_for_log_N_i_minus_log_i': excess_bound,
        'log_delta': Decimal(RAMARE_SAOUTER_DELTA).ln(),
        'log_margin': Decimal(RAMARE_SAOUTER_DELTA).ln() - excess_bound,
    }


def main() -> int:
    """Run every finite and analytic obligation and return the checker status."""

    parser = tools.evidence_parser(
        'Check the full i >= 906 cutoff for E0699.', quick=False
    )
    parser.parse_args()
    checker = tools.Checker()
    getcontext().prec = 50

    checker.check(
        'record gaps and lower endpoints are strictly increasing',
        all(
            left_gap < right_gap and left_endpoint < right_endpoint
            for (left_gap, left_endpoint), (right_gap, right_endpoint) in zip(
                RECORD_GAPS, RECORD_GAPS[1:]
            )
        )
        and RECORD_GAPS[0][0] > INDEX_CUTOFF
        and RECORD_GAPS[-1][0] == RECORD_GAP_LIMIT,
    )

    prime_pi = prime_pi_table(FINITE_LIMIT)
    log_superfactorial = superfactorial_logs((FINITE_LIMIT + 1) // 2)
    checker.check(
        'prime-counting sieve calibration',
        prime_pi[100] == 25
        and prime_pi[1000] == 168
        and prime_pi[FINITE_LIMIT] == 78_498,
    )
    checker.check(
        'superfactorial recurrence calibration',
        abs(log_superfactorial[3] - Decimal(12).ln()) < Decimal('1e-48'),
    )

    first_minimum = (Decimal('Infinity'), -1)
    for i in range(INDEX_CUTOFF, RECORD_GAP_LIMIT):
        margin = Decimal(first_record_gap_above(i)).ln() - log_counterexample_bound(
            i, prime_pi, log_superfactorial
        )
        if margin < first_minimum[0]:
            first_minimum = margin, i
    checker.check(
        f'counterexample bounds for {INDEX_CUTOFF} <= i < {RECORD_GAP_LIMIT}',
        first_minimum[0] > 0,
        f'minimum log margin {first_minimum[0]} at i={first_minimum[1]}',
    )
    previous_margin = (
        Decimal(PREVIOUS_RECORD_GAP[1]).ln()
        - log_counterexample_bound(
            INDEX_CUTOFF - 1, prime_pi, log_superfactorial
        )
    )
    checker.check(
        'record-gap confinement method stops at i=906',
        previous_margin < 0,
        f'log margin at i=905 is {previous_margin}',
    )

    second_minimum = (Decimal('Infinity'), -1)
    for i in range(RECORD_GAP_LIMIT, FINITE_LIMIT):
        margin = Decimal(PRIME_GAP_LIMIT).ln() - log_counterexample_bound(
            i, prime_pi, log_superfactorial
        )
        if margin < second_minimum[0]:
            second_minimum = margin, i
    checker.check(
        f'counterexample bounds for {RECORD_GAP_LIMIT} <= i < {FINITE_LIMIT}',
        second_minimum[0] > 0,
        f'minimum log margin {second_minimum[0]} at i={second_minimum[1]}',
    )

    tail = analytic_tail()
    checker.check(
        f'analytic counterexample bound for i >= {FINITE_LIMIT}',
        tail['log_margin'] > 0,
        f"log margin {tail['log_margin']}",
    )

    result = {
        'precision_decimal_digits': getcontext().prec,
        'counterexample_bound': {
            'description': (
                'n < N_i from the uncoarsened factorial-product form of '
                'Lemma 1 and G <= n^pi(i)'
            ),
            'lcm_bound': 'lcm(1,...,i) < exp(1.04*i)',
        },
        'finite_checks': [
            {
                'range': f'{INDEX_CUTOFF} <= i < {RECORD_GAP_LIMIT}',
                'comparison': (
                    'N_i is below the first lower endpoint of a prime gap '
                    'longer than i'
                ),
                'minimum_log_margin': str(first_minimum[0]),
                'minimum_at_i': first_minimum[1],
            },
            {
                'range': f'{RECORD_GAP_LIMIT} <= i < {FINITE_LIMIT}',
                'comparison': (
                    'N_i < 4e18, where every prime gap is at most 1476'
                ),
                'minimum_log_margin': str(second_minimum[0]),
                'minimum_at_i': second_minimum[1],
            },
        ],
        'method_boundary': {
            'i': INDEX_CUTOFF - 1,
            'first_longer_gap': PREVIOUS_RECORD_GAP[0],
            'first_longer_gap_lower_endpoint': PREVIOUS_RECORD_GAP[1],
            'log_margin': str(previous_margin),
            'interpretation': (
                'the same confinement comparison does not certify i=905'
            ),
        },
        'analytic_tail': {
            'start': FINITE_LIMIT,
            **{key: str(value) for key, value in tail.items()},
        },
        'prime_interval_input': {
            'delta': RAMARE_SAOUTER_DELTA,
            'start': RAMARE_SAOUTER_START,
            'statement': (
                'for x above start, (x*(1-1/delta), x] contains a prime'
            ),
        },
        'conclusion': (
            f'Every admissible triple with i >= {INDEX_CUTOFF} has a common '
            'prime divisor p > i.'
        ),
    }
    print(json.dumps(result, indent=2))
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
