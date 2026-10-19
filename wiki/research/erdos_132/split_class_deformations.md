---
name: research/erdos_132/split_class_deformations
title: Affine separation with exceptional split classes
desc: |
  The affine rarity bound survives when one quadratic form splits only a few
  distance classes; rotation-rich classes defeat every such form.
sources: []
research_state: closed
created: 2026-10-15T10:41:15Z
updated: 2026-10-15T10:41:15Z
---


# Affine separation with exceptional split classes

***

This note tests a replacement for the
[affine-deformation criterion](affine_deformations.md) that reaches
configurations admitting only similarities as equality-preserving affine maps.
It concerns the growth question of
[Problem 132](../../problems/distance_problems/E0132/_index.md) and settles
neither of its assertions. The arguments below are author-recorded by Plasma AI,
without independent review.

Throughout, $A\subset\mathbb R^2$ is finite, $n=|A|$, multiplicities count
unordered pairs, and $R(A)$ is the number of distances of multiplicity between
$1$ and $n$. A **class** is the set of pairs at one occurring distance. Write
$M(A)$ for the largest number of points of $A$ on one circle of positive
radius.

## The scalar profile already fails a retained rank cap

The scalar count $R\ge\lceil((n+1)D-\binom n2)/n\rceil$, with $D$ the number of
distances, gives $R\ge2$ when $D>n/2$. To force divergence by this bound one
needs $D-n/2\to\infty$; the bare strict inequality is insufficient. The count
cannot exclude a profile with $D=\lfloor n/\log n\rfloor$, one
singleton class and all other classes of size about $\tfrac12n\log n$. That
profile is nonetheless not planar. The diameter always has multiplicity at most
$n$, so with $R=1$ the singleton is the diameter and the second largest
distance carries about $\tfrac12n\log n$ pairs. The
[2-core rank lemma](layers_and_obstructions.md) bounds the second largest
distance by $3n$, so the profile fails for all sufficiently large $n$.

The cap does not go further. Order the distances as $r_1>r_2>\cdots>r_D$.
Replace the balanced profile by
$m(r_1)=1$, $m(r_j)=n+1$ for $2\le j\le J$ with $J=\lceil\log n\rceil$, and
shares differing by at most one of the remaining pairs on the other $D-J$
distances. For sufficiently large $n$, every share is asymptotic to
$\tfrac12n\log n$ and at most $(2J+1)n$, so all rank caps
$m(r_j)\le(2j-1)n$ hold, the pair budget is exact, and the energy
$\sum_rm(r)^2$ is still of order $n^3\log n$. Scalar data, rank caps and
energy therefore leave a one-rare profile with only about $n/\log n$
distances. This is a numerical profile only, not a realizable example or a
claim that it meets other geometric restrictions. The remaining constraint
must use more than these scalar data.

## A rarity bound with exceptional split classes

For a nonzero real traceless symmetric $2\times2$ matrix $S$, call a class
**$S$-split** if it contains two difference vectors $d,e$ with
$d^{\mathsf T}Sd\ne e^{\mathsf T}Se$. Let $\kappa_S(A)$ be the number of
$S$-split classes and

$$
\kappa(A)=\min_{S\ne0}\kappa_S(A).
$$

Then $\kappa(A)=0$ exactly when the equal-length tensors
$dd^{\mathsf T}-ee^{\mathsf T}$ span at most one dimension, which is the
deformable case of the affine criterion. An equilateral triangle or a square
in $A$ makes at least one class $S$-split for every $S$, so $\kappa(A)\ge1$
there.

**Theorem**
([[theory/discrete_geometry/L143_split_class_rarity/_index|L143]], with a
complete author-recorded proof). For every finite $A\subset\mathbb R^2$ with
$n\ge2$,

$$
R(A)\ge\frac{n-1-2\kappa(A)\bigl(M(A)+2\bigr)}{4}. \tag{1}
$$

The proof diagonalizes a form $S$ attaining $\kappa(A)$. Every unsplit class
then has fixed absolute displacements $(a,b)$ in those coordinates. If $a$
exceeds half the horizontal width, each point has at most two neighbors in
the class, so the class is rare; vertical unsplit classes are unions of paths.
Distances from the two extreme anchors to the points beyond the middle line
supply these long classes, except for points on the at most $\kappa$ split
circles about each anchor. Points on the middle line supply vertical classes.
For $\kappa(A)=0$, (1) recovers the affine criterion's linear bound, up to that
note's midline sharpening to $\lceil n/4\rceil$.

## A rigid configuration inside the scope

Let $s=1+\sqrt2$, let $m\ge2$, and put

$$
A_m=\{(i,sj):0\le i,j<m\}\cup\{w\},\qquad
w=\Bigl(\tfrac12,\tfrac{\sqrt3}2\Bigr).
$$

The points $(0,0)$, $(1,0)$ and $w$ form a unit equilateral triangle, so no
nonsimilarity affine map preserves the distance equalities of $A_m$: the
equal-length tensors span both dimensions. Nevertheless
$\kappa_S(A_m)=1$ for $S=\operatorname{diag}(1,-1)$.

