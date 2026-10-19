"""Certify finite prime-pair inequalities by covering exponent quadrants.

One modular inverse certifies two entire strips of larger exponents. Their
complement is another quadrant, usually with geometrically larger starting
exponents. Exact boundary checks handle anchors where neither strip applies.
GMP is optional, but recommended for caps with millions of decimal digits.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations
import hashlib
import json
from math import isqrt, log, log2
from pathlib import Path
import time


def certify(p: int, q: int, cap: int, difference: int, backend: str,
            max_boundary_pairs: int, exponent: Fraction = Fraction(1, 3)) -> dict:
    numerator, denominator = exponent.numerator, exponent.denominator
    assert 0 < 2 * numerator <= denominator
    complement = denominator - numerator
    if backend == "gmpy2":
        import gmpy2
        Integer = gmpy2.mpz
        inverse = gmpy2.invert
        integer_root = lambda value, degree: gmpy2.iroot(value, degree)[0]
    else:
        Integer = int
        inverse = lambda x, modulus: pow(x, -1, modulus)
        def integer_root(value, degree):
            if degree == 1:
                return value
            if degree == 2:
                return isqrt(value)
            root = 1 << ((value.bit_length() + degree - 1) // degree)
            while True:
                following = ((degree - 1) * root + value // root ** (degree - 1)) // degree
                if following >= root:
                    while (root + 1) ** degree <= value:
                        root += 1
                    while root ** degree > value:
                        root -= 1
                    return root
                root = following
    bound = Integer(10) ** cap

    def last_exponent(prime):
        exponent = max(0, int(cap * log(10) / log(prime)))
        power = Integer(prime) ** exponent
        while power > bound:
            exponent -= 1
            power //= prime
        while power * prime <= bound:
            exponent += 1
            power *= prime
        return exponent

    a_limit, b_limit = last_exponent(p), last_exponent(q)
    a, P = 1, Integer(p)
    while P <= difference:
        a += 1
        P *= p
    b, Q = 1, Integer(q)
    while Q <= difference:
        b += 1
        Q *= q
    initial_exponents = [a, b]
    exceptions = []
    anchors = []
    boundary_pairs = 0
    boundary_hash = hashlib.sha256()

    def coefficients(A, B):
        residue = Integer(0)
        inv = inverse(A, B)
        for d in range(1, difference + 1):
            residue += inv
            if residue >= B:
                residue -= B
            other = (A * residue - d) // B
            assert 0 < residue < B and 0 < other < A
            yield d, residue, other
            yield -d, B - residue, A - other

    def check_boundary(aa, bb, A, B):
        nonlocal boundary_pairs
        boundary_pairs += 1
        if boundary_pairs > max_boundary_pairs:
            raise RuntimeError("boundary-pair budget exhausted; proof incomplete")
        boundary_hash.update(f"{aa}:{bb}\n".encode())
        for d, u, v in coefficients(A, B):
            if u ** complement >= A ** numerator or v ** complement >= B ** numerator:
                continue
            x, y = A * u, B * v
            if max(x, y) > bound:
                continue
            if max(u, v) ** denominator < min(x, y) ** numerator:
                exceptions.append({
                    "p_exponent": aa, "q_exponent": bb,
                    "signed_difference": d,
                    "p_cofactor": int(u), "q_cofactor": int(v),
                    "smaller_height": int(min(x, y)),
                    "larger_height": int(max(x, y)),
                })

    def safe_steps(minimum, power, prime):
        ratio = minimum ** complement // power ** numerator
        if ratio < 1:
            return -1
        # Floating point proposes a step count. Both inequalities defining
        # the final integer logarithm are then checked with exact arithmetic.
        steps = max(0, int(ratio.bit_length() / (denominator * log2(prime))))
        base = prime ** denominator
        test = Integer(base) ** steps
        while test > ratio:
            steps -= 1
            test //= base
        while test * base <= ratio:
            steps += 1
            test *= base
        assert test <= ratio < test * base
        return steps

    while a <= a_limit and b <= b_limit:
        min_u, min_v = Q, P
        for _, u, v in coefficients(P, Q):
            min_u = min(min_u, u)
            min_v = min(min_v, v)
        a_steps = safe_steps(min_u, P, p)
        b_steps = safe_steps(min_v, Q, q)
        record = {
            "p_exponent": a, "q_exponent": b,
            "p_power_bits": P.bit_length(), "q_power_bits": Q.bit_length(),
            "minimum_u_bits": min_u.bit_length(), "minimum_v_bits": min_v.bit_length(),
        }
        if a_steps < 0 and b_steps < 0:
            # Remove the two boundary lines exactly. Outside the stated
            # limits, (max(P,Q)-D)^(s-r)<min(P,Q)^s fails, where r/s is
            # the target exponent, so no exception can occur.
            vertical_limit = min(bound, integer_root(P ** denominator, complement) + difference)
            bb, B = b, Q
            before = boundary_pairs
            while bb <= b_limit and B <= vertical_limit:
                check_boundary(a, bb, P, B)
                bb += 1
                B *= q
            horizontal_limit = min(bound, integer_root(Q ** denominator, complement) + difference)
            aa, A = a + 1, P * p  # The corner was included on the first line.
            while aa <= a_limit and A <= horizontal_limit:
                check_boundary(aa, b, A, Q)
                aa += 1
                A *= p
            advance_a = advance_b = 1
            record.update(method="exact boundary lines", boundary_pairs=boundary_pairs - before)
        else:
            advance_a = a_steps + 1 if a_steps >= 0 else 0
            advance_b = b_steps + 1 if b_steps >= 0 else 0
            # Each accepted inequality is the exact condition used by the
            # strip lemma, including the last exponent in that strip.
            if advance_a:
                assert min_u ** complement >= P ** numerator * Integer(p) ** (denominator * a_steps)
            if advance_b:
                assert min_v ** complement >= Q ** numerator * Integer(q) ** (denominator * b_steps)
            record["method"] = "coefficient lower-bound strips"
        record.update(p_exponent_advance=advance_a, q_exponent_advance=advance_b)
        anchors.append(record)
        a += advance_a
        b += advance_b
        if a <= a_limit and b <= b_limit:
            P *= Integer(p) ** advance_a
            Q *= Integer(q) ** advance_b
    exceptions.sort(key=lambda r: (r["p_exponent"], r["q_exponent"], r["signed_difference"]))
    threshold = max(int(integer_root(Integer(difference) ** denominator, complement)) + 1,
                    max((r["smaller_height"] + 1 for r in exceptions), default=1))
    return {
        "pair": [p, q], "height_cap_power_of_ten": cap,
        "maximum_difference": difference,
        **({"reciprocal_exponent_denominator": denominator} if numerator == 1 else
           {"cofactor_exponent_numerator": numerator, "cofactor_exponent_denominator": denominator}),
        "height_threshold": threshold, "backend": backend,
        "initial_exponents": initial_exponents,
        "maximum_exponents": [a_limit, b_limit],
        "final_exponents": [a, b],
        "anchor_count": len(anchors), "exact_boundary_pairs": boundary_pairs,
        "boundary_pairs_sha256": boundary_hash.hexdigest(),
        "exception_count": len(exceptions), "exceptions": exceptions,
        "anchors": anchors,
        "conclusion": (f"max(u,v)^{denominator} >= min(p^a*u,q^b*v)" +
                       (f"^{numerator}" if numerator != 1 else "") +
                       " throughout the stated height range"),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pairs", nargs="+", default=["2,3"])
    parser.add_argument("--clique", nargs="+", type=int)
    parser.add_argument("--cap", type=int, default=1732)
    parser.add_argument("--difference", type=int, default=20)
    parser.add_argument("--exponent", type=Fraction, default=Fraction(1, 3))
    parser.add_argument("--backend", choices=["builtin", "gmpy2"], default="builtin")
    parser.add_argument("--max-boundary-pairs", type=int, default=100_000)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_suffix(".json"))
    args = parser.parse_args()
    records = []
    pairs = args.pairs if args.clique is None else [f"{p},{q}" for p, q in combinations(args.clique, 2)]
    for pair in pairs:
        p, q = map(int, pair.split(","))
        started = time.monotonic()
        row = certify(p, q, args.cap, args.difference, args.backend, args.max_boundary_pairs, args.exponent)
        records.append(row)
        print(json.dumps({k: v for k, v in row.items() if k not in ("anchors", "exceptions")} |
                         {"elapsed_seconds": time.monotonic() - started}), flush=True)
        args.output.write_text(json.dumps({
            "scope": "Exact coverage of prime-power exponent quadrants; no binomial rows enumerated.",
            "records": records,
        }, indent=2) + "\n")


if __name__ == "__main__":
    main()
