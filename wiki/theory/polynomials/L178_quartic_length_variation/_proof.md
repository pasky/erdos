---
name: theory/polynomials/L178_quartic_length_variation/_proof
title: Critical-value motion and the exact Hessian
desc: |
  Polynomial division constructs a holomorphic motion before a real
  normalization puts the critical values back on the unit circle. Its
  velocity and acceleration give the length derivatives and, by the chain
  rule, the Hessian in angular-gap coordinates.
created: 2026-10-15T20:21:22Z
updated: 2026-10-15T20:21:22Z
---

***

Let $p=z^4+az^2+bz+c$ satisfy the
[[theory/polynomials/L178_quartic_length_variation/_index|claim]].
Its three critical points are simple, since it has three distinct
critical values. Polynomial division gives

$$
\begin{aligned}
V_p(z)&=\frac{z^5}{4}+\frac{3a z^3}{8}+\frac{7b z^2}{16}
       +\left(\frac{a^2}{16}+\frac c2\right)z+\frac{3ab}{16},\\
Q_p(z)&=V_p'(z)=\frac54z^4+\frac{9a}{8}z^2+\frac{7b}{8}z
       +\frac{a^2}{16}+\frac c2,\\
R_p(z)&=p(z)^2-p'(z)V_p(z)=r_2z^2+r_1z+r_0,\\
r_2&=ac-\frac{a^3}{8}+\frac{9b^2}{16},\qquad
r_1=\frac32bc-\frac{7a^2b}{16},\qquad
r_0=c^2-\frac{3ab^2}{16}.
\end{aligned} \tag{1}
$$

## A local family with prescribed critical values

Solve the holomorphic coefficient differential equation

$$
\partial_\tau q_\tau=R_{q_\tau},\qquad q_0=p. \tag{2}
$$

Its polynomial right-hand side gives a unique holomorphic solution for
$\tau$ in a neighborhood of zero, consisting of centered monic
quartics. The critical points remain simple there. At a moving critical
point $c_j(\tau)$ its value $v_j(\tau)=q_\tau(c_j(\tau))$ satisfies

$$
v_j'(\tau)=R_{q_\tau}(c_j(\tau))=v_j(\tau)^2,
\qquad v_j(\tau)=\frac{v_j}{1-\tau v_j}. \tag{3}
$$

Shrink the parameter neighborhood to lie in $|\tau|<1$ and define

$$
p_\tau(z)=(1-|\tau|^2)
 q_\tau\bigl((1-|\tau|^2)^{-1/4}z\bigr)-\bar\tau. \tag{4}
$$

This is a real analytic centered monic family. Its critical values are

$$
\frac{v_j-\bar\tau}{1-\tau v_j}, \tag{5}
$$

which lie on the unit circle and stay distinct. No global continuation
or theorem about the critical-value map is needed here.

## Differentiating the length

For $\zeta$ on the unit circle and different from the three $v_j$, each
solution $w=w(\tau,\zeta)$ of

$$
q_\tau(w)=\frac{\zeta}{1-\tau\zeta}
$$

is locally holomorphic in $\tau$. Differentiating and using (2) gives

$$
\partial_\tau w=V_{q_\tau}(w). \tag{6}
$$

On each of the open arcs between consecutive $v_j$ choose the four
inverse branches and let $h=\partial_\theta w$, where
$\zeta=e^{i\theta}$. This tangent derivative is nonzero, and (6) implies

$$
\partial_\tau\log h=Q_{q_\tau}(w),\qquad
\partial_\tau^2\log h\big|_{\tau=0}=W_p(w), \tag{7}
$$

where, by differentiating (1) in the coefficient direction $R_p$,

$$
W_p=V_pQ_p'+\frac{9r_2}{8}z^2+\frac{7r_1}{8}z
                   +\frac{ar_2}{8}+\frac{r_0}{2}. \tag{8}
$$

The singular endpoints cause no loss of differentiability. Near a
simple critical point the inverse branches have a convergent square-root
expansion. The parameterization in (3) moves the endpoint and the target
by the same fractional linear map, so that the singular factor is
$|\theta-\theta_j|^{-1/2}$ at a fixed value of $\theta_j$. The expansion
coefficients are holomorphic in $\tau$ and bounded on a smaller closed
parameter disc, since the critical points remain simple and their values
remain distinct. Consequently $|h|$ has a common integrable majorant.
The factors $Q_{q_\tau}(w)$ and their first parameter derivatives are
bounded there as well, since all the roots in question stay in a compact
set. Thus the first and second parameter derivatives of $|h|$ have a
common integrable majorant. Differentiation under the sum and integral
below is justified.

