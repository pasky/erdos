# evidence: entry manual
"""Sparse log-height covers for the two remaining index-seven initial boxes.

Use fixed Pade indices and the exact two-prime denominator cost. Every
accepted interval has four rational endpoint inequalities. The complete
witness chains are retained, and verification recomputes each gcd bound.
The existing uniform numerical source bounds handle the remaining tail.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import gzip
import json
import time

from mpmath import iv

from erdos_699_index_7_height_cover_cache import load_prime_prefix
from erdos_699_index_7_gcd_pointwise import PointwiseGcdLower
from erdos_699_prime_power_addendum import PrimePowerAddendum
from erdos_699_off_diagonal_boxed_sparse import prepare_box,index_proposals,window_right,verify_window
from erdos_699_off_diagonal_pade import rational

ROOT=Path(__file__).parent
TMP=Path(__file__).resolve().parents[4]/'tmp'/'erdos699'
SOURCE=ROOT/'erdos_699_index_7_base_pairs_numerical_relaxed.json'
OUTPUT=Path(__file__).with_suffix('.json.gz')
START_POWER=100000000


def ceil_interval(value):
    result=int(value.b)+1
    assert value<result
    return result


def prepare_jobs(start_power=START_POWER):
    source=json.loads(SOURCE.read_text())
    assert source['index']==7 and source['height']=='h=n-6'
    first=int((start_power*iv.log(10)).a)-1
    assert first>iv.log(7) and first<start_power*iv.log(10)
    jobs=[]
    for index in (2,3):
        row=source['records'][index]
        edge=row['edge']
        assert edge[:2]==[2,5]
        targets={str(p):str(F(e,10000)) for p,e in zip(edge[:2],edge[2:])}
        assert {p:F(e) for p,e in targets.items()}=={p:F(e) for p,e in row['targets'].items()}
        clause=row['clause']
        cost=sum((max(F(0),F(g)+F(targets[p]))
                  for p,g in clause['positive_part_intercepts'].items()),F(0))
        assert cost==F(row['boxed_positive_part_upper_bound'])
        assert cost<F(clause['positive_part_threshold'])
        tail=row['numerical_threshold']
        assert tail['gap_bound']==tail['maximum_shift']==6
        prepared=prepare_box(clause,targets,source_id=':'.join(map(str,edge)),
                             gap=6,maximum_shift=6)
        stop=ceil_interval(tail['threshold_power_of_ten']*iv.log(10))+1
        jobs.append({'source_record_index':index,'edge':edge,'targets':targets,
                     'prepared':prepared,'start_power_of_ten':start_power,
                     'start_log_height':first,'stop_log_height':stop,
                     'uniform_tail_power_of_ten':tail['threshold_power_of_ten']})
    return jobs


def cover(job,theta,powers,*,max_steps=0):
    prepared=job['prepared']
    directions=prepared['directions']
    frontier=job['start_log_height']
    stop=job['stop_log_height']
    evaluators={}
    terms=8000
    preferred=0
    points=[]
    started=time.monotonic()
    probes=0
    while frontier<stop and (not max_steps or len(points)<max_steps):
        accepted=None
        for proposed_terms in (terms,16000,40000,100000):
            if proposed_terms<terms:continue
            if proposed_terms not in evaluators:
                evaluators[proposed_terms]=PointwiseGcdLower(
                    theta,directions,terms=proposed_terms,powers=powers)
            evaluator=evaluators[proposed_terms]
            candidates=index_proposals(prepared,frontier)
            order=[preferred]+[k for k in range(len(candidates)) if k!=preferred]
            for k in order:
                if k>=len(candidates):continue
                m=candidates[k]
                lower=evaluator.log_lower(m)
                probes+=1
                endpoint=window_right(prepared,m,frontier,lower)
                if endpoint>frontier:
                    accepted=(m,min(endpoint,stop),lower,proposed_terms,k)
                    break
            if accepted is not None:break
        if accepted is None:break
        m,right,lower,terms,preferred=accepted
        assert verify_window(prepared,m,frontier,right,lower)
        points.append([m,right,lower,terms])
        frontier=right
        if len(points)%5000==0:
            print(json.dumps({'edge':job['edge'],'witnesses':len(points),
                              'log_height':frontier,'stop':stop,
                              'seconds':round(time.monotonic()-started,2)}),flush=True)
    result=dict(job)
    result.update({'status':'covered' if frontier>=stop else 'incomplete',
                   'covered_through_log_height':frontier,'witness_count':len(points),
                   'gcd_evaluations':probes,'elapsed_seconds':round(time.monotonic()-started,3),
                   'witness_columns':['m','right_log_height','log_gcd_lower_scaled','terms'],
                   'witnesses':points})
    print(json.dumps({'edge':job['edge'],'status':result['status'],
                      'witnesses':len(points),'seconds':result['elapsed_seconds']}),flush=True)
    return result


def verify_record(record,job,theta=None,powers=None,*,replay_gcd=True):
    assert all(record[key]==value for key,value in job.items())
    assert record['status']=='covered'
    assert record['witness_count']==len(record['witnesses'])
    evaluators={}
    left=job['start_log_height']
    for m,right,lower,terms in record['witnesses']:
        assert type(lower) is int and lower>=0
        if replay_gcd:
            assert theta is not None and powers is not None
            if terms not in evaluators:
                evaluators[terms]=PointwiseGcdLower(theta,job['prepared']['directions'],
                                                   terms=terms,powers=powers)
            assert evaluators[terms].log_lower(m)==lower
        assert verify_window(job['prepared'],m,left,right,lower)
        left=right
    assert left==record['covered_through_log_height']>=job['stop_log_height']


def file_names():
    files=[SOURCE,Path(__file__),ROOT/'erdos_699_off_diagonal_boxed_sparse.py',
           ROOT/'erdos_699_off_diagonal_sparse_witness.py',
           ROOT/'erdos_699_index_7_gcd_pointwise.py',ROOT/'erdos_699_prime_power_addendum.py',
           ROOT/'erdos_699_index_7_height_cover_cache.py']
    return [path.name for path in files]


def check(data,*,replay_gcd=False,cache=TMP/'prime-prefix-1000000000'):
    """Validate both complete chains; optionally recompute pointwise gcds.

    The default checks every retained rational interval inequality and all
    source/input bindings. The pointwise gcd bounds can independently be
    recomputed by requesting replay_gcd=True.
    """
    assert data['index']==7 and data['height_variable']=='h=n-6'
    assert data['start_power_of_ten']==START_POWER
    assert data['source_file']==SOURCE.name
    assert set(data['files'])==set(file_names())
    jobs={job['source_record_index']:job for job in prepare_jobs()}
    assert len(data['records'])==2
    assert {row['source_record_index'] for row in data['records']}==set(jobs)
    theta=powers=None
    if replay_gcd:
        theta=load_prime_prefix(cache)
        powers=PrimePowerAddendum(theta,10**14)
        assert data['prime_log_certificate']==theta.metadata
        assert data['prime_power_certificate']==powers.metadata
    for record in data['records']:
        verify_record(record,jobs[record['source_record_index']],theta,powers,
                      replay_gcd=replay_gcd)
    source=json.loads(SOURCE.read_text())
    assert all(source['records'][i]['numerical_threshold']['threshold_power_of_ten']
               <=START_POWER for i in (0,1,4))
    return {'index':7,'covered_boxes':2,'all_initial_alternatives':5,
            'source_height_exponent':START_POWER,
            'witness_count':sum(row['witness_count'] for row in data['records']),
            'pointwise_gcd_bounds_replayed':bool(replay_gcd)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache',type=Path,default=TMP/'prime-prefix-1000000000')
    parser.add_argument('--output',type=Path,default=OUTPUT)
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--max-steps',type=int,default=0)
    parser.add_argument('--records',default='2,3')
    args=parser.parse_args()
    selected={int(value) for value in args.records.split(',')}
    assert selected<={2,3} and selected
    jobs=[job for job in prepare_jobs() if job['source_record_index'] in selected]
    theta=load_prime_prefix(args.cache)
    powers=PrimePowerAddendum(theta,10**14)
    names=file_names()
    if args.write:
        result={'index':7,'height_variable':'h=n-6','start_power_of_ten':START_POWER,
                'scope':'The two explicit initial2/5 cofactor boxes, followed by their retained numerical tails.',
                'source_file':SOURCE.name,'files':names,
                'prime_log_certificate':theta.metadata,'prime_power_certificate':powers.metadata,
                'records':[]}
        for job in jobs:
            result['records'].append(cover(job,theta,powers,max_steps=args.max_steps))
            args.output.write_bytes(gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0))
    else:
        assert not args.max_steps
        with gzip.open(args.output,'rt') as handle:result=json.load(handle)
        assert set(result['files'])==set(names)
        assert result['prime_log_certificate']==theta.metadata
        assert result['prime_power_certificate']==powers.metadata
        assert {r['source_record_index'] for r in result['records']}==selected
        by_index={job['source_record_index']:job for job in jobs}
        for record in result['records']:
            verify_record(record,by_index[record['source_record_index']],theta,powers)
    print(json.dumps({'covered_sources':sum(r['status']=='covered' for r in result['records']),
                      'total_sources':len(result['records']),
                      'witnesses':sum(r['witness_count'] for r in result['records']),
                      'source_height_exponent':START_POWER},indent=2))


if __name__=='__main__':main()
