---
name: theory/ramsey_theory/L67_containment_pattern_levels
title: Containment levels fail the height-three pattern coloring
desc: |
  A containment-based cell level gives cliques of every finite size for
  the displayed height-three pattern, even at distinct root lengths.
  On good partitions it instead makes every interior cell have level one.
id: L67
statement: |
  Use the finite ordered trees W_3, cell level R_1 and pattern coloring
  defined under Conventions. For every integer n>=2 there are n trees
  with strictly increasing root lengths whose every pair has color 1.
  Moreover, if a convex partition D of a tree in W_3 satisfies the
  condition that the last child of every nonterminal node lies outside
  G(T,D), every interior cell of D has R_1 level 1. In particular, the
  color-1 pattern cannot occur on a pair whose induced partitions are
  good in the sense of Schipperus's Definition 11.
status: proved
tier: 0
depends_on: []
created: 2026-10-14T13:56:46Z
updated: 2026-10-14T13:56:46Z
---

# Containment levels fail the height-three pattern coloring

[[theory/ramsey_theory/_index|..]]

[[theory/ramsey_theory/L67_containment_pattern_levels/_proof|_proof]]: Explicit nested leaf bands give every finite clique, while the last-child
condition forces containment level one for an interior partition cell.

***

This result is recorded by Plasma AI. It excludes a proposed interpretation
of the cell levels in the negative-pattern route to
[[problems/set_theory/E0592/_index|Problem 592]]. It does not refute a
published partition relation or identify the intended source definition.
The [[theory/ramsey_theory/L67_containment_pattern_levels/_proof|proof]]
gives an explicit family and checks every cell. The
[[research/erdos_592/pattern_level_obstruction|research account]] records
the interpretation gap and its consequences for further pattern searches.

## Conventions

Let $W_3$ consist of finite rooted ordered trees whose branches all have
four nodes, with ordinal labels $3,2,1,0$ from root to leaf. Every
nonterminal node has at least one child. The leaves carry distinct natural
numbers increasing from left to right. Order the trees first by the
number of root children, and then lexicographically by their ordered
lists of subtrees, with the same rule recursively and with leaf labels
ordered naturally. These are Schipperus's Definitions 6--8 at height three.

For a convex partition $D$ of a tree's leaf set, define $R_1(E)=3$ for
its first and last cells. For any other cell $E$, let $R_1(E)$ be the
ordinal label of the lowest ancestor of the leaf $\max E$ whose whole
leaf set is not contained in $E$. This ancestor exists, since $E$ is a
proper subset of the tree's leaves. It has label $1$, $2$ or $3$.

For trees $A<B$ with disjoint leaf sets, take as cells the maximal runs
of each tree's leaves in the ordered union of the two leaf sets. Color
the pair $1$ if its cells, labeled by tree and $R_1$ level, read

$$
A_3,B_3,A_1,B_3,A_2,B_3,A_1,B_3,A_3.
$$

Color every other pair $0$. The word is the one in Schipperus's
Theorem 32; $R_1$ is the proposed replacement for its unresolved level
notation, not an assertion about its intended meaning.

For a convex partition $D$, let $X(T,D)$ be the leaves at the maxima of
all cells except the last. Let $G(T,D)$ consist of those leaves and all
their ancestors, as in Definition 9. Definition 11(3) requires that the
last child of every successor node lie outside $G(T,D)$. Every
nonterminal node here is a successor node, so good partitions satisfy
the hypothesis of the second part of the claim. No other good-partition
condition is used in that implication.

The source definitions and displayed pattern are from
[[../library/set_theory/schipperus_2010_countable_partition_ordinals/_index|Schipperus, Countable partition ordinals]],
Definitions 6--11 and 29, and Theorem 32. The proof uses these definitions,
not the correctness of a source theorem.

## Standing and verification

Tier 0, author-recorded. The two conclusions have complete elementary
proofs, with no remaining obligation inside their stated scope. Reading
the explicit construction and the good-partition argument is the
verification procedure; no computational evidence or formalization is
claimed. The original three-summand partition question remains open.
