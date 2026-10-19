"""The fifteen initial index-nine target boxes for sparse height covers.

The eleven pair families come from the retained initial-source certificate.
Each AP uses a new off-diagonal family with directions (d,c-d,d), where
the retained BFT seed is (P,Q,a,b,c,d). Its old coefficient-gcd certificate
is not used for this new adjacent pair. A sparse-cover driver must supply
the actual gcd lower bound from PointwiseGcdLower.

The original AP tail remains valid: both arguments exclude precisely the
same target box under the same arithmetic-progression hypothesis.
"""

from fractions import Fraction
import json
from pathlib import Path

from erdos_699_off_diagonal_boxed_sparse import prepare_box
from erdos_699_off_diagonal_clauses import rational_joint_clause

HERE = Path(__file__).resolve().parent
INPUT = HERE/'erdos_699_index_9_initial_relaxed_numerical.json'
AP_RATES = {
    'erdos_699_ap_cofactors.json:choices:0': '3',
    'erdos_699_ap_cofactors.json:choices:1': '6/5',
    'erdos_699_ap_cofactors.json:choices:3': '11/10',
    'erdos_699_additional_product_cofactors.json:choices:10': '52/5',
}


def ap_family(row):
    """Prepare valid polynomial constants, independently of the target box."""
    old = row['numerical_product_bound']
    P, Q, a, b, c, d = old['seed']
    directions = (d, c-d, d)
    assert min(directions) > 0
    components = [component[:4] for component in old['components']]
    assert old['degree'] == 2
    assert {str(p): str(target) for p, power, mult, side, target in old['components']} == row['targets']
    # The constructor checks this rational proposal against the new
    # off-diagonal finite prime-interval sum and verifies both growth
    # rates. No AP gcd starting index is inherited here.
    rate = Fraction(AP_RATES[row['id']])
    certificate = rational_joint_clause(
        (P, Q, a, b), directions, rate, components, degree=2,
        terms=4000, scale=10**12, gcd_sum_scale=10**12)
    certificate['source'].pop('gcd_eligible_t', None)
    return certificate


def source_jobs():
    """Return fifteen JSON-ready jobs, including their validated tail caps."""
    data = json.loads(INPUT.read_text())
    assert data['index'] == 9 and len(data['records']) == 15
    jobs = []
    for row in data['records']:
        kind = row['kind']
        if kind == 'pair':
            p, q, a, b = row['edge_scaled']
            targets = {str(p): str(Fraction(a, 10000)), str(q): str(Fraction(b, 10000))}
            certificate = row['clause']
            gap = 8
            hypothesis = {'kind': 'pair', 'primes': [p, q]}
            family_note = 'Retained pair polynomial family; pointwise gcd required for each sparse witness.'
        else:
            assert kind == 'ordinary_ap'
            certificate = ap_family(row)
            targets = {p: str(Fraction(value)) for p, value in row['targets'].items()}
            gap = 16
            hypothesis = row['hypothesis']
            family_note = ('New off-diagonal directions (d,c-d,d), adjacent shifts '
                           '(0,-1,0) and (1,-2,1); the old BFT gcd certificate is not reused.')
        jobs.append({
            'source_id': row['id'], 'kind': kind,
            'certificate': certificate, 'targets': targets,
            'directions': certificate['source']['directions'],
            'gap': gap, 'maximum_shift': 8, 'hypothesis': hypothesis,
            'height_variable': 'h=n-8',
            'tail_height_power_of_ten': row['threshold_power_of_ten'],
            'provenance': {
                'file': INPUT.name, 'record_id': row['id'],
                'family': family_note,
                'tail': 'The retained numerical target-box exclusion with exactly these targets and hypothesis.',
            },
        })
    assert sum(job['kind'] == 'pair' for job in jobs) == 11
    assert sum(job['kind'] == 'ordinary_ap' for job in jobs) == 4
    assert len({job['source_id'] for job in jobs}) == 15
    return jobs


def prepare_jobs():
    """Add exact directed constants for the boxed sparse witness checker."""
    jobs = source_jobs()
    for job in jobs:
        job['prepared'] = prepare_box(
            job['certificate'], job['targets'], source_id=job['source_id'],
            gap=job['gap'], maximum_shift=job['maximum_shift'])
    return jobs


if __name__ == '__main__':
    jobs = prepare_jobs()
    print(json.dumps({
        'source_count': len(jobs),
        'direction_count': len({tuple(job['directions']) for job in jobs}),
        'jobs': [{key: job[key] for key in
                  ('source_id', 'kind', 'targets', 'directions', 'gap',
                   'maximum_shift', 'tail_height_power_of_ten')}
                 for job in jobs],
    }, indent=2))
