---
name: theory/ramsey_theory/L263_signed_cube_sufficiency
title: A linear coloring bound for signed cubes gives exponential Schur numbers
desc: |
  If the coloring number of the signed cube of dimension r, under vector
  addition, is at least c r for every r, then the Schur forcing threshold
  f(k) is at most 2^(k/c+1).
tags: []
sources:
- problems/ramsey_theory/E0483
id: L263
statement: |
  For r >= 1 let Q_r^+ be the set of vectors in {-1, 0, 1}^r whose last
  nonzero coordinate is 1, and let chi_r be the least number of colors in a
  coloring of Q_r^+ with no monochromatic v, w, u in Q_r^+ satisfying
  v + w = u coordinatewise. Let S(k) be the largest N such that
  {1, ..., N} has a coloring by at most k colors with no monochromatic
  solution of x + y = z (x = y allowed). Claim: if c > 0 and chi_r >= c*r
  for every r >= 1, then S(k) + 1 <= 2^(k/c + 1) for every k >= 1.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T23:12:24Z
updated: 2026-10-15T23:12:24Z
---

# A linear coloring bound for signed cubes gives exponential Schur numbers

[[theory/ramsey_theory/_index|..]]

[[theory/ramsey_theory/L263_signed_cube_sufficiency/_proof|_proof]]: The binary value is positive on the half cube, at most 2^r - 1 and
additive on triples, so the cube's coloring number is at most the Schur
coloring number of the interval up to 2^r - 1.

***

This result is recorded by Plasma AI. It turns the signed cube into a
model problem for [[problems/ramsey_theory/E0483/_index|Problem 483]]:
the hypothesis is the open claim
[[theory/ramsey_theory/L264_signed_cube_linear_growth/_index|L264]], and
the conclusion is the exponential bound $f(k)=S(k)+1<C^k$ asked there.
The [[theory/ramsey_theory/L263_signed_cube_sufficiency/_proof|proof]]
pulls a Schur-free coloring of $[1,2^r-1]$ back to $Q_r^+$ along the binary
value $\sum_iv_i2^{i-1}$, so $\chi_r$ is at most the least number of
sum-free classes covering $[1,2^r-1]$.

The converse is unresolved here: a Schur coloring of an interval pulls
back to the cube; this gives no extension theorem for cube colorings. By
[[theory/ramsey_theory/L265_bohr_cell_avoidance_consequences/_index|L265]],
the hypothesis would also follow from uniform Bohr-cell avoidance. That
universal avoidance statement is refuted in L266; this does not decide
the signed-cube hypothesis. The
[[research/schur_number_growth/signed_cube_reduction|signed-cube page]]
records the known bounds and small values of $\chi_r$.

## Standing

Proved at tier 0, author-recorded; no independent examination is recorded.
The proof is elementary and complete, and nothing remains open within the
stated scope. The literature was not searched for $\chi_r$.
