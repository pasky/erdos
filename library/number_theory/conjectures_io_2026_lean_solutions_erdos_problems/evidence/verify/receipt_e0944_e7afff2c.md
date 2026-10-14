---
name: number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/receipt_e0944_e7afff2c
title: "Replay receipt: Conjectures.io record e7afff2c (Problem 944)"
desc: |
  Kernel replay of Conjectures.io record e7afff2c on Lean v4.34.1 from an
  empty environment, on 2026-10-13: passed, with the axioms propext,
  Classical.choice and Quot.sound and the task's statement unchanged.
created: 2026-10-14T02:00:00Z
updated: 2026-10-14T02:00:00Z
---

***

**Subject.** The Conjectures.io record `e7afff2c-bb07-4fa8-92b6-67a530aaad70`
(Problem 944): its solution file
<https://conjectures.io/results/e7afff2c-bb07-4fa8-92b6-67a530aaad70/solution/download>,
459,268 bytes, SHA-256
`8bf7cd0e83463e5f304ad848921c5078d57e8f3411050e705c69a69822abecd5`. The file is
not held here; the
[source record](../../conjectures_io_2026_lean_solutions_erdos_problems.md) says
why.

**Task.** `fc-8432eac9-erdos944-erdos-944-874ac96a8b-formalized-v1`, with target
`Bounty.target : Erdos944.erdos_944` in mode `formalized`. The bundle is
`pool/tier-1/erdos-944-formalized` in the conjectures-tasks repository at commit
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

**Port.** None: the file built unchanged.

**Command.** [replay.sh](../util/replay.sh)
`WORKDIR e7afff2c-bb07-4fa8-92b6-67a530aaad70`, which builds `Challenge` and
`Solution`, runs [Replay.lean](Replay.lean) and prints the target's axioms.

**Result (2026-10-13T18:39:14Z).** The build succeeded. The kernel replayed the
13,672 declarations `Bounty.target` depends on into an empty environment and
accepted them (10.8 s). The target's type equals the challenge's, and the 1,311
declarations its statement reaches are identical in both: PASS.
`#print axioms Bounty.target`: `propext`, `Classical.choice`, `Quot.sound`. The
source-type hash that Conjectures.io's inspector computes matches the task
manifest.

**Statement check.** The target is `Erdos944.erdos_944` with answer true.
`IsCritical` and `IsCriticalEdges` say what the Statement says. The finite-graph
reading rests on the finiteness of the proof's witnesses, which the claim page
records and this replay did not recheck.
