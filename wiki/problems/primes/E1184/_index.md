---
name: problems/primes/E1184
title: Problem 1184
desc: |
  Asks whether, for $n=k^{\alpha+o(1)}$ with $\alpha>1$, the number of integers
  among $n+1,\ldots,n+k$ whose largest prime factor exceeds $k$ is
  $(1-\rho(\alpha)+o(1))k$, with $\rho$ the Dickman function.
tags:
- Number theory
- Primes
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 1184

[[problems/primes/_index|..]]

***

**Statement.** Let $f(n,k)$ count the number of $1\leq i\leq k$ such that
$P(n+i)>k$ (where $P(m)$ is the largest prime divisor of $m$). Is it true that,
if $\alpha>1$ is such that $n=k^{\alpha+o(1)}$, then

$$
f(n,k)=(1-\rho(\alpha)+o(1))k,
$$

where $\rho$ is the Dickman function?

**Status.** Open.

**Source.** [erdosproblems.com/1184](https://www.erdosproblems.com/1184),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1184,
https://www.erdosproblems.com/1184.

**References.**

- [Er76e] Erdős, P., Problems and results on consecutive integers. Publ. Math.
  Debrecen (1976), 271-282.
- [RST75b] Ramachandra, K. and Shorey, T. N. and Tijdeman, R., On Grimm's
  problem relating to factorisation of a block of consecutive integers. II. J.
  Reine Angew. Math. (1976), 192-201.

**Formalization.** None recorded.

## Current assessment

The inspected statements of
[[../library/primes/erdos_1976_problems_results_consecutive_integers/_index|Erdős's
Theorems 1 and 3]] give, along $n=k^{\alpha+o(1)}$,

$$
1-1/\alpha\le\liminf f(n,k)/k
 \le\limsup f(n,k)/k\le\min(\alpha-1,1).
$$

Apply their strict ranges first with $1<\beta<\alpha<\gamma$ and then let
$\beta\uparrow\alpha$, $\gamma\downarrow\alpha$. In contrast,
[[../library/primes/ramachandra_1976_grimm_s_problem_relating_factorisation_block/theorem_2|Ramachandra–Shorey–Tijdeman's
Theorem 2]] requires $\log n\ge C(\log k)^2$, outside every fixed-$\alpha$
regime eventually. Neither theorem proof was audited.

For $1<\alpha<2$, eventually $n+k<k^2$, so a term has at most one prime factor
greater than $k$. Consequently

$$
f(n,k)=\sum_{1\le a<(n+k)/k}
 \#\{q>k\text{ prime}:n/a<q\le(n+k)/a\}.
$$

This is exact: each eligible term is counted once with its cofactor. Cofactors
reach size $k^{\alpha-1+o(1)}$, giving intervals as short as
$k^{2-\alpha+o(1)}$ near $k$. The author reduction identifies the needed
summable uniform errors; it supplies no such estimate. Global Dickman counts or
the disjoint logarithmic range do not settle these fixed blocks.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/primes/erdos_1976_problems_results_consecutive_integers/_index|erdos_1976_problems_results_consecutive_integers]]
- [[../library/primes/ramachandra_1976_grimm_s_problem_relating_factorisation_block/_index|ramachandra_1976_grimm_s_problem_relating_factorisation_block]]
- [[../library/primes/ramachandra_1976_grimm_s_problem_relating_factorisation_block/theorem_2|ramachandra_1976_grimm_s_problem_relating_factorisation_block / theorem_2]]

<!-- END problem library links -->
