# Grading assignment: Problem 420 statement fidelity

You are a fresh-context grader, distinct from the author and the reviewer.
Grade the report PASS or VOID. No native mathematical tier is sought.
Examination date: 2026-10-20.

## Allowed reading

Read only this assignment, the statement-fidelity report at
`../../verify/statement_fidelity/report.md`, and the files explicitly named in
`extraction/assignment.md`, including that assignment. Standard Lean and
Mathlib definitions at the pinned version may be inspected under the same
permission as the reviewer. Do not inspect source-card or claim acceptance
text, reproduction results, previous verdicts, or unrelated research material.
General repository reading instructions do not expand this scoped assignment.

## Grade requirements

Independently assess the assignment's adequacy and the report's compliance with
`extraction/report_contract.md`. Identify the actual subject and read set,
independence facts and any exposure. Rule on each exposure's materiality by
whether it influenced the attack or supplied reasoning unavailable in the allowed
subject; do not treat mere agreement as independence.

Check the semantic reasoning yourself, especially natural versus integer floor,
negative shifts and finite-prefix effects, the domain and monotonicity of log
at natural zero, nonvanishing factorial-divisor denominators, closure versus
relative density, every-tail quantifiers, eventual bounds, and the distinction
between density and a limit along all integers. Confirm both challenge/solution
comparisons and the scope of the resulting partial claim.

The report must give its subject and independence, restatements, explicit
verdicts for every canonical checklist item, independent derivations of the
weakest semantic steps, a serious strongest attack, premise/definition
boundaries, and a verdict for each theorem with exact coverage. A missing
contract part, material contamination without a justified ruling, or a
substantive error in a verdict makes the report VOID. Note immaterial errors
without silently rewriting the reviewer's report.

## Filed grade

Write only `evidence/verify/statement_fidelity/grade.md` in the owning source
home; the commissioner provides the absolute output path. Use ordinary Markdown
without frontmatter. Include Subject and independence, Contract, Soundness,
Exposure ruling, Refutation charge, Grade (PASS or VOID), and Accepted judgment.
Use repository-relative paths and roles, never machine-local paths or personal,
agent, session or tool-harness names. If PASS, state exactly what is faithful
and which questions are answered. A favorable grade is about statement fidelity;
it does not assert successful reproduction, public acceptance, or a native tier.
