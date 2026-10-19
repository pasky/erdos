---
name: research/erdos_132/two_off_circle
title: Two rare distances with all but two points on a circle
desc: |
  A small-difference lemma and explicit regular-polygon palette tests
  prove the first assertion whenever n minus two points are concyclic.
sources: []
research_state: closed
created: 2026-09-23T04:01:34Z
updated: 2026-09-24T22:12:56Z
---


# Two rare distances with all but two points on a circle

***

**Theorem.** Let $A$ be an $n$-point planar set, $n\ge5$. If $n-2$
points of $A$ are concyclic, then $R(A)\ge2$.

The subsequent [three-off-circle theorem](three_off_circle.md) extends
this conclusion to $n-3$ concyclic points. The palette lemmas below
remain inputs to its proof.

The two remaining points may be anywhere. This strengthens the
[cocircular-hull extension](circular_configurations.md), which required
one noncentral added point to lie inside the circular subset's hull.
It uses the checked [small-order](small_orders.md) and
[unique-diameter](unique_diameter_obstruction.md) theorems, but no
classification of general near-minimal convex polygons.

## 1. A small difference set on a circle

Let $S$ be a finite nonempty subset of an abelian group, $|S|=h$,
and put $D=S-S$. If $|D|<3h/2$, then $D$ is a subgroup.
Indeed, for $x=a-b\in D$, the sets $S-a,S-b\subset D$ intersect
in at least $2h-|D|>h/2$ points. Equivalently,
$|S\cap(S+x)|>h/2$. For $x,y\in D$, the two subsets
$S\cap(S+x)$ and $S\cap(S+y)$ of $S$ intersect. A point $z$ in
their intersection has $z-x,z-y\in S$, so $x-y\in D$.
Thus the finite nonempty set $D$ is closed under subtraction.

For the angles $S\subset\mathbb R/(2\pi\mathbb Z)$ of $h$
circular points $C$, every positive chord length accounts for at most
two elements of $D$, and zero accounts for one. Therefore

$$h\le |D|\le2q(C)+1.$$

When $2q(C)+1<3h/2$, the lemma makes $D$ a finite subgroup of the
circle group. It has the form $(2\pi/k)\mathbb Z/(2\pi\mathbb Z)$,
where $k=|D|$. Since $S$ lies in one coset of $D$, $C$ is a subset
of a regular $k$-gon. No additive-combinatorial theorem is imported here.

## 2. A regular-polygon palette extension lemma

Let $V$ be a regular $k$-gon, $k\ge5$, with chord-length palette
$P(V)$. In each of the following cases, there is no point off the
circumcircle and off its center whose distances to $C$ all lie in $P(V)$:

- $k$ is even and $C$ is $V$ or $V$ minus one vertex;
- $k$ is odd and $C$ is $V$ minus one or two vertices.

Write $M=\lfloor k/2\rfloor$ and normalize the circle to radius one.
A noncentral point has at most two circle points at each prescribed
distance. Here $|C|$ equals $2M$ or $2M-1$, so every one of the $M$
palette values must occur. The pinned list consists of pairs, or of
pairs and exactly one singleton. There is at least one pair. Reflection
in the line joining the center to the pin exchanges that pair; as both
vertices belong to $V$, this line is a reflection axis of $V$.

### Even order

For $k=2M$, an edge-midpoint axis has no fixed vertex of $V$.
Deleting at most one vertex does not remove any pinned value. Writing
the pin's radius as $\rho>0$, its squared palette is

$$\left\{1+\rho^2-2\rho\cos\frac{(2j-1)\pi}{2M}:1\le j\le M\right\}.$$

Equality with the squared chord palette
$\{2-2\cos(j\pi/M):1\le j\le M\}$ gives, from means and ranges,

$$\rho^2=1+2/M,\qquad \rho=\cos(\pi/(2M)),$$

a contradiction. Here the cosine sums are respectively zero and $-1$;
the ranges are $4\rho c$ and $4c^2$, where $c=\cos(\pi/(2M))$.

A vertex axis has two fixed vertices. It is impossible when $C=V$,
since all pinned values must be paired. With one vertex deleted, that
vertex must be fixed; otherwise the two fixed vertices and the reflected
mate of the deleted vertex give three singletons. Normalize the deleted
vertex to $1$ and write the pin as signed $\rho\ne0$ on the real axis.
The pinned and chord squared palettes are affine images of the same
nonconstant list $\{\cos(j\pi/M):1\le j\le M\}$. Equality of
their ranges forces $|\rho|=1$, contrary to being off the circle.

### Odd order with one or two deletions

For $k=2M+1$, a reflection has one fixed vertex. With one deletion,
all surviving vertices must be paired, so the fixed vertex is the
deleted one. The same-list range argument again gives $|\rho|=1$.

With two deletions, exactly one singleton is allowed. Either one deleted
vertex is fixed, or the reflection exchanges the two deleted vertices.
In the first case the other deleted vertex has a surviving mate, so the
pinned palette is unchanged from deleting only the fixed vertex. The
preceding argument applies.

