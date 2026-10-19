---
name: problems/distance_problems/E0100
title: Problem 100
desc: |
  Asks whether $n$ points in the plane whose pairwise distances are at least
  $1$, and whose distinct distances differ by at least $1$, must have diameter
  $\gg n$.
tags:
- Geometry
- Distances
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 100

[[problems/distance_problems/_index|..]]

***

**Statement.** Let $A$ be a set of $n$ points in $\mathbb{R}^2$ such that all
pairwise distances are at least $1$ and if two distinct distances differ then
they differ by at least $1$. Is the diameter of $A$ $\gg n$?

**Status.** Open.

**Source.** [erdosproblems.com/100](https://www.erdosproblems.com/100), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #100,
https://www.erdosproblems.com/100.

**References.**

- [GuKa15] Guth, Larry and Katz, Nets Hawk, On the Erdős distinct distances
  problem in the plane. Ann. of Math. (2) (2015), 155-190.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/100.lean).

## Current assessment

Current standing is as stated above; the route analysis records a scoped
mathematical comparison.

## Route analysis

The [[research/distance_multiplicity_interfaces/counts|Distance counts,
multiplicities and pinned occupancy]] account records the following scope. If
$D$ is the number of distinct positive distance values and consecutive values
are separated by at least one, the diameter is at least $D$. The held general
bound gives only order $n/\log n$ through this argument, leaving the requested
linear scale open.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/distance_problems/guth_2015_erdos_distinct_distance_problem_plane/_index|guth_2015_erdos_distinct_distance_problem_plane]]
- [[../library/distance_problems/guth_2015_erdos_distinct_distance_problem_plane/theorem_1_1|guth_2015_erdos_distinct_distance_problem_plane / theorem_1_1]]

<!-- END problem library links -->
