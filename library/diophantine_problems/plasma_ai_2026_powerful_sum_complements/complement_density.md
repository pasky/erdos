---
name: diophantine_problems/plasma_ai_2026_powerful_sum_complements/complement_density
title: Positive lower density of the cubic and quartic complements
desc: |
  For each r in {3, 4}, the complement of sums of at most r r-powerful
  numbers has positive lower natural density and is infinite, accepted
  on the separate Lean formalization.
created: 2026-10-20T15:35:11Z
updated: 2026-10-22T21:49:15Z
---

***

## Statement

For $r\in\{3,4\}$, let $S_r$ consist of the natural numbers that can be
written as a sum of at most $r$ natural numbers, each divisible by the
$r$th power of every prime dividing it. Repetitions are allowed. There is
a positive integer $C_r$ such that, for every sufficiently large natural $N$,

$$
N\le C_r\,\#\{n<N:n\notin S_r\}.
$$

Consequently the complement has positive lower natural density and is
infinite. Removing zero summands gives the same representability convention
for positive integers. These conclusions answer the infinitude question of
[[../wiki/problems/diophantine_problems/E0940/_index|Problem 940]] for these
two exponents only. They do not assert density zero of $S_r$ or any result
for $r\ge5$.

**Source.** The separate formalization identified on the
[[diophantine_problems/plasma_ai_2026_powerful_sum_complements/_index|source card]]:
`Solution.lean` exports `Erdos940.cubic_complement_density`,
`Erdos940.quartic_complement_density`, `Erdos940.cubic_large_integers`, and
`Erdos940.quartic_large_integers`. The cubic result is Beyer de Ryke's; the
quartic result is Plasma AI's extension. The manuscript and quartic prose
argument make stronger progression claims outside these formal targets.

**Proof pointer.** `Erdos940/FinalAssembly.lean` restates both cases in the
form of `Challenge.lean` from the cubic assembly `Erdos940/Cubic/Assembly.lean`
and the quartic result `Erdos940/Quartic/Result.lean`; `Erdos940/Density.lean`
and `Erdos940/Progression.lean` hold the counting shared by both cases. Both
cases use the Chebotarev density theorem of Chris Birkbeck's AINTLIB, vendored
under `vendor/AINTLIB`, and the quartic case's reciprocity and Hilbert-symbol
steps use Naganori Yamaguchi's ClassFieldTheory, vendored under
`vendor/ClassFieldTheory`. The source card records both libraries'
provenance.

**Read depth.** Claims checked: the four target statements and their
representation definitions were independently compared with the mathematical
Claim and Covers sections preserved for review. The
[[diophantine_problems/plasma_ai_2026_powerful_sum_complements/evidence/verify/statement_fidelity/grade|separate grade]]
passed all four semantic findings on 2026-10-20. The
[[diophantine_problems/plasma_ai_2026_powerful_sum_complements/evidence/verify/replay_receipt|mechanical receipt]]
records the successful build, Comparator, empty-environment kernel replay,
standard-axiom closure and correspondence with the reviewed snapshots.
Together they support acceptance of these external results, with no numerical
tier. Neither the manuscript proof nor the quartic prose proof is accepted
by those checks.

**Bears on.**

- [[../wiki/problems/diophantine_problems/E0940/_index|Problem 940]]:
  answers the infinitude question for $r=3$ and $r=4$, with a complement of
  positive lower density; it says nothing on the density-zero question or on
  $r\ge5$.
