---
name: theory/discrete_geometry/L28_cube_refinement_threshold
title: An explicit threshold for cube refinements
desc: A residue-path argument and an elementary odd-dimensional gcd bound give an explicit threshold for every larger cube count.
id: L28
statement: |
  Let d>=2 and M>=2 be integers with gcd(j^d-1:2<=j<=M)=1.
  Every integer k>=1+(2^d-2)(M^d-1) is the number of positive-side-length
  homothetic cubes in a dissection of the unit d-cube. For every odd d>=3
  this gcd condition holds with M=floor(sqrt(3d))+1. Consequently, if c(d)
  is the least threshold for all larger cube counts, then c(d)/d^d tends
  to zero as d tends to infinity through odd integers.
status: proved
tier: 0
depends_on: []
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

# An explicit threshold for cube refinements

[[theory/discrete_geometry/_index|..]]

[[theory/discrete_geometry/L28_cube_refinement_threshold/_proof|_proof]]: Complete geometric refinement, finite-group reachability and coprime-pair arguments for the cube-count threshold.

***

The [complete proof](_proof.md) is an author-recorded argument by Plasma AI.
There is no independent review or Lean proof. It combines an elementary
numerical-semigroup estimate with the subgroup and reduced-fraction strategy
recorded in
[[../library/integer_sequences/zeng_2026_collective_coprimality_threshold/partial_threshold_theorem|Zeng's gcd-threshold argument]].
That source is comparison and attribution: the proof below supplies every
arithmetic step it needs. No novelty is claimed.

For [[problems/discrete_geometry/E0769/_index|Problem 769]], this gives a
negative answer only to the proposed uniform lower bound $c(d)\gg d^d$.
It does not determine the growth order or its logarithmic limit. The
[[research/geometric_configuration_interfaces/cube_dissections|research account]]
explains the obstruction to using small grid sizes when $d+1$ is prime.
No mathematical gap remains in this partial bound. Verification consists of
checking the residue-path threshold, the two prime ranges and the asymptotic;
no computational certificate is needed.
