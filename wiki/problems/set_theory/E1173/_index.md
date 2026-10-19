---
name: problems/set_theory/E1173
title: Problem 1173
desc: |
  Asks whether, under the generalized continuum hypothesis, every set mapping on
  $\omega_{\omega+1}$ whose values have size at most $\aleph_\omega$ and
  pairwise intersections of size below $\aleph_\omega$ has a free set of size
  $\aleph_{\omega+1}$.
tags:
- Set theory
- Combinatorics
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 1173

[[problems/set_theory/_index|..]]

***

**Statement.** Assume the generalised continuum hypothesis. Let

$$
f: \omega_{\omega+1}\to [\omega_{\omega+1}]^{\leq \aleph_\omega}
$$

be a set mapping such that

$$
\lvert f(\alpha)\cap f(\beta)\rvert <\aleph_\omega
$$

for all $\alpha\neq \beta$. Does there exist a free set of cardinality
$\aleph_{\omega+1}$?

**Status.** Open. The erdosproblems.com label was OPEN.

**Source.** [erdosproblems.com/1173](https://www.erdosproblems.com/1173),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1173,
https://www.erdosproblems.com/1173.

**Formalization.** None recorded.

## Current assessment

The held free-set theorem handles the subcase in which sufficiently many
values have size strictly below $\aleph_\omega$, as follows. This is an
author-recorded specialization of a theorem read at statement depth, not an
independent review of its proof or a current literature survey. The full
question, including values of size exactly $\aleph_\omega$, is unresolved
by this argument.

Put $\mu=\aleph_\omega$ and $\lambda=\mu^+$. If
$A=\{x<\lambda:|f(x)|<\mu\}$ has size $\lambda$, transport $A$ by a
bijection to $\lambda$ and restrict each value to $A$.
[[../library/set_systems/kunen_2013_impact_paul_erdos_set_theory/theorem_p359_free_set_lemma|Hajnal's Free Set Lemma]]
applies with bound $\mu<\lambda$ and gives a free set of size $\lambda$.
The lemma requires no regularity of $\mu$; neither GCH nor the pairwise
intersection hypothesis is needed for this subcase.

Consequently a counterexample must have at most $\mu$ vertices with smaller
values, and $\lambda$ vertices whose original values have size exactly
$\mu$. This does not imply that restricting the map to those vertices
preserves the size of every value. The distinction matters for any proposed
normalization. The example $f(\alpha)=\alpha$ on $\mu^+$ shows that
replacing the strict bound in Hajnal's lemma by $\le\mu$ is impossible:
it has no free pair. It fails the pairwise intersection hypothesis here and
is not a counterexample to the problem.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/set_systems/kunen_2013_impact_paul_erdos_set_theory/_index|kunen_2013_impact_paul_erdos_set_theory]]
- [[../library/set_systems/kunen_2013_impact_paul_erdos_set_theory/theorem_p359_free_set_lemma|kunen_2013_impact_paul_erdos_set_theory / theorem_p359_free_set_lemma]]
- [[../library/set_theory/erdos_1974_unsolved_solved_problems_set_theory/_index|erdos_1974_unsolved_solved_problems_set_theory]]
- [[../library/set_theory/erdos_1974_unsolved_solved_problems_set_theory/problem_35|erdos_1974_unsolved_solved_problems_set_theory / problem_35]]
- [[../library/set_theory/erdos_1974_unsolved_solved_problems_set_theory/theorem_p278_shelah|erdos_1974_unsolved_solved_problems_set_theory / theorem_p278_shelah]]
- [[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|komjath_2025_erdos_hajnal_problem_list]]

<!-- END problem library links -->
