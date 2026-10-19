---
name: theory/number_theory/L66_divisor_residue_spread/_proof
title: Exponent pairing and full-divisor mixing
desc: |
  A finite residue-fiber count, its uniform dyadic consequence, and the
  conversion of polynomial mixing parameters into L63's local representatives.
created: 2026-10-14T09:12:10Z
updated: 2026-10-14T09:12:10Z
---

***

We prove [[theory/number_theory/L66_divisor_residue_spread/_index|L66]].

## Pair the exponents

Write $N=\prod_p p^{e_p}$. Partition the exponent choices
$0,1,\ldots,e_p$ for each $p\in P$ into consecutive pairs
$\{0,1\},\{2,3\},\ldots$, allowing a final singleton. Fix the chosen
pair for every selected prime and fix all exponents at the other primes.
Within this cell a divisor has the form

$$
b\prod_{p\in P}p^{\delta_p},\qquad \delta_p\in\{0,1\},
$$

with some choices possibly forced by the singleton cells. The factor $b$
is fixed and invertible modulo $q$. The products of selected primes are
distinct positive integers, by unique factorization, and all are smaller
than $q$. Thus this cell contains at most one divisor in any specified
residue class modulo $q$.

There are $\lceil(e_p+1)/2\rceil$ cells at prime $p$. Dividing the total
number of cells by the number $\tau(N)=\prod_p(e_p+1)$ of divisors gives

