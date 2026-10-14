---
name: extremal_graph_theory/kim_2026_proof_erdos_gallai_cycle_decomposition_conjecture/theorem_1_3
title: "Theorem 1.3 (p. 2): light graphs of large minimum degree have near-closed subgraphs (preprint)"
desc: |
  The preprint's new ingredient: a light graph of large minimum degree has a
  set S inducing minimum degree at least |S|^(1/1000) with at least |S|/12
  vertices having at most two neighbors outside S; statement only checked.
created: 2026-10-14T00:20:00Z
updated: 2026-10-14T00:25:00Z
---

***

## Statement

A cycle $C$ of a graph $G$ is heavy if there is a real $b\ge1$ such that at
least $b^{3/2}$ vertices of $C$ have degree at most $b$ in $G$, and $G$ is
light if it has no heavy cycle (Definition 1.2, p. 2). **Theorem 1.3.** There
is $\delta_0$ such that every light graph $G$ with minimum degree at least
$\delta_0$ has a nonempty set $S\subseteq V(G)$ for which $G[S]$ has minimum
degree at least $|S|^{1/1000}$ and at least $|S|/12$ vertices of $S$ have at
most two neighbors outside $S$ in $G$. The paper calls such a set near-closed
and did not try to optimize the exponent or the constant $12$.

**Source.** arXiv:2610.07840v2, Theorem 1.3 on p. 2, proved in Sections 3--5.
The edition is identified in the
[[extremal_graph_theory/kim_2026_proof_erdos_gallai_cycle_decomposition_conjecture/_index|source digest]].

**Read depth.** Claims checked for the statement; the proof was read only
through the paper's outline (Section 2.2) and was not checked.

## Proof pointer

By the outline, lightness bounds the length of every cycle in a subgraph whose
high-degree vertices are independent, so a depth-first search forest cuts it
into small regions with small separators; and only few vertices of small
degree can have two neighbors of much larger degree, since otherwise those
paths link into a heavy cycle. A degree window, the regions and the removal of
low-degree vertices then yield the set $S$ (Section 5). The proof uses no
expanders.

## Bears on

- [[../wiki/problems/extremal_graph_theory/E0184/_index|#184]]: one of the two
  ingredients of
  [[extremal_graph_theory/kim_2026_proof_erdos_gallai_cycle_decomposition_conjecture/theorem_1_1|Theorem 1.1]].
