---
name: number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/receipt_e0096_7ffd1c09
title: "Replay receipt: Conjectures.io record 7ffd1c09 (Problem 96)"
desc: |
  Kernel replay of Conjectures.io record 7ffd1c09 on Lean v4.34.1 from an
  empty environment, on 2026-10-13: passed, with the axioms propext,
  Classical.choice and Quot.sound and the task's statement unchanged.
created: 2026-10-14T02:00:00Z
updated: 2026-10-14T02:00:00Z
---

***

**Subject.** The Conjectures.io record `7ffd1c09-2912-4c4c-a7ff-a4faa263f517`
(Problem 96): its solution file
<https://conjectures.io/results/7ffd1c09-2912-4c4c-a7ff-a4faa263f517/solution/download>,
102,974 bytes, SHA-256
`d445f7ec23d57a36ea4402c11eb8cc65fd6fd18ca1d6192e17f41cc359ea308c`. The file is
not held here; the
[source record](../../conjectures_io_2026_lean_solutions_erdos_problems.md) says
why.

**Task.** `fc-8432eac9-erdos96-erdos-96-9f43077a0f-counterexample-v1`, with
target `Bounty.target : Erdos96.erdos_96` in mode `counterexample`. The bundle
is `pool/tier-1/erdos-96-counterexample` in the conjectures-tasks repository at
commit `c47124e63e99200e48ffde0c00d4754a8cc15f2a`; its files match the
manifest's hashes.

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

**Port.** None: the file built unchanged.

**Command.** [replay.sh](../util/replay.sh)
`WORKDIR 7ffd1c09-2912-4c4c-a7ff-a4faa263f517`, which builds `Challenge` and
`Solution`, runs [Replay.lean](Replay.lean) and prints the target's axioms.

**Result (2026-10-13T18:36:52Z).** The build succeeded. The kernel replayed the
41,490 declarations `Bounty.target` depends on into an empty environment and
accepted them (25.4 s). The target's type equals the challenge's, and the 2,886
declarations its statement reaches are identical in both: PASS.
`#print axioms Bounty.target`: `propext`, `Classical.choice`, `Quot.sound`. The
source-type hash that Conjectures.io's inspector computes matches the task
manifest.

**Statement check.** The target is the negation of `Erdos96.erdos_96` with
answer true. `ConvexIndep` is strict convex position and `unitDistNum` counts
unordered pairs of distinct points at distance $1$, so the negation answers the
Statement no.
