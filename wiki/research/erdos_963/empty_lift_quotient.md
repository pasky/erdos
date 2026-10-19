---
name: research/erdos_963/empty_lift_quotient
title: 'A proved one-step empty lattice lift'
desc: Noncoherence permits one empty, normal simplex quotient preserving all vertices and heights; iteration to coherent dimension is unproved.
tags: []
sources: []
created: 2026-09-19T02:15:34Z
updated: 2026-09-19T02:15:34Z
---


# A proved one-step empty lattice lift

***

For a positive integer set $P=\{a_1,\ldots,a_n\}$, recall that
coherence means that $\mathbf1$ is a vertex of

$$
\operatorname{conv}\{u\in\mathbb Z_{\ge0}^n:a\cdot u=\sum_i a_i\}.
$$

Let $c(P)$ be the largest coherent-subset size. Coherence implies
dissociation, so $c(P)\le d(P)$.

An empty lattice polytope has no lattice points other than its vertices.
The following is a proved construction, not a construction in dimension
$c(P)$ for general $P$.

## One-step quotient theorem

**Theorem.** If $P$ is noncoherent, there is an empty lattice polytope
of dimension $n-1$ with $n+1$ vertices, together with an integer linear
functional taking the values $0,a_1,\ldots,a_n$ on those vertices.
The polytope has a unimodular triangulation that is a star at the
height-zero vertex, and is normal.

### A relation with one unit-coefficient side

Take a nontrivial convex decomposition

$$
\mathbf1=\sum_\nu \theta_\nu u^{(\nu)},\qquad
\theta_\nu>0,\quad \sum_\nu\theta_\nu=1,
$$

in the integer fiber, with all $u^{(\nu)}\ne\mathbf1$. Put
$r^{(\nu)}=u^{(\nu)}-\mathbf1$. Each entry is at least $-1$, and
$a\cdot r^{(\nu)}=0$.

There exists one such $r$ with $\sum_i r_i\le0$ for which the affine
relation

$$
v=(v_0,v_1,\ldots,v_n)
   =\left(-\sum_i r_i,r_1,\ldots,r_n\right)                 \tag{1}
$$

has at least two positive and two negative entries. Every negative
entry is $-1$.

To prove this, first suppose some participating $u$ has degree less
than $n$. Then $v_0>0$, and positivity of $a$ forces $r$ to have a
positive entry too. If $r$ had only one negative entry, its total
positive coefficient sum would be less than one, which is impossible
in a nonzero relation on positive weights. Thus both sides have at
least two entries.

Otherwise every participating point has degree at least $n$; their
average degree is $n$, so all have degree exactly $n$. If every
associated $r$ had only one positive entry, say $r_j=m$, its negative
entries would be $-1$ on a set $J$ of size $m$. The case $m=1$
would equate two distinct weights, so $m\ge2$, and

$$
ma_j=\sum_{i\in J}a_i.
$$

Strict convexity of the square function gives

$$
\sum_i a_i^2r_i=ma_j^2-\sum_{i\in J}a_i^2<0.
$$

This contradicts the fact that the weighted average of these $r$ is
zero. Hence some $r$ has at least two positive entries; degree equality
then gives at least two negative entries as well. This proves the claim.
In particular, $r$ is primitive because it has entries equal to $-1$.

### The quotient polytope

Let

$$
\Lambda=\mathbb Z^n/\mathbb Zr,\qquad
Q=\operatorname{conv}(\bar0,\bar e_1,\ldots,\bar e_n)
    \subset\Lambda\otimes\mathbb R.
$$

Primitivity makes $\Lambda$ a free lattice of rank $n-1$. The height
$x\mapsto a\cdot x$ descends to $\Lambda$.

The entire space of affine relations on the $n+1$ displayed points
is spanned by (1). As its positive and negative supports both have
size at least two, no displayed point lies in the convex hull of the
others and no two coincide. Thus all $n+1$ points are vertices.

Let $J=\{j:v_j=-1\}$. The simplices obtained by deleting one vertex
$j\in J$ form a unimodular triangulation of $Q$. Indeed, for any
barycentric vector $\lambda\ge0$ with $\sum\lambda_i=1$, replace it by

$$
\lambda+t v,\qquad t=\min_{j\in J}\lambda_j.
$$

Its entries remain nonnegative, its sum remains one, and at least one
negative-side coordinate becomes zero. This proves coverage.

