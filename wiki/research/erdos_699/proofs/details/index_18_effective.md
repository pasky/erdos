---
name: research/erdos_699/proofs/details/index_18_effective
title: "Erdős 699: a complete effective cutoff certificate at index 18"
desc: "An exact check of 65 cofactor vectors and 5707 collision capacity lists gives gain 186/625. The full stopping bound includes every symmetric and asymmetric source threshold."
created: 2026-09-22T04:20:08Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: a complete effective cutoff certificate at index 18

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/weighted_ramps|Weighted certificates]] ·
[[research/erdos_699/methods/details/asymmetric_cofactors|Asymmetric cofactor bounds]]

***

**Subsequent result.** The [complete index-18 proof](index_18_complete.md)
instantiates a numerical cutoff and excludes its entire remaining interval.
There are no bad triples with $i=18$. The earlier effective reduction is
retained below.

**Every bad triple with $i=18$ lies below an effectively computable
last row.** This note supplies the complete finite arithmetic certificate
and includes the source thresholds in the final bound.

Let $X_{18}$ be the maximum of the effective bounded-gap thresholds,
with gap $D=17$, for the symmetric constraints used below. The
thresholds come from BFT Corollary 2.3 and the
[verified new prime-pair estimates](../../archive/other_approaches/more_prime_pairs.md).
Then an exclusive bound is

$$
\boxed{n<\max\{X_{18},10^{2\,405\,782}\}+17.}\tag{1}
$$

The number $X_{18}$ is effectively computable but has not been evaluated
numerically here. Thus (1) is an effective bound, not a fully numerical
bound or an assertion that the exceptional set is empty.

## Source constraints and the finite certificate

Put $S=\{2,3,5,7,11,13,17\}$. For each $p\in S$, choose
$r_p\in\{0,\ldots,17\}$ maximizing $v_p(n-r_p)$ and write

$$
n-r_p=P_pu_p,\qquad P_p=p^{v_p(n-r_p)},\qquad h=n-17.
$$

The inputs associated with any two primes differ by at most $17$.
Use every symmetric edge from BFT Corollary 2.3 and the new-pair table
whose two primes belong to $S$. Add exactly two asymmetric constraints:

$$\begin{aligned}
u_5>h^{3613/10000}&\quad\text{or}\quad u_7>h^{2277/10000},\\
u_7>h^{987/10000}&\quad\text{or}\quad u_{13}>h^{2080/10000}.
\end{aligned}\tag{2}$$

The asymmetric source checker proves (2) once all selected inputs exceed,
respectively,

$$
10^{2\,405\,782},\qquad10^{484\,367}.\tag{3}
$$

These are valid for gaps through $100$, so they apply here. At the row
level it is enough to add $17$ to each threshold in (3).

Write $z_p=\log u_p/\log h$. Each symmetric or asymmetric constraint
has the form $z_p\ge a$ or $z_q\ge b$. Choosing a witnessing endpoint
of each constraint and discarding componentwise larger vectors produces
**65 minimal vectors**. Every admissible real vector $z$ dominates one
of them: when another constraint is added, raise an endpoint that
witnesses that constraint for $z$; removing a dominated vector preserves
this property.

The [exact checker](../../computations/erdos_699_index_18_effective.py)
constructs these vectors with integer weights scaled by $10^4$. Its
[recorded output](../../computations/erdos_699_index_18_effective.json)
contains all 65 vectors, every source edge, the worst collision capacity
list, and the arithmetic constants below. It also recomputes the two
interval proofs giving (3). No binomial rows are searched.

## The polynomial and all collisions of maximal positions

Take

$$F(X,Y)=\prod_{a=0}^{11}((X-a)(Y-a))^{12-a},\qquad
D=156,\qquad m_t=24-t\quad(0\le t<18).$$

At a Kummer point $(r,s)$ with $r+s=t$, the vanishing order of $F$ is
at least $m_t$. Also $0<F(j,n-j)\le n^{156}/2^{156}$.
The weighted divisibility argument therefore gives

$$\prod_{p\in S}P_p^{m_{r_p}}
\ge\frac{2^{156}(1-1887/n)n^{123}}{C_*},\tag{4}$$

where the exact contribution away from each selected maximum is bounded by

$$\begin{aligned}
C_*&=\prod_{p\in S}p^{A_p},\\
A_p&=\max_{0\le r<18}\sum_{\substack{0\le t<18\\t\ne r}}
             (24-t)v_p(|t-r|),\\
C_*&=2^{272}3^{108}5^{57}7^{41}11^{24}13^{24}17^{24}.
\end{aligned}\tag{5}$$

Indeed $v_p(n-t)\le v_p(t-r_p)$ away from a maximal position. The
remaining constants in (4) are
$\sum m_t=279$ and $\sum t m_t=1887$.

For a minimal vector $v$ dominated by $z$, a singleton position occupied
by prime $p$ has exponent capacity $1-v_p$. A position shared by two or
more primes has capacity $1$, since the product of those prime powers
divides one integer $n-r$. For each possible subset $J$ of singleton
primes, the worst list of capacities is

$$\underbrace{1,\ldots,1}_{\lfloor(7-|J|)/2\rfloor},
\qquad (1-v_p)_{p\in J},\tag{6}$$

sorted in decreasing order; omit the impossible case $7-|J|=1$.
Rearrangement puts these capacities at positions $0,1,\ldots$ in the
worst case. These lists include arbitrary coincidences of maximal
positions, as proved in the weighted-certificate note.

The checker evaluates **5707 vector-and-capacity cases across the 65
vectors** and proves

$$
123-\sum_{r=0}^{g-1}(24-r)c_r\ge\frac{186}{625}.\tag{7}
$$

Equality occurs at

$$
v=(.3560,.3453,.2091,.2667,0,.0729,0),
$$

in prime order, with capacities

$$
(1,1,.9271,.7909,.7333,.6547,.6440).
$$

The replacement $P_p\le n^{1-v_p}(n/h)^{v_p}$ introduces a factor
at most $(n/h)^{168}$. For

$$
n\ge1000(1887+168\cdot17)=4\,743\,000,
$$

we have $(1-1887/n)(h/n)^{168}\ge999/1000$. Combining (4)--(7)
therefore gives

$$
n^{186/625}\le\frac{1000}{999}\frac{C_*}{2^{156}}.\tag{8}
$$

The checker clears the rational exponent and compares integer powers
to prove that (8) requires $n<10^{814}$.

## The full stopping bound

All parts of the argument apply when

$$n\ge\max\{10^{814},X_{18}+17,
                10^{2\,405\,782}+17,10^{484\,367}+17\}.$$

Then (8) contradicts $n\ge10^{814}$. Thus every bad row is below
that maximum, which equals the bound in (1). The large asymmetric
thresholds are essential terms in this statement; the algebraic term
$10^{814}$ alone is not a complete stopping bound.
