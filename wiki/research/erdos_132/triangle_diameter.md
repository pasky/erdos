---
name: research/erdos_132/triangle_diameter
title: Diameter triangles and bounded odd diameter cycles
desc: |
  A diameter triangle forces two rare distances; a bounded-length odd
  diameter cycle forces rarity divergence along an unbounded sequence.
sources: []
research_state: closed
created: 2026-09-23T05:40:00Z
updated: 2026-09-24T22:12:56Z
---


# Diameter triangles and bounded odd diameter cycles

***

**Theorem.** If a planar $n\ge5$ point set has three points whose mutual
distances all equal its diameter, then $R(A)\ge2$.

Also, along any unbounded sequence in which the diameter graph contains an
odd cycle of bounded length, $R(A)\to\infty$.

These cover additional diameter graphs, not arbitrary sets: a diameter
graph can be acyclic, and its odd cycle can have unbounded length.

## Reuleaux triangle geometry

Normalize the diameter to one and write the diameter triangle as
$a=0,b=1,c=\omega=e^{i\pi/3}$. Let


$$
K=\overline B(a,1)\cap\overline B(b,1)\cap\overline B(c,1).
$$


This is the Reuleaux triangle of width one and contains $A$. Its boundary
points are exactly those points of $A$ active for the diameter: every
boundary point has a corner as a diameter partner; an interior point
cannot attain the diameter of $K$. Put $S=A\cap\partial K$, $T=A\setminus S$,
$s=|S|$, $t=|T|$, and let $r<1$ be the second-largest distance.
If $T\ne\varnothing$, distances to the three corners show
$r\ge1/\sqrt3$. For example, their squared distances from any point
sum to at least one.

Let $Q=\bigcap_{v\in\{a,b,c\}}\overline B(v,r)$, so $T\subseteq Q$.
Here is a useful strict arc inequality. In coordinates centered at a
unit-circle arc's center, an interior point $w$ of its short arc from
$p$ to $q$ has


$$
w=\lambda p+\mu q,\qquad\lambda,\mu>0,\qquad h=\lambda+\mu>1.
$$


If $|z-p|,|z-q|\le r<1$, expansion gives


$$
|z-w|^2\le r^2-(h-1)(|z|^2+1-r^2)<r^2. \tag{1}
$$


Thus every point of $Q$ is within $r$ of all of $K$, and strictly
within $r$ of every noncorner boundary point. In particular, there are
no $r$-pairs between $T$ and $S\setminus\{a,b,c\}$.

Opposite support points of $K$ have projections $h_K(u)$ and
$h_K(u)-1$ in each unit direction $u$. For $z\in Q$, the distance
bounds to those points imply


$$
h_K(u)-r\le z\cdot u\le h_K(u)-1+r.
$$


Every width of $Q$, and hence its diameter, is at most $2r-1$. Therefore


$$
\operatorname{diam}T\le2r-1<r. \tag{2}
$$


Every $S$--$T$ distance is at least $1-r$: use a diameter partner
in $S$ for its endpoint in $S$, and the triangle inequality.

For $r>1/\sqrt3$, at most three points of $Q$ are on two of its
defining circles, and none is on all three. Indeed, each pair of the
circles has at most one intersection in the third disk, and the unique
point equidistant from all three corners has distance $1/\sqrt3$.
Consequently


$$
e_r(T,\{a,b,c\})\le t+3. \tag{3}
$$


At $r=1/\sqrt3$, $Q$ is a singleton and (3) also holds.

## Three path components on the boundary

Assume $1/\sqrt3\le r<1$, and that $S\subset\partial K$ contains the
three corners and has no distance in $(r,1)$. Put


$$
r_0=(\sqrt5-1)/2.
$$


We prove


$$
e_r(S)\le s-3\quad(r\ne r_0),\qquad
e_r(S)\le s-2\quad(r=r_0). \tag{4}
$$


The [constant-width two-intersection theorem](constant_width.md) makes
this graph have maximum degree two. Each corner has degree at most one.
To see this at $a$, put $\theta=\arccos(r/2)>\pi/3$. Its two possible
boundary neighbors are separated by


$$
d=2r\sin(\theta-\pi/6)>r.
$$


