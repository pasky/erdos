#!/usr/bin/env python3
"""Close a terminal prime-power orthant with an independent numerical pair theorem.

The retained finite strip files are unchanged. All calculations here use their
final exponents, rational source targets, and short directed logarithms.
"""
from fractions import Fraction
import json
from math import floor
from pathlib import Path

from mpmath import iv

iv.dps=80
HERE=Path(__file__).resolve().parent


def rational(value):
    value=Fraction(value)
    return iv.mpf(value.numerator)/value.denominator


def verify_unbounded_prefix(record):
    p,q=record['pair'];r=record.get('cofactor_exponent_numerator',1)
    s=record.get('cofactor_exponent_denominator',record.get('reciprocal_exponent_denominator'))
    assert 0<2*r<=s
    boundary_cap=record['height_cap_power_of_ten']
    prefix=record
    while 'continuation' in prefix:
        continuation=prefix['continuation'];name=continuation['source_file']
        assert Path(name).name==name
        path=HERE/name
        matches=[row for row in json.loads(path.read_text())['records'] if row['pair']==[p,q]]
        assert len(matches)==1
        prior=matches[0]
        assert prior['height_cap_power_of_ten']<prefix['height_cap_power_of_ten']
        boundary_cap=min(boundary_cap,prior['height_cap_power_of_ten'])
        prefix=prior
    c=s-r;cursor=record['initial_exponents'][:]
    for anchor in record['anchors']:
        assert cursor==[anchor['p_exponent'],anchor['q_exponent']]
        advances=[anchor['p_exponent_advance'],anchor['q_exponent_advance']]
        assert all(type(x)is int and x>=0 for x in advances) and max(advances)>0
        if anchor['method']=='exact boundary lines':
            # p^a < 2^(a*bit_length(p)); this deliberately loose integer
            # estimate suffices for every retained small boundary anchor.
            bits=max(cursor[0]*p.bit_length(),cursor[1]*q.bit_length())
            # Even the earliest generation's height filter was inactive.
            assert c+(c+s)*bits<3*c*boundary_cap
        cursor=[x+y for x,y in zip(cursor,advances)]
    assert cursor==record['final_exponents']


def certify_terminal_corner(record,source):
    verify_unbounded_prefix(record)
    p,q=record['pair'];A,B=record['final_exponents']
    assert source['pair']==[p,q] and source['gap']>=record['maximum_difference']
    targets=source['targets_by_prime']
    alpha,beta=Fraction(targets[str(p)]),Fraction(targets[str(q)])
    assert 0<alpha<Fraction(1,2) and 0<beta<Fraction(1,2)
    source_power=source['threshold_power_of_ten']
    assert source_power>=3 and record['maximum_difference']<1000
    lp,lq,l10,l2=iv.log(p),iv.log(q),iv.log(10),iv.log(2)
    frontier=[A*lp,B*lq]
    assert all((value-source_power*l10).a>0 for value in frontier)
    slopes=[1-rational(alpha),1-rational(beta)]
    proposals=[(value-l2)/(slope*l10) for value,slope in zip(frontier,slopes)]
    power=floor(float(min(value.a for value in proposals)))
    def margins(k):return [value-l2-k*slope*l10 for value,slope in zip(frontier,slopes)]
    while not all(value.a>0 for value in margins(power)):power-=1
    while all(value.a>0 for value in margins(power+1)):power+=1
    assert power>record['height_cap_power_of_ten']
    return {
        'pair':[p,q],'final_exponents':[A,B],
        'original_finite_exponent':str(Fraction(record.get('cofactor_exponent_numerator',1),
            record.get('cofactor_exponent_denominator',record.get('reciprocal_exponent_denominator')))),
        'numerical_global_targets':[str(alpha),str(beta)],
        'numerical_global_height_threshold_power_of_ten':source_power,
        'previous_finite_cap_power_of_ten':record['height_cap_power_of_ten'],
        'terminal_corner_cap_power_of_ten':power,
        'logarithmic_margins':[iv.nstr(value,35) for value in margins(power)],
        'conclusion':'The remaining orthant contains no positive pair solution below the stated height cap.'}


def main():
    source_path=HERE/'erdos_699_i10_numerical_pairs.json'
    sources=json.loads(source_path.read_text())['choices']
    groups=[]
    for index,name in [(7,'erdos_699_prime_pair_strips_7_extended.json'),
                       (9,'erdos_699_prime_pair_strips_9_extended.json')]:
        path=HERE/name;records=json.loads(path.read_text())['records'];rows=[]
        for record in records:
            source=next(r for r in sources if r['pair']==record['pair'])
            rows.append(certify_terminal_corner(record,source))
        groups.append({'index':index,'input_strip_file':name,
                       'common_extended_pair_cap_power_of_ten':min(r['terminal_corner_cap_power_of_ten'] for r in rows),
                       'records':rows})
    result={'scope':'Analytic extension of the pair cofactor ranges. Existing finite-index aggregate certificates remain unchanged.',
            'source_file':source_path.name,
            'groups':groups,'new_modular_inversions':0}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({str(g['index']):g['common_extended_pair_cap_power_of_ten'] for g in groups},indent=2))


if __name__=='__main__':main()
