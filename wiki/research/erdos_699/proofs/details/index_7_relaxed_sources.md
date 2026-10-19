---
name: research/erdos_699/proofs/details/index_7_relaxed_sources
title: "Erdős 699: source margins for a numerical index-seven proof"
desc: "A slightly weaker set of cofactor inequalities still gives exact complete coverage at index seven, with polynomial height exponent 99990923."
created: 2026-09-22T16:55:22Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: source margins for a numerical index-seven proof

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/proofs/details/index_7_effective|The effective proof]] ·
[[research/erdos_699/proofs/details/index_7_polynomial_bounds|Sharper coefficient bounds]] ·
[[research/erdos_699/proofs/details/index_7_nonvanishing|Arithmetic nonvanishing]]

***

The saved rational source inequalities were rounded extremely close to
their limiting analytic boundaries. They can be weakened slightly while
preserving a complete exact proof. This gives room to use smaller
coefficient-gcd rates and more practical numerical starting indices.

The polynomial part of the modified proof holds for

$$
h=n-6\ge10^{99\,990\,923}. \tag{1}
$$

Numerical starting heights for the analytic sources must still be
included separately. The polynomial family and its verified modular
ranks are unchanged.

## The modified inequalities

Lower both endpoints of each of the five initial pair alternatives by
$1/10000$. They become

$$
(2,3):(.2920,.2920),\ (.3295,.2915),\qquad
(2,5):(.2675,.2710),\ (.2678,.2678),\qquad
(3,5):(.2561,.3773).
$$

In each of the $258$ joint inequalities

$$
\sum_p(g_p+w_pe_p)_+\ge R,
$$

keep every $g_p$ and $w_p$, and replace $R$ by $R-\eta$. Usually
$\eta=1/10000$; the five exceptions are

| Source ID | $\eta$ |
| --- | --- |
| `source_069` | $1/100000$ |
| `source_078` | $1/100000$ |
| `source_263` | $97863/10^9$ |
| `source_326` | $1/20000$ |
| `source_361` | $6367/10^9$ |

Every modified $R$ remains positive. For a fixed source block parameter
$t$, lowering its logarithmic gcd rate from $\ell$ to $\ell'$ changes
both analytic margins by $t(\ell'-\ell)$. Thus a choice satisfying

$$
\ell'\ge\ell-\frac{3\eta}{4t}
$$

retains an additional margin of at least $\eta/4$ in both terms of the
integer estimate. This observation guides the numerical source bounds;
the coverage argument itself uses only exact rational inequalities.

## Complete rational coverage

Uniformly subtracting $1/10000$ from the positive coordinates of the
old minimal witnessing vectors gives exactly the new minimal vectors.
The original position-zero restriction and collision certificate still
apply. Thus the same $540$ position-and-vector cases remain exhaustive.

For a polynomial certificate with coefficient exponent $E_F$, use its
actual finite-height inequality

$$\sum_p m_{r_p}e_p
\le D-\sum_{r\notin\{r_2,r_3,r_5\}}m_r+
\frac{E_F}{K},\qquad h\ge10^K.$$

At $K=10^8$, almost all old Farkas witnesses still apply. Ten additional
branches, using existing sources, complete the remaining cases. The
retained forest has $4336$ nodes, $948$ branches, and $3388$ leaves.
Every child of every branch is present, and every leaf has an exact
rational Farkas certificate.

For each leaf, let $\alpha$ be the negative weighted right side before
the polynomial errors $E_F/K$ are added, and put
$C=\sum_F\lambda_FE_F$. The leaf is impossible whenever
$K>C/\alpha$. The largest exact ratio is

$$
\frac{40482625000000}{404863}<99990923.
$$

This proves (1). The collision bound is smaller, and the separate
arithmetic nonvanishing certificate eliminates the former common-zero
height restriction.

The [checker](../../computations/erdos_699_index_7_relaxed_sources.py)
and [data](../../computations/erdos_699_index_7_relaxed_sources.json)
name the original proof and coefficient-bound files by basename. They check
the new minimal vectors, every source hypothesis, all exact Farkas
leaves, and the final weighted height. No new interpolation matrix or
binomial row is tested.

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_7_relaxed_sources.py
```
