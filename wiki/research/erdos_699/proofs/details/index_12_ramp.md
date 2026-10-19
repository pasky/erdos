---
name: research/erdos_699/proofs/details/index_12_ramp
title: "Erdős 699: a simpler effective proof at index twelve"
desc: "Twenty off-diagonal pair estimates and one explicit degree 72 product replace the large interpolation certificates; the algebraic part of the bound becomes 10^845."
created: 2026-09-22T06:47:00Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: a simpler effective proof at index twelve

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/archive/previous_bounds/index_12_effective|The first effective proof]] ·
[[research/erdos_699/methods/details/off_diagonal_pade|Off-diagonal source estimates]]

***

The new off-diagonal estimates simplify the effective index-twelve proof
to one explicit polynomial. Let $X$ be the largest effective threshold
for the twenty prime-pair alternatives in the
[certificate](../../computations/erdos_699_index_12_ramp.json). Then

$$
\boxed{n<\max\{10^{845},X+11\}\qquad\text{for every bad triple at }i=12.}
$$

The number $X$ is effectively computable but has not been numerically
evaluated. Thus $10^{845}$ is the algebraic part of the bound, not a
claim that the whole finite range has been excluded.

The [subsequent numerical proof and finite certificate](index_12_complete.md)
complete this argument: index twelve has no bad triples.

## One polynomial and a positive exponent

Use the explicit coordinate-line product

$$
F_8(X,Y)=\prod_{a=0}^{7}((X-a)(Y-a))^{8-a}.
$$

It has degree $72$, is positive at every admissible $(j,n-j)$, and has
multiplicity at least

$$
m_t=16-t\qquad(0\le t<12)
$$

at every nonnegative grid point on row $x+y=t$. The total multiplicity
is $M=126$, so $M-\deg F_8=54$.

The twenty off-diagonal pair alternatives give eighty-two minimal
cofactor witnessing vectors in prime order $2,3,5,7,11$. For a singleton
selected position, the capacity is $1-v_p$. For a group of two or more
primes at the same position, its product of prime powers divides $n-r$
and has capacity at most one.

The [exact checker](../../computations/erdos_699_index_12_ramp.py)
regenerates all witness vectors and the resulting 402 capacity lists.
As the multiplicities decrease with $t$, rearrangement puts the largest
capacities at the first available rows. In every case,

$$
\sum_t m_t c_t\le53.9.
$$

The exponent gained in the weighted divisibility inequality is therefore
at least $54-53.9=1/10$. This covers all positions and all collisions,
without an interpolation rank calculation.

The twenty alternatives are weakenings of individual sources in the
[directed off-diagonal table](../../computations/erdos_699_off_diagonal_pairs.json).
The checker revalidates each selected source and its strict endpoint
margin. Their two endpoint exponents sum to less than one; if the selected
positions coincide, $u_pu_q\ge n-r$ proves the corresponding alternative
directly. The zero-gap case is consequently included too.

## The algebraic bound

The exact off-maximum valuation constant is

$$
C_*=2^{102}3^{55}5^{27}7^{16}11^{16}.
$$

The [weighted-ramp inequality](../../methods/details/weighted_ramps.md), with
its bounded row-shift corrections, gives

$$n^{1/10}\le\frac{1000}{999}\frac{C_*}{2^{72}}
\qquad(n\ge1\,430\,000),$$

once the cofactor sources hold. The checker verifies the integer comparison

$$
10^{845}(999\cdot2^{72})^{10}>(1000C_*)^{10}.
$$

This proves the stated bound. The earlier twelve-certificate proof remains
valid, but its algebraic bound $10^{3\,643\,130\,001}$ is not needed.
Both arguments leave the separate task of evaluating source thresholds
and excluding the finite range.

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_12_ramp.py
```
