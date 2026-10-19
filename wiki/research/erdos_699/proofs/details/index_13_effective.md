---
name: research/erdos_699/proofs/details/index_13_effective
title: "Erdős 699: an explicit bound at index 13"
desc: "A surjective finite interpolation system and asymmetric prime-pair estimates prove n<10^56000 for every bad triple with i=13."
created: 2026-09-22T04:06:03Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: an explicit bound at index 13

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/methods/details/jet_nonvanishing|Surjective interpolation lemma]]

***

**Complete exclusion.** A subsequent
[asymmetric bound and interval proof](further_interval_certificates.md) excludes
every bad triple with $i=13$. The interpolation construction below remains
useful in the proofs for indices $15,20$.

**Every bad triple with $i=13$ satisfies $n<10^{56000}$.** The bound uses
the original threshold $p\ge13$. It covers all assignments of the
small-prime maxima, including coinciding positions.

The proof combines an exact finite-field rank calculation with a
position-sensitive polynomial argument. No binomial rows are enumerated.
The earlier interpolation construction applied to one position pattern;
the nonincreasing row multiplicities below allow rearrangement to handle
every pattern, while surjectivity supplies nonvanishing throughout the
physical region.

## 1. The finite interpolation system

Use coordinate-line exponents and row multiplicities

$$
 h=(57,54,45,39,32,24,13,3,0,0,0,0,0),
$$
$$
 m=(114,111,111,103,99,99,89,78,70,63,57,51,46).
$$

At each integer point $x,y\ge0$, $x+y\le12$, require residual
multiplicity

$$
R_{xy}=\max\{0,m_{x+y}-h_x-h_y\}.
$$

The symmetric jet map on polynomials of total degree at most 106 has
2911 rows and 2916 columns. Its rank over $\mathbb F_{65521}$ is exactly
2911. This proves surjectivity over $\mathbb Q$.
The [exact rank checker](../../computations/erdos_699_index_13_interpolation_gcd.py)
and [retained certificate](../../computations/erdos_699_index_13_interpolation_gcd.json)
give the matrix conventions and verification. Its additional polynomial
gcd calculation is not required for the present proof.

The [surjective interpolation lemma](../../methods/details/jet_nonvanishing.md)
now supplies finitely many integer polynomials $G_a$ of degree at most
107, all having the residual multiplicities, that cannot vanish
simultaneously when $X+Y>12$. Put

$$
H(X,Y)=\prod_{a=0}^{12}((X-a)(Y-a))^{h_a},\qquad F_a=HG_a.
$$

Then $\deg H=534$, $\deg F_a\le641$, and every $F_a$ has multiplicity
at least $m_t$ at each Kummer point on $x+y=t$. In the admissible region
$13<j\le n-j$, the factor $H(j,n-j)$ is positive. Hence at least one
$F_a(j,n-j)$ is nonzero at every admissible pair.

## 2. Every position assignment has a positive gain

For $p\in\{2,3,5,7,11\}$, choose a position $r_p$ maximizing
$v_p(n-r_p)$, and write $n-r_p=P_pu_p$ as before. Use the original,
fully explicit BFT Theorem 2.1 table, together with the certified
asymmetric estimate

$$
u_5\ge(n-12)^{.35}\quad\text{or}\quad u_7\ge(n-12)^{.22}. \tag{1}
$$

The [asymmetric source calculation](../../methods/details/asymmetric_cofactors.md)
proves (1) when the smaller numerator factor is at least $10^{1731}$.
The other pair estimates hold beyond the much smaller published
threshold. In particular, every source estimate applies for
$n\ge10^{1732}$.

The finite maximum/disjunction system has 18 componentwise minimal
cofactor vectors $v$, one of which satisfies
$u_p\ge(n-12)^{v_p}$ for every small prime. Its coordinates are less
than $1/2$.

A singleton maximal position has exponent capacity $1-v_p$; a position
occupied by two or more primes has capacity one. As proved in the
[weighted-certificate note](../../methods/details/weighted_ramps.md), choose
the singleton subset and give the other primes as many paired positions
as possible. This finite set of capacity lists includes every collision
pattern. Because $m_t$ is nonincreasing, the worst assignment places the
largest capacities at the smallest positions.

