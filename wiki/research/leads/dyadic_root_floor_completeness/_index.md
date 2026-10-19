---
name: research/leads/dyadic_root_floor_completeness
title: Dyadic subrays inside geometric floor sequences
desc: The accepted base-two theorem yields strong completeness at every root 2^(1/m) with m at least two, with the existential and universal base questions kept separate.
problems: [354, 349]
research_state: candidate
review_status: reviewed
last_reviewed: 2026-10-14
created: 2026-10-14T18:42:37Z
updated: 2026-10-16T06:44:50Z
---

# Dyadic subrays inside geometric floor sequences

[[research/leads/_index|..]]

***

[[theory/additive_bases/L33_dyadic_root_floor_completeness/_index|L33]]
proves, at independently graded tier 1, that for every $m\ge2$ and $t>0$ the
distinct positive values of $\lfloor t2^{n/m}\rfloor$ remain complete
after any finite deletion. Its only non-elementary input is the
[[../library/additive_bases/jenw1n_2026_erdos_354_part_i_lean_proof/target|accepted two-ray theorem at base two]].
No new examination of that theorem's long proof is asserted.

The interface is exact: indices in two consecutive residue classes
modulo $m$ give two dyadic rays with irrational coefficient ratio.
Moving sufficiently far into the original ray removes zeros, repeated
values and any prescribed finite deletion. Thus the input theorem's
permission to use equal values at different indices is harmless here.

For [[problems/additive_bases/E0354/_index|Problem 354(ii)]], $m=2$
answers the existential-base formulation, even using just one ray. The
question for every base is separate; the recorded Salem-base obstruction
is compatible with L33. For
[[problems/additive_bases/E0349/_index|Problem 349]], L33 describes a
family of complete parameters, not the full classification. No effective
uniform completeness threshold is supplied.

The general noninteger-base obstruction in the
[[research/erdos_354/connections|existing connections account]] concerns
the loss of an exact doubling recurrence. Grouping exponents restores
that recurrence at the specific bases $2^{1/m}$; it does not produce a
recurrence at an arbitrary base. The implication is complete at this
scope. Historical formulation and novelty questions remain separate from
the mathematical deduction and from its independent examination.

The
[[research/erdos_354/evidence/verify/dyadic_roots/_index|whole-conclusion examination and separate grade]]
of 2026-10-14 cover this deduction and its existential-base consequence.
Both verdicts are **refutation-failed**. The source theorem remains at
claims-checked reading depth; the record retains the reviewer's excess
source-record exposure and the grader's immateriality ruling.
