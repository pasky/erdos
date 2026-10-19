---
name: research/erdos_699/archive/other_approaches/more_prime_pairs
title: "Erdős 699: further effective prime-pair estimates"
desc: "Twelve certified Padé parameter choices strengthen two published pair estimates, add bounds involving 17,19,23, and improve the cofactor exponents available to the small-index argument."
created: 2026-09-22T03:25:22Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: further effective prime-pair estimates

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/archive/previous_bounds/small_index_effective|Small-index bounds]] ·
[[research/erdos_699/archive/previous_bounds/effective_index_24|The first effective index-24 bound]]

The general Padé theorem of Bennett, Filaseta, and Trifonov (BFT) gives
additional useful prime-pair estimates. The twelve choices below are
certified by directed interval arithmetic. They include improvements to
the published weights for $(2,11)$ and $(3,5)$.

The source is the BFT paper,
Theorem 2.2. No assertion of optimality is made for these parameters.

## The additional estimates

For each pair in the table, and every fixed positive integer $D$, there
is an effectively computable threshold such that

$$|p^a u-q^b v|\le D
\quad\Longrightarrow\quad
\max(u,v)>\min(p^a u,q^b v)^{\lambda}.
\tag{1}$$

Both quantities in the minimum must exceed the threshold. The cofactors
are positive integers and $a,b$ are nonnegative integers.

In the seed column, $P$ and $Q$ are powers of the two indicated primes,
in whichever order makes $a_0P-b_0Q$ positive.

| Pair | Certified $\lambda$ | Seed $a_0P-b_0Q$ | $s=c/d$ |
| --- | ---: | --- | --- |
| $2,11$ | $.1399$ | $21\cdot2^{15}-47\cdot11^4=1$ | $13/6$ |
| $3,5$ | $.2543$ | $7\cdot5^4-2\cdot3^7=1$ | $13/8$ |
| $2,17$ | $.3560$ | $17-2^4=1$ | $34/25$ |
| $3,17$ | $.1190$ | $2\cdot3^2-17=1$ | $31/18$ |
| $5,17$ | $.0093$ | $3\cdot17-2\cdot5^2=1$ | $57/26$ |
| $3,19$ | $.1268$ | $3^6-2\cdot19^2=7$ | $35/27$ |
| $7,19$ | $.1588$ | $20\cdot7^3-19^3=1$ | $67/40$ |
| $11,19$ | $.2077$ | $3\cdot11^2-19^2=2$ | $53/37$ |
| $17,19$ | $.2176$ | $5\cdot17^2-4\cdot19^2=1$ | $32/17$ |
| $2,23$ | $.0245$ | $23^2-2^9=17$ | $45/38$ |
| $5,23$ | $.2144$ | $5^2-23=2$ | $41/31$ |
| $11,23$ | $.1478$ | $23-2\cdot11=1$ | $5/3$ |

For $(17,19)$ take $\epsilon=10^{-6}$ in BFT Theorem 2.2;
for every other row take $\epsilon=10^{-5}$. The
[parameter certificate](../../computations/erdos_699_bft_more_pairs.py)
checks $\Omega_1>1$, $\Omega_2>1$, and
$\lambda_1>\lambda+\epsilon$ for every row. Its lower bounds for the
digamma differences use the positive series and integral tails proved
in the earlier index-24 note, rather than unbounded floating-point
evaluations. Thus (1) follows directly from BFT Theorem 2.2.

For example, the two improved old pairs have certified intervals

$$\begin{array}{c|c|c|c}
\{p,q\}&\log\Omega_1&\log\Omega_2&\lambda_1\\\hline
\{2,11\}&(.00658244,.00658249)&(3.66503731,3.66503736)&(.139927933,.139927936)\\
\{3,5\}&(.04739944,.04739948)&(4.26327874,4.26327879)&(.254372338,.254372341).
\end{array}$$

Their weights in the
[prime-pair table](../previous_bounds/small_index_effective.md) are $.0698$ and
$.2238$, respectively.

## Combining all available pairs

Choose the maximal positions $r_p$ and cofactors $u_p$ as in the
small-index note, and set

$$
z_p=\frac{\log u_p}{\log(n-i+1)}.
$$

