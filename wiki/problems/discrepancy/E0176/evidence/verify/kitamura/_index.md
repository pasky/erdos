---
name: problems/discrepancy/E0176/evidence/verify/kitamura
title: Whole-proof record for the two discrepancy bounds
desc: A distinct PASS grade covers nine precise conclusions from the Kitamura argument, including polynomial bounds, finite minima and exponential consequences; catalog acceptance remains pending.
created: 2026-10-15T23:59:17Z
updated: 2026-10-15T23:59:17Z
---

# Whole-proof record for the two discrepancy bounds

[[problems/discrepancy/E0176/evidence/verify/_index|..]]

[[problems/discrepancy/E0176/evidence/verify/kitamura/grade|grade]]: Independent grading of the unchanged whole-proof examination of E176 discrepancy bounds, finite minima, one-term cases, and exponential consequences.

[[problems/discrepancy/E0176/evidence/verify/kitamura/report|report]]: Independent adversarial examination of two arithmetic-progression discrepancy bounds, their finite bases and exponential consequences.

***

The [whole-proof examination](report.md), dated 2026-10-15 UTC,
has verdict **refutation-failed** on each of nine conclusions. Its
[distinct independent grade](grade.md) is **PASS** for each conclusion and
for the whole report. This is mathematical proof inspection with exact finite
reproduction. Neither record certifies Lean execution or the original builds.

Write $N(k,\ell)$ for the least positive interval length forcing a
positive-difference $k$-term arithmetic progression of absolute discrepancy
at least $\ell$ in every sign coloring. The reviewed scope is:

- For $k\ge5$, $N(k,2)\le\lfloor 2(k^2-1)(k-1)(2k+1)/(k-3)\rfloor+1$.
- For $k\ge2$, $N(k,\sqrt k)\le\lfloor\frac43(k^2-k+1)(k-1)(k(k-1)+1)\rfloor+1$.
- $N(2,2)=3$, $N(3,2)=9$, and $N(4,2)=13$, with every smaller positive length excluded.
- $N(1,2)$ does not exist, whereas $N(1,1)=1$.
- $N(k,2)\le16^k$ for $k\ge2$, and $N(k,\sqrt k)\le64^k$ for $k\ge1$.

The two source claim pages remain pending catalog acceptance:
[[problems/discrepancy/E0176/claims/2026_06_21_kitamura|the target 2]] and
[[problems/discrepancy/E0176/claims/2026_06_23_kitamura|the square-root target]].
The `ell_ck` question and Erdős–Graham's strict variant are outside this
nine-conclusion examination. It supplies no new whole-catalog decision.

## Argument and evidence

The [report](report.md) rederives the finite Fourier and Fejér
identities, counts all wrapping starts, and proves a strict positive gap
before selecting the least successful positive length. The square-root
argument uses its own weighted gap, not the target-2 polynomial conclusion.
Floors are applied after real division. Translation between $[0,N)$ and
$\{1,\ldots,N\}$ preserves the exact non-strict discrepancy property.
The finite bases use two structurally different routes: sign enumeration
and partition inclusion-exclusion or a balanced four-block recurrence.
The latter's mathematical reductions are part of the report, not inferred
from matching output. The exponential consequences pay for every base case.

All exact code, inputs and witnesses are retained under [the assessed subject and inputs](../../assets/kitamura/reviewed/subject/manifest.json).
From `evidence/assets/kitamura/reviewed/`, run `rerun.py --output` with an explicit disposable
output path through the prepared Python environment, as the report's
Reproduction section specifies. It freshly executes both routes and three
false-minimum controls under optimization, compares all 28 rows representing
17,421 sign colorings, and confirms the 17 frozen runtime imports. A failed
control, count, witness or import check is a nonzero result. The source Lean
files are static proof-reading material; no Lean command is part of this
reproduction.

## Qualifications and retained subject

The grade's independence ruling uses the visible primary records and their
absence of excluded received material. The historical inbox was unavailable,
not established empty. That explicit evidentiary limitation survives this
filing. The theorem proofs have no unread external mathematical premise;
source-archive identity, the second archive's unlisted Basic file, and any
formal build remain outside the examination's coverage.

Kenta Kitamura / KitaKen1 receives source credit, with the source's disclosed
preparation assistance preserved. Plasma AI receives the extraction,
finite-probe, consequence and independent-derivation credit. The two source
archives' Apache 2.0 licenses were separately inspected for this filing and
a copy is retained beside the excerpts; this is not an enlargement of the
grader's source-reading claim.

The mathematical statement, proof, source excerpts and executable operations
match the examined subject. Editorial filing removes private custody hashes
and operating directives from the manifest/provenance, replaces the author's
obsolete docstring path by its relative public filename, and appends source
attribution/extraction notices without changing the reviewed source lines.
The reports' statements about unchanged input bytes describe the original
examinations; these disclosed filing changes are non-mathematical. The [submitted report](../../assets/kitamura/reviewed/report.md) and
[submitted grade](../../assets/kitamura/grade.md) retain their assessed text.
The filed copies maintain relative links to the retained assets and rejoin one wrapped compound word in the report. The complete
original delivery remains retained for custody. No later mathematical repair
or stronger statement inherits the grade.
