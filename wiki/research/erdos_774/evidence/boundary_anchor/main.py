"""Check the exact boundary-anchor certificate for the Grow deletion.

Input and range: the fixed 14-element source A, all 2**14 source subsets,
all proper two-color classes, and the 83 three-coloring templates held in
``assets/boundary_anchor_certificate.json``. All six ray permutations of
each template are included, giving 498 proper colorings in the
symmetry-expanded witness family. There are exactly 12,730 nonzero
universal-anchor orbits, and every one must be excluded. A second
ordinary-set implementation independently rechecks every coloring and one
exclusion per candidate. Arithmetic is exact Python integer and bitset
arithmetic; the run performs no search.

Run from the repository root:
    uv run --no-sync python wiki/research/erdos_774/evidence/boundary_anchor/main.py

Dependencies are the standard library and the installed root ``tools``
package. The only input is the certificate asset beside this script; no
output file is written and there is no reduced mode. Expected runtime is
under a few seconds. Failed obligations exit nonzero, including under
``python -O``. The mathematical reading of each clause is on the owning
page, ``_index.md`` beside this script.

Simplex rays are t1=(1,0), t2=(0,1), t3=(-1,-1). A coloring is stored as
three layer rows of three masks. Its color c is dissociated exactly when
its three source masks are dissociated and their signed-sum sets meet
only at zero. Its signed span contains (x,y) exactly when some signed sum
a from layer 3 has a+x in layer 1's signed span and a+y in layer 2's.
"""

from __future__ import annotations

import json
import pathlib
import sys
from itertools import permutations

import tools

__all__ = [
    'main',
]

# locate the retained certificate relative to this script
_ASSET = pathlib.Path(__file__).with_name('assets') / 'boundary_anchor_certificate.json'

# fix the source set and the counts the certificate must reproduce
_SOURCE = [4, 5, 9, 11, 13, 27, 30, 33, 81, 85, 89, 243, 248, 253]
_TWO_COLOR_CLASSES = 56
_UNIVERSAL_SPAN_SIZE = 501
_CANDIDATE_ORBITS = 12_730
_TEMPLATES = 83


def _ray_orbit(point: tuple[int, int]) -> tuple[tuple[int, int], ...]:
    """Return all six ray permutations; signed spans absorb the overall sign."""
    x, y = point
    return ((x, y), (y, x), (-x, y - x), (y - x, -x), (-y, x - y), (x - y, -y))


def _shift(bits: int, distance: int) -> int:
    """Shift a signed-sum bitset by a signed distance."""
    return bits << distance if distance >= 0 else bits >> -distance


