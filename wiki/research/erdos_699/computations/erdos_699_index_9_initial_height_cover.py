# evidence: entry manual
"""Sparse boxed Pade covers for all fifteen initial index-nine sources.

The eleven pair and four AP target boxes are unchanged. Complete interval
chains connect the polynomial height to the retained numerical source
tails. No interpolation rank or binomial row is recomputed.
"""
from pathlib import Path
import argparse
import gzip
import json
import multiprocessing as mp

from mpmath import iv

from erdos_699_index_9_boxed_sources import prepare_jobs as source_jobs
from erdos_699_index_7_height_cover_cache import load_prime_prefix
from erdos_699_prime_power_addendum import PrimePowerAddendum
from erdos_699_index_7_initial_height_cover import cover,verify_record,ceil_interval

ROOT=Path(__file__).parent
TMP=Path(__file__).resolve().parents[4]/'tmp'/'erdos699'
OUTPUT=Path(__file__).with_suffix('.json.gz')
START_POWER=241547627
THETA=POWERS=None


def prepare_jobs():
    first=int((START_POWER*iv.log(10)).a)-1
    assert first>iv.log(9) and first<START_POWER*iv.log(10)
    jobs=[]
    for item in source_jobs():
        stop=ceil_interval(item['tail_height_power_of_ten']*iv.log(10))+1
        job=dict(item)
        job.update({'source_record_index':item['source_id'],
                    'edge':item['source_id'],
                    'start_power_of_ten':START_POWER,
                    'start_log_height':first,'stop_log_height':stop,
                    'uniform_tail_power_of_ten':item['tail_height_power_of_ten']})
        jobs.append(job)
    assert len(jobs)==15 and len({j['source_id'] for j in jobs})==15
    return jobs


def file_names():
    names=(Path(__file__).name,'erdos_699_index_9_boxed_sources.py',
           'erdos_699_index_9_initial_relaxed_numerical.json',
           'erdos_699_index_7_initial_height_cover.py',
           'erdos_699_off_diagonal_boxed_sparse.py',
           'erdos_699_off_diagonal_sparse_witness.py',
           'erdos_699_index_7_gcd_pointwise.py',
           'erdos_699_prime_power_addendum.py',
           'erdos_699_index_7_height_cover_cache.py')
    return list(names)


def check(data,*,replay_gcd=False,cache=TMP/'prime-prefix-1000000000'):
    assert data['index']==9 and data['height_variable']=='h=n-8'
    assert data['start_power_of_ten']==START_POWER
    assert set(data['files'])==set(file_names())
    jobs={j['source_id']:j for j in prepare_jobs()}
    assert len(data['records'])==len(jobs)==15
    assert {r['source_id'] for r in data['records']}==set(jobs)
    theta=powers=None
    if replay_gcd:
        theta=load_prime_prefix(cache)
        powers=PrimePowerAddendum(theta,10**14)
        assert data['prime_log_certificate']==theta.metadata
        assert data['prime_power_certificate']==powers.metadata
    for record in data['records']:
        verify_record(record,jobs[record['source_id']],theta,powers,replay_gcd=replay_gcd)
    return {'index':9,'covered_source_boxes':15,'initial_pair_sources':11,
            'ordinary_AP_sources':4,'source_height_exponent':START_POWER,
            'witness_count':sum(r['witness_count'] for r in data['records']),
            'pointwise_gcd_bounds_replayed':bool(replay_gcd)}


def run_job(job):
    assert THETA is not None and POWERS is not None
    return cover(job,THETA,POWERS)


def write_result(path,data):
    path.write_bytes(gzip.compress((json.dumps(data,separators=(',',':'))+'\n').encode(),
                                   compresslevel=6,mtime=0))


def main():
    global THETA,POWERS
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache',type=Path,default=TMP/'prime-prefix-1000000000')
    parser.add_argument('--output',type=Path,default=OUTPUT)
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--replay-gcd',action='store_true')
    parser.add_argument('--workers',type=int,default=4)
    args=parser.parse_args()
    if args.write:
        assert args.workers>=1
        jobs=prepare_jobs()
        THETA=load_prime_prefix(args.cache)
        POWERS=PrimePowerAddendum(THETA,10**14)
        POWERS.powers.flags.writeable=False
        POWERS.prefix_lo.flags.writeable=False
        result={'index':9,'height_variable':'h=n-8','start_power_of_ten':START_POWER,
                'scope':'All eleven initial pair boxes and four ordinary AP boxes, under their retained hypotheses.',
                'files':file_names(),'prime_log_certificate':THETA.metadata,
                'prime_power_certificate':POWERS.metadata,'records':[]}
        context=mp.get_context('fork')
        with context.Pool(args.workers) as pool:
            for record in pool.imap_unordered(run_job,jobs):
                result['records'].append(record)
                result['records'].sort(key=lambda r:r['source_id'])
                write_result(args.output,result)
                print(json.dumps({'completed_sources':len(result['records']),
                                  'covered_sources':sum(r['status']=='covered' for r in result['records'])}),flush=True)
        summary={'index':9,'covered_source_boxes':sum(r['status']=='covered' for r in result['records']),
                 'witness_count':sum(r['witness_count'] for r in result['records']),
                 'source_height_exponent':START_POWER}
    else:
        with gzip.open(args.output,'rt') as handle:result=json.load(handle)
        summary=check(result,replay_gcd=args.replay_gcd,cache=args.cache)
    print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
