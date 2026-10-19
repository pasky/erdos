---
name: problems/integer_sequences/E1073
title: Problem 1073
desc: |
  Asks whether the number $A(x)$ of composite $u<x$ dividing $n!+1$ for some $n$
  satisfies $A(x)\le x^{o(1)}$.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 1073

[[problems/integer_sequences/_index|..]]

***

**Statement.** Let $A(x)$ count the number of composite $u<x$ such that
$n!+1\equiv 0\pmod{u}$ for some $n$. Is it true that $A(x)\leq x^{o(1)}$?

**Status.** Open.

**Source.** [erdosproblems.com/1073](https://www.erdosproblems.com/1073),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1073,
https://www.erdosproblems.com/1073.

**References.**

- [HaSu02] Hardy, G. E. and Subbarao, M. V., A modified problem of Pillai and
  some related questions. Amer. Math. Monthly (2002), 554-559.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/1073.lean).

## Current assessment

The [[research/arithmetic_construction_interfaces/factorial_divisor_cutoff|fixed-modulus reduction]]
shows that a composite $u$ can divide $n!+1$ only when $n<P^-(u)$, where
$P^-(u)$ is its least prime factor. Thus each specified modulus has a finite
test. This author-recorded observation by Plasma AI supplies no subpower
bound for the number of eligible composite moduli. The counting estimate,
rather than the per-modulus decision, remains the missing step.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/integer_sequences/hardy_2002_modified_problem_pillai_related_questions/_index|hardy_2002_modified_problem_pillai_related_questions]]
- [[../library/integer_sequences/hardy_2002_modified_problem_pillai_related_questions/problem_f|hardy_2002_modified_problem_pillai_related_questions / problem_f]]

<!-- END problem library links -->
