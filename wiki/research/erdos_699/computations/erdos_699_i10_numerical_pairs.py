"""Numerical BFT certificates for the weakened index-ten pair constraints.

Each certified asymmetric disjunction implies both the symmetric and
asymmetric effective constraints after lowering their endpoints by .001.
The exact finite prime-interval bootstrap supplies the smaller valid m0;
the analytic gcd tail is regenerated here. This records source thresholds,
not a row search or a full index-ten interpolation certificate.
"""

from fractions import Fraction
import json
from pathlib import Path

from erdos_699_bft_asymmetric import asymmetric_bound
from erdos_699_bft_asymmetric_pair_table import prime_base
from erdos_699_bft_dusart_gcd import gcd_exponent_lower
from erdos_699_bft_pair_extension import rational
from erdos_699_prime_pair_savings import EDGES


CHOICES = {
    (2, 3): (10**8, (".3286", ".2911")),
    (2, 5): (3*10**6, (".2669", ".2701")),
    (2, 7): (10**8, (".2747", ".3208")),
    (3, 5): (3*10**7, (".2552", ".3764")),
    (3, 7): (10**8, (".0495", ".3261")),
    (5, 7): (10**8, (".3921", ".2657")),
}


def main():
    directory = Path(__file__).parent
    source = json.loads((directory / "erdos_699_bft_asymmetric_pair_parameters.json").read_text())
    bootstrap_source = json.loads((directory / "erdos_699_bft_prime_bootstrap.json").read_text())
    bootstraps = {tuple(row["pair"]): row for row in bootstrap_source["records"]}
    rows = []
    symmetric = {(p, q): Fraction(weight - 10, 10000) for p, q, weight in EDGES}
    for original in source["effective_gcd_parameters"]:
        pair = tuple(original["pair"])
        if pair not in CHOICES:
            continue
        m0, targets = CHOICES[pair]
        by_prime = dict(zip(pair, targets))
        seed = original["seed"]
        p_base, q_base = prime_base(seed[0], pair), prime_base(seed[1], pair)
        gcd_bound = gcd_exponent_lower(seed[-2], seed[-1], m0=m0)
        bootstrap = bootstraps[pair]
        assert bootstrap["seed"] == seed
        assert Fraction(bootstrap["ell_lower"]) == Fraction(gcd_bound["ell_lower"])
        assert bootstrap["analytic_gcd_certificate"]["m0"] == m0
        smaller_m0 = bootstrap["finite_interval_start"]
        certificate = asymmetric_bound(
            *seed, rational(gcd_bound["ell_lower"]), smaller_m0, 100,
            by_prime[p_base], by_prime[q_base],
        )
        # These source bounds also subsume the weakened effective endpoints.
        assert all(Fraction(target) >= Fraction(weight - 10, 10000)
                   for target, weight in zip(targets, original["endpoints_scaled"]))
        assert all(Fraction(target) >= symmetric[pair] for target in targets)
        rows.append({
            "pair": list(pair), "targets_by_prime": by_prime,
            "analytic_gcd_certificate": gcd_bound,
            "bootstrap_certificate": {
                key: bootstrap[key] for key in (
                    "finite_interval_start", "finite_interval_end",
                    "certified_intervals", "partition_sha256",
                )
            },
            **certificate,
        })
    assert len(rows) == len(CHOICES)
    result = {
        "scope": "Analytic source thresholds; no binomial rows enumerated.",
        "bootstrap_source": "erdos_699_bft_prime_bootstrap.json",
        "height_variable": "Minimum of the two selected numerator factors",
        "choices": rows,
        "common_row_threshold_power_of_ten":
            1 + max(row["threshold_power_of_ten"] for row in rows),
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "thresholds": {str(row["pair"]): row["threshold_power_of_ten"] for row in rows},
        "common_row_threshold_power_of_ten": result["common_row_threshold_power_of_ten"],
        "output": str(output),
    }, indent=2))


if __name__ == "__main__":
    main()
