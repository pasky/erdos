#!/usr/bin/env python3
# evidence: entry manual
"""Sparse shrinking-denominator covers for the relaxed index-seven clauses.

At a left coverage coordinate y, an integer Pade index m<=y gives a
pointwise gcd witness. Exact integer endpoint tests certify the source
clauses on [y/t,next_y/t], intersected with the stated global height domain.
A checked compact prime prefix is shared read-only by forked workers.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import multiprocessing as mp
from pathlib import Path
import time

from mpmath import iv

from erdos_699_compact_prime_prefix import CompactPrimeLogIntervals
from erdos_699_index_7_height_cover_compact import CompactPointwiseGcdLower
from erdos_699_prime_power_addendum import PrimePowerAddendum
from erdos_699_off_diagonal_sparse_witness import prepare_witness,group_window,verify_window,index_proposals
from erdos_699_off_diagonal_explicit_clauses import joint_clause_threshold
from erdos_699_off_diagonal_pade import rational

HERE=Path(__file__).parent
TMP=Path(__file__).resolve().parents[4]/'tmp'/'erdos699'
COMPACT=POWERS=None
WITNESS_RULE='shrinking_denominator_cost'


def ceil_interval(value):
    result=int(value.b)+1
    assert value<result
    return result


def prepare_jobs(directory,gcd_data,direct,start_power,chosen=None):
    source_path=directory/gcd_data['source_file']
    relaxed_path=directory/gcd_data['relaxation_file']
    original_data=json.loads(source_path.read_text())
    relaxed=json.loads(relaxed_path.read_text())
    assert relaxed['source_eta']==gcd_data['source_eta']
    assert start_power>=direct['target_height_power_of_ten']
    for name in direct['helper_files']:
        assert (directory/name).is_file(),name
    original={row['id']:row for row in original_data['sources']}
    reblocked={row['source_id']:row for row in direct['records']}
    assert set(original)==set(reblocked)
    required={sid for sid,row in reblocked.items()if not row['directly_valid_at_target']}
    assert required==set(direct['target_summary']['remaining_source_ids'])
    for sid,row in reblocked.items():
        if sid not in required:
            assert row['target_numerical_certificate']['threshold_power_of_ten']<=start_power
    jobs=[];witnesses={};tails={};tail_bindings={};prerequisites={}
    for record in gcd_data['records']:
        directions=tuple(record['directions'])
        if chosen is not None and directions not in chosen:continue
        bindings=[b for b in record['source_bindings']if b['source_id']in required]
        if not bindings:continue
        analytic=record['analytic_gcd_certificate']
        rate=Fraction(record['requested_log_rate'])
        assert analytic['directions']==record['directions'] and Fraction(analytic['ell_lower'])>rate
        prepared=[];ends=[]
        for binding in bindings:
            sid=binding['source_id'];row=original[sid]
            eta=Fraction(relaxed['source_eta'][sid])
            assert str(eta)==binding['source_eta']
            assert row['hypothesis']['kind']in('pair','ap')
            gap=6 if row['hypothesis']['kind']=='pair'else 9
            witness=prepare_witness(row['certificate'],source_id=sid,threshold_weakening=eta,
                                    gap=gap,maximum_shift=6,shrinking_cost=True)
            assert witness['directions']==record['directions']
            assert Fraction(witness['block_parameter'])==Fraction(binding['block_parameter'])
            source_margin=eta+Fraction(binding['block_parameter'])*(rate-Fraction(binding['old_rate']))
            assert source_margin>=eta/4
            start_log=start_power*iv.log(10)
            required_log=iv.log(witness['maximum_shift']+1)
            assert start_log>required_log
            prerequisites[sid]={'start_power_of_ten':start_power,'maximum_shift':6,
                'start_log_height':iv.nstr(start_log,40),'required_log_height':iv.nstr(required_log,40),
                'verified_inequality':'start_log_height > log(maximum_shift+1)'}
            old=joint_clause_threshold(row['certificate'],analytic['m0'],gap=gap,maximum_shift=6,
                                       gcd_log_rate=rate,threshold_weakening=eta)
            new=reblocked[sid]['uniform_numerical_certificate']
            assert new['directions']==record['directions']
            assert Fraction(new['threshold_weakening'])==eta
            assert Fraction(new['positive_part_threshold'])==Fraction(witness['positive_part_threshold'])
            assert new['positive_part_intercepts']==row['certificate']['positive_part_intercepts']
            assert new['maximum_shift']>=6 and new['gap_bound']>=gap
            tail,kind=(new,'reblocked')if new['threshold_power_of_ten']<old['threshold_power_of_ten']else(old,'original')
            block=Fraction(witness['block_parameter'])
            end=ceil_interval(rational(block)*tail['threshold_power_of_ten']*iv.log(10))+1
            ends.append(end);prepared.append(witness);witnesses[sid]=witness;tails[sid]=tail
            tail_bindings[sid]={'kind':kind,'ending_index':end,'nominal_block_parameter':str(block),
                                'threshold_power_of_ten':tail['threshold_power_of_ten']}
        smallest=min(Fraction(p['block_parameter'])for p in prepared)
        first_value=rational(smallest)*start_power*iv.log(10)
        first=int(first_value.a)-1
        assert first>=2 and directions[1]*first>=2 and rational(first)<first_value
        assert all(rational(first)<rational(Fraction(p['block_parameter']))*start_power*iv.log(10)for p in prepared)
        jobs.append({'directions':list(directions),'direction_key':record['direction_key'],
            'source_ids':[p['source_id']for p in prepared],'prepared':prepared,
            'start_power_of_ten':start_power,'start_m':first,'stop_m':max(ends),
            'analytic_gcd_m0':analytic['m0'],'requested_log_rate':str(rate),'initial_terms':4000,
            'minimum_eta':str(min(Fraction(p['threshold_weakening'])for p in prepared))})
    jobs.sort(key=lambda j:(Fraction(j['minimum_eta']),tuple(j['directions'])))
    if chosen is not None:assert {tuple(j['directions'])for j in jobs}==chosen
    return jobs,witnesses,tails,tail_bindings,prerequisites,required


def cover_direction(job):
    assert COMPACT is not None and POWERS is not None
    directions=tuple(job['directions']);prepared=job['prepared']
    frontier=job['start_m'];stop=job['stop_m'];terms=job['initial_terms']
    evaluators={};digest=sha256();count=probes=shortened=0;terms_counts={}
    first_point=last_point=None;smallest_ratio=None;status='covered';started=time.monotonic()
    while frontier<stop:
        accepted=None
        for proposed_terms in sorted({terms,8000,16000,40000}):
            if proposed_terms<terms:continue
            evaluator=evaluators.get(proposed_terms)
            if evaluator is None:
                evaluator=CompactPointwiseGcdLower(COMPACT,directions,terms=proposed_terms,powers=POWERS)
                evaluators[proposed_terms]=evaluator
            # Nominal first: the shrinking bound already improves its right
            # endpoint. Shorter proposals are used only if it does not advance.
            candidates=[frontier]
            for m in candidates:
                log_gcd=evaluator.log_lower(m);probes+=1
                endpoint=group_window(prepared,m,frontier,log_gcd)
                if endpoint>frontier:
                    accepted=(m,min(endpoint,stop),log_gcd,proposed_terms);break
            if accepted is None:
                for m in index_proposals(prepared,frontier):
                    if m==frontier:continue
                    log_gcd=evaluator.log_lower(m);probes+=1
                    endpoint=group_window(prepared,m,frontier,log_gcd)
                    if endpoint>frontier:
                        accepted=(m,min(endpoint,stop),log_gcd,proposed_terms);break
            if accepted is not None:break
        if accepted is None:
            status='gap';break
        m,right,log_gcd,terms=accepted
        assert 2<=m<=frontier<right and directions[1]*m>=2
        assert all(verify_window(p,m,frontier,right,log_gcd)for p in prepared)
        if m<frontier:shortened+=1
        ratio=Fraction(right-frontier,frontier)
        smallest_ratio=ratio if smallest_ratio is None else min(smallest_ratio,ratio)
        point={'m':m,'left_y':frontier,'right_y':right,'log_gcd_lower_scaled':log_gcd,'terms':terms}
        if first_point is None:first_point=point
        last_point=point
        digest.update(f'{m},{frontier},{right},{log_gcd},{terms}\n'.encode())
        count+=1;terms_counts[str(terms)]=terms_counts.get(str(terms),0)+1;frontier=right
        if count%50000==0:
            print(json.dumps({'directions':list(directions),'witnesses':count,'covered_y':frontier,
                              'stop_y':stop,'seconds':round(time.monotonic()-started,1)}),flush=True)
    result={key:job[key]for key in ['directions','direction_key','source_ids','start_power_of_ten',
        'start_m','stop_m','analytic_gcd_m0','requested_log_rate','initial_terms']}
    result.update({'witness_rule':WITNESS_RULE,'status':status,'covered_through_m':frontier,
        'witness_count':count,'gcd_evaluations':probes,'shortened_index_witnesses':shortened,
        'terms_counts':terms_counts,'smallest_step_ratio':str(smallest_ratio)if smallest_ratio is not None else None,
        'first_witness':first_point,'last_witness':last_point,'witness_sequence_sha256':digest.hexdigest(),
        'elapsed_seconds':round(time.monotonic()-started,3)})
    print(json.dumps({k:result[k]for k in ['directions','status','witness_count','elapsed_seconds']}),flush=True)
    return result


def verify(data,directory=HERE):
    """Check source and boundary bindings without replaying the witness chain.

    Every step was checked with exact arithmetic during generation. The
    replay mode reproduces the retained witness-sequence digests. The
    input files the record names are checked for presence only.
    """
    directory=Path(directory)
    for name in data['files']:
        assert (directory/name).is_file(),name
    gcd_data=json.loads((directory/data['input_file']).read_text())
    direct=json.loads((directory/data['direct_source_file']).read_text())
    chosen={tuple(r['directions'])for r in data['records']}if data['selection_directions']is not None else None
    jobs,witnesses,tails,bindings,prerequisites,required=prepare_jobs(directory,gcd_data,direct,data['start_power_of_ten'],chosen)
    assert data['witness_rule']==WITNESS_RULE
    assert witnesses==data['prepared_sources'] and tails==data['analytic_source_tails']
    assert bindings==data['analytic_tail_bindings'] and prerequisites==data['source_height_prerequisites']
    assert sorted(witnesses)==data['required_sparse_source_ids']
    assert sorted(required)==data['all_remaining_source_ids']
    by_direction={tuple(j['directions']):j for j in jobs}
    assert len(data['records'])==len(by_direction)==data['expected_directions']
    ids=[]
    for record in data['records']:
        job=by_direction[tuple(record['directions'])]
        assert record['status']=='covered' and record['witness_rule']==WITNESS_RULE
        assert all(record[k]==job[k]for k in ['source_ids','start_m','stop_m','start_power_of_ten','initial_terms'])
        assert record['covered_through_m']>=record['stop_m']
        assert len(record['witness_sequence_sha256'])==64
        if record['witness_count']:
            first,last=record['first_witness'],record['last_witness']
            assert first['left_y']==record['start_m'] and last['right_y']==record['covered_through_m']
            for point in (first,last):
                assert all(verify_window(p,point['m'],point['left_y'],point['right_y'],point['log_gcd_lower_scaled'])for p in job['prepared'])
        else:assert record['start_m']>=record['stop_m']
        for sid in record['source_ids']:
            assert record['covered_through_m']>=bindings[sid]['ending_index']
        ids.extend(record['source_ids'])
    assert len(ids)==len(set(ids)) and set(ids)==set(witnesses)
    assert data['summary']['gaps']==[]
    assert data['summary']['witness_count']==sum(r['witness_count']for r in data['records'])
    return {'verified_directions':len(jobs),'verified_sparse_sources':len(ids),
            'source_threshold_power_of_ten':data['start_power_of_ten'],'chain_replayed':False}


certify=verify


def main():
    global COMPACT,POWERS
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,default=HERE/'erdos_699_index_7_gcd_numerical.json')
    parser.add_argument('--direct-source-file',type=Path,default=HERE/'erdos_699_index_7_reblocked_numerical.json')
    parser.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json'))
    parser.add_argument('--start-power',type=int,default=100000000)
    parser.add_argument('--workers',type=int,default=8)
    parser.add_argument('--compact-cache',type=Path,default=TMP/'compact-prime-prefix-10000000000')
    parser.add_argument('--power-limit',type=int,default=10**14)
    parser.add_argument('--directions',default='')
    parser.add_argument('--reuse',type=Path,action='append',default=[])
    parser.add_argument('--check',action='store_true')
    parser.add_argument('--replay',action='store_true')
    args=parser.parse_args()
    if args.check:
        print(json.dumps(verify(json.loads(args.output.read_text())),indent=2));return
    assert args.start_power>=1 and args.workers>=1
    gcd_data=json.loads(args.input.read_text());direct=json.loads(args.direct_source_file.read_text())
    assert len(gcd_data['records'])==gcd_data['summary']['directions']==210
    chosen={tuple(map(int,x.split(',')))for x in args.directions.split(';')}if args.directions else None
    jobs,witnesses,tails,bindings,prerequisites,required=prepare_jobs(args.input.parent,gcd_data,direct,args.start_power,chosen)
    print(json.dumps({'prepared_directions':len(jobs),'prepared_sparse_sources':len(witnesses)}),flush=True)
    COMPACT=CompactPrimeLogIntervals.load(args.compact_cache)
    POWERS=PrimePowerAddendum(COMPACT.base,power_limit=args.power_limit)
    for array in (COMPACT.words,COMPACT.lower_weight,COMPACT.upper_weight,COMPACT.lower_prefix,
                  COMPACT.upper_prefix,POWERS.powers,POWERS.prefix_lo):array.flags.writeable=False
    files=[args.input,args.direct_source_file,Path(__file__),
        HERE/'erdos_699_index_7_gcd_pointwise.py',HERE/'erdos_699_index_7_height_cover_compact.py',
        HERE/'erdos_699_off_diagonal_sparse_witness.py',HERE/'erdos_699_off_diagonal_explicit_clauses.py',
        HERE/'erdos_699_prime_power_addendum.py',HERE/'erdos_699_compact_prime_prefix.py']
    result={'scope':'Numerical log-height covers for retained relaxed index-seven clauses under their stated hypotheses.',
        'witness_rule':WITNESS_RULE,'input_file':args.input.name,
        'direct_source_file':args.direct_source_file.name,
        'files':[p.name for p in files],
        'start_power_of_ten':args.start_power,'selection_directions':[list(x)for x in sorted(chosen)]if chosen is not None else None,
        'prime_log_certificate':COMPACT.metadata,'prime_power_certificate':POWERS.metadata,
        'expected_directions':len(jobs),'required_sparse_source_ids':sorted(witnesses),'all_remaining_source_ids':sorted(required),
        'prepared_sources':witnesses,'analytic_source_tails':tails,'analytic_tail_bindings':bindings,
        'source_height_prerequisites':prerequisites,
        'coverage_domain':'Witness windows are intersected with log(h)>=start_power_of_ten*log(10).',
        'integer_index_prerequisites':{'m_at_least':2,'B_times_m_at_least':2},'records':[]}
    previous_records={}
    job_map={tuple(j['directions']):j for j in jobs}
    for path in args.reuse:
        previous=json.loads(path.read_text())
        for key in ['witness_rule','start_power_of_ten','prime_log_certificate','prime_power_certificate']:
            assert previous[key]==result[key],(path,key)
        for record in previous['records']:
            d=tuple(record['directions'])
            if d not in job_map or record['status']!='covered':continue
            job=job_map[d]
            assert all(record[k]==job[k]for k in ['source_ids','start_m','stop_m','initial_terms'])
            assert all(previous['prepared_sources'][sid]==witnesses[sid]for sid in job['source_ids'])
            assert all(previous['analytic_source_tails'][sid]==tails[sid]for sid in job['source_ids'])
            previous_records[d]=record
    if not args.replay:result['records']=list(previous_records.values())
    pending=[j for j in jobs if args.replay or tuple(j['directions'])not in previous_records]
    print(json.dumps({'prefix_ready':True,'directions_to_run':len(pending),'reused':len(result['records'])}),flush=True)
    context=mp.get_context('fork')
    with context.Pool(args.workers)as pool:
        for record in pool.imap_unordered(cover_direction,pending):
            if args.replay and tuple(record['directions'])in previous_records:
                old=previous_records[tuple(record['directions'])]
                assert record['witness_sequence_sha256']==old['witness_sequence_sha256']
                assert record['witness_count']==old['witness_count']
            result['records'].append(record);result['records'].sort(key=lambda r:tuple(r['directions']))
            args.output.write_text(json.dumps(result,indent=2)+'\n')
            print(json.dumps({'completed_directions':len(result['records']),'expected':len(jobs)}),flush=True)
    assert len(result['records'])==len(jobs)
    result['summary']={'directions':len(jobs),'sources':len(witnesses),
        'covered_directions':sum(r['status']=='covered'for r in result['records']),
        'witness_count':sum(r['witness_count']for r in result['records']),
        'gcd_evaluations':sum(r['gcd_evaluations']for r in result['records']),
        'gaps':[r['directions']for r in result['records']if r['status']!='covered'],
        'source_threshold_power_of_ten':args.start_power}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    if not result['summary']['gaps']:verify(result)
    print(json.dumps(result['summary'],indent=2),flush=True)


if __name__=='__main__':main()
