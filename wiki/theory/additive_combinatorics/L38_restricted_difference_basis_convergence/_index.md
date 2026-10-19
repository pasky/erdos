---
name: theory/additive_combinatorics/L38_restricted_difference_basis_convergence
title: Restricted difference bases converge after an endpoint patch
desc: A Singer lift and an explicit endpoint patch prove convergence of the restricted difference-basis ratio and an infimum formula with an additive two.
id: L38
statement: |
  For an integer N>=1, let F(N) be the least cardinality of a subset A of
  {0,...,N} such that {0,...,N} is contained in A-A. For every integer n>=1,
  limsup as N tends to infinity of F(N)/sqrt(N) is at most
  (F(n)+2)/sqrt(n+1). The sequence F(N)/sqrt(N) converges to a finite limit L,
  and L=inf over integers n>=1 of (F(n)+2)/sqrt(n+1).
status: proved
tier: 0
depends_on: []
created: 2026-10-14T20:10:13Z
updated: 2026-10-14T20:10:13Z
---

# Restricted difference bases converge after an endpoint patch

[[theory/additive_combinatorics/_index|..]]

[[theory/additive_combinatorics/L38_restricted_difference_basis_convergence/_proof|_proof]]: The modular carry covers the initial interval, a square-root-cost patch covers the endpoint, and a liminf subsequence closes the convergence argument.

***

This is an author-recorded argument by Plasma AI. It uses Singer's perfect
difference sets and the prime number theorem as classical external premises.
Their exact specializations are stated in the [proof](_proof.md); no
independent review or formal proof is claimed.

The restriction that every mark lies in $[0,N]$ is essential. A modular
difference cover is lifted only through $nq$, and a separate set of marks
covers the remaining interval. The added cost yields the $+2$ in the formula.

[[problems/additive_combinatorics/E0170/_index|Problem 170 asks for the value
of this limit]], which is not determined here. The result does not assert
that $L=\inf_n F(n)/\sqrt n$, the infimum printed by Erdős and Gál, or
recover their printed numerical upper bound.
[[research/leads/restricted_difference_basis_limit/_index|The research
account explains the covering gap and the remaining constant problem]].

Verification is by reading the proof, particularly the modular carry, the
placement of the endpoint marks and the order of the two limits. No finite
computation is a premise. Independent examination remains outstanding.
