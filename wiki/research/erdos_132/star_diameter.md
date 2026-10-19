---
name: research/erdos_132/star_diameter
title: Two rare distances when all diameters share an endpoint
desc: |
  A star diameter graph always gives R at least two; with at least
  three diameter edges the second-largest distance itself is rare.
sources: []
research_state: closed
created: 2026-09-23T02:33:01Z
updated: 2026-09-24T22:12:56Z
---


# Two rare distances when all diameters share an endpoint

***

**Theorem.** Let $A\subset\mathbb R^2$, $|A|=n\ge5$. If every
diameter pair contains one common point, then $R(A)\ge2$.
If there are at least three diameter pairs, the second-largest
distance itself has multiplicity at most $n$.

This extends the [unique-diameter theorem](unique_diameter_obstruction.md).
It does not settle configurations whose diameter graph has vertex-cover
number at least two, or the unrestricted growth question.

## The sharp bound and its equality case

Normalize the second-largest distance to one. Let $a$ be the common
diameter endpoint, let $B$ be its diameter neighbors, and write
$D>1$ for the diameter. Every pair in $A\setminus\{a\}$ has length
at most one.

Let $d$ be the unit degree of $a$. If $d\le1$, deleting $a$ and
using the diameter bound gives $m_A(1)\le n-1+d\le n$.
Otherwise, fix $b\in B$. After putting $a=0$ and $b=(D,0)$,
each unit neighbor $(\cos\theta,\sin\theta)$ of $a$ satisfies
$\cos\theta\ge D/2$. The neighbors therefore lie in an arc of
width less than $2\pi/3$. Their extreme members $u,v$ are at
distance at most one, so their angular separation is at most
$\pi/3$.

Let $L$ be the $d-2$ neighbors strictly between $u,v$. The
[unit-circle arc lemma](unique_diameter_obstruction.md) shows that
each $w\in L$ has unit degree exactly one: for every $x\ne a$,
both $|x-u|,|x-v|\le1$, and consequently $|x-w|<1$.
Deleting $a\cup L$ removes exactly $d$ unit edges and leaves
$n-d+1$ points of diameter at most one. Hence

$$m_A(1)\le n+1. \tag{1}$$

Equality implies that the remaining set has as many diameter-one
edges as vertices. No remaining vertex is isolated in that graph,
since deleting an isolate would violate the diameter bound. The
deleted points are also unit-active. Thus equality in (1) makes
**every point of $A$ unit-active**.

## Three diameter neighbors make the second distance rare

All mutual distances in $B$ are at most one. Put
$\alpha=2\arcsin(1/(2D))<\pi/3$. Relative to one member of $B$,
all arguments lie in $[-\alpha,\alpha]$. Their extreme difference
is less than $\pi$; the distance condition on these extremes then
makes that difference at most $\alpha$. Thus $B$ lies on a minor
arc of its radius-$D$ circle.

If $|B|\ge3$, choose $b$ strictly between its extremes $b_-,b_+$.
With $a=0$, write

$$b=\lambda b_-+\mu b_+,\qquad
\lambda,\mu>0,\quad s=\lambda+\mu>1.$$

For every $y\ne a$, the bounds $|y-b_-|,|y-b_+|\le1$ give

$$|y-b|^2\le1-(s-1)(|y|^2+D^2-1)<1.$$

The remaining point $a$ is at distance $D$ from $b$. Hence $b$
is unit-inactive. Equality in (1) is impossible, proving
$m_A(1)\le n$ whenever $|B|\ge3$.

## Exactly two diameter neighbors

The case $|B|=1$ is the checked unique-diameter theorem. Suppose
$B=\{b,c\}$ and, for contradiction, $R(A)=1$. Then (1) forces
$m_A(1)=n+1$, and all points are unit-active.
The diameter has multiplicity two, so the pair budget gives

$$\binom n2\ge2+(q(A)-1)(n+1),$$

and therefore

$$q(A)\le
\begin{cases}
(n-1)/2,&n\text{ odd},\\
n/2-1,&n\text{ even}.
\end{cases} \tag{2}$$

