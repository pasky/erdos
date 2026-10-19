#!/usr/bin/env python3
"""Finite index-seven intervals using pair and three-prime cofactor clauses."""
from bisect import bisect_left
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction
import hashlib
import json
from math import comb, gcd, log
from pathlib import Path
import sys
import erdos_699_window_intervals as base
from erdos_699_effectivity import primes_through
from erdos_699_prime_pair_savings import EXPLICIT_EDGES,SCALE
from erdos_699_weighted_ramps import minimal_vectors
previous,ordinary = base.previous,base.ordinary
prepare_edge,intersects = base.prepare_edge,base.intersects
BFT_THRESHOLD=base.BFT_THRESHOLD


def crosses_row(rows,left,right):
    k=bisect_left(rows,left)
    return k<len(rows) and rows[k]<=right


def extend_triple(vectors,target):
    extended=set()
    for v in vectors:
        if max(v)>=target:
            extended.add(v)
        else:
            for k in range(3):
                w=list(v);w[k]=target;extended.add(tuple(w))
    result=[]
    for v in sorted(extended,key=lambda v:(sum(v),v)):
        if not any(all(a<=b for a,b in zip(u,v)) for u in result):result.append(v)
    return result


def interval_run(index: int, tail_power: int, sources: list[Path], triple_paths: list[Path],
                 max_nodes: int, exact_limit: int) -> dict:
    assert index == 7
    primes = primes_through(index - 1)
    triples = []
    for path in triple_paths:
        record = json.loads(path.read_text())
        assert record['primes'] == primes and record['difference'] == 6
        assert record['position_pattern_count'] == 127
        assert record['cap_power_of_ten'] >= tail_power
        target = Fraction(record['cofactor_exponent'])*SCALE
        assert target.denominator == 1 and SCALE//2 < target < 2*SCALE//3
        rows = record['exceptional_rows']
        assert rows == sorted(set(rows))
        triples.append({'target':int(target),'rows':rows,'minimum_row':record['row_start'],
                        'coarse_minimum_row':max(rows,default=0)+1})
    coarse_triple = min(triples,key=lambda row:row['target'])
    gaps = json.loads(ordinary.GAP_DATA.read_text())["records"]
    lower = min(start for gap, start in gaps if gap > index)
    constants = ordinary.constants(index, lower)
    edges = [prepare_edge(row, index)
             for path in sources for row in json.loads(path.read_text())["records"]
             if all(p < index for p in row["pair"])]
    if not edges:
        raise ValueError("no applicable finite prime-pair certificate")
    coarse_edges = [edge for edge in edges if edge["height_cap_power_of_ten"] >= tail_power]
    coarse_vectors = minimal_vectors(primes, EXPLICIT_EDGES + tuple(
        (*edge["pair"], edge["weight"]) for edge in coarse_edges))
    coarse_vectors = extend_triple(coarse_vectors,coarse_triple['target'])
    saving = min(map(sum, coarse_vectors))
    previous.CAPS[index] = tail_power
    previous.base.PAIR_THRESHOLD = max(
        BFT_THRESHOLD, coarse_triple["coarse_minimum_row"], max((e["coarse_minimum_row"] for e in coarse_edges), default=0))
    # The two historical fixed-cap cases are not targets of this generic tool.
    if index in (22, 25):
        raise ValueError("use the retained fixed-cap certificates for indices 22 and 25")
    cap, cap_power = previous.reduced_cap(index, primes, constants, saving)
    if cap_power > 10_000:
        raise RuntimeError("the analytic cap is still too large for this interval engine")
    for edge in edges:
        edge["maximum_row"] = (None if edge["height_cap_power_of_ten"] >= cap_power
                               else 10 ** edge["height_cap_power_of_ten"])
    basis_cache = {}

    def basis(left, right):
        weights = {(p, q): w for p, q, w in EXPLICIT_EDGES
                   if p < index and q < index and left >= BFT_THRESHOLD}
        for edge in edges:
            if (left >= edge["minimum_row"] and
                    (edge["maximum_row"] is None or right <= edge["maximum_row"]) and
                    not intersects(edge, left, right)):
                pair = edge["pair"]
                weights[pair] = max(weights.get(pair, 0), edge["weight"])
        pair_key = tuple((p, q, w) for (p, q), w in sorted(weights.items()))
        active_triples = tuple(row['target'] for row in triples
                              if left >= row['minimum_row'] and not crosses_row(row['rows'],left,right))
        key = pair_key,active_triples
        if key not in basis_cache:
            vectors = minimal_vectors(primes,pair_key)
            for target in active_triples:
                vectors = extend_triple(vectors,target)
            basis_cache[key] = (vectors, [tuple(v / SCALE for v in vector) for vector in vectors])
        return basis_cache[key]

    data = [(*row, [q for q, _ in row[3]])
            for row in ordinary.prime_power_data(index, cap, primes)]
    lower_logs = [ordinary.log_bounds(p)[0] for p in primes]
    valuations_i = [previous.base.prime_valuation(index, p) for p in primes]
    fat_exponent = constants["fat_exponent_numerator"] / constants["multiplicity"]
    fat_constant = float(constants["fat_constant_lo"])
    orbit_constant = float(constants["orbit_constant_lo"])
    stack = [(lower, cap)]
    visited = leaves = pair_leaves = exact_columns = congruence_leaves = 0
    minimum = Decimal("Infinity")
    partition_hash = hashlib.sha256()
    exact_rows = []

    while stack:
        left, right = stack.pop()
        visited += 1
        if visited > max_nodes:
            raise RuntimeError(f"node budget exhausted at [{left},{right}]; proof incomplete")
        if visited % 100_000 == 0:
            print(f"i={index}: {visited} intervals visited; current lower endpoint {left}", file=sys.stderr, flush=True)
        if not any(right//modulus > (left-1)//modulus for modulus in (8,9,25)):
            leaves += 1
            congruence_leaves += 1
            partition_hash.update(f"{left}:{right}:CRT\n".encode())
            continue
        counts = previous.fast_valuation_upper_counts(left, right, data)
        individual = [count * row[1] for count, row in zip(counts, data)]
        guide_lower = max(fat_exponent * log(left) + fat_constant,
                          index / 4 * log(left) + orbit_constant)
        margin = Decimal(0)
        used_pair = False
        if guide_lower > sum(individual):
            margin = ordinary.certified_margin(index, left, counts, data, constants)
        else:
            vectors, float_vectors = basis(left, right)
            log_right, log_base = log(right), log(left - index + 1)
            guide_upper = max(sum(min(individual[k], log_right - weight * log_base
                                      - valuations_i[k] * data[k][1])
                                  for k, weight in enumerate(vector))
                              for vector in float_vectors)
            if guide_lower > guide_upper:
                right_hi = ordinary.log_bounds(right)[1]
                base_lo = ordinary.log_bounds(left - index + 1)[0]
                left_lo = ordinary.log_bounds(left)[0]
                with localcontext() as context:
                    context.prec = ordinary.PRECISION
                    context.rounding = ROUND_FLOOR
                    deductions = [[Decimal(weight) * base_lo / SCALE + valuations_i[k] * lower_logs[k]
                                   for k, weight in enumerate(vector)] for vector in vectors]
                with localcontext() as context:
                    context.prec = ordinary.PRECISION
                    context.rounding = ROUND_CEILING
                    ordinary_upper = [count * row[2] for count, row in zip(counts, data)]
                    upper = max(sum((min(ordinary_upper[k], right_hi - deduction)
                                     for k, deduction in enumerate(vector)), Decimal(0))
                                for vector in deductions)
                with localcontext() as context:
                    context.prec = ordinary.PRECISION
                    context.rounding = ROUND_FLOOR
                    fat = constants["fat_exponent_numerator"] * left_lo / constants["multiplicity"] + constants["fat_constant_lo"]
                    orbit = index * left_lo / 4 + constants["orbit_constant_lo"]
                    margin = max(fat, orbit) - upper
                used_pair = margin > 0
        if margin > 0:
            leaves += 1
            pair_leaves += used_pair
            minimum = min(minimum, margin)
            partition_hash.update(f"{left}:{right}\n".encode())
            continue
        if left == right:
            if left > exact_limit:
                raise RuntimeError(f"unexcluded singleton n={left}; proof incomplete")
            fixed, current = comb(left, index), 1
            for j in range(1, left // 2 + 1):
                current = current * (left - j + 1) // j
                if j <= index:
                    continue
                common = gcd(fixed, current)
                for p in primes:
                    while common % p == 0:
                        common //= p
                assert common > 1, f"Bad triple found: {(left, index, j)}"
                exact_columns += 1
            exact_rows.append(left)
            partition_hash.update(f"{left}:{right}\n".encode())
            continue
        middle = (left + right) // 2
        stack.extend([(left, middle), (middle + 1, right)])
    return {
        "i": index, "supplied_tail_power_of_ten": tail_power,
        "inclusive_interval_cap_power_of_ten": cap_power,
        "terminal_prime_lower_row": lower, "coarse_cofactor_saving_scaled": saving,
        "visited_intervals": visited, "certified_intervals": leaves,
        "intervals_requiring_prime_pairs": pair_leaves,
        "intervals_excluded_by_row_congruences":congruence_leaves,
        "total_partition_leaves": leaves + len(exact_rows),
        "minimum_certified_log_margin": str(minimum),
        "interval_partition_sha256": partition_hash.hexdigest(),
        "active_cofactor_graphs_used": len(basis_cache),
        "finite_pair_constraints": len(edges),
        "exceptional_row_windows": sum(len(edge["windows"]) for edge in edges),
        "exact_singleton_rows": exact_rows, "exact_columns_checked": exact_columns,
        "source_certificates": [{"file": path.name} for path in sources],
        "gap_data_file": ordinary.GAP_DATA.name,
        "triple_sources": [{"file": path.name} for path in triple_paths],
        "coarse_triple_exponent_scaled":coarse_triple['target'],
        "conclusion": "No bad index-seven rows remain through the supplied finite cap.",
    }


def main():
    from erdos_699_low_crt_row_zero import verify_index
    assert verify_index(7)['surviving_candidates'] == []
    here=Path(__file__).resolve().parent
    pair_sources=[here/'erdos_699_prime_pair_strips_7_middle.json',
                  here/'erdos_699_prime_pair_strips_20.json']
    triple_sources=[here/'erdos_699_triple_prime_power_strips_7_061.json',
                    here/'erdos_699_triple_prime_power_strips_066_3000.json']
    result=interval_run(7,2057,pair_sources,triple_sources,20_000_000,30000)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in
        ['i','inclusive_interval_cap_power_of_ten','certified_intervals','minimum_certified_log_margin',
         'exact_singleton_rows','exact_columns_checked','conclusion']},indent=2))


if __name__=='__main__':main()
