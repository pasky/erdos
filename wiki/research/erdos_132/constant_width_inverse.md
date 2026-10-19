---
name: research/erdos_132/constant_width_inverse
title: Near-minimal distance counts on constant-width boundaries
desc: |
  Bounded excess over m/2 distances on a constant-width boundary forces
  a positive circular fraction; this treats boundedly many diameter-inactive points.
sources: []
research_state: closed
created: 2026-09-22T23:35:00Z
updated: 2026-09-24T22:12:56Z
---


# Near-minimal distance counts on constant-width boundaries

***

## The inverse statement

**Theorem.** Fix $L\ge0$. There is $c_L>0$ such that, for all
sufficiently large $m$, every $m$-point subset $C$ of the boundary
of a planar constant-width body with

$$q(C)\le m/2+L$$

contains at least $c_Lm$ concyclic points.

This is a restricted inverse theorem. A general convex polygon need not lie on a
constant-width boundary. Neither unrestricted assertion of
[Problem 132](../../problems/distance_problems/E0132/_index.md) follows from it.

### 1. Diameter degree and the ranks in a row

Write $D$ for the body's width, $q=q(C)$, and label the points
$p_0,\ldots,p_{m-1}$ counterclockwise. Indices are taken modulo
$m$. The [boundary theorem](constant_width.md) supplies strict
convexity, monotonicity of distance along each directed boundary
arc up to the $D$-farthest arc, and $q\ge\lfloor m/2\rfloor$.

We use Altman's maximal-side lemma: a convex $v$-gon having a side which attains
its diameter determines at least $v-2$ distances. This is Lemma 1 in the
supplied
[Fishburn paper](../../../library/distance_problems/fishburn_1995_convex_polygons_few_intervertex_distances/_index.md),
whose statement and definition of a maximal side were checked.

If $|p_i-p_{i+s}|=D$, apply that lemma to the two subpolygons
having this chord as a side. They have $s+1$ and $m-s+1$
vertices, so

$$q\ge\max\{s,m-s\}-1.$$

For a two-vertex subpolygon the needed inequality is trivial.
Thus every $D$-neighbor of $p_i$ has index displacement in
$[m-q-1,q+1]$. In particular its $D$-degree $a_i$ satisfies

$$a_i\le2q-m+3\le2L+3. \tag{1}$$

List the occurring distances increasingly as $d_1<\cdots<d_q$.
The two strictly increasing directed lists from any $p_i$ contain
each subdiametral distance at most once each. If $D$ is absent
from $C$, their total number of missing entries from this
palette is $2q-(m-1)\le2L+1$. If $D$ is present, remove it
from the palette. The missing-entry count becomes

$$2(q-1)-(m-1-a_i)\le4L+2. \tag{2}$$

Set $E=\lceil4L+4\rceil$. Each of the two increasing lists
therefore has at least $\lfloor m/2\rfloor-1-E$ entries.
For sufficiently large $m$, the first $F=\lfloor m/3\rfloor$
successors of every $p_i$ lie on its increasing arc, and

$$|p_i-p_{i+k}|=d_{k+e_i(k)},\qquad 1\le k\le F, \tag{3}$$

where $e_i(k)$ is nondecreasing and takes integer values in
$\{0,\ldots,E\}$. It counts omitted palette entries before
the $k$-th entry. Each row $e_i$ has at most $E$ jumps.

### 2. Four compatible rows

Use the finite van der Waerden theorem to choose $N$ such that
every $(E+1)^2$-coloring of $\{0,\ldots,N-1\}$ has a
monochromatic four-term arithmetic progression. Choose an
integer $M\ge8N(E+1)$. All these constants depend only on $L$.

Partition $\{1,\ldots,F\}$ into $M$ consecutive intervals of
nearly equal length. A row is nonconstant on at most $E$ of
them. Some interval $J=[u,v]$, of length $\Omega_L(m)$,
therefore has fewer than $m/(8N)$ nonconstant rows.

