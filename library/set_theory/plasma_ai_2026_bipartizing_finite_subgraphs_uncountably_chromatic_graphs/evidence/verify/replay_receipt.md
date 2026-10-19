---
name: set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/replay_receipt
title: "Replay receipt: Plasma AI's Problem 111 formalization"
desc: |
  Build, Comparator check and kernel replay of Plasma AI's Problem 111
  formalization at de72caf on Lean v4.35.0-rc3, on 2026-10-19: Comparator
  accepts its three theorems against the challenge, each replays in the kernel
  from an empty environment, and each depends only on propext,
  Classical.choice and Quot.sound.
created: 2026-10-18T02:15:08Z
updated: 2026-10-19T06:23:35Z
---

***

**Subject.** The held archive
[erdos_111_formalization.tar.gz](../assets/erdos_111_formalization.tar.gz),
the tree of [plasma-ai/erdos-111](https://github.com/plasma-ai/erdos-111) at
commit `de72caf0e388c729697b6813f4ea90bfe1617c7b`. On 2026-10-19 its
extraction matched, file for file, a fresh `git archive` of that commit from a
fresh clone of the repository. The three theorems are
`Erdos111.countably_colorable_of_linear`,
`Erdos111.tendsto_of_not_countably_colorable` and `Erdos111.erdos_111`,
stated with `sorry` in `Challenge.lean` and proved in `Solution.lean`; the
tree's `comparator.json` names them and permits the axioms `propext`,
`Quot.sound` and `Classical.choice`.

**Environment.** The toolchain the tree pins, `leanprover/lean4:v4.35.0-rc3`,
with Mathlib and its dependencies fetched at the commits its
`lake-manifest.json` pins, Mathlib at
`c55e6e786f49471c72fbddbec5415808896aec1e` (tag `v4.35.0-rc3`), built from
Mathlib's prebuilt cache, whose files were already in lake's cache folder; the
tree's own modules were compiled from source. Comparator at its tag
`v4.35.0-rc3`, commit `fd5d5bcf14177b187f66d4502071268d877887c3`, with
lean4export at its tag `v4.35.0-rc3`, commit
`66f1fb4bc256072069767fce52d39480e4524869`. The machine was an arm64 Mac, and
the work folder was outside the repository.

**Command.** [replay.sh](../util/replay.sh) `WORKDIR`, which runs the fetch
and then the check, with `LEAN_NUM_THREADS=4` at the lowest scheduling
priority. The check ran under [build.sb](../util/build.sb): no network, and
writes only to the work folder, the temporary folders and lake's and elan's
caches. The check took under 2 minutes, and the whole run 2 minutes 35
seconds.

**Result (2026-10-19).**

- **Comparator**, run before anything else built `Solution`: it built
  `Challenge` (1,255 jobs) and `Solution` (2,994 jobs, all succeeding),
  exported both with lean4export, matched the three theorems' statements, and
  the Lean kernel accepted the solution: "Your solution is okay!". Comparator's
  own sandbox, landrun, runs only on Linux, so its `scripts/fake-landrun.sh`
  stood in and build.sb was the sandbox. The build printed the challenge's
  three `sorry` warnings and no error.
- **Kernel replay** with the Conjectures.io card's
  [Replay.lean](../../../../number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/Replay.lean),
  from an empty environment on Lean 4.35.0-rc3. For each theorem the closure
  holds no unsafe or partial constant, its axioms are `propext`,
  `Classical.choice` and `Quot.sound`, the kernel accepted it, its type equals
  the challenge's, and every constant its statement reaches is identical in the
  challenge and the solution:

  | Theorem | Constants replayed | Replay | Statement constants |
  | --- | --- | --- | --- |
  | `Erdos111.countably_colorable_of_linear` | 37,085 | 10 s | 1,572, identical: PASS |
  | `Erdos111.tendsto_of_not_countably_colorable` | 37,195 | 10 s | 1,761, identical: PASS |
  | `Erdos111.erdos_111` | 37,204 | 10 s | 2,040, identical: PASS |

- **`#print axioms`** on each of the three: `propext`,
  `Classical.choice`, `Quot.sound`.

**Statement check.** Whether the three statements say what Problem 111 and the
claim say is the separate, graded
[[set_theory/plasma_ai_2026_bipartizing_finite_subgraphs_uncountably_chromatic_graphs/evidence/verify/statement_fidelity/_index|statement-fidelity audit]]:
all three faithful, the second question covered whole, the open-ended first
question not formalized.

**Standing.** A locally rebuilt, kernel-replayed external formal proof whose
whole statement a graded fresh-context review found faithful is documented
independent acceptance of that external result (`docs/anatomy.md` "Tiers").
It confers no tier, since the proof is not in this repository's Lean closure.
