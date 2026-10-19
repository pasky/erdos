---
name: research/erdos_699/archive/other_approaches/polynomial_factor_limits
title: "Erdős 699: limits of adding polynomial factors"
desc: "Exact rational certificates show that adding factors of arbitrary degree cannot repair the usual residual dimension criterion for three remaining cofactor profiles."
created: 2026-09-22T06:11:49Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: limits of adding polynomial factors

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]]

For three remaining cofactor profiles, adding more polynomial factors cannot
make the usual asymptotic dimension count sufficient. This statement includes
factors of arbitrary degree, not just lines or conics. It identifies where new
arithmetic information is needed; it neither supplies bad triples nor rules
out other interpolation arguments.

The profiles are listed in increasing prime order. A coordinate $e_p$ at
position $r_p$ gives the row capacity $\alpha_{r_p}=e_p$; all other row
capacities are 1.

| $i$ | Prime positions $(r_p)$ | Cofactor exponents $(e_p)$ | Lower bound for normalized residual square sum |
|---|---|---|---:|
| 7 | $(2,1,0)$ | $(.2679,.2921,0)$ | $1.2104947700$ |
| 9 | $(1,3,0,2)$ | $(.2757,.2921,0,.2667)$ | $1.2011790174$ |
| 14 | $(2,5,3,4,1,0)$ | $(.1399,.3453,.2711,.3218,0,.0729)$ | $1.1311429951$ |

These statements concern the displayed profiles. Stronger cofactor inequalities
or an argument excluding the corresponding position assignment can remove a
profile from consideration.

## A weighted Bezout lemma

Let

$$
T_i=\{(x,y)\in\mathbf Z_{\ge0}^2:x+y<i\}.
$$

Suppose nonnegative rational point weights $\lambda_P$ satisfy

$$
\sum_{P=(x,y),\ x+y=t}\lambda_P=\alpha_t,
$$

and every affine line contains point weight at most 1. Suppose also that
there are affine lines $L_j$ and nonnegative rational weights $w_j$ such that

$$\lambda_P\le\sum_{j:P\in L_j}w_j,
\qquad \sum_jw_j\le1.$$

Then every nonzero polynomial $F\in\mathbf Q[X,Y]$ satisfies

$$\boxed{\sum_{P\in T_i}\lambda_P\operatorname{ord}_P(F)
\le\deg F.}$$

To prove this, first remove every affine-line component of $F$. Such a
component already satisfies the assertion by the line-weight hypothesis.
For the remaining polynomial $G$, no covering line $L_j$ is a component,
so Bezout gives

$$
\sum_{P\in L_j\cap T_i}\operatorname{ord}_P(G)\le\deg G.
$$

Multiply by $w_j$, sum, and use the pointwise covering inequality. Add back
the removed line components. The argument applies without a symmetry
assumption on $F$.

## Consequence for prescribed factors and residual jets

Allow any collection of factors $F_k$, with nonnegative normalized powers
$c_k$, and prescribed row multiplicities $m_t$. Let $\rho_P\ge0$ be residual
jet multiplicities satisfying

$$m_{x+y}\le\rho_P+
\sum_kc_k\operatorname{ord}_P(F_k).$$

If the remaining degree is normalized to 1, the arithmetic gain needed for
the usual interpolation argument is

$$
\sum_t\alpha_tm_t-\sum_kc_k\deg F_k\ge1.
$$

The lemma implies $\sum_P\lambda_P\rho_P\ge1$. Therefore

$$\boxed{\sum_P\rho_P^2\ge
\frac1{\sum_P\lambda_P^2}.}$$

For each profile above, the denominator is strictly below 1. Thus no choice
of factors, factor degrees, or real multiplicities can give the sufficient
asymptotic dimension inequality $\sum_P\rho_P^2<1$ for that profile. This does
not exclude a construction using extra dependencies among jet conditions,
another polynomial existence theorem, or additional arithmetic constraints.

## Exact certificates

The [rational certificate data](../../computations/erdos_699_polynomial_factor_barriers.json)
record all point weights and line covers. Their squared norms and cover
weights are respectively

| $i$ | $\sum_P\lambda_P^2$ | $\sum_jw_j$ |
|---|---:|---:|
| 7 | $.8261084845238095\ldots$ | $.88470977$ |
| 9 | $.8325153748493235\ldots$ | $.91593478$ |
| 14 | $.8840615238730434\ldots$ | $.93793889$ |

The [standalone checker](../../computations/erdos_699_polynomial_factor_barriers.py)
uses rational arithmetic only. It checks the row sums, every line through
two grid points, every pointwise covering inequality, and both strict bounds.
Lines containing at most one grid point automatically have weight at most 1,
since each row sum is at most 1. Run it with

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_polynomial_factor_barriers.py
```

The exploratory search leading to this lemma considered symmetric cubics
through five off-diagonal point orbits, cubics singular at a diagonal point,
and divided differences $(f(X)-f(Y))/(X-Y)$ for polynomials $f$ with distinct
integer roots in $[0,i-1]$. Those searches are unnecessary for verifying the
result: the rational line covers handle every polynomial degree at once.
The analogous cover feasibility calculation did not produce such a
certificate for the tested residual index-12 profile; no conclusion about
that profile follows from this note.
