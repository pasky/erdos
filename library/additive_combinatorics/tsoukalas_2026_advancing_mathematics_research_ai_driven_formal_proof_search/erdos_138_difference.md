---
name: additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/erdos_138_difference
title: "Erdős #138, Differences Variant: W(k+1) is at least W(k) + k"
desc: |
  The two-color van der Waerden numbers satisfy W(k+1) >= W(k) + k, so
  W(k+1) - W(k) tends to infinity, by extending a coloring greedily; this is
  Erdős's difference question of 1981, not the problem's main request.
created: 2026-10-13T10:06:04Z
updated: 2026-10-13T10:06:04Z
---

***

**Source.** Appendix B.4, section "Erdős #138, Differences Variant", Question
and Proof, pp. 35--36 of arXiv:2605.22763v2, the edition named on
[[additive_combinatorics/tsoukalas_2026_advancing_mathematics_research_ai_driven_formal_proof_search/_index|the card]];
the published version in Science was not read. Table 1 (p. 7) lists it as
138, marked as a variant of the problem with that number.

## Statement

Let $W(k)$ be the two-color van der Waerden number: the least $N$ such that
every coloring of $\{1,\ldots,N\}$ with two colors has a monochromatic $k$-term
arithmetic progression. Then for every $k\ge1$

$$
W(k+1)\ge W(k)+k,
$$

so $W(k+1)-W(k)\to\infty$ (pp. 35--36).

**Lean.** The paper (p. 36) gives
[`erdos_138.variants.difference.lean`](https://github.com/google-deepmind/alphaproof-nexus-results/blob/42f344cfa9d57154f36e6b9bef1f71760a438c54/APNOutputs/ErdosProblems/erdos_138.variants.difference.lean)
(918 lines), cited at the repository commit of 2026-05-19, as the Lean proof.
Its `target_theorem_0` proves `answer(True)` for formal-conjectures'
`erdos_138.variants.difference`, that `W (k + 1) - W k` tends to infinity,
with `W` defined as the infimum of the $N$ whose two-colorings of
$\{1,\ldots,N\}$ all contain a monochromatic $k$-term progression; the lemma
`W_diff_ge_k_all` gives `W (k + 1) - W k ≥ k` for every `k` (natural-number
subtraction). The proof posted on the site's thread in April 2026 and pinned on
the claim page is a different Lean file, ending in a lemma `W_diff_tendsto`.
Read statically, not built.

**Read depth.** Claims checked: the question and the bound were read clause by
clause on the page images of pp. 35--36. The proof was read in full but not
checked step by step; nothing here is independently reviewed.

## Proof pointer

Start from a two-coloring of $\{1,\ldots,W(k)-1\}$ with no monochromatic
$k$-term progression and add $k$ further integers one at a time, coloring each
red unless that completes a red $(k+1)$-term progression and blue otherwise.
Both colors are blocked only if a red and a blue $k$-term progression both have
the new integer as their next term. Each contains a newly added integer, so both
common differences $d_R,d_B$ are at most $k-1$, and stepping back $d_B$ terms
along the red one and $d_R$ terms along the blue one lands on the same positive
integer, which would carry both colors (p. 36). The site's curator noted on the
thread that the argument generalizes to $W(k+1,l+1)\ge W(k,l)+\min(k,l)$
(p. 36).

## Dependencies

None; the argument is elementary.

## Bears on

- [[../wiki/problems/additive_combinatorics/E0138/_index|Problem 138]]: the
  problem asks for better bounds on $W(k)$, for example
  $W(k)^{1/k}\to\infty$. The theorem answers a different question, Erdős's of
  1981 whether $W(k+1)-W(k)\to\infty$, recorded in the site's commentary, and
  leaves the problem's request untouched. The paper calls post 5314 of the
  site's thread its original communication of the result (p. 36). The result
  is recorded on the claim page
  [[../wiki/problems/additive_combinatorics/E0138/claims/2026_04_10_deepmind|Google DeepMind 2026]].
