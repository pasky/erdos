#!/usr/bin/env python3
"""Exact position-dependent interpolation certificates for Erdos 699, i=10.

The finite calculations concern cofactor witnesses, small-prime positions,
and polynomial jets. They do not enumerate binomial rows or columns.
The default run recomputes every modular rank; --arithmetic-only checks
the rational inequalities and complete coverage without repeating ranks.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product
import json
from math import comb
from pathlib import Path

import erdos_699_index_13_interpolation_gcd as interpolation


HERE = Path(__file__).resolve().parent
DATA = HERE / "erdos_699_index_10_effective.json"
PRIMES = (2, 3, 5, 7)
SCALE = 10000


def minimal_vectors(edges):
    positions = {p: k for k, p in enumerate(PRIMES)}
    vectors = [(0,) * 4]
    for p, q, a, b in edges:
        left, right = positions[p], positions[q]
        extended = set()
        for v in vectors:
            if v[left] >= a or v[right] >= b:
                extended.add(v)
            else:
                for k, value in ((left, a), (right, b)):
                    w = list(v)
                    w[k] = value
                    extended.add(tuple(w))
        vectors = []
        for v in sorted(extended, key=lambda v: (sum(v), v)):
            if not any(all(a <= b for a, b in zip(old, v)) for old in vectors):
                vectors.append(v)
    return vectors


def coefficient_bound(record):
    h, m = record["line_exponents"], record["row_multiplicities"]
    r, d = record["symmetric_jet_count"], record["interpolation_degree"]
    assert r < 100000 and max(h + m) < 1000 and d < 1000
    if r:
        assert 28 * r < 10**7
    # Entries of the jet matrix are at most 2*10^d. Adjugates give
    # C <= r! (2*10^d)^r < 10^(r(d+6)); the generator factor is <10^7.
    # ||H|| <= 10^(2 sum h), and (9!)^max(m) < 10^(6 max(m)).
    return r * (max(0, d) + 6) + 2 * sum(h) + 6 * max(m) + 9


def degree(record):
    return 2 * sum(record["line_exponents"]) + max(
        0, record["interpolation_degree"] + 1)


def gain_scaled(record, positions, vector):
    """All coincidences use the product bound for their whole prime group."""
    m = record["row_multiplicities"]
    groups = {}
    for k, position in enumerate(positions):
        groups.setdefault(position, []).append(k)
    loss = 0
    for position, members in groups.items():
        capacity = SCALE if len(members) > 1 else SCALE - vector[members[0]]
        loss += m[position] * capacity
    return SCALE * (sum(m) - degree(record)) - loss


def check_record(record, ranks):
    h, m = record["line_exponents"], record["row_multiplicities"]
    d, expected_rank = record["interpolation_degree"], record["symmetric_jet_count"]
    assert len(h) == len(m) == 10
    assert all(type(x) is int and x >= 0 for x in h + m)
    interpolation.LINE_EXPONENTS = h
    interpolation.ROW_MULTIPLICITIES = m
    interpolation.DEGREE = d
    interpolation.PRIME = record["modular_prime"]
    jets = interpolation.symmetric_jets()
    assert len(jets) == expected_rank
    if expected_rank:
        basis = interpolation.symmetric_basis()
        assert len(basis) == record["symmetric_monomial_count"]
        assert expected_rank <= len(basis)
        if ranks:
            print(f"Rank {record['name']}: {len(jets)} x {len(basis)}", flush=True)
            assert interpolation.jet_matrix(basis, jets).rank() == len(jets)
    else:
        assert d == -1 and record["symmetric_monomial_count"] == 0
    assert coefficient_bound(record) == record["constant_power_of_ten"]
    assert 1000 * (sum(t*w for t, w in enumerate(m)) + 36*max(m)) < 10**10


def check_sources(data):
    """Compare the exact edges and conditional targets with retained sources."""
    from erdos_699_weighted_ramps import EDGES
    from erdos_699_bft_more_pairs import NEW_EDGES

    available = []
    for p, q, w in EDGES + NEW_EDGES:
        if p in PRIMES and q in PRIMES:
            available.append((p, q, w, w))
    pairs = json.loads((HERE / "erdos_699_bft_asymmetric_pair_table.json").read_text())
    for key in ("published_gcd_pairs", "effective_gcd_pairs"):
        for row in pairs[key]:
            p, q = row["pair"]
            if p in PRIMES and q in PRIMES:
                assert row["verified"]
                available.append((p, q, *row["endpoints_scaled"]))
    for p, q, a, b in data["pair_edges_scaled"]:
        assert any(p == u and q == v and a <= x and b <= y
                   for u, v, x, y in available)

    source = json.loads((HERE / "erdos_699_ap_cofactors.json").read_text())
    for rule in data["conditional_rules"].values():
        targets = {p: Fraction(v, SCALE) for p, v in rule["targets_scaled"].items()}
        if rule["kind"] == "ap":
            matches = [row for row in source["choices"]
                       if row["middle_prime"] == rule["middle_prime"]
                       and set(row["targets"]) == set(targets)]
        else:
            matches = [row for row in source["four_factor_choices"]
                       if row["equal_position_sums"] == rule["equal_position_sums"]]
        assert any(all(Fraction(row["targets"][p]) >= value
                       for p, value in targets.items()) for row in matches)

    numerical_pairs = json.loads((HERE / "erdos_699_i10_numerical_pairs.json").read_text())
    for p, q, a, b in data["pair_edges_scaled"]:
        rows = [row for row in numerical_pairs["choices"] if row["pair"] == [p, q]]
        assert len(rows) == 1
        targets = rows[0]["targets_by_prime"]
        assert Fraction(targets[str(p)]) >= Fraction(a, SCALE)
        assert Fraction(targets[str(q)]) >= Fraction(b, SCALE)
    numerical_products = json.loads((HERE / "erdos_699_product_thresholds.json").read_text())
    rule_names = {
        "equal_pairs": "balanced_2357",
        "middle3_27": "ap_237_middle_3",
        "middle3_57": "ap_357_middle_3",
        "middle2_37": "ap_237_middle_2",
        "middle7_23": "ap_237_middle_7",
    }
    for key, rule in data["conditional_rules"].items():
        rows = [row for row in numerical_products["choices"] if row["name"] == rule_names[key]]
        assert len(rows) == 1
        targets = {str(component[0]): Fraction(component[-1])
                   for component in rows[0]["components"]}
        assert all(targets[p] >= Fraction(value, SCALE)
                   for p, value in rule["targets_scaled"].items())
    source_cap = max(numerical_pairs["common_row_threshold_power_of_ten"],
                     numerical_products["common_row_threshold_power_of_ten"])
    assert source_cap == data["source_row_threshold_power_of_ten"]
    assert source_cap < data["algebraic_power_of_ten"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--arithmetic-only", action="store_true")
    args = parser.parse_args()
    data = json.loads(DATA.read_text())
    check_sources(data)
    vectors = minimal_vectors(data["pair_edges_scaled"])
    assert [list(v) for v in vectors] == data["minimal_vectors_scaled"]
    critical = tuple(data["critical_vector_scaled"])
    records = {r["name"]: r for r in data["certificates"]}
    assert len(records) == len(data["certificates"])
    for record in records.values():
        check_record(record, ranks=not args.arithmetic_only)

    cap = data["algebraic_power_of_ten"]
    checked = branches = 0
    used = set()
    minima = {}

    def check(name, positions, vector):
        nonlocal branches
        record = records[name]
        gain = gain_scaled(record, positions, vector)
        assert gain > 0, (name, positions, vector, gain)
        assert cap * gain > SCALE * coefficient_bound(record)
        minima[name] = min(minima.get(name, gain), gain)
        used.add(name)
        branches += 1

    for positions in product(range(10), repeat=4):
        for source_vector in vectors:
            checked += 1
            vector = (critical if all(a <= b for a, b in zip(critical, source_vector))
                      else source_vector)
            if len(set(positions)) < 4:
                check("collisions", positions, vector)
            elif set(positions) != {0, 1, 2, 3}:
                check("num_outside", positions, vector)
            elif vector != critical:
                check("num_others", positions, vector)
            else:
                key = "".join(map(str, positions))
                if key not in data["exceptional_position_rules"]:
                    check("num_pos_" + key, positions, vector)
                    continue
                rule = data["conditional_rules"][data["exceptional_position_rules"][key]]
                at = dict(zip(PRIMES, positions))
                if rule["kind"] == "ap":
                    middle = rule["middle_prime"]
                    endpoints = [int(p) for p in rule["targets_scaled"] if int(p) != middle]
                    assert sum(at[p] for p in endpoints) == 2 * at[middle]
                else:
                    left, right = rule["equal_position_sums"]
                    assert sum(at[p] for p in left) == sum(at[p] for p in right)
                for p, value in rule["targets_scaled"].items():
                    k = PRIMES.index(int(p))
                    augmented = list(vector)
                    augmented[k] = max(augmented[k], value)
                    check(f"num_extra_{key}_{k}", positions, augmented)

    assert used == set(records), set(records) - used
    for name, gain in minima.items():
        assert Fraction(gain, SCALE) == Fraction(records[name]["minimum_gain"])
    print(json.dumps({
        "index": 10,
        "minimal_vectors": len(vectors),
        "position_vector_cases": checked,
        "certificate_applications": branches,
        "certificate_count": len(records),
        "ranks_checked": not args.arithmetic_only,
        "largest_jet_matrix": max(r["symmetric_jet_count"] for r in records.values()),
        "algebraic_power_of_ten": cap,
        "source_row_threshold_power_of_ten": data["source_row_threshold_power_of_ten"],
        "conclusion": "Every bad row at index 10 is below 10^15000000",
    }, indent=2))


if __name__ == "__main__":
    main()
