"""Additional certified AP and equal-sum cofactor constraints.

The fixed Padé choices supplement erdos_699_ap_cofactors.py, particularly
for selected positions involving the prime 11. No binomial rows are searched.
Both the limiting-exponent margins and explicit product thresholds are
verified by directed interval arithmetic.
"""

from fractions import Fraction
import json
from math import prod
from pathlib import Path

from mpmath import iv

from erdos_699_ap_cofactors import analytic_parameters, certify
from erdos_699_bft_pair_extension import rational
from erdos_699_product_thresholds import product_bound


AP_CHOICES = (
    (2, 5, 3, 1, 11, 1, 1, 1, 43, 33, (".394", ".615", ".161")),
    (3, 5, 2, 1, 11, 2, 1, 1, 47, 39, (".857", ".433", ".011")),
    (11, 2, 2, 3, 5, 1, 1, 3, 14, 9, (".330", ".481", ".228")),
    (11, 4, 2, 6, 7, 3, 3, 2, 29, 22, (".312", ".035", ".207")),
    (3, 3, 5, 1, 11, 1, 2, 1, 3, 2, (".396", ".410", ".121")),
    (11, 3, 3, 2, 7, 2, 1, 3, 27, 20, (".442", ".012", ".087")),
    (2, 6, 3, 2, 7, 1, 1, 1, 34, 27, (".410", ".376", ".448")),
    (3, 3, 2, 2, 7, 1, 1, 1, 33, 25, (".485", ".388", ".277")),
    (7, 2, 2, 2, 3, 1, 1, 4, 15, 8, (".296", ".442", ".013")),
    (7, 4, 2, 5, 5, 2, 1, 3, 33, 25, (".429", ".469", ".359")),
    (3, 5, 5, 1, 7, 2, 1, 1, 47, 39, (".358", ".624", ".091")),
)

# Position-sum partition, seed P,Q,a,b,c,d, prime exponents, targets.
FOUR_CHOICES = (
    (((2, 11), (3, 7)), (22, 21, 1, 1, 4, 3),
     {2: 1, 3: 1, 7: 1, 11: 1}, {2: ".718", 3: ".554", 7: ".210", 11: ".027"}),
    (((2, 7), (5, 11)), (56, 55, 1, 1, 14, 11),
     {2: 3, 5: 1, 7: 1, 11: 1}, {2: ".385", 5: ".524", 7: ".424", 11: ".290"}),
    (((2, 3), (5, 11)), (3025, 432, 1, 7, 31, 21),
     {2: 4, 3: 3, 5: 2, 11: 2}, {2: ".4949", 3: ".3996", 5: ".4136", 11: ".1264"}),
    (((2, 7), (3, 11)), (99, 98, 1, 1, 5, 4),
     {2: 1, 3: 2, 7: 2, 11: 1}, {2: ".824", 3: ".442", 7: ".012", 11: ".391"}),
    (((3, 11), (5, 7)), (3267, 1225, 3, 8, 37, 22),
     {3: 3, 5: 2, 7: 2, 11: 2}, {3: ".3930", 5: ".4072", 7: ".2833", 11: ".1169"}),
)


def add_numerical_threshold(row, components):
    bound = product_bound(
        tuple(row["seed"]), rational(row["gcd_certificate"]["ell_lower"]),
        row["gcd_certificate"]["m0"], 121, components, degree=2, shift=11,
    )
    return {**row, "height_variable": "h=n-11",
            "numerical_product_bound": bound,
            "threshold_power_of_ten": bound["threshold_power_of_ten"]}


def ap_certificate(choice):
    row = certify(choice)
    middle, exponent, left, a_left, right, a_right = choice[:6]
    middle_side = 0 if row["seed"][0] == middle**exponent else 1
    targets = row["targets"]
    components = [
        (middle, exponent, 2, middle_side, targets[str(middle)]),
        (left, a_left, 1, 1-middle_side, targets[str(left)]),
        (right, a_right, 1, 1-middle_side, targets[str(right)]),
    ]
    return add_numerical_threshold(row, components)


def four_certificate(choice):
    partition, seed, powers, targets = choice
    kappa, parameters = analytic_parameters(*seed)
    margin = Fraction(1, 10000)
    alpha = {p: 1 - 2*exponent*iv.log(p)/kappa for p, exponent in powers.items()}
    for p, target in targets.items():
        assert alpha[p] - rational(margin) > rational(target)
    sides = {}
    for group in partition:
        value = prod(p**powers[p] for p in group)
        assert value in seed[:2]
        side = seed[:2].index(value)
        for p in group:
            sides[p] = side
    row = {
        "equal_position_sums": [list(group) for group in partition],
        "prime_powers": {str(p): exponent for p, exponent in powers.items()},
        "targets": {str(p): target for p, target in targets.items()},
        "exponent_margin": str(margin),
        "alpha": {str(p): iv.nstr(value, 28) for p, value in alpha.items()},
        **parameters,
    }
    components = [(p, exponent, 1, sides[p], targets[p]) for p, exponent in powers.items()]
    return add_numerical_threshold(row, components)


def cubic_certificate():
    # Z*(Z-3t)^2 - (Z-t)^2*(Z-4t) = 4*t^3.
    # Prime order at positions a,a+t,a+3t,a+4t is 11,7,3,2.
    seed = (99, 98, 1, 1, 5, 4)
    kappa, parameters = analytic_parameters(*seed)
    components = [
        (3, 2, 2, 0, ".5818"), (11, 1, 1, 0, ".0873"),
        (2, 1, 1, 1, ".736"), (7, 2, 2, 1, ".2593"),
    ]
    margin = Fraction(1, 10000)
    for prime, exponent, multiplicity, _, target in components:
        limit = 1 - 3*exponent*iv.log(prime)/(multiplicity*kappa)
        assert limit - rational(margin) > rational(target)
    bound = product_bound(
        seed, rational(parameters["gcd_certificate"]["ell_lower"]),
        parameters["gcd_certificate"]["m0"], 4*11**3,
        components, degree=3, shift=11,
    )
    return {
        "position_primes": [11, 7, 3, 2],
        "position_offsets": [0, 1, 3, 4],
        "nonzero_integer_step_required": True,
        "targets": {str(p): target for p, _, _, _, target in components},
        "exponent_margin": str(margin),
        **parameters,
        "height_variable": "h=n-11",
        "numerical_product_bound": bound,
        "threshold_power_of_ten": bound["threshold_power_of_ten"],
    }


def report():
    aps = [ap_certificate(choice) for choice in AP_CHOICES]
    fours = [four_certificate(choice) for choice in FOUR_CHOICES]
    cubics = [cubic_certificate()]
    return {
        "source": "BFT Section 7, the retained explicit GCD estimate, and the quadratic-product lemma",
        "scope": "Conditional on the stated AP, equal-sum, or cubic position relation; no whole-index claim.",
        "maximum_position": 11,
        "maximum_product_gap": 4*11**3,
        "choices": aps,
        "four_factor_choices": fours,
        "cubic_product_choices": cubics,
        "common_input_threshold_power_of_ten": max(row["threshold_power_of_ten"] for row in aps+fours+cubics),
    }


if __name__ == "__main__":
    result = report()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "AP_constraints": len(result["choices"]),
        "equal_sum_constraints": len(result["four_factor_choices"]),
        "cubic_product_constraints": len(result["cubic_product_choices"]),
        "common_input_threshold_power_of_ten": result["common_input_threshold_power_of_ten"],
    }, indent=2))
