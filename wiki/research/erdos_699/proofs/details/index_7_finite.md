---
name: research/erdos_699/proofs/details/index_7_finite
title: "Erdős 699: finite exclusion at index seven through 10^100000001"
desc: "Pair and three-prime CRT certificates reduce the finite range to 18,000 intervals and 28 explicitly checked rows. The numerical infinite tail remains separate."
created: 2026-09-22T17:01:09Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: finite exclusion at index seven through 10^100000001

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/proofs/details/index_7_effective|Index-seven effectivity]] ·
[[research/erdos_699/methods/details/triple_prime_power_strips|Three-prime CRT strips]]

***

**Theorem.** There is no admissible bad triple with $i=7$ and
$n\le10^{100\,000\,001}$, for the original threshold $p\ge7$.

This unconditional finite-range exclusion now meets the
[completed numerical infinite tail](index_7_complete.md),
settling index seven entirely. The calculation here supplies the finite
part of that combined proof.

The [combination checker](../../computations/erdos_699_index_7_finite.py)
and its [record](../../computations/erdos_699_index_7_finite.json)
retain the following reductions.

| Step | Finite cofactor information | Resulting row cap |
| --- | --- | ---: |
| First pair certificate | Every pair among $2,3,5$ has exponent $11/25=.44$ | $10^{132427}$ |
| Second pair certificate | Every pair has exponent $47/100=.47$ | $10^{2057}$ |
| Three-prime certificates | A cofactor has exponent $.61$, or $.66$, outside the respective exact exceptional rows | $10^{40}$ |
| Directed interval partition and exact residual checks | All remaining rows and columns | None |

## The pair reductions

The first [pair certificate](../../computations/erdos_699_prime_pair_strips_7_extended.json)
works through $10^{100\,000\,001}$; the
[second](../../computations/erdos_699_prime_pair_strips_7_middle.json)
works through $10^{132427}$. Both allow differences up to six.
Their finitely many exceptional pairs have explicit heights below the
row caps subsequently obtained.

For a complete three-prime graph of exponent $\delta$, the cofactor
witnesses are permutations of $(0,\delta,\delta)$. Apply the already
verified polynomial families from the index-seven effectivity proof.
Only the families with uniform nonvanishing are used here; the
coprime-kernel certificate is unnecessary. The central column is already
excluded by the elementary argument in that proof.

The fixed-slope lemma forces at least one selected maximal prime-power
position to be zero. The checker therefore considers all $90$ distinct
position assignments and all three witnesses: $270$ exact gain
comparisons at each step. Repeated positions use the separate collision
certificate. The explicit coefficient bounds give the caps in the table,
including the shift from $h=n-6$ to $n$. No large modular-rank calculations
are repeated.

## Three primes and the final intervals

The [$.61$ certificate](../../computations/erdos_699_triple_prime_power_strips_7_061.json)
and [$.66$ certificate](../../computations/erdos_699_triple_prime_power_strips_066_3000.json)
cover heights through $10^{3000}$. They include all $127$ selected-position
patterns with minimum zero, including coincidences.

Combining the $.61$ alternative with the pair exponent $.47$ gives a
cofactor sum of at least $1.08$. The ordinary fat-point lower bound then
reduces the remaining range to $n\le10^{40}$. The larger $.66$ alternative
improves the interval comparisons where it is available. The interval
checker disables a triple alternative precisely on its listed exceptional
rows, and handles the pair exceptions by their corresponding row windows.

The [interval driver](../../computations/erdos_699_index_7_finite_intervals.py)
and [output](../../computations/erdos_699_index_7_finite_intervals.json)
record:

- **18,000 certified intervals**, including 145 intervals containing no
  row divisible by eight, nine, or twenty-five;
- **28 residual rows**, all at most $26,250$;
- **41,740 exact column checks**, each producing a common factor with a
  prime divisor at least seven.

The smallest directed logarithmic margin is greater than
$0.00000808393925427$. The terminal-prime lemma covers the prefix below
row $89$. The output records the interval partition hash, the source file
names, and the count of residual column gcd checks.

## Large pair certificates without large auxiliary powers

The [optimized strip generator](../../computations/erdos_699_prime_pair_log_strips.py)
uses the same strip inequalities as the earlier integer checker. It avoids
forming high powers of integers with tens of millions of digits.

If $A=2^s a+e$, with $0\le e<2^s$, then

$$
\log a+s\log2\le\log A<\log(a+1)+s\log2.
$$

Leading integer bits therefore give rigorous short intervals for $\log A$.
Directed arithmetic certifies the required power comparisons. Ambiguous
small comparisons are evaluated with integers; higher precision handles
large comparisons, with perfect-power equality treated exactly.

One extended gcd supplies both modular coefficient progressions. Thus the
loop does not repeatedly multiply and divide the large prime powers for
every small difference. At cap $1000$, the new implementation reproduces
all anchors and exceptions of the original checker for each of the three
pairs. The extended certificates contain 176, 171, and 165 anchors.

The [original pair certificate](../../computations/erdos_699_prime_pair_strips_7_global.json)
through $10^{44\,245\,906}$ is preserved. Its certified slabs are valid
without an upper restriction on the transverse exponent. At a boundary
with first power $P$, any potentially bad second power satisfies
$Q-D<P^{s/(s-r)}$, so every minimal CRT height is less than
$2P^{1+s/(s-r)}$. The horizontal boundary has the symmetric bound.
These bounds verify that neither the old height filter nor the old
prime-power caps truncated any boundary check.

The extension therefore starts at the retained final orthant and adds
eight anchors for each pair. It does not repeat the earlier large modular
inversions. The records name the original file and each retained
prefix, and the combination checker verifies that the continuation
reproduces the prefix's anchors, boundary checks and height cap.
A small continuation from cap $50$ to cap $1000$ reproduces the fresh
calculation's anchors, exceptions, and boundary hash for all three pairs.

To reproduce the final interval and combination steps using the already
retained source certificates, with the
[pinned dependencies](../../evidence/assets/erdos_699_interpolation_requirements.txt)
installed in the repository's `.venv/`:

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_7_finite_intervals.py
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_7_finite.py
```
