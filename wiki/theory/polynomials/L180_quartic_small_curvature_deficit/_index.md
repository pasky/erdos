---
name: theory/polynomials/L180_quartic_small_curvature_deficit
title: A uniform signed quartic deficit at small curvature
desc: |
  Explicit root-window and far-field estimates transfer a quantitative
  harmonic-line deficit to every sufficiently flat circle, uniformly over
  centered quartic shapes whose largest critical-point modulus is one.
  The curvature cutoff is explicit and very small.
id: L180
statement: |
  Put d=1/2500, K=100000, T_0=65536, eta=(d/6000)^4,
  T=max(2T_0,(128K/(3d))^(4/3)), B=T+12, m=eta^3/B^9, M=13B^2, and
  kappa_0=min(1/T,2eta/T^2,d m^3/(32M T^3),
               sqrt(d m/(32T^3)),sqrt(9d/(20T^(9/4)))).
  Let F(z)=z^4+a z^2+b z have largest critical-point modulus one, and let
  sigma_0 be any of its critical values. For any circle Gamma through
  sigma_0 with curvature magnitude at most kappa_0, or any line Gamma
  through sigma_0, define G_F(sigma)=sum_{F(z)=sigma} 1/|F'(z)| away from
  critical values. The absolutely convergent signed integral
  integral_Gamma (G_F(sigma)-|sigma-sigma_0|^(-3/4)) |d sigma|
  is at most -1/5000. No separation of the critical points or values is
  assumed.
status: proved
tier: 0
depends_on: [L179]
created: 2026-10-15T20:21:22Z
updated: 2026-10-15T20:21:22Z
---

# A uniform signed quartic deficit at small curvature

[[theory/polynomials/_index|..]]

[[theory/polynomials/L180_quartic_small_curvature_deficit/_proof|_proof]]: Uniform inverse-series bounds control the signed tails. On a bounded
target interval, fourth-root coverings control all singular windows and
a resultant bounds the inverse derivatives on their complement. The
resulting explicit modulus transfers the negative harmonic-line bound.

***

This author-recorded result by Plasma AI gives a uniform negative
leading coefficient near the unicritical limit in the
[[research/erdos_114/quartic_critical_values|quartic length reduction]].
For a circle of radius $R$, write $s=R^{-1/4}$ for the polynomial's
scale. The exact length identity in that reduction turns this estimate
into $\ell(p)\le\ell(z^4-1)-s/5000$ whenever the stated curvature
bound holds.

The [proof](_proof.md) uses the explicit line deficit
[[theory/polynomials/L179_quartic_harmonic_deficit/_index|L179]].
Small windows are controlled by covering the full preimage of a target
disc with four discs of radius proportional to its fourth root. This
continues to work when critical points or values collide. A quantitative
estimate on the regular part and a uniform inverse-series estimate at
infinity complete the comparison.

The cutoff is deliberately coarse and is not a practical mesh size for
a certificate on the remaining parameter set. The separate claim
[[theory/polynomials/L181_quartic_collision_pencil_deficits/_index|L181]]
covers the collision pencils at all curvatures at author standing;
practical neighborhoods of those pencils and the regular complement
remain open.
Standing: a complete analytic proof at author-recorded tier 0, without
independent review; no executable evidence is used.
