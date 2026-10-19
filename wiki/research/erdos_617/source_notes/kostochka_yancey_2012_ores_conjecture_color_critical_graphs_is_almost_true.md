---
name: research/erdos_617/source_notes/kostochka_yancey_2012_ores_conjecture_color_critical_graphs_is_almost_true
title: "Ore's Conjecture on color-critical graphs is almost true"
desc: "Source notes for Problem 617: Ore's Conjecture on color-critical graphs is almost true."
tags: []
sources: []
created: 2026-09-24T22:18:26Z
updated: 2026-10-13T04:56:43Z
---

# Ore's Conjecture on color-critical graphs is almost true


[Full paper in Markdown](../../../../library/extremal_graph_theory/kostochka_yancey_2012_ores_conjecture_color_critical_graphs_is_almost_true/_index.md).

***

Alexandr Kostochka, Matthew Yancey, "Ore's Conjecture on color-critical graphs
is almost true," arXiv:1209.1050 (2012).

## Read status

**Claims checked.** The full paper in Markdown was read. The statement
of Theorem 3 and equation (9), the sharpness paragraph following them, and
Theorem 37 were checked against that copy; their proofs have not been
independently verified here.

## Critical-graph density theorem

The paper calls a graph $G$ $k$-critical when it is not
$(k-1)$-colorable but every proper subgraph is $(k-1)$-colorable. Its main
result is Theorem 3 in Section 1, with the equivalent extremal formulation in
equation (9): for $k\geq4$ and every $k$-critical graph $G$,

$$
|E(G)|\geq
\left\lceil
\frac{(k+1)(k-2)|V(G)|-k(k-3)}{2(k-1)}
\right\rceil.
$$

Thus, writing $f_k(n)$ for the least number of edges in an $n$-vertex
$k$-critical graph,

$$
f_k(n)\geq F(k,n):=
\left\lceil
\frac{(k+1)(k-2)n-k(k-3)}{2(k-1)}
\right\rceil
$$

for $n\geq k$, $n\neq k+1$. The excluded order is not an unresolved case:
there is no $k$-critical graph on $k+1$ vertices.

Section 5, Theorem 37, records exactness when $n\equiv1\pmod{k-1}$ and
$n\geq k$; for every $k=4$, $n\geq4$, $n\neq5$; and also for $k=5$,
$n\geq10$, $n\equiv2\pmod4$. The proof propagates a few base examples using
the Hajós recurrence (5). It proves existence at equality in these orders, not
a classification of all equality graphs. In particular, the bound is exact for
every admissible order when $k=4$ and for every order congruent to $1$ modulo
$k-1$ when $k\geq5$.

## Use as an E0617 obstruction

Fix $r\geq3$ and suppose an $r$-edge-coloring of $K_{r^2+1}$ were a
counterexample to [E0617](../../../problems/extremal_graph_theory/E0617/_index.md). For
each edge color $c$, let $G_c$ be the spanning graph formed by the edges of
color $c$. The counterexample condition says exactly that $\alpha(G_c)\leq r$
for every $c$: an independent set of $r+1$ vertices in $G_c$ is an induced
$K_{r+1}$ whose edges omit $c$.

Since $G_c$ has $r^2+1$ vertices, it cannot be properly $r$-colored: $r$
independent color classes, each of size at most $r$, cover at most $r^2$
vertices. Hence $\chi(G_c)\geq r+1$. Extracting an inclusion-minimal subgraph
$H_c\subseteq G_c$ that is not $r$-colorable gives an $(r+1)$-critical graph.
If $m_c=|V(H_c)|$, Theorem 3 forces

$$
|E(G_c)|\geq |E(H_c)|\geq F(r+1,m_c)
=\left\lceil
\frac{(r+2)(r-1)m_c-(r+1)(r-2)}{2r}
\right\rceil.
$$

This closes a residual fixed-$r$ configuration whenever its structural or
finite-case constraints leave fewer than $F(r+1,m)$ edges of some color on
every possible $m$-vertex critical support. Bounds for several colors may also
be summed because the color classes have disjoint edge sets, although their
critical supports need not have the same vertices. The unknown support orders
$m_c$ must therefore be retained or bounded in such an application.

This is an obstruction method, not a balanced-coloring theorem: the paper
controls the density of a proper-vertex-coloring obstruction extracted inside
one edge-color class. It neither constructs the desired $r+1$ vertices nor
proves that an edge coloring is balanced or split.
