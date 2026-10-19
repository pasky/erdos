#!/usr/bin/env python3
# evidence: entry manual
"""Sparse shrinking-denominator covers for the frozen index-nine clauses."""
from __future__ import annotations
import argparse,gzip,json,multiprocessing as mp,time
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from mpmath import iv
from erdos_699_compact_prime_prefix import CompactPrimeLogIntervals
from erdos_699_index_7_height_cover_compact import CompactPointwiseGcdLower
from erdos_699_prime_power_addendum import PrimePowerAddendum
from erdos_699_off_diagonal_sparse_witness import prepare_witness,group_window,verify_window,index_proposals
from erdos_699_off_diagonal_pade import rational
HERE=Path(__file__).parent
TMP=Path(__file__).resolve().parents[4]/'tmp'/'erdos699'
COMPACT=POWERS=None
WITNESS_RULE='shrinking_denominator_cost'
TARGET=241547627

def read_json(path):
    path=Path(path)
    return json.loads(gzip.decompress(path.read_bytes()))if path.suffix=='.gz'else json.loads(path.read_text())

def ceil_interval(value):
    answer=int(value.b)+1
    assert value<answer
    return answer

def prepare_jobs(directory,inputs,direct,start_power,chosen=None):
    assert inputs['index']==direct['index']==9 and start_power==TARGET
    assert inputs['target_global_height_power_of_ten']==direct['target_height_power_of_ten']==TARGET
    for name in inputs['input_files']:
        assert (directory/name).is_file(),name
        assert name in direct['input_files']
    for name in direct['helper_files']:
        assert (directory/name).is_file(),name
    catalog=read_json(directory/inputs['source_file'])
    old=read_json(directory/inputs['old_numerical_file'])
    weakening=read_json(directory/inputs['weakening_file'])
    sources=catalog['records'];old_rows=old['records']
    source_ids={r['id']for r in sources}
    assert len(sources)==len(old_rows)==len(direct['records'])==790
    assert inputs['source_eta']==weakening['per_source_half_budget']
    new_by_id={r['source_id']:r for r in direct['records']}
    assert set(new_by_id)==source_ids
    assert direct['uniform_summary']['sources']==790
    old_under={r['source_id']for r in old_rows if r['threshold_power_of_ten']<=start_power}
    new_direct={sid for sid,r in new_by_id.items()if r['directly_valid_at_target']}
    for sid in new_direct:assert new_by_id[sid]['target_numerical_certificate']['threshold_power_of_ten']<=start_power
    skipped=old_under|new_direct;required=source_ids-skipped
    jobs=[];prepared_all={};tails={};bindings_all={};prerequisites={}
    for group in inputs['records']:
        directions=tuple(group['directions'])
        if chosen is not None and directions not in chosen:continue
        relevant=[b for b in group['source_bindings']if b['source_id']in required]
        if not relevant:continue
        prepared=[];ends=[]
        for b in relevant:
            sid=b['source_id'];source=sources[b['source_record_index']]
            previous=old_rows[b['old_numerical_record_index']]
            assert source['id']==previous['source_id']==sid
            assert source['certificate']['source']['directions']==group['directions']==previous['directions']
            eta=Fraction(inputs['source_eta'][sid]);assert eta==Fraction(b['source_eta'])
            assert source['hypothesis']['kind']==b['hypothesis_kind']in('pair','ap','four')
            gap=8 if b['hypothesis_kind']=='pair'else 64
            assert gap==b['gap_bound']and b['maximum_shift']==8
            witness=prepare_witness(source['certificate'],source_id=sid,threshold_weakening=eta,
                                    gap=gap,maximum_shift=8,shrinking_cost=True)
            assert witness['directions']==group['directions']
            assert Fraction(witness['block_parameter'])==Fraction(b['block_parameter'])
            new=new_by_id[sid]['uniform_numerical_certificate']
            for candidate in (previous,new):
                assert candidate['directions']==group['directions']
                assert Fraction(candidate['threshold_weakening'])==eta
                assert Fraction(candidate['positive_part_threshold'])==Fraction(witness['positive_part_threshold'])
                assert candidate['positive_part_intercepts']==source['certificate']['positive_part_intercepts']
                assert candidate['maximum_shift']==8 and candidate['gap_bound']==gap
            tail,kind=(new,'reblocked')if new['threshold_power_of_ten']<previous['threshold_power_of_ten']else(previous,'old')
            block=Fraction(witness['block_parameter'])
            end=ceil_interval(rational(block)*tail['threshold_power_of_ten']*iv.log(10))+1
            start_log=start_power*iv.log(10);required_log=iv.log(9)
            assert start_log>required_log
            prerequisites[sid]={'start_power_of_ten':start_power,'maximum_shift':8,
                'start_log_height':iv.nstr(start_log,40),'required_log_height':iv.nstr(required_log,40),
                'verified_inequality':'start_log_height > log(maximum_shift+1)'}
            prepared.append(witness);prepared_all[sid]=witness;tails[sid]=tail;ends.append(end)
            bindings_all[sid]={'kind':kind,'ending_index':end,'nominal_block_parameter':str(block),
                'threshold_power_of_ten':tail['threshold_power_of_ten'],
                'old_numerical_record_index':b['old_numerical_record_index'],
                'old_gcd_certificate_index':b['old_gcd_certificate_index']}
        smallest=min(Fraction(p['block_parameter'])for p in prepared)
        value=rational(smallest)*start_power*iv.log(10);first=int(value.a)-1
        assert first>=2 and directions[1]*first>=2 and rational(first)<value
        assert sum(directions)*max(ends)<2**62
        jobs.append({'directions':list(directions),'direction_key':group['direction_key'],
            'source_ids':[p['source_id']for p in prepared],'prepared':prepared,
            'start_power_of_ten':start_power,'start_m':first,'stop_m':max(ends),'initial_terms':4000,
            'minimum_eta':str(min(Fraction(p['threshold_weakening'])for p in prepared))})
    jobs.sort(key=lambda j:(Fraction(j['minimum_eta']),tuple(j['directions'])))
    if chosen is not None:assert {tuple(j['directions'])for j in jobs}==chosen
    partition={'old_source_ids_under_target':sorted(old_under),'new_direct_source_ids':sorted(new_direct),
               'skipped_source_ids':sorted(skipped),'all_remaining_source_ids':sorted(required)}
    return jobs,prepared_all,tails,bindings_all,prerequisites,partition

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
        'start_m','stop_m','initial_terms']}
    result.update({'witness_rule':WITNESS_RULE,'status':status,'covered_through_m':frontier,
        'witness_count':count,'gcd_evaluations':probes,'shortened_index_witnesses':shortened,
        'terms_counts':terms_counts,'smallest_step_ratio':str(smallest_ratio)if smallest_ratio is not None else None,
        'first_witness':first_point,'last_witness':last_point,'witness_sequence_sha256':digest.hexdigest(),
        'elapsed_seconds':round(time.monotonic()-started,3)})
    print(json.dumps({k:result[k]for k in ['directions','status','witness_count','elapsed_seconds']}),flush=True)
    return result


