---
name: research/erdos_699/methods/details/weighted_ramps
title: "Erdős 699: weighted certificates make index 21 effective"
desc: "Position-sensitive polynomial bounds, with all coincidences of small-prime maxima covered, make index 21 effective and sharply reduce several earlier stopping bounds."
created: 2026-09-22T03:36:52Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: weighted certificates make index 21 effective

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/archive/previous_bounds/small_index_effective|Small-index bounds]]

***

**Completed follow-up.** The
[cutoff-21 proof](../../archive/previous_bounds/cutoff_21.md) completely
excludes index $21$ and every numerically bounded case in this note. The
weighted inequalities below supply their analytic tails.

**Index 21 has an effective last row.** A weighted polynomial gives a
positive exponent even though the unweighted small-prime estimate misses
the required exponent. The same construction substantially reduces the
algebraic terms in several existing stopping bounds. Coinciding maximal
positions of different small primes are included in the proof.

The exact [checker](../../computations/erdos_699_weighted_ramps.py) and
[recorded output](../../computations/erdos_699_weighted_ramps.json)
contain the exponent optimizations and integer comparisons. They enumerate
finite sets of exponent vectors and subsets of small primes, not binomial
rows or columns.

## 1. Weighted divisibility

Let $S_i=\{p:p<i\}$, $s=|S_i|$, and choose a position
$r_p\in\{0,\ldots,i-1\}$ maximizing $v_p(n-r_p)$. Write

$$
 P_p=p^{v_p(n-r_p)},\qquad u_p=(n-r_p)/P_p,
 \qquad h=n-i+1.
$$

For an integer $k\le i$ with $2k\ge i-1$, put

$$
 F_k(X,Y)=\prod_{a=0}^{k-1}((X-a)(Y-a))^{k-a},\quad
 D=k(k+1),\quad m_t=2k-t,
$$

and $M=\sum_{t=0}^{i-1}m_t$, $L=\sum_{t=0}^{i-1}t m_t$.
The [position-sensitive construction](../../archive/other_approaches/adapted_certificates.md)
proves the required vanishing at the Kummer points, and
$0<F_k(j,n-j)\le n^D/2^D$ on every admissible pair.

Here we retain the exact constants away from the selected maxima. Define

$$
 A_p=\max_{0\le r<i}\sum_{\substack{0\le t<i\\t\ne r}}
            m_t v_p(|t-r|),\qquad C_* =\prod_{p<i}p^{A_p},
 \qquad
 H=\begin{cases}i&i\text{ prime},\\1&i\text{ composite}.\end{cases}
$$

The maximality of $r_p$ implies
$v_p(n-t)\le v_p(t-r_p)$ for $t\ne r_p$. Also
$\prod_t(n-t)^{m_t}\ge n^M(1-L/n)$. Thus badness gives

$$
 \prod_{p<i}P_p^{m_{r_p}}
 \ge\frac{2^D(1-L/n)n^{M-D}}{H^{2k}C_*}.                  \tag{1}
$$

The factor $H^{2k}$ covers the rough prime in $i!$ at prime indices.
Formula (1) is valid whether or not the selected positions coincide.

## 2. All position assignments, including coincidences

The source estimates supply maximum constraints

$$
 \max\left\{\frac{\log u_p}{\log h},
             \frac{\log u_q}{\log h}\right\}\ge\lambda_{pq}.
$$

Select a witnessing endpoint of each constraint. At a vertex, take the
largest weight assigned to it. Removing componentwise dominated vectors
leaves a finite list of $v=(v_p)$, one of which satisfies

$$
 u_p\ge h^{v_p},\qquad
 P_p\le n^{1-v_p}(n/h)^{v_p}.                              \tag{2}
$$

Every vector used here has $0\le v_p<1/2$.

Group the primes having the same selected position. A singleton group
$\{p\}$ has exponent capacity $c=1-v_p$. A group with at least two
primes has capacity $c=1$, because the product of its distinct prime
powers divides the single integer $n-r$ and is at most $n$. Applying (2)
only at singleton groups therefore gives an upper bound for the left
side of (1) of the form

$$
 n^{\sum_r(2k-r)c_r}(n/h)^B,\qquad 0\le B\le2ks.           \tag{3}
$$

For fixed capacities, their largest possible weighted sum occurs at the
positions $0,1,\ldots,g-1$, with the capacities in decreasing order. This
is just rearrangement, since every capacity is positive and the weights
$2k-r$ decrease with $r$.

It remains to cover all ways of forming groups. Choose the subset $J$ of
primes at singleton positions. If $b=s-|J|$ primes remain, then $b\ne1$;
when $b\ge2$, there are at most $\lfloor b/2\rfloor$ other occupied
positions. Each has capacity one. The worst possibility has exactly that
many: inserting another capacity one at the start increases the weighted
sum by at least $2k-g\ge0$. Hence it suffices to consider the finite
capacity list

