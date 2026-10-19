---
name: problems/arithmetic_functions/E0416/claims/2026_09_14_kruer_kohlmeyer
title: Conjectures.io Lean proof of the doubling law
desc: |
  A 64,775-line Lean proof, with a write-up by Kruer and Kohlmeyer, shows that
  the count $V(x)$ of distinct totient values up to $x$ satisfies
  $V(2x)/V(x)\to2$. The bounty site Conjectures.io certified it in September
  2026, and it is accepted on the first question of Problem 416 only.
authors:
- Liam Kruer
- Jensen Kohlmeyer
status: accepted
claim: proved
scope: partial
evidence:
- formalized
published: 2026-09-14
submitted: 2026-09-27
links:
- url: https://conjectures.io/results/51923647-3c0d-418e-b330-aa595f5cad42
  kind: record
  date: 2026-09-14
- url: https://conjectures.io/results/51923647-3c0d-418e-b330-aa595f5cad42/solution
  kind: formalization
  date: 2026-09-14
- url: https://conjectures.io/results/51923647-3c0d-418e-b330-aa595f5cad42/solution/download
  kind: formalization
  date: 2026-09-14
- url: https://conjectures.io/papers/erdos416i.pdf
  kind: preprint
  date: 2026-09-18
- url: https://www.erdosproblems.com/forum/thread/416/proof-claims#proof-claim-360
  kind: discussion
  date: 2026-09-27
created: 2026-10-07T10:44:32Z
updated: 2026-10-17T21:49:34Z
---

***

