---
name: additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_741_i
title: "Erdős #741-(i): a set whose sumset has positive upper density splits into two such sets"
desc: |
  If A+A has positive upper density then A splits into two parts whose
  sumsets both have positive upper density, by an alternating block
  partition. The Lean file the paper links proves another statement.
created: 2026-10-13T10:06:04Z
updated: 2026-10-13T10:06:04Z
---

***

**Source.** Appendix B.4, section "Erdős #741-(i)", Question and Proof,
pp. 36--37 of arXiv:2605.22763v2, the edition named on
[[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/_index|the card]];
the published version in Science was not read. Table 1 (p. 7) lists it as
741 (i), and Section 3 (p. 6) describes the change of density reading.

## Statement

Let $A\subseteq\mathbb N$ be such that $A+A$ has positive upper density. Then
$A=A_1\sqcup A_2$ with $A_1+A_1$ and $A_2+A_2$ both of positive upper density
(pp. 36--37).

The paper reports (p. 37, and Section 3, p. 6) that the agent first disproved
the formulation in which density must exist as a limit, and that the formal
statement was amended to upper density, following the site curator's remark
that Erdős likely meant upper density, before the agent proved the statement
above.

**Discrepancy: the linked Lean file proves the exact-density answer.** The
paper (p. 37) gives
[`erdos_741.parts.i.lean`](https://github.com/google-deepmind/alphaproof-nexus-results/blob/42f344cfa9d57154f36e6b9bef1f71760a438c54/APNOutputs/ErdosProblems/erdos_741.parts.i.lean)
(1,504 lines), cited at the repository commit of 2026-05-13, as the Lean proof
of the upper-density statement. The file does not prove it. Its
`target_theorem_0` proves
`answer(False) ↔ ∀ A : Set ℕ, HasPosDensity (A + A) → ∃ A₁ A₂, A = A₁ ∪ A₂ ∧ Disjoint A₁ A₂ ∧ HasPosDensity (A₁ + A₁) ∧ HasPosDensity (A₂ + A₂)`,
where formal-conjectures' `HasPosDensity S` says that the natural density of
$S$ exists and is positive. That is the exact-density reading, answered no by
the set `SandorA`, a union of integers with restricted base-4 digits and of the
intervals $[4^{3^k},10\cdot4^{3^k})$: the counterexample first posted on
2026-03-31, filed under the name that formal-conjectures then gave the
statement, which upstream now calls `erdos_741.variants.exact_density`. The
repository's prose PDF `erdos741i.pdf` is the upper-density proof, so the
paper's prose and its Lean file disagree. The Lean proof of the upper-density
statement is the formal-conjectures commit of 2026-04-16 linked from the claim
page below. Read statically, not built.

**Read depth.** Claims checked: the question and both cases of the proof were
read clause by clause on the page images of pp. 36--37. The proof was read
for its structure only; nothing here is independently reviewed.

## Proof pointer

Choose a fast-growing sequence $M_0<M_1<\cdots$ and let $A_1$ be the part of
$A$ in the intervals $(M_{2k},M_{2k+1}]$ and $A_2$ the rest. If $A$ has
positive upper density, with $|A\cap[1,N]|\ge cN$ along a sequence of scales,
dependent choice gives $M_k$ with $|A\cap[1,M_{k+1}]|\ge cM_{k+1}$ and
$|A\cap[1,M_k]|\le\tfrac c4M_{k+1}$; then $A_1$ and $A_2$ have positive upper
density, and so do their sumsets. If $A$ has upper density zero, choose $M_k$
with $|(A+A)\cap[1,M_{k+1}]|\ge cM_{k+1}$ and
$(M_k+1)|A\cap[1,M_{k+1}]|\le\tfrac c4M_{k+1}$. When every element of $A_2$
up to $N$ is at most $K$,
$|(A+A)\cap[1,N]|\le|(A_1+A_1)\cap[1,N]|+(K+1)|A\cap[1,N]|$, so at the scales
$N=M_{2k+1}$ the sumset $A_1+A_1$ has at least $\tfrac{3c}4N$ elements up to
$N$, and symmetrically for $A_2$ at $N=M_{2k+2}$ (pp. 36--37).

## Dependencies

None; the argument is elementary.

## Bears on

- [[../wiki/problems/additive_combinatorics/E0741/_index|Problem 741]]: the
  first question, under the upper-density reading the site adopts, is answered
  yes. The paper calls the problem's thread its original communication of the
  result (p. 38). The result is recorded on the claim page
  [[../wiki/problems/additive_combinatorics/E0741/claims/2026_03_31_deepmind|Google DeepMind 2026]],
  which also records the exact-density answer that the linked Lean file proves.
