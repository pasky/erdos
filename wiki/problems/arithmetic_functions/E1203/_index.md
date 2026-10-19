---
name: problems/arithmetic_functions/E1203
title: Problem 1203
desc: |
  Asks whether $F(n)=\max_k\omega(n+k)\log\log k/\log k$ tends to infinity as
  $n\to\infty$, where $\omega$ counts distinct prime factors.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 1203

[[problems/arithmetic_functions/_index|..]]

***

**Statement.** If $\omega(n)$ counts the number of distinct prime divisors of
$n$ then let

$$
F(n)=\max_k \omega(n+k)\frac{\log\log k}{\log k}.
$$

Prove that $F(n)\to \infty$ as $n\to \infty$.

**Status.** Open.

**Source.** [erdosproblems.com/1203](https://www.erdosproblems.com/1203),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1203,
https://www.erdosproblems.com/1203.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/1203.lean).

## Current assessment

Use integer offsets $k\ge3$, where the logarithmic factor is positive. The
elementary maximal-order bound from $m\ge(\omega(m)+1)!$ and Stirling's formula
gives, for every fixed $\delta>0$, uniformly over $k\ge n^\delta$,

$$
\omega(n+k)\frac{\log\log k}{\log k}
 \le\max(1,1/\delta)+o(1).
$$

Indeed $\log(n+k)\le\log2+\max(\log n,\log k)$ and the two iterated logarithms
have ratio tending to one uniformly. Divergence must therefore come from
subpower offsets.

A precise sufficient premise is that, for some fixed $c,C>0$ and every large
$x$, the interval $(x-H(x),x]$, with $H(x)=C\log x\sqrt{\log\log x}$, contains
$m$ with $\omega(m)\ge c\log\log m$. This is the relevant component of
[[../library/arithmetic_functions/lau_2026_number_prime_factors_consecutive_integers/_index|Lau's
Conjecture 7]], not a proved theorem. Apply it at $x=n+3H(n)$. Since $H(x)\sim
H(n)$, its witness $m=n+k$ has $H(n)\le k\le3H(n)$ and normalized value at
least $(c+o(1))\log\log\log n\to\infty$. The implication is complete at author
standing; its uniform short-interval premise remains open. An existential
small-offset formulation alone would not force a growing witness.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/arithmetic_functions/lau_2026_number_prime_factors_consecutive_integers/_index|lau_2026_number_prime_factors_consecutive_integers]]
- [[../library/arithmetic_functions/tao_2025_quantitative_correlations_problems_prime_factors_consecutive/_index|tao_2025_quantitative_correlations_problems_prime_factors_consecutive]]

<!-- END problem library links -->
