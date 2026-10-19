"""Certify the rational-block BFT refinement for the prime pair 2,3.

The coefficient-gcd threshold is effective via BFT Theorem 2.2, but is not
numerically evaluated here. This file certifies the fixed analytic constants
and strict exponent margins, not a numerical height cutoff.
"""
from fractions import Fraction
import json
from pathlib import Path

from mpmath import iv
from erdos_699_bft_pair_extension import log_l_bounds, rational

iv.dps = 80


def main():
    p_power, q_power, a, b, c, d = 9, 8, 1, 1, 3, 2
    ell = Fraction(308, 625)
    log_l = log_l_bounds(c, d)
    assert rational(ell) < log_l
    s = rational(Fraction(c, d))
    z = rational(Fraction(a*p_power - b*q_power, a*p_power))
    root = iv.sqrt(s*s*z*z + 4 - 4*z)
    u1 = 2*(s - 1)/(s*(2 - z) + root)
    u2 = 2/(s*z + 2 + root)
    log_alpha = (s + 1)*iv.log(s + 1) - (s - 1)*iv.log(s - 1)
    log_q = (log_alpha + (s - 1)*iv.log(u1)
             + iv.log(1 - u1) + iv.log(1 - u1 + z*u1))
    log_e = (log_alpha + iv.log(u2) + iv.log(1 - u2)
             + (s - 1)*iv.log(1 - z*u2))
    log_omega3 = ((s - 1)*iv.log(p_power) + rational(ell)
                  - iv.log(a) - s*iv.log(b) - log_q)
    log_omega4 = (s*iv.log(min(p_power, q_power)) + rational(ell)
                  - (s - 1)*iv.log(a*p_power)
                  - 2*iv.log(a*p_power - b*q_power) - log_e)
    assert log_omega3 > 0 and log_omega4 > 0
    A, B = iv.log(p_power), iv.log(q_power)
    C = log_omega3/s
    H = log_omega4/s
    K = A + H
    J = K - C
    assert J > A > B
    target = Fraction(1463, 5000)
    positive_term = A - J*(1 - rational(target))
    negative_term = B - J*(1 - rational(target))
    assert positive_term > 0
    assert negative_term < 0
    assert positive_term < C
    assert H/J > rational(target)
    values = {
        "log_L_interval": log_l,
        "log_omega3": log_omega3, "log_omega4": log_omega4,
        "C": C, "H": H, "K": K, "J": J,
        "cofactor_3_knee": 1 - A/J, "cofactor_2_knee": 1 - B/J,
        "cofactor_3_axis_intercept": H/J,
        "cofactor_2_axis_intercept": (K - B)/J,
        "diagonal_boundary": (2 - (A + B - C)/J)/2,
        "strict_diagonal_margin": C - positive_term,
    }
    result = {
        "seed": [p_power, q_power, a, b, c, d],
        "log_L1": str(ell),
        "target_maximum_exponent": str(target),
        "target_product_exponent": str(target),
        "height_scope": "Effective threshold for every fixed gap; not numerically evaluated.",
        "verified_intervals": {key: iv.nstr(value, 30) for key, value in values.items()},
    }
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
