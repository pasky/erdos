"""Explicit asymmetric cofactor bounds from BFT Section 7.

This retains the two seed prime-power logarithms separately and avoids
the final symmetric maximum in BFT Theorem 2.4. See the accompanying
../methods/details/asymmetric_cofactors.md for the threshold proof.
"""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path

from mpmath import iv

from erdos_699_bft_explicit_thresholds import explicit_bound, interval_max
from erdos_699_bft_pair_extension import rational
from erdos_699_prime_pair_savings import EXPLICIT_EDGES
from erdos_699_weighted_ramps import capacities, exact_power_of_ten, off_maximum_constant


iv.dps = 80


def asymmetric_bound(p_power, q_power, a, b, c, d, log_l1, m0,
                     gap, target_p, target_q):
    """Certify u>x**target_p OR v>x**target_q for bounded-gap inputs.

    The p and q labels follow the oriented seed powers, not sorted primes.
    x is the minimum of the two inputs. log_l1 and m0 must certify BFT
    (2.8). The returned integer B guarantees the assertion for x>=10**B.
    """
    target_p, target_q = Fraction(target_p), Fraction(target_q)
    assert 0 < target_p < 1 and 0 < target_q < 1
    # Kappas do not depend on epsilon; this call reuses their exact integrals.
    data = explicit_bound(p_power, q_power, a, b, c, d,
                          log_l1, m0, gap, Fraction(1, 100))
    log_p, log_q = iv.log(p_power), iv.log(q_power)
    s = rational(Fraction(c, d))
    k = iv.log(max(p_power, q_power)) + data["log_omega4"] / s
    l = interval_max([
        log_p / (1 - rational(target_p)),
        log_q / (1 - rational(target_q)),
    ])
    assert l < k
    m = interval_max([
        iv.mpf(m0), iv.log(data["kappa1"]) / (d*data["log_omega3"]),
    ])
    terms = [
        iv.log(gap),
        c*l*(m + 1),
        l*(c*k + iv.log(2) - iv.log(data["kappa2"])) / (k - l),
    ]
    threshold = interval_max(terms)
    cap = int(float((threshold / iv.log(10)).b)) + 1
    while not threshold < cap*iv.log(10):
        cap += 1
    return {
        "seed": [p_power, q_power, a, b, c, d],
        "gap": gap,
        "m0": m0,
        "targets": [str(target_p), str(target_q)],
        "limiting_exponents": [iv.nstr(1 - log_p/k, 24),
                               iv.nstr(1 - log_q/k, 24)],
        "log_omega3": iv.nstr(data["log_omega3"], 24),
        "log_omega4": iv.nstr(data["log_omega4"], 24),
        "kappa1": iv.nstr(data["kappa1"], 24),
        "kappa2": iv.nstr(data["kappa2"], 24),
        "K": iv.nstr(k, 24), "L": iv.nstr(l, 24),
        "M": iv.nstr(m, 24),
        "log_threshold_terms": [iv.nstr(term, 24) for term in terms],
        "log_threshold": iv.nstr(threshold, 24),
        "threshold_power_of_ten": cap,
    }


def main():
    choices = [
        ((5, 7), (25, 49, 2, 1, 8, 5), "1.5407", 53, ".29", ".20"),
        ((5, 7), (25, 49, 2, 1, 8, 5), "1.5407", 53, ".35", ".22"),
        ((5, 7), (25, 49, 2, 1, 8, 5), "1.5407", 53, ".35", ".20"),
        ((2, 7), (8, 7, 1, 1, 3, 2), "1.5395", 138, ".24", ".29"),
    ]
    rows = []
    for pair, seed, l1, m0, target_p, target_q in choices:
        result = asymmetric_bound(
            *seed, iv.log(rational(l1)), m0, 100, target_p, target_q,
        )
        rows.append({"pair": pair, "L1": l1, **result})
    primes = (2, 3, 5, 7)
    positions = {p: k for k, p in enumerate(primes)}
    edges = [
        (positions[p], positions[q], Fraction(w, 10000), Fraction(w, 10000))
        for p, q, w in EXPLICIT_EDGES if p in positions and q in positions
    ] + [(positions[5], positions[7], Fraction(29, 100), Fraction(1, 5))]
    gains = []
    configurations = 0
    for choices in range(1 << len(edges)):
        values = [Fraction(0)]*4
        for bit, (p, q, target_p, target_q) in enumerate(edges):
            vertex, value = ((q, target_q) if choices & (1 << bit)
                             else (p, target_p))
            values[vertex] = max(values[vertex], value)
        scaled = tuple(int(10000*value) for value in values)
        for caps in capacities(scaled):
            configurations += 1
            gains.append(43 - sum(Fraction((14 - r)*value, 10000)
                                  for r, value in enumerate(caps)))
    gain = min(gains)
    assert gain == Fraction(13, 125)
    off_maximum, factors = off_maximum_constant(11, [14 - t for t in range(11)], primes)
    constant = Fraction(1000*11**14*off_maximum, 999*2**56)
    cap = exact_power_of_ten(constant, gain, 945000)
    assert cap == 711
    result = {
        "source": "BFT Section 7 before taking the symmetric maximum",
        "scope": "Numerical analytic parameters; no binomial rows enumerated.",
        "pairs": rows,
        "index_11": {
            "orientations_checked": 1 << len(edges),
            "capacity_configurations_checked": configurations,
            "minimum_weighted_gain": str(gain),
            "off_maximum_factors": factors,
            "elementary_threshold": 945000,
            "comparison_constant": str(constant),
            "algebraic_cap_power_of_ten": cap,
            "full_row_cap_power_of_ten": max(cap, rows[0]["threshold_power_of_ten"] + 1),
        },
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "certificates": [{"pair": row["pair"], "targets": row["targets"],
                          "threshold_power_of_ten": row["threshold_power_of_ten"]}
                         for row in rows],
        "index_11": result["index_11"],
        "output": str(output),
    }, indent=2))


if __name__ == "__main__":
    main()
