---
name: theory/additive_bases/L239_consecutive_unique_differences
title: Consecutive uniquely represented differences have subquadratic length
desc: |
  If m integers represent every positive difference up to L exactly once,
  then L <= (3 + 2 sqrt(2)) m^(5/3) - 2m + 2, regardless of their
  diameter. Sliding interval counts and an elementary smoothing bound
  exclude a quadratic-length Sidon difference basis.
tags: []
sources:
- problems/additive_bases/E0156
id: L239
statement: |
  Let m >= 2 and L >= 0 be integers, and let B be a set of exactly m
  integers. Suppose that for every integer d with 1 <= d <= L there is
  exactly one ordered pair (b, b-prime) in B x B with b-prime - b = d.
  Then L <= (3 + 2 sqrt(2)) m^(5/3) - 2m + 2. No condition is imposed
  on the diameter of B or on representations of differences greater than L.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T20:36:53Z
updated: 2026-10-15T20:36:53Z
---

# Consecutive uniquely represented differences have subquadratic length

[[theory/additive_bases/_index|..]]

[[theory/additive_bases/L239_consecutive_unique_differences/_proof|_proof]]: Exact counts for overlapping and adjacent intervals give a small discrete
energy. Averaging translates of the resulting sequences bounds their
squared norm and gives the m^(5/3) estimate without a diameter bound.

***

This author-recorded result is due to Plasma AI. The
[proof](_proof.md) uses two exact sliding-interval counts and an
elementary inequality for finitely supported sequences. It uses no
external theorem or computational premise.

**Conventions and scope.** A representation of a positive difference has
the ordered form $d=b'-b$; its two entries are necessarily distinct.
The set $B$ need not be Sidon for differences larger than $L$. A strong
Sidon set, whose unordered pair sums include doubles, has at most one
representation of every positive difference and therefore satisfies the
hypothesis whenever $[1,L]\subseteq B-B$. Negative elements of $B$ are
allowed, and neither its location nor its diameter enters the bound.

**Significance.** Along any family with $m\to\infty$, the conclusion
implies $L/m^2\to0$. Thus the
[[research/small_maximal_sidon_attack/integer_transfer|proposed integer
transfer using a quadratic-length Sidon difference basis]] cannot work.
This does not refute
[[problems/additive_bases/E0156/_index|Problem 156]]: maximality involves
$A+A-A$ and midpoints, and different translates of a difference set or
interactions among added points can cover one another's gaps. The
[[research/small_maximal_sidon_attack/consecutive_differences|research
extension allows missing differences]] and records that separate scope.

**Standing.** Tier 0, with no independent review or novelty determination
recorded. Verification consists of checking the two interval identities,
the averaged norm inequality, and the choice of the integer smoothing
parameter in the proof. No mathematical obligation remains inside this
statement; the interval construction sought in the
[[research/small_maximal_sidon_attack/proof_sketch|editable proof sketch]]
remains open.
