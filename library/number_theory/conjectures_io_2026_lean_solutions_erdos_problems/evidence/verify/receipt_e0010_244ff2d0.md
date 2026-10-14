---
name: number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/receipt_e0010_244ff2d0
title: "Replay receipt: Conjectures.io record 244ff2d0 (Problem 10, the Grechuk variant)"
desc: |
  Kernel replay of Conjectures.io record 244ff2d0 on Lean v4.34.1 from an
  empty environment, on 2026-10-14: passed, with the axioms propext,
  Classical.choice and Quot.sound and the task's statement unchanged.
created: 2026-10-14T02:00:00Z
updated: 2026-10-14T02:00:00Z
---

***

**Subject.** The Conjectures.io record `244ff2d0-399d-4e37-a307-4ff6f3cb3493`
(Problem 10, the Grechuk variant): its solution file
<https://conjectures.io/results/244ff2d0-399d-4e37-a307-4ff6f3cb3493/solution/download>,
36,298 bytes, SHA-256
`803c7579866cccd1b276b3b5443c49850ceb8cac02357f569f0b04699c8f5757`. The file is
not held here; the
[source record](../../conjectures_io_2026_lean_solutions_erdos_problems.md) says
why.

**Task.** `fc-379fc029-variants-grechuk-e26c885566-formalized-v1`, with target
`Bounty.target : Erdos10.erdos_10.variants.grechuk` in mode `formalized`. The
bundle is `pool/tier-2/erdos-10-variants-grechuk-formalized` in the
conjectures-tasks repository at commit
`d3801a0b5555de45169a3e7118cdf6af04aa4ed5`; its files match the manifest's
hashes.

**Environment.** The toolchain the repository pins in `lean/lean-toolchain`
(`leanprover/lean4:v4.34.1`), with Mathlib at the revision
`lean/lake-manifest.json` pins. formal-conjectures at
`8432eac998110a563e03df65a28c117e97c8c142`, reproduced from
`7d1a8c9912747679d0093f6d1216420c33ee5ffa` and the audit patch of
conjectures-tasks commit `7af5c26410631a213de97a3d327a5fac8ad9ca14` and ported
with [ports/fc_8432eac9.diff](../assets/ports/fc_8432eac9.diff). The task pins
`379fc0298dc146df549e7061c3ede0353a5bb51f`, which reproduces from
`f7349f32ba6df6e7b7baf77467a3c6c7777a634d` and the audit patch of
conjectures-tasks commit `2cd3426e862148153a0430f34f96008f3a3c1928`; its
`FormalConjectures/ErdosProblems/10.lean` is byte-identical to the one at
`8432eac9`, and the target reaches only that file's definitions and Mathlib, so
the file was built against the `8432eac9` port. `TaskSupport.lean` comes from
conjectures-validator commit `bc4e1f7d5354fbb20d09636399ac24df2b6b63d8`.

**Port.** None: the file built unchanged.

**Command.** [replay.sh](../util/replay.sh)
`WORKDIR 244ff2d0-399d-4e37-a307-4ff6f3cb3493`, which builds `Challenge` and
`Solution`, runs [Replay.lean](Replay.lean) and prints the target's axioms.

**Result (2026-10-14T00:39:50Z).** The build succeeded. The kernel replayed the
7,877 declarations `Bounty.target` depends on into an empty environment and
accepted them (4.3 s). The target's type equals the challenge's, and the 413
declarations its statement reaches are identical in both: PASS.
`#print axioms Bounty.target`: `propext`, `Classical.choice`, `Quot.sound`. The
source-type hash that Conjectures.io's inspector computes differs on v4.34.1;
the task's pin was built on Lean v4.27.0.

**Statement check.** The target is
`({n | Even n} \ Erdos10.sumPrimeAndTwoPows 3).Infinite`. `sumPrimeAndTwoPows 3`
is the set of primes plus at most three powers of $2$, exponent zero and repeats
allowed, so the target is the Grechuk variant the claim states.
