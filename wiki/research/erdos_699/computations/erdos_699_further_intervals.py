"""Full interval exclusion using exact prime-pair bounds on finite ranges.

Uses the already established numerical tail caps, plus the separately
certified modular prime-power inequalities on every row below those caps.
No individual binomial rows are enumerated.
"""

from __future__ import annotations

import argparse
from bisect import bisect_right
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
import json
from math import comb, gcd
from pathlib import Path

import erdos_699_effective_intervals as base
from erdos_699_effectivity import primes_through
from erdos_699_weighted_ramps import minimal_vectors


CAPS = {13: 1046, 15: 15170264, 18: 700000, 19: 976, 21: 1732, 22: 957, 24: 976, 25: 957}
PAIR_SETS = {
    13: {(2, 3), (2, 5), (2, 7), (3, 5), (3, 7), (5, 7), (2, 11), (3, 11), (5, 11), (7, 11)},
    18: {(2, 3), (2, 5), (2, 7), (2, 11), (2, 13), (3, 5), (3, 7), (3, 11),
         (3, 13), (5, 7), (5, 11), (5, 13), (7, 11), (7, 13), (11, 13)},
    19: {(2, 17), (5, 17), (7, 17), (2, 3), (2, 5), (3, 5), (3, 7), (5, 7)},
    21: {(17, 19), (2, 17), (5, 17), (7, 17), (2, 3), (2, 5), (3, 5), (3, 7), (5, 7), (11, 13)},
    22: {(17, 19), (2, 17)},
    24: {(17, 19), (2, 17), (11, 23), (5, 17), (2, 3), (2, 5), (3, 5), (3, 7), (5, 7)},
    25: {(17, 19), (2, 17), (11, 23)},
}
PAIR_SETS[15] = PAIR_SETS[18]
PAIR_CERTIFICATE = Path(__file__).with_name("erdos_699_finite_prime_pairs.json")
ORIGINAL_PAIR_THRESHOLD = base.PAIR_THRESHOLD


def reduced_cap(i: int, primes: list[int], constants: dict, saving: int) -> tuple[int, int]:
    """Apply the finite pair inequality to the remaining bounded interval."""
    if i in (22, 25):
        return 10 ** CAPS[i], CAPS[i]
    gamma = Decimal(saving) / base.SCALE
    divisor = 1 if all(i % p for p in primes) else i
    divisor_log_lo = base.intervals.log_bounds(divisor)[0] if divisor > 1 else Decimal(0)
    with localcontext() as ctx:
        ctx.prec = base.intervals.PRECISION
        ctx.rounding = ROUND_CEILING
        upper_constant = gamma * base.intervals.log_bounds(2)[1] - divisor_log_lo
    bounds = []
    for numerator, denominator, lower_constant in [
        (constants["fat_exponent_numerator"], constants["multiplicity"], constants["fat_constant_lo"]),
        (i, 4, constants["orbit_constant_lo"]),
    ]:
        with localcontext() as ctx:
            ctx.prec = base.intervals.PRECISION
            ctx.rounding = ROUND_FLOOR
            gap_lo = Decimal(numerator) / denominator - len(primes) + gamma
        if gap_lo > 0:
            with localcontext() as ctx:
                ctx.prec = base.intervals.PRECISION
                ctx.rounding = ROUND_CEILING
                bounds.append((upper_constant - lower_constant) / gap_lo)
    assert bounds
    with localcontext() as ctx:
        ctx.prec = base.intervals.PRECISION
        ctx.rounding = ROUND_CEILING
        bound = max(min(bounds), base.intervals.log_bounds(base.PAIR_THRESHOLD)[1])
        exponent = int((bound / base.intervals.log_bounds(10)[0]).to_integral_value(rounding=ROUND_CEILING))
    assert exponent <= CAPS[i]
    return 10 ** exponent, exponent


