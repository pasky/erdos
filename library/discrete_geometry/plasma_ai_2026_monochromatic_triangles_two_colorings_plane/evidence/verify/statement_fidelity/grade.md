---
name: discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/evidence/verify/statement_fidelity/grade
title: Grade of the Problem 173 fidelity audit
desc: |
  A distinct grader's check, on 2026-10-19, of the five-statement Problem 173
  fidelity audit: PASS, every part of the contract present, each verdict
  re-derived, the exposure immaterial and the refutation charge met.
created: 2026-10-18T02:18:16Z
updated: 2026-10-19T02:49:23Z
---

***

# Grade of the Problem 173 fidelity audit

- **Grader:** I am an independent fresh-context grader. I did not write the material under audit or the report. Examination date (UTC): 2026-10-19. I read these files in full: `grading_assignment.md`, `report.md`, `extraction/assignment.md`, `extraction/problem_statement.md`, `extraction/claim_statement.md`, `extraction/challenge.lean`, `extraction/fc_173.lean` and `extraction/fc_2d.lean`. I ran no command, compiled nothing, searched nothing and used no web source.

  Material outside the read set: the launch environment put the organization's and the repository's general agent-instruction text into my context. It also added environment details (working directories, platform, date) and an account note. It gave the grading assignment as an absolute path, which shows a worktree name and the library folder name. None of this concerns Problem 173 or its formalization, and this grade relies on none of it. Points marked "(general knowledge)" rest on my general knowledge of Lean 4, Mathlib or the mathematics.

- **Contract:** All parts are present.

  - **Subject:** present. It gives the role and independence with no names, the six files read, the freeze date 2026-10-19, and the scope: the definition, the five theorems, the bridge, the colorings, the copy claim with the docstrings, and coverage.
  - **Independence:** present. It says what was read. It discloses four exposures: the instruction text, directory names, the link targets printed inside `problem_statement.md`, and the import files it did not read.
  - **(a) Restatement:** present. It restates all five targets, the definition and all five Lean statements.
  - **(b) Clause-by-clause comparison:** present. It unfolds every definition the assignment lists: `ℝ²`, `Affine.Triangle`, `Congruent`/`≅`, `Fin 2` colorings, `Equiv.Perm` composed with `T.points`, `∠`, `dist`, `Function.Injective` and `HasMonochromaticCopy`. It compares each of the five theorems. It checks the bridge of item 6 in both directions under both readings. It also covers items 7, 8 and 9.
  - **(c) Checklist:** present. All five modes are judged applicable or not, with reasons.
  - **(d) Strongest attack:** present. It attacks the reflection convention. The attack fails against the targets and finds a coverage gap in the claim. The other failed attacks are listed.
  - **Verdicts:** present. The definition and all five theorems are judged "faithful" in full words, and the copy claim holds. Coverage of the Statement is judged whole under reading (a) and under reading (b). Coverage of the claim is judged partial, with the gaps named.

