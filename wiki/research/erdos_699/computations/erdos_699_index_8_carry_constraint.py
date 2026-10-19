"""A numerical conditional carry restriction at index eight.

For selected positions (r2,r3,r5,r7)=(1,3,0,2) and u2,u3,u5>=h**(3/10),
a bad triple with h=n-7>=10**850001 must have j mod 7**v7(n-2)>2.
The certificate uses the actual overlap E7=7**min(v7(n-2),v7(C(n,j))).
No whole-index effectivity assertion is made.
"""
from fractions import Fraction
from pathlib import Path
import argparse
import json

import erdos_699_index_13_interpolation_gcd as interpolation

DATA = Path(__file__).with_suffix('.json')


def verify(data, ranks=False):
    assert data['index'] == 8 and data['prime_order'] == [2, 3, 5, 7]
    assert data['selected_positions'] == [1, 3, 0, 2]
    h, m = data['line_exponents'], data['row_multiplicities']
    assert len(h) == len(m) == 8 and all(type(x) is int and x >= 0 for x in h+m)
    d, p = data['interpolation_degree'], data['modular_prime']
    assert p == 251 and d == 84
    interpolation.LINE_EXPONENTS = h
    interpolation.ROW_MULTIPLICITIES = m
    interpolation.residual = lambda x, y: max(0, m[x+y]-h[x]-h[y])
    interpolation.DEGREE = d
    interpolation.PRIME = p
    rows = interpolation.symmetric_jets()
    basis = interpolation.symmetric_basis()
    assert len(rows) == data['symmetric_jet_count'] == data['symmetric_rank'] == 1845
    assert len(basis) == data['symmetric_monomial_count'] == 1849
    if ranks:
        assert interpolation.jet_matrix(basis, rows).rank() == len(rows)
    degree = 2*sum(h)+d+1
    assert degree == data['polynomial_degree'] == 283
    other_loss = Fraction(7, 10)*(m[0]+m[1]+m[3])
    residual_power = Fraction(sum(m)-degree)-other_loss
    assert residual_power == Fraction(data['overlap_power_numerator']) == Fraction(367, 10)
    assert m[2] == data['overlap_power_denominator'] == 73
    gain = residual_power-Fraction(m[2], 2)
    assert gain == Fraction(data['gain_with_square_root_overlap']) == Fraction(1, 5)
    # A jet entry is below 2*8**d. Hadamard/adjugates and the generator
    # construction give log10 ||G||_1 < r*(d+6)+50. The remaining terms
    # bound H, (7!)**max(m), n<=2h, and the three cofactor corrections.
    constant = (len(rows)*(d+6)+50 + 2*sum(h) + 4*max(m)
                + degree + m[0]+m[1]+m[3])
    assert constant == data['integer_logarithmic_constant_bound'] == 167228
    assert constant < data['overlap_constant_power_of_ten'] == 169000
    assert 169000 + (m[2]+1)//2 < 170000
    H = data['height_threshold_power_of_ten']
    assert H == 850001 and H*gain > 170000
    alpha = residual_power/m[2]
    assert alpha == Fraction(367, 730)
    # From 7^v7(B)*[(j)_3]_7 <= n-2 and E7 <= 7^v7(B).
    assert Fraction(169000, m[2])+1 < (alpha-Fraction(1, 2))*H


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ranks', action='store_true',
                        help='Repeat the modular rank already computed at construction.')
    args = parser.parse_args()
    data = json.loads(DATA.read_text())
    verify(data, ranks=args.ranks)
    print(json.dumps({'conditional_index': 8, 'rank': [1845, 1849],
                      'ranks_recomputed': args.ranks,
                      'height_threshold_power_of_ten': 850001,
                      'gain': '1/5', 'whole_index_effective': False}))


if __name__ == '__main__':
    main()
