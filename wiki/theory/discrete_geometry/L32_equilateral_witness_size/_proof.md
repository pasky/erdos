---
name: theory/discrete_geometry/L32_equilateral_witness_size/_proof
title: Strip coloring and a limiting hypergraph
desc: Unit equilateral triangles can be avoided by strips; every bounded witness at nearby scales would limit to an avoidable fixed hypergraph.
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

Put $h=\sqrt3/2$ and color $(u,v)$ by $\lfloor v/h\rfloor$ modulo two.
A unit equilateral triangle has vertical span at least $h$: one of its
three unoriented edge directions is within $30$ degrees of vertical.
Its span is at most $1$. Hence a monochromatic triangle cannot lie in one
half-open strip and can meet at most two strips of its color. In the
latter case the lone vertex in one strip has vertical displacement
strictly greater than $h$ from each of the other two vertices, in the same
direction. The two unit vectors to those vertices make angle $60$ degrees,
so their sum has length $\sqrt3$. Its vertical component would exceed
$2h=\sqrt3$, a contradiction. The coloring avoids all unit equilateral
triangles, including boundary cases.

Suppose the statement of
[[theory/discrete_geometry/L32_equilateral_witness_size/_index|L32]]
fails for some $B$. There are then positive $x_j\to1$ and planar sets
of at most $B$ points whose hypergraphs of equilateral triples of lengths
$1$ or $x_j$ are not two-colorable. Some component of each hypergraph is
not two-colorable, since separate component colorings combine. Pass to
these components and a subsequence with fixed number of labeled vertices
and fixed abstract hyperedge set; there are only finitely many possibilities.

Translate one vertex to the origin. In a connected component, any vertex
can be reached by a path of at most $B-1$ pairs belonging to hyperedges.
Those pairs have length at most $2$ eventually. All coordinates are
therefore bounded, and a subsequence converges coordinatewise.
Every hyperedge limits to three distinct points forming a unit equilateral
triangle. Vertices outside a common hyperedge may coalesce; this does not
matter. Pull back the strip coloring of the limiting points to the labels.
It properly colors every hyperedge of the fixed abstract hypergraph,
contradicting its non-two-colorability.
