---
name: research/erdos_132/diameter_activity
title: Supporting disks and activity below the diameter
desc: |
  Rich fixed-long-rank cores have linear cycle surplus under bounded
  rarity; supporting disks and active-circle bounds constrain their supports.
sources: []
research_state: closed
created: 2026-09-23T02:33:01Z
updated: 2026-09-24T22:12:56Z
---


# Supporting disks and activity below the diameter

***

The later [long-rank gap theorem](long_rank_gaps.md) uses the linear
core surplus proved here to obtain adjacent gaps $O_{K,k}(\Delta/n^2)$
at rich fixed ranks, and growing odd girth for fixed top-rank unions.
These are further necessary conditions, not an unrestricted conclusion.

All counts are unordered. For an occurring distance $r$, let

$$S=\{x\in A:\text{some }y\in A\text{ has }|x-y|>r\},
\qquad T=A\setminus S.$$

Write $H=G_r(A)$, $s=|S|$, and $h=e(H[S])$. The key point is
that every radius-$r$ disk centered at a point of $T$ contains
all of $A$.

## Exposed points and circular leaves

Every $r$-active point of $T$ is exposed in $\operatorname{conv}T$:
if $|x-y|=r$, the disk centered at $y$ contains $T$ and its tangent
at $x$ supports $T$ uniquely. If $x$ has an $r$-neighbor in $T$,
the same disk contains all of $A$, so $x$ is exposed in
$\operatorname{conv}A$.

For any $y\in A$, its $r$-neighbors in $T$ occupy an arc of
angle at most $\pi/3$. Indeed, their mutual distances are at
most $r$; the angular localization argument in
[star_diameter](star_diameter.md) applies after scaling.
Every neighbor strictly between the two extremes has global
$r$-degree one. The unit-circle arc lemma applies because each
extreme belongs to $T$, and hence is within $r$ of every point
of $A$. Thus each $y\in S$ has at most two nonleaf neighbors in
$T$.

Partition $T$ into $C,F,P,Z$: $C$ consists of points incident
with an $r$-edge inside $T$; $F$ consists of global degree-one
points whose neighbor is in $S$; $P$ consists of points with no
neighbor in $T$ and global degree at least two; and $Z$ consists
of isolated points. The preceding argument gives

$$e_H(S,T)\le |F|+2s.$$

The graph on $C$ is a diameter graph, so $e(H[T])\le |C|$.
Consequently the following elementary bound needs no stronger
description of that graph:

$$m_A(r)\le n+h+s-|P|-|Z|. \tag{1}$$

In particular, richness implies $|P|+|Z|\le h+s-1$, while
$T\setminus Z$ is strictly convex. At the second-largest distance,
$S$ is the set of diameter-active vertices. Its points lie on a
constant-width boundary, so the [boundary theorem](constant_width.md)
gives $h\le s$. Thus a rich second distance supplies a convex
subset of size at least $n-3s+1$.

## The sharper inactivity estimate

Let $D$ be the diameter, $d=m_A(D)$, and let $r$ be the
second-largest distance. Vesztergombi's theorem states

$$m_A(r)\le n+2d. \tag{2}$$

