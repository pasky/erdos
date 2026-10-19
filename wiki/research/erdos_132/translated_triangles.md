---
name: research/erdos_132/translated_triangles
title: Translated triangles, convex differences, and lattice orientations
desc: |
  The improved three-anchor bound limits translated triangle families to
  n^(5/7) and forces n^(2/7) minimum-lattice orientations under R equal to one.
sources: []
research_state: closed
created: 2026-09-23T05:40:00Z
updated: 2026-09-24T22:12:56Z
---


# Translated triangles, convex differences, and lattice orientations

***

These results use the small global palette directly, without requiring the
triangle copies to touch or lie near the convex subset. They do not resolve
either unrestricted question in
[Problem 132](../../problems/distance_problems/E0132/_index.md).

## A translation bound

Let $C\subseteq A\subset\mathbb R^2$, with $C$ strictly convex and
$|C|=m\ge3$. Let $T=\{t_1,t_2,t_3\}$ be a fixed noncollinear triangle,
and let $P$ be a nonempty set of translation vectors such that


$$
P+T\subseteq A,\qquad |P|=p.
$$


There is an absolute constant $c_0>0$ such that


$$
q(A)+1\ge c_0
\left(\frac{m^2p}{m+2p-2}\right)^{7/12}. \tag{1}
$$


For a finite set $X$, let $r_X(v)$ count ordered representations of $v$
as a difference of two points of $X$. Strict convexity gives
$r_C(v)\le2$ for every nonzero $v$. One elementary justification is to
rotate $v$ horizontally: each representation is a full horizontal chord
of the convex hull of length $|v|$. Three such chords would, by concavity
of the horizontal width, force the left and right boundary functions to be
affine between their heights. Their middle endpoints would not be extreme
points. Two representations at the same height would likewise contradict
strict convexity.

The additive energy consequently satisfies


$$
E(C,P)=\sum_v r_C(v)r_P(v)
\le mp+2p(p-1).
$$


Applying Cauchy--Schwarz to representations of $C-P$ gives


$$
|C-P|\ge\frac{m^2p^2}{mp+2p(p-1)}
=\frac{m^2p}{m+2p-2}. \tag{2}
$$


Every $z=c-u\in C-P$ satisfies


$$
|z-t_i|=|c-(u+t_i)|\in D(A)\cup\{0\}.
$$


Solymosi--Zahl's improved three-anchor theorem says that the distances from
three noncollinear fixed points to $N$ other planar points include at least
$cN^{7/12}$ values. Apply it to $(C-P)\setminus T$, losing at most three points,
and absorb the small cases using the added one in (1). This proves (1).

