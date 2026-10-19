---
name: research/erdos_132/constant_width
title: All distances are rare on a constant-width boundary
desc: |
  Gives a geometric all-rarity criterion and its consequence for sets in
  which every point is incident with a diameter pair.
sources: []
research_state: closed
created: 2026-09-22T23:15:00Z
updated: 2026-09-24T22:12:56Z
---


# All distances are rare on a constant-width boundary

***

This is a restricted geometric criterion, not a proof of either unrestricted
assertion of [Problem 132](../../problems/distance_problems/E0132/_index.md).

## Boundary theorem

**Theorem.** If an $n$-point set lies on the boundary of a planar
convex body of constant width, then every occurring distance has
at most $n$ unordered occurrences. Consequently

$$R(A)=q(A)\ge\lfloor n/2\rfloor.$$

Let the body $K$ have width $D>0$. It has diameter $D$: project any
chord onto its own direction for the upper bound, and use opposite
support points for the lower bound. If $q$ has unit outward
supporting normal $\nu$, an opposite support point $q'$ satisfies

$$ (q-q')\cdot\nu=D,\qquad |q-q'|\le D,$$

so $q'=q-D\nu$. Every support face is therefore a singleton
(fixing $q'$ uniquely fixes $q$), and $K$ is strictly convex.

Fix $p\in\partial K$. We show that each circle centered at $p$
with radius $0<r<D$ meets $\partial K$ in exactly two points.
Suppose $q\ne p$ is a local extremum of distance from $p$ along
the boundary. Let $u,v$ be its two one-sided unit tangent
directions pointing away from $q$, and put $w=p-q$.

If the tangent cone has angle less than $\pi$, strict convexity
puts $w$ strictly inside it, so $w=a u+b v$ with $a,b>0$.
At a local minimum, one-sided differentiation gives
$w\cdot u,w\cdot v\le0$, contradicting

$$0<|w|^2=a\,w\cdot u+b\,w\cdot v.$$

At a local maximum the inequalities reverse, making
$\nu=-w/|w|$ an outward normal. If the tangent-cone angle is
$\pi$, then $u=-v$, and either type of extremum forces
$w\cdot u=0$; since $p$ is inside the supporting half-plane,
$\nu=-w/|w|$ is again outward. These one-sided tangents exist for
the boundary of every planar convex body; no smoothness is used.

Thus at any nonzero local extremum, both
$p=q-r\nu$ and $q-D\nu$ lie on the boundary. Strict convexity
excludes $0<r<D$, so the extremum has value $D$.
Parametrize the boundary from $p$ back to $p$. Its $D$-level set
is an interval: a gap would contain a positive local minimum
below $D$. Before this interval the distance is strictly
increasing, and afterward it is strictly decreasing; otherwise
there would again be a nonzero local extremum below $D$.
This proves the two-intersection assertion.

Every distance $r<D$ consequently gives a graph of maximum
degree two on $A$, hence at most $n$ unordered edges. If $D$
occurs, apply the planar diameter theorem. This proves all-rarity.
Finally $\binom n2\le nq(A)$ gives
$q(A)\ge\lceil(n-1)/2\rceil=\lfloor n/2\rfloor$.

## Diameter-active points

**Corollary.** Let $S$ consist of the points of $A$ incident with
a pair attaining its diameter $D$. Every distance $r<D$ has
maximum degree at most two on $S$. If $S=A$, all distances of
$A$ are rare.

Here is a self-contained proof of the completion fact needed
for the corollary. Choose, by maximality under inclusion, a
diameter-$D$ set $K$ containing $A$. The union of a chain of
admissible sets remains admissible, so Zorn's lemma applies.
Closure and convex hull do not increase diameter; hence $K$
is compact and convex. It has interior: a segment or point
can be enlarged without increasing its positive diameter.
Maximality also gives

$$K=\bigcap_{x\in K}\overline B(x,D). \tag{1}$$

At $q\in\partial K$, let

$$C_q=\{q-x:x\in K,\ |q-x|=D\}.$$

It is nonempty by compactness and (1). Its vectors have length
$D$ and pairwise angles at most $\pi/3$, because $|x-y|\le D$.
Every outward supporting normal $\nu$ at $q$ belongs to their
positive cone. Otherwise separation supplies $v$ with
$\nu\cdot v>0$ and $a\cdot v\le0$ for all $a\in C_q$.
Perturb $v$ slightly toward an interior point of $K$ to make all
the latter inequalities strictly negative. Compactness then
shows that $q+tv$ belongs to every disk in (1) for sufficiently
small $t>0$: nearly active disks have negative first derivative,
and the remaining disks have uniform slack. This contradicts
the supporting inequality in direction $\nu$.

Normalize $\nu$ to length one. In the plane it lies between
two extreme active normals $q-x,q-y$. Their angle is at most
$\pi/3$. The point $q-D\nu$ lies on the short radius-$D$ arc
from $x$ to $y$ centered at $q$. For every $z\in K$, both
$|z-x|$ and $|z-y|$ are at most $D$. The
[short-circle-arc lemma](unique_diameter_obstruction.md) gives
$|z-(q-D\nu)|\le D$. By (1), $q-D\nu\in K$.
The width in direction $\nu$ is therefore $D$; the diameter
bound supplies the reverse inequality. Thus $K$ has constant width.

Every diameter-active point lies on $\partial K$: an interior
point at distance $D$ from another point could be moved slightly
farther away while remaining in $K$. The boundary theorem now
proves the corollary.

## Scope and checks

The argument was checked for nonsmooth boundaries, the possible
diametral arc, and unordered multiplicities. The maximal-set
completion argument was also checked by the author and is
author-recorded. It gives no bound for distance edges touching the points
outside $S$. Bounded rarity has not been shown to force $S=A$,
or even all but a bounded number of points into $S$.
