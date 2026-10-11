---
name: problems/additive_bases/E0221
title: Problem 221
desc: |
  Asks whether some set $A$ with $\ll N/\log N$ elements up to $N$ makes every
  large integer of the form $2^k+a$ with $a\in A$; proved.
tags:
- Number theory
- Additive bases
status: solved
claim: proved
created: 2026-09-04T09:17:27Z
updated: 2026-10-08T02:16:54Z
---

# Problem 221

[[problems/additive_bases/_index|..]]

[[problems/additive_bases/E0221/claims/_index|claims/]]: The 2 claim pages of Problem 221, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Is there a set $A\subset\mathbb{N}$ such that, for all large $N$,

$$
\lvert A\cap\{1,\ldots,N\}\rvert \ll N/\log N
$$

and such that every large integer can be written as $2^k+a$ for some $k\geq 0$
and $a\in A$?

**Status.** PROVED (LEAN), the site's label. The standing rests on two accepted
claim pages. The first is
[[problems/additive_bases/E0221/claims/1972_06_01_ruzsa|Ruzsa 1972]], the
refereed construction with $\ll N/\log N$ elements up to $N$, built from the
powers of $5$. The second is
[[problems/additive_bases/E0221/claims/2001_04_01_ruzsa|Ruzsa 2001]], the
refereed exact complement with $\sim N/\log_2 N$ elements, which is the best
possible count. The label's Lean qualification refers to an outside
formalization of the 1972 construction, linked from its page. That formalization
is not part of this repository's audited Lean.

**Source.** [erdosproblems.com/221](https://www.erdosproblems.com/221), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #221,
https://www.erdosproblems.com/221.

**References.**

- [Lo54] Lorentz, G. G., On a problem of additive number theory. Proc. Amer.
  Math. Soc. (1954), 838-841.
- [Ru01] Ruzsa, Imre Z., Additive completion of lacunary sequences.
  Combinatorica (2001), 279-291.
- [Ru72] Ruzsa, Jr., I., On a problem of P. Erdős. Canad. Math. Bull. (1972),
  309-310.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/221.lean).

## Progress

Not yet compiled.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/additive_bases/erdos_1954_results_additive_number_theory/_index|erdos_1954_results_additive_number_theory]]
- [[../library/additive_bases/erdos_1954_results_additive_number_theory/question_p853|erdos_1954_results_additive_number_theory / question_p853]]
- [[../library/additive_bases/ruzsajr_1972_problem_p/_index|ruzsajr_1972_problem_p]]
- [[../library/additive_bases/ruzsajr_1972_problem_p/theorem_p309|ruzsajr_1972_problem_p / theorem_p309]]
- [[../library/additive_combinatorics/erdos_1956_problems_results_additive_number_theory/_index|erdos_1956_problems_results_additive_number_theory]]
- [[../library/additive_combinatorics/erdos_1956_problems_results_additive_number_theory/problem_p133|erdos_1956_problems_results_additive_number_theory / problem_p133]]

<!-- END problem library links -->
