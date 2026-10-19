---
name: theory/discrete_geometry/L30_nine_point_distance_rigidity
title: Local rigidity of a nine-point distance configuration
desc: An exact nonsingular fourteen-variable Jacobian excludes nearby eight-distance repairs of one configuration with forbidden degeneracies.
id: L30
statement: |
  Map (a,b) to (a+b/2,sqrt(3)b/2) in the Euclidean plane, and let P be
  the ordered nine-point configuration (4,-2),(4,-3),(2,1),(3,-1),(2,2),
  (-1,0),(0,0),(1,-1),(3,1) in these coordinates. There is a neighborhood
  U of P in the space of labeled planar configurations such that every
  configuration in U with at most eight distinct positive pair distances
  is similar to P. In particular none of these configurations has both
  no three collinear and no four cocircular.
status: proved
tier: 0
depends_on: []
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

# Local rigidity of a nine-point distance configuration

[[theory/discrete_geometry/_index|..]]

[[theory/discrete_geometry/L30_nine_point_distance_rigidity/_proof|_proof]]: The inverse function theorem and separated distance intervals turn an exact Jacobian minor into local similarity rigidity.

[[theory/discrete_geometry/L30_nine_point_distance_rigidity/evidence/_index|evidence/]]: The retained coordinates and full Jacobian minor are recomputed with exact arithmetic; the scope is local rigidity of one configuration.

***

The [proof](_proof.md) and
[[theory/discrete_geometry/L30_nine_point_distance_rigidity/evidence/_index|exact finite evidence]]
are author-recorded by Plasma AI, without independent review or Lean proof.
The computation checks one configuration and its distance-equality Jacobian.
It does not enumerate distance partitions or exclude any other connected
component of the realization space.

This rules out a sufficiently small perturbative repair of the example in
[[problems/distance_problems/E0217/_index|Problem 217]]. The
[[research/distance_multiplicity_interfaces/exact_optimizers|research account]]
keeps other finite-realization questions separate. No gap remains in this
local statement. The global order-nine existence question remains open here.
