---
name: research/leads/equilateral_two_scale/evidence/verify/whole_conclusion
title: Whole-conclusion review of the two-scale triangle proof
desc: |
  A separate grade accepts the independent review's refutation-failed
  verdict for the arbitrary-coloring conclusion at every positive unequal
  real ratio. Exact subjects, derivations, source boundaries and the
  runnable rational check are retained.
created: 2026-10-17T08:30:38Z
updated: 2026-10-17T08:30:38Z
---

# Whole-conclusion review of the two-scale triangle proof

[[research/leads/equilateral_two_scale/evidence/verify/_index|..]]

[[research/leads/equilateral_two_scale/evidence/verify/whole_conclusion/grade|grade]]: Independent pass-or-void grade of the complete frozen Problem 173 review,
its isolation, proof coverage, executable evidence and adoption limits.

[[research/leads/equilateral_two_scale/evidence/verify/whole_conclusion/review|review]]: Independent adversarial examination of the complete supplied argument for
Problem 173, including arbitrary colorings, transcendental scale ratios,
degenerate triangles, and the source specializations.

[[research/leads/equilateral_two_scale/evidence/verify/whole_conclusion/source_access|source_access]]: Exact editions and lawful access for the source interfaces examined in
the two-scale proof, separating text-level proof coverage from PDF
fidelity, external theorem assumptions and unused results.

***

The [[research/leads/equilateral_two_scale/evidence/verify/whole_conclusion/grade|separate grade]]
of 2026-10-17 is **PASS**, accepting the
[[research/leads/equilateral_two_scale/evidence/verify/whole_conclusion/review|whole review]]'s
mathematical verdict **refutation-failed**. Both examinations covered the
frozen conclusion and its complete consumed argument. The reviewer and
grader were distinct from the authors and from each other, with fresh
isolated contexts; the grade supplies their eligibility ruling. Filing
these records adds no independent mathematical judgment.

For every map $c:\mathbb R^2\to\{-1,1\}$, the accepted conclusion says
that at most one positive equilateral side length is missing, and every
non-equilateral triple of distinct points has a monochromatic congruent
copy. Collinear triples are included. Equivalently, for every real $x>0$,
$x\ne1$, a monochromatic equilateral triangle of side $1$ or $x$ occurs.
For measurable colorings, every non-equilateral triangle has a
positive-measure set of monochromatic placements, for area times arc
length. The exception, if present, depends on the coloring.

The examined chain supplies its rigidity input by proof. Its conclusion
does not assume the separate Lean interface (R0). The grade does not
accept the unused two-element template argument, the alternative spectral
argument, or the full proper-unit-distance-coloring result as standalone
results. Their narrower statements and standing remain as recorded on
their own pages. Source-proof coverage, formalization fidelity, novelty,
outside acceptance and the problem's catalog status are separate from
this mathematical review. No claim card or problem-status decision is
made by this record.

## Exact subject and retained evidence

The subject is the native argument frozen on 2026-10-17, identified by
original paths and retained line ranges in
[`subject_manifest.json`](../../assets/whole_conclusion/subject_manifest.json).
Its eight exact excerpts are under
`wiki/research/leads/equilateral_two_scale/evidence/assets/whole_conclusion/native_subject/`.
They preserve the problem statement, whole conclusion, unit template,
rigidity extension, template conversion, binary transfer, circle proof
and spectral proof. The uniform `[cut]` marker denotes omitted text; the
retained sections, rather than an entire page, delimit the examined
subject. The editable proof pages retain the same examined mathematical
statements and deductions.

The exact [submitted review](../../assets/whole_conclusion/submitted_review.md)
and [submitted grade](../../assets/whole_conclusion/submitted_grade.md)
are preserved alongside the
[independent grading derivations](../../assets/whole_conclusion/keepers/grader_derivations.md).
The source editions, lawful access paths and external theorem boundaries
are set out in the
[[research/leads/equilateral_two_scale/evidence/verify/whole_conclusion/source_access|source-access account]].
The historical procedural adapter named in the submitted grade is not
distributed with the public corpus; it is not a mathematical input.
The report contract itself is retained in `docs/verification.md`.

The maintained review and grade have authored display titles and
wiki-generated navigation and metadata. The maintained review's two
execution commands use the explicit `python3` executable. The maintained
grade describes its historical procedural adapter without a private
operating-file path and rejoins a line break within `relative-singularity`.
These are the only editorial transformations of the
submitted reports. The submitted snapshots, subject excerpts, derivations,
checker, literal inputs, mathematical checks and verdicts are unchanged.

## Reproduction and adoption check

From the repository root, run:

```sh
python3 -I wiki/research/leads/equilateral_two_scale/evidence/assets/whole_conclusion/keepers/bessel_bounds.py
python3 -I -O wiki/research/leads/equilateral_two_scale/evidence/assets/whole_conclusion/keepers/bessel_bounds.py --negative-control
```

The first command must exit zero. The second deliberately replaces a
rational upper bound by a false one and must exit one with
`row 0: S_20 < upper fails`. It tests rejection with Python optimization
enabled. The standard-library checker reads no external input and writes
no files. Its scope is the nine rational Taylor enclosures and fixed
scalar margins; the analytic and infinite-range arguments are in the
reviewed proofs.

The adopted-path check on 2026-10-17 verified the retained bytes and
executed both commands with those exit codes. The positive run obtained
energy margins $15583/100000000$ and $3/62500$, and exclusion gap $1/375$.
This checks the grade's filing and reproducibility conditions. A saved
success message supplies no substitute for rerunning the executable.
