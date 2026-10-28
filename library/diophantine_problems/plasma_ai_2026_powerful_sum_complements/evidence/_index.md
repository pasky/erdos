---
name: diophantine_problems/plasma_ai_2026_powerful_sum_complements/evidence
desc: |
  The held Lean formalization of the Problem 940 complement results, as its
  repository's tree at the pinned commit, with statement-review inputs and
  this corpus's verification records.
created: 2026-10-20T15:09:38Z
updated: 2026-10-28T16:00:09Z
---

# diophantine_problems/plasma_ai_2026_powerful_sum_complements/evidence

[[diophantine_problems/plasma_ai_2026_powerful_sum_complements/_index|..]]

[[diophantine_problems/plasma_ai_2026_powerful_sum_complements/evidence/verify/_index|verify/]]: Kernel replay and statement-fidelity records for the cubic and quartic complement targets.

***

The formalization is held as
[assets/erdos_940_formalization.tar.gz](assets/erdos_940_formalization.tar.gz):
the tree of [plasma-ai/erdos-940](https://github.com/plasma-ai/erdos-940) at
commit 491733e, made by `git archive 491733e | gzip -n`, with its vendored
libraries and their licenses. `assets/statement_fidelity/` holds
`Challenge.lean`, which contains the reviewed definitions and all four target
statements, and `mathematical_subject.md`, the mathematical claims they were
compared against. The other inspected source files are in the archive at the
paths listed on the
[[diophantine_problems/plasma_ai_2026_powerful_sum_complements/evidence/verify/statement_fidelity/_index|audit's subject record]].

The independent review and grade are filed under
[[diophantine_problems/plasma_ai_2026_powerful_sum_complements/evidence/verify/statement_fidelity/_index|statement fidelity]].
The reproduction script is [util/replay.sh](util/replay.sh). From the corpus
root, give it a fresh scratch directory:

```sh
bash library/diophantine_problems/plasma_ai_2026_powerful_sum_complements/evidence/util/replay.sh WORKDIR
```

The `fetch` phase extracts the archive, compares it with the source
repository when that is reachable, and fetches the pinned toolchain's
dependencies. The `check` phase runs Comparator,
replays each target's full dependency closure in an empty kernel environment,
and prints the axioms. It uses the corpus's shared
[Replay.lean](../../../number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/Replay.lean).
Allow several hours for a fresh build, and several GB of disk and memory.
A successful run checks the formal proof terms; it does not by itself check
that their statements express the intended mathematics.
