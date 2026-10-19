---
name: problems/additive_bases/E0044
title: Problem 44
desc: |
  Asks whether, for any $\epsilon>0$, every Sidon set $A\subset\{1,\ldots,N\}$
  extends by elements above $N$ to a Sidon set of size at least
  $(1-\epsilon)M^{1/2}$ in some $\{1,\ldots,M\}$.
tags:
- Number theory
- Sidon sets
- Additive combinatorics
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-18T22:19:33Z
---

# Problem 44

[[problems/additive_bases/_index|..]]

[[problems/additive_bases/E0044/claims/_index|claims/]]: The 1 claim page of Problem 44, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $N\geq 1$ and $A\subset \{1,\ldots,N\}$ be a Sidon set. Is it
true that, for any $\epsilon>0$, there exist $M$ and $B\subset \{N+1,\ldots,M\}$
(which may depend on $N,A,\epsilon$) such that $A\cup B\subset \{1,\ldots,M\}$
is a Sidon set of size at least $(1-\epsilon)M^{1/2}$?

**Status.** Open.

**Source.** [erdosproblems.com/44](https://www.erdosproblems.com/44), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #44,
https://www.erdosproblems.com/44.

**References.**

- [Gu04] Guy, Richard K., Unsolved problems in number theory. Third edition,
  Problem Books in Mathematics, Springer, New York (2004), xviii+437 pp.;
  section C9 "Packing sums of pairs", printed p. 177: whether a finite
  Sidon sequence can be prolonged to one with $a_n<(1+o(1))n^2$, "as dense
  as possible asymptotically".
  Library home:
  [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]].

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/44.lean).

## Current assessment

Current standing is as stated above; the route analysis records a scoped
mathematical comparison.

## Route analysis

The [[research/sidon_extension_interfaces/finite_extremality|finite sidon
extremality and prefix extension]] account records the following scope. The
author-recorded L31 extends every fixed strong Sidon prefix to arbitrarily large
intervals with coefficient $1/\sqrt2$, using Singer sets. This extension is
Plasma AI's pending partial claim on
[[problems/additive_bases/E0044/claims/2026_10_19_plasma_ai|its claim page]].
It leaves the coefficient $1$ and the newly exposed mixed equations unresolved.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/number_theory/guy_1991_western_number_theory_problems/_index|guy_1991_western_number_theory_problems]]
- [[../library/number_theory/guy_1991_western_number_theory_problems/problem_91_05|guy_1991_western_number_theory_problems / problem_91_05]]
- [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]]

<!-- END problem library links -->
