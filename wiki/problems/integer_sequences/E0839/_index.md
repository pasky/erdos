---
name: problems/integer_sequences/E0839
title: Problem 839
desc: |
  Asks whether an increasing sequence of positive integers in which no term is a
  sum of consecutive earlier terms must satisfy $\limsup a_n/n=\infty$.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 839

[[problems/integer_sequences/_index|..]]

***

**Statement.** Let $1\leq a_1<a_2<\cdots$ be a sequence of integers such that no
$a_i$ is the sum of consecutive $a_j$ for $j<i$. Is it true that

$$
\limsup \frac{a_n}{n}=\infty?
$$

Or even

$$
\lim \frac{1}{\log x}\sum_{a_n<x}\frac{1}{a_n}=0?
$$

**Status.** Open. Bloom's catalog labeled the problem OPEN.

**Source.** [erdosproblems.com/839](https://www.erdosproblems.com/839), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #839,
https://www.erdosproblems.com/839.

**References.**

- [Fr93] R. Freud, Adding numbers - on a problem of P. Erdős. James Cook
  Mathematical Notes (1993), 6199-6202 (the erdosproblems.com key; the issue
  prints the title "Adding numbers").

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/839.lean).

## Current assessment

These deductions leave the full question unresolved. They have author-recorded
standing; this assessment is limited to the arguments and source interfaces
stated below. No comprehensive search for recent proof claims is recorded here.

For $A=\{a_1<a_2<\cdots\}$, $\limsup a_n/n=\infty$ is equivalent to
$\liminf_{x\to\infty}A(x)/x=0$. At $x=a_n$ the ratio is $n/a_n$; between
successive terms, $A(x)$ is constant, and the endpoint ratios have only an index
shift. Positive upper density therefore does not refute the first question.

The held Freud account gives an infinite construction with upper density
$19/36$, with its explicitly unverified construction standing.
That detailed construction was not checked here. Upper density, and
finite extremizers, decide neither lower density nor logarithmic density.
Conversely zero logarithmic density would imply the first conclusion.
If $A(x)\ge\delta x$ eventually, partial summation yields
$$
 \sum_{a\le x,\ a\in A}1/a
 =A(x)/x+\int_1^x A(t)t^{-2}\,dt
 \ge\delta\log x-O(1),
$$
contradicting zero logarithmic density.

E0359 satisfies the forbidden consecutive-block condition, but its special
greedy coverage is not assumed for arbitrary E0839 sequences. The Freud
construction and upper-bound accounts were read with their source qualifications
intact.

The unresolved obligation is to control lower density or logarithmic mass for
every forbidden-block sequence, including sparse concatenations with dense
blocks. Any density argument should be tested against
Freud's claimed positive-upper-density construction and should identify where it
uses lower density. Stop if positive upper density is presented as a
counterexample to the first question, or if the greedy coverage invariant is
assumed for arbitrary sequences.

Source interfaces:
[[../library/additive_combinatorics/freud_1993_adding_numbers_problem_p/construction_p6199|Finite
construction and infinite version, pp. 6199-6202; explicit unverified
construction status]];
[[../library/additive_combinatorics/freud_1993_adding_numbers_problem_p/upper_bound_p6201|Scope
of upper bounds and source discrepancy]].

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/additive_combinatorics/freud_1993_adding_numbers_problem_p/_index|freud_1993_adding_numbers_problem_p]]
- [[../library/additive_combinatorics/freud_1993_adding_numbers_problem_p/construction_p6199|freud_1993_adding_numbers_problem_p / construction_p6199]]
- [[../library/integer_sequences/erdos_1977_problems_results_combinatorial_number_theory_iii/_index|erdos_1977_problems_results_combinatorial_number_theory_iii]]
- [[../library/integer_sequences/erdos_1981_many_old_some_new_problems_number_theory/_index|erdos_1981_many_old_some_new_problems_number_theory]]
- [[../library/integer_sequences/erdos_1981_many_old_some_new_problems_number_theory/problem_iii_3|erdos_1981_many_old_some_new_problems_number_theory / problem_iii_3]]
- [[../library/integer_sequences/erdos_1992_my_forgotten_problems_number_theory/_index|erdos_1992_my_forgotten_problems_number_theory]]
- [[../library/number_theory/erdos_1980_old_new_problems_results_combinatorial_number_theory/_index|erdos_1980_old_new_problems_results_combinatorial_number_theory]]
- [[../library/number_theory/erdos_1982_some_new_problems_results_number_theory/_index|erdos_1982_some_new_problems_results_number_theory]]
- [[../library/number_theory/erdos_1982_some_new_problems_results_number_theory/construction_p57|erdos_1982_some_new_problems_results_number_theory / construction_p57]]
- [[../library/number_theory/guy_1991_western_number_theory_problems/_index|guy_1991_western_number_theory_problems]]
- [[../library/number_theory/guy_1991_western_number_theory_problems/problem_91_02|guy_1991_western_number_theory_problems / problem_91_02]]
- [[../library/ramsey_theory/erdos_1980_noen_mindre_kjente_problemer_i_kombinatorisk/_index|erdos_1980_noen_mindre_kjente_problemer_i_kombinatorisk]]
- [[../library/ramsey_theory/erdos_1980_noen_mindre_kjente_problemer_i_kombinatorisk/question_p160|erdos_1980_noen_mindre_kjente_problemer_i_kombinatorisk / question_p160]]
- [[../library/ramsey_theory/erdos_1980_noen_mindre_kjente_problemer_i_kombinatorisk/theorem_p160|erdos_1980_noen_mindre_kjente_problemer_i_kombinatorisk / theorem_p160]]

<!-- END problem library links -->
