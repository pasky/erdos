---
name: additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_846
title: "Erdős #846: a plane set with many points in general position in every subset that is not a finite union of such sets"
desc: |
  An infinite plane set in which every n points contain n/2 with no three on a
  line, but which is not a finite union of sets with no three on a line: one
  point per edge of the infinite complete graph and the infinite Ramsey
  theorem.
created: 2026-10-13T10:06:04Z
updated: 2026-10-13T10:06:04Z
---

***

**Source.** Appendix B.4, section "Erdős #846", Theorem and Proof, pp. 40--42
of arXiv:2605.22763v2, the edition named on
[[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/_index|the card]];
the published version in Science was not read. Table 1 (p. 7) lists it as 846.

## Statement

There is an infinite set $A\subset\mathbb R^2$ such that every subset of $A$
with $n$ points contains at least $n/2$ points with no three on a line, while
$A$ is not a union of finitely many sets with no three points on a line
(pp. 40--41). This answers no to the question whether every infinite plane set
with, for some $\epsilon>0$, at least $\epsilon n$ such points in every
$n$-point subset is a finite union of sets with no three on a line; here
$\epsilon=1/2$.

**Lean.** The paper (p. 42) gives
[`erdos_846.lean`](https://github.com/google-deepmind/alphaproof-nexus-results/blob/42f344cfa9d57154f36e6b9bef1f71760a438c54/APNOutputs/ErdosProblems/erdos_846.lean)
(923 lines), cited at the repository commit of 2026-05-19, as the Lean proof.
Its `target_theorem_0` proves
`answer(False) ↔ ∀ᵉ (A : Set ℝ²) (ε > 0), A.Infinite → NonTrilinearFor A ε → WeaklyNonTrilinear A`,
the statement `erdos_846` of formal-conjectures, whose `NonTrilinearFor A ε`
asks every finite subset to contain an $\epsilon$-fraction with no three on a
line and whose `WeaklyNonTrilinear A` asks for a finite union of such sets.
Read statically, not built.

**Read depth.** Claims checked: the statement and the two lemmas were read
clause by clause on the page images of pp. 40--41. The proof was read for its
structure only; nothing here is independently reviewed.

## Proof pointer

Label the vertices of the countably infinite complete graph by $x_n=100^{4^n}$
and send each edge $\{x_i,x_j\}$ to the point
$(x_i+x_j,\;x_i^2+x_ix_j+x_j^2)$. The first lemma: three of these points are
collinear exactly when their edges form a triangle; for a triangle on
$a,b,c$ every pair of the three points spans a line of slope $a+b+c$, and for
three edges that do not form a triangle the fast growth of the $x_n$ keeps the
collinearity determinant away from zero. The second lemma: $n$ points come
from $n$ edges, which contain a bipartite subgraph with at least $n/2$ edges,
and a bipartite graph has no triangle. Finally, a cover of $A$ by finitely many
sets with no three on a line colors the edges finitely, and the infinite Ramsey
theorem gives a monochromatic triangle, three collinear points in one set
(pp. 40--41).

## Dependencies

The infinite Ramsey theorem and the fact that every graph with $n$ edges has a
bipartite subgraph with at least $n/2$ of them; no other source.

## Bears on

- [[../wiki/problems/discrete_geometry/E0846/_index|Problem 846]]: the theorem
  answers the question no. The paper calls post 4447 of the erdosproblems.com
  thread its original communication of the result and notes that an internal
  model at OpenAI found it independently and that it also follows from a
  projection argument of Reiher, Rödl and Sales (p. 42). The result is recorded
  on the claim page
  [[../wiki/problems/discrete_geometry/E0846/claims/2026_02_25_deepmind|Google DeepMind 2026]].
