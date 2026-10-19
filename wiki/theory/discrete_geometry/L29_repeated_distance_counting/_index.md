---
name: theory/discrete_geometry/L29_repeated_distance_counting
title: Repeated-distance four-sets and isosceles triples
desc: Two counting inequalities isolate the isosceles-triple contribution missed by a disjoint-pair distance-energy estimate.
id: L29
statement: |
  Let P be a set of n>=4 distinct points in the Euclidean plane. Let I(P)
  count unordered triples with two equal side lengths, including collinear
  midpoint triples. Let D(P) count unordered four-subsets whose six pair
  lengths are not all distinct. Let Q(P) count ordered (a,b,c,d) in P^4
  with |a-b|=|c-d|>0. Then (n-3)I(P)/4<=D(P)<=Q(P)+(n-3)I(P).
status: proved
tier: 0
depends_on: []
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

# Repeated-distance four-sets and isosceles triples

[[theory/discrete_geometry/_index|..]]

[[theory/discrete_geometry/L29_repeated_distance_counting/_proof|_proof]]: Count extensions of equal-side triples and separate equal-length pairs by their number of distinct endpoints.

***

The [proof](_proof.md) is a complete author-recorded counting argument by
Plasma AI. No independent review or Lean proof is recorded. Its inequality
uses no external distance theorem.

Together with the external bound $Q(P)=O(n^3\log n)$, it makes the
$n^{3+o(1)}$ question in
[[problems/distance_problems/E1087/_index|Problem 1087]] equivalent to a
uniform bound $I(P)\le n^{2+o(1)}$. The
[[research/geometric_configuration_interfaces/distance_subsets|research account]]
states that source premise and its reading limit. No gap remains in these
inequalities; the near-quadratic isosceles estimate is still an additional
obligation. Verification is direct double counting.
