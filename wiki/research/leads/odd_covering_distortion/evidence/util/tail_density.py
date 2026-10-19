"""Outward rational certificate for the exact-loss tail from uniform density.

Specification: exact_loss_tail.md, 'A uniform-density sufficient condition'.
Integer atom weights are lower probabilities in units of 2**128. First and
second moments are rounded upwards in the same units. Dropped atoms and
geometric tails are charged through the full first moment, never ignored.
"""

from __future__ import annotations

from collections.abc import Callable
from fractions import Fraction

from tools import Checker

SCALE = 2**128
PRODUCT_CUTOFF = 4096
DEPTH_CUTOFF = 10


def ceiling_ratio(numerator: int, denominator: int) -> int:
    """Ceiling of a nonnegative rational number."""
    if numerator < 0 or denominator <= 0:
        raise ValueError('expected a nonnegative ratio')
    return (numerator + denominator - 1) // denominator


def factor_probabilities(
    p: int, small: bool, first_size: int | None = None
) -> list[tuple[int, int]]:
    """Exact probabilities for agreement depth j, 0 <= j <= 10.

    In a small coordinate with r allowed first digits,
    Pr(a >= t) = p**(1-t)/r. The default is r = p-1.
    At a large prime, delta = 2/5 and Pr(g >= t) = 5/(3*p**t).
    The omitted deeper factors retain their contribution to full moments.
    """
    if small:
        r = p - 1 if first_size is None else first_size
        if not 1 <= r <= p - 1:
            raise ValueError('invalid first-digit alphabet size')
        return [(r - 1, r)] + [(p - 1, r * p**j) for j in range(1, DEPTH_CUTOFF + 1)]
    return [(3 * p - 5, 3 * p)] + [
        (5 * (p - 1), 3 * p ** (j + 1)) for j in range(1, DEPTH_CUTOFF + 1)
    ]


def extend_atoms(
    atoms: dict[int, int], p: int, small: bool, first_size: int | None = None
) -> dict[int, int]:
    """Convolve retained atoms, rounding each contribution down."""
    result: dict[int, int] = {}
    for j, (numerator, denominator) in enumerate(
        factor_probabilities(p, small, first_size)
    ):
        for value, weight in atoms.items():
            product = value * (j + 1)
            if product <= PRODUCT_CUTOFF:
                lower = weight * numerator // denominator
                if lower:
                    result[product] = result.get(product, 0) + lower
    return result


def product_tail(
    primes: list[int], first_sizes: dict[int, int] | None = None
) -> tuple[int, int, int, int]:
    """Return upper losses, upper final second moment, and state diagnostics.

    All returned moment/loss integers are in units of SCALE. The supplied
    list is the complete prime list from 2 through 19997. The small-coordinate
    law is uniform on the specified number of allowed first digits and on
    every later digit. Omitted sizes default to p-1.
    """
    atoms = {1: SCALE}
    first = SCALE
    second = SCALE
    losses = 0
    first_sizes = {} if first_sizes is None else first_sizes
    for p in primes:
        if p == 2:
            continue
        if p <= 73:
            r = first_sizes.get(p, p - 1)
            atoms = extend_atoms(atoms, p, True, r)
            first = ceiling_ratio(first * (r * (p - 1) + p), r * (p - 1))
            second = ceiling_ratio(
                second * (r * (p - 1) ** 2 + p * (3 * p - 1)), r * (p - 1) ** 2
            )
            continue

        # E[(T/(p-1) - 2/5)+] = E[T]/(p-1) - E[min(T/(p-1), 2/5)].
        # Lower atom weights give a lower bound on the latter expectation;
        # the rounded full first moment accounts for every discarded atom.
        subtract = sum(
            weight * min(5 * value, 2 * (p - 1)) for value, weight in atoms.items()
        )
        losses += ceiling_ratio(5 * first - subtract, 3 * (p - 1))

        atoms = extend_atoms(atoms, p, False)
        first = ceiling_ratio(first * (3 * (p - 1) + 5), 3 * (p - 1))
        second = ceiling_ratio(
            second * (3 * (p - 1) ** 2 + 5 * (3 * p - 1)), 3 * (p - 1) ** 2
        )
    return losses, second, first, len(atoms)


def check_tail_density(
    checker: Checker,
    primes: list[int],
    log_bounds: Callable[[Fraction], tuple[Fraction, Fraction]],
) -> None:
    """Check the quarter-density tail and its exact termination margin."""
    checker.check(
        'uniform-density tail: complete prime endpoint is p_2262 = 19997',
        len(primes) == 2262 and primes[0] == 2 and primes[-1] == 19997,
    )
    # Small checks use exact rational arithmetic independently of the
    # rounding implementation, including a deliberately discarded atom.
    example = {1: SCALE // 3, 2: SCALE // 5, PRODUCT_CUTOFF: SCALE // 7}
    extended = extend_atoms(example, 3, True)
    expected: dict[int, Fraction] = {}
    for j in range(DEPTH_CUTOFF + 1):
        probability = Fraction(1, 2) if j == 0 else Fraction(1, 3**j)
        for value, weight in example.items():
            if value * (j + 1) <= PRODUCT_CUTOFF:
                product = value * (j + 1)
                expected[product] = (
                    expected.get(product, Fraction(0)) + weight * probability
                )
    checker.check(
        'atom convolution rounds down, including collisions and the product boundary',
        set(extended) == set(expected)
        and all(0 <= extended[value] <= target for value, target in expected.items())
        and sum(extended.values()) < sum(example.values()),
    )
    losses, second, _, count = product_tail(primes)
    checker.check(
        'uniform-density tail: certified total loss is below 201/1000',
        Fraction(0) < Fraction(losses, SCALE) < Fraction(201, 1000) and count > 0,
    )
    denominator = SCALE // 4 - losses
    checker.check(
        'uniform-density tail: density 1/4 gives positive mass and f_2262 < 94000',
        denominator > 0 and Fraction(second, denominator) < 94000,
    )
    log_k_lower, _ = log_bounds(Fraction(2262))
    log_log_lower, _ = log_bounds(Fraction(77, 10))
    checker.check(
        'uniform-density tail: source termination threshold exceeds 101000',
        log_k_lower > Fraction(77, 10)
        and log_log_lower > 2
        and 2262 * Fraction(67, 10) ** 2 > 101000,
    )
    forced = extend_atoms({1: SCALE}, 3, True, 1)
    checker.check(
        'one allowed first digit: no zero-depth atom and every retained weight is a lower bound',
        1 not in forced
        and all(
            Fraction(weight, SCALE) <= Fraction(2, 3 ** (value - 1))
            for value, weight in forced.items()
        ),
    )
    sizes = {p: p - 2 for p in primes if 11 <= p <= 73 and p != 17}
    sizes[3] = 1
    density = 1 - Fraction(43, 288) - Fraction(1, 324) - Fraction(1, 176)
    losses, second, _, _ = product_tail(primes, sizes)
    loss_upper = Fraction(losses, SCALE)
    checker.check(
        'density extension under adapted product measure: mass > 841/1000, loss < 417/1000, f < 21000',
        density == Fraction(24005, 28512)
        and density > Fraction(841, 1000)
        and loss_upper < Fraction(417, 1000)
        and Fraction(second, SCALE) < 21000 * (density - loss_upper),
    )
