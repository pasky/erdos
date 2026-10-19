---
name: research/erdos_699/proofs/details/further_interval_certificates
title: "Erdős 699: complete proofs at further small indices"
desc: "Exact prime-power certificates, interval proofs, and small residual-row checks complete the original claim for every i>=15, and also for i=10,13."
created: 2026-09-22T04:08:00Z
updated: 2026-09-22T04:33:49Z
---

# Erdős 699: complete proofs at further small indices

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/archive/previous_bounds/further_effective_bounds|Numerical stopping bounds]] ·
[[research/erdos_699/methods/details/finite_prime_pairs|Finite prime-pair proof]]

***

**There are no bad triples at $i=10,13$ or at any $i\ge15$, with the original
threshold $p\ge i$.** The new certificates here cover
$10,13,15,18,19,20,21,22,24,25$. The other required indices
$16,17,23$ and every $i\ge26$ were already excluded.

The numerical stopping bounds already excluded $n\ge10^{976}$ for
$i=19,24$ and $n\ge10^{957}$ for $i=22,25$. The
[asymmetric cofactor bound](../../methods/details/asymmetric_cofactors.md)
also gives $n<10^{1046}$ at $i=13$ and $n<10^{1732}$ at $i=21$;
their weighted constants are retained in
the [exact checker](../../computations/erdos_699_asymmetric_ramp_caps.py).
The [numerical index-18 proof](index_18_effective.md)
gives $n<10^{700\,000}$.
The fully numerical interpolation bounds at
[index 10](index_10_effective.md),
[index 15](index_15_numerical_tail.md), and
[index 20](index_20_numerical_tail.md) give
$n<10^{15\,000\,000}$, $n<10^{15\,170\,264}$, and
$n<10^{27\,027\,659}$, respectively.
Interval certificates handle these finite ranges. They leave two small
rows at index 10 and forty at index 13, each verified by exact binomial
gcd calculations.

## Bridging the bounded range

The [finite prime-pair certificates](../../methods/details/finite_prime_pairs.md)
prove

$$
\max(u_p,u_q)\ge\min(P_pu_p,P_qu_q)^{1/3}
$$

for the retained pairs, bounded differences at most 24, and all heights
up to $10^{976}$, above explicit small thresholds. A second table extends
the required pairs to $10^{1732}$ with differences at most 20 for index 21.
A further table completes the five-prime graph needed at index 13.
For index 18, the [strip argument](../../methods/details/prime_power_strips.md)
certifies all 15 pairs among $2,3,5,7,11,13$ through $10^{1\,200\,000}$.
The same graph is certified through $10^{15\,170\,264}$ for index 15.
The earlier checker enumerates prime-power exponents; the strip checker
certifies entire regions of exponents using modular coefficient bounds.
Both reduce their remaining cases to minimal solutions of a linear congruence.
Every other positive solution is handled by a uniform inequality.

For selected maximal positions $n-r_p=P_pu_p$, these estimates give
cofactor constraints of exponent $3333/10000<1/3$. The common row threshold
is $39\,059\,469$ at index 13, $73\,516\,020$ at index 15,
$73\,516\,023$ at index 18, and $1\,771\,595$ at
$19,21,22,24,25$.
Combine them with the original
explicit BFT constraints. The interval proof takes the maximum over all
minimal cofactor vectors, exactly as in the
[preceding interval proof](effective_interval_certificates.md).

The sum of the vector coordinates also yields

$$
U_i(n)\le\frac{2^\gamma}{[i]_S}n^{s-\gamma}.
$$

At $i=13,15,18,19,21,24$, the new savings are
$\gamma=1.3332,1.6665,1.6665,1.3549,1.5922,1.6462$,
respectively. Comparing with the previous fat-point lower bound
excludes the ranges above $10^{27},10^{27},10^{37},10^{43},10^{59},10^{61}$,
respectively, up to the already established stopping bounds. These comparisons do
not apply beyond the finite prime-pair cap: the earlier infinite-tail
proof supplies that part of the argument.

## Stronger edges and their exceptional row windows

Indices 10 and 20 use the exponent $2/5$. The generalized strip argument
certifies $\max(u_p,u_q)^5\ge h^2$, where $h$ is the smaller numerator
factor. At index 20, use the two triangles $\{2,3,5\}$ and $\{7,11,13\}$,
and the pair $17,19$. All seven edges are certified through
$10^{27\,027\,659}$. Together with the original explicit BFT edges, their
minimum cofactor sum is $\gamma=2.038$, reducing the remaining cap to
$10^{39}$.

At index 10, five edges of the complete graph on $\{2,3,5,7\}$ are
certified at least through $10^{15\,000\,000}$. The omitted edge $2,7$
retains its original explicit BFT exponent $.259$. Their minimum sum is
$\gamma=1.059$, reducing the cap to $10^{80}$. The stronger $2,7$ edge
of exponent $2/5$ had already been certified through $10^{1732}$, so it
applies throughout this remaining range. Thus the interval proof can use
the full four-prime graph without repeating the large-height computation
for that sixth edge.

The [window checker](../../computations/erdos_699_window_intervals.py)
keeps the exact exceptional solutions from each finite pair certificate.
An exception with numerator factors $x,y$ can occur in an index-$i$ row
only when

$$
\max(x,y)\le n\le\min(x,y)+i-1.
$$

Above the elementary small-power threshold, an edge is therefore valid
throughout any interval avoiding its exceptional row windows. For each
interval, the checker uses exactly the available edges and recomputes the
finite set of minimal cofactor vectors. It also checks the height cap of
each source, so certificates with different caps can be combined.
The completed index-20 proof uses 43 such graphs and 124 edge-specific
windows; index 10 uses 35 graphs and 142 edge-specific windows.

