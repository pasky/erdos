"""An effective three-cofactor restriction from the seed 49-48=1.

This certifies a fixed rational upper cofactor box using unequal Pade
blocks. The starting height is effective, but not numerically evaluated.
"""

from fractions import Fraction
import json
from pathlib import Path

from mpmath import iv

from erdos_699_off_diagonal_pade import growth_parameters, rational


def main():
    c0, k0, record = growth_parameters(
        49, 48, 1, 1, 49, 12, 20, Fraction(5), terms=200,
    )
    block = Fraction(29, 4000)
    targets = {2: Fraction(36, 100), 3: Fraction(19, 100),
               7: Fraction(15, 100)}
    components = [(7, 2, 2, 61), (2, 4, 1, 32), (3, 1, 1, 32)]
    delta = iv.mpf(0)
    for p, exponent, multiplicity, side_block in components:
        term = (rational(block) * side_block * exponent * iv.log(p)
                - multiplicity * (1 - rational(targets[p])))
        assert term > 0 or term < 0
        if term > 0:
            delta += term
    first = rational(block) * c0 - delta
    second = rational(block) * k0 - delta - 2
    assert first > rational(Fraction(47, 1000))
    assert second > rational(Fraction(47, 1000))
    record.update({
        "scope": "AP positions r2+r3=2*r7 with r2!=r3; effective, unevaluated threshold.",
        "product_degree": 2,
        "position_relation": {"middle_prime": 7, "endpoint_primes": [2, 3]},
        "left_prime_powers": {"7": 2},
        "right_prime_powers": {"2": 4, "3": 1},
        "components": components,
        "targets": {str(p): str(t) for p, t in targets.items()},
        "block_parameter": str(block),
        "denominator_cost": iv.nstr(delta, 35),
        "first_margin": iv.nstr(first, 35),
        "second_margin": iv.nstr(second, 35),
        "strict_margin": "47/1000",
        "conclusion": "u2>h^.36 or u3>h^.19 or u7>h^.15 above an effective height.",
    })
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"output": str(output),
                      "first_margin": record["first_margin"],
                      "second_margin": record["second_margin"]}))


if __name__ == "__main__":
    main()