For sufficiently large $m$, all $M$ intervals

$$[N^a,N^{a+1}],\qquad 0\le a<M,$$

lie in $[1,F]$. Each jump is internal to at most one such
interval. Some $H=[h,Nh]$ again has fewer than $m/(8N)$
nonconstant rows. Here $h\le N^{M-1}$ is bounded in terms of
$L$, independently of $m$.

Call a row good if it is constant on both $J$ and $H$, and
color it by its two constant values. Fewer than $m/(4N)$
rows are bad. A bad row spoils at most $N$ cyclic chains

$$i,i+h,\ldots,i+(N-1)h.$$

Hence some such chain is all good. Its indices are distinct
for sufficiently large $m$. Van der Waerden's theorem now
supplies four same-colored rows

$$a,a+k,a+2k,a+3k,$$

where $k=dh$, $1\le d\le(N-1)/3$. In particular $k,2k\in H$
and $k=O_L(1)$.

### 3. A rotation propagates across a long interval

Put $x_\ell=p_{a+\ell k}$ for $0\le\ell\le3$. Their common
color on $H$ and (3) imply

$$
|x_0x_1|=|x_1x_2|=|x_2x_3|,
\qquad |x_0x_2|=|x_1x_3|.
$$

They occur in convex cyclic order. The successive triangles
are congruent with the same orientation, so an orientation-preserving
isometry $T$ sends $x_0,x_1,x_2$ to $x_1,x_2,x_3$.
It is not a translation, since the first three points are
noncollinear. Thus $T$ is a nontrivial rotation.

Let $b$ be the common row value on $J$ and put $z_j=p_{a+j}$.
For $u+2k\le j\le v$ and $\ell=0,1,2$, (3) gives

$$
|z_{j+k}-x_{\ell+1}|
=d_{j-\ell k+b}
=|z_j-x_\ell|.
$$

The point $Tz_j$ has the same three distances to the
noncollinear anchors $x_1,x_2,x_3$, so uniqueness of
intersection with three prescribed-radius circles gives

$$z_{j+k}=Tz_j. \tag{4}$$

An interval of $\Omega_L(m)$ vertices is therefore partitioned,
by index modulo $k$, into at most $k=O_L(1)$ rotation orbits.
Each nonsingleton orbit lies on a positive-radius circle.
The largest orbit has $\Omega_L(m)$ vertices, proving the theorem.

## Consequence: boundedly many diameter-inactive points

**Corollary.** Fix $t\ge0$. Along any sequence of $n$-point
sets in which at most $t$ points are not incident with a diameter
pair, $R(A)\to\infty$ as $n\to\infty$.

Suppose otherwise that $R(A)\le K$ on an unbounded subsequence.
Let $C$ be its $m\ge n-t$ diameter-active points. By
[constant_width](constant_width.md), these lie on a common
constant-width boundary. The pair budget gives

$$q(C)\le q(A)\le n/2+K\le m/2+t/2+K.$$

The theorem supplies a positive fraction of $C$, hence of $A$,
on one circle. The [circle-incidence theorem](circle_incidence.md)
then gives linearly many rare distances, a contradiction.

## Checks and remaining gap

The author checked (1)--(4), including zero diameter degrees,
the two palette cases, the shared endpoints of the short intervals,
cyclic indices, orientation of the anchor isometry, and its
propagation by three anchors, together with the combinatorial
selection and rotation argument; the argument is author-recorded. The finite
van der Waerden theorem and Altman's stated maximal-side lemma
are the external inputs.

For a merely positive-fraction subset $m=cn$, bounded rarity
only gives $q(C)\le n/2+O(1)$. Its excess over $m/2$ can be
linear in $n$, so the bounded row-error argument does not apply.
No proof makes an arbitrary bounded-rarity configuration have
only boundedly many diameter-inactive points. This is the
unresolved step, not a conclusion of the inverse theorem.
