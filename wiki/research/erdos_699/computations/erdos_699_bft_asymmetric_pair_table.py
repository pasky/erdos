"""Verify a larger table of asymmetric BFT cofactor constraints.

Published GCD parameters give numerical thresholds. Parameters using a
strict rational lower bound on log L(c/d) give effective thresholds via
BFT's proof of Theorem 2.2; this checker does not evaluate those thresholds.
No binomial rows are enumerated.
"""

from fractions import Fraction
import json
from pathlib import Path

from mpmath import iv

from erdos_699_bft_asymmetric import asymmetric_bound
from erdos_699_bft_pair_extension import log_l_bounds, rational


iv.dps = 80
PARAMETERS = Path(__file__).with_name("erdos_699_bft_asymmetric_pair_parameters.json")
PUBLISHED_GCD = {
    (9, 8): ("1.1742", 25), (8, 7): ("1.1951", 28),
    (7, 6): ("1.2219", 53), (6, 5): ("1.2581", 35),
    (5, 4): ("1.3098", 50), (9, 7): ("1.3317", 15),
    (7, 5): ("1.4135", 74), (4, 3): ("1.4170", 153),
    (3, 2): ("1.5395", 138), (8, 5): ("1.5407", 53),
    (5, 3): ("1.5454", 86), (3, 1): ("1.5498", 260),
    (25, 17): ("1.5540", 582), (7, 4): ("1.6219", 60),
    (8, 3): ("1.6560", 149), (9, 5): ("1.6636", 79),
    (5, 2): ("1.7017", 231), (7, 3): ("1.7282", 161),
    (9, 4): ("1.7666", 87), (2, 1): ("1.9377", 150),
}


def prime_base(power, pair):
    assert power > 1
    for prime in pair:
        value = power
        while value % prime == 0:
            value //= prime
        if value == 1:
            return prime
    raise AssertionError("seed is not a power of an indicated prime")


def endpoint_limits(seed, log_l1):
    p_power, q_power, a, b, c, d = seed
    delta = a*p_power - b*q_power
    assert delta > 0 and c > d >= 1
    s = rational(Fraction(c, d))
    z = rational(Fraction(delta, a*p_power))
    assert s < 1/z
    root = iv.sqrt(s*s*z*z + 4 - 4*z)
    u1 = 2*(s - 1) / (s*(2 - z) + root)
    u2 = 2 / (s*z + 2 + root)
    log_alpha = (s + 1)*iv.log(s + 1) - (s - 1)*iv.log(s - 1)
    log_q = (log_alpha + (s - 1)*iv.log(u1)
             + iv.log(1 - u1) + iv.log(1 - u1 + z*u1))
    log_e = (log_alpha + iv.log(u2) + iv.log(1 - u2)
             + (s - 1)*iv.log(1 - z*u2))
    omega3 = ((s - 1)*iv.log(p_power) + log_l1 - iv.log(a)
              - s*iv.log(b) - log_q)
    omega4 = (s*iv.log(min(p_power, q_power)) + log_l1
              - (s - 1)*iv.log(a*p_power) - 2*iv.log(delta) - log_e)
    assert omega3 > 0 and omega4 > 0
    k = iv.log(max(p_power, q_power)) + omega4/s
    return 1 - iv.log(p_power)/k, 1 - iv.log(q_power)/k


def check_row(row, published):
    seed = row["seed"]
    p_power, q_power, _, _, c, d = seed
    pair = row["pair"]
    p_base, q_base = prime_base(p_power, pair), prime_base(q_power, pair)
    assert p_base != q_base
    targets = dict(zip(pair, map(lambda x: Fraction(x, 10000), row["endpoints_scaled"])))
    assert all(0 < x < Fraction(1, 2) for x in targets.values())
    if published:
        assert (row["L1"], row["m0"]) == PUBLISHED_GCD[c, d]
        log_l1 = iv.log(rational(row["L1"]))
    else:
        log_l1 = rational(row["log_L1"])
        assert log_l1 < log_l_bounds(c, d)
    limits = endpoint_limits(seed, log_l1)
    assert limits[0] > rational(targets[p_base])
    assert limits[1] > rational(targets[q_base])
    result = {
        **row,
        "asymmetric_edge_scaled": pair + row["endpoints_scaled"],
        "verified": True,
    }
    if published:
        threshold = asymmetric_bound(*seed, log_l1, row["m0"], 100,
                                     targets[p_base], targets[q_base])
        result["numerical_threshold"] = threshold
    else:
        result["threshold_scope"] = "Effectively computable by BFT Section 7; not numerically evaluated."
    return result


def main():
    parameters = json.loads(PARAMETERS.read_text())
    result = {
        "source": parameters["source"],
        "weight_denominator": parameters["weight_denominator"],
        "published_gcd_pairs": [check_row(row, True)
                                for row in parameters["published_gcd_parameters"]],
        "effective_gcd_pairs": [check_row(row, False)
                                for row in parameters["effective_gcd_parameters"]],
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    for key in ("published_gcd_pairs", "effective_gcd_pairs"):
        print(key, len(result[key]), "verified")


if __name__ == "__main__":
    main()