Once the source thresholds hold, every pair gives
$\max(z_p,z_q)\ge\lambda_{pq}$. Combining the new table with
BFT Corollary 2.3 gives the exact minimum sums below:

| Available primes | Minimum sum of the $z_p$ |
| --- | ---: |
| $2,3,5,7,11,13$ | $1.0120$ |
| The preceding primes and $17$ | $1.0923$ |
| The preceding primes and $19$ | $1.3099$ |
| The preceding primes and $23$ | $1.4577$ |

The [recorded certificate](../../computations/erdos_699_bft_more_pairs.json)
contains all componentwise minimal vectors, not just their minimum sums.
They can therefore also be used in estimates that keep the individual
cofactor exponents.

The finite verification is elementary. Start with the zero vector. For
each edge of weight $w$, leave a vector unchanged if an endpoint is
already at least $w$; otherwise make the two possible extensions by
raising one endpoint to $w$. Remove any vector componentwise larger
than another retained vector. Every feasible real vector dominates a
retained vector at every stage, by induction on the edges. Thus the
minimum sum in the final list is the exact minimum for the original
maximum inequalities. This verifies a finite system of inequalities;
it does not search through binomial rows.

## Algebraic bounds after the source thresholds

If $\gamma$ is the relevant minimum, the earlier argument gives

$$U_i(n)\le\frac{2^\gamma}{[i]_{S_i}}n^{s_i-\gamma}
\quad(n\ge2(i-1)).$$

Together with the retained fat-point lower bound, this implies

$$n^{\eta_i}<\frac{2^\gamma i^i}{[i]_{S_i}},\qquad
\eta_i=i-\rho_i-s_i+\gamma.$$

The certificate checks the following powers of ten by clearing the
rational exponent denominators and comparing integer powers:

| $i$ | $\gamma$ | $\eta_i$ | Bound once all source thresholds hold |
| --- | ---: | ---: | --- |
| $19$ | $1.0923$ | $.0923$ | $n<10^{267}$ |
| $22$ | $1.3099$ | $.3099$ | $n<10^{93}$ |
| $24$ | $1.4577$ | $.1377$ | $n<10^{234}$ |
| $25$ | $1.4577$ | $.4577$ | $n<10^{75}$ |

These improve the algebraic part of the stopping argument. They are not
complete numerical last-row bounds: the additional BFT thresholds must
also be included, and stronger exponents can require larger thresholds.

## An evaluator for the fully explicit theorem

The separate [explicit-threshold evaluator](../../computations/erdos_699_bft_explicit_thresholds.py)
implements BFT Theorem 2.4. It accepts a certified value of $\log L_1$
and a threshold $m_0$ proving BFT (2.8), together with the seed,
$c,d,D,\epsilon$.

Both integrals defining $C_{1,\delta}$ and $C_{2,\delta}$ are
polynomial integrals with rational coefficients. The evaluator computes
them exactly using

$$\int_0^1 t^a(1-t)^b(1-zt)^k\,dt
=\sum_{r=0}^k\binom kr(-z)^r
\frac{(a+r)!b!}{(a+b+r+1)!}.$$

It then encloses $\kappa_1,\kappa_2,M,\log x_0$ by directed interval
arithmetic and certifies an integer $K$ for which $x_0<10^K$.
The value of $\log L_1$ and its $m_0$ remain explicit inputs; the
evaluator does not assume an effective asymptotic estimate is already
a numerical bound.

## Fully numerical bounds at 22, 24, and 25

Using the published entries of BFT Proposition 5.1, the evaluator
certifies these deliberately less sharp exponents with useful numerical
thresholds. Here $D=100$ throughout.

| Pair | Seed | $c/d$ | $L_1$ | $m_0$ | $\epsilon$ | Certified weight | Row threshold |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| $2,17$ | $17-16=1$ | $7/5$ | $1.4135$ | $74$ | $.012$ | $.3259$ | $10^{976}$ |
| $17,19$ | $5\cdot289-4\cdot361=1$ | $2$ | $1.9377$ | $150$ | $.007$ | $.1855$ | $10^{957}$ |
| $11,23$ | $23-2\cdot11=1$ | $7/4$ | $1.6219$ | $60$ | $.011$ | $.1068$ | $10^{940}$ |

