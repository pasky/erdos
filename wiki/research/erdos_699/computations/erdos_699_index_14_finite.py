#!/usr/bin/env python3
"""Exclude all i=14 rows below 10^15170264, conditional on a separate tail.

A retained 1/3 clique first gives the degree-90 weighted-ramp cap 10^41.
The new exact 2/5 clique and exceptional-row windows then close that range.
The numerical infinite-tail theorem is deliberately a separate input.
"""
from itertools import combinations
import json
from pathlib import Path

import erdos_699_window_intervals as windows
from erdos_699_weighted_ramps import certify

DIRECTORY = Path(__file__).resolve().parent
TAIL_POWER = 15_170_264


def run():
    first = DIRECTORY/'erdos_699_prime_pair_strips_15.json'
    second = DIRECTORY/'erdos_699_prime_pair_strips_14.json'
    primes = (2,3,5,7,11,13)
    pairs = set(combinations(primes,2))
    first_rows = [r for r in json.loads(first.read_text())['records'] if tuple(r['pair']) in pairs]
    assert {tuple(r['pair']) for r in first_rows} == pairs
    assert all(r['height_cap_power_of_ten']>=TAIL_POWER and r['maximum_difference']>=13
               and r['reciprocal_exponent_denominator']==3 for r in first_rows)
    ramp = certify(14,9,[(*pair,3333) for pair in sorted(pairs)],
                   'The retained finite six-prime clique of exponent 1/3 through 10^15170264.')
    cap_power = ramp['algebraic_cap_power_of_ten']
    assert cap_power == 41 and ramp['minimum_gain'] == '1199/400'
    assert max(r['height_threshold']+13 for r in first_rows) < 10**cap_power
    second_rows = json.loads(second.read_text())['records']
    assert {tuple(r['pair']) for r in second_rows} == pairs
    assert all(r['height_cap_power_of_ten']>=cap_power and r['maximum_difference']>=13
               and r['cofactor_exponent_numerator']==2
               and r['cofactor_exponent_denominator']==5 for r in second_rows)
    original = windows.previous.reduced_cap
    def ramp_cap(index, selected_primes, constants, saving):
        assert index==14 and tuple(selected_primes)==primes and saving>=16665
        return 10**cap_power,cap_power
    windows.previous.reduced_cap = ramp_cap
    try:
        result = windows.run(14,TAIL_POWER,[first,second],20_000_000,10_000)
    finally:
        windows.previous.reduced_cap = original
    for source in result['source_certificates']:
        source['file'] = Path(source['file']).name
    result.update({
        'weighted_ramp_reduction':ramp,
        'tail_assumption':'Every bad triple at index 14 has n<10^15170264.',
        'tail_theorem_supplied_by_this_file':False,
        'conclusion':'No admissible bad triples at index 14 remain below 10^15170264; complete exclusion follows from a separately proved tail at or below that exponent.',
    })
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in (
        'i','supplied_tail_power_of_ten','inclusive_interval_cap_power_of_ten',
        'certified_intervals','minimum_certified_log_margin','exact_singleton_rows',
        'exact_columns_checked','conclusion')},indent=2))
    return result


if __name__=='__main__': run()
