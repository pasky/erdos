"""Check the index-three curve families for Erdős problem 699.

Run with Python 3.11 or later; no third-party packages are required.
The mathematics is in ../archive/other_approaches/cubic_label_families.md.

Write d = n - 2j. The conditions from n - 1 and n - 2 say that every active
odd prime-power component of n - 1 divides d - 1 or d + 1, and every active
component of n - 2 divides d - 2, d, or d + 2. The label from n says that
every active component of n divides d.

The script verifies the polynomial identities for the cubic curve, the
congruences excluding powers of two from it, and the identities for the
conics k(d^2 - 1) = (n - 1)(n + 3k - 2). It then reruns the complete search
for rows 4 | n up to --limit and re-verifies every recorded solution with
n <= 8*10^9. The recorded list above the search limit came from a compiled
port of the same enumeration; its completeness is not rechecked here.
"""

from __future__ import annotations

import argparse
from array import array
from fractions import Fraction
import json
from math import gcd, isqrt
from pathlib import Path


RECORD_LIMIT = 8 * 10**9

# Every pair (n, j) with 8 <= n <= 8*10^9, 4 | n, 4 <= j < n/2 satisfying the
# initial Lucas blocks at the active primes of n - 1 and n - 2.
SOLUTIONS = [
    (76672, 26775), (175492, 60606), (335548, 115092),
    (1500868, 509067), (2218328, 468787), (2310352, 605201),
    (2832832, 957672), (6486472, 2185407), (7999552, 2693250),
    (9731332, 3274236), (17272972, 5802291), (17677792, 1866295),
    (18610024, 7865522), (23270536, 7811280), (29785472, 3964455),
    (36099856, 12106215), (40706812, 13647942), (45689932, 15315300),
    (46770572, 14546477), (54734052, 8748251), (65206612, 21843675),
    (78090488, 16502461), (79229008, 26532792), (106832728, 35761167),
    (116213176, 38896650), (126127252, 42210252), (154746736, 34894431),
    (163217692, 54605187), (188624152, 63094176), (236600992, 79122231),
    (252434548, 84411342), (268959196, 89931060), (291912296, 79181835),
    (326778608, 114125573), (329222116, 110058795), (369371872, 123467400),
    (443320552, 148161375), (467286832, 156163986), (492101668, 164449692),
    (581135788, 194176467), (639388072, 213624432), (744907312, 248850567),
    (778685932, 260126550), (813470572, 271738116), (936874612, 312930171),
    (1016588656, 339537240), (1159277176, 387161775), (1204547752, 402271002),
    (1250981812, 417768300), (1336095752, 275982752), (1414354492, 472291875),
    (1518889528, 507177792), (1704346048, 569066967), (1762788196, 588569310),
    (1822551292, 608512212), (2031491332, 678233547), (2164206592, 722518056),
    (2398029832, 800538111), (2471323168, 824993442), (2546094916, 849941820),
    (2806201036, 936727155), (2969546956, 1129181515), (2970455752, 991530000),
    (3205956776, 1556134875), (3258244432, 1087547175), (3348068572, 1117515366),
    (3439528588, 1148029092), (3756399508, 1253744667), (3955552912, 1320185592),
    (4302905752, 1436066127), (4323307328, 1183905164), (4410940312, 1472107050),
    (4520768212, 1508745996), (4870955104, 670863116), (4900002652, 1635258051),
    (5024865776, 922080051), (5137413976, 1714456800), (5210970568, 843429005),
    (5549929696, 1852066935), (5677854292, 1894740462), (5807729692, 1938064500),
    (6075310748, 1166818829), (6254926372, 2087239275), (6533954848, 2180315592),
    (7017232168, 2341521567), (7166726416, 2391387570), (7318328932, 2441956572),
    (7839086572, 2615660307),
]


