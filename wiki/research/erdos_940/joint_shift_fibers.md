---
name: research/erdos_940/joint_shift_fibers
title: Simultaneous shifted representations remain critical
desc: The complete intersections for arbitrarily many distinct target shifts are normal and have ample anticanonical bundle; increasing the number of shifts gives no general-type obstruction.
tags: []
sources: []
created: 2026-09-23T02:10:00Z
updated: 2026-09-23T02:10:00Z
---


# Simultaneous shifted representations remain critical

***

## Statement and scope

A possible way to disprove cofiniteness was to demand representations
of many consecutive targets at once and force a higher-genus or
general-type obstruction. The following calculation rules out that
particular geometric argument. It is not a point-counting theorem.

Fix $r\ge3$, $L\ge2$, distinct rational numbers $h_1,\ldots,h_L$,
and forms in disjoint blocks of $r$ variables

$$
F_j(\mathbf x_j)=\sum_{i=1}^r a_{ji}x_{ji}^r,
\qquad a_{ji}\in\mathbb Q^\times.
$$

Let

$$
V:\quad F_j(\mathbf x_j)=n+h_j\quad(1\le j\le L).
$$

Eliminating $n$ and homogenizing gives

$$
X\subset\mathbb P^{rL}:\quad
F_j(\mathbf x_j)-F_1(\mathbf x_1)
=(h_j-h_1)z^r\quad(2\le j\le L).                       \tag{1}
$$


**Theorem.** The projective variety $X$ is geometrically integral,
normal, and a complete intersection, with

$$
\dim X=L(r-1)+1,\qquad
\omega_X\simeq\mathcal O_X(-r-1).                     \tag{2}
$$

The affine chart $V=\{z\ne0\}$ is smooth. Set-theoretically, the
singular locus of $X$ consists exactly of points with $z=0$ and
at least two entire root blocks zero. It is empty for $L=2$ and
has codimension $2r$ for $L\ge3$.

In particular $X$ is normal Gorenstein with ample anticanonical
bundle, for every $L$. Positivity of the coefficients is not needed
for these geometric statements.

## Complete intersection and integrality

Work over an algebraically closed characteristic-zero field $k$.
Order the equations in (1) by increasing $j$. Each is monic, up to a
nonzero scalar, in the previously unused variable $x_{j,r}$.
They form a regular sequence, giving the complete-intersection
dimension in (2) and Cohen--Macaulayness.

For integrality introduce $T$. The affine cone ring can equivalently
be written

$$
R=k[z,T,\mathbf x_1,\ldots,\mathbf x_L]/
   (F_j-T-h_jz^r:1\le j\le L).
$$

Eliminating $T=F_1-h_1z^r$ recovers the original cone ring. The
monic equations in the $x_{j,r}$ make $R$ finite free over

$$
k[z,T,(x_{ji})_{i<r}].
$$

It is therefore torsion-free over $A=k[z,T]$ and injects into its
generic fiber over $K=k(z,T)$. That generic fiber is the tensor
product of

$$
K[\mathbf x_j]/(F_j-(T+h_jz^r)).
$$

Each factor is geometrically integral: over an algebraic closure of
$K$, its degree-$r$ homogenization is a smooth diagonal hypersurface
in $\mathbb P^r$. Such a hypersurface is irreducible, since distinct
positive-degree components would meet and create singular points.
The tensor product is thus integral. Its subring $R$ is integral,
proving geometric integrality of $X$.

## The singular locus and normality

Put $d_j=h_j-h_1$. A dependency among the differentials of (1),
with coefficients $\lambda_j$ for $j\ge2$, satisfies

$$
\lambda_j\nabla F_j=0,\qquad
\left(\sum_{j\ge2}\lambda_j\right)\nabla F_1=0,\qquad
z^{r-1}\sum_{j\ge2}\lambda_jd_j=0.                    \tag{3}
$$

The gradient of a diagonal $F_j$ vanishes exactly when its whole
block is zero. If at most one block is zero, (3) forces every
$\lambda_j=0$. On $z\ne0$, two zero blocks are impossible:
they would give $0=(h_j-h_k)z^r$. Thus $V$ is smooth.

When $z=0$, the last condition in (3) disappears. If precisely $t$
blocks are zero, the dependency space has dimension
$\max(t-1,0)$. This proves the asserted set-theoretic description.
For a prescribed zero pair, all remaining blocks satisfy $F_j=0$.
For $L\ge3$ the resulting projective stratum has dimension

$$
(L-2)(r-1)-1.
$$

Subtracting this from $\dim X$ gives codimension $2r$. For $L=2$
both zero blocks would leave no projective point. The statement is
about the reduced singular set; the Jacobian singular subscheme may
have nilpotents.

Cohen--Macaulayness gives Serre's condition $S_2$, and the singular
codimension gives regularity in codimension one. Serre's criterion
therefore proves normality. Complete-intersection adjunction gives

$$
\omega_X
=\mathcal O_X\bigl((L-1)r-(rL+1)\bigr)
=\mathcal O_X(-r-1),
$$

as claimed.

## What cofiniteness would imply, and what was not proved

Assume now the coefficients are positive, the shifts are integers, and $S_r$
is cofinite. The
[canonical-core tail bound](finite_core_reduction.md#uniform-approximation-of-the-sumset)
allows a finite cutoff $Y$ such that targets with a representation using a
larger core have upper density less than $1/(4L)$. Targets with fewer than
$r$ summands have density zero. It follows that a positive lower proportion of
$n\le X$ have, for every $j$, an exactly-$r$-term representation of
$n+h_j$ using only cores at most $Y$.

There are only finitely many tuples of forms from this cutoff.
Consequently, along an unbounded sequence of $X$, one fixed tuple
$(F_1,\ldots,F_L)$ accounts for $\gg X$ distinct such targets.
Choosing one representation of each gives $\gg B^r$ positive
integer points of $V$ with roots $O(B)$, where $B=X^{1/r}$.

No estimate contradicting this consequence was established. In
particular, dimension and adjunction do not yield $o(B^r)$.
Each additional shifted equation introduces exactly $r$ new
root variables. The archimedean critical counting scale remains

$$
B^{rL-r(L-1)}=B^r.
$$

For the unit quintic form, even the finite joint system is locally soluble for
every local target $n$, by the established
[local universality](local_first_moments.md#a-single-locally-universal-core-for-the-fifth-powers).

The argument does not give a gap theorem. It excludes the proposed
general-type explanation, while leaving the distribution of distinct
integer targets, and hence complement infinitude for $r\ge5$, open.
