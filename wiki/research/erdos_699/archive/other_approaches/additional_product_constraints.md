---
name: research/erdos_699/archive/other_approaches/additional_product_constraints
title: "Erdős 699: further product constraints for selected small-prime positions"
desc: "Eleven AP, five equal-sum, and one cubic product estimate give certified cofactor restrictions. They do not by themselves settle index 12."
created: 2026-09-22T05:25:42Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: further product constraints for selected small-prime positions

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/ap_cofactors|Quadratic constant-gap identities]] ·
[[research/erdos_699/methods/details/asymmetric_cofactors|Asymmetric cofactor bounds]]

The quadratic-product argument gives additional useful cofactor
restrictions involving $2,3,5,7,11$. This note records eleven AP
estimates, five estimates for two pairs of positions with equal sums,
and one cubic product estimate.
The underlying inequalities are proved; combining them into a complete
index-12 argument remains separate work.

Write

$$
n-r_p=p^{a_p}u_p,\qquad0\le r_p\le11,\qquad h=n-11.
$$

In each table below, the listed targets mean that at least one of the
inequalities $u_p>h^{\gamma_p}$ holds beyond the corresponding numerical
threshold. The other primes impose no condition in that row.

## Arithmetic-progression positions

These rows apply when the indicated middle prime occupies the middle
of three **distinct** AP positions. The endpoint primes may occur in
either order.

| Middle prime | Endpoint primes | Certified targets |
| --- | --- | --- |
| $2$ | $3,11$ | $\gamma_2=.394,\ \gamma_3=.615,\ \gamma_{11}=.161$ |
| $3$ | $2,11$ | $\gamma_2=.857,\ \gamma_3=.433,\ \gamma_{11}=.011$ |
| $11$ | $2,5$ | $\gamma_2=.330,\ \gamma_5=.481,\ \gamma_{11}=.228$ |
| $11$ | $2,7$ | $\gamma_2=.312,\ \gamma_7=.035,\ \gamma_{11}=.207$ |
| $3$ | $5,11$ | $\gamma_3=.396,\ \gamma_5=.410,\ \gamma_{11}=.121$ |
| $11$ | $3,7$ | $\gamma_3=.442,\ \gamma_7=.012,\ \gamma_{11}=.087$ |
| $2$ | $3,7$ | $\gamma_2=.410,\ \gamma_3=.376,\ \gamma_7=.448$ |
| $3$ | $2,7$ | $\gamma_2=.485,\ \gamma_3=.388,\ \gamma_7=.277$ |
| $7$ | $2,3$ | $\gamma_2=.296,\ \gamma_3=.442,\ \gamma_7=.013$ |
| $7$ | $2,5$ | $\gamma_2=.429,\ \gamma_5=.469,\ \gamma_7=.359$ |
| $3$ | $5,7$ | $\gamma_3=.358,\ \gamma_5=.624,\ \gamma_7=.091$ |

For example, the middle-$2$ row on $2,3,7$ uses
$64-63=1$, with middle base $2^6$ and endpoint base $3^2\cdot7$.
The middle-$7$ row on $2,5,7$ uses
$2401-3\cdot800=1$, with bases $7^4$ and $2^5\cdot5^2$.
The three-way alternative in the AP note explains why each endpoint
prime contributes twice its seed logarithm, while the middle contributes
once.

## Equal sums of two pairs of positions

These rows require four distinct selected positions and the stated
equality of their sums.

| Position relation | Seed | Certified targets |
| --- | --- | --- |
| $r_2+r_{11}=r_3+r_7$ | $22-21=1$ | $\gamma_2=.718,\ \gamma_3=.554,\ \gamma_7=.210,\ \gamma_{11}=.027$ |
| $r_2+r_7=r_5+r_{11}$ | $56-55=1$ | $\gamma_2=.385,\ \gamma_5=.524,\ \gamma_7=.424,\ \gamma_{11}=.290$ |
| $r_2+r_3=r_5+r_{11}$ | $3025-7\cdot432=1$ | $\gamma_2=.4949,\ \gamma_3=.3996,\ \gamma_5=.4136,\ \gamma_{11}=.1264$ |
| $r_2+r_7=r_3+r_{11}$ | $99-98=1$ | $\gamma_2=.824,\ \gamma_3=.442,\ \gamma_7=.012,\ \gamma_{11}=.391$ |
| $r_3+r_{11}=r_5+r_7$ | $3\cdot3267-8\cdot1225=1$ | $\gamma_3=.3930,\ \gamma_5=.4072,\ \gamma_7=.2833,\ \gamma_{11}=.1169$ |

The seed decompositions are

$$\begin{gathered}
22=2\cdot11,\quad21=3\cdot7,\quad
56=2^3\cdot7,\quad55=5\cdot11,\\
3025=5^2\cdot11^2,\quad432=2^4\cdot3^3,\quad
99=3^2\cdot11,\quad98=2\cdot7^2,\\
3267=3^3\cdot11^2,\qquad1225=5^2\cdot7^2.
\end{gathered}$$

As in the earlier four-factor lemma, equality of the position sums
makes the difference of the corresponding quadratic products constant.
Distinctness of the four positions makes this constant nonzero.

## A cubic constant-gap identity

There is also the exact identity

$$
Z(Z-3d)^2-(Z-d)^2(Z-4d)=4d^3.
$$

Suppose the selected positions of primes $11,7,3,2$, in that order,
are $a,a+d,a+3d,a+4d$, with integer $d\ne0$. The two products above
then have degree three, with factor multiplicities $(1,2)$ and $(2,1)$.
Use the seed $99-98=1$, where $99=3^2\cdot11$ and $98=2\cdot7^2$,
and the Padé parameter $s=5/4$.

Matching all four prime-power blocks gives limiting cofactor exponents

$$
1-\frac{3b_p\log p}{w_pK},
$$

where $b_p$ is the prime exponent in the seed and $w_p$ is its factor
multiplicity. This follows from the same determinant inequality as the
quadratic argument: the two original products now have size at most
$n^3$, so its degree factor is three.
The checker proves the additional alternative

$$u_2>h^{.736}\quad\text{or}\quad
u_3>h^{.5818}\quad\text{or}\quad
u_7>h^{.2593}\quad\text{or}\quad
u_{11}>h^{.0873}.$$

The position hypothesis allows either sign of $d$. The product gap is
nonzero and at most $4\cdot11^3$, which is the bound used in the
threshold calculation.

## Certificates and thresholds

The [checker](../../computations/erdos_699_additional_product_cofactors.py)
evaluates every fixed parameter choice with the retained explicit
coefficient-gcd estimate, using $m_0=10^8$ and 4000 prime intervals.
It verifies $\Omega_3,\Omega_4>1$ and a margin of $10^{-4}$ between
each target and its limiting exponent. The Padé parameters and all
interval values are in the
[recorded certificate](../../computations/erdos_699_additional_product_cofactors.json).

It also applies the general numerical product-threshold formula with
maximum position $11$. The quadratic rows use degree $2$ and product
gap $121$; the cubic row uses degree $3$ and product gap $4\cdot11^3$.
Consequently every table entry holds uniformly, under its position
condition, whenever

$$
h\ge10^{9\,897\,968\,998}.
$$

This is a convenient common threshold, not an optimized one. Individual
thresholds are retained in the certificate. The calculation verifies
fixed analytic parameters and does not enumerate binomial rows.

The position conditions are essential. In particular, these estimates
must not be applied to arbitrary assignments of the selected maxima
without checking the AP or equal-sum relation.
