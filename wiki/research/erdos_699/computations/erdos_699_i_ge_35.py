"""Certify that Erdős 699 has no bad triples for i>=35, or for i=29.

This checks i=29 and 35<=i<=905; the retained i>=906 theorem covers the tail.
Integer interval bounds on binomial valuations are compared with the symmetric
discriminant bound and the fat-point bound. Every accepted interval has a
positive, outward-rounded Decimal margin. Floating point only guides splitting.

Run with Python 3.11 or later, without third-party packages. The mathematical
derivation is in ../proofs/details/cutoff_and_cubic.md.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
import hashlib
import json
from math import log
from pathlib import Path
import sys

from erdos_699_effectivity import certificate, primes_through


PRECISION = 60
GAP_DATA = Path(__file__).with_name("erdos_699_prime_gap_records.json")


def log_bounds(n: int) -> tuple[Decimal, Decimal]:
    with localcontext() as ctx:
        ctx.prec = PRECISION
        value = Decimal(n).ln()
        return value.next_minus(), value.next_plus()


def constants(i: int, lower_row: int) -> dict:
    """Outward bounds for log C in U>C_f*n**lambda and G>=C_o*n**(i/4)."""
    _, m, degree, a = certificate(i)
    logs = [None, (Decimal(0), Decimal(0))]
    logs.extend(log_bounds(r) for r in range(2, i + 1))
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_CEILING
        log_factorial_hi = sum((logs[r][1] for r in range(2, i + 1)), Decimal(0))
        log_k_hi = sum((r * logs[r][1] for r in range(2, i + 1)), Decimal(0))
        k_term_hi = log_k_hi / (2 * i - 2)
    gamma_num = 2 * lower_row - i * (i - 1)
    gamma_den = 2 * lower_row
    if gamma_num <= 0:
        raise ValueError("the chosen lower row is too small for the product bound")
    gamma_num_lo = log_bounds(gamma_num)[0]
    gamma_den_hi = log_bounds(gamma_den)[1]
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_FLOOR
        log_gamma_lo = gamma_num_lo - gamma_den_hi
        fat_lo = a * logs[4][0] / m - log_factorial_hi + log_gamma_lo
        orbit_lo = i * logs[4][0] / 4 - k_term_hi + log_gamma_lo
    return {
        "multiplicity": m,
        "fat_exponent_numerator": i * m - degree,
        "fat_constant_lo": fat_lo,
        "orbit_constant_lo": orbit_lo,
    }


def inclusive_row_cap(i: int, primes: list[int], c: dict) -> tuple[int, int]:
    s = len(primes)
    # Kummer: v_p(C(n,i)) <= floor(log_p n)-v_p(i).
    # Product over p<i divides by i when i is composite, and by 1 otherwise.
    divisor = 1 if all(i % p for p in primes) else i
    log_divisor_lo = log_bounds(divisor)[0] if divisor > 1 else Decimal(0)
    bounds = []
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_CEILING
        e = c["fat_exponent_numerator"] - s * c["multiplicity"]
        if e > 0:
            bounds.append(
                (-log_divisor_lo - c["fat_constant_lo"]) * c["multiplicity"] / e
            )
        if i > 4 * s:
            bounds.append(4 * (-log_divisor_lo - c["orbit_constant_lo"]) / (i - 4 * s))
        if not bounds:
            raise ValueError(f"no numerical last row derived for i={i}")
        b = int((min(bounds) / log_bounds(10)[0]).to_integral_value(rounding=ROUND_CEILING))
    b = max(0, b)
    return 10**b, b


def prime_power_data(i: int, cap: int, primes: list[int]) -> list[tuple]:
    data = []
    for p in primes:
        powers = []
        q = p
        while q <= cap:
            residue = i % q
            if residue:
                powers.append((q, residue))
            q *= p
        data.append((p, log(p), log_bounds(p)[1], powers))
    return data


def valuation_upper_counts(left: int, right: int, data: list[tuple]) -> list[int]:
    """Upper bounds valid for every integer n in [left,right].

    v_p(C(n,i)) = sum_{a>=1} 1[n mod p**a < i mod p**a]. A summand can
    occur somewhere in the interval only if its left endpoint already meets
    the residue condition, or the interval crosses a multiple of p**a.
    """
    counts = []
    for _, _, _, powers in data:
        count = 0
        for q, residue in powers:
            if q > right:
                break
            if left // q < right // q or left % q < residue:
                count += 1
        counts.append(count)
    return counts


def certified_margin(i: int, left: int, counts: list[int], data: list[tuple], c: dict) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_CEILING
        upper = sum((e * item[2] for e, item in zip(counts, data)), Decimal(0))
    ln_left_lo = log_bounds(left)[0]
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_FLOOR
        fat = c["fat_exponent_numerator"] * ln_left_lo / c["multiplicity"] + c["fat_constant_lo"]
        orbit = i * ln_left_lo / 4 + c["orbit_constant_lo"]
        return max(fat, orbit) - upper


def check_index(i: int, all_primes: list[int], records: list[list[int]], max_nodes: int) -> dict:
    lower = min(start for gap, start in records if gap > i)
    primes = [p for p in all_primes if p < i]
    c = constants(i, lower)
    cap, cap_exponent = inclusive_row_cap(i, primes, c)
    data = prime_power_data(i, cap, primes)
    stack = [(lower, cap)] if lower <= cap else []
    visited = 0
    leaves = 0
    minimum = Decimal("Infinity")
    leaf_hash = hashlib.sha256()
    fat_exponent = c["fat_exponent_numerator"] / c["multiplicity"]
    fat_constant = float(c["fat_constant_lo"])
    orbit_constant = float(c["orbit_constant_lo"])
    while stack:
        left, right = stack.pop()
        visited += 1
        if visited > max_nodes:
            raise RuntimeError(f"node limit reached at i={i}; proof incomplete")
        counts = valuation_upper_counts(left, right, data)
        guide_upper = sum(e * item[1] for e, item in zip(counts, data))
        guide_lower = max(
            fat_exponent * log(left) + fat_constant,
            i / 4 * log(left) + orbit_constant,
        )
        if guide_lower > guide_upper:
            margin = certified_margin(i, left, counts, data, c)
            if margin > 0:
                minimum = min(minimum, margin)
                leaves += 1
                leaf_hash.update(f"{left}:{right}\n".encode())
                continue
        if left == right:
            raise RuntimeError(f"unexcluded row n={left} at i={i}; proof incomplete")
        middle = (left + right) // 2
        stack.extend([(left, middle), (middle + 1, right)])
    return {
        "i": i,
        "terminal_prime_lower_row": lower,
        "inclusive_cap_power_of_ten": cap_exponent,
        "visited_intervals": visited,
        "certified_intervals": leaves,
        "minimum_certified_log_margin": str(minimum) if leaves else None,
        "interval_partition_sha256": leaf_hash.hexdigest(),
        "conclusion": "no bad triples",
    }


def check_valuation_formula() -> int:
    """Check the interval upper bound against exact factorial valuations."""
    from erdos_699_effectivity import valuation_factorial

    comparisons = 0
    for i in range(3, 36):
        primes = primes_through(i - 1)
        data = prime_power_data(i, 160, primes)
        for left in range(2 * i, 150, 7):
            right = min(160, left + 10)
            counts = valuation_upper_counts(left, right, data)
            for p, bound in zip(primes, counts):
                for n in range(left, right + 1):
                    value = valuation_factorial(n, p) - valuation_factorial(i, p) - valuation_factorial(n - i, p)
                    assert value <= bound
                    comparisons += 1
    return comparisons


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-nodes", type=int, default=250_000)
    parser.add_argument("--indices", type=int, nargs="+")
    args = parser.parse_args()
    gap_data = json.loads(GAP_DATA.read_text())
    indices = args.indices or [29, *range(35, 906)]
    primes = primes_through(max(indices))
    results = []
    for i in indices:
        row = check_index(i, primes, gap_data["records"], args.max_nodes)
        results.append(row)
        if i < 60 or i % 100 == 0:
            print(f"i={i}: {row['certified_intervals']} intervals certified", file=sys.stderr, flush=True)
    margins = [Decimal(r["minimum_certified_log_margin"]) for r in results if r["certified_intervals"]]
    output = {
        "threshold": "p >= i",
        "precision": PRECISION,
        "checked_indices": indices,
        "small_prime_valuation_checks": check_valuation_formula(),
        "total_certified_intervals": sum(r["certified_intervals"] for r in results),
        "minimum_certified_log_margin": str(min(margins)) if margins else None,
        "gap_data_file": GAP_DATA.name,
        "prior_tail": "i>=906 is covered by erdos_699_i_ge_906.py and its retained proof",
        "conclusion": (
            "No bad triples for i=29 or i>=35."
            if indices == [29, *range(35, 906)]
            else "No bad triples at the checked indices; this was a partial run."
        ),
        "indices": results,
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
