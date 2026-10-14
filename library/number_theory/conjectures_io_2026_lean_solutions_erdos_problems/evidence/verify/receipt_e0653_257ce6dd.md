---
name: number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/receipt_e0653_257ce6dd
title: "Replay receipt: Conjectures.io record 257ce6dd (Problem 653)"
desc: |
  Kernel replay of Conjectures.io record 257ce6dd on Lean v4.34.1 from an
  empty environment, on 2026-10-13: passed, with the axioms propext,
  Classical.choice and Quot.sound and the task's statement unchanged.
created: 2026-10-14T02:00:00Z
updated: 2026-10-14T02:00:00Z
---

***

**Subject.** The Conjectures.io record `257ce6dd-e3e5-4169-9d7e-2811092977ca`
(Problem 653): its solution file
<https://conjectures.io/results/257ce6dd-e3e5-4169-9d7e-2811092977ca/solution/download>,
1,352,064 bytes, SHA-256
`f3b51c0df8d3c8fb5ad2b71b01474345fc3dece2d1bd37c9d60b45acc711fde4`. The file is
not held here; the
[source record](../../conjectures_io_2026_lean_solutions_erdos_problems.md) says
why.

**Task.** `fc-8432eac9-erdos653-erdos-653-15000f4d45-formalized-v1`, with target
`Bounty.target : Erdos653.erdos_653` in mode `formalized`. The bundle is
`pool/tier-1/erdos-653-formalized` in the conjectures-tasks repository at commit
`275ef4824c41d41f97ac4e9fff95ca471de9341d`; its files match the manifest's
hashes.

**Environment.** The toolchain the repository pins in `lean/lean-toolchain`
(`leanprover/lean4:v4.34.1`), with Mathlib at the revision
`lean/lake-manifest.json` pins. formal-conjectures at the commit the task pins,
`8432eac998110a563e03df65a28c117e97c8c142`, reproduced from
`7d1a8c9912747679d0093f6d1216420c33ee5ffa` and the audit patch of
conjectures-tasks commit `7af5c26410631a213de97a3d327a5fac8ad9ca14`, then ported
to the toolchain with
[ports/fc_8432eac9.diff](../assets/ports/fc_8432eac9.diff). `TaskSupport.lean`
comes from conjectures-validator commit
`bc4e1f7d5354fbb20d09636399ac24df2b6b63d8`.

**Port.** Proof-side changes for Mathlib's API at v4.34.1, made by the diff
`solution_257ce6dd/port.diff` under `evidence/assets/` (SHA-256
`e5fca3bccd2724011c1e7da7bd92761f80237d9756a1ca572bfacf7f37aa9ad0`): eight lemma
renames, a restatement of the removed `isProbabilityMeasure_map` (Mathlib PR
#42322) and one binder type. The target's statement is unchanged, and no
`sorry` was introduced. The diff quotes the reserved solution file, so it is
held privately beside that file; a reader rebuilds the port from the held diff,
which the driver applies.

**Command.** [replay.sh](../util/replay.sh)
`WORKDIR 257ce6dd-e3e5-4169-9d7e-2811092977ca`, which builds `Challenge` and
`Solution`, runs [Replay.lean](Replay.lean) and prints the target's axioms.

**Result (2026-10-13T18:56:05Z).** The build succeeded. The kernel replayed the
81,804 declarations `Bounty.target` depends on into an empty environment and
accepted them (59.2 s). The target's type equals the challenge's, and the 2,715
declarations its statement reaches are identical in both: PASS.
`#print axioms Bounty.target`: `propext`, `Classical.choice`, `Quot.sound`. The
source-type hash that Conjectures.io's inspector computes matches the task
manifest.

**Statement check.** The target is `Erdos653.erdos_653` with answer true. The
per-point count includes the self-distance $0$, which shifts every count by one
and leaves the number of distinct values unchanged, so the target is the
Statement.
