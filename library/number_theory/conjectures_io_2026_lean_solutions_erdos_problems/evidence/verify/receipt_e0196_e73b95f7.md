---
name: number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/receipt_e0196_e73b95f7
title: "Replay receipt: Conjectures.io record e73b95f7 (Problem 196)"
desc: |
  Kernel replay of Conjectures.io record e73b95f7 on Lean v4.34.1 from an
  empty environment, on 2026-10-13: passed, with the axioms propext,
  Classical.choice and Quot.sound and the task's statement unchanged.
created: 2026-10-14T01:27:55Z
updated: 2026-10-18T10:20:09Z
---

***

**Subject.** The Conjectures.io record `e73b95f7-1d1b-42b5-a442-c07077741d73`
(Problem 196): its solution file
<https://conjectures.io/results/e73b95f7-1d1b-42b5-a442-c07077741d73/solution/download>,
26,497 bytes, SHA-256
`e65c98a926ce4eca5df30277790c8b3dbcc630074ceaa24a551464951b3d2826`. The file is
not held here; the
[source record](../../conjectures_io_2026_lean_solutions_erdos_problems.md) says
why.

**Task.** `fc-8432eac9-erdos196-erdos-196-b7454f0edd-counterexample-v1`, with
target `Bounty.target : Erdos196.erdos_196` in mode `counterexample`. The bundle
is `pool/tier-1/erdos-196-counterexample` in the conjectures-tasks repository at
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
`WORKDIR e73b95f7-1d1b-42b5-a442-c07077741d73`, which builds `Challenge` and
`Solution`, runs [Replay.lean](Replay.lean) and prints the target's axioms.

**Result (2026-10-13T18:31:38Z).** The build succeeded. The kernel replayed the
7,026 declarations `Bounty.target` depends on into an empty environment and
accepted them (1.3 s). The target's type equals the challenge's, and the 404
declarations its statement reaches are identical in both: PASS.
`#print axioms Bounty.target`: `propext`, `Classical.choice`, `Quot.sound`. The
source-type hash that Conjectures.io's inspector computes matches the task
manifest.

**Statement check.** The target is the negation of `Erdos196.erdos_196` with
answer true. `HasMonotoneAP` uses increasing index lists, and the reversed list
covers decreasing indices, so the negation answers the Statement no.
