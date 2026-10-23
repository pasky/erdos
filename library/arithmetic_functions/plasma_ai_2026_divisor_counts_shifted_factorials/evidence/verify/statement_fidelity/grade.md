---
name: arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/evidence/verify/statement_fidelity/grade
title: Grade of the Problem 420 statement-fidelity report
desc: |
  PASS for the independent statement-fidelity report on the two density
  questions; general-instruction exposure is ruled immaterial.
created: 2026-10-20T18:38:29Z
updated: 2026-10-20T18:38:29Z
---

***

## Subject and independence

Examination date: 2026-10-20. The grader is distinct from the subject author and
the reviewer and received a fresh context without a prior grading verdict. The
subject is
`library/arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/evidence/verify/statement_fidelity/report.md`.
Paths beginning with `evidence/` below are relative to that owning source
directory.

The actual read set was the report,
`evidence/assets/statement_fidelity/grading_assignment.md`, and all nine files
allowed by `evidence/assets/statement_fidelity/extraction/assignment.md`: that
assignment, `report_contract.md`, `problem_statement.md`, `challenge.lean`,
`statement.lean`, `solution.lean`, `lean-toolchain`, `lake-manifest.json`, and
`comparator.json`. The problem statement is the supplied frozen Statement from
`wiki/problems/arithmetic_functions/E0420/_index.md`; the original page was not
inspected. Neither the archive nor source-card acceptance text, claim acceptance
text, build or replay results, imported solution proofs, unrelated reports, or
web sources were read.

Targeted semantic checks used the supplied Mathlib version, pinned by the
extraction to `leanprover/lean4:v4.35.0-rc4`. The grader inspected definitions
or interfaces and nearby lines in `Mathlib/NumberTheory/Divisors.lean`
(`Nat.divisors`, `mem_divisors`, `one_mem_divisors`);
`Mathlib/Data/Nat/Factorial/Basic.lean` (`Nat.factorial`, `factorial_pos`,
`factorial_ne_zero`, `factorial_dvd_factorial`);
`Mathlib/Algebra/Order/Floor/Defs.lean` (`Nat.floor`) and `Semiring.lean`
(`floor_eq_iff`, `floor_of_nonpos`);
`Mathlib/Analysis/SpecialFunctions/Log/Basic.lean` (`Real.log`, `log_of_pos`,
`log_zero`, `log_one`, `log_le_log`, `tendsto_log_atTop`);
`Mathlib/Order/Monotone/Defs.lean` (`Monotone`, `Antitone`);
`Mathlib/Order/Filter/AtTopBot/Basic.lean` (`eventually_atTop`,
`tendsto_atTop_atTop`); `Mathlib/Order/Interval/Set/Defs.lean` (interval
definitions and their order-dual forms); `Mathlib/Data/Set/Operations.lean`
(`Set.range`, `mem_range`); `Mathlib/Topology/Closure.lean` (`mem_closure_iff`);
`Mathlib/Data/Finset/Card.lean` (`Finset.card`, `card_pos`); and
`Mathlib/Basic/Real/Basic.lean` (natural casts and the real field and division
instances). This was a semantic inspection, not a proof or library audit.

## Contract

The assignment is adequate for this focused examination. It supplies the exact
question, both declaration presentations, the ratio definition, target
selection, pins, the complete reporting contract, and permission to resolve
standard semantics. It explicitly separates statement correspondence from proof
validation. Excluding imported proof bodies is appropriate to that scope; it
prevents this report from warranting proof validity or complete elaborated
dependency identity.

The report satisfies every required part: subject and independence, quantified
restatements, all ten named checklist items with explicit verdicts, three
independently explained weakest steps, a concrete strongest attack, premise and
definition boundaries, and separate theorem verdicts with exact coverage. Its
computation and reproduction rulings are appropriate because no computation is
used as evidence and proof replay is outside its charge. The circularity finding
is expressly limited to displayed premises rather than the unread proofs. No
contract part is missing.

## Soundness

The semantic judgments withstand independent checking:

- **Ratio and denominator.** Factorial is the ordinary natural factorial. The
  divisor finset counts positive natural divisors, and every factorial is
  nonzero. Its divisor set contains 1, so its cardinality, including the
  denominator at zero, is positive. Both cardinalities are cast before real
  division. The zero convention for divisors therefore has no effect.
- **Floor transfer.** Natural floor is not integer floor on negative arguments.
  At $n=2$ and $f(2)=-1/2$, the printed ratio is $1/2$, whereas the formal ratio
  is 1. The report correctly retains this defect in unrestricted pointwise
  equality. Under iii, divergence supplies a natural cutoff $M$ beyond which
  $f(n)\geq0$. At every such index both floors agree. Applying iii with cutoff
  $\max(N,M)$ transfers each required approximation to the printed expression.
  Noninteger nonnegative inputs have the ordinary floor, with no rounding
  discrepancy.