def verify(data,directory=HERE):
    """Verify source, metadata and endpoint bindings; chain replay is separate.

    The input files the record names are checked for presence only.
    """
    directory=Path(directory)
    for name in data['files']:assert (directory/name).is_file(),name
    inputs=read_json(directory/data['input_file']);direct=read_json(directory/data['direct_source_file'])
    chosen={tuple(r['directions'])for r in data['records']}if data['selection_directions']is not None else None
    jobs,prepared,tails,bindings,prerequisites,partition=prepare_jobs(directory,inputs,direct,data['start_power_of_ten'],chosen)
    assert data['witness_rule']==WITNESS_RULE
    assert prepared==data['prepared_sources']and tails==data['analytic_source_tails']
    assert bindings==data['analytic_tail_bindings']and prerequisites==data['source_height_prerequisites']
    assert sorted(prepared)==data['required_sparse_source_ids']
    assert all(data[k]==v for k,v in partition.items())
    by_dir={tuple(j['directions']):j for j in jobs};assert len(data['records'])==len(by_dir)==data['expected_directions']
    seen=[]
    for row in data['records']:
        job=by_dir[tuple(row['directions'])]
        assert row['status']=='covered'and row['witness_rule']==WITNESS_RULE
        assert all(row[k]==job[k]for k in ['source_ids','start_m','stop_m','start_power_of_ten','initial_terms'])
        assert row['covered_through_m']>=row['stop_m']and len(row['witness_sequence_sha256'])==64
        if row['witness_count']:
            first,last=row['first_witness'],row['last_witness']
            assert first['left_y']==row['start_m']and last['right_y']==row['covered_through_m']
            for point in (first,last):
                assert all(verify_window(p,point['m'],point['left_y'],point['right_y'],point['log_gcd_lower_scaled'])for p in job['prepared'])
        else:assert row['start_m']>=row['stop_m']
        assert all(row['covered_through_m']>=bindings[sid]['ending_index']for sid in row['source_ids'])
        seen.extend(row['source_ids'])
    assert len(seen)==len(set(seen))and set(seen)==set(prepared)
    assert data['summary']['gaps']==[]
    assert data['summary']['witness_count']==sum(r['witness_count']for r in data['records'])
    return {'verified_directions':len(jobs),'verified_sparse_sources':len(seen),
            'source_threshold_power_of_ten':data['start_power_of_ten'],'chain_replayed':False}

certify=verify


