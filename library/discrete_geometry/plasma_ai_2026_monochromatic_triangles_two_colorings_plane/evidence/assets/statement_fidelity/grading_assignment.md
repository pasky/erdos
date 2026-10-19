# Grading assignment: the fidelity audit of the Erdős Problem 173 challenge statements

You are an independent grader with a fresh context. You are distinct from the author of the material under audit and from the reviewer who wrote the report. Your task is to grade one filed report: PASS or VOID.

## Read set (read only these files)

- `grading_assignment.md`: this file.
- `report.md`: the report to grade.
- `extraction/assignment.md`: the reviewer's assignment.
- `extraction/problem_statement.md`, `extraction/claim_statement.md`, `extraction/challenge.lean`, `extraction/fc_173.lean`, `extraction/fc_2d.lean`: the frozen subject the reviewer read, frozen on 2026-10-19.

All paths are relative to this folder. Read no other file. Do not search the filesystem, run git or a build, or use the web.

## What to check

1. **The contract.** The report must have:
   - a Subject block giving the reviewer's role and independence facts with no names, the files read, the freeze date and the exact scope;
   - an Independence section saying what was read, whether any exposure occurred, and what it was;
   - (a) a restatement of each target and each of the five Lean statements;
   - (b) a clause-by-clause comparison that covers every clause and definition the assignment lists, including the bridge of its item 6;
   - (c) a verdict for each checklist mode the assignment names, saying whether each applies;
   - (d) the strongest attack attempted, and why it failed or what it found;
   - a verdict for each of the five theorems and for the definition in full words ("faithful" or "not faithful (defect: …)"), a verdict on the copy claim, and a coverage statement against the Statement under each reading of "triangle" and against the claim.

   A missing part voids the report.
2. **Soundness.** Check the reasoning against the extraction yourself. In particular:
   - the equivalence of `erdos_173` with "all but at most one triangle up to congruence", including the role of the relabelling `σ` and of reflections in `HasMonochromaticCopy`;
   - that the angle hypothesis of `right_triangle` covers every right triangle;
   - that `equilateral_exception` is not vacuous or degenerate;
   - that the hypothesis of `non_equilateral` says exactly "not equilateral", and what its restriction to `Affine.Triangle` leaves out of Conjecture 3;
   - for `three_distinct_points`: that `Function.Injective p` means three distinct points, collinear ones allowed; that `he` means "not equilateral" and whether any collinear triple of distinct points is equilateral; that the conclusion allows reflection and relabelling but not rescaling; how triples with coincident points are treated; and that the theorem is not vacuous;
   - the bridge between a monochromatic congruent copy of three labelled points and `HasMonochromaticCopy` for an affinely independent triple, and whether `erdos_173` and `three_distinct_points` together cover the Statement whole when three distinct collinear points count as a triangle, and when they do not;
   - the verbatim-copy comparison with `fc_173.lean`, which applies to the definition and the first three theorems only, and the check of the module docstring's assertions;
   - the coverage statements against the Statement and against the claim.

   A substantive error in a verdict voids the report. An error that changes no verdict is noted, but does not void it.
3. **Exposure materiality.** If the report discloses that the agent environment put instruction files, a repository status snapshot or environment details into the reviewer's context, rule by the content test: could anything in the report have come only from that material, or did the direction of an attack or the strength of the refutation charge follow it? Say whether any exposure was material.
4. **Charge.** Did the reviewer genuinely attempt refutation, rather than agree?

## Your grade

Return your grade as the text of your final reply, in this form:

- **Grader:** your role, as an independent fresh-context grader, with no names. Give the UTC date of your examination. List the files read.
- **Contract:** each part, present or missing.
- **Soundness:** your independent check of each point in item 2, with any errors.
- **Exposure ruling:** material or immaterial, with the reason.
- **Charge:** met or not met.
- **Grade:** PASS or VOID, with the reason in one paragraph.
- **Accepted judgment:** if PASS, restate the accepted verdicts for the five theorems and the definition, the copy claim, and the coverage against the Statement under each reading and against the claim.
