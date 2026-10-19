---
name: research/erdos_132/short_incident_inverse
title: Short-edge incidence inverse and convex rarity growth
desc: |
  A bin-to-triangle argument proves rarity divergence for convex sets
  and fixed convex covers; arbitrary sets retain an interior-support gap.
sources: []
research_state: closed
created: 2026-09-23T03:11:32Z
updated: 2026-09-24T22:12:56Z
---


# Short-edge incidence inverse and convex rarity growth

***

This is a proved partial result for Erdős problem 132. It proves divergence
of rarity for sets in strictly convex position, but does not settle the
unrestricted problem. The external structural input is the already checked
convex rich-motion criterion recalled below.

Write $q(A)$ for the number of distinct positive distances of a finite planar
set $A$. Distance multiplicities count unordered pairs. Write $R(A)$ for the
number of occurring distances of multiplicity at most $|A|$.

**Quantitative strengthening.** The
[anchor-multiplicity argument](quantitative_short_incidence.md) gives
$R(A)+1\gg n^{1/64}/[L^{7/8}(\log(2n))^{1/8}]$ for a cover by
$L$ convex subsets, and extends divergence to
$L=o(n^{1/56}/(\log n)^{1/7})$ with $o(n)$ uncovered points.
The qualitative proof below remains valid.

## External input: rich motions on a convex set

For every $a,b>0$, there are $c>0$ and $m_0$ such that the following holds.
If $C$ is a strictly convex $m$-point set, $m\ge m_0$, and at least $a m$
distinct direct Euclidean isometries $g$ satisfy


$$
|C\cap gC|\ge b m,
$$


then one circle contains at least $c m$ points of $C$.

This is the convex consequence of Mansfield--Passant, *A Structural Theorem
for Sets with Few Triangles*, Combinatorica 44 (2024), Theorem 1.6:

[full primary paper](https://link.springer.com/article/10.1007/s00493-023-00066-z)

The theorem gives either a positive circular fraction or additive energy
of cubic order. The latter is impossible for a strictly convex set:
every nonzero vector has at most two ordered representations as a
difference of its vertices, so its additive energy is at most $3m^2-2m$.
The theorem and this consequence have already been checked in
[motion_incidence](motion_incidence.md); the author has also checked the
primary theorem for the present application.

## 1. A narrow-chain triangle lemma

**Lemma.** Fix $B,\alpha>0$ and an integer $s\ge 1$. There are $c>0$ and
$m_0$, depending only on these parameters, with the following property.
Let $A$ be a planar set and let
$C=(p_0,\ldots,p_{m-1})$ be a strictly convex ordered chain contained in $A$,
where all directions of its consecutive edges lie in one interval of
width at most $\pi/3$. Suppose that:

1. $q(A)\le B m$;
2. at most $s-1$ distances of $C$ are strictly smaller than a positive
   number $r$;
3. there is a family $F$ of at least $\alpha m$ distinct ordered anchors
   $(p,q)$, where $p\in C$, $q\in A$, and $|p-q|=r$.

Then a circle contains at least $c m$ points of $C$.

No upper bound on the size of $F$, no hypothesis that $q$ belongs to $C$,
and no equilateral-chain hypothesis is needed.

### Pinned occupancy in intervals of width r

For a fixed $p_i$, its distances to the subsequent chain points strictly
increase. More precisely, if $i<j<k$,


$$
|p_k-p_i|-|p_j-p_i|
\ge \tfrac12\sum_{t=j}^{k-1}|p_{t+1}-p_t|. \tag{1}
$$


Indeed, every partial chord and the next edge lie in the same direction
sector of width at most $\pi/3$. The supporting-line inequality for the
Euclidean norm therefore makes each increment of distance at least half
the added edge length. The same assertion holds when moving backwards
from $p_i$ along the chain.

Consequently, points on one side of $p_i$ whose distances from $p_i$ belong
to a fixed half-open interval of length $r$ occupy a subchain of arc length
less than $2r$. Partition its arc-length parameter into four half-open
intervals of length $r/2$. Each part has diameter less than $r$, hence
determines at most $s-1$ distances. Altman's convex distance bound gives
at most $2s-1$ vertices per part. The cases of one or two vertices also
satisfy this conclusion directly. Thus, on both sides together, every
radius interval of length $r$ contains at most


$$
M:=8(2s-1)\le16s \tag{2}
$$


positive pinned distances, counted with their endpoints. It is harmless
to replace $M$ by $20s$ below.

### Discard overloaded bins

Partition the positive real axis into the half-open bins
$[tr,(t+1)r)$, for integers $t\ge 0$. Let $D=D(A)$ and let $q=|D|$.
Choose the fixed integer


$$
T=\lceil 12MB\rceil+1.
$$


A bin is bad if it contains more than $T$ distinct values of $D$.
There are at most $q/T$ bad bins. Enlarge their index set by also taking
both neighboring indices, ignoring negative indices.

For an anchor $(p,q_0)$ in $F$, discard an apex $x\in C$ if $|p-x|$
lies in one of these enlarged bad bins, or if $p,q_0,x$ are not three
noncollinear points. By (2), the first rule removes at most


$$
3M q/T\le m/4
$$


choices. Since $C$ is strictly convex, a line contains at most two of its
points; thus the second rule removes at most two additional choices.
For sufficiently large $m$, at least $m/2$ apex choices remain for every
anchor.

For every retained triangle, both long sides lie in good bins. This needs
no monotonicity about the possibly off-chain point $q_0$: the triangle
inequality gives


$$
\bigl||p-x|-|q_0-x|\bigr|\le r,
$$


so their bin indices differ by at most one.

### Only linearly many retained triangle types

The type of a retained triangle is


$$
\bigl(|p-x|,|q_0-x|,
\operatorname{sgn}\det(q_0-p,x-p)\bigr).
$$


There are at most $q$ choices for the first length. Its bin and its two
neighbors contain at most $3T$ eligible second lengths. The orientation
has two signs. Hence the number of types is at most


$$
6qT\le6BTm. \tag{3}
$$


Put $E=|F|$. There are at least $Em/2$ retained triangles. By
Cauchy--Schwarz, the number of ordered pairs of retained triangles having
the same type is at least


$$
\frac{(Em/2)^2}{6BTm}
=\kappa E^2m,
\qquad \kappa:=\frac1{24BT}. \tag{4}
$$


### Many rich direct motions

For each ordered pair of anchors $(p,q_0)$ and $(p',q_0')$, there is a
unique direct isometry $g$ taking the first ordered pair to the second.
Equal triangle types imply that $g$ takes the first apex to the second:
equal distances to the two anchors and the same orientation determine
the point uniquely. Therefore a fixed ordered pair of anchors contributes
at most


$$
\nu_C(g):=|C\cap gC|
$$


pairs counted in (4).

There are $E^2$ ordered anchor pairs and each has at most $m$ matching
apices. It follows from (4) that at least $kappa E^2/2$ ordered anchor
pairs have


$$
\nu_C(g)\ge\kappa m/2. \tag{5}
$$


A fixed motion occurs for at most $E$ anchor pairs: once the source anchor
is specified, its image anchor is unique. Thus at least


$$
\kappa E/2\ge(\kappa\alpha/2)m
$$


distinct motions satisfy (5). Apply the rich-motion criterion. This proves
the lemma. The identity, if it occurs, contributes only one motion and
can be discarded after slightly reducing the constant.

## 2. Uniform degree bound for a fixed short rank

**Lemma.** If at most $s-1$ distances in a planar set $A$ are smaller than
$r$, every vertex has at most $6s$ neighbors at distance $r$.

Fix the vertex and split its radius-$r$ circle into six half-open angular
arcs of width $\pi/3$. Within one arc, distances from its first occurring
point to all the other occurring points are distinct and strictly smaller
than $r$. Thus the arc contains at most $s$ points. Summing proves the
claim. No convexity of $A$ is needed.

## 3. Incident edges on an arbitrary convex subset

**Theorem.** Fix $B,\alpha>0$ and an integer $s\ge 1$. There are $c>0$ and
$n_0$, depending only on these parameters, such that the following holds.
Suppose $A$ has $n\ge n_0$ points and $q(A)\le Bn$. Let $r$ be an occurring
distance with at most $s-1$ smaller distances in $A$. If a strictly convex
subset $C_0$ is incident with at least $\alpha n$ unordered length-$r$
pairs of $A$, then some circle contains at least $cn$ points of $A$.

To prove this, partition the cyclic order of $C_0$ into at most $J=12$
disjoint consecutive chains whose directed edges lie in sectors of width
at most $\pi/3$ (width $\pi/6$ sectors also suffice). Orient every incident
edge with its first endpoint in $C_0$, using both orientations when both
endpoints belong to $C_0$. Some chain $C$ supports at least
$\alpha n/J$ such ordered anchors. If $m=|C|$, the degree lemma gives


$$
m\ge \alpha n/(6sJ).
$$


Thus $q(A)\le B(6sJ/\alpha)m$, while the number of anchors is at least
$(\alpha/J)m$. Apply the narrow-chain lemma. Its circular fraction of
$C$ is a positive fraction of $A$, with all constants uniform in $A$.

In particular, the separately stated assumption that $C_0$ contains a
positive fraction of $A$ is unnecessary: the incident-edge hypothesis
already forces this by the degree bound.

## 4. Rarity diverges in strictly convex position

**Corollary.** If $A_n$ is any sequence of strictly convex planar sets and
$|A_n|$ tends to infinity, then $R(A_n)$ tends to infinity.

Suppose instead that $R(A)\le K$ along an unbounded sequence. The pair budget
gives $q(A)\le n/2+K$, and therefore $q(A)\le n$ for sufficiently large $n$.
Altman's convex lower bound gives $q(A)\ge floor(n/2)$, so the first $K+1$
positive distances exist for large $n$. At least one of them, say $r_s$
with $s\le K+1$, is rich and hence has more than $n$ unordered pairs.

Apply the incident-edge theorem with $C_0=A$, $B=1$, $\alpha=1$, and $s=K+1$. It
gives a positive circular fraction, with a constant depending only on $K$. The
checked positive-circle theorem in [circle_incidence](circle_incidence.md) then
gives linearly many rare distances in the full set $A$, contradicting
$R(A)\le K$.

## 5. Fixed convex covers

The same conclusion holds for sets that are unions of at most $L$ strictly
convex subsets, for any fixed $L$. Under $R(A)\le K$, choose a rich distance
among the first $K+1$. One covering subset is incident with at least $n/L$
of its edges. The incident-edge theorem and circle theorem again give a
contradiction for sufficiently large $n$.

The conclusion still holds if the convex subsets cover all but $o(n)$
points. The omitted points touch at most $6s\,o(n)=o(n)$ edges of a
fixed-rank class, so a rich class still has a linear number of edges
incident with one covering subset.

In particular, this treats a fixed number of convex layers, including
one- or two-point final layers. Such small layers cannot support the
required linear number of fixed-rank edges by the degree bound. The cover
hypothesis allows overlaps and is stronger than a bounded-layer statement.

## 6. What this gives, and does not give, unrestrictedly

For a hypothetical bounded-rarity sequence of arbitrary planar sets, the
incident-edge theorem and the positive-circle theorem imply the following
uniform restriction: for every fixed $s$, every strictly convex subset is
incident with $o(n)$ edges of the $s$-th smallest distance. The same holds
for the union of any fixed number of smallest-distance classes.

In particular, let $B_s$ be the set of endpoints of a rich class $r_s$.
The degree bound gives $|B_s|>n/(3s)$. Nevertheless, its largest strictly
convex subset has $o(n)$ points: any such subset $C\subseteq B_s$
touches at least $|C|/2$ edges, since each vertex has an incident edge
and an edge accounts for at most two of its vertices. A linear-sized
$C$ would trigger the inverse and contradict bounded rarity. Thus a
linear-sized low-rank support can be convexly diffuse even while the
full set has a linear-sized outer convex layer.

The [proximal-anchor extension](remote_anchors.md) strengthens this
restriction to the fixed-$Lr$ neighborhood of the convex subset's
vertices. It does not cover arbitrary remote interior anchors: the same
note gives an exact annular-occupancy obstruction, whose distance palette
is quadratic rather than linear.

The existing layer reduction supplies a linear-sized convex subset among
the first boundedly many outer layers. It does not guarantee linearly many
fixed-small-rank edges incident with that subset. Thus the new theorem
proves the full convex asymptotic assertion but does not by itself settle
the arbitrary-planar asymptotic assertion or the arbitrary-planar
two-rare-distance assertion.


## Checks and scope

The author checked the pinned monotonicity, half-open-bin endpoints,
the neighboring-bin deletion, ordered triangle and unordered edge
factors, sector selection, and the multiplicity with which one motion
represents anchor pairs, and read the statement and at-least-rich
formulation of the Mansfield--Passant theorem in the full primary
source; the argument is author-recorded.

Neither unrestricted question is resolved. In particular, the general
convex few-distance inverse statement in [motion_incidence](motion_incidence.md)
is not asserted: the new proof needs a fixed short rank with linearly many
incident edges. For a large convex subset of an arbitrary set, those
edges may all lie in the complementary interior set.
