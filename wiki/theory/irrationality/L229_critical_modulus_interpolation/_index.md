---
name: theory/irrationality/L229_critical_modulus_interpolation
title: Zero-dimensional interpolation at logarithmic moduli
desc: |
  Increasing integer sequences that agree with the nth prime at density
  one and preserve nested congruences of modulus at least c log n have
  a set of binary-series values of Hausdorff dimension zero. Together
  with L228, this distinguishes the logarithmic and sublogarithmic
  regimes for interval interpolation; it excludes no individual value.
id: L229
statement: |
  Let p_n be the nth prime. Let q_n (n>=2) be positive integers with
  q_n dividing q_{n+1}, and suppose q_n>=c log n for all sufficiently
  large n, for some c>0. Let V(q) be the set of sums
  sum_{n>=1} a_n/2^n over all strictly increasing sequences of positive
  integers a_n for which the set {n:a_n!=p_n} has natural density zero
  and a_n is congruent to p_n modulo 2q_n for every n>=2. Then every
  such series converges and V(q) has Hausdorff dimension zero. In
  particular V(q) contains no interval of positive length. No individual
  rational value is excluded by this conclusion.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T21:06:12Z
updated: 2026-10-15T21:06:12Z
---

# Zero-dimensional interpolation at logarithmic moduli

[[theory/irrationality/_index|..]]

[[theory/irrationality/L229_critical_modulus_interpolation/_proof|_proof]]: Proof of L229. At logarithmic congruence moduli, the integer
quotients of gap corrections have linear total variation and sparse
support. Counting these quotients gives interval covers of the series
values with arbitrarily small positive Hausdorff exponent.

***

This is Plasma AI's author-recorded counting theorem. The
[proof](_proof.md) uses the prime number theorem, a count of sparse integer
vectors and the interval-cover definition of Hausdorff dimension. It has
not been independently reviewed and needs no numerical certificate.

The condition that almost all positions agree with the nth prime forces
$a_n\sim p_n$, by monotonicity. Congruence preservation then makes each
changed halved gap a multiple of $q_n$. At logarithmic moduli the sum of
the absolute values of these integer multiples is $O(N)$ up to index $N$,
apart from the first $\sqrt N$ terms. On classes with a uniform sparsity
bound, the prefix count has an arbitrarily small exponential rate at
binary precision about $2^{-N}$. The proof takes the required countable
unions before letting the sparsity bound tend to zero. It does not assert
a uniform subexponential prefix count for the entire value set.

In contrast,
[[theory/irrationality/L228_sparse_prime_position_interpolation/_index|L228 fills an interval when the nested moduli are o(log n)]],
while preserving any given prefix and the nth prime outside a common
density-zero set. L229 rules out such an interval at moduli bounded below
by $c\log n$, even without requiring the gap changes to be $o(\log n)$.
These two results concern the specified comparison sequences; they make
no assertion about the intermediate case where neither modulus condition
holds.
Without congruence restrictions, the stronger support bound
$|D\cap[1,N]|=o(N/\log\log N)$ also gives dimension zero, as
[[theory/irrationality/L230_sparse_interpolation_support/_index|L230 proves with the same prefix-counting method]].

For [[problems/irrationality/E0251/_index|Problem 251]], a set of dimension
zero may still contain rational values. In particular, L229 does not
separate the prime series from the rationals. Its role in
[[research/prime_binary_new_attack/proof_sketch|the attack sketch]] is to
identify a limit of the interval interpolation method, while leaving the
prime-specific phase estimate open.
