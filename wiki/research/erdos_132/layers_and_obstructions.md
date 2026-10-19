---
name: research/erdos_132/layers_and_obstructions
title: Convex-layer reduction and obstructions to unrestricted arguments
desc: |
  A balanced-circle 2-core argument gives the rank bound (2k-1)|B_k|;
  the short-edge inverse also proves divergence for linear aspect ratios.
sources: []
research_state: closed
created: 2026-09-22T21:24:00Z
updated: 2026-10-14T00:26:52Z
---


# Convex-layer reduction and obstructions to unrestricted arguments

***

All statements here concern unordered-pair multiplicities. These reductions
do not resolve [Problem 132](../../problems/distance_problems/E0132/_index.md).

## Rank versus layer depth

Let $L_i$ be the successive sets of convex-hull vertices, including the
usual one-point or two-point degenerate final hulls. Put
$B_k=L_1\cup\cdots\cup L_k$, and write $d(x)$ for layer depth.
If $|x-y|=r_k$, the $k$-th largest distinct distance, then

$$d(x)+d(y)\le k+1. \tag{1}$$

Indeed, a point of $L_i$, $i>1$, is a nontrivial convex combination of
vertices of $L_{i-1}$. Strict convexity of $z\mapsto |z-y|^2$ supplies
a vertex of the preceding layer strictly farther from $y$. Move $x$
outward repeatedly, then $y$ outward relative to the final $x$. This
produces $d(x)+d(y)-2$ distinct larger distances. The argument also
applies to collinear boundary points, since the convex combination is
still nontrivial.

Thus every top-$k$ edge has both endpoints in $B_k$. Every top-$2h$
edge has at least one endpoint in $B_h$.

## A rank bound using only the diameter theorem

For every occurring rank $k$,

$$m_A(r_k)\le4^{k-1}|A|. \tag{2}$$

For $k=1$ this is the planar diameter bound. The diameter graph is a
pseudoforest: each connected component, on its own vertex set, has
at most as many edges as vertices, again by that bound. Orient it
with outdegree at most one. Give every vertex an independent fair bit;
retain it if its own bit is $1$ and its out-neighbor's bit is $0$.
For a vertex with no out-neighbor, use a private independent fair
dummy blocker. Each vertex survives with probability $1/4$.

No diameter edge survives. For a nondiametral pair $u,v$, its two
required positive bits are distinct from both required blocker bits.
The blockers may coincide, but that only increases survival probability.
Therefore this pair survives with probability at least $1/16$.

In a retained set $S$, an original $r_k$ class, if present, has rank
at most $k-1$. Strong induction gives at most $4^{k-2}|S|$ surviving pairs.
Taking expectations gives

$$m_A(r_k)/16\le4^{k-2}|A|/4,$$

which proves (2). Applying it to $B_k$, which preserves every top-$k$
class and its full multiplicity by (1), gives

$$m_A(r_k)\le4^{k-1}|B_k|. \tag{3}$$

Consequently, if every fixed convex layer of a sequence $A_n$ has
$o(n)$ points, then $R(A_n)\to\infty$. For fixed $k$, eventually
$4^{k-1}|B_k|\le n$, so all its top $k$ distances are rare. These
ranks exist eventually: if $D$ is the total number of distances,
two fixed anchor points locate each other point among at most two
intersections of each of $D^2$ pairs of circles, giving
$n\le2D^2+2$.

Conversely, if $R(A)\le K$ and $D\ge K+1$, then

$$|B_{K+1}|>n/4^K.$$

Thus any hypothetical bounded-$R$ sequence must concentrate a positive
fraction of its points in one of finitely many outer layers. This
leaves large arbitrary convex layers untreated, rather than reducing
the problem to sparse layers.

## A stronger geometric rank bound

The angular argument in the
[independent input](independent/largest_distance_ranks_and_small_orders.md) was
checked by the author and is author-recorded. It gives the following
improvement, without any incidence theorem.

