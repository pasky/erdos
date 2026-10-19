---
name: research/erdos_699/proofs/details/index_11_complete
title: "Erdős 699: complete exclusion at index 11"
desc: "An asymmetric Padé bound, exact finite prime-power certificates and interval inequalities exclude every bad triple with i=11; eleven small remaining rows are checked directly."
created: 2026-09-22T04:15:00Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: complete exclusion at index 11

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]]

***

**For every $11<j\le n/2$, some prime $p\ge11$ divides both
$\binom n{11}$ and $\binom nj$.** The proof combines an analytic tail,
exact finite prime-power calculations, interval inequalities and a small
number of direct binomial-gcd checks. All ranges are covered.

## 1. The analytic tail

The [asymmetric cofactor argument](../../methods/details/asymmetric_cofactors.md)
proves that every bad triple at index eleven satisfies

$$
n<10^{914}.\tag{1}
$$

Its new ingredient is the explicit alternative
$u_5>x^{.29}$ or $u_7>x^{.20}$ for nearby integers
$5^a u_5,7^b u_7$, valid once their minimum exceeds $10^{913}$.
Together with the original BFT table and the weighted polynomial $F_7$,
this gives gain $13/125$ and algebraic bound $10^{711}$. Equation (1)
also absorbs the bounded numerator shifts.

## 2. Stronger bounds on the remaining finite range

Apply the [finite prime-pair method](../../methods/details/finite_prime_pairs.md)
to all six pairs from $\{2,3,5,7\}$, with maximum height $10^{914}$ and
difference at most $10$. Exact modular arithmetic proves

$$
\max(u,v)^3\ge\min(p^a u,q^b v)\tag{2}
$$

above the following minimum-height thresholds:

| Pair | Threshold |
| --- | ---: |
| $2,3$ | $641$ |
| $2,5$ | $5626$ |
| $2,7$ | $19\,529\,729$ |
| $3,5$ | $43\,741$ |
| $3,7$ | $5832$ |
| $5,7$ | $1373$ |

The [six certificates](../../computations/erdos_699_finite_prime_pairs_small.json)
retain every exception below these thresholds. The calculation enumerates
prime-power exponents and bounded differences. For each exponent pair,
only the minimal positive solution needs testing: every other solution
already satisfies (2). Zero difference and zero exponents are covered by
the elementary cases in the linked proof.

For $19\,529\,739\le n\le10^{914}$, every selected numerator factor
$n-r_p$ exceeds all six thresholds. Set
$z_p=\log u_p/\log(n-10)$. Then every pair has
$\max(z_p,z_q)\ge1/3$. We conservatively use $.3333$ in the numerical
checker. The four componentwise minimal vectors put zero at one vertex
and $.3333$ at each of the other three. Thus

$$\sum_{p<11}z_p\ge.9999,\qquad
 U_{11}(n)\le2^{.9999}n^{3.0001}.\tag{3}$$

The retained fat-point inequality gives, for $n\ge113$,

$$U_{11}(n)>
 \frac{4^{28/11}}{11!}\frac{58}{113}\,n^{37/11}.\tag{4}$$

Here $58/113=1-55/113$ bounds the normalized numerator product from
below. Comparing (3) and (4), with outward-rounded logarithms, gives

$$
n<10^{19}.\tag{5}
$$

This comparison is used only inside the already justified range (1).
Together, (1)--(5) remove every larger row.

## 3. Covering every remaining row

For $24\le n<113$, there is a prime $n-11<p\le n$.
It satisfies $p>n/2$ and $n\bmod p<11<j$, so it divides both required
binomial coefficients. This is the terminal-prime argument, with the
same retained prime-gap record as the earlier interval proofs.

On $[113,10^{19}]$, the interval checker bounds every small-prime
valuation over an entire interval and compares their sum to (4) and
the symmetric discriminant bound. Above $19\,529\,739$, it also uses
the four cofactor vectors from (3). It accepts **31,796 intervals**;
the minimum certified logarithmic margin exceeds $.0000076428$.

Exactly eleven singleton rows require a different certificate:

$$
129,130,135,250,252,253,352,385,1030,1032,1380.
$$

For each one, the checker computes $\binom nj$ successively by the
integer recurrence
$\binom nj=\binom n{j-1}(n-j+1)/j$.
It forms $\gcd(\binom n{11},\binom nj)$ and removes every factor
$2,3,5,7$. The result exceeds one for all **2,541 admissible columns**,
so each column has a common prime at least eleven.

The complete partition has 31,807 leaves and 63,613 visited nodes.
The [certificate](../../computations/erdos_699_index_11_complete.json)
records the partition hash, the exact singleton rows and, as its own run
record, the names of its inputs. These checks,
together with the analytic tail,
prove the assertion for every admissible row.

## Reproduction

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_bft_asymmetric.py
mkdir -p tmp/erdos699
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_finite_prime_pairs.py --pairs 2,3 2,5 2,7 3,5 3,7 5,7 --cap 914 --difference 10 --output tmp/erdos699/erdos_699_finite_prime_pairs_small.json
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_11_complete.py
```

The second command writes under the ignored repository `tmp/`; compare
its output with the retained
[pair certificate](../../computations/erdos_699_finite_prime_pairs_small.json)
on its mathematical fields, since elapsed times differ between runs.

The [index-eleven driver](../../computations/erdos_699_index_11_complete.py)
reuses the earlier directed-rounding interval engine. Its optional exact
singleton callback accepts no row above 2000; a larger unresolved
singleton stops the proof rather than being treated as covered.
