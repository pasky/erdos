"""Certify effective rational-block cofactor restrictions for index 12.

The fixed arithmetic and analytic margins are checked by directed intervals.
The coefficient-gcd starting point exists effectively by BFT Theorem 2.2;
this certificate does not assign it a numerical value. No full-index claim
is made by this file.
"""
from fractions import Fraction
import json
from pathlib import Path

from mpmath import iv
from erdos_699_bft_pair_extension import log_l_bounds, rational

iv.dps = 80

CHOICES = [
    {
        "name": "2_11_stronger_ordinary_endpoints",
        "seed": [512, 1331, 13, 5, 80, 39],
        "prime_exponents": {2: 9, 11: 3},
        "log_L1": "347257/500000",
        "target_cofactor_exponents": {2: "31/125", 11: "133/1000"},
        "epsilon": "9/1000000",
        "ordinary_target_exponents": {2: "31/125", 11: "133/1000"},
    },
    {
        "name": "2_7_stronger_ordinary_endpoints",
        "seed": [49, 16, 1, 3, 53, 31],
        "prime_exponents": {2: 4, 7: 2},
        "log_L1": "255299/500000",
        "target_cofactor_exponents": {2: "3/8", 7: "123/1000"},
        "epsilon": "1/2500",
        "ordinary_target_exponents": {2: "3/8", 7: "123/1000"},
    },
    {
        "name": "2_7_first_box",
        "seed": [49, 16, 1, 3, 61, 33],
        "prime_exponents": {2: 4, 7: 2},
        "log_L1": "577/1000",
        "target_cofactor_exponents": {2: "2773/10000", 7: "59/2000"},
        "epsilon": "6/25",
        "ordinary_target_exponents": {2: "87/250", 7: "17/200"},
    },
    {
        "name": "2_7_second_box",
        "seed": [49, 16, 1, 3, 70, 37],
        "prime_exponents": {2: 4, 7: 2},
        "log_L1": "609/1000",
        "target_cofactor_exponents": {2: "2773/10000", 7: "0"},
        "epsilon": "8/25",
    },
    {
        "name": "2_11_third_box",
        "seed": [512, 1331, 13, 5, 37, 16],
        "prime_exponents": {2: 9, 11: 3},
        "log_L1": "121/200",
        "target_cofactor_exponents": {2: "7/50", 11: "0"},
        "epsilon": "12/25",
        "ordinary_target_exponents": {2: "193/1000", 11: "69/1000"},
    },
]


def certify(choice):
    P, Q, a, b, c, d = choice["seed"]
    D = a*P - b*Q
    assert D == 1
    assert set(choice["prime_exponents"]) == set(choice["target_cofactor_exponents"])
    assert sorted(p**k for p, k in choice["prime_exponents"].items()) == sorted([P, Q])
    ell = Fraction(choice["log_L1"])
    log_l = log_l_bounds(c, d)
    assert rational(ell) < log_l
    s = rational(Fraction(c, d))
    z = rational(Fraction(D, a*P))
    assert 1 < s < 1/z
    root = iv.sqrt(s*s*z*z + 4 - 4*z)
    u1 = 2*(s - 1)/(s*(2 - z) + root)
    u2 = 2/(s*z + 2 + root)
    log_alpha = (s + 1)*iv.log(s + 1) - (s - 1)*iv.log(s - 1)
    log_q = (log_alpha + (s - 1)*iv.log(u1)
             + iv.log(1 - u1) + iv.log(1 - (1 - z)*u1))
    log_e = (log_alpha + iv.log(u2) + iv.log(1 - u2)
             + (s - 1)*iv.log(1 - z*u2))
    log_omega3 = ((s - 1)*iv.log(P) + rational(ell)
                  - iv.log(a) - s*iv.log(b) - log_q)
    log_omega4 = (s*iv.log(min(P, Q)) + rational(ell)
                  - (s - 1)*iv.log(a*P) - 2*iv.log(D) - log_e)
    assert log_omega3 > 0 and log_omega4 > 0
    C = log_omega3/s
    K = iv.log(max(P, Q)) + log_omega4/s
    J = K - C
    assert J > 0
    terms = {}
    total = iv.mpf(0)
    for p, power in choice["prime_exponents"].items():
        exponent = rational(Fraction(choice["target_cofactor_exponents"][p]))
        term = power*iv.log(p) - J*(1 - exponent)
        # Certify the sign before taking its positive part.
        if term > 0:
            total += term
        else:
            assert term < 0
        terms[p] = iv.nstr(term, 50)
    margin = C - total
    assert margin > rational(Fraction(choice["epsilon"]))
    ordinary_endpoints = {}
    for p, target in choice.get("ordinary_target_exponents", {}).items():
        alpha = 1 - choice["prime_exponents"][p]*iv.log(p)/K
        assert alpha > rational(Fraction(target))
        ordinary_endpoints[p] = iv.nstr(alpha, 50)
    return {
        **choice,
        "ordinary_endpoint_intervals": ordinary_endpoints,
        "log_L_interval": iv.nstr(log_l, 50),
        "log_omega3_interval": iv.nstr(log_omega3, 50),
        "log_omega4_interval": iv.nstr(log_omega4, 50),
        "C_interval": iv.nstr(C, 50),
        "J_interval": iv.nstr(J, 50),
        "positive_part_arguments": terms,
        "strict_margin_interval": iv.nstr(margin, 50),
        "conclusion": "The listed two cofactor upper bounds cannot both hold above an effective height threshold.",
    }


def main():
    result = {
        "description": "Effective rational-block prime-pair constraints for the last three exploratory index-12 boxes.",
        "scope": "For every fixed positive gap bound D; the effective height threshold is not numerically evaluated.",
        "choices": [certify(choice) for choice in CHOICES],
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
