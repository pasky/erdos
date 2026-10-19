---
name: set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/statement_fidelity
title: Statement fidelity of the Problem 111 challenge statements
desc: |
  Accepted independent statement-fidelity audit, on 2026-10-18, of the three
  statements in the Problem 111 formalization's challenge file, with its
  distinct grade: all three faithful, the second question covered whole, no
  tier awarded.
created: 2026-10-18T02:15:08Z
updated: 2026-10-19T06:41:06Z
---

# Statement fidelity of the Problem 111 challenge statements

[[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/_index|..]]

[[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/statement_fidelity/grade|grade]]: A distinct grader's check, on 2026-10-18, of the Problem 111 fidelity
audit: PASS, every part of the contract present, each verdict re-derived,
the exposure immaterial and the refutation charge met.

[[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/statement_fidelity/report|report]]: Fresh-context refutation-charge audit, on 2026-10-18, of the three
statements of the Problem 111 formalization's challenge file against the
problem's Statement, the claim's countable-coloring theorem and the challenge's
own Claim paragraph: all three faithful; the second question covered whole,
the open-ended first question not formalized.

***

**Accepted judgment.** The [[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/statement_fidelity/report|report]]
audits, under a refutation charge, the three statements of the formalization's
`Challenge.lean`: `Erdos111.erdos_111` against the second question of
[[../wiki/problems/set_theory/E0111/_index|Problem 111]]'s Statement,
`Erdos111.tendsto_of_not_countably_colorable` against the Claim paragraph of
the challenge's own module doc comment, and
`Erdos111.countably_colorable_of_linear` against the countable-coloring
theorem of the claim. The distinct
[[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/statement_fidelity/grade|grade]] passes the report. All
three statements are faithful. `erdos_111` covers the second question whole,
for graphs of chromatic number $\aleph_1$ at every vertex cardinality; the
first question, on the behaviour of $h_G(n)$, is open-ended and not
formalized. `tendsto_of_not_countably_colorable` implies `erdos_111`, and
letting $C$ range over all reals in `countably_colorable_of_linear` adds only
vacuous instances. This is statement-fidelity acceptance only. It awards no
tier, and it covers neither the proofs nor the build.

**Exact subject.** The extraction the reviewer read was frozen on 2026-10-18 and
is held, byte for byte, under
[assets/statement_fidelity/extraction/](../../assets/statement_fidelity/extraction/assignment.md):

- `assignment.md`: the reviewer's assignment.
- `problem_statement.md`: the Statement paragraph of
  `wiki/problems/set_theory/E0111/_index.md` as it stood on 2026-10-18.
- `claim_statement.md`: the first two paragraphs of the Claim section of
  `wiki/problems/set_theory/E0111/claims/2026_10_19_plasma_ai.md` as they stood
  on 2026-10-18.
- `challenge.lean`: `Challenge.lean` of plasma-ai/erdos-111 at commit
  115aef1. The held commit, de72caf, changes only two of its docstrings, so
  every declaration the audit read is unchanged. The module docstring now
  attributes the question to Erdős, Hajnal and Szemerédi, and its Claim
  paragraph, which the audit used as reference text, reads "for every real `C`
  (vacuous for `C < 0`)" where it read "for every `C ≥ 0`"; its sentence on
  `h G n / n → ∞` is unchanged. The docstring of `bipartizationNumber` adds
  that the subgraph has finitely many vertices in every use.
- `mathlib_definitions.lean`: excerpts of the Mathlib definitions the
  statements reach, at Mathlib v4.35.0 (commit 56a0058), the version 115aef1
  pins, each naming its file and lines, under Mathlib's Apache-2.0 license.
  The held commit de72caf pins Mathlib v4.35.0-rc3 (commit c55e6e7); on
  2026-10-19 each of the 12 excerpts was found there verbatim, at shifted line
  numbers.

The grader's commission is
[assets/statement_fidelity/grading_assignment.md](../../assets/statement_fidelity/grading_assignment.md).
The records name their files relative to the folder they were read in, where
`extraction/`, `grading_assignment.md` and the report lay side by side. The
reviewer and the grader returned their records as text, and they are filed as
returned, with these edits: in the report's Independence section and the
grade's Grader line, the instruction files are described generically in place
of their file name, and the repository's local name and its branch are removed;
the grade's note on that naming describes it without repeating the names. Paths,
scope, dates and verdicts are unchanged.

**Independence.** The reviewer and the grader each worked from a fresh context,
apart from the author of the formalization and the extraction and from each
other, and each read only its read set. The report discloses that the agent
environment placed general instruction files, a repository status snapshot and
an environment date in its context. The grade rules that exposure immaterial by
the content test.
