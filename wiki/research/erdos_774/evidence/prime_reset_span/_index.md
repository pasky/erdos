---
name: research/erdos_774/evidence/prime_reset_span
title: Stopped common-span test for the seven-layer prime coloring
desc: The 96-by-105 common-span matrix of the explicit seven-layer three-coloring of S_3 x S_5 x S_7 has nullity 22, above the enumeration gate, so the test decides nothing.
tags: [E0774, computational, incomplete]
sources: []
created: 2026-09-24T23:30:00Z
updated: 2026-09-24T23:30:00Z
---

# Stopped common-span test for the seven-layer prime coloring

[[research/erdos_774/evidence/_index|..]]

***

## Purpose and outcome

The [prime reset and plateau page](../../routes/prime_reset_plateau.md)
exhibits an explicit seven-layer three-coloring of $S_3\otimes S_5\otimes S_7$
and proves its root-omission properties by an algebraic cyclic signed-sum
lemma. Before that lemma was found, one fixed computation tried to decide
the common signed-span intersection of the three classes directly. It was
designed to form the $96\times105$ matrix whose kernel consists of the
coefficient triples with equal signed sums in all three classes, and to
enumerate at most $3^{12}$ ternary values of the free original coefficients
only if the nullity was at most 12. The nullity is 22, so no enumeration ran
and the test decides nothing about the intersection. The algebraic lemma
supersedes this route; no zero-intersection conclusion is drawn from the
stopped computation.

The coloring itself was discovered in an exact search of at most 120 column
permutations of its specified Latin coloring; the search stopped at
permutation 2. Its coordinate proof on the route page supersedes discovery.

## What is checked

Run, from the repository root,

```sh
uv run --no-sync python wiki/research/erdos_774/evidence/prime_reset_span/main.py
```

The [checker](main.py) rebuilds the seven-layer coloring, forms the
equality matrix, and reduces it by exact rational elimination, using the
standard library and the shared root `tools` checker; it performs no
search and finishes in a few seconds. Its named checks are the class sizes
$(35,35,35)$, the matrix shape $96\times105$, rank 83, nullity 22, and
that the nullity exceeds the declared gate, so that the ternary enumeration
is not run. A failed clause exits nonzero. These are exact facts about the
matrix; they certify nothing about dissociated coloring.
