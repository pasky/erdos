---
name: research/erdos_699/archive/previous_bounds/effectivity
title: "Erdős 699: how much of the finite exceptional set is effective?"
desc: "Every i>=9 and i=1,2,7 is excluded; four indices at least four still lack effective bounds."
created: 2026-09-21T19:02:37Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: how much of the finite exceptional set is effective?

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]]

**Current classification.** The [cutoff-nine proof](../../proofs/details/cutoff_9.md)
combines fully numerical Padé estimates with completed finite certificates.

| Index | What can be concluded |
| --- | --- |
| $i=1,2,7$ or $i\ge9$ | No bad triples. |
| $i\in\{4,5,6,8\}$ | Finiteness is known, but no effective row bound is obtained here. |
| $i=3$ | Global finiteness remains unproved; bad rows exceed $10^{19}$ and have $v_2(n)\ge49$. |

The whole-index effectivity gap is concentrated in **four indices**.
The [complete proofs at seven and nine](../../proofs/details/cutoff_9.md)
exclude every bad triple at both indices. The arguments below retain the
original effectivity reduction.

The reductions below are deductions made in this investigation. Their novelty
has not been assessed. We use the original threshold $p\ge i$ throughout;
replacing it with $p>i$ changes the small-prime set at prime indices.

## Inputs from the retained work

Write

$$\binom ni=U_i(n)V_i(n),\qquad
S_i=\{p:p<i\},\qquad s_i=|S_i|=\pi(i-1),$$

where $U_i$ is supported on $S_i$ and $V_i$ on primes at least $i$.
A triple is bad if no prime at least $i$ divides both required binomial
coefficients.

The detailed manuscript,
Propositions 3 and 4, gives under badness

$$V_i(n)<n^{\rho_i},\qquad
\rho_4=\frac{17}{6},\qquad
\rho_i=\frac{3k(k+1)}{2(3k-i+1)},\quad
k=\left\lfloor\frac{2i}{3}\right\rfloor\quad(i\ge5).\tag{1}$$

In particular $\rho_i<i-1$. The existing fixed-index proof combines this
with Bugeaud–Evertse–Győry (BEG), Theorem 2.1, which gives
$U_i(n)\ll_{i,\epsilon}n^{1+\epsilon}$ with an ineffective constant.
This is exactly where its last-row bound is lost. The sharp theorem uses
$p$-adic Thue–Siegel–Roth; it is not merely a numerical estimate whose
constant the manuscript forgot to calculate.

The separate [retained determinant calculation](../../../../../library/factorials_binomials/van_doorn_rocca_2026_binomial_coefficients_sharing_large_prime_divisor/_index.md)
and [checker](../../computations/erdos_699_i_ge_906.py) eliminate $i\ge906$.
Improving that upper cutoff alone does not make the small-index theorem
effective.

## Elementary effective bounds

Kummer's formula gives, for every prime $p$,

$$
p^{v_p(\binom ni)}\le n,
$$

and therefore

$$
U_i(n)\le n^{s_i}.\tag{2}
$$

Combining (1), (2), and $\binom ni\ge(n/i)^i$ shows that badness implies

$$
n^{\eta_i}<i^i,\qquad \eta_i=i-\rho_i-s_i.\tag{3}
$$

Whenever $\eta_i>0$, this is the explicit bound
$n<i^{i/\eta_i}$, uniform in $j$.
Exact rational calculation for $4\le i\le905$ gives

$$\begin{aligned}
\eta_i>0&\iff i=29\text{ or }35\le i\le905,\\
\eta_i=0&\iff i\in\{28,31,34\},\\
\eta_i<0&\iff i\in\{4,\ldots,27,30,32,33\}.
\end{aligned}\tag{4}$$

We can retain constants to improve (3). For $i\ge5$ put

$$
m=3k-i+1,\qquad A=\frac{k(k+1)}2,\qquad d=3A.
$$

In the manuscript's polynomial $F_i(j,c)$, $c=n-j$, pair its vertical and
horizontal factors. Since

$$
(j-r)(c-r)\le jc\le n^2/4,
$$

its displayed product gives

$$
V_i(n)^m\le F_i(j,c)<\frac{n^d}{4^A}.\tag{5}
$$

For $n\ge i(i-1)$, the elementary product inequality
$\prod_r(1-r/n)\ge1-\sum_r r/n\ge1/2$ also gives

$$
\binom ni\ge\frac{n^i}{2i!}.
$$

