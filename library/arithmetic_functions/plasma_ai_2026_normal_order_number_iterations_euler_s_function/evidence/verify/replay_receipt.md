---
name: arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/replay_receipt
title: "Replay receipt: Plasma AI's Problem 408 formalization"
desc: |
  Build, Comparator check and kernel replay of Plasma AI's Problem 408
  formalization at 5b02bf9 on Lean v4.35.0, on 2026-10-14: Comparator accepts
  its three theorems against the challenge, each replays in the kernel from an
  empty environment, and each depends only on propext, Classical.choice and
  Quot.sound.
created: 2026-10-14T22:51:27Z
updated: 2026-10-14T22:51:27Z
---

***

**Subject.** The held archive
[erdos_408_formalization.tar.gz](../assets/erdos_408_formalization.tar.gz),
the tree of [plasma-ai/erdos-408](https://github.com/plasma-ai/erdos-408) at
commit `5b02bf9ab59fd813af8f19c604ba70254fced08d` without its `paper/`
folder. On 2026-10-14 its extraction matched, file for file, a fresh
`git archive` of that commit from a fresh clone of the public repository. The
three theorems are `Erdos408.normal_order_rate`,
`Erdos408.erdos_408.parts.i` and `Erdos408.erdos_408.parts.ii`, stated with
`sorry` in `Challenge.lean` and proved in `Solution.lean`; the tree's
`comparator.json` names them and permits the axioms `propext`,
`Quot.sound` and `Classical.choice`.

**Environment.** The toolchain the tree pins, `leanprover/lean4:v4.35.0`,
with Mathlib at the commit its `lake-manifest.json` pins,
`56a005855ea17e0b0958f73ec801ae140b0a1679` (tag `v4.35.0`), from Mathlib's
prebuilt cache; the tree's vendored libraries and its own modules were compiled
from source. Comparator at its tag `v4.35.0`, commit
`e3dcf3083fc53d44b27a4431fabf7d43181583f5`, with lean4export at its tag
`v4.35.0`, commit `5a9a355dc6c5fd82b69058d433e2ae2e8dfbf8fe`. The machine was
an arm64 Mac, and the work folder was outside the repository.

**Command.** [replay.sh](../util/replay.sh) `WORKDIR fetch`, then
`replay.sh WORKDIR check` with `LEAN_NUM_THREADS=4` at the lowest scheduling
priority. The check ran under [build.sb](../util/build.sb): no network, and
writes only to the work folder, the temporary folders and lake's and elan's
caches. It took 1 h 25 min, most of it the compile.

**Result (2026-10-14).**

- **Comparator**, run before anything else built `Solution`: it built
  `Challenge` (2,075 jobs) and `Solution` (12,774 jobs, all succeeding),
  exported both with lean4export, matched the three theorems' statements, and
  the Lean kernel accepted the solution: "Your solution is okay!". Comparator's
  own sandbox, landrun, runs only on Linux, so its `scripts/fake-landrun.sh`
  stood in and build.sb was the sandbox. The build printed linter, deprecation
  and module-system warnings and no error.
- **Kernel replay** with the Conjectures.io card's
  [Replay.lean](../../../../number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/Replay.lean),
  from an empty environment on Lean 4.35.0. For each theorem the closure holds
  no unsafe or partial constant, the kernel accepted it, its type equals the
  challenge's, and every constant its statement reaches is identical in the
  challenge and the solution:

  | Theorem | Constants replayed | Replay | Statement constants |
  | --- | --- | --- | --- |
  | `Erdos408.normal_order_rate` | 143,078 | 232 s | 1,883, identical: PASS |
  | `Erdos408.erdos_408.parts.i` | 143,091 | 225 s | 2,201, identical: PASS |
  | `Erdos408.erdos_408.parts.ii` | 143,084 | 223 s | 2,198, identical: PASS |

- **`#print axioms`** on each of the three: `propext`,
  `Classical.choice`, `Quot.sound`.

**Statement check.** Whether the three statements say what Problem 408 and the
preprint's Theorem 1.1 say is the separate, graded
[[arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/statement_fidelity/_index|statement-fidelity audit]]:
all three faithful, the coverage partial, since the problem's third question is
not formalized.

**Standing.** A locally rebuilt, kernel-replayed external formal proof whose
whole statement a graded fresh-context review found faithful is documented
independent acceptance of that external result (`docs/anatomy.md` "Tiers").
It confers no tier, since the proof is not in this repository's Lean closure.
