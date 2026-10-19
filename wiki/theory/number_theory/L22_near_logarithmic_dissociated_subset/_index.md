---
name: theory/number_theory/L22_near_logarithmic_dissociated_subset
title: Finite real sets have near-logarithmically large dissociated subsets
desc: |
  Every set of n real numbers contains an additively dissociated subset of
  size at least log_2 n - log_2(log_2 n + 1); the binary residue-tree bound of
  the Problem 963 research, weaker than the asked floor(log_2 n).
tags: []
sources:
- problems/number_theory/E0963
id: L22
statement: |
  A set B of real numbers is additively dissociated if distinct finite
  subsets of B have distinct sums, the empty subset with sum 0 included.
  Let A be a nonempty finite set of real numbers with n = |A| elements, and
  write log_2 for the logarithm to base two. Then A contains an additively
  dissociated subset B with |B| >= log_2 n - log_2(log_2 n + 1). In the
  notation of Problem 963 this gives f(n) >= log_2 n - log_2(log_2 n + 1)
  for every integer n >= 1. Nothing is asserted about whether
  f(n) >= floor(log_2 n), about any upper bound on f(n), or about the
  sharpness of this bound.
status: proved
tier: 2
depends_on: []
lean: Erdos.L22.claim
created: 2026-09-28T02:43:51Z
updated: 2026-10-16T07:31:20Z
---

# Finite real sets have near-logarithmically large dissociated subsets

[[theory/number_theory/_index|..]]

[[theory/number_theory/L22_near_logarithmic_dissociated_subset/_proof|_proof]]: A binary residue tree yields a pivot with companions whose differences have
distinct 2-adic valuations, distinct valuations force dissociation after a
short deletion, and an integer model transfers the bound to real sets; this
account maps the Lean modules.

[[theory/number_theory/L22_near_logarithmic_dissociated_subset/evidence/_index|evidence/]]: Native statement-fidelity records for L22 as it stood on 2026-09-28, with
the grade and the non-author clean gate of 2026-09-29 for its kernel-only
promotion, and the two non-author clean gates of 2026-10-13, the later of
which, on Lean v4.34.1, the card's standing cites.

***

## Statement

A set $B\subset\mathbb R$ is additively dissociated if distinct finite
subsets of $B$ have distinct sums, the empty subset with sum $0$ included.
Let $A\subset\mathbb R$ be a nonempty finite set with $n=|A|$ elements.
Then $A$ contains an additively dissociated $B\subseteq A$ with

$$
|B|\;\ge\;\log_2 n-\log_2(\log_2 n+1).
$$

In the notation of [[problems/number_theory/E0963/_index|Problem 963]] this is the
near-logarithmic lower bound $f(n)\ge\log_2 n-\log_2(\log_2 n+1)$ for every
$n\ge1$, the bound proved in prose by the section "Proved near-logarithmic
bound via a binary tree" of [[research/erdos_963/proof_sketch|the proof sketch]].
It is weaker than the asked $\lfloor\log_2 n\rfloor$ by the
$\log_2(\log_2 n+1)$ term: the two agree only at $n=1$, and the bound lies
strictly below $\lfloor\log_2 n\rfloor$ for every $n\ge2$. The claim gives
no upper bound on $f(n)$ and does not answer the problem. The interior
theorem `integer_card_le_pow` proves the sharper estimate
$|S|\le2^{d+\lfloor\log_2(d+1)\rfloor}$, with $d$ the largest size of a
dissociated subset, for finite integer sets only; the development transfers
only the product form $(d+1)2^d$ to real sets, and the claim's bound follows
from that form.

## Argument and formal surface

The [proof account](_proof.md) maps the argument to its modules. The
[native claim surface](../../../../lean/Erdos/L22.lean) states the bound in
`Erdos.L22.statement` over Mathlib's `AddDissociated` and `Real.logb`, so no
project definition is restated and no bridge lemma is needed, and derives
`Erdos.L22.claim` from `Erdos.Problem963.exists_real_dissociated_large` in
`lean/Erdos/Problem963/CardBound.lean`. The development under
`lean/Erdos/Problem963/` (seven modules in the namespace `Erdos.Problem963`)
is the checked form of the binary residue-tree argument of
[[research/erdos_963/proof_sketch|the proof sketch]]. No other native L-claim
is used as a premise.

## Current standing

