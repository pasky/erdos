---
name: problems/irrationality/E0495
title: Problem 495
desc: |
  Asks whether $\liminf_{n\to\infty} n\|n\alpha\|\|n\beta\|=0$ for all real
  $\alpha,\beta$, where $\|x\|$ is the distance from $x$ to the nearest integer.
tags:
- Diophantine approximation
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 495

[[problems/irrationality/_index|..]]

***

**Statement.** Let $\alpha,\beta \in \mathbb{R}$. Is it true that

$$
\liminf_{n\to \infty} n \| n\alpha \| \| n\beta\| =0
$$

where $\|x\|$ is the distance from $x$ to the nearest integer?

**Status.** Open.

**Source.** [erdosproblems.com/495](https://www.erdosproblems.com/495), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #495,
https://www.erdosproblems.com/495.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/495.lean).

## Current assessment

[[../library/irrationality/einsiedler_2006_invariant_measures_set_exceptions_littlewood_s/_index|Einsiedler–Katok–Lindenstrauss,
Theorem 1.5]] gives dimension zero for the exceptional set, not emptiness; a
singleton already has that size. Their measure-classification Theorem 1.3
assumes positive entropy for a diagonal one-parameter subgroup, and Corollary
1.4 excludes compact support under that hypothesis. A hypothetical exceptional
orbit does not automatically provide positive entropy.

Elementary cases are separate: a rational coordinate supplies a subsequence on
which one factor vanishes; if $\liminf n\|n\alpha\|=0$, then $\|n\beta\|\le1/2$
supplies the conclusion. These do not cover all badly approximable pairs. Only
the primary statements were inspected, not the measure-classification proof.
The remaining interface needs individual-orbit rigidity or an entropy argument
from the actual exceptional-orbit hypotheses, not genericity or a dimension
bound.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/irrationality/einsiedler_2006_invariant_measures_set_exceptions_littlewood_s/_index|einsiedler_2006_invariant_measures_set_exceptions_littlewood_s]]
- [[../library/irrationality/einsiedler_2006_invariant_measures_set_exceptions_littlewood_s/conjecture_1_2|einsiedler_2006_invariant_measures_set_exceptions_littlewood_s / conjecture_1_2]]
- [[../library/irrationality/einsiedler_2006_invariant_measures_set_exceptions_littlewood_s/corollary_1_4|einsiedler_2006_invariant_measures_set_exceptions_littlewood_s / corollary_1_4]]
- [[../library/irrationality/einsiedler_2006_invariant_measures_set_exceptions_littlewood_s/proposition_11_1|einsiedler_2006_invariant_measures_set_exceptions_littlewood_s / proposition_11_1]]
- [[../library/irrationality/einsiedler_2006_invariant_measures_set_exceptions_littlewood_s/theorem_10_1|einsiedler_2006_invariant_measures_set_exceptions_littlewood_s / theorem_10_1]]
- [[../library/irrationality/einsiedler_2006_invariant_measures_set_exceptions_littlewood_s/theorem_1_3|einsiedler_2006_invariant_measures_set_exceptions_littlewood_s / theorem_1_3]]
- [[../library/irrationality/einsiedler_2006_invariant_measures_set_exceptions_littlewood_s/theorem_1_5|einsiedler_2006_invariant_measures_set_exceptions_littlewood_s / theorem_1_5]]
- [[../library/irrationality/einsiedler_2006_invariant_measures_set_exceptions_littlewood_s/theorem_2_1|einsiedler_2006_invariant_measures_set_exceptions_littlewood_s / theorem_2_1]]

<!-- END problem library links -->
