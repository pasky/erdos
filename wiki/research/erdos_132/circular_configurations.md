---
name: research/erdos_132/circular_configurations
title: One off-circle point and concentric polygon constructions
desc: |
  A cocircular hull with two nonvertices has a second rare distance;
  near-circular and fixed-ring families have linear rarity growth.
sources: []
research_state: closed
created: 2026-09-22T21:30:00Z
updated: 2026-10-14T00:26:52Z
---


# One off-circle point and concentric polygon constructions

***

These are restricted results and construction obstructions, not solutions of
[Problem 132](../../problems/distance_problems/E0132/_index.md). Pair multiplicities
are unordered.

## Comparison with two-polygon rich-distance constructions

The [independent input](independent/largest_distance_ranks_and_small_orders.md),
Appendix D.6, correctly warns that constructing many rich classes does not bound
the number of rare classes. The established
[positive-circle theorem](circle_incidence.md) says more for Bhowmick's
two-polygon constructions: they have linearly many rare classes as well.

In
[Bhowmick, Section 2](../../../library/distance_problems/bhowmick_2024_problem_erdos_about_rich_distances/_index.md),
the odd construction has $n=2m+1$ points and contains a regular $(m+1)$-gon; the
even construction has $n=2m$ points and also contains a regular $(m+1)$-gon.
Applying the circle theorem with fraction $1/2$ gives, respectively,

$$R(A)\ge(n-1)/4-O(n^{2/3}),\qquad
  R(A)\ge n/4-O(n^{2/3}).$$

The constants are uniform in the allowed rotation in the odd construction.
Thus neither is a bounded-$R$ family. The source construction and this
deduction were checked by the author; the deduction is author-recorded.
In counting the selected rich classes, subtract shared unordered pairs,
not shared distance values: congruent polygons have the same chord
spectrum, but in the reflection case their only shared pair is the
common edge. Cross-pairs may further increase multiplicities, so the
source's counts are lower bounds for the full classes.

## All but one point on a circle

**Theorem.** If $n\ge5$ and $n-1$ points of $A$ lie on a circle, then

$$R(A)\ge\max\left\{2,\left\lceil\frac{n-5}{5}\right\rceil\right\}.$$

Let $H=A\setminus\{p\}$, $h=n-1$, and normalize its circle to radius
one and center zero. A circle distance graph has maximum degree two,
so every chord length has at most $h$ occurrences in $H$. Distances
from one vertex give at least $\lfloor h/2\rfloor$ distinct chord lengths.
If $p$ lies on the circle, all distances in $A$ are rare. Assume first
that $p$ is neither on the circle nor its center. Every distance from
$p$ has at most two occurrences. Richness therefore requires exactly
$h$ occurrences inside $H$ and exactly two involving $p$.

### Nonregular circle sets

A chord length with $h$ occurrences has degree two at every vertex.
The corresponding chord rotation preserves $H$. If the rotational
symmetry group has order $g$, then $g\mid h$, and the number of
potentially rich lengths is at most $\lfloor(g-1)/2\rfloor$; antipodal
chords have only $h/2$ occurrences and cannot be rich. Unless $H$ is
regular, $g\le h/2$. Thus

$$R(A)\ge\lfloor h/2\rfloor-\lfloor(g-1)/2\rfloor
 \ge\lfloor h/4\rfloor+1.$$

### Regular circle sets: a quantitative argument

If $p$ is on no reflection axis, all distances from it to $H$ differ,
so no class is rich. Otherwise put $p=(\rho,0)$, $\rho>0$, $\rho\ne1$,
and set $m=\lfloor h/2\rfloor$, $\delta=2\pi/h$. The increasing lists
of squared chord lengths and distinct squared distances from $p$ are

$$S=\{2-2\cos(j\delta):1\le j\le m\},$$
$$T=\{1+\rho^2-2\rho\cos((i+\alpha)\delta):0\le i<\ell\},$$

where $\alpha\in\{0,1/2\}$, $\ell\in\{m,m+1\}$, and $m+\ell\ge h$.
The latter assertions follow by folding the regular polygon's angles
into $[0,\pi]$ along its reflection axis.

