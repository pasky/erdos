---
name: research/erdos_699/proofs/details/index_14_effective
title: "Erdős 699: index 14 is effective"
desc: "Off-diagonal prime-pair alternatives and one universal polynomial interpolation certificate make the remaining index fourteen effective."
created: 2026-09-22T06:48:00Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: index 14 is effective

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/methods/details/off_diagonal_pade|Off-diagonal Padé estimates]]

***

**Theorem.** There is an effectively computable integer $N_{14}$ such
that every bad triple $(n,14,j)$ satisfies $n<N_{14}$, for the original
threshold $p\ge14$.

One polynomial certificate works for every cofactor alternative, every
selected position, and every collision between selected positions.
Its symmetric interpolation matrix has only $831$ rows and $841$ columns.
The pair-source starting heights are effective but have not all been
numerically evaluated. Thus this proves effectivity, rather than a
complete exclusion of the finite range below $N_{14}$.

**Subsequent complete result.** The [numerical tail and finite certificates](../../archive/previous_bounds/cutoff_10.md)
exclude this entire index. The effective proof below is retained as
an earlier step.

## Unequal Padé blocks give stronger pair alternatives

Let $\mathcal P=\{2,3,5,7,11,13\}$. For each $p\in\mathcal P$, choose
$r_p\in\{0,\ldots,13\}$ maximizing $v_p(n-r_p)$, and put

$$
n-r_p=p^{a_p}u_p,\qquad h=n-13.
$$

The [off-diagonal argument](../../methods/details/off_diagonal_pade.md)
allows different prime-power block lengths on the two sides of a seed
$aP-bQ=\delta>0$. For positive integer directions $(A,B,C)$, write
$L_0=A+B$, $L_1=B+C$, and let $C_0,K_0$ be the two positive decay rates
in that argument. If $P=p^k$ and $Q=q^l$, then every pair of targets
strictly below

$$\alpha_p=1-\frac{kL_0\log p}{K_0},\qquad
  \alpha_q=1-\frac{lL_1\log q}{K_0}$$

gives an effective alternative

$$
u_p>h^{\gamma_p}\quad\text{or}\quad u_q>h^{\gamma_q}. \tag{1}
$$

The [source checker](../../computations/erdos_699_off_diagonal_pairs.py)
and [source records](../../computations/erdos_699_off_diagonal_pairs.json)
retain $294$ such alternatives. Each has an exact finite rational
coefficient-gcd sum, a strictly smaller rational gcd growth rate,
directed interval bounds on $C_0,K_0$, and an endpoint margin greater
than $1/10000$. All endpoints are exact rationals with denominator
$10000$. The coefficient-gcd proof has an effective threshold because
it uses finitely many prime intervals and a computable prime-number
estimate; no infinite sum or ineffective approximation theorem enters.

The usual application assumes $r_p\ne r_q$, so that the factor gap is
nonzero and at most $13$. There is also a direct treatment of the
zero-gap case. If $r_p=r_q$, the selected prime powers are coprime and
both divide $n-r_p$, hence $u_pu_q\ge n-r_p\ge h$. Every retained pair
satisfies $\gamma_p+\gamma_q<1$. Thus (1) also holds when the positions
coincide.

Together with $18$ retained earlier pair alternatives, these give $312$
disjunctions. Their exact, componentwise minimal witnessing vectors
number $1598$. This means that for every sufficiently large row there
is a listed vector $v=(v_p)_{p\in\mathcal P}$ with
$u_p\ge h^{v_p}$ for every prime. The
[whole-index checker](../../computations/erdos_699_index_14_effective.py)
regenerates the vectors by induction over the alternatives and matches
every source against its retained certificate.

## One polynomial family handles every position

Use coordinate-factor exponents

$$
\mathbf h=(33,29,26,22,19,15,10,5,0,0,0,0,0,0)
$$

and row multiplicities

$$
\mathbf m=(66,65,62,58,55,53,51,46,41,37,33,30,27,24).
$$

Define

$$H(X,Y)=\prod_{a=0}^{13}((X-a)(Y-a))^{h_a},\qquad
 R_{xy}=\max\{0,m_{x+y}-h_x-h_y\}\quad(x+y<14).$$

The symmetric Hasse-jet map on polynomials of degree at most $56$ has
$831$ prescribed coefficients and $841$ monomials. Its exact rank modulo
$65521$ is $831$, proving surjectivity over $\mathbb Q$. The
[nonvanishing lemma](../../methods/details/jet_nonvanishing.md) therefore
supplies a finite integer polynomial family of residual degree at most
$57$, with no common zero in $X+Y>13$. After multiplication by $H$, its
members have degree at most

$$
D=2\sum h_a+57=375.
$$

For $14<j\le n-j$, the coordinate factor does not vanish. At least one
member $F$ consequently has $F(j,n-j)\ne0$.

For a given cofactor vector, a selected position occupied by exactly
one prime $p$ has capacity $1-v_p$. A position occupied by several
primes has capacity at most one for the whole group, since the product
of its selected prime powers divides the corresponding factor $n-r$.
The multiplicities $m_r$ are nonincreasing. Rearrangement puts the
largest capacities at the earliest rows, covering all assignments of
the selected positions, not just consecutive assignments.

For every subset of singleton primes, the checker assigns capacity one
to the maximum possible number of remaining groups, namely half the
number of remaining primes rounded down. A single remaining prime is
omitted from this construction because it would itself be a singleton.
This yields an upper bound for every possible collision pattern.
All these capacity vectors are checked against all $1598$ cofactor
vectors using exact integers. The minimum gain is

$$\boxed{\eta=\sum_{r=0}^{13}m_r-D-\sum_r C_rm_r
       \ \ge\ \frac{149}{5000}>0.} \tag{2}$$

No position-dependent AP identity or further branch of a product
alternative is needed in this argument.

## Effective stopping bound

Badness and Kummer's formula imply that the large-prime part of
$\prod_{r=0}^{13}(n-r)^{m_r}$ divides the nonzero integer $F(j,n-j)$.
Away from the selected position for a prime $p<14$,

$$
v_p(n-r)\le v_p(|r-r_p|).
$$

The omitted small-prime contribution away from all selected positions
is thus bounded by $(13!)^{66}$. Together with (2), polynomial growth
gives

$$
n^{149/5000}\le 2\,\|F\|_1(13!)^{66}
$$

above an elementary computable correction threshold. The constant
factor absorbs the bounded shifts between $n-r$, $h$, and $n$.

The explicit adjugate and Hadamard estimate from the
[interpolation extension proof](../../archive/previous_bounds/interpolation_extensions.md)
bounds this right side by $10^{100814}$. The checker verifies

$$
3\,400\,000\cdot\frac{149}{5000}>100814.
$$

Consequently every bad row for which all the source estimates hold
satisfies $n<10^{3\,400\,000}$. Taking the maximum of this evaluated
algebraic bound, the elementary correction threshold, and the finitely
many effective pair-source thresholds defines $N_{14}$ effectively.
The numerical values of the latter thresholds remain to be evaluated.

The [certificate data](../../computations/erdos_699_index_14_effective.json)
retain the full alternatives, the minimal vectors, the rank parameters,
and the exact worst capacity comparison. Reproduce it with the pinned
[interpolation dependencies](../../evidence/assets/erdos_699_interpolation_requirements.txt):

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_off_diagonal_pairs.py
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_14_effective.py
```

The second command accepts `--arithmetic-only` to repeat the source and
finite cofactor comparisons without repeating the modular rank.
