---
name: research/erdos_699/proofs/details/index_10_effective
title: "Erdős 699: index 10 is effective"
desc: "Position-dependent interpolation and constant-gap product identities prove that every bad row at index 10 is below 10^15000000."
created: 2026-09-22T05:27:34Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: index 10 is effective

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/methods/details/jet_nonvanishing|Interpolation nonvanishing]]

***

**Complete follow-up.** The [cutoff-15 proof](../../archive/previous_bounds/cutoff_15.md)
closes this numerical range: 43,985 certified intervals and two exact
rows exclude every bad triple at index ten. The tail argument below is an
input to that complete exclusion.

**Theorem.** Every bad triple with $i=10$ satisfies

$$
 n<10^{15\,000\,000}.
 \tag{1}
$$

The result uses 40 integer polynomial certificates. Their construction and
complete finite case division are retained in the
[checker](../../computations/erdos_699_index_10_effective.py) and
[certificate data](../../computations/erdos_699_index_10_effective.json).
The finite enumeration concerns small-prime positions and polynomial jets;
it does not enumerate rows $n$ or columns $j$.

The new step is to retain the actual positions of the largest powers of
$2,3,5,7$. A single polynomial for all assignments narrowly misses the
needed exponent. Most assignments admit substantially stronger polynomials,
and the few difficult assignments have additional arithmetic structure.

## 1. Cofactor witnesses and the exceptional assignments

Write $c=n-j$, $10<j\le c$, and choose $r_p\in\{0,\ldots,9\}$ maximizing
$v_p(n-r_p)$ for each $p\in\{2,3,5,7\}$. Put

$$
 P_p=p^{v_p(n-r_p)},\qquad u_p=(n-r_p)/P_p,\qquad h=n-9.
$$

Use the retained BFT symmetric and
[asymmetric pair estimates](../../methods/details/asymmetric_cofactors.md),
with the exponents weakened by $1/1000$ where indicated in the data. The
exact disjunctions have 16 componentwise minimal witnessing vectors
$v=(v_2,v_3,v_5,v_7)$: at least one satisfies $u_p\ge h^{v_p}$ for every
prime. The two troublesome vectors may both be weakened to

$$
 v_*=(.3286,.0492,.3921,0).
 \tag{2}
$$

Here and below these terminating decimals are exact rational numbers.
The other 14 vectors are covered by one certificate with decreasing row
multiplicities. Another such certificate covers every distinct-position
assignment whose position set differs from $\{0,1,2,3\}$.

Thus only the 24 permutations assigning (2) to the first four positions
require individual treatment. Eighteen have direct interpolation
certificates. The following six use additional cofactor disjunctions.
Positions in the first column are ordered as $(r_2,r_3,r_5,r_7)$.

| Positions | Identity | Additional alternative |
|---|---|---|
| $(3,0,2,1)$ | $r_2+r_3=r_5+r_7$ | $u_2\ge h^{.43}$ or $u_3\ge h^{.18}$ or $u_5\ge h^{.449}$ or $u_7\ge h^{.18}$ |
| $(2,0,3,1)$ | $r_2+r_3=2r_7$ | $u_2\ge h^{.428}$ or $u_3\ge h^{.13}$ or $u_7\ge h^{.198}$ |
| $(2,1,3,0)$ | $r_2+r_7=2r_3$ | $u_2\ge h^{.43}$ or $u_3\ge h^{.25}$ or $u_7\ge h^{.15}$ |
| $(3,1,2,0)$ | $r_5+r_7=2r_3$ | $u_3\ge h^{.30}$ or $u_5\ge h^{.60}$ or $u_7\ge h^{.065}$ |
| $(1,0,3,2)$, $(1,2,3,0)$ | $r_3+r_7=2r_2$ | $u_2\ge h^{.390}$ or $u_3\ge h^{.356}$ or $u_7\ge h^{.429}$ |

These are applications of the
[constant-gap cofactor estimates](../../methods/details/ap_cofactors.md),
using respectively the seeds $36-35$, $7-6$, $28-27$, $245-243$, and $64-63$.
For example, the first identity makes

$$
(n-r_2)(n-r_3)-(n-r_5)(n-r_7)
$$

a fixed nonzero integer. The other identities give the square of the AP
spacing. Composite-base Padé estimates can therefore be applied to these
quadratic products. Every branch of every displayed alternative has its
own certificate.

Repeated positions are covered by a single coordinate-line certificate.
If at least two primes occupy position $r$, the product of their maximal
prime powers divides $n-r$ and is at most $n$. This gives capacity one for
that whole group. A singleton prime has capacity $1-v_p$. This handles
coincidences without assuming that individual capacities add at a shared
position.

