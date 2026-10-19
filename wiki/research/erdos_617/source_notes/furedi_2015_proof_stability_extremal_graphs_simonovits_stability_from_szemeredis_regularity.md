---
name: research/erdos_617/source_notes/furedi_2015_proof_stability_extremal_graphs_simonovits_stability_from_szemeredis_regularity
title: "A proof of the stability of extremal graphs, Simonovits' stability from Szemerédi's regularity"
desc: "Source notes for Problem 617: A proof of the stability of extremal graphs, Simonovits' stability from Szemerédi's regularity."
tags: []
sources: []
created: 2026-09-24T22:18:26Z
updated: 2026-10-13T04:56:43Z
---

# A proof of the stability of extremal graphs, Simonovits' stability from Szemerédi's regularity


[Full paper in Markdown](../../../../library/extremal_graph_theory/furedi_2015_proof_stability_extremal_graphs_simonovits_stability_from_szemeredis_regularity/_index.md).

***

Zoltán Füredi, "A proof of the stability of extremal graphs, Simonovits'
stability from Szemerédi's regularity," arXiv:1501.03129 (2015).

The
[Full paper in Markdown](../../../../library/extremal_graph_theory/furedi_2015_proof_stability_extremal_graphs_simonovits_stability_from_szemeredis_regularity/_index.md)
is the source used for this digest.

## Finite clique-stability bounds

Write $T_{n,p}$ for the balanced complete $p$-partite graph on $n$
vertices.

**Theorem 1** (p. 3) states that if $G$ is an $n$-vertex
$K_{p+1}$-free graph and

$$
e(G)=e(T_{n,p})-t,
$$

then $G$ has a spanning subgraph $H_0$ of chromatic number at most $p$
with $e(H_0)\geq e(G)-t$. Equivalently, at most $t$ edges need be deleted
to make $G$ $p$-partite. Its proof begins after equation (3) on p. 3 and
ends at the top of p. 4. The degree-majorization procedure successively
chooses a maximum-degree vertex in the remaining graph and makes its
nonneighborhood a part. The chosen vertices form a clique, so there are
at most $p$ parts; summing equation (4) shows that the total number of
edges internal to those parts is at most $t$.

**Corollary 2** (p. 3) states that if $G$ is $K_{p+1}$-free and
$e(G)\geq e(T_{n,p})-t$, there is a complete, not necessarily balanced,
$p$-partite graph $K$ on the same vertex set such that

$$
|E(G)\mathbin{\triangle}E(K)|\leq 3t.
$$

The complete proof is the paragraph immediately following the statement
on p. 3: delete at most $t$ edges using Theorem 1, then add at most $2t$
missing cross-edges. The same page records the separate estimate (3) for
moving from this possibly unbalanced $K$ to the balanced Turán graph.
These are finite bounds for every $n,p,t$; the regularity/removal-lemma
argument in Section 3 is needed only for the later general forbidden-graph
stability theorem.

## Reduction for Problem 617

Fix the parameter $r$ in
[Problem 617](../../../problems/extremal_graph_theory/E0617/_index.md), put $N=r^2+1$,
and suppose an $r$-edge-coloring of $K_N$ were a counterexample. Let $C_i$ be
the set of edges of color $i$ and let

$$
H_i=K_N-C_i=\bigcup_{j\ne i}C_j.
$$

Every $(r+1)$-set uses color $i$, so it cannot span a clique in $H_i$;
thus every $H_i$ is $K_{r+1}$-free. Define its Turán deficit by

$$
t_i=e(T_{N,r})-e(H_i)\geq0.
$$

Because each original edge belongs to exactly $r-1$ of the graphs $H_i$,
and because

$$
e(T_{r^2+1,r})=\frac{r(r-1)(r^2+2)}2,
$$

the deficits satisfy the exact budget

$$
\sum_{i=1}^r t_i
=r e(T_{N,r})-(r-1)\binom N2
=\frac{r^2(r-1)}2.
$$

Theorem 1 therefore supplies, across all colors, partitions for which at
most $r^2(r-1)/2$ non-$i$ edges in total lie inside the corresponding
parts. Corollary 2 strengthens the structural formulation: for each $i$
there is a complete $r$-partite graph $K_i$ with
$|E(H_i)\mathbin{\triangle}E(K_i)|\leq3t_i$, hence

$$
\sum_{i=1}^r |E(H_i)\mathbin{\triangle}E(K_i)|
\leq\frac{3r^2(r-1)}2.
$$

After complementation, the color-$i$ graph is within $3t_i$ edits of a
union of $r$ cliques. Thus a fixed-$r$ argument can reduce a hypothetical
counterexample to $r$ multipartite templates, a deficit vector of the
displayed fixed total, and bounded sets of exceptional edges. The global
coloring question is then concentrated in the finite residue and in the
compatibility of those templates.

This transfer does not solve the compatibility problem. The theorem
chooses the $r$ partitions independently, does not make them balanced or
mutually orthogonal, and its edit operations need not respect the other
colors. Its $O(r^3)$ total residue also grows with $r$, so it is not a
uniform finite verification of Problem 617. Any completion must use the
fact that the $C_i$ partition one common edge set to control the relative
positions of the parts and then eliminate the exceptional edges.
