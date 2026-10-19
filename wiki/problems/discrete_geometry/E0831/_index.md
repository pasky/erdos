---
name: problems/discrete_geometry/E0831
title: Problem 831
desc: |
  Asks to estimate the least number of distinct radii among circles through
  three of $n$ points in the plane, with no three collinear and no four
  concyclic.
tags:
- Geometry
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-14T15:30:27Z
---

# Problem 831

[[problems/discrete_geometry/_index|..]]

***

**Statement.** Let $h(n)$ be maximal such that in any $n$ points in
$\mathbb{R}^2$ (with no three on a line and no four on a circle) there are at
least $h(n)$ many circles of different radii passing through three points.
Estimate $h(n)$.

**Status.** Open.

**Source.** [erdosproblems.com/831](https://www.erdosproblems.com/831), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #831,
https://www.erdosproblems.com/831.

**Formalization.** None recorded.

## Current assessment

Current standing is as stated above; the route analysis records a scoped
mathematical comparison.

## Route analysis

The [[research/geometric_configuration_interfaces/circumradii|circle counts and
distinct circumradii]] account records the following scope. Every triple gives a
distinct circle, while fixed-radius circles use at least three pairs and every
pair lies on at most two such circles. Hence there are at least
$\lceil(n-2)/2\rceil$ distinct radii. The conjectured little-$o$ bound in
E0104 would imply a superlinear number; that premise remains open.
