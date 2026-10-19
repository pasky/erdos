---
name: theory/polynomials/L179_quartic_harmonic_deficit/_proof
title: Quantitative missing intersections for harmonic quartics
desc: |
  A set of lines of controlled measure misses at least two intersections
  with the harmonic quartic. When the quadratic coefficient is substantial
  its depressed real restriction has a positive quadratic coefficient;
  otherwise the linear coefficient violates a real-root moment bound.
created: 2026-10-15T20:21:22Z
updated: 2026-10-15T20:21:22Z
---

***

We prove the
[[theory/polynomials/L179_quartic_harmonic_deficit/_index|claim]].
The change $z=\lambda w$, followed by division of $P$ by $\lambda^4$,
multiplies the renormalized length by $\lambda$. It therefore suffices
to treat

$$
|a|\le1,\qquad |b|\le1,\qquad \max(|a|,|b|)=1. \tag{1}
$$

The real constant $c$ is unrestricted. All constants below are independent
of it.

## The projection inequality

For $\alpha\in\mathbb R/\pi\mathbb Z$ and $s\in\mathbb R$ let

$$
N(\alpha,s)=\#\{t\in\mathbb R:
 \operatorname{Re}P(e^{i\alpha}(t+is))=0\}.
$$

Except for finitely many directions and a null set of tangent lines,
this is a number between zero and four. If $A$ is any measurable set of
such lines, the projection inequality is

$$
J(P)\le-\frac12\int_A(4-N(\alpha,s))\,ds\,d\alpha. \tag{2}
$$

Here $J(P)$ exists: centering gives eight ends with positions
$re^{i(\pi/8+j\pi/4)}+O(r^{-1})$ and tangent derivatives differing
from those of rays by $O(r^{-2})$. Each end therefore has a finite
length excess over its radial coordinate. The compact portion of the
real algebraic curve has finite length.

For clarity, (2) is the normalization of the projection argument in
the proof of Fryntov and Nazarov's Lemma 1, pp. 5--6 of the preprint
identified on the
[[../library/polynomials/fryntov_2009_new_estimates_length_erdos_herzog/_index|source card]].
Project the plane centrally onto the lower hemisphere of a sphere of
radius $R$ tangent to it at zero. Spherical Crofton gives projected
total length $4\pi R-D_R$, with

$$
D_R=\frac12\int_0^\pi\int_{\mathbb R}
(4-N(\alpha,s))(1+s^2/R^2)^{-3/2}\,ds\,d\alpha.
$$

For all sufficiently large $r$, every circle of radius $\rho\ge r$
meets $H$ at least eight times, by the leading term $\operatorname{Re}z^4$.
The radial coordinate on the hemisphere therefore bounds the length of
the projected part outside $D_r$ from below by
$4\pi R-8R\arctan(r/R)$. Its part inside has length at most
$8R\arctan(r/R)-D_R$. Letting $R\to\infty$, restricting the
nonnegative deficit integral to $A$, and then letting $r\to\infty$
gives (2). Equivalently the unoriented Euclidean line measure is
$\tfrac12\,ds\,d\alpha$, which fixes the factor in (2).

## A quadratic coefficient bounded away from zero

Suppose $|a|\ge1/100$. There is a direction

$$
\alpha_0\in\{-\pi/12,\pi/12,\pi/2-\pi/12,\pi/2+\pi/12\}
$$

for which
$\cos4\alpha_0=1/2$ and
$\operatorname{Re}(ae^{2i\alpha_0})\ge|a|/2$.
Indeed, writing $a=x+iy$, the first two choices yield
$\sqrt3x/2\pm y/2$, and the other two change their signs. The largest
absolute value of the first two is at least
$\sqrt{3x^2/4+y^2/4}\ge|a|/2$.

For $|\alpha-\alpha_0|\le1/100$, the elementary Lipschitz estimates for
the exponential give, with $A_4=\cos4\alpha$ and
$B=\operatorname{Re}(ae^{2i\alpha})$,

