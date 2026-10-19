---
name: research/erdos_699/remaining/details/five_curve_obstruction
title: "Erdős 699: a curve obstruction for one remaining index-five profile"
desc: "An exact nine-line covering proves that adding arbitrary fixed plane-curve factors cannot bring the residual quadratic cost below one at cofactor exponents .13 and .34 in positions zero and one."
created: 2026-09-22T08:42:56Z
updated: 2026-10-13T05:28:09Z
---

# Erdős 699: a curve obstruction for one remaining index-five profile

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/weighted_ramps|Weighted polynomial certificates]]

***

At index five, consider selected small-prime positions $0,1$ and
cofactor exponents $e_0=13/100$, $e_1=17/50$. The row capacities are

$$
\alpha=(13/100,17/50,1,1,1).
$$

The current construction combines fixed curve factors with a residual
polynomial obtained by counting linear conditions. For this profile,
adding more fixed plane curves cannot lower the normalized residual
quadratic cost below

$$
\boxed{\frac{310000}{270691}=1.14521724032\ldots>1.}\tag{1}
$$

This is an exact statement in every degree, proved by nine lines. It
explains why searches for additional conics, cubics, or higher curves
cannot complete this particular construction. It does not exclude this
arithmetic profile from bad triples, and it does not obstruct stronger
cofactor estimates, additional column congruences, or estimates using
the particular value of a polynomial at a column.

## Exact point weights

Let $S=\{(a,b)\in\mathbf Z_{\ge0}^2:a+b\le4\}$. Assign symmetric
weights $w_{a,b}=w_{b,a}$ using the following numerators, all divided by
$3100$.

| Point | Numerator |
| --- | ---: |
| $(0,0)$ | 403 |
| $(0,1)$ | 527 |
| $(0,2)$ | 1031 |
| $(0,3)$ | 676 |
| $(0,4)$ | 463 |
| $(1,1)$ | 1038 |
| $(1,2)$ | 874 |
| $(1,3)$ | 661 |
| $(2,2)$ | 852 |

Direct addition gives

$$\sum_{a+b=r}w_{a,b}=\alpha_r,\qquad
\sum_{P\in S}w_P^2=\frac{270691}{310000}<1.\tag{2}$$

These weights obey, for every nonzero polynomial $F\in\mathbf C[X,Y]$,

$$
\boxed{\sum_{P\in S}w_P\operatorname{ord}_P F\le\deg F.}\tag{3}
$$

In particular, a polynomial having multiplicity at least $m_r$ at
every point of row $r$ necessarily satisfies

$$
\deg F\ge\frac{13}{100}m_0+rac{17}{50}m_1+m_2+m_3+m_4.\tag{4}
$$

Thus a strict comparison of weighted row multiplicities against total
degree cannot succeed at this profile. This statement concerns that
specific exponent comparison; equality cases and stronger arithmetic
information are not addressed by it.

## A nine-line proof

Give the following lines the indicated positive coefficients, now with
common denominator $15500$.

| Lines | Numerator for each line |
| --- | ---: |
| $X=0$, $Y=0$ | 1376 |
| $X=1$, $Y=1$ | 1259 |
| $X=2$, $Y=2$ | 1107 |
| $X+Y=2$ | 2672 |
| $X+Y=3$ | 2004 |
| $X+Y=4$ | 2046 |

Write these coefficients as $\lambda_L$. At every $P\in S$,

$$w_P\le\sum_{L\ni P}\lambda_L,\qquad
\sum_L\lambda_L=\frac{7103}{7750}<1.\tag{5}$$

The only strict pointwise excesses are $737/15500$ at $(0,0)$ and
$1107/15500$ at each of $(0,4),(4,0)$.

If an irreducible curve $C$ is different from these nine lines,
Bézout's theorem gives

$$
\sum_{P\in S\cap L}\operatorname{mult}_P C\le\deg C
$$

for each line $L$: the local intersection multiplicity with a line is
at least the curve multiplicity, and the total projective intersection
number is $\deg C$. Therefore

$$\sum_{P\in S}w_P\operatorname{mult}_P C
\le\frac{7103}{7750}\deg C<\deg C.\tag{6}$$

Each of the nine lines itself has weighted incidence at most one.
Seven have incidence exactly one; $X=2$ and $Y=2$ each have incidence
$2757/3100$. Factoring a nonzero polynomial into irreducible factors
now proves (3), since multiplicities and degrees are additive.

## Consequence for every collection of fixed curve factors

Let $C_\ell$ be arbitrary curves, with degrees $d_\ell$ and point
multiplicities $\nu_{\ell,P}$. Suppose nonnegative real factor weights
$t_\ell$, row multiplicities $m_r$, and residual point multiplicities
$z_P$ satisfy

$$m_{a+b}\le z_{(a,b)}+\sum_\ell t_\ell\nu_{\ell,(a,b)}
\quad((a,b)\in S).$$

Their gain before constructing the residual polynomial is

$$
G=\sum_r\alpha_r m_r-\sum_\ell t_\ell d_\ell.
$$

Multiplication by the point weights, followed by (2) and (3), gives

$$G\le\sum_P w_Pz_P.
$$

For the normalization $G\ge1$, Cauchy's inequality therefore forces

$$1\le\left(\sum_Pw_P^2\right)\left(\sum_Pz_P^2\right),\qquad
\sum_Pz_P^2\ge\frac{310000}{270691}.$$

This proves (1) for every finite collection of curve factors, with no
degree restriction and no positivity restriction on the curves. The
usual residual dimension count needs a quadratic cost strictly below
one, so no enlargement of the fixed-curve catalog can meet that
criterion at these capacities.

The lower bound is attained using just the factors $X,Y,X-1,Y-1$.
Put $q=310000/270691$, take row multiplicities

$$
\frac q{3100}(1181,1107,1420,1065,852),
$$

and give $X,Y$ factor multiplicity $389q/3100$ each and $X-1,Y-1$
factor multiplicity $191q/3100$ each. The resulting residual at $P$
is exactly $q w_P$, the gain is exactly one, and its quadratic cost is
exactly $q$. Thus (1) is the minimum, not just a lower bound.

The [integer/rational checker](../../computations/erdos_699_five_curve_obstruction.py)
and its [output](../../computations/erdos_699_five_curve_obstruction.json)
verify the weights, line covering, incidence bounds, row sums, and exact
quadratic cost. Their proof input is the elementary Bézout argument
above; no optimization solver or finite degree search is needed.
