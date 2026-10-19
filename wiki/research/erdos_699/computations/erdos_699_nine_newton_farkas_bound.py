"""Sharpen the algebraic index-9 tail using monic Newton bases and exact Farkas weights.

Each polynomial row has right side b0 + E/log10(h), where h=n-8.
The retained proof used b0+epsilon. Removing epsilon from those rows gives
alpha = -weighted_rhs + epsilon*sum(polynomial multipliers) > 0.
The leaf is impossible once log10(h) > sum(lambda*E)/alpha.

This reuses the existing rank and analytic-source certificates; it does not
rerun ranks or assign numerical thresholds to the analytic sources. Exact
Farkas checking is repeated against the unchanged ordered tree rows.
"""
from fractions import Fraction
import gzip
import json
from pathlib import Path
import erdos_699_index_9_effective as main
import erdos_699_nine_polynomial_cuts as poly
ROOT = main.ROOT
from erdos_699_index_7_polynomial_bounds import newton_jet_tables, ceiling_log10
from hashlib import sha256

def new_bounds(record,roots):
 d,r=record['interpolation_degree'],record['symmetric_jet_count'];z=dict(record);z.setdefault('row_factor_exponents',[0]*9);z.setdefault('diagonal_power',0)
 if not r:return {'name':record['name'],'minor_power':0,'basis_norm_power':0,'constant_power':poly.constant_power(z),'basepoint_power':0,'roots':list(roots)}
 vals,prefix=newton_jet_tables(d,9,tuple(roots));h,m,q,k=z['line_exponents'],z['row_multiplicities'],z['row_factor_exponents'],z['diagonal_power'];power=0;count=0;dig=sha256()
 for t in range(9):
  for x in range(t//2+1):
   y=t-x;res=max(0,m[t]-h[x]-h[y]-q[t]-(k if x==y else 0))
   for o in range(res):
    for a in range(o+1):
     b=o-a
     if x==y and a>b:continue
     entry=2*max(abs(vals[x][j][a])*prefix[y][b][d-j] for j in range(a,d-b+1))
     p=(ceiling_log10(r*entry*entry)+1)//2
     assert r*entry*entry<=10**(2*p)
     power+=p;count+=1;dig.update(f'{x}:{y}:{a}:{b}:{p}\n'.encode())
 assert count==r
 norm=ceiling_log10((1+max(roots))**d)
 E=poly.constant_power(z)-r*(d+6)+power+norm
 bp=0
 if record.get('nonvanishing_method')=='coprime_kernel':
  s=record['symmetric_monomial_count'];assert2=2*s*(s+1)*record['modular_prime'];assert assert2<10**20
  bp=2*d*(power+norm+20+d+8)+2
 newton_jet_tables.cache_clear()
 return {'name':record['name'],'jet_count':r,'interpolation_degree':d,'minor_power':power,'basis_norm_power':norm,'constant_power':E,'basepoint_power':bp,'roots':list(roots),'row_bounds_sha256':dig.hexdigest()}




def main_bound():
    proof=json.load(gzip.open(main.DATA,'rt'))
    baseline=json.load(open(ROOT/'erdos_699_index_9_baseline.json'))
    extra=json.load(open(ROOT/'erdos_699_nine_polynomial_cuts.json'))
    source_data=json.load(gzip.open(ROOT/'erdos_699_nine_cofactor_clauses.json.gz','rt'))
    sources={r['id']:r for r in source_data['records']};ordinary=main.ordinary_sources()
    polys={r['name']:r for r in baseline['certificates']+extra['certificates']}
    needed = {name for row in proof['roots'] for name in row['polynomial_ids']}
    needed.update(row['name'] for row in baseline['certificates'])
    newton = {}
    for name in sorted(needed):
        row = polys[name]
        if row['symmetric_jet_count']:
            newton[name] = min((new_bounds(row, range(length)) for length in (5, 6, 7)),
                               key=lambda value: value['constant_power'])
        else:
            z = dict(row)
            z.setdefault('row_factor_exponents', [0]*9)
            z.setdefault('diagonal_power', 0)
            newton[name] = {'name': name, 'jet_count': 0, 'minor_power': 0,
                            'basis_norm_power': 0, 'constant_power': poly.constant_power(z),
                            'basepoint_power': 0, 'roots': []}
    constants={};basepoints={}
    for name,r in polys.items():
     z=dict(r);z.setdefault('row_factor_exponents',[0]*9);z.setdefault('diagonal_power',0)
     constants[name]=newton[name]['constant_power'] if name in newton else poly.constant_power(z)
     basepoints[name]=newton[name]['basepoint_power'] if name in newton else (poly.basepoint_bound(z) if z.get('nonvanishing_method')=='coprime_kernel' else 0)
    leaves=[];roots=[];weighted_polynomials=set()
    for ri,root in enumerate(proof['roots']):
     case=baseline['residual_cases'][root['root_index']]
     ids=root['polynomial_ids'];selected=[polys[n] for n in ids];base=main.base_rows(case,selected)
     stack=[(0,[])];worst=Fraction(0)
     while stack:
      ni,region=stack.pop();node=root['tree'][ni]
      if 'farkas' not in node:
       for mask,child in zip(node['masks'],node['children']):stack.append((child,region+main.branch_rows(node['source'],mask,sources,ordinary)))
       continue
      cert=node['farkas'];rows=base+region
      assert main.verify_infeasibility_certificate(rows,cert)
      polyweights=[(ids[index],Fraction(w)) for index,w in zip(cert['support'],cert['multipliers']) if index<len(ids)]
      weighted_polynomials.update(name for name,w in polyweights if w > 0)
      eps_weight=sum((w for name,w in polyweights),Fraction(0))
      alpha=-Fraction(cert['weighted_rhs'])+main.SLACK*eps_weight
      height=sum((w*constants[name] for name,w in polyweights),Fraction(0))
      cap=height/alpha
      record={'root_index':root['root_index'],'node_index':ni,'positions':case['positions'],'vector_scaled':case['vector_scaled'],'cap':str(cap),'cap_decimal':float(cap),'alpha':str(alpha),'weighted_constant':str(height),'polynomial_weights':[[name,str(w),constants[name],basepoints[name]] for name,w in polyweights]}
      leaves.append(record);worst=max(worst,cap)
     roots.append({'root_index':root['root_index'],'weighted_cap':str(worst),'weighted_cap_decimal':float(worst)})
    leaves.sort(key=lambda r:Fraction(r['cap']),reverse=True)
    baseline_caps=[]
    for r,count,gain in zip(baseline['certificates'],baseline['certificate_first_use_counts'],baseline['certificate_first_use_min_gains_scaled']):
     if not count:continue
     cap=Fraction(10000*constants[r['name']],gain)
     baseline_caps.append({'polynomial':r['name'],'cases':count,'gain_scaled':gain,'constant':constants[r['name']],'cap':str(cap),'cap_decimal':float(cap)})
    baseline_caps.sort(key=lambda r:Fraction(r['cap']),reverse=True)
    assert len(leaves) == proof['farkas_leaf_count']
    assert len(roots) == proof['residual_root_cases']
    assert sum(r['cases'] for r in baseline_caps) == proof['baseline_covered_root_cases']
    used=weighted_polynomials
    basepoint_caps=sorted([{'polynomial':n,'cap':basepoints[n]} for n in used if basepoints[n]],key=lambda r:(-r['cap'],r['polynomial']))
    best=max(Fraction(leaves[0]['cap']),Fraction(baseline_caps[0]['cap']),Fraction(basepoint_caps[0]['cap']))
    result={'index':9,'height_variable':'h=n-8','claim':'The algebraic part of the retained proof holds above the stated power, conditional on the retained effective analytic-source thresholds.','leaf_count':len(leaves),'root_count':len(roots),'old_cap':proof['polynomial_height_threshold_power_of_ten'],'weighted_leaf_max':leaves[0],'baseline_max':baseline_caps[0],'basepoint_max':basepoint_caps[0],'overall_exact_cap':str(best),'overall_integer_power':best.numerator//best.denominator+1,'top_leaves':leaves[:30],'baseline_caps':baseline_caps,'basepoint_caps':basepoint_caps,'root_caps':roots}
    inputs = [main.DATA, ROOT/'erdos_699_index_9_baseline.json', ROOT/'erdos_699_nine_polynomial_cuts.json', ROOT/'erdos_699_nine_cofactor_clauses.json.gz']
    result['input_files'] = [path.name for path in inputs]
    result['polynomial_bounds'] = [newton[name] for name in sorted(newton)]
    result['basis_justification'] = 'Symmetric products of monic integer Newton polynomials give a unitriangular integer change from the original monomial basis. This preserves rank and the reductions of chosen kernel polynomials modulo 251.'
    result['ranks_recomputed'] = False
    result['basepoint_polynomials_actually_used_by_farkas'] = sorted(used)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    return result


if __name__ == "__main__":
    result = main_bound()
    print(json.dumps({key: result[key] for key in ("leaf_count", "root_count", "old_cap", "weighted_leaf_max", "baseline_max", "basepoint_max", "overall_exact_cap", "overall_integer_power")}, indent=2))
