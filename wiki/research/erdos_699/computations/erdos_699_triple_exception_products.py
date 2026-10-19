"""Check the full cofactor product at large three-prime CRT exception rows.

Only valuations at 2,3,5 are computed. No binomial columns or large-prime
factorizations are enumerated.
"""
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
SOURCE=HERE/'erdos_699_triple_prime_power_strips_066_3000.json'
OUTPUT=Path(__file__).with_suffix('.json')
PRIMES=(2,3,5)


def worst_cofactor(n,p):
    best=None
    for offset in range(7):
        value=n-offset;exponent=0
        while value%p==0:
            value//=p;exponent+=1
        candidate=(exponent,-value,offset)
        if best is None or candidate>best:best=candidate
    exponent,negative,offset=best
    return {'prime':p,'exponent':exponent,'position':offset,'cofactor':-negative}


def main():
    source=json.loads(SOURCE.read_text())
    assert source['primes']==list(PRIMES) and source['difference']==6
    assert source['cofactor_exponent']=='33/50' and source['cap_power_of_ten']==3000
    threshold=10**53
    rows=[]
    for n in source['exceptional_rows']:
        if n<=threshold:continue
        factors=[worst_cofactor(n,p)for p in PRIMES]
        U=1
        for factor in factors:
            U*=factor['cofactor']
            assert factor['prime']**factor['exponent']*factor['cofactor']==n-factor['position']
        assert U**50>=(n-6)**53
        rows.append({'row':n,'selected_factors':factors,'cofactor_product':U})
    result={'source':SOURCE.name,
            'row_threshold_power_of_ten':53,'height_variable':'h=n-6',
            'cofactor_product_exponent':'53/50','checked_row_count':len(rows),
            'scope':'Every three-prime exception row above 10^53 in the source certificate passes the product bound for every maximal-valuation selection.',
            'records':rows}
    OUTPUT.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()if k!='records'},indent=2))


if __name__=='__main__':main()
