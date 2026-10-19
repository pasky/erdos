---
name: research/erdos_699/proofs
title: "Erdős 699: why the completed cases are proved"
desc: "The mathematical argument and proof dependencies for i=1,2,7 and every i>=9, with a direct route to the retained certificates."
created: 2026-09-22T19:09:27Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: why the completed cases are proved

[[research/erdos_699/_index|..]]

[[research/erdos_699/proofs/details/_index|details/]]: Individual proof notes and the finite and infinite-range arguments they use.

***

[Erdős 699 research guide](../_index.md)

The completed conclusion is that every admissible triple with $i=1,2,7$
or $i\ge9$ has a common prime divisor $p\ge i$. This page explains the
proof by its mathematical ingredients. The case references below cover
all these indices without requiring the sequence of earlier cutoff
announcements.

## From a bad triple to incompatible size bounds

Write $c=n-j$, $S_i=\{p:p<i\}$, and

$$
\binom ni=U_i(n)V_i(n),
$$

where $U_i$ is supported on $S_i$ and every prime dividing $V_i$ is at
least $i$. The following steps are the common structure of the proofs.

**1. Local divisibility records a finite triangular grid.** Under
badness, each $q^a\Vert V_i(n)$ divides both $j-r$ and $c-s$ for some
nonnegative $r,s$ with $r+s<i$. Consequently an integer polynomial
vanishing to order $m$ on
$\Delta_i=\{(r,s):r,s\ge0,\ r+s<i\}$ satisfies

$$
V_i(n)^m\mid F(j,c).
$$

This is the central reduction in
[van Doorn and Rocca's detailed manuscript](../../../../library/factorials_binomials/van_doorn_rocca_2026_partial_progress_erdos_problem_699/_index.md).
Their explicit nonvanishing polynomials have degree-to-multiplicity ratio
less than $i-1$ for every $i\ge4$. Combining this with the sharp
$S_i$-part theorem proves finiteness. Its constant is ineffective, so
that argument alone does not give a stopping bound for computation.

**2. Explicit cofactor estimates replace the ineffective input.** For
each $p<i$, choose $r_p$ maximizing $v_p(n-r_p)$ and write

$$
n-r_p=P_pu_p,\qquad P_p=p^{v_p(n-r_p)}.
$$

The numerator factors differ by at most $i-1$. Padé approximation
therefore gives effective alternatives forcing some of their cofactors
$u_p$ to be large. The proof keeps these alternatives simultaneously,
with the actual prime labels and positions. Coincident positions are
included. At seven and nine, the
[adjustment of Padé blocks](../methods/details/pade_block_adjustment.md)
also makes the estimates valid low enough to meet the finite proof.

**3. Position-dependent polynomials give a strict exponent gain.**
Different multiplicities on the rows $r+s=t$ use more of the cofactor
information than one uniform multiplicity. The
[weighted polynomial argument](../methods/details/weighted_ramps.md)
is a concrete model. Harder cases use exact interpolation and rational
certificates showing that every permitted cofactor configuration gives
a positive gain. Nonvanishing must also be established: the
[interpolation lemma](../methods/details/jet_nonvanishing.md)
constructs a family whose members cannot all vanish in the physical
range, while some of the smallest indices use separate arithmetic
arguments. Coefficient bounds then turn the gain into a numerical
height above which bad triples are impossible.

**4. The remaining finite range is covered by inequalities on whole
intervals.** Local valuation bounds control $U_i(n)$ throughout an
interval of rows. On bounded height ranges,
[prime-power strip estimates](../methods/details/prime_power_strips.md)
give stronger cofactor bounds by solving congruences between powers of
small primes. Their exceptional solutions are retained and applied only
to the row windows they affect. An interval is excluded when its
small-prime upper bound contradicts the polynomial or discriminant
lower bound. Any residual individual rows are checked with exact
binomial gcd arithmetic. This proves coverage of the entire finite
range, even when its endpoint has millions of digits.

**5. The uniform large-index argument closes the infinite range of
indices.** An orbit polynomial has every coefficient divisible by
$\binom ni/\gcd(\binom ni,\binom nj)$. Its explicit discriminant gives
a lower bound on that gcd. Comparing it with a small-prime upper bound
confines the row; a prime in $(n-i,n]$ then divides both binomial
coefficients. The
[symmetric discriminant and interval proof](details/cutoff_and_cubic.md)
supplies the complete range $i\ge35$ and the additional case $i=29$,
including its dependence on the retained large-index argument and
explicit prime-gap results.

## Direct references for the completed cases

The rows of this table partition the completed indices. Each reference
includes its analytic inputs and links to the required finite records.

| Indices | Proof to read |
| --- | --- |
| $1,2$ | Proposition 2 of the detailed manuscript linked above. |
| $7$ | [Complete index-seven proof](details/index_7_complete.md). |
| $9$ | [Complete index-nine proof](details/index_9_complete.md). |
| $11,16$ | Complete proofs at [eleven](details/index_11_complete.md) and [sixteen](details/index_16_complete.md). |
| $12$ | [Complete index-twelve proof](details/index_12_complete.md). |
| $14$ | [Numerical tail](details/index_14_numerical_tail.md) together with the [finite proof](details/index_14_finite.md). |
| $10,13,15,18,19,20,21,22,24,25$ | [Combined interval proofs](details/further_interval_certificates.md), with the individual numerical tails linked there. |
| $17,23,26,27,28,30,31,32,33,34$ | [Ten complete interval certificates](details/effective_interval_certificates.md). |
| $29$ and every $i\ge35$ | [Discriminant and interval proof](details/cutoff_and_cubic.md). |

For the two most recently completed indices, the overlap is explicit:

| Index | Infinite-tail exclusion | Finite exclusion |
| --- | --- | --- |
| $7$ | $n-6\ge10^{100000000}$ | $n\le10^{100000001}$ |
| $9$ | $n-8\ge10^{241547627}$ | $n\le10^{241547629}$ |

Thus neither seven nor nine has an outstanding finite exceptional set.
The large displayed numbers are thresholds at which complementary
proofs meet, not unexamined search ranges.

## What the computational records establish

The small-index proofs combine exact integer and rational calculations
with directed bounds for analytic quantities. Modular ranks establish
rational interpolation claims; exact rational inequalities cover the
permitted cases; interval certificates and residual gcd checks exhaust
the finite ranges. The associated source theorems remain mathematical
inputs.

At seven and nine, the combined checkers bind the selected source data,
polynomial coverage, and finite certificates and verify their overlap.
By default they then regenerate every joint Padé witness sequence and
compare each direction's witness count and sequence digest with the
retained joint record; `--quick` skips that regeneration and says so.
The construction checked each interval, the individual replay drivers
regenerate the sequences on their own, and the initial-source drivers
can also reconstruct every pointwise coefficient-gcd bound. The proof
notes distinguish these longer replays from the combined checks. An
exact finite certificate is not, by itself, a completed Lean
formalization of the whole result.

The [computation guide](../computations/_index.md) gives the entry points
for reproducing the proofs. For the remaining mathematical questions,
return to the [research guide](../_index.md).
