#!/usr/bin/env python3
"""Check the fixed fat-point interpolation certificate for Erdos 699, i=13.

This enumerates monomials and prescribed Taylor coefficients, not binomial
rows or columns.  All field calculations are exact.  Dependencies: numpy
and python-flint, neither declared by the repository; run from the
repository root as

  uv run --no-sync --with numpy --with python-flint python wiki/research/erdos_699/computations/erdos_699_index_13_interpolation_gcd.py

The adjacent JSON stores two modular sections.  Use --regenerate to replace
them with two coprime sections obtained from FLINT's nullspace calculation.
"""

from __future__ import annotations

import argparse
import json
from math import comb, isqrt
from pathlib import Path

import numpy as np
from flint import nmod_mat, nmod_mpoly_ctx


DEGREE = 106
PRIME = 65521
LINE_EXPONENTS = (57, 54, 45, 39, 32, 24, 13, 3, 0, 0, 0, 0, 0)
ROW_MULTIPLICITIES = (114, 111, 111, 103, 99, 99, 89, 78, 70, 63, 57, 51, 46)
CERTIFICATE = Path(__file__).with_suffix(".json")


def residual(x: int, y: int) -> int:
    return max(0, ROW_MULTIPLICITIES[x + y] - LINE_EXPONENTS[x] - LINE_EXPONENTS[y])


def symmetric_basis() -> list[tuple[int, int]]:
    """X^a Y^b + X^b Y^a for a<b; X^a Y^a for a=b."""
    return [(a, degree - a) for degree in range(DEGREE + 1)
            for a in range(degree // 2 + 1)]


def symmetric_jets() -> list[tuple[int, int, int, int]]:
    """Representatives (x,y,a,b) of the required Hasse Taylor coefficients."""
    rows = []
    for total in range(len(ROW_MULTIPLICITIES)):
        for x in range(total // 2 + 1):
            y = total - x
            for order in range(residual(x, y)):
                for a in range(order + 1):
                    b = order - a
                    if x != y or a <= b:
                        rows.append((x, y, a, b))
    return rows


def jet_matrix(basis, rows):
    """Reduce the integer jet matrix modulo PRIME, without numerical arithmetic."""
    left = np.array([a for a, _ in basis], dtype=np.int64)
    right = np.array([b for _, b in basis], dtype=np.int64)
    unequal = left != right
    max_order = max(a + b for _, _, a, b in rows)
    powers = []
    for x in range(len(ROW_MULTIPLICITIES)):
        powers.append(np.array([
            [(comb(exponent, order) * pow(x, exponent - order, PRIME)) % PRIME
             if exponent >= order else 0
             for exponent in range(DEGREE + 1)]
            for order in range(max_order + 1)
        ], dtype=np.int64))

    storage = np.uint16 if PRIME < 65536 else np.int64
    values = np.empty((len(rows), len(basis)), dtype=storage)
    for index, (x, y, a, b) in enumerate(rows):
        coefficients = powers[x][a, left] * powers[y][b, right]
        coefficients += unequal * (powers[x][a, right] * powers[y][b, left])
        # Each summand is below PRIME^2, so signed int64 cannot overflow.
        values[index] = coefficients % PRIME
    return nmod_mat(len(rows), len(basis), values.ravel().tolist(), PRIME)


def polynomial(context, basis, coefficients):
    terms = {}
    for (a, b), coefficient in zip(basis, coefficients, strict=True):
        if coefficient:
            terms[a, b] = coefficient
            if a != b:
                terms[b, a] = coefficient
    return context.from_dict(terms)


def metadata(basis, rows):
    index = len(ROW_MULTIPLICITIES)
    multiplicities = [residual(x, y) for x in range(index) for y in range(index - x)]
    return {
        "degree": DEGREE,
        "prime": PRIME,
        "line_exponents": list(LINE_EXPONENTS),
        "row_multiplicities": list(ROW_MULTIPLICITIES),
        "residual_sum": sum(multiplicities),
        "residual_square_sum": sum(value * value for value in multiplicities),
        "full_jet_count": sum(comb(value + 1, 2) for value in multiplicities),
        "symmetric_jet_count": len(rows),
        "symmetric_monomial_count": len(basis),
        "symmetric_rank": len(rows),
        "symmetric_nullity": len(basis) - len(rows),
        "basis_order": "increasing a+b, then increasing a, with a<=b",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--regenerate", action="store_true")
    args = parser.parse_args()
    assert PRIME > 1 and all(PRIME % p for p in range(2, isqrt(PRIME) + 1))

    basis = symmetric_basis()
    rows = symmetric_jets()
    expected = metadata(basis, rows)
    assert (len(rows), len(basis)) == (2911, 2916)
    assert (expected["residual_sum"], expected["residual_square_sum"],
            expected["full_jet_count"]) == (844, 10738, 5791)
    matrix = jet_matrix(basis, rows)
    context = nmod_mpoly_ctx.get(("X", "Y"), modulus=PRIME)

    if args.regenerate:
        kernel, nullity = matrix.nullspace()
        assert len(basis) - nullity == len(rows)
        sections = []
        common = None
        for column in range(nullity):
            coefficients = [int(kernel[row, column]) for row in range(len(basis))]
            section = polynomial(context, basis, coefficients)
            common = section if common is None else common.gcd(section)
            sections.append(coefficients)
            if common.is_one():
                break
        assert common.is_one(), "The modular sections have a nonconstant common factor"
        certificate = expected | {"sections": sections}
        CERTIFICATE.write_text(json.dumps(certificate, indent=2) + "\n")
    else:
        certificate = json.loads(CERTIFICATE.read_text())
        assert {key: certificate[key] for key in expected} == expected
        assert matrix.rank() == len(rows), "The modular jet matrix is not full row rank"

    sections = certificate["sections"]
    assert len(sections) >= 2
    assert all(len(section) == len(basis) for section in sections)
    assert all(type(value) is int and 0 <= value < PRIME
               for section in sections for value in section)
    section_matrix = nmod_mat(len(basis), len(sections),
                             [section[row] for row in range(len(basis))
                              for section in sections], PRIME)
    assert matrix * section_matrix == nmod_mat(len(rows), len(sections), PRIME)
    common = None
    degrees = []
    for coefficients in sections:
        section = polynomial(context, basis, coefficients)
        assert not section.is_zero()
        degrees.append(int(section.total_degree()))
        common = section if common is None else common.gcd(section)
    assert common.is_one()  # Full bivariate gcd, including coefficient content.
    print(json.dumps({
        "prime": PRIME,
        "matrix_shape": [len(rows), len(basis)],
        "rank": len(rows),
        "nullity": len(basis) - len(rows),
        "section_degrees": degrees,
        "modular_gcd": "1",
    }, indent=2))


if __name__ == "__main__":
    main()
