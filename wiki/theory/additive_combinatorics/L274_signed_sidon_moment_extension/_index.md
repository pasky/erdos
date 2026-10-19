---
name: theory/additive_combinatorics/L274_signed_sidon_moment_extension
title: "Signed degree-four extension of Sidon moments"
desc: "For N at least 55, genuine fixed-cardinality moments through degree two have signed degree-four extensions satisfying every Sidon zero and cardinality identity; for N at least 58 the parity square can also be preserved. No matrix positivity is asserted."
id: L274
statement: |
  Let N>=55 and 0<=k<=N be integers, and let rho be any probability measure
  on the k-element subsets of {0,...,N-1}. There exists a real linear
  functional L on Boolean-reduced polynomials of degree at most four in
  z_0,...,z_(N-1) such that L agrees with E_rho in degrees at most two;
  L(z_S)=0 for every non-Sidon S with |S|<=4; and for every |T|<=3,
  sum_{x not in T} L(z_(T union {x}))=(k-|T|)L(z_T).
  Here z_S=product_{i in S}z_i, Boolean reduction means z_i^2=z_i, and
  strong Sidon means that equality of two sums, including repeated
  summands, implies equality of their unordered pairs.
  Moreover, if N>=58, L can be chosen so that for
  A=sum_{0<=i<j<N}(-1)^(i+j)z_i z_j one also has
  L((A-L(A))^2)=Var_rho(A).
status: proved
tier: 0
depends_on: []
created: 2026-10-16T00:29:25Z
updated: 2026-10-16T00:29:25Z
---

# Signed degree-four extension of Sidon moments

[[theory/additive_combinatorics/_index|..]]

[[theory/additive_combinatorics/L274_signed_sidon_moment_extension/_proof|_proof]]: Incidence Gram identities and bounded forbidden extensions give full row rank, the exact compatibility subspace, and a signed degree-four completion; a sixteen-support Sidon trade restores the parity square.

***

This is Plasma AI's complete author-recorded argument, without independent
review or formal verification. It constructs real signed moments and proves
their linear consistency. It does not assert nonnegativity of all quadratic
squares or give an extremal bound in
[[problems/additive_bases/E0030/_index|Problem 30]].

The [proof](_proof.md) counts forbidden extensions of pairs and Sidon triples.
The resulting incidence matrices have Gram lower bounds $N-13$ and $N-54$,
giving explicit right inverses. It also identifies exactly the compatibility
conditions on prescribed forbidden four-set data. A square kernel matrix
that ignores the relations from forbidden triples is singular, while these
compatible data admit a global correction.

For the parity refinement, the proof supplies an explicit eight-element
Sidon set, lists all its distinct positive differences and constructs a
signed trade on sixteen of its four-subsets. The trade has zero three-set
margins and changes the alternating square by a nonzero multiple. This
permits exact restoration of that one variance, without a parity restriction
on $N$.

The proof is self-contained and has no unresolved mathematical step. Its
matrix inequalities and finite witness are exposed directly; there is no
external source premise or computational reduction. The
[[research/sidon_extremal_error/signed_linear_completion|research account explains the global norm bounds and their limits]],
and the
[[research/sidon_extremal_error/local_repair_gap|local-repair analysis records the additional locality and spectral obligations]].
The
[[research/sidon_extremal_error/proof_sketch|editable proof sketch]]
keeps full matrix positivity and both halves of the extremal target open.
