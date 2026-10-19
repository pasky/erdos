---
name: theory/integer_sequences/L271_repeated_simplex_extraction
title: Uniform extraction for repeated power-of-two simplexes
desc: The integer relation lattice of a repeated power-of-two simplex is semistable, and its normalized determinant stays above one at a critical tensor scale, giving one hereditary dissociation constant through the stated stable-lattice and phase-entropy theorems.
tags: [E0774, tensor, lattice, extraction]
sources:
- problems/integer_sequences/E0774
id: L271
statement: |
  Let S_q be the (q-1)-by-q integer matrix [I_(q-1) | -1], let
  A_(q,k) be its k-fold tensor power, and let K_(q,k) be the integer
  kernel in Z^(q^k), with Euclidean covolume in its real span.
  For q=2^b, b>=1, k>=1, put m=q^k-(q-1)^k. Every nonzero
  sublattice M of K_(q,k) satisfies
  det(M)^(1/rank(M)) >= det(K_(q,k))^(1/m)
  = q^(k(q-1)^(k-1)/(2m)).
  Moreover, for each fixed real c there are delta(c)>0 and q_0(c)
  such that whenever q=2^b>=q_0(c) and
  k=floor(q(log log q+log log log q+c)), every subset F of the
  columns of A_(q,k) contains a subset D with |D|>=delta(c)|F|
  having no nonzero relation with coefficients in {-1,0,1}.
  The logarithms in this schedule are natural. The extraction
  deduction consumes the author-recorded stable-lattice Gaussian
  theorem and finite phase-entropy criterion stated in the proof.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T23:24:37Z
updated: 2026-10-15T23:24:37Z
---

# Uniform extraction for repeated power-of-two simplexes

[[theory/integer_sequences/_index|..]]

[[theory/integer_sequences/L271_repeated_simplex_extraction/_proof|_proof]]: Boolean spectral compression and stochastic monotonicity under an empty-block condition prove semistability; fixed normalized covolume and the stated analytic interfaces give uniform hereditary extraction.

[[theory/integer_sequences/L271_repeated_simplex_extraction/evidence/_index|evidence/]]: Integer Smith forms and monomial Gram determinants check ten full relation lattices, all 254 spectral subfamilies in two small cases, and every downset in four small cases.

***

This theorem, recorded by Plasma AI, supplies a finite family with one
hereditary extraction constant while the number of repeated simplex
factors exceeds the side length by an unbounded factor. The
[proof](_proof.md) identifies its relation lattice with Boolean spectral
functions missing a whole block. A monotone coupling, followed by exact
spectral compression, proves semistability. The normalized covolume tends
to $\exp(e^{-c}/2)>1$ on the stated scale.

The extraction deduction uses the
[weak stable-lattice Gaussian theorem](../../../research/erdos_774/lemmas/stable_lattice_free_energy.md)
and the
[finite phase-entropy criterion](../../../research/erdos_774/routes/moment_phase_entropy.md)
at their author-recorded standing, including their explicitly stated
classical source premises. The proof states the exact uniform estimates
needed and the Gaussian/Rademacher source interface. No other native
L-claim is consumed.

## Standing

Proved at tier 0: the proof and the inherited arguments are author-recorded,
not independently accepted here. The
[local exact diagnostics](evidence/_index.md) check small spectral lattices,
conditional mean degrees and determinant formulas; they are not a finite
reduction of the unbounded theorem and do not replace its proof.
There is no claimed solution of Problem 774.

## Roadmap

The stated result has a complete author argument. At one fixed $c$,
unbounded actual dissociated covering of this family is the open
obligation in the
[[research/dissociated_covering_attack/proof_sketch|covering proof sketch]].
The entropy bound and limitations of algebraic colorings are explained in
the [[research/dissociated_covering_attack/repeated_simplex|research account]].