def fast_valuation_upper_counts(left: int, right: int, data: list[tuple]) -> list[int]:
    """Skip the prefix of prime powers whose multiples every interval crosses."""
    counts = []
    width = right - left
    for _, _, _, powers, moduli in data:
        first = bisect_right(moduli, width)
        count = first
        last = bisect_right(moduli, right)
        for q, residue in powers[first:last]:
            if left // q < right // q or left % q < residue:
                count += 1
        counts.append(count)
    return counts


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--indices", type=int, nargs="+", default=[19, 22, 24, 25])
    parser.add_argument("--max-nodes", type=int, default=1_000_000)
    parser.add_argument("--pair-certificate", type=Path, default=PAIR_CERTIFICATE)
    parser.add_argument("--extra-pair-certificate", type=Path)
    parser.add_argument("--exact-singleton-limit", type=int, default=0)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_suffix(".json"))
    args = parser.parse_args()
    pair_data = json.loads(args.pair_certificate.read_text())["records"]
    if args.extra_pair_certificate:
        pair_data += json.loads(args.extra_pair_certificate.read_text())["records"]
    gap_records = json.loads(base.intervals.GAP_DATA.read_text())["records"]
    original_prime_power_data = base.intervals.prime_power_data

    def indexed_prime_power_data(i, cap, primes):
        return [(*record, [q for q, _ in record[3]])
                for record in original_prime_power_data(i, cap, primes)]

    base.intervals.prime_power_data = indexed_prime_power_data
    base.intervals.valuation_upper_counts = fast_valuation_upper_counts
    results = []
    for i in args.indices:
        primes = tuple(primes_through(i - 1))
        selected = [r for r in pair_data if tuple(r["pair"]) in PAIR_SETS[i]]
        assert {tuple(r["pair"]) for r in selected} == PAIR_SETS[i]
        base.PAIR_THRESHOLD = max(ORIGINAL_PAIR_THRESHOLD,
                                  max(r["height_threshold"] + i - 1 for r in selected))
        for row in selected:
            assert row["height_cap_power_of_ten"] >= CAPS[i]
            assert row["maximum_difference"] >= i - 1
            assert row["height_threshold"] + i - 1 <= base.PAIR_THRESHOLD
            assert row["reciprocal_exponent_denominator"] == 3
        edges = base.EXPLICIT_EDGES + tuple((*r["pair"], 3333) for r in selected)
        vectors = minimal_vectors(primes, edges)
        saving = min(map(sum, vectors))
        base.TABLE_PRIMES = primes
        base.pair_vectors = lambda: vectors
        base.inclusive_row_cap = lambda index, ps, c: reduced_cap(index, ps, c, saving)
        exact_columns = 0

        def singleton(n, index):
            nonlocal exact_columns
            if n > args.exact_singleton_limit:
                return False
            fixed = comb(n, index)
            current = 1
            for j in range(1, n // 2 + 1):
                current = current * (n - j + 1) // j
                if j <= index:
                    continue
                common = gcd(fixed, current)
                for p in primes:
                    while common % p == 0:
                        common //= p
                assert common > 1, f"Bad triple found: {(n, index, j)}"
                exact_columns += 1
            return True

        try:
            result = base.check_index_with_pairs(
                i, list(primes), gap_records, args.max_nodes,
                singleton_checker=singleton if args.exact_singleton_limit else None)
        except RuntimeError as error:
            result = {"i": i, "conclusion": "interval proof incomplete", "reason": str(error)}
        result["finite_prime_pairs"] = [r["pair"] for r in selected]
        result["original_numerical_cap_power_of_ten"] = CAPS[i]
        result["cofactor_saving_scaled"] = saving
        result["finite_pair_row_threshold"] = base.PAIR_THRESHOLD
        if args.exact_singleton_limit:
            result["exact_singleton_limit"] = args.exact_singleton_limit
            result["exact_columns_checked"] = exact_columns
        results.append(result)
        print(json.dumps(result), flush=True)
        output = {
            "scope": "Interval certificate, using a separate finite prime-power certificate; no row enumeration.",
            "finite_pair_certificate_file": args.pair_certificate.name,
            "gap_data_file": base.intervals.GAP_DATA.name,
            "maximum_nodes_per_index": args.max_nodes,
            "records": results,
        }
        if args.extra_pair_certificate:
            output["extra_finite_pair_certificate_file"] = args.extra_pair_certificate.name
        args.output.write_text(json.dumps(output, indent=2) + "\n")


if __name__ == "__main__":
    main()
