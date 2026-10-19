---
name: research/erdos_132/motion_incidence
title: What ordinary motion incidences do not detect
desc: |
  A rich-motion inverse criterion isolates the missing moment step;
  ordinary incidences and cubic distance energy alone do not detect rarity.
sources: []
research_state: closed
created: 2026-09-22T21:50:03Z
updated: 2026-10-13T05:28:09Z
---


# What ordinary motion incidences do not detect

***

The attempted motion-space approach gives the following exact
obstructions, not a proof of either assertion of
[Problem 132](../../problems/distance_problems/E0132/_index.md).

## A rich radius can have only ordinary intersections

Let $J(x,y)=(-y,x)$. Fix an occurring radius $r$ and artificial anchors
$a,b$ with $|a-b|=r$, choosing $b-a$ unequal to every oriented
length-$r$ difference of $A$. Only finitely many directions are
excluded. For $p\in A$, define the line in $\mathbb R^2\times\mathbb R$

$$L_{a,p}=\left\{\left(\frac{a+p}{2}
              +\frac t2J(p-a),t\right):t\in\mathbb R\right\},$$

and similarly define $L_{b,q}$ for $q\in A$.

Within either family the lines are pairwise disjoint. An intersection
for distinct $p,p'$ would require

$$p-p'+tJ(p-p')=0,$$

which is impossible over $\mathbb R$. Put $d=b-a$ and $e=q-p$.
A cross-family intersection is equivalent to

$$d+e=tJ(d-e). \tag{1}$$

When $d\ne e$, a real $t$ exists uniquely precisely when
$(d+e)\cdot(d-e)=0$, or $|d|=|e|$. The anchor choice excludes $d=e$
for all pairs at distance $r$. Thus

$$L_{a,p}\cap L_{b,q}\ne\varnothing
\quad\Longleftrightarrow\quad |p-q|=r.$$

There are exactly $2m_A(r)$ intersection points. Each belongs to
exactly two lines, since within each family the lines are disjoint.
Every intersection is therefore ordinary, even for $m_A(r)>n$.

The presence or abundance of ordinary intersections in this
representation does not identify a rare radius. A useful argument
would have to compare the arrangements for different radii, or use
more metric information. No such implication was established.

## Global motion energy loses the leading-order distinction

For the global arrangement $\{L_{a,p}:a,p\in A\}$, an intersection
represents a nontranslation direct isometry mapping at least two
points of $A$ into $A$: the first two coordinates are its rotation
center, and $t=\cot(\theta/2)$ for its nonzero rotation angle $\theta$.
Put $\nu(g)=|A\cap gA|$. Let $\mathcal I$ be the nontranslation direct
isometries with $\nu(g)\ge2$, and $\mathcal T$ the translations with
that property. Counting ordered pairs of congruent unordered segments
and their two endpoint matchings gives

$$\sum_{g\in\mathcal I}
   \binom{\nu(g)}2
=2\sum_r m_A(r)^2
-\sum_{t\in\mathcal T}
   \binom{\nu(t)}2. \tag{2}$$

The translation sum includes the identity. All sums are finite:
matching two distinct source points to two distinct target points
determines a direct isometry uniquely. Formula (2) counts motion
overlaps, not individual distance-class sizes.

If at most $B$ classes are rare, their total multiplicity is at most
$Bn$, and every rich class has multiplicity at least $n+1$. Hence

$$\sum_r m_A(r)^2
 \ge(n+1)\left(\binom n2-Bn\right)
 =\tfrac12n^3-O_B(n^2).$$

But a regular odd $n$-gon has every class rare and energy exactly
$n^2(n-1)/2$. Thus an energy estimate at this leading order cannot
distinguish the hypothesized bounded-rarity spectrum from a spectrum
in which all classes are rare. This does not rule out finer,
distance-labeled incidence information.

## A checked inverse criterion and the missing moment step

The unrestricted attempt tested whether the large convex layer forced
by bounded rarity could be treated using an inverse theorem for rigid
motions. The following conditional implication is valid; its needed
hypothesis has not been deduced from bounded rarity.

