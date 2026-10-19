---
name: number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/receipt_e0014_dce3d778
title: "Replay receipt: Conjectures.io record dce3d778 (Problem 14, first question)"
desc: |
  Kernel replay of Conjectures.io record dce3d778 on Lean v4.34.1 from an
  empty environment, on 2026-10-13: passed, with the axioms propext,
  Classical.choice and Quot.sound and the task's statement unchanged.
created: 2026-10-14T01:27:55Z
updated: 2026-10-18T10:20:09Z
---

***

**Subject.** The Conjectures.io record `dce3d778-6f52-4c27-8da0-c82d2f391b64`
(Problem 14, first question): its solution file
<https://conjectures.io/results/dce3d778-6f52-4c27-8da0-c82d2f391b64/solution/download>,
49,184 bytes, SHA-256
`496840684dd5dc4f0747bf4732ee4fe246340353f8a11aae00bde325fa100ca5`. The file is
not held here; the
[source record](../../conjectures_io_2026_lean_solutions_erdos_problems.md) says
why.

**Task.** `fc-8432eac9-parts-i-8313191e7a-formalized-v1`, with target
`Bounty.target : Erdos14.erdos_14.parts.i` in mode `formalized`. The bundle is
`pool/tier-1/erdos-14-parts-i-formalized` in the conjectures-tasks repository at
commit `275ef4824c41d41f97ac4e9fff95ca471de9341d`; its files match the
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
`WORKDIR dce3d778-6f52-4c27-8da0-c82d2f391b64`, which builds `Challenge` and
`Solution`, runs [Replay.lean](Replay.lean) and prints the target's axioms.

**Result (2026-10-13T18:33:37Z).** The build succeeded. The kernel replayed the
18,045 declarations `Bounty.target` depends on into an empty environment and
accepted them (4.7 s). The target's type equals the challenge's, and the 2,049
declarations its statement reaches are identical in both: PASS.
`#print axioms Bounty.target`: `propext`, `Classical.choice`, `Quot.sound`. The
source-type hash that Conjectures.io's inspector computes matches the task
manifest.

**Statement check.** The target is the first question with answer true.
`allUniqueSums` counts exactly one unordered pair, equal summands allowed, the
count runs over $\{1,\ldots,N\}$, and `≫` is big-O in the direction the question
asks, so the target answers the first question yes.
