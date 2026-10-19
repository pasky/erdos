---
name: theory/polynomials/L182_quartic_critical_value_mixtures
title: Critical-value mixtures fail for quartic inverse densities
desc: |
  Arbitrarily near a unicritical quartic, a quartic with three distinct unit
  critical values admits no pointwise upper bound by a convex combination
  of unicritical inverse densities centered at those values. Two opposite
  tails of an explicit collision limit give the obstruction.
id: L182
statement: |
  For every epsilon>0 there is a centered monic quartic
  p(z)=z^4+a z^2+b z+c with max(|a|,|b|,|c+i|)<epsilon and three pairwise
  distinct critical values v_1,v_2,v_3 of modulus one, such that for every
  triple of real numbers alpha_j>=0 with alpha_1+alpha_2+alpha_3=1 there
  exists zeta of modulus one, different from all v_j, for which
  sum_{p(z)=zeta} 1/|p'(z)| > sum_{j=1}^3 alpha_j |zeta-v_j|^(-3/4).
  The weights may depend on p but are fixed as zeta varies.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T23:06:58Z
updated: 2026-10-15T23:06:58Z
---

# Critical-value mixtures fail for quartic inverse densities

[[theory/polynomials/_index|..]]

[[theory/polynomials/L182_quartic_critical_value_mixtures/_proof|_proof]]: Exact inverse derivatives for z^4-2z^2 give incompatible far-tail
requirements. A strict two-point inequality persists on nearby circles
and under an explicit regular perturbation of the critical points.

***

This author-recorded result by Plasma AI rules out a possible repair of the
pointwise comparison in the
[[research/erdos_114/quartic_critical_values|quartic length reduction]].
Each reference density in the statement integrates over the unit circle
to the length of $|z^4-1|=1$. A pointwise majorant with fixed nonnegative
weights summing to one would therefore prove the desired length bound.
The [proof](_proof.md) shows that no choice of these weights works for
certain regular quartics arbitrarily close to $z^4-i$.

The proof is analytic: it computes the two far tails for $F(z)=z^4-2z^2$,
passes their strict obstruction to large circles through its critical
values, and then perturbs to three distinct critical values. It does not
use numerical quadrature or a finite sample as evidence.

Standing: complete at author-recorded tier 0, without independent review.
There is no remaining obligation for this obstruction. It does not refute
the quartic length inequality, an integrated comparison, or a comparison
using reference centers away from the critical values.
