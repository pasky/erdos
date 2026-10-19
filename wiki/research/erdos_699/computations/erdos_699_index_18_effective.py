"""Exact whole-index effectivity certificate for Erdős 699 at i=18.

This checks every minimal cofactor vector and every collision capacity
list, plus the final integer-power inequality. It does not enumerate rows.
The two asymmetric source thresholds are recomputed with interval arithmetic;
the symmetric pair sources retain an effectively computable threshold X_18.
"""

from fractions import Fraction
import json
from pathlib import Path

from erdos_699_bft_asymmetric_pair_table import check_row
from erdos_699_bft_more_pairs import EDGES, NEW_EDGES, SCALE
from erdos_699_weighted_ramps import (
    capacities, exact_power_of_ten, off_maximum_constant,
)


INDEX, K = 18, 12
PRIMES = (2, 3, 5, 7, 11, 13, 17)
ASYMMETRIC_EDGES = ((5, 7, 3613, 2277), (7, 13, 987, 2080))


def minimal_vectors(edges):
    positions = {p: j for j, p in enumerate(PRIMES)}
    vectors = [(0,) * len(PRIMES)]
    used = []
    for p, q, wp, wq in edges:
        a, b = positions[p], positions[q]
        used.append((a, b, wp, wq))
        extensions = set()
        for vector in vectors:
            if vector[a] >= wp or vector[b] >= wq:
                extensions.add(vector)
            else:
                for vertex, weight in ((a, wp), (b, wq)):
                    new = list(vector)
                    new[vertex] = weight
                    extensions.add(tuple(new))
        vectors = []
        for vector in sorted(extensions, key=lambda v: (sum(v), v)):
            if not any(all(a <= b for a, b in zip(old, vector))
                       for old in vectors):
                vectors.append(vector)
        assert all(any(all(a <= b for a, b in zip(old, vector))
                       for old in vectors) for vector in extensions)
        assert all(v[a] >= wp or v[b] >= wq
                   for v in vectors for a, b, wp, wq in used)
    assert all(0 <= entry < SCALE // 2 for v in vectors for entry in v)
    return vectors


def report():
    symmetric_edges = tuple((p, q, w, w) for p, q, w in EDGES + NEW_EDGES
                            if p in PRIMES and q in PRIMES)
    edges = symmetric_edges + ASYMMETRIC_EDGES
    vectors = minimal_vectors(edges)
    assert len(vectors) == 65
    weights = tuple(2*K - t for t in range(INDEX))
    degree, total = K*(K + 1), sum(weights)
    moment = sum(t*w for t, w in enumerate(weights))
    worst = None
    configurations = 0
    for vector in vectors:
        for caps in capacities(vector):
            configurations += 1
            gain_scaled = SCALE*(total - degree) - sum(
                weights[r]*capacity for r, capacity in enumerate(caps))
            item = gain_scaled, vector, caps
            if worst is None or item < worst:
                worst = item
    gain_scaled, worst_vector, worst_capacities = worst
    gain = Fraction(gain_scaled, SCALE)
    assert gain == Fraction(186, 625)

    off_maximum, factors = off_maximum_constant(INDEX, weights, PRIMES)
    assert [(row["prime"], row["exponent"]) for row in factors] == [
        (2, 272), (3, 108), (5, 57), (7, 41), (11, 24), (13, 24), (17, 24),
    ]
    constant = Fraction(1000*off_maximum, 999*2**degree)
    elementary_threshold = 1000*(moment + 2*K*len(PRIMES)*(INDEX - 1))
    assert elementary_threshold == 4_743_000
    algebraic_cap = exact_power_of_ten(constant, gain, elementary_threshold)
    assert algebraic_cap == 814

    parameter_path = Path(__file__).with_name("erdos_699_bft_asymmetric_pair_parameters.json")
    source_parameters = json.loads(parameter_path.read_text())["published_gcd_parameters"]
    source_rows = []
    for p, q, wp, wq in ASYMMETRIC_EDGES:
        row = next(row for row in source_parameters
                   if row["pair"] == [p, q] and row["endpoints_scaled"] == [wp, wq])
        checked = check_row(row, published=True)
        source_rows.append({
            "pair": [p, q], "endpoints_scaled": [wp, wq],
            "seed": row["seed"], "L1": row["L1"], "m0": row["m0"],
            "threshold_power_of_ten": checked["numerical_threshold"]["threshold_power_of_ten"],
        })
    assert [row["threshold_power_of_ten"] for row in source_rows] == [2_405_782, 484_367]
    return {
        "scope": "Whole-index effective bound; finite exponent and collision verification, no row search.",
        "i": INDEX, "k": K, "primes": list(PRIMES), "weight_denominator": SCALE,
        "edges_scaled": [list(edge) for edge in edges],
        "minimal_vector_count": len(vectors),
        "minimal_vectors_scaled": [list(v) for v in vectors],
        "collision_capacity_lists_checked": configurations,
        "row_weights": list(weights), "degree": degree,
        "total_multiplicity": total, "weighted_moment": moment,
        "minimum_gain": str(gain),
        "worst_vector_scaled": list(worst_vector),
        "worst_capacities_scaled": list(worst_capacities),
        "off_maximum_factors": factors,
        "algebraic_constant": str(constant),
        "elementary_threshold": elementary_threshold,
        "algebraic_cap_power_of_ten": algebraic_cap,
        "asymmetric_sources": source_rows,
        "asymmetric_parameter_file": parameter_path.name,
        "X_18_definition": (
            "Maximum of the effective bounded-gap thresholds, with D=17, for the "
            "symmetric edges used here from BFT Corollary 2.3 and the verified new-pair table."
        ),
        "full_exclusive_bound": "max(10^814, X_18 + 17, 10^2405782 + 17, 10^484367 + 17)",
        "simplified_full_exclusive_bound": "max(X_18, 10^2405782) + 17",
    }


if __name__ == "__main__":
    result = report()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in (
        "i", "minimal_vector_count", "collision_capacity_lists_checked", "minimum_gain",
        "algebraic_cap_power_of_ten", "full_exclusive_bound",
    )}, indent=2))
