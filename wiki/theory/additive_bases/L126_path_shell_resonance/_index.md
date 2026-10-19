---
name: theory/additive_bases/L126_path_shell_resonance
title: Logarithmic representation peaks in admissible path shells
desc: |
  Every prescribed large path can be paired with admissible smaller paths
  giving logarithmically many distinct representations of one integer.
  One infinite path family realizes such peaks, so local increment
  restrictions alone cannot give a uniform bound against all earlier shells.
tags: []
sources:
- problems/additive_bases/E1145
id: L126
statement: |
  A path h_q on {0,...,4*q} is admissible if h_q(0)=0, all its increments
  are 1 or 2, and its increment word contains neither 111 nor 22. Define
  A_q = {q^2+q*x+h_q(x)+d: 0 <= x <= 4*q, d in {0,1,2,3}} and
  B_q = {q^2+q*y-h_q(y)+e: 0 <= y <= 4*q, e in {0,1,2,3}}.
  For every integer k >= 26, Q=2^k, and every admissible h_Q, there are
  admissible paths h_q for all q=2^j with ceil(k/2)+4 <= j <= k-8 such
  that n=3*Q^2+h_Q(2*Q) has at least floor(k/2)-11 distinct ordered
  representations (a,b) in A_Q times the union of these B_q.
  Moreover, there is a choice of admissible h_q for every
  q in {2^j, 3*2^(j-1): j >= 4} such that, for A the union of all A_q
  and B the union of all B_q, there are integers n tending to infinity
  with r_{A,B}(n) >= (log_2 n)/4 - 13, where r counts ordered pairs.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T11:57:22Z
updated: 2026-10-15T11:57:22Z
---

# Logarithmic representation peaks in admissible path shells

[[theory/additive_bases/_index|..]]

[[theory/additive_bases/L126_path_shell_resonance/_proof|_proof]]: A lattice choice of the small index fixes the carry, and a prefix made
from 12 and 112 realizes the required height. The resulting sums agree
exactly while their small summands lie in disjoint scale intervals.

***

This result is author-recorded by Plasma AI. The
[proof](_proof.md) constructs exact integer representations; it needs no
numerical search. Its scope is an obstruction to a bound valid for
**every** admissible choice of paths. It is not an obstruction to every
globally coordinated choice.

The [[research/erdos_1145/monotone_path_shells|path-shell construction]]
proves balance and cofinite coverage for every admissible family, and an
$O(\log n)$ representation bound. This claim shows that the logarithmic
bound is attained in order of magnitude within that class, even when the
large path at each selected scale is prescribed in advance. The
[[research/erdos_1145/prefix_resonance|research account]] explains why
this leaves the uniform whole-prefix condition open. No bounded
representation construction or answer to
[[problems/additive_bases/E1145/_index|Problem 1145]] is asserted.

Tier 0, with no independent review. Verification consists of checking the
integer lattice choice of $y$, admissibility of the constructed prefix,
the exact sum identity, and distinctness of the representations. There is
no remaining obligation inside this statement.