The [recorded intervals](../../computations/erdos_699_bft_explicit_thresholds.json)
give respectively

$$\begin{aligned}
\log x_0&<2246.800,\\
\log x_0&<2202.645,\\
\log x_0&<2163.632.
\end{aligned}$$

Each row threshold already absorbs all maximal-position shifts through
$33$: the checker verifies $x_0<10^K-33$ for the displayed exponent
$K$. Thus the estimates hold at every binomial row $n\ge10^K$ for
the indices at most $34$ considered here.

For $i=22,25$, the pair $(17,19)$ is disjoint from the six primes in
the original explicit table. Its saving $.1855$ therefore adds directly
to the published-table saving $.913$, giving

$$
\gamma=1.0985,\qquad\eta_{22}=\eta_{25}=.0985.
$$

Exact integer comparisons in the pair checker give algebraic caps
$10^{290}$ and $10^{344}$, respectively. The source threshold dominates
both. Hence

$$
\boxed{n<10^{957}\quad\text{for every bad triple with }i=22\text{ or }25.}
$$

For $i=24$, retain the individual cofactor exponents in the
[weighted-ramp argument](../../methods/details/weighted_ramps.md).
The original explicit BFT table together with the three weights above
gives gain $983/1250=.7864$ at $k=16$, including every possible
collision of maximal positions. The
[exact weighted certificate](../../computations/erdos_699_weighted_ramps.py)
gives the algebraic cap $10^{635}$ and elementary threshold
$11\,132\,000$. Again the source threshold dominates, proving

$$
\boxed{n<10^{976}\quad\text{for every bad triple with }i=24.}
$$

These three are complete numerical row bounds. The intervals below them
have not been excluded by these arguments.

## Retaining different exponents at the two endpoints

The [asymmetric cofactor lemma](../../methods/details/asymmetric_cofactors.md)
improves the estimates further. For an oriented seed with prime powers
$P,Q$, put

$$
K=\log\max(P,Q)+\frac{\log\Omega_4}{s}.
$$

Any strict endpoint targets

$$t_P<1-\frac{\log P}{K},\qquad
t_Q<1-\frac{\log Q}{K}$$

give the disjunction $u>x^{t_P}$ or $v>x^{t_Q}$ for sufficiently large
bounded-gap inputs, where $x$ is the smaller input. The two targets
need not be equal. The cited lemma supplies an explicit threshold when
$L_1,m_0$ are explicit, and an effective threshold for a strict rational
lower bound on $\log L(s)$.

The [larger table checker](../../computations/erdos_699_bft_asymmetric_pair_table.py)
verifies [23 numerical and 24 effective parameter choices](../../computations/erdos_699_bft_asymmetric_pair_table.json).
It checks every seed's prime-power labels, the published $L_1,m_0$
entries, and strict interval margins for both endpoint targets. For
the effective entries it also verifies the rational inequality
$\log L_1<\log L(c/d)$ by the finite series bounds above.
These disjunctions supplement the old symmetric table; replacing a
symmetric constraint by an asymmetric one can lose an independently
useful restriction.

Two of the numerical entries are

$$\begin{aligned}
u_5>x^{.3613}&\quad\text{or}\quad u_7>x^{.2277},\\
u_7>x^{.0987}&\quad\text{or}\quad u_{13}>x^{.2080}.
\end{aligned}$$

They use respectively the published GCD parameters
$(c,d,L_1,m_0)=(8,5,1.5407,53)$ and $(7,5,1.4135,74)$.
For input gaps at most $100$, the direct threshold checker gives
$x\ge10^{2\,405\,782}$ and $x\ge10^{484\,367}$, respectively.
Together with the earlier effective pair constraints, these are the
additional inputs to the positive whole-index $i=18$ weighted
certificate: $k=12$, degree $156$, and gain $186/625$ over every
cofactor vector and every collision pattern. The
[complete index-18 certificate](../../proofs/details/index_18_effective.md)
checks all 65 minimal vectors and 5707 collision capacity lists. Its
algebraic term is $10^{814}$, and its full bound is
$n<\max\{X_{18},10^{2\,405\,782}\}+17$, where $X_{18}$ is the maximum
of the effective symmetric source thresholds for gap $17$.
