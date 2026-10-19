"""Verify the strengthened ``i >= 906`` cutoff in the Van Doorn--Rocca bound.

The calculation keeps the factorial product discarded in the last, coarser
line of Lemma 1.  It verifies the two finite ranges against the published
prime-gap records and checks the elementary analytic estimate used for the
remaining tail.  Python's decimal logarithm is correctly rounded; 50 decimal
digits are used, while the smallest reported logarithmic margin exceeds 0.56.

Run with Python 3.11 or later.  No third-party packages are required.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
import json


FINITE_LIMIT = 1_000_000
INDEX_CUTOFF = 906
PRIME_GAP_LIMIT = 4_000_000_000_000_000_000
RAMARE_SAOUTER_DELTA = 28_314_000
RAMARE_SAOUTER_START = 10_726_905_041
ROSSER_SCHOENFELD_PI_CONSTANT = Decimal("1.25506")
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
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for prime in range(2, int(limit**0.5) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start : limit + 1 : prime] = b"\x00" * (
                (limit - start) // prime + 1
            )
    result = [0] * (limit + 1)
    count = 0
    for value in range(limit + 1):
        count += sieve[value]
        result[value] = count
    return result


def superfactorial_logs(limit: int) -> list[Decimal]:
    """Return log(prod_{r=1}^k r!) for 0 <= k <= limit."""

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
    """Return log N_i, where a counterexample would have n < N_i."""

    k = (i + 1) // 2
    exponent_n_numerator = (i - k) + k * (k - 1) // 2
    exponent_two_numerator = (i - k) + k * i - k * (k - 1) // 2
    alpha = Decimal(exponent_n_numerator) / Decimal(k + 1)
    beta = Decimal(exponent_two_numerator) / Decimal(k + 1)
    denominator = alpha - Decimal(prime_pi[i])
    if denominator <= 0:
        raise AssertionError(f"nonpositive exponent at i={i}")
    numerator = (
        Decimal("1.04") * Decimal(i)
        + beta * Decimal(2).ln()
        + log_superfactorial[k] / Decimal(k + 1)
    )
    return numerator / denominator


def first_record_gap_above(i: int) -> int:
    for gap, lower_endpoint in RECORD_GAPS:
        if gap > i:
            return lower_endpoint
    raise AssertionError(f"no record threshold supplied for i={i}")


def analytic_tail_margin() -> dict[str, str]:
    """Prove N_i < Delta*i for real i >= 10^6 using coarse bounds."""

    x = Decimal(FINITE_LIMIT)
    log_x = x.ln()
    # For i >= x, k <= (i+1)/2, alpha >= i/4,
    # beta <= 3(i+1)/4, and log(prod r!)/(k+1) <= (k/2)log k.
    # Dividing the numerator by i gives at most log(i)/4 + C.  The
    # (1+1/i)-terms decrease, so their value at x is a uniform bound.
    constant = (
        Decimal("1.04")
        + Decimal("0.75") * (1 + 1 / x) * Decimal(2).ln()
        + Decimal("0.25")
        * (1 + 1 / x)
        * ((1 + 1 / x).ln() - Decimal(2).ln())
    )
    a = 4 * constant
    b = 4 * ROSSER_SCHOENFELD_PI_CONSTANT
    # Rosser--Schoenfeld gives pi(i) < 1.25506*i/log(i).  Therefore
    # log N_i - log i <= (a+b)L/(L-b), which decreases with L=log i.
    excess_bound = (a + b) * log_x / (log_x - b)
    margin = Decimal(RAMARE_SAOUTER_DELTA).ln() - excess_bound
    if margin <= 0:
        raise AssertionError("analytic tail margin is not positive")
    return {
        "start": str(FINITE_LIMIT),
        "numerator_constant_C": str(constant),
        "upper_bound_for_log_N_i_minus_log_i": str(excess_bound),
        "log_delta": str(Decimal(RAMARE_SAOUTER_DELTA).ln()),
        "log_margin": str(margin),
    }


def main() -> None:
    getcontext().prec = 50
    prime_pi = prime_pi_table(FINITE_LIMIT)
    log_superfactorial = superfactorial_logs((FINITE_LIMIT + 1) // 2)

    first_minimum = (Decimal("Infinity"), -1)
    for i in range(INDEX_CUTOFF, 1476):
        margin = Decimal(first_record_gap_above(i)).ln() - log_counterexample_bound(
            i, prime_pi, log_superfactorial
        )
        if margin <= 0:
            raise AssertionError(f"prime-gap threshold fails at i={i}")
        if margin < first_minimum[0]:
            first_minimum = (margin, i)

    second_minimum = (Decimal("Infinity"), -1)
    for i in range(1476, FINITE_LIMIT):
        margin = Decimal(PRIME_GAP_LIMIT).ln() - log_counterexample_bound(
            i, prime_pi, log_superfactorial
        )
        if margin <= 0:
            raise AssertionError(f"4e18 confinement fails at i={i}")
        if margin < second_minimum[0]:
            second_minimum = (margin, i)

    result = {
        "precision_decimal_digits": getcontext().prec,
        "counterexample_bound": {
            "description": "n < N_i from the uncoarsened factorial-product form of Lemma 1 and G <= n^pi(i)",
            "lcm_bound": "lcm(1,...,i) < exp(1.04*i)",
        },
        "finite_checks": [
            {
                "range": f"{INDEX_CUTOFF} <= i < 1476",
                "comparison": "N_i is below the first lower endpoint of a prime gap longer than i",
                "minimum_log_margin": str(first_minimum[0]),
                "minimum_at_i": first_minimum[1],
            },
            {
                "range": f"1476 <= i < {FINITE_LIMIT}",
                "comparison": "N_i < 4e18, where every prime gap is at most 1476",
                "minimum_log_margin": str(second_minimum[0]),
                "minimum_at_i": second_minimum[1],
            },
        ],
        "method_boundary": {
            "i": INDEX_CUTOFF - 1,
            "first_longer_gap": PREVIOUS_RECORD_GAP[0],
            "first_longer_gap_lower_endpoint": PREVIOUS_RECORD_GAP[1],
            "log_margin": str(
                Decimal(PREVIOUS_RECORD_GAP[1]).ln()
                - log_counterexample_bound(
                    INDEX_CUTOFF - 1, prime_pi, log_superfactorial
                )
            ),
            "interpretation": "the same confinement comparison does not certify i=905",
        },
        "analytic_tail": analytic_tail_margin(),
        "prime_interval_input": {
            "delta": RAMARE_SAOUTER_DELTA,
            "start": RAMARE_SAOUTER_START,
            "statement": "for x above start, (x*(1-1/delta), x] contains a prime",
        },
        "conclusion": f"Every admissible triple with i >= {INDEX_CUTOFF} has a common prime divisor p > i.",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
