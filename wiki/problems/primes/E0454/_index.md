---
name: problems/primes/E0454
title: Problem 454
desc: |
  Asks whether $f(n)=\min_{i<n}(p_{n+i}+p_{n-i})$, the least sum of two primes
  placed symmetrically around $p_n$, satisfies $\limsup_n(f(n)-2p_n)=\infty$.
tags:
- Number theory
- Primes
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 454

[[problems/primes/_index|..]]

***

**Statement.** Let

$$
f(n) = \min_{i<n} (p_{n+i}+p_{n-i}),
$$

where $p_k$ is the $k$th prime. Is it true that

$$
\limsup_n (f(n)-2p_n)=\infty?
$$

**Formulation.** The minimum is taken over $1\le i<n$. Pomerance [Po79]
defines the same quantity over $0<i<n$ and proves $f(n)>2p_n$ for infinitely
many $n$, so the $\limsup$ is at least $2$, as the erdosproblems.com commentary
records; McNew's quantity (23) and the formal-conjectures statement also take
$1\le i<n$. Admitting $i=0$ would give $f(n)\le 2p_n$ for every $n$ and the
trivial answer no, so erdosproblems.com's $\min_{i<n}$ is read as the sources
read it.

**Status.** Open.

**Source.** [erdosproblems.com/454](https://www.erdosproblems.com/454), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #454,
https://www.erdosproblems.com/454.

**References.**

- [Po79] Pomerance, Carl,
  [[../library/primes/pomerance_1979_prime_number_graph/_index|The prime number graph]].
  Math. Comp. (1979), 399-408.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/6fbb54f24ccc2e64dcfaffc28c58950e377110d2/FormalConjectures/ErdosProblems/454.lean),
at the linked commit of 18 September 2026, which defines `f n` as the
infimum over $0<i<n$ and carries no `formal_proof` annotation; its variant
`two_le_limsup`, the Pomerance bound, is marked `research solved` with a
`sorry` proof.

## Current assessment

The [[research/covering_prime_interfaces/prime_pattern_uniformity|gap-sum identity]]
writes the margin as the minimum of all partial sums of forward prime gaps
minus backward prime gaps. A large first difference, or infinitely many
positive margins, does not make that minimum unbounded. The recorded finite
data do not settle its growth. This author-recorded comparison identifies
the missing simultaneous control of every partial sum at one center.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/primes/mcnew_2018_convex_hull_prime_number_graph/_index|mcnew_2018_convex_hull_prime_number_graph]]
- [[../library/primes/mcnew_2018_convex_hull_prime_number_graph/midpoint_convex_primes_p13|mcnew_2018_convex_hull_prime_number_graph / midpoint_convex_primes_p13]]
- [[../library/primes/mcnew_2018_convex_hull_prime_number_graph/theorem_2_2|mcnew_2018_convex_hull_prime_number_graph / theorem_2_2]]
- [[../library/primes/mcnew_2018_convex_hull_prime_number_graph/theorem_2_3|mcnew_2018_convex_hull_prime_number_graph / theorem_2_3]]
- [[../library/primes/pomerance_1979_prime_number_graph/_index|pomerance_1979_prime_number_graph]]

<!-- END problem library links -->