For exchanged deletions, normalize the fixed vertex to $1$ and put

$$a=\pi/k,\quad c=\cos a,\quad u=2c-1,\quad c_j=\cos(2ja).$$

The holes are $e^{\pm2ita}$ for some $1\le t\le M$. Palette equality
for the signed real pin $\rho\ne0$ is precisely

$$F=\rho E+(1-\rho^2)/2,\quad
F=\{c_1,\ldots,c_M\},\quad
E=\{c_0,\ldots,c_M\}\setminus\{c_t\}. \tag{1}$$

Since $c_M=-c$ and $c_{M-1}=-\cos3a$, the ranges give

$$|\rho|=u\quad(t<M),\qquad |\rho|=1/u\quad(t=M). \tag{2}$$

Explicitly, $\operatorname{range}F=(1+c)u$, whereas the two
possible ranges of $E$ are $1+c$ and $(1+c)u^2$.
If $\rho>0$, matching maxima in (1) gives
$|\rho-1|=2\sin a$. But

$$1-u=2(1-c)<2\sin a,\qquad 1/u-1<2\sin a. \tag{3}$$

For the second inequality, squaring and canceling $1-c>0$ reduces
to $1-c<(1+c)(2c-1)^2$. The difference is
$2c(2c^2-1)>0$, since $k\ge5$ gives $c>1/\sqrt2$.
If $\rho<0$, matching minima instead gives
$|\rho|=2\cos(a/2)-1$, strictly between $u$ and $1$ and hence
equal to neither value in (2). This proves the extension lemma.

## 3. Proof of the theorem

The [small-order theorem](small_orders.md) handles $5\le n\le10$.
Assume $n\ge11$ and $R(A)=1$, and let $C$ be the $h=n-2$ points
on the chosen circle. If another point lies on that circle, the
[all-but-one-circle theorem](circular_configurations.md) already gives
a contradiction. Thus both remaining points are off the circle.

Pair counting and the unique-diameter theorem give

$$q(A)\le
\begin{cases}
n/2-1,&n\text{ even},\\
(n-1)/2,&n\text{ odd}.
\end{cases} \tag{4}$$

Indeed, equality $q(A)=n/2$ at even order would force a uniquely
attained diameter. This use of the unique-diameter theorem is not
circular: its small-order base cases were proved independently.

If $h=2m$ is even, then $|S-S|\le h+1<3h/2$. Section 1 puts $C$
in a regular polygon of order $h$ or $h+1$. All $m$ chord lengths of
that polygon survive the possible single deletion, exhausting the
palette in (4). At least one of the two added points is noncentral,
contradicting the extension lemma.

If $h=2m+1$ is odd, then $|S-S|\le h+2<3h/2$. Thus $C$ is a
regular $h$-gon, a regular $(h+1)$-gon minus one vertex, or a regular
$(h+2)$-gon minus two vertices. In the latter two cases all $m+1$
chord values survive and exhaust the palette, again giving a
contradiction. For these survival assertions, a deleted vertex removes
at most two pairs of any nondiametral chord class; such a class starts
with $k$ pairs. At even order the diameter has $k/2$ pairs and loses
at most one per deleted vertex.

It remains that $C$ is a regular odd $h=2m+1$ polygon. Normalize its
circumradius to one. If one added point is the center, its unit distance
has at most $h+2=n$ pairs: there are no unit chords in an odd regular
polygon, the other pin adds at most two, and the pin-pin distance is
not one because the other pin is off the circle. This rare distance
is smaller than the polygon diameter, a contradiction.

Both added points are therefore noncentral. Each sees at least $m+1$
lengths on $C$, so there is exactly one new value beyond its $m$ chord
values. It occurs at most $2+2+1=5\le n$ times. Hence it is rare
and, under $R(A)=1$, is the full diameter $D$.

Each pin uses every value of this $(m+1)$-element palette, with exactly
one singleton. Its center line is a reflection axis of $C$.
Normalize its fixed vertex to $1$, write the pin as signed $\rho$,
and use $a=\pi/h$, $c_j=\cos(2ja)$, and $u=2\cos a-1$.
If $\rho<0$, its largest pinned value $D$ comes from the fixed vertex.
Removing it leaves the same cosine list $c_1,\ldots,c_m$ as the
chord palette. Equality of ranges forces $\rho=-1$, on the circle.
If $\rho>0$, its largest value comes from $c_m$. The remaining pinned
list uses $c_0,\ldots,c_{m-1}$; the range and minimum comparisons
in (2)--(3) give $\rho=1/u$ and $\rho-1=2\sin a$, contradicting
(3). This excludes the last case and proves the theorem.

## Scope

The author checked the small-difference argument, reflection singleton
counts, palette survival, signed-radius comparisons, and parity in (4);
the argument is author-recorded.
The [positive-circle theorem](circle_incidence.md) already gives linear
rarity growth for this family; the new conclusion is the exact finite
bound $R\ge2$ at every order. The resulting
[even-order convex corollary](nearly_convex.md) is also proved. Arbitrary
odd-order sets with two points outside convex position, and the
unrestricted planar problem, remain untreated.
