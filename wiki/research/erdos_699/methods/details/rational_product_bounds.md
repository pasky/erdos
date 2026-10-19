---
name: research/erdos_699/methods/details/rational_product_bounds
title: "Erdős 699: joint cofactor bounds with freely chosen Padé blocks"
desc: "A numerical product lemma retains denominator costs and optimizes the Padé block; it gives stronger joint cofactor restrictions than separate endpoint alternatives."
created: 2026-09-22T06:09:00Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: joint cofactor bounds with freely chosen Padé blocks

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/bft_rational_blocks|Rational residual blocks]] ·
[[research/erdos_699/methods/details/product_thresholds|Numerical product thresholds]]

***

The rational-block argument applies to products of several nearby factors.
It can also choose the block size according to the proposed cofactor bounds.
This gives effective joint restrictions beyond the rectangular alternatives
obtained by stopping at the first exhausted prime-power block.

The lemma below is conditional on a bounded product difference.
It does not, by itself, settle an index of the binomial problem.

## The product lemma

For distinct primes $p$, write

$$
f_p=p^{k_p}u_p,\qquad h\le f_p\le h+R,
$$

where $u_p$ are positive integers and $R\ge1$ is fixed. Partition the
primes into two nonempty sets $I_0,I_1$ and assign positive multiplicities
$b_p$ such that each product has degree $\nu$:

$$X=\prod_{p\in I_0}f_p^{b_p},\qquad
Y=\prod_{p\in I_1}f_p^{b_p},\qquad
\sum_{p\in I_0}b_p=\sum_{p\in I_1}b_p=\nu.$$

Assume $|X-Y|\le D$, where $D>0$ is fixed. Choose a valid BFT seed

$$P=\prod_{p\in I_0}p^{A_p},\qquad
Q=\prod_{p\in I_1}p^{A_p},\qquad aP-bQ>0,$$

and valid coefficient estimates for $s=c/d>1$ at every integer $m>m_0$.
Let $\kappa_1,\kappa_2,\Omega_3,\Omega_4$ be the constants of BFT
Theorem 2.4 for this seed and gap $D$. Suppose $\Omega_3,\Omega_4>1$ and put

$$C=\frac{\log\Omega_3}{s},\qquad
K=\log\max(P,Q)+\frac{\log\Omega_4}{s},\qquad J=K-C>0.$$

Given proposed upper exponents $0\le e_p\le1$ and any real $t>0$, define

$$
\Delta(t,e)=\sum_p(tA_p\log p-b_p(1-e_p))_+,
$$

$$\sigma_1=tC-\Delta(t,e),\qquad
\sigma_2=tK-\Delta(t,e)-\nu.$$

**Lemma.** If both margins $\sigma_1,\sigma_2$ are positive, then the
inequalities $u_p\le h^{e_p}$ cannot all hold once

$$\log h>
\max\left\{\log R,\ \frac{c(m_0+1)}t,\
\frac{\log A}{\min(\sigma_1,\sigma_2)}\right\},\qquad
A=\frac{\kappa_1}{2}e^{cC}
  +\frac{2^{\nu-1}}{\kappa_2}e^{cK}.\tag{1}$$

All constants in (1) are numerical when the coefficient-gcd estimate is
numerical. Otherwise the resulting threshold is still effectively computable
if the coefficient-gcd starting value $m_0$ is effective.

**Proof.** Set $m=\lfloor t\log h/c\rfloor>m_0$. The two residual
products $U_m=X/P^{cm}$ and $V_m=Y/Q^{cm}$ are positive rationals.
Their denominators divide

$$
Z_m=\prod_p p^{(A_pcm-b_pk_p)_+}.
$$

The integer Padé determinant argument, after multiplying by $Z_m$, gives
exactly as in the [two-prime proof](bft_rational_blocks.md)

$$1\le\frac{\kappa_1}{2}e^{\log Z_m-cmC}
       +\frac{Y}{2\kappa_2}e^{\log Z_m-cmK}.\tag{2}$$

This argument uses that $P,Q$ have disjoint prime supports; it does not
require them to be prime powers. The BFT determinant gives a nonzero
rational linear combination, whose product with $Z_m$ is a nonzero integer.

If every $u_p\le h^{e_p}$, then
$b_pk_p\log p\ge b_p(1-e_p)\log h$. Since $cm\le t\log h$,

$$
\log Z_m\le\Delta(t,e)\log h.
$$

Also $cm>t\log h-c$ and $Y\le(h+R)^\nu<2^\nu h^\nu$.
Thus the right side of (2) is at most

