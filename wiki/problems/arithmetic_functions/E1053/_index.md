---
name: problems/arithmetic_functions/E1053
title: Problem 1053
desc: |
  Asks whether every $k$ with $\sigma(n)=kn$ must satisfy $k=o(\log\log n)$.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 1053

[[problems/arithmetic_functions/_index|..]]

***

**Statement.** Call a number $k$-perfect if $\sigma(n)=kn$, where $\sigma(n)$ is
the sum of the divisors of $n$. Must $k=o(\log\log n)$?

**Status.** Open.

**Source.** [erdosproblems.com/1053](https://www.erdosproblems.com/1053),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1053,
https://www.erdosproblems.com/1053.

**References.**

- [Gu04] Guy, Richard K., Unsolved problems in number theory. Third edition,
  Problem Books in Mathematics, Springer, New York (2004), xviii+437 pp.;
  doi:10.1007/978-0-387-26677-0. Section B2, p. 78, records the multiperfect
  counts known at the end of 2002 and "Can $k$ be as large as we wish? Erdős
  conjectured that $k=o(\ln\ln n)$." Library home:
  [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]].

**Formalization.** None recorded.

## Current assessment

Here $k$ is a positive integer allowed to vary with $n$. A theorem for
each fixed $k$ cannot establish the requested uniform little-o bound:
fixed $k$ already has $k/\log\log n\to0$. Bounded $\omega(n)$ also
only addresses a restricted range, since
$\sigma(n)/n\le\prod_{p\mid n}(1-1/p)^{-1}$ then bounds $k$.
The held historical account does not supply the needed saving for
varying $k$; no complete current-literature audit is asserted here.

Integrality is essential to such a saving. To see this, let
$Q_y=\prod_{p\le y}p$. Then

$$
\frac{\sigma(Q_y)}{Q_y}
=\prod_{p\le y}(1-p^{-2})
 \prod_{p\le y}(1-p^{-1})^{-1}
\ge\frac12\sum_{m\le y}\frac1m.
$$

The first product is at least
$\prod_{m\ge2}(1-m^{-2})=1/2$. Expanding the second product includes
every $1/m$ for $m\le y$. Also $\log Q_y\le y\log y$, so
$\log\log Q_y\le\log y+\log\log y$. Consequently
$\sigma(Q_y)/Q_y$ is not $o(\log\log Q_y)$.

These values are nonintegral once the largest prime $q\mid Q_y$ exceeds
$3$. No factor $p+1$ with prime $p\le q$ is divisible by $q$:
for $p<q$ this would force $p+1=q$ and the even prime $p=q-1=2$,
whereas $p=q$ gives $q+1$. Thus $q$ cannot cancel from the denominator
of $\prod_{p\le y}(p+1)/p$. This author-recorded argument of Plasma AI
is an obstruction to discarding integrality, not a counterexample to
the problem. It has not been independently reviewed. A useful next
estimate must exploit integrality with the multiplier unbounded, rather
than use only a general maximal-order bound or a fixed-$k$ classification.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]]

<!-- END problem library links -->
