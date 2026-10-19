---
name: research/erdos_132/order_type_relaxations
title: What projection order and crossing inequalities omit
desc: |
  Affine sweeps and finite-alphabet Monge blocks omit metric rank;
  isosceles counting gives a necessary but insufficient surplus for R equal to one.
sources: []
research_state: closed
created: 2026-09-23T01:43:51Z
updated: 2026-09-24T22:12:56Z
---


# What projection order and crossing inequalities omit

***

These are checks of a new sweep/order approach, not a solution of
[Problem 132](../../problems/distance_problems/E0132/_index.md).

## An affine sweep can have all distances rare

Every finite planar configuration admits an orientation-preserving
affine image with the same order type and cyclic projection-sweep
sequence, up to reparametrizing the direction, in which all distances
are rare.

Let $v,w$ range over its nonzero difference vectors with $v\ne\pm w$.
Choose a positive-definite symmetric matrix $H$ avoiding all finitely
many hyperplanes

$$v^{\mathsf T}Hv=w^{\mathsf T}Hw.$$

Each hyperplane is proper because $vv^{\mathsf T}\ne ww^{\mathsf T}$.
With $T=H^{1/2}$, equal distances in $T(A)$ therefore correspond
only to a single displacement up to sign. The graph for such a
displacement is a disjoint union of finite translation paths, so
has at most $n-1$ edges.

The determinant of $T$ is positive, preserving orientation signs.
Projection of $T(A)$ in direction $u$ is projection of $A$ in
direction $T^{\mathsf T}u$. The induced map on the direction circle
preserves cyclic order, including simultaneous crossings. Thus the
sweep ordering does not retain the equal-length amplitudes.
This does not prove that all order-type methods must fail; it
identifies information that cannot be discarded.

Unlike the [equality-preserving affine criterion](affine_deformations.md),
this deformation can split the original distance classes. It gives
no lower bound for $R(A)$ from the transformed configuration.

## Few-valued strict Monge matrices need not be Euclidean

Crossing diagonals in a convex quadrilateral have greater total
length than either pair of opposite sides. Opposite-chain distance
blocks consequently satisfy Monge inequalities, with the sign
depending on column orientation. These inequalities and a linear
number of distinct entries alone do not impose Euclidean rank.

For $1\le i,j\le h$ and $L>0$, set

$$D_{ij}=L+(i-j)^2+\tfrac14\delta_{ij}.$$

This matrix has exactly $h$ distinct entries. For $i<i'$ and
$j<j'$,

$$D_{ij}+D_{i'j'}-D_{ij'}-D_{i'j}
=-2(i'-i)(j'-j)+E,\qquad |E|\le\tfrac12,$$

so it is strictly Monge. Reversing the columns reverses the sign.
Nevertheless its entrywise squared matrix satisfies

$$\operatorname{rank}(D^{\circ2})\ge h-5.$$

Indeed, the matrix $P_{ij}=(L+(i-j)^2)^2$ has rank at most five,
by expansion in the row powers $1,i,\ldots,i^4$, while

$$D^{\circ2}=P+(L/2+1/16)I.$$

The latter scalar is nonzero, and the rank inequality gives the
claim. A planar bipartite squared-distance matrix has rank at most
four, since

$$|p_i-q_j|^2=|p_i|^2+|q_j|^2-2p_i\cdot q_j.$$

For $h\ge10$ the displayed Monge matrix cannot be such a distance
matrix. Taking $L\ge h^2$ even puts all its entries within a factor
of two. This is an obstruction to the scalar relaxation, not a
nonexistence result for actual planar configurations with few distances.

## Limits of distinct-entry inductions for Monge matrices

The [nonlinear collision approach](nonlinear_cluster_limits.md) raised
the separate question whether a strictly Monge $b\times b$ matrix must
have at least $b$ distinct entries. This was neither proved nor refuted.
The following abstract-matrix checks delimit proposed proofs; they are
not planar configurations or counterexamples to Problem 132.

First, neither a row with $b$ distinct values nor a monochromatic-forest
argument is available. The matrix

$$\begin{pmatrix}-1&0&0\\0&1/2&0\\0&0&-1\end{pmatrix}$$

