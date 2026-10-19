---
name: problems/divisors/E0693
title: Problem 693
desc: |
  Asks for an estimate of the largest gap between consecutive integers in
  $[n,n^k]$, for fixed $k\ge2$, that have a divisor in $(n,2n)$, and whether it
  is at most $(\log n)^{O(1)}$.
tags:
- Number theory
- Divisors
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 693

[[problems/divisors/_index|..]]

***

**Statement.** Let $k\geq 2$ and $n$ be sufficiently large depending on $k$. Let
$A=\{a_1<a_2<\cdots \}$ be the set of those integers in $[n,n^k]$ which have a
divisor in $(n,2n)$. Estimate

$$
\max_{i} a_{i+1}-a_i.
$$

Is this $\leq (\log n)^{O(1)}$?

**Status.** Open.

**Source.** [erdosproblems.com/693](https://www.erdosproblems.com/693), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #693,
https://www.erdosproblems.com/693.

**Formalization.** None recorded.

## Current assessment

Multiples of $n+1$ give the elementary bound $a_{i+1}-a_i\le n+1$ between
consecutive qualifying integers. A sufficient sharper local condition, for
every relevant integer $u$, is a divisor $n<d<2n$ with

$$
1\le d\left(\left\lfloor\frac ud\right\rfloor+1\right)-u\le H.
$$

This produces a qualifying integer in $(u,u+H]$; endpoint cases must stay
inside the target range.
[[../library/divisors/ford_2008_distribution_integers_divisor_given_interval/theorem_2|Ford's
short-window theorem]], specialized to $y=n$, requires $X\ge n^2$ and length at
least $X/(\log(2n))^{10}$, which is already longer than $n$ eventually. It
therefore does not improve the elementary gap bound in this application. Only
its statement was inspected. A uniform remainder-approximation theorem at
polylogarithmic $H$, not global density, is the missing input.

## Known Results

Not yet compiled.
