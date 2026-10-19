---
name: theory/polynomials/L180_quartic_small_curvature_deficit/_proof
title: A quantitative comparison with the tangent line
desc: |
  Uniform inverse-series bounds control the signed tails. On a bounded
  target interval, fourth-root coverings control all singular windows and
  a resultant bounds the inverse derivatives on their complement. The
  resulting explicit modulus transfers the negative harmonic-line bound.
created: 2026-10-15T20:21:22Z
updated: 2026-10-15T20:21:22Z
---

***

Use the constants in the
[[theory/polynomials/L180_quartic_small_curvature_deficit/_index|claim]].
Since all critical points of $F$ have modulus at most one, their
factorization in $F'$ gives $|a|\le6$ and $|b|\le4$. Every critical
value has modulus at most $11$. Since some critical point $w$ has
$|w|=1$, the identity $4w^3+2aw+b=0$ gives
$4\le2|a|+|b|$. Consequently

$$
\lambda_F=\max(|a|^{1/2},|b|^{1/3})>1. \tag{1}
$$

For a line $L$ through $\sigma_0$, rotate the target and variable so
that its preimage is the zero set of the real part of a centered monic
quartic. Its quadratic and linear coefficient moduli are still $|a|$
and $|b|$; an imaginary constant may be dropped. The inverse-branch
integral against $|\sigma-\sigma_0|^{-3/4}$ equals its renormalized
length, since the two radial truncations differ by $O(r^{-1})$ at
infinity. Thus
[[theory/polynomials/L179_quartic_harmonic_deficit/_index|L179]] and (1)
give

$$
\widetilde I(F,L)\le-\lambda_F/2500\le-d. \tag{2}
$$

This uses no assumption that the other critical values lie on $L$.

## A uniform far-field constant

We first prove that whenever $|a|\le6$, $|b|\le4$, and $|\sigma_0|\le11$,

$$
\left|G_F(\sigma)-|\sigma-\sigma_0|^{-3/4}\right|
\le K|\sigma-\sigma_0|^{-7/4}
\quad\text{if }|\sigma-\sigma_0|\ge T_0. \tag{3}
$$

Write $H=F-\sigma_0=z^4+az^2+bz+c$, so $|c|\le11$, and put
$\xi=(\sigma-\sigma_0)^{-1/4}$. Its normalized inverse roots solve

$$
w^4+a\xi^2w^2+b\xi^3w+c\xi^4=1.
$$

For $|\xi|\le1/8$ there is exactly one root $w_\omega(\xi)$ in each
disc $|w-\omega|<1/4$, $\omega^4=1$. On its boundary,
$|w^4-1|\ge(1/4)(\sqrt2-1/4)^2(7/4)>1/2$, whereas the perturbation
has modulus at most $651/4096<1/5$. This is Rouché's theorem. At every
root the derivative has modulus at least

$$
4(3/4)^3-2(6/64)(5/4)-4/512=185/128>1.
$$

The roots therefore depend holomorphically on $\xi$ in that disc.
The holomorphic functions

$$
h_\omega(\xi)=
\frac{4\omega^3}{4w_\omega(\xi)^3+2a\xi^2w_\omega(\xi)+b\xi^3}
$$

have modulus at most $4$ there, and direct expansion gives

$$
h_\omega=1+\frac{a}{4\omega^2}\xi^2
              +\frac{b}{2\omega^3}\xi^3+E_\omega(\xi).
$$

Cauchy's coefficient estimate yields
$|E_\omega(\xi)|\le32768|\xi|^4$ for $|\xi|\le1/16$.
In particular $|h_\omega-1|\le130|\xi|^2<3/4$.
For $|u|\le3/4$,
$0\le|1+u|-1-\operatorname{Re}u\le2|u|^2$.
The displayed quadratic and cubic terms cancel on summing over
$\omega^4=1$, so

$$
\left|\frac14\sum_{\omega^4=1}|h_\omega|-1\right|
\le(32768+2\cdot130^2)|\xi|^4<K|\xi|^4.
$$

Since $G_F(\sigma)=|\sigma-\sigma_0|^{-3/4}
\tfrac14\sum|h_\omega|$, this proves (3) for $T_0=16^4$.

## The circle, its tangent line, and their tails

Choose a unit tangent $e$ at $\sigma_0$ and a signed curvature $\kappa$.
The circle, with one point omitted, and its tangent line are parametrized by

$$
\sigma_\kappa(x)=\sigma_0+\frac{ex}{1-i\kappa x/2},
\qquad \sigma_L(x)=\sigma_0+ex,\qquad x\in\mathbb R.
$$

Here $|d\sigma_\kappa/dx|=(1+\kappa^2x^2/4)^{-1}$ and

