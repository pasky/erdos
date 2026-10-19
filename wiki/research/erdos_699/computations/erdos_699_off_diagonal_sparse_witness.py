"""Integer certificates for sparse Padé indices covering log-height intervals.

A pointwise coefficient-gcd lower bound at one integer m suffices. After
directed setup, witness endpoints use integer arithmetic only. The same m
can cover [m/t,next_m/t] for several source clauses with different t.
"""

from fractions import Fraction as F
from math import prod

from mpmath import iv

from erdos_699_off_diagonal_pade import growth_parameters, rational

SCALE = 1 << 32
iv.dps = 100
LOG2_UPPER_SCALED = int((iv.log(2)*SCALE).b)+1
assert rational(F(LOG2_UPPER_SCALED,SCALE)) > iv.log(2)


def _lower_scaled(value):
    result = int((value*SCALE).a)-1
    assert rational(F(result,SCALE)) < value
    return result


def _upper_scaled(value):
    result = int((value*SCALE).b)+1
    assert rational(F(result,SCALE)) > value
    return result


def prepare_witness(certificate, *, source_id, threshold_weakening,
                    gap, maximum_shift, shrinking_cost=False):
    """Certify rational constants for a fixed retained source clause."""
    source = certificate['source']
    seed = source['seed']
    P,Q,a,b = (seed[key] for key in ('P','Q','a','b'))
    A,B,C = source['directions']
    H,left,right = A+B+C,A+B,B+C
    T,delta = a*P,a*P-b*Q
    assert delta > 0 and gap > 0 and maximum_shift >= 0
    ell = F(source['gcd_log_rate'])
    c0,k0,_ = growth_parameters(
        P,Q,a,b,A,B,C,ell,terms=source['gcd_terms'],
        sum_scale=source.get('gcd_sum_rounding_denominator'))
    degree = certificate['product_degree']
    components = certificate['components']
    assert len({p for p,power,multiplicity,side in components}) == len(components)
    for side,expected in enumerate((P,Q)):
        assert prod(p**power for p,power,multiplicity,s in components if s==side) == expected
        assert sum(multiplicity for p,power,multiplicity,s in components if s==side) == degree
    t = F(certificate['block_parameter'])
    original_R = F(certificate['positive_part_threshold'])
    weakening = F(threshold_weakening)
    R = original_R-weakening
    assert 0 <= weakening < original_R and R > 0 and t > 0
    for p,power,multiplicity,side in components:
        raw = rational(t)*(left if side==0 else right)*power*iv.log(p)-multiplicity
        assert rational(certificate['positive_part_intercepts'][str(p)]) > raw
    assert rational(t)*c0 > rational(original_R)
    assert rational(t)*k0-degree > rational(original_R)

    entropy = H*iv.log(H)-A*iv.log(A)-B*iv.log(B)-C*iv.log(C)
    q = left*iv.log(P)-right*iv.log(b)-A*iv.log(T)+rational(ell)-c0
    e = (left*iv.log(P)+right*iv.log(Q)-B*iv.log(T)
         -(A+C)*iv.log(delta)+rational(ell)-k0)
    trim = F(2,B)
    prefactor = max(F(B),F((H+1)*B*B,A*C))
    log_Q_prefactor = iv.log(rational(prefactor))-rational(trim)*(q-entropy)
    log_E_prefactor = iv.log(rational(prefactor))-rational(trim)*(e-entropy)
    first_prefactor = iv.log(2*gap*T)+log_Q_prefactor
    second_prefactor = ((degree+1)*iv.log(2)+3*iv.log(delta)-iv.log(T)
                        +log_E_prefactor)
    result = {
        'source_id':source_id, 'seed':seed, 'directions':[A,B,C],
        'product_degree':degree, 'gap_bound':gap, 'maximum_shift':maximum_shift,
        'threshold_weakening':str(weakening), 'block_parameter':str(t),
        'positive_part_threshold':str(R), 'scale':SCALE,
        'intrinsic_first_rate_lower_scaled':_lower_scaled(c0-rational(ell)),
        'intrinsic_second_rate_lower_scaled':_lower_scaled(k0-rational(ell)),
        'first_doubled_log_prefactor_upper_scaled':_upper_scaled(first_prefactor),
        'second_doubled_log_prefactor_upper_scaled':_upper_scaled(second_prefactor),
        'first_height_coefficient':str(R/t),
        'second_height_coefficient':str((R+degree)/t),
        'log2_upper_scaled':LOG2_UPPER_SCALED,
        'integral_trim':str(trim), 'factorial_prefactor_F':str(prefactor),
    }
    if shrinking_cost:
        kappa_scaled = min(_lower_scaled(
            (left if side==0 else right)*power*iv.log(p))
            for p,power,multiplicity,side in components)
        assert kappa_scaled > 0
        kappa = F(kappa_scaled,SCALE)
        J = k0-c0
        assert J > 0
        ratio = degree/(rational(t)*J)
        offset = (second_prefactor-first_prefactor)/J
        result.update({
            'kappa_lower_scaled':kappa_scaled,
            'degree_over_block':str(F(degree)/t),
            # These are proposals only; every chosen integer m is verified.
            'balanced_index_ratio':str(F(str(float(ratio.mid))).limit_denominator(10**12)),
            'balanced_index_offset':str(F(str(float(offset.mid))).limit_denominator(10**12)),
            'zero_cost_index_ratio':str(max(F(0),1-R/(t*kappa))),
        })
    return result


