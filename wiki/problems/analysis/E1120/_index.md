---
name: problems/analysis/E1120
title: Problem 1120
desc: |
  Asks for the shortest length of a path from $0$ to $|z|=1$ inside
  $\{z:|f(z)|\le1\}$, where $f$ is a monic polynomial of degree $n$ with all
  roots in $|z|\le1$.
tags:
- Analysis
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 1120

[[problems/analysis/_index|..]]

[[problems/analysis/E1120/claims/_index|claims/]]: The 2 claim pages of Problem 1120, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $f\in \mathbb{C}[z]$ be a monic polynomial of degree $n$, all
of whose roots satisfy $\lvert z\rvert\leq 1$. Let

$$
E= \{ z : \lvert f(z)\rvert \leq 1\}.
$$

What is the shortest length of a path in $E$ joining $z=0$ to $\lvert z\rvert
=1$?

**Formulation.** The question is read as asking for the worst case: the
largest, over admissible $f$ of degree $n$, of the shortest length of such a
path, as a function $S(n)$ of $n$. This is how the erdosproblems.com commentary
reads it. The trivial lower bound is $S(n)\geq 1$, with equality for $f(z)=z^n$.

**Status.** Bloom's catalog labeled the problem OPEN (page last edited 30
December 2025). Two pending partial claims by Pendyala bear on it: an arXiv
preprint asserting $c\sqrt{\log n}\leq S(n)\leq \pi n$ for large $n$
([[problems/analysis/E1120/claims/2026_06_17_pendyala|claim page]]), and an
SSRN preprint asserting $S(n)=1$ for $n\leq 3$ and $S(6)>1$
([[problems/analysis/E1120/claims/2026_06_17_pendyala_radial|claim page]]).

**Source.** [erdosproblems.com/1120](https://www.erdosproblems.com/1120),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1120,
https://www.erdosproblems.com/1120.

**References.**

- [Ha74] Hayman, W. K., Research problems in function theory: new problems.
  (1974), 155-180.

**Formalization.** None recorded.

## Current assessment

The target is the worst-case shortest escape length $S(n)$ for every degree.
The two pending Pendyala claims in Status cover bounds and some fixed degrees,
and neither supplies the exact function. Section 9 of the held arXiv paper
has been inspected through Proposition 9.7: reflection to a zero-free
polynomial, two exits on a level graph, and Crofton's formula give its claimed
upper bound $S(n)\le\pi n$, with its topological and integral-geometric
inputs retained as source dependencies. The lower-bound maze proof has not
been checked. The separate degree-six radial witness and its angular
certificate remain uninspected. This is a bounded source-interface assessment,
not a wider status search or independent review.

**A deduction and its scope.**
[[research/erdos_1120/radial_obstruction_transfer|Radial obstructions and degree transfer]] gives the author-recorded
argument and source boundaries: compactness turns the absence of an allowed radius into shortest escape length greater than one; powers preserve that obstruction only at degree multiples.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/analysis/pendyala_2026_radial_access_lemniscates/_index|pendyala_2026_radial_access_lemniscates]]
- [[../library/analysis/pendyala_2026_radial_access_lemniscates/theorem_1_1|pendyala_2026_radial_access_lemniscates / theorem_1_1]]
- [[../library/analysis/pendyala_2026_radial_access_lemniscates/theorem_5_1|pendyala_2026_radial_access_lemniscates / theorem_5_1]]
- [[../library/analysis/pendyala_2026_radial_access_lemniscates/theorem_6_2|pendyala_2026_radial_access_lemniscates / theorem_6_2]]
- [[../library/analysis/pendyala_2026_shortest_paths_polynomial_lemniscate_sublevel_sets/_index|pendyala_2026_shortest_paths_polynomial_lemniscate_sublevel_sets]]
- [[../library/analysis/pendyala_2026_shortest_paths_polynomial_lemniscate_sublevel_sets/proposition_9_7|pendyala_2026_shortest_paths_polynomial_lemniscate_sublevel_sets / proposition_9_7]]
- [[../library/analysis/pendyala_2026_shortest_paths_polynomial_lemniscate_sublevel_sets/theorem_1_2|pendyala_2026_shortest_paths_polynomial_lemniscate_sublevel_sets / theorem_1_2]]

<!-- END problem library links -->
