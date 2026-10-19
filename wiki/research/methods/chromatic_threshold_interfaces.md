---
name: research/methods/chromatic_threshold_interfaces
title: Interfaces between chromatic thresholds
desc: Exact path, cochromatic and inverse-extremum reductions, with counterexamples to dropping parity, local cardinality, or anti-concentration hypotheses.
created: 2026-10-14T12:38:34Z
updated: 2026-10-14T12:38:34Z
---

***

The following author-recorded arguments identify what several proposed
graph-coloring reductions preserve. They neither assert that the remaining
thresholds exist nor upgrade the source standing recorded on the linked
problem pages.

## Odd cycles and paths spanning many colors

For [[problems/graph_coloring/E0640/_index|Problem 640]], let $p(k)$ be
the least finite threshold, when one exists, forcing a simple path whose
vertices induce a graph of chromatic number at least $k$. Write $f(k)$
for the analogous threshold for odd cycles; the cycle itself need not be
induced. For $k\ge1$, whenever $p(k+1)$ is finite,

$$
p(k)\le f(k)\le2p(k+1)-1.
$$

Opening an odd cycle to a path proves the first inequality. For the second,
take a connected graph of chromatic number at least $2p(k+1)-1$ and its
breadth-first levels. If each level used at most $p(k+1)-1$ colors, two
palettes for the even and odd levels would color the whole graph with
$2p(k+1)-2$ colors. Some level therefore contains a path $P$ whose
vertex span needs at least $k+1$ colors. If $P$ has even length, delete
one endpoint; this loses at most one color and leaves an odd-length path
$Q$. Otherwise take $Q=P$.

The breadth-first-tree paths from the endpoints of $Q$ to their lowest
common ancestor have equal positive length and disjoint interiors, all in
earlier levels. Their union with $Q$ is a simple odd cycle whose span
contains the at-least-$k$-chromatic span of $Q$. Fixed finite thresholds
for infinite graphs reduce to finite subgraphs by coloring compactness.
This does not prove $p(k)$ finite. At the first boundary $f(3)=3$;
$K_4$ shows $f(4)\ge5$, since all its odd cycles are triangles.

## Chromatic and cochromatic versions of an orientation threshold

In [[problems/graph_coloring/E0761/_index|Problem 761]], let $d(G)$ be
the maximum dichromatic number over orientations of the finite graph $G$,
and let $\zeta(G)$ be its cochromatic number, the minimum number of
parts that are each a clique or an independent set. The two qualitative
threshold questions are equivalent.

First, $\zeta(G)\le\chi(G)$, so an ordinary chromatic threshold
implies the cochromatic version with the entire graph as its subgraph.
Conversely, suppose for each $q$ there is $Z(q)$ such that
$\zeta(G)\ge Z(q)$ forces a subgraph with dichromatic number at least
$q$. Choose $R(q)$ with $d(K_{R(q)})\ge q$. Such a value exists by the
elementary random-tournament argument: the probability of a transitive
$t$-set in an $R$-vertex random tournament is at most
$R^t2^{-t(t-1)/2}$, which is below one for
$t=\lceil3\log_2R\rceil$ and sufficiently large $R$. An orientation
with no such set needs at least $R/(t-1)$ acyclic color classes, which
tends to infinity.

Now $\chi(G)\le\zeta(G)\omega(G)$, by coloring each cochromatic
part separately with at most $\omega(G)$ colors. If
$\chi(G)\ge R(q)Z(q)$, either $G$ contains $K_{R(q)}$, or
$\omega(G)<R(q)$ forces $\zeta(G)\ge Z(q)$. Both give
$d(G)\ge q$: an orientation of a subgraph extends to the whole graph,
and any acyclic coloring restricts. This equivalence preserves ordinary
dichromatic number; substituting a list or fractional invariant requires
an additional argument.

## Triangle-free extrema and their inverse

Let $F(n)$ be the maximum chromatic number of a triangle-free graph on
$n$ vertices and $h_3(k)$ the least order of a triangle-free graph of
chromatic number exactly $k$. The quantities in
[[problems/graph_coloring/E1013/_index|Problem 1013]] and
[[problems/graph_coloring/E1104/_index|Problem 1104]] obey

$$
h_3(k)=\min\{n:F(n)\ge k\}.
$$

Deleting a vertex drops chromatic number by at most one, so repeated
deletion reaches the exact value $k$; adding isolates pads the order.
Deleting from a minimum $(k+1)$-chromatic graph also proves
$h_3(k+1)>h_3(k)$.

