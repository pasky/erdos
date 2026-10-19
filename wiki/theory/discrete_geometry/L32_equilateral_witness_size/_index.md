---
name: theory/discrete_geometry/L32_equilateral_witness_size
title: Finite equilateral witnesses cannot stay bounded near equal scales
desc: A strip coloring and compactness of bounded connected configurations force any two-scale non-two-colorability witness to grow near scale ratio one.
id: L32
statement: |
  For every positive integer B there is delta>0 such that, for every
  positive x with |x-1|<delta and every planar set P of at most B points,
  P admits a two-coloring with no monochromatic equilateral triangle of
  side length 1 or x. No measurability condition is imposed.
status: proved
tier: 0
depends_on: []
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

# Finite equilateral witnesses cannot stay bounded near equal scales

[[theory/discrete_geometry/_index|..]]

[[theory/discrete_geometry/L32_equilateral_witness_size/_proof|_proof]]: Unit equilateral triangles can be avoided by strips; every bounded witness at nearby scales would limit to an avoidable fixed hypergraph.

***

The [proof](_proof.md) is a complete author-recorded argument by Plasma AI,
without independent review or Lean proof. No external geometric theorem is
needed. This limits a bounded finite-certificate strategy for
[[problems/discrete_geometry/E0173/_index|Problem 173]]; it does not give a
whole-plane coloring avoiding two unequal scales. The
[[research/geometric_configuration_interfaces/colorings|research account]]
distinguishes fixed-pair compactness from a uniform bound on witness size.
No mathematical gap remains in this finite statement. Verification checks
the strip boundaries and the possible coalescence of vertices in the limit.
