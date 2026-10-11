---
name: problems/additive_combinatorics/E0331
title: Problem 331
desc: |
  Asks whether two sets of integers whose counting functions are both
  $\gg N^{1/2}$ must share infinitely many equal nonzero differences; the answer
  is no.
tags:
- Number theory
- Additive combinatorics
status: solved
claim: disproved
created: 2026-09-04T09:17:27Z
updated: 2026-10-08T00:44:24Z
---

# Problem 331

[[problems/additive_combinatorics/_index|..]]

[[problems/additive_combinatorics/E0331/claims/_index|claims/]]: The 2 claim pages of Problem 331, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $A,B\subseteq \mathbb{N}$ such that for all large $N$

$$
\lvert A\cap \{1,\ldots,N\}\rvert \gg N^{1/2}
$$

and

$$
\lvert B\cap \{1,\ldots,N\}\rvert \gg N^{1/2}.
$$

Is it true that there are infinitely many solutions to $a_1-a_2=b_1-b_2\neq 0$
with $a_1,a_2\in A$ and $b_1,b_2\in B$?

**Status.** DISPROVED (LEAN), the site's label. The answer is no, by a
binary-digit counterexample. The site credits it to Ruzsa, and it is recorded on
[[problems/additive_combinatorics/E0331/claims/2024_06_19_ruzsa|its claim page]]
with the site's acceptance as its evidence. Erdős and Freud had published the
same counterexample in 1984 (J. Number Theory 18, 99--109, refereed) without
crediting Ruzsa. Their publication is recorded on
[[problems/additive_combinatorics/E0331/claims/1984_02_01_erdos_freud|its own claim page]].
The label's Lean mark refers to van Doorn's Lean formalization of the
counterexample. It was posted in the site's discussion thread in January 2026
and is linked by the catalog. The Ruzsa page lists it as a formalization link.
It is third-party Lean, so it gives no `formalized` evidence.

**Source.** [erdosproblems.com/331](https://www.erdosproblems.com/331), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #331,
https://www.erdosproblems.com/331.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/331.lean).

## Progress

Not yet compiled.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/additive_combinatorics/erdos_freud_1984_disjoint_sets_differences/_index|erdos_freud_1984_disjoint_sets_differences]]
- [[../library/additive_combinatorics/erdos_freud_1984_disjoint_sets_differences/counterexample_p100|erdos_freud_1984_disjoint_sets_differences / counterexample_p100]]
- [[../library/additive_combinatorics/erdos_freud_1984_disjoint_sets_differences/theorem_4|erdos_freud_1984_disjoint_sets_differences / theorem_4]]

<!-- END problem library links -->
