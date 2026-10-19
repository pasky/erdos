---
name: research/erdos_699/proofs/details/index_12_complete
title: "Erdős 699: no exceptions at index twelve"
desc: "Numerical unequal-block Padé bounds, two finite prime-pair cliques, and a completed interval certificate exclude every bad triple with i=12."
created: 2026-09-22T08:38:00Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: no exceptions at index twelve

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/archive/previous_bounds/cutoff_15|Current classification]]

***

**Theorem.** For every $12<j\le n/2$, a prime $p\ge12$ divides both
$\binom n{12}$ and $\binom nj$. Thus index twelve has no bad triples.

The proof first makes the earlier effective bound numerical. Existing
finite prime-pair certificates then reduce the remaining range to
$n\le10^{43}$. A completed interval calculation and exact checks on fifteen
residual rows exclude that entire range.

## A numerical bound for the infinite tail

The [numerical unequal-block argument](../../methods/details/off_diagonal_numerical_thresholds.md)
evaluates all constants in the twenty pair alternatives used by the
[index-twelve ramp](index_12_ramp.md). Explicit factorial
and integral estimates supply the finite prefactors. A finite prime-interval
calculation preserves the coefficient-gcd rates from starting indices at
most $18795$ onward, including the analytic tails.

The largest source threshold is $h=10^{3071169}$, where $h=n-11$.
The ramp's algebraic term is $10^{845}$. Consequently every bad row satisfies

$$
\boxed{n<10^{3\,071\,170}.}\tag{1}
$$

All constants in (1) are numerical. The
[source certificate](../../computations/erdos_699_off_diagonal_explicit_pairs.json)
names the twenty sources, their numerical gcd bounds, and their finite
prime-interval certificates, which the checker validates by their
recorded domains.

## Reducing the finite range

For $p\in\{2,3,5,7,11\}$ choose a position $r_p\in\{0,\ldots,11\}$
maximizing $v_p(n-r_p)$, and write $n-r_p=P_pu_p$.
The [retained index-fifteen pair certificate](../../computations/erdos_699_prime_pair_strips_15.json)
includes all ten pairs of these primes. It proves

$$
\max(u_p,u_q)\ge\min(n-r_p,n-r_q)^{1/3}\tag{2}
$$

through height $10^{15170264}$, for differences at most nineteen,
apart from its explicitly listed exceptions. Thus it covers (1).
All exceptions are below the selected inputs when $n\ge39059468$.
Coincident selected positions also satisfy (2), since
$u_pu_q\ge n-r_p$.

Use the slightly weaker exponent $3333/10000$. At most one of the five
cofactors lies below $(n-11)^{3333/10000}$. In the explicit polynomial

$$
F_8(X,Y)=\prod_{a=0}^{7}((X-a)(Y-a))^{8-a},
$$

the degree is $72$ and the row multiplicities are $m_t=16-t$,
$0\le t\le11$, with sum $126$. The exact capacity calculation,
including every collision of maximal positions, gives gain

$$126-72-\left(16+\frac{6667}{10000}(15+14+13+12)\right)
=\frac{9991}{5000}.\tag{3}$$

The off-maximum constant is

$$
C_*=2^{102}3^{55}5^{27}7^{16}11^{16}.
$$

The same weighted-ramp inequality as in the earlier proof gives, above
the elementary threshold $1430000$,

$$
n^{9991/5000}\le\frac{1000C_*}{999\,2^{72}}.
$$

The exact integer comparison in the checker contradicts this when
$n\ge10^{43}$. Both the elementary and exceptional-height thresholds
are smaller. Hence every possible bad row lies in $n\le10^{43}$.

## Completing the finite exclusion

On this smaller range the [new pair certificate](../../computations/erdos_699_prime_pair_strips_12.json)
certifies all ten stronger alternatives

$$
\max(u_p,u_q)^5\ge\min(n-r_p,n-r_q)^2,\tag{4}
$$

for differences at most eleven. It records every exception separately.
For an exceptional pair of input heights $x,y$, only rows

$$
\max(x,y)\le n\le\min(x,y)+11
$$

can contain it. The existing interval checker disables the corresponding
edge precisely on these row windows. Elsewhere it uses (4), together
with (2) and the original explicit BFT estimates wherever available.

The terminal-prime argument excludes $n<113$. The completed partition of
$[113,10^{43}]$ contains **149926 certified intervals** and **15 exact
singleton rows**. Its minimum directed logarithmic margin exceeds
$0.00003244$. The singleton rows are

$$
128,129,130,132,135,136,200,245,250,251,252,253,256,352,736.
$$

For every admissible column in these rows, the checker computes the exact
binomial gcd and removes its factors $2,3,5,7,11$. The remaining integer
exceeds one in all **1610 checks**. Thus it has a prime divisor at least
thirteen, as required. No row remains unresolved.

The [complete checker](../../computations/erdos_699_index_12_complete.py)
validates the numerical tail, checks the two finite pair ranges and the
exact ramp reduction, and executes the interval and singleton arguments.
Its [certificate](../../computations/erdos_699_index_12_complete.json)
retains the partition hash and, as its own run record, the names of its
source files.

```sh
mkdir -p tmp/erdos699
.venv/bin/python \
  wiki/research/erdos_699/computations/erdos_699_prime_pair_strips.py \
  --clique 2 3 5 7 11 --cap 43 --difference 11 --exponent 2/5 \
  --backend gmpy2 \
  --output tmp/erdos699/erdos_699_prime_pair_strips_12.json
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_12_complete.py
```

The first command writes under the ignored repository `tmp/`; compare its
output with the retained
[strip certificate](../../computations/erdos_699_prime_pair_strips_12.json)
on its mathematical fields, since elapsed times differ between runs.

The first command uses the retained pinned `gmpy2` dependency. The checker
also supports `--backend builtin`, which requires no extra package for
this small finite cap. The larger
retained pair table and the numerical sources have their own reproduction
commands in the linked proofs.
