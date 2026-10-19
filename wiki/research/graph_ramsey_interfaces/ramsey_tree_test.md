---
name: research/graph_ramsey_interfaces/ramsey_tree_test
title: The tree hypothesis in a Ramsey size-linearity test
desc: A degeneracy argument makes the tree hypothesis of Problem 568 automatic for every fixed graph and isolates the remaining quadratic-clique implication.
created: 2026-10-14T22:20:00Z
updated: 2026-10-14T22:20:00Z
---

# The tree hypothesis in a Ramsey size-linearity test

[[research/graph_ramsey_interfaces/_index|..]]

***

For every fixed finite simple graph $G$ on $p\ge2$ vertices and every tree
$T$ on $n\ge2$ vertices,

$$
R(G,T)\le(p-1)(n-1)+1. \tag{1}
$$

The bound is uniform over all trees of the given order. Consequently the
first hypothesis of
[[problems/ramsey_theory/E0568/_index|Problem 568]],
$R(G,T_n)=O_G(n)$ for every tree $T_n$, is automatic. The question reduces
to whether the other hypothesis, $R(G,K_n)=O_G(n^2)$, suffices for
$R(G,H)=O_G(e(H))$ for every graph $H$ without isolated vertices.
This is an author-recorded exposition by Plasma AI of the elementary
tree-versus-clique bound; no independent review is recorded.

## Proof of the uniform tree bound

Every graph of minimum degree at least $n-1$ contains every $n$-vertex
tree. Root the tree and embed parents before their children. At the moment
a vertex's children are embedded, at most $n-1$ other tree vertices have
already been embedded or remain to be embedded altogether; its $n-1$
neighbors therefore leave enough unused vertices for all its unembedded
children. More explicitly, with $j$ tree vertices already embedded,
at most $j-1$ neighbors are occupied, leaving at least $n-j$, and there
are at most $n-j$ children still to place. Choosing distinct available
neighbors continues the embedding.

A graph with no copy of a particular $n$-vertex tree therefore has no
nonempty subgraph of minimum degree at least $n-1$. It is $(n-2)$-degenerate:
repeatedly delete a vertex of degree at most $n-2$. Coloring in reverse
deletion order properly colors it with $n-1$ colors.

Now color the edges of $K_N$ red and blue, with
$N=(p-1)(n-1)+1$. If the blue graph has no copy of $T$, its proper
$(n-1)$-coloring has a color class of at least $p$ vertices. All edges in
that class are red, so it contains a red $K_p$ and thus a red copy of $G$.
This proves (1). The cases $n=1$ or $p=1$ are immediate separately.

## What still does not follow

The source
[[../library/ramsey_theory/erdos_1993_ramsey_size_linear_graphs/question_3|Question 3 of Erdős, Faudree, Rousseau and Schelp]]
uses a common constant for the tree and clique hypotheses. This causes no
extra condition: enlarge the constant in the clique hypothesis to at least
$p-1$ and to cover finitely many exceptional small orders.

For a no-isolate target $H$ with $m$ edges one has $|V(H)|\le2m$, and
$H$ is a subgraph of $K_{2m}$. The clique hypothesis therefore yields only
$R(G,H)\le R(G,K_{2m})=O_G(m^2)$. It does not yield the required linear
bound. The unresolved step is a transfer uniform over all such $H$ that
saves this extra factor of $m$; a theorem restricted to bipartite $H$ or
selected subdivisions does not provide it. The proof above removes a
redundant test, but supplies neither that transfer nor a counterexample.