[[../library/graph_coloring/davies_2022_ramsey_problem_triangle_free_graphs/theorem_1|Davies–Illingworth Theorem 1]]
gives the ordinary chromatic upper bound. The preprint
[[../library/ramsey_theory/hefty_2025_improving_just_two_bites/theorem_1_3|Hefty–Horn–King–Pfender Theorem 1.3]]
gives the stronger lower input via $\chi(G)\alpha(G)\ge n$.
Using those source-dependent bounds,
$(1-o(1))\sqrt{n/\log n}\le F(n)\le
(2+o(1))\sqrt{n/\log n}$, inversion at $n=A k^2\log k$ gives

$$
(1/2-o(1))k^2\log k\le h_3(k)\le(2+o(1))k^2\log k.
$$

The factor two comes from $\log n\sim2\log k$, with natural
logarithms. The stronger lower input for $F$ is an unreviewed preprint;
this calculation does not change that qualification or reconstruct either
source proof. The result accounts were read at statement depth.

Even strict monotonicity and order $\Theta(k^2\log k)$ do not imply
the consecutive-ratio limit. The integer sequence

$$
u(k)=k+\left\lceil4^{\lfloor\log_2 k\rfloor}\log(k+1)\right\rceil
$$

has both properties, but $u(k+1)/u(k)\to4$ along $k=2^j-1$.
This is a logical countermodel, not a graph-realizable extremum. The
Mycielski upper bound $h_3(k+1)\le2h_3(k)+1$ has multiplicative slack
too; an operation adding only $o(h_3(k))$ vertices would resolve that
particular gap.

