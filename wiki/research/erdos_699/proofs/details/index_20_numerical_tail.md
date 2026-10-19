---
name: research/erdos_699/proofs/details/index_20_numerical_tail
title: "Erdős 699: a fully numerical stopping bound at index 20"
desc: "Twelve explicit cofactor estimates and a surjective degree-118 interpolation map prove n < 10^27027659 for every bad triple with i=20."
created: 2026-09-22T05:19:42Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: a fully numerical stopping bound at index 20

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/methods/details/jet_nonvanishing|Interpolation nonvanishing]]

***

Every bad triple with $i=20$ satisfies the fully numerical bound


$$
\boxed{n<10^{27027659}.}
$$


Every source threshold used in this proof has been numerically
instantiated. The bound holds for all assignments and collisions of the
small-prime maximum positions, and there is no remaining exceptional
curve. Excluding the rows below this endpoint is a separate finite
verification.

## Twelve numerical cofactor estimates

For positive integers $u,v$, nonnegative exponents $a,b$, and
$|p^a u-q^b v|\le100$, put $x=\min(p^a u,q^b v)$. Each row of the table
gives


$$
u>x^{\alpha_p}\quad\text{or}\quad v>x^{\alpha_q}
\qquad(x\ge10^K).
$$


| Pair | $\alpha_p$ | $\alpha_q$ | $K$ | Coefficient-gcd input |
| --- | ---: | ---: | ---: | --- |
| $2,11$ | .1197 | .1879 | 785060 | Published |
| $3,5$ | .2412 | .3648 | 211993 | Published |
| $5,13$ | .1638 | .3337 | 146201 | Published |
| $7,13$ | .0987 | .2080 | 484367 | Published |
| $3,19$ | .1162 | .2104 | 268440 | Published |
| $7,19$ | .4299 | .1374 | 601485 | Published |
| $3,11$ | .3414 | .4249 | 12315735 | Explicit bound with $m_0=100000$ |
| $5,7$ | .3869 | .2589 | 16877043 | Explicit bound with $m_0=100000$ |
| $5,11$ | .2051 | .2105 | 13982107 | Explicit bound with $m_0=100000$ |
| $11,13$ | .1260 | .0652 | 8222386 | Explicit bound with $m_0=100000$ |
| $2,17$ | .3643 | .3505 | 12692980 | Explicit bound with $m_0=100000$ |
| $17,19$ | .2442 | .2146 | 27027658 | Explicit bound with $m_0=100000$ |

The first six are retained in the
[asymmetric pair table](../../computations/erdos_699_bft_asymmetric_pair_table.json).
The last six are certified by the
[numerical parameter checker](../../computations/erdos_699_interpolation_numeric_pairs.py)
and its [recorded bounds](../../computations/erdos_699_interpolation_numeric_pairs.json).
They use a finite, explicit coefficient-gcd lower bound and the
[asymmetric BFT threshold formula](../../methods/details/asymmetric_cofactors.md).
No effective-but-unevaluated threshold is invoked.

For each prime $p<20$, select $r_p\in\{0,\ldots,19\}$ maximizing
$v_p(n-r_p)$, and write $n-r_p=P_pu_p$. Set
$e_p=\log u_p/\log(n-19)$.
The table supplies the indicated disjunctions for the $e_p$ once
$n\ge10^{27027659}$, because every relevant smaller input is at least
$n-19>10^{27027658}$.

Choosing an endpoint witnessing each disjunction and removing dominated
vectors leaves **60** componentwise minimal vectors $v$, with some
$v\le e$ for every feasible $e$. A singleton maximum has exponent
capacity $1-v_p$; a position shared by at least two primes has capacity
$1$. The collision-capacity construction from the
[weighted certificate](../../archive/previous_bounds/interpolation_extensions.md)
covers every possible grouping. Monotone row weights let rearrangement
place the largest capacities at the earliest positions.

## A surjective interpolation system

Use the integer vectors


$$
\begin{aligned}
h={}&(32,30,28,26,24,21,19,16,12,8,4,0,0,0,0,0,0,0,0,0),\\
m={}&(64,63,63,63,61,59,57,56,56,54,50,46,42,39,37,34,32,30,28,26).
\end{aligned}
$$


The vector $m$ is nonincreasing. On the grid $x,y\ge0$, $x+y<20$,
prescribe residual multiplicities


$$
R_{xy}=\max\{0,m_{x+y}-h_x-h_y\}.
$$


There are 3599 independent symmetric jet conditions. More precisely,
the integer jet matrix on the 3600 symmetric monomials through degree
$D=118$ has rank **3599 modulo 65521**, as checked exactly. It therefore
has full row rank over $\mathbb Q$.

The [nonvanishing lemma](../../methods/details/jet_nonvanishing.md) supplies
integer polynomials of degree at most $119$ with these prescribed
residual multiplicities and no common zero when $X+Y>19$.
Multiplication by


$$
H(X,Y)=\prod_{a=0}^{19}((X-a)(Y-a))^{h_a}
$$


raises their multiplicities to at least $m_t$ on every Kummer row $t$.
Here $\deg H=440$, so the resulting degree bound is $559$.
The factor $H$ is positive throughout $20<j\le c$.

Exact enumeration of the **8001** collision-capacity configurations
gives the uniform gain


$$
\boxed{\sum_t m_t-\sum_a m_a c_a-559\ge\frac{319}{1250}>0.}
$$


One worst vector, in prime order $(2,3,5,7,11,13,17,19)$, is


$$
(3643,3414,2051,2589,0,652,0,2146)/10000,
$$


with sorted capacities


$$
(10000,10000,9348,7949,7854,7411,6586,6357)/10000.
$$


## The numerical endpoint

The cofactor-minor estimate in the
[general interpolation proof](../../archive/previous_bounds/interpolation_extensions.md)
applies with


$$
r=3599,\quad D=118,\quad m_0=64,\quad \sum h_a=220.
$$


It bounds the complete divisibility constant by $10^E$, where


$$
\begin{aligned}
E&=r(6+2D)+1+8m_0+2\cdot19m_0+4\sum h_a+7\\
 &=874790.
\end{aligned}
$$


For completeness, the rational interpolation sections can be cleared
using cofactors of a full-rank minor, whose coefficients are bounded by
$r!(2\cdot20^{118})^r$.
The multiplier for the nonvanishing generators is bounded by
$1+(210+24)\binom{120}{2}=1670761<10^7$.
These are the inputs to the displayed elementary power-of-ten bound.

Consequently every bad row beyond the source thresholds satisfies


$$
n^{319/1250}<10^{874790}.
$$


Since
$4000000\cdot319/1250=1020800>874790$, the algebraic argument excludes
$n\ge10^{4000000}$ whenever the source estimates hold. All twelve
source estimates certainly hold for $n\ge10^{27027659}$, proving the
stated bound.

The [checker](../../computations/erdos_699_index_20_numerical_tail.py)
and [certificate](../../computations/erdos_699_index_20_numerical_tail.json)
retain the twelve source references, integer interpolation data, exact
gain, modular rank, and final exponent comparison. Run the checker with
the
[pinned dependencies](../../evidence/assets/erdos_699_interpolation_requirements.txt)
installed in the repository's `.venv/`:

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_20_numerical_tail.py
```

Only finite cofactor vectors, collision patterns, and a fixed polynomial
jet matrix are enumerated; no binomial rows are scanned.
