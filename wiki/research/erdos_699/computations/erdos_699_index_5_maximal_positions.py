"""Effective confinement of the small-prime maxima for Erdős 699, index five.

The finite cases are cofactor witnesses and positions, never binomial rows.
Two small modular jet matrices and four polynomial products are sufficient.
"""
import argparse
from fractions import Fraction
import json
from pathlib import Path

import sympy as sp

import erdos_699_index_13_interpolation_gcd as jet
from erdos_699_two_three_off_diagonal import certify


X, Y = sp.symbols("X Y")
S, T = X + Y, X * Y
FACTORS = {
    "xy": T,
    "shift1": (X - 1) * (Y - 1),
    "diagonal": (X - Y) ** 2,
    "q1": S**2 - 3*T - S,
    "q2": 2*S**2 - 3*T - 6*S + 4,
    "q3": S**2 - T - 3*S + 2,
}
PRODUCTS = {
    "A": {"factors": {"xy": 1, "shift1": 1, "q2": 1},
          "multiplicities": [0, 3, 2, 1, 1], "degree": 6},
    "B": {"factors": {"xy": 2, "shift1": 1, "q1": 1},
          "multiplicities": [5, 4, 2, 2, 1], "degree": 8},
    "C": {"factors": {"xy": 6, "shift1": 2, "diagonal": 1},
          "multiplicities": [14, 8, 6, 0, 2], "degree": 18},
    "D": {"factors": {"xy": 3, "shift1": 2, "q3": 1},
          "multiplicities": [0, 6, 4, 3, 0], "degree": 12},
}
JETS = [
    {"name": "J1", "cofactors_at_0_2": ["1/20", "291/1000"],
     "line_exponents": [17, 12, 0, 0, 0],
     "multiplicities": [37, 58, 25, 29, 23],
     "interpolation_degree": 60, "rank": 938, "basis_count": 961,
     "degree": 119, "gain": "1/8"},
    {"name": "J2", "cofactors_at_0_2": ["1/40", "329/1000"],
     "line_exponents": [21, 15, 0, 0, 0],
     "multiplicities": [46, 76, 34, 38, 31],
     "interpolation_degree": 84, "rank": 1799, "basis_count": 1849,
     "degree": 157, "gain": "42/125"},
]


def order_at(polynomial, x, y):
    shifted = sp.Poly(sp.expand(polynomial.subs({X: X+x, Y: Y+y}, simultaneous=True)), X, Y)
    return min(sum(monomial) for monomial, coefficient in shifted.terms() if coefficient)


def gain(record, r, e0, er):
    alpha = [Fraction(1)] * 5
    alpha[0], alpha[r] = e0, er
    return sum(a*m for a, m in zip(alpha, record["multiplicities"])) - record["degree"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--arithmetic-only", action="store_true")
    args = parser.parse_args()
    sources = certify()
    vectors = [tuple(map(Fraction, v)) for v in sources["minimal_vectors"]]
    orders = {name: {(x, r-x): order_at(f, x, r-x)
                     for r in range(5) for x in range(r+1)}
              for name, f in FACTORS.items()}
    for record in PRODUCTS.values():
        assert record["degree"] == sum(sp.total_degree(FACTORS[k])*v
                                       for k, v in record["factors"].items())
        for r, multiplicity in enumerate(record["multiplicities"]):
            for x in range(r+1):
                assert sum(v*orders[k][x, r-x] for k, v in record["factors"].items()) >= multiplicity
    for record in JETS:
        jet.LINE_EXPONENTS = record["line_exponents"]
        jet.ROW_MULTIPLICITIES = record["multiplicities"]
        jet.DEGREE = record["interpolation_degree"]
        jet.PRIME = 251
        rows, basis = jet.symmetric_jets(), jet.symmetric_basis()
        assert (len(rows), len(basis)) == (record["rank"], record["basis_count"])
        assert record["degree"] == 2*sum(jet.LINE_EXPONENTS) + jet.DEGREE + 1
        assert gain(record, 2, *map(Fraction, record["cofactors_at_0_2"])) == Fraction(record["gain"])
        if not args.arithmetic_only:
            print(f"Checking {record['name']}: {len(rows)} x {len(basis)}", flush=True)
            assert jet.jet_matrix(basis, rows).rank() == len(rows)
    coverage = []
    for r in (2, 3, 4):
        for vector in vectors:
            for reverse in (False, True):
                e0, er = vector[::-1] if reverse else vector
                if r == 4:
                    name, record = "D", PRODUCTS["D"]
                elif r == 3:
                    name = "C" if e0 >= Fraction(291, 1000) else "A"
                    record = PRODUCTS[name]
                else:
                    choices = [(name, record) for name, record in PRODUCTS.items()
                               if name in ("A", "B") and gain(record, r, e0, er) > 0]
                    choices += [(record["name"], record) for record in JETS
                                if all(a <= b for a, b in zip(map(Fraction, record["cofactors_at_0_2"]), (e0, er)))]
                    assert choices, (r, e0, er)
                    name, record = choices[0]
                margin = gain(record, r, e0, er)
                assert margin > 0
                coverage.append({"positions": [0, r], "cofactors": [str(e0), str(er)],
                                 "certificate": name, "gain": str(margin)})
    assert len(coverage) == 30
    result = {
        "index": 5,
        "scope": "Above an effectively computable, unevaluated row threshold.",
        "conclusion": "The distinct maximal positions for 2 and 3 must be 0 and 1.",
        "products": PRODUCTS, "jet_certificates": JETS,
        "modular_prime": 251, "ranks_checked": not args.arithmetic_only,
        "cofactor_witness_vectors_in_prime_order_2_3": sources["minimal_vectors"],
        "position_vector_cases": len(coverage), "coverage": coverage,
    }
    if not args.arithmetic_only:
        Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"position_vector_cases": len(coverage), "products": len(PRODUCTS),
                      "jet_certificates": len(JETS), "ranks_checked": not args.arithmetic_only,
                      "conclusion": result["conclusion"]}, indent=2))


if __name__ == "__main__":
    main()
