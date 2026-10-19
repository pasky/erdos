#!/usr/bin/env python3
"""Close the finite index-nine range through10^122 using pair certificates."""
from itertools import combinations
import json
from pathlib import Path

import erdos_699_window_intervals as windows
from erdos_699_weighted_ramps import certify

HERE=Path(__file__).resolve().parent


def run():
    primes=(2,3,5,7);pairs=set(combinations(primes,2))
    stronger=HERE/'erdos_699_prime_pair_strips_9_middle.json'
    weaker=HERE/'erdos_699_prime_pair_strips_two_fifths.json'
    rows=json.loads(stronger.read_text())['records']
    assert {tuple(r['pair'])for r in rows}==pairs
    assert all(r['height_cap_power_of_ten']>=122 and r['maximum_difference']>=8
               and (r['cofactor_exponent_numerator'],r['cofactor_exponent_denominator'])==(9,20) for r in rows)
    ramp=certify(9,6,[(*pair,4500)for pair in sorted(pairs)],'FiniteK4 cofactor exponent9/20.')
    assert ramp['algebraic_cap_power_of_ten']==25 and ramp['minimum_gain']=='3/2'
    cap_power=max(25,len(str(max(r['height_threshold']+8 for r in rows))))
    assert cap_power==26
    original=windows.previous.reduced_cap
    def reduced(index,selected_primes,constants,saving):
        assert index==9 and tuple(selected_primes)==primes and saving>=13500
        return 10**cap_power,cap_power
    windows.previous.reduced_cap=reduced
    try:
        result=windows.run(9,122,[stronger,weaker],20_000_000,30000)
    finally:
        windows.previous.reduced_cap=original
    for source in result['source_certificates']:source['file']=Path(source['file']).name
    result.update({'weighted_ramp_reduction':ramp,'conclusion':'No bad index-nine triple has n<=10^122.'})
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key]for key in ['i','inclusive_interval_cap_power_of_ten','certified_intervals',
        'minimum_certified_log_margin','exact_singleton_rows','exact_columns_checked','conclusion']},indent=2))
    return result


if __name__=='__main__':run()
