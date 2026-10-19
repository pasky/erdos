---
name: problems/primes/E0680
title: Problem 680
desc: |
  Asks whether every sufficiently large $n$ has some $k$ with $p(n+k)>k^2+1$,
  where $p(m)$ is the least prime factor of $m$.
tags:
- Number theory
- Primes
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 680

[[problems/primes/_index|..]]

***

**Statement.** Is it true that, for all sufficiently large $n$, there exists
some $k$ such that

$$
p(n+k)>k^2+1,
$$

where $p(m)$ denotes the least prime factor of $m$?

Can one prove this is false if we replace $k^2+1$ by
$e^{(1+\epsilon)\sqrt{k}}+C_\epsilon$, for all $\epsilon>0$, where
$C_\epsilon>0$ is some constant?

**Status.** Open.

**Source.** [erdosproblems.com/680](https://www.erdosproblems.com/680), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #680,
https://www.erdosproblems.com/680.

**References.**

- [Gr95] Granville, Andrew,
  [[../library/primes/granville_1995_harald_cramer_distribution_prime_numbers/_index|Harald Cramér and the distribution of prime numbers]].
  Scand. Actuar. J. (1995), 12-28.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/680.lean).

## Current assessment

For positive shifts, $k=1$ handles every even $n$, and $k=2$ handles odd $n$
for which $3,5\nmid n+2$. These cover $23$ of the $30$ residue classes modulo
$30$: $15$ even classes and $15-5-3+1=8$ odd classes. Every quadratic witness
also satisfies $k^2-k+1<n$, since $k^2+1<p(n+k)\le n+k$.

No fixed list of shifts can suffice. Given $K$, take
$n=1+a\operatorname{lcm}(2,\ldots,K+1)$. Then $k+1\mid n+k$ for $1\le k\le K$,
so $p(n+k)\le k+1\le k^2+1$. This gives arbitrarily large failures for every
fixed cap while leaving growing shifts open. The exponential variant likewise
needs control over its whole admissible range. These are exact author
arguments, not a large search. The
[[../library/primes/gafni_2025_rough_numbers_between_consecutive_primes/_index|linear
rough-gap theorem]] does not meet this quadratic threshold.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/primes/gafni_2025_rough_numbers_between_consecutive_primes/_index|gafni_2025_rough_numbers_between_consecutive_primes]]
- [[../library/primes/granville_1995_harald_cramer_distribution_prime_numbers/_index|granville_1995_harald_cramer_distribution_prime_numbers]]
- [[../library/primes/granville_1995_harald_cramer_distribution_prime_numbers/equation_14|granville_1995_harald_cramer_distribution_prime_numbers / equation_14]]
- [[../library/primes/granville_1995_harald_cramer_distribution_prime_numbers/heuristic_p24|granville_1995_harald_cramer_distribution_prime_numbers / heuristic_p24]]

<!-- END problem library links -->