For [[problems/graph_coloring/E0626/_index|Problem 626]], the extremum of
chromatic number at girth greater than three is exactly $F(n)$.
The order of growth already follows from
[[../library/ramsey_theory/kim_1995_ramsey_number_has_order_magnitude/theorem_1_1|Kim's published construction]]
and the upper bound, without the stronger preprint constant. It gives
logarithmic exponent $1/2$ for that subcase, not a limit for every other
girth cutoff.

For girth cutoffs $m\le2$, complete graphs give logarithmic exponent one
under the simple-graph convention. In the fixed-$k$ question, a
vertex-critical $k$-chromatic subgraph has minimum degree at least $k-1$.
Its breadth-first tree below half the girth branches by at least $k-2$,
giving $g_k(n)\le2\log_{k-2}n+O_k(1)$. A lower bound with a different
constant does not force a limit. Independent blow-ups of an edge with two
clones at both ends contain a 4-cycle, as does the Cartesian product of
two graphs each having an edge. These operations therefore do not supply
a general girth-preserving composition.

## Deletion and extraction boundaries

In the $a=2$ case of
[[problems/graph_coloring/E0628/_index|Problem 628]], with
$\chi(G)=k>\omega(G)$ and $a+b=k+1$, the desired partition exists
exactly when some edge $uv$ satisfies
$\chi(G-\{u,v\})\ge k-1$. One direction takes the edge as the first
part; the other selects any edge from that part. Thus failure says
$\chi(G-\{u,v\})=k-2$ for every edge, because deleting two vertices
lowers chromatic number by at most two. This is the double-critical
condition. Deleting an edge, instead of its endpoints, is a different
operation.

The $\aleph_0$ extraction in
[[problems/graph_coloring/E0739/_index|Problem 739]] also has an elementary
proof. In an uncountably chromatic graph, deleting finitely many vertices
leaves it uncountably chromatic. Recursively choose disjoint finite
subgraphs of chromatic number at least $j$ for each integer $j$, using
finite coloring compactness. Their disjoint union, keeping only their
internal edges, is a subgraph of chromatic number exactly $\aleph_0$.
This argument supplies no arbitrary uncountable intermediate chromatic
cardinal and does not claim the subgraph is induced.

For [[problems/graph_coloring/E0918/_index|Problem 918]], disjoint unions
of finite-stage incompactness graphs fail the local condition at the limit:
a component already uncountably chromatic and smaller than
$\aleph_\omega$ fits inside an $\aleph_\omega$-sized vertex set of
the proposed larger graph. That vertex set is not countably colorable.
Padding by isolates preserves the failure. This excludes that limit
construction, not all graphs with the requested local condition.

## Finite distance palettes

For [[problems/graph_coloring/E0706/_index|Problem 706]], a single positive
forbidden planar distance $d$ has a 16-coloring: tile by half-open squares
of side $d/2$, and color the two integer tile coordinates modulo four.
A tile's diameter is less than $d$, and distinct same-colored tiles are
separated in some coordinate by at least $3d/2$. The product of these
colorings for $r$ forbidden distances uses $16^r$ colors, uniformly in
the distances and point set. The collinear points $0,1,\ldots,r$ with
forbidden distances $1,\ldots,r$ need $r+1$ colors. These elementary
bounds do not establish the requested polynomial upper bound. A bound
depending on the ratio of largest to smallest distance is not uniform in
$r$: even two distances can have an arbitrarily large ratio.

## Interval width and concentration on a few values

For [[problems/graph_coloring/E1156/_index|Problem 1156]], an interval
anti-concentration theorem does not automatically bound the mass of an
arbitrary set of a fixed number of values. Let an integer random variable
$X_n$ give equal mass to $a_n$ and $a_n+D_n$, where
$D_n=\lfloor\sqrt n/(\log n)^2\rfloor$. Any deterministic interval
whose mass tends to one must eventually contain both atoms, so its width
is at least $D_n>n^c$ for each fixed $c<1/2$. Yet all mass lies on
two values, and a window of radius below $D_n/2$ around either atom has
mass exactly $1/2$, not strictly less. This is a counterexample to that
logical inference, not a distribution asserted for the chromatic number
of a random graph. Making the variable degenerate on odd $n$ separately
shows why an infinitely-often interval theorem does not give an
every-large-$n$ assertion.

The next useful bound must control arbitrary fixed-size sets of values,
or give the required strict probability at every sufficiently large order.

## Local obstructions to common amplification arguments

The finite remainder in [[problems/graph_coloring/E0019/_index|Problem 19]]
cannot be removed just by padding the dual linear hypergraph to a larger
vertex count $N$: its large-order theorem then allows $N$ colors, not the
original $n$. Disjoint unions take the maximum chromatic index, and
duplicating an edge of size at least two destroys linearity. None of these
three operations preserves the required ratio for an exact $n$-coloring.
This leaves the source's effective-cutoff or amplification gap in place.

For [[problems/extremal_graph_theory/E0062/_index|Problem 62]], knowing
that the two graphs contain all sufficiently long odd cycles gives a common
3-chromatic graph. Adding disjoint bipartite components still gives
chromatic number at most three. Separately obtaining high-chromatic finite
subgraphs in each host does not identify an isomorphic one in both. A
common 4-chromatic configuration needs an additional argument.

For [[problems/graph_coloring/E0627/_index|Problem 627]], the join of $t$
identical graphs multiplies both chromatic and clique numbers by $t$,
so their ratio stays fixed while the vertex count grows. An independent
blow-up preserves both invariants. Neither yields multiplicative growth at
the requested scale $n/(\log_2 n)^2$. A clique blow-up has multicoloring
number, which cannot be replaced by $t\chi(G)$ without proof. These facts
do not remove either conjectural premise of the conditional source result
recorded on the problem page.

The tree in [[problems/graph_coloring/E0738/_index|Problem 738]] must be
finite for the usual finite-graph formulation. For connected finite $T$,
the infinite-chromatic assertion is equivalent to a finite bound on the
chromatic numbers of finite triangle-free induced-$T$-free graphs:
coloring compactness proves one direction, and a disjoint union of
finite counterexamples of unbounded chromatic number proves the other.
If $T$ were allowed infinite, that same union contains no infinite
connected tree and gives a different problem. An induced subdivision
also does not suffice. Subdivide the central edge of the double star with
two adjacent degree-three vertices; the only two degree-three vertices
of the result are nonadjacent, so it has no copy of the original tree
even as a subgraph.

For [[problems/extremal_graph_theory/E1111/_index|Problem 1111]], a
minimum-degree guarantee cannot be changed to a chromatic guarantee even
with clique number bounded by two: $K_{d,d}$ has minimum degree $d$
and chromatic number two. Its disjoint union with a high-chromatic
triangle-free graph has the global chromatic premise and an anticomplete
pair of the weaker kind, while this chosen first side still needs only
two colors. A different successful pair may exist; this is an obstruction
to upgrading the chosen pair, not a counterexample to the target.
Likewise, excluding $K_t$ does not exclude $K_{t,t}$.
