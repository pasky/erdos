---
name: arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/statement_fidelity
title: Statement fidelity of the Problem 408 challenge statements
desc: |
  Accepted independent statement-fidelity audit, on 2026-10-14, of the three
  statements in the Problem 408 formalization's challenge file, with its
  distinct grade: all three faithful, coverage partial, no tier awarded.
created: 2026-10-14T20:39:30Z
updated: 2026-10-19T06:24:13Z
---

# Statement fidelity of the Problem 408 challenge statements

[[arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/_index|..]]

[[arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/statement_fidelity/grade|grade]]: A distinct grader's check, on 2026-10-14, of the Problem 408 fidelity
audit: PASS, every part of the contract present, each verdict re-derived,
the exposure immaterial and the refutation charge met.

[[arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/statement_fidelity/report|report]]: Fresh-context refutation-charge audit, on 2026-10-14, of the three
statements of the Problem 408 formalization's challenge file against the
problem's first two questions and the preprint's Theorem 1.1: all three
faithful, coverage partial.

***

**Accepted judgment.** The [[arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/statement_fidelity/report|report]]
audits, under a refutation charge, the three statements of the formalization's
`Challenge.lean`: `Erdos408.normal_order_rate` against Theorem 1.1 of the
preprint, and `Erdos408.erdos_408.parts.i` and `Erdos408.erdos_408.parts.ii`
against the first two questions of
[[../wiki/problems/arithmetic_functions/E0408/_index|Problem 408]] as its
Formulation reads them. The distinct
[[arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/statement_fidelity/grade|grade]] passes the report. All three
statements are faithful. The coverage is partial: the first two questions are
covered whole, the second under the Formulation's normal-order reading, and the
third, on the largest prime factor of $\phi_k(n)$, is not formalized. One
residual is recorded: under a non-standard reading of "distribution function"
that asks for a density at every point, `parts.i` leaves out the density of
$\{n : f(n)\le\alpha\log n\}$. This is statement-fidelity acceptance only.
It awards no tier, and it covers neither the proofs nor the build.

**Exact subject.** The extraction the reviewer read was frozen on 2026-10-14 and
is held, byte for byte, under
[assets/statement_fidelity/extraction/](../../assets/statement_fidelity/extraction/assignment.md):

- `assignment.md`: the reviewer's assignment.
- `problem_statement.md`: the Statement and Formulation paragraphs of
  `wiki/problems/arithmetic_functions/E0408/_index.md` as they stood on
  2026-10-14.
- `challenge.lean`: `Challenge.lean` of plasma-ai/erdos-408 at commit
  bd581ee, the parent of 5b02bf9. The two differ in one reflowed line of its
  module doc comment and nowhere in its definitions or statements, and the
  held commit 4ea44bf has the `Challenge.lean` of 5b02bf9 byte for byte, so
  the audit applies to the held copy unchanged.
- `paper_theorem_1_1.tex`: lines 37–62 of the preprint's TeX source, the
  definition of $f$ and Theorem 1.1.
- `fc_408.lean` and `fc_density.lean`: formal-conjectures'
  `FormalConjectures/ErdosProblems/408.lean` and
  `FormalConjecturesForMathlib/Data/Set/Density.lean` at its commit
  7db2ea3b91 of 2026-10-14, under their Apache-2.0 headers.

The grader's commission is
[assets/statement_fidelity/grading_assignment.md](../../assets/statement_fidelity/grading_assignment.md).
The records name their files relative to the folder they were written in, where
`extraction/` and `grading_assignment.md` lay beside `report.md` and
`grade.md`. The reviewer returned the report as text, and it is filed as
returned. Both records are filed verbatim, except that the grade's Grader line
names that folder in place of a machine-local path.

**Independence.** The reviewer and the grader each worked from a fresh context,
apart from the author of the extraction and from each other, and each read only
its read set. The report discloses that the agent environment placed general
instruction files, a repository status snapshot and environment details in its
context. The grade rules that exposure immaterial by the content test.

**Later change to the subject.** The problem page's Formulation has since gained
two sentences, which name the three parts and mark the third open-ended. The
reading of the first two questions is unchanged.
