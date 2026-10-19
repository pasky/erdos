#!/usr/bin/env python3
"""Certify the refined index-11 bound; enumerate proof patterns, not rows."""

from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from itertools import permutations
import json
from math import factorial

from erdos_699_index_11_effective import minimal_vectors


PRECISION = 60
PRIMES = (2, 3, 5, 7)
SCALE = 10_000


def log_bounds(integer):
    # Decimal.ln is correctly rounded to nearest, independently of the context
    # rounding mode; adjacent representable values enclose the exact answer.
    with localcontext() as ctx:
        ctx.prec = PRECISION
        value = Decimal(integer).ln()
        return value.next_minus(), value.next_plus()


def valuation(integer, prime):
    result = 0
    while integer % prime == 0:
        result += 1
        integer //= prime
    return result


def report():
    _, vectors = minimal_vectors(PRIMES)
    weights = [14 - t for t in range(11)]
    assert sum(weights) == 99
    assert sum(t * m for t, m in enumerate(weights)) == 385
    # For n >= 10^6, the numerator product and the replacement of n-10
    # by n together lose less than 1000/999.
    base = 10**6
    assert (base - 385) * (base - 560) * 1000 > 999 * base**2
    off_maximum = {
        (p, r): sum(weights[t] * valuation(abs(t - r), p)
                    for t in range(11) if t != r)
        for p in PRIMES for r in range(11)
    }
    logs = {n: log_bounds(n) for n in (*PRIMES, 10, 11, 999, 1000)}
    worst = None
    minimum_margin = Decimal("Infinity")
    patterns = 0
    minimum_gain = SCALE
    for positions in permutations(range(11), 4):
        with localcontext() as ctx:
            ctx.prec = PRECISION
            ctx.rounding = ROUND_FLOOR
            deduction = logs[999][0] + 56 * logs[2][0]
        with localcontext() as ctx:
            ctx.prec = PRECISION
            ctx.rounding = ROUND_CEILING
            log_constant = (logs[1000][1] - deduction + 14 * logs[11][1]
                            + sum(off_maximum[p, r] * logs[p][1]
                                  for p, r in zip(PRIMES, positions)))
        for vector in vectors:
            patterns += 1
            gain = 43 * SCALE - sum(
                weights[r] * (SCALE - v) for r, v in zip(positions, vector))
            assert gain > 0
            minimum_gain = min(minimum_gain, gain)
            with localcontext() as ctx:
                ctx.prec = PRECISION
                ctx.rounding = ROUND_FLOOR
                denominator = gain * logs[10][0]
                left = 484 * denominator
            with localcontext() as ctx:
                ctx.prec = PRECISION
                ctx.rounding = ROUND_CEILING
                right = SCALE * log_constant
                exponent_bound = right / denominator
            with localcontext() as ctx:
                ctx.prec = PRECISION
                ctx.rounding = ROUND_FLOOR
                margin = left - right
            assert margin > 0
            minimum_margin = min(minimum_margin, margin)
            if worst is None or exponent_bound > worst[0]:
                worst = (exponent_bound, positions, vector,
                         [off_maximum[p, r] for p, r in zip(PRIMES, positions)])
    assert patterns == 63_360
    assert minimum_gain == 700
    # The earlier collision argument covers the non-injective assignments.
    assert 10 ** (22 * 4) * 4**28 > (2 * factorial(11))**11
    return {
        "scope": "Proof-pattern enumeration; no binomial rows searched.",
        "distinct_position_assignments": 7920,
        "cofactor_vectors": len(vectors),
        "certified_patterns": patterns,
        "minimum_gain": "7/100",
        "algebraic_cap": "10^484",
        "full_cap": "max(10^484, X_11 + 10)",
        "source_threshold": "X_11 is the unchanged effective BFT threshold.",
        "worst_log10_bound_upper": str(worst[0]),
        "worst_positions_in_prime_order": worst[1],
        "worst_vector_scaled": worst[2],
        "worst_off_maximum_exponents": worst[3],
        "minimum_scaled_log_margin": str(minimum_margin),
        "decimal_precision": PRECISION,
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2))
