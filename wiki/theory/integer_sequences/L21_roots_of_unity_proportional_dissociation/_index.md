---
name: theory/integer_sequences/L21_roots_of_unity_proportional_dissociation
title: The complex roots of unity are proportionately dissociated
desc: |
  One integer denominator works for every finite set of complex roots of
  unity: each contains an additively dissociated subset of proportional
  size; the roots-of-unity analog of Problem 774's hypothesis.
tags: []
sources:
- problems/integer_sequences/E0774
id: L21
statement: |
  Let R be the set of complex roots of unity, the complex z with z^n = 1 for
  some integer n >= 1, viewed inside the additive group of the complex
  numbers. A set B of complex numbers is additively dissociated if distinct
  finite subsets of B have distinct sums. There is an integer k >= 1 such
  that every finite set A contained in R contains an additively dissociated
  subset B with |A| <= k*|B|. Nothing is asserted about the value of k, about
  subsets of the natural numbers, or about Problem 774's question.
status: proved
tier: 2
depends_on:
- L20
lean: Erdos.L21.claim
created: 2026-09-25T22:01:44Z
updated: 2026-10-16T07:31:20Z
---

# The complex roots of unity are proportionately dissociated

[[theory/integer_sequences/_index|..]]

[[theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/_proof|_proof]]: Finite interpolation, Khintchine moments and a Riesz-product average give
a Pisier-type extraction from the analytic Sidon constant; this account
maps the Lean modules.

[[theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/evidence/_index|evidence/]]: Native statement-fidelity records for L21 as it stood on 2026-09-28, with
the grade and the non-author clean gate of 2026-09-29 for its kernel-only
promotion, and the two non-author clean gates of 2026-10-13, the later of
which, on Lean v4.34.1, the card's standing cites.

***

## Statement

Let $R\subset\mathbb C$ be the set of complex roots of unity, the $z$ with
$z^n=1$ for some integer $n\ge1$, regarded inside $(\mathbb C,+)$. A set
$B\subset\mathbb C$ is additively dissociated if distinct finite subsets of
$B$ have distinct sums. There is an integer $k\ge1$ such that every finite
$A\subseteq R$ contains an additively dissociated $B\subseteq A$ with
$|A|\le k\,|B|$.

This is the proportional-dissociation property, in the sense of
[[problems/integer_sequences/E0774/_index|Problem 774]]'s hypothesis, for the set
of all complex roots of unity viewed additively. The claim does not bound
$k$, says nothing about subsets of the natural numbers, and does not answer
Problem 774, whose question concerns unions of finitely many dissociated
sets.

## Argument and formal surface

The [proof account](_proof.md) maps the argument to its modules. The
[native claim surface](../../../../lean/Erdos/L21.lean) restates the set of
roots and the extraction property in `Erdos.L21.statement` over Mathlib's
`AddDissociated`, proves the set equal to the project's by unfolding, and
derives `Erdos.L21.claim` from
`Erdos.Research.Problem774.rootsOfUnity_proportionalDissociation` in
`lean/Erdos/RootsOfUnitySidon/RootsOfUnitySidonComplete.lean`. That theorem
combines the analytic Sidon property, the statement of
[[theory/integer_sequences/L20_roots_of_unity_analytic_sidon/_index|L20]], with a finite Pisier implication
proved in the same development. The proof therefore consumes L20's result,
itself proved at tier 2 for the same checked source, as its analytic input,
which the `depends_on` edge records; the kernel proof reaches the library
theorem `rootsOfUnity_analyticSidon` rather than `Erdos.L20.claim`, so the
manifest row's `depends` field stays empty.

## Current standing