This was checked on p. 380 of the
[full 1996 paper](https://www.researchgate.net/publication/220193784_The_two_largest_distances_in_finite_planar_sets).

Suppose $m_A(r)>n$, and delete all $z$ points isolated in $G_r(A)$.
The retained set must still contain a diameter pair: otherwise
its $r$-graph would be a diameter graph with more edges than
vertices. Applying (2) to the retained set, whose second-largest
distance is still $r$, gives

$$n+1\le m_A(r)\le n-z+2d,$$

so $z\le2d-1$. Deleting the diameter-active vertices as well
leaves a strictly convex subset of size at least

$$n-|S|-2d+1\ge n-4d+1. \tag{3}$$

Thus bounded diameter multiplicity and a rich second distance
force all but a bounded number of points into convex position.

## Scope and the unresolved step

These disk and counting arguments were checked by the author and are
author-recorded. The source inequality is used as stated;
no stronger inequality such as $m_A(r)\le n+d$ is assumed.
That proposed strengthening is false: Vesztergombi's even-ring
construction has $d=n/4$ and $m_A(r)=3n/2$.

Neither (1) nor (3) supplies a constant-width boundary or bounded
individual rank omissions for the resulting convex subset.
Under bounded rarity, (3) only gives a convex core with
$q\le |C|/2+O(d+R(A))$. The required arbitrary-convex inverse
at bounded additive excess remains unproved. No induction on
diameter multiplicity or unrestricted asymptotic conclusion follows.

## A circle bound for the active support of a long distance

Let $k\ge1$ be an integer and $r>0$. Suppose at most $k-1$ distinct distances
exceed $r$, and let $X=\{q\in A:\deg_{G_r(A)}q>0\}$. Every circle of radius
$R>r$, with arbitrary center, contains at most $4k-2$ points of $X$.

To prove this, apply the [balanced-circle lemma](layers_and_obstructions.md)
to its $N\ge2$ points of $X$, selecting $q$, and choose an $r$-neighbor
$w$ of $q$. The center $o$ of the chosen circle differs from $w$, since
$R>r$. Writing $\rho=|o-w|$, its intersection with the closed
radius-$r$ disk about $w$ satisfies

$$\cos\theta\ge\frac{R^2+\rho^2-r^2}{2R\rho}>0.$$

This is an arc shorter than a semicircle, or a singleton, with endpoint
$q$. One semicircle from $q$, excluding $q$, is strictly outside the
disk and contains at least $\lfloor(N-1)/2\rfloor$ selected points.
Their distances to $w$ have at most $k-1$ possible values, each with
at most two circle intersections. Thus $N\le4k-2$.
The cases $N\le1$ are immediate.

In particular, every larger-distance graph induced on $X$ has maximum
degree at most $4k-2$. Unlike the original core lemma, this assertion
requires no vertex peeling.

## Linear surplus in a rich fixed-long-rank core

Suppose $R(A)\le K$ along an unbounded sequence. Choose a rich
smallest-distance rank $s\le K+1$, and let $r_k$ be any rich fixed
largest-distance rank. Such a $k$ is necessarily at least two.
The finitely many possible choices of $s$ allow all asymptotic estimates
below to be uniform, or one may pass to a subsequence with $s$ fixed.

Write $B_k=L_1\cup\cdots\cup L_k$. The short-edge inverse gives
only $o(n)$ edges of the chosen short class touching $B_k$.
Its degree bound $6s$ therefore implies

$$n-|B_k|\ge n/(3s)-o(n).$$

The $r_k$-graph is supported on $B_k$. If its 2-core $H$ has $v$
vertices, peeling removes at most $|B_k|-v$ edges. Consequently

$$e(H)-v\ge m_A(r_k)-|B_k|\ge n/(3s)-o(n). \tag{4}$$

The [2-core bound](layers_and_obstructions.md) gives
$\Delta(H)\le4k-2$. Since
$\sum_{x\in H}(\deg_Hx-2)=2(e(H)-v)$, at least
$n/[6s(k-1)]-o(n)$ core vertices have degree at least three.

There is also a linear matching of pairs longer than $r_k$ inside
this core. Let $J$ be the graph of those longer pairs, and let $\mu$
be its maximum matching size. The $2\mu$ endpoints $U$ of a maximum
matching cover $J$. Thus the remaining points have diameter at most
$r_k$, so $e(H-U)\le v-|U|$. At most $(4k-2)|U|$ edges of $H$
touch $U$, yielding

$$e(H)\le v+2(4k-3)\mu,\qquad
\mu\ge n/[6s(4k-3)]-o(n).$$

If $k$ is the first rich largest rank, all the $k-1$ larger classes
are rare, and at least one contains a linear matching. These conclusions
use the coexistence of a rich short class with a rich long class, not
just the long class's core-degree bound.

For a rich second-largest distance, the checked bound
$m_A(r_2)\le |B_2|+2m_A(\Delta)$, obtained by applying (2) on $B_2$,
also gives $m_A(\Delta)\ge n/(6s)-o(n)$. In particular, a hypothetical
unbounded $R=1$ family has at least $(1/6-o(1))n$ diameter pairs,
since its minimum distance is rich and one may use $s=1$.

The author checked the active-circle geometry, peeling deficit, matching
deletion, and unordered-pair factors; the argument is author-recorded.
Linear branching and a linear
diameter matching do not imply circular concentration: the
[even-order extremal deformations](second_distance_extremality.md)
already exhibit those features without five concyclic points. No new
connection to the interior short-distance palette follows from (4).
