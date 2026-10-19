---
name: research/erdos_699/methods/details/finite_prime_pairs
title: "Erdős 699: finite-range prime-pair certificates"
desc: "Exact exponent and CRT certificates give one-third cofactor bounds through height 10^1732 for the prime pairs needed by the complete interval proofs."
created: 2026-09-22T03:53:49Z
updated: 2026-09-22T04:33:49Z
---

# Erdős 699: finite-range prime-pair certificates

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/archive/previous_bounds/small_index_effective|Small-index bounds]] ·
[[research/erdos_699/proofs/details/effective_interval_certificates|Interval certificates]]

***

For each pair in the table, let $a,b\ge0$ and $u,v\ge1$ be integers,
and set

$$
x=p^a u,\qquad y=q^b v,\qquad h=\min(x,y).
$$

The exact certificate proves

$$
\boxed{\max(u,v)^3\ge h}
\qquad\text{if}\qquad
|x-y|\le24,\quad H\le h,\quad \max(x,y)\le10^{976},
\tag{1}
$$

with the following thresholds. No coprimality or maximal-prime-power
condition is imposed on $u,v$.

| $p,q$ | $H$ | Exponent pairs after the safe filter | Exceptional minimal solutions with $p^a,q^b>24$ | Largest exceptional $h$ |
| --- | ---: | ---: | ---: | ---: |
| $17,19$ | $4333$ | $202\,191$ | $3$ | $4332$ |
| $2,17$ | $49\,131$ | $859\,352$ | $11$ | $49\,130$ |
| $11,23$ | $2646$ | $224\,179$ | $1$ | $2645$ |
| $5,17$ | $34\,376$ | $369\,825$ | $3$ | $34\,375$ |
| $7,17$ | $319\,334$ | $305\,740$ | $4$ | $319\,333$ |
| $2,3$ | $5104$ | $2\,215\,262$ | $30$ | $5103$ |
| $2,5$ | $59\,376$ | $1\,512\,398$ | $32$ | $59\,375$ |
| $3,5$ | $87\,481$ | $953\,347$ | $30$ | $87\,480$ |
| $3,7$ | $5832$ | $788\,146$ | $12$ | $5831$ |
| $5,7$ | $3751$ | $538\,090$ | $8$ | $3750$ |

The [checker](../../computations/erdos_699_finite_prime_pairs.py)
enumerates prime-power exponents and bounded differences. Its
[retained output](../../computations/erdos_699_finite_prime_pairs.json)
contains all these exceptional minimal solutions and their heights. The
calculation does not enumerate binomial rows or columns.
It supplies stronger pair inequalities throughout an already bounded
range, for use in a complete interval proof. This first table makes no
assertion above $10^{976}$; the longer range needed at index 21 is recorded
separately below.

## Why only minimal solutions need checking

Write $P=p^a$, $Q=q^b$, $M=\max(u,v)$, and more generally let the
allowed difference be $D$. The primes $p,q$ are distinct, so
$\gcd(P,Q)=1$.

If $\min(P,Q)\le D$, then $M\ge h/D$, and hence $M^3\ge h$ whenever
$h^2\ge D^3$. For $D=24$, every $h\ge118$ meets this condition. This
also covers zero exponents. If $x=y$, coprimality gives
$(u,v)=k(Q,P)$ for a positive integer $k$, so $M^2\ge h$ and again
$M^3\ge h$.

It remains to consider $P,Q>D$ and a nonzero signed difference
$d=Pu-Qv$, with $|d|\le D$. There is a unique solution

$$
1\le u_0<Q,\qquad
u_0\equiv dP^{-1}\pmod Q,\qquad
v_0=\frac{Pu_0-d}{Q}.
\tag{2}
$$

The assumptions $P,Q>D$ imply $1\le v_0<P$. Every positive solution
with this difference has the form

$$
(u,v)=(u_0+kQ,v_0+kP),\qquad k\ge0.
\tag{3}
$$

For $k\ge1$, we have $M\ge\max(P,Q)$, whereas

$$
h\le\min(P,Q)M\le M^2\le M^3.
\tag{4}
$$

Consequently only $(u_0,v_0)$ can violate (1). The minimal solution
for $-d$ is $(Q-u_0,P-v_0)$, so testing the positive differences
$1,\ldots,D$ and these complementary solutions covers both signs.

Since $P\le x$ and $Q\le y$, the height cap bounds both prime powers.
The retained calculation therefore includes every possible exponent:
$793$ powers of $17$, $763$ of $19$, $3242$ of $2$, $937$ of $11$,
$716$ of $23$, $1396$ of $5$, $1154$ of $7$, and $2045$ of $3$.
Powers at most $D$ have already been handled
uniformly. For all other powers the procedure tests the minimal
solutions, retains only those with $\max(x,y)\le10^{976}$, and records
every failure of $M^3\ge h$. The threshold $H$ is the larger of $118$
and one plus the largest recorded exceptional height. This proves (1).

The exceptional records can repeat a height when that height admits
several prime-power decompositions. For example,
$2^{10}\cdot24=2^{11}\cdot12=2^{12}\cdot6=2^{13}\cdot3$
is checked in all four forms. The certificate requires no restriction
that a chosen prime power be the full component of its integer.

## Exact filters and modular inverses

Put $A=\max(P,Q)$ and $B=\min(P,Q)$. A violating solution satisfies

