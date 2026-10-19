---
name: arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/replay_receipt
title: "Replay receipt: Plasma AI's Problem 408 formalization"
desc: |
  Build, Comparator check and kernel replay of Plasma AI's Problem 408
  formalization at 4ea44bf on Lean v4.35.0-rc3, on 2026-10-19: Comparator
  accepts its three theorems against the challenge, each replays in the kernel
  from an empty environment, and each depends only on propext,
  Classical.choice and Quot.sound.
created: 2026-10-14T22:51:27Z
updated: 2026-10-19T07:07:42Z
---

***

**Subject.** The held archive
[erdos_408_formalization.tar.gz](../assets/erdos_408_formalization.tar.gz),
the tree of [plasma-ai/erdos-408](https://github.com/plasma-ai/erdos-408) at
commit `4ea44bf911f8668aec10ec25c4b309e8ed476666` without its `paper/`
folder. On 2026-10-19 its extraction matched, file for file, a fresh
`git archive` of that commit from a fresh clone of the public repository. The
three theorems are `Erdos408.normal_order_rate`,
`Erdos408.erdos_408.parts.i` and `Erdos408.erdos_408.parts.ii`, stated with
`sorry` in `Challenge.lean` and proved in `Solution.lean`; the tree's
`comparator.json` names them and permits the axioms `propext`,
`Quot.sound` and `Classical.choice`.

**Environment.** The toolchain the tree pins, `leanprover/lean4:v4.35.0-rc3`,
with Mathlib at the commit its `lake-manifest.json` pins,
`c55e6e786f49471c72fbddbec5415808896aec1e` (tag `v4.35.0-rc3`), from
Mathlib's prebuilt cache, whose files were already in lake's cache folder; the
tree's vendored libraries and its own modules were compiled from source.
Comparator at its tag `v4.35.0-rc3`, commit
`fd5d5bcf14177b187f66d4502071268d877887c3`, with lean4export at its tag
`v4.35.0-rc3`, commit `66f1fb4bc256072069767fce52d39480e4524869`. The machine
was an arm64 Mac, and the work folder was outside the repository.

**Command.** [replay.sh](../util/replay.sh) `WORKDIR`, which runs the fetch
and then the check, with `LEAN_NUM_THREADS=6` at the lowest scheduling
priority. The check ran under [build.sb](../util/build.sb): no network, and
writes only to the work folder, the temporary folders and lake's and elan's
caches. It was stopped five times to free the machine's shared build slot for
other checks, and each time resumed with `replay.sh WORKDIR check` in the same
work folder, so lake reused the modules already built; each resumed check ran
Comparator again before anything else built `Solution`. The check took about
50 minutes in all, most of it the compile, and the three kernel replays about
10 minutes of that.

**Result (2026-10-19).**

- **Comparator**, run before anything else built `Solution`: it built
  `Challenge` (2,047 jobs) and `Solution` (8,158 jobs, all succeeding),
  exported both with lean4export, matched the three theorems' statements, and
  the Lean kernel accepted the solution: "Your solution is okay!". Comparator's
  own sandbox, landrun, runs only on Linux, so its `scripts/fake-landrun.sh`
  stood in and build.sb was the sandbox. The build printed the challenge's
  three `sorry` warnings and no error.
- **Kernel replay** with the Conjectures.io card's
  [Replay.lean](../../../../number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/Replay.lean),
  from an empty environment on Lean 4.35.0-rc3. For each theorem the closure
  holds no unsafe or partial constant, the kernel accepted it, its type equals
  the challenge's, and every constant its statement reaches is identical in the
  challenge and the solution:

  | Theorem | Constants replayed | Replay | Statement constants |
  | --- | --- | --- | --- |
  | `Erdos408.normal_order_rate` | 142,898 | 190 s | 1,882, identical: PASS |
  | `Erdos408.erdos_408.parts.i` | 142,911 | 189 s | 2,201, identical: PASS |
  | `Erdos408.erdos_408.parts.ii` | 142,904 | 196 s | 2,198, identical: PASS |

- **`#print axioms`** on each of the three: `propext`,
  `Classical.choice`, `Quot.sound`.

**Registry check, reported and not counted.** The Palomar registry's own
verification of the same commit,
[run 39195414479](https://github.com/PalomarRegistry/PalomarSubmission/actions/runs/39195414479)
of 2026-10-19 (checked at 04:46:55 UTC, on `leanprover/lean4:v4.35.0-rc3`),
reports a pass with no errors or warnings for the same three theorems and the
same permitted axioms. Its Comparator run had the con-ron kernel (140,944
declarations), the nanoda kernel and Lean's default kernel each accept the
solution. This is the registry's fact, not acceptance evidence here: under
`docs/verification.md` "Review and acceptance", acceptance rests on this
repository's own rebuild and replay above.

**Statement check.** Whether the three statements say what Problem 408 and the
preprint's Theorem 1.1 say is the separate, graded
[[arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/evidence/verify/statement_fidelity/_index|statement-fidelity audit]]:
all three faithful, the coverage partial, since the problem's third question is
not formalized.

**Standing.** A locally rebuilt, kernel-replayed external formal proof whose
whole statement a graded fresh-context review found faithful is documented
independent acceptance of that external result (`docs/anatomy.md` "Tiers").
It confers no tier, since the proof is not in this repository's Lean closure.
