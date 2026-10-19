---
name: research/erdos_774/evidence/tensor_layers
title: Exact small tensor tests for the coloring threshold
desc: Exact 3-by-5 tensor-layer certificates give a three-color obstruction, a two-color extension, and bounds 8 to 10 on the separation parameter.
tags: [E0774, computational, proved, tensor]
sources: []
created: 2026-09-18T00:04:10Z
updated: 2026-10-13T04:56:43Z
---

# Exact small tensor tests for the coloring threshold

[[research/erdos_774/evidence/_index|..]]

***

## Purpose, input, and finite range

These checks test the
[signed-span separation parameter](../../routes/tensor_coloring.md)
on the base $X=S_3\otimes S_5$. They show that adding a larger simplex
can **lower**, rather than raise, the coloring number.

Run, from the repository root,

```sh
uv run --no-sync python wiki/research/erdos_774/evidence/tensor_layers/main.py
```

The [checker](main.py) uses explicit eight-coordinate integer vectors and checks
29 layers with at most eight vectors each, enumerating at most $3^8$ ternary
sums per layer. Every arithmetic operation is exact; it uses the standard
library and the shared root `tools` checker and finishes in a few seconds. Its
named checks are that every layer is dissociated, that the successive
intersection sizes below are reproduced, and that both colors of the second
example reach intersection zero by their tenth layer; a failed clause exits
nonzero. The layer lists come from
[Ramsey–Graham, *Planar Sidonicity and quasi-independence for multiplicative subgroups of the roots of unity*, Example 7.3 and Appendix (printed pages 356 and 358)](../../../../../library/analysis/ramsey_graham_2006_planar_sidonicity_quasi_independence_multiplicative_subgroups_roots_unity/_index.md),
checked in the held copy at those pages. The checker verifies the data rather
than assuming the reported computational outcome.

## Checked witnesses

For a 52-element subset of $X\otimes S_7$, all seven layers are
dissociated and the successive signed-span intersection sizes are

$$
2187,\ 339,\ 75,\ 25,\ 15,\ 9,\ 1.
$$

The final intersection is $\{0\}$, so the subset is dissociated by the
layer criterion. For two complementary subsets of $X\otimes S_{11}$,
of sizes 82 and 83, both final intersections are again $\{0\}$. Already
the first ten layers give zero intersections for both colors. Consequently

$$
\chi(X\otimes S_{11})=2,\qquad\tau_2(X)\leq10.
$$

The abstract tensor $X\otimes S_{10}$ also has two colors. It must not be
identified with all 150th roots of unity: that identification of a tensor of
simplexes uses distinct prime side sizes.

## Matching structural upper bound for the 52-point witness — proved

Identify $X$ with the edges of $K_{3,5}$. A rational relation has
coefficient array $a_i+b_j$. Its vanishing outside a set $S$ forces
the associated vertex potentials to agree across every edge of the complement.
Therefore

$$
S\text{ dissociated}\iff S\text{ rationally independent}
\iff K_{3,5}\setminus S\text{ connected}.
$$

If the complement is disconnected, a component cut gives a nonzero signed
relation. Thus the largest dissociated base set has size eight. For an
independent $S$, a root-edge belongs to $\Sigma(S)$ precisely when
it is in $S$ or is a bridge of its connected complement: deleting that
edge creates a cut relation; if it is not a bridge, even rational dependence
on $S$ is impossible.

Consider any dissociated subset of $X\otimes S_r$, with layers $S_j$.
Write $t_j=8-|S_j|$. The complement of $S_j$ has cycle rank $t_j$,
and its nonbridge edges can be covered by $t_j$ fundamental simple cycles.
These nonbridge sets must together cover every edge of $K_{3,5}$, or an
uncovered root-edge would lie in every $\Sigma(S_j)$, contradicting the
layer criterion.

Any cycle cover of $K_{3,5}$ needs at least four cycles. Each of the five
degree-three vertices must have even total incident multiplicity at least
four, requiring at least twenty edge occurrences, while each simple cycle
has at most six edges. Thus $\sum_jt_j\geq4$ and

$$
r(X\otimes S_r)\leq8r-4.
$$

At $r=7$, the verified witness attains 52. Since $2\cdot52<105$,
$\chi(X\otimes S_7)\geq3$. A three-class rational-independent partition
exists by Rado–Horn: averaging coordinate permutations of a 48-element tensor
basis gives rank at least $(48/105)|F|>|F|/3$ on every subset $F$.
Hence $\chi(X\otimes S_7)=3$.

## Lower bound on the separation threshold

In a two-coloring of $X$, class sizes are seven and eight. Across $r$
such colorings, the deficits of the two colors total exactly $r$. To make
each color's signed-span intersection zero, the cycle-cover argument requires
at least four deficit units for each color. Therefore

$$
8\leq\tau_2(S_3\otimes S_5)\leq10.
$$

This is a bounded test of the proposed tensor mechanism, not evidence for
unbounded coloring in the large-side uniform-extraction family.

## A further finite observation on the 52-point witness

A separate finite diagnostic read the fixed $3\times5\times7$ witness as
literal data. One $57\times53$ Smith normal form followed by at most 53
lexicographic free-edge collapses left, after exactly 53 collapses, a
connected 15-vertex, 18-edge graph; a corrected coordinate system was found
among at most $\binom{32}{4}=35960$ candidate bases, stopping at the first
unimodular basis, and all 81 ternary functionals were then evaluated, with
greedy pruning retaining eleven of at most 28 constraints; and a circuit
search over all $\binom{32}{3}=4960$ triples produced 184 primitive
functionals on the 52 vectors, of which one exact $48\times22$ rank
check certified a 22-point circuit with a coefficient two. These
observations reinforce the coefficient-two obstruction to rational-rank
arguments that [the prime-tensor circuit](../../lemmas/prime_tensor_circuit.md)
records exactly. They used a symbolic algebra package with ties broken by
set order rather than a prescribed rule, no script is retained, and no
theorem in the main argument depends on them.
