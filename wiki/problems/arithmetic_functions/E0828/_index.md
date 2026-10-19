---
name: problems/arithmetic_functions/E0828
title: Problem 828
desc: |
  Asks whether, for every integer $a$, there are infinitely many $n$ with
  $\phi(n)\mid n+a$.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 828

[[problems/arithmetic_functions/_index|..]]

***

**Statement.** Is it true that, for any $a\in\mathbb{Z}$, there are infinitely
many $n$ such that

$$
\phi(n) \mid n+a?
$$

**Status.** Open.

**Source.** [erdosproblems.com/828](https://www.erdosproblems.com/828), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #828,
https://www.erdosproblems.com/828.

**References.**

- [Gu04] Guy, Richard K., Unsolved problems in number theory. Third edition,
  Problem Books in Mathematics, Springer, New York (2004), xviii+437 pp.;
  doi:10.1007/978-0-387-26677-0. Section B37 "Does $\phi(n)$ properly divide
  $n-1$?" is on pp. 142--143; Graham's conjecture that for all $k$ there are
  infinitely many $n$ with $\phi(n)\mid(n-k)$ is on p. 143. Library home:
  [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]].

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/828.lean).

## Current assessment

The fixed-cofactor construction below gives some nonpositive values of
$a$, as in Guy's historical account, and an exact limitation on that
construction. It leaves arbitrary $a$, including $a=1$, unresolved.
These elementary arguments are recorded by Plasma AI without independent
review; no complete current-literature or formalization audit is asserted.

Fix $m\ge1$ and let $p\nmid m$ vary over primes. Since
$\phi(mp)=\phi(m)(p-1)$, the divisibility $\phi(mp)\mid mp+a$
forces $p-1\mid m+a$. It can therefore hold for infinitely many such
$p$ only if $a=-m$. For $a=-m$ it is equivalent to
$\phi(m)\mid m$, independently of $p$. Thus this route produces
infinitely many solutions exactly when $a=-m$ and $\phi(m)\mid m$.
It applies to $m=1$, $m=2^u$ with $u\ge1$, and $m=2^u3^v$ with
$u,v\ge1$, whose ratios $m/\phi(m)$ are $1,2,3$ respectively.
Separately, $a=0$ has every positive power of two as a solution.

For nonzero $a$, any solution with $p^e\Vert n$ has
$p^{e-1}\mid\phi(n)$ and $p^{e-1}\mid n$, hence
$p^{e-1}\mid a$. Therefore $e\le v_p(|a|)+1$, and every solution
for $a=1$ is squarefree. A construction for positive $a$ must overcome
this restriction and use a varying cofactor or another mechanism; the
fixed-$m$ argument cannot extend beyond its necessary and sufficient
criterion.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]]

<!-- END problem library links -->
