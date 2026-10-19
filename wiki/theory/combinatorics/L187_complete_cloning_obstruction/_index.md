---
name: theory/combinatorics/L187_complete_cloning_obstruction
title: Obstructions to complete clone-class amplification
desc: Fano caps obstruct complete cloning for each seed, and seven parity rows exclude every nontrivial clone expansion that would retain both the local seven-edge property and a ratio above three quarters.
id: L187
statement: |
  Let H be a nonempty finite k-uniform set family with k>=1, and let
  1<=s<=N be integers. Replace each ground point by a disjoint N-point
  class and each edge by all unions of independently chosen s-subsets
  in its classes; call the expansion C(H). Write P7 for the property
  that every subfamily of at most seven edges has a transversal of
  size at most two. Then C(H) has rank ks and transversal number
  (N-s+1)tau(H). If N>=7ceil(s/4), it fails P7. Consequently, if it
  has P7 then tau(C(H))/(ks) <= (tau(H)/k)(3/4+21/(4s)).
  In particular, let q>=10, |V|=7q+1, |X|=4q, and
  H={E subset V: |E|=4q and |E intersect X| is odd}. If 3N>=4s,
  C(H) fails P7. If C(H) has P7 and s>=2, its transversal-to-rank
  ratio is at most 31/80<3/4. If s=1 and it has P7, then N=1.
  Thus no nontrivial complete clone-class expansion of this parity
  seed has both P7 and transversal-to-rank ratio above 3/4.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T17:09:48Z
updated: 2026-10-15T17:09:48Z
---

# Obstructions to complete clone-class amplification

[[theory/combinatorics/_index|..]]

[[theory/combinatorics/L187_complete_cloning_obstruction/_proof|_proof]]: The transversal product formula, seven Fano-cap spectra and seven distinct parity rows prove the complete-cloning obstruction.

***

The [proof](_proof.md) is author-recorded Plasma AI work, without independent
review or Lean proof. It concerns the expansion containing **every** allowed
$s$-subset in every class. It does not exclude selected inner families or
other amplification operations, nor does it resolve
[[problems/set_systems/E0644/_index|Problem 644]].

The parity family is the construction of Fon-Der-Flaass, Kostochka and
Woodall, described with its source standing in the
[[research/erdos_644/convex_profile_amplification|amplification research account]].
The obstruction is a distinct deduction about complete cloning; the proof
below uses only the explicit parity-family definition and an elementary
transversal upper bound. It assumes neither the source's $P_7$ theorem
nor its exact transversal number. No native L-claim is consumed.

**Conventions.** A transversal is a set meeting every edge. $P_7$ tests
at most seven distinct edges. Each constructed obstruction also defeats
the exactly-seven convention: the expanded family has at least seven
edges, and a smaller bad subfamily can be extended.

**Verification.** Read the exact covering criterion, the Fano-cap incidence
construction and the seven cyclic parity rows in the proof. All arithmetic
and constructions are explicit and need no artificial computation.
No gap remains in the stated obstruction at author standing. The
unrestricted amplification and extremal questions remain open.