- **Quantifiers and bounds.** Part iii states, for every admissible
  natural-indexed real sequence, every natural cutoff $N$, every real $x>1$, and
  every positive error tolerance, the existence of an index at least $N$
  approximating $x$. Its monotonicity is nondecreasing; a nonincreasing sequence
  cannot diverge to positive infinity. Its logarithmic bound is eventual. This
  enlarges the hypothesis class relative to an everywhere bound and still covers
  the printed question. No uniform cutoff in $f$, approximation rate, or
  positive density of indices is asserted.
- **Finite prefixes and topology.** For any nonempty open interval and any
  finite set of deleted values, a smaller nonempty open interval avoids those
  values. Density of the full range supplies a witness there, hence at an
  undeleted index. This proves the report's every-tail equivalence and
  finite-prefix transfer. Ambient closure contains every $x>1$ exactly when the
  range intersected with $(1,\infty)$ is dense in that interval: shrink a
  neighborhood about $x$ to radius less than $x-1$. Thus values equal to 1
  cannot create a false density verdict.
- **Log specialization.** At natural zero and one the logarithm is zero. For
  positive natural inputs, monotonicity follows from positive-domain logarithmic
  monotonicity; comparison from zero follows from $0=\log1\leq\log n$ for
  $n\geq1$. This does not use the false assertion that this extension is
  monotone on all nonnegative reals. Given a real threshold for divergence of
  log, choose a natural threshold above it; the natural-indexed sequence then
  diverges. The eventual bound holds by equality. Taking $N=0$ in iii gives ii.
  Deleting index zero preserves the required positive-index conclusion.
- **Declaration comparison and scope.** The two supplied definitions of F agree
  textually, and the two selected theorem statements in the challenge and
  solution agree, including their quantifiers and closures. This is the visible
  comparison supported by the extraction. Complete elaborated dependency
  identity and the imported proofs remain unchecked. The statements express the
  second and third density questions. For fixed $C>1$, $(\log n)^C>\log n$
  eventually, so iii does not apply to the first question's large powers.
  Density supplies arbitrarily late bounded approximations for the relevant
  shifts; it is not a limit to infinity along all integers and supplies no
  missing growth estimate for the larger shifts.

No substantive semantic error or immaterial error requiring correction was
found. The report's interpretation of the third question's unspecified density
interval as $(1,\infty)$ follows its immediate preceding question and is
disclosed rather than hidden.

## Exposure ruling

The reviewer discloses preloaded general repository instructions and the
commissioning message. Their described content supplies operational constraints
and reporting scope, not a prior mathematical verdict, proof, or unavailable
semantic argument. These exposures are immaterial to independence. The
unsuccessful lookup of a nonexistent permitted Mathlib file supplied no content
and is immaterial. Targeted Mathlib reading was authorized.

The grader likewise received general repository instructions and a commissioning
message, but no prior verdict or solution reasoning beyond the report under
examination and its allowed subjects. These contextual exposures are immaterial
for the same reason. The report itself is required grader evidence, not
contamination. Independence is supported by the separate fresh-context roles,
bounded reading, disclosed exposures, and the grader's independent checks above;
agreement alone is not the basis for this ruling. No material contamination is
identified in the supplied record.

## Refutation charge

The report seriously pursues refutation rather than relying on theorem names or
purported successful compilation. Its negative-floor example is an actual
counterexample to unrestricted equality, and its transfer argument answers that
objection precisely within the theorem's hypotheses. The grader also challenged
whether a finite prefix or the value 1 could falsely create interval density,
whether logarithmic monotonicity crosses zero improperly, and whether the
eventual hypothesis or every-tail conclusion changes the requested claim. The
open-interval and positive-natural-domain arguments above resolve those attacks.
No proof-validity conclusion is inferred from their failure.

## Grade

**PASS.** The report meets the contract, its disclosed exposures are immaterial,
and its statement-fidelity verdicts are sound within the assigned scope.

## Accepted judgment

`Erdos420.erdos_420.parts.ii` faithfully expresses an affirmative answer to the
second question, density of the logarithmic factorial-divisor ratios throughout
$(1,\infty)$. `Erdos420.erdos_420.parts.iii` faithfully answers the third
question, allowing an eventual logarithmic upper bound and explicitly expressing
every-tail density; eventual nonnegativity justifies its natural-floor
convention. The supplied challenge and solution presentations have no visible
statement mismatch.

The accepted partial judgment covers exactly those two density questions,
conditional on separate proof validation. It does not settle the first question
about divergence for large powers of log, assert successful reproduction or
public acceptance, or warrant a native mathematical tier.