For the intersection assertion, suppose $\lambda_j=0$, $\mu_k=0$,
and $\mu-\lambda=t v$ represent a point in the two simplices. At
coordinate $j$ nonnegativity gives $t\le0$; at coordinate $k$ it gives
$t\ge0$. Hence $t=0$, and both omitted coordinates vanish. Their
intersection is exactly the common face.

Each simplex is affinely independent and unimodular. The coefficient
$v_j=-1$ expresses the omitted vertex as an integral affine combination
of the retained ones, so the retained vertices generate the entire
affine lattice. Every lattice point of $Q$ lies in a unimodular simplex
and is consequently one of its vertices. This proves emptiness.
The same triangulation proves normality: a lattice point in $mQ$
has nonnegative integer barycentric coefficients of total $m$ in
one of the dilated unimodular simplices.
Also $v_0\ge0$, so no simplex deletes the height-zero vertex; the
triangulation is a star there.

## Relation to the target and exact gap

An empty lattice polytope in dimension $k$ has at most $2^k$ vertices:
two vertices of the same parity would have a lattice midpoint that
is not a vertex. Therefore an empty lattice lift of the heights
$\{0\}\cup P$ in dimension at most $c(P)$ would establish

$$
|P|\le2^{c(P)}-1\le2^{d(P)}-1.
$$


The theorem supplies such a lift when $c(P)=n-1$; the standard simplex supplies
one when $c(P)=n$. **Arbitrary greedy iteration is false.** The exact example in
[[research/erdos_963/global_lift_gap|the global lift note]] has $c(P)=3$ and a
valid normal, star-triangulated first quotient in dimension four which admits no
further empty, vertex-preserving height projection. A different first quotient
does reach dimension three. Thus compatible choices, or replacement of earlier
relations, are essential.

The substantive next question is whether a minimum-dimensional empty
lift (or one with a unimodular triangulation) must have dimension at
most $c(P)$. This is an additional unproved statement, not an established
duality. “Minimum-dimensional” here must mean a global minimum, not
minimality under further projections of a fixed lift.
The same new note strengthens the one-step lift to a Boolean-coordinate
lift, but does not prove that this construction can be iterated.
The failed minimum- and maximum-element exchange principles in
[[research/erdos_963/convex_route_obstructions|the obstruction note]] do not supply it.

## An exact criterion for an empty lift in dimension three

Let $S\subset\mathbb Z$ contain zero, with $5\le|S|\le8$.
For a block $B$ of at least two heights, write
$g(B)=\gcd\{b-b':b,b'\in B\}$. There is an empty
three-dimensional lattice lift of these heights if and only if
$S$ has a partition $B_0\sqcup B_1$ with the following properties:

* Each block has at most four elements.
* In a four-element block $b_1<b_2<b_3<b_4$,
  $b_1+b_4=b_2+b_3$.
* If both blocks have at least three elements, their $g$-values agree.
* If one block has two elements and the other at least three, the
  latter's $g$-value divides the former's difference.

A singleton imposes no gcd condition. These are all cases, since
there are at least five heights.

For necessity use Howe's width-one theorem, in the source passage already
checked in [[research/erdos_963/global_lift_gap|the global lift note]]. All
vertices occupy two consecutive lattice planes. An empty triangle is unimodular,
and an empty quadrilateral is a unimodular parallelogram. Hence a block of at
least three vertices generates the entire plane difference lattice; its height
differences generate the image of that lattice under the height functional. Both
such blocks therefore have the same gcd. A two-point block is a primitive
segment, whose height difference is a multiple of that image generator. The
parallelogram gives the displayed pair-sum identity.

For sufficiency label the blocks so that $0\in B_0$, take the
generator $g$ from a block of at least three elements, and put
the plane height functional equal to
$g x$ on $\mathbb Z^2$. For a triangle, its two normalized
differences are coprime, so Bézout's identity makes them the first
coordinates of a unimodular basis. For a four-block use the
two differences from its smallest element to its middle elements;
their sum is the difference to the largest. The same construction
gives a unimodular parallelogram. A segment of normalized height
difference $t$ uses primitive direction $(t,1)$. Put the blocks
in layers $z=0,1$, and choose the third height coefficient to
match their offsets. Every lattice point in the resulting convex
hull lies in one of the two layers, where emptiness is already
proved. The layer with at least three vertices and the other
nonempty layer give dimension three. Finally translate the
height-zero vertex to the origin.

This criterion controls emptiness, not normality. It supplies a
finite arithmetic test in dimension three, but no proof that
$c(P)=3$ always forces the required partition of $\{0\}\cup P$.