$$
A_4\ge\frac12-\frac4{100}>\frac25,
\qquad B\ge\frac{|a|}{2}-\frac{2|a|}{100}>\frac{2|a|}{5}. \tag{3}
$$

In the real polynomial
$q(t)=\operatorname{Re}P(e^{i\alpha}(t+is))$ the leading, cubic and
quadratic coefficients are respectively

$$
A_4,\qquad -4s\sin4\alpha,\qquad B-6s^2A_4.
$$

After division by $A_4$ and removal of the cubic term, the quadratic
coefficient is exactly

$$
\frac{B}{A_4}-\frac{6s^2}{A_4^2}. \tag{4}
$$

For $|s|\le\sqrt{|a|}/10$ it is positive, since
$A_4B>4|a|/25>6|a|/100$ by (3). A monic real quartic with four real
roots and zero cubic coefficient has quadratic coefficient
$-\tfrac12\sum_j x_j^2\le0$. Thus $q$ has a nonreal conjugate pair,
and $N(\alpha,s)\le2$ throughout this rectangle, apart from irrelevant
null sets.

The rectangle has angular width $1/50$ and offset width
$\sqrt{|a|}/5$. Substitution in (2) gives

$$
J(P)\le-\frac{\sqrt{|a|}}{250}\le-\frac1{2500}. \tag{5}
$$

Angles are taken modulo $\pi$; crossing an endpoint of a fundamental
interval does not change the rectangle's line measure.

## A substantial linear coefficient

It remains to treat $|a|<1/100$, so (1) gives $|b|=1$.
Choose $\alpha_0\in\{0,\pi/2\}$ such that
$|\operatorname{Re}(be^{i\alpha_0})|\ge1/\sqrt2>7/10$.
For $|\alpha-\alpha_0|\le1/100$ and $|s|\le1/100$, write

$$
q(t)=A_4t^4+d t^3+e t^2+f t+g.
$$

Its coefficients satisfy

$$
\begin{aligned}
&\frac9{10}<A_4\le1,\qquad |d|\le\frac1{25},
\qquad |e|\le\frac1{100}+\frac6{10000}=\frac{53}{5000},\\
&|f|\ge\frac{69}{100}-\frac2{10000}-\frac4{10^6}
>\frac23.
\end{aligned} \tag{6}
$$

Here
$d=-4s\sin4\alpha$,
$e=\operatorname{Re}(ae^{2i\alpha})-6s^2A_4$, and
$f=\operatorname{Re}(be^{i\alpha}+2ias e^{2i\alpha}-4is^3e^{4i\alpha})$.
The constant coefficient plays no role.

Divide by $A_4$ and remove the cubic term. The resulting quadratic and
linear coefficients, $B_0$ and $C_0$, obey

$$
\begin{aligned}
|B_0|&\le\frac{|e|}{A_4}+\frac{3d^2}{8A_4^2}<\frac1{50},\\
|C_0|&\ge\frac{|f|}{A_4}
 -\frac{|de|}{2A_4^2}-\frac{|d|^3}{8A_4^3}>\frac12.
\end{aligned} \tag{7}
$$

These inequalities follow directly by inserting (6); the two error
terms in the second line sum to less than $1/1000$.
If the depressed quartic had four real roots $x_j$, Newton's identities
would give

$$
\sum_jx_j=0,\qquad \sum_jx_j^2=-2B_0\le\frac1{25},
\qquad \left|3C_0\right|=\left|\sum_jx_j^3\right|
\le\left(\sum_jx_j^2\right)^{3/2}\le\frac1{125}.
$$

This contradicts (7). Hence again $N(\alpha,s)\le2$. The angular and
offset widths are both $1/50$, so (2) gives $J(P)\le-1/2500$.
Together with (5), this proves the normalized estimate. Restoring the
scale $\lambda$ proves the claim.
