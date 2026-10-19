# evidence: entry
"""Require complete numerical tails and finite exclusion for index nine.

Partial joint-cover runs, missing source IDs, unverified skipped sources,
and a gap between finite and infinite ranges all fail. The checker reuses
the retained interpolation certificates and exposes no rank calculation.
"""
import argparse
import contextlib
import subprocess
import sys
from fractions import Fraction as F
from functools import lru_cache
import gzip
from itertools import combinations
import io
import json
from pathlib import Path

HERE=Path(__file__).parent
OUTPUT=Path(__file__).with_suffix('.json')
TMP=Path(__file__).resolve().parents[4]/'tmp'/'erdos699'
COMPACT_CACHE=TMP/'compact-prime-prefix-10000000000'
JOINT='erdos_699_index_9_height_cover.json'


def load(name):
    assert Path(name).name==name
    payload=(HERE/name).read_bytes()
    if payload[:2]==b'\x1f\x8b':payload=gzip.decompress(payload)
    return json.loads(payload)


def bound_data(name,data):
    """Check that a retained artifact's recorded inputs are present by basename."""
    for filename in data.get('input_files',[]):
        assert (HERE/filename).is_file(),(name,filename)


@lru_cache(maxsize=None)
def gcd_replay(directions,terms,m0,scale,root_scale):
    from erdos_699_off_diagonal_gcd_sharp import gcd_exponent_lower
    return gcd_exponent_lower(*directions,terms=terms,m0=m0,
                               scale=scale,root_scale=root_scale)


def verify_gcd(analytic,directions):
    assert analytic['directions']==directions
    replay=gcd_replay(tuple(directions),analytic['terms'],analytic['m0'],
                      analytic['rounding_denominator'],analytic['root_scale'])
    assert replay==analytic


def verify_old_skips(old,sources,budgets,target):
    """Independently verify every old numerical tail used as a skip."""
    from erdos_699_off_diagonal_explicit_clauses import joint_clause_threshold
    assert old['index']==9 and old['height_variable']=='h=n-8'
    assert old['source_count']==len(old['records'])==790
    assert {r['source_id'] for r in old['records']}==set(sources)
    for field in ('source','proof','weakening'):
        assert (HERE/old[field+'_file']).is_file(),field
    result={}
    for row in old['records']:
        if row['threshold_power_of_ten']>target:continue
        sid=row['source_id']
        source=sources[sid]
        analytic=old['gcd_certificates'][row['gcd_certificate_index']]
        verify_gcd(analytic,source['certificate']['source']['directions'])
        assert F(row['gcd_log_rate'])==F(analytic['ell_lower'])
        assert F(row['threshold_weakening'])==F(budgets[sid])
        numeric=joint_clause_threshold(source['certificate'],analytic['m0'],
            gap=8 if source['hypothesis']['kind']=='pair' else 64,
            maximum_shift=8,gcd_log_rate=analytic['ell_lower'],
            threshold_weakening=budgets[sid])
        assert all(row[key]==value for key,value in numeric.items())
        assert numeric['threshold_power_of_ten']<=target
        assert sid not in result
        result[sid]=numeric['threshold_power_of_ten']
    return result


def verify_new_direct(direct,sources,budgets,target):
    """Verify direct-target rows even if the uniform-tail replay omits them."""
    from erdos_699_nine_block_adjustment import joint_clause_threshold
    assert direct['index']==9 and direct['height_variable']=='h=n-8'
    assert direct['target_height_power_of_ten']==target
    assert len(direct['records'])==direct['target_summary']['sources']==790
    assert {r['source_id'] for r in direct['records']}==set(sources)
    bound_data('new direct sources',direct)
    for name in direct['helper_files']:assert (HERE/name).is_file(),name
    result={}
    for row in direct['records']:
        assert type(row['directly_valid_at_target']) is bool
        if not row['directly_valid_at_target']:continue
        sid=row['source_id']
        source=sources[sid]
        analytic=row['target_gcd_certificate']
        verify_gcd(analytic,source['certificate']['source']['directions'])
        numeric=joint_clause_threshold(source['certificate'],analytic['m0'],
            gap=8 if source['hypothesis']['kind']=='pair' else 64,
            maximum_shift=8,gcd_log_rate=analytic['ell_lower'],
            threshold_weakening=budgets[sid],prepared=row['prepared'])
        assert numeric==row['target_numerical_certificate']
        assert numeric['threshold_power_of_ten']<=target
        assert sid not in result
        result[sid]=numeric['threshold_power_of_ten']
    assert len(result)==direct['target_summary']['directly_valid']
    assert set(direct['target_summary']['remaining_source_ids'])==set(sources)-set(result)
    return result


