"""Directed growth bounds for unequal-block BFT Pade approximants.

Directions (A,B,C) mean Pade indices (Am,Bm-1,Cm), with adjacent
(Am+1,Bm-2,Cm+1). Thus the prime-power blocks have lengths A+B and B+C.
The finite rational gcd sum yields an effective, unevaluated starting index.
See ../methods/details/off_diagonal_pade.md for the integer argument.
"""
from fractions import Fraction
import json
from pathlib import Path

from mpmath import iv

iv.dps = 80


def rational(value):
    value = Fraction(value)
    return iv.mpf(value.numerator) / value.denominator


def gcd_partial_sum(A, B, C, terms):
    assert min(A, B, C, terms) > 0
    H = A + B + C
    total = Fraction(0)
    eligible = []
    for t in range(1, terms + 1):
        floors = [v * t // H for v in (A, B, C)]
        if sum(floors) != t - 2:
            continue
        assert all(v * t % H for v in (A, B, C))
        upper = Fraction(H, t)
        lower = max(Fraction(v, f + 1) for v, f in zip((A, B, C), floors))
        assert upper > lower
        total += upper - lower
        eligible.append(t)
    return total, eligible


def gcd_partial_lower(A, B, C, terms, scale=10**12):
    """A fixed-denominator lower bound for long finite prime-interval sums."""
    assert min(A, B, C, terms, scale) > 0
    H = A + B + C
    total = 0
    eligible = []
    for t in range(1, terms + 1):
        floors = [v*t//H for v in (A, B, C)]
        if sum(floors) != t-2:
            continue
        assert all(v*t % H for v in (A, B, C))
        lower = max((Fraction(v, f+1) for v, f in zip((A,B,C), floors)))
        numerator = H*lower.denominator-t*lower.numerator
        denominator = t*lower.denominator
        assert numerator > 0
        total += numerator*scale//denominator
        eligible.append(t)
    return Fraction(total, scale), eligible


def growth_parameters(P, Q, seed_a, seed_b, A, B, C, ell, terms=200,
                      sum_scale=None):
    """Return rigorous intervals c0,k0 and JSON-ready source parameters."""
    assert min(P, Q, seed_a, seed_b, A, B, C) > 0
    T, Z = seed_a * P, seed_b * Q
    delta = T - Z
    assert delta > 0
    ell = Fraction(ell)
    gcd_sum, eligible = (gcd_partial_sum(A,B,C,terms) if sum_scale is None else
                         gcd_partial_lower(A,B,C,terms,sum_scale))
    assert 0 < ell < gcd_sum
    z = rational(Fraction(delta, T))
    H = A + B + C
    entropy = (H * iv.log(H) - A * iv.log(A)
               - B * iv.log(B) - C * iv.log(C))
    tq = B * (2 - z) + C + A * (1 - z)
    uq = 2 * B / (tq + iv.sqrt(tq * tq - 4 * (1 - z) * H * B))
    te = A * (1 + z) + C + B * z
    ue = 2 * A / (te + iv.sqrt(te * te - 4 * z * H * A))
    assert 0 < uq < 1 and 0 < ue < 1
    log_q = (entropy + B * iv.log(uq) + C * iv.log(1 - uq)
             + A * iv.log(1 - (1 - z) * uq))
    log_e = (entropy + A * iv.log(ue) + C * iv.log(1 - ue)
             + B * iv.log(1 - z * ue))
    left_block, right_block = A + B, B + C
    c0 = (left_block * iv.log(P) - right_block * iv.log(seed_b)
          - A * iv.log(T) - log_q + rational(ell))
    k0 = (left_block * iv.log(P) + right_block * iv.log(Q)
          - B * iv.log(T) - (A + C) * iv.log(delta) - log_e
          + rational(ell))
    assert c0 > 0 and k0 > 0
    record = {
        "seed": {"P": P, "Q": Q, "a": seed_a, "b": seed_b, "difference": delta},
        "directions": [A, B, C],
        "left_block": left_block, "right_block": right_block,
        "gcd_terms": terms, "gcd_eligible_t": eligible,
        "gcd_partial_sum": str(gcd_sum), "gcd_log_rate": str(ell),
        "gcd_sum_rounding_denominator": sum_scale,
        "gcd_strict_margin": str(gcd_sum - ell),
        "height_scope": "Effectively computable threshold; not numerically evaluated.",
        "intervals": {name: iv.nstr(value, 35) for name, value in {
            "q_saddle": uq, "e_saddle": ue, "log_Q_rate": log_q,
            "log_E_rate": log_e, "first_decay_rate": c0,
            "second_decay_rate": k0,
            "first_decay_per_right_block": c0 / right_block,
            "second_decay_per_right_block": k0 / right_block,
        }.items()},
    }
    return c0, k0, record


def certify_847_845():
    _, k0, record = growth_parameters(847, 845, 1, 1, 39, 7, 33, 3)
    sides = [(7, 1, 46), (11, 2, 46), (5, 1, 40), (13, 2, 40)]
    targets = {5: Fraction(721, 1000), 7: Fraction(612, 1000),
               11: Fraction(44, 1000), 13: Fraction(111, 1000)}
    alpha = {p: 1 - 2 * power * block * iv.log(p) / k0 for p, power, block in sides}
    for p, target in targets.items():
        assert alpha[p] > rational(target + Fraction(1, 10000))
    record.update({
        "equal_position_sums": [[7, 11], [5, 13]],
        "position_scope": "Four distinct positions with equal sums; product difference nonzero.",
        "product_degree": 2,
        "left_prime_powers": {"7": 1, "11": 2},
        "right_prime_powers": {"5": 1, "13": 2},
        "targets": {str(p): str(t) for p, t in sorted(targets.items())},
        "limiting_exponents": {str(p): iv.nstr(v, 35) for p, v in sorted(alpha.items())},
        "strict_margin": "1/10000",
    })
    return record


def main():
    result = {"records": [certify_847_845()]}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
