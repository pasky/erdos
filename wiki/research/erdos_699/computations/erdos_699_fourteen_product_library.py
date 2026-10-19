"""Directed numerical certificates for nine additional index-14 product bounds.

Each bound is conditional on its equal-sum position partition. This module
makes no claim that the bounds cover every index-14 configuration.
"""

from fractions import Fraction
import json
from pathlib import Path
from math import prod

from erdos_699_bft_gcd_bounds import gcd_exponent_lower
from erdos_699_bft_pair_extension import rational
from erdos_699_product_thresholds import product_bound

CHOICES = [{'position_partition': [[2, 5], [3, 13]], 'seed': [40, 39, 1, 1, 13, 10], 'powers': {'2': 3, '3': 1, '5': 1, '13': 1}, 'targets': {'2': '0.3139', '3': '0.6365', '5': '0.4685', '13': '0.1542'}}, {'position_partition': [[2, 11], [3, 13]], 'seed': [352, 351, 1, 1, 6, 5], 'powers': {'2': 5, '3': 3, '11': 1, '13': 1}, 'targets': {'2': '0.3325', '3': '0.3651', '11': '0.5376', '13': '0.5055'}}, {'position_partition': [[3, 13], [7, 11]], 'seed': [39, 77, 2, 1, 16, 11], 'powers': {'3': 1, '7': 1, '11': 1, '13': 1}, 'targets': {'3': '0.6399', '7': '0.3638', '11': '0.2165', '13': '0.1621'}}, {'position_partition': [[2, 11], [5, 13]], 'seed': [4225, 704, 1, 6, 10, 7], 'powers': {'2': 6, '5': 2, '11': 1, '13': 2}, 'targets': {'2': '0.2989', '5': '0.4569', '11': '0.5949', '13': '0.1356'}}, {'position_partition': [[2, 13], [5, 7]], 'seed': [35, 104, 3, 1, 11, 7], 'powers': {'2': 3, '5': 1, '7': 1, '13': 1}, 'targets': {'2': '0.2982', '5': '0.4564', '7': '0.3431', '13': '0.1348'}}, {'position_partition': [[2, 13], [3, 5]], 'seed': [676, 675, 1, 1, 13, 11], 'powers': {'2': 2, '3': 3, '5': 2, '13': 2}, 'targets': {'2': '0.7611', '3': '0.4349', '5': '0.4481', '13': '0.1216'}}, {'position_partition': [[2, 11], [7, 13]], 'seed': [91, 88, 1, 1, 5, 4], 'powers': {'2': 3, '7': 1, '11': 1, '13': 1}, 'targets': {'2': '0.2998', '7': '0.3447', '11': '0.1929', '13': '0.1369'}}, {'position_partition': [[3, 11], [5, 13]], 'seed': [33, 65, 2, 1, 3, 2], 'powers': {'3': 1, '5': 1, '11': 1, '13': 1}, 'targets': {'3': '0.6172', '5': '0.4402', '11': '0.167', '13': '0.1091'}}, {'position_partition': [[2, 11], [5, 7]], 'seed': [176, 175, 1, 1, 11, 9], 'powers': {'2': 4, '5': 2, '7': 1, '11': 1}, 'targets': {'2': '0.3841', '5': '0.2853', '7': '0.5671', '11': '0.4671'}}]


def report():
    records = []
    for choice in CHOICES:
        seed = tuple(choice["seed"])
        powers = {int(p): k for p, k in choice["powers"].items()}
        components = []
        for group in choice["position_partition"]:
            base = prod(p**powers[p] for p in group)
            side = seed[:2].index(base)
            for p in group:
                components.append((p, powers[p], 1, side, Fraction(choice["targets"][str(p)])))
        gcd_certificate = gcd_exponent_lower(seed[4], seed[5], terms=4000, m0=10**8)
        bound = product_bound(seed, rational(gcd_certificate["ell_lower"]), 10**8,
                              169, components, degree=2, shift=13)
        records.append({**choice, "gcd_certificate": gcd_certificate, "bound": bound})
    return {
        "scope": "Conditional cofactor sources; no full-index effectivity assertion.",
        "height_variable": "h=n-13",
        "hypothesis": "The two unordered position pairs are different and have equal sums.",
        "records": records,
        "uniform_threshold_power_of_ten": max(r["bound"]["threshold_power_of_ten"] for r in records),
    }


if __name__ == "__main__":
    result = report()
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(result, indent=2, default=str) + "\n")
    print(json.dumps({"sources": len(result["records"]),
                      "uniform_threshold_power_of_ten": result["uniform_threshold_power_of_ten"],
                      "output": str(path)}, indent=2))
