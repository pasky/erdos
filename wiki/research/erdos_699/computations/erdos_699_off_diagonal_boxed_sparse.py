"""Exact sparse Pade witnesses for an explicit box of cofactor targets.

Unlike a positive-part clause, the target box gives each denominator
contribution separately. There is no restriction m<=t*log(h).
All endpoint checks after directed preparation use rational arithmetic.
"""

from fractions import Fraction as F
from itertools import combinations

from erdos_699_off_diagonal_sparse_witness import (
    SCALE,
    _upper_numerators,
    _upper_scaled,
    prepare_witness,
)
from mpmath import iv


def prepare_box(certificate, targets, *, source_id, gap, maximum_shift):
    base = prepare_witness(
        certificate,
        source_id=source_id,
        threshold_weakening=0,
        gap=gap,
        maximum_shift=maximum_shift,
    )
    targets = {int(p): F(value) for p, value in targets.items()}
    source = certificate["source"]
    components = certificate["components"]
    assert set(targets) == {p for p, power, multiplicity, side in components}
    terms = []
    for p, power, multiplicity, side in components:
        target = targets[p]
        assert 0 <= target < 1
        length = source["left_block"] if side == 0 else source["right_block"]
        kappa = _upper_scaled(length * power * iv.log(p))
        terms.append((p, kappa, multiplicity * (1 - target)))
    # Sum of positive parts = maximum over all subset sums.
    lines = []
    for size in range(len(terms) + 1):
        for subset in combinations(terms, size):
            lines.append(
                {
                    "primes": [p for p, kappa, weight in subset],
                    "index_coefficient_upper_scaled": sum(
                        kappa for p, kappa, weight in subset
                    ),
                    "height_weight": str(
                        sum((weight for p, kappa, weight in subset), F(0))
                    ),
                }
            )
    difference = (
        base["intrinsic_second_rate_lower_scaled"]
        - base["intrinsic_first_rate_lower_scaled"]
    )
    assert difference > 0
    base.update(
        {
            "method": "direct-target-box-v1",
            "box_targets": {str(p): str(e) for p, e in sorted(targets.items())},
            "denominator_cost_lines": lines,
            "zero_cost_index_per_log_height": [
                str(weight * SCALE / kappa) for p, kappa, weight in terms
            ],
            # Proposals only: the chosen integer is verified independently.
            "balanced_index_per_log_height": str(
                F(base["product_degree"] * SCALE, difference)
            ),
            "balanced_index_offset": str(
                F(
                    base["second_doubled_log_prefactor_upper_scaled"]
                    - base["first_doubled_log_prefactor_upper_scaled"],
                    difference,
                )
            ),
        }
    )
    return base


def index_proposals(prepared, left):
    """A short deterministic list; nearby indices can have better gcds."""
    assert type(left) is int and left > 0
    values = [
        F(prepared["balanced_index_per_log_height"]) * left
        + F(prepared["balanced_index_offset"])
    ]
    values.extend(F(rate) * left for rate in prepared["zero_cost_index_per_log_height"])
    values.append(F(prepared["block_parameter"]) * left)
    result = []
    for value in values:
        center = value.numerator // value.denominator
        for offset in (0, -1, 1, -2, 2):
            m = center + offset
            if m >= 2 and m not in result:
                result.append(m)
    return result


def verify_window(prepared, m, left, right, log_gcd_lower_scaled):
    """Prove failure of the box for every natural logarithmic height in [left,right]."""
    if not (type(left) is int and type(right) is int and 0 < left < right):
        return False
    first, second = _upper_numerators(prepared, m, log_gcd_lower_scaled)
    degree = prepared["product_degree"]
    for line in prepared["denominator_cost_lines"]:
        weight = F(line["height_weight"])
        index_part = line["index_coefficient_upper_scaled"] * m
        # Every cost line decreases with height, so the first term needs
        # only the left endpoint. The second term is a maximum of lines.
        if not first * weight.denominator > (
            index_part * weight.denominator - SCALE * weight.numerator * left
        ):
            return False
        slope = F(degree) - weight
        for x in (left, right):
            if not second * slope.denominator > (
                index_part * slope.denominator + SCALE * slope.numerator * x
            ):
                return False
    return True


def window_right(prepared, m, left, log_gcd_lower_scaled):
    """Largest integer right endpoint certified by this fixed index."""
    first, second = _upper_numerators(prepared, m, log_gcd_lower_scaled)
    degree = prepared["product_degree"]
    bounds = []
    for line in prepared["denominator_cost_lines"]:
        weight = F(line["height_weight"])
        index_part = line["index_coefficient_upper_scaled"] * m
        if first * weight.denominator <= (
            index_part * weight.denominator - SCALE * weight.numerator * left
        ):
            return left
        slope = F(degree) - weight
        if second * slope.denominator <= (
            index_part * slope.denominator + SCALE * slope.numerator * left
        ):
            return left
        if slope > 0:
            bounds.append(
                ((second - index_part) * slope.denominator - 1)
                // (SCALE * slope.numerator)
            )
    assert bounds  # The empty subset has positive slope degree.
    result = min(bounds)
    if result > left:
        assert verify_window(prepared, m, left, result, log_gcd_lower_scaled)
    return result
