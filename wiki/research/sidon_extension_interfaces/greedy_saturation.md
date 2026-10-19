---
name: research/sidon_extension_interfaces/greedy_saturation
title: "Greedy prefixes and maximal Sidon blockers"
desc: "The existing cubic blocker count bounds every greedy prefix, while sparse maximal constructions and dissociation require different interfaces."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/additive_bases/E0156/_index|E0156]],
[[problems/additive_bases/E0340/_index|E0340]],
[[problems/additive_bases/E0864/_index|E0864]],
[[problems/number_theory/E0963/_index|E0963]].

For a maximal strong Sidon set $A\subset[1,N]$ of size $k$, the
[[research/erdos_156/foundations/lower_bound|existing blocker proof]] gives
$$
N\le(k^3+k)/2.
$$
Every greedy prefix in $[1,N]$ is maximal there: each omitted integer was
already blocked by earlier marks, and those marks remain. Immediately before the
next greedy mark $a_{k+1}$, the first $k$ marks are maximal in $[1,a_{k+1}-1]$.
Thus
$$
a_{k+1}\le(k^3+k)/2+1.
$$
This supplies the cubic-root baseline for E0340. An existentially small maximal
set does not control this particular greedy sequence. An improvement needs
overlap information for its actual blockers.

For E0156 the [[research/erdos_156/foundations/ruzsa_and_carries|existing
construction account]] identifies the union-bound logarithm and the integer
carry obstruction. No new saturation computation is supplied here.

For E0864, retain the [[research/erdos_864/established_bounds|existing
difference and window bound]] $|A|\le\sqrt{2N}+O(N^{1/4})$ and the
[[research/erdos_864/obstructions|exact-reflection obstruction]]. Neither
establishes the requested coefficient $2/\sqrt3$, and the exponential diameter
of the obstruction leaves dense asymptotic completion separate.

For E0963 the [[research/erdos_963/proof_sketch|existing dissociation sketch]]
already separates maximal ternary spanning from the desired binary-size bound
and proves the reduction to positive sets. Bounds for the largest element of a
dissociated subset of $[1,n]$ bound its size above, hence the universal
guarantee above; they do not give the required lower bound. No finite
dissociation search is part of this account.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/additive_bases/huber_2026_saturated_sidon_sets_consecutive_intervals_eight_mark_threshold_144/_index|Huber:
  Saturated Sidon Sets in Consecutive Intervals: The Eight-Mark Threshold Is
  144]]: fixed-eight theorem and evidence scope (account reading).
- [[../library/additive_bases/redman_2021_small_maximal_sidon_set_z_2/_index|redman
  2021 small maximal sidon set z 2]]: Introduction, Definitions 1.1-1.2 and main
  bound (statement reading).
- [[../library/additive_bases/ruzsa_1998_small_maximal_sidon_set/_index|ruzsa
  1998 small maximal sidon set]]: Theorem and final Remark on minimum maximal
  cardinality (account reading). Theorem, Lemma and full construction through
  maximal extension (proof reading).
- [[../library/additive_combinatorics/lev_yuster_2010_size_dissociated_bases/_index|On
  the size of dissociated bases]]: Introduction, Theorems 1-3 (statement
  reading).