**Lemma.** If at most $k-1$ distinct distances in a planar set $B$ exceed
$r>0$, the distance-$r$ graph is $2k$-degenerate. Thus

$$m_B(r)\le2k|B|. \tag{5}$$

For every nonempty $T\subseteq B$, choose a leftmost point $p$ and put it
at the origin. If its distance-$r$ degree is at most $2k$, it is a
low-degree vertex. Otherwise order its $t\ge2k+1$ neighbors as

$$q_j=r(\cos\theta_j,\sin\theta_j),\qquad
-\pi/2\le\theta_1<\cdots<\theta_t\le\pi/2.$$

Choose $q_i$ with at least $k$ neighbors on each angular side. It has
no distance-$r$ neighbor in $T$ other than $p$. Indeed, write any such
other neighbor as $x=\rho(\cos\phi,\sin\phi)$, where $\rho>0$ and
$-\pi/2\le\phi\le\pi/2$. Then

$$\cos(\theta_i-\phi)=\rho/(2r)>0.$$

If $\theta_i\ge\phi$, take $k$ indices above $i$. The distinct angles
$\theta_j-\phi$ belong to $(\theta_i-\phi,\pi]$, so strict decrease
of cosine on $[0,\pi]$ makes the lengths $|x-q_j|$ distinct and greater
than $r$. If $\theta_i\le\phi$, use the $k$ indices below $i$ instead.
Both cases contradict the rank hypothesis. Thus $q_i$ has degree one.
Every induced subgraph has a vertex of degree at most $2k$, proving
the degeneracy statement and (5) by successive vertex deletion.
The closed angular interval handles ties in the leftmost coordinate.

### A sharper edge count from the 2-core

The
[second independent input](independent/large_distance_graph_and_convex_extension.md),
Sections 2--3, supplies a stronger edge count. Its geometric argument was
checked separately from the earlier degeneracy proof.

**Balanced-circle lemma.** Among $N\ge2$ distinct points on a circle,
some point $q$ has at least $\lfloor(N-1)/2\rfloor$ other points in
each closed semicircle from $q$ to its antipode. An antipodal point
counts in both semicircles; $q$ itself is excluded.

First suppose there are no antipodal pairs. In cyclic order let $c_i$
count the points strictly clockwise between $q_i$ and its antipode.
Every unordered pair contributes once, so the average of the $c_i$ is
$(N-1)/2$. Also $c_{i+1}\ge c_i-1$: moving to the next initial
endpoint removes at most that point, while the terminal endpoint advances.
With $t=\lfloor(N-1)/2\rfloor$, some $c_i\le t$ and some $c_i\ge t$,
and a cyclic downward transition cannot skip $t$. Thus some
$c_i=t$, and its other semicircle contains $N-1-t\ge t$ points.
For antipodal configurations, perturb the angles to remove all antipodal
pairs and pass to a subsequence with the same selected label. Membership
in either corresponding closed semicircle survives in the limit.

**2-core lemma.** Let $k\ge1$ be an integer. If at most $k-1$ distinct distances
of $B$ exceed $r>0$, the distance-$r$ graph has a 2-core of maximum degree at
most $4k-2$. Consequently

$$m_B(r)\le(2k-1)|B|.$$

Delete vertices of current degree at most one until the 2-core remains.
At a core vertex $p$, apply the balanced-circle lemma to its $N$
neighbors on $C(p,r)$, obtaining $q$. Since $q$ belongs to the core,
it has an $r$-neighbor $w\ne p$. The intersection of $C(p,r)$ with
the closed radius-$r$ disk about $w$ is an arc of angular length
strictly less than $\pi$, with $q$ as an endpoint, or the singleton
$q$. Indeed, writing $\rho=|p-w|>0$ and measuring angles toward $w$,
the intersection satisfies

$$\cos\theta\ge\rho/(2r)>0.$$

