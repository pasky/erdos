---
name: research/erdos_774/lemmas/decomposable_cycle_colors
title: Three colors split every decomposable flat simplicial cycle
desc: Balanced totally unimodular Plucker matrices admit a controlled support count, proving simultaneous three-color avoidance of all simple-wedge ternary cycles when log n=o(k).
tags: [E0774, simplicial, coloring, proved, scoped-obstruction]
sources: []
created: 2026-09-19T01:50:00Z
updated: 2026-09-19T01:50:00Z
---


# Three colors split every decomposable flat simplicial cycle

***

## The theorem

Suppose $k\to\infty$, $k<n$, and $\log n=o(k)$. Eventually
there is a three-coloring of $\binom{[n]}k$ with no monochromatic
support of a nonzero **decomposable** ternary vector in

$$
K_{n,k}=\ker\partial=\bigwedge^k A_{n-1}.
$$

Here decomposable means one simple exterior product, not a sum of such
products. The lattice identification is proved in the
[simplicial extraction theorem](../routes/simplicial_extraction.md).
This result applies at its fixed-$C$ critical scale. It does **not**
color arbitrary flat cycles; it shows that simple-wedge supports alone
cannot force unbounded coloring. The stronger two-color result for the
smaller [joined-boundary family](joined_boundary_colors.md) remains valid.

## 1. Flat simple wedges give balanced TU matrices

Take a nonzero decomposable ternary $k$-vector $x\in K_{n,k}$ and
an index $I$ with $x_I\ne0$. Change its global sign to make $x_I=1$,
order $I$ first, and normalize its Plucker matrix to

$$
[I_k\mid D].                                     \tag{1}
$$

Every square minor of $D$ is, up to sign, a maximal minor of (1),
by adjoining the appropriate identity columns. All are therefore
$0,\pm1$; in particular $D$ is an integral totally unimodular
matrix. Delete inactive extra columns, leaving $a$ nonzero columns.

Writing $u=\sum_{v=1}^n e_v$, the cycle condition is $\iota_u x=0$.
If $x=v_1\wedge\cdots\wedge v_k\ne0$, the $k$ wedges obtained by
omitting one factor are independent. The contraction formula therefore
forces each $\langle u,v_i\rangle=0$. Thus the underlying plane is
in $u^\perp$, and its normalized rows obey

$$
D\mathbf1=-\mathbf1.                            \tag{2}
$$

There are no zero rows, and $a\geq1$. The support $T$ of $x$
is exactly the family of column bases of (1).

## 2. Count of balanced TU matrices on one support pattern

Two TU signings of the same zero-pattern differ by row and column
switches. Here is an elementary proof. A chordless cycle in the
bipartite row-column support graph induces a square submatrix with
exactly two nonzero determinant terms. Total unimodularity forces their
cancellation; otherwise the determinant would have magnitude two.
Consequently the entrywise ratio of two signings has product one around
every chordless cycle. Splitting cycles at chords gives the same property
on every cycle. Define vertex signs by multiplying edge ratios along
paths from one chosen vertex in each component. Cycle products make the
definition consistent and express each edge ratio as the product of its
endpoint signs.

Fix one TU signing $D_0$. Every other signing consequently has the form

$$
D=\operatorname{diag}(r)D_0\operatorname{diag}(c).
$$

There are $2^a$ choices of column signs $c$. For each, equation (2)
determines every row sign uniquely if it is possible at all: the
corresponding row sum must be nonzero and become $-1$. Hence there
are at most $2^a$ balanced TU signings of a fixed pattern, and at most

$$
2^{ka+a}                                         \tag{3}
$$

normalized matrices for fixed $I$ and fixed active extra vertices.

## 3. Every such support has at least $ka$ bases

Let the bipartite support graph of $D$ have components with positive
row and column counts $k_j,a_j$. Their sums are $k,a$. Bases factor
over the corresponding blocks of (1).

In a connected component, choose one shortest path from each basic row
to each extra column. A shortest path is induced. It has equally many
row and column vertices and its induced square submatrix has a unique
perfect matching, so determinant $\pm1$. Replacing the identity
columns for its row set by its extra-column set therefore gives a basis.
Different endpoint pairs give different bases: the exchanged row and
column sets recover the induced path, and hence its endpoints. Along
with the original identity basis, this supplies at least $k_ja_j+1$
bases in the component. Thus

$$
|T|\geq\prod_{j=1}^t(k_ja_j+1).                  \tag{4}
$$

For $k\geq4$, the right side is at least $ka$. For $t=1$ this
is immediate. For $t\geq2$, use

$$
k_ja_j+1\geq\frac{(k_j+1)(a_j+1)}2,
\quad
\prod_j(k_j+1)\geq2^{t-1}(k-t+2),
$$

and the analogous inequality for $a_j$. Concentrating all excess above
one in one summand proves the second inequality. It follows that

$$
\prod_j(k_ja_j+1)\geq2^{t-2}(k-t+2)(a-t+2).       \tag{5}
$$

For $t=2$ this equals $ka$. For $t\geq4$, division by $ka$
and $k,a\geq t$ give a ratio at least $2^t/t^2\geq1$.
For $t=3$, use $k\geq4,a\geq3$: the ratio is at least
$2(1-1/4)(1-1/3)=1$. This proves

$$
|T|\geq ka.                                      \tag{6}
$$

Separately $|T|\geq k+1$, since each basic row has a nonzero entry,
giving $k$ distinct single-exchange bases besides the original basis.

## 4. Simultaneous three-color avoidance

Put

$$
\lambda=\tfrac12(\log2+\log3),\quad
\Delta=\lambda-\log2=\log3-\lambda>0,
\quad x_T=e^{-\lambda|T|}.
$$

Use distinct support events, not separate events for different orientations.
For a fixed face $I$, the choice of $a$ active extra vertices has
at most $n^a$ possibilities. Equations (3) and (6) imply

$$
L:=\max_I\sum_{T\ni I}x_T
\leq\sum_{a\geq1}n^a2^{ka+a}e^{-\lambda ka}
=\sum_{a\geq1}(2n e^{-\Delta k})^a=o(1).         \tag{7}
$$

Color faces independently with three equiprobable colors. A support
of size $s$ is monochromatic with probability $3^{1-s}$. Support
intersection is a dependency graph, and $x_T\leq1/2$ eventually.
Using $\log(1-x)\geq-2x$, its neighbor product is at least
$e^{-2sL}$. The asymmetric local-lemma inequality holds if

$$
\log3\leq s(\Delta-2L),
$$

which follows uniformly from $s\geq k+1\to\infty$ and (7).
[Moser--Tardos, Theorem 1.1](../../../../library/set_systems/moser_tardos_2009_constructive_proof_general_lovasz_local_lemma/_index.md),
checked after its digest, gives the required coloring.

## Review and remaining target

The normalization from real decomposability, the TU signing argument,
shortest-path basis injection, the component-product edge case, and all
local-lemma constants are author-recorded; a separate reviewer checked
them. No computation or representation-theoretic theorem is used.

In the particular coloring obtained here, every monochromatic flat cycle
must be nondecomposable. No claim is made about all colorings or all
cycle supports. A color-adaptive nondecomposable cycle theorem would be
needed to continue this simplicial route.
