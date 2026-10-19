---
name: research/erdos_699/archive/other_approaches/cubic_multiplication
title: "Erdős 699: multiplication of the marked elliptic point"
desc: "A rational reconstruction of the row from an elliptic curve and marked point. Doubling always produces a nonintegral row; tripling preserves the two-adic row and column valuations but has uncontrolled odd denominators."
created: 2026-09-21T23:54:05Z
updated: 2026-09-21T23:54:05Z
---

# Erdős 699: multiplication of the marked elliptic point

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/remaining/details/cubic_elliptic|The marked elliptic curve]]

Multiplication of the distinguished point gives rational transformations
of the row and column parameters. This note proves that **doubling never
gives an integer row**, for any hypothetical bad triple. Tripling behaves
differently: it preserves the exact two-adic valuations of the row and
column. The remaining odd denominators are not controlled uniformly.
Neither transformation establishes nonexistence or global finiteness.

## 1. Recovering the parameters from a marked curve

Keep $n=2^hu$, $c=n-j$, $t=v_2(j)=v_2(c)$, and $m=h-t\ge2$.
Normalize the curve at its marked point $Q$ to obtain

$$Y^2=f(X)=1+X+\frac A3X^2+\frac B{27}X^3,
\qquad Q=(0,1),\tag{1}$$

where

$$A=\frac{n(c-1)}{c(n-1)},\qquad
B=\frac{n^2(c-1)(c-2)}{c^2(n-1)(n-2)}.\tag{2}$$

These $A,B$ are coordinates for the marked curve, distinct from the
coordinates in the cubic-surface note. The normalization uses
$X=(P'(1)/P(1))(z-1)$ and $Y=y/y(Q)$ on the specified twist.
Conversely, direct elimination gives

$$n=\frac{2(A^2-B)}{2A^2-A-B},\qquad
c=\frac{2(A^2-B)}{A^2+(A-2)B}.\tag{3}$$

Thus replacing $Q$ by another rational point and normalizing again
reconstructs rational parameters, where the denominators are nonzero.
It does not automatically reconstruct integer parameters.

At a point with abscissa $x$ and $f(x)f'(x)\ne0$, the new coordinates are

$$A_x=\frac{3(f''(x)/2)f(x)}{f'(x)^2},\qquad
B_x=\frac{Bf(x)^2}{f'(x)^3}.\tag{4}$$

An identity useful below is

$$
A_x^2-B_x=(A^2-B)\frac{f(x)^2}{f'(x)^4}.\tag{5}
$$

## 2. Doubling always loses row integrality

The tangent at $Q$ gives $x(2Q)=(1-4A/3)/(4B/27)$. Put

$$
T=36A-8B-27,\qquad S=48A^2-144A+16B+81.
$$

Substitution in (4) gives

$$
A_2=-\frac{(8A-9)T^2}{S^2},\qquad B_2=\frac{T^4}{S^3}.
$$

The reconstructed row simplifies to

$$
n_2=\frac{(A^2-B)T^2}{2L},\tag{6}
$$

where

$$\begin{aligned}
L={}&18A^3(4A-3)^2-3AB(4A-3)(44A-27)\\
&+(80A^2+32A-63)B^2-16B^3.
\end{aligned}$$

**Proposition.** For every hypothetical bad triple, (6) either has zero
denominator or has negative two-adic valuation. In particular, doubling
does not reconstruct an integer row.

**Proof.** Write $v=v_2(c-1)$. Formula (2) and direct subtraction give

$$v_2(A)=m+v,\quad
v_2(B)=2m+v+v_2(c-2)-1,\quad
v_2(A^2-B)=2m+t+v-1.\tag{7}$$

Here the last equality follows from
$A^2-B=n^2(c-1)j/[c^2(n-2)(n-1)^2]$.
In all cases $A,B$ are two-adic integers divisible by four, so $T$ and
$S$ are odd.

If $t\ge2$, (7) gives $v_2(A)=m$ and $v_2(B)=2m$.
The unique term of smallest valuation in $L$ is its $AB$ term, so
$v_2(L)=3m$ and

$$
v_2(n_2)=t-m-2.
$$

Moreover $m>t$: the normalized integer cubic $P$ has two positive
middle coefficients divisible by $2^{t-1}$ and two positive endpoint
coefficients. Hence $2^m=P(1)\ge2^t+2$, forcing $m>t$.

If $t=1$, one has $v_2(A)=m$, $v_2(B)\ge2m+1$, and
$v_2(L)\ge3m+1$ whenever $L\ne0$. Thus

$$
v_2(n_2)\le-m-2<0.
$$

Finally, if $t=0$, then $v\ge1$,
$v_2(A)=h+v$, and $v_2(B)=2h+v-1$. Again the $AB$ term is uniquely
smallest in $L$, giving

$$
v_2(n_2)=-h-v-1<0.
$$

If $L=0$, the numerator in (6) is nonzero and there is no finite
reconstructed row. This covers every case. $\square$

## 3. Tripling preserves the two-adic valuations

The addition formula gives a short expression

$$
x_3=x(3Q)=-\frac{8(36A-8B-27)}{3(4A-3)^2}.\tag{8}
$$

Both parenthesized expressions are odd, so $v_2(x_3)=3$.
Consequently $f(x_3)$ and $f'(x_3)$ are two-adic units. Also
$v_2(f''(x_3)/2)=v_2(A)$, because
$f''(x_3)/2=A/3+(B/9)x_3$ and $v_2(B)>v_2(A)$.
Equations (4) and (5) therefore preserve the three valuations of
$A$, $B$, and $A^2-B$ in (7).

Applying (3), its row denominator has valuation $v_2(A)$: its $-A$
term is uniquely smallest. Its column denominator has valuation $2m$
when $t\ge1$, and $2h+v$ when $t=0$. Hence

$$
v_2(n_3)=h,\qquad v_2(c_3)=v_2(j_3)=t.\tag{9}
$$

This proves only a statement about rational parameters. Equation (9)
does not exclude odd primes in their denominators.

One such obstruction can be stated precisely. Suppose $p\ge5$,
$e=v_p(4A-3)>0$, and both $B$ and $A^2-B$ are $p$-adic units.
Then (8) has valuation $-2e$. The change
$x=(B/27)X+A/9$ puts (1) in short Weierstrass form
$y^2=x^3+ax+b$, with $a$ a $p$-adic unit and $b$ integral at $p$.
For this model, (3) becomes the rational function

$$
n(x)=\frac{-6a(x^3+ax+b)}{9bx^2-4a^2x-3ab}.\tag{10}
$$

At $3Q$ its numerator has valuation $-6e$ and its denominator has
valuation at least $-4e$. Thus either the denominator vanishes or
$v_p(n_3)\le-2e<0$. Such a prime prevents row integrality.

The visible factor $4A-3$ has numerator $(n+3)c-4n$ before cancellation
against $c(n-1)$. There is presently no proof that a prime satisfying
the stated unit conditions must occur for every hypothetical bad pair.
Factors shared with the original parameters can cancel, and primes of
bad reduction require separate analysis. Thus tripling remains an
arithmetic question at odd primes, rather than a completed descent.

The reconstruction and multiplication identities were checked
symbolically. No finite search was used.
