#!/usr/bin/env python3
"""Exact polynomial inequalities for Erdős problem 699 at index nine.

The adjacent JSON is a catalogue of integer polynomials specified by their
coordinate-line, row-line, and diagonal factors and residual symmetric jets.
Some records use two coprime kernel polynomials of full degree d; the
resultant bound in those records excludes all their common zeros above
the stated threshold and saves the generator family's extra degree.
The lifting argument is recorded in the research note
../methods/details/coprime_kernels.md.
The default run recomputes every modular rank.  --arithmetic-only checks the
integer metadata without repeating those ranks; it is not a fresh rank proof.

For selected positions r_p and e_p = log_h((n-r_p)/p**v_p(n-r_p)),
each record proves

    sum_{p at singleton positions} m[r_p]*e_p
        <= degree - sum_{t outside {r_p}} m[t] + slack

above its stated algebraic threshold.  This is a necessary condition on a
bad triple, not a claim that these inequalities alone exclude every case.
At a position shared by several primes their product divides n-r_p, so
the whole collision group has capacity one and contributes no e_p term.

The diagonal factor is permitted because the central column is impossible:
if n=2j>=20 were bad, each of n-1,n-3,n-5,n-7 would have all prime factors
in {3,5,7}.  A prime at least 11 in an odd factor forces a central Kummer
carry.  The pairwise differences are 2, 4, or 6, so each of 5 and 7 divides
at most one of the four odd factors.  At least two are powers of 3.
Both exceed 12, whereas distinct powers of 3
above 12 differ by at least 54, contradicting their distance at most 6.

Dependencies: NumPy and python-flint, as pinned in the interpolation
requirements file.  Candidate selection used floating point calculations;
all statements verified here use exact integers and finite-field arithmetic.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import json
from math import comb, isqrt
from pathlib import Path

import erdos_699_index_13_interpolation_gcd as interpolation


INDEX = 9
PRIMES = (2, 3, 5, 7)
DATA = Path(__file__).with_suffix(".json")


def polynomial_degree(record):
    increment = 0 if record.get("nonvanishing_method") == "coprime_kernel" else 1
    return (2 * sum(record["line_exponents"])
            + sum(record["row_factor_exponents"])
            + record["diagonal_power"]
            + max(0, record["interpolation_degree"] + increment))


def basepoint_bound(record):
    """Bound X+Y at common zeros of the two rational lifts.

    An invertible jet minor lifts a modular kernel vector with coordinates
    below 251.  After multiplication by its determinant, the coefficient
    norm is below 10**L, where L=r*(d+6)+20.  Substitute Y=N-X.  A
    Sylvester determinant has at most 2d rows and coefficient norm below
    10**(2d*(L+d+8)).  Cauchy's bound then gives
    n=j+c < 10**(2d*(L+d+8)+2) at any common zero.
    """
    d, r = record["interpolation_degree"], record["symmetric_jet_count"]
    assert 0 < d < 1000 and r < 100000 and record["modular_prime"] == 251
    return 2 * d * (r * (d + 6) + d + 28) + 2


def constant_power(record):
    """A deliberately coarse integer logarithmic coefficient bound.

    A jet entry is bounded by 2*10**d.  For r<100000, adjugates have
    coefficients below 10**(r*(d+6)); the generator conversion costs less
    than 10**10 and kernel-vector lifting costs less than 10**20.
    The other terms bound the explicit polynomial factors,
    (8!)**max(m), and replacement of n by 2h, where h=n-8>=8.
    """
    h = record["line_exponents"]
    m = record["row_multiplicities"]
    q = record["row_factor_exponents"]
    k = record["diagonal_power"]
    r, d = record["symmetric_jet_count"], record["interpolation_degree"]
    assert r < 100000 and -1 <= d < 1000
    assert (1 + (INDEX * INDEX + INDEX + 4) * comb(max(d, 0) + 2, 2)) < 10**10
    return (r * (max(d, 0) + 6) + 2 * sum(h) + sum(q) + k
            + 6 * max(m) + polynomial_degree(record) + sum(m) + 20)


def cut(record, positions, slack=Fraction(1, 10**6)):
    assert len(positions) == len(PRIMES)
    assert all(type(r) is int and 0 <= r < INDEX for r in positions)
    counts = Counter(positions)
    m = record["row_multiplicities"]
    rhs = polynomial_degree(record) - sum(m[t] for t in range(INDEX)
                                          if t not in positions)
    return [m[r] if counts[r] == 1 else 0 for r in positions], Fraction(rhs) + slack


def verify(record, check_rank=True):
    h, m = record["line_exponents"], record["row_multiplicities"]
    q, k = record["row_factor_exponents"], record["diagonal_power"]
    d, prime = record["interpolation_degree"], record["modular_prime"]
    assert len(h) == len(m) == len(q) == INDEX
    assert all(type(v) is int and v >= 0 for v in h + m + q + [k])
    assert any(m)
    assert prime > 2 and all(prime % p for p in range(2, isqrt(prime) + 1))
    residual = lambda x, y: max(0, m[x + y] - h[x] - h[y] - q[x + y]
                                - (k if x == y else 0))
    interpolation.LINE_EXPONENTS = h
    interpolation.ROW_MULTIPLICITIES = m
    interpolation.DEGREE = d
    interpolation.PRIME = prime
    # Build these locally so another certificate using the interpolation
    # module does not inherit this record's additional fixed factors.
    jets = [(x, y, a, order - a) for t in range(INDEX)
            for x in range(t // 2 + 1) for y in [t - x]
            for order in range(residual(x, y)) for a in range(order + 1)
            if x != y or a <= order - a]
    assert len(jets) == record["symmetric_jet_count"]
    expected_residuals = [[x, y, residual(x, y)] for t in range(INDEX)
                          for x in range(t // 2 + 1) for y in [t - x]]
    assert expected_residuals == record["residual_multiplicities"]
    if jets:
        basis = interpolation.symmetric_basis()
        assert len(basis) == record["symmetric_monomial_count"]
        assert len(basis) >= len(jets)
        if check_rank:
            matrix = interpolation.jet_matrix(basis, jets)
            rank = matrix.rank()
            assert rank == len(jets), (record["name"], rank, len(jets))
    else:
        assert d == -1 and record["symmetric_monomial_count"] == 0
    assert record["symmetric_rank"] == len(jets)
    if record.get("nonvanishing_method") == "coprime_kernel":
        assert jets and record["modular_prime"] == 251
        vectors = record["kernel_vectors"]
        assert len(vectors) == 2
        context = interpolation.nmod_mpoly_ctx.get(("X", "Y"), modulus=prime)
        polys = []
        for vector in vectors:
            assert len(vector) == len(basis)
            assert all(type(v) is int and 0 <= v < prime for v in vector)
            if check_rank:
                column = interpolation.nmod_mat(len(basis), 1, vector, prime)
                assert matrix * column == interpolation.nmod_mat(len(jets), 1, prime)
            poly = interpolation.polynomial(context, basis, vector)
            assert poly.total_degree() == d
            polys.append(poly)
        assert polys[0].gcd(polys[1]).is_one()
        assert record["basepoint_threshold_power_of_ten"] == basepoint_bound(record)
        assert record["algebraic_threshold_power_of_ten"] > basepoint_bound(record)
    assert record["certificate_degree"] == polynomial_degree(record)
    assert record["constant_power_of_ten"] == constant_power(record)
    slack = Fraction(record["slack"])
    assert 0 < slack < 1
    assert record["algebraic_threshold_power_of_ten"] * slack > constant_power(record)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--arithmetic-only", action="store_true")
    args = parser.parse_args()
    data = json.loads(DATA.read_text())
    assert data["index"] == INDEX and data["primes"] == list(PRIMES)
    names = set()
    for row in data["certificates"]:
        assert row["name"] not in names
        names.add(row["name"])
        verify(row, check_rank=not args.arithmetic_only)
        print(row["name"], row["symmetric_jet_count"], flush=True)
    print(json.dumps({"certificates": len(names),
                      "ranks_checked": not args.arithmetic_only,
                      "largest_matrix_row_count": max(
                          r["symmetric_jet_count"] for r in data["certificates"])}))


if __name__ == "__main__":
    main()
