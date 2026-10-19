---
name: research/erdos_940/affine_fiber_brauer
title: Constant Brauer groups on higher-degree affine fibers
desc: For r at least five, the full nonzero affine diagonal fiber has only constant Brauer classes; no height-sensitive obstruction was obtained.
tags: []
sources: []
created: 2026-09-23T01:47:49Z
updated: 2026-09-23T01:47:49Z
---


# Constant Brauer groups on higher-degree affine fibers

***

## Status and scope

The proposition below is proved, with the relevant passages in the
supplied sources checked after their digests. It rules out an ordinary
Brauer--Manin obstruction on each **full affine** fixed-core fiber as a
new mechanism for higher-exponent gaps. It is not a local-global
principle and supplies no rational or integral point.

## The calculation

**Proposition.** Let $r\ge5$, $d_1,\ldots,d_r,n\in\mathbb Q^\times$,
and

$$
U:\quad \sum_{i=1}^r d_i x_i^r=n.
$$

The natural map $\operatorname{Br}(\mathbb Q)\to
\operatorname{Br}(U)$ is an isomorphism.

**Proof.** Compactify to

$$
X:\quad \sum_i d_i X_i^r=nZ^r\subset\mathbb P^r,\qquad
D=X\cap\{Z=0\}.
$$

Since all displayed coefficients are nonzero and the characteristic is
zero, $X$ and $D$ are geometrically smooth hypersurfaces. Their dimensions
are respectively $r-1\ge4$ and $r-2\ge3$; in particular they are
geometrically integral.

Write bars for base extension to $\overline{\mathbb Q}$.
[Colliot-Thélène--Skorobogatov, Corollary 4.4.5 and its
proof](../../../library/number_theory/colliot_thelene_skorobogatov_2021_comparing_two_brauer_groups_ii/_index.md)
give

$$
\operatorname{Br}(\bar X)=0,\qquad
\operatorname{Pic}(\bar X)=\mathbb Z[H],\qquad
\operatorname{Pic}(\bar D)=\mathbb Z.
$$

The Picard assertion uses the restriction isomorphism for smooth
complete intersections of dimension at least three stated in that
proof.

For each $m\ge1$, the Kummer sequence on $\bar D$ gives
$H^1_{\mathrm{\acute et}}(\bar D,\mu_m)=0$: its global units are the
divisible group $\overline{\mathbb Q}^{\times}$ and its Picard group
has no torsion. Identifying $\mu_m$ with the constant group
$\mathbb Z/m$ over the algebraic closure and taking direct limits gives
$H^1_{\mathrm{\acute et}}(\bar D,\mathbb Q_\ell/\mathbb Z_\ell)=0$
for every prime $\ell$.

Apply
[the purity sequence, Theorem 3.7.1](../../../library/number_theory/colliot_thelene_skorobogatov_2021_brauer_groups_schemes/_index.md)
to $\bar U=\bar X\setminus\bar D$. It gives

$$
0\longrightarrow\operatorname{Br}(\bar X)\{\ell\}
\longrightarrow\operatorname{Br}(\bar U)\{\ell\}
\longrightarrow H^1(\bar D,\mathbb Q_\ell/\mathbb Z_\ell).
$$

Both outside groups vanish. The Brauer group of a smooth integral
variety is torsion (also recorded in the supplied chapter), so
$\operatorname{Br}(\bar U)=0$.

Since $D\sim H$, divisor localization gives

$$
\operatorname{Pic}(\bar U)
=\operatorname{Pic}(\bar X)/\mathbb Z[D]=0.
$$

Also $\bar U$ has only constant units: the divisor on $\bar X$ of
such a unit must be $k\bar D$. Its class is $kH$, which is zero
only for $k=0$. The resulting rational function has no zeros or poles
on the projective variety $\bar X$ and hence is constant.

We can therefore apply
[Proposition 4.3.2, sequence (4.9)](../../../library/number_theory/colliot_thelene_skorobogatov_2021_comparing_two_brauer_groups_ii/_index.md)
to $U$. With $\operatorname{Pic}(\bar U)=0$ it identifies
$\operatorname{Br}(\mathbb Q)$ with $\operatorname{Br}_1(U)$. The vanishing of
$\operatorname{Br}(\bar U)$ makes $\operatorname{Br}_1(U)=\operatorname{Br}(U)$,
proving the claim. $\square$

## What this rules out, and what it does not

Constant Brauer classes evaluate independently of the chosen local point,
and their local invariants sum to zero by reciprocity. Thus an existing
adelic collection of local points on $U$ cannot be excluded by its
ordinary Brauer--Manin pairing. The same applies after requiring
integrality at the relevant places or positivity at the real place:
constant evaluations do not detect those choices.

This does not assert that every locally soluble fiber has an integral
point, let alone a positive point with roots of size $O(n^{1/r})$.
It also does not apply to arbitrary smaller open subsets obtained by
removing additional divisors. The attempted coordinate and binary-subsum
punctures yielded no new bound over the remaining root variables.
Consequently no target exclusion, void inequality, or counting estimate
was deduced.

The proposition concerns $n\ne0$, all coefficients nonzero, and $r\ge5$.
No assertion about singular zero fibers or lower-degree affine fibers
is made here. The infinite canonical-core family still requires its
separate tail estimates.
