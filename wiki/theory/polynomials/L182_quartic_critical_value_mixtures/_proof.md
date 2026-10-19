---
name: theory/polynomials/L182_quartic_critical_value_mixtures/_proof
title: Opposite tails obstruct every fixed convex mixture
desc: |
  Exact inverse derivatives for z^4-2z^2 give incompatible far-tail
  requirements. A strict two-point inequality persists on nearby circles
  and under an explicit regular perturbation of the critical points.
created: 2026-10-15T23:06:58Z
updated: 2026-10-15T23:06:58Z
---

***

Write $G_F(\sigma)=\sum_{F(z)=\sigma}|F'(z)|^{-1}$ at a regular value of
$F$. We prove the
[[theory/polynomials/L182_quartic_critical_value_mixtures/_index|claim]]
using $F(z)=z^4-2z^2$, whose critical values are $-1$ and $0$.

## The two tails on the real line

For $T>1$, solving $F(z)=\sigma$ first for $z^2$ gives

$$
\begin{aligned}
G_F(T)
 &=\frac{(\sqrt{T+1}+1)^{-1/2}
            +(\sqrt{T+1}-1)^{-1/2}}{2\sqrt{T+1}}\\
 &=T^{-3/4}\left(1-\frac{3}{8T}+O(T^{-2})\right),\\
G_F(-T)
 &=\frac{T^{-1/4}}{\sqrt{T-1}}
  =T^{-3/4}\left(1+\frac{1}{2T}+O(T^{-2})\right).
\end{aligned} \tag{1}
$$

Indeed $F'(z)=4z(z^2-1)$. At $\sigma=T$ the two values of $z^2$ are
$1\pm\sqrt{T+1}$, and at $\sigma=-T$ they are
$1\pm i\sqrt{T-1}$, each of modulus $\sqrt T$. The expansions in (1)
follow from the convergent binomial series at $1/T=0$; in the first one
the terms odd in $(T+1)^{-1/2}$ cancel.

A mixture supported at the two critical values has the form

$$
H_\alpha(\sigma)=\alpha|\sigma+1|^{-3/4}
                    +(1-\alpha)|\sigma|^{-3/4},\qquad 0\le\alpha\le1.
$$

Its two tails satisfy

$$
H_\alpha(T)+H_\alpha(-T)
 =2T^{-3/4}+O(T^{-11/4}), \tag{2}
$$

uniformly in $\alpha$: the terms of order $T^{-7/4}$ cancel, and the
remainders of the two binomial series are bounded uniformly before
multiplication by $\alpha$. In contrast, (1) gives

$$
G_F(T)+G_F(-T)
 =2T^{-3/4}+\frac18T^{-7/4}+O(T^{-11/4}). \tag{3}
$$

Fix a sufficiently large finite $T$ so that (3) strictly exceeds (2) for
every $\alpha\in[0,1]$. Equivalently, the fixed positive gap is

$$
G_F(T)+G_F(-T)>
\max_{f\in\{-1,0\}}
 \left(|T-f|^{-3/4}+|-T-f|^{-3/4}\right). \tag{4}
$$

Thus the obstruction is uniform over all allowed weights. Looking at the
tails separately would require $\alpha\le1/2$ from the positive tail
and $\alpha\ge2/3$ from the negative tail.

## Passing to circles and monic quartics

For $R>1/2$, put

$$
h_R=\sqrt{R^2-\tfrac14},\qquad
C_R=-\tfrac12+ih_R,\qquad
\Gamma_R=\{\sigma:|\sigma-C_R|=R\}.
$$

These circles pass through $-1$ and $0$ and converge locally to the real
line as $R\to\infty$. More explicitly, for each fixed real $x$, their
lower arcs contain

$$
\sigma_R(x)=x+i\left(h_R-\sqrt{h_R^2-x^2-x}\right)
 \longrightarrow x
$$

when $R$ is sufficiently large. Use $x=T,-T$ with the fixed $T$ of (4).
These target points stay away from the critical values. Their inverse
roots are simple, so $G_F$ and both reference densities are continuous
there. The strict inequality (4) consequently holds with $T,-T$
replaced by $\sigma_R(T),\sigma_R(-T)$ for every sufficiently large $R$.
No $H_\alpha$ can dominate $G_F$ at both of these points.

The centered monic polynomial

$$
q_R(z)=\frac{F(R^{1/4}z)-C_R}{R}
      =z^4-2R^{-1/2}z^2-C_R/R \tag{5}
$$

has unit critical values $(-1-C_R)/R$ and $-C_R/R$, and tends in
coefficients to $z^4-i$. With $\zeta=(\sigma-C_R)/R$, both sides of a
putative density majorant for $q_R$ equal $R^{3/4}$ times the
corresponding side for $F$ on $\Gamma_R$. Therefore the same strict
two-point obstruction applies to $q_R$.

## Separating the critical values

Fix such an $R$, and for small $\delta>0$ set

$$
t=\delta(-h_R+i/2),\qquad
F_t(z)=z^4-2(1+t+t^2)z^2+4t(1+t)z.
$$

Its critical points are $1,t,-1-t$, with values $f_1,f_2,f_3$ in that
order. Direct substitution gives

$$
f_1\to-1,\qquad f_2\to0,\qquad f_3\to-1,\qquad
f_3-f_1=-t(2+t)^3.
$$

For all sufficiently small positive $\delta$ these values are distinct
and noncollinear: $f_2-f_1\to1$ while
$(f_3-f_1)/\delta\to-8(-h_R+i/2)$ has nonzero imaginary part. Let
$C_t,R_t$ be their circumcenter and circumradius. The circumcenter
equations, the second divided by $\delta$, converge to

$$
2\operatorname{Re}(C+1)=1,\qquad
\operatorname{Re}\bigl((C+1)\overline{(-h_R+i/2)}\bigr)=0.
$$

This nonsingular real linear system has the unique solution $C=C_R$.
Hence $C_t\to C_R$ and $R_t\to R$. The centered monic polynomial

$$
p_t(z)=R_t^{-1}\bigl(F_t(R_t^{1/4}z)-C_t\bigr) \tag{6}
$$

therefore tends to $q_R$ and has three distinct unit critical values.

Keep the two unit target points of (5) fixed during this perturbation.
They are regular values of $q_R$, so all four roots above each remain
simple nearby and their inverse-derivative densities converge. The
critical values of $p_t$ converge to those of $q_R$; thus the maximum
over the three reference centers of the sum of the two reference
densities also converges to the maximum over the two centers in (4),
with the scaling described after (5). The strict two-point gap persists.
Since a convex combination of three numbers never exceeds their maximum,
every fixed triple of weights fails at one of those two target points.

Finally choose $R$ so large that the coefficients of $q_R$ differ from
those of $z^4-i$ by less than $\epsilon/2$, while retaining the strict gap.
Then choose $\delta$ small enough that the coefficients of $p_t-q_R$
have modulus less than $\epsilon/2$ and the gap persists. This is the
quartic required in the statement. The argument supplies an obstruction
to the proposed pointwise majorant, not to the integrated length bound.
