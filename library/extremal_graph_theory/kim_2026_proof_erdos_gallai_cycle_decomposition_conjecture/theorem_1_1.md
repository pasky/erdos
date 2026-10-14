---
name: extremal_graph_theory/kim_2026_proof_erdos_gallai_cycle_decomposition_conjecture/theorem_1_1
title: "Theorem 1.1 (p. 1): every n-vertex graph decomposes into O(n) cycles and edges (preprint)"
desc: |
  The preprint's main theorem: the edges of every graph on n vertices
  decompose into O(n) cycles and single edges; the deduction from Theorems
  1.3 and 1.4 followed here; unrefereed.
created: 2026-10-14T00:20:00Z
updated: 2026-10-14T00:25:00Z
---

***

## Statement

Graphs are finite and simple, and a decomposition of $G$ into cycles and edges
is a partition of $E(G)$ into the edge sets of cycles and single edges (Section
1.2). **Theorem 1.1.** There is an absolute constant $C$ such that the edges of
every graph on $n$ vertices decompose into at most $Cn$ cycles and edges. The
proof gives $C=14k$ for an integer $k$ fixed by Theorems 1.3 and 1.4 and not
made explicit. In the notation of the problem page, $f(n)=O(n)$.

The paper notes (p. 2) the Eulerian consequence: removing the cycles of such a
decomposition of an Eulerian graph leaves an Eulerian graph whose cycle
decomposition has no more cycles than single edges, so every Eulerian graph on
$n$ vertices decomposes into $O(n)$ cycles.

**Source.** Jaehoon Kim, *A proof of the Erdős–Gallai cycle decomposition
conjecture*, arXiv:2610.07840v2; Theorem 1.1 on p. 1, its proof in Section 2.1
(pp. 3--4). The edition is identified in the
[[extremal_graph_theory/kim_2026_proof_erdos_gallai_cycle_decomposition_conjecture/_index|source digest]].

**Read depth.** Claims checked: the statement and the deduction of Section 2.1
were read clause by clause and followed, including the potential inequality.
The two theorems it rests on are not checked here.

## Proof sketch

Fix $k\ge\max\{\delta_0,3,C_{1/1000}\}$ with $\delta_0$ from
[[extremal_graph_theory/kim_2026_proof_erdos_gallai_cycle_decomposition_conjecture/theorem_1_3|Theorem 1.3]]
and $C_{1/1000}$ from
[[extremal_graph_theory/kim_2026_proof_erdos_gallai_cycle_decomposition_conjecture/theorem_1_4|Theorem 1.4]].
Starting from $R=G$, repeat until $R$ has no edges. (a) If a vertex has degree
between $1$ and $k-1$, record its edges as single edges. (b) Otherwise, if the
graph $R'$ left after removing isolated vertices has a heavy cycle, record it.
(c) Otherwise $R'$ is light with minimum degree at least $k$; Theorem 1.3 gives
a near-closed set $S$, and Theorem 1.4 decomposes $R'[S]$ into at most $k|S|$
cycles and edges, which are recorded.

Step (a) isolates a vertex each time, so it records at most $kn$ edges. For
step (b), the potential $\Phi(R)=\sum_v\bigl(1-1/\sqrt{d_R(v)+1}\bigr)$ is below
$n$ at the start and never increases; removing a cycle lowers a degree $d$ on
it by two, which lowers its term by at least $d^{-3/2}$, so a heavy cycle with
$b^{3/2}$ vertices of degree at most $b$ lowers $\Phi$ by at least one, and step
(b) runs at most $n$ times. In step (c) at least $|S|/12$ vertices of $S$ are
left with degree at most two, so step (a) isolates them before the next step
(c); each vertex is counted in at most one step (c), the sizes $|S|$ sum to at
most $12n$, and step (c) records at most $12kn$ cycles and edges. The total is
at most $14kn$.

## Depends on

[[extremal_graph_theory/kim_2026_proof_erdos_gallai_cycle_decomposition_conjecture/theorem_1_3|Theorem 1.3]]
and
[[extremal_graph_theory/kim_2026_proof_erdos_gallai_cycle_decomposition_conjecture/theorem_1_4|Theorem 1.4]],
not checked here.

## Bears on

- [[../wiki/problems/extremal_graph_theory/E0184/_index|#184]]: the problem's
  statement, recorded as claimed on
  [[../wiki/problems/extremal_graph_theory/E0184/claims/2026_10_06_kim|the claim page]].