$$
\frac{\#\{d\mid N:d\equiv a\pmod q\}}{\tau(N)}
\le\prod_{p\in P}
       \frac{\lceil(e_p+1)/2\rceil}{e_p+1}
\le(2/3)^{|P|}.                                      \tag{1}
$$

The last inequality holds for every integer $e_p\ge1$; the largest ratio
is $2/3$, at $e_p=2$. The empty choice of $P$ gives the trivial bound one.

## All dyadic levels through K

Let $N$ be the odd part of $K!$. We use the standard Chebyshev bounds in
the explicit forms $\sum_{p\le y}\log p\le C_1y$ for $y\ge2$ and
$\pi(y)\ge c_1y/\log y$ for all sufficiently large $y$.
Choose a fixed $\alpha>0$ smaller than both $1$ and
$(\log2)/(2C_1)$. For sufficiently large $j\le K$, take $P$ to be the
odd primes at most $\alpha j$. They all divide $N$, and

$$
\prod_{p\in P}p\le\exp(C_1\alpha j)<2^j,
\qquad |P|\gg\frac{j}{\log j}\ge c_2\frac{j}{\log(K+1)}.
$$

Equation (1) gives the claimed residue bound for these $j$. There are only
finitely many smaller integers $j\ge2$ to cover. For each of them use
$P=\{3\}$, since $3<2^j$ and $3\mid K!$ once $K\ge3$. Reducing the
absolute constant $c$ covers all these levels simultaneously. This proves
that, for every sufficiently large $K$, the uniform law $\mu_K$ on the
odd divisors of $K!$ satisfies

$$
\max_a\mu_K(a\bmod 2^j)
\le2^{-g_Kj}\quad(2\le j\le K),\qquad
g_K=\frac{c}{\log_2(K+1)}.                            \tag{2}
$$

Reduce $c$ further if necessary so that $g_K\le1/2$.

## A necessary number of multiplicative factors

Fix $0<g\le1/2$ and suppose $W(g;r,t,J_0)$ holds. For large $J$, set
$b_J=\lceil gJ\rceil+1$ and let $X_J$ be all positive odd integers
smaller than $2^{b_J}$. At levels $2\le l\le b_J$ the largest residue
mass is $2^{1-l}\le2^{-gl}$. At levels $b_J<l\le J$ it is
$2^{1-b_J}\le2^{-gJ}\le2^{-gl}$. Thus $X_J$ meets every required
nonconcentration bound.

If $rg<1$, every product $z$ of $r$ members is smaller than $2^{rb_J}$,
and $2^{rb_J-J}\to0$. Hence $e^{2\pi i z/2^J}\to1$ uniformly over
these products. The primitive Fourier coefficient of their product law
has modulus tending to one. This contradicts $W$'s bound $2^{-tJ}\to0$.
Therefore

$$
rg\ge1.                                               \tag{3}
$$

This is a restriction on the universal mixing assertion, not on one
particular factorial-divisor law.

For the separated-block construction,
[[theory/number_theory/L64_factorial_digit_entropy/_index|L64]] gives an
additional consequence. If its factorial index is linear up to logarithms
and its block count is polylogarithmic, an admissible exponent $g_K$ must
tend to zero, because the top-level atom bound requires
$g_KK\le\log_2|X_K|=o(K)$. Hence (3) forces $r_K\to\infty$.
The source's displayed term bound
$s_K((\operatorname{binaryLength}(K)+1)^{r_K}+1)$, with $s_K\ge1$,
then exceeds every fixed power of $\log K$. Thus changing the parameters
alone cannot turn that displayed construction into L63's required bound.
This does not rule out a new representation argument using the same
numbers more efficiently.

## Use quantitative mixing without expanding digit sums

Assume the last clause's quantitative hypothesis, and choose its witnesses
$r,t,J_0$ at $g=g_K$. They obey

$$
r,J_0,1/t=O((\log K)^A).
$$

Let $\sigma$ be the law of a product of $r$ independent odd divisors of
$K!$, viewed modulo $2^K$. For every character of conductor $2^j$ with
$J_0\le j\le K$ and $j\ge2$, (2) and $W$ give

$$
|\widehat\sigma(a/2^j)|\le2^{-tj}\qquad(a\text{ odd}). \tag{4}
$$

The same integer product law may be reduced modulo each $2^j$, so the
application uses the same $r,t$ at every conductor.

Put $b=\max(1,J_0)$ and choose a positive integer $q$ with $tq\ge2$
and $q=O(1+1/t)$. For large $K$, $b<K$. Let $\nu_b$ be the uniform
law on $\{0,1,\ldots,2^b-1\}$, embedded modulo $2^K$. It kills exactly
the needed low conductors: its Fourier coefficient is zero at every
nontrivial character of conductor $2^j$ with $j\le b$. Therefore the
sum of the nontrivial Fourier magnitudes of the **additive** convolution
$\sigma^{*q}*\nu_b$ is at most

$$
\sum_{j=b+1}^K2^{j-1}2^{-tqj}
\le\sum_{j=b+1}^{\infty}2^{-j-1}<1.                  \tag{5}
$$

Fourier inversion makes this convolution positive on every residue.
Accordingly every residue modulo $2^K$ has an integer representative

$$
S=z_1+\cdots+z_q+B,\qquad
0\le B<2^b,
$$

where each $z_i$ is a product of $r$ divisors of $K!$. Such a product is
a **single** divisor of $(rK)!$, since $(K!)^r\mid(rK)!$.
Write $B$ in binary, with at most $b$ summands among
$1,2,\ldots,2^{b-1}$. These divide $(2b)!$.
Thus $S$ is a sum of at most $q+b$ divisors of $F!$, repetitions allowed,
for $F=rK+2b$. It satisfies

$$
\begin{gathered}
F=O(K(\log K)^A),\qquad q+b=O((\log K)^A),\\
0\le S\le q(K!)^r+2^b,\qquad
\log_2(q(K!)^r+2^b)=O(K(\log K)^{A+1}).
\end{gathered}                                                    \tag{6}
$$

These are L63's hypotheses with exponents $a=A$, $b=A$, $d=A+1$
(the exponent called $b$ there is separate from the binary cutoff here).
Rounding the height exponent to an integer and enlarging its fixed constant
does not change the bounds. L63 gives
$h(n!)=O((\log n)^{3A+4})$.

The polynomial quantitative hypothesis has not been proved. The argument
shows precisely why it would suffice; it does not infer such bounds from a
mixing theorem that supplies only existential constants for each fixed $g$.

## The loss in the displayed source witnesses

In the held source's `exists_dyadic_unit_product_fourier_decay`, $R$
flattening steps give a power $N=2^{R+2}$ and decay
$t=(g-\min(g/2,1/2))/N$. The final `weighted_dyadic_mixing` takes
$r=R+2$. Thus for $0<g\le1/2$ the displayed witnesses obey

$$
t=\frac{g}{2^{R+3}},\qquad
R\ge\frac1g-2,\qquad
\frac1t\ge\frac2g\,2^{1/g},                           \tag{7}
$$

where the middle inequality follows from (3), since these witnesses satisfy
the universal property $W$. This lower bound is not polynomial in $1/g$.
At the value $g_K$ in (2) it is at least
$2(K+1)^{1/c}/g_K$, so the additive-copy count certified by this decay
bound is not polylogarithmic in $K$.

This stops the extraction through these displayed witnesses. It does not
refute the polynomial quantitative hypothesis for different witnesses,
stronger concentration of the particular full-divisor law, or a different
way of obtaining coverage. In particular, reducing the number of flattening
steps to $O(\log(1/g))$ while retaining $r=R+2$ cannot repair the universal
argument: (3) forbids that. The exponential loss in the Fourier conversion,
or the use of a universal small-$g$ mixing statement, must be replaced.
