---
name: research/erdos_940/cubic_rational_composition
title: Fixed rational composition loses balanced input mass
desc: No quadratic polynomial composition exists for a diagonal ternary cubic; any fixed rational composition has only O(N^(17/3)) positive integral input pairs.
tags: []
sources: []
created: 2026-09-23T02:10:00Z
updated: 2026-09-23T02:10:00Z
---


# Fixed rational composition loses balanced input mass

***

## Statement and scope

Fix

$$
F(\mathbf x)=a_1x_1^3+a_2x_2^3+a_3x_3^3,
\qquad a_i\in\mathbb Q_{>0}.
$$

The following theorem is proved. It strengthens the
[linear-in-one-input obstruction](rational_transformations.md#no-composition-law-linear-in-one-input),
but does not decide the density of the values of $F$.

**Theorem.** Suppose that a fixed rational map
$C\in\mathbb Q(\mathbf x,\mathbf y)^3$ satisfies

$$
F(C(\mathbf x,\mathbf y))=F(\mathbf x)F(\mathbf y).       \tag{1}
$$

Then $C$ is not polynomial of total degree at most two. Furthermore,

$$
\#\{(\mathbf x,\mathbf y)\in[1,N]^6\cap\mathbb Z^6:
 C\text{ is defined and }C(\mathbf x,\mathbf y)\in\mathbb N^3\}
\ll_{F,C}N^{17/3}.                                    \tag{2}
$$


Thus no fixed rational composition retains a positive fraction of all
input pairs in balanced root boxes. In boxes with both root heights
comparable to $N$, its product values also number $O(N^{17/3})$,
compared with the ambient target scale $N^6$.
The theorem is not a count of all product values with unrestricted,
possibly very unbalanced factors. It also does not control maps whose
complexity varies with $N$.

## Excluding the pure quadratic terms

First suppose $P$ is a homogeneous quadratic polynomial map satisfying
(1). Write

$$
P=A(\mathbf x)+B(\mathbf x,\mathbf y)+D(\mathbf y),
$$

where $B$ is bilinear. Setting $\mathbf y=0$ gives $F(A)=0$.

Suppose $A\ne0$. The plane cubic $E:F=0$ is smooth, since its three
partial derivatives cannot vanish simultaneously at a projective point.
It is therefore geometrically integral of genus one. The rational map
$[A]:\mathbb P^2\dashrightarrow E$ must be constant: if two points in
its domain had different images, restriction to their joining line
would give a nonconstant rational map $\mathbb P^1\dashrightarrow E$.
It extends to a morphism, since $E$ is proper and smooth, contradicting
Riemann--Hurwitz. The constant image is a rational point $q$, as can
also be seen by evaluating at a rational point where $A\ne0$. Hence

$$
A=qH
$$

for a nonzero rational homogeneous quadratic $H$.

Make a rational linear change of output coordinates taking $q$ to
$(1,0,0)$ and its tangent line to $W=0$. The transformed cubic is

$$
\begin{aligned}
G(U,V,W)={}&\alpha U^2W+\beta UV^2+\gamma UVW+\delta UW^2\\
          &+\epsilon V^3+\eta V^2W+\theta VW^2+\kappa W^3,
\end{aligned}                                         \tag{3}
$$

with $\alpha\ne0$. The transformed coordinates of $P$ are

$$
U=H+L+u,\qquad V=M+v,\qquad W=T+w,
$$

where $L,M,T$ are bilinear and $u,v,w$ depend quadratically only
on $\mathbf y$.

Compare bidegrees in $G(P)=F(\mathbf x)F(\mathbf y)$. The $(5,1)$
part gives $\alpha H^2T=0$, so $T=0$. The $(4,2)$ part gives

$$
\alpha Hw+\beta M^2=0.                                \tag{4}
$$


If $\beta=0$, then $w=0$, and $G(P)=\epsilon(M+v)^3$.
This cannot be a nonzero scalar multiple of $F(\mathbf x)$ over
$\mathbb Q(\mathbf y)$: $F$ is absolutely irreducible and not a
cube. If $\beta\ne0$ but $w=0$, then $M=0$, and
$G(P)=\beta Uv^2+\epsilon v^3$ has degree at most two in
$\mathbf x$, again impossible.

