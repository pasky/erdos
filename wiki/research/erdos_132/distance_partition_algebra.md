---
name: research/erdos_132/distance_partition_algebra
title: Algebraic distance partitions and exact-spectrum symmetry tests
desc: |
  Exact-spectrum symmetry tests and three-dimensional countermodels
  expose the missing planar condition in uncentered rank-four arguments.
sources: []
research_state: closed
created: 2026-09-22T22:45:00Z
updated: 2026-09-24T22:12:56Z
---


# Algebraic distance partitions and exact-spectrum symmetry tests

***

These observations do not settle either assertion of
[Problem 132](../../problems/distance_problems/E0132/_index.md).

## A centered planar moment identity

Write $S_1=\sum_{i<j}|p_i-p_j|^2$ and
$S_2=\sum_{i<j}|p_i-p_j|^4$. Translate the centroid to zero, put
$S=\sum_i|p_i|^2$, and let $\lambda_1,\lambda_2$ be the eigenvalues of
$M=\sum_i p_i p_i^{\mathsf T}$. Direct expansion, using
$\sum_i p_i=0$, gives


$$
S_1=nS,\qquad
S_2=n\sum_i|p_i|^4+S^2+2\operatorname{tr}(M^2).
$$


Since $\lambda_1+\lambda_2=S$, this yields the exact identity


$$
S_2-\frac{3S_1^2}{n^2}
=n\sum_i\left(|p_i|^2-\frac Sn\right)^2
+(\lambda_1-\lambda_2)^2\ge0. \tag{M}
$$


Equality means that all points have the same distance from their centroid
and their second-moment matrix is scalar. In terms of the degree-profile
functional $s_i=\sum_j|p_i-p_j|^2=\sum_r r^2d_r(i)$, the first term on
the right is $n^{-1}\sum_i(s_i-2S_1/n)^2$. It controls one weighted
functional, not equality of the full rich-degree profiles.

The two three-dimensional countermodels below fail (M): their
$(S_1,S_2)$ values are respectively $(32,416/5)$ and $(36,96)$, with
$n=6$. Thus (M) detects a missing planar restriction in those examples.
It still does not rule out abstract one-rare shell data. For $n=6$,
multiplicities $(7,7,1)$ at radii $(1,3/2,9/4)$ give


$$
S_1=445/16,\quad S_2=17425/256,\quad
36S_2-3S_1^2=33225/256>0.
$$


All consecutive ratios are below two, so the
[spectral-gap test](spectral_gaps.md) also permits these abstract data. No
planar realization is claimed. The author checked the expansion and the
arithmetic, which are author-recorded; no implication from richness to a small
defect in (M) has been proved.

## What the resultant and operator reformulations give

Identify the distinct points with $z_1,\ldots,z_n\in\mathbb C$ and put

$$f(z)=\prod_i(z-z_i).$$

The difference polynomial is

$$
D(w)=\prod_{i\ne j}\bigl(w-(z_i-z_j)\bigr)
     =\frac{\operatorname{Res}_z(f(z),f(z+w))}{w^n}.
$$

Its roots on the centered circle of radius $r$, counted with
multiplicity, number $2m_A(r)$. Each circle factor is self-inversive
after scaling its circle to the unit circle. This is automatic for
any polynomial whose roots lie on a circle; it adds no restriction
on the distance multiplicities. No useful identity between different
circle factors, beyond their common difference-resultant origin, was
obtained.

Equivalently, set $Z=\operatorname{diag}(z_1,\ldots,z_n)$ and consider
the positive self-adjoint operator on complex matrices

$$L(X)=[Z^*,[Z,X]].$$

For a matrix unit,

$$L(E_{ij})=|z_i-z_j|^2E_{ij}.$$

Thus its kernel has dimension $n$, and the eigenspace for $r^2>0$
has complex dimension $2m_A(r)$.

