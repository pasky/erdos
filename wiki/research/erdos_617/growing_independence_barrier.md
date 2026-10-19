---
name: research/erdos_617/growing_independence_barrier
desc: Critical cycle blowups combine the budget, local caps, two-support, and smaller capacities, but fail an explicit hereditary cap.
tags: [graph-theory, proved, obstructions]
sources: []
created: 2026-09-22T12:10:32Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/growing_independence_barrier

***

**Proved auxiliary counterexample, not a coloring counterexample.** Section 7.2
of the
[third independent input](independent/uniform_capacity_and_clique_packings.md)
supplies a useful barrier to discarding full hereditary caps. Its displayed
construction and calculations were reconstructed and checked by the author; the
input's separate proof files are not retained.

For any integer $a\ge2$, set

$$
r=16a^3,\qquad g=4a,\qquad t=4a^2+1,\qquad B=r-t-g.
$$

Let $H$ be the clique blowup of the cycle with cyclic bags

$$
L_0,Q_1,L_1,Q_2,\ldots,L_{a-1},Q_a,L_a,
$$

where the $Q_i$ have order $B$ and the $L_i$ have order $t$.
Consecutive bags, including $L_a,L_0$, are completely joined; there
are no other cross edges. Put $G=(r-a)K_r\sqcup H$.

Then $H$ satisfies all of the following simultaneously:

$$
|H|=ar+1,\quad \alpha(H)=a,\quad \omega(H)=r-g<r,
\quad\delta(H)=r+t-g-1>r;
$$


$$
|W|\le r\alpha(H[W])\quad(W\subsetneq V(H)),\qquad
2e(H)\le ar(r-1)+r(r+1).
$$

It is connected and independence-critical, has the local $(r+1)$-set
cap, and admits a two-supported maximum independent set with fewer
than $r$ exceptions. Nevertheless it violates full hereditary density.
Thus combining those weaker core properties does not by itself bound
the independence number of a minimal overloaded core.

## Order, criticality, and proper induced sets

The identity $t-ag=1$ gives $aB+(a+1)t=ar+1$. Independence in a
positive clique blowup equals independence in its support, so
$\alpha(H)=a$. We have $B>t$, $2t<r$, and the largest adjacent bag
sum is $B+t=r-g$. Heavy-bag vertices and the two end light bags have
degree $B+2t-1$; other light-bag vertices have degree $2B+t-1$.

Every edge is independence-critical. Deleting an intrabag edge permits
both endpoints together with one vertex from each member of an
independent $(a-1)$-set on the remaining $2a-2$-bag path. Deleting an
edge between consecutive bags permits its endpoints and an independent
$(a-1)$-set on the remaining $2a-3$-bag path. In both cases independence
increases from $a$ to $a+1$. The ordinary $K_r$ components of $G$ are
also independence-critical.

If a subset of $H$ omits a bag, its support is a disjoint union of
paths. Pair consecutive bags along each path, leaving at most one
singleton bag. This partitions that induced graph into
$\alpha(H[W])$ cliques, each of order at most $r$, proving the proper-set
bound. If every bag is met, independence is $a$ and properness gives
$|W|\le ar$ directly. In $G$, the overloaded induced sets are therefore
exactly the whole $H$ together with any selection of whole ordinary
$K_r$ components: an incomplete nonempty component costs at least one
unit of the sole possible excess. Every capacity statement at
independence less than $a$ holds.

## Exact local-cap check

An $(r+1)$-set meeting more than one component of $G$ has at least
$r$ cross-component nonedges. It suffices to treat sets within $H$.
For occupancies $x_i$ of its bags, the number of nonedges is

$$
Q(x)=\sum_{\{i,j\}\text{ nonadjacent cycle bags}}x_ix_j,
\qquad \sum_i x_i=m:=r+1.
$$

