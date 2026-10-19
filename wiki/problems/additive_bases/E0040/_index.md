---
name: problems/additive_bases/E0040
title: Problem 40
desc: |
  Asks for which functions $g(N)\to\infty$ a set with $\gg N^{1/2}/g(N)$
  elements up to $N$ must have integers with arbitrarily many representations as
  a sum of two elements.
tags:
- Number theory
- Additive bases
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 40

[[problems/additive_bases/_index|..]]

***

**Statement.** For what functions $g(N)\to \infty$ is it true that

$$
\lvert A\cap \{1,\ldots,N\}\rvert \gg \frac{N^{1/2}}{g(N)}
$$

implies $\limsup 1_A\ast 1_A(n)=\infty$?

**Status.** Open.

**Source.** [erdosproblems.com/40](https://www.erdosproblems.com/40), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #40,
https://www.erdosproblems.com/40.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/40.lean).

## Current assessment

Current standing is as stated above; the route analysis records a scoped
mathematical comparison.

## Route analysis

The [[research/sidon_extension_interfaces/infinite_density|infinite sidon
density and representation conventions]] account records the following scope.
Conditional on the inspected Pliego Theorem 1.1, every polynomial G(N)=N^delta
with fixed delta>0 fails: choose a fixed integer r>=2 with 1/(4r+2)<=delta, use
A(N)>>N^(r/(2r+1)), and bound ordered convolution by 2r.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/additive_combinatorics/erdos_1956_problems_results_additive_number_theory/_index|erdos_1956_problems_results_additive_number_theory]]
- [[../library/additive_combinatorics/erdos_1956_problems_results_additive_number_theory/conjecture_p128|erdos_1956_problems_results_additive_number_theory / conjecture_p128]]

<!-- END problem library links -->
