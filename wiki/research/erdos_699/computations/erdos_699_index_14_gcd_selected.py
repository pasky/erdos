"""Regenerate the 61 analytic gcd inputs used by the numerical i=14 proof."""

from fractions import Fraction
import json
from pathlib import Path

from erdos_699_off_diagonal_gcd_numeric import gcd_exponent_lower, normalized_edge


def main():
    directory = Path(__file__).parent
    source_path = directory/'erdos_699_off_diagonal_pairs.json'
    selection_path = directory/'erdos_699_index_14_numerical_tail.json'
    previous_path = directory/'erdos_699_off_diagonal_gcd_numeric.json'
    sources = {normalized_edge(row): row
               for row in json.loads(source_path.read_text())['records']}
    edges = sorted(set(map(tuple, json.loads(selection_path.read_text())['pair_edges_scaled'])) & sources.keys())
    assert len(edges) == 61
    cache = {}
    for row in json.loads(previous_path.read_text())['records']:
        cache[(tuple(row['directions']), row['requested_log_rate'])] = {
            key: value for key, value in row.items()
            if key not in ('edge', 'source_edge', 'requested_log_rate', 'strict_rate_margin')}
    records = []
    for edge in edges:
        source = sources[edge]
        target = Fraction(source['gcd_log_rate'])
        key = (tuple(source['directions']), str(target))
        if key not in cache:
            for exponent in range(6, 11):
                row = gcd_exponent_lower(*source['directions'], m0=10**exponent)
                if Fraction(row['ell_lower']) > target:
                    cache[key] = row
                    break
            else:
                raise AssertionError(('No numerical gcd bound found', edge))
        row = dict(cache[key])
        row.update({'edge': list(edge), 'source_edge': list(edge),
                    'requested_log_rate': str(target),
                    'strict_rate_margin': str(Fraction(row['ell_lower'])-target)})
        records.append(row)
    result = {
        'source_file': source_path.name,
        'selection_file': selection_path.name,
        'selected_edges': [list(e) for e in edges],
        'records': records,
    }
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'output': str(output), 'selected_sources': len(records),
                      'maximum_analytic_m0': max(r['m0'] for r in records)}))


if __name__ == '__main__':
    main()
