---
name: discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/evidence
desc: |
  The held repository of Plasma AI's Problem 173 blueprint and Lean
  formalization at its pinned commit, and this corpus's verification records
  of the formalization.
tags: []
sources: []
created: 2026-10-18T02:18:16Z
updated: 2026-10-19T03:06:09Z
---

# discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/evidence

[[discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/_index|..]]

[[discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/evidence/verify/_index|verify/]]: This corpus's verification records for the held Lean formalization of
Plasma AI's Problem 173 result: the receipt of its rebuild, Comparator check
and kernel replay, and the statement-fidelity audit of the definition and
five statements of its challenge file with the audit's distinct grade.

***

The repository is held as
[assets/erdos_173_formalization.tar.gz](assets/erdos_173_formalization.tar.gz):
the tree of [plasma-ai/erdos-173](https://github.com/plasma-ai/erdos-173) at
commit 4a368a6, blueprint included, made by `git archive 4a368a6 | gzip -n`.
The statement-fidelity audit of its challenge statements is filed under
[[discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/evidence/verify/_index|verify/]].
[util/replay.sh](util/replay.sh) rebuilds the formalization at its pinned
toolchain under [util/build.sb](util/build.sb), checks it with Comparator and
replays its five theorems in the kernel; the receipt of the run is under
`verify/`.
