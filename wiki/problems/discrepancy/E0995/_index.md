---
name: problems/discrepancy/E0995
title: Problem 995
desc: |
  Asks for the growth, for almost every $\alpha$, of
  $\sum_{k\le N}f(\{\alpha n_k\})$, where $f\in L^2([0,1])$ and $n_k$ is a
  lacunary integer sequence.
tags:
- Analysis
- Discrepancy
status: claimed
claim: disproved
parts:
- example
created: 2026-09-04T09:17:27Z
updated: 2026-10-16T06:44:50Z
---

# Problem 995

[[problems/discrepancy/_index|..]]

[[problems/discrepancy/E0995/claims/_index|claims/]]: The 1 claim page of Problem 995, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $n_1<n_2<\cdots$ be a lacunary sequence of integers and $f\in
L^2([0,1])$. Estimate the growth of, for almost all $\alpha$,

$$
\sum_{1\leq k\leq N}f(\{ \alpha n_k\}).
$$

For example, is it true that, for almost all $\alpha$,

$$
\sum_{1\leq k\leq N}f(\{ \alpha n_k\})=o(N\sqrt{\log\log N})?
$$

**Formulation.** The second question is the part `example`. The first asks for an estimate of the growth with no target rather than
a definite question, so it is open-ended: it is not a part, and it never blocks the standing. The
second, the example the statement names, asks yes or no, so it is definite.

**Status.** Claimed. The definite little-o question is answered negatively by
[[problems/discrepancy/E0995/claims/2026_04_20_ho|Ho's claimed $p=2$ result]],
whose project acceptance is pending.
Its whole proof and the exact catalog consequence have an independent
examination and a separate passing grade. This is the statement's sole
definite part; the request to estimate growth without a specified target
remains in the discussion below. Credit for the counterexample is Ho's.

**Source.** [erdosproblems.com/995](https://www.erdosproblems.com/995), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #995,
https://www.erdosproblems.com/995.

**References.**

- [Er49d] Erdős, P., On the strong law of large numbers. Trans. Amer. Math. Soc.
  (1949), 51-56.
- [Er64b] Erdős, P., Problems and results on diophantine approximations.
  Compositio Math. (1964), 52-65.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/995.lean).

## Current assessment

Ho's Theorem 1.6 at $p=2$ supplies a single real mean-zero $L^2$ function,
a factor-two lacunary integer sequence and a common full-measure set on which
the positive limsup after division by $N(\log N)^{1/2-\varepsilon}$ is
infinite for every $\varepsilon>0$. The choice $\varepsilon=1/4$ refutes the
displayed $o(N\sqrt{\log\log N})$ question for the same pair.
The [whole-proof review](claims/evidence/verify/ho_theorem_1_6/report.md)
and its [independent PASS grade](claims/evidence/verify/ho_theorem_1_6/grading.md)
cover both conclusions. The exact frozen extracts and print witness are
retained with their qualifications on the claim page.

The reviewed scope is the $p=2$ construction and this definite consequence;
project acceptance remains pending.
The all-$p$ theorem, Remark 7.1's upper bound and the wider growth
interpretation remain source-reported. In particular, the request to estimate
growth is not assigned an extra definite target. Comparing the source's
lower bounds with Erdős's reported upper bound motivates the scale
$N(\log N)^{1/2+o(1)}$ in the worst case, but that broader comparison has
no independent whole-proof acceptance here.

The grade discloses the internal processing of boundary-page text and rules
it immaterial because no neighboring mathematical content reached the
reviewer's displayed inputs or supplied an attack direction. It also retains
the nonconsumed (3.8) transcription discrepancy. These qualifications are part
of the filed examination and grade.

## Known Results

Erdős [Er49d] constructed a lacunary sequence and $f\in L^2([0,1])$ such that,
for every $\epsilon>0$ and almost all $\alpha$, the sums
$\sum_{k\le N}f(\{\alpha n_k\})$ exceed $N(\log\log N)^{1/2-\epsilon}$
infinitely often, and proved that for every lacunary sequence and every
$f\in L^2$ the sums are $o(N(\log N)^{1/2+\epsilon})$ for almost all
$\alpha$; in [Er64b] he thought the lower bound closer to the truth.

Ho (arXiv:2604.18535, Theorem 1.6 and Remark 7.1 of v2) states, for each
$2\le p<\infty$, a mean-zero $f\in L^p$ and a lacunary sequence with
$n_{j+1}/n_j\ge2$ whose partial sums exceed $N(\log N)^{1/p-\varepsilon}$
infinitely often almost everywhere, against the elementary upper bound
$O(N(\log N)^{1/p+\varepsilon})$ valid for every increasing sequence; at
$p=2$ this refutes the $o(N\sqrt{\log\log N})$ example and shows Erdős's
upper bound sharp up to the $\varepsilon$ gap as a source-reported comparison.
Only the $p=2$ lower construction and little-o refutation have the filed
independent examination and passing grade; project acceptance is pending. See
[[problems/discrepancy/E0995/claims/2026_04_20_ho|the claim page]] and the
[[../library/analysis/ho_2026_counterexamples_lacunary_dilates_via_dyadic_spike/_index|library card]].


The [[research/graph_ramsey_interfaces/probability_and_growth_interfaces|growth-comparison account]] writes out the $\varepsilon=1/4$ implication, including centering and lacunarity. The claim page holds the independent whole-proof review and passing grade for the source specialization and this consequence; project acceptance is pending.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/analysis/erdos_1949_strong_law_large_numbers/_index|erdos_1949_strong_law_large_numbers]]
- [[../library/analysis/erdos_1949_strong_law_large_numbers/remark_p52|erdos_1949_strong_law_large_numbers / remark_p52]]
- [[../library/analysis/erdos_1949_strong_law_large_numbers/theorem_1|erdos_1949_strong_law_large_numbers / theorem_1]]
- [[../library/analysis/ho_2026_counterexamples_lacunary_dilates_via_dyadic_spike/_index|ho_2026_counterexamples_lacunary_dilates_via_dyadic_spike]]
- [[../library/discrepancy/erdos_1964_problems_results_diophantine_approximations/_index|erdos_1964_problems_results_diophantine_approximations]]

<!-- END problem library links -->
