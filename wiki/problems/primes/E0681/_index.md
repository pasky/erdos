---
name: problems/primes/E0681
title: Problem 681
desc: |
  Asks whether every large $n$ has some $k$ such that $n+k$ is composite and
  $p(n+k)>k^2$, where $p(m)$ is the least prime factor of $m$.
tags:
- Number theory
- Primes
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 681

[[problems/primes/_index|..]]

***

**Statement.** Is it true that for all large $n$ there exists $k$ such that
$n+k$ is composite and

$$
p(n+k)>k^2,
$$

where $p(m)$ is the least prime factor of $m$?

**Status.** Open.

**Source.** [erdosproblems.com/681](https://www.erdosproblems.com/681), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #681,
https://www.erdosproblems.com/681.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/681.lean).

## Current assessment

When $n+1$ is composite, $k=1$ works. Hence only prime predecessors $n=p-1$
need a further argument. A composite witness must satisfy
$k^2<p(n+k)\le\sqrt{n+k}$, so $k^4<n+k$ and in particular $k<n^{1/4}+1$.

For every fixed $K$, Dirichlet's theorem gives arbitrarily large primes
$p\equiv1\pmod{\operatorname{lcm}(1,\ldots,K)}$. For $n=p-1$, shift one fails
compositeness, and for $2\le k\le K$ the number $n+k$ is divisible by $k$,
forcing $p(n+k)\le k\le k^2$. Thus bounded shifts fail on infinitely many prime
predecessors. This is a complete author reduction using the one-prime Dirichlet
theorem; it assumes no primality of a quotient. A useful input must force a
growing-shift composite witness within the fourth-root range for every prime
predecessor.

## Known Results

Not yet compiled.
