---
name: diophantine_problems/plasma_ai_2026_powerful_sum_complements
title: Cubic and quartic powerful-sum complements
desc: |
  Plasma AI's separate Lean development for positive lower density of the
  cubic and quartic powerful-sum complements; the cubic result is due to
  Beyer de Ryke, and the quartic result is Plasma AI's; both complement
  conclusions are accepted on checked formalizations.
license: Apache-2.0
created: 2026-10-20T15:09:38Z
updated: 2026-10-28T16:23:48Z
---

# Cubic and quartic powerful-sum complements

[[diophantine_problems/_index|..]]

[[diophantine_problems/plasma_ai_2026_powerful_sum_complements/complement_density|complement_density]]: For each r in {3, 4}, the complement of sums of at most r r-powerful
numbers has positive lower natural density and is infinite, accepted
on the separate Lean formalization.

[[diophantine_problems/plasma_ai_2026_powerful_sum_complements/evidence/_index|evidence/]]: The held Lean formalization of the Problem 940 complement results, as its
repository's tree at the pinned commit, with statement-review inputs and
this corpus's verification records.

***

Plasma AI, *Erdős Problem 940: sums of r-powerful numbers*, Lean
formalization in
[plasma-ai/erdos-940](https://github.com/plasma-ai/erdos-940).
The source version inspected is commit
`491733e396424cc681ef439af0536bc08d15fde7` of that separate repository.
That tree is held in the
[[diophantine_problems/plasma_ai_2026_powerful_sum_complements/evidence/_index|evidence folder]].

The source's `formalization.yaml` names Jacob Parish as author and maintainer.
It records that GPT-6 Sol, in Codex, produced the Lean proofs of both cases
under iterative human direction, and that Claude Opus 5.5, in Claude Code,
ported them to Lean `v4.35.0-rc4`. The source declares Apache-2.0 in
`formalization.yaml` and includes the license in `LICENSE`. Its two vendored
libraries retain their own Apache-2.0 licenses and provenance READMEs: Naganori
Yamaguchi's ClassFieldTheory and Chris Birkbeck's AINTLIB Chebotarev
development. These notices were read on 2026-10-20; this card records their
terms without changing their attribution.

## Results and scope

Let $S_r$ be the natural numbers expressible as a sum of at most $r$
$r$-powerful natural numbers, where $n$ is $r$-powerful if every prime
divisor $p$ satisfies $p^r\mid n$. The source includes $0$ and $1$ among the
$r$-powerful numbers. Including zero does not change representability with
at most $r$ positive summands, since zero summands can be removed.

For each $r\in\{3,4\}$, the formalization states

$$
\exists C\in\mathbb N_{>0}\quad\forall N\text{ sufficiently large},\qquad
N\le C\,\#\{n<N:n\notin S_r\}.
$$

Thus the complement has positive lower natural density and is infinite.
`Solution.lean` supplies `Erdos940.cubic_complement_density` and
`Erdos940.quartic_complement_density`, together with their infinitude
corollaries `Erdos940.cubic_large_integers` and
`Erdos940.quartic_large_integers`. `Challenge.lean` states those four targets
using Mathlib alone, with deliberate proof holes; `comparator.json` selects
them for comparison against the proofs in `Solution.lean`.

The cubic result belongs to
[[diophantine_problems/beyer_de_ryke_2026_density_deficit_cube_full_sums/_index|Beyer de Ryke's manuscript]].
The formalization's public targets cover its positive-density-complement
conclusion, not the manuscript's stronger assertion about arbitrarily small
relative densities on suitable progressions. The quartic result is Plasma
AI's extension, with an
[[../wiki/research/erdos_940/quartic_complement|author-recorded prose argument]].
Neither exponent's complement bound proves that $S_r$ has density zero, and
the four targets say nothing about $r\ge5$.

## Method and formal evidence

Both cases decompose a powerful number into an $r$th power times a canonical
part and use summable weights to reduce the argument to finitely many parts.
The cubic proof follows Beyer de Ryke's local-density and Chebotarev argument.
The quartic proof uses the progression $8\pmod {16}$, Hilbert reciprocity to
exclude principal-character coefficient tuples, and a coefficient-uniform
Euler-product estimate to control the remaining tuples and their tail.

The separate project pins Lean and Mathlib to `v4.35.0-rc4`, with dependency
revisions in `lake-manifest.json`. Its documented build is
`lake exe cache get` followed by `lake build`; `lake build Solution Challenge`
builds the proof and comparison targets. The four intentional holes in
`Challenge.lean` are statement placeholders, not proof evidence.

The source metadata reports a successful build, the three standard axioms,
and self-assessed review status; it predates this corpus's checks.
The corpus's
[[diophantine_problems/plasma_ai_2026_powerful_sum_complements/evidence/verify/replay_receipt|build and replay receipt]]
records the successful pinned build, Comparator and empty-environment kernel
replay. The
[[diophantine_problems/plasma_ai_2026_powerful_sum_complements/evidence/verify/statement_fidelity/grade|graded fresh-context statement review]]
found the mathematical targets faithful. These records support acceptance
of the cubic and quartic complement conclusions without a numerical tier.
They do not review the manuscript or retained prose proofs, or certify their
stronger arbitrary-$\varepsilon$ progression statements.

Read status: the README, `formalization.yaml`, `Challenge.lean`,
`Solution.lean`, dependency configuration, and vendored provenance notes were
read. That source inspection is separate from the independent
statement review and mechanical verification linked above.

## Bears on

- [[../wiki/problems/diophantine_problems/E0940/_index|Problem 940]]:
  positive lower density of the complement, and hence the infinitude
  conclusion, at $r=3$ and $r=4$. Attribution and acceptance are separate for
  the two cases.