One closed semicircle based at $q$, except for $q$ itself, is therefore
strictly outside the disk. It contains at least
$\lfloor(N-1)/2\rfloor$ neighbors $x$ of $p$ with $|x-w|>r$.
There are at most $k-1$ possible such lengths, and each corresponding
circle about $w$ meets $C(p,r)$ in at most two points. Hence

$$\lfloor(N-1)/2\rfloor\le2(k-1),\qquad N\le4k-2.$$

If the core has $v$ vertices, it has at most $(2k-1)v$ edges.
Deleting the other vertices removed at most $|B|-v$ edges, so
$m_B(r)\le |B|-v+(2k-1)v\le(2k-1)|B|$. This includes an empty
core. At $k=1$ it recovers the diameter bound.

By (1), all pairs at $r_j$ occur within $B_j$, which also contains every
larger distance. Writing $s_j=|B_j|$ now gives

$$m_A(r_j)\le(2j-1)s_j. \tag{6}$$

Rarity in an arbitrary convex subset does not survive restoration of
the other points; the exact support statement (1) avoids that loss here.

In particular, $(2k-1)s_k\le n$ makes all top $k$ distances rare.
No extra rank-existence hypothesis is needed: if $k\ge2$, this premise
implies $s_k<n$, so a point deeper than layer $k$, paired with a
first-layer point, has distance rank greater than $k$ by (1). The case
$k=1$ needs only $n\ge2$.

The earlier $2k$-degeneracy statement is retained as a separate graph
property; the 2-core lemma improves its edge count, not its asserted
degeneracy. The exponential proof uses only hereditary diameter counting.
The source's second-distance estimates recorded below remain sharper
than (6) at rank two.

### An alternative disk-core argument

Section 3 of the
[third independent report](independent/layer_bound_and_circular_majority.md)
gives a different, valid elementary proof of $m_B(r)\le(6k-5)|B|$ when at most
$k-1$ distances exceed $r$. This is weaker than the 2-core bound above, but its
local statement about neighbors outside a common disk intersection is worth
retaining. An empty distance-$r$ graph needs no proof.

Put

$$C=\{x\in B:|x-p|\le r\text{ for every }p\in B\},
\qquad E=B\setminus C.$$

Fix $q\in B$ and let $S=B\cap\Gamma(q,r)$, where $\Gamma(q,r)$ denotes
the radius-$r$ circle. For each $p\in B\setminus\{q\}$, its closed
radius-$r$ disk cuts this circle in a closed arc $I_p$ of angular
length strictly less than $\pi$, a singleton, or the empty set.
There are at most $2(k-1)$ points of $S$ outside $I_p$: their
distances to $p$ exceed $r$, and each of the at most $k-1$ larger
distance circles meets $\Gamma(q,r)$ in at most two points. Omitting
$p=q$ ensures that these circles have distinct centers.

If $J=\bigcap_p I_p$ is nonempty, cut the circle at the antipode
of a common point. All arcs become intervals, and two extreme
endpoints determine their intersection. At most $4(k-1)$ points of
$S$ lie outside $J$. If $J$ is empty, at most three arcs witness
this: fix one nonempty arc $I_0$; its intersection with every other
short arc is an interval in $I_0$, and two such intervals already
witness an empty intersection. An empty individual arc is an
immediate witness. Hence in this case $|S|\le6(k-1)$.
Since $S\cap J=S\cap C$, both cases give

$$\#\{x\in E:|x-q|=r\}\le6(k-1).$$

Summing over $q$ counts every $r$-edge meeting $E$ at least once,
so there are at most $6(k-1)|B|$ such edges. The edges within $C$
are diameter edges of $C$, if any, and number at most $|C|$ by
the planar diameter theorem. This proves the asserted rank bound.
The author checked the short-arc intersection claims, including empty
and singleton arcs; the argument is author-recorded.