## 2. The polynomial inequalities

Each certificate specifies integer vectors $(h_a)_{a=0}^9$ and
$(m_t)_{t=0}^9$, and uses the nonvanishing factor

$$
 H(X,Y)=\prod_{a=0}^9((X-a)(Y-a))^{h_a}.
$$

At the Kummer point $(x,y)$, $x+y<10$, the remaining required multiplicity
is

$$
 R_{xy}=\max\{0,m_{x+y}-h_x-h_y\}.
$$

When all these multiplicities vanish, use $F=H$. Otherwise the certificate
gives a degree $d$ at which the symmetric jet map is surjective. Its full
row rank is checked over $\mathbf F_{251}$. The
[nonvanishing lemma](../../methods/details/jet_nonvanishing.md) supplies a
finite family of integer polynomials $G$ of degree at most $d+1$, having
these residual multiplicities, which cannot all vanish when $X+Y>9$.
At least one $F=HG$ is therefore nonzero at $(j,c)$.

Let $D$ be the degree bound for $F$, $M=\sum_t m_t$, and
$L=\sum_t t m_t$. At distinct selected positions, the gain is

$$
 \eta=M-D-\sum_{p<10}(1-v_p)m_{r_p}.
 \tag{3}
$$

For a repeated-position group, replace its contribution in the last sum
by $m_r$, as explained above. All gains in the retained case division
are strictly positive.

Let $Q_t$ be the part of $n-t$ supported on primes at least 10. Badness
and Taylor expansion give

$$
 \prod_{t=0}^9 Q_t^{m_t}\mid F(j,c).
$$

Since $10!$ has no prime at least 10, there is no rough denominator to
remove. Away from its selected position,
$v_p(n-t)\le v_p(t-r_p)$, so the total contribution of these small-prime
factors is at most $(9!)^{\max m_t}$. Also

$$
 \prod_t(1-t/n)^{m_t}\ge1-L/n,
 \qquad
 P_p\le n^{1-v_p}(n/(n-9))^{v_p}.
$$

For $n\ge1000(L+36\max m_t)$ the resulting product of correction factors
is at least $999/1000$. Thus

$$
 n^\eta\le\frac{1000}{999}\,\|F\|_1(9!)^{\max m_t}.
 \tag{4}
$$

## 3. Effective constants and exhaustive coverage

Suppose the symmetric jet matrix has $r$ rows. Each entry has absolute
value at most $2\cdot10^d$. A nonzero maximal minor and its adjugate give
the coefficient bound

$$
 C=r!(2\cdot10^d)^r<10^{r(d+6)}.
$$

In the usual symmetric Taylor basis, multiplication by $X+Y$ has column
sum at most 12. The resulting nonvanishing generators have coefficient
sum at most $28rC<10^7C$. Finally
$\|H\|_1\le10^{2\sum h_a}$ and $(9!)^{\max m_t}<10^{6\max m_t}$.
The checker consequently uses the conservative integer bound

$$
 E=r(d+6)+2\sum h_a+6\max m_t+9
 \tag{5}
$$

for the base-ten logarithm of the right side of (4). For a line-only
certificate take $r=0$. Every retained certificate satisfies
$15\,000\,000\,\eta>E$. The elementary row threshold preceding (4) is
below $10^{10}$ in every case.

The checker enumerates all $10^4$ labeled small-prime position assignments
and all 16 pair-witness vectors. For a conditional case it checks every
branch of the applicable additional alternative. It verifies the exact
rational gain, the constant comparison, and use of every retained
certificate. Thus (4) excludes all rows at or above the bound (1).

There are 28 nonempty jet matrices and 12 line-only certificates. The
largest jet matrix is $16899\times16900$; its degree is 258. Its algebraic
stopping exponent is less than $14\,465\,877$, and all the other
certificates have smaller exponents than the stated uniform bound.

The source thresholds are numerical as well. The
[prime-power calculation for the BFT gcd bounds](../../methods/details/bft_prime_bootstrap.md)
and the [numerical pair checker](../../computations/erdos_699_i10_numerical_pairs.py)
give the six pair alternatives needed here for $n\ge10^{996149}$.
The [product-threshold calculation](../../methods/details/product_thresholds.md)
gives every additional alternative in the table for
$n\ge10^{557368}$. Both are below the algebraic threshold in (1).
The index-10 checker compares its exact rational targets with these
retained numerical source records.

Thus (1) is a fully numerical stopping bound. Excluding the remaining
finite range is a separate step.
