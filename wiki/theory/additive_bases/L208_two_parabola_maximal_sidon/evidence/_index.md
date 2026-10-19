---
name: theory/additive_bases/L208_two_parabola_maximal_sidon/evidence
title: Exhaustive check of the two-parabola sets for small q
desc: Recompute the size, strong Sidon property, maximality and proof witnesses of the two-parabola set for every non-square in each small odd field.
created: 2026-10-15T18:15:30Z
updated: 2026-10-15T18:15:30Z
---

# Exhaustive check of the two-parabola sets for small q

[[theory/additive_bases/L208_two_parabola_maximal_sidon/_index|..]]

***

From the repository root run:

```sh
uv run --no-sync python wiki/theory/additive_bases/L208_two_parabola_maximal_sidon/evidence/main.py
```

The program builds $\mathbb F_q$ for $q\in\{3,5,7,9,11,13,17,19,23,25,27,49\}$
from explicit irreducible polynomials, whose irreducibility it checks, and
forms the set $A$ of the [claim](../_index.md) for every non-square $\mu$.
For each pair $(q,\mu)$ it checks that $|A|=2q-1$, that all unordered pair
sums with doubles are distinct, that every point of $\mathbb F_q^3$ outside
$A$ is of the form $a+b-c$ with $c\notin\{a,b\}$, and that the three
explicit witness formulas of the [proof](../_proof.md) produce valid
witnesses for every such point. As a control, for every non-zero square
$\mu$ it finds the repeated sum $P(t)+P(-t)=C(u)+C(-u)$ that the proof
excludes for non-squares.

All arithmetic is exact. The program uses the repository's evidence harness
and the Python standard library; it runs in about ten seconds and has no
quick mode. Any failed obligation gives a nonzero exit, also under
optimized Python. The check covers these finite fields only; the statement
for every odd prime power rests on the proof.
