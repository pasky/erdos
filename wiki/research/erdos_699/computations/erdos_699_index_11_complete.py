"""Complete index eleven using a numerical tail and finite pair certificates.

The pair certificate covers heights through 10^914. Its stronger exponents
shrink the remaining possible row bound to 10^19. Interval inequalities
cover that range, with direct exact binomial gcd checks at any unresolved
singleton at most 2000. No larger singleton is silently accepted.
"""

from __future__ import annotations

import argparse
from decimal import Decimal
import json
from math import comb, gcd
from pathlib import Path

import erdos_699_effective_intervals as base
from erdos_699_further_intervals import fast_valuation_upper_counts
from erdos_699_weighted_ramps import minimal_vectors


PAIR_PATH = Path(__file__).with_name("erdos_699_finite_prime_pairs_small.json")
PRIMES = (2, 3, 5, 7)
INITIAL_CAP = 914


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-nodes", type=int, default=300_000)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_suffix(".json"))
    args = parser.parse_args()
    rows = json.loads(PAIR_PATH.read_text())["records"]
    assert {tuple(r["pair"]) for r in rows} == {
        (2, 3), (2, 5), (2, 7), (3, 5), (3, 7), (5, 7)}
    assert all(r["height_cap_power_of_ten"] >= INITIAL_CAP
               and r["maximum_difference"] >= 10
               and r["reciprocal_exponent_denominator"] == 3 for r in rows)
    vectors = minimal_vectors(
        PRIMES, base.EXPLICIT_EDGES + tuple((*r["pair"], 3333) for r in rows))
    assert len(vectors) == 4 and min(map(sum, vectors)) == 9999
    base.TABLE_PRIMES = PRIMES
    base.pair_vectors = lambda: vectors
    base.PAIR_THRESHOLD = max(r["height_threshold"] + 10 for r in rows)
    base.PAIR_SAVING = Decimal(".9999")
    base.ELIGIBLE = [11]
    gaps = json.loads(base.intervals.GAP_DATA.read_text())["records"]
    lower = min(start for gap, start in gaps if gap > 11)
    c = base.intervals.constants(11, lower)
    _, exponent = base.inclusive_row_cap(11, list(PRIMES), c)
    assert exponent == 19 and exponent <= INITIAL_CAP

    original_data = base.intervals.prime_power_data
    base.intervals.prime_power_data = lambda i, cap, primes: [
        (*row, [q for q, _ in row[3]]) for row in original_data(i, cap, primes)]
    base.intervals.valuation_upper_counts = fast_valuation_upper_counts
    exact_columns = 0

    def singleton(n, i):
        nonlocal exact_columns
        if n > 2000:
            return False
        fixed = comb(n, i)
        current = 1
        for j in range(1, n // 2 + 1):
            current = current * (n - j + 1) // j
            if j <= i:
                continue
            common = gcd(fixed, current)
            for p in PRIMES:
                while common % p == 0:
                    common //= p
            assert common > 1, f"Bad triple found: {(n, i, j)}"
            exact_columns += 1
        return True

    result = base.check_index_with_pairs(
        11, list(PRIMES), gaps, args.max_nodes, singleton_checker=singleton)
    result.update({
        "initial_numerical_tail_power_of_ten": INITIAL_CAP,
        "finite_pair_threshold": base.PAIR_THRESHOLD,
        "finite_pair_sum": ".9999",
        "exact_columns_checked": exact_columns,
        "finite_pair_certificate_file": PAIR_PATH.name,
        "gap_data_file": base.intervals.GAP_DATA.name,
        "scope": "Full index-11 exclusion: analytic tail, intervals and exact small-row gcd checks.",
    })
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
