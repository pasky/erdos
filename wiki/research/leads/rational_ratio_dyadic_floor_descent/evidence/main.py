"""Certify the completeness of specific two-ray dyadic floor sets.

For positive reals ``alpha, beta`` with ``floor(beta) < floor(alpha) <
2 floor(beta)`` and ``floor(beta) >= 2`` (a normalized pair in the sense of
the Problem 354 reconstructions), the weights ``a_i = floor(2^i alpha)`` and
``b_i = floor(2^i beta)`` interlace as ``b_0 < a_0 < b_1 < a_1 < ...`` with
each weight at most twice its predecessor. If the subset sums of the ``2n``
weights of indices below ``n`` contain ``b_n`` consecutive integers, then
every integer from the start of that run on is a subset sum of the weights
of some longer prefix: this is the mesh lemma of the reconstructed Yu--Chen
argument with gap one, as applied on its digit-budget page. Such a run is a
finite certificate that the set of nonzero values of the two rays is
complete, and so that the interleaved sequence of Problem 354 is complete
for that pair.

This entry point recomputes the certificates recorded on the lead page for
pairs whose ratio is a rational number other than a power of two and whose
coefficients are both non-dyadic (rational or quadratic irrational), the
cases of Hegyvari's conjecture that no held source covers, and for one
irrational-ratio control pair. The weights are computed exactly from
integer data (``floor(2^i p/q)`` as an integer quotient and
``floor(2^i sqrt(c)/d)`` as an integer square root), the subset sums are
held as one Python integer used as a bit set, and the longest run of
represented integers is found by binary search on the run length. Each
certificate is pinned by its depth and the start of its run. A sweep then
certifies, without pinning, every pair ``(3 gamma, 2 gamma)`` with
``gamma = 2^T / d`` for the odd denominators ``d`` from 5 to 99 that are not
multiples of 3, normalized by the least ``T`` for which the pair is
normalized, ``2 <= floor(2 gamma) < floor(3 gamma) < 2 floor(2 gamma)``.
A negative control checks that the search finds no certificate to depth
16 for the multiset of Hegyvari's incomplete pair ``alpha = 5/2``,
``beta = 5``; the absence of a certificate proves nothing and is only a
check that the search is not vacuous.

Run from the repository root:
    uv run --no-sync python wiki/research/leads/rational_ratio_dyadic_floor_descent/evidence/main.py

Dependencies are the standard library and the installed root ``tools``
package. There are no input files, output files, random choices or reduced
modes; the run takes a few seconds. Failed obligations exit nonzero,
including under ``python -O``, because every check goes through the shared
``Checker``. Passing certifies completeness of the listed pairs only; it
does not bear on Hegyvari's conjecture in general and awards no tier.
"""

from __future__ import annotations

from math import isqrt

import tools

__all__ = [
    'PINNED',
    'certificate',
    'check_pinned',
    'check_sweep',
    'check_control',
    'main',
]