With $\beta=\pi-2\theta\in(0,\pi/3)$, the same expression is
$d=2\cos(\pi/3-\beta)-1<1$. They cannot both belong to $S$.
This already proves the second bound in (4) by handshaking.

For the first bound, start a path $a-x$ and interchange $b,c$ if
necessary so that $x$ is on the arc $a$--$c$ centered at $b$. Then


$$
x=(r^2/2,r\sqrt{4-r^2}/2)=r e^{i\theta},\qquad
|c-x|=\sqrt{1-r^2/4}-\sqrt3r/2<r.
$$


If $x$ has a second $r$-neighbor $y$, boundary-distance monotonicity
and the two-intersection theorem place $y$ in the interior arc
$b$--$c$ centered at $a$. Thus $|a-y|=1$, while
$|b-y|,|c-y|\le r$. If $|b-y|=r$, then


$$
y=(1-r^2/2,r\sqrt{4-r^2}/2),\qquad |x-y|=1-r^2=r,
$$


forcing $r=r_0$. Exclude that case. Now $|b-y|<r$; also $|c-y|<r$,
since otherwise the two-intersection count for the circle about $y$
would be exceeded. Any next neighbor $z$ must lie in the interior arc
$a$--$b$ centered at $c$. Hence $|c-z|=1$. A noncorner boundary
point has just one diameter partner, its arc center. Thus $|x-z|<1$,
and the spectral gap makes it at most $r$. We would have


$$
z\in L:=\overline B(x,r)\cap\overline B(y,r),\qquad |c-z|=1. \tag{5}
$$


The following calculation rules this out. For two points $x,y$ at
distance $r$, and $c\in L$, the point of $L$ farthest from $c$ is
the equilateral completion $e_-$ on the opposite side of $xy$ from
$c$. In coordinates $x=(0,0),y=(r,0),c=(u,v)$, take $v\ge0$.
The lens conditions give $0\le u\le r$. On its circle-about-$x$ arc,
$\cos\phi\ge1/2$ and $\sin\phi\ge-\sqrt3/2$, so
$u\cos\phi+v\sin\phi\ge u/2-\sqrt3v/2$; the other arc gives the
same maximum at $e_-=(r/2,-\sqrt3r/2)$.

In the original coordinates put $\alpha=\arccos(1/(2r))$. Then


$$
y=e^{i(\theta-\alpha)},\quad
e_-=\omega x+\overline\omega y,\quad
1-x=e^{-i\beta},\quad
c-e_-=\omega(1-x+\omega y).
$$


The angle between the two unit summands is
$\gamma=4\pi/3-\theta-\alpha$. Here


$$
\pi/3<\theta+\alpha<2\pi/3.
$$


For the upper inequality, $\cos(\theta+\alpha)>-1/2$ reduces after
squaring positive quantities to $4(1-r^2)^2>0$. The lower inequality
is immediate from $\theta>\pi/3$, $\alpha>0$. Thus
$2\pi/3<\gamma<\pi$ and


$$
|c-e_-|=2\cos(\gamma/2)<1,
$$


contradicting (5). Every corner component is consequently a path of at
most two edges and contains no other corner. There are three distinct
path components; all remaining maximum-degree-two components have no
more edges than vertices. This proves the first bound in (4).

## Completing the finite theorem

If $T$ is empty, the constant-width theorem makes every distance rare,
and there are at least $\lfloor n/2\rfloor\ge2$ distances.
Otherwise, when $r\ne r_0$, (2)--(4) give


$$
m_A(r)\le(s-3)+(t+3)=n.
$$


For $r=r_0<2/3$ and $t\ge2$, take
$\tau=\operatorname{diam}T>0$. By (2),


$$
\tau\le2r-1<1-r.
$$


It has no $S$--$T$ occurrences. Its pairs inside $S$ number at most
$s$ by the constant-width theorem, and inside $T$ at most $t$ by
the diameter theorem. Hence $\tau$ is rare and differs from the full
diameter. If $t=1$, the single interior point has at most two corner
neighbors at $r_0>1/\sqrt3$, and (4) gives $m_A(r_0)\le s<n$.
This proves $R(A)\ge2$ in all cases.

## Bounded-length odd diameter cycles

