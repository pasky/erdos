"""Numerical thresholds for bounded-gap products of nearby linear factors.

This extends the direct asymmetric BFT threshold to three or more matched
prime exponents. Every product has the same degree. The seed components
record prime powers and how often each associated linear factor occurs.
"""

from fractions import Fraction
import json
from math import prod
from pathlib import Path

from mpmath import iv

from erdos_699_bft_explicit_thresholds import explicit_bound, interval_max
from erdos_699_bft_pair_extension import rational
from erdos_699_bft_gcd_bounds import gcd_exponent_lower
from erdos_699_bft_dusart_gcd import gcd_exponent_lower as dusart_gcd_exponent_lower


iv.dps = 80


def product_bound(seed, log_l1, m0, gap, components, degree=2, shift=9):
    """Return a directed certificate for a disjunction of cofactor bounds.

    components consists of (prime, seed exponent, factor multiplicity,
    side, target), where side is 0 or 1. Its prime powers multiply to the
    corresponding seed power, and multiplicities on either side sum to
    degree. The original factors lie between h and h+shift, and their two
    products must have a nonzero difference of absolute value at most gap.
    The conclusion
    is that at least one cofactor exceeds h**target once h >= 10**B.
    """
    p_power, q_power, a, b, c, d = seed
    assert degree >= 1 and shift >= 1
    assert len({row[0] for row in components}) == len(components)
    for side, expected in ((0, p_power), (1, q_power)):
        assert prod(prime**exponent for prime, exponent, _, which, _ in components
                    if which == side) == expected
        assert sum(multiplicity for _, _, multiplicity, which, _ in components
                   if which == side) == degree
    values = explicit_bound(*seed, log_l1, m0, gap, Fraction(1, 100))
    s = rational(Fraction(c, d))
    k = iv.log(max(p_power, q_power)) + values["log_omega4"] / s
    l = interval_max([
        exponent*iv.log(prime) / (multiplicity*(1 - rational(target)))
        for prime, exponent, multiplicity, _, target in components
    ])
    assert degree*l < k
    m = interval_max([
        iv.mpf(m0), iv.log(values["kappa1"]) / (d*values["log_omega3"]),
    ])
    terms = [
        iv.log(shift), c*l*(m + 1),
        l*(c*k + degree*iv.log(2) - iv.log(values["kappa2"])) / (k - degree*l),
    ]
    bound = interval_max(terms)
    cap = int(float((bound / iv.log(10)).b)) + 1
    while not bound < cap*iv.log(10):
        cap += 1
    return {
        "seed": list(seed), "m0": m0, "gap": gap,
        "degree": degree, "maximum_shift": shift,
        "components": [list(row) for row in components],
        "limiting_exponents": [
            {"prime": prime, "exponent": iv.nstr(
                1 - degree*exponent*iv.log(prime)/(multiplicity*k), 24)}
            for prime, exponent, multiplicity, _, _ in components
        ],
        "log_omega3": iv.nstr(values["log_omega3"], 24),
        "log_omega4": iv.nstr(values["log_omega4"], 24),
        "K": iv.nstr(k, 24), "L": iv.nstr(l, 24), "M": iv.nstr(m, 24),
        "log_threshold_terms": [iv.nstr(term, 24) for term in terms],
        "log_threshold": iv.nstr(bound, 24),
        "threshold_power_of_ten": cap,
    }


def main():
    choices = (
        ("ap_237_middle_3", (28, 27, 1, 1, 4, 3), "1.4170", 153,
         [(2, 2, 1, 0, ".43"), (7, 1, 1, 0, ".15"),
          (3, 3, 2, 1, ".25")]),
        ("ap_357_middle_3", (245, 243, 1, 1, 5, 4), "1.3098", 50,
         [(5, 1, 1, 0, ".60"), (7, 2, 1, 0, ".065"),
          (3, 5, 2, 1, ".30")]),
        ("ap_237_middle_2", (64, 63, 1, 1, 9, 7), "1.3317", 15,
         [(2, 6, 2, 0, ".390"), (3, 2, 1, 1, ".356"),
          (7, 1, 1, 1, ".429")]),
    )
    rows = []
    for name, seed, l1, m0, components in choices:
        row = product_bound(seed, iv.log(rational(l1)), m0, 100, components)
        rows.append({"name": name, "L1": l1,
                     "gcd_source": "BFT Proposition 5.1", **row})
    middle7_gcd = dusart_gcd_exponent_lower(3, 2, m0=200000)
    middle7 = product_bound(
        (7, 6, 1, 1, 3, 2), rational(middle7_gcd["ell_lower"]), 200000, 100,
        [(7, 1, 2, 0, ".198"), (2, 1, 1, 1, ".428"),
         (3, 1, 1, 1, ".13")],
    )
    rows.append({"name": "ap_237_middle_7", "gcd_certificate": middle7_gcd, **middle7})
    gcd_bound = gcd_exponent_lower(124, 95, terms=1500, m0=3000)
    row = product_bound(
        (36, 35, 1, 1, 124, 95), rational(gcd_bound["ell_lower"]), 3000, 100,
        [(2, 2, 1, 0, ".43"), (3, 2, 1, 0, ".18"),
         (5, 1, 1, 1, ".449"), (7, 1, 1, 1, ".18")],
    )
    rows.append({"name": "balanced_2357", "gcd_certificate": gcd_bound, **row})
    result = {
        "scope": "Uniform numerical product bounds; no binomial rows enumerated.",
        "height_variable": "h=n-9; every selected factor lies between h and h+9",
        "source": "BFT Section 7 and the retained explicit coefficient-gcd bound",
        "choices": rows,
        "common_row_threshold_power_of_ten":
            1 + max(row["threshold_power_of_ten"] for row in rows),
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "thresholds": {row["name"]: row["threshold_power_of_ten"] for row in rows},
        "common_row_threshold_power_of_ten": result["common_row_threshold_power_of_ten"],
        "output": str(output),
    }, indent=2))


if __name__ == "__main__":
    main()
