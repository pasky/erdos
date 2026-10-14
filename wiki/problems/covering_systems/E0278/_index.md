---
name: problems/covering_systems/E0278
title: Problem 278
desc: |
  Asks for the maximum density of integers covered by choosing one congruence
  class for each modulus in a finite set, and whether equal classes minimize the
  density.
tags:
- Number theory
- Covering systems
status: claimed
claim: answered
parts: [maximum, equal_residues]
created: 2026-09-04T09:17:27Z
updated: 2026-10-08T00:44:25Z
---

# Problem 278

[[problems/covering_systems/_index|..]]

[[problems/covering_systems/E0278/claims/_index|claims/]]: The 5 claim pages of Problem 278, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $A=\{n_1<\cdots<n_r\}$ be a finite set of positive integers.
What is the maximum density of integers covered by a suitable choice of
congruences $a_i\pmod{n_i}$?

Is the minimum density achieved when all the $a_i$ are equal?

**Status.** Open. The site labeled the problem OPEN (page last edited 20 January
2026). The page lists the two questions as parts, the maximum covered density
and equal residues. Simpson's accepted claim settles the second. Onishi's
pending claim asserts a complete answer to the first: an exact characterization
of the maximum for every finite set of moduli. The problem's standing is
therefore claimed through that claim, without adopting it.

The site's commentary records the second question as settled. Simpson's
inclusion-exclusion lower bound for the covered density is attained when all the
residues agree, so equal residues cover least. This is the accepted partial
claim on
[[problems/covering_systems/E0278/claims/1986_04_01_simpson|Simpson's claim page]].
The same theorem, credited to Rogers, had appeared in Halberstam and Roth's
*Sequences* in 1966. It is recorded as an accepted partial result on
[[problems/covering_systems/E0278/claims/1966_01_01_rogers|Rogers' claim page]].

The first question was open on the site. Three claims about it are recorded
without adoption, two from the proof-claims tab and one from the discussion
thread. The curator has ruled on none of the three.

[[problems/covering_systems/E0278/claims/2025_08_25_cambie|Cambie]] argues that
no efficient general formula should be expected. The argument rests on exact
balanced-partition formulas for structured moduli, a hard knapsack order for
distinct moduli, and NP-hardness of deciding zero uncovered density for lists
with repeated moduli. It is an arXiv note, submitted as a proof claim on
2026-08-17. The note credits its NP-hardness observation to GPT Pro Sol 5.6, the
system that the site's claim names GPT pro 5.6 Sol.

[[problems/covering_systems/E0278/claims/2026_09_10_onishi|Onishi]] claims an
exact characterization of the maximum covered density as the largest clique
inclusion-exclusion value over the realizable compatibility graphs. The claim
includes a dynamic program enumerating these graphs and a Lean companion. The
manuscript and proof claim date from 2026-09-10 and were written with GPT-5.6
Sol and GPT-6 Astra. The claim has two comments. Cambie calls it a complementary
attempt reaching an essentially opposite answer to Cambie's own, and leaves the
thread's closure to the curator. The same comment also notes that for moduli up
to $2^{\varepsilon r}$ its running-time bound is no smaller than enumerating all
residue choices. Onishi replies that they see no mathematical contradiction.

[[problems/covering_systems/E0278/claims/2026_09_22_schroeder|Schroeder]] claims
several results. They are an inclusion-exclusion formula for the maximum covered
density when classes with noncoprime moduli can be made disjoint, an exact
finite optimization formula for every finite set of moduli, #P-hardness of exact
evaluation, NP-hardness of the covering and threshold decisions, and
fixed-parameter tractability in the treewidth of the noncoprime graph. They
appear in a Zenodo manuscript of 2026-09-22, with a Lean companion in its
archive. The manuscript was announced on the discussion thread on 2026-09-23.
Its acknowledgments disclose research assistance by AI systems developed by
OpenAI and Anthropic.

Cambie's partition formulas and Schroeder's closed formula settle only
structured families. Schroeder's exact formula for general sets is a finite
optimization of the same kind as Onishi's. The manuscript offers it as one
part of a combined answer rather than as a resolution.

**Source.** [erdosproblems.com/278](https://www.erdosproblems.com/278), accessed
2026-09-04 and 2026-10-06 (five comments in the discussion thread, two proof
claims). Cite as: T. F. Bloom, Erdős Problem #278,
https://www.erdosproblems.com/278.

**References.**

- [Si86] Simpson, R. J., Exact coverings of the integers by arithmetic
  progressions. Discrete Math. 59 (1986), 181-190.
- [HaRo66] Halberstam, H. and Roth, K. F., Sequences. Vol. I. Clarendon
  Press, Oxford (1966); reissued by Springer (1983).
- [Ca25] Cambie, S., Proving it is impossible; on Erdős problem #278.
  arXiv:2508.18270 (v1 2025, v2 2026).

**Formalization.** None recorded.

## Progress

Not yet compiled.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/covering_systems/cambie_2025_proving_it_is_impossible_erdos_problem/_index|cambie_2025_proving_it_is_impossible_erdos_problem]]

<!-- END problem library links -->
