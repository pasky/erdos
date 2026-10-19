---
name: research/factorial_sum_valuation_tree
title: Finite congruence levels for sums of factorials
desc: |
  A complete cutoff at each p-adic precision, the compactness equivalence
  for unbounded factorial-sum valuations, and the exact example f(4,2) = 6.
tags: []
sources: []
created: 2026-10-14T20:10:13Z
updated: 2026-10-14T20:10:13Z
---

# Finite congruence levels for sums of factorials

***

Fix an integer $a\ge1$ and a prime $p$, as in
[[problems/factorials_binomials/E0404/_index|Problem 404]]. The following
reductions are author-recorded arguments of Plasma AI, without independent
review. They give no pair $(a,p)$ with unbounded valuation.

Put $t_K=\min\{t:v_p(t!)\ge K\}$. If $K>v_p(a!)$, then
$a<t_K\le pK$. All factorials of index at least $t_K$ vanish modulo
$p^K$. Hence a sum of distinct factorials beginning with $a!$ can be
divisible by $p^K$ if and only if a subset of
$\{a,\ldots,t_K-1\}$ containing $a$ has factorial sum zero modulo
$p^K$. This is an exhaustive finite decision. If $K\le v_p(a!)$,
the singleton $a!$ already works.

Unboundedness at this fixed pair is equivalent to an infinite increasing
sequence beginning with $a$ whose partial sums have valuations tending to
infinity. Indeed, represent a choice by $(x_i)_{i\ge a}\in\{0,1\}^{\mathbb N}$
with $x_a=1$. The congruence at precision $K$ constrains only finitely
many coordinates. Unboundedness makes each such closed set $C_K$
nonempty, and $C_{K+1}\subseteq C_K$. Compactness, or a diagonal
subsequence of finite choices, supplies a choice in every $C_K$. Its
support is infinite: a finite positive factorial sum cannot be divisible
by every power of $p$. For each fixed $K$, once the selected indices have
passed $t_K$, every subsequent partial sum is zero modulo $p^K$.
Thus its valuations tend to infinity. Conversely, the finite partial
sums of any such sequence give unbounded valuations at its first index.

If $p\mid a+1$, every factorial of index greater than $a$ has valuation
strictly above $v_p(a!)$. Every allowed sum then has valuation exactly
$v_p(a!)$, so $f(a,p)=v_p(a!)$.

For another exact example, modulo $128$ the only potentially nonzero
terms of index at least $4$ are

$$
4!\equiv24,\qquad5!\equiv120,\qquad
6!\equiv80,\qquad7!\equiv48.
$$

Adding $24$ to the eight subset sums of $\{120,80,48\}$ gives
$24,16,104,72,96,64,24,16$ modulo $128$. None is zero, whereas
$4!+5!+7!=5184=2^6\cdot81$. Thus $f(4,2)=6$.

The general remaining obligation is a lifting or survival argument at
every precision for one fixed pair, or a finite level with no admissible
choice. Larger individual lower witnesses do not establish infinite
survival. The separate reported tables and lower bounds on the problem's
claim pages retain their stated pending standing; this argument does not
replay them.
