"""Complete index twelve using its numerical tail and finite pair certificates.

The numerical Padé source checker supplies the infinite tail. A retained
five-prime clique of exponent 1/3 reduces the finite range by the explicit
degree-72 ramp. Stronger 2/5 edges on that smaller range then feed the
existing interval checker, with exact gcd checks for residual small rows.
"""

from itertools import combinations
import json
from pathlib import Path

import erdos_699_window_intervals as windows
from erdos_699_weighted_ramps import certify


def main():
    directory = Path(__file__).parent
    tail_path = directory / 'erdos_699_off_diagonal_explicit_pairs.json'
    tail = json.loads(tail_path.read_text())
    tail_power = tail['complete_row_cap_power_of_ten']
    assert tail['index'] == 12 and tail_power == 3_071_170
    for field in ('ramp', 'source', 'gcd', 'bootstrap'):
        source = directory / tail[field + '_file']
        assert source.is_file(), source.name

    first = directory / 'erdos_699_prime_pair_strips_15.json'
    second = directory / 'erdos_699_prime_pair_strips_12.json'
    primes = (2, 3, 5, 7, 11)
    pairs = set(combinations(primes, 2))
    first_rows = [row for row in json.loads(first.read_text())['records']
                  if tuple(row['pair']) in pairs]
    assert {tuple(row['pair']) for row in first_rows} == pairs
    assert all(row['height_cap_power_of_ten'] >= tail_power
               and row['maximum_difference'] >= 11
               and row['reciprocal_exponent_denominator'] == 3
               for row in first_rows)
    ramp = certify(12, 8, [(*pair, 3333) for pair in sorted(pairs)],
                   'The retained finite five-prime clique of exponent 1/3.')
    cap_power = ramp['algebraic_cap_power_of_ten']
    assert cap_power == 43
    assert max(row['height_threshold'] + 11 for row in first_rows) < 10**cap_power
    second_rows = json.loads(second.read_text())['records']
    assert {tuple(row['pair']) for row in second_rows} == pairs
    assert all(row['height_cap_power_of_ten'] >= cap_power
               and row['maximum_difference'] >= 11
               and row['cofactor_exponent_numerator'] == 2
               and row['cofactor_exponent_denominator'] == 5
               for row in second_rows)

    original = windows.previous.reduced_cap

    def ramp_cap(index, selected_primes, constants, saving):
        assert index == 12 and tuple(selected_primes) == primes
        assert saving >= 13332
        ordinary, ordinary_power = original(index, selected_primes, constants, saving)
        return min(ordinary, 10**cap_power), min(ordinary_power, cap_power)

    windows.previous.reduced_cap = ramp_cap
    try:
        result = windows.run(12, tail_power, [first, second], 2_000_000, 10_000)
    finally:
        windows.previous.reduced_cap = original
    for source in result['source_certificates']:
        source['file'] = Path(source['file']).name
    result.update({
        'numerical_tail_file': tail_path.name,
        'weighted_ramp_reduction': ramp,
        'conclusion': 'No admissible bad triples exist at index twelve.',
    })
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: result[key] for key in (
        'i', 'supplied_tail_power_of_ten', 'inclusive_interval_cap_power_of_ten',
        'certified_intervals', 'minimum_certified_log_margin',
        'exact_singleton_rows', 'exact_columns_checked', 'conclusion')}, indent=2))


if __name__ == '__main__':
    main()
