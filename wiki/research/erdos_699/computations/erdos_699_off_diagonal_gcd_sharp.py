#!/usr/bin/env python3
"""Uniform off-diagonal coefficient-gcd rates with sharper theta bounds.

The BFT intervals and floor stability are unchanged. Broadbent et al.'s
GLOBAL theta bounds are combined with Johnston--Yang Lemma 2.2 on its
stated finite range, and the retained BFT small-x lower bound. All endpoint
errors and final sums are rational. A short directed initialization supplies
upward-rounded exponential thresholds and logarithm constants.
"""
from fractions import Fraction
from functools import lru_cache
from math import isqrt

from mpmath import iv
from erdos_699_off_diagonal_gcd_numeric import floor_stability_bound

iv.dps = 120

# Active final Table 14 (ThetaEpsilon) in the retained Broadbent et al. paper.
# Every printed error is rounded UP by at least one last displayed unit,
# because the paper explicitly warns that its printf display rounds values.
# (log X0, upper error, lower error), each valid for ALL x > X0.
GLOBAL_THETA_TABLE = (
    (20, '0.000042677', '0.000091640'),
    (25, '0.0000035032', '0.0000074367'),
    (30, '0.00000028756', '0.00000060752'),
    (35, '0.000000023604', '0.000000049767'),
    (40, '0.000000019339', '0.000000021483'),
    (45, '0.000000010908', '0.000000011085'),
    (50, '0.0000000011200', '0.0000000011345'),
    (60, '0.000000000012216', '0.000000000012313'),
    (70, '0.0000000000027924', '0.0000000000027931'),
    (80, '0.0000000000026109', '0.0000000000026109'),
    (90, '0.0000000000025214', '0.0000000000025214'),
    (100, '0.0000000000024531', '0.0000000000024531'),
    (200, '0.0000000000021816', '0.0000000000021817'),
)
GLOBAL_UPPER = Fraction('0.000000019338')  # Corollary 2.1: 1.93378e-8.
JY_MAX = 2169 * 10**22  # 2.169e25, not 2.169e22.
PI_LOWER = Fraction(3141592653589793, 10**15)
LN2_UPPER = Fraction(693147180559946, 10**15)
assert iv.pi > iv.mpf(PI_LOWER.numerator) / PI_LOWER.denominator
assert iv.log(2) < iv.mpf(LN2_UPPER.numerator) / LN2_UPPER.denominator

assert 64**6 <= 10**11
assert 512**4 <= 10**11
assert 1024**10 <= (10**11)**3
assert (Fraction(194,100) + Fraction(103883,100000)/64
        + Fraction(94,100)/512 + Fraction(103883,100000)/1024) < Fraction(49,25)


def _ceil_interval(value):
    """Smallest nearby integer certified strictly above an interval."""
    answer = int(value.b) + 1
    assert value < answer
    return answer


TABLE = tuple((_ceil_interval(iv.exp(b)), Fraction(up), Fraction(lo))
              for b, up, lo in GLOBAL_THETA_TABLE)
assert TABLE[1][0] < 10**11
assert TABLE[6][0] < JY_MAX
LOG_MANTISSA_UPPER = tuple(
    Fraction(_ceil_interval(iv.log(iv.mpf(k)/16)*10**15), 10**15)
    for k in range(16, 33)
)


def _log_upper(numerator, denominator):
    """Rational upper log via a 16-bin binary mantissa, no float arithmetic."""
    k = numerator.bit_length() - denominator.bit_length()
    if k >= 0:
        if numerator < denominator * (1 << k):
            k -= 1
    else:
        if numerator * (1 << -k) < denominator:
            k -= 1
    assert k >= 0  # callers use x > 599
    den = denominator * (1 << k)
    q = (16*numerator + den - 1)//den
    assert 16 <= q <= 32
    return k*LN2_UPPER + LOG_MANTISSA_UPPER[q-16]