def verify_sparse_tails(joint,old,direct,sources,budgets,sparse_ids):
    """Regenerate the numerical tail actually chosen for each sparse source."""
    from erdos_699_off_diagonal_explicit_clauses import joint_clause_threshold as old_bound
    from erdos_699_nine_block_adjustment import joint_clause_threshold as new_bound
    old_rows={row['source_id']:row for row in old['records']}
    new_rows={row['source_id']:row for row in direct['records']}
    groups={tuple(row['directions']):row for row in direct['uniform_gcd_records']}
    assert len(groups)==direct['uniform_summary']['directions']
    counts={'old':0,'reblocked':0}
    for sid in sorted(sparse_ids):
        source=sources[sid]
        directions=source['certificate']['source']['directions']
        binding=joint['analytic_tail_bindings'][sid]
        kind=binding['kind']
        assert kind in counts
        if kind=='old':
            row=old_rows[sid]
            analytic=old['gcd_certificates'][row['gcd_certificate_index']]
            verify_gcd(analytic,directions)
            numeric=old_bound(source['certificate'],analytic['m0'],
                gap=8 if source['hypothesis']['kind']=='pair' else 64,
                maximum_shift=8,gcd_log_rate=analytic['ell_lower'],
                threshold_weakening=budgets[sid])
            assert all(row[key]==value for key,value in numeric.items())
            retained=row
        else:
            row=new_rows[sid]
            group=groups[tuple(directions)]
            assert sid in group['source_ids']
            analytic=group['analytic_certificate']
            verify_gcd(analytic,directions)
            assert F(analytic['ell_lower'])>F(group['required_log_rate'])
            numeric=new_bound(source['certificate'],analytic['m0'],
                gap=8 if source['hypothesis']['kind']=='pair' else 64,
                maximum_shift=8,gcd_log_rate=analytic['ell_lower'],
                threshold_weakening=budgets[sid],prepared=row['prepared'])
            retained=row['uniform_numerical_certificate']
            assert numeric==retained
        assert joint['analytic_source_tails'][sid]==retained
        assert numeric['threshold_power_of_ten']==binding['threshold_power_of_ten']
        counts[kind]+=1
    return counts


def verify_finite(finite):
    from erdos_699_index_9_finite import CAP,check_continuation
    from erdos_699_weighted_ramps import certify
    assert finite['index']==9 and finite['finite_row_cap_power_of_ten']==CAP
    pair_name=finite['initial_pair_file']
    pairs=load(pair_name)['records']
    expected=set(combinations((2,3,5,7),2))
    assert len(pairs)==6 and {tuple(r['pair']) for r in pairs}==expected
    for row in pairs:
        check_continuation(row)
        assert row['height_cap_power_of_ten']>=CAP
        assert row['maximum_difference']>=8
        assert (row['cofactor_exponent_numerator'],row['cofactor_exponent_denominator'])==(41,100)
    ramp=certify(9,6,[(*pair,4100) for pair in sorted(expected)],
                 'Finite K4 cofactor exponent41/100.')
    assert ramp==finite['weighted_ramp_reduction']
    assert ramp['algebraic_cap_power_of_ten']==122 and ramp['minimum_gain']=='3/10'
    assert max(row['height_threshold']+8 for row in pairs)<10**122
    interval_name=finite['interval_file']
    intervals=load(interval_name)
    assert intervals['i']==9 and intervals['supplied_tail_power_of_ten']>=122
    assert finite['interval_cap_power_of_ten']==intervals['inclusive_interval_cap_power_of_ten']
    assert intervals['visited_intervals']==2*intervals['total_partition_leaves']-1
    assert F(intervals['minimum_certified_log_margin'])>0
    for row in intervals['source_certificates']:
        assert (HERE/row['file']).is_file(),row['file']
    for key in ('certified_intervals','exact_singleton_rows','exact_columns_checked'):
        assert finite[key]==intervals[key]
    return {'finite_row_cap_power_of_ten':CAP,
            'certified_intervals':finite['certified_intervals'],
            'exact_residual_rows':len(finite['exact_singleton_rows']),
            'exact_columns_checked':finite['exact_columns_checked']}