This claim is **proved at tier 2** for the Lean sources and the statement
as they stood on 2026-09-28 (the default branch at 13:50:48Z), first bound to
the Lean tree checked by the non-author clean gate of 2026-09-29T20:10:11Z
(2,977 modules in `lean/Manifest.json`, of which the claim's import closure
is eight handwritten modules, `Erdos.L22` and the seven under
`lean/Erdos/Problem963/`). The claim's row in `lean/Manifest.json` records
an axiom footprint of `propext`, `Classical.choice` and `Quot.sound` with no
compiler axiom. The
[[theory/number_theory/L22_near_logarithmic_dissociated_subset/evidence/verify/statement_fidelity/report|fidelity audit]]
found **PASS** for the whole English statement above against
`Erdos.L22.statement` as it stood on that date: the seven clauses of the
`statement` field, the Statement section, the formal-surface sentences and
the proof
page's module map each have their counterpart, the specialization to Problem
963's $f(n)$ is argued rather than assumed, and `claim` proves exactly
`statement`. The
[[theory/number_theory/L22_near_logarithmic_dissociated_subset/evidence/verify/statement_fidelity/grade|distinct grade]]
passed the audit against the fidelity contract and its independence record,
agreed on every clause, on the equivalence for $f(n)$ and on the vacuity
analysis, ruled each of the audit's disclosed exposures E1-E8 immaterial by
the content test, and asserts tier 2, kernel-only: the row's `compiler` list
and the manifest's top-level `compiler` array are empty, and a sweep of the
eight closure modules found no `sorry`, axiom, `native_decide` or
metaprogramming command, so this card carries no `assumes: compiler` key.
The
[non-author clean gate](evidence/verify/statement_fidelity/clean_gate.json)
built the checked source from a fresh archive of its `lean/` tree
(`lean/scripts/gate.sh --clean`, run on the repository as it stood on
2026-09-28: 7,501 jobs; `AUDIT PASS` over 42,230 constants in 2,977 modules
with 7 claims and 0 compiler axioms; the committed self-test stamp matched;
exit 0), run from 2026-09-29T20:10:11Z to 2026-09-29T21:30:54Z, one run
serving the five claims whose records name that source; the grade's
assertion is in force from this promotion, which cites the grade together
with that receipt.
The audit's one observation, that the proof page words the case split of
`log_bound_of_card_le` as $d\ge\log_2 n$ and $d<\log_2 n$ where the Lean
splits on $d\le\log_2 n$ and its negation, concerns the proof account and
not the statement; both texts cover the boundary case and no card wording
is required.

