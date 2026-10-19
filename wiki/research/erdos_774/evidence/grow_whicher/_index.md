---
name: research/erdos_774/evidence/grow_whicher
title: The 15-point obstruction and a weighted extraction gap
desc: An exact exhaustive certificate verifies the Grow–Whicher example and its fractional dissociated coloring number 27/13.
tags: [E0774, computational, finite]
sources: []
created: 2026-09-17T23:53:25Z
updated: 2026-10-13T04:56:43Z
---

# The 15-point obstruction and a weighted extraction gap

[[research/erdos_774/evidence/_index|..]]

***

## Input, range, and conclusions

The fixed input is

$$
E=\{3^j+kj:1\leq j\leq5,\ 0\leq k\leq2\}
=\{3,4,5,9,11,13,27,30,33,81,85,89,243,248,253\},
$$

the fifteen-point example of
[Grow and Whicher](../../../../../library/analysis/grow_whicher_1984_finite_unions_quasi_independent_sets/_index.md),
whose proposition supplies the hereditary ratio, rank and three-coloring facts
reproduced here; the fractional certificate is additional computation, not a
claim quoted from that paper.

Run, from the repository root,

```sh
uv run --no-sync python wiki/research/erdos_774/evidence/grow_whicher/main.py
```

The [checker](main.py) tabulates all $2^{15}=32768$ subsets by exact
subset-sum bitsets and dynamic programming. It uses the standard library
and the shared root `tools` checker, performs no random trials and needs
no external solver, and finishes in a few seconds. Its named checks cover
the subset count, rank, hereditary ratio, the absence of a proper
two-coloring, the one-point deletion, the two sides of the fractional
certificate, the rank of fourteen listed relations, and the no-clone
supports below; a failed clause exits nonzero. The checked results are

$$
\eta(E)=\tfrac12,\qquad r(E)=8,\qquad\chi(E)=3,
\qquad\chi_f(E)=\tfrac{27}{13}.
$$

There are 7568 nonempty dissociated subsets. The first three assertions
independently reproduce the full-source Grow–Whicher proposition.

## Exact fractional certificate

Give weight $2/13$ to each of the first twelve elements and $1/13$ to
each of the last three. The checker verifies that every dissociated set has
weight at most one. The total weight is $27/13$, giving the fractional
coloring lower bound.

For the reverse bound the checker lists 11 dissociated subsets with integer
multiplicities totaling 27; every point is covered exactly 13 times.
Assigning weight $1/13$ to each repeated set proves the matching upper
bound using only rational arithmetic. A bounded optimization search located
that certificate, but no optimization solver is needed to verify it.

In particular the unweighted hereditary half-extraction condition does
**not** imply weighted half-extraction. An amplification argument must not
substitute a fractional-coloring bound of two for the actual hypothesis.

## Further finite checks and their scope

Fourteen listed signed relations have rank fourteen. In addition, for each
point $a\in E$, two listed minimal relation supports force its positive
replacement to equal $a$ if all other numerical labels are fixed. The
checker verifies this by intersecting the two sets of possible signed sums.

This rules out a distinct positive clone **around this fixed numerical
realization**. It does not rule out every alternative representation of the
unsigned hypergraph or every possible substitution construction.

Neither this example nor its relation-separated repeated copies gives
unbounded coloring number; their coloring number remains three. See the
[direct-sum identity](../../lemmas/finite_blocks.md). The deletion of the
point $3$ is the source of the
[boundary-anchor certificate](../boundary_anchor/_index.md).
