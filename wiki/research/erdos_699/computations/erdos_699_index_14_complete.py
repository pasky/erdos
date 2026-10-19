"""Bind the proved numerical tail and complete finite range at index fourteen.

The two constituent checkers reproduce their analytic/coverage calculations.
This small checker verifies that their source files are present and that
their ranges overlap.
"""

import json
from pathlib import Path


def main():
    directory = Path(__file__).parent
    tail_path = directory / 'erdos_699_index_14_numerical_tail.json'
    finite_path = directory / 'erdos_699_index_14_finite.json'
    tail_data = json.loads(tail_path.read_text())
    tail = tail_data['certificate']
    finite = json.loads(finite_path.read_text())
    assert tail['index'] == finite['i'] == 14
    assert tail['complete_row_cap_power_of_ten'] <= finite['supplied_tail_power_of_ten']
    assert tail['complete_row_cap_power_of_ten'] == 8_516_269
    assert finite['supplied_tail_power_of_ten'] == 15_170_264
    for family in ('source_files', 'bootstrap_files'):
        for name in tail[family]:
            assert (directory/name).is_file(), name
    polynomial = directory / tail_data['polynomial_certificate_file']
    assert polynomial.is_file(), polynomial.name
    for source in finite['source_certificates']:
        assert (directory/source['file']).is_file(), source['file']
    assert finite['certified_intervals'] == finite['total_partition_leaves'] == 400_818
    assert finite['exact_singleton_rows'] == [] and finite['exact_columns_checked'] == 0
    result = {
        'index': 14,
        'numerical_tail_power_of_ten': tail['complete_row_cap_power_of_ten'],
        'certified_finite_range_power_of_ten': finite['supplied_tail_power_of_ten'],
        'inclusive_interval_cap_power_of_ten': finite['inclusive_interval_cap_power_of_ten'],
        'certified_intervals': finite['certified_intervals'],
        'minimum_certified_log_margin': finite['minimum_certified_log_margin'],
        'numerical_tail_file': tail_path.name,
        'finite_certificate_file': finite_path.name,
        'conclusion': 'No admissible bad triples exist at index fourteen.',
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
