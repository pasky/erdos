#!/usr/bin/env python3
"""Numerical sources for the three extra index-fourteen pair alternatives."""
from fractions import Fraction
import json
from pathlib import Path

from erdos_699_off_diagonal_pade import growth_parameters, rational, iv
from erdos_699_off_diagonal_gcd_numeric import gcd_exponent_lower

CONFIGURATIONS = [
    {'edge':(2,7,2747,3213),'seed':(8,7,1,1),'directions':(32,15,32),
     'ell':'1421/100','growth_terms':4000,'analytic_terms':4000,'m0':10**8,'theta_mode':'fixed'},
    {'edge':(5,7,3921,2653),'seed':(25,49,2,1),'directions':(2,1,2),
     'ell':'97/100','growth_terms':4000,'analytic_terms':4000,'m0':10**8,'theta_mode':'fixed'},
    {'edge':(11,13,726,726),'seed':(13,11,1,1),'directions':(147,59,147),
     'ell':'2859/50','growth_terms':4000,'analytic_terms':4000,'m0':10**10,'theta_mode':'fixed'},
]


def main():
    sources=[]
    gcds=[]
    for config in CONFIGURATIONS:
        p,q,ep,eq=config['edge']
        P,Q,a,b=config['seed']
        dirs=config['directions']
        ell=Fraction(config['ell'])
        c0,k0,record=growth_parameters(P,Q,a,b,*dirs,ell,
            terms=config['growth_terms'],sum_scale=10**12)
        primes=[p,q] if P%p==0 else [q,p]
        targets={p:ep,q:eq}
        limits={}
        for prime,base,block in zip(primes,(P,Q),(record['left_block'],record['right_block'])):
            value=base
            while value%prime==0:value//=prime
            assert value==1
            alpha=1-block*iv.log(base)/k0
            assert alpha>rational(Fraction(targets[prime],10000))
            limits[str(prime)]=iv.nstr(alpha,35)
        record.update({'primes':primes,'endpoints_scaled':[targets[x]for x in primes],
                       'edge':list(config['edge']),'limiting_exponents':limits,
                       'strict_endpoint_scope':'Each limiting exponent strictly exceeds its endpoint; no fixed 1/10000 extra margin is asserted.'})
        certificate=gcd_exponent_lower(*dirs,terms=config['analytic_terms'],m0=config['m0'],
                                       theta_mode=config['theta_mode'])
        assert Fraction(certificate['ell_lower'])>ell
        certificate.update({'edge':list(config['edge']),'source_edge':list(config['edge']),
                            'requested_log_rate':str(ell),
                            'strict_rate_margin':str(Fraction(certificate['ell_lower'])-ell)})
        sources.append(record)
        gcds.append(certificate)
    directory=Path(__file__).parent
    source_path=Path(__file__).with_suffix('.json')
    gcd_path=directory/'erdos_699_index_14_additional_gcd.json'
    source_path.write_text(json.dumps({'records':sources},indent=2)+'\n')
    gcd_path.write_text(json.dumps({'source_file':source_path.name,'records':gcds},indent=2)+'\n')
    print(json.dumps({'source_file':str(source_path),'gcd_file':str(gcd_path),
                      'sources':[[s['edge'],s['directions'],s['gcd_log_rate']]for s in sources]},indent=2))


if __name__=='__main__':main()
