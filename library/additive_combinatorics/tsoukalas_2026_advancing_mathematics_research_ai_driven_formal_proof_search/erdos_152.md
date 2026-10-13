---
name: additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_152
title: "Erdős #152: a Sidon set of size n has at least (n^2 - 100n - 16)/16 isolated sums"
desc: |
  Every Sidon set of size n has at least (n^2 - 100n - 16)/16 elements s of
  A+A with s-1 and s+1 outside A+A, so the minimum f(n) tends to infinity;
  proved by counting adjacent pairs in the sumset and the difference set.
created: 2026-10-13T10:06:04Z
updated: 2026-10-13T10:06:04Z
---

***

**Source.** Appendix B.4, section "Erdős #152", Theorem and Proof, pp. 42--43
of arXiv:2605.22763v2, the edition named on
[[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/_index|the card]];
the published version in Science was not read. Table 1 (p. 7) lists it as 152.

## Statement

For a Sidon set $A\subset\mathbb N$ with $|A|=n$, let $I(A+A)$ be the number of
$s\in A+A$ with $s-1\notin A+A$ and $s+1\notin A+A$, and let $f(n)$ be the
minimum of $I(A+A)$ over Sidon sets of size $n$. Then every Sidon set of size
$n$ satisfies

$$
16\,I(A+A)+100n+16\ge n^2,
$$

so $f(n)\ge(n^2-100n-16)/16$, and in particular $f(n)\to\infty$ (p. 42).

**Lean.** The paper (p. 43) gives
[`erdos_152.lean`](https://github.com/google-deepmind/alphaproof-nexus-results/blob/42f344cfa9d57154f36e6b9bef1f71760a438c54/APNOutputs/ErdosProblems/erdos_152.lean)
(517 lines), cited at the repository commit of 2026-05-13, as the Lean proof.
It defines `f n` as the infimum, over Sidon sets `A ⊆ ℕ` with `A.ncard = n`, of
the number of $s$ with $s-1\notin A+A$, $s\in A+A$ and $s+1\notin A+A$
(natural-number subtraction), proves `f_lower_bound_div`,
`f n ≥ (n * n - 100 * n - 16) / 16` in natural-number arithmetic, and from it
`target_theorem_0`, `answer(True) ↔ Tendsto f atTop atTop`, the statement
`erdos_152` of formal-conjectures. Read statically, not built.

**Read depth.** Claims checked: the statement was read clause by clause on the
page image of p. 42. The proof was read for its structure only; nothing here is
independently reviewed.

## Proof pointer

For $X\subseteq\mathbb Z$ let $N_k(X)$ count $x\in X$ with $x+k\in X$ and
$V_2(X)$ the elements with both neighbors in $X$. Three counting facts hold for
finite $X$: $I(X)+2N_1(X)=|X|+V_2(X)$; $4N_1(X)+N_3(X)\le3|X|+2N_2(X)$, from a
pointwise inequality on windows of four consecutive integers; and
$2N_2(X)\le N_3(X)+2V_2(X)+2I(X)$. For $k=1,2,3$ the quadruples in $A^4$ with
$a+b+k=c+d$ number at most $N_k(D)+2n$, where $D=A-A$, by the Sidon property,
and at least $4N_k(S)-8n$, where $S=A+A$. Applying the second fact to $D$,
transferring to $S$ and using the other two facts, the terms in $N_1$, $N_3$
and $V_2$ cancel and leave $16\,I(S)+100n\ge8|S|-3|D|$; with $|S|\ge n^2/2$,
$|D|\le n^2$ and a correction of $16$ at zero this is the bound (pp. 42--43).

## Dependencies

The standard Sidon-set counts $|A+A|\ge n^2/2$ and $|A-A|\le n^2$; no other
source.

## Bears on

- [[../wiki/problems/additive_bases/E0152/_index|Problem 152]]: the problem
  asks whether, for every $M$, every sufficiently large finite Sidon set has at
  least $M$ such isolated sums; the theorem answers it yes, with quadratically
  many. The paper names no forum post for this result. It is recorded on the
  claim page
  [[../wiki/problems/additive_bases/E0152/claims/2026_04_03_deepmind|Google DeepMind 2026]].
