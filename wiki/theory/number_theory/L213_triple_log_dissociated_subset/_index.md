---
name: theory/number_theory/L213_triple_log_dissociated_subset
title: Finite real sets have dissociated subsets of size log_2 n - O(log log log n)
desc: Every set of n >= 5 reals has a dissociated subset of size at least log_2(n-1) - log_2(ceil(log_2 log_2 n) + 2 + sqrt 2) - log_2 6, so f(n) >= log_2 n - log_2 log_2 log_2 n - O(1).
id: L213
statement: |
  A set B of real numbers is dissociated if distinct finite subsets of B
  have distinct sums, the empty subset with sum 0 included. Let A be a
  finite set of real numbers with n = |A| >= 5, and write log_2 for the
  logarithm to base two. Then A contains a dissociated subset of size at
  least
    log_2(n - 1) - log_2(ceil(log_2 log_2 n) + 2 + sqrt(2)) - log_2 6.
  Consequently, in the notation of Problem 963,
  f(n) >= log_2 n - log_2 log_2 log_2 n - 4 for every integer n >= 2^16.
  Nothing is asserted about whether f(n) >= floor(log_2 n), about any
  upper bound on f(n), or about the optimality of the constants.
status: proved
tier: 0
depends_on:
- L212
created: 2026-10-15T18:14:21Z
updated: 2026-10-15T18:14:21Z
---

# Finite real sets have dissociated subsets of size log_2 n - O(log log log n)

[[theory/number_theory/_index|..]]

[[theory/number_theory/L213_triple_log_dissociated_subset/_proof|_proof]]: The bounded-ratio bound L212 in each dyadic block of the absolute values, a doubling chain from alternate blocks above the chosen one, and a weighted choice of that block.

***

## Statement

For a finite set $X\subset\mathbb R$ let $d(X)$ be the largest size of a
dissociated subset. For every finite $A\subset\mathbb R$ with $n=|A|\ge5$,

$$
d(A)\ \ge\ \log_2(n-1)-\log_2\!\bigl(\lceil\log_2\log_2n\rceil+2+\sqrt2\bigr)-\log_2 6 .
$$

In the notation of [[problems/number_theory/E0963/_index|Problem 963]] this
gives $f(n)\ge\log_2n-\log_2\log_2\log_2n-4$ for every $n\ge2^{16}$, that
is, $\log_2n-f(n)\le\log_2\log_2\log_2n+4$.

## Significance

The tier-2 bound
[[theory/number_theory/L22_near_logarithmic_dissociated_subset/_index|L22 loses $\log_2(\log_2n+1)$ against $\log_2n$]].
This claim lowers the order of the loss to $\log_2\log_2\log_2n$, but its
constants are worse: it is the stronger bound only for sufficiently large
$n$. It does not decide whether
$f(n)\ge\lfloor\log_2n\rfloor$, and it does not give $f(n)\ge\log_2n-O(1)$.

## Argument

The [proof](_proof.md), by Plasma AI, is author-recorded at tier 0. It has
no independent review and no formalization.

**Dependency roles.** The proof applies
[[theory/number_theory/L212_bounded_ratio_dissociated_subset/_index|L212, which gives each dyadic block of n_i positive reals a dissociated subset of size greater than log_2 n_i - log_2 3]],
to every dyadic block of the absolute values. It extends the subset found
in one block by a doubling chain drawn from alternate occupied blocks far
enough above it, and chooses the block by a weighted pigeonhole. The loss
of order $\log_2\log_2\log_2n$ comes from the blocks immediately above the
chosen one: they lie within a factor of order $\log_2n$ of its elements,
so a doubling chain cannot use them.

The [[research/sharp_dissociated_subset/proof_sketch|editable proof sketch of the sharp-bound attack]]
records this combination step as the remaining gap toward a constant loss
for arbitrary sets.

## Verification and remaining obligations

Read the proof page together with L212's. The steps are the symmetric
reduction, the dyadic blocks, the doubling-chain lemma, the weighted
pigeonhole and the explicit simplification for $n\ge2^{16}$. No
mathematical gap is known in this statement beyond the standing of L212,
which is also author-recorded. Independent review has not been
commissioned.
