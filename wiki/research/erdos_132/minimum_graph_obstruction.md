---
name: research/erdos_132/minimum_graph_obstruction
title: A rich minimum-distance graph need not contain a large cycle
desc: |
  Strictly convex examples have n+1 minimum-distance edges but only two
  triangular cycles, invalidating a proposed large-cycle reduction.
sources: []
research_state: closed
created: 2026-09-22T22:45:00Z
updated: 2026-09-24T22:12:56Z
---


# A rich minimum-distance graph need not contain a large cycle

***

The later [deletion-criticality examples](deletion_criticality.md) give
nonstar-diameter versions, including one with a sublinear total distance
palette. They show why making a single rich class rare after every
deletion does not yield a contradiction either.

A proposed convex-set approach sought a near-spanning equilateral
cycle from richness of the minimum distance. The following explicit
family refutes that inference. It is not a counterexample to
[Problem 132](../../problems/distance_problems/E0132/_index.md).

Take $q\ge2$ and $0<\alpha<\pi/6$. Starting at
$C=(0,1/2)$, draw $q$ successive unit edges with directions

$$
\alpha,\ \alpha-\frac{2\alpha}{q-1},\ \ldots,\ -\alpha.
$$

Their vertical components sum to zero, so the final vertex is
$F=(L,1/2)$ for some $L\ge q\cos\alpha>1$.
Add the four points

$$
(0,-1/2),\quad(-\sqrt3/2,0),\quad
(L,-1/2),\quad(L+\sqrt3/2,0).
$$

These $n=q+5$ points are in strictly convex position. In clockwise
boundary order, the upper-chain edge directions strictly decrease
from $\alpha$ to $-\alpha$. At its ends the next directions are
$\pi/6$ and $-\pi/6$; the other boundary turns, through the two
outer tips and the lower horizontal side, are also strictly between
zero and $\pi$ in magnitude. Thus no point is collinear on a side
or lies in the hull of the others.

The minimum distance is one. Adjacent upper-chain vertices are a
unit apart. Nonadjacent ones have horizontal separation at least
$2\cos\alpha>1$. All chain vertices lie at height at least $1/2$:
the cumulative vertical displacement rises and then falls to zero.
Hence their distances to either lower point are greater than one
unless they form the respective vertical unit pair. Distances from
nonendpoint chain vertices to either outer tip exceed one by their
horizontal separation. The remaining nonlisted pairs between the
two end triples have horizontal separation at least $L>1$.

The left end triple and the right end triple are unit equilateral
triangles. Therefore the unit graph consists exactly of these two
triangles joined by the $q$-edge upper chain. It has

$$q+6=n+1$$

edges, but its only cycles are the two triangles.

This rules out the claimed large-cycle consequence of a rich
minimum-distance graph, even in strict convex position. It does
not rule out a stronger argument that also uses a bound on the
total number of distances. No such additional rigidity statement
was proved.
