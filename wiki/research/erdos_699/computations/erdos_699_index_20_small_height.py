#!/usr/bin/env python3
"""Verify a small-height basis for the complete index-20 interpolation kernel.

The earlier modular certificate proves surjectivity through degree 96.
Here 51 integer sections through degree 97 are checked directly, without
repeating that rank calculation. Their independence, exact vanishing, and
coefficient norms give the improved algebraic tail.

--regenerate optionally repeats Dixon solving, integer-lattice saturation,
and LLL reduction. Ordinary verification uses the retained compressed JSON.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import json
from math import comb, gcd
from pathlib import Path

import numpy as np
from flint import fmpq_mat, fmpz, fmpz_mat, nmod_mat

import erdos_699_index_13_interpolation_gcd as interpolation
from erdos_699_interpolation_extensions import DATA
from erdos_699_weighted_ramps import PRIMES, off_maximum_constant


DIRECTORY = Path(__file__).parent
BASIS_FILE = DIRECTORY / "erdos_699_index_20_small_height_basis.json.gz"
REPORT_FILE = Path(__file__).with_suffix(".json")


def system():
    data = DATA[20]
    interpolation.DEGREE = data["degree"] + 1
    interpolation.LINE_EXPONENTS = data["h"]
    interpolation.ROW_MULTIPLICITIES = data["m"]
    basis = interpolation.symmetric_basis()
    jets = interpolation.symmetric_jets()
    assert (len(jets), len(basis)) == (2399, 2450)
    left = np.array([a for a, _ in basis])
    right = np.array([b for _, b in basis])
    unequal = left != right
    max_order = max(a + b for _, _, a, b in jets)
    powers = [np.array([
        [comb(exponent, order) * x ** (exponent - order)
         if exponent >= order else 0 for exponent in range(98)]
        for order in range(max_order + 1)
    ], dtype=object) for x in range(20)]
    entries = np.empty((len(jets), len(basis)), dtype=object)
    for row, (x, y, a, b) in enumerate(jets):
        entries[row] = (powers[x][a, left] * powers[y][b, right]
                        + unequal * powers[x][a, right] * powers[y][b, left])
    matrix = fmpz_mat(len(jets), len(basis), entries.ravel().tolist())
    return data, basis, matrix


def regenerate(basis, matrix):
    rank, columns = matrix.nrows(), matrix.ncols()
    dimension = columns - rank
    pivot = fmpz_mat(rank, rank, [matrix[i, j]
                                for i in range(rank) for j in range(rank)])
    free = fmpz_mat(rank, dimension, [matrix[i, j]
                                    for i in range(rank) for j in range(rank, columns)])
    solution = fmpq_mat(pivot).solve(-fmpq_mat(free), algorithm="dixon")
    vectors = []
    for column in range(dimension):
        denominator = fmpz(1)
        for row in range(rank):
            denominator = denominator.lcm(solution[row, column].q)
        vector = [0] * columns
        vector[rank + column] = int(denominator)
        for row in range(rank):
            entry = solution[row, column]
            vector[row] = int(entry.p * (denominator // entry.q))
        content = gcd(*vector)
        vectors.append([entry // content for entry in vector])

    # If H is a row basis of the coordinate lattice of B^T, then
    # B^T H^-1 is integral and is a basis of the saturated column lattice.
    old = fmpz_mat(vectors)
    hermite = old.transpose().hnf()
    h = fmpz_mat(dimension, dimension,
                 [hermite[i, j] for i in range(dimension) for j in range(dimension)])
    saturated = fmpq_mat(h.transpose()).solve(fmpq_mat(old), algorithm="dixon")
    assert all(saturated[i, j].q == 1
               for i in range(dimension) for j in range(columns))
    integral = fmpz_mat(dimension, columns,
                       [saturated[i, j].p for i in range(dimension)
                        for j in range(columns)])
    assert h.transpose() * integral == old
    reduced, transform = integral.lll(transform=True)
    assert transform * integral == reduced and abs(transform.det()) == 1
    vectors = [[int(reduced[i, j]) for j in range(columns)]
               for i in range(dimension)]
    record = {
        "index": 20,
        "degree": 97,
        "symmetric_basis_order": "increasing a+b, then increasing a, a<=b",
        "coefficient_vectors": vectors,
    }
    raw = json.dumps(record, separators=(",", ":")).encode()
    BASIS_FILE.write_bytes(gzip.compress(raw, compresslevel=9, mtime=0))


def tail_bound(height, h, m, gain):
    primes = tuple(prime for prime in PRIMES if prime < 20)
    off_maximum, factors = off_maximum_constant(20, m, primes)
    numerator = 1000 * off_maximum * height
    denominator = 999 * 2 ** (2 * sum(h))
    exponent = max(0, len(str(numerator)) - len(str(denominator)))
    while 10**exponent * denominator <= numerator:
        exponent += 1
    while exponent and 10**(exponent - 1) * denominator > numerator:
        exponent -= 1
    cap = exponent * gain.denominator // gain.numerator + 1
    assert cap * gain.numerator > exponent * gain.denominator
    elementary_threshold = 1000 * (
        sum(t * weight for t, weight in enumerate(m)) + len(primes) * m[0] * 19)
    assert elementary_threshold < 10**10 and cap >= 10
    return {
        "off_maximum_factors": factors,
        "constant_log10_upper": exponent,
        "exponent_gain": str(gain),
        "algebraic_tail_power_of_ten": cap,
        "elementary_threshold": elementary_threshold,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--regenerate", action="store_true")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    data, basis, matrix = system()
    if args.regenerate:
        regenerate(basis, matrix)
    blob = BASIS_FILE.read_bytes()
    record = json.loads(gzip.decompress(blob))
    assert record["index"] == 20 and record["degree"] == 97
    assert record["symmetric_basis_order"] == "increasing a+b, then increasing a, a<=b"
    vectors = record["coefficient_vectors"]
    assert len(vectors) == 51 and all(len(vector) == 2450 for vector in vectors)
    assert all(type(value) is int for vector in vectors for value in vector)
    kernel = fmpz_mat(vectors).transpose()
    assert matrix * kernel == fmpz_mat(2399, 51)

    minor = nmod_mat(51, 51, [vector[column] % 65521
                             for vector in vectors for column in range(2399, 2450)],
                     65521)
    determinant = int(minor.det())
    assert determinant != 0
    height = max(sum(abs(value) * (1 if a == b else 2)
                     for (a, b), value in zip(basis, vector)) for vector in vectors)
    coefficient_height = max(abs(value) for vector in vectors for value in vector)
    leading_bound = max(Fraction(abs(value), comb(97, a))
                        for vector in vectors for (a, b), value in zip(basis, vector)
                        if a + b == 97)
    # On X,Y >= 0 with X+Y=n, the degree-97 Bernstein basis is positive
    # and sums to n^97. Lower-degree terms contribute < n^97 once n>=10^H.
    evaluation_constant = -(-leading_bound.numerator // leading_bound.denominator) + 1
    evaluation_threshold = len(str(height))
    report = {
        "index": 20,
        "degree": 97,
        "jet_equations": 2399,
        "symmetric_monomials": 2450,
        "generator_count": 51,
        "independence_minor_modulus": 65521,
        "independence_minor_determinant": determinant,
        "maximum_coefficient_digits": len(str(coefficient_height)),
        "maximum_L1_norm": str(height),
        "maximum_L1_digits": len(str(height)),
        "leading_Bernstein_bound": str(leading_bound),
        "evaluation_constant": str(evaluation_constant),
        "evaluation_threshold_power_of_ten": evaluation_threshold,
        "basis_gzip_file": BASIS_FILE.name,
        **tail_bound(evaluation_constant, data["h"], data["m"], Fraction(713, 5000)),
        "scope": "Algebraic tail after the specified cofactor source thresholds hold",
    }
    assert report["algebraic_tail_power_of_ten"] > evaluation_threshold
    if args.write:
        REPORT_FILE.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: report[key] for key in
                      ("index", "generator_count", "maximum_L1_digits",
                       "independence_minor_determinant", "constant_log10_upper",
                       "algebraic_tail_power_of_ten", "scope")}, indent=2))


if __name__ == "__main__":
    main()
