# Grading assignment: the fidelity audit of the Erdős Problem 408 challenge statements

You are an independent grader with a fresh context. You are distinct from the author of the material under audit and from the reviewer who wrote the report. Your task is to grade one filed report: PASS or VOID.

## Read set (read only these files)

- `grading_assignment.md`: this file.
- `report.md`: the report to grade.
- `extraction/assignment.md`: the reviewer's assignment.
- `extraction/problem_statement.md`, `extraction/challenge.lean`, `extraction/paper_theorem_1_1.tex`, `extraction/fc_408.lean`, `extraction/fc_density.lean`: the frozen subject the reviewer read.

All paths are relative to this folder. Read no other file. Do not search the filesystem, run git or a build, or use the web.

## What to check

1. **The contract.** The report must have:
   - a Subject block giving the reviewer's role and independence facts with no names, the files read, the freeze date and the exact scope;
   - an Independence section saying what was read, whether any exposure occurred, and what it was;
   - (a) a restatement of each target and each Lean statement;
   - (b) a clause-by-clause comparison that covers every clause and definition the assignment lists;
   - (c) a verdict for each checklist mode the assignment names, saying whether each applies;
   - (d) the strongest attack attempted, and why it failed or what it found;
   - a verdict for each theorem in full words ("faithful" or "not faithful (defect: …)"), with a coverage statement.

   A missing part voids the report.
2. **Soundness.** Check the reasoning against the extraction yourself. In particular:
   - the treatment of f at n = 0 and n = 1, against the problem's and the paper's definitions;
   - the equivalence of the local `HasDensity` with `Set.HasDensity` at `A = univ`;
   - the equivalence of `parts.ii` with a normal order on a density-one set, including the diagonal argument;
   - the reading of "distribution function" in `parts.i`, including the residual "every c" reading the report raises;
   - the junk-value accounting in `normal_order_rate` (n = 1, n = 2, log log at 1 and 2) and whether the constant C absorbs it;
   - the coverage statement.

   A substantive error in a verdict voids the report. An error that changes no verdict is noted, but does not void it.
3. **Exposure materiality.** The report says the agent environment put the organization's and the repository's general instruction files, a repository status snapshot and environment details into the reviewer's context. Rule by the content test: could anything in the report have come only from that material, or did the direction of an attack or the strength of the refutation charge follow it? Say whether the exposure was material.
4. **Charge.** Did the reviewer genuinely attempt refutation, rather than agree?

## Your grade

Return your grade as the text of your final reply, in this form:

- **Grader:** your role, as an independent fresh-context grader, with no names. The examination date is 2026-10-14. List the files read.
- **Contract:** each part, present or missing.
- **Soundness:** your independent check of each point in item 2, with any errors.
- **Exposure ruling:** material or immaterial, with the reason.
- **Charge:** met or not met.
- **Grade:** PASS or VOID, with the reason in one paragraph.
- **Accepted judgment:** if PASS, restate the accepted verdicts for the three theorems and the coverage.