Keeping the sum fixed and moving mass between two coordinates strictly
between their bounds makes $Q$ affine or concave. A minimum is therefore
attained with at most one coordinate strictly between zero and its bag
capacity. Since $2B>m$, at most one heavy bag is full.

If a heavy bag is full, let $p,q$ be the occupancies in its neighboring
light bags, and let $z$ count all other chosen vertices outside it.
Then $p+q+z=t+g+1$ and

$$
Q\ge Bz+pq.
$$

For $0\le z\le g+1$, the bounds $p,q\le t$ give
$pq\ge t(g+1-z)$, hence $Q\ge t(g+1)+(B-t)z$.
For $z\ge g+1$, already $Bz\ge t(g+1)$.

If no heavy bag is full, the total light capacity $(a+1)t$ is less
than $m$. There is one partial heavy bag of occupancy

$$
x\ge m-(a+1)t=12a^3-4a^2-a>g+1,
$$

and all occupied light bags are full. There are at least two of them,
since $B+t<m$. If these are exactly the heavy bag's two neighbors,
their mutual nonedges contribute $t^2>t(g+1)$. Otherwise a full light
bag nonadjacent to that heavy bag contributes $xt>t(g+1)$.

Equality is attained with a full heavy bag, one adjacent light bag
full, and $g+1$ vertices of the other adjacent light bag. Thus

$$
\min Q=t(g+1)=(4a^2+1)(4a+1)>r,
$$

stronger than the $r-1$ nonedges required by the local cap.

## The edge budget and bounded two-support

Direct counting gives

$$
e(H)=a\binom B2+(a+1)\binom t2+2aBt+t^2.
$$

With $T=r\binom r2+r$, its surplus is

$$
e(G)-T=e(H)-a\binom r2-r
=(a-1)(64a^5-16a^4+8a^3-8a^2-1)
<64a^6=\frac{r^2}{4}<\binom r2.
$$

Consequently $G$ meets the minority budget and $H$ meets the displayed
least-core budget. These are one-graph statements, not compatible
color-class constructions.

Choose one anchor in each heavy bag. These anchors form a maximum
independent set. Its private cliques are

$$
P_1=Q_1\cup L_0,\qquad P_a=Q_a\cup L_a,\qquad
P_i=Q_i\quad(2\le i\le a-1).
$$

The exceptions are $L_1,\ldots,L_{a-1}$, each supported on exactly two
anchors. Their number and the row deficits satisfy

$$
b=(a-1)t<r,\qquad d_1=d_a=g,\quad d_i=t+g\ (2\le i\le a-1),
\qquad b=1+\sum_i d_i.
$$

All heavy anchors have minimum degree, and in fact
$a(r+t-g-1)<a(r-1)+r+1$. The example is therefore not a counterexample
to the desired light-independent-set conclusion; it already has such
a set. Its failure is elsewhere.

## An explicit hereditary-cap violation

Take a heavy bag and its two neighboring light bags. Their union has
$n=r+t-g$ vertices with $r<n<2r$, and exactly $t^2$ nonedges. The
inherited cap instead requires at least

$$
(r-1)p_r(n)=(r-1)(t-g)
$$

nonedges. This is strictly larger than $t^2$: for $a\ge2$,

$$
t<3a(2a-1),\qquad 9a^2<16a^3-1,
\qquad t-g=(2a-1)^2.
$$

Thus the failure occurs already on $r+O(r^{2/3})$ vertices, not only
on the entire core.

With full caps, all these cycle blowups are already excluded by the
budget-free span theorem in [Line-graph obstruction](line_graph_obstruction.md):
they are line graphs of multicycles. The
[subdivision-network theorem](clique_path_networks.md) also gives
$\chi_f(H)\le r$ for positive cycle blowups under full caps when $r\ge12$.
The archived provisional weighted-cycle idea is not needed to reject
this family. No inference about a surviving full-cap core or a
counterexample coloring follows from these auxiliary graphs.
