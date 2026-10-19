---
name: problems/extremal_graph_theory/E0614
title: Problem 614
desc: |
  Asks for the fewest edges in a graph on $n$ vertices in which every set of
  $k+2$ vertices induces a subgraph of maximum degree at least $k$.
tags:
- Graph theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-18T22:19:33Z
---

# Problem 614

[[problems/extremal_graph_theory/_index|..]]

[[problems/extremal_graph_theory/E0614/claims/_index|claims/]]: The 1 claim page of Problem 614, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $f(n,k)$ be minimal such that there is a graph with $n$
vertices and $f(n,k)$ edges where every set of $k+2$ vertices induces a subgraph
with maximum degree at least $k$. Determine $f(n,k)$.

**Status.** Open.

**Source.** [erdosproblems.com/614](https://www.erdosproblems.com/614), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #614,
https://www.erdosproblems.com/614.

**Formalization.** None recorded.

## Current assessment

The [[research/graph_ramsey_interfaces/local_degree_complement_reduction|complement reduction]]
gives $f(n,k)=\binom n2-\operatorname{ex}(n,\mathcal F_{k+2})$ for
$k\ge1$ and $n\ge k+2$, where $\mathcal F_{k+2}$ is the family of
$(k+2)$-vertex graphs with minimum degree at least two. Mantel's theorem
then evaluates the case $k=1$, while $k=2$ reduces exactly to
$\operatorname{ex}(n,C_4)$. The reduction is author-recorded by Plasma AI;
it leaves the all-order four-cycle extremal function and the general
parameter unresolved. An unrefereed note by Ma and Tang, posted on the
erdosproblems.com discussion thread, gives the same complement reduction and
the same consequences for $k=1$ and $k=2$; it is a pending partial claim on
[[problems/extremal_graph_theory/E0614/claims/2026_01_07_ma_tang|its claim page]].
