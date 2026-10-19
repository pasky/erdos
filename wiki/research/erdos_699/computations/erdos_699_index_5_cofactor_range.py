"""Effective positive-power bounds for both cofactors in a bad quintic row."""
import argparse
from fractions import Fraction
import json
from pathlib import Path

from mpmath import iv

import erdos_699_index_13_interpolation_gcd as jet
from erdos_699_off_diagonal_pade import growth_parameters, rational


def sources():
    records = []
    for direction, ell, targets in [
        ((13, 12, 49), Fraction(3597, 625), (Fraction(1, 100), Fraction(57, 100))),
        ((33, 9, 10), Fraction(43743, 10000), (Fraction(23, 40), Fraction(1, 100))),
    ]:
        A, B, C = direction
        _, k0, record = growth_parameters(9, 8, 1, 1, A, B, C, ell, terms=1000)
        alpha = {2: 1 - (B+C)*iv.log(8)/k0,
                 3: 1 - (A+B)*iv.log(9)/k0}
        for p, target in zip((2, 3), targets):
            assert alpha[p] > rational(target + Fraction(1, 10000))
        record.update({
            "pair": [2, 3],
            "targets": {str(p): str(t) for p, t in zip((2, 3), targets)},
            "limiting_exponents": {str(p): iv.nstr(alpha[p], 35) for p in (2, 3)},
            "strict_margin": "1/10000",
        })
        records.append(record)
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--arithmetic-only", action="store_true")
    args = parser.parse_args()
    records = sources()
    h = [101, 76, 27, 0, 0]
    m = [0, 223, 190, 142, 114]
    D = 164
    jet.LINE_EXPONENTS, jet.ROW_MULTIPLICITIES = h, m
    jet.DEGREE, jet.PRIME = D, 251
    rows, basis = jet.symmetric_jets(), jet.symmetric_basis()
    assert (len(rows), len(basis)) == (6817, 6889)
    total_degree = 2*sum(h) + D + 1
    assert total_degree == 573
    gain = Fraction(57, 100)*m[1] + sum(m[2:]) - total_degree
    assert gain == Fraction(11, 100)
    if not args.arithmetic_only:
        print(f"Checking {len(rows)} x {len(basis)} jet matrix", flush=True)
        assert jet.jet_matrix(basis, rows).rank() == len(rows)
    ramp = {"line_exponents": [3, 2, 1, 0, 0],
            "multiplicities": [6, 5, 4, 3, 2], "degree": 12}
    for r, multiplicity in enumerate(ramp["multiplicities"]):
        assert all(ramp["line_exponents"][x] + ramp["line_exponents"][r-x] >= multiplicity
                   for x in range(r+1))
    ramp_gain = Fraction(57, 100)*6 + 4 + 3 + 2 - 12
    assert ramp_gain == Fraction(21, 50)
    result = {
        "index": 5,
        "scope": "Beyond an effectively computable, unevaluated threshold.",
        "required_position_result": "erdos_699_index_5_maximal_positions.json",
        "sources": records,
        "ramp_certificate": ramp | {"gain": str(ramp_gain)},
        "jet_certificate": {
            "line_exponents": h, "multiplicities": m, "interpolation_degree": D,
            "modular_prime": 251, "matrix_rows": len(rows), "matrix_columns": len(basis),
            "rank": len(rows), "total_degree": total_degree, "gain": str(gain),
        },
        "ranks_checked": not args.arithmetic_only,
        "conclusion": "For h=n-4, every bad quintic triple has h^(1/100)<u,v<h^(57/100).",
    }
    if not args.arithmetic_only:
        Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"conclusion": result["conclusion"], "rank": len(rows),
                      "gain": str(gain), "ranks_checked": not args.arithmetic_only}, indent=2))


if __name__ == "__main__":
    main()
