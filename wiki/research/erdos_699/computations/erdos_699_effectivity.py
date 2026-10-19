"""Compute the effective-index reduction for Erdős problem 699.

Run with Python 3.11 or later; no third-party packages are required.
The proof is in ../archive/previous_bounds/effectivity.md.

The index classification uses exact rational arithmetic. Numerical row bounds
are certified powers of ten, obtained with outward-rounded Decimal logarithms.
The bounded check compares a residue/Lucas search with direct binomial gcds;
it does not enumerate the entire possible exceptional set.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction
import json
from math import comb, factorial, gcd, isqrt


PRECISION = 60
KNOWN_INDEX_CUTOFF = 906


def primes_through(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return [p for p in range(2, limit + 1) if sieve[p]]


def certificate(i: int) -> tuple[int, int, int, int]:
    """Return k, multiplicity, degree, and the exponent of the factor 4."""
    if i == 4:
        return 0, 6, 17, 5
    k = 2 * i // 3
    return k, 3 * k - i + 1, 3 * k * (k + 1) // 2, k * (k + 1) // 2


def logarithm_intervals(limit: int) -> list[tuple[Decimal, Decimal]]:
    with localcontext() as ctx:
        ctx.prec = PRECISION
        result = [(Decimal(0), Decimal(0))] * (limit + 1)
        for n in range(1, limit + 1):
            value = Decimal(n).ln()  # Correctly rounded, independently of mode.
            result[n] = value.next_minus(), value.next_plus()
        return result


def factorial_log_upper_bounds(
    logs: list[tuple[Decimal, Decimal]],
) -> list[Decimal]:
    result = [Decimal(0)] * len(logs)
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_CEILING
        for i in range(2, len(logs)):
            result[i] = result[i - 1] + logs[i][1]
    return result


def certified_bound_exponent(
    i: int,
    s: int,
    logs: list[tuple[Decimal, Decimal]],
    log_factorials_upper: list[Decimal],
) -> int:
    """Certify that a bad triple has n < 10**b; return b.

    For n >= i(i-1), badness implies
        4**A * n**E < (2*i!)**m,
    where E=m*(i-s)-d>0. Bound its logarithmic threshold from above.
    """
    _, m, d, a = certificate(i)
    e = m * (i - s) - d
    if e <= 0:
        raise ValueError("the elementary exponent is not positive")
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_FLOOR
        subtrahend_lower = a * logs[4][0]
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_CEILING
        numerator_upper = m * (logs[2][1] + log_factorials_upper[i])
        numerator_upper -= subtrahend_lower
        log10_bound_upper = numerator_upper / e / logs[10][0]
        b = int(log10_bound_upper.to_integral_value(rounding=ROUND_CEILING))
    while 10**b < i * (i - 1):
        b += 1
    return b


def valuation_factorial(n: int, p: int) -> int:
    total = 0
    while n:
        n //= p
        total += n
    return total


def rough_prime_powers(n: int, i: int, primes: list[int]) -> list[tuple[int, int]]:
    result = []
    for q in primes:
        if q > n:
            break
        if q < i:
            continue
        a = (
            valuation_factorial(n, q)
            - valuation_factorial(i, q)
            - valuation_factorial(n - i, q)
        )
        if a:
            result.append((q, q**a))
    return result


def lucas_nonzero(n: int, j: int, p: int) -> bool:
    while j:
        if j % p > n % p:
            return False
        n //= p
        j //= p
    return True


def bad_columns(n: int, i: int, primes: list[int]) -> list[int]:
    """An exact, terminating search for bad j in one supplied row/index.

    Kummer localization supplies j mod q**a <= n mod q**a < i. Generate
    columns from the sparsest of these conditions and check full Lucas digits
    at every rough prime. This also handles the allowed prime q=i.
    """
    if not 1 <= i < n // 2:
        return []
    powers = rough_prime_powers(n, i, primes)
    if not powers:
        return list(range(i + 1, n // 2 + 1))
    for _, power in powers:
        assert n % power < i

    _, modulus = max(
        powers, key=lambda pair: Fraction(pair[1], n % pair[1] + 1)
    )
    result = []
    for residue in range(n % modulus + 1):
        first = residue + max(0, (i + 1 - residue + modulus - 1) // modulus) * modulus
        for j in range(first, n // 2 + 1, modulus):
            if all(lucas_nonzero(n, j, q) for q, _ in powers):
                result.append(j)
    return sorted(result)


def bounded_check(limit: int) -> dict:
    primes = primes_through(limit)
    index_rows = 0
    triples = 0
    bad = []
    for n in range(4, limit + 1):
        row = [comb(n, j) for j in range(n // 2 + 1)]
        for i in range(1, min(35, n // 2)):
            expected = []
            for j in range(i + 1, n // 2 + 1):
                common = gcd(row[i], row[j])
                for p in primes:
                    if p >= i:
                        break
                    while common % p == 0:
                        common //= p
                if common == 1:
                    expected.append(j)
                triples += 1
            actual = bad_columns(n, i, primes)
            assert actual == expected, (n, i, actual, expected)
            bad.extend([n, i, j] for j in actual)
            index_rows += 1
    return {
        "n_at_most": limit,
        "i_at_most": 34,
        "index_rows": index_rows,
        "admissible_triples": triples,
        "comparison": "Kummer-residue/Lucas search equals direct binomial gcd search",
        "bad_triples": bad,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-limit", type=int, default=200)
    args = parser.parse_args()
    primes = primes_through(KNOWN_INDEX_CUTOFF)
    logs = logarithm_intervals(KNOWN_INDEX_CUTOFF)
    log_factorials = factorial_log_upper_bounds(logs)
    positive = []
    borderline = []
    unresolved = []
    data = []
    for i in range(4, KNOWN_INDEX_CUTOFF):
        s = sum(p < i for p in primes)
        k, m, d, a = certificate(i)
        e = m * (i - s) - d
        item = {
            "i": i,
            "number_of_small_primes": s,
            "rho": str(Fraction(d, m)),
            "elementary_exponent_gain": str(Fraction(e, m)),
        }
        if e > 0:
            positive.append(i)
            b = certified_bound_exponent(i, s, logs, log_factorials)
            item["bad_row_bound_exclusive"] = f"10^{b}"
            item["power_of_ten_exponent"] = b
            # Independent exact comparisons at representative indices, including
            # the largest certified decimal exponent and both ends of the band.
            if i in {29, 35, 44, 100, 905}:
                assert 4**a * 10 ** (b * e) >= (2 * factorial(i)) ** m
        elif e == 0:
            borderline.append(i)
        else:
            unresolved.append(i)
        data.append(item)

    assert positive == [29, *range(35, 906)]
    assert borderline == [28, 31, 34]
    assert unresolved == [*range(4, 28), 30, 32, 33]
    worst = max(
        (item for item in data if "power_of_ten_exponent" in item),
        key=lambda item: item["power_of_ten_exponent"],
    )
    result = {
        "threshold": "p >= i (the original problem)",
        "elementary_effective_indices": "i=29 and 35<=i<=905",
        "elementary_effective_index_count": len(positive),
        "effective_via_peak_polynomial_and_BEG_2_2": borderline,
        "BEG_constants_evaluated": False,
        "no_effective_cutoff_derived": unresolved,
        "i_3": "outside the finite-set theorem",
        "known_empty_tail": "i>=906, from the retained earlier calculation",
        "uniform_elementary_row_bound_exclusive": worst["bad_row_bound_exclusive"],
        "largest_bound_at_i": worst["i"],
        "logarithm_precision": PRECISION,
        "bound_method": "outward-rounded Decimal intervals, with five exact integer cross-checks",
        "index_data": data,
        "bounded_search_check": bounded_check(args.check_limit),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
