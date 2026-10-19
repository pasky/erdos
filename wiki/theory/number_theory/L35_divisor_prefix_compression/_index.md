---
name: theory/number_theory/L35_divisor_prefix_compression
title: Compressing a divisor prefix to its least common multiple
desc: An exact finite partition formula computes the least integer realizing a prescribed divisor-prefix sum, with complete values through 64.
id: L35
statement: |
  For an integer N>=2, the least positive integer n having a prefix of its
  increasing divisors greater than 1 with sum N equals the minimum lcm(P)
  over partitions P of N into distinct integers at least 2 for which the
  divisors of lcm(P) between 2 and max(P) are exactly P; if the family is
  empty, no such n exists. For 2<=N<=64 this family is empty exactly when
  N=4, and the largest of these least integers is 265, attained at N=58.
status: proved
tier: 0
depends_on: []
created: 2026-10-14T18:42:37Z
updated: 2026-10-14T18:42:37Z
---

# Compressing a divisor prefix to its least common multiple

[[theory/number_theory/_index|..]]

[[theory/number_theory/L35_divisor_prefix_compression/_proof|_proof]]: Taking the least common multiple preserves a divisor prefix, making exhaustive minimization finite for each target sum.

[[theory/number_theory/L35_divisor_prefix_compression/evidence/_index|evidence/]]: Exhaust all distinct-part partitions, check their counts independently, and compare the minima with an exact divisor sieve.

***

The [proof](_proof.md) gives the exact reduction and the
[[theory/number_theory/L35_divisor_prefix_compression/evidence/_index|executable evidence]]
exhausts its finite domain for $2\le N\le64$. This is author-recorded
work by Plasma AI with no independent review or Lean proof recorded.

For [[problems/divisors/E0468/_index|Problem 468]], the calculation
determines the minimum over all original integers $n$, rather than
over a bounded search in $n$. It gives no asymptotic estimate for
$f(N)$ and no general count of newly occurring prefix sums. In particular,
finite values exceeding $N$ do not decide $f(N)=o(N)$.

Run the command on the evidence page from the repository root.
The exact table, witnesses and input interval are retained with the
checker; successful cached output is not a substitute for rerunning it.