def main():
    global COMPACT,POWERS
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,default=HERE/'erdos_699_index_9_height_inputs.json')
    parser.add_argument('--direct-source-file',type=Path,default=HERE/'erdos_699_index_9_reblocked_numerical.json.gz')
    parser.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json'))
    parser.add_argument('--workers',type=int,default=8)
    parser.add_argument('--compact-cache',type=Path,default=TMP/'compact-prime-prefix-10000000000')
    parser.add_argument('--power-limit',type=int,default=10**14)
    parser.add_argument('--directions',default='')
    parser.add_argument('--reuse',type=Path,action='append',default=[])
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    if args.check:print(json.dumps(verify(read_json(args.output)),indent=2));return
    inputs=read_json(args.input);direct=read_json(args.direct_source_file)
    chosen={tuple(map(int,x.split(',')))for x in args.directions.split(';')}if args.directions else None
    jobs,prepared,tails,bindings,prerequisites,partition=prepare_jobs(args.input.parent,inputs,direct,TARGET,chosen)
    print(json.dumps({'prepared_directions':len(jobs),'prepared_sparse_sources':len(prepared),'skipped_sources':len(partition['skipped_source_ids'])}),flush=True)
    COMPACT=CompactPrimeLogIntervals.load(args.compact_cache)
    POWERS=PrimePowerAddendum(COMPACT.base,power_limit=args.power_limit)
    for array in (COMPACT.words,COMPACT.lower_weight,COMPACT.upper_weight,COMPACT.lower_prefix,COMPACT.upper_prefix,POWERS.powers,POWERS.prefix_lo):array.flags.writeable=False
    # Point smoke checks exercise the exact same integer API as the full run.
    for job in jobs[:3]:
        evaluator=CompactPointwiseGcdLower(COMPACT,job['directions'],terms=4000,powers=POWERS)
        left=job['start_m'];g=evaluator.log_lower(left)
        right=group_window(job['prepared'],left,left,g)
        if right<=left:
            for m in index_proposals(job['prepared'],left):
                right=max(right,group_window(job['prepared'],m,left,evaluator.log_lower(m)))
        print(json.dumps({'smoke_directions':job['directions'],'left':left,'right':right,'advances':right>left}),flush=True)
    files=[args.input,args.direct_source_file,Path(__file__)]+[HERE/name for name in (
        'erdos_699_index_7_gcd_pointwise.py','erdos_699_index_7_height_cover_compact.py',
        'erdos_699_off_diagonal_sparse_witness.py','erdos_699_prime_power_addendum.py','erdos_699_compact_prime_prefix.py')]
    files.extend(HERE/name for name in inputs['input_files'])
    result={'index':9,'height_variable':'h=n-8','scope':'Sparse numerical covers of the frozen index-nine source clauses under their stated hypotheses.',
        'witness_rule':WITNESS_RULE,'input_file':args.input.name,
        'direct_source_file':args.direct_source_file.name,
        'old_numerical_file':inputs['old_numerical_file'],
        'files':[p.name for p in files],
        'start_power_of_ten':TARGET,'selection_directions':[list(x)for x in sorted(chosen)]if chosen is not None else None,
        'prime_log_certificate':COMPACT.metadata,'prime_power_certificate':POWERS.metadata,'expected_directions':len(jobs),
        'required_sparse_source_ids':sorted(prepared),**partition,'prepared_sources':prepared,
        'analytic_source_tails':tails,'analytic_tail_bindings':bindings,'source_height_prerequisites':prerequisites,
        'coverage_domain':'Witness windows are intersected with log(h)>=241547627*log(10).',
        'integer_index_prerequisites':{'m_at_least':2,'B_times_m_at_least':2},'records':[]}
    by_dir={tuple(j['directions']):j for j in jobs};done={}
    for path in args.reuse:
        previous=read_json(path)
        for key in ['witness_rule','start_power_of_ten','prime_log_certificate','prime_power_certificate']:assert previous[key]==result[key]
        for row in previous['records']:
            d=tuple(row['directions'])
            if d not in by_dir or row['status']!='covered':continue
            job=by_dir[d]
            assert all(row[k]==job[k]for k in ['source_ids','start_m','stop_m','initial_terms'])
            assert all(previous['prepared_sources'][sid]==prepared[sid]for sid in job['source_ids'])
            assert all(previous['analytic_source_tails'][sid]==tails[sid]for sid in job['source_ids'])
            done[d]=row
    result['records']=list(done.values());pending=[j for j in jobs if tuple(j['directions'])not in done]
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'launching_workers':args.workers,'directions_to_run':len(pending),'sources':len(prepared)}),flush=True)
    with mp.get_context('fork').Pool(args.workers)as pool:
        for row in pool.imap_unordered(cover_direction,pending):
            result['records'].append(row);result['records'].sort(key=lambda r:tuple(r['directions']))
            args.output.write_text(json.dumps(result,indent=2)+'\n')
            print(json.dumps({'completed_directions':len(result['records']),'expected':len(jobs)}),flush=True)
    assert len(result['records'])==len(jobs)
    result['summary']={'directions':len(jobs),'sources':len(prepared),
        'covered_directions':sum(r['status']=='covered'for r in result['records']),
        'witness_count':sum(r['witness_count']for r in result['records']),
        'gcd_evaluations':sum(r['gcd_evaluations']for r in result['records']),
        'gaps':[r['directions']for r in result['records']if r['status']!='covered'],
        'source_threshold_power_of_ten':TARGET}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    if not result['summary']['gaps']:verify(result)
    print(json.dumps(result['summary'],indent=2),flush=True)

if __name__=='__main__':main()
