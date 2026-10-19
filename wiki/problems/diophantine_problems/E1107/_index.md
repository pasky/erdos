---
name: problems/diophantine_problems/E1107
title: Problem 1107
desc: |
  Asks whether, for $r\geq 2$, every large integer is the sum of at most $r+1$
  numbers divisible by the $r$th power of each of their prime factors.
tags:
- Number theory
- Powerful numbers
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-14T15:30:27Z
---

# Problem 1107

[[problems/diophantine_problems/_index|..]]

[[problems/diophantine_problems/E1107/claims/_index|claims/]]: The 1 claim page of Problem 1107, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $r\geq 2$. A number $n$ is $r$-powerful if for every prime
$p$ which divides $n$ we have $p^r\mid n$. Is every large integer the sum of at
most $r+1$ many $r$-powerful numbers?

**Status.** Open.

**Source.** [erdosproblems.com/1107](https://www.erdosproblems.com/1107),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1107,
https://www.erdosproblems.com/1107.

**References.**

- [He88] Heath-Brown, D. R., Ternary quadratic forms and sums of three
  square-full numbers. Séminaire de Théorie des Nombres, Paris 1986–87, Progr.
  Math. 75, Birkhäuser Boston (1988), 137-163.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/1107.lean).

## Current assessment

The problem is open for every $r\geq3$. The case $r=2$ is Heath-Brown's
theorem that every large integer is a sum of at most three 2-powerful numbers,
an accepted partial claim on
[[problems/diophantine_problems/E1107/claims/1988_01_01_heath_brown|its claim page]],
credited by the erdosproblems.com curator on
[[problems/diophantine_problems/E0941/_index|Problem 941]]. The notes below
record author-recorded transfers from research folders and are not
independently reviewed.

## Progress

The [[research/erdos_939/connections|Problem 939 connections page]] records that
the binomial construction of Problem 939 bears on no case of this question,
because the totals of any identity of its transfer lemma's kind are $r$-powerful
integers, which have density zero; at $r=2$ the question coincides with
[[problems/diophantine_problems/E0941/_index|Problem 941]], answered by
[[problems/diophantine_problems/E1107/claims/1988_01_01_heath_brown|Heath-Brown's theorem]].

## Route analysis

The
[[research/diophantine_representation_interfaces/local_congruences|congruence
coverage and lifting obstructions]] account records the following scope. Every
residue modulo any fixed M is a sum of at most three units (two for an even
target modulo even M, three for odd). Raising those unit representatives to
suitable powers preserves their residues and makes them $r$-powerful. This
rules out a fixed-modulus obstruction, but gives no global size control.