is strictly Monge (all four adjacent defects are $-1/2$), but every row and
column has only two values. Its zero entries form a bipartite six-cycle. A
[three-point analytic collision example](nonlinear_cluster_limits.md) also rules
out the corresponding fully distinct pinned-distance shortcut for actual
Euclidean clusters.

Second, an induction deleting one row and one column to remove an
extreme entry fails. Consider

$$\begin{pmatrix}
0&5&4&11&9&13\\
5&9&7&13&10&13\\
0&3&0&5&1&3\\
11&13&9&13&8&9\\
7&8&3&6&0&0\\
13&13&6&8&1&0
\end{pmatrix}.$$

Its adjacent rectangle defects are all $-1$, except the defect with
upper-left position $(5,2)$, which is $-2$. Every general rectangle
defect is a sum of adjacent defects, proving strict Monge. Minimum
positions include $(1,1),(3,3),(5,5)$, and maximum positions include
$(2,6),(4,4),(6,2)$. Neither support can be covered by one row and
one column. The author checked this finite integer certificate directly.

There is an exact alternative formulation of the unresolved entry-count
question. For a strictly Monge matrix $M$, the matrix
$E(t)=(e^{-tM_{ij}})$ is totally positive for all sufficiently large
$t$. In each minor, uncrossing an inversion strictly decreases the sum
of the selected $M$ entries. The diagonal permutation is therefore the
unique minimum-cost permutation. Its positive determinant term dominates
the finite exponential sum for large $t$. Conversely, minus the
entrywise logarithm of a totally positive matrix is strictly Monge by
its positive $2\times2$ minors. These transformations preserve the
number of distinct entries. Thus the question is equivalent to asking
whether a totally positive $b\times b$ matrix must have at least $b$
distinct entries. This equivalence does not supply that lower bound.

Small numerical optimizations conducted during the exploration are not
being treated as exact classifications or as proofs of additional orders.

## A necessary isosceles surplus under R equal to one

Let $d_r(p)$ be the distance-$r$ degree of $p$, and put

$$I(A)=\sum_r\sum_{p\in A}\binom{d_r(p)}2.$$

This counts isosceles triples with a distinguished apex and an
unordered base; an equilateral triangle contributes three.
If $R(A)=1$, then

$$I(A)\ge
\begin{cases}
\binom n2+n-3,&n\text{ odd},\\
\binom n2+3n/2-4,&n\text{ even}.
\end{cases} \tag{1}$$

Write $M=\binom n2$, $q=q(A)$, and let the diameter have $e$ pairs.
Every other class is rich. The elementary integer inequalities
$\binom d2\ge2d-3$ and $\binom d2\ge d-1$ give

$$I(A)\ge4(M-e)-3n(q-1)+2e-n
=4M-2e-3nq+2n. \tag{2}$$

The pair budget gives $q\le\lfloor n/2\rfloor$. For odd $n$ at
$q=(n-1)/2$, it also gives $e\le(n+3)/2$; substituting in (2)
proves (1). If $q\le(n-3)/2$, use $e\le n$ in (2) to obtain
the stronger $I(A)\ge M+3n$.

For even $n$ at $q=n/2$, the exact spectrum is one diameter pair
and $n+1$ pairs in each of the other $n/2-1$ classes. Each rich
class contributes at least $4(n+1)-3n=n+4$ to $I(A)$; the
diameter contributes zero. This gives
$(n/2-1)(n+4)=M+3n/2-4$. For smaller $q$, (2) gives the
stronger bound $M+3n/2$.

If $k_{ab}$ is the number of points of $A$ on the perpendicular
bisector of $ab$, then $I(A)=\sum_{\{a,b\}}k_{ab}$ and

$$\sum_{\{a,b\}}\binom{k_{ab}}2\ge I(A)-M.$$

Thus a counterexample requires linearly many choices of a base
and two equidistant apices. This does not force a line containing
many points: the count could be spread over many bisectors with
exactly two apices. No geometric argument concentrating that surplus
was established.

The author checked the affine hyperplanes, sweep reparametrization,
Monge and rank calculations, and both parity cases in (1); the argument
is author-recorded.
