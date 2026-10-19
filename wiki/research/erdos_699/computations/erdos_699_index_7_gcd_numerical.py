#!/usr/bin/env python3
"""Practical gcd rates for the proved relaxed index-seven source clauses.

For each original source with block t and relaxation eta, a replacement
rate ell >= ell_old-3*eta/(4*t) preserves at least eta/4 of numerical
margin. The maximum requirement over a direction is rounded upward.
The stronger retained theta bounds then give an explicit starting index
for both adjacent coefficient gcds. This file does not perform bootstraps.
"""
from collections import Counter
from fractions import Fraction
import json
from pathlib import Path
import time

from erdos_699_off_diagonal_gcd_sharp import gcd_exponent_lower


def shared_requirements(sources, source_eta, scale=10**9):
    grouped={}
    assert {row['id']for row in sources}==set(source_eta)
    for row in sources:
        certificate=row['certificate']
        source=certificate['source']
        directions=tuple(source['directions'])
        old=Fraction(source['gcd_log_rate'])
        block=Fraction(certificate['block_parameter'])
        eta=Fraction(source_eta[row['id']])
        assert block>0 and eta>0
        required=old-Fraction(3,4)*eta/block
        grouped.setdefault(directions,[]).append({
            'source_id':row['id'],'old_rate':str(old),'block_parameter':str(block),
            'source_eta':str(eta),'minimum_rate':str(required)})
    records=[]
    for directions,bindings in sorted(grouped.items()):
        required=max(Fraction(x['minimum_rate'])for x in bindings)
        rate=Fraction((required.numerator*scale+required.denominator-1)//required.denominator,scale)
        assert rate>=required and rate>0
        for binding in bindings:
            margin=Fraction(binding['source_eta'])+Fraction(binding['block_parameter'])*(rate-Fraction(binding['old_rate']))
            assert margin>=Fraction(binding['source_eta'])/4
            binding['guaranteed_margin_increment']=str(margin)
        records.append({'directions':list(directions),'direction_key':','.join(map(str,directions)),
                        'requested_log_rate':str(rate),'rate_rounding_denominator':scale,
                        'source_bindings':bindings})
    return records


def main():
    directory=Path(__file__).parent
    source_path=directory/'erdos_699_index_7_effective.json'
    relaxed_path=directory/'erdos_699_index_7_relaxed_sources.json'
    helper_path=directory/'erdos_699_off_diagonal_gcd_sharp.py'
    data=json.loads(source_path.read_text())
    relaxed=json.loads(relaxed_path.read_text())
    records=shared_requirements(data['sources'],relaxed['source_eta'])
    result={'scope':'Numerical gcd starting bounds for the proved relaxed index-seven clauses; finite bootstraps are separate.',
            'source_file':source_path.name,
            'relaxation_file':relaxed_path.name,
            'theta_helper_file':helper_path.name,
            'source_eta':relaxed['source_eta'],'records':[]}
    output=Path(__file__).with_suffix('.json')
    start=time.monotonic()
    for i,record in enumerate(records):
        required=Fraction(record['requested_log_rate'])
        found=None
        for exponent in range(6,13):
            certificate=gcd_exponent_lower(*record['directions'],terms=4000,m0=10**exponent)
            if Fraction(certificate['ell_lower'])>required:
                found=certificate
                break
        if found is None:
            certificate=gcd_exponent_lower(*record['directions'],terms=40000,m0=10**12)
            assert Fraction(certificate['ell_lower'])>required,record['directions']
            found=certificate
        record['analytic_gcd_certificate']=found
        record['analytic_strict_rate_margin']=str(Fraction(found['ell_lower'])-required)
        result['records'].append(record)
        if (i+1)%30==0:
            output.write_text(json.dumps(result,indent=2)+'\n')
            print(json.dumps({'directions_done':i+1,'elapsed_seconds':round(time.monotonic()-start,1)}),flush=True)
    result['summary']={'directions':len(records),'sources':len(data['sources']),
                       'maximum_analytic_m0':max(r['analytic_gcd_certificate']['m0']for r in records),
                       'm0_counts':dict(sorted(Counter(r['analytic_gcd_certificate']['m0']for r in records).items()))}
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['summary'],indent=2),flush=True)


if __name__=='__main__':main()
