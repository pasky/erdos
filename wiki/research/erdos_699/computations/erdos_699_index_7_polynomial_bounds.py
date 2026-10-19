#!/usr/bin/env python3
"""Sharper algebraic height for the retained index-seven proof.

Uses exact row-dependent Hadamard bounds and each retained Farkas margin.
The modular ranks and analytic source claims are the previously retained
certificates. This checks the new integer bounds and all rational leaves;
it does not repeat the modular ranks or evaluate the analytic thresholds.
"""
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import argparse
import json
from math import comb
from pathlib import Path

import erdos_699_index_7_effective as original

HERE = Path(__file__).parent
DATA = Path(__file__).with_suffix('.json')


def ceiling_log10(value):
    assert type(value) is int and value > 0
    candidate = len(str(value)) - 1
    return candidate if value == 10**candidate else candidate + 1


@lru_cache(None)
def monomial_jet_bound(degree, x, y, a, b):
    """Maximum unsigned Hasse coefficient over monomials of degree <=d.

    Coordinates are nonnegative integers with x<=y. Away from the origin,
    increasing a monomial exponent on a nonzero coordinate cannot reduce
    its Hasse coefficient, so the maximum occurs in degree d.
    """
    assert 0 <= x <= y and 0 <= a+b <= degree
    if not y:
        return 1
    if not x:
        return comb(degree-a, b)*y**(degree-a-b)
    return max(comb(k, a)*comb(degree-k, b)*x**(k-a)*y**(degree-k-b)
               for k in range(a, degree-b+1))


@lru_cache(None)
def newton_jet_tables(degree, index, roots):
    """Hasse coefficients for the monic integer basis with periodic roots.

    f_a(X)=product_{0<=k<a}(X-roots[k % len(roots)]). The triangular
    change from monomials is integral with diagonal one, in every degree.
    Prefix maxima let us bound every product with combined degree <=d.
    """
    values, prefixes = [], []
    for x in range(index):
        rows = [[1]]
        for degree_now in range(1, degree+1):
            old = rows[-1]
            constant = x-roots[(degree_now-1) % len(roots)]
            rows.append([constant*old[0]]+[
                constant*(old[a] if a < len(old) else 0)+old[a-1]
                for a in range(1, degree_now+1)])
        values.append(rows)
        table = []
        for order in range(degree+1):
            sequence, largest = [0]*order, 0
            for degree_now in range(order, degree+1):
                largest = max(largest, abs(rows[degree_now][order]))
                sequence.append(largest)
            table.append(sequence)
        prefixes.append(table)
    return values, prefixes


