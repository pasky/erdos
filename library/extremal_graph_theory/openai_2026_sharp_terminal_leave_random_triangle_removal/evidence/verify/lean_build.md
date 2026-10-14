---
name: extremal_graph_theory/openai_2026_sharp_terminal_leave_random_triangle_removal/evidence/verify/lean_build
title: Build of the release's Lean proof of the sharp terminal leave
desc: |
  Plasma AI's build of 2026-10-14 of the release's comparator challenge and
  solution module for random triangle removal at the pinned revision, with
  Lean v4.34.1: both built, and the declaration's axioms are exactly propext,
  Classical.choice and Quot.sound.
created: 2026-10-14T00:34:43Z
updated: 2026-10-14T00:34:43Z
---

***

## Record and attribution

Builder: Plasma AI. Date of the run: 2026-10-14 (UTC). The builder had not
written the claim page's acceptance or the corpus's earlier, undated record of
a build of the same declaration. This is the build on which the
[[../wiki/problems/extremal_graph_theory/E1155/claims/2026_09_25_openai|Problem 1155 claim page]]
accepts the declaration `OAI.SharpTerminalLeave.sharp_terminal_leave`.

The record covers the build, the axiom check and one statement check, each
stated below. It gives no verdict on the statement's fidelity to the problem,
which the claim page's statement audit records, and none on the manuscript.

## Subject

- Repository: <https://github.com/openai/math>, the OpenAI mathematics
  release, at revision `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, the
  revision the claim page pins.
- Lean project: the release's `lean/` folder. Its `lean/lean-toolchain` pins
  `leanprover/lean4:v4.34.1`, and its `lean/lake-manifest.json` pins Mathlib
  at the commit tagged `v4.34.1`.
- Targets: the comparator challenge
  `lean/ComparatorChallenges/TriangleRemoval.lean` (module
  `ComparatorChallenges.TriangleRemoval`), whose configuration
  `lean/ComparatorChallenges/TriangleRemoval.json` names the solution module
  and permits only `propext`, `Classical.choice` and `Quot.sound`; and the
  solution module `lean/OAI/Combinatorics/TriangleRemoval/Main.lean` (module
  `OAI.Combinatorics.TriangleRemoval.Main`), whose import closure within the
  release is the 287 Lean files under `lean/OAI/Combinatorics/TriangleRemoval/`.

## Commands

The clone was made in an empty scratch folder outside this repository. Lean
4.34.1 was the toolchain elan selected from `lean/lean-toolchain`, and it
reported itself as the release build for arm64 macOS.

```sh
git clone --filter=blob:none --no-checkout https://github.com/openai/math.git
git -C math checkout --detach adc7f1241b42e322a6451854ab7e4b4c146bf78a
cd math/lean
lake exe cache get
lake build ComparatorChallenges.TriangleRemoval \
  OAI.Combinatorics.TriangleRemoval.Main
lake env lean ScratchE1155Solution.lean
lake env lean ScratchE1155Challenge.lean
```

The last two commands run two scratch files written in `lean/` for this check,
which are not part of the release. `ScratchE1155Solution.lean`:

```lean
import OAI.Combinatorics.TriangleRemoval.Main

open Filter
open scoped BigOperators Topology

namespace OAI.SharpTerminalLeave

-- The comparator challenge's statement, verbatim, elaborated against the
-- solution's model and closed by the solution's declaration.
example :
    Tendsto (fun n => expectation n (fun G =>
      (normalizedLeave n G - sharpConstant) ^ 2)) atTop (𝓝 0) ∧
    (∀ ε : ℝ, 0 < ε →
      Tendsto (fun n => probability n (fun G =>
        ε < |normalizedLeave n G - sharpConstant|)) atTop (𝓝 0)) ∧
    Tendsto (fun n => expectation n (fun G => (G.card : ℝ)) / normalization n)
      atTop (𝓝 sharpConstant) :=
  sharp_terminal_leave

end OAI.SharpTerminalLeave

#print axioms OAI.SharpTerminalLeave.sharp_terminal_leave
```

`ScratchE1155Challenge.lean`:

```lean
import ComparatorChallenges.TriangleRemoval

#print axioms OAI.SharpTerminalLeave.sharp_terminal_leave
```

## Result

- `lake exe cache get` exited 0. Lake's configuration step, which the
  release's `lean/lakefile.lean` defines, cloned the eleven packages that the
  release patches before dependency resolution and applied the release's
  compatibility patches from `lean/patches/` to them. Resolution then cloned
  every other required package at the revision `lean/lake-manifest.json`
  pins. Mathlib's prebuilt files for its pinned revision came from Mathlib's
  cache, which the build host already held, so none were downloaded.
- `lake build` exited 0 and reported "Build completed successfully (9211
  jobs)". It compiled from source the 288 release modules of the two targets'
  import closures: the challenge and the 287 files of the solution tree. Its
  one Lean warning was ``declaration uses `sorry` `` at
  `ComparatorChallenges/TriangleRemoval.lean:55:8`, the challenge's theorem,
  which a comparator challenge states with the body `sorry`. Lake also
  reported that the eleven patched packages have local changes, which are the
  applied patches.
- Both scratch files elaborated without error and each run exited 0. The
  `example` in `ScratchE1155Solution.lean` type-checked, so the solution's
  declaration proves the challenge's statement, read word for word against the
  solution's model in `lean/OAI/Combinatorics/TriangleRemoval/Model.lean`. A
  text comparison found that model's definitions identical to the challenge's,
  line for line.

## Axioms printed

For the solution's declaration:

```text
'OAI.SharpTerminalLeave.sharp_terminal_leave' depends on axioms: [propext, Classical.choice, Quot.sound]
```

For the challenge's declaration of the same name, whose body is `sorry`:

```text
'OAI.SharpTerminalLeave.sharp_terminal_leave' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
```

The solution's declaration depends on exactly the three axioms the challenge's
configuration permits, with no `sorryAx`. The `sorryAx` is the challenge's
open theorem, as expected.

## Not checked

The comparator program, which compares the two modules' fingerprints, was not
run. This record's evidence that the built declaration is the one the
challenge pins is the statement check and the text comparison above. The
statement audit against the problem, the manuscript and every module outside
the two targets' import closures lie outside this record.
