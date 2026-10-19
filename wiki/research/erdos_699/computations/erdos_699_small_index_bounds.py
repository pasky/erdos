"""Certify numerical row bounds for ten small indices of Erdős problem 699.

Uses BFT Theorem 2.1 (the fully explicit table), the exact max-constraint
optimization checked by erdos_699_prime_pair_savings.py, and the retained
fat-point constants. This calculation enumerates no rows or columns.
"""

from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction
import json
from math import factorial
from pathlib import Path

from erdos_699_effectivity import certificate, primes_through

PRECISION = 60
THRESHOLD = 1_771_595
GAMMA = Fraction(913, 1000)
INDICES = (17, 23, 26, 27, 28, 30, 31, 32, 33, 34)


def log_interval(value: int | Decimal) -> tuple[Decimal, Decimal]:
    with localcontext() as ctx:
        ctx.prec = PRECISION
        result = Decimal(value).ln()
        return result.next_minus(), result.next_plus()


def certify(i: int) -> dict:
    _, m, degree, a = certificate(i)
    s = len(primes_through(i - 1))
    eta = i - Fraction(degree, m) - s + GAMMA
    assert eta > 0
    small_part_i = 1 if i in primes_through(i) else i
    factorial_hi = log_interval(factorial(i) // small_part_i)[1]
    four_lo = log_interval(4)[0]
    two_hi = log_interval(2)[1]
    ten_lo, ten_hi = log_interval(10)
    # gamma_i = 1 - i(i-1)/(2*THRESHOLD), the numerator product bound.
    numerator_lo = log_interval(2 * THRESHOLD - i * (i - 1))[0]
    denominator_hi = log_interval(2 * THRESHOLD)[1]
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_FLOOR
        gamma_log_lo = numerator_lo - denominator_hi
        four_term_lo = a * four_lo / m
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_CEILING
        log_m_hi = factorial_hi - four_term_lo - gamma_log_lo
        rhs_hi = log_m_hi + GAMMA.numerator * two_hi / GAMMA.denominator
        exponent_hi = rhs_hi * eta.denominator / eta.numerator / ten_lo
        exponent = int(exponent_hi.to_integral_value(rounding=ROUND_CEILING))
    assert 10**exponent >= THRESHOLD
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_FLOOR
        lhs_lo = exponent * ten_lo * eta.numerator / eta.denominator
        margin_lo = lhs_lo - rhs_hi
    assert margin_lo > 0
    return {
        "i": i,
        "eta": str(eta),
        "exclusive_row_bound": f"10^{exponent}",
        "power_of_ten": exponent,
        "log_M_upper": str(log_m_hi),
        "comparison_margin_lower": str(margin_lo),
    }


def main() -> None:
    result = {
        "description": "Fully numerical small-index bounds, using BFT Theorem 2.1; no row enumeration.",
        "precision": PRECISION,
        "BFT_uniform_threshold": THRESHOLD,
        "cofactor_exponent_sum": str(GAMMA),
        "records": [certify(i) for i in INDICES],
    }
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
