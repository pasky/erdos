---
name: problems/additive_bases/E1191
title: Problem 1191
desc: |
  Asks whether every infinite Sidon set $A$ has
  $\lvert A\cap[1,x]\rvert=o\bigl((x/\log x)^{1/2}\bigr)$ along a subsequence,
  and whether some infinite Sidon set has
  $\lvert A\cap[1,x]\rvert\gg x^{1/2}/(\log x)^c$ for some $c>0$.
tags:
- Additive combinatorics
- Sidon sets
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-14T15:30:27Z
---

# Problem 1191

[[problems/additive_bases/_index|..]]

***

**Statement.** Let $A\subset\mathbb{N}$ be an infinite Sidon set. Is it true
that

$$
\liminf_{x\to \infty} \frac{\lvert A\cap [1,x]\rvert}{x^{1/2}}(\log x)^{1/2}=0?
$$

Does there exist an infinite Sidon set $A$ such that

$$
\liminf_{x\to \infty} \frac{\lvert A\cap [1,x]\rvert}{x^{1/2}}(\log x)^c>0
$$

for some $c>0$?

**Status.** Open.

**Source.** [erdosproblems.com/1191](https://www.erdosproblems.com/1191),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1191,
https://www.erdosproblems.com/1191.

**References.**

- [Er80] Erdős, Paul, A survey of problems in combinatorial number theory. Ann.
  Discrete Math. (1980), 89-115.
- [HaRo66] Halberstam, H. and Roth, K. F., Sequences. Vol. I. (1966), xx+291.

**Formalization.** None recorded.

## Current assessment

Current standing is as stated above; the route analysis records a scoped
mathematical comparison.

## Route analysis

The [[research/sidon_extension_interfaces/infinite_density|infinite sidon
density and representation conventions]] account records the following scope.
O’Bryant I (arXiv:2606.28651v3) Theorem 1 at difference cap 1 gives only
liminf<=2/sqrt(log 2), and II (arXiv:2607.23795v1) describes that finite-bound
history.