This claim is **proved at tier 2** for the Lean sources and the statement
as they stood on 2026-09-28 (the default branch at 13:50:48Z), first bound to
the Lean tree checked by the non-author clean gate of 2026-09-29T20:10:11Z
(2,977 modules in `lean/Manifest.json`, of which the claim's import closure
is 72 modules, `Erdos.L21` and the 71 under
`lean/Erdos/RootsOfUnitySidon/`). The claim's
row in `lean/Manifest.json` records an axiom footprint of `propext`,
`Classical.choice` and `Quot.sound` with no compiler axiom. The
[[theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/evidence/verify/statement_fidelity/report|fidelity audit]]
found **PASS** for the whole English statement above against
`Erdos.L21.statement` as it stood on that date: the eight clauses of the
`statement` field each have their Lean counterpart after the unfolding
steps, the
converse direction is closed (no hypothesis, parameter, instance argument or
side condition beyond them is present), and `Erdos.L21.claim` is declared at
exactly `statement` with no binders. The
[[theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/evidence/verify/statement_fidelity/grade|distinct grade]]
passed the audit against the fidelity contract and its independence record,
confirmed every finding by its own comparison, ruled each of the audit's
disclosed exposures E1-E7 immaterial by the content test, and asserts tier 2,
kernel-only: the row's `compiler` list and the manifest's top-level
`compiler` array are empty, so this card carries no `assumes: compiler` key.
The kernel proof reaches only source modules of
`lean/Erdos/RootsOfUnitySidon/` and no other L-claim; the declared
dependency
[[theory/integer_sequences/L20_roots_of_unity_analytic_sidon/_index|L20]]
is the analytic input, whose own fidelity audit of the same source is
graded pass in the batch order L20 before L21, and whose card is promoted in
the same change on the same clean gate. The
[non-author clean gate](evidence/verify/statement_fidelity/clean_gate.json)
built the checked source from a fresh archive of its `lean/` tree
(`lean/scripts/gate.sh --clean`, run on the repository as it stood on
2026-09-28: 7,501 jobs; `AUDIT PASS` over 42,230 constants in 2,977 modules
with 7 claims and 0 compiler axioms; the committed self-test stamp matched;
exit 0), run from 2026-09-29T20:10:11Z to 2026-09-29T21:30:54Z, one run
serving the five claims whose records name that source; the grade's
assertion is in force from this promotion, which cites the grade together
with that receipt.

