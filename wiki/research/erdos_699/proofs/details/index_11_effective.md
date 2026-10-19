---
name: research/erdos_699/proofs/details/index_11_effective
title: "Erdős 699: an effective bound at index 11"
desc: "A weighted Kummer polynomial and the maximum constraints in Bennett–Filaseta–Trifonov give a positive exponent 7/100 and an effective last row for i=11."
created: 2026-09-22T02:29:39Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: an effective bound at index 11

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/archive/other_approaches/adapted_certificates|Position-sensitive certificates]]

***

**Complete exclusion.** The [index-eleven proof](index_11_complete.md) excludes
every bad triple with $i=11$. The bounds below remain intermediate inputs.

**Numerical alternative.** The
[explicit source-threshold calculation](../../methods/details/bft_numerical_thresholds.md)
now also proves the unconditional bound $n<10^{3\,639\,160\,902}$.
The argument below keeps the original stronger cofactor exponents and
improves their algebraic term to $10^{484}$.

**There is an effectively computable last row for bad triples with $i=11$.**
The essential estimate has a positive exponent $7/100$. More precisely,
let $X$ be the maximum of the six effective constants $x_0(10)$ supplied by
Bennett–Filaseta–Trifonov, Corollary 2.3, for pairs from
$\{2,3,5,7\}$. Every bad triple with $i=11$ satisfies

$$
 n<\max\{10^{484},X+10\}.                                 \tag{1}
$$

The algebraic term $10^{484}$ is certified explicitly. The six source
constants comprising $X$ are effectively computable, but have not been
numerically evaluated here. Thus (1) is an effective bound, not a claim that
$10^{484}$ alone bounds every bad row. The sharper constant calculation
below improves the original algebraic term $10^{1525}$.

The original threshold $p\ge11$ is used throughout. In particular, 11 is
not a small prime, and its contribution to $11!$ must be retained.

## The prime-pair input

For each $p\in S=\{2,3,5,7\}$, choose
$r_p\in\{0,\ldots,10\}$ maximizing $v_p(n-r_p)$, and write

$$
 n-r_p=P_pu_p,\qquad P_p=p^{v_p(n-r_p)}.
$$

The BFT paper,
Corollary 2.3, proves that for sufficiently large, effectively bounded
$n-r_p$,

$$
 \max(u_p,u_q)>(n-r_p)^{\lambda_{pq}},
$$

because $|(n-r_p)-(n-r_q)|\le10$. The required values are

| Pair | $\lambda_{pq}$ |
| --- | --- |
| 2, 3 | 0.2921 |
| 2, 5 | 0.2679 |
| 2, 7 | 0.2757 |
| 3, 5 | 0.2238 |
| 3, 7 | 0.0505 |
| 5, 7 | 0.2667 |

Assume $n\ge\max\{20,X+10\}$ and set

$$
 e_p=\frac{\log u_p}{\log(n/2)}.
$$

Then $\max(e_p,e_q)>\lambda_{pq}$ for every pair. For each of the six
pairs, select an endpoint witnessing its inequality, and assign to each
vertex the largest edge weight assigned to it. This gives a vector
$v=(v_2,v_3,v_5,v_7)$ with $0\le v_p\le e_p$.

Enumerating the $2^6=64$ endpoint choices and removing vectors that are
componentwise larger than another leaves exactly the following eight.
The last column is an exact rational calculation used below.

| $(v_2,v_3,v_5,v_7)$, multiplied by 10000 | Minimum weighted gain |
| --- | --- |
| $(0,2921,2679,2757)$ | $15021/5000$ |
| $(2679,2921,0,2757)$ | $15021/5000$ |
| $(2757,2921,0,2667)$ | $14943/5000$ |
| $(2757,2921,2667,0)$ | $14943/5000$ |
| $(2921,0,2238,2667)$ | $23229/10000$ |
| $(2921,0,2667,505)$ | $7/100$ |
| $(2921,505,2667,0)$ | $7/100$ |
| $(2921,2238,0,2667)$ | $23229/10000$ |

Thus one of these eight vectors is componentwise at most $e$. In
particular,

$$
 P_p=\frac{n-r_p}{u_p}
 \le 2^{v_p}n^{1-v_p}.                                    \tag{2}
$$

The input is a **maximum** constraint, not merely
$e_p+e_q>\lambda_{pq}$. Replacing it by the latter loses the saving needed
here.

## The weighted polynomial

Use the polynomial from the position-sensitive construction with $k=7$:

$$
 F(X,Y)=\prod_{a=0}^6((X-a)(Y-a))^{7-a}.
$$

It has degree $D=56$, and at every Kummer point on $x+y=t\le10$ its
multiplicity is at least

$$
 m_t=14-t.
$$

Here $M=\sum m_t=99$ and $L=\sum t m_t=385$. The weighted valuation
estimate proved in the
[position-sensitive note](../../archive/other_approaches/adapted_certificates.md),
equation (7), therefore gives, for $n\ge770$,

$$
 \prod_{p\in S}P_p^{14-r_p}
 \ge\frac{2^{55}n^{43}}{(11!)^{14}}.                       \tag{3}
$$

This uses $[11!]_{\{p\ge11\}}=11$, explaining the $11!$ in the
denominator.

First suppose the four positions $r_p$ are distinct. Combine (2) and (3).
The resulting exponent of $n$ is

