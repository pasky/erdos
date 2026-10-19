---
name: theory/polynomials/L186_quartic_critical_value_parameters
title: Compact quartic critical-value parameters
desc: Explicit compact coordinates cover centered monic quartics with unit critical values, including point and value collisions; the unicritical length comparison is also proved.
id: L186
statement: |
  For p(z)=z^4+az^2+bz+c with all critical values of modulus one, its
  critical points u,v,w counted with multiplicity satisfy u+v+w=0,
  p(u)-p(v)=w(u-v)^3, max(|u|,|v|,|w|)<=2, |a|<=24, |b|<=32 and
  |c|<=177. This centered coefficient set is compact. Up to translation
  and p(z) -> exp(-4i theta)p(exp(i theta)z), its generic members are
  s^4(F_t(z/s)-C(t)), where |t|<=1, |1+t|<=1,
  F_t(z)=z^4-2(1+t+t^2)z^2+4t(1+t)z, the critical points
  1,t,-1-t are distinct, the three values f_i at these points are
  noncollinear, C(t) and R(t)>0 are their circumcenter and circumradius,
  and s=R(t)^(-1/4). The remaining members, up to these transformations
  and complex conjugation, are the double-critical-point family
  z^4-6sqrt(h)z^2+8h^(3/4)z+21h/2 +/- i sqrt(1-729h^2/4),
  0<h<=2/27; the distinct-critical-point repeated-value family
  z^4-2sqrt(h)z^2+h/2 +/- i sqrt(1-h^2/4), 0<h<=2; and z^4-1.
  If l(p) is the length of {|p|=1}, then for every complex c,
  l(z^4+c)<=l(z^4-1)=2^(1/4) B(1/2,1/8), with equality exactly
  when |c|=1. No inequality for the other quartic families is asserted.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T17:09:48Z
updated: 2026-10-15T17:09:48Z
---

# Compact quartic critical-value parameters

[[theory/polynomials/_index|..]]

[[theory/polynomials/L186_quartic_critical_value_parameters/_proof|_proof]]: Critical-value differences bound the roots, circumcircles parametrize the generic family, and explicit collision calculations complete the coordinate reduction.

***

The [proof](_proof.md) is author-recorded Plasma AI work, with no independent
review or formal proof attached. It gives a compact parameter domain, a
complete treatment of its collision strata and the comparison for the
single-critical-point family. It consumes no other native claim.

The [[research/erdos_114/quartic_critical_values|quartic research sketch]]
uses these coordinates for [[problems/polynomials/E0114/_index|Problem 114]].
That application separately invokes Eremenko--Hayman's existence and
critical-value deformation results. They are not premises of the elementary
coordinate theorem here. The separate author-recorded comparison
[[theory/polynomials/L181_quartic_collision_pencil_deficits/_index|L181]]
covers both nonunicritical collision families: reflection puts the
double-critical family in the form $s^4F_D(z/s)+c$ with
$s=2h^{1/4}$, and the repeated-value family has the form
$s^4F_E(z/s)+c$ with $s=h^{1/4}$. The unit-critical-value condition
makes the circle with center $-c/s^4$ and radius $s^{-4}$ pass through
the two critical values of the corresponding normalized polynomial.
Thus L181 gives a length deficit greater than $s$ on these families.
The generic comparison and practical neighborhoods of the collision
pencils remain open. The small-curvature result
[[theory/polynomials/L180_quartic_small_curvature_deficit/_index|L180]]
covers an explicit range near the unicritical limit. These applications
are separate from the coordinate theorem and do not change its standing.

**Verification.** Read the integral identity for critical-value differences,
the maximal-root bound, the circumcenter equations, both collision
calculations and the one-variable length comparison. No computation is
needed for this claim, and no gap remains in its stated scope at author
standing. A proof for every monic quartic is outside that scope.
