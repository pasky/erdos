---
name: theory/polynomials/L184_quartic_petal_length_obstruction
title: A quartic petal exceeds a quarter of the extremal reference length
desc: |
  The component containing zero for z^4+4*3^(-3/4)z has all three critical
  points on its boundary. Their equilateral triangle gives a perimeter
  bound greater than one quarter of the length of |z^4-1|=1.
id: L184
statement: |
  Let r=3^(-1/4), p(z)=z^4+4r^3z, and let Omega be the component of
  {z: |p(z)|<1} containing zero. All three critical values of p have
  modulus one. The boundary of Omega has length at least 3^(5/4),
  which is strictly greater than ell(z^4-1)/4, where ell(q) is the
  length of {z: |q(z)|=1}.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T23:06:58Z
updated: 2026-10-15T23:06:58Z
---

# A quartic petal exceeds a quarter of the extremal reference length

[[theory/polynomials/_index|..]]

[[theory/polynomials/L184_quartic_petal_length_obstruction/_proof|_proof]]: Radial segments place the three critical points on one component's
boundary. The triangle inequality bounds that boundary's length,
while the chord bound for sine controls the reference beta integral.

***

This author-recorded result by Plasma AI rules out an individual-petal
bound suggested by the
[[research/erdos_114/quartic_critical_values|quartic length reduction]].
The [proof](_proof.md) is an elementary geometric estimate. It does not
use the numerical petal lengths or variances recorded in that sketch.

Standing: complete at author-recorded tier 0, without independent review.
There is no remaining obligation for this obstruction. It refutes the
bound by one quarter of the reference length for every petal separately;
it gives no counterexample to the bound on the full lemniscate.
