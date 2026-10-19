"""Moderate numerical tail bounds using the explicit asymmetric pair theorem."""

from fractions import Fraction
import json
from pathlib import Path

from erdos_699_prime_pair_savings import EXPLICIT_EDGES
from erdos_699_weighted_ramps import capacities, off_maximum_constant, exact_power_of_ten


PRIMES = (2, 3, 5, 7, 11, 13, 17, 19)
ROOT = Path(__file__).parent


def minimal_vectors(primes, edges):
    positions = {p: j for j, p in enumerate(primes)}
    vectors = [(0,) * len(primes)]
    used = []
    for p, q, left, right in edges:
        if p not in positions or q not in positions:
            continue
        p, q = positions[p], positions[q]
        used.append((p, q, left, right))
        candidates = set()
        for v in vectors:
            if v[p] >= left or v[q] >= right:
                candidates.add(v)
            else:
                for vertex, weight in ((p, left), (q, right)):
                    new = list(v)
                    new[vertex] = max(new[vertex], weight)
                    candidates.add(tuple(new))
        vectors = []
        for v in sorted(candidates, key=lambda v: (sum(v), v)):
            if not any(all(x <= y for x, y in zip(w, v)) for w in vectors):
                vectors.append(v)
        assert all(any(all(x <= y for x, y in zip(w, v)) for w in vectors)
                   for v in candidates)
    assert all(v[p] >= a or v[q] >= b for v in vectors for p, q, a, b in used)
    return vectors


def certificate(index, k, side_weights, extra_pairs, source_cap, extra_asymmetric=()):
    primes = tuple(p for p in PRIMES if p < index)
    edges = [(p, q, w, w) for p, q, w in EXPLICIT_EDGES]
    edges += [(5, 7, *side_weights)]
    edges += [(p, q, w, w) for p, q, w in extra_pairs]
    edges += list(extra_asymmetric)
    vectors = minimal_vectors(primes, edges)
    weights = [2*k - t for t in range(index)]
    degree = k*(k + 1)
    total = sum(weights)
    moment = sum(t*m for t, m in enumerate(weights))
    gains = [10000*(total - degree) - sum((2*k-r)*c for r, c in enumerate(caps))
             for v in vectors for caps in capacities(v)]
    gain = Fraction(min(gains), 10000)
    assert gain > 0
    off_maximum, factors = off_maximum_constant(index, weights, primes)
    rough_denominator = index if all(index % p for p in primes) else 1
    constant = Fraction(1000*rough_denominator**(2*k)*off_maximum, 999*2**degree)
    threshold = 1000*(moment + 2*k*len(primes)*(index-1))
    cap = exact_power_of_ten(constant, gain, threshold)
    return {
        "i": index, "k": k, "minimum_gain": str(gain),
        "minimal_vector_count": len(vectors),
        "capacity_configurations_checked": len(gains),
        "asymmetric_5_7_weights_scaled": side_weights,
        "extra_symmetric_pairs_scaled": extra_pairs,
        "extra_asymmetric_pairs_scaled": extra_asymmetric,
        "off_maximum_factors": factors,
        "comparison_constant": str(constant),
        "elementary_threshold": threshold,
        "algebraic_cap_power_of_ten": cap,
        "source_threshold_power_of_ten": source_cap,
        "full_row_cap_power_of_ten": max(cap, source_cap + 1),
    }


def main():
    source_path = ROOT / "erdos_699_bft_asymmetric.json"
    explicit_path = ROOT / "erdos_699_bft_explicit_thresholds.json"
    source = json.loads(source_path.read_text())["pairs"]
    explicit = json.loads(explicit_path.read_text())
    for weights, bound in (((2900, 2000), 913), ((3500, 2200), 1731), ((3500, 2000), 985)):
        assert any(row["pair"] == [5, 7]
                   and [Fraction(t) for t in row["targets"]] == [Fraction(w, 10000) for w in weights]
                   and row["threshold_power_of_ten"] <= bound for row in source)
    assert any(row["pair"] == [2, 7]
               and [Fraction(t) for t in row["targets"]] == [Fraction(24, 100), Fraction(29, 100)]
               and row["threshold_power_of_ten"] <= 497 for row in source)
    for p, q, w, bound in ((2, 17, 3259, 976), (17, 19, 1855, 957)):
        assert any(row["pair"] == [p, q] and Fraction(row["target"]) == Fraction(w, 10000)
                   and row["threshold_power_of_ten"] <= bound for row in explicit)
    records = [
        certificate(11, 7, (2900, 2000), (), 913),
        certificate(13, 8, (3500, 2000), (), 985, ((2, 7, 2400, 2900),)),
        certificate(16, 10, (2900, 2000), (), 913),
        certificate(21, 14, (3500, 2200), ((2, 17, 3259), (17, 19, 1855)), 1731),
    ]
    assert [r["minimum_gain"] for r in records] == ["13/125", "103/1000", "23/100", "831/1250"]
    assert [r["full_row_cap_power_of_ten"] for r in records] == [914, 1046, 914, 1732]
    result = {
        "scope": "Exact weighted proof inequalities; no binomial rows searched.",
        "source_file": source_path.name,
        "explicit_pair_source_file": explicit_path.name,
        "records": records,
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps([{k: r[k] for k in ("i", "minimum_gain", "algebraic_cap_power_of_ten",
                                        "full_row_cap_power_of_ten")} for r in records], indent=2))


if __name__ == "__main__":
    main()
