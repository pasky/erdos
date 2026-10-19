---
name: research/erdos_617/transversal_equality
desc: Exact equality in the independent-transversal union bound, its clique-merging consequence, and the missing stability step.
tags: [graph-theory, proved, transversals]
sources: []
created: 2026-09-22T04:18:35Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/transversal_equality

***

**Proved, but not a solution of the remaining core problem.** This checks
Appendix E of the
[independent input](independent/small_independence_and_packing_obstructions.md)
and records its precise conditional consequence.

## Equality classification

Let $B_1,\ldots,B_k$ be disjoint nonempty parts, $k\ge2$, and let
$Q$ contain only edges between parts. Put $b_i=|B_i|$ and
$m_{ij}=e_Q(B_i,B_j)$. If $Q$ has no independent transversal, then

$$
w(Q):=\sum_{i<j}\frac{m_{ij}}{b_i b_j}\ge1.
$$

Indeed, the number $Z$ of edges in a uniformly random transversal
is always at least one and has expectation $w(Q)$.

Equality holds if and only if there is a central part $B_c$ and a
map $j:B_c\longrightarrow[k]\setminus\{c\}$ such that the entire
edge set consists, for each $x\in B_c$, of all edges from $x$ to
$B_{j(x)}$.

To prove necessity, equality implies that every transversal contains
exactly one edge, since every transversal has positive probability.
Thus two edges cannot occur together in a transversal. In the graph
on part indices recording which pairs support edges, any two edges
must intersect. Such a family of pairs is a star or is contained
in a triangle. If all three pairs $AB,BC,CA$ occur, then within
each part the vertices used toward the two other parts are disjoint:
otherwise two edges could occur together. Choose an $AB$-incident
vertex in $A$, a $BC$-incident vertex in $B$, and a $CA$-incident
vertex in $C$. They are pairwise nonadjacent. No further supported
pair can meet all three triangle pairs unless it belongs to the
triangle. Arbitrary choices in the other parts therefore give an
independent transversal, a contradiction.

Hence all supported pairs share a central index $c$. A fixed
$x\in B_c$ has neighbors in at most one other part, again because
two edges cannot occur together. It must have neighbors in some
part, and must be complete to that part: otherwise a transversal
through $x$ with a nonneighbor there has no edge. This proves the
description. Conversely the described graph gives exactly one
edge in every transversal, proving sufficiency.

For equal part sizes $b$, this classifies precisely the obstructions
with $b^2$ cross edges.

## Conditional clique merging

Suppose the $B_i$ are cliques of a graph $G$ and $Q$ records all
its cross edges. Under the equality hypothesis define
$A_j=\{x\in B_c:j(x)=j\}$. Then

$$
\{B_j\cup A_j:j\ne c\}
$$

partitions the union of the parts into $k-1$ cliques. In particular,
if $\omega(G)\le r$, then

$$
\sum_i b_i\le(k-1)r,
\qquad \sum_i(r-b_i)\ge r.
$$

If $k=r$ and every $b_i=r-1$, these are $r-1$ disjoint $K_r$'s.
This is an exact-equality conclusion, not a method to complete the
near-full cliques currently available.

That special configuration cannot occur in an actual counterexample
for $r\ge4$. Its union has $r(r-1)$ vertices, leaving $r+1$
vertices. The remaining set contains a target-nonadjacent pair
$x,y$, since $K_{r+1}$ is forbidden. Each has at most one
neighbor in every merged $K_r$. Thus each of the $r-1$ peripheral
parts $B_j$, $j\ne c$, retains at least $r-3\ge1$ vertices
avoiding both. These peripheral parts have no target cross edges;
their representatives together with $x,y$ give an independent
$(r+1)$-set.

## What equality does not establish

The global stability partition allows $O(r^2)$ cross edges and
substantial list-size variation after neighborhoods are removed.
Neither [large-clique clusters](large_clique_clusters.md) nor
[hereditary span](hereditary_span_bound.md) forces $w(Q)=1$ in
its surviving parameter range.

Even arbitrarily small positive slack does not give the exact
classification. On three parts of size $b$, take all edges between
$B_1,B_2$ and one further edge between $B_2,B_3$. There is no
independent transversal and $w(Q)=1+1/b^2$, but the graph is not
an equality system. This is only a transversal example, not a
coloring counterexample or a disproof of an approximate stability
theorem. No such stability theorem is proved here.

The matching-conflict theorem in [Packing tools](packing_tools.md)
has a different extremal regime. If all parts have size at least
two and every pair of parts is joined by a matching, an equality
system is impossible: its central vertex would have to dominate
a nonsingleton part. In the rigid system of $k$ parts of size
$k-1$, the normalized cross-edge count is $k/2$.

Finally, summing a separate conflict lower bound for every
exception is unjustified without controlling reuse of edges. If
many exceptions have the same available lists, one cross edge
appears in every one of their obstruction counts. The independent
input's failed additive charge is therefore a real limitation,
not a missing arithmetic estimate. The weighted inequalities in
[Two-supported private cliques](two_supported_private_cliques.md)
retain the exceptional-edge terms instead of discarding them.
