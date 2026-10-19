"""Rational necessary cofactor clauses from directed off-diagonal sources.

These certificates eliminate floating coefficients from subsequent linear
programs. Each returned disjunction is valid above an effective threshold.
The seed product identity, where needed, is a separate explicit hypothesis.
"""

from fractions import Fraction
from itertools import combinations
import json
from math import prod, floor, ceil
from pathlib import Path

from mpmath import iv
from erdos_699_off_diagonal_pade import growth_parameters, rational


def rational_joint_clause(seed, directions, ell, components, degree=1,
                          terms=200, block=None, scale=10**8,
                          gcd_sum_scale=None):
    """Return OR clauses sum(mult_p*e_p)>=rational_rhs.

    seed=(P,Q,a,b); components=(prime, seed power, multiplicity, side).
    The positive integer multiplicities on either side sum to degree.
    `block` is the rational t in m~t log h. The default rationalizes the
    balanced t=degree/(k0-c0). All rounding is verified with intervals.
    """
    assert degree >= 1 and scale >= 100
    assert len({p for p,A,m,s in components}) == len(components)
    for side,expected in enumerate(seed[:2]):
        assert prod(p**A for p,A,m,s in components if s==side)==expected
        assert sum(m for p,A,m,s in components if s==side)==degree
    c0,k0,source=growth_parameters(*seed,*directions,ell,terms=terms,
                                   sum_scale=gcd_sum_scale)
    assert k0>c0
    if block is None:
        block=Fraction(str(float((degree/(k0-c0)).mid))).limit_denominator(10**12)
    block=Fraction(block)
    assert block>0
    t=rational(block)
    rates=[t*c0,t*k0-degree]
    limiting=iv.mpf([min(x.a for x in rates),min(x.b for x in rates)])
    assert limiting>0
    # Reserve a strict amount for the effective asymptotic estimates.
    numerator=floor(float(limiting.a)*scale)-2
    threshold=Fraction(numerator,scale)
    while not rational(threshold+Fraction(1,scale))<limiting:
        numerator-=1;threshold=Fraction(numerator,scale)
    assert threshold>0
    weights=[]
    for p,A,m,side in components:
        assert p>=2 and A>=1 and m>=1 and side in (0,1)
        length=source['left_block'] if side==0 else source['right_block']
        value=t*length*A*iv.log(p)-m
        numerator=ceil(float(value.b)*scale)+1
        upper=Fraction(numerator,scale)
        while not rational(upper)>value:
            numerator+=1;upper=Fraction(numerator,scale)
        weights.append((p,m,upper))
    clauses=[]
    for size in range(1,len(weights)+1):
        for subset in combinations(weights,size):
            clauses.append({'coefficients':{str(p):m for p,m,g in subset},
                            'rhs':str(threshold-sum((g for p,m,g in subset),Fraction(0)))})
    return {
        'source':source,'product_degree':degree,
        'components':[list(v) for v in components],
        'block_parameter':str(block),'rounding_scale':scale,
        'positive_part_intercepts':{str(p):str(g) for p,m,g in weights},
        'positive_part_threshold':str(threshold),
        'strict_source_margin_at_least':str(Fraction(1,scale)),
        'clauses':clauses,
        'meaning':'At least one listed rational linear inequality holds above an effective height.',
    }


def main():
    row=rational_joint_clause((847,845,1,1),(39,7,33),3,
        [(7,1,1,0),(11,2,1,0),(5,1,1,1),(13,2,1,1)],degree=2)
    out=Path(__file__).with_suffix('.json')
    out.write_text(json.dumps({'records':[row]},indent=2)+'\n')
    print(json.dumps({'output':str(out),'clause_count':len(row['clauses']),
                     'threshold':row['positive_part_threshold']},indent=2))


if __name__=='__main__':main()