def polynomial_bounds_in_basis(record, roots=None):
    d, r = record['interpolation_degree'], record['symmetric_jet_count']
    if not r:
        return {'name': record['name'], 'minor_power_of_ten': 0,
                'coefficient_power_of_ten': original.coefficient_exponent(record),
                'common_zero_power_of_ten': 0}
    h, m = record['line_exponents'], record['row_multiplicities']
    q = record.get('row_line_exponents', [0]*7)
    diagonal = record.get('diagonal_power', 0)
    minor_power, row_count = 0, 0
    if roots is not None:
        values, prefixes = newton_jet_tables(d, 7, tuple(roots))
    digest = sha256()
    for t in range(7):
        for x in range(t//2+1):
            y = t-x
            residual = max(0, m[t]-h[x]-h[y]-q[t]-(diagonal if x == y else 0))
            for order in range(residual):
                for a in range(order+1):
                    b = order-a
                    if x == y and a > b:
                        continue
                    if roots is None:
                        entry = 2*monomial_jet_bound(d, x, y, a, b)
                    else:
                        entry = 2*max(abs(values[x][z][a])*prefixes[y][b][d-z]
                                      for z in range(a, d-b+1))
                    assert entry > 0
                    power = (ceiling_log10(r*entry*entry)+1)//2
                    assert r*entry*entry <= 10**(2*power)
                    # Every r-column minor has this row norm bound.
                    minor_power += power
                    row_count += 1
                    digest.update(f'{x}:{y}:{a}:{b}:{power}\n'.encode())
    assert row_count == r
    basis_norm_power = 0 if roots is None else ceiling_log10((1+max(roots))**d)
    coefficient = original.coefficient_exponent(record)-r*(d+6)+minor_power+basis_norm_power
    basepoint = 0
    if record.get('nonvanishing_method') == 'coprime_kernel':
        s = record['symmetric_monomial_count']
        # All r-minors, including Cramer replacements, have norm <=10**P.
        assert 2*s*(s+1)*record['modular_prime'] < 10**20
        lifted_norm = minor_power+basis_norm_power+20
        # The established resultant argument uses actual X-degrees <=d.
        basepoint = 2*d*(lifted_norm+d+8)+2
    return {'name': record['name'], 'jet_count': row_count,
            'basis': 'monomial' if roots is None else 'monic periodic Newton',
            'basis_roots': roots, 'basis_norm_power_of_ten': basis_norm_power,
            'row_bounds_sha256': digest.hexdigest(),
            'minor_power_of_ten': minor_power,
            'coefficient_power_of_ten': coefficient,
            'common_zero_power_of_ten': basepoint}


def polynomial_bounds(record):
    candidates = [polynomial_bounds_in_basis(record),
                  polynomial_bounds_in_basis(record, [0, 1, 2, 3, 4])]
    return min(candidates, key=lambda row: row['coefficient_power_of_ten'])


def certify():
    source = original.DATA
    proof = json.loads(source.read_text())
    # Reconstruct exact complete coverage; no rank or analytic work repeated.
    coverage = original.check_forest(proof)
    import erdos_699_index_7_nonvanishing as nonvanishing
    arithmetic_nonvanishing = nonvanishing.verify()
    assert arithmetic_nonvanishing['selected_columns'] == [0, 1, 2]
    polynomials = proof['polynomials']
    bounds = [polynomial_bounds(p) for p in polynomials]
    delta = Fraction(proof['polynomial_slack'])
    worst = (Fraction(0), None)
    leaf_count = 0
    for root_number, root in enumerate(proof['forest']):
        stack = [('', root['tree'])]
        while stack:
            path, node = stack.pop()
            if 'farkas' not in node:
                stack.extend((path+'/'+mask, child)
                             for mask, child in sorted(node['children'].items()))
                continue
            certificate = node['farkas']
            terms = [(k, Fraction(weight)) for k, weight in zip(
                certificate['support'], certificate['multipliers']) if k < len(polynomials)]
            alpha = -Fraction(certificate['weighted_rhs'])+delta*sum(w for k, w in terms)
            constant = sum(w*bounds[k]['coefficient_power_of_ten'] for k, w in terms)
            assert alpha > 0
            ratio = constant/alpha
            if ratio > worst[0]:
                worst = (ratio, {'root': root_number, 'path': path,
                                 'positions': root['positions'], 'vector': root['vector'],
                                 'margin_without_slack': str(alpha),
                                 'weighted_coefficient_power': str(constant)})
            leaf_count += 1
    assert leaf_count == coverage['leaves']
    weighted_cap = worst[0].numerator//worst[0].denominator+1
    collision = proof['collision_certificate']
    collision_bound = polynomial_bounds(collision)
    m = collision['row_multiplicities']
    collision_gain = sum(m)-original.total_degree(collision)-m[0]-m[1]
    assert collision_gain > 0
    collision_cap = collision_bound['coefficient_power_of_ten']//collision_gain+1
    previous_common_zero = max(b['common_zero_power_of_ten'] for b in bounds)
    assert {p['name'] for p in polynomials
            if p.get('nonvanishing_method') == 'coprime_kernel'} == {'poly_coprime_last'}
    # This sole coprime-kernel record now has arithmetic nonvanishing everywhere
    # outside the grid, using three sections with the same coefficient bound.
    common_zero = 0
    algebraic_cap = max(weighted_cap, common_zero, collision_cap, 10)
    return {'index': 7, 'height_variable': 'h=n-6',
            'input_file': source.name,
            'coverage': coverage, 'polynomial_bounds': bounds,
            'collision_bound': collision_bound, 'collision_gain': collision_gain,
            'collision_power_of_ten': collision_cap,
            'largest_weighted_ratio': str(worst[0]), 'worst_leaf': worst[1],
            'weighted_coefficient_power_of_ten': weighted_cap,
            'maximum_common_zero_power_of_ten': common_zero,
            'former_resultant_power_with_newton_basis': previous_common_zero,
            'arithmetic_nonvanishing': arithmetic_nonvanishing,
            'nonvanishing_certificate_file': nonvanishing.DATA.name,
            'algebraic_height_power_of_ten': algebraic_cap,
            'previous_algebraic_height_power_of_ten': 19813540001,
            'conclusion': 'All polynomial and common-zero estimates used in the index-seven proof hold above the displayed algebraic height; analytic thresholds must also be included.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = certify()
    if args.write:
        DATA.write_text(json.dumps(result, indent=2)+'\n')
    else:
        assert json.loads(DATA.read_text()) == result
    print(json.dumps({k: v for k, v in result.items() if k != 'polynomial_bounds'}, indent=2))


if __name__ == '__main__':
    main()
