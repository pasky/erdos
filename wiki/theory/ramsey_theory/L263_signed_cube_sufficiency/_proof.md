---
name: theory/ramsey_theory/L263_signed_cube_sufficiency/_proof
title: Pulling interval colorings back along binary values
desc: |
  The binary value is positive on the half cube, at most 2^r - 1 and
  additive on triples, so the cube's coloring number is at most the Schur
  coloring number of the interval up to 2^r - 1.
created: 2026-10-15T23:12:24Z
updated: 2026-10-15T23:12:24Z
---

***

We prove
[[theory/ramsey_theory/L263_signed_cube_sufficiency/_index|L263]] in the
notation of its statement. The proof is author-recorded by Plasma AI.

Let $\iota_2(v)=\sum_{i=1}^rv_i2^{i-1}$ for $v\in\{-1,0,1\}^r$. If the
last nonzero coordinate of $v$ is $v_j=1$, then
$\iota_2(v)\ge2^{j-1}-\sum_{i<j}2^{i-1}=1$; and $\iota_2(v)\le2^r-1$. So
$\iota_2$ maps $Q_r^+$ into $[1,2^r-1]$, though not injectively. It is
linear, so $v+w=u$ gives $\iota_2(v)+\iota_2(w)=\iota_2(u)$.

Let $n=2^r-1$ and let $\gamma$ be a coloring of $[1,n]$ by $H$ colors with
no monochromatic $x+y=z$. Then $\gamma\circ\iota_2$ colors $Q_r^+$, and a
monochromatic triple $v+w=u$ would give a monochromatic
$\iota_2(v)+\iota_2(w)=\iota_2(u)$. Hence $\chi_r\le H$ whenever
$S(H)\ge2^r-1$.

Now let $k\ge1$ and $r=\lfloor\log_2(S(k)+1)\rfloor\ge1$, so that
$2^r-1\le S(k)<2^{r+1}-1$. By the previous paragraph with $H=k$ and the
hypothesis, $cr\le\chi_r\le k$. Hence
$S(k)+1<2^{r+1}\le2^{k/c+1}$. $\square$
