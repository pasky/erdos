---
name: research/erdos_699/archive/other_approaches/low_off_diagonal_ap
title: "Erdős 699: a three-cofactor alternative from 49−48"
desc: "Unequal Padé blocks at the seed 49−48 give an effective alternative for AP positions carrying the primes 2,3,7."
created: 2026-09-22T07:45:00Z
updated: 2026-10-13T05:28:09Z
---

# Erdős 699: a three-cofactor alternative from 49−48

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/off_diagonal_pade|Unequal Padé blocks]]

Fix $D\ge1$. Suppose $0\le r_2,r_3,r_7\le D$ satisfy

$$
r_2+r_3=2r_7,\qquad r_2\ne r_3,
$$

and write $n-r_p=p^{a_p}u_p$ for $p=2,3,7$. There is an effectively
computable $H(D)$ such that, for $h=n-D>H(D)$,

$$\boxed{u_2>h^{.36}\quad\text{or}\quad
u_3>h^{.19}\quad\text{or}\quad u_7>h^{.15}.} \tag{1}$$

The starting height has not been numerically evaluated. This is a
conditional cofactor estimate, not a whole-index assertion.

## Unequal blocks at the AP identity

The two products

$$
X=(n-r_7)^2,\qquad Y=(n-r_2)(n-r_3)
$$

satisfy $0<X-Y=(r_2-r_7)^2\le D^2$. Use the seed

$$
P=49=7^2,\quad Q=48=2^4\cdot3,\quad P-Q=1,
$$

with Padé directions $(A,B,C)=(49,12,20)$. Its two block lengths are
$A+B=61$ and $B+C=32$. The finite coefficient-gcd sum through $t=200$
is greater than $5.5496$. Thus the strictly smaller logarithmic gcd
rate $\ell=5$ has an effective starting index.

The directed growth calculation gives

$$
C_0>9.9872414455,\qquad K_0>285.7745674357.
$$

Set $\tau=29/4000$. For the cofactor box complementary to (1), the
denominator loss is

$$
\Delta=\bigl(122\tau\log7-2(1-.15)\bigr)_+
+\bigl(128\tau\log2-(1-.36)\bigr)_+
+\bigl(32\tau\log3-(1-.19)\bigr)_+.
$$

The retained interval calculation certifies

$$\tau C_0-\Delta>.04800,\qquad
\tau K_0-\Delta-2>.04746.$$

Choose the Padé index proportional to $\tau\log h$. The nonzero integer
from the unequal-block lemma is then bounded by two terms tending
effectively to zero, with the displayed positive powers. This is a
contradiction for effectively large $h$, proving (1).

The [integer and interval checker](../../computations/erdos_699_low_off_diagonal_ap.py)
and [certificate](../../computations/erdos_699_low_off_diagonal_ap.json)
record the exact finite gcd sum, strict gcd margin, rational block
parameter, and directed bounds. No binomial rows are enumerated.

At the labeled positions $(r_2,r_3,r_5,r_7)=(2,0,3,1)$, the required
AP is present. In particular (1) excludes the cofactor box containing
$(.355407,.174272,.463949,.141301)$ in prime order $2,3,5,7$; the
cofactor $u_5$ is unrestricted by this source.