The subspace of matrices with zero row and column sums has codimension
$2n-1$. A rich eigenspace therefore meets it nontrivially. But this
supplies only linear flows supported on the distance graph, not
real edgewise equilibrium stresses. In particular it does not give
sign-controlled coefficients satisfying

$$\sum_j\omega_{ij}(p_i-p_j)=0.$$

No spectral inequality for $L$ proving the required multiplicity
statement was established. Treating this dimension intersection as
such an inequality would leave the same missing stress inference as
in the [variational reduction](variational_reduction.md).

## A forced spectrum at the even counting boundary

Suppose $n=2m$ and the set has exactly $m$ distances and $R(A)=1$.
Since the diameter is rare, the pair budget forces the exact spectrum

$$
(\underbrace{2m+1,\ldots,2m+1}_{m-1\text{ classes}},1). \tag{1}
$$

Indeed, its minimum possible total is
$(m-1)(2m+1)+1=m(2m-1)=\binom{2m}{2}$.
In particular the diameter is attained uniquely and every class has
odd multiplicity.

The checked [small-order argument](small_orders.md) uses (1) together
with both endpoint deletions and the few-distance classifications to
exclude $R=1$ for $n=6,8,10$, without a symmetry assumption. Together
with the odd-order checks, this settles every $5\le n\le10$.
The later [unique-diameter theorem](unique_diameter_obstruction.md)
excludes (1) in the plane at every even order $n\ge5$. In particular,
combined with exclusion of the twelve-point five-distance type, it
settles order twelve. The matrix obstructions below remain valid
examples in higher dimension, not outstanding planar candidates.

### Central symmetry is impossible for $n\ge6$

Assume also $A=-A$ after translation. Since $n$ is even, zero is
absent, and write

$$A=\{\pm u_1,\ldots,\pm u_m\}.$$

The half-turn pairs all non-antipodal unordered edges. Its fixed
edges are the $m$ antipodal pairs. Each of the $m$ distance classes
in (1) has odd cardinality, so contains an odd, positive number of
fixed edges. Therefore each contains exactly one antipodal pair.
The radii $r_i=|u_i|$ are consequently distinct; order them increasingly.
Every distance in $A$ equals some $2r_i$.

For $i<j$,

$$|u_i\pm u_j|<2r_j.$$

Thus both lengths belong to $\{2r_1,\ldots,2r_{j-1}\}$.
Writing $s_i=r_i^2$, the parallelogram identity gives

$$s_i+s_j=2(s_a+s_b) \tag{2}$$

for some $a,b<j$. Taking $(i,j)=(1,2)$ gives $s_2=3s_1$.
For $j=3$, equation (2) with $i=1$ requires

$$s_3/s_1\in\{3,7,11\},$$

while the same equation with $i=2$ requires

$$s_3/s_1\in\{1,5,9\}.$$

The sets are disjoint. Hence $m\ge3$ is impossible.
The four-point unit rhombus shows why $m=2$ cannot be excluded.

### A reflection without fixed points is impossible

Under (1), suppose $m\ge2$ and a reflection preserves $A$ but its axis
contains no point of $A$. The $m$ reflection-fixed unordered edges
are the pairs of mirrored points. The same parity argument assigns
exactly one to each distance class.

Let their positive heights above the axis be
$0<h_1<\cdots<h_m$. The distance set is exactly
$\{2h_1,\ldots,2h_m\}$, with $2h_m$ the unique diameter.
But a point at height $h_m$ and the reflected point at height
$-h_{m-1}$ have distance at least

$$h_m+h_{m-1}>2h_{m-1}.$$

This is not the unique diametral pair, and there is no other allowable
length above $2h_{m-1}$. This is a contradiction.

## Limits of the symmetry arguments

These exclusions assume both $q=n/2$ and an actual Euclidean symmetry.
They do not cover $q<n/2$, odd $n$, or asymmetric configurations.
Neither rank four of the Euclidean distance matrix nor the
multiplicities in (1) were shown to force an involution. No such
symmetry inference should be used without a separate proof.

