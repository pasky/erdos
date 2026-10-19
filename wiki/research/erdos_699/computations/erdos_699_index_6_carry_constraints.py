"""Exact column restrictions in the difficult index-six cofactor region.

The explicit coordinate product F3 needs no interpolation or rank computation.
All threshold comparisons below are rational or integer comparisons. The
finite valuation examples illustrate the general factorial identity; they
are not a search for bad triples.
"""
from fractions import Fraction as F
from math import comb, factorial, prod
from pathlib import Path
import json


def vp(number, prime):
    assert number > 0 and prime >= 2
    value = 0
    while number % prime == 0:
        number //= prime
        value += 1
    return value


def column_identity(n, j, prime, r):
    A = vp(n-r, prime)
    P = prime**A
    assert P > r and r < j <= n
    u = (n-r)//P
    J = (j-r-1)//P
    B = comb(n, j)
    falling = prod(j-s for s in range(r+1))
    right = A+vp(factorial(r), prime)+vp(comb(u-1, J), prime)
    assert vp(B, prime)+vp(falling, prime) == right
    assert prime**right <= prime**vp(factorial(r), prime)*(n-r)
    b = j % P
    if b <= r:
        assert prime**vp(B, prime) <= prime**vp(comb(r, b), prime)*u
    return {'n': n, 'j': j, 'prime': prime, 'r': r, 'row_power': P,
            'cofactor': u, 'column_valuation': vp(B, prime),
            'falling_factorial_valuation': vp(falling, prime),
            'low_residue_branch': b <= r}


def report():
    positions = {2: 2, 3: 1, 5: 0}
    lower = {2: F(31, 100), 3: F(9, 25), 5: F(31, 100)}
    h = [3, 2, 1, 0, 0, 0]
    m = [6, 5, 4, 3, 2, 1]
    for t in range(6):
        assert min(h[x]+h[t-x] for x in range(t+1)) == m[t]
    degree = 2*sum(h)
    assert degree == 12 and sum(m)-degree == 9
    C0 = factorial(5)**max(m)
    records = []
    for p in (2, 3, 5):
        power = m[positions[p]]
        other = [q for q in (2, 3, 5) if q != p]
        exponent = F(sum(m)-degree)-sum((1-lower[q])*m[positions[q]] for q in other)
        constant = C0*2**sum(m[positions[q]] for q in other)
        effective_loss = F(2, 5) if p != 5 else F(1, 2)
        gain = exponent-power*effective_loss
        low_constant = constant*(2**power if p == 2 else 2**(power//2) if p == 5 else 1)
        records.append({'prime': p, 'overlap_power': power,
                        'height_exponent': str(exponent),
                        'constant': constant,
                        'limiting_overlap_exponent': str(exponent/power),
                        'low_branch_gain': str(gain),
                        'low_branch_constant': low_constant})
    assert [F(r['height_exponent']) for r in records] == [F(83, 50), F(21, 10), F(76, 25)]
    assert [F(r['low_branch_gain']) for r in records] == [F(3, 50), F(1, 10), F(1, 25)]
    H = 425
    assert C0*2**15 < 10**17
    assert all(r['low_branch_constant'] <= C0*2**15 for r in records)
    assert all(H*F(r['low_branch_gain']) >= 17 for r in records)
    C5 = records[2]['constant']
    # Both u5 and the 5-part of j are at most 2*C5^(1/6)*h^(37/75).
    assert (2**6*C5)**25 < 10**H
    assert C5**25 < 10**H
    examples = [column_identity(*x) for x in
                ((18, 7, 2, 2), (50, 17, 2, 2), (28, 10, 3, 1),
                 (125, 40, 5, 0), (130, 35, 5, 0))]
    return {'index': 6, 'scope': 'Conditional column restrictions, not whole-index effectivity.',
            'height_variable': 'h=n-5', 'height_threshold_power_of_ten': H,
            'selected_positions': {str(p): r for p, r in positions.items()},
            'lower_cofactor_exponents': {str(p): str(e) for p, e in lower.items()},
            'additional_upper_exponents_for_2_and_3': '2/5',
            'line_exponents': h, 'row_multiplicities': m, 'polynomial_degree': degree,
            'overlap_bounds': records, 'valuation_identity_examples': examples,
            'matrix_ranks_used': False}


if __name__ == '__main__':
    result = report()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'height_threshold_power_of_ten': 425,
                      'low_branch_gains': [r['low_branch_gain'] for r in result['overlap_bounds']],
                      'matrix_ranks_used': False, 'whole_index_effective': False}))
