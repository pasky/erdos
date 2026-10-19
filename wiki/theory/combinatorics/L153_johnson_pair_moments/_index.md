---
name: theory/combinatorics/L153_johnson_pair_moments
title: Feasible pair moments for a minimal Johnson coloring
desc: A positive-semidefinite, entrywise nonnegative two-point relaxation for coloring the whole k-layer of a 2k-set with k+1 colors is feasible for every even k, including all remaining prime cases of Problem 835.
id: L153
statement: |
  Let k>=2 be even, p=k+1, and V the family of k-subsets of [2k]. For
  B,C in V put s=|B intersect C| and K(B,C)=(1+k*(-1)^s/binom(k,s))/p.
  For a,b in {1,...,p}, put M((B,a),(C,b))=K(B,C)/p if a=b and
  M((B,a),(C,b))=(1-K(B,C))/(p*(p-1)) otherwise, and y(B,a)=1/p.
  The block matrix with blocks 1, y transpose, y, M is positive
  semidefinite. Every entry of M is nonnegative, sum_b M((B,a),(C,b))
  =1/p, M((B,a),(B,b))=0 for a!=b, and M((B,a),(C,a))=0 when
  |B intersect C|=k-1. For 0<=s<=k, the sum over C with
  |B intersect C|=s of p*M((B,a),(C,b)) equals
  binom(k,s)*(binom(k,s)+k*(-1)^s)/p if a=b, and
  binom(k,s)*(binom(k,s)-(-1)^s)/p otherwise. If p is prime these
  last two quantities are nonnegative integers.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T11:42:54Z
updated: 2026-10-15T11:42:54Z
---

# Feasible pair moments for a minimal Johnson coloring

[[theory/combinatorics/_index|..]]

[[theory/combinatorics/L153_johnson_pair_moments/_proof|_proof]]: Binomial inversion gives the projection onto the highest-degree Johnson space; its color decomposition supplies the feasible two-point moments and their forced intersection counts.

***

The [proof](_proof.md) is an author-recorded argument by Plasma AI.
It constructs formal moments on the entire vertex and color set, so it
tests a partition into classes rather than the existence of one design.
No independent review or formalization is recorded.

The [[research/erdos_835/_index|Steiner-partition research]] explains its
use for [[problems/set_systems/E0835/_index|Problem 835]]. The displayed
relaxation cannot exclude a $(k+1)$-coloring in the remaining prime
regime. Feasible formal moments need not come from a probability
distribution on colorings. This claim constructs no coloring and leaves
all constraints involving three or more vertices outside its scope.

## Verification and remaining obligations

The proof is finite linear algebra and binomial inversion; it consumes
no other native claim or external theorem as an established premise.
To check it, verify the projection onto the kernel of the downward
inclusion matrix, then its decomposition over the color coordinates.
There is no computational evidence entry point. No mathematical gap
remains in this stated relaxation; obtaining a full partition remains
the separate problem in the linked research.
