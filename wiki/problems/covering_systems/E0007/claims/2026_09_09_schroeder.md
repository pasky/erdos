---
name: problems/covering_systems/E0007/claims/2026_09_09_schroeder
title: Schroeder's obstruction for three prime divisors per modulus
desc: A pending claim excludes distinct odd covering systems when every modulus has at most three prime divisors, without bounding the total prime support.
authors:
- Michael Schroeder
status: claimed
claim: disproved
scope: partial
published: 2026-09-09
submitted: 2026-09-15
links:
- url: https://michaelschroeder.ai/research/ThreePrimeDivisors/three_prime_factors_per_modulus.pdf
  kind: preprint
  date: 2026-09-09
- url: https://michaelschroeder.ai/#research
  kind: record
- url: https://www.erdosproblems.com/forum/thread/7#post-9056
  kind: discussion
  date: 2026-09-15
created: 2026-10-16T12:22:34Z
updated: 2026-10-16T12:22:34Z
---

***

**Claim.** Michael Schroeder's *Noncoverage for Distinct Odd Moduli with at
Most Three Prime Divisors* asserts that a finite family of residue classes
with distinct odd moduli greater than one cannot cover all integers if every
individual modulus has at most three distinct prime divisors.

**Covers.** The negative answer to
[[problems/covering_systems/E0007/_index|Problem 7]] under this restriction
on each modulus. Prime powers and the total number of primes across the
family are unrestricted. The conclusion is distinct from bounding the prime
support of the overall least common multiple; neither restriction treats
all possible odd covers.

**Standing.** Claimed. The author's research-page description, dated
2026-09-09 and revised 2026-09-15, and the forum announcement were read on
2026-10-16. They report a Lean proof. The manuscript, proof and supporting
formalization were not checked here, and no independent review or journal
acceptance was located in those records.

**Depends on.** Nothing in this wiki. The announced proof uses a system of
factorial moments; its hypotheses and implementation have not been audited.

**Submission note.** The author posted the result to the problem's
discussion on 2026-09-15.
