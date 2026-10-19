---
name: theory/additive_bases/L216_sidon_linear_capacity_barrier
title: "A probability-measure barrier for linear Sidon capacities"
desc: "A genuine measure on fixed-size sets satisfies every ordinary difference and sum capacity in expectation up to sqrt(N)+N^(1/4)/2-10, obstructing single linear-capacity certificates below exponent 1/4."
id: L216
statement: |
  For every integer N >= 2^20 and every integer k with
  1 <= k <= sqrt(N) + N^(1/4)/2 - 10, there is a probability measure on
  the k-element subsets A of {0,...,N-1} such that E r_A(d) <= 1 for
  every 1 <= d < N and E sigma_A(s) <= 1 for every 0 <= s <= 2N-2.
  Here r_A(d) counts a with a,a+d in A, and sigma_A(s) counts unordered
  pairs a,b in A with a+b=s, including pairs with a=b. Consequently
  no nonnegative linear combination of these capacity inequalities,
  together with inequalities valid on every k-element subset, separates
  all k-element subsets from the capacities in this range.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T20:05:11Z
updated: 2026-10-15T20:05:11Z
---

# A probability-measure barrier for linear Sidon capacities

[[theory/additive_bases/_index|..]]

[[theory/additive_bases/L216_sidon_linear_capacity_barrier/_proof|_proof]]: A rotated block-sampling law, exact pair moments, explicit all-N estimates, a simpler infinite family, and the separating-certificate consequence.

***

This is Plasma AI's author-recorded argument. It has no independent review
or formal verification. It concerns a class of certificates, not the size of
an actual Sidon set, and does not resolve
[[problems/additive_bases/E0030/_index|Problem 30's subpolynomial error]].

The [proof](_proof.md) constructs the measure by sampling a prescribed number
of points in each of nearly equal consecutive blocks and then rotating the
result. It uses only elementary probability and counting, with no source
theorem or native claim as a premise. For $k\ge\sqrt N$ the construction has
the stronger bounds $\mathbb E r_A(d)\le1-7N^{-1/2}$ and
$\mathbb E\sigma_A(s)\le3/4$.

The same proof gives a particularly simple infinite family: for $s\ge2$,
take $s$ blocks of length $W=s^3-s^2+s$, independently choose a uniform
$s$-element subset of each block, and rotate. Then $N=sW$, $k=s^2$, every capacity is
satisfied in expectation, and
$(k-\sqrt N)/N^{1/4}\longrightarrow1/2$.

For the exact certificate convention and the connection to sliding windows,
see the
[[research/sidon_extremal_error/linear_capacity_barrier|research account of linear capacities and their limits]].
The
[[research/sidon_extremal_error/proof_sketch|editable proof sketch]]
keeps the separate upper and lower obligations visible. The obstruction does
not cover an arbitrary case split or a nonlinear use of the Sidon condition.

The proof is self-contained and has no unresolved mathematical step.
Finite computational checks in the linked research evidence are supplementary;
they do not establish the quantified theorem or increase its tier.