The report's layer localization repeats (1). Its consequences
$s_{K+1}>n/(6K+1)$ and divergence for $\Delta/\delta=o(n)$ are
superseded by the constants and the $O(n)$ aspect-ratio theorem below.
Its unused Ramsey alternative in Section 9 is not certified: the
companion proof file is absent, and "disjoint segments" must mean
geometrically disjoint, not merely vertex-disjoint. The two diagonals
of a square refute the latter interpretation of its longer-pair claim.
No Ramsey constant from that alternative is used here.

### Quantitative consequences

Let $h=\max_i|L_i|$, and assume $n\ge2$. Then

$$R(A)\ge
 \left\lfloor\frac{1+\sqrt{1+8n/h}}4\right\rfloor. \tag{7}$$

Indeed, $s_k\le kh$, and solving $k(2k-1)h\le n$ gives (7).
Its right side is at least one since $h\le n$.
The qualitative sparse-layer theorem above stands, and its converse holds
without a separate distance-count assumption: if $R(A)\le K$,
then

$$s_{K+1}>\frac{n}{2K+1}.$$

Some layer among the first $K+1$ therefore has more than
$n/[(K+1)(2K+1)]$ vertices. This improves the previous numerical
constants, but does not exclude a positive-density outer layer.

If $\delta$ is the minimum distance and $\Delta$ the diameter, each
nondegenerate layer has perimeter at least $|L_i|\delta$ and at most
$\pi\Delta$. To see the latter, integrate its edge projections over
directions $0\le\theta\le\pi$: the sum of absolute projections is
twice the width, every width is at most $\Delta$, and an edge of length
$a$ contributes $2a$ to the integral. One- and two-point layers satisfy
the same cardinality bound directly. Consequently

$$R(A)\ge\max\left\{1,
 \left\lfloor\frac{1+\sqrt{1+8n\delta/(\pi\Delta)}}4\right\rfloor
 \right\}. \tag{8}$$

Thus $\Delta/\delta=o(n)$ forces divergence, and separation bounded
below with diameter $O(\sqrt n)$ gives $R(A)=\Omega(n^{1/4})$.
Both qualitative conclusions predate the second independent input;
the 2-core argument sharpens their displayed bounds. The author checked
antipodal limits, tangent intersections, empty cores, degenerate layers,
and existence of the required ranks; the argument is author-recorded.

There is also a complementary support-size estimate. In a fixed-distance
graph on $s$ points, two vertices have at most two common neighbors.
For $e$ edges, counting pairs of neighbors and applying Cauchy--Schwarz
gives

$$2e^2/s-e\le\sum_v\binom{\deg v}{2}\le2\binom s2,
\qquad e\le U(s):=\frac{s}{4}(1+\sqrt{8s-7}).$$

Provided $q(A)\ge k$, $U(s_k)\le n$ also makes all top $k$ distances rare. Since
$U(s)\le s/4+s^{3/2}/\sqrt2$, the condition $s_k\le n^{2/3}$ suffices, giving
$R(A)\ge\lfloor n^{2/3}/h\rfloor$. Importing the standard unit-distance estimate
$e\le Cs^{4/3}$ similarly gives $R(A)\ge\lfloor c n^{3/4}/h\rfloor$ with
$c=\min\{1,C^{-3/4}\}$. That optional input is stated in Section 1.4 of the
[supplied Clemen--Dumitrescu--Liu
paper](../../../library/distance_problems/clemen_2025_multiplicities_interpoint_distances/_index.md);
the angular and elementary support bounds do not depend on it.

## Linear aspect ratios force rarity divergence

**Theorem.** If $|A_n|=n\to\infty$ and
$\Delta(A_n)/\delta(A_n)=O(n)$, then $R(A_n)\to\infty$.
Equivalently, every bounded-rarity sequence satisfies

$$\frac{\Delta(A_n)}{n\delta(A_n)}\longrightarrow\infty. \tag{9}$$

Suppose $R(A)\le K$ and $\Delta\le C_0n\delta$ along an unbounded
sequence, where $K,C_0$ are fixed. The layer converse above gives a
strictly convex layer $C$ with

