"""Numerical Padé bounds with rational residual products and free block size.

The input coefficient-gcd lower bound and m0 must be independently certified.
Product identities and their bounded gaps are hypotheses supplied by
the caller. All successful box exclusions and returned height bounds use
directed intervals; floating point only proposes a block parameter.
"""

from fractions import Fraction
import json
from math import prod
from pathlib import Path

from mpmath import iv

from erdos_699_bft_explicit_thresholds import explicit_bound, interval_max, interval_min
from erdos_699_bft_pair_extension import rational
from erdos_699_bft_dusart_gcd import gcd_exponent_lower

iv.dps = 80


def rational_product_bound(seed, log_l1, m0, gap, components,
                           degree=2, shift=13, block=None):
    """Exclude an upper cofactor box, with a numerical height threshold.

    components=(prime, seed exponent, factor multiplicity, side, upper exponent).
    Each factor lies in [h,h+shift]. Each product has degree `degree`, and
    the two products have difference of absolute value <=gap, possibly zero.
    `block`, when given, is a positive rational t with cm~t log h.
    Otherwise the balanced block and all positive denominator breakpoints
    propose candidates; only a final rational, interval-verified t is used.
    Return None if no proposed block gives strictly positive margins.
    """
    P, Q, a, b, c, d = seed
    assert degree >= 1 and shift >= 1
    assert len({x[0] for x in components}) == len(components)
    for side, expected in ((0, P), (1, Q)):
        assert prod(p**A for p, A, m, s, e in components if s == side) == expected
        assert sum(m for p, A, m, s, e in components if s == side) == degree
    for p, A, m, side, e in components:
        assert p >= 2 and A >= 1 and m >= 1 and side in (0, 1)
        assert 0 <= Fraction(e) <= 1
    vals = explicit_bound(*seed, log_l1, m0, gap, Fraction(1, 100))
    s = rational(Fraction(c, d))
    C = vals['log_omega3']/s
    K = iv.log(max(P, Q)) + vals['log_omega4']/s
    J = K-C
    assert J > 0
    coordinates = [(A*iv.log(p), m*(1-rational(e)))
                   for p, A, m, side, e in components]

    def margins(t):
        delta = sum((interval_max([iv.mpf(0), t*A-w])
                     for A, w in coordinates), iv.mpf(0))
        return t*C-delta, t*K-delta-degree, delta

    if block is None:
        candidates = [degree/J]
        candidates.extend(w/A for A, w in coordinates if w > 0)
        proposals = []
        for t in candidates:
            # No floating result is treated as evidence: rationalize it and
            # re-evaluate both margins with directed intervals below.
            tf = Fraction(str(float(t.mid))).limit_denominator(10**12)
            if tf > 0:
                first, second, _ = margins(rational(tf))
                proposals.append((float(min(first.a, second.a)), tf))
        _, block = max(proposals)
    block = Fraction(block)
    assert block > 0
    first, second, delta = margins(rational(block))
    if not (first > 0 and second > 0):
        return None
    saving = interval_min([first, second])
    log_A = iv.log(vals['kappa1']/2*iv.exp(c*C)
                   + 2**(degree-1)/vals['kappa2']*iv.exp(c*K))
    terms = [iv.log(shift), c*(m0+1)/rational(block), log_A/saving]
    bound = interval_max(terms)
    cap = max(1, int(float((bound/iv.log(10)).b))+1)
    while not bound < cap*iv.log(10):
        cap += 1
    return {
        'seed': list(seed), 'm0': m0, 'gap': gap,
        'degree': degree, 'maximum_shift': shift,
        'components': [[p,A,m,side,str(e)] for p,A,m,side,e in components],
        'block_parameter': str(block),
        'C': iv.nstr(C, 32), 'K': iv.nstr(K, 32), 'J': iv.nstr(J, 32),
        'denominator_cost': iv.nstr(delta, 32),
        'first_margin': iv.nstr(first, 32),
        'second_margin': iv.nstr(second, 32),
        'log_threshold_terms': [iv.nstr(x, 32) for x in terms],
        'threshold_power_of_ten': cap,
        'conclusion': 'At least one cofactor exceeds its listed power of h.',
    }


def main():
    # The AP 2r_3=r_2+r_7 is the seed28-27 application already retained.
    # These exponents demonstrate a joint improvement over the corresponding
    # rectangular limiting alternatives (the 2-cofactor may already be large).
    examples = [
        ('ap_237_middle3', (28,27,1,1,4,3), iv.log(rational('1.4170')),153,
         [(2,2,1,0,'.45'),(7,1,1,0,'.05'),(3,3,2,1,'.01')],
         {'source':'BFT Proposition 5.1'}),
    ]
    gcd = gcd_exponent_lower(3,2,m0=10**8)
    examples.append(
        ('equal_sums_35_211', (45,44,1,1,3,2),rational(gcd['ell_lower']),10**8,
         [(3,2,1,0,'.3453'),(5,1,1,0,'.3931'),
          (2,2,1,1,'.2757'),(11,1,1,1,'0')],
         {'gcd_certificate':gcd}))
    rows=[]
    for name,seed,ell,m0,components,source in examples:
        row=rational_product_bound(seed,ell,m0,121,components,degree=2,shift=13)
        assert row is not None, name
        rows.append({'name':name,**source,**row})
    out=Path(__file__).with_suffix('.json')
    out.write_text(json.dumps({'scope':'Conditional product estimates, not a whole-index proof.',
                               'certificates':rows},indent=2)+'\n')
    print(json.dumps({'output':str(out),'thresholds':{
        r['name']:r['threshold_power_of_ten'] for r in rows}},indent=2))


if __name__ == '__main__':
    main()