Put $t=|S\cap T|$, $a=m-t$, $b=\ell-t$, and $s=a+b$. Every value in
$S\triangle T$ is rare, hence $R(A)\ge s$. A match at indices $j,i$
has index difference $d=j-(i+1)\in[-b,a]$: before the match this is
the number of unmatched $S$ entries minus unmatched $T$ entries.
There are at most $s+1$ such integer differences.

For a fixed $d$, put $\psi=(d+1-\alpha)\delta$ and
$\theta=(i+\alpha)\delta$. The matching equation is

$$(\cos\psi-\rho)\cos\theta-\sin\psi\sin\theta
  =(1-\rho^2)/2.$$

Its two coefficients cannot both vanish, since $\rho>0$, $\rho\ne1$.
A line intersects the unit circle in at most two points. Thus there
are at most two matches for each $d$, giving

$$t\le2(s+1),\qquad h\le m+\ell=2t+s\le5s+4\le5R(A)+4.$$

### Excluding a single rare distance in the regular case

Suppose first $h=2m+1$ is odd. The star at $p$ has at least $m+1$
distinct lengths, but $H$ has only $m$. A unique rare class would
therefore be a new star length; every old chord length would have
to occur twice in the star. There are $2m+1$ star edges, so the new
length occurs once. Reflection pairing about the line $0p$ fixes
its vertex. Label that vertex $(1,0)$ and write $p=(\rho,0)$ with
signed $\rho$. With $c_j=\cos(2\pi j/h)$ this forces

$$\{1+\rho^2-2\rho c_j:1\le j\le m\}
  =\{2-2c_j:1\le j\le m\}.$$

The ranges of the two sets give $|\rho|=1$, contradicting that $p$
is off the circle. Here $h\ge5$, so the ranges are nonzero.

If $h=2m$ is even, the polygon diameter is rare: it has at most
$m+2\le n$ occurrences after adding $p$. Uniqueness of this rare
class would force all $m$ chord lengths to occur twice in the star,
with no new length. The reflection axis then has no fixed polygon
vertex and passes through opposite edge midpoints. Its folded
angles are $(2i-1)\pi/(2m)$, $1\le i\le m$. Put
$c=\cos(\pi/(2m))$. Equality of the means of the squared-length sets
gives $\rho^2=1+2/m>1$; equality of their ranges gives
$4\rho c=4c^2$, or $\rho=c<1$. This contradiction includes $h=4$.

### The center

If $p=0$, only the circumradius can become rich. Thus
$R(A)\ge\lfloor h/2\rfloor-1$, which gives both claimed bounds for
$h\ge6$. For $h=4,5$, three or more total distances immediately give
two rare classes. Suppose there are only two lengths, $1,s$.
Richness of $1$ would require two unit chords in $H$.

If the chords share a vertex, their endpoints are three consecutive
vertices of a regular hexagon, and $s=\sqrt3$. A fourth circle point
at only distances $1,\sqrt3$ from those three does not exist: the only
remaining candidates relative to the middle vertex are antipodal
to one of the other two. If two unit chords are disjoint and no
unit chords share a vertex, all four distances between them equal
$s$. The endpoints of one chord then both lie on the perpendicular
bisector of the other; since this line passes through the circle
center they are antipodal, contradicting their unit separation.
Thus the radius is rare too, completing the proof.

## A cocircular hull with two nonvertices

The
[second independent input](independent/large_distance_graph_and_convex_extension.md),
Section 5.3, proves $R(A)\ge2$ when exactly two points are nonvertices and the
hull vertices are cocircular. The checked
[unique-diameter theorem](unique_diameter_obstruction.md) shortens its proof and
gives the following slightly more general statement.

**Proposition.** Let $A$ be an $n$-point planar set, $n\ge5$, and let
$C\subset A$ be $n-2$ points on a circle with center $o$. If one point
$p\in A\setminus C$ lies in $\operatorname{conv}C$ and differs from
$o$, then $R(A)\ge2$. The other point of $A\setminus C$ is unrestricted.

Write $p=\sum_i\alpha_i c_i$ as a nontrivial convex combination
of points of $C$, with positive coefficients. For every $c\in C$,

$$|p-c|^2
=\sum_i\alpha_i|c_i-c|^2-\sum_i\alpha_i|c_i-p|^2
<\operatorname{diam}(C)^2\le\operatorname{diam}(A)^2.$$