def report():
    source_name='erdos_699_nine_cofactor_clauses.json.gz'
    forest_name='erdos_699_nine_relaxed_forest.json.gz'
    baseline_name='erdos_699_index_9_relaxed_baseline.json'
    initial_name='erdos_699_index_9_initial_height_cover.json.gz'
    joint_name=JOINT
    inputs_name='erdos_699_index_9_height_inputs.json'
    finite_name='erdos_699_index_9_finite.json'
    catalogue,forest,baseline,initial,joint,inputs,finite=map(load,(
        source_name,forest_name,baseline_name,initial_name,joint_name,inputs_name,finite_name))
    assert catalogue['index']==forest['index']==baseline['index']==inputs['index']==9
    sources={r['id']:r for r in catalogue['records']}
    assert len(sources)==len(catalogue['records'])==forest['joint_source_count']==790
    budgets=forest['source_threshold_weakenings']
    assert set(budgets)==set(sources)
    assert inputs['source_file']==source_name and inputs['source_count']==790
    bound_data(inputs_name,inputs)
    assert {sid:F(eta) for sid,eta in inputs['source_eta'].items()}=={
        sid:F(eta) for sid,eta in budgets.items()}
    assert joint['input_file']==inputs_name
    assert joint['selection_directions'] is None
    assert joint['summary']['gaps']==[]
    assert all(row['status']=='covered' for row in joint['records'])
    target=joint['start_power_of_ten']
    assert target==inputs['target_global_height_power_of_ten']

    from erdos_699_index_9_initial_height_cover import check as check_initial
    initial_result=check_initial(initial,replay_gcd=False)
    from erdos_699_index_9_height_cover import verify as check_joint
    joint_result=check_joint(joint)
    old_name=inputs['old_numerical_file']
    old=load(old_name)
    direct_name=joint['direct_source_file']
    direct=load(direct_name)
    old_direct=verify_old_skips(old,sources,budgets,target)
    new_direct=verify_new_direct(direct,sources,budgets,target)
    skipped=set(old_direct)|set(new_direct)
    sparse_list=[sid for row in joint['records'] for sid in row['source_ids']]
    sparse=set(sparse_list)
    assert len(sparse_list)==len(sparse)
    assert sparse.isdisjoint(skipped)
    assert sparse|skipped==set(sources)
    assert sparse==set(joint['required_sparse_source_ids'])
    assert set(old_direct)==set(joint['old_source_ids_under_target'])
    assert set(new_direct)==set(joint['new_direct_source_ids'])
    assert skipped==set(joint['skipped_source_ids'])
    assert joint_result['verified_sparse_sources']==len(sparse)
    sparse_tails=verify_sparse_tails(joint,old,direct,sources,budgets,sparse)

    # The forest checks all828 residual roots and their exact rational
    # leaves, including the arithmetic nonvanishing of the two kernels.
    from erdos_699_nine_relaxed_forest import main as check_forest
    with contextlib.redirect_stdout(io.StringIO()):check_forest()
    initial_numeric=load('erdos_699_index_9_initial_relaxed_numerical.json')
    assert initial_numeric['weakened_baseline_edges_scaled']==baseline['pair_edges_scaled']
    assert F(initial_numeric['baseline_endpoint_weakening'])==F(forest['initial_pair_endpoint_weakening'])
    by_id={row['id']:row for row in initial_numeric['records']}
    bindings=initial_numeric['baseline_bindings']
    assert len(bindings)==len(baseline['pair_edges_scaled'])==19
    for index,binding in enumerate(bindings):
        edge=baseline['pair_edges_scaled'][index]
        assert binding['baseline_edge_index']==index and binding['edge_scaled']==edge
        strong=by_id[binding['numerical_source_id']]['edge_scaled']
        assert strong[:2]==edge[:2] and all(a>=b for a,b in zip(strong[2:],edge[2:]))
    ordinary={row['id'] for row in initial_numeric['records'] if row['kind']=='ordinary_ap'}
    used={node['source'] for root in forest['roots'] for node in root['tree'] if 'source' in node}
    assert used-set(sources)==ordinary and len(ordinary)==4
    assert used&set(sources)==set(sources)
    assert initial_result['covered_source_boxes']==15
    height_cap=max(initial_result['source_height_exponent'],
        joint_result['source_threshold_power_of_ten'],
        max(old_direct.values(),default=0),max(new_direct.values(),default=0),
        forest['height_power_of_ten'])
    finite_result=verify_finite(finite)
    assert height_cap>=1 and finite_result['finite_row_cap_power_of_ten']>=height_cap+1
    # If n>10^(K+1), then n-8>10^K because 9*10^K>8.
    assert 9*10>8
    names=(source_name,forest_name,baseline_name,initial_name,joint_name,
           inputs_name,direct_name,old_name,finite_name,
           finite['initial_pair_file'],finite['interval_file'],
           'erdos_699_index_9_initial_relaxed_numerical.json',
           'erdos_699_index_9_initial_height_cover.py',
           'erdos_699_index_9_height_cover.py',
           'erdos_699_nine_relaxed_forest.py',
           'erdos_699_index_9_relaxed_baseline.py',
           'erdos_699_index_9_finite.py',
           'erdos_699_index_9_nonvanishing.json',
           'erdos_699_nine_newton_farkas_bound.json',
           'erdos_699_nine_newton_source_weakening.json',
           'erdos_699_nine_block_adjustment.py',
           'erdos_699_index_9_reblocked_numerical.py',
           'erdos_699_off_diagonal_explicit_clauses.py',
           'erdos_699_off_diagonal_gcd_sharp.py')
    return {'index':9,'prime_threshold':'p>=9','height_variable':'h=n-8',
            'initial_pair_alternatives':19,'initial_pair_sources':11,'ordinary_AP_sources':4,
            'joint_sources':790,'old_direct_joint_sources':len(old_direct),
            'new_direct_joint_sources':len(new_direct),'skipped_joint_sources':len(skipped),
            'sparse_joint_sources':len(sparse),
            'sparse_tail_sources_by_method':sparse_tails,
            'initial_witness_count':initial_result['witness_count'],
            'joint_witness_count':joint['summary']['witness_count'],
            'root_cases':forest['root_case_count'],'farkas_leaf_count':forest['farkas_leaf_count'],
            'initial_source_height_power_of_ten':initial_result['source_height_exponent'],
            'joint_source_height_power_of_ten':joint_result['source_threshold_power_of_ten'],
            'polynomial_height_power_of_ten':forest['height_power_of_ten'],
            'complete_tail_height_power_of_ten':height_cap,**finite_result,
            'input_files':list(names),
            'conclusion':'Every admissible triple (n,9,j) has a prime p>=9 dividing both binomial coefficients.'}