The external input is Theorem 1.4 and Section 1.1 of József Solymosi and Joshua
Zahl, [*Improved Elekes--Szabó type estimates using
proximity*](https://arxiv.org/pdf/2211.13294). The full statements were checked;
the constant in Theorem 1.4 depends only on polynomial degree. A uniformity
check is given below. This replaces the earlier $6/11$ theorem of
Sharir--Solymosi, whose weaker consequences remain valid.

In particular, if $|A|=n$, $m\ge cn$, and $q(A)\le Bn$, then $p\le n$
and (1) imply


$$
p=O_{B,c}(n^{5/7}). \tag{3}
$$


## Uniformity of the improved three-anchor estimate

Normalize the anchors to $(0,0),(1,0),(a,b)$, with $b>0$.
Their squared-distance triples $(X,Y,Z)$ satisfy the degree-two equation

$$b^2(X-Y+1)^2+
\bigl((1-a)X+aY-Z+a^2+b^2-a\bigr)^2-4b^2X=0. \tag{7}$$

An invertible affine change of coordinates turns the left side into
$4b^2(x^2+y^2-X)$, so it is irreducible. Its three pure second
derivatives are nonzero, excluding an axis-parallel cylinder.

For completeness, it is also not one of the additive-group surfaces
excluded by the theorem. Such a surface, locally written $Z=f(X,Y)$,
would satisfy $\partial_X\partial_Y\log(f_X/f_Y)=0$ wherever these
derivatives are defined. On the branch with $y>0$, use

$$X=x^2+y^2,\quad Y=(x-1)^2+y^2,$$
$$f_X=\frac{(1-a)y+b(x-1)}y,\qquad
f_Y=\frac{ay-bx}y,$$
$$\partial_X=\tfrac12\partial_x+\frac{1-x}{2y}\partial_y,
\qquad
\partial_Y=-\tfrac12\partial_x+\frac{x}{2y}\partial_y.$$

At $y=b$, direct differentiation gives

$$\partial_X\partial_Y\log(f_X/f_Y)=
\frac{x^3-3ax^2+(3a-1-b^2)x+b^2(1-a)}
 {4b^4(x-a)^2}.$$

This rational function is not identically zero, since its numerator
has leading coefficient one. Derivatives of the logarithm here mean
the rational logarithmic derivatives; no choice of a real logarithm
is required. Irreducibility then excludes a generic local separated
form. Theorem 1.4 therefore applies with an absolute degree-two
constant, even when $b$ tends to zero.

The distance triple determines $(x,y)$ uniquely by subtraction of
squared distances. Thus a $q$-element nonnegative squared palette
permits only $O(q^{12/7})$ points for any noncollinear anchor triangle.
The author checked the polynomial identity, recomputed the displayed
derivative, and checked the primary theorem and its stated application;
the argument is author-recorded.

## Consequences for a hypothetical one-rare sequence

Assume $n\to\infty$ and $R(A)=1$, with minimum distance $\delta$.
Use the checked [triangular-core reduction](one_rare_asymptotics.md).
There is a convex subset of size at least $(1/3-o(1))n$, while
$q(A)\le n/2$. In


$$
I=A\setminus(L_1\cup L_2),
$$


all but $b=o(n)$ points have six minimum-distance neighbors in $I$.
Call those points good. At each good point the six directions form a
regular hexagon. Group good points according to these direction sets,
that is, according to lattice orientation modulo $\pi/3$.

For each orientation choose the same two adjacent length-$\delta$ vectors
$u,v$. Every good center in the group supplies a translate of
$\{0,u,v\}$. Formula (3) shows that each group has $O(n^{5/7})$ centers,
with one constant valid for all the groups. Since there are
$(1/3+o(1))n$ good centers, the number of orientations is


$$
\Omega(n^{2/7}). \tag{4}
$$


Thus no such unbounded family can have all its points in one triangular
lattice of mesh $\delta$, or a positive fraction of its good centers in
parallel translates of that lattice. This does **not** exclude a common
finer triangular lattice, which can have minimum-length vectors in many
orientations; the refinement must, however, be superpolynomial, as shown
below.

Every entire minimum-distance component has $o(n)$ vertices. Indeed,
the earlier reduction puts each component in a mesh-$\delta$ triangular
lattice. Its good vertices number $O(n^{5/7})$; there are only $o(n)$
bad interior vertices in total. The outer layers have only $o(n)$
minimum-distance incidences, so only $o(n)$ of their vertices can belong
to nontrivial minimum-distance components.

The [first exceptional length](first_exceptional_distance.md) must therefore
exist eventually. Otherwise all distances have mesh-$\delta$ triangular
lattice norms; distances to a unit equilateral triangle in a good patch
then put every point in its mesh-$\delta$ lattice by the integral norm
argument in that note, contradicting (4). Its ranks from both ends still
tend to infinity, as established there.

## A lower bound on the exceptional vertices

Let $S$ range over components induced by good vertices in $I$.
Each has at most $C n^{5/7}$ vertices. In its own axial lattice
coordinates, let $a_S,b_S$ count the occupied coordinate values.
The boundary edges in two lattice directions alone number at least
$2(a_S+b_S)\ge4\sqrt{|S|}$, since $|S|\le a_Sb_S$.
Every outgoing lattice neighbor exists in $I$, by goodness, and is bad.
Each bad vertex receives at most six such incidences. Hence


$$
6b\ge4\sum_S\sqrt{|S|}
\ge\frac{4\sum_S|S|}{\sqrt{C n^{5/7}}}
\gg n^{9/14}. \tag{5}
$$


Richness of the second-largest distance and its $3|L_1\cup L_2|/2$
upper bound give $|I|<n/3$. Also


$$
e_\delta(I)\le3|I|-b/2,
$$


because each bad vertex has degree at most five. Since the full minimum
class is rich, at least $b/2\gg n^{9/14}$ of its pairs touch the outer
two layers. This remains compatible with their previously proved $o(n)$
upper bound; it is not a contradiction.

## A common finer lattice requires superpolynomial refinement

Suppose additionally that $A$ lies in a triangular lattice of mesh $h$.
Then $M=\delta^2/h^2$ is a positive integer. Each minimum-length
orientation is represented by an Eisenstein integer of norm $M$,
modulo the six unit rotations. The ideal-count argument in
[arithmetic palettes](arithmetic_palettes.md), now in
$\mathbb Q(\sqrt{-3})$, bounds the number of such orientations by
$\tau(M)$. Consequently (4) gives

$$\tau(M)\gg n^{2/7}.$$

Since $\tau(M)=O_\varepsilon(M^\varepsilon)$ for every
$\varepsilon>0$, it follows that $M>n^B$ eventually for every fixed
$B$. Thus a polynomially finer common triangular lattice is excluded,
not merely the lattice of mesh $\delta$.

There is a coordinate-free arithmetic consequence. Normalize
$\delta=1$. If the squared-distance palette is contained in
$D^{-1}\mathbb Z$, with $D$ a positive integer, choose a good unit
equilateral triangle with vertices $0,u,v$. For every $p\in A$,
subtraction of its squared distances gives

$$U=2p\cdot u\in D^{-1}\mathbb Z,\qquad
V=2p\cdot v\in D^{-1}\mathbb Z,$$
$$p=\frac{2U-V}{3}u+\frac{2V-U}{3}v.$$

Hence $A\subseteq(3D)^{-1}\Lambda$, where $\Lambda$ is the unit
triangular lattice generated by $u,v$. Applying the preceding result
with $M=9D^2$ shows that $D>n^B$ eventually for every fixed $B$.
No bounded-height rational reduction is inferred for arbitrary sets.

## The missing rotation estimate

More generally, if $G$ is a family of direct isometries with
$gT\subseteq A$, then


$$
\left|\bigcup_{g\in G}g^{-1}C\right|
=O\bigl((q(A)+1)^{12/7}\bigr). \tag{6}
$$


Every point of this union has its three anchor distances in
$D(A)\cup\{0\}$, so the same theorem proves (6). For translations,
convex difference multiplicities supply (2). For varying rotations, the
collision count instead involves intersections $C\cap gC$. The
[moving-frame argument](moving_frames.md) supplies a lower bound
$\gg_K n^{17/16}/\sqrt{\log n}$ under bounded rarity, still compatible
with (6). The [arithmetic-palette argument](arithmetic_palettes.md)
closes this gap only under its progression-cover hypothesis. No common
orientation or unrestricted contradiction is inferred.

The author checked (1)--(4), the primary source, the boundary count,
and the scope of the common-lattice conclusion in (5); the argument is
author-recorded. Neither unrestricted assertion is solved.

## A local field-alignment observation for finite patches

Let $\omega=e^{i\pi/3}$ and $\Lambda=\mathbb Z+\mathbb Z\omega$.
Suppose

$$P\subset z+a\{u+v\omega:|u|,|v|\le L\},\qquad a\ne0,\quad L\ge1.$$

If a point $x$ is equidistant from three distinct points of $P$, then

$$(x-z)/a\in\mathbb Q(\omega),\qquad |x-z|=O(|a|L^3).$$

Indeed, normalize $z=0,a=1$ and write $x=s+t\omega$. Three points
on a circle are noncollinear. Subtracting their squared-distance equations
therefore gives an invertible two-by-two integer linear system for $s,t$:
its coefficients are differences of $2u+v$ and $u+2v$, of size $O(L)$,
and its right sides are differences of $Q(u,v)$, of size $O(L^2)$.
The determinant is a nonzero integer of size $O(L^2)$; Cramer's rule
bounds the numerators by $O(L^3)$ and proves both assertions.

If a second patch is contained in $w+b\Lambda$ and
$b/a\notin\mathbb Q(\omega)$, at most one of its points can be
such a circumcenter of three points of $P$, even allowing different
radii. Two distinct centers would have difference both in
$a\mathbb Q(\omega)$ and in $b\Lambda\setminus\{0\}$, forcing
$b/a\in\mathbb Q(\omega)$. Thus any fixed cross-distance graph
between two such patches has degree at most two at all but one vertex
on each side, by applying the statement in both directions.

This does not bound the multiplicity in the full configuration: one
vertex may have two neighbors in each of many different patches.
Field-commensurable but differently oriented patches are not excluded.
No near-linear many-anchor bound, palette progression cover, or global
alignment conclusion was established. The author checked the integer
linear system and the field intersection argument; they are
author-recorded.