**Claim.** Let $V(x)$ be the number of integers $n$ with $1\le n\le x$ such
that $\varphi(m)=n$ for some $m$. Then $V(2x)/V(x)\to2$ as real
$x\to\infty$. This is the first question of
[[problems/arithmetic_functions/E0416/_index|Problem 416]], answered yes. The
proof is a Lean file of 64,775 lines submitted to the bounty site
Conjectures.io under Conjectures.io's account JenW1N; the write-up
Conjectures.io publishes beside it is by Liam Kruer and Jensen Kohlmeyer
([[../library/arithmetic_functions/kruer_kohlmeyer_2026_doubling_law_distinct_totient_values/_index|card]],
dated 18 September 2026), and this page carries their names. The file's
target theorem closes the formal-conjectures statement
`Erdos416.erdos_416.parts.i`, whose `V` counts the same finite set as
erdosproblems.com's: values $n$ with $1\le n\le\lfloor x\rfloor$, preimages
unrestricted, $m=0$ contributing only the excluded value $0$. The method, as the
write-up describes it
([[../library/arithmetic_functions/kruer_kohlmeyer_2026_doubling_law_distinct_totient_values/theorem_1_1|Theorem 1.1 on its card]]):
a finite counting inequality separates missing values from repeated
representations; families of prime–core pairs $b(p-1)$, with cores chosen
from bounded records, cover almost every totient up to $y$ with few
collisions; uniform prime counting gives the pair counts at $y$ and $y/2$ in
ratio $2$. The file contains the analytic developments (the prime number
theorem, Mertens's estimates and a sieve), including attributed ports from
PrimeNumberTheoremAnd. The prose deduction from the write-up's Proposition
4.1 is reconstructed, author-recorded, in
[[research/erdos_416/kruer_kohlmeyer_theorem_1_1_reconstruction|the Problem 416 research folder]].

**Submission note.** Posted to erdosproblems.com as a proof claim by
conjectures.io (account TFBloom) on 27 September 2026, giving "Unknown" as the
AI used:

> This formalisation claims to prove that $V(2x)/V(x)\to 2$. Notes: This was
> posted on conjectures.io. I have not verified the proof yet, and do not claim
> that the formalisation is correct, nor have I looked into the proof at all. I
> am posting this here so that others are aware that this claim has been made,
> and we can discuss it here. This should also not be read as any kind of
> endorsement of the conjectures.io program - in my view it is using these
> problems, which it does not care about, for its own ends, without making any
> attempts to explain these proofs or engage with the mathematical community. It
> is also not transparent (e.g. of who is running these through the AI, how long
> for, and which AI).

**Covers.** The first question only: $V(2x)/V(x)\to2$, with $V$ counting
distinct totient values. The proof establishes the scale $2$; the scales $2^j$,
$j$ an integer, follow by iteration, and no other scale follows. It gives no
limit $V(cx)/V(x)\to c$ for any $c$ that is not an integer power of $2$, and no
asymptotic formula for $V(x)$; the second question is not touched.

**Depends on.** No page of this wiki: the result rests on the accepted Lean
file alone.

**Acceptance.** Formalized. This corpus's verification rebuilt the record's
solution file on the repository's pinned toolchain, `leanprover/lean4:v4.34.1`
with Mathlib at the revision `lean/lake-manifest.json` pins, after renaming the
big-operator lemmas that Mathlib moved to `₀` names since Conjectures.io's
toolchain; the target's statement is unchanged. The kernel replayed, from an
empty environment, every declaration the target `Bounty.target` depends on, Lean
core, Mathlib and formal-conjectures included, and accepted them all. The
target's axioms are exactly `propext`, `Classical.choice` and `Quot.sound`. Its
type, and every definition its statement reaches, are identical to the
formal-conjectures statement `Erdos416.erdos_416.parts.i` of Conjectures.io's
task, at the formal-conjectures commit the task pins, which Conjectures.io
builds from a public formal-conjectures commit and an audit patch and the replay
reproduced exactly. That statement is the claim above, $V(2x)/V(x)\to2$ with `V`
counting the values $1\le n\le\lfloor x\rfloor$. Acceptance rests on this replay
and that check.

The bounty site Conjectures.io certified the record; the certification is
reported, not counted. Its Lean kernel accepted the file on 14 September 2026.
Fourteen gates passed, among them "Statement unchanged" and "Only permitted
axioms" with `propext`, `Quot.sound` and `Classical.choice`. Conjectures.io's
second kernel, Nanoda, was not run. Conjectures.io's review approved the record
on 15 September 2026 under its policy v3. The approval rested on two
language-model assessments of one model family and the production kernel check.
It claimed no fresh replay, no complete axiom export and no line-by-line audit.
The record was certified and its bounty paid on 16 September 2026. This is
Conjectures.io's certification, not a referee's report.

This corpus's reading audited the target statement, as the problem page records.
The target theorem is the formal-conjectures statement `parts.i` by `exact`, and
the file's own `V` equals the formal-conjectures catalog's count by `rfl`. A
text scan of the file found no `sorry`, no axiom declaration, no `native_decide`
and no `unsafe`. The 2,776-declaration analytic body is checked by the kernel
replay, not by reading.

Not refereed: no journal or arXiv version exists. erdosproblems.com
lists the record as an unverified partial proof claim, posted by its maintainer
on 2026-09-27 with an explicit non-endorsement, and labeled the problem OPEN.
The formal-conjectures statement `parts.i` was categorized `research open` from
the file's addition in July 2025 until 11 October 2026, when the
formal-conjectures catalog marked it `research solved` with a `formal_proof`
link to the OpenAI release's theorem, not to this file ([`416.lean` at that
commit](https://github.com/google-deepmind/formal-conjectures/blob/3dfd999dfe5a3a1c739d362d3189daf9e08d9fa8/FormalConjectures/ErdosProblems/416.lean)).
A second, independent formal proof of the same limit, for every real scale
$c>0$, is the OpenAI release's
[[problems/arithmetic_functions/E0416/claims/2026_09_25_openai|accepted partial claim]].

**Replay record.**
[[../library/number_theory/conjectures_io_2026_lean_solutions_erdos_problems/evidence/verify/receipt_e0416_51923647|The receipt of the kernel replay]].
