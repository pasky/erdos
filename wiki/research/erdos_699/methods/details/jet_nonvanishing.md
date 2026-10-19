---
name: research/erdos_699/methods/details/jet_nonvanishing
title: "Erdős 699: surjective interpolation gives nonvanishing polynomials"
desc: "A finite-dimensional multiplication operator turns a surjective symmetric jet map into degree-D+1 polynomials that cannot vanish simultaneously when X+Y exceeds the grid."
created: 2026-09-22T04:06:03Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: surjective interpolation gives nonvanishing polynomials

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]]

***

This lemma supplies the nonvanishing step for the index-13 and subsequent
interpolation certificates. It requires an exact rank calculation, but
does not require a polynomial gcd or a bound for an exceptional algebraic
zero set.

**Lemma.** Prescribe symmetric multiplicities $R_{xy}=R_{yx}\ge0$ at the
integer points $x,y\ge0$, $x+y<i$. Suppose that the map taking symmetric
polynomials of total degree at most $D$ to their prescribed Hasse jets is
surjective over $\mathbb Q$. Then there is an effectively constructible
finite family of integer polynomials of degree at most $D+1$, all having
the prescribed multiplicities, that cannot vanish simultaneously at a
point $(X,Y)$ with $X+Y>i-1$.

**Proof.** Let

$$
 I=\bigcap_{R_{xy}>0}(X-x,Y-y)^{R_{xy}},\qquad
 A=\mathbb Q[X,Y]/I,
$$

and let $A^\sigma$ be the invariant subalgebra under $\sigma(X,Y)=(Y,X)$.
The symmetric jets are exactly the coordinates of this finite-dimensional
algebra. Let $\pi:A^\sigma\to\mathbb Q[X,Y]_{\le D}^\sigma$ be a rational
linear right inverse to the jet map. Put $s=X+Y$.

For a rational basis $a_1,\ldots,a_r$ of $A^\sigma$, use the polynomials

$$
 G_0=1-\pi(1),\qquad
 G_j=s\pi(a_j)-\pi(sa_j)\quad(1\le j\le r).               \tag{1}
$$

They belong to $I$ and have degree at most $D+1$. Clear a common
denominator to obtain integer polynomials with the same common zeros.

Suppose they all vanished at $P$. The functional
$\varepsilon(a)=\pi(a)(P)$ would satisfy

$$
 \varepsilon(1)=1,\qquad
 \varepsilon(sa)=s(P)\varepsilon(a)
 \quad\text{for every }a\in A^\sigma.
$$

Thus $s(P)$ would be an eigenvalue of multiplication by $s$ on
$A^\sigma$. On the local algebra at $(x,y)$, this operator is $(x+y)$
times the identity plus a nilpotent operator. Its eigenvalues, including
those on the invariant subalgebra, therefore belong to
$\{0,1,\ldots,i-1\}$. This contradicts $s(P)>i-1$. $\square$

The right inverse is found by selecting a nonsingular maximal minor of
the integer jet matrix. In particular, full row rank modulo any prime
proves the required rational surjectivity. Adjugates of that minor give
effective coefficient bounds for all polynomials (1), even if the
rational polynomials are not explicitly computed.

For the usual symmetric Taylor-coordinate basis, multiplication by $s$
has integer entries. Its local constant term is $x+y$, and its remaining
terms raise the jet order. A column has coefficient sum at most
$x+y+3$: at a diagonal support point, for example, multiplying $U+V$ by
$U+V$ gives invariant coordinates $1,2$ in
$U^2+2UV+V^2$. These small coefficient bounds make the adjugate estimate
quite direct.

If a known integer polynomial $H$ already supplies some of the desired
Kummer multiplicities and is nonzero in the physical range, multiplying
the family (1) by $H$ gives the complete certificate. The added degree
needed to guarantee nonvanishing is only one.