$$
 \underbrace{1,\ldots,1}_{\lfloor(s-|J|)/2\rfloor},
 \quad (1-v_p)_{p\in J},                                  \tag{4}
$$

sorted in decreasing order. This covers arbitrary collisions using only
$2^s$ subsets, rather than enumerating positions or set partitions.

Let $c_0\ge\cdots\ge c_{g-1}$ denote a list (4). The gain to check is

$$
 G(v,J)=M-D-\sum_{r=0}^{g-1}(2k-r)c_r.                     \tag{5}
$$

If every gain is at least $\eta>0$, combine (1)--(3). For

$$
 n\ge N:=1000\bigl(L+2ks(i-1)\bigr),
$$

the elementary product inequality gives

$$
 (1-L/n)(1-(i-1)/n)^{2ks}\ge999/1000.
$$

Consequently every bad row above the source thresholds satisfies

$$
 \boxed{\displaystyle
 n^\eta\le\frac{1000}{999}\,\frac{H^{2k}C_*}{2^D}.}        \tag{6}
$$

All quantities on the right are explicit rational numbers.

## 3. The new index and smaller algebraic bounds

For index 21, take $k=14$ and the published BFT Corollary 2.3 table,
augmented by

$$
 (2,17):\ .3560,\qquad (17,19):\ .2176.
$$

Both additional exponents are certified applications of BFT Theorem 2.2;
see the [new prime-pair estimates](../../archive/other_approaches/more_prime_pairs.md).
The finite calculation above has minimum gain

$$
 \eta_{21}=\frac{7683}{5000}>0.
$$

Its worst case has all eight positions distinct, and the cofactor vector
in prime order $2,3,5,7,11,13,17,19$ is

$$
 (.3560,.3453,.2667,0,0,.1243,0,.2176).
$$

Equation (6) supplies the algebraic term $10^{232}$. Hence

$$
 n<\max\{10^{232},X_{21}+20\},                             \tag{7}
$$

where $X_{21}$ is the maximum of the finitely many effective source
thresholds for these pairs. This proves effectivity independently of
evaluating those thresholds numerically.

For comparison, retaining the same sources as the previous effective
bounds gives:

| $i$ | $k$ | Minimum gain | Algebraic term in the stopping bound |
| --- | --- | --- | --- |
| 16 | 11 | $693/500$ | $10^{127}$ |
| 19 | 13 | $711/500$ | $10^{222}$ |
| 22 | 15 | $729/500$ | $10^{275}$ |
| 25 | 17 | $747/500$ | $10^{370}$ |
| 24 | 16 | $21893/10000$ | $10^{228}$ |

The first four use only the published Corollary 2.3 table. The last uses
that table and the already established pairs $(17,19):.21$ and
$(11,23):.145$. These improved algebraic terms do not discard the source
thresholds: the complete bounds remain their maxima with the applicable
source threshold and its row shift.

## 4. Fully numerical versions

Smaller, explicitly certified prime-pair exponents can give stronger
complete bounds because their source thresholds are much smaller. The
[numerical source calculations](bft_numerical_thresholds.md)
and [explicit new pairs](../../archive/other_approaches/more_prime_pairs.md) supply
the required thresholds. With the original, fully explicit BFT Theorem
2.1 table as the starting point, the following choices give:

| $i$ | Added pairs and exponents | $k$ | Gain | Algebraic term | Complete bound |
| --- | --- | --- | --- | --- | --- |
| 16 | $(2,7):.27307$, $(5,7):.23237$ | 10 | $.01841$ | $10^{8560}$ | $n<10^{163\,785}$ |
| 19 | $(2,17):.3259$ | 12 | $.7121$ | $10^{406}$ | $n<10^{976}$ |
| 22 | $(17,19):.1855$ | 15 | $3.927$ | $10^{102}$ | $n<10^{957}$ |
| 25 | $(17,19):.1855$ | 17 | $4.2225$ | $10^{131}$ | $n<10^{957}$ |
| 24 | $(2,17):.3259$, $(17,19):.1855$, $(11,23):.1068$ | 16 | $.7864$ | $10^{635}$ | $n<10^{976}$ |

At indices 19, 22, 24, and 25, the source checker verifies the row shifts
up to 33 directly, so no extra power of ten is required. At index 16, the
source threshold is below $10^{163\,784}$ and the displayed extra power
of ten absorbs the row shift.

At index 21, use the numerical refinements of the old table, including
$(5,7):.2587$, $(7,13):.1184$, and $(3,11):.3432$, together with
$(2,17):.3379$ and $(17,19):.1925$. The same $F_{14}$ calculation has gain
$1711/10000$ and algebraic term $10^{2075}$. Every source threshold is
below $10^{45\,411\,830}$, so allowing the row shift gives the fully
numerical bound

$$
 \boxed{n<10^{45\,411\,831}\qquad(i=21).}                  \tag{8}
$$

These are stopping bounds. No search through all rows below them is
claimed in this note.