Since $p\ne o$, a circle centered at $p$ meets the circle of $C$
in at most two points. Thus $p$ sees at least
$\lceil(n-2)/2\rceil$ distinct lengths on $C$, all strictly below
the full diameter, and

$$q(A)\ge\lceil(n-2)/2\rceil+1.$$

If $R(A)=1$, the pair budget gives $q(A)\le\lfloor n/2\rfloor$.
At odd order these bounds contradict each other. At even order they
force $q(A)=n/2$, hence the diameter occurs uniquely, contradicting
the unique-diameter theorem. This proves the proposition.

In the stated hull case both remaining points lie in $\operatorname{conv}C$,
and at least one is not the center, so the proposition applies. It includes
nonvertex points on hull edges. The independent proof's alternative
reflection-pairing argument also checks out, but is not needed once the
unique-diameter theorem is available. The author checked both the strict
distance exclusion and the parity argument; the argument is
author-recorded.

This is a finite-order extension, not a new asymptotic theorem: the
[positive-circle theorem](circle_incidence.md) already gives linear rarity
growth for this family. The subsequent
[all-but-two-circle theorem](two_off_circle.md) removes the interior-point
assumption altogether: any $n-2$ concyclic points suffice for $R(A)\ge2$.
Its proof uses a small-difference lemma and exact regular-polygon palette
tests. Arbitrary hulls with two nonvertices remain a separate question,
apart from the [even-order case](nearly_convex.md) covered by that theorem.

## Concentric regular rings

The following bounds concern $t\ge2$ regular $m$-gons with distinct
positive circumradii, a common center, and arbitrary rotations.
There are $n=tm$ points. The radii and rotations may depend on $m$.

### Two rings: a simple uniform bound

Put $K=\lfloor m/2\rfloor$ and normalize the radii to $1,r$, $0<r<1$.
If their within-ring chord spectra have $C$ common values, each gives

$$\sin(a\pi/m)=r\sin(b\pi/m),\qquad1\le a<b\le K.$$

The increasing function
$f(b)=(m/\pi)\arcsin(r\sin(b\pi/m))$ has $f'(b)<1$. Thus the
integer gaps $b-a$ strictly increase along these matches. At the
$j$-th match both $a\ge j$ and $b-a\ge j$, so $b\ge2j$. Therefore
$C\le\lfloor K/2\rfloor$.

If the relative rotation is a multiple of $\pi/m$, there are at most
$K+1$ cross-lengths. The within spectra have $2K-C$ values; every one
absent from the cross spectrum has at most $2m=n$ occurrences. Hence

$$R(A)\ge K-C-1\ge\lceil K/2\rceil-1.$$

Otherwise every cross-length has multiplicity exactly $m$, so a rich
length must occur in both within spectra. In this case
$R(A)\ge2K-2C\ge2\lceil K/2\rceil$. In particular two rings cannot
give a bounded-$R$ sequence as $m\to\infty$.

### Any fixed number of rings

Put $P=t(t+1)/2$ and $C_m=12(1+(2m)^{2/3})$. Then

$$R(A)\ge P\lfloor m/2\rfloor-P(P-1)C_m. \tag{5}$$

For each unordered radius pair $\beta$, its squared-distance spectrum
$D_\beta$ has at least $\lfloor m/2\rfloor$ values and the form

$$A_\beta-B_\beta\cos(2\pi j/m+\eta_\beta),\qquad
 (A_\beta,B_\beta)=(r_i^2+r_j^2,2r_ir_j).$$

These parameter pairs are distinct for different unordered radius
pairs, since $A+B=(r_i+r_j)^2$ and $A-B=(r_i-r_j)^2$. A length
belonging to exactly one radius-pair spectrum has multiplicity at
most $2m\le n$, and is rare.

To bound overlaps, fold angles into $[0,\pi]$, giving at most two
translated angular grids for each spectrum. Equality of two values
from different spectra gives

$$y=\arccos(a+b\cos x),\qquad b>0.$$

The sign of the second derivative is the sign of

$$-ab\cos^2x+(1-a^2-b^2)\cos x-ab.$$

This polynomial vanishes identically only if $(a,b)=(0,1)$, which
would make the spectra's parameter pairs identical. A singleton
overlap domain contributes at most one value. Every nondegenerate
domain splits into at most three strictly convex or strictly concave
monotone pieces; singular endpoint derivatives do not affect this
claim. Scale the coordinates by $m/(2\pi)$. Coincidences lie in a
translate of $\mathbb Z^2$ and have total Manhattan span at most $m$.

