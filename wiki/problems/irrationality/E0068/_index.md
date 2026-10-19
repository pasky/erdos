---
name: problems/irrationality/E0068
title: Problem 68
desc: |
  Asks whether $\sum_{n\ge2}\frac{1}{n!-1}$ is irrational.
tags:
- Number theory
- Irrationality
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 68

[[problems/irrationality/_index|..]]

***

**Statement.** Is

$$
\sum_{n\geq 2}\frac{1}{n!-1}
$$

irrational?

**Status.** Open.

**Source.** [erdosproblems.com/68](https://www.erdosproblems.com/68), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #68,
https://www.erdosproblems.com/68.

**References.**

- [Er88c] Erdős, P., On the irrationality of certain series: problems and
  results. New advances in transcendence theory (Durham, 1986) (1988), 102-109.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/68.lean).

## Current assessment

For $u_k=(k+1)!-1$, one has $\log u_k=O(k\log k)$ and therefore
$u_k^{1/2^k}\to1$.
[[../library/irrationality/erdos_1976_problems_results_irrationality_sum_infinite_series/_index|Erdős's
Theorem 1]] instead requires this quantity to have infinite limsup; Theorem 2
has a stronger growth hypothesis. Multiplying by $N!$ also does not clear the
denominators $n!-1$.

A positive answer to the factorial case of
[[problems/irrationality/E0264/_index|Problem 264]] would imply the present
irrationality: choose bounded nonzero perturbations $b_1=1$ and $b_n=-1$ for
$n\ge2$. Its sum equals $1/2$ plus the sum here. The converse does not follow,
since Problem 264 quantifies over every permitted bounded perturbation. These
are complete elementary comparisons with the inspected sufficient statements,
not an irrationality proof. The missing argument must handle the actual
factorial-minus-one denominators.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/irrationality/erdos_1969_irrationality_certain_series/_index|erdos_1969_irrationality_certain_series]]
- [[../library/irrationality/erdos_1976_problems_results_irrationality_sum_infinite_series/_index|erdos_1976_problems_results_irrationality_sum_infinite_series]]
- [[../library/irrationality/erdos_1976_problems_results_irrationality_sum_infinite_series/question_p2|erdos_1976_problems_results_irrationality_sum_infinite_series / question_p2]]
- [[../library/irrationality/erdos_1988_irrationality_certain_series_problems_results/_index|erdos_1988_irrationality_certain_series_problems_results]]
- [[../library/irrationality/kaneko_2026_refinements_erdos_s_irrationality_criterion_certain/_index|kaneko_2026_refinements_erdos_s_irrationality_criterion_certain]]

<!-- END problem library links -->
