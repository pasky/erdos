---
name: theory/irrationality/L230_sparse_interpolation_support
title: A support bound for prime-position interpolation
desc: |
  The binary-series values of increasing integer sequences that change
  only o(N/log log N) of the first N prime positions form a set of
  Hausdorff dimension zero. No congruence condition is required. Thus
  an interval interpolation cannot have a common exceptional set this
  sparse, although an individual rational value is not excluded.
id: L230
statement: |
  Let p_n be the nth prime. Let V be the set of sums sum_{n>=1} a_n/2^n
  over all strictly increasing sequences of positive integers a_n such
  that #{n<=N:a_n!=p_n}=o(N/log log N) as N tends to infinity. Then each
  such series converges and V has Hausdorff dimension zero. Consequently
  a set D with #{n<=N:n in D}=o(N/log log N) cannot support an interval
  of binary-series values by changing p_n only at indices in D while
  preserving strict increase and positivity. No individual rational
  value is excluded by this conclusion.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T21:15:43Z
updated: 2026-10-15T21:20:52Z
---

# A support bound for prime-position interpolation

[[theory/irrationality/_index|..]]

[[theory/irrationality/L230_sparse_interpolation_support/_proof|_proof]]: Proof of L230. The integer changes to consecutive differences have
total variation O(N log N) and support o(N/log log N). Uniform support
bounds give binary-scale covers with arbitrarily small positive
Hausdorff exponent; countable unions give the full dimension bound.

***

This is Plasma AI's author-recorded counting argument. The
[proof](_proof.md) uses the prime number theorem and elementary counts
of sparse integer vectors. It has not been independently reviewed.
No congruence condition is assumed, and no numerical evidence is needed.

[[theory/irrationality/L228_sparse_prime_position_interpolation/_index|L228 attains an interval while changing prime positions on a density-zero set]].
The exceptional set in any such interval construction must fail the
stronger bound $o(N/\log\log N)$, even if the interval and the set depend
on a prescribed initial prefix. L228 achieves $O(N/\log\log N)$ when
the nested moduli satisfy $q_n=O((\log n)^\alpha)$ for some fixed
$\alpha<1$, including when there is no congruence restriction beyond
parity. The attainable big-oh bound therefore cannot be improved to
little-oh for interval interpolation. In a complementary direction,
[[theory/irrationality/L229_critical_modulus_interpolation/_index|L229 obtains dimension zero from logarithmic congruence moduli]]
with only the density-zero support assumption.

Among starts $1\le n\le N$, put $m=|D\cap[1,N+K]|$. The changed
positions can affect at most $(K+1)m$ exact blocks of $K$ gaps.
Thus $m=o(N/\log\log N)$ is a sufficient support bound to retain such
blocks at almost every start when $K=O(\log\log N)$. L230 prevents an
interval interpolation with that support bound. It does not prove that
the bound is necessary for preservation of block laws: changed windows
can overlap, and distributional cancellations can occur.

The remaining arithmetic question is separate. A set of Hausdorff
dimension zero may contain a given rational number. The theorem
therefore does not settle
[[problems/irrationality/E0251/_index|Problem 251]], nor does it rule out
a sparse construction for one specified rational target. The
[[research/prime_binary_new_attack/proof_sketch|attack sketch]] retains
that limitation.
