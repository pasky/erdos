"""Index-nine adapter for shorter integer Pade witness blocks.

For a clause with intercepts g_p>t*a_p-b_p and threshold R, a witness
m=floor(t_new*log h), t_new<=t, has denominator cost at most
max(0,R-kappa*(t-t_new))*log h, where kappa<=min(a_p).
The clause and its exact Farkas coverage remain unchanged.
"""
from fractions import Fraction as F
from math import prod

from mpmath import iv
from erdos_699_off_diagonal_explicit_clauses import _growth
from erdos_699_off_diagonal_pade import rational

iv.dps = 80


def floor_rational(value, scale=10**15):
    result = F(int((value*scale).a),scale)
    while rational(result) > value:
        result -= F(1,scale)
    assert rational(result) <= value
    return result


def prepare(certificate, *, threshold_weakening=0, scale=10**15):
    source=certificate['source'];seed=source['seed']
    P,Q,a,b=(seed[k]for k in ('P','Q','a','b'))
    A,B,C=source['directions'];left,right=A+B,B+C
    ell=F(source['gcd_log_rate'])
    c0,k0,_=_growth((P,Q,a,b),(A,B,C),ell,source['gcd_terms'],source.get('gcd_sum_rounding_denominator'))
    t=F(certificate['block_parameter']);R=F(certificate['positive_part_threshold'])-F(threshold_weakening)
    degree=certificate['product_degree'];components=certificate['components']
    coefficients=[]
    assert len({p for p,_,_,_ in components})==len(components)
    for p,power,multiplicity,side in components:
        ap=(left if side==0 else right)*power*iv.log(p)
        assert rational(F(certificate['positive_part_intercepts'][str(p)])) > rational(t)*ap-multiplicity
        coefficients.append(ap)
    for side,expected in enumerate((P,Q)):
        assert prod(p**power for p,power,multiplicity,s in components if s==side)==expected
        assert sum(multiplicity for p,power,multiplicity,s in components if s==side)==degree
    kappa=min(floor_rational(x,scale)for x in coefficients)
    assert kappa>0 and all(rational(kappa)<=x for x in coefficients)
    candidates={t}
    balance=degree/(k0-c0)
    base=floor_rational(balance,scale)
    candidates.update(x for x in (base,base+F(1,scale))if 0<x<=t)
    if R>=0:
        zero=t-R/kappa
        if 0<zero<=t:candidates.add(zero)
    def gains(u):
        cost=max(F(0),R-kappa*(t-u))
        return rational(u)*c0-rational(cost),rational(u)*k0-rational(cost)-degree
    # Floating values only select among finitely many explicit candidates.
    # Every resulting margin is subsequently checked by directed intervals.
    u=max(candidates,key=lambda x:min(float(y.a)for y in gains(x)))
    g1,g2=gains(u);margin=min(floor_rational(g1,scale),floor_rational(g2,scale))
    assert margin>0
    # Some index-nine budgets permit ell<=0. Retain a simple positive
    # rate while preserving at least the proved margin reserve.
    requested=max(ell/2,ell-F(3,4)*margin/u)
    rate_scale=10**12
    requested=F((requested.numerator*rate_scale+requested.denominator-1)//requested.denominator,rate_scale)
    assert requested>0
    old_g1=rational(t)*c0-rational(R);old_g2=rational(t)*k0-rational(R)-degree
    return {
        'directions':[A,B,C], 'original_gcd_log_rate':str(ell),
        'original_block_parameter':str(t), 'witness_block_parameter':str(u),
        'kappa_lower':str(kappa), 'positive_part_threshold':str(R),
        'denominator_cost_rate':str(max(F(0),R-kappa*(t-u))),
        'threshold_weakening':str(F(threshold_weakening)),
        'old_uniform_margin_lower':str(min(floor_rational(old_g1,scale),floor_rational(old_g2,scale))),
        'new_uniform_margin_lower':str(margin),
        'requested_gcd_log_rate':str(requested),
        'rate_rounding_denominator':rate_scale,
        'minimum_remaining_margin':str(margin/4),
        'balanced_block_interval':iv.nstr(balance,35),
    }


def joint_clause_threshold(certificate,m0,*,gap,maximum_shift,gcd_log_rate,
                           threshold_weakening=0,prepared=None,integral_trim=None):
    prepared=prepare(certificate,threshold_weakening=threshold_weakening)if prepared is None else prepared
    assert prepared==prepare(certificate,threshold_weakening=threshold_weakening)
    source=certificate['source'];seed=source['seed'];P,Q,a,b=(seed[k]for k in('P','Q','a','b'))
    A,B,C=source['directions'];H=A+B+C;T=a*P;delta=T-b*Q
    oldell=F(source['gcd_log_rate']);ell=F(gcd_log_rate)
    assert ell>0 and m0>=2 and B*m0>=2 and gap>=0
    c0,k0,_=_growth((P,Q,a,b),(A,B,C),oldell,source['gcd_terms'],source.get('gcd_sum_rounding_denominator'))
    entropy=H*iv.log(H)-A*iv.log(A)-B*iv.log(B)-C*iv.log(C)
    q_rate=(A+B)*iv.log(P)-(B+C)*iv.log(b)-A*iv.log(T)+rational(oldell)-c0
    e_rate=(A+B)*iv.log(P)+(B+C)*iv.log(Q)-B*iv.log(T)-(A+C)*iv.log(delta)+rational(oldell)-k0
    mq,me=q_rate-entropy,e_rate-entropy
    assert mq<0 and me<0
    factorial=max(F(B),F((H+1)*B*B,A*C))
    trim=F(2,B)if integral_trim is None else F(integral_trim)
    assert F(2,B)<=trim<=m0
    log_q_prefactor=iv.log(rational(factorial))-rational(trim)*mq
    log_e_prefactor=iv.log(rational(factorial))-rational(trim)*me
    c0+=rational(ell-oldell);k0+=rational(ell-oldell)
    tau=rational(F(prepared['witness_block_parameter']));cost=rational(F(prepared['denominator_cost_rate']))
    degree=certificate['product_degree']
    eta1=tau*c0-cost;eta2=tau*k0-cost-degree
    assert eta1>0 and eta2>0
    log_a2=3*iv.log(delta)-iv.log(T)+log_e_prefactor
    log_b2=iv.log(2*tau)+degree*iv.log(2)+log_a2+k0
    log_a1=iv.log(gap*T)+log_q_prefactor if gap else None
    log_b1=iv.log(2*tau)+log_a1+c0 if gap else None
    def holds(cap):
        if cap<=0:return False
        x=cap*iv.log(10)
        return (tau*x>=m0+1 and x>=iv.log(maximum_shift+1)
                and eta2*x>1 and log_b2+iv.log(x)-eta2*x<0
                and(not gap or(eta1*x>1 and log_b1+iv.log(x)-eta1*x<0)))
    upper=1
    while not holds(upper):upper*=2
    lower=0
    while upper-lower>1:
        mid=(lower+upper)//2
        if holds(mid):upper=mid
        else:lower=mid
    assert holds(upper)
    return {
        **prepared,'seed':seed,'components':certificate['components'],
        'product_degree':degree,'gap_bound':gap,'maximum_shift':maximum_shift,
        'gcd_m0':m0,'gcd_log_rate':str(ell),
        'positive_part_intercepts':certificate['positive_part_intercepts'],
        'factorial_prefactor_F':str(factorial),'integral_trim':str(trim),
        'threshold_power_of_ten':upper,
        'intervals':{key:iv.nstr(value,40)for key,value in {
            'first_decay_rate':c0,'second_decay_rate':k0,
            'first_uniform_gain':eta1,'second_uniform_gain':eta2,
            'log_Q_integrand_maximum':mq,'log_E_integrand_maximum':me,
            'second_doubled_log_coefficient':log_b2,
            **({'first_doubled_log_coefficient':log_b1}if gap else{}),
        }.items()},
        'conclusion':'For every h>=10^K the unchanged retained positive-part clause holds, using the displayed shorter witness block.',
    }
