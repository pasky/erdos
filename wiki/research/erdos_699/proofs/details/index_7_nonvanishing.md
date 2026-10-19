---
name: research/erdos_699/proofs/details/index_7_nonvanishing
title: "Erdős 699: removing the index-seven common-zero bound"
desc: "Three modular kernel sections and two local p-adic calculations prove uniform arithmetic nonvanishing in degree 196."
created: 2026-09-22T16:39:52Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: removing the index-seven common-zero bound

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/coprime_kernels|Coprime kernel sections]] ·
[[research/erdos_699/proofs/details/index_7_effective|The index-seven argument]]

***

The degree-196 certificate `poly_coprime_last` needs no bound
for the common integer zeros of two polynomials. Three sections suffice
to exclude such zeros uniformly outside the prescribed grid. This removes
the resultant contribution to the numerical threshold; the coefficient
and other thresholds in the index-seven argument are separate.

## The exact certificate

The residual multiplicity at $(x,y)$, $x,y\ge0$, $x+y\le6$, is

$$
R_{xy}=\max(0,m_{x+y}-h_x-h_y),
$$

where

$$h=(119,90,60,26,0,0,0),\qquad
m=(282,237,198,196,157,131,109).$$

There are 26 positive-multiplicity support points. The symmetric Hasse
jet matrix in degree at most 196 has 9,792 rows and 9,801 columns. Its
full row rank modulo $p=251$ was already retained; a new nullspace
calculation retained all nine kernel basis vectors. Select the first
three, denoted $\overline F,\overline G,\overline H$.

The [certificate](../../computations/erdos_699_index_7_nonvanishing.json)
and [exact checker](../../computations/erdos_699_index_7_nonvanishing.py)
verify the following facts without repeating the large rank calculation:

1. All nine vectors satisfy the prescribed jets. The first two agree
   with the previously retained coprime sections.
2. The common $\mathbf F_{251}$-points of $\overline F,\overline G$
   are precisely the support and
   $(66,185),(185,66),(160,195),(195,160)$.
3. The third section takes values 133 at the first pair and 33 at the
   second pair, so it excludes all four additional residue points.
4. The degree-$R_{xy}$ tangent forms of the first two sections are
   coprime at every support point except $(2,2)$ and $(3,3)$.
   At those points their common tangent is exactly $U+V=0$.
5. The two local calculations below resolve both exceptional directions.

The residue calculation concerns polynomial evaluations over a fixed
finite field, not a search through binomial rows or columns.

## Lifting the sections

Full row rank modulo 251 gives a maximal jet minor with determinant a
251-adic unit. Each of the three modular kernel vectors therefore lifts
to a symmetric polynomial in $\mathbf Z_{(251)}[X,Y]$ of degree at most
196, satisfying the prescribed jets exactly. Denote the lifts by $F,G,H$.

This remains valid after an integral unimodular triangular change to a
Newton basis. It also remains valid for the usual normalized factorial
bases, whose change-of-basis denominators are units at 251 because
$196<251$. Thus the arithmetic nonvanishing certificate is compatible
with coefficient estimates obtained in those bases.

Clearing denominators prime to 251 gives integer sections. No enormous
explicit rational lift or resultant is needed.

## Arithmetic nonvanishing

**Proposition.** The common zeros of $F,G,H$ in $\mathbf Z_{251}^2$ are
exactly the 26 prescribed support points. In particular, they have no
common integer zero with $X,Y\ge7$.

**Proof.** Reduction modulo 251 and the third-section evaluations show
that a common zero must reduce to a support point $(a,b)$. Put
$U=X-a$, $V=Y-b$ and $R=R_{ab}$. All terms of $F$ and $G$ at this point
have total degree at least $R$.

Suppose $(U,V)\ne(0,0)$ and put
$k=\min(v_{251}(U),v_{251}(V))\ge1$. Dividing both equations by
$251^{kR}$ and reducing shows that the nonzero direction

$$
[\overline{U/251^k}:\overline{V/251^k}]
$$

is a common zero of the two tangent forms. Coprimality excludes this at
all but the two exceptional support points.

At $(2,2)$ and $(3,3)$, the multiplicities are respectively 37 and 57,
and the only common direction is $[1:-1]$. Hence $U\ne0$, and

$$
t=U,\qquad w=\frac{U+V}{U}
$$

both belong to $251\mathbf Z_{251}$. The strict transforms

$$\widetilde F(t,w)=t^{-R}F(a+t,a+t(w-1)),\qquad
\widetilde G(t,w)=t^{-R}G(a+t,a+t(w-1))$$

are polynomials over $\mathbf Z_{(251)}$. Their constant terms vanish
**exactly**, since a symmetric homogeneous polynomial of odd degree
vanishes at $(1,-1)$. This is why the symmetry of the lifts matters.

Their linear coefficient matrices in $(t,w)$ reduce respectively to

$$\begin{pmatrix}86&242\\217&98\end{pmatrix},\qquad
\begin{pmatrix}180&45\\23&211\end{pmatrix}.$$

The determinants are 90 and 48 modulo 251, both nonzero. If
$\ell=\min(v_{251}(t),v_{251}(w))$, dividing the two strict-transform
equations by $251^\ell$ and reducing would make the corresponding
invertible matrix annihilate a nonzero vector. This is impossible.
Thus the original zero was the support point itself. Conversely, every
support point is a zero by the prescribed jets. $\square$

The conclusion concerns arithmetic zeros over $\mathbf Z_{251}$.
It does not claim that the linear system has no geometric basepoints
over an algebraic closure. Extension-field residue points do not affect
the argument: a 251-adically integral pair reduces to an
$\mathbf F_{251}$-point.

The selected lifts have the same degree and prescribed multiplicities
as the earlier coprime pair, and the same type of effective coefficient
bound. The index-seven divisibility inequality may consequently use
degree 196 with **no additional common-zero threshold**.