$$m=|C|\ge c_Kn,\qquad c_K=\frac1{(K+1)(2K+1)}.$$

Its perimeter is at most $\pi\Delta\le\pi C_0n\delta$. Hence at
least $m/2$ polygon sides have length at most $L\delta$, where
$L=\max\{1,2\pi C_0/c_K\}$ is fixed.

The disks of radius $\delta/2$ about points of $A$ have disjoint
interiors. All disks whose centers are within $L\delta$ of a fixed
point lie in a disk of radius $(L+1/2)\delta$. Thus there are at most
$M=(2L+1)^2$ such centers, and at most $Mn/2$ unordered pairs of
length at most $L\delta$. Each rich class consumes more than $n$
pairs, while there are at most $K$ rare classes. The number of occurring
lengths in this interval is therefore at most

$$T=K+\lceil M/2\rceil.$$

One of them occurs on at least $c_Kn/(2T)$ sides of $C$ and has
global smallest-distance rank at most $T$. Also the pair budget gives
$q(A)\le n/2+K\le n$ for large $n$. The
[short-edge incident inverse](short_incident_inverse.md) therefore
supplies a positive fraction of $A$ on one circle. The
[circle theorem](circle_incidence.md) then contradicts $R(A)\le K$.
The selected side length need not itself be rich: the inverse only
requires linearly many incidences at a bounded short rank.

This strengthens the earlier $\Delta/\delta=o(n)$ criterion, but
uses the short-edge inverse and its external rich-motion theorem,
not merely the elementary 2-core estimate. The author checked the
packing, perimeter, rank, and quantifiers; the argument is
author-recorded. It gives
no contradiction when $\Delta/(n\delta)$ tends to infinity.

## A small-vertex-cover restriction

If two distinct rich distance graphs have vertex covers of sizes
$s,t$, then

$$n\le2st+3\binom s2+3\binom t2-2. \tag{4}$$

For one such cover $C$ of size $t$, let $u$ count vertices outside
$C$ with no neighbor in $C$. At most $n-t-u$ incidences can be the
first at an outside vertex. The remaining incidences number at most
$2\binom t2$, since two different radius-$r$ circles meet in at most
two points and $(d-1)_+\le\binom d2$. Including edges inside $C$ gives

$$m_A(r)\le n-t-u+3\binom t2.$$

Richness therefore implies $u\le3\binom t2-t-1$. All but at most
$3\binom t2-1$ points lie on the union of the $t$ circles centered
at $C$. The analogous $s$ circles for a different radius have at
most $2st$ intersections with this union, because no circles of the
two families coincide. This proves (4).

Combining with (1), if $S_h=|B_h|$ and
$n>5S_h^2-3S_h-2$, then

$$R(A)\ge\min\{D,2h\}-1.$$

## A concrete obstruction to a larger-residue valuation extension

The [binary valuation proof](dyadic_distances.md) does not extend by
simply taking the largest Euclidean distance at each dyadic level in
an Eisenstein-coordinate set. Put $\omega=(1+i\sqrt3)/2$, so
$|a+b\omega|^2=a^2+ab+b^2$, and take

$$A=\{\omega,2\omega,1+\omega,1+3\omega,2+3\omega,3\}.$$

Its exact squared-distance multiplicities are

| Squared distance | Multiplicity |
| --- | ---: |
| $1$ | 4 |
| $3$ | 2 |
| $4$ | 1 |
| $7$ | 7 |
| $12$ | 1 |

These sum to $15=\binom62$. The largest squared distance of $2$-adic
valuation zero is $7$, and it occurs $7>6$ times. This is **not** an
E132 counterexample: four of its five distances are rare. It only
refutes that particular extension of the binary lemma. The executable
[exact certificate](evidence/util/valuation_counterexample.py) checks all
15 pairs using integer arithmetic.

