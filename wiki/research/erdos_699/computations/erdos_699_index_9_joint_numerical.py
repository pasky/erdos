"""Numerical heights for every joint Pade clause used in the index-nine proof.

This evaluates source constants, not modular ranks or binomial rows.
The sign branches remain unchanged. Threshold weakenings are supplied by
the separately retained exact Farkas-margin certificate.
"""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import argparse
import gzip
import json

from erdos_699_off_diagonal_explicit_clauses import joint_clause_threshold
from erdos_699_off_diagonal_gcd_sharp import gcd_exponent_lower

ROOT = Path(__file__).parent
SOURCE = ROOT/'erdos_699_nine_cofactor_clauses.json.gz'
PROOF = ROOT/'erdos_699_index_9_effective.json.gz'
WEAKENING = ROOT/'erdos_699_nine_source_weakening.json'
OUTPUT = Path(__file__).with_suffix('.json.gz')
TERMS = 10000


def read_compressed(path):
    with gzip.open(path, 'rt') as handle:
        return json.load(handle)


def build():
    sources, proof = read_compressed(SOURCE), read_compressed(PROOF)
    weakening_data = json.loads(WEAKENING.read_text())
    weakenings = weakening_data['per_source_half_budget']
    assert sources['index'] == proof['index'] == 9
    used = {node['source'] for root in proof['roots'] for node in root['tree']
            if 'source' in node}
    rows = [row for row in sources['records'] if row['id'] in used]
    assert len(rows) == proof['directed_rational_source_count'] == 790
    gcd_records, gcd_index, gcd_cache, records = [], {}, {}, []
    for row in rows:
        certificate = row['certificate']
        source = certificate['source']
        weakening = Fraction(weakenings[row['id']])
        assert Fraction(weakening_data['modified_thresholds'][row['id']]) == (
            Fraction(certificate['positive_part_threshold'])-weakening)
        requested = Fraction(source['gcd_log_rate'])
        tau = Fraction(certificate['block_parameter'])
        target = max(requested/2, requested-weakening/(2*tau))
        directions = tuple(source['directions'])
        for exponent in (5,6,7,8,9,10,11,12,13,14,16,18,20,24,30,40,60,80,120):
            key = (directions, 10**exponent)
            if key not in gcd_cache:
                try:
                    gcd_cache[key] = gcd_exponent_lower(
                        *directions, terms=TERMS, m0=key[1])
                except AssertionError:
                    # Small trial m0 can precede the exact floor-stability
                    # bound or give a nonpositive prime-interval estimate.
                    gcd_cache[key] = None
            gcd = gcd_cache[key]
            if gcd is not None and Fraction(gcd['ell_lower']) > target:
                break
        else:
            raise AssertionError(('No numerical gcd bound', row['id']))
        if key not in gcd_index:
            gcd_index[key] = len(gcd_records)
            gcd_records.append(gcd)
        index = gcd_index[key]
        gcd = gcd_records[index]
        kind = row['hypothesis']['kind']
        assert kind in ('pair','ap','four')
        assert certificate['product_degree'] == (1 if kind=='pair' else 2)
        # For pair sources the gap is at most8. Equal-sum degree-two
        # products differ by a difference of products of positions0..8,
        # bounded by64. This bound includes actual difference zero.
        numeric = joint_clause_threshold(
            certificate, gcd['m0'], gap=8 if kind=='pair' else 64,
            maximum_shift=8, gcd_log_rate=gcd['ell_lower'],
            threshold_weakening=weakening)
        numeric.update({'source_id':row['id'], 'hypothesis':row['hypothesis'],
                        'gcd_certificate_index':index})
        records.append(numeric)
        if len(records)%100==0:
            print(json.dumps({'joint_sources':len(records),
                              'unique_gcd_sources':len(gcd_records),
                              'current_maximum_K':max(r['threshold_power_of_ten'] for r in records)}), flush=True)
    maximum = max(row['threshold_power_of_ten'] for row in records)
    return {
        'index':9, 'height_variable':'h=n-8',
        'scope':'Numerical thresholds for the790 rational clauses with independently certified Farkas-margin weakenings; initial pairs and ordinary products are separate inputs.',
        'source_file':SOURCE.name,
        'proof_file':PROOF.name,
        'weakening_file':WEAKENING.name,
        'polynomial_height_threshold_power_of_ten':weakening_data['polynomial_height_threshold_power_of_ten'],
        'source_count':len(records), 'source_kinds':dict(Counter(r['hypothesis']['kind'] for r in records)),
        'gcd_certificate_count':len(gcd_records), 'gcd_certificates':gcd_records,
        'records':records, 'maximum_joint_threshold_power_of_ten':maximum,
        'maximizing_sources':[r['source_id'] for r in records if r['threshold_power_of_ten']==maximum],
        'conclusion':'All790 specified weakened joint clauses hold for every h at least10 raised to the displayed maximum exponent.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = build()
    if args.write:
        payload = (json.dumps(result,sort_keys=True,separators=(',',':'))+'\n').encode()
        OUTPUT.write_bytes(gzip.compress(payload,mtime=0))
    else:
        assert result == read_compressed(OUTPUT)
    print(json.dumps({key:result[key] for key in (
        'index','source_count','gcd_certificate_count',
        'maximum_joint_threshold_power_of_ten','maximizing_sources')}, indent=2))


if __name__=='__main__':
    main()
