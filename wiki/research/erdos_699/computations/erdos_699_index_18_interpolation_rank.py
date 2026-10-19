#!/usr/bin/env python3
"""Exact surjectivity certificate for the numerical index-18 argument.

The matrix consists of Hasse Taylor coefficients at a fixed triangular
grid.  This checks analytic proof parameters, not binomial rows.  A full
row rank calculation over F_65521 proves surjectivity over Q; the degree
131 generators from the surjective interpolation lemma then have no
common zero with X+Y>17.

Dependencies are pinned in erdos_699_interpolation_requirements.txt.
"""

from __future__ import annotations

import argparse
import json
from math import isqrt
from pathlib import Path

import erdos_699_index_13_interpolation_gcd as interpolation


DEGREE = 130
PRIME = 65521
LINE_EXPONENTS = (37, 34, 32, 29, 26, 23, 19, 15, 10, 4, 0, 0, 0, 0, 0, 0, 0, 0)
ROW_MULTIPLICITIES = (71, 71, 71, 71, 69, 66, 66, 66, 63, 58, 53, 49, 44, 41, 38, 36, 34, 31)
CERTIFICATE = Path(__file__).with_suffix(".json")


def report():
    assert all(PRIME % p for p in range(2, isqrt(PRIME) + 1))
    assert all(a >= b >= 0 for a, b in zip(ROW_MULTIPLICITIES, ROW_MULTIPLICITIES[1:]))
    interpolation.DEGREE = DEGREE
    interpolation.PRIME = PRIME
    interpolation.LINE_EXPONENTS = LINE_EXPONENTS
    interpolation.ROW_MULTIPLICITIES = ROW_MULTIPLICITIES
    basis = interpolation.symmetric_basis()
    jets = interpolation.symmetric_jets()
    matrix = interpolation.jet_matrix(basis, jets)
    rank = matrix.rank()
    assert (len(jets), len(basis), rank) == (4355, 4356, 4355)
    metadata = interpolation.metadata(basis, jets)
    return {
        "scope": "Exact fixed interpolation system; no binomial rows enumerated.",
        "index": 18,
        **metadata,
        "generator_degree_bound": DEGREE + 1,
        "coordinate_factor_degree": 2 * sum(LINE_EXPONENTS),
        "total_polynomial_degree_bound": DEGREE + 1 + 2 * sum(LINE_EXPONENTS),
        "nonvanishing_region": "X+Y>17, after excluding the coordinate lines X=a or Y=a with h_a>0",
        "surjectivity": "The symmetric integer Hasse-jet matrix has full row rank modulo 65521.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--regenerate", action="store_true")
    args = parser.parse_args()
    result = report()
    if args.regenerate:
        CERTIFICATE.write_text(json.dumps(result, indent=2) + "\n")
    else:
        assert json.loads(CERTIFICATE.read_text()) == result
    print(json.dumps({key: result[key] for key in (
        "index", "degree", "symmetric_jet_count", "symmetric_monomial_count",
        "symmetric_rank", "total_polynomial_degree_bound",
    )}, indent=2))


if __name__ == "__main__":
    main()