A bounded exploratory enumeration of all $65,535$ nonempty subsets
of the $4$-by-$4$ Eisenstein-coordinate grid found this example.
A second bounded check on the same domain found that every occurring
valuation level still had some rare class. That latter observation
is finite computational evidence only; no general assertion per level
has been proved, and no further enumeration is proposed on its basis.

## Source correction

The actual statement of Clemen--Dumitrescu--Liu, Theorem 1.3, is

$$\min\{\tfrac32(h+s),\tfrac43h+2s,2h+s\}\le n,$$

where $h=|L_1|$ and $s=|L_2|$. The supplied digest swaps some coefficients. The
statement was checked in the
[full supplied paper](../../../library/distance_problems/clemen_2025_multiplicities_interpoint_distances/_index.md)
and the [arXiv version](https://arxiv.org/html/2505.04283v2#S1.SS1). None of the
elementary layer or cover bounds relies on that criterion.

There is a separate arithmetic slip in the supplied full transcription,
Section 2.2. After $e(L'_1,L'_2)=2|L'_2|$, the identity is

$$2|L'_1|-\tfrac12 e(L'_1,L'_2)=2|L'_1|-|L'_2|,$$

not $2|L'_1|-2|L'_2|$. The following display uses the correct coefficient,
and the final theorem is unaffected. This agrees with the independent
input's correction; it is not the earlier digest's coefficient swap.

## Why hereditary diameter structure alone cannot suffice

The independent input supplies a stronger abstract obstruction than
merely failing to bound the second distance. For $n=4s$, $s\ge2$,
color the edges on labels $0,\ldots,n-1$ according to the interval
containing the absolute label difference:

$$\{1\},\ [2,3],\ [4,5],\ \ldots,\ [2s-2,2s-1],\ [2s,4s-1],$$

with earlier intervals higher in the color order. The highest color
has $n-1$ edges. A middle color $[2j,2j+1]$ has
$2n-4j-1\ge n+3$ edges; the last has $s(2s+1)>n$.
Exactly one color has between one and $n$ edges.

Nevertheless every induced highest-color graph is a linear forest.
If its interval is $[L,U]$, all gaps between consecutive selected
labels are at least $L$, because smaller gaps would have higher colors.
Every interval above has $U<2L$. Thus a highest-color edge can only
join consecutive selected labels, making the graph a subgraph of a path.
This satisfies hereditary diameter edge bounds, absence of even cycles,
and the at-most-one-cycle restriction, without forcing a second rare color.

It is **not** a planar distance coloring. Five consecutive labels
already give a contradiction. Suppose their colors had lengths
$a>b>c>0$, with adjacent labels at $a$, gaps two or three at $b$,
and gap four at $c$. Put $p_1=(0,0)$ and $p_2=(a,0)$. Then

$$p_0=(a-b^2/(2a),y),\quad p_3=(b^2/(2a),z),
\qquad y^2=z^2=b^2-b^4/(4a^2)>0.$$

If $z=-y$, then $|p_0-p_3|^2=a^2+2b^2>b^2$, a contradiction.
Thus $z=y$, so $p_0,p_3$ are reflections across the perpendicular
bisector of $p_1p_2$. Since $|p_1-p_4|=|p_2-p_4|=b$, that bisector
contains $p_4$. Hence $|p_0-p_4|=|p_3-p_4|=a$, contradicting $c<a$.
Both the abstract count and this Euclidean obstruction were checked.

For actual point sets, a rich distance graph has a component with
more edges than vertices. Its geometric diameter must exceed that
distance, or the diameter theorem applied to the component would
contradict its edge count. This supplies an upward dependency but
not an injection: many rich classes may depend on the same larger
distance. Neither it nor the abstract construction fills that counting
gap. The [unique-diameter family](unique_diameter_obstruction.md)
is a different, genuinely Euclidean obstruction to bounding a rich
second-distance core from diameter multiplicity alone.

Nor can one always choose a rare class just from the smallest and
second-largest distances. The supplied Clemen--Dumitrescu--Liu
Proposition 1.5 gives constructions with

$$m_A(r_2)\ge3m,\qquad m_A(\delta)\ge3n-5m+o(m).$$

Taking $m=\lfloor3n/8\rfloor$ makes both at least $9n/8+o(n)>n$
for sufficiently large $n$. The theorem statement and construction
passage in Sections 1.1 and 2.3 were compared with the independent input.
The cited proposition is an obstruction to choosing these two classes,
not a counterexample to the existence of some second rare class.

### A correction to the cited short-distance construction

The source's literal assertion that its minimum distance is between
consecutive inner-polygon vertices is false for large odd $m$, with
the vertices indexed cyclically. The independent input explicitly did
not reconstruct that construction. Here is a checked correction for
the proportional regime needed for the obstruction.

Write $\alpha=\pi/m$ and take the outer regular odd $m$-gon with
circumradius $R=n$. Its second-largest distance is
$d_2=2R\cos(3\alpha/2)$. The source's inner circle intersections give
an aligned regular $m$-gon of radius

$$\rho=R\left(\sqrt{4\cos^2(3\alpha/2)-\sin^2\alpha}
                    -\cos\alpha\right)
       =R(1-2\alpha^2+O(\alpha^4)).$$

Indeed the inward intersection for two consecutive outer vertices is
opposite their angular midpoint, an outer-vertex ray when $m$ is odd.
The radial pairs have length
$\delta=R-\rho=2R\alpha^2+O(R\alpha^4)$, whereas inner sides have
length $2\rho\sin\alpha=2R\alpha+O(R\alpha^3)$. Thus for large $m$
the radial distance, not the inner side, is the minimum of the two
rings, and it occurs $m$ times. Other cross-ring distances are larger
by the cosine formula.

There is also an exact finite certificate at $m=9$, $n=24$. Then
$\rho/R=\sqrt{2+\cos^2(\pi/9)}-\cos(\pi/9)\in(2/3,1)$:
the upper bound follows from $\cos(\pi/9)>1/2$, and rationalizing
gives the lower bound $\rho/R>\sqrt3-1>2/3$. Since
$\sin(\pi/9)>\sin(\pi/12)>1/4$, the radial distance is less than
$R/3$ while the inner side is greater than $R/3$.

The largest cross-ring distance is exactly $d_2$, attained by $2m$
pairs: the largest angular separation is $\pi-\alpha$, and the
displayed value of $\rho$ solves
$R^2+\rho^2+2R\rho\cos\alpha=d_2^2$. The inner diameter is

strictly below $d_2$, since

$$d_2^2-[2\rho\cos(\alpha/2)]^2
 =(R-\rho)(R+\rho+2\rho\cos\alpha)>0.$$

Hence the two rings have $3m$ pairs at their second-largest distance
(the additional $m$ lie in the outer polygon).

For an explicit unbounded parameter sequence, take $n=8t$, $m=3t$
with odd $t\to\infty$. Add $n-2m$ points of a compact triangular-lattice
patch of mesh $\delta$ near the origin, with radius
$O(\delta\sqrt n)=O(n^{-1/2})$. A patch with $s=n-2m$ points and
$O(\sqrt s)$ boundary points has at least $3s-O(\sqrt s)$ nearest-neighbor
pairs; complete triangular rows and a partial final row give such a patch.
Its distances to either ring are between $\delta$ and $d_2$ for large
$n$, and its own diameter is below $d_2$. Thus in the full set

$$m_A(d_2)=3m=9n/8,\qquad
 m_A(\delta)\ge m+3(n-2m)-O(\sqrt n)=9n/8-O(\sqrt n)>n.$$

This repairs the relevant asymptotic obstruction without certifying
every parameter regime of the source proposition. It still contains a
regular $m$-gon of positive fraction, so the
[circle theorem](circle_incidence.md) forces linearly many other rare
distances. The radius calculation and repaired construction were checked
by the author and are author-recorded.
