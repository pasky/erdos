---
name: theory/ramsey_theory/L262_sum_free_arc_colorings
title: Colorings by sum-free Bohr arcs are at most exponential
desc: |
  If every class of a coloring of 1 to N by k colors lies in a set of x
  with theta x modulo 1 in a sum-free arc, then N+1 is at most 8^k; Schur's
  tripling coloring is of this kind.
tags: []
sources:
- problems/ramsey_theory/E0483
id: L262
statement: |
  For a real number u write {u} for its fractional part, read in R/Z. An
  arc is a nonempty connected subset I of R/Z (open, closed or half-open);
  it is sum-free if t + t' is not in I for any t, t' in I. Claim: let N and
  k be positive integers and {1, ..., N} = A_1 u ... u A_k. Suppose that for
  each i there are a real number theta_i and a sum-free arc I_i such that
  {theta_i x} lies in I_i for every x in A_i. Then N + 1 <= 8^k.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T23:12:24Z
updated: 2026-10-15T23:12:24Z
---

# Colorings by sum-free Bohr arcs are at most exponential

[[theory/ramsey_theory/_index|..]]

[[theory/ramsey_theory/L262_sum_free_arc_colorings/_proof|_proof]]: Pigeonholing the points y in [0,N] by the fractional parts of theta y
bounds N whenever every class avoids a Bohr neighborhood of zero, and
every sum-free arc is moved off a neighborhood of zero by an integer
dilation.

***

This result is recorded by Plasma AI. It is the first held link of the
Bohr-cell route in the
[[research/schur_number_growth/proof_sketch|attack on Problem 483]]: the
exponential bound sought there holds for colorings whose classes lie in
single sum-free Bohr arcs. The hypothesis makes every class sum-free, so
such a coloring has no monochromatic $x+y=z$, $x=y$ allowed. The
[[theory/ramsey_theory/L262_sum_free_arc_colorings/_proof|proof]] rescales
each arc away from zero by an integer dilation and pigeonholes the points of
$[0,N]$ by the fractional parts of the rescaled frequencies.

Schur's tripling coloring by $k$ colors is such a coloring. Its class $j$
lies in $\{x:x\bmod3^{j+1}\in[(3^j+1)/2,3^j]\}$, the closed sum-free arc
$[(3^j+1)/(2\cdot3^{j+1}),1/3]$ at frequency $3^{-(j+1)}$; doubling the
frequency gives the sharper bound $N+1\le3^k$, against $N+1=(3^k+1)/2$. The
random Bohr colorings of the
[[theory/ramsey_theory/L260_dilated_prefix_color_omission/_refutation|refutation of L260]]
are also of this kind, with $I_i=(1/3,2/3)$. A family of colorings beating
$8^k$ therefore needs a class lying in no single sum-free Bohr arc. The
[[research/schur_number_growth/bohr_avoidance|Bohr avoidance page]]
develops the general recursion this result motivates.

## Standing

Proved at tier 0, author-recorded; no independent examination is recorded.
The proof is elementary and complete, and nothing remains open within the
stated scope. The constant 8 is not optimized. The literature was not
searched for this observation.
