#!/usr/bin/env python3
"""Bootstrap the selected index-fourteen gcd sources, reusing exact old proofs."""
from copy import deepcopy
import json
from pathlib import Path
from erdos_699_off_diagonal_gcd_bootstrap import bootstrap, PrimeLogIntervals


def main():
    directory=Path(__file__).parent
    input_path=directory/'erdos_699_index_14_gcd_selected.json'
    previous_path=directory/'erdos_699_off_diagonal_gcd_bootstrap.json'
    selected=json.loads(input_path.read_text())
    previous=json.loads(previous_path.read_text())
    by_key={(tuple(row['directions']),row['requested_log_rate']):row for row in previous['records']}
    theta=PrimeLogIntervals()
    assert theta.metadata==previous['prime_log_certificate']
    out={'input_file':input_path.name,
         'reused_bootstrap_file':previous_path.name,
         'prime_log_certificate':theta.metadata,'records':[]}
    output=Path(__file__).with_suffix('.json')
    for row in selected['records']:
        key=(tuple(row['directions']),row['requested_log_rate'])
        if key in by_key:
            old=by_key[key]
            # Only edge labels can differ between these analytical records.
            for name,value in row.items():
                if name not in ('edge','source_edge'):
                    assert old['analytic_gcd_certificate'][name]==value
            record=deepcopy(old)
            record.update({'edge':row['edge'],'source_edge':row['source_edge'],
                           'analytic_gcd_certificate':row,'reused_source_edge':old['source_edge']})
            print(json.dumps({'reused_edge':row['edge'],'finite_interval_start':record['finite_interval_start']}),flush=True)
        else:
            record=bootstrap(row,theta)
            by_key[key]=record
        out['records'].append(record)
        output.write_text(json.dumps(out,indent=2)+'\n')
    assert len(out['records'])==len(selected['records'])==61
    print(json.dumps({'completed':61,'largest_m0':max(r['finite_interval_start']for r in out['records'])}),flush=True)


if __name__=='__main__':main()
