"""Two numerical asymmetric prime-pair estimates for the remaining indices."""

import json
from pathlib import Path

from mpmath import iv

from erdos_699_bft_pair_extension import rational
from erdos_699_rational_product_bounds import rational_product_bound


def main():
    choices = [
        ('pair_2_7', (49,16,1,3,7,4), '1.6219', 60,
         [(7,2,1,0,'.085'),(2,4,1,1,'.348')]),
        ('pair_2_11', (512,1331,13,5,9,4), '1.7666', 87,
         [(2,9,1,0,'.193'),(11,3,1,1,'.069')]),
    ]
    rows=[]
    for name,seed,L1,m0,components in choices:
        certificate=rational_product_bound(
            seed,iv.log(rational(L1)),m0,196,components,
            degree=1,shift=13)
        assert certificate is not None
        rows.append({'name':name,'L1':L1,
                     'gcd_source':'BFT Proposition 5.1',**certificate})
    out=Path(__file__).with_suffix('.json')
    out.write_text(json.dumps({
        'scope':'Pair estimates for a nonzero gap at most196; no whole-index claim.',
        'certificates':rows,
        'common_row_threshold_power_of_ten':
            1+max(r['threshold_power_of_ten'] for r in rows),
    },indent=2)+'\n')
    print(json.dumps({'output':str(out),'thresholds':{
        r['name']:r['threshold_power_of_ten'] for r in rows}},indent=2))


if __name__=='__main__':
    main()
