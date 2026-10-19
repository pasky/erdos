---
name: research/erdos_940/cubic_matrix_composition
title: Trying multiplicative composition through cubic matrices
desc: Input-dependent conjugation and scalar repair of cubic matrix products produce only a density-zero set of products.
tags: []
sources: []
created: 2026-09-23T00:59:15Z
updated: 2026-09-23T00:59:15Z
---


# Trying multiplicative composition through cubic matrices

***

## The idea and its outcome

This attempt uses multiplication, rather than additive collision estimates or
progression first moments. Realize a positive diagonal cubic as a matrix
determinant, multiply two representatives, and try to return the product to the
diagonal family by an input-dependent conjugation. Unlike a fixed number-field
norm, a matrix determinant can restrict to an absolutely irreducible diagonal
cubic, so the existing
[constant-field norm obstruction](finite_core_reduction.md#a-fixed-number-field-norm-cannot-equal-the-diagonal-form)
does not exclude this starting point.

The attempt fails for a precise arithmetic reason. Ordinary products
have a trace obstruction; modifying the product removes that obstruction
but changes its determinant. Even allowing arbitrary pointwise rational
scalars to repair the determinant yields only
$O_\varepsilon(T^{17/18+\varepsilon})$ candidate product values up to $T$.
These statements are proved below. They concern this particular
composition mechanism, not arbitrary rational composition laws or the
density of the original cubic values. No target case is resolved.

## 1. A determinant model

Fix positive integers $a,b$, put $c=(a,b,a^2b)$, and write

$$
F(\mathbf x)=\sum_{i=1}^3c_ix_i^3.
$$

The choice $a=2,b=1$ gives $x^3+2y^3+4z^3$ after permuting variables.
Let $\zeta$ be a primitive cube root of unity and work over
$L=\mathbb Q(\zeta,\alpha,\beta)$, with $\alpha^3=a$, $\beta^3=b$.
Define

$$
U=\alpha\operatorname{diag}(1,\zeta^2,\zeta),\qquad
V=\beta\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}.
$$

Then $U^3=aI$, $V^3=bI$, and $VU=\zeta UV$. The nine matrices
$U^iV^j$, $0\le i,j\le2$, form a basis of $M_3(L)$, with multiplication

$$
(U^iV^j)(U^kV^l)
=\zeta^{jk}a^{\lfloor(i+k)/3\rfloor}b^{\lfloor(j+l)/3\rfloor}
U^{(i+k)\bmod3}V^{(j+l)\bmod3}.
\tag{1}
$$

All these basis matrices except $I$ have trace zero.

Set $e_1=U$, $e_2=V$, $e_3=U^2V$, and
$X(\mathbf x)=\sum_i x_i e_i$. The relation
$e_je_i=\zeta e_ie_j$ for $i<j$, together with
$1+\zeta+\zeta^2=0$, gives

$$
X(\mathbf x)^3=F(\mathbf x)I,\quad
\operatorname{tr}X(\mathbf x)=\operatorname{tr}(X(\mathbf x)^2)=0,
\quad\det X(\mathbf x)=F(\mathbf x).
\tag{2}
$$

The last equality also follows from Newton's identity
$\det X=\operatorname{tr}(X^3)/3$ when the first two traces vanish.
Call a matrix *pure* when those traces vanish. Purity is necessary for
a nonzero scalar multiple of a matrix to be conjugate into
$\mathcal V=\operatorname{span}_L(e_1,e_2,e_3)$.
Purity alone does not give a conjugate with positive rational coordinates.

## 2. Ordinary products and sandwiches

Write $X=X(\mathbf x)$ and $Y=X(\mathbf y)$. Multiplication using (1)
gives

$$
\operatorname{tr}(XY)=0,
\qquad
\operatorname{tr}((XY)^2)
=6ab(1+\zeta)(x_1y_2-x_2y_1)(x_2y_3-x_3y_2).
\tag{3}
$$

For a direct check, the six coefficients of $XY$, at basis elements
$(U^2,UV,V,V^2,U^2V^2,UV^2)$, are respectively

$$
x_1y_1,\quad x_1y_2+\zeta x_2y_1,\quad
a(x_1y_3+\zeta x_3y_1),\quad x_2y_2,\quad
x_3y_2+\zeta^2x_2y_3,\quad a\zeta^2x_3y_3.
$$

In the square, only the pairs $(UV,U^2V^2)$ and $(V,V^2)$ have
scalar products. Their two orders each contribute $\zeta^2ab$ and
$b$, respectively, proving (3).