Let $V=\{c_0,\ldots,c_{\ell-1}\}$ be the vertices of an odd diameter
cycle, with consecutive cycle vertices at distance $D$. In any
constant-width-$D$ completion $K$ of $A$, the short radius-$D$ arc
centered at $c_i$ from $c_{i-1}$ to $c_{i+1}$ lies in $partial K$.
The arc lemma in [constant_width](constant_width.md) proves inclusion in
$K$; being at distance $D$ from $c_i$ forces boundary inclusion.

No other cycle vertex is interior to this arc, because interior points
have the unique diameter partner $c_i$, whereas a cycle vertex has two
distinct partners. Distinct arcs have disjoint interiors: an interior
overlap on the Jordan curve $partial K$ would contain an interval,
impossible for arcs on distinct circles. Their endpoint graph is the
step-two cycle on the indices, connected since $\ell$ is odd. Their
union is therefore a closed subcurve and equals $partial K$.

For any $r<D$, the radius-$D$ version of (1) now gives


$$
Q_r:=\bigcap_{v\in V}\overline B(v,r)
=\bigcap_{x\in K}\overline B(x,r),\qquad
\operatorname{diam}Q_r\le2r-D<r, \tag{6}
$$


whenever $Q_r$ is nonempty. The support-projection proof above applies
with width $D$.

Suppose $R(A)\le M$ and $n\to\infty$, while $\ell$ is bounded.
Choose a rich distance $r=r_k$ among the largest $M+1$ ranks, so
$2\le k\le M+1$. Such ranks exist eventually: two anchors already
bound $n\le2q(A)^2+2$, so $q(A)\to\infty$. Put


$$
B=\{p\in A:|p-v|>r\text{ for some }v\in V\}.
$$


This set lies on at most $\ell(k-1)$ circles. The
[circle theorem](circle_incidence.md) implies $|B|=o(n)$, uniformly.
The complement lies in $Q_r$, so (6) makes $B$ a vertex cover of the
$r$-graph. Its (2)-core has maximum degree at most $4k-2$, hence
has at most $(4k-2)|B|=o(n)$ edges. But the
[rich long-core surplus](diameter_activity.md), using a rich short rank
$s\le M+1$, gives a surplus of at least $n/(3s)-o(n)$. This is a
contradiction, proving divergence under the bounded-cycle hypothesis.

## Quantitative cycle restrictions

The [quantitative circle bound](quantitative_circle.md) improves the last
conclusion: under $R(A)\le M$, every circle has $O_M(n^{31/32})$ points.
Thus the exceptional cover above satisfies


$$
|B|\le C_M\ell n^{31/32}.
$$


The bounded-degree core and its linear surplus force $|B|\ge c_M n$.
Consequently any odd diameter cycle in a bounded-rarity sequence has


$$
\ell\ge c'_M n^{1/32}. \tag{7}
$$


In particular, $\ell=o(n^{1/32})$ forces rarity divergence.

For $R=1$ the stronger bound


$$
\ell\ge(1/5-o(1))n \tag{8}
$$


follows. Let $S$ be the diameter-active set and $T=A\setminus S$.
At the second distance $r$, every point of $T$ is within $r$ of every
point of $A$. Formula (6) makes $T$ independent, and the strict arc
inequality makes all its $r$-neighbors belong to $V$.
In the $2$-core $H$, let $E$ count $V$--$T$ edges and $t_H$ count its
$T$-vertices. The arc-leaf argument in
[diameter_activity](diameter_activity.md) gives at most two core neighbors
in $T$ for each vertex of $V$, so $E\le2\ell$. The core degree bound six
gives $t_H\ge E/6$. The constant-width theorem gives no positive surplus
on $H[S]$. Hence


$$
e(H)-v(H)\le E-t_H\le5E/6\le5\ell/3.
$$


The known surplus lower bound for the rich minimum and second-largest
classes is $n/3-o(n)$, proving (8).

The author checked the arc contraction, the corner-path trigonometry,
the exceptional case, the odd-cycle tiling and core count, and
(7)--(8) against their stated inputs; the argument is author-recorded.
No conclusion covers acyclic diameter graphs or general growing odd
cycles. Neither unrestricted target has been resolved.