$$
 G(v,r)
 =43-\sum_{p\in S}(14-r_p)(1-v_p)
 =14\sum_pv_p-13+\sum_pr_p(1-v_p).                         \tag{4}
$$

Every coefficient $1-v_p$ is positive. Hence the minimum over distinct
nonnegative integer positions occurs at $\{0,1,2,3\}$. Rearrangement assigns
the largest $v_p$ to the largest position. If
$v_{(0)}\le\cdots\le v_{(3)}$ are the sorted coordinates, this minimum is

$$
 -7+\sum_{a=0}^3(14-a)v_{(a)}.                            \tag{5}
$$

The eight exact evaluations in the table show

$$
 G(v,r)\ge\frac7{100}>0                                  \tag{6}
$$

for every assignment of the four primes to distinct positions, without
enumerating the 7920 assignments individually.

As $v_p<1$ and $14-r_p\le14$, we can bound the harmless power of two in
(2) by $2^{56}$. Equations (3)--(6) yield

$$
 n^{7/100}\le 2(11!)^{14}.                                \tag{7}
$$

The exact integer comparison

$$
 10^{1525\cdot7}>\bigl(2(11!)^{14}\bigr)^{100}
$$

then excludes $n\ge10^{1525}$ once the BFT thresholds have been reached.

If the selected positions are not distinct, at most three numerator
factors contain all four selected maxima. The degree-reduction bound in
the [effectivity note](../../archive/previous_bounds/effectivity.md) gives
$U_{11}(n)\le n^3$. The existing uniform certificate has
$V_{11}(n)^{11}<n^{84}/4^{28}$, so for $n\ge110$,

$$
 n^4<\frac{(2\cdot11!)^{11}}{4^{28}}.
$$

In particular $n<10^{22}$. This also lies below the algebraic cutoff in
(1), completing the effective reduction.

The [exact checker](../../computations/erdos_699_index_11_effective.py)
verifies the finite endpoint optimization, all eight gains, and the
displayed integer comparisons. It does not enumerate rows or columns.

## Sharper constants: from $10^{1525}$ to $10^{484}$

Keep the exact contributions away from the selected maximum. Define

$$
 A_p(r)=\sum_{\substack{0\le t\le10\\t\ne r}}
              (14-t)v_p(|t-r|).
$$

The ultrametric estimate gives the following stronger version of (3):

$$
 \prod_{p\in S}P_p^{14-r_p}
 \ge
 \frac{2^{56}n^{43}\prod_{t=0}^{10}(1-t/n)^{14-t}}
 {11^{14}\prod_{p\in S}p^{A_p(r_p)}}.                    \tag{8}
$$

Here $11^{14}$ bounds the removed rough denominator, and each other
denominator factor is bounded separately at its actual selected position.
Normalize the cofactors by $n-10$ instead of $n/2$. The same eight vectors
then give

$$
 P_p\le n^{1-v_p}(1-10/n)^{-v_p}.
$$

Since $\sum(14-r_p)v_p\le56$, combining this with (8) shows

$$
 n^{G(v,r)}
 \le \frac{1000}{999}\,
 \frac{11^{14}\prod_{p\in S}p^{A_p(r_p)}}{2^{56}}
 \qquad(n\ge10^6).                                    \tag{9}
$$

Indeed, the two factors moved to the denominator have product at least
$(1-385/n)(1-560/n)>999/1000$. This follows from the elementary product
inequality and Bernoulli's inequality; the displayed numerical comparison
holds already at $n=10^6$.

There are $11\cdot10\cdot9\cdot8=7920$ assignments of distinct positions
and eight cofactor vectors. Evaluating (9) for these **63,360 proof
patterns**, with outward-rounded logarithms, gives

$$
 \log_{10}n<483.776812.
$$

The largest ratio occurs at

$$
 (r_2,r_3,r_5,r_7)=(3,0,2,1),\qquad
 v=(.2921,0,.2667,.0505),
$$

where $G=7/100$ and
$(A_2,A_3,A_5,A_7)=(41,29,7,6)$.
Thus the right side of (9) is
$\frac{1000}{999}3^{29}5^7 7^6 11^{14}/2^{15}$ in this worst pattern.
The collision bound $10^{22}$ and the starting threshold $10^6$ are both
smaller than $10^{484}$, proving (1). The
[refined checker](../../computations/erdos_699_index_11_refined_bound.py)
and its [certificate](../../computations/erdos_699_index_11_refined_bound.json)
retain every comparison needed for this bound. This calculation checks
the finitely many proof patterns, not binomial rows.

## Why the same calculation stops at index 13

For $i=13$, the graph on $\{2,3,5,7,11\}$ has 15 componentwise minimal
vectors. With the analogous polynomial $F_8$, fourteen give a positive
gain after the same rearrangement argument. The sole remaining vector is

$$
 (v_2,v_3,v_5,v_7,v_{11})
 =(0.2757,0.3453,0.2667,0,0),
$$

whose minimum gain is $-1077/2000$. Thus this calculation does not make
index 13 effective. The BFT table has no entry for the pair $(7,11)$;
after Corollary 2.3 and again in Section 8, the authors explicitly identify
that pair as one for which their construction supplies no positive bound.
The index-11 conclusion does not depend on filling that gap.
