#!/usr/bin/env python3
"""Certify one conditional AP cofactor bound relevant to index fourteen.

The positions for primes5,2,13 must form a nonconstant arithmetic
progression. This does not assert coverage of all index14 cases.
"""

import json
from pathlib import Path

from erdos_699_bft_gcd_bounds import gcd_exponent_lower
from erdos_699_bft_pair_extension import rational
from erdos_699_product_thresholds import product_bound


def report():
    gcd_certificate = gcd_exponent_lower(13, 10, terms=4000, m0=10**8)
    certificate = product_bound(
        (65, 64, 1, 1, 13, 10), rational(gcd_certificate["ell_lower"]),
        10**8, 100,
        [(5, 1, 1, 0, ".535"), (13, 1, 1, 0, ".260"),
         (2, 6, 2, 1, ".400")],
        shift=13,
    )
    return {
        "scope": "Conditional AP bound; no whole-index effectivity or exclusion claim.",
        "middle_prime": 2,
        "endpoint_primes": [5, 13],
        "require_nonzero_step": True,
        "height_variable": "h=n-13",
        "targets": {"2": ".400", "5": ".535", "13": ".260"},
        "gcd_certificate": gcd_certificate,
        **certificate,
    }


if __name__ == "__main__":
    result = report()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