def main() -> int:
    """Run every finite obligation and return the shared checker's exit code."""
    # parse the fixed-domain interface and load the retained certificate
    parser = tools.evidence_parser(
        'Check the Grow-deletion boundary-anchor certificate.', quick=False
    )
    parser.parse_args()
    checker = tools.Checker()
    data = json.loads(_ASSET.read_text())
    source = data['A']
    checker.check('certificate source set is the fixed Grow deletion', source == _SOURCE)
    count = 1 << len(source)
    full = count - 1
    offset = sum(source)
    zero = 1 << offset

    # tabulate dissociation, subset sums and signed sums for every source mask
    independent = [False] * count
    independent[0] = True
    subset_bits = [0] * count
    subset_bits[0] = 1
    signed_bits = [0] * count
    signed_bits[0] = zero
    for mask in range(1, count):
        bit = mask & -mask
        value = source[bit.bit_length() - 1]
        smaller = mask ^ bit
        if independent[smaller] and not (subset_bits[smaller] & (subset_bits[smaller] << value)):
            independent[mask] = True
            subset_bits[mask] = subset_bits[smaller] | (subset_bits[smaller] << value)
        signed_bits[mask] = (
            signed_bits[smaller]
            | (signed_bits[smaller] << value)
            | (signed_bits[smaller] >> value)
        )

    # collect the proper two-color classes and the source universal span
    two_color_classes = [
        mask for mask in range(count) if independent[mask] and independent[full ^ mask]
    ]
    checker.check('the full source is not dissociated', not independent[full])
    checker.check(
        'exactly 56 proper two-color classes',
        len(two_color_classes) == data['expected_source_two_color_classes'] == _TWO_COLOR_CLASSES,
        f'observed {len(two_color_classes)}',
    )
    universal_bits = signed_bits[two_color_classes[0]]
    for mask in two_color_classes:
        universal_bits &= signed_bits[mask]
    checker.check(
        'source universal signed span has 501 members including zero',
        universal_bits.bit_count() == data['expected_source_universal_span_size'] == _UNIVERSAL_SPAN_SIZE,
        f'observed {universal_bits.bit_count()}',
    )
    checker.check('the source anchor 3 lies in the universal span', bool(universal_bits & (1 << (offset + 3))))

    # reduce universal vectors to the canonical nonzero candidate orbits
    universal_values = {
        value for value in range(-offset, offset + 1) if universal_bits & (1 << (offset + value))
    }
    candidates = {
        (x, y)
        for x in universal_values
        for y in universal_values
        if x > 0 and 0 <= 2 * y <= x and x - y in universal_values
    }
    checker.check(
        'exactly 12,730 nonzero candidate orbits',
        len(candidates) == data['expected_nonzero_candidate_orbits'] == _CANDIDATE_ORBITS,
        f'observed {len(candidates)}',
    )

    def contains(coloring: list, color: int, x: int, y: int) -> bool:
        """Intersect possible a1=a3+x, a2=a3+y using a common bit origin."""
        return bool(
            signed_bits[coloring[0][color]]
            & _shift(signed_bits[coloring[1][color]], x - y)
            & _shift(signed_bits[coloring[2][color]], x)
        )

    def proper(coloring: list) -> bool:
        """Decide whether three layer rows form a proper dissociated three-coloring."""
        if len(coloring) != 3:
            return False
        for row in coloring:
            if len(row) != 3 or not all(0 <= mask < count and independent[mask] for mask in row):
                return False
            if row[0] | row[1] | row[2] != full:
                return False
            if row[0] & row[1] or row[0] & row[2] or row[1] & row[2]:
                return False
        return all(
            (signed_bits[coloring[0][color]] & signed_bits[coloring[1][color]] & signed_bits[coloring[2][color]]) == zero
            for color in range(3)
        )

    # check every template, its palette bridge and all ray permutations
    colorings = data['witnesses']
    checker.check('exactly 83 templates supplied', len(colorings) == _TEMPLATES, f'observed {len(colorings)}')
    ray_permutations = tuple(permutations(range(3)))
    proper_count = bridge_count = 0
    failures: list[str] = []
    for index, coloring in enumerate(colorings):
        if not proper(coloring):
            failures.append(f'template {index} is not a proper coloring')
            continue
        if coloring[1][2] != 0:
            failures.append(f'template {index} has a nonempty middle color-3 mask')
            continue
        q, q_prime = coloring[0][2], coloring[2][2]
        if q not in two_color_classes or q_prime not in two_color_classes:
            failures.append(f'template {index} outer color-3 masks are not two-color classes')
            continue
        bridge = ((full ^ q, 0, q), tuple(coloring[1]), (0, full ^ q_prime, q_prime))
        if not proper(bridge) or any(bridge[layer][2] != coloring[layer][2] for layer in range(3)):
            failures.append(f'template {index} has no proper palette bridge')
            continue
        for ray_permutation in ray_permutations:
            permuted_coloring = tuple(coloring[layer] for layer in ray_permutation)
            permuted_bridge = tuple(bridge[layer] for layer in ray_permutation)
            if not proper(permuted_coloring) or not proper(permuted_bridge):
                failures.append(f'template {index} permutation {ray_permutation} is improper')
                break
            if any(permuted_bridge[layer][2] != permuted_coloring[layer][2] for layer in range(3)):
                failures.append(f'template {index} permutation {ray_permutation} loses its bridge')
                break
            # relabel the permuted bridge into the fixed palette family
            target_omissions = (1, 2, 0)
            old_to_new = {}
            for row, new_color in zip(permuted_bridge, target_omissions):
                omitted = [color for color in range(3) if row[color] == 0]
                if len(omitted) != 1:
                    break
                old_to_new[omitted[0]] = new_color
            if set(old_to_new) != {0, 1, 2} or set(old_to_new.values()) != {0, 1, 2}:
                failures.append(f'template {index} permutation {ray_permutation} has no relabeling')
                break
            fixed_palette = [[0, 0, 0] for _ in range(3)]
            for layer, row in enumerate(permuted_bridge):
                for old_color, mask in enumerate(row):
                    fixed_palette[layer][old_to_new[old_color]] = mask
            if not proper(fixed_palette) or not all(
                row[omitted] == 0 and all(mask in two_color_classes for mask in row if mask)
                for row, omitted in zip(fixed_palette, target_omissions)
            ):
                failures.append(f'template {index} permutation {ray_permutation} leaves the palette family')
                break
            proper_count += 1
            bridge_count += 1
    checker.check(
        'all 83 templates, their bridges and all ray permutations are proper',
        not failures and proper_count == bridge_count == 6 * _TEMPLATES,
        failures[0] if failures else f'observed {proper_count} colorings',
    )

    # exclude every candidate orbit by some template, color and ray image
    remaining = set(candidates)
    exclusions = []
    for index, coloring in enumerate(colorings):
        removed = []
        for point in remaining:
            omitted = next(
                ((color, x, y) for color in range(3) for x, y in _ray_orbit(point) if not contains(coloring, color, x, y)),
                None,
            )
            if omitted is not None:
                removed.append(point)
                exclusions.append((point, index, omitted))
        remaining.difference_update(removed)
    checker.check('every candidate orbit is excluded', not remaining, f'{len(remaining)} survivors')
    checker.check('one exclusion recorded per candidate', len(exclusions) == len(candidates))

    # recheck the colorings and exclusions with ordinary integer sets
    used_masks = set(two_color_classes)
    used_masks.update(mask for coloring in colorings for row in coloring for mask in row)
    signed_sets = {}
    subset_failures = 0
    for mask in used_masks:
        subset_sums = {0}
        signed_sums = {0}
        for i, value in enumerate(source):
            if mask & (1 << i):
                new_subset_sums = {s + value for s in subset_sums}
                if subset_sums & new_subset_sums:
                    subset_failures += 1
                subset_sums |= new_subset_sums
                signed_sums = signed_sums | {s + value for s in signed_sums} | {s - value for s in signed_sums}
        signed_sets[mask] = signed_sums
    checker.check('every used mask is dissociated by ordinary subset sums', subset_failures == 0)
    checker.check(
        'ordinary-set universal span agrees with the bitset span',
        set.intersection(*(signed_sets[mask] for mask in two_color_classes)) == universal_values,
    )
    checker.check(
        'every template color has zero ordinary-set span intersection',
        all(
            set.intersection(*(signed_sets[row[color]] for row in coloring)) == {0}
            for coloring in colorings
            for color in range(3)
        ),
    )
    recheck_failures = 0
    for point, index, (color, x, y) in exclusions:
        if (x, y) not in _ray_orbit(point):
            recheck_failures += 1
            continue
        first, second, third = (signed_sets[row[color]] for row in colorings[index])
        if any(a + x in first and a + y in second for a in third):
            recheck_failures += 1
    checker.check('every recorded exclusion holds with ordinary sets', recheck_failures == 0, f'{recheck_failures} failures')
    print(
        f'source subsets checked: {count}; two-color classes: {len(two_color_classes)}; '
        f'universal span: {len(universal_values)}; candidate orbits: {len(candidates)}; '
        f'templates: {len(colorings)}'
    )
    return checker.finish()


if __name__ == '__main__':
    sys.exit(main())
