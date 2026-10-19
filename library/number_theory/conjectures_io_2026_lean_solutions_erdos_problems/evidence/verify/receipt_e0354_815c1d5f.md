---
name: number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/receipt_e0354_815c1d5f
title: "Replay receipt: Conjectures.io record 815c1d5f (Problem 354, first question)"
desc: |
  Kernel replay of Conjectures.io record 815c1d5f on Lean v4.34.1 from an
  empty environment, on 2026-10-14: passed, with the axioms propext,
  Classical.choice and Quot.sound and the task's statement unchanged.
created: 2026-10-14T01:27:55Z
updated: 2026-10-18T10:20:09Z
---

***

**Subject.** The Conjectures.io record `815c1d5f-3afb-4430-8e2c-260d9038f5b0`
(Problem 354, first question): its solution file
<https://conjectures.io/results/815c1d5f-3afb-4430-8e2c-260d9038f5b0/solution/download>,
485,414 bytes, SHA-256
`7188a481c218751aa666a8577f0e6b1281462d4d3d97d548a565db99b44cc2ac`. The file is
not held here; the
[source record](../../conjectures_io_2026_lean_solutions_erdos_problems.md) says
why.

**Task.** `fc-8432eac9-parts-i-5c027f4194-formalized-v1`, with target
`Bounty.target : Erdos354.erdos_354.parts.i` in mode `formalized`. The bundle is
`pool/tier-1/erdos-354-parts-i-formalized` in the conjectures-tasks repository
at commit `275ef4824c41d41f97ac4e9fff95ca471de9341d`; its files match the
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

**Port.** Proof-side changes for Mathlib's API at v4.34.1, made by the diff
`solution_815c1d5f/port.diff` under `evidence/assets/` (SHA-256
`450149b418a7e8a2adec19bc5a902082afb3b530880473c58caa5af70cea8eac`): Mathlib's
`ProbabilityMeasure.map`, which now takes the function rather than its
measurability proof (26 call sites, internal lemma statements included), the
side goal `Measure.map_finset_sum` leaves after `rw`, and `eventuallyConst_set'`
replaced by `Filter.eventuallyEmptyOrUniv_iff'`. The target's statement is
unchanged, and no `sorry` was introduced. The diff quotes the reserved solution
file, so it is held privately beside that file; a reader rebuilds the port from
the held diff, which the driver applies.

**Command.** [replay.sh](../util/replay.sh)
`WORKDIR 815c1d5f-3afb-4430-8e2c-260d9038f5b0`, which builds `Challenge` and
`Solution`, runs [Replay.lean](Replay.lean) and prints the target's axioms.

**Result (2026-10-14T01:08:29Z).** The build succeeded. The kernel replayed the
41,792 declarations `Bounty.target` depends on into an empty environment and
accepted them (28.3 s). The target's type equals the challenge's, and the 1,292
declarations its statement reaches are identical in both: PASS.
`#print axioms Bounty.target`: `propext`, `Classical.choice`, `Quot.sound`. The
source-type hash that Conjectures.io's inspector computes matches the task
manifest.

**Statement check.** The target is `Erdos354.erdos_354.parts.i` with answer
true: for $\alpha,\beta>0$ with $\alpha/\beta$ irrational, `interleave α β 2`,
the floors of $2^k\alpha$ and $2^k\beta$, is eventually complete over finite
index sets. That is the first question, the claim's statement.
