---
name: theory/set_systems/L268_linear_word_sunflowers
title: Exponential sunflower bounds for affine linear words
desc: |
  A linear word space of dimension at least sn contains an s-dimensional
  subspace whose coordinate maps are zero or injective. Consequently an
  affine linear word family without a k-sunflower has fewer than k^(2n)
  members, uniformly over finite fields and coordinate alphabet dimensions.
id: L268
statement: |
  Let q be a prime power, n >= 1 an integer, A_1,...,A_n finite-dimensional
  vector spaces over F_q, and C a linear subspace of their direct sum.
  A word c=(c_1,...,c_n) represents the n-element set
  S(c)={(i,c_i):1 <= i <= n}. A k-sunflower consists of k distinct such
  sets whose pairwise intersections all equal one set, which may be empty.
  For every integer s >= 1, if dim C >= sn, there is an s-dimensional
  subspace U of C such that each coordinate projection restricted to U is
  either zero or injective. For every a in the direct sum, the q^s sets
  S(c), c in a+U, form a q^s-sunflower. Consequently, for every integer
  k >= 3 and every a in the direct sum, if the family of sets S(c),
  c in a+C, contains no k-sunflower, then |C| < k^(2n). More precisely,
  dim C < n ceil(log_q k) and |C| <= q^(n ceil(log_q k)-1); if q >= k,
  then C={0} and the affine family has one member.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T21:21:39Z
updated: 2026-10-15T21:21:39Z
---

# Exponential sunflower bounds for affine linear words

[[theory/set_systems/_index|..]]

[[theory/set_systems/L268_linear_word_sunflowers/_proof|_proof]]: Maximize the deficit between the desired dimension and the span of
coordinate dual spaces, contract that span, and apply linear Hall
selection. Dualizing gives a subspace whose coordinates are zero or
injective and whose affine cosets are sunflowers.

***

This argument is recorded by Plasma AI. The
[[theory/set_systems/L268_linear_word_sunflowers/_proof|proof]]
is self-contained: a linear independent-representative criterion and a
maximal dimension-deficit argument construct the required subspace.

The independent-representative criterion is the classical linear version
of Hall's condition. No novelty is claimed for that criterion or for the
structured sunflower bound without a fuller literature comparison. No
external theorem or other project claim is a premise: the needed
selection argument is proved in full.

## Significance and scope

The coordinate alphabets can have arbitrarily large dimensions, so the
base $k^2$ is independent of the alphabet size. This proves the exponential
bound for an algebraically structured subclass of the word formulation of
[[problems/set_systems/E0020/_index|Problem 20, the sunflower conjecture]].
It does not prove the conjecture for arbitrary families. Passing from an
arbitrary word family to its affine span can introduce new words and new
sunflowers.

The
[[research/sunflower_exponential_bound/linear_word_families|linear-word research note]]
uses cosets of the constructed subspace to obtain an exponential bound
for subsets of fixed positive density in an affine linear family. The
[[research/sunflower_exponential_bound/additive_word_families|additive-growth deduction]]
then handles binary word families with bounded fourfold growth. Those
extensions retain author standing; their hypotheses do not hold for all
word families. The
[[research/sunflower_exponential_bound/proof_sketch|general proof sketch]]
records the missing structural reduction.

## Standing and verification

Tier 0, author-recorded. The proof is complete and noncomputational. No
independent review or formalization exists. To verify it, check the
independent-representative induction, the choice of a proper maximizing
coordinate set even when $\dim C=sn$, the dual construction, and the
conversion of its subspace to a sunflower. The final field-size split
gives the uniform exponential base.

Nothing remains open within this structured statement. The unrestricted
sunflower conjecture and any novelty assessment remain outside its
conclusion.
