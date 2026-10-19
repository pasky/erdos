---
name: discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/evidence/verify
title: Verification records for the Problem 173 formalization
desc: |
  This corpus's verification records for the held Lean formalization of
  Plasma AI's Problem 173 result: the receipt of its rebuild, Comparator check
  and kernel replay, and the statement-fidelity audit of the definition and
  five statements of its challenge file with the audit's distinct grade.
created: 2026-10-18T02:18:16Z
updated: 2026-10-19T03:06:09Z
---

# Verification records for the Problem 173 formalization

[[discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/evidence/_index|..]]

[[discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/evidence/verify/replay_receipt|replay_receipt]]: Build, Comparator check and kernel replay of Plasma AI's Problem 173
formalization at 4a368a6 on Lean v4.35.0-rc3, on 2026-10-19: Comparator
accepts its five theorems against the challenge, each replays in the kernel
from an empty environment, and each depends only on propext,
Classical.choice and Quot.sound.

[[discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/evidence/verify/statement_fidelity/_index|statement_fidelity/]]: Accepted independent statement-fidelity audit, on 2026-10-19, of the
definition and five statements in the Problem 173 formalization's challenge
file, with its distinct grade: all faithful, the Statement covered whole under
both readings of a triangle, the claim partly, no tier awarded.

***

The records here check the formalization held in the
[archive](../assets/erdos_173_formalization.tar.gz) one step at a time. The
statement-fidelity audit compares the definition and the five statements of
its `Challenge.lean` with the problem's Statement, Shader's theorem, the
problem's remark on the exception and Conjecture 3 of *Euclidean Ramsey
Theorems, III*, and with the claim the formalization accompanies. The replay
receipt records the rebuild of the formalization, Comparator's check of the
five theorems against `Challenge.lean`, and their kernel replay from an empty
environment.
