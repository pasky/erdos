---
name: research/erdos_699/remaining/details/index_5_maximal_positions
title: "Erdős 699: effective confinement of the quintic maximal positions"
desc: "Beyond an effective threshold, a bad index-five row must place the maximal powers of two and three at n and n-1. Four unequal-block Padé constraints further restrict their cofactors."
created: 2026-09-22T07:10:00Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: effective confinement of the quintic maximal positions

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/remaining/details/indices_4_5_row_zero|The row-zero restriction]] ·
[[research/erdos_699/methods/details/off_diagonal_pade|Unequal-block Padé approximants]]

***

**Proposition.** There is an effectively computable integer $N_5$ such
that a bad triple $(n,5,j)$ with $n>N_5$ has

$$
\boxed{\{r_2,r_3\}=\{0,1\},}
$$

where $r_p$ maximizes $v_p(n-r)$ over $0\le r\le4$.
The bound $N_5$ is not numerically evaluated here. This eliminates the
other maximal-position patterns effectively; it does not make the entire
index effective.

The retained calculation uses four polynomial products and two exact
modular interpolation matrices. It covers all 30 cofactor-position cases
needed for the proposition, without enumerating binomial rows or columns.

## Four effective cofactor alternatives

Write

$$
n-r_2=2^a u,\qquad n-r_3=3^b v,\qquad h=n-4.
$$

For distinct positions, the difference of these two integers is nonzero
and at most four in absolute value. Applying the unequal-block construction
to the seed $9-8=1$ gives, above effective thresholds, all four alternatives

$$
\begin{array}{ll}
u>h^{.02}&\text{or }v>h^{.56},\\
u>h^{.05}&\text{or }v>h^{.52},\\
u>h^{.329}&\text{or }v>h^{.291},\\
u>h^{.55}&\text{or }v>h^{.025}.
\end{array}\tag{1}
$$

The Padé directions $(A,B,C)$, respectively, are

$$
(11,10,40),\quad(6,5,18),\quad(49,22,49),\quad(21,6,7).
$$

The [source checker](../../computations/erdos_699_two_three_off_diagonal.py)
and its [record](../../computations/erdos_699_two_three_off_diagonal.json)
use exact rational prime-interval sums truncated at $t=1000$ for each coefficient-gcd bound and
directed interval arithmetic for the analytic inequalities. Every exponent
has a certified margin greater than $10^{-4}$. The source starting indices
are effective, but unevaluated.

Thus at least one of the following lower cofactor witnesses holds, in prime
order $2,3$:

$$
(0,.56),\quad(.02,.52),\quad(.05,.291),\quad
(.329,.025),\quad(.55,0).\tag{2}
$$

A witness $(e_2,e_3)$ means $u\ge h^{e_2}$, $v\ge h^{e_3}$.
These are five alternatives for simultaneous lower bounds, not five exact
cofactor values.

## The polynomial products

Put $X=j$, $Y=n-j$, $s=X+Y=n$, and $t=XY$. Define

$$
\begin{aligned}
q_1&=s^2-3t-s,\\
q_2&=2s^2-3t-6s+4,\\
q_3&=s^2-t-3s+2.
\end{aligned}
$$

All three are positive on the admissible region when $n\ge12$: use

$$
q_1\ge n(n-4)/4,\quad
q_2\ge(5n^2-24n+16)/4,\quad
q_3\ge(3n^2-12n+8)/4.
$$

The following products have at least the listed multiplicities at every
nonnegative integer point on each row $X+Y=r$, $0\le r\le4$.

| Product | Polynomial | Row multiplicities $m_0,\ldots,m_4$ | Degree |
|---|---|---|---:|
| $A$ | $XY(X-1)(Y-1)q_2$ | $0,3,2,1,1$ | 6 |
| $B$ | $(XY)^2(X-1)(Y-1)q_1$ | $5,4,2,2,1$ | 8 |
| $C$ | $(XY)^6((X-1)(Y-1))^2(X-Y)^2$ | $14,8,6,0,2$ | 18 |
| $D$ | $(XY)^3((X-1)(Y-1))^2q_3$ | $0,6,4,3,0$ | 12 |

