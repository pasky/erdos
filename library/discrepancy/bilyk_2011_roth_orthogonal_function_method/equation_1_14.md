---
name: discrepancy/bilyk_2011_roth_orthogonal_function_method/equation_1_14
title: "Equation (1.14): Halász's planar L1 discrepancy bound"
desc: |
  The counting discrepancy of every planar N-point set has L1 norm at
  least an absolute constant times the square root of log N.
created: 2026-10-15T05:59:54Z
updated: 2026-10-15T05:59:54Z
---

***

For a set $P_N\subset[0,1]^2$ of $N\ge2$ points, put

$$
D_N(u,v)=\#\bigl(P_N\cap([0,u)\times[0,v))\bigr)-Nuv.
$$

The [[discrepancy/bilyk_2011_roth_orthogonal_function_method/_index|source]]
states Halász's bound

$$
\int_0^1\int_0^1 |D_N(u,v)|\,du\,dv\ge c\sqrt{\log N}
$$

with an absolute $c>0$. It uses counting discrepancy, without division by $N$.
The definition is (1.4), p. 145; the bound is (1.14), p. 148; the complex
Riesz product proof outline is (4.15)--(4.17), p. 169. Definitions and statement
are claims checked; the full argument has not been reverified.

**Bears on.** [[../wiki/problems/analysis/E1221/_index|Problem 1221]]:
the localized planar sets in
[[../wiki/research/erdos_1221/ko26b_lemma_7_2_reconstruction|Lemma 7.2]]
have distinct time coordinates. Changing strict to non-strict rectangle
boundaries changes the integrand only on finitely many lines, preserving the
integral. The source interface therefore matches this imported inequality;
the remaining consecutive-gap argument retains its own standing.
