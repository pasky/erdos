---
name: research/leads/property_p_sieve_multiplicity/evidence
title: Evidence
desc: |
  Exact finite normalization, occupancy and obstruction checks, retained
  admissible-window witnesses, and certified two-block harmonic upper
  bounds, with exploratory solver maxima kept at their finite scope.
tags: []
sources: []
created: 2026-10-16T20:05:55Z
updated: 2026-10-16T20:06:27Z
---

# Evidence

[[research/leads/property_p_sieve_multiplicity/_index|..]]

***

The [entry point](main.py) checks the finite evidence for the
[sieve lead](../_index.md) with the shared failure harness. It uses the
root Python environment with NumPy and SciPy, reads the two JSON assets
below, and writes no output files. Run it from the repository root:

```sh
uv run --no-sync python wiki/research/leads/property_p_sieve_multiplicity/evidence/main.py
```

Expected runtime is about 90 seconds. Solver calls are restricted to one
thread and must report completion; their optimality remains a floating-point
report. There is no reduced mode. The checks cover:

- direct property-P tests of the truncated gcd-one example, the
  self-inverse-residue witness, and the congruence blocks;
- exhaustive residue occupancy for six coprime pairs and for $\{15,21\}$;
- greedy integer and prime property-P sets and the stated finite bounds;
- the first-prime normalization, exact ownership, inherited exclusions,
  strict descent and the mass and Euler-weight telescoping identities,
  including children containing 1 or 2;
- the sibling-discount family for $(k,M)=(3,105),(3,315),(4,1155),(5,15015)$;
  the largest uses the proved automatic-interval reduction for property P,
  and the others also receive direct checks;
- the semiprime family for $y=7,13,31$, including the greedy matching,
  nonempty small-prime branches and discarded-large-prime bounds;
- the direct-toll obstruction with $M=625,1225$, including its fixed early
  element, exact root list and nonempty prime branches;
- [nine retained above-product witnesses](assets/above_product.json),
  checking every element's domain, admissible residues, property P and
  exact rational mass;
- [the retained two-block witness](assets/two_block.json), with exact mass
  above $0.0929$, and the separate exhaustive matching upper bound
  $0.101959737$ over all $2^{14}$ early subsets;
- the three further exhaustive matching bounds for later interval starts
  625, 3125 and 78125, with their complete candidate counts and rounded
  separate masses. Each covers the same $2^{14}$ early choices.

The two-block upper bounds in [the checker](util/two_block.py) use integer
weights rounded upward, disjoint edges representing forbidden distinct
pairs, and every early subset. They are certified finite upper bounds when
replayed; they do not assert exact optima. The lower witness
was found by a time-limited mixed-integer search and is checked directly.
The nine above-product witnesses were also found by the mixed-integer
solver; replay of their feasibility does not certify their optimality.
Earlier finite-window maxima in `main.py` retain that same distinction.

Arithmetic for witness properties, masses, ownership and the matching
bound is exact. Numerical regional comparisons and solver optimality are
explicitly numerical. The infinite semiprime obstruction uses the written
prime-number-theorem argument; no finite grid replaces it. These checks
prove neither (H), (U), nor E12(iii), and confer no independent review.
