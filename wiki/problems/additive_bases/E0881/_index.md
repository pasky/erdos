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
updated: 2026-10-07T23:33:05Z
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

**Formulation.** The site's definitions page (read 2026-10-13) calls a set
$A\subseteq\mathbb N$ an additive basis of order $r$ when "all sufficiently
large integers are the sum of at most $r$ integers from $A$". The page reads
the question with that definition, at order $k$ in the hypothesis and at order
$k+1$ in the conclusion. Counting sums of exactly $k$ elements gives a
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
question as this page reads it.

**Status.** Open. The site's label was OPEN, and the site lists no proof
claim. One pending claim is recorded,
[[problems/additive_bases/E0881/claims/2026_05_03_svyable|Svyable]], a
manuscript posted in the site's thread on 2026-05-03. It claims a complete
answer, no for every $k\ge2$, but it counts sums of exactly $k$ elements, so
under the Formulation above its counterexample is to a different question and
the claim is partial. A reader's AI check also finds fatal defects in its
proof.

**Source.** [erdosproblems.com/881](https://www.erdosproblems.com/881), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #881,
https://www.erdosproblems.com/881.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/881.lean).

## Progress

Not yet compiled.

## Known Results

Not yet compiled.
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
