---
name: problems/distance_problems/E1087
title: Problem 1087
desc: |
  Asks to estimate the largest number of four-point subsets with two pairs at
  equal distance among $n$ points in the plane, and whether it is at most
  $n^{3+o(1)}$.
tags:
- Geometry
- Distances
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 1087

[[problems/distance_problems/_index|..]]

***

**Statement.** Let $f(n)$ be minimal such that every set of $n$ points in
$\mathbb{R}^2$ contains at most $f(n)$ many sets of four points which are
'degenerate' in the sense that some pair are the same distance apart. Estimate
$f(n)$ - in particular, is it true that $f(n)\leq n^{3+o(1)}$?

**Status.** Open.

**Source.** [erdosproblems.com/1087](https://www.erdosproblems.com/1087),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1087,
https://www.erdosproblems.com/1087.

**References.**

- [ErPu71] Erdős, Paul and Purdy, George, Some extremal problems in geometry. J.
  Combinatorial Theory Ser. A (1971), 246-252.

**Formalization.** None recorded.

## Current assessment

Current standing is as stated above; the route analysis records a scoped
mathematical comparison.

## Route analysis

The [[research/geometric_configuration_interfaces/distance_subsets|repeated
distances and geometric sidon subsets]] account records the following scope. The
author-recorded L29 separates disjoint equal-distance pairs from isosceles
triples with arbitrary fourth points. With the external Guth–Katz energy bound,
the proposed $n^{3+o(1)}$ upper bound is equivalent to a uniform $n^{2+o(1)}$
isosceles-triple bound, including midpoint triples.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/distance_problems/erdos_1971_extremal_problems_geometry/_index|erdos_1971_extremal_problems_geometry]]
- [[../library/distance_problems/erdos_1971_extremal_problems_geometry/question_p251|erdos_1971_extremal_problems_geometry / question_p251]]

<!-- END problem library links -->
