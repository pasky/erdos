"""Complete exclusion at index 16, with certified tail and interval bounds."""

import argparse
from decimal import Decimal
import json
from pathlib import Path

import erdos_699_effective_intervals as base
from erdos_699_further_intervals import fast_valuation_upper_counts
from erdos_699_weighted_ramps import minimal_vectors


ROOT = Path(__file__).parent
PRIMES = (2, 3, 5, 7, 11, 13)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-nodes", type=int, default=1_000_000)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_suffix(".json"))
    args = parser.parse_args()
    pair_path = ROOT / "erdos_699_finite_prime_pairs_16.json"
    tail_path = ROOT / "erdos_699_asymmetric_ramp_caps.json"
    rows = json.loads(pair_path.read_text())["records"]
    tail = next(r for r in json.loads(tail_path.read_text())["records"] if r["i"] == 16)
    initial_cap = tail["full_row_cap_power_of_ten"]
    assert initial_cap == 914
    assert {tuple(r["pair"]) for r in rows} == {
        (2, 3), (2, 5), (3, 5), (3, 7), (5, 7), (7, 13), (11, 13)}
    assert all(r["height_cap_power_of_ten"] >= initial_cap
               and r["maximum_difference"] >= 15
               and r["reciprocal_exponent_denominator"] == 3 for r in rows)
    vectors = minimal_vectors(
        PRIMES, base.EXPLICIT_EDGES + tuple((*r["pair"], 3333) for r in rows))
    assert len(vectors) == 13 and min(map(sum, vectors)) == 12589
    base.TABLE_PRIMES = PRIMES
    base.pair_vectors = lambda: vectors
    base.PAIR_THRESHOLD = max(1_771_595, max(r["height_threshold"] + 15 for r in rows))
    base.PAIR_SAVING = Decimal("1.2589")
    base.ELIGIBLE = [16]
    gaps = json.loads(base.intervals.GAP_DATA.read_text())["records"]
    lower = min(start for gap, start in gaps if gap > 16)
    _, reduced_cap = base.inclusive_row_cap(
        16, list(PRIMES), base.intervals.constants(16, lower))
    assert reduced_cap == 41 and reduced_cap <= initial_cap
    original = base.intervals.prime_power_data
    base.intervals.prime_power_data = lambda i, cap, primes: [
        (*r, [q for q, _ in r[3]]) for r in original(i, cap, primes)]
    base.intervals.valuation_upper_counts = fast_valuation_upper_counts
    result = base.check_index_with_pairs(16, list(PRIMES), gaps, args.max_nodes)
    result.update({
        "initial_numerical_tail_power_of_ten": initial_cap,
        "finite_pair_sum": "1.2589",
        "finite_pair_threshold": base.PAIR_THRESHOLD,
        "finite_pair_certificate_file": pair_path.name,
        "analytic_tail_certificate_file": tail_path.name,
        "gap_data_file": base.intervals.GAP_DATA.name,
        "scope": "Complete index-16 exclusion by analytic tail and certified intervals.",
    })
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
