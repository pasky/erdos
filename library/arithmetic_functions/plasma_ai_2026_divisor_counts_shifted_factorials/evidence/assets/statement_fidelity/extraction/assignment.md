# Whole-statement fidelity examination: Problem 420 density clauses

Examination date: 2026-10-20. You are an independent reviewer in a fresh
context, distinct from the authors and from the subsequent grader. Seek a
counterexample, semantic mismatch, hidden hypothesis, or unsupported inference
in the correspondence between these Lean statements and the problem. Agreement
is not the goal. This is a statement-fidelity review, not a prose-proof audit
or a numerical tier assessment. Compilation and kernel replay are separate.

## Frozen subject and allowed reading

Read only this assignment and these files in this extraction:

- `problem_statement.md`: the Statement of
  `wiki/problems/arithmetic_functions/E0420/_index.md`, frozen on 2026-10-20;
  status, assessment, and review material have been excluded.
- `challenge.lean`, `statement.lean`, `solution.lean`: code from
  `Challenge.lean`, `Erdos420/Statement.lean`, and `Solution.lean` of the held
  `evidence/assets/erdos_420_formalization.tar.gz`. Only block comments were
  removed; declarations and proof terms are unchanged. Challenge and Solution
  are alternative modules, not intended to be imported together.
- `lean-toolchain`, `lake-manifest.json`, `comparator.json`: the exact pins and
  target selection from that source.
- `report_contract.md`: the complete repository-specific report contract and
  canonical checklist. Apply every item within statement-fidelity scope.

You may additionally inspect standard Lean and Mathlib definitions and lemmas
at the pinned version where needed to resolve semantics. Record the exact
module paths and declarations used. Do not inspect the source project's README,
formalization metadata, mathematical proof note, build reports, prior reviews,
research notes, other corpus pages, or any sibling review. Do not browse the web
or search broadly. Ask the commissioner if additional subject material is needed.
Report every exposure outside this read set and its effect on the examination.
The extraction was prepared by the commissioner; do not extract additional
material from the owning problem or source card yourself.

## Questions requiring a verdict

1. Does `F` denote the stated factorial divisor ratio? Unfold factorial,
   divisors.card, casts, division, and the natural floor. Examine zero inputs,
   negative f, nonintegral f, and denominator nonvanishing.
2. Restate part iii with every quantifier and compare it with the third
   question. Check Monotone, Tendsto atTop atTop, the eventual log bound,
   image of Ici N, closure, Ioi 1, and the domain of f. Identify any strengthening
   or weakening and prove that it answers the target question as written.
3. Restate part ii and compare with the second question. Explain density in
   (1,infinity) versus a range allowed to contain 1. Check log at 0 and 1 and
   the specialization from part iii, without assuming monotonicity of log
   on an inappropriate domain.
4. Compare the challenge definitions and declarations with the solution-side
   definitions and declarations. The replay will separately check their entire
   statement dependency closure. Identify any mismatch visible here.
5. Determine exactly which of the three questions are covered. Do the two
   statements together settle the divergence question? State what a partial
   claim may assert, with no unsupported consequence.

No local L-claims are premises. Standard Lean/Mathlib semantics are the external
interfaces to inspect. Treat the two theorem proofs as awaiting independent
kernel validation; do not infer validity from their names or closed bodies.

## Report and independence

Write only `evidence/verify/statement_fidelity/report.md` in the owning source
home; the commissioner supplies the absolute output path separately. Do not modify the
subject. Use ordinary Markdown without frontmatter; integration will add it.
Use repository-relative paths in the filed report and identify the date and
scope, your fresh-context independence, actual reading and exposures. Give
clause-by-clause comparisons, all checklist verdicts, up to three independently
rederived weakest semantic steps, the strongest attempted refutation, premises,
and a faithful/not faithful verdict for each theorem, with the exact coverage.
A separate grader will rule on the report and any exposures. Do not state a
native tier or claim that a kernel replay has succeeded.
