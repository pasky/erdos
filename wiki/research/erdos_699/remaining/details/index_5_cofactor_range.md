---
name: research/erdos_699/remaining/details/index_5_cofactor_range
title: "Erdős 699: effective power bounds for both quintic cofactors"
desc: "Beyond an effective threshold, both cofactors in a bad index-five row lie strictly between (n-4)^(1/100) and (n-4)^(57/100). The maximal positions are already confined to zero and one."
created: 2026-09-22T08:00:00Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: effective power bounds for both quintic cofactors

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/remaining/details/index_5_maximal_positions|The maximal-position confinement]] ·
[[research/erdos_699/methods/details/off_diagonal_pade|Unequal-block Padé approximants]]

***

**Proposition.** Beyond an effectively computable threshold, a bad triple
at index five satisfies

$$
n-r_2=2^a u,\qquad n-r_3=3^b v,\qquad
\{r_2,r_3\}=\{0,1\},\qquad
\boxed{(n-4)^{1/100}<u,v<(n-4)^{57/100}.}
\tag{1}
$$

The cofactors are those obtained by removing the maximal powers of two
and three from their respective numerator factors. The threshold is not
numerically evaluated. This excludes every family in which either cofactor
is at most a fixed hundredth power of the row, with the harmless shift in
(1). It does not make the whole index effective.

Unlike the earlier consequence of Yu's theorem, the lower exponent here
is a fixed positive constant. The additional input is the quintic
polynomial argument, which first gives an effective upper bound for
*each* cofactor.

## An effective upper bound at either position

Put $h=n-4$. The previous confinement theorem leaves only the two maximal
positions zero and one. Suppose that the cofactor at one of those positions
is at least $h^{57/100}$.

If that position is zero, use

$$
F(X,Y)=(XY)^3((X-1)(Y-1))^2(X-2)(Y-2).
$$

It has degree 12 and row multiplicities $(6,5,4,3,2)$ on the quintic
Kummer grid. The gain in the weighted divisor inequality is

$$
6\cdot\frac{57}{100}+4+3+2-12=\frac{21}{50}>0.
$$

The product is nonzero for $X=j>5$ and $Y=n-j>5$. Thus this case has an
effective row bound.

For a cofactor of size at least $h^{57/100}$ at position one, use the
following symmetric interpolation data:

$$
\begin{aligned}
(h_0,h_1,h_2,h_3,h_4)&=(101,76,27,0,0),\\
(m_0,m_1,m_2,m_3,m_4)&=(0,223,190,142,114),\\
D&=164.
\end{aligned}
$$

Here $\prod_{k=0}^4((X-k)(Y-k))^{h_k}$ is the initial positive product.
The residual multiplicity at $(x,y)$ is
$\max(0,m_{x+y}-h_x-h_y)$.
The symmetric jet matrix of degree at most 164 has size
$6817\times6889$ and full row rank modulo 251.
The surjective-jet nonvanishing lemma therefore gives a finite residual
family of degree at most 165, with a nonzero member at each physical
pair. After restoring the initial product, its total degree is

$$
2(101+76+27)+165=573.
$$

The gain is

$$
\frac{57}{100}\,223+190+142+114-573=\frac{11}{100}>0.
$$

All coefficients can be computed rationally from the finite matrix, so
the corresponding row bound is effective. Replacing $h$ by $n$ in the
exponent comparisons introduces only bounded factors of $n/(n-4)$.
Consequently, sufficiently large bad triples have both $u,v<h^{57/100}$.

## Turning the upper bound into a lower bound

Two further applications of the seed $9-8=1$ give the effective alternatives

$$
\begin{aligned}
u>h^{1/100}&\quad\text{or}\quad v>h^{57/100},\\
u>h^{23/40}&\quad\text{or}\quad v>h^{1/100}.
\end{aligned}\tag{2}
$$

Their Padé directions and coefficient-gcd rates are

| $(A,B,C)$ | Chosen logarithmic gcd rate | Targets in prime order $2,3$ |
|---|---|---|
| $(13,12,49)$ | $3597/625$ | $(.01,.57)$ |
| $(33,9,10)$ | $43743/10000$ | $(.575,.01)$ |

In each case the exact prime-interval sum truncated at $t=1000$ exceeds
the chosen gcd rate. Directed interval arithmetic gives a margin greater
than $10^{-4}$ for both targets. The general unequal-block construction
makes the starting indices effective.

The first alternative in (2), together with $v<h^{57/100}$, forces
$u>h^{1/100}$. The second, together with
$u<h^{57/100}<h^{23/40}$, forces $v>h^{1/100}$. This proves (1).

## Certificate and remaining restriction

The [checker](../../computations/erdos_699_index_5_cofactor_range.py)
verifies the source inequalities, the elementary product, and the full
modular rank. Its [record](../../computations/erdos_699_index_5_cofactor_range.json)
contains the exact data. The --arithmetic-only option rechecks the
inequalities without repeating the matrix rank.

The earlier upper product bound remains

$$
uv<\frac{240}{4^{6/5}}n^{3/5},
$$

and all four cofactor alternatives in the maximal-position note still
hold. Intermediate cofactor sizes satisfy these necessary conditions,
so a complete quintic stopping bound has not been obtained.
