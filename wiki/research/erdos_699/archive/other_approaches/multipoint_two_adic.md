---
name: research/erdos_699/archive/other_approaches/multipoint_two_adic
title: "Erdős 699: exact powers of two for the three-seed integral"
desc: "For the seeds 10,9,8, an integer beta expansion proves a common 2-power in the cross product and a further 2-power in its third coefficient, without estimating a maximal gcd."
created: 2026-09-22T08:56:07Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: exact powers of two for the three-seed integral

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/off_diagonal_pade|Unequal Padé blocks]]

The three-seed construction with $(10,9,8)$ has two exact powers of two
that can be used simultaneously. The clean normalization is to divide
individual rows only by **odd** common factors, then divide their cross
product by a specified power of two. No estimate for the full primitive
gcd is needed.

This note proves divisibilities. It does not claim that the resulting
analytic estimates settle another index.

## Integer beta expansion

Let $a,b,c,d$ be nonnegative integers, put $L=a+b+c+d$, and set

$$
N=\frac{(L+1)!}{a!b!c!d!}.
$$

For integers $u,v,w,z$,

$$
N\int_0^1 t^a(1-t)^d(u+vt)^b(w+zt)^c\,dt\in\mathbb Z. \tag{1}
$$

Indeed, the coefficient of $u^{b-r}v^r w^{c-s}z^s$ in its expansion is

$$
\frac{(a+r+s)!}{a!r!s!}
\frac{(L+1)!}{(a+d+r+s+1)!(b-r)!(c-s)!}, \tag{2}
$$

which is a product of two multinomial coefficients. This proves (1)
without losing any power of two to integration denominators.

## The three integral rows

Fix positive integer directions $A_0,A_1,A_2,D$. For integers $m\ge1$
and $0\le k\le Dm-1$, put

$$
a=A_0m+k,\quad b=A_1m+k,\quad c=A_2m+k,\quad d=Dm-1-k,
$$

$$
f_k(x)=x^a(x-1)^b(x-2)^c(x-10)^d.
$$

Using the normalizer $N_k$ from (1), define

$$J_{i,k}=N_k\int_{r_i}^{10}f_k(x)\,dx,
\qquad(r_0,r_1,r_2)=(0,1,2),$$

and the integer row

$$
Z_k=(Z_{0,k},Z_{1,k},Z_{2,k})
=\left(
\frac{J_{0,k}}{5^{(A_0+D)m}},
\frac{J_{1,k}}{9^{(A_1+D)m}},
\frac{J_{2,k}}{8^{(A_2+D)m}}
\right). \tag{3}
$$

The integrality of all three coordinates follows from (1) after the
substitutions $x=10t$, $x=1+9t$, and $x=2+8t$, respectively. More
precisely,

$$
Z_{0,k}=(-1)^d2^{a+c+d+1}N_k
 \int_0^1t^a(1-t)^d(10t-1)^b(5t-1)^c\,dt,
$$

$$
Z_{1,k}=(-1)^dN_k
 \int_0^1t^b(1-t)^d(1+9t)^a(9t-1)^c\,dt,
$$

$$
Z_{2,k}=(-1)^d2^aN_k
 \int_0^1t^c(1-t)^d(1+4t)^a(1+8t)^b\,dt.
$$

Write

$$
a_*=A_0m,\qquad E=(A_0+A_2+D)m.
$$

Equation (1) now gives the exact statements

$$\boxed{2^{E+k}\mid Z_{0,k},\qquad
             2^{a_*+k}\mid Z_{2,k}.} \tag{4}$$

There is no logarithmic error term. Dividing each row by any odd common
divisor preserves both divisibilities.

## The cross product

Assume $Dm\ge2$. Let $R_0,R_1$ be the rows with $k=0,1$, after any such odd row
normalizations, and write

$$
(c_0,c_1,c_2)=R_0\times R_1.
$$

From (4), directly term by term,

$$
2^{a_*}\mid c_0,\qquad
2^{a_*+E+1}\mid c_1,\qquad
2^E\mid c_2. \tag{5}
$$

Consequently the integer vector

$$
W=2^{-A_0m}(R_0\times R_1)
$$

has

$$
\boxed{2^{(A_2+D)m}\mid W_2.} \tag{6}
$$

Thus the common factor $2^{A_0m}$ can be removed while retaining the
additional factor $2^{(A_2+D)m}$ in the coefficient of the third
prime-power cofactor. Any further **odd** common divisor of $W$ can also
be removed without affecting (6). The second coordinate has the stronger
remaining divisibility $2^{E+1}\mid W_1$.

The distinction between this chosen normalization and a fully primitive
cross product matters. Removing an additional, uncontrolled even common
factor could reduce the valuation in (6). Equations (4)–(6) establish the
normalization needed for the analytic argument directly; they do not
assert an upper bound for an entire row gcd or cross-product gcd.

For arbitrary distinct rows $k,\ell$, the same argument gives cross-product
valuations at least

$$
\bigl(a_*+\min(k,\ell),\quad
      a_*+E+k+\ell,\quad
      E+\min(k,\ell)\bigr).
$$

After dividing the displayed common power of two, the third coordinate
still contains $2^{(A_2+D)m}$. These divisibility statements remain true
when a minor is zero; nonvanishing of the cross product is a separate
condition in any application.

The [integer checker](../../computations/erdos_699_multipoint_two_adic.py)
implements (2) and compares small cases with direct rational integration.
Its [record](../../computations/erdos_699_multipoint_two_adic.json)
illustrates the row and cross-product valuations for sixteen parameter
choices. The proof of the general assertion is the multinomial identity
(2), followed by the substitutions and the cross-product calculation.
