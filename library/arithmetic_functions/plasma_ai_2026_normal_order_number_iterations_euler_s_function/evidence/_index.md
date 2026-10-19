---
name: arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence
desc: |
  The held Lean formalization of Plasma AI's Problem 408 preprint, as the
  repository's tree at its pinned commit without the paper, and this corpus's
  verification records of it.
tags: []
sources: []
created: 2026-10-14T20:24:15Z
updated: 2026-10-19T06:24:13Z
---

# arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence

[[arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/_index|..]]

[[arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/_index|verify/]]: This corpus's verification records for the held Lean formalization of
Plasma AI's Problem 408 preprint: the receipt of its rebuild, Comparator
check and kernel replay, and the statement-fidelity audit of its three
challenge statements with the audit's distinct grade.

***

The formalization is held as
[assets/erdos_408_formalization.tar.gz](assets/erdos_408_formalization.tar.gz):
the tree of [plasma-ai/erdos-408](https://github.com/plasma-ai/erdos-408) at
commit 4ea44bf without its `paper/` folder, made by
`git archive 4ea44bf -- . ':(exclude)paper' | gzip -n`. The statement-fidelity
audit of its challenge statements is filed under
[[arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/_index|verify/]].
[util/replay.sh](util/replay.sh) rebuilds it at its pinned toolchain under
[util/build.sb](util/build.sb), checks it with Comparator and replays its three
theorems in the kernel; the receipt of the run is under `verify/`.