In the remaining case $\beta w\ne0$, work over
$K=\mathbb Q(\mathbf y)$. Equation (4) makes $H$ a scalar multiple
of $M^2$. Thus all coordinates of $P$ belong to $K[L,M]$.
Choose a nonzero $h\in K^3$ annihilated by the two linear forms
$L,M$. Directional differentiation of (1) gives

$$
0=F(\mathbf y)D_hF(\mathbf x)
 =3F(\mathbf y)\sum_i a_i h_i x_i^2.
$$

This forces every $h_i=0$, a contradiction.

Consequently $A=0$. Interchanging the input blocks proves $D=0$,
so the proposed quadratic composition must be bilinear.

## Excluding the bilinear map and the lower-degree terms

Write $P=M(\mathbf y)\mathbf x$ over $K=\mathbb Q(\mathbf y)$, and
put $m=F(\mathbf y)$. The matrix $M$ is invertible: a kernel vector
would again give a nonzero direction $h$ with $D_hF=0$.
The Hessian determinant is

$$
\det\operatorname{Hess}F
 =216a_1a_2a_3x_1x_2x_3.
$$

Applying the Hessian transformation formula to $F(M\mathbf x)=mF(\mathbf x)$
shows that the product of the row forms of $M$ is a nonzero scalar
multiple of $x_1x_2x_3$. Unique factorization makes $M$ monomial.
Coefficient comparison therefore gives

$$
F(\mathbf y)=c\,g(\mathbf y)^3,
\qquad c\in\mathbb Q^\times,\quad g\in K^\times.
$$

This is impossible by the valuation at the irreducible divisor $F=0$:
it is one on the left and divisible by three on the right.
Absolute irreducibility follows from smoothness; distinct projective
components of positive degree in the plane would intersect and give
a singular point.

For a polynomial $C$ of total degree at most two, degree at most one
is impossible by degrees. In degree two, comparison of the total
degree-six parts gives

$$
F(C_2)=F(\mathbf x)F(\mathbf y),
$$

where $C_2$ is the homogeneous quadratic part. The preceding argument
excludes this. Lower-degree terms therefore provide no exception.

## Counting positive integral images

If some coordinate of $C$ is nonpolynomial, the
[resultant divisibility lemma](rational_transformations.md#integer-inputs-of-a-fixed-nonpolynomial-rational-map)
in six variables gives $O_{C,\varepsilon}(N^{5+\varepsilon})$ integral input
points. Choose a fixed $\varepsilon<2/3$.

Otherwise $C$ is polynomial of degree $D\ge3$. Choose a coordinate
$P$ of degree $D$. At a counted point, positivity and (1) imply

$$
|P(\mathbf x,\mathbf y)|\ll_F N^2.                    \tag{5}
$$

Let $P_D$ be its highest homogeneous part. Choose a primitive integer
vector $v$ with $P_D(v)\ne0$, and complete it to a unimodular integral
basis. The transformed input box is contained in a fixed dilate of
$[-N,N]^6$. Along each line in direction $v$, the polynomial
$p(t)$ has degree $D$ and leading coefficient $c=P_D(v)\ne0$,
independent of the other five coordinates.

Uniformly over the lower coefficients, a degree-$D$ polynomial with
leading coefficient $c$ satisfies

$$
\#\{t\in\mathbb Z:|p(t)|\le T\}\ll_{D,c}1+T^{1/D}.     \tag{6}
$$

Indeed, factoring over $\mathbb C$, every such $t$ lies within
$(T/|c|)^{1/D}$ of at least one of the $D$ roots. The corresponding
real intervals contain $O_D(1+(T/|c|)^{1/D})$ integers.

There are $O_C(N^5)$ choices for the other coordinates. Equations
(5)--(6) give

$$
O_{F,C}(N^{5+2/D})\le O_{F,C}(N^{17/3}),
$$

which proves (2).

## Remaining arithmetic question

The theorem concerns a prescribed rational rule, not the existence of other
integral representations of the product. It does not bound ordinary integer
fibers of $F$, and supplies neither density zero nor positive density for
those values. The
[bounded-fiber criterion](energy_and_multiplicity.md#a-weaker-target-than-the-complete-second-moment)
remains unproved.
