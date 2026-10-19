---
name: research/erdos_1145/collision_density
desc: Finite-bin difference counting forces a quantitative collision density.
tags: [proved, reductions]
sources: []
created: 2026-09-22T18:25:06Z
updated: 2026-09-24T22:12:57Z
---


# research/erdos_1145/collision_density

***

Suppose the hypotheses of Problem 1145 hold and $1\le r(n)\le M$
eventually. Then repeated sums have positive lower density. The following
explicit constants are crude but make the conclusion quantitative.

By [counting regularity](counting_regularity.md),

$$
A(x)-B(x)=o(\sqrt x),\qquad
(1-o(1))\sqrt x\le A(x),B(x)\le(\sqrt{2M}+o(1))\sqrt x.
\tag{1}
$$

Set $L=128M$. Partition each of the three annuli
$(L^jx,L^{j+1}x]$, $j=0,1,2$, into intervals $I$ of length $x$,
for integer $x$. Write $\alpha_I=|A\cap I|$, $\beta_I=|B\cap I|$.
There are only finitely many bins, with number independent of $x$, so
(1) yields $\beta_I=\alpha_I+o(\sqrt x)$ uniformly. On each annulus,
Cauchy--Schwarz gives

$$
\sum_I\alpha_I\beta_I=\sum_I\alpha_I^2+o(x)
\ge\left(\frac{(\sqrt L-\sqrt{2M})^2}{L-1}+o(1)\right)x
>\left(\frac{49}{64}+o(1)\right)x.
$$

Let $T=L^3x$ and let $d_T(t)$, $r_T(n)$ count differences and sums
using only elements at most $T$. Same-bin pairs have difference of
absolute value at most $x$, and therefore

$$
\sum_{|t|\le x}d_T(t)\ge(147/64+o(1))x.
$$

Using $\binom m2\ge m-1$ and the exact bijection
$a-b=a'-b'\leftrightarrow a+b'=a'+b$, we obtain

$$
\sum_{n\le2T}\binom{r(n)}2
\ge\sum_n\binom{r_T(n)}2
=\sum_t\binom{d_T(t)}2
\ge(19/64+o(1))x.
$$

For arbitrary $Y$, use $x=\lfloor Y/(2L^3)\rfloor$. Thus

$$
\liminf_{Y\to\infty}\frac1Y\sum_{n\le Y}\binom{r(n)}2
\ge\frac{19}{128(128M)^3}.
\tag{2}
$$

This contradicts $M=1$. If $M\ge2$, (2) implies

$$
\underline d\{n:r(n)\ge2\}
\ge\frac{19}{64(128M)^3M(M-1)}.
$$

Also $\binom r2\le M(r-1)/2$ for $1\le r\le M$, so

$$
\liminf_{x\to\infty}\frac{\sum_{n\le x}r(n)}x
\ge1+\delta_M,\qquad
\delta_M=\frac{19}{64M(128M)^3}.
\tag{3}
$$

## Consequence for counting products

Without assuming bounded $r$, termwise balance and eventual coverage imply

$$
\Lambda:=\limsup_{x\to\infty}\frac{A(x)B(x)}x\ge\frac4\pi.
$$

To see this, assume $\Lambda<\infty$. The inequalities
$A(x)\le B((1+\varepsilon)x)+O(1)$ and their symmetric counterparts
give $\limsup A(x)/\sqrt x,\limsup B(x)/\sqrt x\le\sqrt\Lambda$.
Consequently the Laplace sums satisfy

$$
F_A(t),F_B(t)\le(\sqrt\Lambda\,\Gamma(3/2)+o(1))t^{-1/2}.
$$

If $R(x)=\sum_{n\le x}r(n)$ has $\liminf R(x)/x\ge\kappa$, then
$F_A(t)F_B(t)\ge(\kappa-o(1))/t$. Since $\Gamma(3/2)^2=\pi/4$,
we get $\Lambda\ge4\kappa/\pi$.
Coverage permits $\kappa=1$, proving the claim. Under boundedness, (3)
improves it to

$$
\Lambda\ge\frac4\pi(1+\delta_M)>\frac4\pi.
$$

In particular the target assertion holds if one adds the hypothesis
$\limsup A(x)B(x)/x\le4/\pi$. The general case remains open here.

## Exact capacity descent and its missing hypotheses

For $h>0$, define
$$
 A_h=\{a:a,a+h\in A\},\qquad B_h=\{b:b,b+h\in B\}.
$$
If $R_n=\{a\in A:n-a\in B\}$, then
$$
 r_{A_h,B_h}(n-h)=|R_n\cap(R_n-h)|
 \le\max\{r_{A,B}(n)-1,0\}.
\tag{4}
$$
Indeed, a derivative representation has $b=n-a-h$, so it is
equivalent to $a,a+h\in R_n$. The largest element of a nonempty
finite $R_n$ cannot start such a pair. Thus a global capacity $M$
descends to $M-1$ for every derivative pair.

Counting unordered pairs of distinct representations also gives the
coefficientwise identity
$$
 \binom{r_{A,B}(n)}2
 =\sum_{h\ge1}r_{A_h,B_h}(n-h).
\tag{5}
$$
Every pair has one positive difference $h$ between its two first
coordinates, so it contributes to exactly one term.

Under a global capacity two, all derivative pairs have unique sums,
and the shifted sumsets $A_h+B_h+h$ are pairwise disjoint. Their
union is exactly the set of doubly represented integers. With eventual
coverage, (5) becomes
$$
 r_{A,B}(n)-1=\sum_{h\ge1}r_{A_h,B_h}(n-h)
$$
for all sufficiently large $n$. With merely eventual capacity two,
the same statements apply to the corresponding sufficiently large
target sums, not necessarily to their finite initial portions.

This descent does not iterate the capacity-one contradiction: neither
cofinite coverage nor rank balance has been proved for any derivative
pair. Those are the missing hypotheses, not consequences of (4) or (5).
