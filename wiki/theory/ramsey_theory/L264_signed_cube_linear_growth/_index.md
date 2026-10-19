---
name: theory/ramsey_theory/L264_signed_cube_linear_growth
title: The signed cube needs linearly many colors
desc: |
  Open: coloring the vectors of {-1,0,1}^r with last nonzero coordinate 1
  so that no class contains v, w and v+w needs at least c r colors; by L263
  this would make the Schur forcing threshold exponential.
tags: []
sources:
- problems/ramsey_theory/E0483
id: L264
statement: |
  For r >= 1 let Q_r^+ be the set of vectors in {-1, 0, 1}^r whose last
  nonzero coordinate is 1, and let chi_r be the least number of colors in a
  coloring of Q_r^+ with no monochromatic v, w, u in Q_r^+ satisfying
  v + w = u coordinatewise. Claim: there is a real number c > 0 such that
  chi_r >= c*r for every r >= 1.
status: open
depends_on: []
created: 2026-10-15T23:12:24Z
updated: 2026-10-15T23:12:24Z
---

# The signed cube needs linearly many colors

[[theory/ramsey_theory/_index|..]]

***

This open claim is recorded by Plasma AI. By
[[theory/ramsey_theory/L263_signed_cube_sufficiency/_index|L263]] it
implies the exponential bound $f(k)\le2^{k/c+1}$ that
[[problems/ramsey_theory/E0483/_index|Problem 483]] asks for, and by
[[theory/ramsey_theory/L265_bohr_cell_avoidance_consequences/_index|L265]]
the uniform Bohr-cell hypothesis would imply it. That hypothesis is
refuted in L266, independently of this claim, as the
[[research/schur_number_growth/proof_sketch|research sketch]] explains.
Whether the exponential Schur bound implies the claim is unresolved here.

Equivalently, $\chi_r$ is the least number of colors in a triangle-free
coloring of the edges of the complete graph on $\{0,1\}^r$ in which the
color of $\{x,y\}$ depends only on $\pm(y-x)$. General triangle-free
colorings of that graph need only $o(r)$ colors, by
[[problems/ramsey_theory/E0183/claims/2026_08_01_openai|the accepted claim on Problem 183]],
so the claim asserts that invariance under differences costs a factor that
grows without bound.

## Standing

Open in these notes; neither a proof nor a counterexample is established. The
[[research/schur_number_growth/signed_cube_reduction|signed-cube page]]
records the evidence: $\chi_1,\ldots,\chi_7=1,2,3,3,4,5,5$; the bound
$\chi_r\le0.584\,r+O(1)$ through binary values and the Schur colorings of
Ageron et al.; the bound through sum-free colorings of
$\mathbb F_2^r\setminus\{0\}$, whose linear growth is itself an open
conjecture that Hunter and Pohoata record (arXiv:2309.02424v2, p. 11);
subadditivity; and the Ramsey lower bound
$\chi_r\ge(1-o(1))\,r\log2/\log r$, which no argument through general
triangle-free colorings can raise above $o(r)$. So any constant $c$ in the
claim is at most about $0.584$. Two web searches on 2026-10-15 found no
treatment of this coloring number; they are not exhaustive.

## Remaining obligations

- [ ] Prove or refute the claim. The refutation of uniform Bohr-cell
  avoidance does not decide it: that construction colors a slice of the
  cube, not the whole cube.
- [ ] A family of sum-free colorings of $\mathbb F_2^n\setminus\{0\}$ by
  $k$ colors with $n/k\to\infty$ would refute the claim through the
  support map; the claim needs the conjectured linear bound for those
  colorings.
- [ ] The first value not determined by the arguments here is
  $\chi_8\in\{5,6\}$; a five-coloring
  would also give $R_5(3)>256$.
