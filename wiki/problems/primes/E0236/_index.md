---
name: problems/primes/E0236
title: Problem 236
desc: |
  Asks whether the number $f(n)$ of solutions of $n=p+2^k$, with $p$ prime and
  $k\ge0$, satisfies $f(n)=o(\log n)$.
tags:
- Number theory
- Primes
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 236

[[problems/primes/_index|..]]

***

**Statement.** Let $f(n)$ count the number of solutions to $n=p+2^k$ for prime
$p$ and $k\geq 0$. Is it true that $f(n)=o(\log n)$?

**Status.** Open.

**Source.** [erdosproblems.com/236](https://www.erdosproblems.com/236), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #236,
https://www.erdosproblems.com/236.

**References.**

- [Er50] Erdős, P., On integers of the form $2^k+p$ and some related problems.
  Summa Brasil. Math. (1950), 113-123.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/236.lean).

## Current assessment

The [[research/covering_prime_interfaces/prime_pattern_uniformity|second-moment comparison]]
shows that a bound $\sum_{n\le X}r(n)^2\ll X$ permits
$O_\varepsilon(X/\log^2X)$ values in a dyadic interval with
$r(n)>\varepsilon\log n$. It controls almost all values, while the
question requires a pointwise little-oh bound and still allows sparse
spikes. Including exponent zero changes the count by at most one. This is
an author-recorded limitation of the direct moment argument, not a
counterexample to the problem.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/primes/chen_2023_conjecture_erdos_p_2_k/_index|chen_2023_conjecture_erdos_p_2_k]]
- [[../library/primes/erdos_1950_integers_form_related_problems/_index|erdos_1950_integers_form_related_problems]]
- [[../library/primes/erdos_1950_integers_form_related_problems/conjecture_p115|erdos_1950_integers_form_related_problems / conjecture_p115]]
- [[../library/primes/erdos_1950_integers_form_related_problems/theorem_2|erdos_1950_integers_form_related_problems / theorem_2]]

<!-- END problem library links -->
