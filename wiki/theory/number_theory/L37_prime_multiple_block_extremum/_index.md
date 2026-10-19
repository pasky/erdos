---
name: theory/number_theory/L37_prime_multiple_block_extremum
title: The prime-multiple block extremum between two and three
desc: A two-half lower bound and a rectangular prime-grid construction give the exact minimum over prime sets for every number of primes.
id: L37
statement: |
  For every real alpha with 2<alpha<3 and every integer u>=1, the
  minimum, over all sets of u distinct primes with largest prime P and
  all blocks of floor(alpha P) consecutive positive integers, of the
  number of integers in the block divisible by at least one selected
  prime is ceil(2 sqrt(u)). Integers divisible by several primes count once.
status: proved
tier: 0
depends_on: []
created: 2026-10-14T18:42:37Z
updated: 2026-10-14T18:42:37Z
---

# The prime-multiple block extremum between two and three

[[theory/number_theory/_index|..]]

[[theory/number_theory/L37_prime_multiple_block_extremum/_proof|_proof]]: Distinct translates give the lower bound, and repeated prime patterns with Chinese remaindering attain it in an exact integer block.

***

The [proof](_proof.md) is a rectangular form of the Erdős–Selfridge
construction recorded in
[[../library/extremal_graph_theory/erdos_1978_problems_results_combinatorial_analysis_combinatorial_number/_index|Erdős's 1978 paper]],
Section 6, Theorem 1 and its lemma. The argument is given in full here,
using the prime number theorem and the Chinese remainder theorem.
This exposition and extension to arbitrary $u$ are author-recorded by
Plasma AI, with no novelty, independent review or Lean proof claimed.
The [[problems/primes/E1143/claims/1978_01_01_erdos_selfridge|earlier square-case claim]]
keeps its own credit and standing.

For [[problems/primes/E1143/_index|Problem 1143]], this determines the
extremum over prime sets for $2<\alpha<3$. It does not compute the
minimum for every prescribed prime set, and says nothing sharp for
$\alpha\ge3$. The
[[research/prime_multiple_interval_extrema/_index|research account]]
records these distinctions. Verification is the lower bound, repeated
prime-pattern count, congruence construction and integer endpoints;
there is no computational premise.
