---
name: research/erdos_699/methods/details/product_thresholds
title: "Erdős 699: numerical bounds for three and four cofactors"
desc: "A direct numerical threshold for the composite-base Padé argument, with explicit AP and equal-sum product certificates."
created: 2026-09-22T05:06:58Z
updated: 2026-09-22T05:06:58Z
---

# Erdős 699: numerical bounds for three and four cofactors

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/methods/details/ap_cofactors|AP and equal-sum cofactor bounds]]

***

The three- and four-factor estimates have fully numerical versions.
For selected factors among $n,n-1,\ldots,n-9$, the five conditional
constraints in the table below all apply once $n\ge10^{557368}$.
This is a common threshold for these **product constraints**; it is not
by itself a stopping bound for every bad triple at index ten. A full
index-ten argument must also instantiate the other prime-pair estimates
used in its interpolation certificates.

## 1. A numerical product lemma

Write selected numerator factors as

$$
f_p=n-r_p=p^{k_p}u_p,\qquad h\le f_p\le h+R,
$$

where the primes $p$ are distinct, $u_p$ are positive integers, and
$R\ge1$. Partition these primes into two nonempty sets $I_0,I_1$ and
choose positive integer multiplicities $b_p$ with

$$
\sum_{p\in I_0}b_p=\sum_{p\in I_1}b_p=\nu.
$$

Suppose the corresponding products have bounded difference:

$$0<\left|\prod_{p\in I_0}f_p^{b_p}
       -\prod_{p\in I_1}f_p^{b_p}\right|\le D.\tag{1}$$

Choose positive integers $A_p$ and a BFT seed

$$P=\prod_{p\in I_0}p^{A_p},\qquad
Q=\prod_{p\in I_1}p^{A_p},\qquad aP-bQ=D_0>0.$$

The symbols $b$ and $b_p$ have different roles: $b$ is the fixed seed
coefficient, while $b_p$ counts occurrences of a numerator factor.
Take any explicit BFT parameters $s=c/d,L_1,m_0$ for which the coefficient
gcd estimate holds and $\Omega_3,\Omega_4>1$. Use the constants
$\kappa_1,\kappa_2$ from BFT Theorem 2.4 for the gap $D$.

For target exponents $0<t_p<1$, put

$$
K=\log\max(P,Q)+\frac{\log\Omega_4}{s},
$$

$$L=\max_p\frac{A_p\log p}{b_p(1-t_p)},\qquad
M=\max\left\{m_0,\frac{\log\kappa_1}{d\log\Omega_3}\right\}.$$

Assume $\nu L<K$. Define

$$H=\max\left\{
 \log R,\ cL(M+1),\
 \frac{L}{K-\nu L}
 \bigl(cK+\nu\log2-\log\kappa_2\bigr)
\right\}.\tag{2}$$

Then

$$\boxed{\log h>H\quad\Longrightarrow\quad
 u_p>h^{t_p}\text{ for at least one }p.}\tag{3}$$

**Proof.** If every $u_p\le h^{t_p}$, then
$p^{k_p}\ge h^{1-t_p}$. Match the seed blocks by choosing

$$m=\min_p\left\lfloor\frac{b_pk_p}{cA_p}\right\rfloor
 >\frac{\log h}{cL}-1>M.$$

Each product in (1) is respectively $P^{cm}U$ or $Q^{cm}V$, with
positive integral residual cofactors. The absolute-gap integer Padé
argument in BFT Section 7, before its final cofactor maximum, gives

$$
Q^{cm}V>\kappa_2\exp(cmK).\tag{4}
$$

This is the same step used in the
[asymmetric two-factor lemma](asymmetric_cofactors.md).
It uses the common block $m$ and does not require each residual cofactor
to be a power of one original cofactor.

On the other hand, $h>R$ implies
$Q^{cm}V\le(h+R)^\nu<2^\nu h^\nu$. Therefore

$$\left(\frac K L-\nu\right)\log h
 <cK+\nu\log2-\log\kappa_2,$$

contradicting (2). This proves (3).

The limiting target at the coordinate $p$ is

$$
1-\frac{\nu A_p\log p}{b_pK}.
$$

For an AP identity, the middle factor has multiplicity two and both
endpoint factors have multiplicity one. For the equal-sum identity,
all four multiplicities are one. Either product may correspond to the
larger seed; the absolute-gap argument handles both orientations.

## 2. Numerical certificates for the index-ten range

Put $h=n-9$, so $R=9$, and use $D=100$. The following table lists
conditional alternatives: at least one of the listed cofactor
inequalities holds whenever the condition on the positions is satisfied.

