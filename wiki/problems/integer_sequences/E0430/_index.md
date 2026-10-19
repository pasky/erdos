---
name: problems/integer_sequences/E0430
title: Problem 430
desc: |
  Asks whether, for all large $n$, the decreasing sequence with $a_1=n-1$ and
  each $a_k$ the greatest integer in $[2,a_{k-1})$ whose prime factors all
  exceed $n-a_k$ must contain a composite term.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 430

[[problems/integer_sequences/_index|..]]

***

**Statement.** Fix some integer $n$ and define a decreasing sequence in $[1,n)$
by $a_1=n-1$ and, for $k\geq 2$, letting $a_k$ be the greatest integer in
$[1,a_{k-1})$ such that all of the prime factors of $a_k$ are $>n-a_k$.

Is it true that, for sufficiently large $n$, not all of this sequence can be
prime?

**Statement (modified).** Fix some integer $n$ and define a decreasing sequence
in $[1,n)$ by $a_1=n-1$ and, for $k\geq 2$, letting $a_k$ be the greatest
integer in $[2,a_{k-1})$ such that all of the prime factors of $a_k$ are
$>n-a_k$.

Is it true that, for sufficiently large $n$, not all of this sequence can be
prime?

**Notes.** The erdosproblems.com wording holds trivially for every $n\ge3$. The
integer $1$ has no prime factors, so it meets the rule vacuously and every
sequence ends at it: for $n=3$ the rule gives $2,1$, and for $n=8$ it gives
$7,5,1$. Since $1$ is not prime, no sequence is all prime. The failure is this
page's own elementary check. The change replaces the range $[1,a_{k-1})$ by
$[2,a_{k-1})$, so that the sequence stops when no integer greater than $1$
qualifies; nothing else changes. The evidence is erdosproblems.com's own
commentary: its worked example for $n=8$ stops after $a_1=7$ and $a_2=5$, which
holds only when $1$ is excluded; erdosproblems.com kept the label OPEN, and the
commentary credits the equivalence with Problem 385 to Sarosh Adenwalla, both of
which fit only the corrected question. The defect is already in the poser's
text: Erdős and Graham [ErGr80, p. 85] index the sequence from the other end,
with $a_1=1$ and $a_k$ the least integer exceeding $a_{k-1}$ for which all prime
factors of $n-a_k>0$ are greater than $a_k$, and the value $n-a_k=1$ qualifies
vacuously in the same way. Their report that Selfridge's preliminary
calculations point to a yes answer "but no proof is in sight" fits only the
corrected question. Above the excluded value no vacuous case remains, since
every integer at least $2$ has a prime factor, and the corrected question is a
real one: for $n=8$ the sequence $7,5$ is all prime. No result about the
erdosproblems.com wording exists beyond the trivial check recorded here.

**Formulation.** In Erdős and Graham's indexing [ErGr80, p. 85] their $a_k$ is
$n$ minus erdosproblems.com's, so their condition, that all prime factors of
$n-a_k$ exceed $a_k$, is erdosproblems.com's, and their question, whether for
all large $n$ not all the quantities $n-a_k$ can be prime, is
erdosproblems.com's, with the same vacuous value $n-a_k=1$; with that value
excluded it is the modified Statement: whether, for all large $n$, some term of
the sequence is composite.

**Status.** Open, the erdosproblems.com label (OPEN), which describes the
modified Statement.

**Source.** [erdosproblems.com/430](https://www.erdosproblems.com/430), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #430,
https://www.erdosproblems.com/430.

**References.**

- [ErGr80] [[../library/number_theory/erdos_1980_old_new_problems_results_combinatorial_number_theory/_index|P. Erdős and R. L. Graham, Old and new problems and results in combinatorial number theory]],
  Monographies de L'Enseignement Mathématique 28, Université de Genève
  (1980); p. 85.

**Formalization.** None recorded.

## Current assessment

erdosproblems.com's OPEN label concerns the modified Statement: whether, for all
large $n$, the sequence has a composite term. For each integer $n\geq5$, the
sequence has a composite term exactly when $F(n)>n$, so the question is
equivalent to the first question of Problem 385; erdosproblems.com credits this
observation to Sarosh Adenwalla, and the proof written on Problem 385's page is
author-recorded. That proof carries no independent review, no computational
range is recorded here, and no literature search beyond erdosproblems.com is
recorded for this problem.

## Progress

For integer $n\geq5$, the sequence contains a composite term if and only if
$F(n)>n$ in [[problems/arithmetic_functions/E0385/_index|E0385]]. Hence the
modified Statement is equivalent to that problem's first eventual inequality.
This does not address its stronger question $F(n)-n\to\infty$.

## Known Results

[[problems/arithmetic_functions/E0385/_index|E0385]] gives the
author-recorded proof: the greedy sequence visits every eligible integer, and
a composite $m<n$ is eligible exactly when $m+p(m)>n$. erdosproblems.com credits
the equivalence to Sarosh Adenwalla. Erdős and Graham report that preliminary
calculations by Selfridge point to a yes answer but that no proof was known.
The reconstruction on Problem 385's page has author-recorded standing only,
and no computational range is recorded here.

## Research

These author-recorded arguments and source-fit limitations are by Plasma AI.
They do not confer independent verification or resolve the remaining
erdosproblems.com question.

Use the modified formulation excluding 1.
For fixed $n$, an integer $2\le m<n$ is selected precisely when
$$
 P^-(m)>n-m,
$$
where $P^-(m)$ is its least prime factor. The existing E0385 account's
proof and relation to E0430 were read, including the static eligibility
argument, rather than inferred from examples.

If such an $m$ is composite, $P^-(m)\le\sqrt m<\sqrt n$; hence $n-\sqrt n<m<n$.
For $n\ge5$, a composite $n-1$ is immediately eligible. Any remaining
counterexample therefore has $n-1$ prime. A per-$n$ exact test only needs this
interval and least prime factors. Existence of an eligible composite is exactly
$F(n)>n$, where E0385 defines $F(n)=\max_{m<n,\ m\text{ composite}}(m+P^-(m))$.
Equality with $n$ does not qualify: the inequality is strict.

The window grows with $n$. This is not a finite-state reduction of the
all-large-$n$ assertion; no range was computed here.

The unresolved obligation is to find a suitable rough composite in every final
square-root window for all large n. A finite checker may
restrict to n with n-1 prime and test composites in the strict square-root
window; any universal claim still needs a uniform analytic bound. Stop at any
finite n cutoff, at equality m+p(m)=n, or by reinstating the excluded terminal
value 1.
