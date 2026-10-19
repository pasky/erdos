---
name: theory/integer_sequences/L20_roots_of_unity_analytic_sidon
title: The complex roots of unity form an analytic Sidon set
desc: |
  One constant bounds every trigonometric polynomial supported on roots of
  unity by the value of some additive character of the discrete additive
  group of the complex numbers; a step of the Problem 774 extraction route.
tags: []
sources:
- problems/integer_sequences/E0774
id: L20
statement: |
  Let R be the set of complex roots of unity, the complex z with z^n = 1 for
  some integer n >= 1, viewed as a subset of the additive group of the
  complex numbers with the discrete topology. There is a real K > 0 such
  that for every finite set A contained in R and every function c from the
  complex numbers to the complex numbers there is an additive character chi
  from the complex numbers to the unit circle, a group homomorphism from
  (C,+) to the multiplicative circle group with no continuity required, with
  sum_{z in A} |c(z)| <= K * |sum_{z in A} c(z) chi(z)|. Nothing is asserted
  about the size of K, about continuity of chi, or about Problem 774's
  question.
status: proved
tier: 2
depends_on: []
lean: Erdos.L20.claim
created: 2026-09-25T22:01:44Z
updated: 2026-10-16T07:31:20Z
---

# The complex roots of unity form an analytic Sidon set

[[theory/integer_sequences/_index|..]]

[[theory/integer_sequences/L20_roots_of_unity_analytic_sidon/_proof|_proof]]: The prime tensor argument gives a uniform finite estimate, small primes are
absorbed with a fixed factor, and cyclotomic decomposition transfers the
bound to all roots of unity; this account maps the Lean modules.

[[theory/integer_sequences/L20_roots_of_unity_analytic_sidon/evidence/_index|evidence/]]: Native statement-fidelity records for L20 as it stood on 2026-09-28, with
the grade and the non-author clean gate of 2026-09-29 for its kernel-only
promotion, and the two non-author clean gates of 2026-10-13, the later of
which, on Lean v4.34.1, the card's standing cites.

***

## Statement

Let $R\subset\mathbb C$ be the set of complex roots of unity, the $z$ with
$z^n=1$ for some integer $n\ge1$, regarded inside the additive group
$(\mathbb C,+)$ with the discrete topology. There is a real $K>0$ such that
for every finite $A\subseteq R$ and every $c:\mathbb C\to\mathbb C$ there
is an additive character $\chi:(\mathbb C,+)\to S^1$, a group homomorphism
with no continuity required, with

$$
\sum_{z\in A}|c(z)|\;\le\;K\,\Bigl|\sum_{z\in A}c(z)\,\chi(z)\Bigr|.
$$

This is the analytic Sidon property of $R$ in the discrete group; it is the
harmonic-analytic assertion that the
[[research/erdos_774/routes/prime_tensor_extraction|prime tensor extraction route]]
of the Problem 774 research needs. The claim does not bound $K$, does not
concern continuous characters, and does not answer
[[problems/integer_sequences/E0774/_index|Problem 774]], which asks about subsets
of the natural numbers.

## Argument and formal surface

The [proof account](_proof.md) maps the argument to its modules. The
[native claim surface](../../../../lean/Erdos/L20.lean) restates the set of
roots and the inequality in `Erdos.L20.statement`, proves the set equal to
the project's by unfolding, and derives `Erdos.L20.claim` from
`Erdos.Research.Problem774.rootsOfUnity_analyticSidon` in
`lean/Erdos/RootsOfUnitySidon/RootsOfUnitySidonAnalytic.lean`. No other native
L-claim is used as a premise.

## Current standing

