"""Numerical stopping heights for rational positive-part Pade clauses.

The caller supplies a uniform coefficient-gcd estimate exp(ell*m), valid
for both adjacent rectangles at every m>=m0. A stronger ell can be used
without changing the retained rational cofactor clause. An independently
verified weakening of its threshold can also permit a smaller ell.
"""
from fractions import Fraction
from functools import lru_cache
from math import prod

from mpmath import iv

from erdos_699_off_diagonal_pade import growth_parameters, rational

iv.dps = 80


@lru_cache(maxsize=None)
def _growth(seed, directions, ell, terms, scale):
    return growth_parameters(*seed, *directions, ell, terms=terms, sum_scale=scale)


def joint_clause_threshold(certificate, m0, *, gap, maximum_shift,
                           gcd_log_rate=None, integral_trim=None,
                           threshold_weakening=0):
    """Certify the stated clause for all h>=10**K.

    `gap` bounds |X-Y| and may be zero. X,Y are equal-degree products
    of factors in [h,h+maximum_shift]. The actual gap may vanish even
    when a positive upper bound is supplied: the seed determinant, not
    the actual gap, supplies the nonzero integer.
    """
    source = certificate['source']
    seed = source['seed']
    P, Q, a, b = (seed[key] for key in ('P', 'Q', 'a', 'b'))
    T, delta = a*P, a*P-b*Q
    A, B, C = source['directions']
    H, left, right = A+B+C, A+B, B+C
    degree = certificate['product_degree']
    original_ell = Fraction(source['gcd_log_rate'])
    ell = original_ell if gcd_log_rate is None else Fraction(gcd_log_rate)
    assert ell > 0 and m0 >= 2 and B*m0 >= 2
    assert delta > 0 and gap >= 0 and maximum_shift >= 0 and degree >= 1
    c0, k0, _ = _growth((P,Q,a,b), (A,B,C), original_ell,
                        source['gcd_terms'], source.get('gcd_sum_rounding_denominator'))
    components = certificate['components']
    assert len({p for p,power,multiplicity,side in components}) == len(components)
    for side, expected in enumerate((P,Q)):
        assert prod(p**power for p,power,multiplicity,s in components if s==side) == expected
        assert sum(multiplicity for p,power,multiplicity,s in components if s==side) == degree
    block = Fraction(certificate['block_parameter'])
    tau = rational(block)
    original_threshold = Fraction(certificate['positive_part_threshold'])
    weakening = Fraction(threshold_weakening)
    threshold = original_threshold-weakening
    assert 0 <= weakening < original_threshold and threshold > 0 and tau > 0
    intercepts = certificate['positive_part_intercepts']
    assert set(intercepts) == {str(p) for p,power,multiplicity,side in components}
    for p,power,multiplicity,side in components:
        assert min(p,power,multiplicity) > 0 and side in (0,1)
        raw = tau*(left if side==0 else right)*power*iv.log(p)-multiplicity
        assert rational(intercepts[str(p)]) > raw
    assert tau*c0 > rational(original_threshold) and tau*k0-degree > rational(original_threshold)

    entropy = H*iv.log(H)-A*iv.log(A)-B*iv.log(B)-C*iv.log(C)
    q_rate = left*iv.log(P)-right*iv.log(b)-A*iv.log(T)+rational(original_ell)-c0
    e_rate = (left*iv.log(P)+right*iv.log(Q)-B*iv.log(T)
              -(A+C)*iv.log(delta)+rational(original_ell)-k0)
    log_mq, log_me = q_rate-entropy, e_rate-entropy
    assert log_mq < 0 and log_me < 0
    F = max(Fraction(B), Fraction((H+1)*B*B,A*C))
    trim = Fraction(2,B) if integral_trim is None else Fraction(integral_trim)
    assert Fraction(2,B) <= trim <= m0
    log_q_prefactor = iv.log(rational(F))-rational(trim)*log_mq
    log_e_prefactor = iv.log(rational(F))-rational(trim)*log_me
    c0 += rational(ell-original_ell)
    k0 += rational(ell-original_ell)
    eta1, eta2 = tau*c0-rational(threshold), tau*k0-rational(threshold)-degree
    assert eta1 > 0 and eta2 > 0
    log_a2 = 3*iv.log(delta)-iv.log(T)+log_e_prefactor
    # Twice each term must be <1; this avoids weakening to a common rate.
    log_b2 = iv.log(2*tau)+degree*iv.log(2)+log_a2+k0
    log_a1 = iv.log(gap*T)+log_q_prefactor if gap else None
    log_b1 = iv.log(2*tau)+log_a1+c0 if gap else None

    def holds(cap):
        if cap <= 0:
            return False
        x = cap*iv.log(10)
        return (tau*x >= m0+1 and x >= iv.log(maximum_shift+1)
                and eta2*x > 1 and log_b2+iv.log(x)-eta2*x < 0
                and (not gap or (eta1*x > 1 and log_b1+iv.log(x)-eta1*x < 0)))

    upper = 1
    while not holds(upper):
        upper *= 2
    lower = 0
    while upper-lower > 1:
        middle = (lower+upper)//2
        if holds(middle):
            upper = middle
        else:
            lower = middle
    assert holds(upper)
    x = upper*iv.log(10)
    values = {
        'first_decay_rate':c0, 'second_decay_rate':k0,
        'first_uniform_gain':eta1, 'second_uniform_gain':eta2,
        'log_Q_integrand_maximum':log_mq, 'log_E_integrand_maximum':log_me,
        'log_Q_prefactor':log_q_prefactor, 'log_E_prefactor':log_e_prefactor,
        'log_second_prefactor':log_a2, 'second_doubled_log_coefficient':log_b2,
        'threshold_second_doubled_log_upper_bound':log_b2+iv.log(x)-eta2*x,
        'threshold_block_lower_bound':tau*x,
    }
    if gap:
        values.update({'log_first_prefactor':log_a1,
                       'first_doubled_log_coefficient':log_b1,
                       'threshold_first_doubled_log_upper_bound':log_b1+iv.log(x)-eta1*x})
    return {
        'seed':seed, 'directions':[A,B,C], 'components':components,
        'product_degree':degree, 'gap_bound':gap, 'maximum_shift':maximum_shift,
        'gcd_m0':m0, 'original_gcd_log_rate':str(original_ell),
        'gcd_log_rate':str(ell), 'gcd_rate_increase':str(ell-original_ell),
        'block_parameter':str(block), 'positive_part_threshold':str(threshold),
        'original_positive_part_threshold':str(original_threshold),
        'threshold_weakening':str(weakening),
        'positive_part_intercepts':intercepts, 'factorial_prefactor_F':str(F),
        'integral_trim':str(trim), 'threshold_power_of_ten':upper,
        'intervals':{key:iv.nstr(value,40) for key,value in values.items()},
        'conclusion':'For every h>=10^K the stated positive-part inequality holds, including actual product gap zero.',
    }
