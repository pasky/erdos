---
name: problems/factorials_binomials/E0912
title: Problem 912
desc: |
  Asks for a proof that the number $h(n)$ of distinct exponents in the prime
  factorization of $n!$ satisfies $h(n)\sim c(n/\log n)^{1/2}$ for some $c>0$.
tags:
- Number theory
- Factorials
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 912

[[problems/factorials_binomials/_index|..]]

***

**Statement.** If

$$
n! = \prod_i p_i^{k_i}
$$

is the factorisation into distinct primes then let $h(n)$ count the number of
distinct exponents $k_i$.

Prove that there exists some $c>0$ such that

$$
h(n) \sim c \left(\frac{n}{\log n}\right)^{1/2}
$$

as $n\to \infty$.

**Status.** Open.

**Source.** [erdosproblems.com/912](https://www.erdosproblems.com/912), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #912,
https://www.erdosproblems.com/912.

**References.**

- [Er82c] Erdős, P., Miscellaneous problems in number theory. Congr. Numer.
  (1982), 25-45.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/912.lean).

## Current assessment

The author-recorded
[[research/factorial_exponent_prime_intervals|prime-interval reduction]] gives
the exact identity

$$
h(n)=\#\{\lfloor n/p\rfloor:p\le n,\ p\text{ prime}\}.
$$

It also states a precise, unproved averaged occupancy law for the reciprocal
intervals $(n/(j+1),n/j]$. If that law holds, the fully justified tail bounds
and integral yield $h(n)\sim\sqrt{2\pi}\sqrt{n/\log n}$. The conditional
constant is not established. The held Erdős theorem proves the order of
magnitude only; ordinary long-interval prime estimates do not provide occupancy
at the logarithmic lengths involved here. No numerical experiment, source-proof
audit, or independent review is claimed.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/factorials_binomials/erdos_1982_miscellaneous_problems_number_theory/_index|erdos_1982_miscellaneous_problems_number_theory]]
- [[../library/factorials_binomials/erdos_1982_miscellaneous_problems_number_theory/display_4|erdos_1982_miscellaneous_problems_number_theory / display_4]]
- [[../library/factorials_binomials/erdos_1982_miscellaneous_problems_number_theory/theorem_1|erdos_1982_miscellaneous_problems_number_theory / theorem_1]]

<!-- END problem library links -->
