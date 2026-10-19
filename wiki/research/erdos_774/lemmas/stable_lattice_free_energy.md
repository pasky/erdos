---
name: research/erdos_774/lemmas/stable_lattice_free_energy
title: A dimension-uniform weak Gaussian bound for stable lattices
desc: Regular M-ellipsoids and a fixed-parameter Voronoi induction give log theta_L(t) <= epsilon(t) rank(L), with epsilon(t) tending to zero uniformly over stable lattices.
tags: [E0774, lattice, extraction, proved]
sources: []
created: 2026-09-19T01:18:00Z
updated: 2026-09-19T01:18:00Z
---


# A dimension-uniform weak Gaussian bound for stable lattices

***

## The theorem

A rank-$m$ Euclidean lattice $L$ is *stable* if $\det L=1$ and every
nonzero sublattice has determinant at least one. Set

$$
\theta_L(t)=\sum_{v\in L}e^{-\pi t^2\|v\|^2}.
$$

**Theorem.** There are an absolute $T_0$ and a function
$\epsilon(t)\downarrow0$, independent of rank, such that every stable
lattice satisfies

$$
\boxed{\theta_L(t)\leq e^{\epsilon(t)m}\quad(t\geq T_0).} \tag{1}
$$

Consequently, for $0<u\leq1/T_0$,

$$
\boxed{\theta_L(u)\leq u^{-m}e^{\epsilon(1/u)m}.}       \tag{2}
$$

This is an exponential-in-dimension bound, not a dimension-free bound
such as $\theta_L(t)\leq3/2$ at fixed $t$. It is nevertheless sufficient
for [critical moment extraction](../routes/moment_boundary_extraction.md).

## 1. The checked convex-body input

The regular $M$-ellipsoid theorem, at parameter $\alpha=1$, supplies
an absolute $C\geq1$: every symmetric convex body $K\subset\mathbb R^m$
has a centered ellipsoid $E$ with

$$
N(K,uE),\ N(E,uK)\leq e^{Cm/u}\qquad(u\geq C).       \tag{3}
$$

Here $N(F,H)$ is the least number of translates of $H$ covering $F$. The exact
statement was checked in
[Vritsiou, Theorem 1, equations (2)--(3)](../../../../library/discrete_geometry/vritsiou_2023_regular_ellipsoids_blaschke_santalo_type_inequality_projections_non_symmetric_convex_bodies/_index.md)
(arXiv:2303.17753v2). It explicitly restates Pisier's 1989 theorem; this is not
a new verification of Pisier's original proof.

For measurable $F\subset\mathbb R^m$, write
$\gamma(F)=\int_F e^{-\pi\|x\|^2}\,dx$ and
$\Gamma_t(F)=\gamma(tF)$. Define

$$
c=\frac{e^{-1/2}}{2C},\qquad T_0=16eC^4,\qquad
a(t)=\frac{t}{4e}-\frac{\log2}{2},
$$

$$
\epsilon(t)=\frac{C/c}{\sqrt t}
             -\log(1-e^{-a(t)})\qquad(t\geq T_0).  \tag{4}
$$

These constants are dimension-independent, $a(t)>0$, and
$\epsilon(t)$ is positive and decreases to zero.

## 2. Every volume-one symmetric body has a good position

**Claim.** If $K=-K$ and $|K|=1$, then for each $t\geq T_0$ there
is $A\in\mathrm{SL}_m(\mathbb R)$ with

$$
\Gamma_t(AK)\geq e^{-\epsilon(t)m}.                \tag{5}
$$

**Proof.** Let $D_m=r_mB_2^m$ be the volume-one ball, and put
$b=|E|^{1/m}$. Applying (3) at $u=2C$ and comparing volumes gives

$$
1\leq e^{m/2}(2C)^m|E|,\qquad b\geq c.
$$

Write $E=TB_2^m$ with $T$ positive definite. The map
$A=br_mT^{-1}$ has determinant one and sends $E$ to $bD_m$.
Put $R=\sqrt t$, $u=bt/R=b\sqrt t$. Since
$t\geq T_0=(2C/c)^2$, one has $u\geq2C$. Invariance and scaling of
covering numbers give

$$
N(RD_m,tAK)=N(bD_m,(bt/R)AK)
           =N(E,uK)
           \leq e^{(C/c)m/\sqrt t}.               \tag{6}
$$

For every symmetric convex body $F$, its translates have Gaussian
measure at most $\gamma(F)$. An elementary justification is as follows.
For each centered ball $B$, put $U=(F+x)\cap B$.
Symmetry and convexity give $(U-U)/2\subset F\cap B$; Brunn--Minkowski
implies $|U|\leq|(U-U)/2|$. Integrate the resulting intersection-volume
inequality over Gaussian level balls. A cover in (6) therefore yields

