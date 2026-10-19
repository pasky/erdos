---
name: theory/additive_bases/L125_random_singer_lift_residual
title: Random Singer lifts leave a linear residual at the cube-root scale
desc: |
  Uniform independent lifts of a perfect difference set leave linearly many
  integer targets unblocked with probability tending to one when p cubed is
  comparable to N. The proof uses bounded dependence and includes doubles
  and integer carries; it does not exclude structured lifts or small repairs.
tags: []
sources:
- problems/additive_bases/E0156
id: L125
statement: |
  Let p be prime, q = p^2+p+1, s = p+1, N a positive integer, and
  M = floor(N/q) >= 16. Let B = {b_1,...,b_s} be a subset of {1,...,q}
  whose ordered differences b_i-b_j, i != j, represent every nonzero
  residue modulo q exactly once. Choose d_1,...,d_s independently and
  uniformly from {0,...,M-1}, and set A_0 = {b_i+q*d_i: 1 <= i <= s}.
  Let W be the number of integers m in {1,...,N} whose residue modulo q
  is outside B, and let U be the number of these m for which neither
  m is in A_0+A_0-A_0 nor 2*m is in A_0+A_0. Put
  beta = (1-2/M)^(s+1) and L = 6*s^2+2*s. Then A_0 is strong Sidon
  (unordered pair sums including doubles are distinct), E[U] >= W*beta,
  Var(U) <= s*L^2, and, if W > 0,
  P(U < W*beta/2) <= 4*s*L^2/(W^2*beta^2).
  Consequently, for any fixed positive a <= b, along N,p with
  a*p^3 <= N <= b*p^3 and p tending to infinity, there is c > 0 depending
  only on a,b such that P(U >= c*N) = 1-O(1/p), uniformly in B.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T11:57:22Z
updated: 2026-10-15T11:57:22Z
---

# Random Singer lifts leave a linear residual at the cube-root scale

[[theory/additive_bases/_index|..]]

[[theory/additive_bases/L125_random_singer_lift_residual/_proof|_proof]]: Each target has a blocking-event dependency graph of maximum degree four.
An elementary local-lemma induction bounds its probability of remaining
unblocked below, and a bounded-difference variance estimate gives a
linear residual with probability tending to one.

***

This author-recorded result is due to Plasma AI. The
[proof](_proof.md) is elementary and noncomputational. It supplies the
random-lift obstruction in the
[[research/erdos_156/uniform_coverage|coverage-and-repair argument for Problem 156]].
The hypotheses concern exact integer blockers and the strong Sidon
convention, including doubles.

The conclusion excludes obtaining an $O(p)$ initial residual with high
probability from uniform independent lifts at $p^3\asymp N$. It does not
exclude exceptional choices of the lifts. Nor does a large initial residual
imply that every maximal completion needs more than $O(p)$ new elements:
each added element can block many old targets, and relations among added
elements are not bounded here. No conclusion about
[[problems/additive_bases/E0156/_index|Problem 156 itself]] follows.

Tier 0. No independent review is recorded. Verification consists of reading
the proof, particularly the degree-four dependency graph and the bounded
change estimate. There is no remaining obligation inside the stated scope.
