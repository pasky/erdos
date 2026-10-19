---
name: theory/polynomials/L176_quartic_constant_term_comparison
title: A quartic obstruction to comparison at the same constant term
desc: |
  An explicit family of centered monic quartics with three distinct unit
  critical values tends to z^4+1 while its lemniscate is longer than that of
  the unicritical quartic with the same constant term. A positive scaled
  limiting difference is proved by a geometric estimate on a harmonic curve.
id: L176
statement: |
  Write ell(q) for the Euclidean length of {z in C: |q(z)|=1}. Set
  Y=sqrt(9/4+3 sqrt(3)/2). For y>Y define
  F_y(z)=z^4+(2y^2-3/2)z^2-(1+4y^2)z,
  d_y=y^4-(9/2)y^2-27/16, v_y=-3/2-2y^2,
  R_y=(d_y^2+16y^6)/(2d_y), C_y=v_y-R_y, and
  p_y(z)=R_y^(-1)F_y(R_y^(1/4)z)-C_y/R_y.
  Then p_y is centered and monic, its three critical points and three
  critical values are each distinct, all its critical values have modulus
  one, and p_y tends coefficientwise to z^4+1 as y decreases to Y.
  Moreover the limit of R_y^(1/4)(ell(p_y)-ell(z^4+p_y(0))) exists and is
  strictly greater than 31/20. In particular ell(p_y)>ell(z^4+p_y(0)) for
  every y>Y sufficiently close to Y.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T20:21:22Z
updated: 2026-10-15T20:21:22Z
---

# A quartic obstruction to comparison at the same constant term

[[theory/polynomials/_index|..]]

[[theory/polynomials/L176_quartic_constant_term_comparison/_proof|_proof]]: Critical values give an explicit family of flattening circles. A lower
bound for the length of a harmonic tree makes the limiting comparison
with the same constant term positive, and uniform local and far-field
estimates transfer this sign to the quartic family.

***

This author-recorded result by Plasma AI disproves the proposed inequality
$\ell(p)\le\ell(z^4+p(0))$ even for quartics with three distinct critical
values on the unit circle, arbitrarily close to a unicritical extremizer.
It does not refute the degree-four lemniscate conjecture: the polynomial
used for comparison has a constant term of modulus greater than one and
has length strictly below $\ell(z^4-1)$.

The [proof](_proof.md) is analytic. Its main estimate bounds the eight
unbounded arcs and two finite edges of an explicitly specified harmonic
curve from below. A uniform inverse-branch estimate passes from this curve
to nearby quartic lemniscates. No numerical quadrature or computational
certificate is used.

The
[[research/erdos_114/quartic_critical_values|quartic research sketch]]
explains the failed comparison and the replacement that compares directly
with $z^4-1$. The result does not consume the cubic length claim or any
other native claim.

Standing: a complete author-recorded proof, without independent review.
Verification consists of checking the critical-value calculation, the
finite-tree length estimate, and the uniform passage to the line integral
in the proof. There is no remaining mathematical obligation for the stated
obstruction; the quartic upper bound remains open in the linked sketch.
