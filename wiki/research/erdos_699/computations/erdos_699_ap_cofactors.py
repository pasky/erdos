"""Certify effective cofactor bounds from quadratic constant-gap identities.

This evaluates fixed Padé parameter choices, not binomial rows. The
coefficient-gcd estimates are exact rational bounds, and the remaining
inequalities use directed interval arithmetic. See the accompanying lead
../methods/details/ap_cofactors.md for the three-way minimum argument.
The four-factor assertion requires different unordered position pairs,
so that its constant product difference is nonzero.
"""

from fractions import Fraction
import json
from pathlib import Path

from mpmath import iv

from erdos_699_bft_gcd_bounds import gcd_exponent_lower
from erdos_699_bft_pair_extension import rational


iv.dps = 80

# Middle prime and exponent; endpoint primes and exponents; seed coefficients;
# rational Padé parameter; target exponents in increasing prime order.
CHOICES = (
    (2, 4, 3, 1, 5, 1, 1, 1, 11, 8, (".348", ".483", ".243")),
    (3, 4, 2, 4, 5, 1, 1, 1, 5, 4, (".262", ".415", ".571")),
    (3, 4, 2, 3, 5, 1, 1, 2, 29, 20, (".3299", ".292", ".4813")),
    (5, 2, 2, 3, 3, 1, 1, 1, 4, 3, (".194", ".574", ".376")),
    (3, 3, 2, 2, 7, 1, 1, 1, 4, 3, (".483", ".385", ".274")),
    (3, 5, 5, 1, 7, 2, 1, 1, 5, 4, (".346", ".617", ".074")),
    (2, 6, 3, 2, 7, 1, 1, 1, 4, 3, (".390", ".356", ".429")),
    (7, 1, 2, 1, 3, 1, 1, 1, 3, 2, (".428", ".13", ".198")),
)


def analytic_parameters(p_power, q_power, a, b, c, d):
    if a*p_power < b*q_power:
        p_power, q_power, a, b = q_power, p_power, b, a
    delta = a*p_power - b*q_power
    assert delta > 0
    gcd_certificate = gcd_exponent_lower(c, d, terms=4000, m0=10**8)
    ell = rational(gcd_certificate["ell_lower"])
    s = rational(Fraction(c, d))
    z = rational(Fraction(delta, a*p_power))
    assert 1 < s < 1/z
    root = iv.sqrt(s*s*z*z + 4 - 4*z)
    u1 = 2*(s - 1) / (s*(2 - z) + root)
    u2 = 2 / (s*z + 2 + root)
    log_alpha = (s + 1)*iv.log(s + 1) - (s - 1)*iv.log(s - 1)
    log_q = (log_alpha + (s - 1)*iv.log(u1)
             + iv.log(1 - u1) + iv.log(1 - u1 + z*u1))
    log_e = (log_alpha + iv.log(u2) + iv.log(1 - u2)
             + (s - 1)*iv.log(1 - z*u2))
    omega3 = ((s - 1)*iv.log(p_power) + ell
              - iv.log(a) - s*iv.log(b) - log_q)
    omega4 = (s*iv.log(min(p_power, q_power)) + ell
              - (s - 1)*iv.log(a*p_power) - 2*iv.log(delta) - log_e)
    assert omega3 > 0 and omega4 > 0
    kappa = iv.log(max(p_power, q_power)) + omega4/s
    return kappa, {
        "seed": [p_power, q_power, a, b, c, d],
        "gcd_certificate": gcd_certificate,
        "log_omega3": iv.nstr(omega3, 28),
        "log_omega4": iv.nstr(omega4, 28),
        "K": iv.nstr(kappa, 28),
    }


def certify(choice):
    middle, exponent, left, a_left, right, a_right, a, b, c, d, targets = choice
    middle_power = middle**exponent
    endpoint_product = left**a_left * right**a_right
    kappa, parameters = analytic_parameters(middle_power, endpoint_product, a, b, c, d)
    exponents = {
        middle: 1 - iv.log(middle_power)/kappa,
        left: 1 - 2*iv.log(left**a_left)/kappa,
        right: 1 - 2*iv.log(right**a_right)/kappa,
    }
    primes = sorted(exponents)
    epsilon = Fraction(1, 10000)
    for prime, target in zip(primes, targets):
        assert exponents[prime] - rational(epsilon) > rational(target)
    return {
        "middle_prime": middle,
        "middle_power": exponent,
        "endpoint_powers": {str(left): a_left, str(right): a_right},
        **parameters,
        "exponent_margin": str(epsilon),
        "targets": dict(zip(map(str, primes), targets)),
        "alpha": {str(p): iv.nstr(exponents[p], 28) for p in primes},
    }


def certify_four_factors():
    kappa, parameters = analytic_parameters(36, 35, 1, 1, 13, 10)
    powers = {2: 2, 3: 2, 5: 1, 7: 1}
    targets = {2: ".528", 3: ".253", 5: ".453", 7: ".338"}
    exponents = {p: 1 - 2*k*iv.log(p)/kappa for p, k in powers.items()}
    epsilon = Fraction(1, 10000)
    for prime, target in targets.items():
        assert exponents[prime] - rational(epsilon) > rational(target)
    return {
        "equal_position_sums": [[2, 3], [5, 7]],
        "prime_powers": {str(p): k for p, k in powers.items()},
        **parameters,
        "exponent_margin": str(epsilon),
        "targets": {str(p): t for p, t in targets.items()},
        "alpha": {str(p): iv.nstr(e, 28) for p, e in exponents.items()},
    }


if __name__ == "__main__":
    result = {
        "source": "BFT Theorem 2.4 and (7.6), matching three or four prime-power exponents",
        "scope": "AP triples or two pairs with equal position sums; effective asymptotic bounds",
        "row_enumeration": False,
        "choices": [certify(choice) for choice in CHOICES],
        "four_factor_choices": [certify_four_factors()],
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
