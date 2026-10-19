---
name: problems/diophantine_problems/E0389
title: Problem 389
desc: |
  Asks whether every $n\ge1$ has some $k$ for which $n(n+1)\cdots(n+k-1)$
  divides $(n+k)\cdots(n+2k-1)$.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 389

[[problems/diophantine_problems/_index|..]]

***

**Statement.** Is it true that for every $n\geq 1$ there is a $k$ such that

$$
n(n+1)\cdots(n+k-1)\mid (n+k)\cdots (n+2k-1)?
$$

**Status.** Open.

**Source.** [erdosproblems.com/389](https://www.erdosproblems.com/389), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #389,
https://www.erdosproblems.com/389.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/389.lean).

## Current assessment

The [[research/powerful_numbers_and_products/_index|factorial-valuation formulation]]
gives an exact test for each specified pair $(n,k)$ and checks witnesses
$(1,1),(2,5),(3,4)$. It provides no construction of $k$ for arbitrary $n$.
These finite checks are author-recorded by Plasma AI and do not resolve
the all-$n$ question.

The [[../library/diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/_index|Ulas source account]]
records a digit-sum criterion, infinitely many successful block lengths for
the problem's $n=2,3$, and reported witnesses through $n=21$. The paper's question
at index $n$ is this problem at index $n+1$. The source account follows the
relevant proofs but has no independent review; its numerical table was not
recomputed there. No all-$n$ conclusion follows.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/_index|ulas_2013_note_erdos_straus_erdos_graham]]
- [[../library/diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/table_2|ulas_2013_note_erdos_straus_erdos_graham / table_2]]
- [[../library/diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_2_1|ulas_2013_note_erdos_straus_erdos_graham / theorem_2_1]]
- [[../library/diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_2_2|ulas_2013_note_erdos_straus_erdos_graham / theorem_2_2]]
- [[../library/diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_2_7|ulas_2013_note_erdos_straus_erdos_graham / theorem_2_7]]
- [[../library/diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_a_1|ulas_2013_note_erdos_straus_erdos_graham / theorem_a_1]]

<!-- END problem library links -->