The acceptance is of the source of 2026-09-28, and the warrant is bound to the
`lean/` tree checked by the non-author clean gate of 2026-10-13T19:54:37Z
(receipt
`wiki/theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/evidence/verify/clean_gate_2/clean_gate.json`,
with the captured log `clean_gate_log.txt` beside it;
[[theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/evidence/verify/clean_gate_2/_index|its record]]),
keyed to the build inputs under `lean/`. That gate ran from 2026-10-13T19:54:37Z
to 2026-10-13T19:59:38Z over a fresh archive of the whole `lean/` tree of the
change that ported the Lean modules of L20, L21 and L22 to Lean v4.34.1, as
committed at 2026-10-13T19:38:30Z, exit 0, which built all 278 modules,
`Erdos.L21` among them, reported `AUDIT PASS` over 3,771 constants with 4 claims
and 0 compiler axioms and matched the committed self-test stamp, one run serving
L20, L21 and L22. A grade decision applied the filed grade to the Lean v4.34.1
tree: its surface differs only by Mathlib's rename of `setOf` to `Set.ofPred`, a
deprecated alias with the same type and body; the statement declaration, every
definition it reaches, the statement fingerprints in `lean/Manifest.json` and
the statement field are unchanged. The tier assertion is in force on that tree
from the filing that cites the grade, the grade decision and the gate together.
The earlier non-author clean gate of 2026-10-13T05:05:07Z
([[theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/evidence/verify/clean_gate/_index|its record]])
checked the whole `lean/` tree as it stood on 2026-10-13T04:56:43Z, on Lean
v4.32.0-rc1, and reported `AUDIT PASS` over 3,788 constants in 278 modules with
4 claims and 0 compiler axioms, exit 0, one run serving L17, L20, L21 and L22;
the warrant was first bound to the tree the gate of 2026-09-29T20:10:11Z
checked. Under the carry-forward rule (`docs/verification.md` "Exact subjects
and durable evidence"), which overrides the grade's own wording about later
changes, the warrant carries forward over every later change to the build inputs
while (a) the ordinary gate passes and (b) the claim's statement is unchanged in
meaning: its declaration `Erdos.L21.statement`, every definition it reaches, its
manifest row over every field both rows carry except `module`, and the
`statement:` field above. A later change under `lean/` does not lower this card;
only a change that ends coverage is listed here, with what it touched, until the
claim is re-graded, and none is listed. The carry-forward check last ran on 2026-10-16, over that day's tree, and found the statement unchanged in meaning. Any change to the `statement` field, to
`Erdos.L21.statement` or to a definition it reaches is a new subject the grade
does not cover. The
[[theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/evidence/verify/statement_fidelity/_index|record]]
holds the audit, the grade, the clean-gate receipt, the gate's captured log and
the runner's wrapper. These records cover the whole English statement above.
They assert nothing about the value of $k$, about subsets of the natural
numbers, about Problem 774's question, about the library proof's correctness, or
about novelty or public acceptance, and the clean gate validates the committed
sources without reviewing the mathematics or the statement.

Author: the formalization author and integrating author of the delivery
commit, who recorded tier 0 on this card. Auditor: the independent fidelity
auditor for L21, in a fresh context, given only its assignment, who took no
part in the claim, its Lean development or its card and audited by reading
alone. Grader: a distinct grader in a fresh context, given only its
assignment, not the author of the claim, its modules, its card or its proof
page, not the auditor, and not the runner of any gate. Clean gate: for the gate
of 2026-09-29, a non-author clean-gate runner, in a fresh context, who received
only its commission, ran the gate once for the five claims and asserts no tier;
for the gate of 2026-10-13T19:54:37Z, a non-author clean-gate runner in a fresh
context, who did not author the port to Lean v4.34.1 and asserts no tier. Grade
decision: a maintainer who took no part in the port. Filing: the integrator of
the promotion, who adds paths and dates and asserts no tier.

## Verification

From `lean/`, `lake exe cache get`, then `scripts/gate.sh`: the full build,
the axiom audit against `Manifest.json`, and the self-test stamp. The targeted
build `lake build Erdos.L21` checks the claim's own module and its import
closure. The filed record of 2026-09-28,
[[theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/evidence/verify/statement_fidelity/_index|statement_fidelity/]],
holds the fidelity audit, its distinct grade and the non-author clean gate
of 2026-09-29 (`scripts/gate.sh --clean` from `lean/`, run on the repository
as it stood on 2026-09-28), whose receipt, captured log and wrapper are filed
in that folder and cited above.

## Remaining obligations

- [x] Independent whole-statement fidelity audit of `Erdos.L21.statement`
  against the statement above, graded separately, with a non-author clean
  gate, under the verification contract: filed under
  `evidence/verify/statement_fidelity/` for the source of 2026-09-28,
  verdict PASS, graded pass with tier 2 asserted on 2026-09-28 in the batch
  order L20 before L21, and the clean gate filed and the tier in force on
  2026-09-29.
- [x] The Problem 774 research pages reconciled with this claim in the same
  change.
- [x] A non-author clean gate of the Lean v4.34.1 tree, with a grade decision
  applying the filed grade to it: the gate of 2026-10-13 under
  `evidence/verify/clean_gate_2/`, whose receipt
  `wiki/theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/evidence/verify/clean_gate_2/clean_gate.json`
  records a run from 2026-10-13T19:54:37Z to 2026-10-13T19:59:38Z over the
  `lean/` tree of the change that ported the Lean modules of L20, L21 and L22 to
  Lean v4.34.1, as committed at 2026-10-13T19:38:30Z, exit 0, which built
  `Erdos.L21`, reported `AUDIT PASS` with 0 compiler axioms over 4 claims and
  matched the committed self-test stamp; a grade decision applied the filed
  grade to that tree, whose surface differs only by Mathlib's rename of `setOf`.
  The earlier non-author clean gate of 2026-10-13, under
  `evidence/verify/clean_gate/`, checked the `lean/` tree as it stood on
  2026-10-13T04:56:43Z, on Lean v4.32.0-rc1.
- [x] Closed by the carry-forward rule (`docs/verification.md` "Exact subjects
  and durable evidence"): no fresh non-author clean gate is owed after a later
  change under `lean/`; the warrant carries forward while the ordinary gate
  passes and the statement is unchanged in meaning, checked by
  `scripts/claim_carry_forward.py`, and a change to the statement's meaning ends
  coverage of the new tree until the claim is re-graded.