$$
|\sigma_\kappa-\sigma_0|^{-3/4}|d\sigma_\kappa/dx|
=|x|^{-3/4}(1+\kappa^2x^2/4)^{-5/8}. \tag{4}
$$

Suppose $|\kappa|\le1/T$. On $|x|\ge T$, set $u=1/x$.
Then $|\sigma_\kappa-\sigma_0|=(u^2+\kappa^2/4)^{-1/2}
\ge2T/\sqrt5\ge T_0$.
By (3), the absolute signed tail density in $u$ is at most
$K(u^2+\kappa^2/4)^{-1/8}\le K|u|^{-1/4}$.
Each of the circle and line tails therefore has integral at most
$\tfrac83KT^{-3/4}$. Their total possible contribution to the
difference is at most

$$
\frac{16}{3}KT^{-3/4}\le\frac d8. \tag{5}
$$

For finite circles all local singularities are integrable. Together with
(3), this also establishes the absolute convergence of the signed
integrals used here, including the line case.

## Singular windows without a separation assumption

Write $f_1,f_2,f_3$ for the critical values of $F$, with multiplicity.
In $[-T,T]$ remove the set

$$
E=\{x:|\sigma_L(x)-f_j|\le2\eta
       \text{ for at least one }j\}.
$$

If $|\kappa|T^2/2\le\eta$, then
$|\sigma_\kappa(x)-\sigma_L(x)|\le\eta$ on this whole interval.
Thus a removed piece lies within target distance $2\eta$ of some
$f_j$ on the line and within distance $3\eta$ on the circle.

For a monic quartic, $|F(z)-f_j|\le r$ implies that $z$ lies within
$r^{1/4}$ of one of the four roots of $F-f_j$, counted with
multiplicity. This follows immediately by factoring $F-f_j$.
The preimage of a target line is a real algebraic curve of degree at
most four, and that of a circle has degree at most eight. Euclidean
Crofton bounds their length inside a disc of radius $s$ by $4\pi s$
and $8\pi s$, respectively. Covering the three target windows by these
twelve root discs gives a bound for the sum of the two removed density
integrals:

$$
48\pi(2\eta)^{1/4}+96\pi(3\eta)^{1/4}
<750\eta^{1/4}=\frac d8. \tag{6}
$$

For the numerical inequality one may use
$\pi<4$, $2^{1/4}<6/5$, and $3^{1/4}<4/3$.
Overlaps of the root discs only increase this upper bound. No critical
point or critical value is required to stay separated from another.

## The regular part and the reference term

For $x\notin E$ the straight segment between $\sigma_L(x)$ and
$\sigma_\kappa(x)$ stays at least $\eta$ from every critical value.
Every root above this segment has modulus at most $B=T+12$ by the
Cauchy root bound, since $|\sigma|\le T+11$. On that disc,
$|F'|\le5B^3$ and $|F''|\le M=13B^2$.
The resultant identity

$$
\left|\prod_{F(z)=\sigma}F'(z)\right|
=256\prod_{j=1}^3|f_j-\sigma|
$$

therefore gives $|F'(z)|\ge256\eta^3/(125B^9)>m$ at every root on
the segment. Label the four inverse branches along it. Differentiating
$1/F'$ along a branch bounds its change by
$M|\sigma_\kappa-\sigma_L|/m^3$. Hence the density change is at most
$4M|\kappa|T^2/(2m^3)$, and the additional Jacobian change is bounded
using $G_F(\sigma_L)\le4/m$ and
$1-(1+\kappa^2x^2/4)^{-1}\le\kappa^2x^2/4$.
The absolute difference of the two regular density integrals is at most

$$
\frac{4M|\kappa|T^3}{m^3}+\frac{2\kappa^2T^3}{m}
\le\frac d8+\frac d{16}. \tag{7}
$$

The reference terms can be compared over the entire interval, including
$E$. From (4) and $1-(1+t)^{-5/8}\le5t/8$,

$$
\int_{-T}^T |x|^{-3/4}
 \left(1-(1+\kappa^2x^2/4)^{-5/8}\right)\,dx
\le\frac5{36}\kappa^2T^{9/4}\le\frac d{16}. \tag{8}
$$

All inequalities used in (5)--(8), as well as the required bounds
$|\kappa|\le1/T$ and $|\kappa|T^2/2\le\eta$, follow from the stated
definition of $\kappa_0$. Summing them yields

$$
|\widetilde I(F,\Gamma)-\widetilde I(F,L)|\le\frac d2.
$$

Equation (2) now gives
$\widetilde I(F,\Gamma)\le-d/2=-1/5000$, as claimed.