$$
M^3<h\le BM,\qquad h\ge A-D.
$$

Thus $M^2<B$, and necessarily

$$
(A-D)^2<B^3.
\tag{5}
$$

The program rejects an exponent pair only when integer bit lengths
already prove the opposite inequality. If $\ell(z)$ denotes the bit
length of a positive integer, then
$2^{\ell(z)-1}\le z<2^{\ell(z)}$. In particular,

$$
2(\ell(A-D)-1)\ge3\ell(B)
\quad\Longrightarrow\quad
(A-D)^2>B^3.
$$

This is a sufficient rejection test; no approximation to logarithms is
used. Similarly, $u^2\ge P$ proves $u^3\ge Pu\ge h$, and
$v^2\ge Q$ proves $v^3\ge Qv\ge h$. The first test is sometimes
settled immediately by the safe bit-length comparison
$2(\ell(u)-1)\ge\ell(P)$; otherwise the program multiplies the
integers exactly.

For a fixed $Q$, all inverses of successive powers of $p$ are computed
without repeated extended Euclidean calculations. Start with $I=1$,
the inverse of $p^0$ modulo $Q$. Choose $0\le k<p$ so that
$I+kQ$ is divisible by $p$, and replace

$$
I\longleftarrow\frac{I+kQ}{p}.
\tag{6}
$$

If the old $I$ is the inverse of $p^{a-1}$, (6) is the inverse of
$p^a$ modulo $Q$. Moreover $1\le I<Q$ is preserved. The recurrence
is performed for every exponent, including powers skipped because
they are at most $D$.

## Use in the interval proof

For an index $i\le25$, choose maximal positions $r_p,r_q$ in
$\{0,\ldots,i-1\}$ and write

$$
n-r_p=P_pu_p,\qquad n-r_q=P_qu_q.
$$

Their difference is at most $24$, their smaller height is at least
$n-i+1$, and their larger height is at most $n$. Therefore (1) gives

$$
\max(u_p,u_q)\ge(n-i+1)^{1/3}
\quad\text{for}\quad
H+i-1\le n\le10^{976}.
\tag{7}
$$

Equivalently, putting $z_p=\log u_p/\log(n-i+1)$, the pair contributes
the exact constraint $\max(z_p,z_q)\ge1/3$. These constraints can be
combined with the existing prime-pair inequalities when bounding the
small-prime part of $\binom ni$ throughout an integer interval.
Coincident maximal positions are included by the $x=y$ argument above.

The finite-range inequalities and an independently established infinite
tail have separate roles: the tail bounds the remaining rows by
$10^{976}$, and (7) strengthens the inequalities used to exclude
intervals inside that bound. This note alone does not assert the
completion of any particular interval partition.

To reproduce the ten certificates from the repository root:

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_finite_prime_pairs.py --cap 976 --difference 24
```

## The longer range for index 21

The same proof and checker also cover differences at most $20$ and
heights at most $10^{1732}$. The
[second retained certificate](../../computations/erdos_699_finite_prime_pairs_21.json)
gives the following lower thresholds $H$:

| Pair | $H$ |
| --- | ---: |
| $17,19$ | $4333$ |
| $2,17$ | $24\,566$ |
| $5,17$ | $34\,376$ |
| $7,17$ | $319\,334$ |
| $2,3$ | $5104$ |
| $2,5$ | $59\,376$ |
| $3,5$ | $87\,481$ |
| $3,7$ | $5832$ |
| $5,7$ | $1373$ |
| $11,13$ | $43\,924$ |

Thus every edge in this second table applies to the selected numerator
positions of an index-21 row whenever
$319\,354\le n\le10^{1732}$. The common interval cutoff
$1\,771\,595$ is larger and also accommodates the original explicit BFT
table. Reproduce this second table under the ignored repository `tmp/`
with:

```sh
mkdir -p tmp/erdos699
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_finite_prime_pairs.py \
  --pairs 17,19 2,17 5,17 7,17 2,3 2,5 3,5 3,7 5,7 11,13 \
  --cap 1732 --difference 20 \
  --output tmp/erdos699/erdos_699_finite_prime_pairs_21.json
```

Compare the regenerated file with the retained one on its mathematical
fields; elapsed times differ between runs.

## Completing the five-prime graph for index 13

Five further certificates cover differences at most $12$ and heights at
most $10^{1732}$:

| Pair | $H$ |
| --- | ---: |
| $2,7$ | $39\,059\,457$ |
| $2,11$ | $1\,376\,255$ |
| $3,11$ | $30\,614$ |
| $5,11$ | $364$ |
| $7,11$ | $243$ |

Combine these with the five pairs among $2,3,5,7$ already present in the
index-21 table. The resulting ten edges form the complete graph on
$\{2,3,5,7,11\}$. All its one-third cofactor constraints hold for an
index-13 row whenever $39\,059\,469\le n\le10^{1732}$.

The [retained extra certificates](../../computations/erdos_699_finite_prime_pairs_13_extra.json)
are reproduced under the ignored repository `tmp/` by:

```sh
mkdir -p tmp/erdos699
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_finite_prime_pairs.py \
  --pairs 2,7 2,11 3,11 5,11 7,11 --cap 1732 --difference 12 \
  --output tmp/erdos699/erdos_699_finite_prime_pairs_13_extra.json
```

Compare the regenerated file with the retained one on its mathematical
fields; elapsed times differ between runs.