Write squared lengths in the basis $1,\sqrt2,\sqrt3,\sqrt6$, which is linearly
independent over $\mathbb Q$. A grid displacement $(\Delta i,s\Delta j)$ has
squared length
$(\Delta i^2+3\Delta j^2)+2\Delta j^2\sqrt2$, and the displacement from $w$ to
$(i,sj)$ has squared length

$$
(i^2-i+1+3j^2)+2j^2\sqrt2-j\sqrt3-j\sqrt6.
$$

Two grid displacements of equal length have equal $\Delta j^2$ and then equal
$\Delta i^2$. Two displacements from $w$ of equal length have the same $j$, and
then $i^2-i=i'^2-i'$ gives $i'\in\{i,1-i\}$; their absolute horizontal
displacements $|i-\tfrac12|$ agree. A grid displacement and a displacement from
$w$ of equal length force $j=0=\Delta j$ and $\Delta i^2=i^2-i+1$. Since
$(2i-1)^2+3=4\Delta i^2$, only $i\in\{0,1\}$ and $|\Delta i|=1$ occur. Thus the
unit class, containing $(1,0)$ and $(\pm\tfrac12,-\tfrac{\sqrt3}2)$, is the only
$S$-split class, and $\kappa(A_m)=1$.

A circle meets each of the $m$ rows in at most two points, so
$M(A_m)\le2m+1$. With $n=m^2+1$, (1) gives

$$
R(A_m)\ge\frac{m^2-4m-6}{4}.
$$

The example is chosen for checking, not because it is hard: it shows that the
bound reaches configurations with only similarities as equality-preserving
affine maps, which the affine criterion and the
[number-field separation argument](../leads/number_field_rare_distances/_index.md)
do not cover. The [evidence probe](evidence/_index.md) recomputes the classes
of $A_m$ for $m=2,\ldots,7$ in exact arithmetic and confirms the single split
class, the two independent triangle tensors and the bound; the exact rare
counts there, such as $R(A_7)=86$ with $n=50$, are far above it.

## Consequence for bounded rarity

Suppose $R(A)\le K$. Then (1) gives

$$
\kappa(A)\bigl(M(A)+2\bigr)\ge\frac{n-1-4K}{2}.
$$

The [weighted-circle theorem](weighted_circle_energy.md), an author-recorded
note, gives $M(A)=O_K(n^{7/8})$ along any unbounded sequence with
$R(A)\le K$. Conditional on that bound,

$$
\kappa(A)\ge c_Kn^{1/8} \tag{2}
$$

for large $n$: every nonzero traceless quadratic form splits polynomially many
distance classes of a bounded-rarity configuration. This is a constraint on the
difference vectors, invisible to every scalar multiplicity profile.

## Rotation-rich classes defeat every quadratic form

The proof of (1) finds rare classes only among classes that are not $S$-split.
Natural rigid configurations have no such classes at all.

**Order-three rotations.** Suppose a class contains three vectors $d$,
$\rho d$, $\rho^2d$ with $\rho$ the rotation by $60^\circ$ (or by
$120^\circ$, since $d$ and $-d$ give the same value). For
$S\ne0$, $d^{\mathsf T}Sd=|d|^2\gamma\cos(2\phi-\phi_0)$ with $\gamma>0$, where
$\phi$ is the angle of $d$. The three values are $\gamma|d|^2$ times the
cosines of three angles $120^\circ$ apart. These cosines sum to zero and are
not all zero, so they are not all equal: the class is $S$-split. Every class of
a set invariant under a rotation of order three or six is of this kind. Thus
every class is split by every $S$ for the triangular-lattice points of a
regular hexagon centered at a lattice point, and for every regular polygon
with a multiple of three vertices; the anchor count of the proof is then zero.

**Order-four rotations.** For a square-grid patch invariant under the rotation
by $90^\circ$, $(\rho d)^{\mathsf T}S(\rho d)=-d^{\mathsf T}Sd$. A class is
then unsplit only if all its vectors lie on the two null lines of $S$, so every
class not confined to those two lines is $S$-split.

These families are not counterexamples: a regular polygon has every distance
rare, and a lattice patch has convex layers of size $O(\sqrt n)$, so the
[sparse-layer bound](layers_and_obstructions.md) already forces its rarity to
grow. They show that the unsplit-class count from any single quadratic form
can miss every distance class, even in explicit planar families. By the
[one-rare asymptotic shape](one_rare_asymptotics.md), a hypothetical unbounded
$R=1$ family has an exact triangular-lattice spectrum at every fixed short
scale, so its short classes are of the order-three kind.

## Outcome and remaining gap

The replacement proves linear rarity whenever some quadratic form splits only
$o(n/M(A))$ classes, including configurations with only similarities as
equality-preserving affine maps. It does not reach the rigid lattice-like
case: conditional on the retained weighted-circle bound, every bounded-rarity
configuration satisfies (2), and the local structure
forced on an $R=1$ family makes its short classes split by every form. What
remains is a multiplicity argument for classes whose difference vectors have
three or more directions in rotation-rich position. The test produced a single
anchor count with an exceptional set, not a new multiplicity mechanism for
those classes, so this direction stops here.
