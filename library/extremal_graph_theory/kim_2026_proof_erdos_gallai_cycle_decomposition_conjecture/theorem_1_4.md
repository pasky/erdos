---
name: extremal_graph_theory/kim_2026_proof_erdos_gallai_cycle_decomposition_conjecture/theorem_1_4
title: "Theorem 1.4 (p. 2): graphs of polynomial minimum degree decompose into O(n) cycles and edges (preprint)"
desc: |
  The preprint's extension of Conlon, Fox and Sudakov's linear-minimum-degree
  theorem: for every eps > 0, a graph on n vertices with minimum degree at
  least n^eps decomposes into at most C_eps n cycles and edges; statement only
  checked.
created: 2026-10-14T00:20:00Z
updated: 2026-10-14T00:25:00Z
---

***

## Statement

**Theorem 1.4.** For every $\varepsilon>0$ there is $C_\varepsilon$ such that
the edges of every graph on $n$ vertices with minimum degree at least
$n^{\varepsilon}$ decompose into at most $C_\varepsilon n$ cycles and edges.
It extends
[[extremal_graph_theory/conlon_2014_cycle_packing/theorem_1_4|Conlon, Fox and Sudakov's theorem]]
for linear minimum degree to polynomial minimum degree.

**Source.** arXiv:2610.07840v2, Theorem 1.4 on p. 2, proved in Section 6. The
edition is identified in the
[[extremal_graph_theory/kim_2026_proof_erdos_gallai_cycle_decomposition_conjecture/_index|source digest]].

**Read depth.** Claims checked for the statement and for the quoted results it
rests on; the proof was read only through the paper's outline (Section 2.3)
and was not checked.

## Proof pointer

Section 6 uses robust sublinear expanders. It quotes, as its Theorem 6.2 (p.
15), three results of
[[extremal_graph_theory/bucic_2022_towards_erdos_gallai_cycle_decomposition_conjecture/_index|Bucić and Montgomery]]
in the numbering of arXiv:2211.07689v2: a decomposition of every $m$-vertex
graph into at most $m$ paths (their Corollary 22); the removal of at most
$4sm\log m$ edges leaving $s$-expanders whose orders sum to at most $2m$ (their
Lemma 14); and a decomposition of every graph on $m\ge2$ vertices into at most
$6m$ cycles and $O(m\log^{274}m)$ edges (their Theorem 24). As its Theorem 6.3
it quotes two results of
[[extremal_graph_theory/conlon_2014_cycle_packing/_index|Conlon, Fox and Sudakov]]:
every $(\rho,c)$-sparse graph on $m$ vertices decomposes into $O(m)$ cycles and
edges (their Corollary 4.3), and $G(m,p)$ is $(\rho,2/\rho)$-sparse with high
probability for $p\le m^{-\rho}$ (their Lemma 4.4). A random splitting lemma, a
short-path lemma and a deterministic routing lemma then turn the leftover
edges into short and medium cycles. The proof ends with
$C_\varepsilon=\max\{15+2b_{\varepsilon/3},n_0/2\}$.

## Bears on

- [[../wiki/problems/extremal_graph_theory/E0184/_index|#184]]: one of the two
  ingredients of
  [[extremal_graph_theory/kim_2026_proof_erdos_gallai_cycle_decomposition_conjecture/theorem_1_1|Theorem 1.1]].
