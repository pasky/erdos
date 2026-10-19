---
name: set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence
desc: |
  The held Lean formalization of Plasma AI's Problem 111 result, as the
  repository's tree at its pinned commit, and this corpus's verification
  records of it.
tags: []
sources: []
created: 2026-10-18T02:15:08Z
updated: 2026-10-19T06:23:35Z
---

# set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence

[[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/_index|..]]

[[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/_index|verify/]]: This corpus's verification records for the held Lean formalization of
Plasma AI's Problem 111 result: the receipt of its rebuild, Comparator
check and kernel replay, and the statement-fidelity audit of its three
challenge statements with the audit's distinct grade.

***

The formalization is held as
[assets/erdos_111_formalization.tar.gz](assets/erdos_111_formalization.tar.gz):
the tree of [plasma-ai/erdos-111](https://github.com/plasma-ai/erdos-111) at
commit de72caf, made by `git archive de72caf | gzip -n`. The
statement-fidelity audit of its challenge statements is filed under
[[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/_index|verify/]].
[util/replay.sh](util/replay.sh) rebuilds it at its pinned toolchain under
[util/build.sb](util/build.sb), checks it with Comparator and replays its three
theorems in the kernel; the receipt of the run is under `verify/`.
