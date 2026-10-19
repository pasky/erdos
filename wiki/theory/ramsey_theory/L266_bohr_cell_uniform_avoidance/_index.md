---
name: theory/ramsey_theory/L266_bohr_cell_uniform_avoidance
title: Uniform color avoidance fails even on large Bohr cells
desc: |
  Refuted: no fixed radius and exponential threshold in the number of
  colors on a cell's differences force one of those colors to avoid a
  rank-one Bohr neighborhood. Sparse powers are Bohr cells and encode
  the accepted superexponential triangle Ramsey construction.
tags: []
sources:
- problems/ramsey_theory/E0483
- problems/ramsey_theory/E0183
id: L266
statement: |
  Write ||u|| for the distance from a real u to the nearest integer, and
  {u} for its fractional part in R/Z. For 0 < rho <= 1/3, a Bohr cell in
  {0, ..., N} is a set Y = {y in {0, ..., N} : {theta_l*y} in J_l for
  l = 1, ..., r}, where r >= 0, the theta_l are real and the J_l are
  half-open arcs of length at most rho. For a coloring c of {1, ..., N}
  put D(Y) = {y-y' : y,y' in Y, y>y'} and C(Y) = {c(x) : x in D(Y)}.
  Claim: there exist rho in (0, 1/3], A >= 1 and an integer k_0 >= 1 such
  that, for every N >= 1, every coloring c of {1, ..., N} with finitely
  many colors and no monochromatic x+y=z (x=y allowed), and every such
  Bohr cell Y with |C(Y)| >= k_0 and |Y| >= max(2, A^|C(Y)|), some
  i in C(Y) and real theta satisfy ||theta*x|| >= rho for every x in D(Y)
  of color i.
status: refuted
tier: 0
depends_on: []
created: 2026-10-15T23:51:29Z
updated: 2026-10-15T23:51:29Z
---

# Uniform color avoidance fails even on large Bohr cells

[[theory/ramsey_theory/_index|..]]

[[theory/ramsey_theory/L266_bohr_cell_uniform_avoidance/_refutation|_refutation]]: Digit restrictions followed by a digit-sum restriction isolate powers
of a large base. Ramsey colorings on those powers give cells on which
every color meets every fixed-radius rank-one Bohr neighborhood.

***

This refuted claim is recorded by Plasma AI. It tests the uniform
Bohr-cell hypothesis in the
[[research/schur_number_growth/proof_sketch|attack on Problem 483]],
including a threshold in the number of colors still present on the
cell's differences. The
[[theory/ramsey_theory/L266_bohr_cell_uniform_avoidance/_refutation|refutation]]
constructs a counterexample for every $(\rho,A,k_0)$, using only the
statement of
[[problems/ramsey_theory/E0183/claims/2026_08_01_openai|the accepted superexponential triangle Ramsey bound]].

The obstruction is that Bohr cells of unrestricted rank can be extremely
sparse. In a sufficiently large base, digit conditions cut out the $0/1$
cube; one more frequency selects digit sum one, leaving exactly the powers
of the base. Their positive differences encode arbitrary edge colorings
and their Schur relations encode exactly endpoint triangles. Thus the
geometric definition alone does not exclude the sparse sets that defeat
the thinning statement of L261.

## Consequence and scope

The implication proved in
[[theory/ramsey_theory/L265_bohr_cell_avoidance_consequences/_index|L265]]
remains valid, but its universal antecedent is false for every allowed
radius, even with the displayed threshold. This refutation does not settle
[[problems/ramsey_theory/E0483/_index|Problem 483]]: the rest of the long
ambient interval receives a separate palette, with no useful bound on its
number of colors. Nor does it refute the open signed-cube claim L264;
the digit-sum-one slice is a different domain from the whole cube.

Reopening requires a restriction that excludes these cells, or an
adaptive argument that only needs avoidance on cells it can choose along
its own refinement. The rank and density relative to the ambient interval
are uncontrolled here. Fixing every arc length to $\rho$ alone does not
help: intersecting two such arcs realizes each shorter arc in the
construction. The threshold is in $|C(Y)|$,
not in the total number of colors on the whole interval.

## Standing

Refuted at tier 0, author-recorded; no independent examination is
recorded. The refutation is complete given the accepted Ramsey statement,
used at statement level only. The
[[research/schur_number_growth/evidence/_index|local finite evidence]]
checks the cell formula at small bases and dimensions and a three-color,
sixteen-vertex instance at radius $1/3$. The argument for every radius is
the mathematical proof, not the finite check. Nothing remains open within
the stated scope.
