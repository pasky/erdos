---
name: theory/combinatorics/L26_design_size_multiplicity
title: Block-size multiplicity in pairwise balanced designs
desc: A nontrivial pairwise balanced design needs at least n blocks, and near-square-root minimum block size forces too few sizes for an O(sqrt(n)) multiplicity cap.
id: L26
statement: |
  Let a pairwise balanced design on n>=3 points have m blocks, each of size
  at least two and less than n, with every pair of points in exactly one
  block. If a and b are the minimum and maximum block sizes, then m>=n and
  b(a-1)<=n-1. If at most C sqrt(n) blocks have each size, for a real C>0,
  then at least sqrt(n)/C distinct block sizes occur. Consequently there is
  no sequence of such designs with n tending to infinity, minimum block
  size at least (1-o(1))sqrt(n), and one fixed multiplicity constant C.
status: proved
tier: 0
depends_on: []
created: 2026-10-14T12:38:34Z
updated: 2026-10-14T12:38:34Z
---

# Block-size multiplicity in pairwise balanced designs

[[theory/combinatorics/_index|..]]

[[theory/combinatorics/L26_design_size_multiplicity/_proof|_proof]]: The incidence matrix gives m>=n, while a point outside a largest block bounds every block size in terms of the minimum.

***

The [proof](_proof.md) combines the point-incidence rank argument with the
blocks joining a point to a largest block. This is a complete author-recorded
argument by Plasma AI, at tier 0, without independent review or Lean proof.
No other native claim or computation is used. The rank bound is a classical
part of de Bruijn–Erdős; its short proof is included, and no novelty for it
is claimed.

The consequence obstructs the proposed transfer from the near-uniform
designs of [[problems/set_systems/E0665/_index|Problem 665]] to the low
size multiplicities of [[problems/set_systems/E0734/_index|Problem 734]].
It does not rule out designs with a wider range of block sizes. That wider
range is the remaining construction problem. The
[[research/design_size_multiplicity/_index|research note]]
explains the quantitative interface to the held six-size construction.
The stated claim has no remaining mathematical gap; verification consists
of checking the rank identity, the pairwise disjoint petals, and the
asymptotic size interval.
