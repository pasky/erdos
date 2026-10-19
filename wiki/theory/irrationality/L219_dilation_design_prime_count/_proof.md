---
name: theory/irrationality/L219_dilation_design_prime_count/_proof
title: Proof that cancelling dilation designs need many primes
desc: |
  Each vertex needs a fiber-mate at every cancelled level; the mates are
  distinct, and admissibility forces their primes to be distinct.
tags: []
sources:
- theory/irrationality/L219_dilation_design_prime_count/_index
created: 2026-10-15T20:31:18Z
updated: 2026-10-15T20:31:18Z
---

***

This proves the entire statement of
[[theory/irrationality/L219_dilation_design_prime_count/_index|L219]] at
author-recorded tier 0. Say that distinct $u,w\in V$ *meet at level $h$*
when $p_uh-s_u=p_wh-s_w$.

If $p_u=p_w$, meeting at any level forces $s_u=s_w$, which the distinct
pairs exclude; so vertices with the same prime never meet. If
$p_u\ne p_w$, they meet at most at one level, since meeting at levels
$h\ne h'$ gives $(p_u-p_w)(h-h')=0$.

Fix $v\in V$. For each $h\le K$ the hypothesis at $m=p_vh-s_v$ says that the
weights of the vertices $w$ with $p_wh-s_w=m$ sum to zero. This set contains
$v$, and $c_v\ne0$, so it contains some $u_h\ne v$, which meets $v$ at level
$h$. By the previous paragraph, $p_{u_h}\ne p_v$, and the vertices
$u_1,\dots,u_K$ are distinct.

Suppose $p_{u_h}=p_{u_{h'}}=p'$ for some $h\ne h'$. Subtracting
$p_vh-s_v=p'h-s_{u_h}$ from $p_vh'-s_v=p'h'-s_{u_{h'}}$ gives

$$
s_{u_h}-s_{u_{h'}}=(p_v-p')(h'-h).
$$

The admissible $n$ satisfies $n\equiv s_{u_h}$ and $n\equiv s_{u_{h'}}$
modulo $p'$, so $p'$ divides $(p_v-p')(h'-h)$. Being prime, $p'$ divides
$p_v-p'$, hence $p_v$, or it divides $h'-h$. The first is impossible because
$p_v\ne p'$ are primes, and the second because $0<|h'-h|<K<p'$. Thus
$p_v,p_{u_1},\dots,p_{u_K}$ are $K+1$ distinct primes, each greater than
$K$, and the product of all distinct
$p_w$ is at least their product, which exceeds $K^{K+1}$. $\square$
