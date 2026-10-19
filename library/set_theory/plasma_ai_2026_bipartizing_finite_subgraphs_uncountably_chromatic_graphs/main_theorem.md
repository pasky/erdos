---
name: set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/main_theorem
title: "Main theorem: graphs with linear bipartization cost are countably colorable"
desc: |
  For every $C\ge0$, a graph in which every finite subgraph on $m$ vertices
  can be made bipartite by deleting at most $Cm$ edges has countable
  chromatic number, at every vertex cardinality; its Lean formalization is
  rebuilt and kernel-replayed here.
created: 2026-10-18T02:15:08Z
updated: 2026-10-19T06:23:35Z
---

***

## Statement

For a finite graph $F$ let $\beta(F)$ be the least number of edges whose
deletion leaves $F$ bipartite. **Theorem.** Let $C\ge0$, and let $G$ be a
simple graph, on a vertex set of any cardinality, such that
$\beta(F)\le C|V(F)|$ for every finite subgraph $F$ of $G$. Then $G$ has
countable chromatic number.

**Source.** Plasma AI, *Erdős Problem 111: bipartizing finite subgraphs of
uncountably chromatic graphs* (2026), `README.md`, **Theorem.**, and
`blueprint/proof.md`, Section 6, in
[plasma-ai/erdos-111](https://github.com/plasma-ai/erdos-111) at de72caf.
The formalization states it as `Erdos111.countably_colorable_of_linear` in
`Challenge.lean`, for every real $C$ and every subgraph `H` with finitely many
vertices, with conclusion a proper coloring by $\mathbb N$, and proves it in
`Solution.lean`.

**Read depth.** Claims checked: the statement was read in the README and
compared with `Challenge.lean`; the proof was not read. The formalization's
proof was rebuilt, checked with Comparator and replayed in the kernel
([[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/replay_receipt|the replay receipt]]),
and the
[[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/statement_fidelity/_index|statement-fidelity audit]]
found the statement faithful to this theorem, graded on 2026-10-18.

## Bears on

- [[../wiki/problems/set_theory/E0111/_index|Problem 111]]: with countable
  deletion and packing it gives the
  [[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/corollary|corollary]],
  which answers the second question.
