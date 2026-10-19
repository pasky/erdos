---
name: problems/additive_bases/E0757
title: Problem 757
desc: |
  Asks for the best constant $c$ such that $n$ reals whose every four-element
  subset $B$ has $\lvert B-B\rvert\ge11$ contain a Sidon set of size $cn$.
tags:
- Geometry
- Distances
- Sidon sets
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 757

[[problems/additive_bases/_index|..]]

***

**Statement.** Let $A\subset \mathbb{R}$ be a set of size $n$ such that every
subset $B\subseteq A$ with $\lvert B\rvert =4$ has $\lvert B-B\rvert\geq 11$.
Find the best constant $c>0$ such that $A$ must always contain a Sidon set of
size $\geq cn$.

**Status.** Open.

**Source.** [erdosproblems.com/757](https://www.erdosproblems.com/757), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #757,
https://www.erdosproblems.com/757.

**References.**

- [GyLe95] Gyárfás, András and Lehel, Jenő, Linear sets with five distinct
  differences among any four elements. J. Combin. Theory Ser. B (1995), 108-118.
- [MaTa26] J. Ma and Q. Tang, Largest Sidon subsets in weak Sidon sets.
  arXiv:2602.23282 (2026).

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/757.lean).

## Current assessment

Current standing is as stated above; the route analysis records a scoped
mathematical comparison.

## Route analysis

The [[research/four_point_sidon_certificates/_index|four-point difference
conditions and sidon certificates]] account records the following scope. An
exact replay of the fourteen-point Ma–Tang example certifies maximum strong
Sidon size eight. A separate source-qualified transversal specialization
excludes improvements to $4/7$ on at most fifteen points; the sixteen-point
possibility has not been searched.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/additive_bases/ma_2026_largest_sidon_subsets_weak_sidon_sets/_index|ma_2026_largest_sidon_subsets_weak_sidon_sets]]
- [[../library/additive_bases/ma_2026_largest_sidon_subsets_weak_sidon_sets/theorem_1_5|ma_2026_largest_sidon_subsets_weak_sidon_sets / theorem_1_5]]
- [[../library/additive_bases/ma_2026_largest_sidon_subsets_weak_sidon_sets/theorem_1_6|ma_2026_largest_sidon_subsets_weak_sidon_sets / theorem_1_6]]

<!-- END problem library links -->
