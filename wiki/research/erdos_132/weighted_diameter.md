---
name: research/erdos_132/weighted_diameter
title: Sharp weighted diameter bounds do not enforce joint realizability
desc: |
  The exact vertex-weight bound already holds for pseudoforests; every
  linear forest is a planar diameter graph, strengthening the hereditary obstruction.
sources: []
research_state: closed
created: 2026-09-23T01:43:51Z
updated: 2026-09-24T22:12:56Z
---


# Sharp weighted diameter bounds do not enforce joint realizability

***

This checks a proposed fractional-weight or minimax extension of the
hereditary diameter approach. It does not resolve
[Problem 132](../../problems/distance_problems/E0132/_index.md).

## The sharp quadratic weight bound

For nonnegative vertex weights $w_1\ge\cdots\ge w_n$, $n\ge3$,
every planar diameter graph $G$ satisfies

$$\sum_{ij\in E(G)}w_iw_j
\le w_1\sum_{i=2}^n w_i+w_2w_3. \tag{1}$$

In fact (1) holds for every simple pseudoforest. First connect
components without decreasing the edge weight sum. A tree component
not containing vertex 1 can be joined to vertex 1. For a unicyclic
component not containing 1, remove one cycle edge $uv$ and insert
$1v$. The component becomes a tree attached to the component of 1,
and the weight changes by $w_v(w_1-w_u)\ge0$.
After all components are joined, the graph is a tree or is unicyclic.
In the tree case add any absent edge, possible since $n\ge3$.

Now suppose $v$ is not adjacent to 1. On a simple path from 1 to
$v$, let $uv$ be the last edge. Replace it by $1v$. If $uv$ is
a bridge, the new edge reconnects the two pieces; otherwise the
graph stays connected after its removal. Thus the new graph is
again connected and unicyclic. Its weight does not decrease, and
the number of edges incident with 1 increases. Repetition ends
with the full star at 1 and one further edge. That edge has weight
at most $w_2w_3$, proving (1).

A planar diameter graph is a pseudoforest because its restriction
to any vertex subset has at most as many edges as vertices, by
the diameter theorem. Thus the inequality applies to it.

The bound is attained geometrically for every weight vector. Take
a unit equilateral triangle with labels 1,2,3, and put all remaining
points on the open radius-one arc centered at 1 from 2 to 3.
Every point is at distance one from 1. Among the points on the
arc, only its two endpoints are at distance one from each other.
The diameter graph is exactly the star at 1 together with edge 23.

Therefore even the sharp universal quadratic inequality in arbitrary
nonnegative vertex weights supplies no information beyond the
pseudoforest restriction. In particular it holds on every induced
highest-color graph in the abstract one-rare-color construction in
[layers_and_obstructions](layers_and_obstructions.md).

## Every linear forest is a planar diameter graph

There is a stronger obstruction to reasoning about those graphs
one at a time. Every nonempty linear forest $F$ on $n$ labeled
vertices is the exact diameter graph of some planar configuration.

If $F$ has $k$ components, including isolated vertices, choose an
odd integer $N\ge n+k$. The diameter graph of a regular $N$-gon
is an $N$-cycle: its longest chords advance $(N-1)/2$ vertices,
a step coprime to $N$. In that cycle order, select disjoint runs
whose lengths are the component sizes of $F$, with at least one
unselected vertex between successive runs, including the last
and first. The selected induced graph is $F$. Because $F$ has an
edge, the original diameter survives, so this is exactly the
diameter graph of the selected planar points.

The existing abstract ordered coloring has a linear forest as every
nontrivial induced highest-color graph. Hence each such graph is
individually realizable as a planar diameter graph. This does not
realize the whole coloring: the realizations can differ from subset
to subset, and the earlier five-point argument proves that they
cannot be made compatible.

This rules out an approach that imposes only universal properties
of each individual induced diameter graph, even if those properties
are stronger than its edge bound or involve arbitrary vertex weights.
It does not rule out conditions coupling the different subsets in
one planar realization. No suitable joint condition was established.

The author checked the graph transformations, the weighted extremizer,
and the regular-polygon embedding; the argument is author-recorded. No
computation or
additional geometric classification is used.