The acceptance is of the source of 2026-09-28, and the warrant is bound to the
`lean/` tree checked by the non-author clean gate of 2026-10-13T19:54:37Z
(receipt
`wiki/theory/number_theory/L22_near_logarithmic_dissociated_subset/evidence/verify/clean_gate_2/clean_gate.json`,
with the captured log `clean_gate_log.txt` beside it;
[[theory/number_theory/L22_near_logarithmic_dissociated_subset/evidence/verify/clean_gate_2/_index|its record]]),
keyed to the build inputs under `lean/`. That gate ran from 2026-10-13T19:54:37Z
to 2026-10-13T19:59:38Z over a fresh archive of the whole `lean/` tree of the
change that ported the Lean modules of L20, L21 and L22 to Lean v4.34.1, as
committed at 2026-10-13T19:38:30Z, exit 0, which built all 278 modules,
`Erdos.L22` among them, reported `AUDIT PASS` over 3,771 constants with 4 claims
and 0 compiler axioms and matched the committed self-test stamp, one run serving
L20, L21 and L22; of the inputs that fix the claim's statement, only the
toolchain pins changed from the tree of the earlier gate, and the claim's row in
`lean/Manifest.json` is identical. The earlier non-author clean gate of
2026-10-13T05:05:07Z
([[theory/number_theory/L22_near_logarithmic_dissociated_subset/evidence/verify/clean_gate/_index|its record]])
checked the whole `lean/` tree as it stood on 2026-10-13T04:56:43Z, on Lean
v4.32.0-rc1, and reported `AUDIT PASS` over 3,788 constants in 278 modules with
4 claims and 0 compiler axioms, exit 0, one run serving L17, L20, L21 and L22;
the warrant was first bound to the tree the gate of 2026-09-29T20:10:11Z
checked. Under the carry-forward rule (`docs/verification.md` "Exact subjects
and durable evidence"), which overrides the grade's own wording about later
changes, the warrant carries forward over every later change to the build inputs
while (a) the ordinary gate passes and (b) the claim's statement is unchanged in
meaning: its declaration `Erdos.L22.statement`, every definition it reaches, its
manifest row over every field both rows carry except `module`, and the
`statement:` field above. A later change under `lean/` does not lower this card;
only a change that ends coverage is listed here, with what it touched, until the
claim is re-graded, and none is listed. The carry-forward check last ran on 2026-10-16, over that day's tree, and found the statement unchanged in meaning. Any change to the `statement` field, to
`Erdos.L22.statement` or to a definition it reaches is a new subject the grade
does not cover. The proof page's standing phrase changed with this promotion,
and the module map the audit compared is unchanged. The
[[theory/number_theory/L22_near_logarithmic_dissociated_subset/evidence/verify/statement_fidelity/_index|record]]
holds the audit, the grade, the clean-gate receipt, the gate's captured log and
the runner's wrapper. These records cover the whole English statement above.
They assert nothing about whether $f(n)\ge\lfloor\log_2 n\rfloor$, about any
upper bound on $f(n)$, about the sharpness of the bound, or about novelty,
community acceptance or the literature status of Problem 963, and the clean gate
validates the committed sources without reviewing the mathematics or the
statement.

Author: the author of the formalization and this card, who recorded tier 0
and took no part in the audit or the grade. Auditor: the statement-fidelity
auditor for L22, in a fresh context, given only its assignment, who took no
part in the claim, its Lean development or its card and read the Lean
sources without building them. Grader: a distinct grader in a fresh context,
given only its assignment, neither the author nor the auditor, who built
nothing and ran no gate. Clean gate: for the gate of 2026-09-29, a non-author
clean-gate runner, in a fresh context, who received only its commission, ran the
gate once for the five claims and asserts no tier; for the gate of
2026-10-13T19:54:37Z, a non-author clean-gate runner in a fresh context, who did
not author the port to Lean v4.34.1 and asserts no tier. Filing: the integrator
of the promotion, who adds paths and dates and asserts no tier.

## Verification

From `lean/`, `lake exe cache get`, then `scripts/gate.sh`: the full build,
the axiom audit against `Manifest.json`, and the self-test stamp. The targeted
build `lake build Erdos.L22` checks the claim's own module and its import
closure. The filed record of 2026-09-28,
[[theory/number_theory/L22_near_logarithmic_dissociated_subset/evidence/verify/statement_fidelity/_index|statement_fidelity/]],
holds the fidelity audit, its distinct grade and the non-author clean gate
of 2026-09-29 (`scripts/gate.sh --clean` from `lean/`, run on the repository
as it stood on 2026-09-28), whose receipt, captured log and wrapper are filed
in that folder and cited above.

## Remaining obligations

- [x] Independent whole-statement fidelity audit of `Erdos.L22.statement`
  against the statement above, graded separately, with a non-author clean
  gate, under the verification contract: filed under
  `evidence/verify/statement_fidelity/` for the source of 2026-09-28,
  verdict PASS, graded pass with tier 2 asserted on 2026-09-28, and the
  clean gate filed and the tier in force on 2026-09-29.
- [x] The Problem 963 problem and research pages reconciled with this claim
  in the same change.
- [x] A non-author clean gate of the Lean v4.34.1 tree: the gate of 2026-10-13
  under `evidence/verify/clean_gate_2/`, whose receipt
  `wiki/theory/number_theory/L22_near_logarithmic_dissociated_subset/evidence/verify/clean_gate_2/clean_gate.json`
  records a run from 2026-10-13T19:54:37Z to 2026-10-13T19:59:38Z over the
  `lean/` tree of the change that ported the Lean modules of L20, L21 and L22 to
  Lean v4.34.1, as committed at 2026-10-13T19:38:30Z, exit 0, which built
  `Erdos.L22`, reported `AUDIT PASS` with 0 compiler axioms over 4 claims and
  matched the committed self-test stamp; of the inputs that fix the claim's
  statement, only the toolchain pins changed from the tree of the earlier gate
  below, and its row in `lean/Manifest.json` is identical, so no re-grade is
  owed. The earlier non-author clean gate of 2026-10-13, under
  `evidence/verify/clean_gate/`, checked the `lean/` tree as it stood on
  2026-10-13T04:56:43Z, on Lean v4.32.0-rc1.
- [x] Closed by the carry-forward rule (`docs/verification.md` "Exact subjects
  and durable evidence"): no fresh non-author clean gate is owed after a later
  change under `lean/`; the warrant carries forward while the ordinary gate
  passes and the statement is unchanged in meaning, checked by
  `scripts/claim_carry_forward.py`, and a change to the statement's meaning ends
  coverage of the new tree until the claim is re-graded.