def _upper_numerators(prepared, m, log_gcd_lower_scaled):
    assert type(m) is int and m >= 2
    assert type(log_gcd_lower_scaled) is int and log_gcd_lower_scaled >= 0
    assert prepared['scale'] == SCALE
    log_m_upper = m.bit_length()*prepared['log2_upper_scaled']
    first = (prepared['intrinsic_first_rate_lower_scaled']*m+log_gcd_lower_scaled
             -log_m_upper-prepared['first_doubled_log_prefactor_upper_scaled'])
    second = (prepared['intrinsic_second_rate_lower_scaled']*m+log_gcd_lower_scaled
              -log_m_upper-prepared['second_doubled_log_prefactor_upper_scaled'])
    return first,second


def next_index(prepared, m, log_gcd_lower_scaled):
    """Largest integer right endpoint certified by the stored lower bounds."""
    numerators = _upper_numerators(prepared,m,log_gcd_lower_scaled)
    coefficients = [F(prepared[key]) for key in
                    ('first_height_coefficient','second_height_coefficient')]
    # numerator > SCALE*coefficient*next_m, with a strict integer test.
    return min((n*c.denominator-1)//(SCALE*c.numerator)
               for n,c in zip(numerators,coefficients))


def verify_step(prepared, m, next_m, log_gcd_lower_scaled):
    """Verify that this m certifies every log h in [m/t,next_m/t]."""
    if type(next_m) is not int or next_m <= m:
        return False
    nums = _upper_numerators(prepared,m,log_gcd_lower_scaled)
    coefs = [F(prepared[key]) for key in
             ('first_height_coefficient','second_height_coefficient')]
    return all(n*c.denominator > SCALE*c.numerator*next_m for n,c in zip(nums,coefs))


def group_next(prepared_sources, m, log_gcd_lower_scaled):
    result = min(next_index(p,m,log_gcd_lower_scaled) for p in prepared_sources)
    if result > m:
        assert all(verify_step(p,m,result,log_gcd_lower_scaled) for p in prepared_sources)
    return result


def verify_window(prepared, m, left_index, right_index, log_gcd_lower_scaled):
    """Check the improved cost on [left_index/t,right_index/t], m<=left.

    The caller separately ensures h>maximum_shift on the covered heights.
    Convexity makes the two integer endpoint checks sufficient.
    """
    if not (type(left_index) is int and type(right_index) is int
            and m <= left_index < right_index):
        return False
    U,V = _upper_numerators(prepared,m,log_gcd_lower_scaled)
    kappa = prepared['kappa_lower_scaled']
    a = F(prepared['first_height_coefficient'])
    b = F(prepared['second_height_coefficient'])
    d = F(prepared['degree_over_block'])
    for y in (left_index,right_index):
        if not U > 0:
            return False
        if not U*a.denominator > kappa*m*a.denominator+(SCALE*a.numerator-kappa*a.denominator)*y:
            return False
        if not V*d.denominator > SCALE*d.numerator*y:
            return False
        if not V*b.denominator > kappa*m*b.denominator+(SCALE*b.numerator-kappa*b.denominator)*y:
            return False
    return True


def window_right(prepared, m, left_index, log_gcd_lower_scaled):
    """Largest right integer endpoint under the shrinking denominator bound."""
    assert type(left_index) is int and left_index >= m
    U,V = _upper_numerators(prepared,m,log_gcd_lower_scaled)
    kappa = prepared['kappa_lower_scaled']
    a = F(prepared['first_height_coefficient'])
    b = F(prepared['second_height_coefficient'])
    d = F(prepared['degree_over_block'])
    left_ok = (U > 0
               and U*a.denominator > kappa*m*a.denominator+(SCALE*a.numerator-kappa*a.denominator)*left_index
               and V*d.denominator > SCALE*d.numerator*left_index
               and V*b.denominator > kappa*m*b.denominator+(SCALE*b.numerator-kappa*b.denominator)*left_index)
    if not left_ok:
        return left_index
    bounds = [(V*d.denominator-1)//(SCALE*d.numerator)]
    for numerator,coef in ((U,a),(V,b)):
        slope = SCALE*coef.numerator-kappa*coef.denominator
        if slope > 0:
            bounds.append(((numerator-kappa*m)*coef.denominator-1)//slope)
    result = min(bounds)
    if result > left_index:
        assert verify_window(prepared,m,left_index,result,log_gcd_lower_scaled)
    return result


def group_window(prepared_sources, m, left_index, log_gcd_lower_scaled):
    result = min(window_right(p,m,left_index,log_gcd_lower_scaled)
                 for p in prepared_sources)
    if result > left_index:
        assert all(verify_window(p,m,left_index,result,log_gcd_lower_scaled)
                   for p in prepared_sources)
    return result


def index_proposals(prepared_sources, left_index):
    """A few deterministic integer Padé-index proposals, never evidence."""
    candidates = {left_index}
    for source in prepared_sources:
        balanced = (F(source['balanced_index_ratio'])*left_index
                    +F(source['balanced_index_offset']))
        zero = F(source['zero_cost_index_ratio'])*left_index
        for value in (balanced,zero):
            center = value.numerator//value.denominator
            for m in (center-1,center,center+1):
                if 2 <= m <= left_index:
                    candidates.add(m)
    return sorted(candidates,reverse=True)