## Complete partitions

| $i$ | First remaining row | Initial stopping bound | Inclusive interval cap | Certified intervals | Minimum logarithmic margin, rounded down |
| --- | ---: | ---: | ---: | ---: | ---: |
| $10$ | $113$ | $10^{15\,000\,000}$ | $10^{80}$ | $43\,985$ | $0.00005322$ |
| $13$ | $113$ | $10^{1046}$ | $10^{27}$ | $530\,441$ | $0.000007410$ |
| $15$ | $523$ | $10^{15\,170\,264}$ | $10^{27}$ | $575\,194$ | $0.000005231$ |
| $18$ | $887$ | $10^{700\,000}$ | $10^{37}$ | $247\,058$ | $0.00002833$ |
| $19$ | $887$ | $10^{976}$ | $10^{43}$ | $201\,640$ | $0.000006247$ |
| $20$ | $1129$ | $10^{27\,027\,659}$ | $10^{39}$ | $173\,071$ | $0.00001355$ |
| $21$ | $1129$ | $10^{1732}$ | $10^{59}$ | $344\,891$ | $0.00002035$ |
| $22$ | $1327$ | $10^{957}$ | $10^{957}$ | $244\,360$ | $0.000002460$ |
| $24$ | $1327$ | $10^{976}$ | $10^{61}$ | $312\,701$ | $0.00001048$ |
| $25$ | $1327$ | $10^{957}$ | $10^{957}$ | $137\,216$ | $0.00001182$ |

All 2,810,557 accepted intervals have strictly positive directed-rounding
margins. The exact margins, chosen prime pairs, vector counts, and
interval-partition hashes are in the
[four-case certificate](../../computations/erdos_699_further_intervals.json)
and the [index-21](../../computations/erdos_699_further_intervals_21.json)
and [index-13](../../computations/erdos_699_further_intervals_13.json) certificates,
and the [index-15](../../computations/erdos_699_further_intervals_15.json),
[index-18](../../computations/erdos_699_further_intervals_18.json),
[index-20](../../computations/erdos_699_window_intervals_20.json), and
[index-10](../../computations/erdos_699_window_intervals_10.json) certificates.

At index 10, the two remaining rows are $n=1029,252$. All 620 admissible
columns have a common prime at least 10, checked by exact binomial gcds
after removing the primes $2,3,5,7$.

At index 13, the 40 residual rows are all at most 2060 and are listed in
the JSON. For each one and every $13<j\le n/2$, the checker computes
$\gcd(\binom n{13},\binom nj)$ and removes all factors $2,3,5,7,11$.
The remaining integer exceeds one in all 8969 column checks. Thus each
pair has a common prime at least 13. The certificate retains the count of
these exact calculations. The other eight indices require no individual
row or column checks.

The interval valuation upper bound is unchanged mathematically. Its
evaluation now skips all powers $p^a\le R-L$ by binary search, since
every interval $[L,R]$ necessarily crosses a multiple of each such power.
Only the remaining powers require the original division and residue
checks. This makes very large caps practical without weakening the
certificate.

Reproduce the ten partitions, writing the named outputs under the ignored
repository `tmp/`, with:

```sh
mkdir -p tmp/erdos699
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_further_intervals.py --indices 19 22 24 25 --max-nodes 2000000
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_further_intervals.py \
  --indices 21 --max-nodes 2000000 \
  --pair-certificate wiki/research/erdos_699/computations/erdos_699_finite_prime_pairs_21.json \
  --output tmp/erdos699/erdos_699_further_intervals_21.json
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_further_intervals.py \
  --indices 13 --max-nodes 2000000 --exact-singleton-limit 2100 \
  --pair-certificate wiki/research/erdos_699/computations/erdos_699_finite_prime_pairs_21.json \
  --extra-pair-certificate wiki/research/erdos_699/computations/erdos_699_finite_prime_pairs_13_extra.json \
  --output tmp/erdos699/erdos_699_further_intervals_13.json
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_further_intervals.py \
  --indices 18 --max-nodes 2000000 --exact-singleton-limit 10000 \
  --pair-certificate wiki/research/erdos_699/computations/erdos_699_prime_pair_strips_k6.json \
  --output tmp/erdos699/erdos_699_further_intervals_18.json
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_further_intervals.py \
  --indices 15 --max-nodes 2000000 --exact-singleton-limit 10000 \
  --pair-certificate wiki/research/erdos_699/computations/erdos_699_prime_pair_strips_15.json \
  --output tmp/erdos699/erdos_699_further_intervals_15.json
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_window_intervals.py \
  --index 20 --tail-power 27027659 --max-nodes 2000000 \
  --pair-certificate wiki/research/erdos_699/computations/erdos_699_prime_pair_strips_20.json \
  --output tmp/erdos699/erdos_699_window_intervals_20.json
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_window_intervals.py \
  --index 10 --tail-power 15000000 --max-nodes 5000000 \
  --pair-certificate wiki/research/erdos_699/computations/erdos_699_prime_pair_strips_20.json \
    wiki/research/erdos_699/computations/erdos_699_prime_pair_strips_10_global.json \
    wiki/research/erdos_699/computations/erdos_699_prime_pair_strips_two_fifths.json \
  --output tmp/erdos699/erdos_699_window_intervals_10.json
```

Compare each regenerated partition with the retained file of the same
name under `computations/` on its mathematical fields; elapsed times
differ between runs. The source prime-pair JSON must first be reproduced
using the command in its proof note. The interval output names that file
as the run's own record.
