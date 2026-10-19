---
name: theory/polynomials/L177_quartic_maximizer_critical_values/_proof
title: Strictness in the off-circle critical-value deformation
desc: |
  The length formula from Eremenko and Hayman's local deformation and
  equality in the holomorphic mean-value inequality force a putative
  maximizing deformation to be the identity outside its support. Polynomial
  identity then contradicts the moved critical value.
created: 2026-10-15T20:21:22Z
updated: 2026-10-15T20:21:22Z
---

***

Let $p$ be a local maximizer as in the
[[theory/polynomials/L177_quartic_maximizer_critical_values/_index|claim]],
and suppose that $a$ is a critical value with $|a|\ne1$.
Choose a disc $U=D(a,r)$ whose closure misses the unit circle and all
other distinct critical values.

## The source premise

We use the construction in the proof of Eremenko and Hayman's Lemma 5,
pp. 5--6 of the authors' corrected preprint identified on the
[[../library/polynomials/eremenko_1999_length_lemniscates/_index|source card]].
Choose a smooth function $\Phi$ supported in $U$ with $\Phi(a)=1$ and put
$\phi_\lambda(w)=w+\lambda\Phi(w)$. For $\lambda$ in a sufficiently small
complex disc about zero, the source constructs quasiconformal maps
$\psi_\lambda$, with $\psi_0(z)=z$ and

$$
\psi_\lambda(z)=z+o(1)\quad(z\to\infty),\qquad
p_\lambda=\phi_\lambda\circ p\circ\psi_\lambda^{-1}.
$$

The $p_\lambda$ are monic quartics, continuous in their coefficients,
and their critical values are those of $p$ with $a$ replaced by
$a+\lambda$. Multiplicities are preserved; all critical points with
value $a$ move in this way. The maps $\psi_\lambda$ are conformal off
$p^{-1}(\overline U)$, depend holomorphically on $\lambda$ at each such
point, and are conformal on a common neighborhood of $E(p)$. The source
gives

$$
E(p_\lambda)=\psi_\lambda(E(p)),\qquad
\ell(p_\lambda)=\int_{E(p)}|\psi_\lambda'(z)|\,|dz|. \tag{1}
$$

The function $h_z(\lambda)=\psi_\lambda'(z)$ is holomorphic in
$\lambda$ for each $z$ in that neighborhood, with $h_z(0)=1$. On
compact subsets the needed parameter and spatial continuity follow
from the source's analytic-dependence construction and the Cauchy
formula in $z$.

This local construction is used as an external source premise. Its
formulas, normalization, support, analytic dependence and length formula
were read in proof on 2026-10-15 against pp. 5--7 of the corrected preprint
identified on the source card, including the page images and transcription;
the Beltrami existence and analytic-dependence theorems cited there are
not re-proved here. The source's continuation along arcs is not used.

## Constancy of length forces a trivial deformation

By (1), $\lambda\mapsto\ell(p_\lambda)$ is subharmonic. Local maximality
of $p$, and continuity of the coefficients of $p_\lambda$, make it at
most $\ell(p)$ in a small disc. The maximum principle makes it constant
there.

Fix a circle $|\lambda|=\rho$ contained in that disc. For each
$z\in E(p)$ the mean-value inequality gives

$$
\frac1{2\pi}\int_0^{2\pi}|h_z(\rho e^{i\theta})|\,d\theta\ge1.
$$

Integrating over $E(p)$ and using (1) and constancy shows equality for
arclength-almost every $z\in E(p)$. Equality forces $h_z\equiv1$ in
$|\lambda|<\rho$: the mean of $h_z$ is $h_z(0)=1$, and equality in the
triangle inequality says that its boundary values lie on the
nonnegative real axis almost everywhere. Continuity makes the boundary
imaginary part zero everywhere, the harmonic maximum principle makes
it zero in the disc, and the open mapping theorem makes $h_z$ constant.

We next check the spatial component on which this equality holds. The
open set

$$
\Omega=\mathbb C\setminus p^{-1}(\overline U)
=\{z:|p(z)-a|>r\}
$$

is connected. Indeed it contains a neighborhood of infinity, and a
bounded component would have $|p-a|=r$ on its boundary and $|p-a|>r$
inside, contradicting the maximum modulus principle for the polynomial
$p-a$. Since $\overline U$ misses the unit circle, $E(p)\subset\Omega$.

Fix $|\lambda|<\rho$. The holomorphic function
$\psi_\lambda'-1$ on $\Omega$ vanishes at arclength-almost every point
of $E(p)$. The latter contains a regular arc: take any unit value that
is not one of the finitely many critical values and apply the inverse
function theorem. Zeros on that arc have an accumulation point in
$\Omega$. The identity theorem therefore gives
$\psi_\lambda'\equiv1$ on $\Omega$. Connectedness gives
$\psi_\lambda(z)=z+b_\lambda$ there, and the principal normalization
at infinity forces $b_\lambda=0$.

For $z\in\Omega$ we have $\phi_\lambda(p(z))=p(z)$, so the defining
identity for $p_\lambda$ now gives $p_\lambda(z)=p(z)$. Polynomial
identity implies $p_\lambda=p$ everywhere. For a sufficiently small
nonzero $\lambda$, however, $a+\lambda$ is a critical value of
$p_\lambda$ and is not a critical value of $p$, since $U$ contains no
other such value. This is a contradiction.

Thus a local maximizing quartic has no critical value off the unit
circle, as claimed. The argument is author-recorded; it does not assert
an independent audit of the source construction.