def replay_joint(cache,workers):
    """Regenerate every joint witness sequence and compare it with the record.

    The compact prime-log cache is built on first use. The joint driver has no
    replay flag, so it is run to a separate output and every regenerated
    witness count and sequence digest is compared with the retained record.
    """
    if not (cache/'metadata.json').is_file():
        from erdos_699_compact_prime_prefix import CompactPrimeLogIntervals
        CompactPrimeLogIntervals(10**10,base_limit=10**8).save(cache)
    output=TMP/'erdos_699_index_9_height_cover_replay.json'
    output.parent.mkdir(parents=True,exist_ok=True)
    subprocess.run([sys.executable,str(HERE/'erdos_699_index_9_height_cover.py'),
        '--output',str(output),'--compact-cache',str(cache),'--workers',str(workers)],check=True,cwd=HERE)
    retained=load(JOINT)
    replayed=json.loads(output.read_text())
    by_direction={tuple(row['directions']):row for row in replayed['records']}
    for row in retained['records']:
        fresh=by_direction[tuple(row['directions'])]
        assert fresh['witness_count']==row['witness_count'],row['directions']
        assert fresh['witness_sequence_sha256']==row['witness_sequence_sha256'],row['directions']
    assert replayed['summary']['witness_count']==retained['summary']['witness_count']
    return {'replayed_directions':len(retained['records']),
            'replayed_witnesses':retained['summary']['witness_count']}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--quick',action='store_true',
        help='check the retained joint record bindings and endpoints only, without regenerating the witness sequences')
    parser.add_argument('--compact-cache',type=Path,default=COMPACT_CACHE)
    parser.add_argument('--workers',type=int,default=8)
    args=parser.parse_args()
    result=report()
    if args.write:OUTPUT.write_text(json.dumps(result,indent=2)+'\n')
    else:
        retained=load(OUTPUT.name)
        assert result==retained
    print(json.dumps(result,indent=2))
    if args.quick:
        print('quick: joint witness sequences not regenerated; the source and endpoint bindings of the retained joint record were checked')
    else:print(json.dumps(replay_joint(args.compact_cache,args.workers),indent=2))


if __name__=='__main__':main()
