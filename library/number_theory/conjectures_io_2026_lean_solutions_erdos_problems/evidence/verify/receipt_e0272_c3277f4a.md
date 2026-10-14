---
name: number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/receipt_e0272_c3277f4a
title: "Replay receipt: Conjectures.io record c3277f4a (Problem 272, the Szabó variant)"
desc: |
  Kernel replay of Conjectures.io record c3277f4a on Lean v4.34.1 from an
  empty environment, on 2026-10-14: passed, with the axioms propext,
  Classical.choice and Quot.sound and the task's statement unchanged.
created: 2026-10-14T02:00:00Z
updated: 2026-10-14T02:00:00Z
---

***

**Subject.** The Conjectures.io record `c3277f4a-d573-42a9-bfca-e45fb2cb39ff`
(Problem 272, the Szabó variant): its solution file
<https://conjectures.io/results/c3277f4a-d573-42a9-bfca-e45fb2cb39ff/solution/download>,
600,125 bytes, SHA-256
`38201774f640e9c673b5e2a7821a1f031adf5bcf59ada9316fcde1f5455ba5bb`. The file is
not held here; the
[source record](../../conjectures_io_2026_lean_solutions_erdos_problems.md) says
why.

**Task.** `fc-8432eac9-variants-szabo-strong-454001886c-formalized-v1`, with
target `Bounty.target : Erdos272.erdos_272.variants.szabo_strong` in mode
`formalized`. The bundle is
`pool/tier-1/erdos-272-variants-szabo-strong-formalized` in the
conjectures-tasks repository at commit
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
`WORKDIR c3277f4a-d573-42a9-bfca-e45fb2cb39ff`, which builds `Challenge` and
`Solution`, runs [Replay.lean](Replay.lean) and prints the target's axioms.

**Result (2026-10-14T00:49:15Z).** The build succeeded. The kernel replayed the
45,548 declarations `Bounty.target` depends on into an empty environment and
accepted them (54.3 s). The target's type equals the challenge's, and the 1,695
declarations its statement reaches are identical in both: PASS.
`#print axioms Bounty.target`: `propext`, `Classical.choice`, `Quot.sound`. The
source-type hash that Conjectures.io's inspector computes matches the task
manifest.

**Statement check.** The target is `Erdos272.erdos_272.variants.szabo_strong`:
$t(N)-N^2/2=O(N)$, with `IsArithInterSet` and `maxArithInterCard` the families
and their largest size. That is the variant the claim states.
