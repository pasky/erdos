"""Exact finite calculations for the two-root switching trap.

The graph is the Clebsch graph on even subsets of [5] in increasing binary
order, the old colouring is mask 831, and each supported edge is retained
independently with probability 7/8. Root entries name template parts; equal
entries mean distinct sampled vertices in one part, not the same vertex.

For k roots, P[i,c] is 8**k times the probability that a vertex in part i
has coloured profile c. The matrix Q = 7 P.T signed(A) P represents the
expected switching gain, with denominator 16**2 * 8**(2*k+1), in the
convention edges / N**2. All two-root switches, modulo complementation,
are checked for every ordered template-part pair. A specified three-root
move is checked directly, without repeating its discovery.

The finite existence argument using concentration is on the owning research
page. These tables do not exhibit a graph counterexample to Problem 23.
Only integer arrays and Fraction arithmetic carry the checks. The largest
two-term matrix evaluation used here is bounded by
2 * 7 * 80 * 8**6 < 2**29, so signed int64 arithmetic cannot overflow.
The gain weighted by a squared cell mass is accumulated in Python integers
after converting each factor; that larger sum does not use fixed-width arithmetic.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product

import numpy as np

from tools import Checker


def template() -> tuple[np.ndarray, np.ndarray]:
    """Build the specified graph and colouring from their definitions."""
    vertices = [v for v in range(32) if v.bit_count() % 2 == 0]
    adjacency = np.array(
        [[int((u ^ v).bit_count() == 4) for v in vertices] for u in vertices],
        dtype=np.int64,
    )
    colours = np.array([(831 >> i) & 1 for i in range(16)], dtype=np.int64)
    return adjacency, colours


def profile_numerators(
    adjacency: np.ndarray,
    colours: np.ndarray,
    roots: tuple[int, ...],
    retained: int,
    denominator: int,
) -> np.ndarray:
    """Independent root-edge probabilities with a common integer denominator."""
    k = len(roots)
    result = np.zeros((16, 2 << k), dtype=np.int64)
    for bits in product((0, 1), repeat=k):
        probability = np.ones(16, dtype=np.int64)
        profile = 0
        for j, (root, bit) in enumerate(zip(roots, bits)):
            profile += bit << j
            probability *= np.where(
                adjacency[:, root],
                retained if bit else denominator - retained,
                0 if bit else denominator,
            )
        result[np.arange(16), colours + 2 * profile] = probability
    return result


def gain_numerators(signed: np.ndarray, probabilities: np.ndarray,
                    switches: np.ndarray, retained: int) -> np.ndarray:
    """Expected unordered-edge gain, before the common denominator."""
    matrix = retained * (probabilities.T @ signed @ probabilities)
    return switches @ matrix.sum(axis=1) - ((switches @ matrix) * switches).sum(axis=1)


def switching_trap_clauses(checker: Checker) -> None:
    """Check the finite table, escape move, and explicit concentration constants."""
    adjacency, colours = template()
    signed = adjacency * np.where(colours[:, None] == colours[None, :], -1, 1)
    mono = int((adjacency * (colours[:, None] == colours[None, :])).sum() // 2)
    checker.check(
        'switching trap: the defined template is triangle-free, 5-regular, with 40 edges',
        bool(np.array_equal(adjacency, adjacency.T) and not adjacency.trace()
             and np.all(adjacency.sum(axis=1) == 5)
             and not np.any((adjacency @ adjacency) * adjacency)),
    )
    checker.check(
        'switching trap: mask 831 has 12 monochromatic edges and vertex slacks 1 or 5',
        mono == 12 and sorted(signed.sum(axis=1).tolist()) == [1] * 12 + [5] * 4,
    )
    q = Fraction(7, 8)
    density = 2 * q * 40 / 16**2
    mono_density = q * mono / 16**2
    checker.check(
        'switching trap: p = 35/128 lies in the band and M/N^2 = 21/512 exceeds 1/25',
        density == Fraction(35, 128)
        and Fraction(1243, 5000) < density < Fraction(3197, 10000)
        and mono_density == Fraction(21, 512) > Fraction(1, 25),
    )

    # The final cell is fixed at zero; complementing every switch bit leaves
    # the resulting cut cost unchanged. Thus these are all 256 switches up
    # to the sole symmetry used here.
    switches = ((np.arange(128)[:, None] >> np.arange(8)) & 1).astype(np.int64)
    least = None
    relation_minima: dict[tuple[int, int, int], int] = {}
    count = 0
    nontrivial_count = 0
    mass_ok = True
    trivial_ok = True
    for roots in product(range(16), repeat=2):
        probabilities = profile_numerators(adjacency, colours, roots, 7, 8)
        mass_ok &= bool(np.all(probabilities.sum(axis=1) == 64))
        values = gain_numerators(signed, probabilities, switches, 7)
        possible = np.flatnonzero(probabilities.sum(axis=0) > 0)
        nontrivial = np.any(
            switches[:, possible] != switches[:, possible[0]][:, None], axis=1,
        )
        trivial_ok &= bool(np.all(values[~nontrivial] == 0))
        minimum = int(values[nontrivial].min())
        least = minimum if least is None else min(least, minimum)
        relation = (int(roots[0] == roots[1]), int(adjacency[roots]),
                    int(colours[roots[0]] == colours[roots[1]]))
        relation_minima[relation] = min(minimum, relation_minima.get(relation, minimum))
        count += len(values)
        nontrivial_count += int(nontrivial.sum())
    expected = {
        (0, 0, 0): 6272,
        (0, 0, 1): 6272,
        (0, 1, 0): 12544,
        (0, 1, 1): 50176,
        (1, 0, 1): 6272,
    }
    delta = Fraction(49, 65536)
    checker.check(
        'switching trap: all 32768 pair/switch cases, including 31796 nontrivial ones, '
        'have the stated exact minima',
        mass_ok and trivial_ok and count == 32768 and nontrivial_count == 31796
        and relation_minima == expected and least == 6272
        and Fraction(6272, 16**2 * 8**5) == delta,
        f'least numerator {least}; relation minima {relation_minima}',
    )
    probabilities = profile_numerators(adjacency, colours, (0, 6), 7, 8)
    attaining = int(gain_numerators(signed, probabilities, switches[16:17], 7)[0])
    checker.check('switching trap: roots (0,6), switch mask 16 attain 49/65536',
                  Fraction(attaining, 16**2 * 8**5) == delta)

    # At retention one the specified bad cut really does have an improving
    # two-root switch. This detects a gain formula detached from the retention
    # probability or from the chosen switch.
    probabilities = profile_numerators(adjacency, colours, (2, 4), 1, 1)
    control = int(gain_numerators(signed, probabilities, switches, 1).min())
    checker.check('switching trap negative control: retention one admits gain -1/256',
                  Fraction(control, 16**2) == Fraction(-1, 256))

    probabilities = profile_numerators(adjacency, colours, (2, 2, 4), 7, 8)
    move = np.array([[(424 >> i) & 1 for i in range(16)]], dtype=np.int64)
    escape = Fraction(int(gain_numerators(signed, probabilities, move, 7)[0]),
                      16**2 * 8**7)
    after = mono_density + escape
    checker.check(
        'switching trap: the specified three-root move has gain -931/524288 '
        'and cost 20573/524288 < 1/25',
        bool(np.all(probabilities.sum(axis=1) == 512))
        and escape == Fraction(-931, 524288)
        and after == Fraction(20573, 524288) < Fraction(1, 25),
    )
    checker.check('switching trap: int64 intermediate bound is below 2^29',
                  2 * 7 * 80 * 8**6 < 2**29)

    # An order-seven row that actually separates the limiting trap. The roots
    # have colours (1,0,0), with only the edge between roots 1 and 2. Switch
    # cells 1,6,10, and weight the gain by the square of the mass of vertices
    # adjacent to none of the roots. The density convention doubles the
    # unordered gain used in gain_numerators.
    weighted_numerator = 0
    placements = 0
    weighted_switch = np.array([[(1090 >> i) & 1 for i in range(16)]], dtype=np.int64)
    for roots in product(range(16), repeat=3):
        if tuple(int(colours[r]) for r in roots) != (1, 0, 0):
            continue
        root_weight = 1
        for (i, j), edge in (((0, 1), 0), ((0, 2), 0), ((1, 2), 1)):
            supported = bool(adjacency[roots[i], roots[j]])
            root_weight *= (7 if edge else 1) if supported else (0 if edge else 8)
        if root_weight == 0:
            continue
        probabilities = profile_numerators(adjacency, colours, roots, 7, 8)
        gain = int(gain_numerators(signed, probabilities, weighted_switch, 7)[0])
        zero_mass = int(probabilities[:, :2].sum())
        weighted_numerator += int(root_weight) * gain * zero_mass**2
        placements += 1
    weighted_gain = Fraction(2 * weighted_numerator, 16**7 * 8**16)
    checker.check(
        'switching trap: the three-root gain times squared non-neighbour mass '
        'has exact density value -164741871/2^47',
        placements == 96 and weighted_gain == Fraction(-164741871, 2**47) < 0,
    )

    # These rational inequalities justify the explicit order in the prose
    # concentration argument. The exponential estimate itself is proved there.
    order = 2**32
    part = order // 16
    eta = Fraction(1, 25) - after
    checker.check(
        'switching trap: N = 2^32 satisfies every stated concentration threshold',
        order % 16 == 0 and order >= 8 / delta and order >= 12 / eta and eta > delta
        and delta**2 * order / 18 > 128
        and eta**2 * order / 26 > 64
        and q**2 * order / 128 > 64
        and Fraction(169 * part**2, 15000) > 64
        and Fraction(1987**2 * part**2, 20 * 625**2) > 64
        and Fraction(1, 2**57) + Fraction(1, 2**32)
        + 3 * Fraction(1, 2**64) < 1,
    )
