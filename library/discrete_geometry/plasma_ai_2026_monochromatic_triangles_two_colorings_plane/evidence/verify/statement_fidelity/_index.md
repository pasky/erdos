---
name: discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/evidence/verify/statement_fidelity
title: Statement fidelity of the Problem 173 challenge statements
desc: |
  Accepted independent statement-fidelity audit, on 2026-10-19, of the
  definition and five statements in the Problem 173 formalization's challenge
  file, with its distinct grade: all faithful, the Statement covered whole under
  both readings of a triangle, the claim partly, no tier awarded.
created: 2026-10-18T02:18:16Z
updated: 2026-10-19T03:51:30Z
---

# Statement fidelity of the Problem 173 challenge statements

[[discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/evidence/verify/_index|..]]

[[discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/evidence/verify/statement_fidelity/grade|grade]]: A distinct grader's check, on 2026-10-19, of the five-statement Problem 173
fidelity audit: PASS, every part of the contract present, each verdict
re-derived, the exposure immaterial and the refutation charge met.

[[discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/evidence/verify/statement_fidelity/report|report]]: Fresh-context refutation-charge audit, on 2026-10-19, of the definition and
five statements of the Problem 173 formalization's challenge file against
the problem's Statement under both readings of a triangle, Shader's theorem,
the remark on the exception and Conjecture 3: all faithful, the Statement
covered whole, the claim partly.

***

**Accepted judgment.** The
[[discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/evidence/verify/statement_fidelity/report|report]]
audits, under a refutation charge, the definition `HasMonochromaticCopy` and
the five statements of the formalization's `Challenge.lean`:
`Erdos173.erdos_173` against the Statement of
[[../wiki/problems/discrete_geometry/E0173/_index|Problem 173]] with a triangle
read as three non-collinear points; `Erdos173.erdos_173.variants.right_triangle`
against Shader's Theorem 2; `Erdos173.erdos_173.variants.equilateral_exception`
against the problem page's remark that some coloring misses an equilateral
triangle; `Erdos173.erdos_173.variants.non_equilateral` against Conjecture 3 of
*Euclidean Ramsey Theorems, III* for nondegenerate triangles; and
`Erdos173.erdos_173.variants.three_distinct_points` against Conjecture 3 with a
triangle read as any three distinct points. The distinct
[[discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/evidence/verify/statement_fidelity/grade|grade]]
passes the report. The definition and all five statements are faithful; a copy
may be reflected and relabelled, but not rescaled, as the Statement's
congruence allows. `Challenge.lean` copies formal-conjectures' definition and
first three statements verbatim, apart from their attribute lists (`category`,
`question` and `AMS 5 51`) and the local `ℝ²` notation; the two added
statements are the formalization's own.

The Statement is covered whole under both readings of a triangle: by
`erdos_173` alone when a triangle is three non-collinear points, and by
`erdos_173` with `three_distinct_points` when it is any three distinct points.
The claim the formalization accompanies is covered in part. Not covered: its
requirement that the copy come from a translation and a rotation alone, since
every statement allows reflected copies, and its identification of the
alternating-strips coloring, which the formalization states only in prose. Its
single missed side length, that an exceptional triangle is equilateral and that
its side depends on the coloring follow from the statements without being
stated. The grade records three slips of the report that change no verdict.
This is statement-fidelity acceptance only. It awards no tier, and it covers
neither the proofs nor the build.

**Exact subject.** The extraction the reviewer and the grader read was frozen on
2026-10-19 and is held byte for byte under
[assets/statement_fidelity/extraction/](../../assets/statement_fidelity/extraction/assignment.md):

- `assignment.md`: the reviewer's assignment.
- `problem_statement.md`: the targets, the Statement and the question's
  commentary on `wiki/problems/discrete_geometry/E0173/_index.md`, the Claim
  paragraph of `wiki/problems/discrete_geometry/E0173/claims/1976_05_01_shader.md`,
  and Conjectures 2 and 3 of *Euclidean Ramsey Theorems, III* with the
  passages that define them, as they stood on 2026-10-19.
- `claim_statement.md`: the Claim and Covers paragraphs of
  `wiki/problems/discrete_geometry/E0173/claims/2026_10_19_plasma_ai.md` as
  they stood on 2026-10-19.
- `challenge.lean`: `Challenge.lean` of plasma-ai/erdos-173 at commit 4193b5f,
  with the definition and the five statements above; it is byte for byte the
  `Challenge.lean` of commit 4a368a6, which the held archive holds and the
  replay receipt checks.
- `fc_173.lean` and `fc_2d.lean`: formal-conjectures'
  `FormalConjectures/ErdosProblems/173.lean` and
  `FormalConjecturesForMathlib/Geometry/2d.lean` at its commit 7db2ea3b91 of
  2026-10-14, under their Apache-2.0 headers.

The grader's commission is
[assets/statement_fidelity/grading_assignment.md](../../assets/statement_fidelity/grading_assignment.md).
The records name their files relative to the folder they were written in, where
`extraction/` and `grading_assignment.md` lay beside `report.md` and
`grade.md`. The reviewer and the grader returned their records as text; they
are filed as returned, except that a blank line opens each list, as the wiki's
Markdown requires.

**Independence.** The reviewer and the grader each worked from a fresh context,
apart from the author of the formalization, the author of the extraction and
each other, and each read only its read set. Each discloses that the agent
environment placed general instruction text and directory names in its context.
The grade rules that exposure immaterial by the content test.
