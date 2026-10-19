---
name: discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/evidence/verify/replay_receipt
title: "Replay receipt: Plasma AI's Problem 173 formalization"
desc: |
  Build, Comparator check and kernel replay of Plasma AI's Problem 173
  formalization at 4a368a6 on Lean v4.35.0-rc3, on 2026-10-19: Comparator
  accepts its five theorems against the challenge, each replays in the kernel
  from an empty environment, and each depends only on propext,
  Classical.choice and Quot.sound.
created: 2026-10-18T02:18:16Z
updated: 2026-10-19T03:10:59Z
---

***

**Subject.** The held archive
[erdos_173_formalization.tar.gz](../assets/erdos_173_formalization.tar.gz),
the tree of [plasma-ai/erdos-173](https://github.com/plasma-ai/erdos-173) at
commit `4a368a652753fab53272f7a747755876f04bc2cc`. On 2026-10-19 its
extraction matched, file for file, a fresh `git archive` of that commit from a
fresh clone of the repository. The five theorems are `Erdos173.erdos_173`,
`Erdos173.erdos_173.variants.right_triangle`,
`Erdos173.erdos_173.variants.equilateral_exception`,
`Erdos173.erdos_173.variants.non_equilateral` and
`Erdos173.erdos_173.variants.three_distinct_points`, stated with `sorry` in
`Challenge.lean` and proved in `Solution.lean`; the tree's `comparator.json`
names them and permits the axioms `propext`, `Quot.sound` and
`Classical.choice`.

**Environment.** The toolchain the tree pins, `leanprover/lean4:v4.35.0-rc3`,
with Mathlib at the commit its `lake-manifest.json` pins,
`c55e6e786f49471c72fbddbec5415808896aec1e` (tag `v4.35.0-rc3`), from Mathlib's
prebuilt cache; the tree's vendored `OAI/` modules and its own modules were
compiled from source. Comparator at its tag `v4.35.0-rc3`, commit
`fd5d5bcf14177b187f66d4502071268d877887c3`, with lean4export at its tag
`v4.35.0-rc3`, commit `66f1fb4bc256072069767fce52d39480e4524869`. The machine
was an arm64 Mac, and the work folder was outside the repository.

**Command.** [replay.sh](../util/replay.sh) `WORKDIR` with
`LEAN_NUM_THREADS=4` at the lowest scheduling priority, which runs the fetch
and then the check. The check ran under [build.sb](../util/build.sb): no
network, and writes only to the work folder, the temporary folders and lake's
and elan's caches. The fetch and check together took 8 min.

**Result (2026-10-19).**

- **Comparator**, run before anything else built `Solution`: it built
  `Challenge` (2,439 jobs) and `Solution` (3,915 jobs, all succeeding),
  exported both with lean4export, matched the five theorems' statements, and
  the Lean kernel accepted the solution: "Your solution is okay!". Comparator's
  own sandbox, landrun, runs only on Linux, so its `scripts/fake-landrun.sh`
  stood in and build.sb was the sandbox. The build printed the challenge's five
  intended `sorry` warnings and no error.
- **Kernel replay** with the Conjectures.io card's
  [Replay.lean](../../../../number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/Replay.lean),
  from an empty environment on Lean 4.35.0-rc3. For each theorem the closure
  holds no unsafe or partial constant, the kernel accepted it, its type equals
  the challenge's, and every constant its statement reaches is identical in the
  challenge and the solution:

  | Theorem | Constants replayed | Replay | Statement constants |
  | --- | --- | --- | --- |
  | `Erdos173.erdos_173` | 75,763 | 53 s | 3,041, identical: PASS |
  | `Erdos173.erdos_173.variants.right_triangle` | 75,778 | 65 s | 3,217, identical: PASS |
  | `Erdos173.erdos_173.variants.equilateral_exception` | 23,667 | 5 s | 3,045, identical: PASS |
  | `Erdos173.erdos_173.variants.non_equilateral` | 75,761 | 51 s | 3,045, identical: PASS |
  | `Erdos173.erdos_173.variants.three_distinct_points` | 75,716 | 52 s | 2,675, identical: PASS |

- **`#print axioms`** on each of the five: `propext`,
  `Classical.choice`, `Quot.sound`.

**Statement check.** Whether the definition and the five statements say what
Problem 173, Shader's theorem, the problem's remark on the exception and
Conjecture 3 of *Euclidean Ramsey Theorems, III* say is the separate, graded
[[discrete_geometry/plasma_ai_2026_monochromatic_triangles_two_colorings_plane/evidence/verify/statement_fidelity/_index|statement-fidelity audit]]:
all faithful, and the Statement covered whole whether or not three distinct
collinear points count as a triangle. The audit read `Challenge.lean` at
commit 4193b5f, which is byte for byte the `Challenge.lean` of the commit
replayed here.

**Standing.** A locally rebuilt, kernel-replayed external formal proof whose
whole statement a graded fresh-context review found faithful is documented
independent acceptance of that external result (`docs/anatomy.md` "Tiers").
It confers no tier, since the proof is not in this repository's Lean closure.