$$
\gamma(RD_m)\leq N(RD_m,tAK)\,\Gamma_t(AK).         \tag{7}
$$

The radius $r_m>\sqrt{m/(2\pi e)}$. For example,
$1=\int_{\mathbb R^m}e^{-\pi\|x\|^2}dx$ is strictly larger than the
volume of a radius-$\sqrt{m/(2\pi)}$ ball times $e^{-m/2}$, which gives
this bound after taking volume radii.
If $G$ has density $e^{-\pi\|x\|^2}$, then
$\mathbb E e^{\pi\|G\|^2/2}=2^{m/2}$. Markov's inequality gives

$$
1-\gamma(\sqrt tD_m)\leq
e^{-tm/(4e)}2^{m/2}=e^{-a(t)m}.                   \tag{8}
$$

Equations (6)--(8), together with
$1-z^m\geq(1-z)^m$ for $0<z<1$, prove (5). In particular, no
equal-volume assumption on the regular ellipsoid has been inserted.
$\square$

## 3. A fixed-parameter induction on stable Voronoi cells

Let $V(L)$ be the centered Voronoi cell of $L$. We prove

$$
\Gamma_t(V(L))\geq e^{-\epsilon(t)m}.              \tag{9}
$$

The needed lattice facts are checked in
[Regev--Stephens-Davidowitz](../../../../library/discrete_geometry/regev_stephens_davidowitz_2016_reverse_minkowski_theorem/_index.md)
(arXiv:1611.05979v6): stable lattices form a compact set and a boundary lattice
splits into proper stable sublattice and orthogonal quotient (Proposition 2.5);
the Gaussian Voronoi functional has the position gradient of Theorem 3.1;
Gaussian-isotropic bodies maximize Gaussian mass over determinant-one positions
(Proposition 4.3). These apply at every positive parameter.

Fix $t\geq T_0$. Induct on rank, choosing a stable $L$ minimizing
$\Gamma_t(V(L))$, which exists by compactness and continuity.
In rank one, $L=\mathbb Z$ up to isometry and its volume-one interval
has no other determinant-one position; (5) applies directly.

If the minimizer is also a local minimum among determinant-one lattices,
apply the gradient identity to
$f(x)=t^m e^{-\pi t^2x}$. Its derivative matrix is

$$
-2\pi t^{m+2}\int_{V(L)}
       e^{-\pi t^2\|x\|^2}xx^{\mathsf T}\,dx .
$$

Vanishing in all trace-zero directions makes this a scalar matrix.
Thus $V(L)$ is Gaussian-isotropic at parameter $1/t$, and

$$
\Gamma_t(V(L))\geq\Gamma_t(AV(L))
\quad\text{for every }A\in\mathrm{SL}_m(\mathbb R).
$$

As $|V(L)|=\det L=1$, (5) proves (9) in this case. The lattice
minimum has supplied stationarity, and body stationarity supplies a
maximum over positions; there is no reversal of the desired inequality.

Otherwise $L$ lies on the stable boundary. There is a primitive
sublattice $M$ of rank $0<h<m$ such that $M$ and $Q=L/M$, the
orthogonal quotient, are stable. Their orthogonal product Voronoi body
is a fundamental body for $L$. The nearest-point map from that body
to $V(L)$ preserves volume and decreases norm almost everywhere, so

$$
\Gamma_t(V(L))\geq\Gamma_t(V(M))\Gamma_t(V(Q)).
\tag{10}
$$

This is precisely the source's Claim 2.6 and Corollary 2.9, also displayed as
[equation (17)](https://arxiv.org/html/1611.05979v6). Induction at the **same
$t$** gives a lower bound
$e^{-\epsilon(t)h}e^{-\epsilon(t)(m-h)} =e^{-\epsilon(t)m}$. This proves (9).

Finally
$\theta_L(t)\Gamma_t(V(L))\leq1$, by the source's Lemma 4.1.
It also follows directly by integrating translated Gaussian densities
on the symmetric Voronoi cell and pairing $x$ with $-x$.
Equation (9) proves (1).

## 4. Duality and review

The dual of a stable lattice is stable. One can check this by
saturating a sublattice of $L^*$, taking its perpendicular sublattice
in $L$, and using the complementary determinant identity at $\det L=1$.
Poisson summation now gives

$$
\theta_L(u)=u^{-m}\theta_{L^*}(1/u)
           \leq u^{-m}e^{\epsilon(1/u)m},
$$

which is (2).

The primary passages, the volume normalization, covering rescaling,
Gaussian translation and tail inequalities, and the full fixed-parameter
induction are author-recorded; a separate reviewer checked each, and
another checked the moment application. These are internal reviews, not
external verification of an E0774 solution. No computation
or constant-parameter Gaussian extremality conjecture enters the proof.