- **Soundness:** I checked each point of item 2 myself and agree with the report on all of them.

  1. **`erdos_173`.**
     - Exceptions are closed under congruence and under relabelling. If `T'` witnesses a copy for `T`, then `T'.points ∘ τ` stays affinely independent (general knowledge) and is `≅ T.points ∘ τ`. Read literally as "at most one point set", the Statement would allow no exception at all. So "at most one up to congruence" is the only coherent reading, and it is the same as "any two exceptions are congruent".
     - The conclusion parses as `(T₁.points ∘ σ) ≅ T₂.points`. A distance-preserving matching of the two vertex sets extends to an isometry of the plane (general knowledge). Conversely, an isometry between the vertex sets gives `σ`, since the vertices are distinct. The count is not changed to "none" and is not taken up to labelling.
     - `σ` is needed. A scalene exception `T` and its relabelling `T ∘ (0 1)` are both exceptions, but they are not `≅`, because d(T0,T2) ≠ d(T1,T2).
     - `HasMonochromaticCopy` ranges over every triangle with the same distances, label by label. That allows reflected and relabelled copies, but not rescaled ones. This matches "congruent copy" in the Statement under the standard convention of Euclidean Ramsey theory (general knowledge) and under the 1975 paper's side-length parametrization.
     - The report's argument that category theory's `≅` cannot elaborate is right: an isomorphism is a `Type`, while each position needs a `Prop`.
  2. **`right_triangle`.** `∠ (T.points 0) (T.points 1) (T.points 2)` is the unoriented angle at vertex 1. Any right triangle can be relabelled by a transposition so the right angle sits at vertex 1, and a witness for the relabelled triangle transfers back. So every right triangle is covered. The junk value π/2 occurs only at coincident points, which a `Triangle` cannot have. Nothing is assumed beyond the target.
  3. **`equilateral_exception`.** The triangle `T` is affinely independent, so its side is positive and the two distance equalities make it a genuine equilateral triangle. A constant coloring cannot witness the theorem, because `T` itself is then a monochromatic copy.

     I re-derived the strips witness. Use half-open strips of height h = (√3/2)s. An equilateral triangle of side s has vertical extent between h and s, and s < 2h. A monochromatic copy would therefore need vertices only in strips k and k+2, so two vertices share a strip. The third vertex lies within vertical distance h of their midpoint, so it cannot reach the strip two away. The theorem is neither vacuous nor degenerate.
  4. **`non_equilateral`.** The hypothesis `hT` is exactly "the three sides are not all equal", which is "not equilateral", with no other restriction. Through the bridge, the conclusion for every `c` is R(K). The restriction to `Affine.Triangle` leaves out only sets of three distinct collinear points, with sides (a, b, a+b), such as (a,2a,3a). The 3-4-5 triangle shows the statement is not vacuous.
  5. **`three_distinct_points`.**
     - `Function.Injective p` means the three points are pairwise distinct, and it puts no condition on collinearity.
     - `he` means "not equilateral". Three distinct collinear points are never equilateral: the outer distance is the sum of the other two, so it is strictly larger. So every collinear triple of distinct points satisfies `he` and falls under the theorem.
     - In the conclusion, `q ≅ p` forces positive distances between distinct labels, so `q` is three distinct points. It allows reflected and relabelled copies, and it excludes rescaling.
     - Triples with coincident points are excluded by `hp`. They belong neither to Conjecture 3 nor to the Statement under either reading. The report adds that the paper's zero-side triples are never exceptions; that remark is correct.
     - The points (0,0), (1,0), (2,0) satisfy both hypotheses, and the conclusion then needs a genuine monochromatic configuration. The theorem is not vacuous, and there is no junk value to exploit.
  6. **Bridge and the two readings.**
     - The easy direction is immediate.
     - The hard direction holds because the Gram entries are determined by the distances: ⟨u,v⟩ = (d01²+d02²−d12²)/2. A nonzero Gram determinant means u and v are linearly independent, which means the three points are affinely independent (general knowledge).
     - Under reading (a), `erdos_173` alone covers the Statement whole.
     - Under reading (b), take two exceptions. The contrapositive of `three_distinct_points` makes each one equilateral with side s > 0. Their Gram determinant is 3s⁴/4 ≠ 0, so each forms a triangle. The easy bridge direction shows neither triangle has a monochromatic copy, and `erdos_173` then gives `σ`. So the Statement is covered whole, using exactly the steps the report names.
  7. **Copy comparison and docstrings.**
     - I compared the two files line by line. The differences are exactly the six the report lists. The definition and the three copied theorem statements, with their docstrings, are identical.
     - The report notes that the removed attribute lists also hold `question` and `AMS 5 51`, not only `category`. That note is accurate and changes no verdict.
     - The statements depend only on structures that `fc_2d.lean`'s added instances do not touch. The report correctly calls the unread import files an assumption, not a finding.
     - Every docstring assertion either holds or is correctly marked as not checkable in the read set (the catalog attribution, `Solution.lean` and Comparator).
  8. **Coverage.**
     - The Statement is covered whole under both readings.
     - The claim is covered only in part. The single missed side length and its x ≠ 1 form follow without being stated, and the equivalence holds by rescaling the coloring.
     - The claim's "obtained by a translation and a rotation" is not covered, and I agree. For a scalene non-collinear triangle, the matching of vertices is forced by the distances, so a mirror copy is not a direct copy. Applying the theorems to a coloring composed with a reflection only reflects whatever copy they give, so nothing in them yields a direct copy. For collinear and isosceles triples the two notions agree.
     - That the exception is equilateral, and that its side depends on the coloring, follow as the report says. The identification of the strips coloring is prose only.

  Minor errors that change no verdict:

  - The report says the category-theory `≅` cannot elaborate in "any of the five positions". `challenge.lean` contains `≅` only three times; the count reaches five only if `fc_173.lean`'s two are added.
  - It writes "R_c(K)" where the paper writes R_f(K).
  - It says a congruent set "under any correspondence" can serve as `T'`. It means the correspondence that the congruence supplies.

