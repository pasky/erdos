---
name: research/erdos_156
title: Small maximal Sidon sets
desc: "The cubic-root problem, its counting lower bound, and the Ruzsa benchmark."
tags: []
sources: []
created: 2026-09-23T01:53:50Z
updated: 2026-10-15T11:57:22Z
---

# Small maximal Sidon sets

[[research/_index|..]]

[[research/erdos_156/foundations/_index|foundations/]]: The blocking criterion, the cubic counting bound, and the Ruzsa benchmark.

[[research/erdos_156/source_notes/_index|source_notes/]]: Paper summaries and source comparisons used in the research on Problem 156.

[[research/erdos_156/uniform_coverage|uniform_coverage]]: An O(p) residual suffices for a small maximal completion of a Singer lift. At p cubed comparable to N, independent uniform lifts leave a linear residual with probability tending to one; structured lifts and coordinated repair remain unresolved.

***

## The target and the scale

For every sufficiently large $N$, construct a strong Sidon set
$A\subset[1,N]$, maximal in this interval, with $|A|\le C N^{1/3}$
for an absolute constant $C$, or prove that no such bound exists.
Strong Sidonicity counts unordered pair sums, including doubles.
For $x\notin A$, the blocking criterion is

$$
 x\in A+A-A\quad\text{or}\quad 2x\in A+A.
$$

[The counting bound](foundations/lower_bound.md) gives the cubic-root lower
scale. [Ruzsa's lifting argument](foundations/ruzsa_and_carries.md) gives
$O((N\log N)^{1/3})$. The logarithm-free question remains open. At
$p^3\asymp N$, the [uniform-coverage test](uniform_coverage.md) proves that a
Singer lift leaving $O(p)$ targets outside the Singer classes unblocked
completes to a maximal set of size $O(N^{1/3})$. The complete
bounded-dependence argument in
[[theory/additive_bases/L125_random_singer_lift_residual/_index|L125, tier 0]]
proves that uniform independent lifts leave a linear residual with
probability tending to one at that scale. Exceptional structured lifts and
coordinated $O(p)$ repairs remain open; a large initial residual is not a
lower bound on completion size.
