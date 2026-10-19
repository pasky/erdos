"""A fully numerical index-fourteen bound from 64 selected pair sources.

The fixed interpolation matrix is the previously retained index-fourteen
certificate. This checks the new finite cofactor coverage, a sharper
Hadamard bound, and explicit starting heights for every selected source.
"""

import argparse
from fractions import Fraction
import json
from math import comb
from pathlib import Path

from erdos_699_index_14_effective import minimal_vectors
from erdos_699_off_diagonal_pairs import normalized_edge
from erdos_699_off_diagonal_explicit_pairs import pair_threshold
from erdos_699_weighted_ramps import capacities

HERE = Path(__file__).parent
DATA = Path(__file__).with_suffix('.json')
SCALE = 10000
PRIMES = (2, 3, 5, 7, 11, 13)


def certify(data):
    source_paths = [HERE/name for name in data['source_files']]
    bootstrap_paths = [HERE/name for name in data['bootstrap_files']]
    sources = {}
    for path in source_paths:
        for row in json.loads(path.read_text())['records']:
            sources[normalized_edge(row)] = row
    bootstraps = {}
    for path in bootstrap_paths:
        family = json.loads(path.read_text())
        assert (HERE/family['input_file']).is_file(), family['input_file']
        for row in family['records']:
            bootstraps[tuple(row['edge'])] = row
    edges = list(map(tuple, data['pair_edges_scaled']))
    assert len(edges) == len(set(edges)) == 64
    assert all(e in sources and e in bootstraps for e in edges)
    assert all(0 < a and 0 < b and a+b < SCALE for p, q, a, b in edges)
    vectors = minimal_vectors(PRIMES, edges)
    assert [list(v) for v in vectors] == data['minimal_vectors_scaled']

    polynomial_path = HERE/data['polynomial_certificate_file']
    polynomial = json.loads(polynomial_path.read_text())['certificate']
    h = tuple(polynomial['line_exponents'])
    m = tuple(polynomial['row_multiplicities'])
    D = polynomial['interpolation_degree']
    rank = polynomial['symmetric_rank']
    assert h == (33,29,26,22,19,15,10,5,0,0,0,0,0,0)
    assert m == (66,65,62,58,55,53,51,46,41,37,33,30,27,24)
    assert D == 56 and rank == 831
    assert polynomial['symmetric_jet_count'] == rank
    assert polynomial['symmetric_monomial_count'] == 841
    assert polynomial['modular_prime'] == 65521
    total_degree = 2*sum(h)+D+1
    assert total_degree == 375
    capacity_lists = {c for v in vectors for c in capacities(v)}
    gain, worst_capacity = min(
        (SCALE*(sum(m)-total_degree)-sum(a*b for a,b in zip(m,c)), c)
        for c in capacity_lists)
    assert gain == data['expected_gain_scaled'] == 112

    # Hasse jets of a symmetric monomial at coordinates <=13 have size
    # at most 2*(2*13)^56. This covers the sum of its two orientations.
    entry_bound = 2*26**D
    row_norm_power = 81
    assert rank*entry_bound**2 < 10**(2*row_norm_power)
    generator_factor = 1+(14*15//2+14+4)*comb(D+2,2)
    assert generator_factor < 10**7
    coefficient_power = (rank*row_norm_power+1+len(PRIMES)*m[0]
                         +2*13*m[0]+4*sum(h)+7)
    assert coefficient_power == 70067
    algebraic_cap = coefficient_power*SCALE//gain+1
    assert algebraic_cap*gain > coefficient_power*SCALE
    assert 2*max(sum(t*w for t,w in enumerate(m)),13) < 10**10

    numerical_sources = []
    for edge in edges:
        source, bootstrap = sources[edge], bootstraps[edge]
        analytic = bootstrap['analytic_gcd_certificate']
        assert source['directions'] == bootstrap['directions'] == analytic['directions']
        ell = Fraction(source['gcd_log_rate'])
        assert Fraction(bootstrap['requested_log_rate']) == ell
        assert Fraction(analytic['ell_lower']) > ell
        assert bootstrap['finite_interval_end'] == analytic['m0']-1
        assert bootstrap['finite_interval_start'] <= bootstrap['finite_interval_end']
        assert Fraction(bootstrap['minimum_margin']) > 0
        result = pair_threshold(
            source, edge, bootstrap['finite_interval_start'], gap=13,
            maximum_shift=13, separate_terms=True,
            integral_trim=Fraction(2, source['directions'][1]), near_limit=True)
        numerical_sources.append(result)
    largest = max(row['threshold_power_of_ten'] for row in numerical_sources)
    cap = max(algebraic_cap, largest+1)
    return {
        'index': 14, 'height_variable': 'h=n-13',
        'pair_alternatives': len(edges), 'minimal_vectors': len(vectors),
        'capacity_lists': len(capacity_lists), 'minimum_gain': str(Fraction(gain,SCALE)),
        'worst_capacities_scaled': list(worst_capacity),
        'matrix_entry_bound': str(entry_bound), 'row_norm_power_of_ten': row_norm_power,
        'coefficient_bound_power_of_ten': coefficient_power,
        'algebraic_power_of_ten': algebraic_cap,
        'maximum_pair_threshold_power_of_ten': largest,
        'complete_row_cap_power_of_ten': cap,
        'polynomial_certificate_file': polynomial_path.name,
        'source_files': [p.name for p in source_paths],
        'bootstrap_files': [p.name for p in bootstrap_paths],
        'numerical_sources': numerical_sources,
        'conclusion': 'Every bad triple at index fourteen has n below the displayed complete row cap.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    data = json.loads(DATA.read_text())
    result = certify(data)
    if args.write:
        data['certificate'] = result
        DATA.write_text(json.dumps(data, indent=2)+'\n')
    else:
        assert data['certificate'] == result
    print(json.dumps({key: value for key, value in result.items()
                      if key != 'numerical_sources'}, indent=2))


if __name__ == '__main__':
    main()
