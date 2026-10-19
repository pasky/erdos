"""Recompute the exact collision census for s(n) = sigma(n) - n.

Checked clauses:

1. Independent reference. Through x = 10^5 the compiled census agrees
   exactly with a direct Python computation from proper-divisor sums, in
   both flag modes and with buckets narrow enough that every run crosses
   hundreds of bucket boundaries: every count R and pair count C at the 9
   checkpoints, every fiber-size histogram, and the counts of primes and of
   inputs with exactly two prime factors. The same comparison at 2^18 - 1,
   2^18, and 2^18 + 1 checks the first segmented-sieve boundary.
2. External counts. The census's prime counts at 10^3, ..., 10^9 equal the
   known values of pi(10^k), and its counts of n <= 10^k with exactly two
   prime factors, counted with multiplicity, equal the known values
   299, ..., 160788536. Below 2^30 no level is clipped, as s(n) > sqrt(n)
   for composite n requires.
3. Internal consistency at every checkpoint: C >= R and C - R is even; R and
   C are nondecreasing in x and in k; R(D_k) = R(DF_k) + R(DN_k) and
   C(D_k) >= C(DF_k) + C(DN_k); and at every histogram checkpoint
   sum_t t H(t) = R and sum_t t^2 H(t) = C for every class.
4. Recorded findings. Every R, C, histogram and external count recorded in
   both assets is reproduced exactly: mode 0 (flag: at least
   three prime factors) and mode 1 (flag: a prime factor above the square
   root) through 10^9 in ``assets/census.json``, and mode 0 through 10^10
   in ``assets/census_1e10.json``. The overlapping mode-0 findings agree.

``--top-exponent 9`` checks only the first asset, a reduced range. The
default is 10 and also checks pi(10^10) = 455052511 and 1493776443 inputs
with two prime factors.

The classes are defined in ``util/census.cpp``: D_k is the set of composite
n with 2^k s(n) >= n (for k = 15, all composites), DF_k and DN_k its flagged
and unflagged parts. Pairs are ordered, the diagonal is included, and
C = sum_m r(m)^2. The checkpoints are floor(10^(3 + j/4)) for j = 0, ..., 24
through 10^9 and j = 0, ..., 28 through 10^10.

Run from the repository root:
    uv run --no-sync python wiki/research/leads/aliquot_collision_density/evidence/main.py

Dependencies: the root ``tools`` package and a C++17 compiler on PATH
(``c++``, ``clang++`` or ``g++``), with unsigned 128-bit integer support.
All arithmetic is exact integer arithmetic. The full run builds the census,
runs mode 0 to 10^10 and mode 1 to 10^9, taking about forty minutes on one
core and about 40 GB of scratch disk under the work
directory (default ``evidence/output/``), which the census deletes as it
reads. ``--quick`` runs clause 1 and checks clauses 2 to 4 through 10^7 only,
in about thirty seconds. ``--workdir DIR`` moves the scratch files.
Limitation: a finite census proves no asymptotic statement; the page states
what it supports.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from tools import Checker, evidence_parser

sys.path.insert(0, str(Path(__file__).resolve().parent / 'util'))
import brute
import report

__all__ = [
    'main',
]

_HERE = Path(__file__).resolve().parent

# pi(10^k) and the counts of n <= 10^k with Omega(n) = 2, for k = 3, ..., 10
_PI = [168, 1229, 9592, 78498, 664579, 5761455, 50847534, 455052511]
_SEMI = [299, 2625, 23378, 210035, 1904324, 17427258, 160788536, 1493776443]

# classes D_k, DF_k, DN_k for k = 0, ..., 15
_CLASSES = [f'{p}{k}' for p in ('D', 'DF', 'DN') for k in range(16)]


def _grouped(hist: dict) -> dict[tuple[int, str], dict[int, int]]:
    """Return the histogram rows grouped by (checkpoint, class)."""
    out: dict[tuple[int, str], dict[int, int]] = {}
    for (j, c, t), v in hist.items():
        out.setdefault((j, c), {})[t] = v
    return out


def _consistency(rep: dict, xs: list[int], hist_js: list[int]) -> list[str]:
    """Return the names of the internal-consistency obligations that fail."""
    bad = []
    R, C, H = rep['R'], rep['C'], _grouped(rep['H'])
    for j in range(len(xs)):
        for c in _CLASSES:
            if C[c, j] < R[c, j] or (C[c, j] - R[c, j]) % 2:
                bad.append(f'parity or order of C at {c}, j={j}')
            if j and (R[c, j] < R[c, j - 1] or C[c, j] < C[c, j - 1]):
                bad.append(f'monotone in x at {c}, j={j}')
        for p in ('D', 'DF', 'DN'):
            for k in range(1, 16):
                if (
                    R[f'{p}{k}', j] < R[f'{p}{k - 1}', j]
                    or C[f'{p}{k}', j] < C[f'{p}{k - 1}', j]
                ):
                    bad.append(f'monotone in k at {p}{k}, j={j}')
        for k in range(16):
            if R[f'D{k}', j] != R[f'DF{k}', j] + R[f'DN{k}', j]:
                bad.append(f'R split at k={k}, j={j}')
            if C[f'D{k}', j] < C[f'DF{k}', j] + C[f'DN{k}', j]:
                bad.append(f'C split at k={k}, j={j}')
    for j in hist_js:
        for c in _CLASSES:
            rows = H.get((j, c), {}).items()
            if (
                sum(t * v for t, v in rows) != R[c, j]
                or sum(t * t * v for t, v in rows) != C[c, j]
            ):
                bad.append(f'histogram moments at {c}, j={j}')
    return bad


def _recorded(rep: dict, rec: dict, upto: int, hist_js: list[int]) -> list[str]:
    """Return the recorded findings through checkpoint ``upto`` that differ."""
    bad = []
    H = _grouped(rep['H'])
    for c in _CLASSES:
        for j in range(upto + 1):
            if rep['R'][c, j] != rec['R'][c][j] or rep['C'][c, j] != rec['C'][c][j]:
                bad.append(f'R or C at {c}, j={j}')
    for j in hist_js:
        for c in _CLASSES:
            got = H.get((j, c), {})
            want = {int(t): v for t, v in rec['H'][str(j)][c]}
            if got != want:
                bad.append(f'histogram at {c}, j={j}')
    for j in range(upto + 1):
        if rep['PRIMES'][j] != rec['primes'][j] or rep['OMEGA2'][j] != rec['omega2'][j]:
            bad.append(f'prime or two-factor count at j={j}')
    return bad


def main() -> int:
    """Run the checks and return the process exit code."""
    parser = evidence_parser(
        'Recompute the exact collision census for s(n) = sigma(n) - n.'
    )
    parser.add_argument(
        '--workdir', type=Path, default=_HERE / 'output', help='scratch directory'
    )
    parser.add_argument(
        '--top-exponent',
        type=int,
        choices=(9, 10),
        default=10,
        help='default: all findings; 9: reduced range through 10^9',
    )
    args = parser.parse_args()
    checker = Checker()
    exe = report.build(args.workdir / 'build')
    # clause 1: the independent reference through 10^5, both modes
    xs5 = report.checkpoints(5)
    hj5 = list(range(len(xs5)))
    for mode, wbits in ((0, 6), (1, 5)):
        got = report.parse(
            report.run(exe, args.workdir / 'small', wbits, xs5, hj5, mode)
        )
        ref = brute.census(xs5, hj5, mode)
        for key in ('R', 'C', 'H', 'PRIMES', 'OMEGA2'):
            checker.check(
                f'mode {mode}: {key} through 10^5 equals the direct computation',
                got[key] == ref[key],
            )
        boundaries = [2**18 - 1, 2**18, 2**18 + 1]
        got = report.parse(
            report.run(exe, args.workdir / 'boundary', 8, boundaries, [0, 1, 2], mode)
        )
        ref = brute.census(boundaries, [0, 1, 2], mode)
        checker.check(
            f'mode {mode}: all counts and histograms across the first segment boundary',
            all(got[key] == ref[key] for key in ('R', 'C', 'H', 'PRIMES', 'OMEGA2')),
        )
    # clauses 2 to 4 through the run's top checkpoint
    top = 7 if args.quick else args.top_exponent
    if top < 10:
        print(
            f'Reduced coverage: both modes through 10^{top}; the 10^10 extension is unchecked.'
        )
    recorded = json.loads((_HERE / 'assets' / 'census.json').read_text())
    extended = (
        json.loads((_HERE / 'assets' / 'census_1e10.json').read_text())
        if top == 10
        else None
    )
    for mode, run_top in ((0, top), (1, min(top, 9))):
        xs = report.checkpoints(run_top)
        upto = len(xs) - 1
        hist_js = list(range(0, upto + 1, 4))
        rec = extended['mode0'] if run_top == 10 else recorded[f'mode{mode}']
        checker.check(
            f'mode {mode}: recorded checkpoints match',
            rec['checkpoints'][: upto + 1] == xs,
        )
        rep = report.parse(
            report.run(exe, args.workdir / 'large', 22, xs, hist_js, mode)
        )
        checker.check(f'mode {mode}: executed checkpoints match', rep['X'] == xs)
        checker.check(
            f'mode {mode}: one record for every composite input',
            rep['META']['RECORDS']
            == xs[-1] - 1 - rep['PRIMES'][upto]
            == rep['R']['D15', upto],
        )
        if run_top <= 9:
            checker.check(
                f'mode {mode}: no clipped level below 2^30', rep['META']['CLIPPED'] == 0
            )
        decades = list(range(0, upto + 1, 4))
        checker.check(
            f'mode {mode}: pi(10^k) for k = 3..{run_top}',
            [rep['PRIMES'][j] for j in decades] == _PI[: len(decades)],
        )
        checker.check(
            f'mode {mode}: two-prime-factor counts for k = 3..{run_top}',
            [rep['OMEGA2'][j] for j in decades] == _SEMI[: len(decades)],
        )
        bad = _consistency(rep, xs, hist_js)
        checker.check(f'mode {mode}: internal consistency', not bad, '; '.join(bad[:5]))
        bad = _recorded(rep, rec, upto, hist_js)
        checker.check(
            f'mode {mode}: recorded findings reproduced through 10^{run_top}',
            not bad,
            '; '.join(bad[:5]),
        )
        if run_top == 10:
            prefix = recorded['mode0']
            checker.check(
                'mode 0: shared checkpoints match', prefix['checkpoints'] == xs[:25]
            )
            bad = _recorded(rep, prefix, 24, list(range(0, 25, 4)))
            checker.check(
                'mode 0: both assets agree through 10^9', not bad, '; '.join(bad[:5])
            )
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
