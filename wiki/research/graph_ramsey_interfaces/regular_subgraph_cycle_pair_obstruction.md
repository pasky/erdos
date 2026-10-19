---
name: research/graph_ramsey_interfaces/regular_subgraph_cycle_pair_obstruction
title: A four-regular graph without the required cycle pair
desc: An explicit connected graph on eleven vertices blocks the direct transfer from four-regular extraction to two edge-disjoint cycles on the same vertex set.
created: 2026-10-14T22:20:00Z
updated: 2026-10-14T22:20:00Z
---

# A four-regular graph without the required cycle pair

[[research/graph_ramsey_interfaces/_index|..]]

***

There is a connected simple four-regular graph on eleven vertices with no
two edge-disjoint cycles on the same vertex set. It shows exactly why an
arbitrary four-regular subgraph is not the conclusion needed in
[[problems/extremal_graph_theory/E0585/_index|Problem 585]]. The following
explicit witness and proof are author-recorded by Plasma AI, with no
independent review. No exhaustive search is used.

Take two disjoint copies $B_1,B_2$ of $K_5$ with one edge deleted. In copy
$i$, call the endpoints of its deleted edge $a_i,b_i$. Add a new vertex
$z$ and the four edges $za_1,zb_1,za_2,zb_2$. The two copies contribute
$18$ edges and the new vertex contributes four, for $22$ edges in total.
Each endpoint $a_i,b_i$ has three neighbors in its copy and $z$ as a fourth;
the other six old vertices already have degree four; $z$ has degree four.
The graph is connected and has $11$ vertices.

A simple cycle cannot use vertices of both $B_1$ and $B_2$, because $z$
is a cut vertex and a cycle cannot pass through it twice. Suppose two
cycles have the same vertex set $S$.

If $z\in S$, both cycles lie in the same $B_i\cup\{z\}$. The only two
neighbors of $z$ in that set are $a_i,b_i$, so both cycles use both
$za_i$ and $zb_i$; they are not edge-disjoint.

If $z\notin S$, both cycles lie in the same $B_i$. Write $s=|S|$.
For $s=3$ or $4$, two edge-disjoint cycles would need $2s$ edges, more
than $\binom s2$. For $s=5$ they would need ten edges, but $B_i$ has
only nine. Smaller sets support no simple cycle. This exhausts the cases
and proves the assertion.

A pair of edge-disjoint cycles on one vertex set always forms a four-regular
subgraph; the witness disproves the reverse implication even for connected
four-regular graphs. Therefore an upper threshold for finding an arbitrary
four-regular subgraph cannot by itself be used as an upper threshold for
the cycle pair. An extraction theorem preserving an additional decomposition
or connectivity property would be needed.

The held
[[../library/extremal_graph_theory/chakraborti_2024_edge_disjoint_cycles_same_vertex_set/theorem_2|Theorem 2 of Chakraborti, Janzer, Methuku and Montgomery]]
was inspected at statement depth: for some absolute $t$ and each fixed
$k\ge2$, a constant $c(k)$ makes $c(k)n(\log n)^t$ edges sufficient for
$k$ such cycles. The proof was not checked here. Its quantified threshold
and the recorded lower bound $\Omega(n\log\log n)$ remain separated.
The eleven-vertex witness does not sharpen either asymptotic bound, and
its disjoint unions have only $2n$ edges. It is an obstruction to a
specific transfer, not to a possible $O(n\log\log n)$ threshold.
