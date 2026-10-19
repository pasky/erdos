"""Exact unequal-block Padé cofactor constraints for the primes two and three.

The thresholds are effective and are not numerically evaluated.  This checks
finite rational prime intervals and outward-rounded analytic inequalities;
it does not enumerate binomial rows.
"""
from fractions import Fraction
import json
from pathlib import Path

from mpmath import iv

from erdos_699_off_diagonal_pade import growth_parameters, rational


CHOICES = [
    ((11, 10, 40), "5.03", ("0.02", "0.56")),
    ((6, 5, 18), "2.658", ("0.05", "0.52")),
    ((49, 22, 49), "20.913", ("0.329", "0.291")),
    ((21, 6, 7), "3.246", ("0.55", "0.025")),
]


def certify():
    records = []
    for (A, B, C), ell, endpoints in CHOICES:
        _, k0, record = growth_parameters(9, 8, 1, 1, A, B, C, ell, terms=1000)
        alpha = {2: 1 - (B + C) * iv.log(8) / k0,
                 3: 1 - (A + B) * iv.log(9) / k0}
        targets = {p: Fraction(t) for p, t in zip((2, 3), endpoints)}
        for p in (2, 3):
            assert alpha[p] > rational(targets[p] + Fraction(1, 10000))
        record.update({
            "pair": [2, 3],
            "targets": {str(p): str(targets[p]) for p in (2, 3)},
            "limiting_exponents": {str(p): iv.nstr(alpha[p], 35) for p in (2, 3)},
            "strict_margin": "1/10000",
            "conclusion": "u > h^target[2] or v > h^target[3]",
        })
        records.append(record)
    return {
        "scope": "For every fixed D, h=min(2^a*u,3^b*v) above an effective threshold and 0<|2^a*u-3^b*v|<=D.",
        "records": records,
        "minimal_vectors": [
            ["0", "14/25"], ["1/50", "13/25"],
            ["1/20", "291/1000"], ["329/1000", "1/40"],
            ["11/20", "0"],
        ],
    }


def main():
    result = certify()
    vectors = [(Fraction(0), Fraction(0))]
    for record in result["records"]:
        left, right = (Fraction(record["targets"][str(p)]) for p in (2, 3))
        candidates = set()
        for x, y in vectors:
            if x >= left or y >= right:
                candidates.add((x, y))
            else:
                candidates.update(((left, y), (x, right)))
        vectors = [v for v in sorted(candidates)
                   if not any(w != v and all(a <= b for a, b in zip(w, v))
                              for w in candidates)]
    assert vectors == [tuple(map(Fraction, v)) for v in result["minimal_vectors"]]
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"certified_sources": len(result["records"]),
                      "minimal_vectors": result["minimal_vectors"]}, indent=2))


if __name__ == "__main__":
    main()
