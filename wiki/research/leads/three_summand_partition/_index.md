---
name: research/leads/three_summand_partition
title: The three-summand case of the countable partition ordinals
desc: |
  Decide omega^(omega^gamma) -> (omega^(omega^gamma),3)^2 for gamma a sum of
  three indecomposable ordinals, starting at gamma=3. Online three-game
  constructions cover outside strategies and two classes of inside
  strategies. The coherent finite-height source argument leaves middle
  strategies open. Negative patterns need a separated host and
  unavoidability there; neither direction has a three-summand extension.
problems:
- 592
research_state: blocked
review_status: unreviewed
created: 2026-10-16T14:45:50Z
updated: 2026-10-16T14:45:50Z
---

# The three-summand case of the countable partition ordinals

[[research/leads/_index|..]]

***

This lead records Plasma AI's route to the last undecided case of
[[problems/set_theory/E0592/_index|Problem 592]]: for every countable

$$
\gamma=\omega^{\xi_1}+\omega^{\xi_2}+\omega^{\xi_3},\qquad
\xi_1\ge\xi_2\ge\xi_3,
$$

decide whether $\omega^{\omega^\gamma}\to(\omega^{\omega^\gamma},3)^2$. The
problem page's current assessment records that one or two summands give the
positive relation and four or more the negative one, by
[[../library/set_theory/schipperus_2010_countable_partition_ordinals/_index|Schipperus's paper]];
for three summands only the failure of the four-clique relation is known.
Its parameter $\beta$ is the $\gamma$ used here.

The canonical proof sketch is the
[[research/erdos_592/height_three_attack|height-three attack]], for the
first instance $\gamma=3$. It keeps the conditional bridge from a
three-game construction to the partition relation and the
[[research/erdos_592/successor_builder_theorem|finite-height source interface S]]
at author standing. Its outside and inside sections construct the three
plays one node at a time, for strategies that read numerical history,
when every output is outside, or inside with the first tree's top split
at its first or last pair of selected leaves. With Corollary 2 this
reduces the three-game step to *middle* strategies, the remaining open
gap G-mid. The
[[research/erdos_592/successor_tree_interface|successor-tree interface]]
supplies the equal-block normalization, and the
[[research/erdos_592/pattern_level_obstruction|pattern-level page]]
reads the printed negative patterns as fixed pairs of selection shapes.

## What would settle the lead

A positive answer through this route at $\gamma=3$ needs G-mid: three correct,
sufficiently large, complete plays sharing their trees against every
winning middle strategy. The fixed-shape part of G-mid is a finite merging
problem for each pair of shapes. The sketch has a structural lemma and
four templates for it, each under a condition on the second shape, and
one of them is online in a class that the finite-cover refinement can
select. Fixed-shape existence alone does not control future numerical
prescriptions. A negative answer needs a coloring of all pairs of a
specified full-type host, with no color-1 triangle and a color-1 pair
in every full-type subset of that host.
Under the selection-shape reading, a fixed-shape pattern coloring without
triangles would have to be inside and middle; its unavoidability would
still need a proof. The
[[research/erdos_592/pattern_level_obstruction|fixed-prefix embedding]]
shows that this unavoidability is false on unrestricted $W_3$ for
every coloring supported on disjoint leaf sets, including strategy
output graphs. It remains unproved on a separated host. The retained
census found a schedule for every bounded pair it covered.

Either answer at $\gamma=3$ is only a by-product until it is extended to
every three-summand $\gamma$. The positive extension needs a replacement
for the triangle construction of Lemma 26 that works at partial-sum nodes
and at limit nodes with collapsible ladders. The canonical sketch states
the exact common-maxima, ordinal-descent, collapsing-map, history and
termination obligations. No such replacement is proved. The printed
pattern arguments for the negative relations use only the summand level
of a cell, so a negative pattern at $\gamma=3$ would be expected to transfer, but that
transfer is not proved here.

## Standing

All arguments on the linked pages are author-recorded and unreviewed.
[[theory/ramsey_theory/L67_containment_pattern_levels/_index|L67]] is a
tier-0 obstruction to one level interpretation and is not used as a
premise of the route. The
[[research/leads/four_clique_versus_triangle_colors/_index|four-clique lead]]
explains what a positive answer would also settle. The next
discriminating positive test is an online middle construction that places
each double without relying on an unavailable later prescription. For
the negative route, the pattern-level page identifies the concrete
ten-leaf pair obtained by merging levels $3$ and $2$ of the
four-level pattern. Its exclusion proof does not survive that merge;
either a shared-tree triangle or a new exclusion proof would decide
whether to pursue its separate unavoidability obligation. The lead is
blocked on these mathematical inputs, not on source access.
