---
name: research/erdos_132/remote_anchors
title: Proximal short-edge anchors and the remote-anchor obstruction
desc: |
  The short-edge inverse extends to bounded-radius neighborhoods of convex
  subsets; a remote grid-and-parabola model defeats geometry-only unpinning.
sources: []
research_state: closed
created: 2026-09-23T04:04:53Z
updated: 2026-09-24T22:12:56Z
---


# Proximal short-edge anchors and the remote-anchor obstruction

***

The [short-edge inverse](short_incident_inverse.md) assumes linearly many
edges of bounded smallest-distance rank touch a convex subset. The first
result weakens incidence to bounded-distance proximity. The construction
then explains why dropping that proximity cannot be justified by annular
geometry alone.

## A neighborhood version of the inverse

**Theorem.** Fix $B,\alpha,L>0$ and an integer $s\ge1$. Suppose $A$
has $n$ points, $q(A)\le Bn$, and at most $s-1$ distances smaller than
an occurring $r$. Let $C_0\subseteq A$ be strictly convex. If at least
$\alpha n$ unordered $r$-edges have an endpoint at distance at most
$Lr$ from some point of $C_0$, then, for sufficiently large $n$, a
circle contains $cn$ points of $A$, where $c>0$ depends only on the
fixed parameters.

Orient each counted edge with one close endpoint $p$ first and assign
it a point $c(p)\in C_0$ with $|p-c(p)|\le Lr$. A radius-$Lr$ disk
contains at most

$$K=2s^2(\lceil6L\rceil+2)^2$$

points of $A$. To see this, cover it with at most
$(\lceil6L\rceil+2)^2$ squares of side $r/3$. Each square has diameter
less than $r$ and thus at most $s-1$ distance values. Two anchors and
circle intersections bound its cardinality by
$2(s-1)^2+2\le2s^2$ (a square with fewer than two points is immediate).
The fixed-short-rank degree bound is $6s$, so each $c\in C_0$ receives
at most $6sK$ ordered anchors.

Partition $C_0$ into $J\le12$ narrow convex chains, as in the original
inverse proof. One chain $C$, of size $m$, receives
$E\ge\alpha n/J$ anchors and hence has
$m\ge E/(6sK)$. In particular $m=\Omega(n)$ and $q(A)=O(m)$.

The original chain lemma bounds the number of positive pinned distances, counted
with their endpoints, from a chain vertex in any interval of length $r$ by
$M=8(2s-1)$. If $p$ is assigned to $c\in C$ and $|p-x|$ lies in one such
interval, then $|c-x|$ lies in an interval of length $(1+2L)r$. Thus the
corresponding bound for the possibly off-chain anchor $p$ is

$$M'=(\lceil2L\rceil+2)M+1,$$

where the extra one allows $x=c$. Replace $M$ by $M'$ in the
overloaded-bin proof. A retained apex $x\in C$ has both anchor
distances in good neighboring bins, because the anchor edge has length
$r$. The same linear triangle-type count supplies linearly many rich
direct motions on $C$, and hence a positive circular fraction.
No other step of that proof requires the anchor endpoint to lie on $C$.

Consequently, in a bounded-rarity sequence, for every fixed $L$ and
fixed short rank, only $o(n)$ edges of that rank can have an endpoint
within $Lr$ of any convex subset, uniformly over the subset. The
neighborhood is of its vertices, not of the entire filled convex hull.

## Remote anchors can have arbitrarily crowded annular bins

Let even $t\ge6$ tend to infinity, put $k=t^2/2$ and
$H=t^{10}+1/2$, and take

$$P=\{0,\ldots,t-1\}^2,\qquad
C=\{c_i=(i,H-i^2/(2H)):1\le i\le k\}.$$

Add $a=(-2H,-2H)$ and $b=(2H,-2H)$, and put
$A=P\cup C\cup\{a,b\}$. The strictly concave parabola chain,
together with the two lower corners, gives a strictly convex subset
$C_0=C\cup\{a,b\}$ containing $P$ in its interior. Its consecutive
upper-chain slopes strictly decrease; the two joining sides have slopes
respectively greater and smaller than every chain slope. These also
show directly that the grid lies below the upper boundary and above
the lower side.

The minimum distance is one and has precisely the $2t(t-1)$ horizontal
and vertical grid pairs. Chain pairs have distance strictly greater
than one, and all other pairs outside the grid are much longer. Since
$n=3t^2/2+2$, this minimum class is rich. It supplies linearly many
translated anchors in each coordinate direction.

Nevertheless, for every $p=(u,v)\in P$, all $k$ chain vertices lie
in one standard unit annular bin about $p$. Indeed,

$$|p-c_i|^2-(H-v)^2
=u^2-2ui+vi^2/H+i^4/(4H^2).$$

Its absolute value is less than $4t^3$, while $H-v>H/2$, so

$$\bigl||p-c_i|-(H-v)\bigr|<8t^3/H<1/4.$$

Since $H-v$ is a half-integer, every $|p-c_i|$ belongs to
$[\lfloor H\rfloor-v,\lfloor H\rfloor-v+1)$.

No circle contains more than $2t+6=o(n)$ points of $A$: it meets each
of the $t$ grid columns at most twice, the parabola at most four times
(substitution gives a polynomial of degree four with nonzero leading
coefficient), and contains at most the two added corners.

This is **not** an obstruction satisfying the small-palette hypothesis.
In fact all distances within $C$ are distinct, since

$$|c_i-c_j|^2=(i-j)^2\left(1+\frac{(i+j)^2}{4H^2}\right).$$

Different positive values of $|i-j|$ give disjoint intervals: the
correction to the integer square is less than $k^4/H^2<1$.
For a fixed difference, the positive sum $i+j$ distinguishes the pairs.
Thus $q(A)\ge\binom{k}{2}$ is quadratic.

The author checked the neighborhood packing and transfer of the triangle proof,
and the exact parabola formulas, convexity, separation, and pair counts; the
arguments are author-recorded. Remote anchors cannot be controlled by short
rank, richness, translations, or annular geometry alone; a successful extension
there must use the small global palette. No such extension is proved.
