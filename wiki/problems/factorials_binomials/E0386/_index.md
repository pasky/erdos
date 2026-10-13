---
name: problems/factorials_binomials/E0386
title: Problem 386
desc: |
  Asks whether $\binom{n}{k}$ with $2\le k\le n-2$ can be a product of
  consecutive primes infinitely often, as $\binom{21}{2}=2\cdot3\cdot5\cdot7$
  is.
tags:
- Number theory
- Binomial coefficients
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-07T19:40:10Z
---

# Problem 386

[[problems/factorials_binomials/_index|..]]

[[problems/factorials_binomials/E0386/claims/_index|claims/]]: The 2 claim pages of Problem 386, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $2\leq k\leq n-2$. Can $\binom{n}{k}$ be the product of
consecutive primes infinitely often? For example

$$
\binom{21}{2}=2\cdot 3\cdot 5\cdot 7.
$$

**Status.** Open. The site labeled the problem OPEN and credits no solution. The
standing derives from the claim pages: the problem is `open`, with no settling
or pending full claim. There are two pending partial claims.
[[problems/factorials_binomials/E0386/claims/2026_09_29_martins|Martins 2026]]
is a manuscript that bounds the primes and the block length of any sufficiently
large solution. It proves finiteness for each fixed $k$ and block length, and
treats the case $k=2$ in detail.
[[problems/factorials_binomials/E0386/claims/2026_09_30_mysore|Mysore 2026]] is
a draft note showing that any further solution with $k=2$ is a product of at
least $1924$ consecutive primes. Neither decides whether there are infinitely
many solutions.

**Source.** [erdosproblems.com/386](https://www.erdosproblems.com/386), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #386,
https://www.erdosproblems.com/386.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/386.lean).

## Progress

Not yet compiled.

## Known Results

Not yet compiled.
