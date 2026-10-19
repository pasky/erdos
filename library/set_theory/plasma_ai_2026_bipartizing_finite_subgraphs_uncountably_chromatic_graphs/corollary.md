---
name: set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/corollary
title: "Corollary: h_G(n)/n tends to infinity for every graph that is not countably colorable"
desc: |
  For every graph $G$ that is not countably colorable, of any cardinality,
  and in particular for every graph of chromatic number $\aleph_1$, the
  least number $h_G(n)$ of deletions that make every $n$-vertex subgraph
  bipartite satisfies $h_G(n)/n\to\infty$; its Lean formalization is rebuilt
  and kernel-replayed here.
created: 2026-10-18T02:15:08Z
updated: 2026-10-19T06:23:35Z
---

***

## Statement

For a graph $G$ let $h_G(n)$ be the least number such that every subgraph of
$G$ on $n$ vertices can be made bipartite by deleting at most $h_G(n)$ edges.
**Corollary.** If $G$ is not countably colorable, whatever the cardinality of
its vertex set, then $h_G(n)/n\to\infty$: for every $K$ there is an $N$ with
$h_G(n)>Kn$ for all $n\ge N$. In particular this holds for every graph of
chromatic number $\aleph_1$, which answers the second question of
[[../wiki/problems/set_theory/E0111/_index|Problem 111]] in the affirmative.

The corollary follows from the
[[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/main_theorem|main theorem]]:
if the limit failed for some $K$, a maximal family of pairwise vertex-disjoint
finite subgraphs each needing more than $2K$ deletions per vertex would be
countable, and deleting its vertices would leave a $2K$-linear graph that is
not countably colorable. An uncountable family packs into $n$ vertices with
more than $Kn$ deletions for every large $n$.

**Source.** Plasma AI, *Erdős Problem 111: bipartizing finite subgraphs of
uncountably chromatic graphs* (2026), `README.md`, **Corollary.**, and
`blueprint/proof.md`, Section 1, in
[plasma-ai/erdos-111](https://github.com/plasma-ai/erdos-111) at de72caf.
The formalization states it as `Erdos111.tendsto_of_not_countably_colorable`
(for every graph with no coloring by $\mathbb N$) and `Erdos111.erdos_111`
(for `chromaticCardinal G = ℵ₁`) in `Challenge.lean`, with `h G n` the
supremum over subgraphs on $n$ vertices of the least number of deletions that
leave them bipartite, and proves both in `Solution.lean`.

**Read depth.** Claims checked: the statement was read in the README and
compared with `Challenge.lean`; the proof was not read. The formalization's
proofs were rebuilt, checked with Comparator and replayed in the kernel
([[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/replay_receipt|the replay receipt]]),
and the
[[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/statement_fidelity/_index|statement-fidelity audit]]
found both statements faithful, graded on 2026-10-18.

## Bears on

- [[../wiki/problems/set_theory/E0111/_index|Problem 111]]: the second
  question, answered yes;
  [[../wiki/problems/set_theory/E0111/claims/2026_10_19_plasma_ai|the claim page]]
  is accepted on the formalization. The first question is open-ended and not
  addressed beyond the divergence.
