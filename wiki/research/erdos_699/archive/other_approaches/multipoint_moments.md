---
name: research/erdos_699/archive/other_approaches/multipoint_moments
title: "Erdős 699: an exact three-factor moment determinant"
desc: "Polynomial moments provide three integral approximation rows with separate prime-power blocks and an explicit nonzero determinant."
created: 2026-09-22T08:54:00Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: an exact three-factor moment determinant

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/archive/other_approaches/multipoint_minor_divisibility|Prime divisibility of the minors]]

The approximation matrices below have three separately chosen denominator
blocks and a simple exact determinant. Together with the prime-divisibility
lemma, this gives a concrete simultaneous approximation construction to
test on the remaining small indices. No new whole-index effective bound
is claimed from this construction.

Let $A_0,A_1,A_2,D$ be nonnegative integers, and put

$$w(x)=x^{A_0}(x-1)^{A_1}(x-2)^{A_2}(x-T)^D,
\qquad L=A_0+A_1+A_2+D,$$

$$
N=\frac{(L+3)!}{A_0!A_1!A_2!D!},\qquad b_i=A_i+D+1.
$$

For $0\le k,i\le2$, define

$$J_{ki}=N\int_i^T x^k w(x)\,dx,
\qquad B_{ki}=\frac{J_{ki}}{(T-i)^{b_i}}.$$

**Proposition.** Every $B_{ki}$ is an integer polynomial in $T$, and

$$
\boxed{\det B=(-1)^{A_1+D}\,N^2\,2^{A_0+A_2+1}.}\tag{1}
$$

Thus the determinant is nonzero and independent of $T$. If
$T-i=a_iP_i$ with integers $a_i,P_i>0$, then $Z_{ki}=J_{ki}/P_i^{b_i}$
is an integer matrix with

$$
\det Z=(-1)^{A_1+D}N^2 2^{A_0+A_2+1}\prod_{i=0}^2a_i^{b_i}.
$$

Unlike adjacent-exponent constructions, this choice of rows simply
multiplies a common integrand by $1,x,x^2$. These bounded-degree factors
do not change its exponential growth rates.

## Integral coefficients

Substitute $x=i+(T-i)u$. The factors at the endpoints contribute
$(T-i)^{A_i+D+1}u^{A_i}(u-1)^D$. Expand every other factor, including
$x^k$, in powers of $u$. Multiplication of each resulting beta integral
by its binomial coefficients and by $N$ gives an integer: the factorials
can be grouped into two multinomial coefficients and an integer factor.
One can also absorb $x^k$ into $A_0$; its usual integral normalization
divides $N$, since

$$\frac{N}{(L+k+1)!/((A_0+k)!A_1!A_2!D!)}
=\frac{(L+3)!(A_0+k)!}{(L+k+1)!A_0!}\in\mathbb Z.$$

This proves the assertion about integer coefficients, with at least the
stated column power in every row.

## The determinant identity

For general ordered knots $r_0<r_1<r_2<r_3$ and nonnegative exponents
$a_0,a_1,a_2,a_3$, set $l=\sum a_i$ and

$$M_{ki}=\int_{r_i}^{r_{i+1}}x^k\prod_{a=0}^3(x-r_a)^{a_a}\,dx,
\qquad 0\le k,i\le2.$$

The elementary polynomial identity is

$$|\det M|=\frac{\prod_{a=0}^3 a_a!}{(l+3)!}
                 \prod_{a<b}(r_b-r_a)^{a_a+a_b+1}.\tag{2}$$

Here is a derivation. Replacing a column by a sum of consecutive columns
makes it an integral from any selected knot $r_a$ to another $r_b$.
Substitution in that integral shows that the determinant is divisible by
$(r_b-r_a)^{a_a+a_b+1}$. Its homogeneous degree is $3l+6$, precisely the
sum of these six exponents. Thus the determinant is a constant times
their product.

The constant is found by letting two adjacent knots coalesce. The
shrinking interval contributes the beta factor
$a_0!a_1!/(a_0+a_1+1)!$. Use the polynomial row basis
$1,(x-r_0),(x-r_0)x$ and expand along that shrinking column. The remaining
moment determinant has the merged exponent $a_0+a_1+1$. Repeating the
operation cancels the intermediate factorials and leaves exactly the
factor in (2). This proves its absolute value. Alternatively,
multilinearity expresses the determinant as the integral of a
Vandermonde determinant over three disjoint ordered intervals, which
also shows that it is nonzero and determines its sign.

Apply (2) to knots $(0,1,2,T)$ and exponents $(A_0,A_1,A_2,D)$.
Column sums turn consecutive-interval integrals into integrals to the
common endpoint $T$ without changing the determinant. The factors
involving $T$ are exactly $\prod_i(T-i)^{b_i}$, and the other knot
differences contribute $2^{A_0+A_2+1}$. Multiplication by $N^3$ and
division by the column powers give (1). The product of the integrand
signs on the three intervals is $(-1)^{A_1+D}$.

## Combining this with the minor-divisibility lemma

The same Frobenius calculation works for these polynomial-moment rows.
For a prime whose exponent floors are stable under the bounded degree
changes, suppose

$$\left\lfloor L/p\right\rfloor-
 \left\lfloor A_0/p\right\rfloor-
 \left\lfloor A_1/p\right\rfloor-
 \left\lfloor A_2/p\right\rfloor-
 \left\lfloor D/p\right\rfloor=1.$$

Assume also $p^2>L+3$, $p\nmid(L+1)(L+2)(L+3)$, and that $p$ does
not divide the chosen column bases. After taking out the common $p$-th
power from $w$ modulo $p$, multiplication by $x^k$ still leaves a
residual polynomial of degree less than $2p$. Its only term contributing
to a denominator divisible by $p$ is the coefficient of $x^{p-1}$.
Consequently the normalized rows remain proportional modulo $p$.
Every two-by-two minor gains this prime.

The exact determinant also limits additional divisibility: for the
matrix $B$, a prime dividing all its two-by-two minors must divide $2N$.
This follows by expanding its determinant along a row. Such a constraint
is useful when investigating the arithmetic of these approximants, but
does not itself supply the cofactor inequalities needed at $i=6$ or $8$.
