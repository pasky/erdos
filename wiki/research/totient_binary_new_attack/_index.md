---
name: research/totient_binary_new_attack
title: A Fresh Attack on the Binary Totient Series
desc: |
  Exact base-two attack with quantitative kernel shadows, rational comparisons
  preserving prime-power values and any fixed finite set of prime laws, a
  support-independent bound for robust odd kernels, and scoped dilation and
  residue-lifting obstructions. The irrationality question remains open.
tags: []
sources: []
problems:
- 249
created: 2026-10-15T19:52:41Z
updated: 2026-10-15T21:48:35Z
---

# A Fresh Attack on the Binary Totient Series

[[research/_index|..]]

[[research/totient_binary_new_attack/dilation_designs|dilation_designs]]: A signed combination of prime dilations that cancels the first K levels of
the shift tail for every function uses at least K+1 distinct primes, so its
Chinese-remainder modulus exceeds K^(K+1). When that modulus is at most
the averaging scale, the cancelled levels form a vanishing fraction of
a logarithmic window.

[[research/totient_binary_new_attack/evidence/_index|evidence/]]: Exact finite checks of kernel shadows, retained fixed-prime robust vectors,
complete smooth-orbit rounding, sparse comparisons, dilation designs and
residue-lifting inequalities, with explicit limits on their coverage.

[[research/totient_binary_new_attack/kernel_rigidity|kernel_rigidity]]: On the short support [J,2J] the shadow u of every vector is fixed by its
window coefficients at any complementary pair. Fixed-prime robust vectors
have u=0 for sufficiently large even J. At suitable powers of two the
kernel shadows fill 2^J Z x 2Z, giving two quantitative implications between
odd cost and inhomogeneous approximation of S.

[[research/totient_binary_new_attack/partial_multiplicativity|partial_multiplicativity]]: Comparisons with dyadic binary sums preserve all prime-power values and
every totient multiplication law at finitely many fixed primes. They give
an exponential cost bound for robust odd kernels without restricting the
length of their supports.

[[research/totient_binary_new_attack/perturbation_barrier|perturbation_barrier]]: Sparse changes bounded by the square root except at one place, preserving
growing powers of two, give the binary series any real value. The
construction preserves empirical distributions of o(log N) windows up to
o(1), delimiting arguments that use only these shared properties.

[[research/totient_binary_new_attack/proof_sketch|proof_sketch]]: Exact base-two target and complete-tail criterion, quantitative kernel
shadows, rational comparisons preserving all prime-power values and fixed
prime laws, scoped construction obstructions, and the remaining estimates.

[[research/totient_binary_new_attack/residue_lifting|residue_lifting]]: Residue truncations approach the totient sum exponentially fast, but a zero
block occurs only after the first altered coefficient. Rescaling there
amplifies the positive truncation error to at least half the modulus.

***

This folder concerns [[problems/irrationality/E0249/_index|Problem 249]],
the irrationality of $\sum_{n\ge1}\varphi(n)2^{-n}$. Its original results
are Plasma AI's, author-recorded and without independent review. It uses
specified results of the
[[research/leads/totient_binary_series/_index|existing lead]] at their
recorded standing. The
[[research/totient_binary_new_attack/proof_sketch|editable proof sketch]]
carries the exact target, held implications, limitations and open steps.
There is no proposed solution here.

The [[research/totient_binary_new_attack/kernel_rigidity|kernel page]]
computes the possible shadows on $[J,2J]$ at suitable powers of two and
gives quantitative implications between odd-vector cost and
inhomogeneous approximation of $2^{J-2}S$. It does not prove the required
asymptotic approximation estimate.

The strongest comparison is
[[theory/irrationality/L220_partial_multiplicativity_interval/_index|L220]]:
positive integer functions can preserve every prime-power value and the
exact totient multiplication laws at any fixed finite set of primes,
remain arbitrarily close in relative size, and have any binary sum in an
interval about $S$. The
[[research/totient_binary_new_attack/partial_multiplicativity|application
to robust kernels]] uses a dyadic rational in that interval to bound odd
kernel costs on supports of arbitrary length. A growing prime set or
additional rough-composite relations remains outside its strongest bound.

The [[research/totient_binary_new_attack/perturbation_barrier|sparse
comparison]], based on
[[theory/irrationality/L218_sparse_perturbation_any_value/_index|L218]],
preserves empirical distributions of $o(\log N)$ windows up to $o(1)$,
while allowing any real binary sum. The
[[research/totient_binary_new_attack/dilation_designs|dilation design
bound]], based on
[[theory/irrationality/L219_dilation_design_prime_count/_index|L219]],
limits formal level cancellation when the Chinese-remainder modulus fits
the averaging scale. The
[[research/totient_binary_new_attack/residue_lifting|residue-lifting
note]] identifies the positive error that prevents a direct transfer from
bounded-residue zero blocks. Each obstruction is restricted to its stated
mechanism.

All three claim cards remain at tier 0. The
[[research/totient_binary_new_attack/evidence/_index|finite evidence]]
checks lattice examples, retained robust vectors, complete-orbit rounding
bounds, small dilation designs and the residue-lifting inequalities. It
supplies no unbounded family of successful irrationality certificates.

A related comparison mechanism appears in
[[research/prime_binary_new_attack/_index|the prime binary-series research]]:
its increasing integer sequences preserve almost all prime positions and
nested sublogarithmic congruences while their sums fill a one-sided interval.
Here the preserved properties are prime-power values and fixed-prime
multiplication laws. The two constructions test different coefficient
classes; neither proves a transfer between the irrationality questions,
and neither comparison preserves all defining arithmetic information.
