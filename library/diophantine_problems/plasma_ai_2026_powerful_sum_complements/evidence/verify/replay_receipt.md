---
name: diophantine_problems/plasma_ai_2026_powerful_sum_complements/evidence/verify/replay_receipt
title: "Replay receipt: Plasma AI's Problem 940 formalization"
desc: |
  Successful pinned build, Comparator, axiom checks and empty-environment
  kernel replay of the four Problem 940 targets.
created: 2026-10-20T15:29:47Z
updated: 2026-10-28T16:03:26Z
---

***

**Examination date:** 2026-10-20 UTC. **Subject:** the external
[plasma-ai/erdos-940](https://github.com/plasma-ai/erdos-940) repository at
`491733e396424cc681ef439af0536bc08d15fde7`, specifically `Solution.lean`,
`Challenge.lean`, `comparator.json`, and the complete dependency closures of
the four declarations listed below. This receipt records mechanical checks;
the separate
[[diophantine_problems/plasma_ai_2026_powerful_sum_complements/evidence/verify/statement_fidelity/grade|graded statement review]]
checks their mathematical meaning.

## Source and environment

The run was [the reproduction script](../util/replay.sh), started from a fresh
scratch folder. It extracted the held
`../assets/erdos_940_formalization.tar.gz` and compared it with a fresh
`git archive` of the pinned commit from the source repository; the two trees
matched. The tree's `lean-toolchain` specifies
`leanprover/lean4:v4.35.0-rc4`, and the running compiler reported Lean
4.35.0-rc4. Lake fetched the nine dependencies at the revisions in
`lake-manifest.json`, Mathlib at `1f414401f69059aa7eead47b53ee40bd38455eeb`,
and Mathlib's prebuilt cache supplied its compiled modules. The formalization
itself and its vendored libraries were compiled from source.

Comparator and lean4export were built from the toolchain-matching
`v4.35.0-rc4` tags, respectively at tool revisions
`ca04cfc72b550331658ec314bf47685281bfd4bf` and
`05d43a2bc773b40ecfdebb32294192a5ef756951`.
The build, comparison and replay ran on macOS under the retained
[build sandbox](../util/build.sb): network access was denied, and writes
were restricted to scratch, temporary and tool-cache locations. Comparator
used its `fake-landrun.sh` adapter inside that outer sandbox; no Linux
landrun isolation is claimed.

## Executed checks

Comparator ran against the source's `comparator.json`, selecting all four
targets and permitting only `propext`, `Classical.choice`, and `Quot.sound`.
It ran before anything else built `Solution`: it built `Challenge`, then
`Solution`, and ran its Lean default-kernel check. It exited zero and
reported `Your solution is okay!`. The four intentional proof holes in
`Challenge.lean` serve only as statement placeholders; they are not accepted
proofs.

For each target the corpus's shared
[Replay.lean](../../../../number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/Replay.lean)
was then run as follows, in the extracted tree:

```sh
lake env lean --run PATH_TO_REPLAY Solution Challenge TARGET
```

The replay imports the solution, collects the target's transitive dependency
closure, and replays it into an empty Lean environment. It separately
compares the target type and reached statement definitions with the Challenge.
All four invocations exited zero with `RESULT: PASS`:

| Declaration | Proof-closure constants | Statement-closure constants | Result |
| --- | ---: | ---: | --- |
| `Erdos940.cubic_complement_density` | 91,404 | 919 | Pass |
| `Erdos940.quartic_complement_density` | 131,445 | 919 | Pass |
| `Erdos940.cubic_large_integers` | 91,406 | 551 | Pass |
| `Erdos940.quartic_large_integers` | 131,447 | 551 | Pass |

Every closure had exactly the three permitted axioms above, no unsafe or
partial constants, and no `sorryAx`, compiler-trust axiom, or custom axiom.
Each target type matched its Challenge type, and every declaration in the
reached statement closure was identical between Challenge and Solution.
A separate `#print axioms` check of all four targets also reported precisely
`propext`, `Classical.choice`, and `Quot.sound`.

## Correspondence and acceptance scope

The five Lean files supplied for statement review were compared byte for
byte with the checked tree: `Challenge.lean`, `Solution.lean`,
`Erdos940/Powerful.lean`, `Erdos940/Statement.lean`, and
`Erdos940/FinalAssembly.lean`.
They matched exactly. `Challenge.lean` is retained under
`evidence/assets/statement_fidelity/`; the other four files are in the held
archive at the paths listed in the
[subject custody record](statement_fidelity/_index.md#subject-custody).
The mathematical Claim and Covers sections preserved
in `mathematical_subject.md` state the same results as the two claim pages;
bibliographic attribution is outside the statement-review verdict.

Together with the independent review and its separate passing grade, these
checks support external-formalization acceptance of positive lower natural
density of the complement and infinitude for exponents three and four.
They give no numerical tier, no acceptance of a prose proof or stronger
progression theorem, and no conclusion about density zero or exponents at
least five.

Rerunning [the reproduction script](../util/replay.sh) repeats the extraction
and archive comparison, the build, Comparator, the four kernel replays and the
axiom check above; it does not repeat the byte comparison with the supplied
review copies.
