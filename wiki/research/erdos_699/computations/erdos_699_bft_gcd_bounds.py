"""Numerical BFT bounds from finite prime-interval certificates.

This proves estimates for every m >= m0, rather than enumerating rows.
BFT Lemma 5.2 and (5.7)--(5.8) supply disjoint prime intervals dividing
G(c,d,dm-delta). Lemma 5.4 bounds their logarithmic prime products.
Integer square roots and downward rational rounding certify log L1.
The explicit threshold then comes from BFT Theorem 2.4, evaluated by
erdos_699_bft_explicit_thresholds.py with exact polynomial integrals.
"""

from __future__ import annotations

from fractions import Fraction
import json
from math import factorial, gcd, isqrt
from pathlib import Path

from mpmath import iv

from erdos_699_bft_explicit_thresholds import explicit_bound, serializable
from erdos_699_bft_pair_extension import rational


iv.dps = 80


def gcd_exponent_lower(c, d, terms=4000, m0=100000,
                       scale=10**12, root_scale=10**6):
    """Return rational ell with G(c,d,dm-delta) >= exp(dm*ell).

    The conclusion holds for every integer m >= m0 and delta in {0,1}.
    See the derivation in ../methods/details/bft_numerical_thresholds.md.
    """
    assert c > d >= 1 and gcd(c, d) == 1
    assert terms >= 1 and m0 >= 2*terms and scale > 0 and root_scale > 0
    h = c + d
    lower_scaled = eligible = positive = largest_positive_t = 0
    error_num, error_den = 213, 10**6
    for t in range(1, terms + 1):
        k, r = divmod(d*t, h)
        if 2*r <= h:
            continue
        eligible += 1
        den1, den2 = k + 1, t - 2*k - 1
        assert den1 > 0 and den2 > 0
        if d*den2 >= (c - d)*den1:
            numerator_v, denominator_v = d, den1
        else:
            numerator_v, denominator_v = c - d, den2
        # w/root_scale <= sqrt((h*m0-2)/t), certified with integers.
        w = isqrt((h*m0 - 2)*root_scale**2 // t)
        assert w > 0
        error_a, error_b = 259*root_scale, 125*w
        if error_num*error_b >= error_den*error_a:
            error_a, error_b = error_num, error_den
        if error_a >= error_b:
            continue
        numerator = (
            (error_b - error_a)*(h*m0 - 2)*error_den*denominator_v
            - error_b*(error_den + error_num)*numerator_v*m0*t
        )
        denominator = error_b*error_den*m0*t*denominator_v*d
        if numerator <= 0:
            continue
        positive += 1
        largest_positive_t = t
        lower_scaled += numerator*scale // denominator
    ell = Fraction(lower_scaled, scale)
    assert ell > 0
    return {
        "c": c, "d": d, "terms": terms, "m0": m0,
        "rounding_denominator": scale, "root_scale": root_scale,
        "eligible_terms": eligible, "positive_terms": positive,
        "largest_positive_t": largest_positive_t,
        "ell_lower": str(ell),
    }


# pair, oriented seed (P,Q,a,b,c,d), L1, m0, target.
# Every L1,m0 entry here is from BFT Proposition 5.1.
PROPOSITION_CHOICES = (
    ((2, 3), (9, 8, 1, 1, 25, 17), "1.5540", 582, ".28508"),
    ((2, 5), (128, 125, 1, 1, 5, 4), "1.3098", 50, ".25837"),
    ((2, 7), (8, 7, 1, 1, 25, 17), "1.5540", 582, ".27346"),
    ((2, 11), (128, 121, 1, 1, 5, 4), "1.3098", 50, ".05921"),
    ((2, 13), (512, 169, 1, 3, 25, 17), "1.5540", 582, ".06420"),
    ((3, 5), (27, 25, 1, 1, 4, 3), "1.4170", 153, ".21603"),
    ((3, 7), (49, 243, 5, 1, 5, 3), "1.5454", 86, ".03893"),
    ((3, 11), (243, 121, 1, 2, 7, 5), "1.4135", 74, ".32967"),
    ((3, 13), (2197, 2187, 1, 1, 7, 6), "1.2219", 53, ".23104"),
    ((5, 7), (25, 49, 2, 1, 8, 5), "1.5407", 53, ".22776"),
    ((5, 11), (125, 121, 1, 1, 5, 4), "1.3098", 50, ".19948"),
    ((5, 13), (13, 25, 2, 1, 5, 3), "1.5454", 86, ".16386"),
    ((7, 13), (343, 169, 1, 2, 7, 5), "1.4135", 74, ".09874"),
    ((11, 13), (13, 11, 1, 1, 25, 17), "1.5540", 582, ".05228"),
)

# Pair, oriented seed, common m0, target, epsilon.
GCD_CHOICES = (
    ((5, 7), (25, 49, 2, 1, 59, 39), 10**5, ".2587", ".00005"),
    ((7, 13), (343, 169, 1, 2, 51, 38), 10**5, ".1184", ".00005"),
    ((3, 11), (243, 121, 1, 2, 125, 92), 10**5, ".3432", ".00005"),
)

INDEX_11_CHOICES = (
    ((2, 3), (9, 8, 1, 1, 132, 91), 10**7, ".2906", ".0001"),
    ((2, 5), (128, 125, 1, 1, 113, 92), 10**7, ".2671", ".0001"),
    ((2, 7), (8, 7, 1, 1, 119, 81), 10**7, ".2741", ".0001"),
    ((3, 5), (27, 25, 1, 1, 112, 85), 10**7, ".2227", ".0001"),
    ((3, 7), (49, 243, 5, 1, 145, 88), 10**7, ".0493", ".0001"),
    ((5, 7), (25, 49, 2, 1, 3, 2), 10**7, ".2650", ".0001"),
)


def certify_gcd_choice(choice, terms=4000):
    pair, seed, m0, target, epsilon = choice
    bound = gcd_exponent_lower(seed[-2], seed[-1], terms=terms, m0=m0)
    result = explicit_bound(
        *seed, rational(bound["ell_lower"]), m0, gap=100,
        epsilon=Fraction(epsilon),
    )
    assert result["resulting_exponent"] > rational(target)
    return {
        "pair": list(pair), "seed": list(seed), "target": target,
        "epsilon": epsilon, "gap": 100, "gcd_certificate": bound,
        **serializable(result),
    }


def index_11_gain(rows):
    primes = (2, 3, 5, 7)
    positions = {p: k for k, p in enumerate(primes)}
    edges = [
        (positions[row["pair"][0]], positions[row["pair"][1]],
         int(Fraction(row["target"])*10000))
        for row in rows
    ]
    gains = []
    for choices in range(1 << len(edges)):
        values = [0]*4
        for bit, (p, q, weight) in enumerate(edges):
            vertex = q if choices & (1 << bit) else p
            values[vertex] = max(values[vertex], weight)
        gains.append(-7 + sum(
            Fraction((14 - r)*value, 10000)
            for r, value in enumerate(sorted(values))
        ))
    assert min(gains) == Fraction(7, 400)
    assert 10**(6100*7) > (2*factorial(11)**14)**400
    return {
        "orientations_checked": 1 << len(edges),
        "minimum_weighted_gain": str(min(gains)),
        "algebraic_cap_power_of_ten": 6100,
        "full_row_cap_power_of_ten": max(
            6100, 1 + max(row["threshold_power_of_ten"] for row in rows)
        ),
    }


def main():
    base = []
    for pair, seed, l1, m0, target in PROPOSITION_CHOICES:
        result = explicit_bound(
            *seed, iv.log(rational(l1)), m0, gap=100,
            epsilon=Fraction(1, 100000),
        )
        assert result["resulting_exponent"] > rational(target)
        base.append({
            "pair": list(pair), "seed": list(seed), "L1": l1,
            "m0": m0, "target": target, "epsilon": "1/100000",
            "gap": 100, **serializable(result),
        })
    improved = [certify_gcd_choice(choice) for choice in GCD_CHOICES]
    index11 = [certify_gcd_choice(choice) for choice in INDEX_11_CHOICES]
    seed16 = (8, 7, 1, 1, 25, 17)
    result16 = explicit_bound(
        *seed16, iv.log(rational("1.5540")), 582, gap=100,
        epsilon=Fraction(1, 2500),
    )
    assert result16["resulting_exponent"] > rational(".27307")
    index16 = [{
        "pair": [2, 7], "seed": list(seed16), "L1": "1.5540",
        "m0": 582, "target": ".27307", "epsilon": "1/2500",
        "gap": 100, **serializable(result16),
    }, certify_gcd_choice(
        ((5, 7), (25, 49, 2, 1, 79, 51), 100, ".23237", ".001"),
        terms=50,
    )]
    result = {
        "source": "BFT Theorem 2.4, Lemmas 5.2 and 5.4, Proposition 5.1",
        "scope": "Uniform analytic certificates; no binomial rows enumerated.",
        "proposition_5_1_pairs": base,
        "improved_pairs": improved,
        "index_11_pairs": index11,
        "index_11_row_bound": index_11_gain(index11),
        "index_16_pairs": index16,
        "common_base_threshold_power_of_ten": max(
            row["threshold_power_of_ten"] for row in base + improved
        ),
        "common_index_11_threshold_power_of_ten": max(
            row["threshold_power_of_ten"] for row in index11
        ),
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "improved_pairs": [
            {key: row[key] for key in ("pair", "target", "threshold_power_of_ten")}
            for row in improved
        ],
        "common_base_threshold_power_of_ten": result["common_base_threshold_power_of_ten"],
        "common_index_11_threshold_power_of_ten": result["common_index_11_threshold_power_of_ten"],
        "output": str(output),
    }, indent=2))


if __name__ == "__main__":
    main()
