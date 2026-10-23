---
name: arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/evidence/verify/replay_receipt
title: "Replay receipt: Plasma AI's Problem 420 formalization"
desc: |
  Fresh project rebuild with cached vendored dependencies, Comparator check,
  and full empty-environment kernel replay on 2026-10-20. Both density
  theorems pass, with exactly propext, Classical.choice, and Quot.sound;
  their types and statement dependencies agree with Challenge.
created: 2026-10-20T19:37:05Z
updated: 2026-10-20T19:37:05Z
---

***

**Subject.** The held archive
[erdos_420_formalization.tar.gz](../assets/erdos_420_formalization.tar.gz)
contains [plasma-ai/erdos-420](https://github.com/plasma-ai/erdos-420) at
external commit `daa3bba1d72b41c80beaa8bb2114590ac2f76c6a`, excluding
`paper/`. Its 3,211 files were compared byte-for-byte with `git archive` of
that commit. The selected targets are `Erdos420.erdos_420.parts.iii` and
`Erdos420.erdos_420.parts.ii`, stated in `Challenge.lean` and proved in
`Solution.lean`. The archive's `comparator.json` selects both and permits
only `propext`, `Quot.sound`, and `Classical.choice`.

**Environment.** The pinned toolchain is `leanprover/lean4:v4.35.0-rc4`;
the running Lean reported version 4.35.0-rc4, source revision
`c29b6dda4f7c20e3eeaa717c4e565663c5cfa364`. Mathlib is pinned by
`lake-manifest.json` to `1f414401f69059aa7eead47b53ee40bd38455eeb`.
Comparator and lean4export were built at their `v4.35.0-rc4` tags, resolving
to `ca04cfc72b550331658ec314bf47685281bfd4bf` and
`05d43a2bc773b40ecfdebb32294192a5ef756951`, respectively. The check ran
on an arm64 Mac in scratch storage outside the repository, with
`LEAN_NUM_THREADS=4` and scheduling niceness 10.

**Build scope and cache provenance.** This was a fresh project rebuild with
cached vendored dependencies, followed by full kernel replay. A fresh archive
extraction received no build artifacts for `Erdos420`, `Challenge`, or
`Solution`. All 48 modules under `Erdos420/`, and both top-level target
modules, were compiled anew. The following dependency caches were reused:

- Mathlib and its eight manifest dependencies. Their source checkouts were
  clean at the nine pinned Git revisions. `lake exe cache get` found the
  9,004 Mathlib cache files already decompressed.
- The five vendor namespaces `OAI`, `PrimeNumberTheoremAnd`,
  `RellichKondrachov`, `PrimeGapsTheory`, and `PrimeGapsCert`.
  [seed_vendors.py](../util/seed_vendors.py) compares all 3,153 vendor source
  files and the toolchain, Lake configuration, and manifest byte-for-byte
  against the fresh extraction; checks the cache's actual dependency
  checkouts against the manifest pins; and checks the settings for all
  3,144 vendor modules. Each setup names package `Erdos420`, has
  `autoImplicit: false`, and lists no plugins. Reuse is restricted to
  artifacts of vendor modules whose sources are retained in the archive.

These checks establish source, version, and configuration agreement; they do
not independently certify that the cached vendor objects were compiled from
those sources. No vendor module was independently recompiled in this run.
The mathematical warrant comes from replaying every declaration in each target's
proof dependency closure into an empty kernel environment, including the cached
vendor and Mathlib declarations. The challenge uses only Mathlib imports;
its statement and definitions are checked against the solution separately.

**Commands and runtime.** From the repository root, the recorded run used the
fetch and check phases of [replay.sh](../util/replay.sh):

```sh
replay_script=library/arithmetic_functions/plasma_ai_2026_divisor_counts_shifted_factorials/evidence/util/replay.sh
LEAN_NUM_THREADS=4 ERDOS420_PACKAGE_CACHE=PACKAGE_CACHE \
  ERDOS420_VENDOR_CACHE=VENDOR_TREE \
  nice -n 10 bash "$replay_script" WORKDIR fetch
LEAN_NUM_THREADS=4 nice -n 10 bash "$replay_script" WORKDIR check
```

`WORKDIR` is fresh scratch storage, `PACKAGE_CACHE` holds the clean pinned
dependency checkouts, and `VENDOR_TREE` holds the matching built external source
tree. The optional cache inputs are validated by
[seed_packages.py](../util/seed_packages.py) and
[seed_vendors.py](../util/seed_vendors.py). Omitting the cache variables gives
the default reproduction route: fetch the pinned dependencies and rebuild
all vendored sources too. That additional compilation was not completed as part
of this receipt, so its full runtime is not certified here.

The successful check phase took 34 minutes 34 seconds, including both replay
commands, and exited with status 0. It ran under [build.sb](../util/build.sb),
which denies network access and confines writes to scratch storage, temporary
folders, and Lake's and Elan's caches. On macOS Comparator used its supplied
`fake-landrun.sh` launcher, with `build.sb` providing the sandbox; Linux
landrun isolation was not tested.

**Results (2026-10-20).**

- Comparator ran before anything built `Solution`. It built `Challenge`
  (1,990 jobs) and `Solution` (7,583 jobs), exported both, compared both
  statements and their dependencies, checked the permitted axioms, and accepted
  the proof with the Lean kernel: “Your solution is okay!”
- The subsequent full default-target build passed (7,594 jobs). The only
  `sorry` warnings were the challenge's two intentional statement placeholders;
  other warnings concerned deprecations, style, and module-system conventions.
  After both builds, all 3,211 retained source files still matched the archive
  byte-for-byte.
- The shared
  [Replay.lean](../../../../number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/Replay.lean)
  imported `Solution` with 613,818 declarations and replayed each target's
  complete proof dependency closure into an empty environment:

  | Target | Constants replayed | Kernel replay time | Statement dependencies |
  | --- | --- | --- | --- |
  | `Erdos420.erdos_420.parts.iii` | 131,311 | 298.854 s | 2,062; all identical |
  | `Erdos420.erdos_420.parts.ii` | 131,312 | 274.118 s | 2,058; all identical |

  Both outputs report `RESULT: PASS`. Each target's type is identical to its
  challenge type; each statement comparison has no mismatches. Both
  unsafe-or-partial lists are empty. The axiom list in each full closure is
  exactly `propext`, `Classical.choice`, and `Quot.sound`. These lists were
  inspected explicitly, rather than inferred from the replay program's exit
  status. Separate `#print axioms` commands confirmed the same three axioms
  for each target.

**Scope.** This is independent executable reproduction of an external formal
proof. It does not assess whether the formal statements express the intended
mathematical problem, grade a statement review, or award a native claim tier.
Those are separate assessments. No source edits or toolchain port were needed.
