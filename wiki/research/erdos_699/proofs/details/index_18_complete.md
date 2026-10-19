---
name: research/erdos_699/proofs/details/index_18_complete
title: "Erdős 699: no exceptions at index 18"
desc: "A numerical interpolation bound and a completed finite prime-pair and interval certificate exclude every admissible bad triple with i=18."
created: 2026-09-22T05:04:00Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: no exceptions at index 18

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/proofs/details/index_18_effective|Earlier effective reduction]]

***

**Theorem.** For every $18<j\le n/2$, some prime $p\ge18$ divides both
$\binom n{18}$ and $\binom nj$. Thus there are no bad triples with
$i=18$, with the original non-strict prime threshold.

The proof is computer-assisted. First, an interpolation certificate puts
every possible bad row below $10^{700000}$, with all constants numerical.
A finite prime-pair certificate then reduces the interval to $n\le10^{37}$.
The completed interval calculation excludes every remaining row.

## 1. A completely numerical last row

For each $p\in\{2,3,5,7,11,13,17\}$, choose $r_p\in\{0,\ldots,17\}$
maximizing $v_p(n-r_p)$ and write $n-r_p=P_pu_p$, with $P_p$ a power
of $p$. The selected inputs differ by at most $17$.

The source constraints are the original BFT Theorem 2.1 table and
17 asymmetric estimates from the
[asymmetric cofactor lemma](../../methods/details/asymmetric_cofactors.md).
Every latter estimate uses a published BFT Proposition 5.1 coefficient-gcd
bound. The [source checker](../../computations/erdos_699_index_18_pair_sources.py)
recomputes their thresholds with directed intervals from the
[fixed parameters](../../computations/erdos_699_index_18_pair_parameters.json).
Its [output](../../computations/erdos_699_index_18_pair_sources.json)
proves that all source constraints apply to the selected inputs once
$n\ge10^{1733}$. There is no unevaluated source constant.

Use the following line-factor and row multiplicities:

$$\begin{aligned}
h={}&(37,34,32,29,26,23,19,15,10,4,0,0,0,0,0,0,0,0),\\
m={}&(71,71,71,71,69,66,66,66,63,58,53,49,44,41,38,36,34,31).
\end{aligned}$$

Put

$$H(X,Y)=\prod_{a=0}^{17}((X-a)(Y-a))^{h_a},\qquad
R_{xy}=\max\{0,m_{x+y}-h_x-h_y\}.$$

The degree-$130$ symmetric interpolation system for the residual
multiplicities $R_{xy}$ has **4355 equations and 4356 monomials**.
The [rank checker](../../computations/erdos_699_index_18_interpolation_rank.py)
reconstructs its integer Hasse-jet matrix and proves rank $4355$ modulo
the prime $65521$; its
[certificate](../../computations/erdos_699_index_18_interpolation_rank.json)
records the fixed system.

Thus the rational interpolation map is surjective. The
[nonvanishing lemma](../../methods/details/jet_nonvanishing.md), using
multiplication by $X+Y$, supplies a finite family of integer polynomials
of degree at most $131$ with these residual multiplicities and no common
zero when $X+Y>17$. Multiplying by $H$ gives polynomials of degree at
most $589$ with the required row multiplicities, one of which is nonzero
at each physical pair $18<j\le n-j$.

As in the weighted-ramp argument, the cofactor constraints yield finitely
many minimal exponent vectors. The
[whole numerical checker](../../computations/erdos_699_index_18_numerical.py)
checks all **123 minimal vectors and 11,932 collision-capacity cases**.
Since $m$ is nonincreasing, rearrangement covers every assignment of the
maximal positions, including coincidences. The exact minimum gain is

$$\sum_t m_t-589-\sum_t m_tc_t
\ge\frac{5241}{5000}=1.0482.$$

The worst vector, in prime order, is
$$
(.3472,.3290,.1990,.2270,0,.0370,0),
$$
with capacities
$$
(1,1,.9630,.8010,.7730,.6710,.6528).
$$

To make the coefficient bound numerical, set

$$
r=4355,\qquad C=r!(2\cdot18^{130})^r.
$$

Maximal minors and their cofactors give denominator-cleared interpolation
sections with coefficients bounded by $C$. The elementary integer
comparisons

$$
r<10^4,\qquad2^{500}<10^{151},\qquad18^{500}<10^{628}
$$

give $C<10^{730000}$. The factor converting this coefficient bound to
the norms of the nonvanishing generators is $1\,668\,679<10^7$.
Also

$$\|H\|_1\le18^{458}<10^{576},\quad
(17!)^{71}<10^{1065},\quad2^{1+7\cdot71}<10^{151}.$$

The weighted divisibility estimate consequently gives, beyond the source
and elementary thresholds,

$$
n^{5241/5000}<10^{731800}.
$$

But $(10^{700000})^{5241/5000}=10^{733740}$.
Every source and elementary threshold is smaller than $10^{700000}$,
so the [recorded numerical certificate](../../computations/erdos_699_index_18_numerical.json)
proves the exclusive bound

$$
\boxed{n<10^{700000}.}\tag{1}
$$

## 2. A stronger bound on this finite interval

The [prime-pair strip checker](../../computations/erdos_699_prime_pair_strips.py)
certifies all 15 pairs among $2,3,5,7,11,13$, for gaps at most $19$ and
input heights through $10^{1200000}$. Its
[complete certificate](../../computations/erdos_699_prime_pair_strips_k6.json)
lists every exception to

$$
\max(u,v)^3\ge\min(p^a u,q^b v).\tag{2}
$$

The prime-power ranges are covered by finitely many divisor strips;
the certificate applies to all inputs in the stated height range.
At row $n\ge73\,516\,023$, every selected input lies above every
exception threshold. Bound (1) ensures that all selected inputs also
lie below the upper height limit of the pair certificate.

For $h=n-17$, equation (2) implies that at least five of the six
cofactors are at least $h^{1/3}$. Otherwise a pair of smaller cofactors
would violate (2). The checker uses the slightly weaker rational
exponent $.3333$ per selected cofactor, giving the uniform saving

$$
\gamma=5\cdot.3333=1.6665.
$$

Hence throughout the remaining bounded range,

$$
U_{18}(n)\le\frac{n^7}{18(n-17)^{1.6665}}.
$$

Combining this with the retained fat-point and symmetric discriminant
lower bounds reduces every possible bad row to $n\le10^{37}$.
The [interval checker](../../computations/erdos_699_further_intervals.py)
certifies the reduction using outward-rounded logarithms and includes
the source threshold in the upper cap.

## 3. The completed interval exclusion

The retained prime-gap data and terminal-prime lemma exclude $n<887$.
The interval checker covers every integer in $[887,10^{37}]$ by
**247,058 certified intervals**. On each interval the Kummer valuation
upper bounds, augmented where applicable by the local prime-pair
constraints, contradict the lower bound required by badness.

The [completed output](../../computations/erdos_699_further_intervals_18.json)
records 494,115 visited intervals and minimum certified logarithmic margin

$$
0.000028331945486687112311862842845207351396481308461874457>0.
$$

It records the partition hash and, as its own run record, the names of
the finite prime-pair certificate and the prime-gap data. No residual
singleton or separate column
verification was needed. Thus the entire remaining interval is excluded,
proving the theorem.
