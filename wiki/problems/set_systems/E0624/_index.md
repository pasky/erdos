---
name: problems/set_systems/E0624
title: Problem 624
desc: |
  Asks to prove that $H(n)-\log_2 n\to\infty$, where $H(n)$ is the least size
  such that some map from the subsets of an $n$-element set $X$ to $X$ sends the
  subsets of every set that large onto $X$.
tags:
- Combinatorics
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 624

[[problems/set_systems/_index|..]]

***

**Statement.** Let $X$ be a finite set of size $n$ and $H(n)$ be such that there
is a function $f:\{A : A\subseteq X\}\to X$ so that for every $Y\subseteq X$
with $\lvert Y\rvert \geq H(n)$ we have

$$
\{ f(A) : A\subseteq Y\}=X.
$$

Prove that

$$
H(n)-\log_2 n \to \infty.
$$

**Status.** Open.

**Source.** [erdosproblems.com/624](https://www.erdosproblems.com/624), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #624,
https://www.erdosproblems.com/624.

**References.**

- [ErHa68] Erdős, P. and Hajnal, A., On a combinatorial problem. Mat. Lapok
  (1968), 345-348.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/624.lean).

## Current assessment

The [[research/methods/finite_set_thresholds|cube-counting argument]] proves
$H(2^h)\ge h+1$ for $h\ge2$, and hence $H(n)>\log_2n$ for $n\ge3$.
It uses the unrestricted map in the Statement. The argument is
author-recorded, supplies only a unit gap on powers of two, and does not
prove the gap diverges. The source's outside-the-input map convention is
not silently identified with this one. No wider standing search is supplied.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/set_systems/erdos_1968_egy_kombinatorikus_problemarol/_index|erdos_1968_egy_kombinatorikus_problemarol]]
- [[../library/set_systems/erdos_1968_egy_kombinatorikus_problemarol/conjecture_p346|erdos_1968_egy_kombinatorikus_problemarol / conjecture_p346]]
- [[../library/set_systems/erdos_1968_egy_kombinatorikus_problemarol/theorem_p345|erdos_1968_egy_kombinatorikus_problemarol / theorem_p345]]
- [[../library/set_systems/kunen_2013_impact_paul_erdos_set_theory/_index|kunen_2013_impact_paul_erdos_set_theory]]
- [[../library/set_systems/kunen_2013_impact_paul_erdos_set_theory/theorem_p359_free_set_lemma|kunen_2013_impact_paul_erdos_set_theory / theorem_p359_free_set_lemma]]
- [[../library/set_systems/kunen_2013_impact_paul_erdos_set_theory/theorem_p359_nowhere_dense|kunen_2013_impact_paul_erdos_set_theory / theorem_p359_nowhere_dense]]
- [[../library/set_systems/kunen_2013_impact_paul_erdos_set_theory/theorem_p360_erdos_hajnal_mate|kunen_2013_impact_paul_erdos_set_theory / theorem_p360_erdos_hajnal_mate]]
- [[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|komjath_2025_erdos_hajnal_problem_list]]

<!-- END problem library links -->
