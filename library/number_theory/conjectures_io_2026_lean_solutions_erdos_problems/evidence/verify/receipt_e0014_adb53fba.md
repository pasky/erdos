---
name: number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/receipt_e0014_adb53fba
title: "Replay receipt: Conjectures.io record adb53fba (Problem 14, second question)"
desc: |
  Kernel replay of Conjectures.io record adb53fba on Lean v4.34.1 from an
  empty environment, on 2026-10-13: passed, with the axioms propext,
  Classical.choice and Quot.sound and the task's statement unchanged.
created: 2026-10-14T02:00:00Z
updated: 2026-10-14T02:00:00Z
---

***

**Subject.** The Conjectures.io record `adb53fba-0b01-4398-abab-cb9b2176eebc`
(Problem 14, second question): its solution file
<https://conjectures.io/results/adb53fba-0b01-4398-abab-cb9b2176eebc/solution/download>,
46,599 bytes, SHA-256
`188ebf8bdf3a04694155ddf3e2d87c64f53d545781cfda7b63e21d6b1434cd74`. The file is
not held here; the
[source record](../../conjectures_io_2026_lean_solutions_erdos_problems.md) says
why.

**Task.** `fc-8432eac9-parts-ii-837c84619c-counterexample-v1`, with target
`Bounty.target : Erdos14.erdos_14.parts.ii` in mode `counterexample`. The bundle
is `pool/tier-1/erdos-14-parts-ii-counterexample` in the conjectures-tasks
repository at commit `275ef4824c41d41f97ac4e9fff95ca471de9341d`; its files match
the manifest's hashes.

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
`WORKDIR adb53fba-0b01-4398-abab-cb9b2176eebc`, which builds `Challenge` and
`Solution`, runs [Replay.lean](Replay.lean) and prints the target's axioms.

**Result (2026-10-13T18:34:58Z).** The build succeeded. The kernel replayed the
14,198 declarations `Bounty.target` depends on into an empty environment and
accepted them (3.7 s). The target's type equals the challenge's, and the 1,601
declarations its statement reaches are identical in both: PASS.
`#print axioms Bounty.target`: `propext`, `Classical.choice`, `Quot.sound`. The
source-type hash that Conjectures.io's inspector computes matches the task
manifest.

**Statement check.** The target is the negation of the second question's
statement with answer true: no $A$ has $o(N^{1/2})$ exceptions in
$\{1,\ldots,N\}$, with `allUniqueSums` counting exactly one unordered pair,
equal summands allowed. It answers the second question no.
