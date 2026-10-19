---
name: research/erdos_132/affine_deformations
title: Linear rarity under equality-preserving affine deformation
desc: |
  A nonsimilarity affine map preserving distance equalities forces
  R at least ceil(n/4); the finite matrix test exposes the restriction.
sources: []
research_state: closed
created: 2026-09-23T00:27:00Z
updated: 2026-09-24T22:12:56Z
---


# Linear rarity under equality-preserving affine deformation

***

This verifies Section 3 and Appendix B of the
[independent input](independent/largest_distance_ranks_and_small_orders.md), and
slightly strengthens its bound. All multiplicities count unordered pairs in the
full $n$-point set. No assertion for arbitrary planar sets follows.

## Equivalent affine and coordinate conditions

For a finite planar set $A$, the following are equivalent:

1. An invertible affine map whose linear part is not a similarity
   preserves every original equality of pair distances.
2. In some orthonormal coordinates, equal-length difference vectors
   have the same absolute horizontal displacement, and hence also
   the same absolute vertical displacement.
3. The matrices $dd^{\mathsf T}-ee^{\mathsf T}$, over all difference
   vectors $d,e$ of equal length in $A$, span a subspace $V$ of
   dimension at most one in the two-dimensional space of traceless
   symmetric $2\times2$ matrices.

For (1) to (2), put $Q=T^{\mathsf T}T$ for the linear part $T$ and
use its orthonormal eigenbasis. Its positive eigenvalues $\lambda,\mu$
are distinct. Equal vectors in length satisfy both

$$d_x^2+d_y^2=e_x^2+e_y^2,\qquad
\lambda d_x^2+\mu d_y^2=\lambda e_x^2+\mu e_y^2,$$

so $d_x^2=e_x^2$. Conversely, (2) permits any positive diagonal
stretching with unequal scale factors. For (1) and (3), equality
preservation is exactly orthogonality of $Q$ to $V$ under the trace
inner product. The traceless part of a nonscalar $Q$ is nonzero.
Conversely a nonzero traceless $S\perp V$ gives a positive definite
nonscalar $Q=tI+S$ for sufficiently large $t$, and $Q=T^{\mathsf T}T$
for an invertible $T$.

No prohibition on mergers of originally unequal classes is needed.

## A linear bound

**Theorem.** Under these equivalent conditions, for $n\ge2$,

$$R(A)\ge\left\lceil\frac n4\right\rceil. \tag{1}$$

In particular $R(A)\ge2$ for every $n\ge5$ in this family.

Work in coordinates from condition (2). Each distance class has fixed
absolute displacement pair $(a,b)$. A vertical class ($a=0$) is a
disjoint union of finite translation paths, so has at most $n-1$ edges.
If all points lie on one vertical line, every class is rare and at
least $n-1$ distances occur, proving (1).

Otherwise let $m=\min x$, $M=\max x$, $W=M-m>0$, and let $c$ points
lie on the middle line $x=(m+M)/2$. A class with $a>W/2$ has maximum
degree at most two: a vertex can have neighbors on at most one of
$x-a,x+a$, and that line allows at most two ordinates. It is rare.

At least $(n-c)/2$ points lie strictly on one side of the middle line.
Join those points to an anchor on the opposite extreme line. All these
edges belong to rare classes with $a>W/2$. At most two have the same
length, since both their absolute displacements are fixed by that
length. This supplies at least $\lceil(n-c)/4\rceil$ rare classes.
If $c\ge1$, distances from a lowest middle-line point to the other
$c-1$ middle-line points give $c-1$ further distinct vertical classes.
They cannot coincide with any class already counted.

For $c=0$ this proves (1). For $c\ge2$,

$$\left\lceil\frac{n-c}{4}\right\rceil+c-1
 =\left\lceil\frac{n+3c-4}{4}\right\rceil
 \ge\left\lceil\frac n4\right\rceil.$$

It remains to handle $c=1$. Every class with $a=W/2$ is also rare in
this case. On the three lines $x=m,(m+M)/2,M$, its graph is a star
with the unique middle point as center, together with isolates.
Every other point can have neighbors on only one other vertical
line, so the remaining graph has maximum degree at most two.
There are no edges between these two parts. Thus the total edge
count is at most $n$. The distance from the unique middle point
to an extreme anchor supplies one such class, distinct from all
strictly long classes. Hence

$$R(A)\ge\left\lceil\frac{n-1}{4}\right\rceil+1
 \ge\left\lceil\frac n4\right\rceil.$$

This completes the proof. The midpoint argument is a checked improvement
over the input's $\lceil(n-1)/4\rceil$ bound. Without it, the long-class
argument requires the strict inequality $a>W/2$; one cannot simply
replace it by $a\ge W/2$ for an arbitrary middle fiber.

The input's separate five-point argument is also valid but unnecessary
for (1). For $a,b>0$, a connected class component is a subgraph of the
integer grid in the basis $(a,b),(a,-b)$, not in the original coordinate
axes. A component of $u$ vertices occupying $r$ rows and $s$ columns
has at most $2u-r-s\le2u-2\sqrt u$ edges. Summing bounds the full
class by $2n-2\sqrt n$, whose floor is five at $n=5$.

## Obstructions and comparison with earlier notes

An equilateral triangle forces $Q$ to be scalar: equality on the
three unit directions $(1,0),(1/2,\sqrt3/2),(-1/2,\sqrt3/2)$ first
forces the off-diagonal entry to vanish and then the diagonals to
agree. A square also forces this, using its side equalities and
then its diagonal equality. Thus this theorem is a restricted
family result, not a general deformation reduction.

The safe direction of transfer was already proved in
[variational_reduction](variational_reduction.md): if distinct points
are deformed while preserving all original equalities, classes can
merge but cannot split, so $R(\text{new})\le R(\text{old})$.
Arbitrary perturbation goes in the wrong direction. A regular hexagon
with its center has multiplicities $(12,6,3)$ and $R=2$; a generic
small perturbation has 21 singleton classes. Those new rare classes
give no lower bound on the original rarity.

Unlike the [line-cover](line_covers.md) and
[dyadic](dyadic_distances.md) criteria, this theorem requires no bound
on covering lines and no arithmetic assumption. Nor does either of
those criteria imply this one: a rational square already fails the
affine test. These are different sufficient conditions, not an
exhaustive list of planar configurations. A hypothetical bounded-$R$
sequence must eventually have $\dim V=2$ by (1), but that supplies
no useful nonlinear deformation or equilibrium-stress signs.

The original argument, the matrix test, and the midpoint sharpening were checked
by the author; the argument is author-recorded. Neither unrestricted assertion
of [Problem 132](../../problems/distance_problems/E0132/_index.md) is settled.