Writing such a list as $c_0\ge\cdots\ge c_{g-1}$, the exact minimum is

$$
 \boxed{\min_{v,\,\text{collision patterns}}
 \left(\sum_{t=0}^{12}m_t-\sum_{r=0}^{g-1}m_rc_r-641\right)
 =\frac{1287}{200}=6.435.}                                \tag{2}
$$

A minimizing vector in prime order $2,3,5,7,11$ is
$(0,.329,.258,.259,.059)$, with all positions distinct. The
[arithmetic checker](../../computations/erdos_699_index_13_effective.py)
verifies (2) using rational arithmetic and all 18 vectors. No selection
of a favorable position pattern is made.

The collision argument extends unchanged from linear weights to the
present nonincreasing sequence. Inserting a capacity one before a
decreasing list increases its weighted contribution by at least the last
new weight: for $0\le c_r\le1$,

$$
m_0-\sum_{r=0}^{g-1}(m_r-m_{r+1})c_r\ge m_g\ge0.
$$

## 3. A coefficient bound without computing rational interpolants

Let $r=2911$, $D=106$, and put

$$
C=r!\,(2\cdot13^{106})^r.
$$

Every entry of the integer symmetric jet matrix has magnitude at most
$2\cdot13^{106}$. Choose a nonsingular maximal minor with determinant
$\Delta$. Adjugates give integer polynomials $q_j$ of degree at most 106
whose jets are $\Delta$ times the coordinate vectors, with

$$
|\Delta|\le C,\qquad \|q_j\|_1<6000C.
$$

In the invariant Taylor-coordinate basis, multiplication by $X+Y$ has
column norm at most 15; use the convenient bound 20. The construction in
the surjectivity lemma can therefore take the integer generators

$$
 \Delta-\sum_j a_jq_j,\qquad
 (X+Y)q_j-\sum_k T_{kj}q_k,
$$

where $a$ is the jet vector of 1 and $T$ is the multiplication matrix.
There are at most 49 nonzero entries of $a$, each equal to one. Hence all
these generators have coefficient norm less than $10^6C$.

The elementary exact comparisons

$$
2911^2<10^7,\qquad2^{500}<10^{151},\qquad13^{200}<10^{223}
$$

give

$$
C<10^{355119},\qquad \|H\|_1\le13^{534}<10^{596}.
$$

Consequently every resulting $F_a$ satisfies

$$
\|F_a\|_1<10^{355721}.                                  \tag{3}
$$

## 4. The stopping bound

Let $W=\max m_t=114$ and $L=\sum t m_t$. The weighted divisibility
argument, retaining the maximum-position constants as in the weighted
note, gives for each nonzero evaluation

$$
 n^{1287/200}\le\frac{1000}{999}\,
        13^{114}C_*\|F_a\|_1,\qquad
 C_*\le(12!)^{114},                                      \tag{4}
$$

provided
$n\ge1000(L+114\cdot5\cdot12)$ and the source estimates apply.
The factor $13^{114}$ accounts for the rough denominator prime in $13!$.
The elementary threshold is below $10^8$.

Using $13^{114}<10^{128}$, $12!<10^9$, and (3), the right side of (4)
is less than $10^{356876}$. But

$$
56000\cdot\frac{1287}{200}=360360>356876.
$$

Thus $n\ge10^{56000}$ is impossible. This final bound also exceeds the
elementary and source thresholds, proving the stated explicit last row.

Reproduce the arithmetic and rank checks separately:

```sh
python3 wiki/research/erdos_699/computations/erdos_699_index_13_effective.py
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_13_interpolation_gcd.py
```

The rank command uses NumPy and `python-flint`. Versions used for these
certificates are pinned in the [interpolation requirements](../../evidence/assets/erdos_699_interpolation_requirements.txt).
The [arithmetic output](../../computations/erdos_699_index_13_effective.json)
records the exact gain, source threshold, and complete row bound.