The fractional linear image of the unit circle is the circle with
center $\bar\tau/(1-|\tau|^2)$ and radius $(1-|\tau|^2)^{-1}$. The
length of its inverse image under $q_\tau$ is

$$
L(\tau)=\sum_{\text{arcs and branches}}\int |h(\tau,\theta)|\,d\theta,
\qquad \ell(p_\tau)=(1-|\tau|^2)^{1/4}L(\tau). \tag{9}
$$

The sum counts every regular arc of the lemniscate once; the finitely
many critical points have zero arclength. If $h$ is nonzero and
holomorphic in $\tau$, (7) gives at zero

$$
\begin{aligned}
\partial_\tau |h|&=\tfrac12Q|h|,\\
\partial_\tau\partial_{\bar\tau}|h|&=\tfrac14|Q|^2|h|,\\
\partial_\tau^2|h|&=(\tfrac12W+\tfrac14Q^2)|h|.
\end{aligned} \tag{10}
$$

Divide the integrals by $L(0)=\ell(p)$ and write $\mathbb E$ for
normalized arclength expectation on $E(p)$. With $m=\mathbb E Q$,
equations (9)--(10), including the derivative of its real prefactor,
give for $u=\log\ell(p_\tau)$

$$
\begin{aligned}
2u_\tau&=m,\\
4u_{\tau\bar\tau}&=\mathbb E|Q|^2-|m|^2-1,\\
2u_{\tau\tau}&=\mathbb E W+\tfrac12(\mathbb E Q^2-m^2).
\end{aligned} \tag{11}
$$

All derivatives in (11) are evaluated at zero. In particular
$\Delta_\tau u=\operatorname{Var}(Q)-1$ and
$\Delta_\tau\ell(p_\tau)/\ell(p)=\mathbb E|Q|^2-1$ there.

## The Hessian in angular gaps

Label the critical values in counterclockwise order as $v_1,v_2,v_3$.
Choose local real arguments $\theta_j(\tau)$ of (5), and let
$\omega_1=(\theta_2-\theta_1)/(2\pi)$ and
$\omega_2=(\theta_3-\theta_2)/(2\pi)$; the last gap is
$1-\omega_1-\omega_2$. Put

$$
\delta_j=v_{j+1}-v_j,\qquad
\epsilon_j=v_{j+1}^2-v_j^2,\qquad j=1,2.
$$

The real Jacobian at zero is

$$
J=\frac1\pi
\begin{pmatrix}
\operatorname{Im}\delta_1&\operatorname{Re}\delta_1\\
\operatorname{Im}\delta_2&\operatorname{Re}\delta_2
\end{pmatrix}. \tag{12}
$$

It is invertible: three distinct points of a circle are not collinear.
Hence the gaps are real local coordinates for this family. Let $g$ be
the two-component gradient of $\log\ell$ in these coordinates at $p$.
By (11), it is determined by

$$
J^{\mathsf T}g=(\operatorname{Re}m,-\operatorname{Im}m)^{\mathsf T}. \tag{13}
$$

Expanding the arguments in (5) gives

$$
\theta_j(\tau)=\theta_j(0)+2\operatorname{Im}(\tau v_j)
                         +\operatorname{Im}(\tau^2v_j^2)+O(|\tau|^3).
$$

Thus each $\omega_j$ is harmonic in $\tau$ and its real Hessian at zero is

$$
H_j=\frac1\pi
\begin{pmatrix}
\operatorname{Im}\epsilon_j&\operatorname{Re}\epsilon_j\\
\operatorname{Re}\epsilon_j&-\operatorname{Im}\epsilon_j
\end{pmatrix}. \tag{14}
$$

The chain rule says that the Hessian in the gaps is
$J^{-\mathsf T}(D^2_\tau u-g_1H_1-g_2H_2)J^{-1}$.
The middle symmetric matrix has trace $\operatorname{Var}(Q)-1$ and
eigenvalues

$$
\frac{\operatorname{Var}(Q)-1}{2}\ \mathbin{\pm}\ |B|,
\quad
B=\mathbb E W+\frac{\mathbb E Q^2-m^2}{2}
                 +\frac{i}{\pi}\sum_{j=1}^2g_j\epsilon_j. \tag{15}
$$

Congruence by an invertible real matrix preserves positive
semidefiniteness. Therefore convexity of $\log\ell$ in the gaps at $p$
is equivalent to the exact inequality

$$
\boxed{\operatorname{Var}(Q)-1\ge2|B|.} \tag{16}
$$

Equation (16) is a criterion, not an established inequality for every
quartic. The weaker trace inequality and the stationary-point test
following (11) are likewise unresolved in the linked research sketch.
