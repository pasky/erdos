---
name: research/erdos_132/nonlinear_cluster_limits
title: Nonlinear analytic doubling and tripling increase rarity
desc: |
  Two collapsing analytic clusters of two or three points have at least
  their size in cross distances, removing generic-scale exceptions for these sizes.
sources: []
research_state: closed
created: 2026-09-23T05:12:01Z
updated: 2026-10-14T00:26:52Z
---


# Nonlinear analytic doubling and tripling increase rarity

***

**Subsequent extension:** [four_point_collisions](four_point_collisions.md)
proves the same cross-distance bound and rarity increment for $b=4$.
The arguments below retain their original $b=2,3$ scope; the four-point gap is
closed by that separate proof. General $b$ and
an arbitrary-configuration reduction remain unresolved.

This approach permits exact distance coincidences throughout a nonlinear
analytic deformation, unlike
[generic cluster replacement](generic_cluster_replacement.md). The result is
proved only for cluster sizes two and three. It does not resolve either
unrestricted assertion of
[Problem 132](../../problems/distance_problems/E0132/_index.md).

## Two separated collision limits

Let $b\in\{2,3\}$. Suppose the coordinates of

$$X(t)=\{X_1(t),\ldots,X_b(t)\},\qquad
Y(t)=\{Y_1(t),\ldots,Y_b(t)\}$$

are real-analytic at $t=0$. Assume the points within each set are
distinct for all sufficiently small $t>0$, and

$$X_i(t)\longrightarrow p,\qquad Y_j(t)\longrightarrow q,
\qquad p\ne q.$$

Then, for all sufficiently small $t>0$, there are at least $b$
distinct distances between $X(t)$ and $Y(t)$.

Analyticity is used at the endpoint $0$, not merely on a punctured
interval. A nonzero analytic germ has a first nonzero Taylor coefficient;
thus its sign is fixed near zero. In particular, the equality pattern
of the finitely many squared cross-distances is fixed for small positive
$t$. Having too few values at arbitrarily small parameters would give
the same number of analytic distance germs.

### Two-point clusters

If all four cross-distances were equal, the two $Y$ points would be the
two intersections of equal-radius circles centered at the $X$ points.
Their midpoint would equal the midpoint of the $X$ points. Passing to
the limit would give $q=p$, a contradiction.

### Three-point clusters

After a fixed similarity, take $p=(0,0)$ and $q=(d,0)$ with $d>0$.
Suppose there are only two squared cross-distance germs $a(t)<b(t)$.
One value alone is impossible, since three distinct points cannot lie
on two distinct circles of the same radius.

Call a pair within one cluster **flat** if its coordinate difference
satisfies $\Delta x=o(\Delta y)$. If a pair is not flat, analyticity
gives $\Delta y=O(\Delta x)$ and $\Delta x\not\equiv0$. For a nonflat
pair $X_i,X_k$, its squared-distance row difference is

$$|X_i-Y_j|^2-|X_k-Y_j|^2
=-2d\,\Delta x+o(\Delta x), \tag{1}$$

uniformly over the three columns. Indeed, expand the difference as
$\Delta x(x_i+x_k-2x(Y_j))+
\Delta y(y_i+y_k-2y(Y_j))$ and use the collision limits.
Thus the two rows are strictly pointwise ordered for small $t$.
With only the values $a,b$, one row must be constantly $a$ and the
other constantly $b$. All three $Y$ points would lie on the intersection
of two distinct circles, which has at most two points. This is impossible.
The same argument for columns shows that every pair in either cluster
is flat.

Their vertical coordinate germs are consequently distinct. Order both
clusters increasingly by those coordinates, an order fixed for small
$t>0$, and set $D_{ij}=|X_i-Y_j|^2$. For $i<k$, $j<\ell$,

$$D_{ij}+D_{k\ell}-D_{i\ell}-D_{kj}
=-2(X_i-X_k)\cdot(Y_j-Y_\ell)<0. \tag{2}$$

The vertical product is positive and dominates the horizontal product.
Thus $D$ is strictly Monge. For either adjacent column pair, its three
row increments strictly decrease by (2). The possible increments are
only $-(b-a),0,b-a$, so they must occur in the order
$b-a,0,-(b-a)$. The first row therefore increases by $b-a$ across
each of its two column steps. That requires three values, contradicting
the assumed two-value palette. This proves the theorem.

## Consequence for balanced collision families

Let $P$ be any $N$-point planar set, $N\ge2$, and let $A(t)$ consist
of $b$ distinct analytic point curves converging to each point of $P$,
where $b=2$ or $b=3$. Then $|A(t)|=n=Nb$ for sufficiently small $t>0$,
and

$$R(A(t))\ge R(P)+1. \tag{3}$$

No generic choice of a scale parameter is required, and the branch
shapes need not be constant or congruent.

To prove (3), fix a rare base distance $r$, with $m_P(r)\le N$.
All pairs between its corresponding clusters form one limiting-distance
group with exactly $b^2m_P(r)\le b^2N=bn$ unordered pairs. This
group has at least $b$ actual distance classes by the preceding theorem,
applied to any one of its cluster pairs. Hence at least one of these
classes has at most $n$ pairs. Groups with different positive limiting
distances do not merge for sufficiently small $t$, and none merges
with an internal cluster distance, which tends to zero. Each rare base
distance therefore supplies a distinct globally rare class.

