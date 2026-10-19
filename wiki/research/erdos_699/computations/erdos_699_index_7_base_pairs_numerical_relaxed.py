"""Numerical source thresholds for the five relaxed initial index-seven pair edges.

These certificates use rational residual blocks.  Under the two cofactor
upper bounds the positive-part denominator cost is at most the recorded
rational value.  The retained uniform coefficient-gcd bound and the exact
finite-constant Pade estimate contradict that upper bound above the cap.

The source threshold is numerical; this file does not exclude the finite
range below it or prove the whole index-seven assertion.
"""
import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

from erdos_699_off_diagonal_gcd_numeric import gcd_exponent_lower
from erdos_699_off_diagonal_explicit_clauses import joint_clause_threshold

DATA = Path(__file__).with_suffix('.json')
EXPECTED_EDGES = [(2,3,2920,2920), (2,3,3295,2915),
                  (2,5,2675,2710), (2,5,2678,2678), (3,5,2561,3773)]


def certify(data, replay_bootstrap=False):
    theta = None
    if replay_bootstrap:
        from erdos_699_off_diagonal_gcd_bootstrap import bootstrap, PrimeLogIntervals
        theta = PrimeLogIntervals()
        assert theta.metadata == data["prime_log_certificate"]
    assert [tuple(row['edge']) for row in data['records']] == EXPECTED_EDGES
    caps = []
    for row in data['records']:
        p,q,a,b = row['edge']
        targets = {str(p):Fraction(a,10000), str(q):Fraction(b,10000)}
        assert {p:Fraction(v) for p,v in row['targets'].items()} == targets
        clause = row['clause']
        source = clause['source']
        assert clause['product_degree'] == 1
        assert all(multiplicity == 1 for _,_,multiplicity,_ in clause['components'])
        assert {str(p) for p,_,_,_ in clause['components']} == set(targets)
        cost = sum((max(Fraction(0),Fraction(value)+targets[p])
                    for p,value in clause['positive_part_intercepts'].items()), Fraction(0))
        assert cost == Fraction(row['boxed_positive_part_upper_bound'])
        assert cost < Fraction(clause['positive_part_threshold'])
        analytic = row['analytic_gcd_certificate']
        lower_function = gcd_exponent_lower
        mode = {'theta_mode':analytic.get('theta_mode','fixed')}
        if analytic.get('theta_mode') == 'broadbent_johnston_yang':
            from erdos_699_off_diagonal_gcd_sharp import gcd_exponent_lower as lower_function
            mode = {}
        regenerated = lower_function(*analytic['directions'],
            terms=analytic['terms'], m0=analytic['m0'],
            scale=analytic['rounding_denominator'], root_scale=analytic['root_scale'],
            **mode)
        assert analytic['directions'] == source['directions']
        assert Fraction(analytic['requested_log_rate']) == Fraction(source['gcd_log_rate'])
        assert regenerated['ell_lower'] == analytic['ell_lower']
        assert Fraction(analytic['ell_lower']) > Fraction(source['gcd_log_rate'])
        gcd_start = analytic['m0']
        if 'finite_gcd_certificate' in row:
            finite = row['finite_gcd_certificate']
            assert finite['analytic_gcd_certificate'] == analytic
            assert finite['finite_interval_end'] == gcd_start-1
            assert Fraction(finite['minimum_margin']) > 0
            assert Fraction(finite['requested_log_rate']) == Fraction(source['gcd_log_rate'])
            assert finite['finite_interval_start'] <= finite['finite_interval_end']
            gcd_start = finite['finite_interval_start']
            if replay_bootstrap:
                replayed = bootstrap(analytic, theta, terms=finite['terms'])
                assert {k:v for k,v in replayed.items() if k != 'elapsed_seconds'} == {k:v for k,v in finite.items() if k != 'elapsed_seconds'}
        numeric = joint_clause_threshold(clause, gcd_start, gap=6, maximum_shift=6)
        assert {k:v for k,v in numeric.items() if k != 'conclusion'} == {k:v for k,v in row['numerical_threshold'].items() if k != 'conclusion'}
        caps.append(numeric['threshold_power_of_ten'])
    assert max(caps) == data['maximum_threshold_power_of_ten']
    return {'pair_caps':[[list(edge),cap]for edge,cap in zip(EXPECTED_EDGES,caps)],
            'maximum_threshold_power_of_ten':max(caps),
            'conclusion':'Each initial pair alternative is valid whenever h=n-6 exceeds its displayed numerical threshold.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--replay-bootstrap', action='store_true')
    args = parser.parse_args()
    print(json.dumps(certify(json.loads(DATA.read_text()), args.replay_bootstrap), indent=2))
