---
name: research/erdos_132/two_cover_diameter
title: Further restrictions on two-cover diameter graphs
desc: |
  Ten diameter edges suffice when two vertices cover the diameter graph;
  the matching-two sharp case and even active equality cases are excluded.
sources: []
research_state: closed
created: 2026-09-23T03:11:32Z
updated: 2026-09-24T22:12:56Z
---


# Further restrictions on two-cover diameter graphs

***

All multiplicities count unordered pairs. These results extend the
[star-diameter theorem](star_diameter.md), but do not settle either
unrestricted question.

## A bound for a two-vertex diameter cover

Let $D>r$ be the two largest distances. Suppose the diameter graph has
vertex-cover number exactly two, and choose a cover $\{a,c\}$. Put


$$
B=N_D(a)\setminus\{c\},\quad E=N_D(c)\setminus\{a\},\quad
\eta=|B\cap E|.
$$


Then $\eta\le1$ and


$$
m_A(D)+m_A(r)\le n+8+2\eta. \tag{1}
$$


In particular, $r$ is rare if $m_A(D)\ge10$, or if $\eta=0$ and
$m_A(D)\ge8$.

Normalize $r=1$, and let $C=A\setminus\{a,c\}$, of diameter at most one.
Both cover points have diameter neighbors in $C$, since the graph is not
a star. Write $N_a,N_c$ for their unit neighbors in $C$, and put
$h=|N_a\cap N_c|$, $\varepsilon=\mathbf1_{|a-c|=1}$. If $z$ is the
number of globally unit-inactive vertices, then


$$
m_A(1)\le n+2+h+\varepsilon-z. \tag{2}
$$


Indeed, $N_a$ lies on an arc of angular width at most $\pi/3$: its
points are within one of a fixed diameter neighbor of $a$, initially
restricting them to an arc of width less than $2\pi/3$, and its extreme
members are at distance at most one. The
[unit-circle arc lemma](unique_diameter_obstruction.md) makes every
nonextreme member isolated in the unit graph on $C$. The same applies
to $N_c$. If $t=|N_a\cup N_c|$, at least $t-4$ of these points are
isolated on $C$, in addition to globally inactive vertices of $C$.
Apply the diameter bound after removing these isolates and then add
the $t+h+\varepsilon$ unit edges touching the cover. This proves (2)
when both cover vertices are active. An inactive cover vertex removes
two possible extreme positions from this count, so (2) remains valid
with all inactive vertices included in $z$.

We have $h\le1$. Otherwise two common neighbors may be written
$x=(-u,0)$, $y=(u,0)$ and the cover points as
$a=(0,H)$, $c=(0,-H)$, with $H^2=1-u^2$. Every point $w\in A$ lies in
both unit disks about $x,y$, and hence


$$
|w|^2+2u|w_1|\le H^2.
$$


Only $a,c$ lie on the boundary of the enclosing radius-$H$ disk. Thus
$ac$ is the unique diameter, contrary to the cover number.

There is at most one common diameter neighbor. Two such neighbors
$b,d\in C$ would give
$|a-c|^2=4D^2-|b-d|^2>D^2$. Each of $B,E$ lies on a radius-$D$ arc
of angular width less than $\pi/3$. The radius-$D$ arc inequality in
[star_diameter](star_diameter.md) makes every interior member of $B$
unit-inactive in $C$; its only possible unit neighbor in $A$ is $c$.
If $\eta=0$, the same inequality applied to $c$ rules out that neighbor.
If $\eta=1$, the common diameter neighbor is an extreme of the arc
(otherwise its distances to the two extremes give the same contradiction).
The radius-$D$ circle about $a$ meets the unit disk about $c$ in an arc
of angular width less than $\pi$. One extreme of $B$ lies outside that
disk and the other lies inside or on it. Consequently at most one
interior member of $B$ lies on the unit circle about $c$. The identical
argument applies to $E$.

The interiors of the two arcs are disjoint, so, writing
$\delta=\mathbf1_{|a-c|=D}$,


$$
z\ge |B|+|E|-4-2\eta=m_A(D)-\delta-4-2\eta.
$$


Now (2), $h\le1$, and $\delta+\varepsilon\le1$ prove (1).

## A regular even polygon cannot acquire a noncentral point

A regular even $m$-gon, $m\ge4$, admits no new noncentral point whose
distances to all its vertices belong to its chord palette. Its center
is admissible exactly when $6\mid m$.

