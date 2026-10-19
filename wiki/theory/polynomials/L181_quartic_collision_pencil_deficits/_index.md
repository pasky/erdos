---
name: theory/polynomials/L181_quartic_collision_pencil_deficits
title: Strict deficit on both quartic collision pencils
desc: |
  Certified ball arithmetic bounds the rotated length-deficit integral
  strictly below -1 on every circle and line through the critical values of
  either normalized quartic collision stratum. The strict bound is uniform
  up to the flattening limit.
id: L181
statement: |
  Let F_D(z)=z^4-(3/2)z^2-z and F_E(z)=z^4-2z^2. For F_D let
  (f_A,f_B)=(-3/2,3/16), and for F_E let (f_A,f_B)=(-1,0).
  For either F and every circle or line Gamma through f_A and f_B, put
  G_F(sigma)=sum_{F(z)=sigma}1/|F'(z)| away from the critical values.
  Then the absolutely convergent integral over Gamma of
  (G_F(sigma)-|sigma-f_A|^(-3/4)) |d sigma| is strictly less than -1.
  In particular, if Gamma is a circle with center C and radius R, the
  centered monic quartic p(z)=R^(-1)F(R^(1/4)z)-C/R satisfies
  ell(p)<ell(z^4-1)-R^(-1/4), where ell is lemniscate length.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T20:30:28Z
updated: 2026-10-15T20:30:28Z
---

# Strict deficit on both quartic collision pencils

[[theory/polynomials/_index|..]]

[[theory/polynomials/L181_quartic_collision_pencil_deficits/_proof|_proof]]: The two fixed quartics have two real critical values. Conjugation reduces
each pencil to a compact angle interval, on which the retained program
certifies the signed integral. Scaling the inverse images gives the
claimed length inequality.

***

This computer-assisted, author-recorded result by Plasma AI covers the
double-critical-point and equal-critical-value strata of the
[[research/erdos_114/quartic_critical_values|quartic reduction]].
The [proof](_proof.md) gives the circle parametrization, identifies the
exact checked integral, and explains the passage to polynomial length.

The canonical executable evidence is retained in the
[[research/erdos_114/quartic_evidence/_index|collision-strata account]],
at `wiki/research/erdos_114/quartic_evidence/evidence/main.py`.
It reads no external inputs and checks all parameter boxes using balls
and certified root discs. Its full replay, including the two line-limit
controls, is the computational obligation of this claim. The floating-point
landscape probe in that folder is not part of its proof.

The certificate gives strictness on the pencils themselves. Their
two-dimensional neighborhoods and the regular complement are different
subjects. Standing: proved at author-recorded tier 0, with no independent
soundness examination of the enclosure engine or whole-statement bridge.
The degree-four inequality remains open in the linked sketch.
