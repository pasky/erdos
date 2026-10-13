---
name: additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_125
title: "Erdős #125: the sum of the base-3 and base-4 digit sets has lower density zero"
desc: |
  With A and B the integers whose base-3 and base-4 digits are all 0 or 1, the
  lower density of A+B is zero, by an inductive thinning along scales where a
  power of 3 nearly equals a power of 4.
created: 2026-10-13T10:06:04Z
updated: 2026-10-13T10:06:04Z
---

***

**Source.** Appendix B.4, section "Erdős #125", Question and Proof, pp. 34--35
of arXiv:2605.22763v2, the edition named on
[[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/_index|the card]];
the published version in Science was not read. Table 1 (p. 7) and Section 3
(p. 4) also state it.

## Statement

Let $A$ be the set of nonnegative integers whose base-3 digits are all $0$ or
$1$, and $B$ the set of those whose base-4 digits are all $0$ or $1$. Then the
lower density of $A+B$ is $0$: for every $\epsilon>0$ there are arbitrarily
large $N$ with $|(A+B)\cap[0,N)|\le\epsilon N$. So $A+B$ does not have positive
lower density (pp. 34--35).

The paper adds (p. 35) that this leaves two possibilities: $A+B$ has upper
density $0$ as well, or it has positive upper density and so no density.

**Lean.** The paper (p. 35) gives
[`erdos_125.variants.positive_lower_density.lean`](https://github.com/google-deepmind/alphaproof-nexus-results/blob/42f344cfa9d57154f36e6b9bef1f71760a438c54/APNOutputs/ErdosProblems/erdos_125.variants.positive_lower_density.lean)
(370 lines), cited at the repository commit of 2026-05-19, as the Lean proof.
Its `target_theorem_0` proves `answer(False) ↔ 0 < (A + B).lowerDensity`,
formal-conjectures' `erdos_125.variants.positive_lower_density`, through the
lemmas `A_B_gap`, `dirichlet_approx`, `scale_step`, `density_multi_scale` (for
every $d$ some $N>0$ with $|(A+B)\cap[0,N)|\le(11/12)^dN$) and
`density_tends_to_zero`. The file's factor is $11/12$ where the prose uses
$0.99$. The proof posted on the site's thread in March 2026 and pinned on the
claim page is a different Lean file, with different lemmas. Read statically,
not built.

**Read depth.** Claims checked: the question and the proof's conclusion were
read clause by clause on the page images of pp. 34--35. The proof was read for
its structure only; nothing here is independently reviewed.

## Proof pointer

Cut $a\in A$ at its $k$-th base-3 digit,
$a=3^ka_{\mathrm{top}}+a_{\mathrm{bot}}$, with both parts in $A$ and
$a_{\mathrm{bot}}\le(3^k-1)/2$, and cut $b\in B$ at its $m$-th base-4 digit,
with $b_{\mathrm{bot}}\le(4^m-1)/3$. If $3^k\le4^m$ and $M=3^k$, every
$x\in A+B$ below $MN_0$ is $3^k(a_{\mathrm{top}}+b_{\mathrm{top}})+c$ with
$a_{\mathrm{top}}+b_{\mathrm{top}}\in(A+B)\cap[0,N_0)$ and $0\le c\le C$, where
$C=|4^m-3^k|N_0+(3^k-1)/2+(4^m-1)/3$; so the proportion of $A+B$ below $MN_0$
is at most the proportion below $N_0$ times $(C+1)/M$. Since $\log4/\log3$ is
irrational, Dirichlet's approximation theorem gives $k$ and $m$ with $4^m/3^k$
close enough to $1$ that $(C+1)/M\le0.99$. Iterating from scale to scale drives
the proportion to $0$ along a sequence of scales (p. 35).

## Dependencies

Dirichlet's approximation theorem and the irrationality of $\log4/\log3$; no
other source.

## Bears on

- [[../wiki/problems/diophantine_problems/E0125/_index|Problem 125]]: the
  problem asks whether $A+B$ has positive lower density; the theorem answers it
  no. Whether $A+B$ has positive upper density stays open. The paper calls post
  5110 of the site's thread its original communication of the result (p. 35).
  The result is recorded on the claim page
  [[../wiki/problems/diophantine_problems/E0125/claims/2026_03_30_deepmind|Google DeepMind 2026]].
