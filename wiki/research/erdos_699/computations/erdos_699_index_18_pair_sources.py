"""Fully numerical cofactor sources used by the index-18 interpolation proof.

Every chosen L1,m0 is a published BFT Proposition 5.1 entry. The asymmetric
threshold formula is evaluated with directed intervals. This verifies fixed
analytic parameters, not binomial rows or prime-power exponent ranges.
"""

from fractions import Fraction
import json
from pathlib import Path

from mpmath import iv

from erdos_699_bft_asymmetric import asymmetric_bound
from erdos_699_bft_asymmetric_pair_table import PUBLISHED_GCD, prime_base
from erdos_699_bft_pair_extension import rational


INPUT = Path(__file__).with_name("erdos_699_index_18_pair_parameters.json")


def report():
    parameters = json.loads(INPUT.read_text())
    assert parameters["gap"] == 17
    assert parameters["target_input_cap_power_of_ten"] == 1732
    rows = []
    for row in parameters["pairs"]:
        p, q = row["pair"]
        assert p < q < 18
        P, Q, a, b, c, d = row["seed"]
        assert (row["L1"], row["m0"]) == PUBLISHED_GCD[c, d]
        target_map = dict(zip(row["pair"],
                              (Fraction(v, 10000) for v in row["endpoints_scaled"])))
        target_p = target_map[prime_base(P, row["pair"])]
        target_q = target_map[prime_base(Q, row["pair"])]
        source = asymmetric_bound(P, Q, a, b, c, d,
                                  iv.log(rational(row["L1"])), row["m0"],
                                  parameters["gap"], target_p, target_q)
        assert source["threshold_power_of_ten"] <= 1732
        rows.append({**row, **source})
    assert len(rows) == 17
    common = max(row["threshold_power_of_ten"] for row in rows)
    assert common == 1732
    # n >= 10**1733 implies every selected input n-r, r<=17, exceeds
    # 10**1732, with room to spare. The old BFT explicit table also applies.
    assert 10**1733 - 17 > 10**1732
    return {
        "source": "BFT Proposition 5.1 and the verified Section 7 asymmetric refinement",
        "scope": "Fixed numerical analytic sources; no binomial rows enumerated.",
        "parameter_file": INPUT.name,
        "weight_denominator": 10000,
        "gap": 17,
        "pairs": rows,
        "asymmetric_edges_scaled": [row["pair"] + row["endpoints_scaled"] for row in rows],
        "common_input_threshold_power_of_ten": common,
        "common_row_threshold_power_of_ten": common + 1,
    }


if __name__ == "__main__":
    result = report()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "verified_sources": len(result["pairs"]),
        "common_input_threshold_power_of_ten": result["common_input_threshold_power_of_ten"],
        "common_row_threshold_power_of_ten": result["common_row_threshold_power_of_ten"],
    }, indent=2))
