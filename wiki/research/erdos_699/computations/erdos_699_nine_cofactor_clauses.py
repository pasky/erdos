"""Check the directed rational cofactor clauses retained for index nine.

The source catalogue records conditional Padé estimates only. Whole-index
coverage is checked separately. Each source uses the finite coefficient-gcd
lower sum and the exact, outward-rounded clause generator.
"""
from fractions import Fraction
import gzip
import json
from pathlib import Path

from erdos_699_off_diagonal_clauses import rational_joint_clause

DATA = Path(__file__).with_suffix('.json.gz')
PRIMES = (2, 3, 5, 7)


def applicable(record, positions):
    """Check the integer position identity required by this source.

    Equal-position pairs are conservatively omitted. Their prime cofactors
    have additional collision inequalities, supplied by the coverage proof.
    """
    assert len(positions) == len(PRIMES)
    r = dict(zip(PRIMES, positions))
    hypothesis = record['hypothesis']
    kind = hypothesis['kind']
    if kind == 'pair':
        primes = [int(p) for p in record['certificate']['positive_part_intercepts']]
        return len({r[p] for p in primes}) == len(primes)
    if kind == 'ap':
        p, q = hypothesis['endpoints']
        return r[p] != r[q] and r[p] + r[q] == 2*r[hypothesis['middle']]
    if kind == 'four':
        (p, q), (a, b) = hypothesis['groups']
        return (r[p] + r[q] == r[a] + r[b]
                and sorted((r[p], r[q])) != sorted((r[a], r[b])))
    raise ValueError(kind)


def verify(record):
    certificate = record['certificate']
    source = certificate['source']
    seed = source['seed']
    rebuilt = rational_joint_clause(
        (seed['P'], seed['Q'], seed['a'], seed['b']),
        source['directions'], Fraction(source['gcd_log_rate']),
        certificate['components'], degree=certificate['product_degree'],
        terms=source['gcd_terms'], block=Fraction(certificate['block_parameter']),
        scale=certificate['rounding_scale'],
    )
    assert rebuilt == certificate, record['id']
    assert all(component[0] in PRIMES for component in certificate['components'])
    assert record['hypothesis']['kind'] in ('pair', 'ap', 'four')
    assert Fraction(certificate['positive_part_threshold']) > 0


def main():
    with gzip.open(DATA, 'rt') as handle:
        data = json.load(handle)
    assert data['index'] == 9
    names = set()
    for row in data['records']:
        assert row['id'] not in names
        names.add(row['id'])
        verify(row)
    print(json.dumps({'verified_sources': len(names),
                      'scope': 'Conditional estimates above effective source thresholds.'}))


if __name__ == '__main__':
    main()