$$\frac{\kappa_1}{2}e^{cC}h^{-\sigma_1}
+\frac{2^{\nu-1}}{\kappa_2}e^{cK}h^{-\sigma_2}
\le A h^{-\min(\sigma_1,\sigma_2)}<1,$$

contradicting (2). $\square$

The proof includes $X=Y$: the determinant supplies nonvanishing, and the
term bounded by $D$ is then zero. Only the fixed Padé seed is required
to have a nonzero difference.

## The joint inequality and choice of block

For the balanced choice $t=\nu/J$, the two margins agree. In particular,
for every fixed $\epsilon>0$ and sufficiently large $h$, necessarily

$$\boxed{\sum_p\left(A_p\log p-
\frac{Jb_p}{\nu}(1-e_p)\right)_+>C-\epsilon,
\qquad e_p=\frac{\log u_p}{\log h}.}\tag{3}$$

If a cofactor exceeds $h$, its exponent is already too large to belong to
any of the upper boxes under consideration. Formula (3), interpreted with
the actual exponents, also follows directly without the upper restriction
$e_p\le1$.

One should not replace (3) with its rectangular endpoint alternatives when
checking an entire region of possible exponents. Several positive terms
can be relevant simultaneously. To exclude an upper box, the monotonicity
in each $e_p$ makes it enough to evaluate its upper corner. A finite
collection of such boxes may then cover a larger region.

The margins are continuous piecewise linear functions of $t$. Besides the
balanced value, useful block sizes occur at the denominator breakpoints

$$
t=\frac{b_p(1-e_p)}{A_p\log p}.
$$

The checker tries these finitely many choices. It approximates the selected
choice by a positive rational and recomputes both margins with directed
intervals. The proof uses only the verified margins for that rational;
it does not depend on a claim that the search found the best block.

## Numerical examples

For the AP $2r_3=r_2+r_7$ with distinct positions in $[0,13]$, the seed
$28-27=1$, $s=4/3$, $L_1=1.4170$, $m_0=153$ gives

$$u_2>h^{.45}\quad\text{or}\quad u_3>h^{.01}
\quad\text{or}\quad u_7>h^{.05}\qquad(h\ge10^{675}).$$

Here $h\le n-r_p\le h+13$ and the AP gap is at most $121$.
This excludes an upper box which extends past one of the previous
coordinatewise limiting targets from this seed.

For four distinct positions satisfying $r_3+r_5=r_2+r_{11}$, the seed
$45-44=1$, $s=3/2$, and the explicit Dusart gcd bound at $m_0=10^8$ give

$$u_2>h^{.2757}\quad\text{or}\quad u_3>h^{.3453}
\quad\text{or}\quad u_5>h^{.3931}\quad\text{or}\quad u_{11}>1
\qquad(h\ge10^{335538592}).$$

The final alternative is part of the displayed upper-box exclusion; it
is not a claim that $u_{11}$ is bounded in the binomial problem.
Other upper boxes can be passed to the same evaluator.

The [checker](../../computations/erdos_699_rational_product_bounds.py)
and [certificate](../../computations/erdos_699_rational_product_bounds.json)
record the positive margins and numerical thresholds. Product identities
and nonzero gap bounds remain explicit hypotheses of the evaluator.

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_rational_product_bounds.py
```

## Two additional asymmetric prime-pair estimates

The same lemma with $\nu=1$ gives useful alternatives missed by optimizing
only a symmetric maximum-cofactor exponent. For positive integer cofactors,
a nonzero difference at most $196$, and input height $h$ equal to the smaller
factor, the following implications hold:

| Pair | Alternative | Sufficient height |
| --- | --- | --- |
| $2,7$ | $u_2>h^{.348}$ or $u_7>h^{.085}$ | $h\ge10^{1114}$ |
| $2,11$ | $u_2>h^{.193}$ or $u_{11}>h^{.069}$ | $h\ge10^{2658}$ |

For general inputs in this table, use $R=196$ in (1); the logarithmic
$R$ term is smaller than the already certified threshold. In the binomial
applications the factor difference is at most $13$ and the checker directly
uses $R=13$.

The first seed is $49-3\cdot16=1$, with $s=7/4$, $L_1=1.6219$,
$m_0=60$. The second is $13\cdot512-5\cdot1331=1$, with $s=9/4$,
$L_1=1.7666$, $m_0=87$. Both coefficient-gcd bounds are retained entries
of BFT Proposition 5.1. The new feature is the asymmetric use of these
seeds, rather than a new estimate for their coefficient gcds.

The [pair checker](../../computations/erdos_699_asymmetric_pair_additions.py)
and [certificates](../../computations/erdos_699_asymmetric_pair_additions.json)
record exact seed factorizations, positive directed-interval margins,
and the numerical stopping thresholds for these implications.
