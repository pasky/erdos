---
name: diophantine_problems/plasma_ai_2026_powerful_sum_complements/evidence/verify/statement_fidelity/grade
title: Grade of the Problem 940 statement-fidelity review
desc: |
  Independent grading of four external Lean statement-fidelity findings for
  the cubic and quartic complement conclusions of Problem 940.
tags: []
sources: []
created: 2026-10-20T15:16:31Z
updated: 2026-10-28T16:00:09Z
---

***

## Subject and independence

**Examination date:** 2026-10-20 UTC. **Role:** independent grader, distinct
from the subject author and the statement-fidelity reviewer. The grader
received a fresh-context grading assignment and had not participated in
constructing the subject or its review. No author's working discussion,
current claim standing, sibling review, or proposed acceptance decision was
supplied or read. No excluded communication or search exposure occurred.

The report graded is
`library/diophantine_problems/plasma_ai_2026_powerful_sum_complements/evidence/verify/statement_fidelity/review.md`,
examined in full. The subject was the extraction frozen on
2026-10-20 UTC in
`library/diophantine_problems/plasma_ai_2026_powerful_sum_complements/evidence/assets/statement_fidelity/`.
All six files there were read in full: `mathematical_subject.md`,
`Challenge.lean`, `Solution.lean`, `Erdos940/Powerful.lean`,
`Erdos940/Statement.lean`, and `Erdos940/FinalAssembly.lean`. Paths in this
list are relative to the extraction directory used for the examination. The
[subject custody record](_index.md#subject-custody) identifies the two retained
inputs and the four files preserved in the pinned external source. The mathematical
subject reproduces the Problem 940 Statement and the cubic and quartic Claim
and Covers sections; no current claim page was consulted. The extraction was
not edited. This grade identifies those examined statements and does not
independently establish their custody in another checkout.

Governance reading was `docs/verification.md` in full,
`docs/anatomy.md` sections “Tiers” and “Problems and claims,” and
`docs/lean_authoring.md` sections “Statement fidelity and data discipline” and
“Statement fidelity and validation,” with the following “Repository facts”
paragraphs. Links in these documents did not expand the mathematical read set.

The grader also inspected the following dependency-relative Mathlib source
ranges in the authorized Lean 4.35.0-rc4 environment:

- `Mathlib/Data/Nat/PrimeFin.lean`, lines 15–85: prime-factor membership and
  its zero and one cases.
- `Mathlib/Data/Set/Card.lean`, lines 620–698: `ncard`, finite cardinality,
  the infinite-set default, and the finset interface.
- `Mathlib/Order/Filter/AtTopBot/Basic.lean`, lines 60–90: eventual and
  frequent quantifiers at infinity.
- `Mathlib/Data/Multiset/Defs.lean`, lines 50–85 and 207–245: the list
  quotient and cardinality.
- `Mathlib/Algebra/BigOperators/Group/Multiset/Defs.lean`, lines 20–95:
  the additive sum generated from the product definition and its empty,
  cons, singleton, and repetition interfaces.

This reading checked definitions and theorem interfaces, not their proofs.
No standard-library source, external website, build configuration, dependency
lock, native manifest, Comparator implementation, or mechanical verification
record was read. The environment version is supplied commission information;
this grade does not verify its pin. No executable computation supports the
grading judgment.

## Report contract and isolation

**The report meets the external-result statement-fidelity contract for all
four targets.** It identifies the frozen subject, records its allowed and
actual reading, states the reviewer's separation from authorship, and discloses
the limits of its source access. It restates each target separately and gives
each a concrete attempted mismatch. Its three shared semantic derivations
explicitly apply to both exponents. Both the repository checklist and the
canonical failure modes and named patterns have individual verdicts; the
inapplicable entries explain the semantic scope rather than purporting to
clear unread proofs. Premises, consequences, and limitations are explicit.

The reviewer's isolation record is adequate. Its only disclosed intervening
instruction corrected an inaccessible authorized dependency location and
supplied no mathematics. That administrative correction is immaterial: the
reported attacks and their answers are derivable from the frozen subject and
the named imported interfaces. The source comments about attribution,
priority, and current knowledge were visible in the authorized extraction;
the reviewer expressly excluded them from its verdict. The report contains no
finding that depends on accepting those comments.

The attacks are substantive semantic checks, not agreement with a successful
build. In particular, the reviewer tested an integer reciprocal against a
real positive lower density, eventual bounds against subsequence bounds,
multisets against distinct summands, and negated eventuality against a single
exception. Its zero, one, exponent, and multiplicity probes distinguish
different mathematical statements. The finite examples are not used to prove
the infinite conclusions. A structurally different computational reproduction
leg is therefore inapplicable.

No native L-claim is consumed in this semantic comparison. Omitting a live
ledger reading is appropriate here and says nothing about the dependencies of
the external proof. This is not a whole-proof tier-1 report; its explicitly
scoped verdict does not need to assert that an unread proof survived attack.

## Per-target grades and mathematical coverage

The declaration names below occur in both frozen `Challenge.lean` and
`Solution.lean`.

| Declaration | Grade | Accepted semantic coverage |
| --- | --- | --- |
| `Erdos940.cubic_complement_density` | **pass** | The cubic Claim's positive lower natural density assertion, with its infinitude consequence. |
| `Erdos940.quartic_complement_density` | **pass** | The quartic Claim's displayed counting inequality, its positive lower density consequence, and its infinitude consequence. |
| `Erdos940.cubic_large_integers` | **pass** | The cubic Claim's infinitude assertion and the first-question specialization at exponent three in Covers. This target alone does not prove density. |
| `Erdos940.quartic_large_integers` | **pass** | The quartic Claim's infinitude assertion and the first-question specialization at exponent four in Covers. This target alone does not prove density. |

The grader checked the central equivalences independently. For a nonzero
natural summand, `mem_primeFactors` identifies precisely its prime divisors;
at zero the empty factor set agrees with the fact that every prime power
divides zero. One is permitted. A multiset counts repetitions, and its sum
uses every occurrence. Removing zero entries preserves the sum and reduces
the number of summands. Thus the positive convention and the quartic
zero-removal clause agree with the formal natural-number convention.

Write \(A_r(N)\) for the number of nonrepresentable naturals below \(N\).
The counted set is finite, so the infinite-set default of `ncard` is
irrelevant. The density targets assert one \(C>0\) chosen before a threshold,
followed by \(N\le C A_r(N)\) for every later natural cutoff. This gives
\(A_r(N)/N\ge1/C\) for positive cutoffs. Conversely, a positive lower
density supplies an eventual positive real bound \(\delta\); choosing a
positive integer \(C\ge1/\delta\) gives the formal inequality. Changing
between strict natural cutoffs and positive inclusive cutoffs changes the
count by at most one. An integer threshold can be replaced by a nonnegative
one. None of these changes alters the claimed density or eventual bound.

A finite complement of size \(K\) would contradict the density bound at a
cutoff exceeding both the threshold and \(CK\). Separately, negating
eventual representability means that every natural threshold has a missing
integer above it. This is equivalent to an infinite complement in the
naturals. Zero is already representable by the empty multiset, so this is
also infinitude of positive exceptions. These arguments justify both
consequence sentences without treating either infinitude target as a density
theorem.

The Covers clauses are respected individually. The cubic targets address
exponent three only; the quartic targets address exponent four only. Neither
pair asserts representable density zero or answers the infinitude question
for higher exponents. A complement of positive lower density need not have
density one. The cubic Covers explanation concerning one progression is a
restriction on what follows, not an additional progression theorem: a set
can avoid a progression and still have positive density elsewhere. The report
correctly makes no claim to verify the manuscript's progression result or its
statement of what remains unknown. The cubic Claim's attribution to a named
corollary, its posting and source-card description, and comments about priority
are bibliographic or historical assertions outside these four mathematical
targets; this grade does not certify them.

## Sufficiency and remaining conditions

**This graded semantic review is sufficient for external acceptance of the
four stated results once the separate required mechanical checks pass for
the matching external artifact.** No unresolved semantic defect or required
statement correction remains in the reviewed scope.

The omitted definitions `missingCount` and
`HasPositiveLowerDensityComplementFor` occur in proof interfaces, not in the
four target statements or the definitions determining their meaning. Their
omission does not leave the semantic comparison incomplete. The Challenge
and solution-side `Nat.Full` and `Representable` definitions match, and the
visible final target types have the required exponents, quantifiers,
inequalities, and conclusions. Correctness of the internal adapters belongs
to checking their proof terms.

Before external acceptance, separate evidence must establish the repository's
own rebuild on the pinned toolchain, kernel replay from an empty environment
of every declaration on which each accepted target depends, and an axiom
closure containing no axioms beyond `propext`, `Classical.choice`, and
`Quot.sound`. It must also establish that the checked targets and reached
definitions are the ones covered by this frozen comparison; any claimed
Comparator success must be supported by its actual execution. The deliberate
proof holes in the Challenge are statement placeholders, not acceptable
proof evidence. A port may change proofs but may not change the target's
meaning.

These mechanical conditions were not examined and are not presumed to have
passed. This grade neither accepts a current claim page nor awards a
numerical tier. It certifies no manuscript proof, attribution, priority,
general-exponent result, or density-zero conclusion. A change to the reviewed
mathematical statement or a reached definition requires a new fidelity
assessment of that changed subject.
