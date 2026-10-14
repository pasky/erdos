---
name: number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/receipt_e1057_4b28b5fa
title: "Replay receipt: Conjectures.io record 4b28b5fa (Problem 1057)"
desc: |
  Kernel replay of Conjectures.io record 4b28b5fa on Lean v4.34.1 from an
  empty environment, on 2026-10-13: passed, with the axioms propext,
  Classical.choice and Quot.sound and the task's statement unchanged.
created: 2026-10-14T02:00:00Z
updated: 2026-10-14T02:00:00Z
---

***

**Subject.** The Conjectures.io record `4b28b5fa-7e89-47ae-8eb1-1ffd8fcbe516`
(Problem 1057): its solution file
<https://conjectures.io/results/4b28b5fa-7e89-47ae-8eb1-1ffd8fcbe516/solution/download>,
17,716,283 bytes, SHA-256
`0fdd6c710864ba7b3c9ac1aad78b1348d1c1f6db104d9ac35f6c447bff9beb98`. The file is
not held here; the
[source record](../../conjectures_io_2026_lean_solutions_erdos_problems.md) says
why.

**Task.** `fc-v2-erdos1057-erdos-1057-89043d2c6193205901d196e4-formalized`, with
target `Bounty.target : Erdos1057.erdos_1057` in mode `formalized`. The bundle
is `versions/fc-v2-erdos1057-erdos-1057-89043d2c6193205901d196e4-formalized` in
the conjectures-tasks repository at commit
`fdf8b83a74b4edf4419462dc0ff242c21eee4a05`; its files match the manifest's
hashes.

**Environment.** The toolchain the repository pins in `lean/lean-toolchain`
(`leanprover/lean4:v4.34.1`), with Mathlib at the revision
`lean/lake-manifest.json` pins. formal-conjectures at the commit the task pins,
`4b69a7dca3e731dd1f28cb523b9ebd2ea32527f4`, reproduced from
`7d1a8c9912747679d0093f6d1216420c33ee5ffa` and the audit patch of
conjectures-tasks commit `78b724408bb5d5a0600441bcc4851273447e7d3c`, then ported
to the toolchain with
[ports/fc_4b69a7dc.diff](../assets/ports/fc_4b69a7dc.diff). `TaskSupport.lean`
comes from conjectures-validator commit
`bc4e1f7d5354fbb20d09636399ac24df2b6b63d8`.

**Port.** None: the file built unchanged.

**Command.** [replay.sh](../util/replay.sh)
`WORKDIR 4b28b5fa-7e89-47ae-8eb1-1ffd8fcbe516`, which builds `Challenge` and
`Solution`, runs [Replay.lean](Replay.lean) and prints the target's axioms.

**Result (2026-10-13T20:10:19Z).** The build succeeded. The kernel replayed the
124,346 declarations `Bounty.target` depends on into an empty environment and
accepted them (180.0 s). The target's type equals the challenge's, and the 2,172
declarations its statement reaches are identical in both: PASS.
`#print axioms Bounty.target`: `propext`, `Classical.choice`, `Quot.sound`. The
source-type hash that Conjectures.io's inspector computes matches the task
manifest.

**Statement check.** The target is `Erdos1057.erdos_1057` with answer true:
$\log C(x)/\log x\to1$. The formal-conjectures `IsCarmichael` is the usual
definition, a composite $n>1$ with $n\mid b^{n-1}-1$ for every $b$ coprime to
$n$, so the target is the Statement.
