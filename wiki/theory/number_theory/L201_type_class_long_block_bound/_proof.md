---
name: theory/number_theory/L201_type_class_long_block_bound/_proof
title: Type classes of three cells
desc: Balanced three-cell words give exact multinomial and projection counts; prime averaging gives an elementary bound, while full prime realization and Stirling's formula give a smaller logarithmic factor.
created: 2026-10-15T15:58:15Z
updated: 2026-10-15T15:58:15Z
---

***

**The cells.** Let $c_1=(0,1)$, $c_2=(2,1)$ and $c_3=(2,2)$. Their
differences $y-x$ are $1$, $-1$ and $0$. Their values of $x$ are
$0,2,2$; of $y$ are $1,1,2$; and of $2y-x$ are $2,0,2$. So in each of
the three projections exactly one cell takes a value of its own: $c_1$
for $x$, $c_3$ for $y$ and $c_2$ for $2y-x$.

**Type classes.** For $m\ge1$ let $S_m$ be the set of pairs
$\bigl(\sum_{i=1}^{3m}x_i3^{i-1},\ \sum_{i=1}^{3m}y_i3^{i-1}\bigr)$, where
$(x_i,y_i)=c_{\sigma(i)}$ for a sequence $\sigma\in\{1,2,3\}^{3m}$ taking
each value exactly $m$ times. The difference of such a pair is
$\sum_i(y_i-x_i)3^{i-1}$ with digits in $\{-1,0,1\}$. Balanced ternary
digits are unique and the three cells have distinct differences, so the
difference determines $\sigma$. Hence

$$
|S_m|=\frac{(3m)!}{(m!)^3}\ \ge\ \frac{27^m}{(3m+2)^2},
$$

and $y-x$ is injective on $S_m$. The inequality holds because the
$\binom{3m+2}{2}\le(3m+2)^2$ trinomial coefficients of
$(1+1+1)^{3m}$ sum to $27^m$ and the central one is the largest.

The value of $x$ on $S_m$ is determined by the set of positions $i$
with $\sigma(i)=1$, which has $m$ elements; likewise $y$ is determined
by the positions of $c_3$ and $2y-x$ by the positions of $c_2$. So
each projection takes at most

$$
\binom{3m}{m}\ \le\ \frac{(3m)^{3m}}{m^m(2m)^{2m}}=\Bigl(\frac{27}{4}\Bigr)^m
$$

values. In fact there are exactly $\binom{3m}{m}$ values: every set of
$m$ positions can be used for the distinguished cell, and the ordinary
base-three digits of each projection lie in $\{0,1,2\}$, so different
position sets give different values. Finally
$0\le x,y\le2(3^{3m}-1)/2<27^m$ on $S_m$.

**Primes.** Fix $3\le\alpha<4$ and put $\omega_m=27^m$. By the prime
number theorem there is $Q_*$ with
$\pi(31Q/16)-\pi(17Q/16)\ge Q/(2\log Q)$ for all $Q\ge Q_*$. Let $Q_m$
be the least integer with
$Q_m\ge\max\bigl(Q_*,\,32\omega_m,\,(16\omega_m+1)/(4-\alpha)\bigr)$.
Every difference on $S_m$ has absolute value below
$\omega_m\le Q_m/32$, so each interval
$(Q_m+y-x,\,2Q_m+y-x]$ contains $(17Q_m/16,\,31Q_m/16]$ and holds at
least $Q_m/(2\log Q_m)$ primes. Summing over the cells, the $Q_m$
integers $q\in(Q_m,2Q_m]$ make $q+y-x$ prime for at least
$|S_m|\,Q_m/(2\log Q_m)$ pairs of an integer $q$ and a cell. So some
such $q$ makes $q+y-x$ prime for at least $|S_m|/(2\log Q_m)$ cells of
$S_m$.

**The block.** For any $u\ge1$ of these cells, the primes $q+y-x$ are
distinct, $|x|,|y|\le\omega_m$, and $(4-\alpha)q\ge16\omega_m+1$. By
L198 some block of $\lfloor\alpha P\rfloor$ consecutive positive
integers, $P$ the largest of the $u$ primes, contains at most
$3\binom{3m}{m}\le3(27/4)^m$ integers divisible by one of them, each
counted once. Hence, with $G_\alpha(u)$ the least such count over all
sets of $u$ primes and all blocks,

$$
G_\alpha(u)\ \le\ 3\Bigl(\frac{27}{4}\Bigr)^m=3\cdot27^{m\theta}
\qquad\text{whenever }1\le u\le\frac{27^m}{2(3m+2)^2\log Q_m}.
$$

**Parameters.** There is $c_\alpha$ with $\log Q_m\le c_\alpha m$ for all
$m\ge1$, since $Q_m$ is at most a constant multiple of $27^m$. Given
$u\ge2$, let $m\ge1$ be least with
$27^m\ge2c_\alpha m(3m+2)^2u$; the displayed condition then holds. If
$m\ge2$, minimality gives $27^{m-1}<2c_\alpha m(3m+2)^2u$, so
$27^m<54c_\alpha m(3m+2)^2u$ and $m=O_\alpha(\log u)$. Therefore

$$
G_\alpha(u)\ \le\ 3\bigl(54c_\alpha m(3m+2)^2u\bigr)^\theta
=O_\alpha\bigl(u^\theta(\log u)^{3\theta}\bigr),
$$

and $3\theta<2$. For $u$ below any fixed bound, $m$ and hence the
bound $3\cdot27^{m\theta}$ stay bounded, so one constant $C_\alpha$
gives $G_\alpha(u)\le C_\alpha u^\theta(\log u)^2$ for every $u\ge2$.
This is the alternative bound using the prime number theorem.

The numerical range follows from
$\theta=1-2\log2/(3\log3)=0.57938\ldots$.

**The stronger bound using Green--Tao.** Let
$n_m=(3m)!/(m!)^3$ and $b_m=\binom{3m}{m}$. By L202, for every
$1\le u\le n_m$ and every $3\le\alpha<4$, any $u$ cells of $S_m$
have a prime realization whose block has at most $3b_m$ counted
integers. No prime-selection loss occurs. Stirling's formula gives

$$
n_m\asymp\frac{27^m}{m},\qquad
b_m\asymp\frac{(27/4)^m}{\sqrt m}
\asymp n_m^\theta m^{\theta-1/2},
$$

with absolute implied constants. Choose the least $m\ge1$ with
$n_m\ge u$. Since

$$
\frac{n_m}{n_{m-1}}
=\frac{(3m)(3m-1)(3m-2)}{m^3}<27\qquad(m\ge2),
$$

we have $n_m<27u$; this also holds for $m=1$, where $n_1=6$ and
$u\ge2$. The same estimates give $m=O(\log u)$. Since
$\theta>1/2$,

$$
G_\alpha(u)\le3b_m
\le C u^\theta(\log u)^{\theta-1/2}.
$$

All constants are absolute because $\alpha$ enters only L202's prime
realization. This proves the claim. For complete classes $u=n_m$, their
exact three-layer count is $3b_m$, and
$b_m/n_m^\theta\asymp m^{\theta-1/2}\to\infty$. Thus these full
type classes do not themselves yield an $O(u^\theta)$ bound.
