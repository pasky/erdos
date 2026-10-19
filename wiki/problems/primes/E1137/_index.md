---
name: problems/primes/E1137
title: Problem 1137
desc: |
  Asks whether, with $d_n=p_{n+1}-p_n$, the ratio
  $\max_{n<x}d_nd_{n-1}/(\max_{n<x}d_n)^2$ tends to $0$ as $x\to\infty$.
tags:
- Number theory
- Primes
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 1137

[[problems/primes/_index|..]]

***

**Statement.** Let $d_n=p_{n+1}-p_n$, where $p_n$ denotes the $n$th prime. Is it
true that

$$
\frac{\max_{n<x}d_{n}d_{n-1}}{(\max_{n<x}d_n)^2}\to 0
$$

as $x\to \infty$?

**Status.** Open.

**Source.** [erdosproblems.com/1137](https://www.erdosproblems.com/1137),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1137,
https://www.erdosproblems.com/1137.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/1137.lean).

## Current assessment

The [[research/covering_prime_interfaces/prime_gap_statistics|adjacent-gap reduction]]
defines $D_N=\max_{1\le n\le N}d_n$ and
$B_N=\max_{2\le n\le N}\min(d_n,d_{n-1})$. The inequalities
$B_N^2\le\max_{2\le n\le N}d_nd_{n-1}\le D_NB_N$ make the target
equivalent to $B_N/D_N\to0$. This author-recorded equivalence requires
isolation of near-record gaps. A lower bound for a single large gap does
not provide the needed upper control of adjacent pairs.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/primes/maynard_2016_large_gaps_between_primes/_index|maynard_2016_large_gaps_between_primes]]
- [[../library/primes/maynard_2016_large_gaps_between_primes/theorem_1|maynard_2016_large_gaps_between_primes / theorem_1]]

<!-- END problem library links -->
