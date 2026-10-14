---
name: number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/receipt_e1062_8d59a0af
title: "Replay receipt: Conjectures.io record 8d59a0af (Problem 1062, second question)"
desc: |
  Kernel replay of Conjectures.io record 8d59a0af on Lean v4.34.1 from an
  empty environment, on 2026-10-13: passed, with the axioms propext,
  Classical.choice and Quot.sound and the task's statement unchanged.
created: 2026-10-14T02:00:00Z
updated: 2026-10-14T02:00:00Z
---

***

**Subject.** The Conjectures.io record `8d59a0af-6762-4606-93c9-72dd356a57bc`
(Problem 1062, second question): its solution file
<https://conjectures.io/results/8d59a0af-6762-4606-93c9-72dd356a57bc/solution/download>,
4,965,602 bytes, SHA-256
`2ebc87b06386daf9720ac037996ce87eb760dc58097cd098ec6620b1c7df92b6`. The file is
not held here; the
[source record](../../conjectures_io_2026_lean_solutions_erdos_problems.md) says
why.

**Task.** `fc-8432eac9-parts-ii-71df995464-formalized-v1`, with target
`Bounty.target : Erdos1062.erdos_1062.parts.ii` in mode `formalized`. The bundle
is `pool/tier-1/erdos-1062-parts-ii-formalized` in the conjectures-tasks
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

**Port.** Proof-side changes for Mathlib's API at v4.34.1, applied by
[ports/solution_8d59a0af.diff](../assets/ports/solution_8d59a0af.diff): 22 lemma
renames, 112 rewrites of the deleted `MvPolynomial.coeff` uses (Mathlib PR
#41427), four argument names, four uses of `mapDomain_apply_of_injective`, one
simp lemma and one `swap` with `congr 2`. The target's statement is unchanged,
and no `sorry` was introduced.

**Command.** [replay.sh](../util/replay.sh)
`WORKDIR 8d59a0af-6762-4606-93c9-72dd356a57bc`, which builds `Challenge` and
`Solution`, runs [Replay.lean](Replay.lean) and prints the target's axioms.

**Result (2026-10-13T19:41:20Z).** The build succeeded. The kernel replayed the
87,095 declarations `Bounty.target` depends on into an empty environment and
accepted them (426.7 s). The target's type equals the challenge's, and the 1,705
declarations its statement reaches are identical in both: PASS.
`#print axioms Bounty.target`: `propext`, `Classical.choice`, `Quot.sound`. The
source-type hash that Conjectures.io's inspector computes matches the task
manifest.

**Statement check.** The target is `Erdos1062.erdos_1062.parts.ii` with answer
true: $f(n)/n$ converges to an irrational limit, with `ForkFree` and
`Nat.findGreatest` defining exactly the $f$ of the Statement. It settles the
irrationality question; it answers the first question only as $f(n)=(l+o(1))n$.
