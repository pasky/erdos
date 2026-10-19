---
name: research/erdos_132/monotone_chain_inverse
title: Near-minimal distance counts on convex monotone chains
desc: |
  Bounded rank errors force a large circular subset of a convex monotone
  chain; half-sized chains therefore force rarity growth in the full set.
sources: []
research_state: closed
created: 2026-09-23T01:15:00Z
updated: 2026-09-24T22:12:56Z
---


# Near-minimal distance counts on convex monotone chains

***

This extends the bounded-omission mechanism in
[constant_width_inverse](constant_width_inverse.md). It does not resolve either
unrestricted assertion of
[Problem 132](../../problems/distance_problems/E0132/_index.md).

## A chain inverse theorem

Call an ordered strictly convex set $C=(p_0,\ldots,p_{m-1})$
distance-monotone if, whenever $i<j<k$,

$$|p_ip_j|<|p_ip_k|,\qquad |p_jp_k|<|p_ip_k|.$$

**Theorem.** For each fixed $L\ge0$, there are $c_L>0$ and $m_L$
such that, if $m\ge m_L$ and $q(C)\le m-1+L$, then some circle
contains at least $c_Lm$ points of $C$.

List the distances as $d_1<\cdots<d_q$ and write $r(i,j)$ for the
rank of $|p_ip_j|$, $i<j$. Growing the interval $[i,i+1]$ to
$[i,j]$ proves $r(i,j)\ge j-i$. Extending $[i,j]$ to $[0,m-1]$
increases rank strictly at every step, so

$$q\ge r(i,j)+(m-1)-(j-i).$$

Consequently

$$j-i\le r(i,j)\le j-i+L. \tag{1}$$

Put $E=\lceil L\rceil$ and $e_i(k)=r(i,i+k)-k$. Each row is
nondecreasing, takes values in $\{0,\ldots,E\}$, and has at most
$E$ jumps. Set $s=\lfloor m/4\rfloor$, and restrict to rows
$0\le i<s$ and offsets $1\le k\le s$.

Choose $N$ so that every $(E+1)^2$-coloring of $N$ consecutive
integers has a monochromatic four-term arithmetic progression, and
choose $M\ge8N(E+1)$. These are constants depending only on $L$.
Partition $[1,s]$ into $M$ consecutive intervals of almost equal
length. Some interval $J=[u,v]$, of length $\Omega_L(m)$, has fewer
than $s/(8N)$ rows nonconstant on it: each row is nonconstant on at
most $E$ intervals.

For large enough $m$, all intervals $[N^a,N^{a+1}]$, $0\le a<M$,
fit in $[1,s]$. Each jump is internal to at most one such interval,
so some $H=[h,Nh]$ also has fewer than $s/(8N)$ nonconstant rows.
Here $h$ is bounded in terms of $L$ alone.

Call a row good if it is constant on both $J$ and $H$, and give it
the ordered pair of its constant values as color. Fewer than
$s/(4N)$ rows are bad. Each bad row spoils at most $N$ progressions

$$i,i+h,\ldots,i+(N-1)h$$

contained in $[0,s-1]$. There are $s-O_L(1)$ possible starts, so one
progression is entirely good. By the choice of $N$, it contains
four same-colored rows

$$a,\quad a+k,\quad a+2k,\quad a+3k,$$

where $k=dh=O_L(1)$ and $k,2k\in H$.

Set $x_\ell=p_{a+\ell k}$. Formula (1) and the common row values on
$H$ give

$$|x_0x_1|=|x_1x_2|=|x_2x_3|,
\qquad |x_0x_2|=|x_1x_3|.$$

The successive triangles are congruent and have the same orientation.
The direct isometry $T$ taking $(x_0,x_1,x_2)$ to $(x_1,x_2,x_3)$
cannot be a translation, since three consecutive anchors are
noncollinear. Thus $T$ is a nontrivial rotation.

Write $z_j=p_{a+j}$, and let $b$ be the common row value on $J$.
For $u+2k\le j\le v$ and $\ell=0,1,2$,

$$|z_{j+k}-x_{\ell+1}|=d_{j-\ell k+b}=|z_j-x_\ell|.$$

Distances to three noncollinear anchors determine a point uniquely,
so $z_{j+k}=Tz_j$. A consecutive interval of $\Omega_L(m)$ indices
therefore splits into at most $k=O_L(1)$ rotation orbits. One orbit
contains $\Omega_L(m)$ distinct points on a positive-radius circle.
All indices used are less than $2s+O_L(1)<m$; there is no cyclic
wrap in this argument. This proves the theorem.

## Half-sized chains suffice for growth

**Corollary.** Fix $t\ge0$. If each $n$-point set in a sequence contains
a distance-monotone strictly convex chain with at least $n/2-t$
points, then $R(A)\to\infty$ as $n\to\infty$.

Otherwise, on an unbounded subsequence $R(A)\le K$. The pair budget
gives $q(A)\le n/2+K$, so for the $m$-point chain,

$$q(C)\le m-1+(K+t+1).$$

The theorem supplies a positive circular fraction of the full set.
The checked [circle-incidence theorem](circle_incidence.md) then
forces linearly many rare distances, a contradiction. Thresholds
and multiplicities here are always for the full $n$-point set.

One example is a strictly convex set whose minimum enclosing disk
has two antipodal support vertices. The more populous closed
semicircle, counting both endpoints, contains at least $n/2+1$
vertices and forms a cap. Every ordered middle angle in a cap is
at least $\pi/2$, which implies the required strict distance
monotonicity by the cosine rule.

The cap facts were checked in Nivasch--Pach--Pinchasi--Zerbib, [*The number of
distinct distances from a vertex of a convex
polygon*](https://www.renyi.hu/~pach/publications/distdist042512.pdf),
Definition 5 and Properties 1--2, pp. 4--5. Their enclosing-circle argument
splits an arbitrary convex set into at most three caps; that gives only a
third-sized cap, not the half-sized chain needed here.

## Exact obstruction to a diameter-cut shortcut

A convex subpolygon with a diameter side need not be distance-monotone.
The consecutive vertices

$$(0,0),\ (7/10,16/25),\ (9/10,27/100),\ (1,0)$$

form a strictly convex quadrilateral whose closing side is its unique
diameter. Yet the first vertex has successive squared distances
$2249/2500=0.8996$ and $8829/10000=0.8829$, in decreasing order.
All six squared lengths are at most one, and the four consecutive
cross products have the same strict sign.

Thus Altman's maximal-side lemma alone does not produce the required
chain. Nor does the existing outer-layer reduction give a chain of
half the full cardinality: its positive fraction can be much smaller.
These remain substantive gaps, not consequences of the theorem.

The author checked the rank estimates, row selection, and rotation
propagation; the argument is author-recorded. No unrestricted proof or
counterexample resulted.
