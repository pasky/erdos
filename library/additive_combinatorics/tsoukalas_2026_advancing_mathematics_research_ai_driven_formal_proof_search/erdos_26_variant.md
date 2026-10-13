---
name: additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_26_variant
title: "Erdős #26, More General Variant: a thick sequence whose shifts all have multiples of upper density below 3/4"
desc: |
  A sequence with divergent reciprocal sum such that for every shift k >= 1
  the multiples of A + k have upper density below 3/4, refuting Tenenbaum's
  variant; the Lean file states a lower-density bound instead.
created: 2026-10-13T10:06:04Z
updated: 2026-10-13T10:06:04Z
---

***

**Source.** Appendix B.4, section "Erdős #26, More General Variant", Theorem
and Proof, pp. 38--40 of arXiv:2605.22763v2, the edition named on
[[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/_index|the card]];
the published version in Science was not read. Table 1 (p. 7) lists it as 26,
marked as a variant and as a generalization of Erdős's question that Erdős did
not pose.

## Statement

For a set $S$ of positive integers let $\mathcal M(S)$ be the set of multiples
of its elements, and let $\overline d$ be upper asymptotic density. There is a
sequence $A:\mathbb N\to\mathbb N$ with $\sum_i1/A(i)=\infty$ such that, with
$\epsilon=1/4$,

$$
\overline d\bigl(\mathcal M(A+k)\bigr)<1-\epsilon=\tfrac34
\qquad\text{for every }k\ge1,
$$

where $A+k$ is the shifted sequence $A(i)+k$ (p. 38). The construction makes
$A$ strictly increasing, and the proof's union bound gives the smaller value
$0.1+0.2+1/29\approx0.334$ (p. 40). Tenenbaum's variant asks whether, for every
thick sequence and every $\epsilon>0$, some shift has multiples of density at
least $1-\epsilon$; the theorem refutes it. Since no shift's multiples have
density one, the same sequence answers no to the question as the site states
it, which the paper says Ruzsa's simpler counterexample had already resolved
(pp. 38, 40).

**Discrepancy: the Lean file states a different bound.** The paper (p. 40)
gives
[`erdos_26.variants.tenenbaum.lean`](https://github.com/google-deepmind/alphaproof-nexus-results/blob/42f344cfa9d57154f36e6b9bef1f71760a438c54/APNOutputs/ErdosProblems/erdos_26.variants.tenenbaum.lean)
(1,066 lines), cited at the repository commit of 2026-05-13, as the Lean proof.
Its `target_theorem_0` proves `answer(False)` for formal-conjectures'
`erdos_26.variants.tenenbaum`, that every strictly increasing thick
`A : ℕ → ℕ` has, for every $\varepsilon>0$, a shift `k` with
`1 - ε ≤ (MultiplesOf (A · + k)).lowerDensity`. It refutes the statement with
its own sequence `seqA` and $\varepsilon=1/2$, through `seqA_density_bound`:
for every `k`, zero included, the multiples of `seqA + k` have lower density
below $1/2$ (the file counts at most $\tfrac{37}{90}N$ of them up to every
$N\ge1$). The prose's bound is on the upper density with $\epsilon=1/4$; both
refute the variant. Read statically, not built.

**Read depth.** Claims checked: the statement and the three cases of the proof
were read clause by clause on the page images of pp. 38--40. The proof was read
for its structure only; nothing here is independently reviewed.

## Proof pointer

Fix primes $29\le q_1<q_2<\cdots$ and build $A$ in blocks, with $J_m$ the number
of terms before block $m$ and $J_0=0$. Block $m$ uses the step
$P_m=\prod_{j\le10J_m}q_j$, a base $R_m$ with $R_m\equiv-j\pmod{q_j}$ for
$1\le j\le10J_m$ and above the previous term, and a length $L_m$ for which
$\sum_{x=1}^{L_m}1/(R_m+xP_m)$ lies between $0.1$ and $0.2$; its terms are
$R_m+xP_m$, $1\le x\le L_m$. Every block adds at least $0.1$ to the reciprocal
sum, so the sum diverges. For a shift $k$ with $10J_{m_0}\le k<10J_{m_0+1}$,
the terms before block $m_0$ contribute multiples of upper density at most
$J_{m_0}/k\le0.1$, block $m_0$ at most its reciprocal sum $0.2$, and every later
term $A(i)$ has $q_k\mid A(i)+k$, so the rest lie among the multiples of $q_k$,
of density $1/q_k\le1/29$ (pp. 38--40).

## Dependencies

The Chinese remainder theorem; no other source.

## Bears on

- [[../wiki/problems/divisors/E0026/_index|Problem 26]]: the theorem refutes
  Tenenbaum's variant, which the paper says Erdős did not pose, and through it
  answers the site's question no with a set of divergent reciprocal sum. The
  paper calls the problem's thread its original communication of the result
  (p. 40). The result is recorded on the claim page
  [[../wiki/problems/divisors/E0026/claims/2026_04_06_deepmind|Google DeepMind 2026]].
