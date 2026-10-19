"""One conditional four-factor source bound relevant to index fourteen.

The certificate proves a cofactor disjunction at positions with equal
sums. It does not assert coverage of all index-fourteen configurations.
"""

import json
from pathlib import Path

from erdos_699_bft_dusart_gcd import gcd_exponent_lower
from erdos_699_bft_pair_extension import rational
from erdos_699_product_thresholds import product_bound


def main():
    gcd_certificate = gcd_exponent_lower(115, 94, m0=10**8)
    certificate = product_bound(
        (144, 143, 1, 1, 115, 94), rational(gcd_certificate["ell_lower"]),
        10**8, 100,
        [(2, 4, 1, 0, ".359"), (3, 2, 1, 0, ".492"),
         (11, 1, 1, 1, ".445"), (13, 1, 1, 1, ".407")],
        shift=13,
    )
    result = {
        "scope": "Conditional product estimate; no whole-index exclusion or effectivity claim.",
        "equal_position_sums": [[2, 3], [11, 13]],
        "require_distinct_unordered_position_pairs": True,
        "height_variable": "h=n-13",
        "gcd_certificate": gcd_certificate,
        **certificate,
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