def primes_through(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return [p for p in range(2, limit + 1) if sieve[p]]


def lucas_nonzero(n: int, j: int, p: int) -> bool:
    while j:
        if j % p > n % p:
            return False
        n //= p
        j //= p
    return True


# Polynomials are coefficient lists, lowest degree first.
def poly(*coefficients: int | Fraction) -> list[Fraction]:
    return [Fraction(c) for c in coefficients]


def poly_mul(*factors: list[Fraction]) -> list[Fraction]:
    result = [Fraction(1)]
    for factor in factors:
        product = [Fraction(0)] * (len(result) + len(factor) - 1)
        for i, a in enumerate(result):
            for k, b in enumerate(factor):
                product[i + k] += a * b
        result = product
    return result


def poly_add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    length = max(len(a), len(b))
    a = a + [Fraction(0)] * (length - len(a))
    b = b + [Fraction(0)] * (length - len(b))
    return [x + y for x, y in zip(a, b)]


def poly_scale(a: list[Fraction], scalar: int | Fraction) -> list[Fraction]:
    return [scalar * x for x in a]


def poly_equal(a: list[Fraction], b: list[Fraction]) -> bool:
    difference = poly_add(a, poly_scale(b, -1))
    return all(x == 0 for x in difference)


def poly_value(a: list[Fraction], x: int) -> Fraction:
    return sum(c * x**i for i, c in enumerate(a))


X = poly(0, 1)
CUBIC_N = poly_scale(poly(16, -9, 0, 1), Fraction(1, 8))
CUBIC_D = poly_scale(poly_mul(poly(3, 1), poly(16, -11, 1)), Fraction(1, 24))


def cubic_identities() -> dict:
    """The five shifts of d and three shifts of n factor as displayed."""
    one = poly(1)
    shifts = {
        "n - 2 = x(x - 3)(x + 3)/8": (
            poly_add(CUBIC_N, poly(-2)),
            poly_scale(poly_mul(X, poly(-3, 1), poly(3, 1)), Fraction(1, 8)),
        ),
        "n - 1 = (x - 1)(x^2 + x - 8)/8": (
            poly_add(CUBIC_N, poly(-1)),
            poly_scale(poly_mul(poly(-1, 1), poly(-8, 1, 1)), Fraction(1, 8)),
        ),
        "d - 2 = x(x^2 - 8x - 17)/24": (
            poly_add(CUBIC_D, poly(-2)),
            poly_scale(poly_mul(X, poly(-17, -8, 1)), Fraction(1, 24)),
        ),
        "d - 1 = (x - 1)(x^2 - 7x - 24)/24": (
            poly_add(CUBIC_D, poly_scale(one, -1)),
            poly_scale(poly_mul(poly(-1, 1), poly(-24, -7, 1)), Fraction(1, 24)),
        ),
        "d = (x + 3)(x^2 - 11x + 16)/24": (
            CUBIC_D,
            poly_scale(poly_mul(poly(3, 1), poly(16, -11, 1)), Fraction(1, 24)),
        ),
        "d + 1 = (x - 9)(x^2 + x - 8)/24": (
            poly_add(CUBIC_D, one),
            poly_scale(poly_mul(poly(-9, 1), poly(-8, 1, 1)), Fraction(1, 24)),
        ),
        "d + 2 = (x - 3)(x^2 - 5x - 32)/24": (
            poly_add(CUBIC_D, poly(2)),
            poly_scale(poly_mul(poly(-3, 1), poly(-32, -5, 1)), Fraction(1, 24)),
        ),
        "j = (n - d)/2 = x(x - 1)(x + 5)/24": (
            poly_scale(poly_add(CUBIC_N, poly_scale(CUBIC_D, -1)), Fraction(1, 2)),
            poly_scale(poly_mul(X, poly(-1, 1), poly(5, 1)), Fraction(1, 24)),
        ),
    }
    for name, (left, right) in shifts.items():
        assert poly_equal(left, right), name
    return {"verified": list(shifts)}


def cubic_power_of_two_exclusion() -> dict:
    """No x = 4 mod 9 has x^3 - 9x + 16 equal to a power of two."""

    def f(x: int) -> int:
        return x**3 - 9 * x + 16

    # For integer x, gcd(f(x), x - r) divides f(r).
    gcd_bounds = {"f(0)": f(0), "f(1)": f(1), "f(-5)": f(-5)}
    assert [f(0), f(1), f(-5)] == [16, 8, -64]
    residues_27 = sorted({f(x) % 27 for x in range(4, 4 + 27 * 9, 9)})
    assert residues_27 == [17]
    exponents_18 = [e for e in range(18) if pow(2, e, 27) == 17]
    assert exponents_18 == [15]
    order_73 = next(e for e in range(1, 73) if pow(2, e, 73) == 1)
    assert order_73 == 9 and 15 % 9 == 6 and pow(2, 6, 73) == 64
    values_73 = {f(x) % 73 for x in range(73)}
    assert 64 not in values_73
    return {
        "gcd_of_8n_and_24j_divides": 16 * 8 * 64,
        "values_giving_gcd_bounds": gcd_bounds,
        "f_mod_27_for_x_4_mod_9": residues_27,
        "exponents_e_mod_18_with_2^e_17_mod_27": exponents_18,
        "order_of_2_mod_73": order_73,
        "f_attains_64_mod_73": False,
    }


def factor(m: int, primes: list[int]) -> dict[int, int]:
    result = {}
    for p in primes:
        if p * p > m:
            break
        if m % p:
            continue
        exponent = 0
        while m % p == 0:
            m //= p
            exponent += 1
        result[p] = exponent
    if m > 1:
        result[m] = result.get(m, 0) + 1
    return result


def active_components(factors: dict[int, int]) -> list[tuple[int, int]]:
    return [
        (p, p**e) for p, e in factors.items()
        if p != 2 and not (p == 3 and e == 1)
    ]


SHIFTS = {0: (0,), 1: (1, -1), 2: (0, 2, -2)}


def label_status(n: int, j: int, primes: list[int]) -> dict:
    d = n - 2 * j
    components = {t: active_components(factor(n - t, primes)) for t in range(3)}
    holds = {
        t: all(any((d - r) % power == 0 for r in SHIFTS[t]) for _, power in components[t])
        for t in range(3)
    }
    lucas = all(
        lucas_nonzero(n, j, p) for t in (1, 2) for p, _ in components[t]
    )
    return {"labels": holds, "lucas_at_n_minus_1_and_n_minus_2": lucas}


def on_cubic_curve(n: int, j: int) -> int | None:
    root = round((8 * n) ** (1 / 3))
    for x in range(root - 3, root + 4):
        if x**3 - 9 * x + 16 == 8 * n and x * (x - 1) * (x + 5) == 24 * j:
            return x
    return None


def conic_parameters(n: int, j: int) -> tuple[int, int]:
    """Return (a, b) with (m - 3)/(n - 2) = a/b, m = (d^2 - 1)/(n - 1)."""
    d = n - 2 * j
    ratio = (Fraction(d * d - 1, n - 1) - 3) / (n - 2)
    return ratio.numerator, ratio.denominator


def conic_identities() -> dict:
    """On k(d^2 - 1) = (n - 1)(n + 3k - 2) the two labels hold away from k."""
    checked = 0
    for k in range(2, 40):
        for n in range(8, 400):
            # Treat d^2 as the value forced by the conic; the identities are
            # polynomial in n and d^2, so exact rational arithmetic suffices.
            d_squared = Fraction((n - 1) * (n + 3 * k - 2), k) + 1
            assert d_squared - 1 == Fraction((n - 1) * (n + 3 * k - 2), k)
            assert d_squared - 4 == Fraction((n - 2) * (n + 3 * k - 1), k)
            left = (2 * n + 3 * k - 3) ** 2 - 4 * k * d_squared
            assert left == (9 * k - 1) * (k - 1)
            checked += 1
    return {
        "d^2 - 1": "(n - 1)(n + 3k - 2)/k",
        "d^2 - 4": "(n - 2)(n + 3k - 1)/k",
        "pell_form": "(2n + 3k - 3)^2 - k(2d)^2 = (9k - 1)(k - 1)",
        "rational_checks": checked,
    }


def two_adic_conic_test(k: int) -> bool:
    """Whether k d^2 = -2(k - 1) mod 2^h is solvable with d even, h large.

    With k - 1 = 2^v w, w odd, and d = 2^e d', d' odd, the valuations force
    2e = v + 1. The remaining congruence k d'^2 = -w needs -w/k = 1 mod 8.
    """
    if k % 2 == 0:
        return False
    v = ((k - 1) & -(k - 1)).bit_length() - 1
    if v % 2 == 0:
        return False
    w = (k - 1) >> v
    return (-w * pow(k, -1, 8)) % 8 == 1


def largest_prime_factor_table(limit: int) -> array:
    table = array("I", [0]) * (limit + 1)
    for p in primes_through(limit):
        table[p::p] = array("I", [p]) * ((limit - p) // p + 1)
    return table


def search(limit: int) -> list[tuple[int, int]]:
    """All 4 | n <= limit and 4 <= j < n/2 meeting the labels of n-1, n-2."""
    table = largest_prime_factor_table(limit)

    def components(m: int) -> list[int]:
        factors: dict[int, int] = {}
        while m > 1:
            p = table[m]
            while m % p == 0:
                m //= p
                factors[p] = factors.get(p, 0) + 1
        return [power for _, power in active_components(factors)]

    found = []
    for n in range(8, limit + 1, 4):
        conditions = sorted(
            [(power, (0, 1)) for power in components(n - 1)]
            + [(power, (0, 1, 2)) for power in components(n - 2)],
            reverse=True,
        )
        upper = (n - 1) // 2
        modulus, residues = 1, [0]
        for power, allowed in conditions:
            inverse = pow(modulus, -1, power)
            refined = []
            for old in residues:
                for r in allowed:
                    value = old + modulus * (((r - old) * inverse) % power)
                    if value <= upper or modulus * power <= upper:
                        refined.append(value)
            modulus, residues = modulus * power, refined
            if not residues:
                break
        for value in residues:
            for j in range(value, upper + 1, modulus):
                if j >= 4:
                    found.append((n, j))
    return sorted(found)


def report(limit: int) -> dict:
    identities = cubic_identities()
    exclusion = cubic_power_of_two_exclusion()
    conics = conic_identities()

    primes = primes_through(isqrt(RECORD_LIMIT) + 1)
    records = []
    for n, j in SOLUTIONS:
        assert n % 4 == 0 and 4 <= j < n / 2 and n <= RECORD_LIMIT
        status = label_status(n, j, primes)
        assert status["labels"][1] and status["labels"][2]
        assert not status["labels"][0]
        assert not status["lucas_at_n_minus_1_and_n_minus_2"]
        a, b = conic_parameters(n, j)
        d = n - 2 * j
        assert d % b == 0
        x = on_cubic_curve(n, j)
        if x is not None:
            assert x % 9 == 4
            family = "cubic curve"
        elif a == 1:
            family = f"conic k = {b}"
        else:
            family = "other"
        records.append({"n": n, "j": j, "d": d, "a": a, "b": b, "family": family, "x": x})

    searched = search(limit)
    expected = [pair for pair in SOLUTIONS if pair[0] <= limit]
    assert searched == expected, (searched, expected)

    counts: dict[str, int] = {}
    for record in records:
        key = "conic k" if record["family"].startswith("conic") else record["family"]
        counts[key] = counts.get(key, 0) + 1
    conic_ks = sorted({r["b"] for r in records if r["family"].startswith("conic")})
    return {
        "scope": "Curve families for the index-three labels from n - 1 and n - 2; no bad triple exists on the cubic curve. Global nonexistence at index three is not claimed.",
        "cubic_curve": {
            "n": "(x^3 - 9x + 16)/8",
            "j": "x(x - 1)(x + 5)/24",
            "d": "(x + 3)(x^2 - 11x + 16)/24",
            "identities": identities,
            "power_of_two_exclusion": exclusion,
        },
        "conics": conics,
        "two_adic_test_for_observed_conics": {
            str(k): two_adic_conic_test(k) for k in conic_ks
        },
        "recorded_limit": RECORD_LIMIT,
        "recorded_solutions": records,
        "family_counts": counts,
        "search_limit_rechecked_here": limit,
        "solutions_found_by_search": len(searched),
        "checks": "Every recorded pair satisfies the labels from n - 1 and n - 2, fails the label from n, and fails a full Lucas condition at some prime of n - 1 or n - 2. The search below the limit reproduced the recorded list exactly.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=2 * 10**7)
    args = parser.parse_args()
    result = report(args.limit)
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "family_counts": result["family_counts"],
        "two_adic_test_for_observed_conics": result["two_adic_test_for_observed_conics"],
        "solutions_found_by_search": result["solutions_found_by_search"],
        "checks": result["checks"],
    }, indent=2))


if __name__ == "__main__":
    main()
