---
name: theory/irrationality/L228_sparse_prime_position_interpolation
title: Sparse interpolation preserving almost all prime positions
desc: |
  An interval of binary-series values is attained by increasing integer
  sequences agreeing with the nth prime outside one density-zero set,
  preserving nested congruences of modulus o(log n), and changing halved
  gaps by o(log n). In particular, such a sequence can have a dyadic
  rational sum. The altered terms need not be prime.
id: L228
statement: |
  Let p_n be the nth prime, p_1=2, and S=sum_{n>=1} p_n/2^n. Let q_n
  (n>=2) be positive integers with q_n dividing q_{n+1} and
  q_n/log n tending to zero. For every integer N>=2 there exist delta>0
  and a set D of positive integers of natural density zero such that for
  each real T in [S,S+delta] there is a strictly increasing sequence of
  positive integers a_n satisfying sum_{n>=1} a_n/2^n=T,
  a_n=p_n whenever n<=N or n is outside D, a_n>=p_n for every n,
  a_n congruent to p_n modulo 2q_n for every n>=2, a_n/p_n tending to
  one, and ((a_{n+1}-a_n)-(p_{n+1}-p_n))/log n tending to zero.
  The set D and delta are independent of T. Consequently a sequence with
  all these properties can have a dyadic rational sum strictly greater
  than S. If additionally q_n=O((log n)^alpha) for some 0<=alpha<1,
  D can be chosen with #{n<=M:n in D}=O(M/log log M).
  No primality assertion is made for its altered terms.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T20:52:57Z
updated: 2026-10-15T20:52:57Z
---

# Sparse interpolation preserving almost all prime positions

[[theory/irrationality/_index|..]]

[[theory/irrationality/L228_sparse_prime_position_interpolation/_proof|_proof]]: Proof of L228. Sparse positive corrections to halved gaps are matched
with later gaps that absorb equal negative corrections. A prime-pair
sieve bound makes the affected position intervals have density zero;
a greedy expansion controls the value of the binary series.

***

This is Plasma AI's author-recorded interpolation theorem. The
[proof](_proof.md) is complete but has not been independently reviewed.
Its external inputs are the prime number theorem and the classical
prime-pair upper bound stated at the beginning of McNew's proof of
Theorem 4.2, p. 10 of the preprint identified on
[[../library/primes/mcnew_2018_convex_hull_prime_number_graph/_index|the source card]].
That displayed bound was checked against the page image; its underlying
Brun-sieve proof is an external premise, not reconstructed here. The proof
derives the small-gap density estimate it uses from this precise bound.

For [[problems/irrationality/E0251/_index|Problem 251]], the result strengthens
the comparison-sequence obstruction in
[[research/prime_binary_new_attack/critical_length_obstructions|the critical-length notes]]:
the comparison can retain the actual value of the nth prime at density one,
not only its growth and short-block statistics. Taking $q_n=2^{K_n}$, with
$K_n$ nondecreasing and $2^{K_n}=o(\log n)$, also retains every residue
pattern of halved gaps of length at most $K_n$ at each start $n$.
The proof sketch explains
[[research/prime_binary_new_attack/proof_sketch|which prime-specific estimate remains missing]].

The result does not settle Problem 251. The interpolating sequences are
increasing integer sequences, and a nontrivial one cannot consist entirely
of primes: any increasing prime sequence starting at $2$ that skips a prime
has its nth term strictly above $p_n$ at every later index. Agreement with
$p_n$ at density one excludes that possibility.

The sublogarithmic condition has a precise role in this interpolation
statement. If instead $q_n\ge c\log n$ eventually for some $c>0$, the
divisibility $q_n\mid(h'_n-h_n)$ and $h'_n-h_n=o(\log n)$ force all
sufficiently late gap changes to vanish. Agreement with $p_n$ at density
one then forces all sufficiently late position changes to vanish too.
The attainable differences of series values are consequently dyadic
rationals and cannot fill an interval. This does not exclude any one
specified rational value.
Even without the small-gap-change requirement,
[[theory/irrationality/L229_critical_modulus_interpolation/_index|L229 gives a stronger interval obstruction]]:
at these logarithmic moduli all values from density-one agreement with
the prime positions form a set of Hausdorff dimension zero.
Independently of congruences,
[[theory/irrationality/L230_sparse_interpolation_support/_index|L230 limits how sparse the common exceptional set can be]]:
an interval construction cannot have
$|D\cap[1,N]|=o(N/\log\log N)$.
The quantitative clause of L228 attains $O(N/\log\log N)$ whenever
$q_n=O((\log n)^\alpha)$ for some fixed $\alpha<1$, including a fixed
modulus. Thus the achievable big-oh bound cannot be replaced by little-oh
for interval interpolation.

To check the claim, follow the proof's small-gap estimate, the choice of
paired changes, the density-zero argument and the greedy expansion. The
argument needs no numerical search or finite certificate. Its mathematical
obligations are closed at author-recorded standing; independent verification
remains absent.