This claim is **proved at tier 2** for the Lean sources and the statement
as they stood on 2026-09-28 (the default branch at 13:50:48Z), first bound to
the Lean tree checked by the non-author clean gate of 2026-09-29T20:10:11Z
(2,977 modules in `lean/Manifest.json`, of which the claim's import closure
is 72 modules, `Erdos.L20` and the 71 under
`lean/Erdos/RootsOfUnitySidon/`). The claim's
row in `lean/Manifest.json` records an axiom footprint of `propext`,
`Classical.choice` and `Quot.sound` with no compiler axiom. The
[[theory/integer_sequences/L20_roots_of_unity_analytic_sidon/evidence/verify/statement_fidelity/report|fidelity audit]]
found **PASS** for the whole English statement above against
`Erdos.L20.statement` as it stood on that date: its ten-row table accounts
for every clause of the `statement` field, with the quantifier order, the
binder domains, the two coercions and the vacuous cases stated, and
`Erdos.L20.claim` is declared at exactly `Erdos.L20.statement`. The
[[theory/integer_sequences/L20_roots_of_unity_analytic_sidon/evidence/verify/statement_fidelity/grade|distinct grade]]
passed the audit against the fidelity contract and its independence record,
reproduced every row with no discrepancy (checking further that
`IsOfFinOrder` on `z : ℂ` elaborates against the multiplicative monoid, so
the set is the roots of unity and not the additive torsion), ruled each of
the audit's six disclosed exposures immaterial by the content test, and
asserts tier 2, kernel-only: the row's `compiler` list and the manifest's
top-level `compiler` array are empty, so this card carries no
`assumes: compiler` key. The commissioning text of the audit placed the
claim under `wiki/theory/number_theory/`; the audit and the grade are filed
under this, the actual, folder. The
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
`wiki/theory/integer_sequences/L20_roots_of_unity_analytic_sidon/evidence/verify/clean_gate_2/clean_gate.json`,
with the captured log `clean_gate_log.txt` beside it;
[[theory/integer_sequences/L20_roots_of_unity_analytic_sidon/evidence/verify/clean_gate_2/_index|its record]]),
keyed to the build inputs under `lean/`. That gate ran from 2026-10-13T19:54:37Z
to 2026-10-13T19:59:38Z over a fresh archive of the whole `lean/` tree of the
change that ported the Lean modules of L20, L21 and L22 to Lean v4.34.1, as
committed at 2026-10-13T19:38:30Z, exit 0, which built all 278 modules,
`Erdos.L20` among them, reported `AUDIT PASS` over 3,771 constants with 4 claims
and 0 compiler axioms and matched the committed self-test stamp, one run serving
L20, L21 and L22. A grade decision applied the filed grade to the Lean v4.34.1
tree: its surface differs only by Mathlib's rename of `setOf` to `Set.ofPred`, a
deprecated alias with the same type and body, and by the recorded type of the
boundary constant `Circle._proof_1`, which reaches `Semiring ℂ` through
`Ring.toSemiring` instead of `DivisionSemiring.toSemiring`, another path to the
same instance; the statement declaration, every definition it reaches, the
statement fingerprints in `lean/Manifest.json` and the statement field are
unchanged. The tier assertion is in force on that tree from the filing that
cites the grade, the grade decision and the gate together. The earlier
non-author clean gate of 2026-10-13T05:05:07Z
([[theory/integer_sequences/L20_roots_of_unity_analytic_sidon/evidence/verify/clean_gate/_index|its record]])
checked the whole `lean/` tree as it stood on 2026-10-13T04:56:43Z, on Lean
v4.32.0-rc1, and reported `AUDIT PASS` over 3,788 constants in 278 modules with
4 claims and 0 compiler axioms, exit 0, one run serving L17, L20, L21 and L22;
the warrant was first bound to the tree the gate of 2026-09-29T20:10:11Z
checked. Under the carry-forward rule (`docs/verification.md` "Exact subjects
and durable evidence"), which overrides the grade's own wording about later
changes, the warrant carries forward over every later change to the build inputs
while (a) the ordinary gate passes and (b) the claim's statement is unchanged in
meaning: its declaration `Erdos.L20.statement`, every definition it reaches, its
manifest row over every field both rows carry except `module`, and the
`statement:` field above. A later change under `lean/` does not lower this card;
only a change that ends coverage is listed here, with what it touched, until the
claim is re-graded, and none is listed. The carry-forward check last ran on 2026-10-16, over that day's tree, and found the statement unchanged in meaning. Any change to the `statement` field, to
`Erdos.L20.statement` or to a definition it reaches is a new subject the grade
does not cover. The
[[theory/integer_sequences/L20_roots_of_unity_analytic_sidon/evidence/verify/statement_fidelity/_index|record]]
holds the audit, the grade, the clean-gate receipt, the gate's captured log and
the runner's wrapper. These records cover the whole English statement above. L20
is a premise of
[[theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/_index|L21]];
the grade grades L20 on its own terms and asserts nothing about L21, about the
size of $K$, about continuous characters, about Problem 774's question, or about
novelty or public acceptance, and the clean gate validates the committed sources
without reviewing the mathematics or the statement.

Author: the filing author of the formalization, this card and the proof
page, in the delivery commit, who recorded tier 0. Auditor: the independent
statement-fidelity auditor for L20, in a fresh context, given only its
assignment, who took no part in the claim, its Lean development or its card,
built nothing and ran no gate. Grader: a distinct grader in a fresh context,
given only its assignment, not the author of any module, page or record
under review, not the auditor, and not the runner of any gate. Clean gate: for
the gate of 2026-09-29, a non-author clean-gate runner, in a fresh context, who
received only its commission, ran the gate once for the five claims and asserts
no tier; for the gate of 2026-10-13T19:54:37Z, a non-author clean-gate runner in
a fresh context, who did not author the port to Lean v4.34.1 and asserts no
tier. Grade decision: a maintainer who took no part in the port. Filing: the
integrator of the promotion, who adds paths and dates and asserts no tier.

## Verification

From `lean/`, `lake exe cache get`, then `scripts/gate.sh`: the full build,
the axiom audit against `Manifest.json`, and the self-test stamp. The targeted
build `lake build Erdos.L20` checks the claim's own module and its import
closure. The filed record of 2026-09-28,
[[theory/integer_sequences/L20_roots_of_unity_analytic_sidon/evidence/verify/statement_fidelity/_index|statement_fidelity/]],
holds the fidelity audit, its distinct grade and the non-author clean gate
of 2026-09-29 (`scripts/gate.sh --clean` from `lean/`, run on the repository
as it stood on 2026-09-28), whose receipt, captured log and wrapper are filed
in that folder and cited above.

## Remaining obligations

- [x] Independent whole-statement fidelity audit of `Erdos.L20.statement`
  against the statement above, graded separately, with a non-author clean
  gate, under the verification contract: filed under
  `evidence/verify/statement_fidelity/` for the source of 2026-09-28,
  verdict PASS, graded pass with tier 2 asserted on 2026-09-28, and the
  clean gate filed and the tier in force on 2026-09-29.
- [x] The Problem 774 research pages reconciled with this claim in the same
  change.
- [x] A non-author clean gate of the Lean v4.34.1 tree, with a grade decision
  applying the filed grade to it: the gate of 2026-10-13 under
  `evidence/verify/clean_gate_2/`, whose receipt
  `wiki/theory/integer_sequences/L20_roots_of_unity_analytic_sidon/evidence/verify/clean_gate_2/clean_gate.json`
  records a run from 2026-10-13T19:54:37Z to 2026-10-13T19:59:38Z over the
  `lean/` tree of the change that ported the Lean modules of L20, L21 and L22 to
  Lean v4.34.1, as committed at 2026-10-13T19:38:30Z, exit 0, which built
  `Erdos.L20`, reported `AUDIT PASS` with 0 compiler axioms over 4 claims and
  matched the committed self-test stamp; a grade decision applied the filed
  grade to that tree, whose surface differs only by Mathlib's rename of `setOf`
  and another path to the same instance. The earlier non-author clean gate of
  2026-10-13, under `evidence/verify/clean_gate/`, checked the `lean/` tree as
  it stood on 2026-10-13T04:56:43Z, on Lean v4.32.0-rc1.
- [x] Closed by the carry-forward rule (`docs/verification.md` "Exact subjects
  and durable evidence"): no fresh non-author clean gate is owed after a later
  change under `lean/`; the warrant carries forward while the ordinary gate
  passes and the statement is unchanged in meaning, checked by
  `scripts/claim_carry_forward.py`, and a change to the statement's meaning ends
  coverage of the new tree until the claim is re-graded.
