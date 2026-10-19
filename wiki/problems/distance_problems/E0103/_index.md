---
name: problems/distance_problems/E0103
title: Problem 103
desc: |
  Asks whether the number of incongruent $n$-point sets in the plane with
  minimum distance $1$ and the least possible diameter tends to infinity.
tags:
- Geometry
- Distances
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-14T15:30:27Z
---

# Problem 103

[[problems/distance_problems/_index|..]]

***

**Statement.** Let $h(n)$ count the number of incongruent sets of $n$ points in
$\mathbb{R}^2$ which minimise the diameter subject to the constraint that
$d(x,y)\geq 1$ for all points $x\neq y$. Is it true that $h(n)\to \infty$?

**Status.** Open.

**Source.** [erdosproblems.com/103](https://www.erdosproblems.com/103), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #103,
https://www.erdosproblems.com/103.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/103.lean).

## Current assessment

Current standing is as stated above; the route analysis records a scoped
mathematical comparison.

## Route analysis

The [[research/distance_multiplicity_interfaces/exact_optimizers|exact
optimizers and local geometric obstructions]] account records the following
scope. A sufficient flex criterion is explicit: an optimal configuration
containing a point p whose distances to every other point lie strictly between 1
and the optimal diameter admits a neighborhood of motions of p with both extrema
unchanged, yielding continuum many incongruent optimizers.
