"""Certify two BFT Theorem 2.2 parameter choices; this does not search rows.

The digamma differences defining log L(c/d) are bounded by a finite positive
series and two integral tails. All remaining arithmetic uses mpmath's
directed interval arithmetic at 80 decimal digits.
"""

from fractions import Fraction
from math import gcd

from mpmath import iv


iv.dps = 80


def rational(value):
    value = Fraction(value)
    return iv.mpf(value.numerator) / value.denominator


def log_l_bounds(c, d, terms=1000):
    assert c > d >= 1 and gcd(c, d) == 1
    modulus = c + d
    inverse = pow(d, -1, modulus)
    lower, upper = iv.mpf(0), iv.mpf(0)
    for j in range(modulus // 2 + 1, modulus):
        r = j * inverse % modulus
        g = Fraction(r, modulus)
        if j >= c:
            f = Fraction(1 + d * r // modulus, d)
        else:
            f = Fraction(1 + (c - d) * r // modulus, c - d)
        assert f > g > 0
        f_iv, g_iv = rational(f), rational(g)
        partial = sum(
            (f_iv - g_iv) / ((k + g_iv) * (k + f_iv))
            for k in range(terms)
        )
        lower += partial + iv.log((terms + f_iv) / (terms + g_iv))
        upper += partial + iv.log(
            (terms - 1 + f_iv) / (terms - 1 + g_iv)
        )
    return iv.mpf([lower.a, upper.b]) / d


def certify(p_power, q_power, a, b, c, d, target, epsilon=Fraction(1, 1000)):
    delta = a * p_power - b * q_power
    assert delta > 0
    s = rational(Fraction(c, d))
    z = rational(Fraction(delta, a * p_power))
    assert 1 < s < 1 / z
    log_l = log_l_bounds(c, d)
    root = iv.sqrt(s * s * z * z + 4 - 4 * z)
    u1 = (s * (2 - z) - root) / (2 * (1 - z) * (s + 1))
    u2 = (s * z + 2 - root) / (2 * z * (s + 1))
    log_alpha = (s + 1) * iv.log(s + 1) - (s - 1) * iv.log(s - 1)
    log_q = (
        log_alpha
        + (s - 1) * iv.log(u1)
        + iv.log(1 - u1)
        + iv.log(1 - u1 + z * u1)
    )
    log_e = (
        log_alpha
        + iv.log(u2)
        + iv.log(1 - u2)
        + (s - 1) * iv.log(1 - z * u2)
    )
    omega1 = (
        (s - 1) * iv.log(p_power)
        + log_l
        - iv.log(a)
        - s * iv.log(b)
        - log_q
    )
    omega2 = (
        s * iv.log(min(p_power, q_power))
        + log_l
        - (s - 1) * iv.log(a * p_power)
        - 2 * iv.log(delta)
        - log_e
    )
    exponent = omega2 / (s * iv.log(max(p_power, q_power)) + omega2)
    assert omega1 > 0
    assert omega2 > 0
    # Theorem 2.2 permits this fixed epsilon and hence the requested target.
    assert epsilon > 0
    assert exponent > rational(target) + rational(epsilon)
    print(f"seed: {a} * {p_power} - {b} * {q_power} = {delta}; s={c}/{d}")
    print(f"log(Omega_1): {iv.nstr(omega1, 18)}")
    print(f"log(Omega_2): {iv.nstr(omega2, 18)}")
    print(f"lambda_1: {iv.nstr(exponent, 18)}; certified target: {target}")


if __name__ == "__main__":
    certify(17**2, 19**2, 5, 4, 19, 10, Fraction(21, 100))
    certify(23, 11, 1, 2, 5, 3, Fraction(29, 200))
