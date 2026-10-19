---
name: theory/number_theory/L198_three_layer_prime_blocks/evidence
title: Direct counts of three-layer blocks
desc: Build type-class cell sets, keep the cells with prime differences, place the block of the proof and count its prime multiples directly.
created: 2026-10-15T15:58:15Z
updated: 2026-10-15T15:58:15Z
---

# Direct counts of three-layer blocks

[[theory/number_theory/L198_three_layer_prime_blocks/_index|..]]

***

From the repository root run:

```sh
uv run --no-sync python wiki/theory/number_theory/L198_three_layer_prime_blocks/evidence/main.py
```

The [instances](assets/instances.json) list nine triples
$(m,\alpha,q)$ with $m=1,2,3$ and $\alpha=3,7/2,39/10$, chosen by Plasma
AI with $q$ just above the threshold $(16\cdot27^m+1)/(4-\alpha)$ of
L198. For each one the checker builds the type class of the cells
$(0,1)$, $(2,1)$, $(2,2)$ used by
[[theory/number_theory/L201_type_class_long_block_bound/_index|L201]],
verifies its size, its distinct differences and its three projection
sizes $\binom{3m}{m}$, and checks the hypotheses of L198. It then keeps
the cells whose $q+y-x$ is prime, solves the congruences, places the
block given in the [proof](../_proof.md) and makes it positive. Finally it
counts the integers of the block divisible by a kept prime directly from
the primes, each once.

The checks are that every kept prime has exactly three multiples in the
block and that the direct count equals $|X|+|Y|+|W|$ for the kept
cells. The retained prime and multiple counts are reproduced, among them
$302$ primes with $220$ multiples for $m=3$, $\alpha=3$. All arithmetic is
exact, primality is decided by trial division, and the run takes a few
seconds at most. These instances test the endpoint inequalities, the floor in
the block length, positivity and once-only counting; they prove nothing
beyond themselves.