On one such piece, $q$ consecutive lattice points have $q-1$ positive
integer gap vectors with distinct slopes, hence distinct vectors.
At most $(q-1)/2$ positive integer vectors have Manhattan norm at
most $\sqrt{q-1}$. Summing the other vectors' lengths gives
$m\ge(q-1)^{3/2}/2$, so $q\le1+(2m)^{2/3}$. Four pairs of angular
branches, each split into at most three pieces, give
$|D_\beta\cap D_\gamma|\le C_m$.

Finally $\sum_\beta|D_\beta|\ge P\lfloor m/2\rfloor$. A value in
$k\ge2$ spectra contributes $k\le2\binom k2$ to this sum. Removing
all repeated values leaves at least the right side of (5) values
in exactly one spectrum. This proves (5). For fixed $t$ the bound
tends linearly to infinity with $m$.

### Exact small configurations with $R=2$

Two concentric squares of radii $1$ and $q=\sqrt{2-\sqrt3}$, rotated
by $\pi/4$, have cross squared lengths
$1+q^2\pm\sqrt2q\in\{2,2q^2\}$. Each side length has multiplicity
$12>8$, while each of the two diameter lengths has multiplicity two.
Thus this eight-point set has $R=2$, not $R\le1$.

Concentric equilateral triangles of radii $1,1/2$, rotated by $\pi/3$,
have multiplicities $9,3,3$ and also $R=2$. Neither construction
refutes an assertion in the question.

### The two-square extensions through eleven points

The unrestricted construction attempt tested enlargement of that
eight-point example. It cannot produce $R=1$ by adding at most three
points. Here is an exact geometric certificate, independent of a search.

Write $a=(\sqrt3-1)/2$, $c=2-\sqrt3=2a^2$, and use the model

$$B=\{(\pm1,0),(0,\pm1),(\pm a,\pm a)\}.$$

Its inner diameter $d=2\sqrt c$ has two pairs. Every radius-$d$
circle contains at most two points of $B$. To verify this, all the
squared circumradii of its triples belong to

$$\{1,c,2,2/3,2c,2c/3\},$$

none of which equals $d^2=4c$. The outer and inner triples have
squared circumradii $1,c$. The following mixed triples exhaust the
remaining types under the square's symmetry group. Put
$O_1=(1,0),O_2=(0,1),O_3=(-1,0)$ and
$I_+=(a,a),I_-=(-a,-a),J=(-a,a),K=(a,-a)$.

| Triple | Circumcenter | Squared circumradius |
| --- | --- | --- |
| $O_1,O_2,I_+$ | $((\sqrt3+1)/2,(\sqrt3+1)/2)$ | $2$ |
| $O_1,O_2,I_-$ | $((3-\sqrt3)/6,(3-\sqrt3)/6)$ | $2/3$ |
| $O_1,O_2,J$ | $(a,a)$ | $2c$ |
| $O_1,O_3,I_+$ | $(0,-1)$ | $2$ |
| $O_1,I_+,K$ | $(1/\sqrt3,0)$ | $2c/3$ |
| $O_1,J,I_-$ | $(c,0)$ | $2c$ |
| $O_1,I_+,J$ | $(0,-1)$ | $2$ |
| $O_1,I_+,I_-$ | $(a,-a)$ | $2c$ |

Each center is checked by substituting the three points. For the
exhaustion, a pair of outer vertices is adjacent or opposite; the
adjacent case has three positions of an inner vertex up to symmetry,
and the opposite case has one. The same split for a pair of inner
vertices gives the last four rows. All these triples are noncollinear.

If $k\le3$ arbitrary points are added, the full multiplicity of $d$
is at most

$$2+2k+\binom k2\le8+k.$$

It remains rare and is not the full diameter, since $d<2$ and $B$
already contains a pair of length two. The diameter theorem supplies
a second rare class. This excludes only this enlargement strategy,
not general sets of eight through eleven points. The author checked
the symmetry types, displayed circumcenters, and pair bound; the
argument is author-recorded.

The bounds above do not control constructions where both the number
of rings and their orders grow without restriction. Nor is there a
reduction of arbitrary sets to circular ones.