Consequently, with the positive integer $E=m(i-s_i)-d=m\eta_i$,
every bad triple in this range satisfies

$$
4^A n^E<(2i!)^m.\tag{6}
$$

Any integer $B\ge i(i-1)$ satisfying $4^AB^E\ge(2i!)^m$ is therefore an
exclusive row bound: $n<B$. The checker chooses certified powers of ten.
Some examples are:

| $i$ | $\eta_i$ | Certified necessary condition for badness |
| --- | --- | --- |
| 29 | $10/29$ | $n<10^{80}$ |
| 35 | $12/35$ | $n<10^{104}$ |
| 37 | $1$ | $n<10^{39}$ |
| 38 | $13/38$ | $n<10^{117}$ |
| 44 | $15/44$ | $n<10^{144}$ |
| 100 | $8$ | $n<10^{19}$ |
| 905 | $133337/905$ | $n<10^{15}$ |

The largest power of ten needed over all 872 indices is $10^{144}$, at
$i=44$. These are convenient certified bounds, not optimal cutoffs. In
particular, the existing determinant bounds can be used when they are smaller.

## Effective finiteness at the three equalities

The positive saving in BEG's **effective** Theorem 2.2 suffices at
$i=28,31,34$, provided we first reduce the polynomial's degree.

Let

$$
f_i(X)=\prod_{r=0}^{i-1}(X-r).
$$

For each $p\in S_i$, choose $r_p\in\{0,\ldots,i-1\}$ at which
$v_p(n-r)$ is maximal. If $t\ne r_p$, the ultrametric inequality gives

$$
v_p(n-t)\le v_p(t-r_p).
$$

Indeed, if the two valuations at $n-t$ and $n-r_p$ differ, their minimum
is the valuation of the difference; if they agree, the difference has at
least that valuation. Therefore

$$\begin{aligned}
v_p(f_i(n))
&\le v_p(n-r_p)+v_p\bigl(r_p!(i-1-r_p)!\bigr)\\
&\le v_p(n-r_p)+v_p((i-1)!).
\end{aligned}$$

Choose a set $T\subset\{0,\ldots,i-1\}$ of exactly $s_i$ elements
containing every $r_p$; add arbitrary indices if some maxima coincide.
Put $g_T(X)=\prod_{t\in T}(X-t)$. Multiplying the preceding bounds over
$p\in S_i$ yields

$$[f_i(n)]_{S_i}\le(i-1)![g_T(n)]_{S_i},\qquad
U_i(n)\le\frac{(i-1)!}{[i!]_{S_i}}[g_T(n)]_{S_i}.\tag{7}$$

The prefactor in the second inequality is $1/i$ when $i$ is composite
and $1$ when $i$ is prime. In particular it is at most $1$.

Each $g_T$ has degree $s_i\ge2$ and distinct rational roots. BEG Theorem
2.2 supplies effectively computable $C_T>0$ and $0<\kappa_T<1$ such that

$$[g_T(n)]_{S_i}\le C_T|g_T(n)|^{1-\kappa_T}
\le C_T n^{s_i(1-\kappa_T)}.$$

There are only $\binom{i}{s_i}$ choices of $T$. Taking the maximum of their
constants and the minimum of their positive savings gives computable
$C_i\ge1$, $\delta_i>0$ with

$$
U_i(n)\le C_i n^{s_i-\delta_i}.\tag{8}
$$

At $i=28,31,34$, (4) says $i-\rho_i=s_i$, while badness forces
$U_i(n)>i^{-i}n^{s_i}$. Thus

$$
n<(C_i i^i)^{1/\delta_i}.\tag{9}
$$

This proves effective finiteness at these three indices. Extracting numerical
values of $C_i,\delta_i$ from the logarithmic-form bounds has not been carried
out in this investigation, and no numerical cutoff for these indices is
claimed. Merely using Theorem 2.2 on the original degree-$i$ polynomial would
miss this argument: the degree reduction in (7) is essential to reach the
borderline exponent.

## Why this does not yet determine the entire set

For each of the 27 indices left by the estimates above, (8) would need the stronger saving

$$
\delta_i>s_i-(i-\rho_i).\tag{10}
$$

An unspecified positive saving is insufficient. The sharp ineffective
theorem can reach the needed exponent, while the effective theorem does not
allow us to choose an arbitrarily large saving.

For example, at $i=4$ the reconstructed certificate requires

$$U_4(n)>4^{-4}n^{7/6},\qquad
U_4(n)=[\tbinom n4]_{\{2,3\}}.$$