Thus an arbitrary input-dependent conjugation and nonzero scalar can
return $XY$ to $\mathcal V$ only if

$$
x_1y_2=x_2y_1\quad\text{or}\quad x_2y_3=x_3y_2.
\tag{4}
$$

For positive integer inputs, the distinct products $F(\mathbf x)F(\mathbf y)
\le T$ satisfying (4) number

$$
O_{a,b}(T^{2/3}(\log(2T))^2).
\tag{5}
$$

Indeed, in boxes $x_i\le M$, $y_i\le N$, write proportional coordinate
pairs as $s(h,k)$ and $t(h,k)$ with $\gcd(h,k)=1$. There are at most
$2j$ choices with $\max(h,k)=j$, so these pairs number
$O(MN\log(2\min(M,N)))$. The two free coordinates contribute $MN$.
In dyadic maximum-coordinate shells, positivity forces
$MN\ll_{a,b}T^{1/3}$. Summing the resulting
$M^2N^2\log(2\min(M,N))$ bound proves (5).

Sandwiches fare worse. Polarization of (2) gives

$$
\operatorname{tr}(X^2Y)=3\sum_i c_ix_i^2y_i>0
\tag{6}
$$

on positive inputs. Since $XYX$ is similar to $X^2Y$, it cannot return
to $\mathcal V$ by conjugation and a nonzero scalar. More generally
$X^kYX^l$ is similar to $X^{k+l}Y$. Reduction of $k+l$ modulo three
leaves either an existing cube dilation of $F(\mathbf y)$, the product
case (4), or the impossible case (6). Conjugation $XYX^{-1}$ preserves
the old determinant rather than creating a new one.

## 3. A modified product really does remove the trace obstruction

The natural repair is

$$
D=\frac{XY-\zeta YX}{1-\zeta}.
\tag{7}
$$

This matrix is pure for **every** pair of inputs. To see this without
a large expansion, the coefficient of $t$ in $(X+tY)^3=F(\mathbf x+t\mathbf y)I$
is scalar. Multiply it by $Y$ and take traces, using $\operatorname{tr}Y=0$:

$$
\operatorname{tr}((XY)^2)=-2\operatorname{tr}(X^2Y^2).
$$

It follows that

$$
\operatorname{tr}((XY-\zeta YX)^2)
=(1+\zeta^2)\operatorname{tr}((XY)^2)
-2\zeta\operatorname{tr}(X^2Y^2)=0.
$$

Cayley–Hamilton now gives $D^3=(\det D)I$.

The determinant, however, is the following sextic rather than
$F(\mathbf x)F(\mathbf y)$:

$$
H(\mathbf x,\mathbf y)=
\sum_i c_i^2x_i^3y_i^3+
\sum_{i<j}c_ic_j\bigl(3x_i^2x_jy_iy_j^2-x_i^3y_j^3\bigr),
\qquad D^3=HI.
\tag{8}
$$

This follows by cubing $D=\sum_i x_iy_i e_i^2+(1+\zeta)\sum_{i<j}x_iy_j e_ie_j$
using (1). The
[preserved symbolic certificate](evidence/util/cubic_matrix_composition.py)
checks all nine coefficients of (2), (3), (6), and (8) exactly; it is not a test
on finitely many numerical inputs.

There is no rational-function scalar over
$\mathbb Q(\zeta)(\mathbf x,\mathbf y)$ which repairs (8) to the desired
product. The polynomial $F(\mathbf y)$ is absolutely irreducible (its projective
plane cubic is smooth), and does not divide $H$: the coefficient of $x_3^3$ in
$H$ is $c_3^2y_3^3$. Thus $F(\mathbf x)F(\mathbf y)/H$ has valuation one at the
prime divisor $F(\mathbf y)$, and cannot be a cube.

This also exhausts the combinations $A\,XY+B\,YX$ on generic inputs.
Their trace-square equals
$\operatorname{tr}((XY)^2)(A^2-AB+B^2)$, so purity outside (4)
requires $B/A=-\zeta$ or $-\zeta^2$. The second normalized choice is
$D(\mathbf y,\mathbf x)$ and has determinant $H(\mathbf y,\mathbf x)$.

## 4. Even pointwise scalar repair gives only sparse product values

The failure of a rational-function identity does not by itself exclude
scalars chosen separately at each integer input. The following does.