The largest internal cluster distance supplies one more. It occurs only
in clusters attaining that internal diameter, and in each such cluster
it has at most $b$ pairs by the planar diameter bound. Its total
multiplicity is at most $Nb=n$. This proves (3), with the full-set
threshold throughout.

## A sharp example excluding a pinned-distance shortcut

The three-point lower bound cannot be strengthened to the assertion
that some point sees three different cross-distances. Put
$s=\sqrt{1+3t^2}$ and take

$$X(t)=\{(0,-t),(1-s,0),(0,t)\},$$
$$Y(t)=\{(1,-t),(s,0),(1,t)\}.$$

These converge to $(0,0)$ and $(1,0)$, respectively. Their squared
cross-distance matrix is

$$\begin{pmatrix}
1&1+4t^2&1+4t^2\\
1+4t^2&(2s-1)^2&1+4t^2\\
1+4t^2&1+4t^2&1
\end{pmatrix}.$$

For $t>0$ its three displayed values are distinct: the middle diagonal
exceeds $1+4t^2$ because $1+2t^2>\sqrt{1+3t^2}$. Every row and
column nevertheless uses only two values. Thus a fully distinct pinned
spectrum is not available even in this collision setting.

## Precise gap for larger clusters

The analogous assertion for arbitrary fixed $b$ was not proved or
disproved. With three or more palette values, pointwise ordered rows
need not be constant, so the two-circle argument in (1) no longer
applies. The initial four-point attempt stopped at this obstacle, but
the subsequent [four-point proof](four_point_collisions.md) resolves it
by reflection pairs and a three-value Monge argument. The remaining
cluster-size question concerns $b\ge5$.

Even when every pair is flat, the argument would need a general
distinct-entry bound for strictly Monge matrices. The proposed bound
of at least $b$ values in a $b\times b$ matrix is not established here.
The weaker proved estimate is

$$b\le k(k-1)+1$$

when there are $k$ values: differences between two fixed rows strictly
increase across the columns and lie in a difference set of size at
most $k(k-1)+1$.

Replacing the strict Monge inequalities by their ordinal consequence
is insufficient. The matrix

$$\begin{pmatrix}0&0&1\\1&0&1\\1&0&0\end{pmatrix}$$

has two values but satisfies
$\max(M_{i\ell},M_{kj})>\min(M_{ij},M_{k\ell})$
for every $i<k$, $j<\ell$: the maximum on the left is one and the
minimum on the right is zero in every case.

First nonzero Taylor coefficients alone also lose information. A
parabolic coefficient matrix $a_i+b_j-2u_i v_j$ can have $m^3$ distinct
row parameter pairs and $m^3$ distinct column parameter pairs, but only
$O(m^2)$ values: take $a_i,b_j\in\{1,\ldots,m^2\}$ and
$u_i,v_j\in\{1,\ldots,m\}$ independently. Higher-order Euclidean
terms must enter any argument that handles these repeated transverse
coordinates. This example concerns coefficient matrices, not exact
planar cross-distances.

The author checked the two- and three-point arguments, the full-set
pair budget in (3), and the exact sharp example; they are
author-recorded. The general collision
problem and its matrix reductions remain provisional directions.
No reduction of arbitrary planar configurations to such analytic
collision families has been established.

## An exact monic-quadratic model for the remaining cluster question

Choose distinct real numbers $u_1,\ldots,u_b$ and distinct real pairs
$(v_j,\beta_j)$, and set

$$X_i(t)=(0,tu_i),\qquad
Y_j(t)=\left(\sqrt{1+t^2(\beta_j-v_j^2)},\,tv_j\right).$$

For sufficiently small $t$, the positive square root is analytic,
all branches are distinct within their clusters, and the two limits
are $(0,0)$ and $(1,0)$. Direct expansion gives the exact identity

$$|X_i(t)-Y_j(t)|^2
=1+t^2\bigl(u_i^2-2u_iv_j+\beta_j\bigr).$$

Consequently, $b$ distinct monic quadratic polynomials whose collective
values on a $b$-element real set number fewer than $b$ would disprove
the proposed general cluster theorem. No such polynomials have been
found, and no theorem excluding them has been established here. This
is a concrete exact subproblem, not an equivalent reformulation of all
analytic cluster families or a reduction of arbitrary planar sets.

A per-class forest argument also fails. Take

$$X_1=(0,-t),\quad X_2=(0,0),\quad X_3=(0,t),$$
$$Y_1=(\sqrt{1-t^2/4},-t/2),\quad
Y_2=(\sqrt{1-t^2/4},t/2),\quad Y_3=(\sqrt{1-t^2},0).$$

Their squared cross-distance matrix is

$$\begin{pmatrix}
1&1+2t^2&1\\
1&1&1-t^2\\
1+2t^2&1&1
\end{pmatrix}.$$

The unit-distance class is a six-cycle, although both clusters shrink
to distinct points. This disproves acyclicity of individual cross classes,
not the already proved three-cluster bound or the proposed general bound.
The author checked both displayed identities and branch distinctness;
they are author-recorded.
The general strict-Monge palette bound and the nonflat-pair analysis for
$b\ge5$ remain unresolved. No computation from this continuation is
being promoted to an all-size Monge theorem.