Put $C=A\setminus\{a,b,c\}$ and $m=n-3$. For $x\in C$, choose
a unit neighbor $y\in A$. The unit disk centered at $y$ contains
all of $C$, because both endpoints of every exceptional pair
belong to $\{a,b,c\}$. Its tangent at $x$ supports $C$ uniquely.
Thus $C$ is strictly convex. Altman's lower bound, deletion of
the diameter, and (2) imply

$$\lfloor m/2\rfloor\le q(C)\le q(A)-1
\le\lfloor m/2\rfloor. \tag{3}$$

All inequalities are equalities, so the palette of $A$ is exactly
the palette of $C$ together with $D$.

Orders $5\le n\le10$ are [already proved](small_orders.md). For $n\ge11$ we have
$m\ge8$, and the checked Altman--Fishburn classifications in the supplied
[full paper](../../../library/distance_problems/fishburn_1995_convex_polygons_few_intervertex_distances/_index.md)
give three possibilities: $C$ is regular odd, regular even, or a regular odd
polygon with one vertex deleted.

A regular odd polygon admits no new point whose distances to
its vertices all lie in its chord palette. A noncentral point
has at most two neighbors at each prescribed distance, which
is insufficient; its center would create the circumradius,
which is not an odd regular polygon's chord. A regular odd
polygon with one vertex deleted admits only that missing vertex.
The reflection-and-cosine proof of this latter assertion is in
[the unique-diameter argument](unique_diameter_obstruction.md).
Either alternative contradicts the three distinct added points
$a,b,c$ and palette equality in (3).

If $C$ is regular even, its polygon diameter is one by (3).
It supplies $m/2$ unit pairs. Each added point contributes at
most two unit pairs to $C$; a circumcenter contributes none.
Of the three added--added pairs, $ab,ac$ have length $D$, so
only $bc$ can be unit. Consequently

$$m_A(1)\le\frac{n-3}{2}+6+1
=\frac{n+11}{2}\le n,$$

contradicting $m_A(1)=n+1$. This proves the theorem.

The author checked the short-arc deletion, the strict radius-$D$ inequality, the
parity in (2)--(3), and all classification and multiplicity steps; the argument
is author-recorded. In particular the even-order bound in (2) follows directly
from counting; no circular use of the unique-diameter theorem is involved.

## A checked bound for two disjoint diameter pairs

Suppose instead that the only diameter pairs are disjoint $ab,cd$.
For a diameter endpoint $v$, let $k_v\in\{0,1,2\}$ count its unit
neighbors among the other diameter pair. Then

$$m_A(1)\le n+2+\min_v k_v\le n+4. \tag{4}$$

Here are the details beyond the star proof. For an endpoint $a$
with unit degree $d_a\ge2$, its unit neighbors again lie in an
arc of width less than $120$ degrees. Neither $c$ nor $d$ can
be an interior member of this arc: if both are neighbors, their
separation exceeds $60$ degrees and they must be the two extremes;
if only one is a neighbor, the unit-circle arc lemma applied to
its diameter partner rules out an interior position.

Let $L$ be the interior unit neighbors. Each can have unit
neighbors only among $a,c,d$. An extra edge to $c$ requires $d$
to be an extreme neighbor, and conversely. Each of $c,d$ supplies
at most one extra edge: the two intersections of its unit circle
with the circle about $a$ have angular separation at least $120$
degrees, since its distance from $a$ is at most one. Thus at most
$k_a$ extra edges are incident with $L$.

Deleting $a\cup L$ leaves $n-d_a+1$ points with unique diameter
$cd$. Applying the sharp unique-diameter bound gives

$$m_A(1)\le d_a+k_a+(n-d_a+1)+1=n+2+k_a.$$

If $d_a\le1$, simply deleting $a$ gives the stronger bound
$m_A(1)\le n+1$. This proves (4). Equality in an endpoint-specific
bound makes every point unit-active. In particular, $m_A(1)=n+4$
forces all four cross-sides to be unit, so the four diameter
endpoints form a unit-side square.

The bound alone does not give a second rare distance. It is sharp:
take a unit square and the four inward intersections of unit
circles centered at its adjacent vertices. The only diameter
pairs are the square diagonals and there are twelve unit pairs
on eight points. This is not an Erdős-132 counterexample.