@lru_cache(maxsize=65536)
def theta_errors(numerator, denominator=1, *, root_scale=10**6):
    """Return (lower_error, upper_error), uniformly for EVERY x >= n/d.

    theta(x) >= x*(1-lower_error), theta(x) <= x*(1+upper_error).
    This is a tail bound, not a pointwise finite-range assertion.
    """
    assert numerator > 0 and denominator > 0 and root_scale > 0
    lower, upper = Fraction(1), GLOBAL_UPPER
    for threshold, up, lo in TABLE:
        if numerator >= threshold*denominator:
            lower, upper = min(lower, lo), min(upper, up)
        else:
            break
    # Broadbent Corollary 9.1, c=C=.94 and c0=1.03883, gives
    # theta(x)>=x-sqrt(x)*(1.94+1.03883*x^(-1/6)
    #                            +.94*x^(-1/4)+1.03883*x^(-3/10)).
    # For x>=1e11 its bracket is <1.96: use denominators64,512,1024.
    # Combined with the retained BFT bound below1e11, this extends
    # theta(x)>x-2.072sqrt(x) through1e19. Patch beyond1e19 usingb40.
    if numerator <= 10**19*denominator:
        root = isqrt(numerator*root_scale**2//denominator)
        if root:
            constant = Fraction(49,25) if numerator >= 10**11*denominator else Fraction(259,125)
            lower = min(lower, max(constant*root_scale/root,
                                   Fraction(GLOBAL_THETA_TABLE[4][2])))
    # Schoenfeld-shaped bound verified by JY on 599<x<=2.169e25.
    # log(x)^2/sqrt(x) decreases for x>e^4. Patch its finite end with
    # the GLOBAL Broadbent b=50 row; this avoids assuming RH above its
    # verified range or applying a finite-range bound to an infinite tail.
    if 599*denominator < numerator <= JY_MAX*denominator:
        root = isqrt(numerator*root_scale**2//denominator)
        log_upper = _log_upper(numerator, denominator)
        error = log_upper*log_upper*root_scale/(8*PI_LOWER*root)
        lower = min(lower, max(error, Fraction(GLOBAL_THETA_TABLE[6][2])))
        upper = min(upper, max(error, Fraction(GLOBAL_THETA_TABLE[6][1])))
    return lower, upper


def theta_pointwise(numerator, denominator=1, *, root_scale=10**6):
    """Rational pointwise bounds; a finite-prime-prefix caller can improve them."""
    x = Fraction(numerator, denominator)
    low, up = theta_errors(numerator, denominator, root_scale=root_scale)
    lower, upper = x*(1-low), x*(1+up)
    if numerator <= 10**19*denominator:
        upper = min(upper, x)  # Büthe, quoted by Broadbent Corollary2.1.
        root_upper = Fraction(isqrt(numerator*root_scale**2//denominator)+1, root_scale)
        constant = Fraction(49,25) if numerator >= 10**11*denominator else Fraction(259,125)
        lower = max(lower, x-constant*root_upper)
    return lower, upper


def gcd_exponent_lower(A, B, C, *, terms=4000, m0=10**8,
                       scale=10**12, root_scale=10**6, **kwargs):
    """Compatible JSON certificate for log G/m on both rectangles, m>=m0."""
    assert not kwargs, kwargs
    assert min(A, B, C, terms, m0, scale, root_scale) > 0 and B*m0 >= 2
    directions = (A, B, C)
    H = sum(directions)
    total = eligible = positive = largest = 0
    floor_bound = 1
    for t in range(1, terms+1):
        floors = [X*t//H for X in directions]
        if sum(floors) != t-2:
            continue
        eligible += 1
        stable = floor_stability_bound(directions, t)
        floor_bound = max(floor_bound, stable)
        assert m0 >= stable, (directions, t, m0, stable)
        candidates = [(A*m0+1, floors[0]+1),
                      (B*m0, floors[1]+1),
                      (C*m0+1, floors[2]+1)]
        v_num, v_den = candidates[0]
        for num, den in candidates[1:]:
            if num*v_den > v_num*den:
                v_num, v_den = num, den
        low, _ = theta_errors(H*m0-1, t, root_scale=root_scale)
        _, up = theta_errors(v_num, v_den, root_scale=root_scale)
        contribution = ((1-low)*Fraction(H*m0-1, t*m0)
                        - (1+up)*Fraction(v_num, v_den*m0))
        if contribution <= 0:
            continue
        positive += 1
        largest = t
        total += contribution.numerator*scale//contribution.denominator
    ell = Fraction(total, scale)
    assert ell > 0
    return {
        'A': A, 'B': B, 'C': C, 'directions': list(directions),
        'terms': terms, 'm0': m0, 'rounding_denominator': scale,
        'root_scale': root_scale, 'eligible_terms': eligible,
        'positive_terms': positive, 'largest_positive_t': largest,
        'floor_stability_bound': floor_bound, 'ell_lower': str(ell),
        'theta_mode': 'broadbent_johnston_yang',
        'source': 'BFT Lemma 5.2 and retained small-x theta lower bound; Broadbent et al. Corollary 2.1 and final global theta table; Johnston--Yang Lemma 2.2',
        'finite_RH_range_patched': True,
        'conclusion': 'For every integer m>=m0, both coefficient gcds are at least exp(ell_lower*m).',
    }


if __name__ == '__main__':
    import json
    import sys
    A, B, C = map(int, sys.argv[1:4])
    m0 = int(sys.argv[4]) if len(sys.argv) > 4 else 10**8
    terms = int(sys.argv[5]) if len(sys.argv) > 5 else 4000
    print(json.dumps(gcd_exponent_lower(A, B, C, m0=m0, terms=terms), indent=2))
