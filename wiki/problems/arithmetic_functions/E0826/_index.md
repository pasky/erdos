---
name: problems/arithmetic_functions/E0826
title: Problem 826
desc: |
  Asks whether infinitely many $n$ have $\tau(n+k)\ll k$ for every $k\ge1$,
  where $\tau$ is the number of divisors.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 826

[[problems/arithmetic_functions/_index|..]]

***

**Statement.** Are there infinitely many $n$ such that, for all $k\geq 1$,

$$
\tau(n+k)\ll k?
$$

**Status.** Open.

**Source.** [erdosproblems.com/826](https://www.erdosproblems.com/826), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #826,
https://www.erdosproblems.com/826.

**References.**

- [La26] C. F. Lau, On the number of prime factors of consecutive integers.
  arXiv:2604.15042 (2026).

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/826.lean).

## Current assessment

The distinction between $\omega$ and $\Omega$ is essential. Since $e+1\le2^e$,

$$
\tau(m)=\prod_{p^e\parallel m}(e+1)\le2^{\Omega(m)}.
$$

Consequently
[[../library/arithmetic_functions/lau_2026_number_prime_factors_consecutive_integers/_index|Lau's
logarithmic bound for $\Omega$]] yields a polynomial bound of exponent
$C\log2$, not automatically exponent one. Replacing the source starting point
by $N=n+1$ supplies the missing $k=1$ endpoint at a constant cost for that
polynomial bound. To obtain the target by this inequality one needs
$\Omega(n+k)\le\log k/\log2+O(1)$ uniformly, or direct control of the divisor
product. A bound only on distinct prime factors omits the exponents. The
specialization and elementary inequality are checked; the full sieve proof and
any improvement to its coefficient are not audited here.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/arithmetic_functions/lau_2026_number_prime_factors_consecutive_integers/_index|lau_2026_number_prime_factors_consecutive_integers]]

<!-- END problem library links -->