Normalize its circumradius to one and write $m=2s$. A noncentral point
$p$ has at most two vertices at each prescribed distance, so all $s$
chord lengths must occur exactly twice among its $m$ pinned distances.
Since $\sum_{j=1}^s\cos(\pi j/s)=-1$, averaging squares gives


$$
|p|^2=1+2/s=1+4/m.
$$


There is a vertex within angle $\pi/m$ of the direction $-p$, and its
squared distance from $p$ is at least


$$
1+|p|^2+2|p|\cos(\pi/m)>4,
$$


using $\cos(\pi/m)\ge1-2/m$ and $|p|>1$. This exceeds the polygon
diameter. For the center, admissibility is exactly
$2\sin(\pi j/m)=1$, or $6\mid m$.

Consequently, if $n$ is even, the only diameter pairs are two disjoint
pairs, and every point is second-distance-active, then $R(A)\ge2$.
Under $R(A)=1$, the pair budget gives $q(A)\le n/2-1$. Delete the four
diameter endpoints to obtain $C$, of size $m=n-4$. Every remaining point
has a supporting radius-$r$ disk containing $C$, centered at one of its
$r$-neighbors. Thus $C$ is strictly convex, and


$$
m/2\le q(C)\le q(A)-1\le m/2.
$$


For $n\ge12$, the checked Fishburn equality classification makes $C$
a regular even polygon or a regular odd polygon minus one vertex.
The former admits only its center as a possible added point by the
preceding lemma; the latter admits only its missing vertex by the
[checked palette lemma](unique_diameter_obstruction.md). Neither admits
the four deleted points with the required palette. The smaller even
orders are covered by [small_orders](small_orders.md).

## The square endpoint case

Suppose the only diameter pairs are the diagonals of a unit square,
and the second-largest distance is one. All remaining points lie in


$$
K=\{(x,y):x^2+y^2+|x|+|y|\le1/2\}.
$$


Set $k=(\sqrt3-1)/2$ and $s=2k=\sqrt3-1$. The set $K$ lies in the
radius-$k$ disk, meeting its boundary only at the four junctions
$(\pm k,0),(0,\pm k)$. Let $h$ of these junctions be present and let
$z$ other points lie in the interior of $K$. Since $\operatorname{diam}K<1$,
each nonjunction boundary point has one unit corner neighbor, each
junction has two, and interior points have none. Therefore


$$
m_A(1)=n+h-z.
$$


If this class is rich, $z\le h-1$. Under that richness assumption,
if two opposite junctions are present, their distance $s$ is a second
rare distance. There are at most
two $s$-pairs within $K$, all opposite junction pairs. Each nonjunction
boundary point has at most one corner neighbor at distance $s$, each
junction has none, and each interior point has at most two. Hence


$$
m_A(s)\le2+(n-4-z-h)+2z=n-2-h+z\le n-3.
$$


To check those corner bounds, equal distances to two square corners
put a point on an axis or a diagonal. At its intersections with
$\partial K$, the repeated corner radii are
$1$, $\sqrt{2-\sqrt3}$, or $\sqrt{2-\sqrt2}$, none equal to $s$.
Three equidistant corners force the square center, with radius
$1/\sqrt2\ne s$.

The [endpoint-specific bound](star_diameter.md) shows that two disjoint
diameter pairs and $m_A(r)=n+4$ force their endpoints to form this square.
Then $h-z=4$ forces all four junctions, so the sharp $n+4$ case is
excluded for every order. For even $n$, the same bound also excludes
$m_A(r)=n+3$. If the minimum cross-pair unit degree is one, equality
in the endpoint bound gives full activity, which was excluded above.
If that minimum is two, the endpoints form a square; now $h-z=3$
gives $h\ge3$, hence two opposite junctions and the second rare distance.
The bound excludes the remaining minimum-degree-zero case directly.
Likewise, $m_A(r)=n+2$ is excluded at even order when some endpoint has
no unit neighbor among the other diameter pair: equality in its bound
again gives full activity.

## Remaining cases and checks

Few diameter edges with inactive points remain untreated. At odd order,
even full second-distance activity leaves the convex core one distance
above its classified minimum. No general conclusion for these cases is
asserted.

The author checked the cover count, both arc arguments, the
enclosing-disk test, the even-polygon averaging, the square equations
and corner radii, and the equality applications; the argument is
author-recorded. The classification inputs were checked
in the supplied full Fishburn paper by the earlier referenced proofs.
