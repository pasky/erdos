---
name: research/erdos_699/archive/other_approaches/low_rational_four
title: "Erdős 699: the four-cofactor comparison 225−224"
desc: "Rational Padé blocks give a numerical cofactor restriction for the position relation r2+r7=r3+r5, including low-index configurations missed by the separate endpoint alternatives."
created: 2026-09-22T07:10:00Z
updated: 2026-10-13T05:28:09Z
---

# Erdős 699: the four-cofactor comparison 225−224

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/rational_product_bounds|Rational product bounds]]

Let $0\le r_p\le13$ for $p\in\{2,3,5,7\}$, and write

$$
n-r_p=p^{a_p}u_p,\qquad h=n-13.
$$

Suppose

$$r_2+r_7=r_3+r_5,\qquad
\{r_2,r_7\}\ne\{r_3,r_5\},$$

where the unordered pairs include multiplicity. For
$h\ge10^{720\,587\,641}$, the following alternative holds:

$$\boxed{u_2>h^{.35}\quad\text{or}\quad
u_3>h^{.35}\quad\text{or}\quad
u_5>h^{.03}\quad\text{or}\quad
u_7>h^{.35}.} \tag{1}$$

This is a restriction on one position relation, not an effective bound
for an entire index.

## Proof and numerical data

Put $X=(n-r_3)(n-r_5)$ and $Y=(n-r_2)(n-r_7)$. The position assumptions give

$$
0<|X-Y|=|r_3r_5-r_2r_7|\le169.
$$

Apply the rational product estimate with

$$P=225=3^2 5^2,\qquad Q=224=2^5 7,\qquad P-Q=1,
\qquad c/d=5/3.$$

The exact coefficient-gcd calculation, valid for every $m\ge10^8$,
gives

$$
\log L_1=481050309501/10^{12}.
$$

Using the notation of the rational product lemma, its directed interval
evaluation gives

$$C=1.62240418258714\ldots,\qquad
K=8.05108979481149\ldots,\qquad
J=K-C=6.42868561222434\ldots.$$

For the upper cofactor box complementary to (1), choose the rational
block parameter

$$
t=18287447141/60685589176.
$$

The denominator cost $\Delta$ satisfies

$$
tC-\Delta>.08238,\qquad tK-\Delta-2>.01965.
$$

Both terms in the Padé upper bound therefore tend to zero. The explicit
threshold formula in the rational product lemma yields the displayed
power of ten, proving (1).

The [checker](../../computations/erdos_699_low_rational_four.py) and
[certificate](../../computations/erdos_699_low_rational_four.json)
retain the coefficient-gcd bound, rational block parameter, directed
margins, and threshold terms. They enumerate no binomial rows.

For example, the labeled positions
$(r_2,r_3,r_5,r_7)=(1,3,0,2)$ satisfy the required relation. The cofactor
profile $(.2757,.2921,0,.2667)$ left by the earlier separate endpoint
bounds lies strictly inside the excluded box. Other profiles remain,
so this observation alone does not settle index nine.
