---
name: problems/additive_bases/E0155
title: Problem 155
desc: |
  Asks whether the largest size $F(N)$ of a Sidon subset of $\{1,\ldots,N\}$
  satisfies $F(N+k)\leq F(N)+1$ for every fixed $k\geq 1$ and all large $N$.
tags:
- Additive combinatorics
- Sidon sets
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-14T15:30:27Z
---

# Problem 155

[[problems/additive_bases/_index|..]]

***

**Statement.** Let $F(N)$ be the size of the largest Sidon subset of
$\{1,\ldots,N\}$. Is it true that for every $k\geq 1$ we have

$$
F(N+k)\leq F(N)+1
$$

for all sufficiently large $N$?

**Status.** Open.

**Source.** [erdosproblems.com/155](https://www.erdosproblems.com/155), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #155,
https://www.erdosproblems.com/155.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/155.lean).

## Current assessment

Current standing is as stated above; the route analysis records a scoped
mathematical comparison.

## Route analysis

The [[research/sidon_extension_interfaces/finite_extremality|finite sidon
extremality and prefix extension]] account records the following scope. Exactly
equivalent to R(m+1)-R(m)->infinity, where R(m) is minimum interval length for
an m-mark ruler.