**Theorem.** For either $J(\mathbf x,\mathbf y)=H(\mathbf x,\mathbf y)$
or $H(\mathbf y,\mathbf x)$, the number of positive integer input pairs
with

$$
F(\mathbf x)F(\mathbf y)\le T,\qquad J\ne0,\qquad
F(\mathbf x)F(\mathbf y)/J\in\mathbb Q^{\times3}
$$

is $O_{a,b,\varepsilon}(T^{17/18+\varepsilon})$.
The same bound therefore holds for their distinct product values.

**Proof.** If the displayed quotient is a rational cube, then

$$
z^3=F(\mathbf x)F(\mathbf y)J(\mathbf x,\mathbf y)^2
\tag{9}
$$

for an integer $z$. A rational number whose cube is an integer is
itself an integer. Conversely (9) gives the required quotient when
$J\ne0$. Allowing $J=0$ in the counting argument only enlarges the set.

Suppose first $J=H(\mathbf x,\mathbf y)$. Fix positive
$x_1,x_2,\mathbf y$ and set $t=x_3$. Then

$$
G(t)=F(\mathbf x)=c_3t^3+C_0,\qquad
h(t)=H(\mathbf x,\mathbf y)=At^3+Bt+C,
$$

where

$$
C_0>0,\quad A=c_3^2y_3^3>0,\quad
B=3c_3y_3^2(c_1x_1^2y_1+c_2x_2^2y_2)>0.
$$

The polynomial $G$ has three simple complex roots. If
$F(\mathbf y)G h^2$ were a cube in $\mathbb C(t)$, every root of $G$
would have to occur in $h$ with multiplicity $1\pmod3$.
Since $\deg h=3$, this forces $h$ proportional to $G$, contradicting
$B>0$. Consequently
$z^3-F(\mathbf y)G(t)h(t)^2$ is absolutely irreducible of total degree
nine. For $J=H(\mathbf y,\mathbf x)$, vary $t=x_1$ instead: its
cubic and linear coefficients are
$c_1^2y_1^3>0$ and
$3c_1y_1^2(c_2y_2x_2^2+c_3y_3x_3^2)>0$, giving the same proof.

The coefficient-uniform Bombieri–Pila estimate in
[Browning–Verzobio, Lemma 2.2](../../../library/diophantine_problems/browning_verzobio_2026_sums_three_powerful_numbers/_index.md)
states that an absolutely irreducible degree-$e$ integral plane curve has
$O_{e,\epsilon}(Q^{1/e+\epsilon})$ integer points in $[-Q,Q]^2$. Its full
statement, including uniformity, was checked.

In a root box $x_i\le M$, $y_i\le N$ with $M\ge N$, put $S=MN$.
Equation (9) gives $|z|\ll_{a,b}S^3$. Applying that estimate to each
fixed slice gives $O_{a,b,\epsilon}(S^{1/3+\epsilon})$ possibilities.
There are $O(M^2N^3)$ choices of the frozen coordinates, hence

$$
\#\text{pairs in the box}\ll_{a,b,\epsilon}
M^2N^3S^{1/3+\epsilon}=S^{10/3+\epsilon}/M.
\tag{10}
$$

If $N>M$, interchange the tuples and the two orientations of $H$.

Use dyadic maximum-coordinate shells. At fixed dyadic product $S$,
the sum of $1/M$ over $M\ge\sqrt S$ is $O(S^{-1/2})$.
Thus (10) sums to $O(S^{17/6+\epsilon})$. Positivity imposes
$S\ll_{a,b}T^{1/3}$, and summing over $S$ proves the theorem after
renaming $\epsilon$. $\square$

Scalars in $\mathbb Q(\zeta)$ do not change this conclusion: if their
cube is rational, they are rational. Otherwise an irreducible cubic
polynomial over $\mathbb Q$ would have a root in a quadratic field.

## What remains outside the obstruction

These bounds allow the conjugating matrix and the repairing scalar to
depend arbitrarily on the input; they are not just another fixed-map
bound. The second bound also treats unbalanced root heights, so it is
stronger than a zero-density statement in balanced input boxes.

They do not exclude a different nonlinear operation, extra auxiliary
variables, or rational inputs with uncontrolled denominators. Ordinary
matrix multiplication retains the determinant on a nine-dimensional
space, but returning to the three-dimensional diagonal family is the
failed step. The modified product returns to the pure-matrix variety,
not to a positive integral diagonal representation of the product.
No positive-density theorem for $F$ or additional Erdős 940 case follows.
