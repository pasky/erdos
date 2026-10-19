---
name: theory/polynomials/L184_quartic_petal_length_obstruction/_proof
title: The triangle on the central petal
desc: |
  Radial segments place the three critical points on one component's
  boundary. The triangle inequality bounds that boundary's length,
  while the chord bound for sine controls the reference beta integral.
created: 2026-10-15T23:06:58Z
updated: 2026-10-15T23:06:58Z
---

***

We prove the
[[theory/polynomials/L184_quartic_petal_length_obstruction/_index|claim]].
Put $r=3^{-1/4}$ and $p(z)=z^4+4r^3z$. The three critical points are

$$
c_j=r\exp((2j+1)\pi i/3),\qquad j=0,1,2.
$$

They satisfy $c_j^3=-r^3$, so
$p(c_j)=3r^3c_j$ and $|p(c_j)|=3r^4=1$.
For $0\le s<1$,

$$
p(sc_j)=\frac{4s-s^4}{3}p(c_j),\qquad
0\le\frac{4s-s^4}{3}<1.
$$

The segment from zero to each $c_j$, excluding its endpoint, therefore
lies in the same component $\Omega$ of $\{|p|<1\}$. All three $c_j$
belong to $\partial\Omega$.

There are no critical points inside $\Omega$. The restriction of $p$
to that component is a proper unramified map to the unit disc, hence a
conformal bijection: an unramified connected cover of the simply connected
disc has one sheet. Its inverse $\phi$ extends continuously to the
closed disc. Indeed an inverse branch of a polynomial has a convergent
Puiseux expansion at each boundary critical value, and is analytic at
the remaining boundary values. These expansions also make the boundary
curve rectifiable. The radial identities above give
$\phi(p(c_j))=c_j$. Traversing the unit circle visits the three values
$p(c_j)$ once each; applying the triangle inequality to the three arcs
of the closed curve $\phi(\mathbf T)$ gives

$$
\operatorname{length}(\partial\Omega)
 \ge |c_0-c_1|+|c_1-c_2|+|c_2-c_0|
 =3\sqrt3r=3^{5/4}.
$$

For completeness, the boundary parameterization counts each regular
boundary arc once. Two distinct arguments cannot have the same boundary
image, since $p\circ\phi$ is the identity on the closed disc. Thus its
curve length is the boundary length used above.

Write $\ell_0=\ell(z^4-1)$. Solving for the four inverse roots on the
unit circle gives the density $|1+e^{i\theta}|^{-3/4}$, and therefore

$$
\frac{\ell_0}{4}
 =2^{-3/4}\int_0^{\pi/2}(\sin u)^{-3/4}\,du
 \le2^{-3/4}\int_0^{\pi/2}(2u/\pi)^{-3/4}\,du
 =2^{1/4}\pi<3^{5/4}.
$$

The last strict inequality follows, for example, from $\pi<22/7$.
Combining the two estimates proves the claim. The other petals can be
shorter; this argument concerns a proposed bound for each petal
individually and does not refute a bound on their total length.
