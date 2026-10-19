#!/usr/bin/env python3
"""Numerical asymmetric source certificates used by the i=15 and i=20 tails.

Each GCD lower bound holds uniformly for every m>=100000. No binomial
rows, columns, or source-parameter m values are enumerated.
"""

from fractions import Fraction
import json
from pathlib import Path

from erdos_699_bft_asymmetric import asymmetric_bound
from erdos_699_bft_gcd_bounds import gcd_exponent_lower
from erdos_699_bft_pair_extension import rational


# Sorted pair, oriented seed, sorted endpoint numerators, certified log10 cap.
PARAMETERS = (
    ((2, 5), (128, 125, 1, 1, 53, 43), (2638, 2674), 15170263),
    ((3, 11), (243, 121, 1, 2, 34, 25), (3414, 4249), 12315735),
    ((5, 7), (25, 49, 2, 1, 74, 49), (3869, 2589), 16877043),
    ((5, 11), (125, 121, 1, 1, 53, 43), (2051, 2105), 13982107),
    ((11, 13), (13, 11, 1, 1, 69, 49), (1260, 652), 8222386),
    ((2, 17), (17, 16, 1, 1, 67, 49), (3643, 3505), 12692980),
    ((17, 19), (289, 361, 5, 4, 83, 44), (2442, 2146), 27027658),
)


def is_power(value, prime):
    while value % prime == 0:
        value //= prime
    return value == 1


def report():
    rows = []
    for pair, seed, endpoints, cap in PARAMETERS:
        gcd_bound = gcd_exponent_lower(seed[-2], seed[-1], terms=4000, m0=100000)
        targets = [Fraction(value, 10000) for value in endpoints]
        if not is_power(seed[0], pair[0]):
            assert is_power(seed[0], pair[1])
            targets.reverse()
        threshold = asymmetric_bound(*seed, rational(Fraction(gcd_bound["ell_lower"])),
                                     100000, 100, *targets)
        assert threshold["threshold_power_of_ten"] <= cap
        rows.append({
            "pair": list(pair), "seed": list(seed),
            "edge": list(pair + endpoints), "gcd_bound": gcd_bound,
            "threshold": threshold,
            "source": "BFT Section7 asymmetric inequality with Lemmas5.2/5.4 GCD estimate",
        })
    return rows


if __name__ == "__main__":
    rows = report()
    Path(__file__).with_suffix(".json").write_text(json.dumps(rows, indent=2) + "\n")
    print(json.dumps([{ "edge": row["edge"],
                        "threshold_power_of_ten": row["threshold"]["threshold_power_of_ten"]}
                     for row in rows], indent=2))