**Criterion.** Fix $\alpha,\beta>0$. Let $C$ be a strictly convex
$m$-point set. If at least $\alpha m$ distinct direct rigid motions
$g$ satisfy $|C\cap gC|\ge\beta m$, then, for sufficiently large $m$,
a circle contains $\Omega_{\alpha,\beta}(m)$ points of $C$.

The external input is Mansfield--Passant, *A Structural Theorem for
Sets with Few Triangles*, Combinatorica 44 (2024), Theorem 1.6:
these motion hypotheses force either cubic additive energy or a
positive circular fraction. The full statement and its use of
at-least-rich actions in Lemma 3.1 and Corollary 3.2 were checked.
Their Theorem 1.4 also supplies the circular conclusion for a convex
set with only $O(m^2)$ triangle congruence classes.
[Primary source](https://link.springer.com/article/10.1007/s00493-023-00066-z).

Here is the elementary reason the additive-energy alternative is
impossible in strict convex position. For a nonzero vector $v$, write
$r(v)=\#\{(p,q)\in C^2:p-q=v\}$. Then $r(v)\le2$.
Rotate so $v=(a,0)$ with $a>0$. Write the horizontal sections of
$\operatorname{conv}C$ as $[\ell(y),u(y)]$. A representing pair must
be the two section endpoints, so $u(y)-\ell(y)=a$. Three representing
pairs have three different heights $y_1<y_2<y_3$; otherwise there
would be three collinear vertices. The width function is concave.
Equality with the same value at these three heights forces it to be
constant throughout $[y_1,y_3]$. Since $u$ and $-\ell$ are concave,
they must then both be affine on that interval. The middle pair is
therefore on two polygon sides rather than at vertices, a contradiction.

Consequently the additive energy satisfies

$$E_+(C)=\sum_v r(v)^2
 \le m^2+2\sum_{v\ne0}r(v)=3m^2-2m,$$

excluding a lower bound of order $m^3$ and proving the criterion.
The source theorem is imported; this convex exclusion was checked
by the author and is author-recorded.

### Why the available distance count does not meet the criterion

Put $E_D(C)=\sum_r m_C(r)^2$. If $q(C)\le C_0m$, then

$$E_D(C)\ge\frac{\binom m2^2}{C_0m}=\Omega_{C_0}(m^3).$$

In (2), the translation contribution is at most $m(m-1)$: the
identity contributes $\binom m2$, while
$\sum_{v\ne0}\binom{r(v)}2\le\tfrac12\sum_{v\ne0}r(v)=\binom m2$.
Thus the hypothesis yields a cubic second moment of nontranslation
motion overlaps. It does **not** yet yield linearly many motions
with linearly many overlapping points.

The usual rich-motion estimate
$\#\{g:|C\cap gC|\ge k\}=O(m^3/k^2)$ is also recalled in the
checked source, equation (1). Those numerical bounds alone allow
a cubic second moment to be supported on motions of bounded richness.
This is a failure of that numerical inference, not a constructed
convex configuration. A lower bound of order $m^4$ for triangle
energy, or an $O(m^2)$ bound for triangle congruence classes, would
supply the stronger input. The palette estimate gives only
$O(q(C)^3)=O(m^3)$ possible triples of side lengths.

For a hypothetical bounded-rarity family, the layer theorem supplies
$|C|\ge cn$ and hence $q(C)\le n/2+O(1)=O_c(|C|)$. The criterion
would finish this route if the missing moment step were proved: a
positive circular fraction of $C$ would be one of $A$, contradicting
the [circle-incidence theorem](circle_incidence.md). Neither that
step nor the general convex few-distance inverse statement was
proved or refuted. These are provisional directions, not reductions
whose remaining hypotheses can be omitted.

### A labeled short-edge hypothesis does supply the missing motions

The subsequent [short-edge incidence inverse](short_incident_inverse.md)
proves the needed rich-motion conclusion when a fixed smallest-distance
rank has linearly many edges touching the convex subset. Its overloaded-bin
deletion gives linearly many anchored triangle types with quadratically
many realizations, rather than relying on the unlabeled second moment.
This proves rarity divergence for convex sets and fixed convex covers.
The general $q(C)=O(|C|)$ inverse and the arbitrary-layer application
remain unproved: a large convex layer need not meet the short rich graph.
