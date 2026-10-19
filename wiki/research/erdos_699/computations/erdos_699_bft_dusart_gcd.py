"""Uniform BFT coefficient-gcd bounds using the retained Dusart estimates.

The prime interval calculation is the one in erdos_699_bft_gcd_bounds.py.
Only the global upper error and the floor for the lower error change.
All returned bounds are rational; no prime or binomial rows are enumerated.
"""

from fractions import Fraction
from math import gcd, isqrt

from mpmath import iv


def gcd_exponent_lower(c, d, terms=4000, m0=100000,
                       scale=10**12, root_scale=10**6):
    """Certify log G(c,d,dm-delta)/(dm) >= ell for m >= m0."""
    assert c > d >= 1 and gcd(c, d) == 1
    assert terms >= 1 and m0 >= 2 * terms and scale > 0 and root_scale > 0
    # Dusart Theorem 5.2: .01/log(x)^2 < 1/60000 for x >= 10^11.
    assert iv.log(10) > iv.mpf(9) / 4
    assert (11 * Fraction(9, 4)) ** 2 > 600
    h = c + d
    total = eligible = positive = largest = 0
    for t in range(1, terms + 1):
        k, r = divmod(d * t, h)
        if 2 * r <= h:
            continue
        eligible += 1
        den1, den2 = k + 1, t - 2 * k - 1
        assert den1 > 0 and den2 > 0
        if d * den2 >= (c - d) * den1:
            v_num, v_den = d, den1
        else:
            v_num, v_den = c - d, den2
        root = isqrt((h * m0 - 2) * root_scale**2 // t)
        assert root > 0
        # A lower bound for sqrt(U(m0)) gives an upper error bound.
        err_num, err_den = 259 * root_scale, 125 * root
        if err_num * 60000 < err_den:
            err_num, err_den = 1, 60000
        if err_num >= err_den:
            continue
        numerator = (
            (err_den - err_num) * (h * m0 - 2) * 36260 * v_den
            - err_den * 36261 * v_num * m0 * t
        )
        denominator = err_den * 36260 * m0 * t * v_den * d
        if numerator <= 0:
            continue
        positive += 1
        largest = t
        total += numerator * scale // denominator
    ell = Fraction(total, scale)
    assert ell > 0
    return {
        "c": c, "d": d, "terms": terms, "m0": m0,
        "rounding_denominator": scale, "root_scale": root_scale,
        "eligible_terms": eligible, "positive_terms": positive,
        "largest_positive_t": largest, "ell_lower": str(ell),
        "upper_relative_error": "1/36260",
        "lower_relative_error_floor": "1/60000",
        "source": "Dusart 2010 Proposition 5.1 and Theorem 5.2; BFT Lemmas 5.2 and 5.4",
    }


if __name__ == "__main__":
    import json
    import sys

    c, d = map(int, sys.argv[1:3])
    m0 = int(sys.argv[3]) if len(sys.argv) > 3 else 100000
    print(json.dumps(gcd_exponent_lower(c, d, m0=m0), indent=2))
