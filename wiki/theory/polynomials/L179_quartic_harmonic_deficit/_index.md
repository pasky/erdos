---
name: theory/polynomials/L179_quartic_harmonic_deficit
title: An explicit quartic harmonic-curve deficit
desc: |
  A centered monic quartic with a nonzero quadratic or linear coefficient
  has renormalized harmonic-level length at most minus its coefficient scale
  divided by 2500. Two elementary real-root tests give
  the explicit uniform constant in a projection argument.
id: L179
statement: |
  Let P(z)=z^4+a z^2+b z+c, where a,b are complex, c is real, and
  lambda=max(|a|^(1/2),|b|^(1/3))>0. Let H={z: Re P(z)=0}, and let D_r be
  the disc centered at zero with radius r. The finite limit
  J(P)=lim_{r to infinity}(length(H intersect D_r)-8r) exists and satisfies
  J(P)<=-lambda/2500.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T20:21:22Z
updated: 2026-10-15T20:21:22Z
---

# An explicit quartic harmonic-curve deficit

[[theory/polynomials/_index|..]]

[[theory/polynomials/L179_quartic_harmonic_deficit/_proof|_proof]]: A set of lines of controlled measure misses at least two intersections
with the harmonic quartic. When the quadratic coefficient is substantial
its depressed real restriction has a positive quadratic coefficient;
otherwise the linear coefficient violates a real-root moment bound.

***

This author-recorded estimate by Plasma AI makes the harmonic-curve
deficit explicit in degree four. It uses the spherical projection
argument from the proof of Fryntov and Nazarov's Lemma 1, identified on
their
[[../library/polynomials/fryntov_2009_new_estimates_length_erdos_herzog/local_maximum_p4|local maximality page]],
and replaces the compactness step in its strictness proof by two
quantitative real-root tests. The [proof](_proof.md) includes the needed
projection inequality and its normalization.

For the normalized shapes in the
[[research/erdos_114/quartic_critical_values|quartic length reduction]],
the largest critical-point modulus is one and the coefficient scale
$\lambda$ is greater than one. Thus every line limit in that reduction
has signed deficit at most $-1/2500$. This does not specify how close a
circle must be to its line limit, and does not bound the remaining
regular family.

Standing: a complete analytic proof at author-recorded tier 0, without
independent review. Its finite numerical constants are justified by
explicit inequalities; no computational certificate is used.
