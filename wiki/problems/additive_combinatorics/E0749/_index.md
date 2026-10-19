---
name: problems/additive_combinatorics/E0749
title: Problem 749
desc: |
  Asks whether, for each $\epsilon>0$, some $A\subseteq\mathbb{N}$ has $A+A$ of
  lower density at least $1-\epsilon$ while every integer has $O_\epsilon(1)$
  representations as a sum of two elements of $A$.
tags:
- Additive combinatorics
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 749

[[problems/additive_combinatorics/_index|..]]

***

**Statement.** Let $\epsilon>0$. Does there exist $A\subseteq \mathbb{N}$ such
that the lower density of $A+A$ is at least $1-\epsilon$ and yet $1_A\ast 1_A(n)
\ll_\epsilon 1$ for all $n$?

**Status.** Open.

**Source.** [erdosproblems.com/749](https://www.erdosproblems.com/749), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #749,
https://www.erdosproblems.com/749.

**References.**

- [Er94b] Erdős, Paul,
  [[../library/distance_problems/erdos_1994_some_problems_number_theory_combinatorics_combinatorial_geometry/_index|Some problems in number theory, combinatorics and combinatorial geometry]].
  Math. Pannon. (1994), 261-269.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/749.lean).

## Current assessment

[[../library/additive_bases/ruzsa_1990_just_basis/theorem_2|Ruzsa's
second-moment bound]] $\sum_{n\le x}r_A(n)^2\le Cx$ implies that at most
$Cx/M^2$ targets have $r_A(n)>M$. Discarding these target integers does not
construct a set of generators with bounded representation function. Deleting
generators can also destroy unique representations of other targets; that loss
needs a separate estimate.

A periodic lift cannot solve the problem either. If a nonempty residue class
$r\bmod q$ is included in $A$, then at sufficiently large integers
$n\equiv2r\pmod q$, the pairs of positive elements in that class summing to $n$
already grow linearly with $n$. Thus the representation bound fails. These
elementary deductions are author-recorded by Plasma AI; the source's second-moment theorem
was inspected at statement depth. A useful thinning lemma must bound both the
surviving multiplicities and the newly uncovered targets.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/distance_problems/erdos_1994_some_problems_number_theory_combinatorics_combinatorial_geometry/_index|erdos_1994_some_problems_number_theory_combinatorics_combinatorial_geometry]]

<!-- END problem library links -->
