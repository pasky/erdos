---
name: additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_741_ii
title: "Erdős #741-(ii): a basis of order 2 that no partition splits into two self-sumsets with bounded gaps"
desc: |
  A set A with A together with 0 a basis of order 2 such that in every
  partition of A into two parts one part's sumset has unbounded gaps, built
  from forbidden zones at scales 100^k, each with one surviving element.
created: 2026-10-13T10:06:04Z
updated: 2026-10-13T10:06:04Z
---

***

**Source.** Appendix B.4, section "Erdős #741-(ii)", Question and Proof,
pp. 37--38 of arXiv:2605.22763v2, the edition named on
[[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/_index|the card]];
the published version in Science was not read. Table 1 (p. 7) lists it as
741 (ii).

## Statement

There is a set $A\subseteq\mathbb N$ such that $A\cup\{0\}$ is a basis of order
$2$, that is, every natural number is a sum of two elements of $A\cup\{0\}$,
and for every partition $A=A_1\sqcup A_2$ the sets $A_1+A_1$ and $A_2+A_2$ do
not both have bounded gaps (pp. 37--38). The question is worded with $A$ as the
basis; the proof's Step 2 shows that $A\cup\{0\}$ is one.

**Lean.** The repository's file for this result is
[`erdos_741.parts.ii.lean`](https://github.com/google-deepmind/alphaproof-nexus-results/blob/42f344cfa9d57154f36e6b9bef1f71760a438c54/APNOutputs/ErdosProblems/erdos_741.parts.ii.lean)
(657 lines), cited at the repository commit of 2026-05-19. Its
`target_theorem_0` proves
`answer(True) ↔ ∃ A : Set ℕ, IsAddBasisOfOrder (A ∪ {0}) 2 ∧ ∀ A₁ A₂, A = A₁ ∪ A₂ → Disjoint A₁ A₂ → ¬(IsSyndetic (A₁ + A₁) ∧ IsSyndetic (A₂ + A₂))`,
formal-conjectures' `erdos_741.parts.ii`. The file builds its set by a
recursive extension step (`valid_ext_exists`, `seq_step`) and does not use the
scales $100^k$ of the prose; the two constructions were not compared further.
Read statically, not built.

**Discrepancy.** The paper (p. 38) gives `erdos_12.parts.ii.lean`, the file for
Problem 12's second question, as the Lean proof of this result; the file above
is the right one.

**Read depth.** Claims checked: the question and the three steps of the proof
were read clause by clause on the page images of pp. 37--38. The proof was read
for its structure only; nothing here is independently reviewed.

## Proof pointer

Take scales $P_k=100^k$. For each $k\ge1$ remove from $\mathbb N$ a zone $Z_k$
running roughly from $\tfrac{11}2P_k$ to $11P_k+k$, except for the single
element $x_k=10P_k$; $A$ is what remains. A number outside every zone is in
$A$; one in the lower half of $Z_k$ is $\lfloor n/2\rfloor+\lceil n/2\rceil$
with both halves in $A$; one in the upper half is $x_k+(n-x_k)$ with
$n-x_k$ below $Z_k$. A sum in $[11P_k,11P_k+k]$ of two elements of $A$ needs a
summand in the zone, so it uses $x_k$; the part of the partition without $x_k$
has a self-sumset missing that whole interval, a gap of length $k$, and one
part misses infinitely many such intervals (pp. 37--38).

## Dependencies

None; the argument is elementary.

## Bears on

- [[../wiki/problems/additive_combinatorics/E0741/_index|Problem 741]]: the
  second question is answered yes. The paper calls the problem's thread its
  original communication of the result (p. 38). The result is recorded on the
  claim page
  [[../wiki/problems/additive_combinatorics/E0741/claims/2026_03_31_deepmind|Google DeepMind 2026]];
  the same answer was found independently in the Alexeev, Putterman, Sawhney,
  Sellke and Valiant preprint, recorded on its own claim page.