The only possible zero in the admissible region is the central column in
product $C$, and that column is always good. Indeed, if $n=2j$ and
$r\in\{1,3\}$, a prime $p\ge7$ dividing $n-r$ produces a carry
in $\binom nj$, because $j\bmod p=(p+r)/2>r$. The same is true
of $p=5$, which is active in $\binom n5$ whenever
$v_5(n-r)\ge2$. Thus badness would force both odd numbers $n-1,n-3$
to be of the form $3^a5^b$, with $b\le1$. Both numbers are at least
nine, so each would be divisible by three: the only three-free
possibilities are one and five. Their difference is two, a contradiction.

Suppose the distinct maximal positions are $0,r$, and let $e_0,e_r$
denote the cofactor witness at those positions. The exponent gain of a
degree-$d$ certificate with multiplicities $m_t$ is

$$
G=\sum_{t\ne0,r}m_t+e_0m_0+e_rm_r-d.\tag{3}
$$

If $G>0$, the weighted divisibility argument bounds $n^G$ by an
effective constant. Replacing $h=n-4$ by $n$ only introduces factors
$(n/(n-4))^{e_0m_0+e_rm_r}$, which are uniformly bounded for $n\ge12$.
Thus a positive gain gives an effective row bound.

For $r=4$, product $D$ has gain one without any cofactor estimate.
For $r=3$, use $C$ when $e_0\ge.291$, and $A$ otherwise; (1)
ensures $e_3\ge.291$ in the latter case. Their gains are respectively
$14e_0-2>0$ and $e_3>0$.

For $r=2$, products $A,B$ have gains $2e_2-1$ and
$5e_0+2e_2-1$. They cover eight of the ten possibilities obtained by
placing the five vectors (2) in either order at $0,2$. The two remaining
profiles are

$$
(e_0,e_2)=(.05,.291),\qquad(.025,.329).\tag{4}
$$

## The two interpolation certificates

For (4), first multiply by the coordinate-line product

$$
H(X,Y)=(XY)^{h_0}((X-1)(Y-1))^{h_1}.
$$

The residual multiplicity at $(x,y)$ is
$\max(0,m_{x+y}-h_x-h_y)$, with $h_2=h_3=h_4=0$.
The following exact data suffice.

| Profile at $0,2$ | $(h_0,h_1)$ | $(m_0,\ldots,m_4)$ | Jet interpolation degree | Matrix size | Total degree | Gain |
|---|---|---|---:|---|---:|---:|
| $(.05,.291)$ | $17,12$ | $37,58,25,29,23$ | 60 | $938\times961$ | 119 | $1/8$ |
| $(.025,.329)$ | $21,15$ | $46,76,34,38,31$ | 84 | $1799\times1849$ | 157 | $42/125$ |

Both symmetric jet matrices have full row rank modulo 251, hence over
the rationals. The [surjective-jet nonvanishing lemma](../../methods/details/jet_nonvanishing.md)
then supplies a finite family of residual polynomials of degree at most
61 or 85, one of which is nonzero at every physical pair with $n>4$.
Multiplying that polynomial by $H$ gives the total degrees in the table.
Their rational coefficients, and hence integer coefficient bounds after
clearing denominators, can be computed from the finite matrices. The two
strict positive gains therefore give effective row bounds.

The [position checker](../../computations/erdos_699_index_5_maximal_positions.py)
verifies the multiplicities, both modular ranks, and all 30 positive-gain
applications. Its [record](../../computations/erdos_699_index_5_maximal_positions.json)
contains the exact certificates and coverage. Run it with the retained
interpolation dependencies; `--arithmetic-only` omits repeating the ranks.

## Completing the confinement and the remaining region

The row-zero result says that a bad index-five row has $8\mid n$ or
$9\mid n$. In the first case $r_2=0$ uniquely; in the second
$r_3=0$ uniquely. Thus some maximal position is zero.
Coincident maxima are effectively excluded by

$$
2^a3^b>\frac{4^{6/5}}{240}n^{7/5},
$$

whereas $2^a3^b\le n$ when they occur at the same position.
The preceding certificates exclude every distinct pair $\{0,2\}$,
$\{0,3\}$, $\{0,4\}$, leaving precisely $\{0,1\}$ above an
effective threshold. This proves the proposition.

In the remaining patterns, (1) and (2) still apply. The same product
bound also gives the useful upper restriction

$$\boxed{uv<\frac{240}{4^{6/5}}n^{3/5}.}\tag{5}
$$

Together, the positions $\{0,1\}$, the four effective alternatives (1),
and (5) are necessary conditions for every sufficiently large bad quintic
triple. They do not contradict each other: intermediate cofactor sizes
remain. No complete quintic stopping bound is asserted.
