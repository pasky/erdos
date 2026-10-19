---
name: problems/primes/E0463
title: Problem 463
desc: |
  Asks whether there is a function $f$ with $f(n)\to\infty$ such that, for all
  large $n$, some composite $m$ satisfies $n+f(n)<m<n+p(m)$, where $p(m)$ is the
  least prime factor of $m$.
tags:
- Number theory
- Primes
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 463

[[problems/primes/_index|..]]

***

**Statement.** Is there a function $f$ with $f(n)\to \infty$ as $n\to \infty$
such that, for all large $n$, there is a composite number $m$ such that

$$
n+f(n)<m<n+p(m)?
$$

(Here $p(m)$ is the least prime factor of $m$.)

**Status.** Open.

**Source.** [erdosproblems.com/463](https://www.erdosproblems.com/463), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #463,
https://www.erdosproblems.com/463.

**References.**

- [Er92e] Erdős, Pál, Some Unsolved problems in Geometry, Number Theory and
  Combinatorics. Eureka (1992), 44-48.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/463.lean).

## Current assessment

Define $D(n)$ as the largest integer $d\ge1$ with $n+d$ composite and
$d<p(n+d)$, or zero if none exists. The least-prime-factor bound
$p(n+d)\le\sqrt{n+d}$ gives $d^2-d<n$, so each $D(n)$ is determined by a finite
window. The question is equivalent to $D(n)\to\infty$: if that holds take
$f(n)=D(n)/2$ eventually; the forward implication follows from each required
witness.

[[../library/primes/gafni_2025_rough_numbers_between_consecutive_primes/_index|Gafni–Tao's
Theorem 1.1]], inspected at statement depth, gives $D(p_j)\ge1$ at almost all
prime-gap left endpoints, not every $n$ or a diverging displacement. The
explicit subsequence $n=q^2-q+1$, $q$ prime, has $D(n)\ge q-1$ using $m=q^2$,
but only proves unbounded limsup. These author deductions identify the missing
uniform quantifier; no finite diagnostic or subsequence settles it.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/primes/gafni_2025_rough_numbers_between_consecutive_primes/_index|gafni_2025_rough_numbers_between_consecutive_primes]]

<!-- END problem library links -->
