"""Exact checks for the three-prime running-lcm research page.

Run from the repository root:
    uv run --no-sync python wiki/research/smooth_lcm_three_prime/evidence/main.py

The checks are:

- the running lcm at every smooth cutoff m <= 10^14 (10^9 with ``--quick``)
  equals prod_u u^floor(log_u m), against a brute-force cumulative lcm, for the
  prime sets {2,3,5}, {2,3,7}, {3,5,7}, {2,5,11} and {2,3,5,7}, with the
  number of smooth integers pinned;
- the finite telescoping identity: for every prime power X <= 10^12 of the set,
  sum (u - 1)/D(u^j) over prime powers u^j <= X equals 1 - 1/D(X), for
  {2,3}, {2,3,5} and {2,3,5,7};
- the finite event identity: for every prime power X <= 10^9 of {2,3,5}, the
  sum of 1/D(m) over smooth m < X equals the sum of (u - 1) Psi(u^j)/D(u^j)
  over prime powers u^j <= X plus Psi(X)/D(X), where Psi(x) counts smooth
  integers below x;
- the cutoff m = 30 for {2,3,5}: D(30) = 10800 exceeds D(m_1) D(m_2) for each
  of the three splittings 30 = m_1 m_2 across a bipartition of the primes, the
  carries of D(30) against D(2) D(3) D(5) are (0,1,1), and D(6) = 60 differs
  from the two-prime value 12;
- for {2,3,5}, each pair u, v with third prime z, and N = 1, ..., 6: exponents
  i_1..i_N, j_1..j_N whose z-carries form the triangular pattern
  carry = [t >= s], and whose matrix of 1/D(u^i_s v^j_t) is invertible;
- formal relation counts over Z/(2^31 - 1), described in ``util/formal.py``:
  two positive controls (the two-prime product identity and the telescoping
  identity among the prime-power sums are each found exactly once), then the
  absence of any relation between S(Y) and the one- and two-slope prime-power
  sums: no relation sum_i c_i M_i = 0 with M_i = S^k times a monomial in A_p,
  A_q, A_{p;q}, A_{p;r}, A_{q;r} of total degree at most 3 and c_i of degree
  at most 4, truncated at degree 42, for {2,3,5}; the same with c_i of degree
  at most 3 at truncation 36 for {2,3,7} and {3,5,7}; none when the three
  face sums of S join the base, at total degree at most 2, c_i of degree at
  most 3 and truncation 44, for {2,3,5}; and none among the products of total
  degree at most 3 in S and the three two-prime series S_{pq}, S_{pr}, S_{qr},
  with c_i of degree at most 4 at truncation 40, for {2,3,5}. ``--quick``
  keeps the controls and runs only the {2,3,5} search with c_i of degree at
  most 3 at truncation 36.

Every floor of a logarithm is an exact integer comparison of prime powers. The
witness search reads 50-digit fractional parts from mpmath only to propose
exponents; every proposed witness is then verified in exact arithmetic. Each
formal count is exact: full column rank modulo a prime implies full rank over
Q, so a zero relation count proves that no relation of the stated shape exists.
Dependencies are the standard library, numpy, mpmath and the installed root
``tools`` package. There are no file inputs; nothing is written. The full run
takes about two minutes and about 1 GB of memory, dominated by the degree-4
search; ``--quick`` takes about fifteen seconds. Failed obligations exit
nonzero, including under ``python -O``. The checks concern only the stated
finite ranges and families; the identities themselves are proved on the
research page, and no check bears on the irrationality of any series.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

import mpmath
import tools

sys.path.insert(0, str(Path(__file__).resolve().parent / 'util'))
from formal import (  # noqa: E402
    face_series,
    monomial_family,
    multiply,
    pair_series,
    prime_power_series,
    relation_count,
    staircase_series,
    two_prime_series,
)
from smooth import (  # noqa: E402
    brute_force_mismatches,
    carry,
    events_upto,
    exact_sum_below,
    running_lcm,
    smooth_upto,
)

__all__ = [
    'check_formula',
    'check_telescoping',
    'check_events',
    'check_cutoff_thirty',
    'triangular_witness',
    'check_witnesses',
    'check_relations',
    'main',
]

# pin the number of smooth integers up to each formula bound
_FORMULA_SETS = {
    (2, 3, 5): {10**9: 1530, 10**14: 5310},
    (2, 3, 7): {10**9: 1293, 10**14: 4457},
    (3, 5, 7): {10**9: 590, 10**14: 1997},
    (2, 5, 11): {10**9: 762, 10**14: 2575},
    (2, 3, 5, 7): {10**9: 5194, 10**14: 25861},
}


def check_formula(checker: tools.Checker, bound: int) -> None:
    """Compare the running-lcm formula with a cumulative lcm up to bound."""
    for primes, counts in _FORMULA_SETS.items():
        count, bad = brute_force_mismatches(primes, bound)
        checker.check(
            f'running lcm formula at every smooth m <= {bound} for {primes}',
            bad == 0 and count == counts[bound],
            f'{bad} mismatches among {count} cutoffs',
        )


def check_telescoping(checker: tools.Checker) -> None:
    """Check sum (u - 1)/D(u^j) over prime powers u^j <= X equals 1 - 1/D(X)."""
    for primes in [(2, 3), (2, 3, 5), (2, 3, 5, 7)]:
        total, ok, count = Fraction(0), True, 0
        for x, u in events_upto(primes, 10**12):
            total += Fraction(u - 1, running_lcm(primes, x))
            ok = ok and total == 1 - Fraction(1, running_lcm(primes, x))
            count += 1
        checker.check(
            f'finite telescoping identity at all {count} prime powers <= 10^12 '
            f'for {primes}',
            ok,
        )


def check_events(checker: tools.Checker) -> None:
    """Check the finite event identity at every prime power X <= 10^9 of {2,3,5}."""
    primes = (2, 3, 5)
    smooth = smooth_upto(primes, 10**9)
    events = events_upto(primes, 10**9)
    ok = True
    partial = Fraction(0)
    for x, u in events:
        psi = sum(1 for m in smooth if m < x)
        d = running_lcm(primes, x)
        partial += Fraction((u - 1) * psi, d)
        ok = ok and exact_sum_below(primes, x) == partial + Fraction(psi, d)
    checker.check(
        f'finite event identity at all {len(events)} prime powers <= 10^9 for '
        f'{primes}',
        ok,
    )


def check_cutoff_thirty(checker: tools.Checker) -> None:
    """Check the cutoff m = 30 examples for {2,3,5}."""
    primes = (2, 3, 5)
    d = {m: running_lcm(primes, m) for m in (2, 3, 5, 6, 10, 15, 30)}
    checker.check('D(30) = 2^4 3^3 5^2 = 10800', d[30] == 2**4 * 3**3 * 5**2 == 10800)
    checker.check(
        'D(30) exceeds D(m_1) D(m_2) across each prime bipartition',
        all(d[30] > d[a] * d[b] for a, b in ((2, 15), (3, 10), (5, 6))),
    )
    checker.check(
        'carries of D(30) against D(2) D(3) D(5) are (0,1,1)',
        d[2] * d[3] * d[5] == 720
        and (carry(2, 3, 5), carry(3, 2, 5), carry(5, 2, 3)) == (0, 1, 1)
        and d[30] == 720 * 3 * 5,
    )
    checker.check(
        'D(6) = 60 for {2,3,5} but 12 for {2,3}',
        d[6] == 60 and running_lcm((2, 3), 6) == 12,
    )


def triangular_witness(
    u: int, v: int, z: int, size: int
) -> tuple[list[int], list[int]] | None:
    """Propose small exponents whose z-carries on u^i v^j form [t >= s].

    The j_t are the least exponents with frac(j log v/log z) within
    1/(4(size + 1)) of t/(size + 1), and each i_s is the least exponent with
    frac(i log u/log z) in the middle half of (1 - y_s, 1 - y_{s-1}), where
    y_0 = 0. Only exponents below 4000 are tried; exact checks follow.
    """
    # read 50-digit fractional parts to propose exponents
    mpmath.mp.dps = 50
    ru, rv = mpmath.log(u) / mpmath.log(z), mpmath.log(v) / mpmath.log(z)
    width = mpmath.mpf(1) / (4 * (size + 1))
    js, ys = [], []
    for t in range(1, size + 1):
        target = mpmath.mpf(t) / (size + 1)
        j = next(
            (k for k in range(1, 4000) if abs(mpmath.frac(k * rv) - target) < width),
            None,
        )
        if j is None:
            return None
        js.append(j)
        ys.append(mpmath.frac(j * rv))
    is_ = []
    for s in range(size):
        lo, hi = 1 - ys[s], (1 if s == 0 else 1 - ys[s - 1])
        a, b = lo + (hi - lo) / 4, hi - (hi - lo) / 4
        i = next((k for k in range(1, 4000) if a < mpmath.frac(k * ru) < b), None)
        if i is None:
            return None
        is_.append(i)
    return is_, js


def check_witnesses(checker: tools.Checker) -> None:
    """Verify triangular carry witnesses and invertible submatrices exactly."""
    primes = (2, 3, 5)
    for u, v, z in ((2, 3, 5), (2, 5, 3), (3, 5, 2)):
        for size in range(1, 7):
            found = triangular_witness(u, v, z, size)
            if found is None:
                checker.check(f'witness proposal for {u},{v},{z}, N={size}', False)
                continue
            is_, js = found
            pattern = all(
                carry(z, u**i, v**j) == (1 if t >= s else 0)
                for s, i in enumerate(is_)
                for t, j in enumerate(js)
            )
            matrix = [
                [Fraction(1, running_lcm(primes, u**i * v**j)) for j in js]
                for i in is_
            ]
            checker.check(
                f'triangular {z}-carries and invertible {size}x{size} matrix of '
                f'1/D(u^i v^j) for u={u}, v={v}',
                pattern and _determinant(matrix) != 0,
            )


def _determinant(matrix: list[list[Fraction]]) -> Fraction:
    """Return the determinant of a square matrix by exact elimination."""
    a = [row[:] for row in matrix]
    n, det = len(a), Fraction(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if a[r][c] != 0), None)
        if piv is None:
            return Fraction(0)
        if piv != c:
            a[c], a[piv] = a[piv], a[c]
            det = -det
        det *= a[c][c]
        for r in range(c + 1, n):
            f = a[r][c] / a[c][c]
            a[r] = [x - f * y for x, y in zip(a[r], a[c])]
    return det


def check_relations(checker: tools.Checker, quick: bool) -> None:
    """Run the two positive controls and the formal relation searches."""
    primes, n = (2, 3, 5), 30
    pq = pair_series(primes, 2, 3, n)
    control = [{(0, 0, 0): 1}, pq, _square(pq, n), two_prime_series(primes, 2, 3, n)]
    cols, rank, _ = relation_count(control, 2, n)
    checker.check(
        'control: the two-prime product identity is the one relation among '
        '1, A_{p;q}, A_{p;q}^2 and S_{pq} with degree-2 coefficients',
        cols - rank == 1,
        f'{cols - rank} relations',
    )
    control = [{(0, 0, 0): 1}] + [prime_power_series(primes, u, n) for u in primes]
    cols, rank, _ = relation_count(control, 3, n)
    checker.check(
        'control: the telescoping identity is the one relation among 1, A_p, '
        'A_q, A_r with degree-3 coefficients',
        cols - rank == 1,
        f'{cols - rank} relations',
    )
    searches = [((2, 3, 5), 3, 36, 'prime-power')]
    if not quick:
        searches = [
            ((2, 3, 5), 4, 42, 'prime-power'),
            ((2, 3, 7), 3, 36, 'prime-power'),
            ((3, 5, 7), 3, 36, 'prime-power'),
            ((2, 3, 5), 3, 44, 'face'),
            ((2, 3, 5), 4, 40, 'two-prime'),
        ]
    for primes, d, n, kind in searches:
        p, q, r = primes
        base = {
            'Ap': prime_power_series(primes, p, n),
            'Aq': prime_power_series(primes, q, n),
            'Apq': pair_series(primes, p, q, n),
            'Apr': pair_series(primes, p, r, n),
            'Aqr': pair_series(primes, q, r, n),
        }
        degree, label = 3, ''
        if kind == 'face':
            base['Fab'] = face_series(primes, (1, 1, 0), n)
            base['Fac'] = face_series(primes, (1, 0, 1), n)
            base['Fbc'] = face_series(primes, (0, 1, 1), n)
            degree, label = 2, 'with face sums '
        if kind == 'two-prime':
            base = {
                'Spq': two_prime_series(primes, p, q, n),
                'Spr': two_prime_series(primes, p, r, n),
                'Sqr': two_prime_series(primes, q, r, n),
            }
            label = 'with the two-prime series '
        family = monomial_family(staircase_series(primes, n), base, degree, n)
        cols, rank, met = relation_count([ser for _, ser in family], d, n)
        checker.check(
            f'no relation {label}for {primes}: {len(family)} products, '
            f'coefficient degree <= {d}, truncation {n} ({cols} columns, '
            f'{met} equations)',
            rank == cols,
            f'{cols - rank} relations',
        )


def _square(ser: dict[tuple[int, int, int], int], n: int) -> dict:
    """Return the square of a series truncated at total degree n."""
    return multiply(ser, ser, n)


def main() -> int:
    """Run every check and return the harness exit status."""
    args = tools.evidence_parser(__doc__ or '').parse_args()
    checker = tools.Checker()
    check_formula(checker, 10**9 if args.quick else 10**14)
    check_telescoping(checker)
    check_events(checker)
    check_cutoff_thirty(checker)
    check_witnesses(checker)
    check_relations(checker, args.quick)
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