| Position condition | Cofactor targets | Sufficient height |
| --- | --- | --- |
| $2r_3=r_2+r_7$ | $u_2>h^{.43}$ or $u_3>h^{.25}$ or $u_7>h^{.15}$ | $h\ge10^{651}$ |
| $2r_3=r_5+r_7$ | $u_3>h^{.30}$ or $u_5>h^{.60}$ or $u_7>h^{.065}$ | $h\ge10^{1558}$ |
| $2r_2=r_3+r_7$ | $u_2>h^{.390}$ or $u_3>h^{.356}$ or $u_7>h^{.429}$ | $h\ge10^{860}$ |
| $2r_7=r_2+r_3$ | $u_2>h^{.428}$ or $u_3>h^{.13}$ or $u_7>h^{.198}$ | $h\ge10^{329051}$ |
| $r_2+r_3=r_5+r_7$ | $u_2>h^{.43}$ or $u_3>h^{.18}$ or $u_5>h^{.449}$ or $u_7>h^{.18}$ | $h\ge10^{557367}$ |

The AP conditions are used with distinct positions, giving a square minus
a product equal to a nonzero fixed squared gap. The last condition is used
with four distinct positions and gives

$$
(n-r_2)(n-r_3)-(n-r_5)(n-r_7)=r_2r_3-r_5r_7.
$$

With all positions in $[0,9]$, these gaps are at most $100$.
The source parameters are:

| Seed | $c/d$ | $L_1$ | $m_0$ |
| --- | --- | --- | ---: |
| $28-27=1$ | $4/3$ | $1.4170$ | $153$ |
| $245-243=2$ | $5/4$ | $1.3098$ | $50$ |
| $64-63=1$ | $9/7$ | $1.3317$ | $15$ |
| $7-6=1$ | $3/2$ | $\exp(22630898059/50000000000)$ | $200000$ |
| $36-35=1$ | $124/95$ | $\exp(300161803779/10^{12})$ | $3000$ |

The first three gcd estimates are BFT Proposition 5.1 entries. The $7-6$
entry uses the [Dusart refinement of the gcd bound](dusart_gcd_bounds.md).
The last
uses the [explicit prime-interval gcd lemma](bft_numerical_thresholds.md)
with $T=1500$. It is a finite rational certificate valid for every
$m\ge3000$, not a check of finitely many Padé degrees.

All five entries are evaluated by the
[direct product-threshold checker](../../computations/erdos_699_product_thresholds.py).
Its [recorded output](../../computations/erdos_699_product_thresholds.json)
contains the prime components of each seed, multiplicities, exact gcd
certificate, directed intervals for (2), and the verified integer powers
of ten. A floating approximation proposes each integer exponent; the
final inequality $H<B\log10$ is checked with directed intervals.

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_product_thresholds.py
```

## 3. Numerical pair inputs for the same index

The near-limiting pair constraints used alongside these product bounds
also have evaluated thresholds. The
[finite prime-interval bootstrap](bft_prime_bootstrap.md)
reduces the valid coefficient-gcd starting values while preserving their
exact lower exponents. Re-evaluating the direct asymmetric threshold gives:

| Pair | Two alternative cofactor exponents | Input height at least |
| --- | --- | --- |
| $2,3$ | $(.3286,.2911)$ | $10^{497522}$ |
| $2,5$ | $(.2669,.2701)$ | $10^{718704}$ |
| $2,7$ | $(.2747,.3208)$ | $10^{575027}$ |
| $3,5$ | $(.2552,.3764)$ | $10^{996148}$ |
| $3,7$ | $(.0495,.3261)$ | $10^{918924}$ |
| $5,7$ | $(.3921,.2657)$ | $10^{197514}$ |

The input height is the minimum of the two selected factors, and the gap
bound is $100$. Each table entry is an asymmetric disjunction. Its two
endpoints dominate both the symmetric and asymmetric source requirements
after the indicated weakening by $.001$ in the index-ten construction.

The [pair-threshold checker](../../computations/erdos_699_i10_numerical_pairs.py)
regenerates the analytic tails, matches their exact exponents to the
retained finite bootstrap, and then evaluates the smaller numerical
thresholds. Its [output](../../computations/erdos_699_i10_numerical_pairs.json)
records all six certificates. Hence every pair constraint in this table
and every product constraint above applies whenever

$$
n\ge10^{996149}.
$$

This is the common evaluated source threshold; the interpolation argument
has its own algebraic cutoff.

## 4. A conditional constraint relevant to index fourteen

The same construction gives another useful source estimate. Suppose the
four distinct selected positions for $2,3,11,13$ lie in $[0,13]$ and
satisfy

$$
r_2+r_3=r_{11}+r_{13}.
$$

Use the seed

$$
144-143=1,\qquad144=2^4\cdot3^2,\qquad143=11\cdot13,
$$

with $s=115/94$ and the exact Dusart coefficient-gcd bound at $m_0=10^8$.
The [checker](../../computations/erdos_699_fourteen_product_sources.py)
and its [certificate](../../computations/erdos_699_fourteen_product_sources.json)
prove that, for $h=n-13\ge10^{21602776816}$,

$$u_2>h^{.359}\quad\text{or}\quad
u_3>h^{.492}\quad\text{or}\quad
u_{11}>h^{.445}\quad\text{or}\quad u_{13}>h^{.407}.$$

The equal-sum product gap is nonzero and at most $42$, so the checked
bound $D=100$ applies. This is a conditional restriction on labeled
positions. It does not establish a whole-index result at fourteen;
other position patterns and every branch of the disjunction still
require coverage.
