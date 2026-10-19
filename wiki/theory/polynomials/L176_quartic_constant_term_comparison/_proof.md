---
name: theory/polynomials/L176_quartic_constant_term_comparison/_proof
title: Proof of the quartic constant-term comparison obstruction
desc: |
  Critical values give an explicit family of flattening circles. A lower
  bound for the length of a harmonic tree makes the limiting comparison
  with the same constant term positive, and uniform local and far-field
  estimates transfer this sign to the quartic family.
created: 2026-10-15T20:21:22Z
updated: 2026-10-15T20:21:22Z
---

***

We prove the
[[theory/polynomials/L176_quartic_constant_term_comparison/_index|stated obstruction]].
All lengths are Euclidean arc lengths; crossing points are counted once,
which has no effect on length integrals.

## The family and its limiting line

For $y>0$ put

$$
F_y(z)=z^4+(2y^2-\tfrac32)z^2-(1+4y^2)z.
$$

Its derivative is
$4(z-1)((z+\frac12)^2+y^2)$, so its three simple critical points are
$1$ and $-\frac12\pm iy$. Their values are

$$
v_y=-\tfrac32-2y^2,\qquad
u_y\pm4iy^3,\qquad
u_y=\tfrac3{16}+\tfrac52y^2-y^4.
$$

Thus $d_y=v_y-u_y=y^4-\frac92y^2-\frac{27}{16}$.
Its positive zero is
$Y=\sqrt{\frac94+\frac32\sqrt3}$, and $d_y>0$ for $y>Y$.
The circle $\Gamma_y$ through these values has real center and radius

$$
C_y=v_y-R_y,\qquad
R_y=\frac{d_y^2+16y^6}{2d_y}.
$$

Indeed $|v_y-C_y|=R_y$ and
$(u_y-C_y)^2+16y^6=(R_y-d_y)^2+16y^6=R_y^2$.
Consequently
$p_y(z)=R_y^{-1}F_y(R_y^{1/4}z)-C_y/R_y$ is centered and monic and has
three distinct critical values on the unit circle. Its critical points
are distinct too.

As $y\downarrow Y$, the radius tends to infinity and
$-C_y/R_y=1-v_y/R_y\to1$. The other two nonleading coefficients tend to
zero. Hence $p_y\to z^4+1$. On every bounded set $\Gamma_y$ converges
smoothly to the line

$$
L=-c+i\mathbb R,\qquad c=6+3\sqrt3,
$$

and
$F_Y(z)=z^4+(3+3\sqrt3)z^2-(10+6\sqrt3)z$ has all three critical values
on $L$.

## The limiting integral is positive

For any centered monic quartic $F$, set

