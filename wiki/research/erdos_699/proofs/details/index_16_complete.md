---
name: research/erdos_699/proofs/details/index_16_complete
title: "Erdős 699: complete exclusion at index 16"
desc: "An asymmetric cofactor estimate reduces the stopping bound to 10^914; finite prime-power certificates and 100204 certified intervals exclude every remaining row."
created: 2026-09-22T04:20:00Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: complete exclusion at index 16

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]]

***

**For every $16<j\le n/2$, some prime $p\ge16$ divides both
$\binom n{16}$ and $\binom nj$.** All rows are covered by an analytic
tail and certified intervals; no singleton row requires direct testing.

The [asymmetric cofactor estimate](../../methods/details/asymmetric_cofactors.md)
for $5,7$, with targets $(.29,.20)$, is valid above input height
$10^{913}$. With the original explicit BFT table, the weighted polynomial
$F_{10}$ has minimum gain $23/100$, covering all 36 cofactor vectors
and every collision pattern. The exact off-maximum constant is

$$
C_*=2^{160}3^{84}5^{45}7^{33}11^{20}13^{20}.
$$

For $n\ge2\,960\,000$, the weighted inequality gives

$$
n^{23/100}\le\frac{1000C_*}{999\,2^{110}}.
$$

An exact integer comparison yields the algebraic cap $10^{686}$.
Including the source threshold and shifts proves that every bad row
satisfies $n<10^{914}$. The
[weighted certificate](../../computations/erdos_699_asymmetric_ramp_caps.json)
retains this calculation.

On that finite range, use the [prime-power method](../../methods/details/finite_prime_pairs.md)
for the seven pairs

$$\{2,3\},\{2,5\},\{3,5\},\{3,7\},\{5,7\},
\{7,13\},\{11,13\}.$$

The [retained pair certificates](../../computations/erdos_699_finite_prime_pairs_16.json)
cover heights at least through $10^{914}$ and differences at least
through $15$. Every pair gives a maximum-cofactor exponent $1/3$ above
its displayed small exceptional range. Using the conservative weight
$.3333$ and the original BFT table leaves thirteen minimal cofactor
vectors, whose minimum sum is $1.2589$. All estimates apply to the
selected numerator factors whenever $n\ge1\,771\,595$.

Thus, on the remaining range,

$$
U_{16}(n)\le\frac{2^{1.2589}}{16}\,n^{4.7411}.
$$

The retained fat-point lower bound has exponent $5$. A directed-rounding
comparison reduces the possible row range further to $n<10^{41}$.
This reduction is applied only below the already proved cap $10^{914}$.

The terminal-prime argument excludes all admissible $n<523$. On
$[523,10^{41}]$, the interval method accepts **100,204 intervals**,
with 200,407 visited nodes. Its minimum certified logarithmic margin is

$$
.000015922085670308186452647323639868978608022312196899924.
$$

There are no unresolved singletons. The
[complete output](../../computations/erdos_699_index_16_complete.json)
records the partition hash and, as its own run record, the names of
its inputs. Together with the analytic
tail, it proves the stated full-index result.

Reproduce the last two stages with:

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_asymmetric_ramp_caps.py
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_16_complete.py
```

The finite pair records can be reproduced by the generic prime-pair
checker, using their recorded primes, height cap and difference bound.
