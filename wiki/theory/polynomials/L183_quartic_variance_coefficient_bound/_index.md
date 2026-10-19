---
name: theory/polynomials/L183_quartic_variance_coefficient_bound
title: An exterior coefficient lower bound for the quartic variance
desc: |
  Five Laurent modes and an orthogonal projection give an explicit lower
  bound for the arclength variance of the quartic length-variation
  polynomial. The bound is strictly below the needed value at the
  unicritical extremizer, so it does not settle the full sign condition.
id: L183
statement: |
  Let p(z)=z^4+a z^2+b z+c have all its critical values on the unit circle.
  Let mu be normalized arclength on {|p|=1}, S=ell(p)/(2 pi), and
  Q(z)=(5/4)z^4+(9a/8)z^2+(7b/8)z+a^2/16+c/2. Put m=E_mu Q,
  A=21a^2/512-9c/32, and
  D=25/16+|a|^2/1024+|b|^2/256+25|ab|^2/16384.
  Then S>1 and Var_mu(Q)>=D/S+|A-m|^2/(S-1).
  At p(z)=z^4+c with |c|=1 the right-hand side is strictly less than
  Var_mu(Q)=1.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T23:06:58Z
updated: 2026-10-15T23:06:58Z
---

# An exterior coefficient lower bound for the quartic variance

[[theory/polynomials/_index|..]]

[[theory/polynomials/L183_quartic_variance_coefficient_bound/_proof|_proof]]: The exterior inverse identifies arclength with a Hardy norm. Polynomial
division fixes five modes of the variation, and orthogonality to the
constant observable bounds the remaining modes. Their nonproportionality
gives strict loss at a unicritical polynomial.

***

This author-recorded result by Plasma AI supplies a finite coefficient
bound for the unresolved variance inequality in the
[[research/erdos_114/quartic_critical_values|quartic length reduction]].
Its [proof](_proof.md) uses the exterior inverse of $p^{1/4}$, Parseval's
identity, and Cauchy--Schwarz on the remaining Laurent modes. The singular
boundary points are included by their integrable Puiseux behavior.

The estimate retains the actual mean $m$. At a stationary member, setting
$m=0$ gives the corresponding necessary coefficient constraint for a
local maximum. The estimate does not classify stationary members or prove
that their variance exceeds one. In particular, this finite projection
does not recover the equality value at the unicritical limit.

Standing: a complete analytic argument at author-recorded tier 0, without
independent review. No computational evidence is required. The variance
sign on the full regular family remains open in the linked research
sketch.
