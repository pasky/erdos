---
name: problems/primes/E0890
title: Problem 890
desc: |
  Asks whether $\liminf_n\sum_{0\le i<k}\omega_k(n+i)\le k$ for every $k\ge1$,
  where $\omega_k$ counts the distinct prime factors above $k$, and whether
  $\limsup_n\bigl(\sum_{0\le i<k}\omega(n+i)\bigr)\log\log n/\log n=1$, where
  $\omega$ counts all distinct prime factors.
tags:
- Number theory
- Primes
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 890

[[problems/primes/_index|..]]

***

**Statement.** If $\omega_k(n)$ counts the number of distinct prime factors of
$n$ which are $>k$, then is it true that, for every $k\geq 1$,

$$
\liminf_{n\to \infty}\sum_{0\leq i<k}\omega_k(n+i)\leq k?
$$

Is it true that

$$
\limsup_{n\to \infty}\left(\sum_{0\leq i<k}\omega(n+i)\right) \frac{\log\log n}{\log n}=1,
$$

where $\omega$ counts the number of distinct prime factors without restriction?

**Status.** Open.

**Source.** [erdosproblems.com/890](https://www.erdosproblems.com/890), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #890,
https://www.erdosproblems.com/890.

**References.**

- [ErSe67] Erdős, P. and Selfridge, J. L., Some problems on the prime factors of
  consecutive integers. Illinois J. Math. (1967), 428-430.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/890.lean).

## Current assessment

The Pólya gap argument in
[[../library/arithmetic_functions/erdos_1967_problems_prime_factors_consecutive_integers/_index|Erdős–Selfridge]]
gives the opposite bound: at most one member of a sufficiently late length-$k$
block is $k$-smooth, so the total count of prime factors above $k$ is at least
$k-1$. It does not give the desired liminf upper bound $k$. The proof was
followed with Pólya's theorem imported as stated.

A simultaneous-primality construction makes the missing step explicit. Fix
$n_0>0$, let $s_i$ be the part of $n_0+i$ supported on primes at most $k$, and
set $M=\prod_{p\le k}p^{1+\max_i v_p(n_0+i)}$. The forms
$L_i(t)=(n_0+i+Mt)/s_i$ are integral and admissible: primes at most $k$ divide
their slopes but not constants, while a prime greater than $k$ excludes at most
$k$ residues. Infinitely many simultaneous prime values would give the desired
sum exactly $k$, but that is an unproved tuple premise.

For the separate limsup, elementary maximal order and primorial inputs give
only $1\le L_k\le k$. The lower bound uses the first term alone; the upper sums
the usual maximal-order bound over $k$ terms. An upper coefficient one requires
simultaneous control, not another construction for the lower bound.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/arithmetic_functions/erdos_1967_problems_prime_factors_consecutive_integers/_index|erdos_1967_problems_prime_factors_consecutive_integers]]
- [[../library/arithmetic_functions/erdos_1967_problems_prime_factors_consecutive_integers/conjecture_p429|erdos_1967_problems_prime_factors_consecutive_integers / conjecture_p429]]
- [[../library/arithmetic_functions/erdos_1967_problems_prime_factors_consecutive_integers/inequality_1|erdos_1967_problems_prime_factors_consecutive_integers / inequality_1]]

<!-- END problem library links -->
