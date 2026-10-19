"""Exact compatibility check for an unresolved index-eight cofactor profile.

This checks one abstract exponent/position profile against named retained
inequalities. It does not assert that any integer n realizes the profile,
that a bad triple exists, or that stronger inequalities cannot exclude it.
"""
from fractions import Fraction as F
import gzip
import json
from pathlib import Path

from erdos_699_nine_cofactor_clauses import applicable

ROOT = Path(__file__).parent
PRIMES = (2, 3, 5, 7)
POSITIONS = (1, 3, 0, 2)
EXPONENTS = {p: F(3, 10) for p in PRIMES}


def report():
    baseline = json.loads((ROOT/'erdos_699_index_9_baseline.json').read_text())
    pair_sources = json.loads((ROOT/'erdos_699_off_diagonal_pairs.json').read_text())
    pair_count = 0
    for p, q, a, b in baseline['pair_edges_scaled'] + pair_sources['edges_scaled']:
        if p not in EXPONENTS or q not in EXPONENTS:
            continue
        assert EXPONENTS[p] >= F(a, 10000) or EXPONENTS[q] >= F(b, 10000)
        pair_count += 1
    with gzip.open(ROOT/'erdos_699_nine_cofactor_clauses.json.gz', 'rt') as handle:
        sources = json.load(handle)['records']
    rational_margins = []
    for row in sources:
        if not applicable(row, POSITIONS):
            continue
        certificate = row['certificate']
        weights = {p: m for p, A, m, side in certificate['components']}
        value = sum((max(F(0), F(g)+weights[int(p)]*EXPONENTS[int(p)])
                     for p, g in certificate['positive_part_intercepts'].items()), F(0))
        margin = value-F(certificate['positive_part_threshold'])
        assert margin >= 0, row['id']
        rational_margins.append((margin, row['id']))
    ordinary_count = 0
    for filename in ('erdos_699_ap_cofactors.json', 'erdos_699_additional_product_cofactors.json'):
        source = json.loads((ROOT/filename).read_text())
        for kind, key in (('ap', 'choices'), ('four', 'four_factor_choices')):
            for row in source[key]:
                targets = {int(p): F(v) for p, v in row['targets'].items()}
                if not set(targets) <= set(PRIMES):
                    continue
                if kind == 'ap':
                    hypothesis = {'kind': kind, 'middle': row['middle_prime'],
                                  'endpoints': list(map(int, row['endpoint_powers']))}
                else:
                    hypothesis = {'kind': kind, 'groups': row['equal_position_sums']}
                if not applicable({'hypothesis': hypothesis}, POSITIONS):
                    continue
                assert any(EXPONENTS[p] >= value for p, value in targets.items())
                ordinary_count += 1
    extra = json.loads((ROOT/'erdos_699_nine_polynomial_cuts.json').read_text())
    polynomial_gains = []
    for row in baseline['certificates'] + extra['certificates']:
        degree = row['degree'] if 'degree' in row else row['certificate_degree']
        m = row['row_multiplicities']
        # Retaining an index-nine polynomial is legitimate for its first
        # eight grid rows, but the ninth row no longer contributes a divisor.
        gain = F(sum(m[:8])-degree) - sum((1-EXPONENTS[p])*m[r]
                                                    for p, r in zip(PRIMES, POSITIONS))
        assert gain <= 0, row['name']
        polynomial_gains.append((gain, row['name']))
    closest = min(rational_margins)
    best = max(polynomial_gains)
    return {
        'index': 8,
        'scope': 'An abstract profile compatible with specified retained inequalities; not an integer counterexample.',
        'prime_order': list(PRIMES), 'positions': list(POSITIONS),
        'cofactor_exponents': [str(EXPONENTS[p]) for p in PRIMES],
        'ordinary_pair_alternatives_checked': pair_count,
        'applicable_rational_clauses_checked': len(rational_margins),
        'smallest_rational_compatibility_margin': str(closest[0]),
        'closest_rational_clause': closest[1],
        'applicable_ordinary_product_alternatives_checked': ordinary_count,
        'transferred_index_nine_polynomials_checked': len(polynomial_gains),
        'largest_transferred_polynomial_gain': str(best[0]),
        'best_transferred_polynomial': best[1],
    }


if __name__ == '__main__':
    result = report()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
