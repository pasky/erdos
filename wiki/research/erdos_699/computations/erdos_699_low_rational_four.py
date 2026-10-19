"""A numerical four-cofactor restriction from 225-224=1.

The factors have different unordered position pairs with equal position
sums. This certifies a conditional analytic bound; no binomial rows are
enumerated and no additional whole index is claimed.
"""

import json
from pathlib import Path

from erdos_699_bft_dusart_gcd import gcd_exponent_lower
from erdos_699_bft_pair_extension import rational
from erdos_699_rational_product_bounds import rational_product_bound


def main():
    gcd = gcd_exponent_lower(5, 3, m0=10**8)
    result = rational_product_bound(
        (225, 224, 1, 1, 5, 3), rational(gcd["ell_lower"]),
        10**8, 169,
        [(3, 2, 1, 0, ".35"), (5, 2, 1, 0, ".03"),
         (2, 5, 1, 1, ".35"), (7, 1, 1, 1, ".35")],
        degree=2, shift=13,
    )
    assert result is not None
    record = {
        "scope": "Conditional on r2+r7=r3+r5 and different unordered position pairs.",
        "source": "BFT Theorem 2.4 with rational residual products; Dusart coefficient-gcd bounds.",
        "equal_position_sums": [[2, 7], [3, 5]],
        "height_variable": "h=n-13",
        "gcd_certificate": gcd,
        **result,
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"output": str(output),
                      "threshold_power_of_ten": result["threshold_power_of_ten"]}))


if __name__ == "__main__":
    main()
