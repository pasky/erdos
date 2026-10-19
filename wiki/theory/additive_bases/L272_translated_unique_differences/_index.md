---
name: theory/additive_bases/L272_translated_unique_differences
title: Translated unique differences have subquadratic size
desc: |
  If k integers have distinct nonzero ordered differences and their
  difference set contains s+(W-W), where |s| exceeds the diameter of W,
  then |W| <= (3/2 + sqrt(2)) k^(5/3). An averaged sliding count gives
  the bound for every finite nonempty W.
tags: []
sources:
- problems/additive_bases/E0156
id: L272
statement: |
  Let A be a set of k >= 2 integers such that a-prime - a, over ordered
  pairs of distinct elements of A, are pairwise distinct. Let W be a
  finite nonempty set of integers, and let s be an integer with
  |s| > max(W) - min(W) and s + (W-W) contained in A-A. Then for every
  integer K >= 1,
  sqrt(|W|) <= k/sqrt(K) + ((K-1)/2) sqrt(2(k-1)).
  In particular, |W| <= (3/2 + sqrt(2)) k^(5/3).
status: proved
tier: 0
depends_on: []
created: 2026-10-15T23:58:19Z
updated: 2026-10-15T23:58:19Z
---

# Translated unique differences have subquadratic size

[[theory/additive_bases/_index|..]]

[[theory/additive_bases/L272_translated_unique_differences/_proof|_proof]]: A translated difference set forces a large sliding-count correlation.
Averaging disjoint windows bounds the count's norm and gives the
k^(5/3) estimate without a diameter restriction on the Sidon set.

***

This author-recorded result is due to Plasma AI. Its
[proof](_proof.md) averages translates of the sliding count
$F(j)=|A\cap(j+W)|$. It uses no external theorem or computational premise.

**Conventions and scope.** The differences are ordered and nonzero. For
integer sets their uniqueness is equivalent to the strong Sidon convention,
in which unordered pair sums include doubles. Neither the diameter nor the
location of $A$ is restricted. The separation condition concerns $s$ and
$W$, and is essential to the supplied averaging argument.

**Significance.** The
[[research/small_maximal_sidon_attack/translated_difference_sets|research
consequences bound progressions, combs and certain translated Bohr sets]]
inside $A-A$. In particular, a construction using one separated piece
$s+(W-W)$ of bounded doubling and translates by elements of $A$ cannot
cover an interval at the cube-root scale. This restricts that mechanism;
it neither proves nor disproves
[[problems/additive_bases/E0156/_index|Problem 156]].

L239 is a comparison, not a premise. Its hypothesis requires uniqueness
only for an initial interval of differences, and its conclusion has the
additional term $-2k+2$. The proof here also works under the restricted
representation hypotheses identified at its end; that observation
recovers L239's leading term without imposing global Sidonicity.

**Standing and verification.** Tier 0, without independent review or a
novelty determination. Check the sliding-count identity, the correlation
at shift $s$, disjointness of the $K$ windows, and the integer choice of
$K$. No mathematical obligation remains within this statement. The
[[research/small_maximal_sidon_attack/proof_sketch|integer construction
and compatible completion sought by the proof sketch]] remain open.