def floors_rational(p: int, q: int, count: int) -> list[int]:
    """Return floor(2^i p / q) for 0 <= i < count."""
    return [(p << i) // q for i in range(count)]


def floors_sqrt(c: int, d: int, count: int) -> list[int]:
    """Return floor(2^i sqrt(c) / d) for 0 <= i < count.

    The integer ``k = floor(2^i sqrt(c) / d)`` is the largest ``k`` with
    ``k^2 d^2 <= c 4^i``, which is the integer square root of the integer
    quotient ``c 4^i // d^2``.
    """
    return [isqrt((c << (2 * i)) // (d * d)) for i in range(count)]


def _has_run(sums: int, length: int) -> int:
    """Return the AND of the shifts of ``sums`` by 0, ..., length - 1."""
    # fold the shifts by doubling so that bit z is set exactly when the
    # integers z, ..., z + length - 1 are all represented
    result = sums
    got = 1
    while got * 2 <= length:
        result &= result >> got
        got *= 2
    if got < length:
        result &= result >> (length - got)
    return result


def longest_run(sums: int, limit: int) -> int:
    """Return the longest run of represented integers, capped at ``limit``."""
    lo, hi = 0, limit
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if _has_run(sums, mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


def certificate(
    a: list[int], b: list[int], depth: int,
) -> tuple[int, int, int] | None:
    """Search the prefixes of a weight pair for a completeness certificate.

    Returns ``(n, start, b_n)`` for the least ``n <= depth`` at which the
    subset sums of the weights of indices below ``n`` contain the ``b_n``
    consecutive integers ``start, ..., start + b_n - 1``, or ``None``.
    The lists must hold at least ``depth + 1`` weights.
    """
    # the empty sum, then adjoin the weights layer by layer
    sums = 1
    for n in range(1, depth + 1):
        sums |= sums << a[n - 1]
        sums |= sums << b[n - 1]
        needed = b[n]
        if longest_run(sums, needed) >= needed:
            starts = _has_run(sums, needed)
            start = (starts & -starts).bit_length() - 1
            return n, start, needed
    return None


def _interlaced(a: list[int], b: list[int]) -> bool:
    """Return whether b_0 < a_0 < b_1 < ... with each term at most double."""
    merged = [w for pair in zip(b, a) for w in pair]
    return all(
        merged[i] < merged[i + 1] <= 2 * merged[i]
        for i in range(len(merged) - 1)
    )


# (label, alpha-weights, beta-weights, expected depth, expected start)
PINNED: list[tuple[str, list[int], list[int], int, int]] = [
    ('48/5, 32/5', floors_rational(48, 5, 24), floors_rational(32, 5, 24), 9, 1423),
    ('48/7, 32/7', floors_rational(48, 7, 24), floors_rational(32, 7, 24), 9, 577),
    ('80/9, 64/9', floors_rational(80, 9, 24), floors_rational(64, 9, 24), 7, 445),
    ('6 sqrt 2, 4 sqrt 2', floors_sqrt(72, 1, 24), floors_sqrt(32, 1, 24), 7, 183),
    ('5 sqrt 2, 3 sqrt 2', floors_sqrt(50, 1, 24), floors_sqrt(18, 1, 24), 3, 18),
    ('sqrt 50, sqrt 20', floors_sqrt(50, 1, 24), floors_sqrt(20, 1, 24), 6, 77),
]


def check_pinned(checker: tools.Checker) -> None:
    """Recompute the pinned certificates."""
    for label, a, b in ((row[0], row[1], row[2]) for row in PINNED):
        # normalization and interlacing of the recorded pair
        big, small = a[0], b[0]
        checker.check(
            f'{label}: normalized pair',
            small >= 2 and small < big < 2 * small,
            f'floor(alpha) = {big}, floor(beta) = {small}',
        )
        checker.check(f'{label}: interlaced weights', _interlaced(a, b))
    for label, a, b, depth, start in PINNED:
        found = certificate(a, b, 20)
        checker.check(
            f'{label}: certificate at depth {depth} from {start}',
            found is not None and found[0] == depth and found[1] == start,
            str(found),
        )


def check_sweep(checker: tools.Checker) -> None:
    """Certify the family (3 gamma, 2 gamma), gamma = 2^T / d, d odd."""
    certified = 0
    total = 0
    worst = 0
    for d in range(5, 100, 2):
        if d % 3 == 0:
            continue
        # the least T for which (3 gamma, 2 gamma) is normalized:
        # 2 <= floor(2 gamma) < floor(3 gamma) < 2 floor(2 gamma)
        shift = 0
        while True:
            small, big = (2 << shift) // d, (3 << shift) // d
            if 2 <= small < big < 2 * small:
                break
            shift += 1
        a = floors_rational(3 << shift, d, 24)
        b = floors_rational(2 << shift, d, 24)
        total += 1
        if not _interlaced(a, b):
            continue
        found = certificate(a, b, 20)
        if found is not None:
            certified += 1
            worst = max(worst, found[0])
    checker.check(
        'sweep: 32 denominators, all certified to depth 20',
        total == 32 and certified == total,
        f'{certified} of {total} certified',
    )
    checker.check('sweep: greatest depth needed is 12', worst == 12, str(worst))


def check_control(checker: tools.Checker) -> None:
    """Check that the incomplete pair alpha = 5/2, beta = 5 gets no certificate."""
    # the multiset of the two rays: b_i = a_{i+1}, so the sorted list is
    # a_0, a_1, a_1, a_2, a_2, ...; from a_1 on each term is at most twice
    # its predecessor (5/2 = 10.1 in binary, so a_{i+1} = 2 a_i for i >= 1),
    # which is all the mesh lemma needs after the first layer
    a = floors_rational(5, 2, 24)
    b = floors_rational(5, 1, 24)
    checker.check('control: beta-ray is the shifted alpha-ray', b[:23] == a[1:])
    merged = [w for i in range(1, 23) for w in (a[i], a[i])]
    doubling = all(merged[i] <= merged[i + 1] <= 2 * merged[i] for i in range(len(merged) - 1))
    checker.check('control: merged multiset at most doubles from the second term', doubling)
    checker.check('control: no certificate to depth 16', certificate(a, b, 16) is None)


def main() -> int:
    """Run every check and return the exit code."""
    parser = tools.evidence_parser(
        'Certify the completeness of specific two-ray dyadic floor sets.',
        quick=False,
    )
    parser.parse_args()
    checker = tools.Checker()
    check_pinned(checker)
    check_sweep(checker)
    check_control(checker)
    return checker.finish()


if __name__ == '__main__':
    raise SystemExit(main())
