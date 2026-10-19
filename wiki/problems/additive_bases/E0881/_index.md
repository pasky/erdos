---
name: problems/additive_bases/E0881
title: Problem 881
desc: |
  Asks whether every minimal additive basis $A$ of order $k$, one that stops
  being a basis of order $k$ when any infinite subset is removed, has an
  infinite $B\subset A$ with $A\setminus B$ a basis of order $k+1$.
tags:
- Number theory
- Additive bases
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 881

[[problems/additive_bases/_index|..]]

[[problems/additive_bases/E0881/claims/_index|claims/]]: The 1 claim page of Problem 881, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $A\subset\mathbb{N}$ be an additive basis of order $k$ which
is minimal, in the sense that if $B\subset A$ is any infinite set then
$A\backslash B$ is not a basis of order $k$.

Must there exist an infinite $B\subset A$ such that $A\backslash B$ is a basis
of order $k+1$?

**Formulation.** The erdosproblems.com definitions page (read 2026-10-13) calls
a set $A\subseteq\mathbb N$ an additive basis of order $r$ when "all
sufficiently large integers are the sum of at most $r$ integers from $A$". The
page reads the question with that definition, at order $k$ in the hypothesis and
at order $k+1$ in the conclusion. Counting sums of exactly $k$ elements gives a
different question, the reading of formal-conjectures (`erdos_881`) and of
Svyable's manuscript, whose set $A=C\cup\{1\}$ with
$C\subset\{2,3,\ldots\}$ does not contain $0$, so shorter sums cannot be
padded to $k$ terms (the
[[../library/additive_bases/svyable_2026_infinite_deletions_strongly_minimal_additive_bases/_index|source card]]
records the definition, p. 2, and the construction, pp. 3--11). The two
readings differ: the odd numbers are a basis of order $2$
with at most two summands but not with exactly two. So neither the
manuscript's minimality hypothesis (no infinite deletion is a basis with
exactly $k$ summands) nor its conclusion (no infinite deletion is a basis with
exactly $k+1$ summands) carries over to the reading with at most $k$ and at
most $k+1$ summands, and its counterexample settles no instance of the
question as this page reads it. The exactly-$k$ reading is a variant, which
this page sets aside.

**Status.** Open. The erdosproblems.com label was OPEN, and erdosproblems.com
lists no proof claim. One claim is recorded,
[[problems/additive_bases/E0881/claims/2026_05_03_svyable|Svyable]], a
manuscript posted in the erdosproblems.com thread on 2026-05-03. It claims a
complete answer, no for every $k\ge2$, but it counts sums of exactly $k$
elements, a variant the Formulation above sets aside, so its claim page is
rejected. A reader's AI check also finds fatal defects in its proof.

**Source.** [erdosproblems.com/881](https://www.erdosproblems.com/881), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #881,
https://www.erdosproblems.com/881.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/881.lean).

## Current assessment

The at-most-$k$ formulation above is unresolved for $k\ge2$ in this account.
The rejected exact-$k$ manuscript does not remove its convention gap.
The case $k=1$ has an elementary positive answer, without needing the minimality
hypothesis. An asymptotic basis of order at most one is cofinite. Remove an
infinite density-zero subset $B\subset A$, for example all sufficiently large
squares, and put $C=A\setminus B$. Then $C$ has density one. For all large
$n$, both $C\cap[0,n]$ and $n-(C\cap[0,n])$ have more than $(n+1)/2$
elements in $[0,n]$ and therefore intersect. The intersection gives $n=c+c'$
with $c,c'\in C$, so $C$ is a basis of order at most two.

This author-recorded argument by Plasma AI settles only that elementary case. For higher orders,
adjoining zero can identify the coverage predicates, but it does not
establish that a minimality or infinite-deletion obstruction survives. A useful
transfer must prove those hypotheses as well. The mathematical account here
uses the existing formulation and rejection record; it is not an independent
review of the manuscript or a new comprehensive status search.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/additive_bases/svyable_2026_infinite_deletions_strongly_minimal_additive_bases/_index|svyable_2026_infinite_deletions_strongly_minimal_additive_bases]]
- [[../library/additive_bases/svyable_2026_infinite_deletions_strongly_minimal_additive_bases/lemma_8|svyable_2026_infinite_deletions_strongly_minimal_additive_bases / lemma_8]]
- [[../library/additive_bases/svyable_2026_infinite_deletions_strongly_minimal_additive_bases/lemma_9|svyable_2026_infinite_deletions_strongly_minimal_additive_bases / lemma_9]]
- [[../library/additive_bases/svyable_2026_infinite_deletions_strongly_minimal_additive_bases/main_theorem_6|svyable_2026_infinite_deletions_strongly_minimal_additive_bases / main_theorem_6]]
- [[../library/additive_bases/svyable_2026_infinite_deletions_strongly_minimal_additive_bases/proposition_12|svyable_2026_infinite_deletions_strongly_minimal_additive_bases / proposition_12]]
- [[../library/additive_bases/svyable_2026_infinite_deletions_strongly_minimal_additive_bases/proposition_7|svyable_2026_infinite_deletions_strongly_minimal_additive_bases / proposition_7]]
- [[../library/additive_bases/svyable_2026_infinite_deletions_strongly_minimal_additive_bases/theorem_11|svyable_2026_infinite_deletions_strongly_minimal_additive_bases / theorem_11]]

<!-- END problem library links -->
