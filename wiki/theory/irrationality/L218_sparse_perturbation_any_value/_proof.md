---
name: theory/irrationality/L218_sparse_perturbation_any_value/_proof
title: Proof that sparse small totient changes reach every value
desc: |
  Greedy rounding at each changed place keeps the remaining error below
  2^(s-e-1), so the next change is at most 2^(s+g), which is at most e^(1/2).
tags: []
sources:
- theory/irrationality/L218_sparse_perturbation_any_value/_index
created: 2026-10-15T20:31:18Z
updated: 2026-10-15T20:31:18Z
---

***

This proves the entire statement of
[[theory/irrationality/L218_sparse_perturbation_any_value/_index|L218]] at
author-recorded tier 0. Write $S=\sum_{n\ge1}\varphi(n)2^{-n}$, which
converges absolutely since $0<\varphi(n)\le n$, and write
$\lfloor x\rceil$ for an integer nearest to $x$.

Choose the $\delta_k$ in turn. Put $\eta_0=r-S$ and, for $k\ge1$,

$$
\delta_k=2^{s(e_k)}\left\lfloor\eta_{k-1}2^{e_k-s(e_k)}\right\rceil,
\qquad
\eta_k=\eta_{k-1}-\delta_k2^{-e_k}.
$$

Item 1 holds by construction. Since
$\eta_k=2^{s(e_k)-e_k}\bigl(x-\lfloor x\rceil\bigr)$ with
$x=\eta_{k-1}2^{e_k-s(e_k)}$, every $k\ge1$ satisfies

$$
|\eta_k|\le2^{s(e_k)-e_k-1}.
\tag{1}
$$

For $k\ge2$, rounding gives
$|\delta_k|\le|\eta_{k-1}|2^{e_k}+2^{s(e_k)-1}$. By (1) at $k-1$, the gap
condition $e_k-e_{k-1}\le g(e_{k-1})$, and the monotonicity of $s$ and $g$,

$$
|\delta_k|\le2^{s(e_{k-1})+g(e_{k-1})-1}+2^{s(e_k)-1}
\le2^{s(e_k)+g(e_k)}\le e_k^{1/2},
$$

the last step because $e_k\ge n_0$. This is item 2.

For item 3, the bounds $|\psi(n)|\le n$ off the $e_k$, $|\delta_k|\le
e_k^{1/2}$ for $k\ge2$ and the single term $\delta_1$ make
$\sum_n|\psi(n)|2^{-n}$ finite. Rearranging the absolutely convergent
series,

$$
\sum_{n\ge1}\psi(n)2^{-n}=S+\sum_{i\ge1}\delta_i2^{-e_i}
=r-\eta_k+\sum_{i>k}\delta_i2^{-e_i}
$$

for every $k\ge1$, by the definition of the $\eta_i$. As $k\to\infty$,
$\eta_k\to0$ by (1), since $s(e_k)\le\frac12\log_2e_k$ gives
$|\eta_k|\le e_k^{1/2}2^{-e_k-1}$, and the last sum tends to $0$ as the
tail of a convergent series. Hence the sum equals $r$. $\square$