## Uncentered distance-matrix rank does not enforce planarity

The unrestricted attempt checked a specific failure of an algebraic
relaxation. For a squared Euclidean distance matrix $D$, the necessary
bound $\operatorname{rank}D\le4$ is not sufficient for a planar
realization, even if one also imposes conditional negative definiteness,
the required multiplicity pattern, and a unique diameter.

### The exact even-boundary spectrum in three dimensions

Let $u=(0,0,1)$, $v=(0,0,-1)$, and take any four of the five points

$$p_j=\left(\frac2{\sqrt5}\cos\frac{2\pi j}{5},
            \frac2{\sqrt5}\sin\frac{2\pi j}{5},
            \frac1{\sqrt5}\right),\qquad0\le j<5.$$

All six points lie on the unit sphere. Put
$a=2-2/\sqrt5$ and $b=2+2/\sqrt5$. Their squared-distance
multiplicities are exactly

$$a:7,\qquad b:7,\qquad4:1. \tag{3}$$

Each of the four latitude points has squared distances $a,b$ to
$u,v$, respectively. The latitude pentagon has short and long chord
squares $a,b$, five pairs each; removing one vertex leaves three
of each. The pole pair has square four. Thus (3) is precisely the
forced $n=6,q=3,R=1$ spectrum, but in $\mathbb R^3$.

If $P$ is the matrix of point coordinates, then

$$D=2(\mathbf1\mathbf1^{\mathsf T}-PP^{\mathsf T}).$$

The columns of $[\mathbf1,P]$ are independent: the two poles kill
the constant and vertical coefficients of an affine relation, and
the latitude points kill the two horizontal coefficients. Hence
$D$ has rank four and inertia $(1,3)$. For $\mathbf1^{\mathsf T}x=0$,
$x^{\mathsf T}Dx=-2|P^{\mathsf T}x|^2\le0$.

This example fails a basic additional planar test: four points have
the same pair of pinned distances to the two poles. It also fails
hereditary diameter counting, since deleting $u$ leaves seven maximum
distance pairs on five points. It is not a planar counterexample.

### Rank four plus hereditary diameter structure still does not suffice

A complementary example is the six-point octahedron
$\{\pm e_1,\pm e_2,\pm e_3\}\subset\mathbb R^3$. Its squared-distance
spectrum is $(2:12,4:3)$, so $R=1$. The same matrix decomposition
gives rank four, inertia $(1,3)$, and conditional negative definiteness.

Every induced maximum-distance graph satisfies the hereditary restrictions
used in the layer notes. If an antipodal pair occurs, the maximum-distance
graph is a matching. Otherwise there is at most one vertex from each
antipodal pair, hence at most three vertices, all equidistant; the graph
is at most $K_3$. Thus the diameter edge bound, pseudoforest condition,
absence of even cycles, and at-most-one-cycle condition all hold.
This example does not have the exact spectrum (3). The two certificates
rule out different relaxations and should not be combined as though
one example satisfied all the listed conditions.

### The missing rank condition

With $H=I-\mathbf1\mathbf1^{\mathsf T}/n$, the exact Euclidean
dimension is

$$\operatorname{rank}(-HDH/2).$$

Planarity requires this centered rank to be at most two. Equivalently,
the bordered Cayley--Menger matrix has rank at most four. For a
Euclidean realization of affine dimension $d$, its rank is $d+2$:
after centering the coordinates, subtract the squared-norm multiples
of the first row and column, then separate the constant vector from
its orthogonal complement. The resulting blocks are a nonsingular
$2\times2$ block and the rank-$d$ centered Gram block.

The author checked both explicit spectra, the matrix decompositions, and the
induced-subset assertions; they are author-recorded. No inequality relating
centered rank two to the required distance-class multiplicities was established,
and no edgewise stress-sign conclusion follows from these certificates.
