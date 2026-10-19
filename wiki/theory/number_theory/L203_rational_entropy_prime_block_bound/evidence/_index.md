---
name: theory/number_theory/L203_rational_entropy_prime_block_bound/evidence
title: Rational certification of the seven-point entropy ratio
desc: Recompute the seven-point measure's marginals and use rational logarithm enclosures to certify that its largest projection entropy is less than 0.56213 times its joint entropy.
created: 2026-10-15T16:33:51Z
updated: 2026-10-15T16:33:51Z
---

# Rational certification of the seven-point entropy ratio

[[theory/number_theory/L203_rational_entropy_prime_block_bound/_index|..]]

***

From the repository root run:

```sh
uv run --no-sync python wiki/theory/number_theory/L203_rational_entropy_prime_block_bound/evidence/main.py
```

The [measure](assets/measure.json) records Lemm's seven integer points
and the rational weights used in the [proof](../_proof.md). The points
come from the proof of
[[../library/additive_combinatorics/lemm_2015_new_counterexamples_sums_differences/theorem_2_1|Lemm's Theorem 2.1 in arXiv:1404.3745v2]], pp. 4--5.
The weights are an exact rational choice close to the source's printed
probabilities; no optimization is rerun or assumed.

The checker recomputes the differences and all three marginals, checks
the change to cell coordinates, and encloses the joint and projection
entropies with rational arithmetic. Each logarithm uses 32 terms of the
series and the tail estimate proved in the owning proof. No floating
point arithmetic enters a check. It fails unless the retained measure
has distinct differences and the certified upper bound for the largest
projection entropy is less than $56213/100000$ times the certified
lower bound for the joint entropy. All failures produce a nonzero exit,
including with Python optimization enabled.

This finite certificate is the numerical premise of L203. Its scope
does not include the type-class asymptotics or Green--Tao prime
realization, whose proofs and dependencies are stated separately.
The run uses one thread, takes a few seconds at most, and needs only the
standard library and the repository evidence harness.
