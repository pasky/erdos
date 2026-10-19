---
name: research/erdos_774/lemmas/private_conductor_lifts
title: Collision-free private lifts and their color limitation
desc: Private projections permit shared conductors and an exact relation-preserving lift, but that lift always has two rationally independent colors.
tags: [E0774, proved, algebra, obstruction]
sources: []
created: 2026-09-18T02:38:00Z
updated: 2026-09-18T02:38:00Z
---


# Collision-free private lifts and their color limitation

***

## Standing

Pairwise coprime conductors are sufficient but not necessary in
[determinant flattening](../routes/bounded_height_flattening.md).
This page removes that formal restriction under an exact injectivity
hypothesis. It does not remove the requirement of one actual support color.
All arguments are algebraic and use no computation.

## Private projections suffice

Let $M,n_1,\ldots,n_r$ be pairwise coprime, and let
$X_i\subset\mu_{Mn_i}$. If projection of $X_i$ to its private
$\mu_{n_i}$-coordinate is injective, multiplication on
$X_1\times\cdots\times X_r$ is injective: project an equality of
products onto $\mu_{n_i}$ to recover its $i$-th factor.

The existing determinant proof therefore works for factors sharing the entire
conductor $M$, provided their private projections are injective and the
surviving determinant support is monochromatic. The disjoint magnitude groups
still make different matching blocks disjoint.

## A universal exact lift

Given finite $X\subset\mu_M$, assign to each $x$ a distinct odd
prime $p_x\nmid M$, and put
$$
L_x=\{x\zeta_{p_x}^{\,j}:1\leq j<p_x\},\qquad
L(X)=\bigcup_{x\in X}L_x.
$$
Its integral relations are exactly
$$
b_{x,j}=a_x\text{ for all }j,
\qquad \sum_{x\in X}a_xx=0.
\tag{1}
$$

To prove this, fix $x$ and let $F$ be the compositum of the old conductor
field and all private-prime fields other than the $p_x$-field. The
$p_x-1$ nonidentity $p_x$-th roots are an $F$-basis, by the
coprime cyclotomic degree formula. Write all other terms of a relation as
one $u\in F$, and use $1=-\sum_{j=1}^{p_x-1}\zeta_{p_x}^j$.
The coefficient equations $xb_{x,j}-u=0$ make all $b_{x,j}$ equal.
Do this for each block; their sums are $-a_xx$, proving (1).
The converse follows from the same root-sum identity.

Thus the entire integer relation lattice, primitivity, and coefficient heights
are preserved by coefficient duplication. The private projection is injective:
the order of a private component identifies its prime $p_x$, hence its
block, and then its exponent identifies the point. Independently lifted
factors can share all old conductor primes and still have injective products.

**Color limitation.** The lift is always the union of two rationally
independent sets. Color one point of every $L_x$ red and its nonempty
remainder blue. Equation (1), also for rational relations after clearing
denominators, forces every nonzero relation to use all points of some block.
Neither color does so. Exact preservation of the integer kernel therefore
does not preserve chromatic forcing.

Moreover a proper dissociated coloring cannot preserve the color of $x$
on every member of $L_x$, since
$x+\sum_{y\in L_x}y=0$ would be monochromatic.

## Why prime powers and translations do not supply automatic copies

Put $R=\operatorname{rad}(N)$. The $N/R$ representatives of
$\mu_R$-cosets in $\mu_N$ span
$\mathbb Q(\zeta_N)$ over $\mathbb Q(\zeta_R)$. That extension
has degree $\varphi(N)/\varphi(R)=N/R$, so the representatives form
a basis. Every rational relation therefore separates by these cosets.
For every coefficient height $h$,
$$
\chi_h(\mu_N)=\chi_h(\mu_R).
$$
Restriction proves one inequality; using the same proper palette in all the
additively independent rotated cosets proves the other.

An irredundant relation lies in one such coset. If $r$ such supports
in this fixed prime-power tower have injective products, normalizing each by
its coset representative puts every product in $\mu_R$, so
$\prod_i|X_i|\leq R$. Arbitrarily high prime powers do not give new
multiplicatively independent copies of the old relation.

Scalar translations do not repair collisions either:
$\prod_i(t_ix_i)=\prod_i(t_iy_i)$ if and only if
$\prod_i x_i=\prod_i y_i$. For translates of one fixed grouped
relation, the formal group-ring rows are scalar monomial multiples of the
same row; their determinant is identically zero even before evaluation.
There need not be a nonzero formal support left to color.

## Fresh private primes force growing supports

Normalize an irredundant relation into its squarefree relative conductor.
For an active prime $p$, grouping by its $p$-coordinate makes all
$p$ layer sums equal over the other-prime field. If one layer is empty,
all sums vanish; more than one occupied layer would split the relation.
Thus an active prime has all $p$ layers occupied and the support has
at least $p$ points.

In particular, an irredundant relation whose private projection is injective
and whose private primes all exceed $B$ has more than $B$ points.
Some private coordinate must vary, since a one-point relation is impossible.
Fixed-size relation copies cannot be moved into arbitrarily fresh private
primes. This explains another loss in whole-support profile focusing, but
does not prove that all adaptive focusing must fail.