$$
G_F(\sigma)=\sum_{F(z)=\sigma}\frac1{|F'(z)|}
$$

away from its critical values. Write $F=F_Y$ and define

$$
J=\int_{-\infty}^{\infty}
\left(G_F(-c+iv)-|v|^{-3/4}\right)\,dv,
\qquad
I=\int_{-\infty}^{\infty}
\left(G_F(-c+iv)-(c^2+v^2)^{-3/8}\right)\,dv.
$$

Both differences are absolutely integrable. Near a critical value the
inverse branches have integrable square-root singularities, since the
critical points are simple. At infinity the estimate proved below gives
$G_F(\sigma)=|\sigma|^{-3/4}+O(|\sigma|^{-7/4})$, and translating the
reference by the fixed number $c$ preserves integrability.

Let $H=\{z:\operatorname{Re}F(z)=-c\}$. Centering and monicity give
eight ends of $H$, with asymptotic directions

$$
e_j=\exp\bigl(i(\pi/8+j\pi/4)\bigr),\qquad 0\le j<8.
$$

For sufficiently large $r$ each end meets $|z|=r$ once, at
$re_j+O(r^{-1})$. This follows by applying the implicit function theorem
to $\operatorname{Re}(r^{-4}(F(re^{i\theta})+c))=0$ near the eight
simple zeros of $\cos4\theta$; differentiating also makes the end radial
coordinate eventually monotone. The same expansion shows

$$
J=\lim_{r\to\infty}\bigl(|H\cap\{|z|\le r\}|-8r\bigr). \tag{1}
$$

For completeness, cutting the integral defining $J$ at $|v|\le r^4$
gives the length of the part of $H$ with $|F(z)+c|\le r^4$, minus $8r$.
Along each end its cutting point differs from that on $|z|=r$ by
$O(r^{-1})$, because $F$ has no cubic term. Thus the two length cuts
differ by $O(r^{-1})$.

The only vertices of $H$ are its three critical points
$w_0=1$, $w_+=-\frac12+iY$, $w_-=-\frac12-iY$, each of valence four.
There is no cycle: a cycle would contain a Jordan curve on which the
harmonic function $\operatorname{Re}F+c$ vanishes, forcing that function
to vanish on the enclosed domain by the maximum principle. Cut the eight
ends at a sufficiently large circle and regard the cut points as vertices
of valence one. The resulting finite forest has eleven vertices and ten
edges, by the degree sum $3\cdot4+8=20$. It is therefore a tree. In
particular it has two finite edges connecting the three critical points.
Their total length is at least

$$
2\sqrt{\tfrac94+Y^2}>5, \tag{2}
$$

since the two distances from $w_0$ to $w_\pm$ are the two shortest
pairwise distances and $Y>2$.

For a unit vector $e$ let
$h(e)=\max_{w\in\{w_0,w_+,w_-\}}\operatorname{Re}(w\bar e)$.
An end beginning at a critical point has length, up to its intersection
with $|z|=r$, at least $r-h(e_j)+o(1)$. In the upper half-plane the
maximizing point is $w_0$ in direction $\pi/8$, and $w_+$ in directions
$3\pi/8,5\pi/8,7\pi/8$. To check the first two assertions, use
$Y<9/4<\frac32\cot(\pi/8)$ and
$Y>2>\frac32\cot(3\pi/8)$; the last two are immediate. Conjugation
handles the lower half-plane. Writing $q=\cos(\pi/8)$ and
$s=\sin(\pi/8)$, we obtain

$$
\sum_{j=0}^7h(e_j)=3q+2Y(2q+s)
<3+\frac92\left(2+\frac12\right)=\frac{57}{4}. \tag{3}
$$

Here $2<Y<9/4$, $q<1$ and $s<1/2$. The bound on $Y$ follows directly
from its displayed square: $Y^2>4$ and $Y^2<81/16$.
Combining (1)--(3) gives $J>-37/4$.

The difference between the two reference integrals is exactly

$$
I-J=c^{1/4}K,\qquad
K=\int_{-\infty}^{\infty}
\left(|v|^{-3/4}-(1+v^2)^{-3/8}\right)\,dv>6.
$$

Indeed the integrand is positive everywhere and its integral on
$[-1,1]$ is greater than $2\int_0^1(v^{-3/4}-1)\,dv=6$.
Also $c>11>(9/5)^4$. Therefore

$$
I> -\frac{37}{4}+\frac{54}{5}=\frac{31}{20}. \tag{4}
$$

## Passing to the nearby circles

Inverse-branch integration and the change of scale give exactly

$$
R_y^{1/4}\left(\ell(p_y)-\ell(z^4+p_y(0))\right)
=\int_{\Gamma_y}\left(G_{F_y}(\sigma)-|\sigma|^{-3/4}\right)|d\sigma|.
\tag{5}
$$

The reference is correct because
$|\sigma|^{-3/4}$ is the inverse-derivative density of $z^4$, and
$\{z:z^4\in\Gamma_y\}$ has length
$R_y^{1/4}\ell(z^4-C_y/R_y)$.

We justify convergence of the right side of (5) to $I$, including its
singularities and expanding tail. Restrict $y$ to a small fixed compact
interval about $Y$. Its critical points stay simple and separated and
their second derivatives stay bounded away from zero. The local inverse
function theorem in a square-root coordinate therefore gives uniform
constants $A,\eta_0>0$ such that, near each critical value $f_y$,

$$
G_{F_y}(\sigma)\le A|\sigma-f_y|^{-1/2}+A
\quad (0<|\sigma-f_y|<\eta_0).
$$

Since $\Gamma_y$ passes through $f_y$ and its radius tends to infinity,
integrating this estimate over $|\sigma-f_y|<\eta$ gives
$O(\eta^{1/2})$, uniformly for $y>Y$ sufficiently close to $Y$.
One can see this directly from the chord formula
$|\sigma-f_y|=2R_y|\sin(t/(2R_y))|$ in arclength $t$ from $f_y$.
The reference has no singularity there: the distance from $0$ to
$\Gamma_y$ is $|v_y|\to c>0$.

Away from these windows, smooth convergence of the circles and the
implicit function theorem for simple roots give convergence on each
bounded set. To control infinity uniformly, take $\rho^4=\sigma$ and
$\omega^4=1$. For $F_y(z)=z^4+a_yz^2+b_yz$, its four inverse branches
have the uniform expansions

$$
z_\omega=\omega\rho-\frac{a_y}{4\omega\rho}
-\frac{b_y}{4\omega^2\rho^2}+O(|\rho|^{-3}),
\qquad
\frac{dz_\omega}{d\sigma}
=\frac{\omega}{4\rho^3}
\left(1+\frac{a_y}{4\omega^2\rho^2}
+\frac{b_y}{2\omega^3\rho^3}+O(|\rho|^{-4})\right).
$$

These are convergent inverse series near infinity with a uniform radius
for the bounded coefficient family; differentiation is legitimate there.
On summing the moduli, the linear terms of orders $\rho^{-2}$ and
$\rho^{-3}$ cancel because
$\sum_{\omega^4=1}\omega^{-2}=\sum_{\omega^4=1}\omega^{-3}=0$.
Consequently

$$
\left|G_{F_y}(\sigma)-|\sigma|^{-3/4}\right|
\le B|\sigma|^{-7/4}
$$

beyond a fixed radius, with $B$ independent of $y$. The length of the
part of any circle in a disc of radius $r$ is at most $2\pi r$ (and that
of a line is at most $2r$). Summing over the annuli
$2^jT<|\sigma|\le2^{j+1}T$ bounds the integral of
$|\sigma|^{-7/4}$ on the tail by
$4\pi T^{-3/4}\sum_{j\ge0}2^{-3j/4}$, independently of the circle.
Thus the tails tend uniformly to zero.

First remove the critical windows and the tail, take $y\downarrow Y$
on the remaining compact arcs, and then let the windows shrink and the
tail radius increase. This proves convergence in (5) to $I$. Inequality
(4) proves the claimed limit and hence the strict length comparison for
all $y>Y$ sufficiently close to $Y$.
