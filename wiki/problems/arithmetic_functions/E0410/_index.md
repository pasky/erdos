---
name: problems/arithmetic_functions/E0410
title: Problem 410
desc: |
  Asks whether $\sigma_k(n)^{1/k}\to\infty$ as $k\to\infty$ for every $n\ge2$,
  where $\sigma_k$ is the $k$-th iterate of the sum-of-divisors function.
tags:
- Number theory
- Iterated functions
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 410

[[problems/arithmetic_functions/_index|..]]

***

**Statement.** Let $\sigma_1(n)=\sigma(n)$, the sum of divisors function, and
$\sigma_k(n)=\sigma(\sigma_{k-1}(n))$. Is it true that for all $n\geq 2$

$$
\lim_{k\to \infty} \sigma_k(n)^{1/k}=\infty?
$$

**Status.** Open.

**Source.** [erdosproblems.com/410](https://www.erdosproblems.com/410), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #410,
https://www.erdosproblems.com/410.

**References.**

- [Gu04] Guy, Richard K., Unsolved problems in number theory, third
  edition, Problem Books in Mathematics, Springer (2004), xviii+437 pp.;
  B41 "Iterations of $\phi$ and $\sigma$", printed p. 148: the third of six
  statements on the iterates $\sigma^k(n)$ that [EGPS90] "are unable to
  prove or disprove", "for every $n>1$, $(\sigma^k(n))^{1/k}\to\infty$ as
  $k\to\infty$?". Library home:
  [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]].

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/410.lean).

## Current assessment

For a fixed start $n\ge2$, put $a_0=n$ and $a_{j+1}=\sigma(a_j)$. Telescoping
gives the exact identity

$$
\frac{\log a_k}{k}=\frac{\log n}{k}
 +\frac1k\sum_{j<k}\log\frac{\sigma(a_j)}{a_j}.
$$

The question is therefore divergence of the Cesàro average on each fixed orbit.
Unbounded isolated abundancy ratios do not imply that average diverges.
[[../library/arithmetic_functions/erdos_1990_normal_behavior_iterates_arithmetic_functions/_index|Erdős
and collaborators]] separate this iteration question from their almost-all
results;
[[../library/arithmetic_functions/cohen_1996_iterating_sum_divisors_function/_index|Cohen's
numerical discussion]] concerns finite prefixes. The averages in
[[../library/arithmetic_functions/pomerance_2018_first_function_iterates/_index|Pomerance's
Theorem 1.1]] concern the different map $s(n)=\sigma(n)-n$ and finitely many
iterates averaged over starts. The inspected statements supply no persistent
growth on every fixed $\sigma$ orbit. A useful input would bound the displayed
cumulative logarithmic abundancy from below; no source computation has been
replayed.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/arithmetic_functions/cohen_1996_iterating_sum_divisors_function/_index|cohen_1996_iterating_sum_divisors_function]]
- [[../library/arithmetic_functions/cohen_1996_iterating_sum_divisors_function/remark_p98|cohen_1996_iterating_sum_divisors_function / remark_p98]]
- [[../library/arithmetic_functions/erdos_1990_normal_behavior_iterates_arithmetic_functions/_index|erdos_1990_normal_behavior_iterates_arithmetic_functions]]
- [[../library/arithmetic_functions/erdos_1990_normal_behavior_iterates_arithmetic_functions/statements_p169|erdos_1990_normal_behavior_iterates_arithmetic_functions / statements_p169]]
- [[../library/arithmetic_functions/maier_1984_third_iterates_phi_sigma_functions/_index|maier_1984_third_iterates_phi_sigma_functions]]
- [[../library/arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/_index|plasma_ai_2026_normal_order_number_iterations_euler_s_function]]
- [[../library/arithmetic_functions/pollack_2016_problems_erdos_sum_divisors_function/_index|pollack_2016_problems_erdos_sum_divisors_function]]
- [[../library/arithmetic_functions/pollack_2016_problems_erdos_sum_divisors_function/theorem_1_2|pollack_2016_problems_erdos_sum_divisors_function / theorem_1_2]]
- [[../library/arithmetic_functions/pollack_2016_problems_erdos_sum_divisors_function/theorem_1_3|pollack_2016_problems_erdos_sum_divisors_function / theorem_1_3]]
- [[../library/arithmetic_functions/pomerance_2018_first_function_iterates/_index|pomerance_2018_first_function_iterates]]
- [[../library/arithmetic_functions/pomerance_2018_first_function_iterates/theorem_1_1|pomerance_2018_first_function_iterates / theorem_1_1]]
- [[../library/arithmetic_functions/pomerance_2018_first_function_iterates/theorem_2_4|pomerance_2018_first_function_iterates / theorem_2_4]]
- [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]]

<!-- END problem library links -->