After the degree reduction, the elementary scale is $n^2$. To contradict
badness using (8) needs $\delta_4>5/6$, not merely $\delta_4>0$.
At $i=5$, the analogous requirement is $\delta_5>3/5$.
No such effective estimates have been established here.

Nor does the familiar observation that $S$-unit or Thue–Mahler equations are
effectively solvable immediately complete the proof. Writing
$f_i(n)=u b$ with $u$ an $S_i$-unit leaves an unbounded rough cofactor $b$.
The certificate bounds that cofactor by a positive power of $n$, not by an
absolute constant. Solving the equation for each fixed $b$ therefore leaves
an infinite family unless another argument bounds $b$.

The first unresolved index can be made more concrete. At $i=4$, let
$2^a\Vert n-r_2$ and $3^b\Vert n-r_3$ be the maximal powers among the
four numerator factors. The proof of (7), before replacing the selected
powers by $[g_T(n)]_{S_i}$, gives

$$
U_4(n)\le\frac{2^a3^b}{4}.\tag{11}
$$

The quartic certificate also retains a factor $4^5$: its paired vertical
and horizontal factors have total exponent $5$ in $j(n-j)$, so
$V_4(n)^6<n^{17}/4^5$. For $n\ge12$, it follows that

$$
U_4(n)>\frac{4^{5/6}}{48}n^{7/6}.\tag{12}
$$

If $r_2=r_3$, the product $2^a3^b$ divides a single number $n-r_2\le n$.
Equations (11) and (12) then imply

$$
n<\left(\frac{12}{4^{5/6}}\right)^6=2916.
$$

Thus any bad triple with $i=4$ and $n\ge2916$ has distinct maximal
positions. Write

$$
n-r_2=2^a u,\qquad n-r_3=3^b v.
$$

It must satisfy

$$2^a u-3^b v=r_3-r_2\in\{-3,-2,-1,1,2,3\},\qquad
uv<4n^{5/6}.\tag{13}$$

There are only twelve ordered position pairs, but the cofactors $u,v$
remain unbounded. These are necessary conditions, not a characterization
of badness. They identify a specific place to combine an effective
Diophantine argument with the additional congruences on $j$.

A productive next step is to retain the individual Kummer labels
$r+s=t$, rather than replace all the congruences with one estimate on $U_i$.
The target is an additional relation bounding a cofactor or reducing to a
finite list of explicitly solvable equations. Better constants in the
$i\ge906$ argument do not supply that relation.

## Exact testing once a row is supplied

For fixed $n,i$, factor $\binom ni$ and retain each $q^a\Vert V_i(n)$.
Kummer localization gives the necessary condition

$$
j\bmod q^a\in\{0,\ldots,n\bmod q^a\},\qquad n\bmod q^a<i.\tag{14}
$$

These conditions can be intersected by CRT. Alternatively, generate $j$
from the sparsest single condition and filter by the others. Finally test
the full Lucas condition at each rough prime: every base-$q$ digit of $j$
must be at most the corresponding digit of $n$. The columns that pass all
these tests are exactly the bad columns, without constructing
$\binom nj$. Checking only (14) is not sufficient: carries in higher digits
can still make $q\mid\binom nj$.

The [checker](../../computations/erdos_699_effectivity.py) implements this
fixed-row search, the index classification, and the bounds (6). Its
[recorded output](../../computations/erdos_699_effectivity.json) includes
all 902 index records. It uses 60-digit outward-rounded logarithms to certify
the powers of ten, with independent exact integer comparisons at five
representative indices. The row search agrees with direct binomial gcd
testing on all 234,685 admissible triples with $n\le200$ and $i\le34$;
none is bad. This bounded check validates the search implementation and is
not evidence that the global finite search is complete.

Reproduce with Python 3.11 or later:

```sh
python3 wiki/research/erdos_699/computations/erdos_699_effectivity.py
```

The original outstanding question was a **provable stopping bound** for
27 indices. The [subsequent prime-pair argument](small_index_effective.md)
reduces this to the nine indices listed at the top of this note.
Finiteness alone, or a counterexample-free search through a large row,
does not provide a stopping bound.

## Additional source

Bugeaud, Evertse and Győry, *S-parts of values of univariate polynomials,
binary forms and decomposable forms at integral points*, Acta Arith. 184
(2018), 151–185, [DOI](https://doi.org/10.4064/aa170828-7-3).
Theorem 2.1 is the sharp ineffective input; Theorem 2.2 is the effective
input used in (8).
