---
name: problems/arithmetic_functions/E0663
title: Problem 663
desc: |
  Asks whether, for fixed $k$ and large $n$, the least prime not dividing
  $(n+1)\cdots(n+k)$ is less than $(1+o(1))\log n$.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 663

[[problems/arithmetic_functions/_index|..]]

***

**Statement.** Let $k\geq 2$ and $q(n,k)$ denote the least prime which does not
divide $\prod_{1\leq i\leq k}(n+i)$. Is it true that, if $k$ is fixed and $n$ is
sufficiently large, we have

$$
q(n,k)<(1+o(1))\log n?
$$

**Status.** Open.

**Source.** [erdosproblems.com/663](https://www.erdosproblems.com/663), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #663,
https://www.erdosproblems.com/663.

**Formalization.** None recorded.

## Current assessment

For fixed $k$ and $y$, the inequality $q(n,k)>y$ is equivalent to

$$
n\bmod p\in\{-1,\ldots,-k\}\pmod p\quad\text{for every prime }p\le y.
$$

The Chinese remainder theorem gives exactly $\prod_{p\le y}\min(k,p)$
admissible classes modulo $M_y=\prod_{p\le y}p$. Their density is
$\prod_{k<p\le y}k/p=\exp(-y+o(y))$ for fixed $k$, by the prime number theorem.
This average spacing does not bound the least positive representative of any
admissible class.

The elementary product-size estimate gives only $q(n,k)\le(k+o(1))\log n$.
Conversely $n=M_y-1$ has $q(n,k)>y$ and $\log n\sim y$, so coefficient one
would be sharp. The unresolved input is a uniform lower bound of size
$\exp((1-o(1))y)$ for the relevant exceptional representatives, not their
density. These are author-recorded deductions; no CRT enumeration or stronger
sieve result is asserted.

## Known Results

Not yet compiled.