- **Exposure ruling:** Immaterial. The report discloses that the general instruction text and directory names, including the library folder's name, reached its context; it discloses no repository status snapshot. By the content test, every finding traces to the extraction or to knowledge the report marks as general. The folder name adds nothing that `claim_statement.md` does not already say. The direction of the strongest attack, reflections, comes from assignment items 1, 5 and 9 and from the claim's "translation and a rotation". The strength of the refutation charge comes from the assignment.

- **Charge:** Met. The reviewer built a real attack on the reflection convention and carried it to a precise coverage gap in the claim. It also tested whether `σ` is needed, whether the two notions of exception match under reading (b), whether collinear triples escape `he`, whether the witness for `equilateral_exception` could be vacuous or degenerate, and whether the `∠` junk value could be reached. It derived the strips witness and its treatment of coincident and zero-side triples on its own.

- **Grade:** PASS. Every part of the contract is present. All six verdicts, the copy verdict and the coverage verdicts survive my independent check against the extraction, including the `σ` and reflection analysis of `erdos_173`, the relabelling argument for `right_triangle`, the Gram-determinant bridge, and the four-step argument for reading (b). The errors I found are a miscount, a notation slip and one loose phrase, and none of them touches a verdict. The disclosed exposure is immaterial under the content test, and the refutation charge was genuinely pursued.

- **Accepted judgment:**

  - `Erdos173.HasMonochromaticCopy`: faithful.
  - `Erdos173.erdos_173`: faithful.
  - `Erdos173.erdos_173.variants.right_triangle`: faithful.
  - `Erdos173.erdos_173.variants.equilateral_exception`: faithful.
  - `Erdos173.erdos_173.variants.non_equilateral`: faithful.
  - `Erdos173.erdos_173.variants.three_distinct_points`: faithful.
  - **Copy claim:** holds. The definition and the first three theorems, with their docstrings, are identical to `fc_173.lean`. The removed attribute lists hold `question` and `AMS 5 51` as well as `category`. The only addition to the copied part is the local `ℝ²` notation with its docstring.
  - **Statement, reading (a)** (a triangle is three non-collinear points): covered whole by `erdos_173` alone.
  - **Statement, reading (b)** (a triangle is any three distinct points): covered whole by `erdos_173` with `three_distinct_points`, through the bridge.
  - **Claim:** partial.
    - Not covered: the requirement that the copy come from a translation and a rotation alone, since every statement allows reflected copies; and the identification of the strips coloring, which is prose only.
    - Follows without being stated: the single missed side length and its x ≠ 1 form, that an exceptional triangle is equilateral, that its side depends on the coloring, and the Statement under reading (b).
    - Stated: a monochromatic copy of every non-equilateral set of three distinct points, collinear ones included, with reflections allowed; "all but at most one triangle" under reading (a); that one exception is needed; and that no regularity is assumed of the coloring.
