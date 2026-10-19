---
name: theory/ramsey_theory/L265_bohr_cell_avoidance_consequences
title: Uniform Bohr-cell avoidance would bound Schur numbers and signed cubes
desc: |
  If every Schur-free coloring has, on every Bohr cell of radius rho, a
  color of the cell's differences avoiding some rank-one neighborhood of
  radius rho, then f(k) is at most ceil(1/rho)^k, and the signed-cube
  coloring number grows at least linearly.
tags: []
sources:
- problems/ramsey_theory/E0483
id: L265
statement: |
  Let rho be a real number with 0 < rho <= 1/3 and let q be the least
  integer >= 1/rho. For a real u let ||u|| be its distance to the nearest
  integer and {u} its fractional part, read in R/Z. A Bohr cell in
  {0, ..., N} is a set {y in {0, ..., N} : {theta_l y} in J_l for
  l = 1, ..., r} for some r >= 0, real numbers theta_l and arcs J_l of R/Z
  of length at most rho. For a set Y of integers let
  D(Y) = {y - y' : y, y' in Y, y > y'}. A coloring of {1, ..., N} has
  property (B) if every Bohr cell Y in {0, ..., N} with at least two
  elements has a color i occurring on D(Y) and a real number theta such
  that no x in D(Y) of color i has ||theta x|| < rho. Let S(k) be the
  largest N such that {1, ..., N} has a coloring by at most k colors with no
  monochromatic solution of x + y = z (x = y allowed). For r >= 1 let Q_r^+
  be the set of vectors in {-1, 0, 1}^r whose last nonzero coordinate is 1,
  and let chi_r be the least number of colors in a coloring of Q_r^+ with
  no monochromatic v, w, u in Q_r^+ satisfying v + w = u coordinatewise.
  Claim: if every coloring of every {1, ..., N} with no monochromatic
  solution of x + y = z (x = y allowed) has property (B), then
  (1) S(k) + 1 <= q^k for every k >= 1, and (2) chi_r >= r*log(2)/log(q)
  for every r >= 1.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T23:12:24Z
updated: 2026-10-15T23:12:24Z
---

# Uniform Bohr-cell avoidance would bound Schur numbers and signed cubes

[[theory/ramsey_theory/_index|..]]

[[theory/ramsey_theory/L265_bohr_cell_avoidance_consequences/_proof|_proof]]: Refinement by the best arc keeps a 1/q fraction of a Bohr cell and
removes a color from its differences; digit cubes in base q+1 are Bohr
cells that carry the signed cube's vector addition exactly.

***

This conditional result is recorded by Plasma AI. Property (B) is the
uniform hypothesis tested in the
[[research/schur_number_growth/proof_sketch|attack on Problem 483]]. Its
universal form is false for every allowed radius, by the refuted claim
[[theory/ramsey_theory/L266_bohr_cell_uniform_avoidance/_index|L266]].
The implication here remains valid; it supplies no unconditional bound.
Conclusion (1) is the exponential bound that
[[problems/ramsey_theory/E0483/_index|Problem 483]] asks for, so the route
would succeed if (B) held for every Schur-free coloring. Conclusion (2)
shows what that would cost: it forces the open claim
[[theory/ramsey_theory/L264_signed_cube_linear_growth/_index|L264]], which
by [[theory/ramsey_theory/L263_signed_cube_sufficiency/_index|L263]]
already implies the exponential bound on its own.

The [[theory/ramsey_theory/L265_bohr_cell_avoidance_consequences/_proof|proof]]
refines a cell by the best arc of length $1/q$ at the frequency the
hypothesis supplies, which keeps a $1/q$ fraction of the cell and removes a
color from its differences. For (2) it plants a coloring of the signed
cube on the base-$(q+1)$ digits $\{-1,0,1\}$, where the digit cube is a
Bohr cell whose differences carry exactly the cube's vector addition.

## Scope

- Property (B) is quantified over every Bohr cell. A recursion that only
  asserts avoidance on cells it chooses along its own path is not
  covered by (2), which plants an arbitrary cube coloring in a prescribed
  cell. Such an adaptive recursion needs its own preservation argument.
- The planted coloring of (2) is consistent with an exponential bound,
  since its second palette needs about as many colors as $[1,N]$ itself.
  So (2) gives no lower bound for Schur numbers.
- Arc colorings, as in
  [[theory/ramsey_theory/L262_sum_free_arc_colorings/_index|L262]], have
  property (B) with radius $1/8$. This restricted positive result survives
  the refutation of the hypothesis for general Schur-free colorings.
- The threshold variant proved below also has a false universal
  antecedent: L266 covers every fixed threshold $A^{|C(Y)|}$. It does not
  refute the open linear bound for $\chi_r$, since a digit-sum-one slice
  need not support a coloring of the full signed cube.

## Standing

Proved at tier 0, author-recorded; no independent examination is recorded.
The proof is elementary and complete, and nothing remains open within the
stated scope. The [[research/schur_number_growth/evidence/_index|research evidence]]
checks the digit-cube and embedding facts of the proof for $r\le5$; they are
proved for every $r$.
