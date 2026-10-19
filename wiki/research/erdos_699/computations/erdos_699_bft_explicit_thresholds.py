"""Directed-interval evaluation of the explicit threshold in BFT Theorem 2.4.

The polynomial integrals in C_{1,delta} and C_{2,delta} are exact Fractions.
The supplied log_l1 must itself be certified, together with its m0, as a
lower bound in BFT (2.8). The main program uses Proposition 5.1 entries.
"""

from __future__ import annotations

from fractions import Fraction
import json
from math import comb, factorial
from pathlib import Path

from mpmath import iv

from erdos_699_bft_pair_extension import rational


iv.dps = 80


def beta_integral(a: int, b: int) -> Fraction:
    """Integral of t**a * (1-t)**b from zero to one."""
    assert a >= 0 and b >= 0
    return Fraction(factorial(a) * factorial(b), factorial(a + b + 1))


def polynomial_integral(a: int, b: int, k: int, z: Fraction) -> Fraction:
    """Integral of t**a * (1-t)**b * (1-z*t)**k, exactly."""
    assert k >= 0
    result = sum(
        (Fraction(comb(k, r)) * (-z)**r * beta_integral(a + r, b)
         for r in range(k + 1)),
        Fraction(0),
    )
    assert result > 0
    return result


def interval_max(values):
    return iv.mpf([max(v.a for v in values), max(v.b for v in values)])


def interval_min(values):
    return iv.mpf([min(v.a for v in values), min(v.b for v in values)])


def explicit_bound(p_power, q_power, a, b, c, d, log_l1, m0, gap, epsilon):
    """Return certified intervals for all inputs to BFT's explicit x0.

    p_power and q_power are the oriented seed prime powers, with
    a*p_power > b*q_power. log_l1 is a directed interval. m0 is an
    integer proving (2.8), gap is the desired D, and epsilon is rational.
    """
    assert a > 0 and b > 0 and c > d >= 1 and m0 >= 0 and gap > 0
    epsilon = Fraction(epsilon)
    assert epsilon > 0
    delta0 = a * p_power - b * q_power
    assert delta0 > 0
    z_rat = Fraction(delta0, a * p_power)
    z, s = rational(z_rat), rational(Fraction(c, d))
    assert 1 < s < 1 / z
    root = iv.sqrt(s*s*z*z + 4 - 4*z)
    # Rationalized versions avoid cancellation when the seed gap is small.
    u1 = 2*(s - 1) / (s*(2 - z) + root)
    u2 = 2 / (s*z + 2 + root)
    log_alpha = (s + 1)*iv.log(s + 1) - (s - 1)*iv.log(s - 1)
    log_q = (log_alpha + (s - 1)*iv.log(u1)
             + iv.log(1 - u1) + iv.log(1 - u1 + z*u1))
    log_e = (log_alpha + iv.log(u2) + iv.log(1 - u2)
             + (s - 1)*iv.log(1 - z*u2))
    log_omega3 = ((s - 1)*iv.log(p_power) + log_l1 - iv.log(a)
                  - s*iv.log(b) - log_q)
    log_omega4 = (s*iv.log(min(p_power, q_power)) + log_l1
                  - (s - 1)*iv.log(a*p_power) - 2*iv.log(delta0) - log_e)
    assert log_omega3 > 0 and log_omega4 > 0
    log_denominator = s*iv.log(max(p_power, q_power)) + log_omega4
    exponent = log_omega4 / log_denominator
    assert 0 < exponent < 1

    alpha_d = Fraction((c + d)**(c + d), d**(2*d) * (c - d)**(c - d))
    constants1, constants2 = [], []
    for delta in (0, 1):
        square_factor = iv.sqrt(s*s - 1)
        if delta:
            square_factor = 1 / square_factor
        common = rational(alpha_d) * square_factor / (2*iv.pi)
        i1 = polynomial_integral(c - d - 1 + delta, d - delta,
                                 d - delta, 1 - z_rat)
        i2 = polynomial_integral(d - delta, d - delta,
                                 c - d - 1 + delta, z_rat)
        constants1.append(common * rational(i1) / iv.exp(d*log_q))
        constants2.append(common * rational(i2) / iv.exp(d*log_e))
    kappa1 = interval_max([
        2*gap*constants1[delta] / (a*p_power)**delta for delta in (0, 1)
    ])
    kappa2 = interval_min([
        rational(Fraction((a*p_power)**(1 - delta), 1)
                 / (2*Fraction(delta0)**(1 - 2*delta))) / constants2[delta]
        for delta in (0, 1)
    ])
    terms = [
        iv.log(kappa1) / (d*log_omega3),
        (1 + exponent)*(c*iv.log(max(p_power, q_power)) - iv.log(kappa2))
        / (rational(epsilon)*d*log_denominator),
        (1 + exponent)*iv.log(kappa2)
        / (rational(epsilon)*d*log_denominator),
        iv.mpf(m0),
    ]
    maximum = interval_max(terms)
    log_x0 = c*(maximum + 1)*iv.log(max(p_power, q_power)) / (1 - exponent)
    # The floating approximation only proposes an integer; the interval
    # comparison below is the certificate for the returned power of ten.
    cap = int(float((log_x0 / iv.log(10)).b)) + 1
    while not log_x0 < cap*iv.log(10):
        cap += 1
    return {
        "log_omega3": log_omega3,
        "log_omega4": log_omega4,
        "lambda3": exponent,
        "resulting_exponent": exponent - rational(epsilon),
        "kappa1": kappa1,
        "kappa2": kappa2,
        "M_terms": terms,
        "log_x0": log_x0,
        "threshold_power_of_ten": cap,
    }


def serializable(result):
    return {
        key: ([iv.nstr(v, 20) for v in value] if key == "M_terms"
              else value if isinstance(value, int) else iv.nstr(value, 20))
        for key, value in result.items()
    }


if __name__ == "__main__":
    choices = (
        ((2, 17), (17, 16, 1, 1, 7, 5), "1.4135", 74,
         Fraction(3259, 10000), Fraction(12, 1000)),
        ((17, 19), (289, 361, 5, 4, 2, 1), "1.9377", 150,
         Fraction(1855, 10000), Fraction(7, 1000)),
        ((11, 23), (23, 11, 1, 2, 7, 4), "1.6219", 60,
         Fraction(1068, 10000), Fraction(11, 1000)),
        ((2, 17), (17, 16, 1, 1, 7, 5), "1.4135", 74,
         Fraction(3379, 10000), Fraction(1, 100000)),
        ((17, 19), (289, 361, 5, 4, 2, 1), "1.9377", 150,
         Fraction(1925, 10000), Fraction(1, 100000)),
    )
    rows = []
    for pair, seed, l1, m0, target, epsilon in choices:
        result = explicit_bound(*seed, iv.log(rational(Fraction(l1))), m0,
                                gap=100, epsilon=epsilon)
        assert result["resulting_exponent"] > rational(target)
        # For every index at most 34, selected factors are at least n-33.
        # Absorb that shift without increasing the power-of-ten cap.
        row_cap = result["threshold_power_of_ten"]
        assert result["log_x0"] < iv.log(iv.mpf(10**row_cap - 33))
        row = {"pair": pair, "seed": seed, "L1": l1, "m0": m0,
               "gap": 100, "epsilon": str(epsilon), "target": str(target),
               "row_threshold_maximum_position": 33,
               "row_threshold_power_of_ten": row_cap,
               **serializable(result)}
        rows.append(row)
        print(json.dumps(row), flush=True)
    Path(__file__).with_suffix(".json").write_text(json.dumps(rows, indent=2) + "\n")
