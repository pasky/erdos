---
name: problems/divisors/E0468
title: Problem 468
desc: |
  Concerns the set $D_n$ of partial sums $d_1,d_1+d_2,\ldots$ of the divisors
  $1<d_1<d_2<\cdots$ of $n$. It asks how many elements of $D_n$ lie in no
  earlier $D_m$, and whether the least $n$ with $N\in D_n$ is $o(N)$.
tags:
- Number theory
- Divisors
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 468

[[problems/divisors/_index|..]]

***

**Statement.** For any $n$ let $D_n$ be the set of sums of the shape
$d_1,d_1+d_2,d_1+d_2+d_3,\ldots$ where $1<d_1<d_2<\cdots$ are the divisors of
$n$.

What is the size of $D_n\backslash \cup_{m<n}D_m$?

If $f(N)$ is the minimal $n$ such that $N\in D_n$ then is it true that
$f(N)=o(N)$? Perhaps just for almost all $N$?

**Status.** Open.

**Source.** [erdosproblems.com/468](https://www.erdosproblems.com/468), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #468,
https://www.erdosproblems.com/468.

**Formalization.** None recorded.

## Current assessment

The finite argument below leaves both the asymptotic question and the general
question about newly occurring sums unresolved. No broader source or status
review is supplied here.

[[theory/number_theory/L35_divisor_prefix_compression/_index|L35]] gives
an exact finite reduction: a divisor prefix may be replaced by its least
common multiple without changing that prefix. Exhausting the resulting
distinct-part partitions computes the true minimum over all original
integers for each $2\le N\le64$. Only $N=4$ is unrepresented in this
range, and the largest minimum is $f(58)=265$.
The retained checker and inputs establish this finite author-recorded
result; no asymptotic estimate or general novelty count follows.
