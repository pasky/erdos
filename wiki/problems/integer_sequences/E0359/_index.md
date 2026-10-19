---
name: problems/integer_sequences/E0359
title: Problem 359
desc: |
  Asks what can be said about the density of the sequence starting at $n$ in
  which each later term is the least integer that is not a sum of consecutive
  earlier terms.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 359

[[problems/integer_sequences/_index|..]]

***

**Statement.** Let $a_1<a_2<\cdots$ be an infinite sequence of integers such
that $a_1=n$ and $a_{i+1}$ is the least integer which is not a sum of
consecutive earlier $a_j$s. What can be said about the density of this sequence?

In particular, in the case $n=1$, can one prove that $a_k/k\to \infty$ and
$a_k/k^{1+c}\to 0$ for any $c>0$?

**Formulation.** Read as Bloom's catalog words it, the rule fails for $n\ge2$.
When $a_2$ is chosen, the only sum of consecutive earlier terms is $a_1=n$, so
the least positive integer that is not such a sum is $1$, giving $a_2<a_1$
against $a_1<a_2<\cdots$; no sequence meets the erdosproblems.com wording. Erdős
and Graham (1980, p. 59) use the same wording, with $a_1=k$. Formal-conjectures
reads $a_{i+1}$ as the least integer exceeding $a_i$ that is not such a sum, and
the questions are recorded under that reading. For $n=1$ the two readings agree,
since every positive integer up to $a_i$ is already such a sum when $a_{i+1}$ is
chosen.

**Status.** Open.

**Source.** [erdosproblems.com/359](https://www.erdosproblems.com/359), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #359,
https://www.erdosproblems.com/359.

**References.**

- [An75] Andrews, George E., Research Problems: Mac Mahon's Prime Numbers of
  Measurement. Amer. Math. Monthly (1975), 922-923.
- [Po77] Porubský, Š., On MacMahon's segmented numbers and related sequences.
  Nieuw Arch. Wisk. (3) 25 (1977), 403-408.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/359.lean).

## Current assessment

The standing recorded here targets the erdosproblems.com wording (page last
edited 28 December 2025), whose rule for $a_{i+1}$ fails as written for $n\ge2$
and is read as the Formulation above states. No independent assessment of proof
coverage is recorded, and the problem has no claim page. The erdosproblems.com
commentary credits Porubský [Po77] with two results for $n=1$: for every
$\varepsilon>0$ infinitely many $k$ have
$a_k<(\log k)^\varepsilon k\log k/\log\log k$, and
$\limsup A(x)/\pi(x)\ge1/\log2$, where $A(x)$ counts the terms up to $x$.
Neither decides the limits the problem asks about: the first gives only
$\liminf_k a_k/k^{1+c}=0$, and the second bounds $A(x)$ from below only along
a sequence of $x$. They settle no instance, so they have no claim page.
Andrews [An75] conjectures $a_k\sim k\log k/\log\log k$.

Search scope. On 2026-10-07 the erdosproblems.com page listed no proof claim,
its discussion thread held one comment, of 29 November 2025, restating
Porubský's first result in its $\liminf$ form, and the formal-conjectures
statement file stated both limits for $n=1$ as open and had no solved
variant.

## Research

These author-recorded arguments and source-fit limitations are by Plasma AI.
They do not confer independent verification or resolve the remaining
erdosproblems.com question.

Use the intended increasing greedy sequence starting at 1. The exact page
already separates the literal-rule defect for a start $n\ge2$; that is not a
solution of the intended question.

Let $S_k=\sum_{i\le k}a_i$. Every positive integer at most $a_k$
is a consecutive sum of the first $k$ terms: this holds at 1; by
definition all integers below the next missing sum are covered, and
adjoining that sum covers it as a singleton. Consequently
$$
 a_k<a_{k+1}\le S_k+1.
$$
A selected term is never a sum of two or more preceding consecutive
terms, so this sequence satisfies E0839, with extra greedy coverage
that arbitrary E0839 sequences need not have.

This does not bound the growing memory of prefix differences or imply the full
limits $a_k/k\to\infty$ and $a_k/k^{1+c}\to0$ for every $c>0$. Monotonicity
alone cannot interpolate a subsequence estimate without control of the spacing
of its good indices.

Porubský, “On MacMahon's segmented numbers and related sequences,” Nieuw Arch.
Wisk. (3) 25 (1977), 403–408, is not held or inspected. Its reported subsequence
estimates are inherited only from the problem account. Its exact quantifiers and
possible control between good indices remain uninspected.

The missing step is uniform interpolation between the good indices
in the reported subsequence bound, and an independent lower-growth argument. A
useful test is to inspect, if the primary 1977 source becomes available, the
exact quantifiers and whether its coverage argument controls intervals between
good indices. Stop at a liminf statement, growing prefix-difference memory, or
the n>=2 literal defect as an answer to the n=1 target.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/integer_sequences/erdos_1977_problems_results_combinatorial_number_theory_iii/_index|erdos_1977_problems_results_combinatorial_number_theory_iii]]
- [[../library/ramsey_theory/erdos_1980_noen_mindre_kjente_problemer_i_kombinatorisk/_index|erdos_1980_noen_mindre_kjente_problemer_i_kombinatorisk]]
- [[../library/ramsey_theory/erdos_1980_noen_mindre_kjente_problemer_i_kombinatorisk/question_p160|erdos_1980_noen_mindre_kjente_problemer_i_kombinatorisk / question_p160]]

<!-- END problem library links -->
