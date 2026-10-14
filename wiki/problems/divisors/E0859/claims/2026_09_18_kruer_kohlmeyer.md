---
name: problems/divisors/E0859/claims/2026_09_18_kruer_kohlmeyer
title: Kruer and Kohlmeyer's Lean disproof of the density asymptotic
desc: |
  Kruer and Kohlmeyer give a kernel-checked Lean proof, certified by the bounty
  site Conjectures.io, that the density of integers whose distinct divisors can
  sum to $t$ exists for every $t$ but is asymptotic to no constant times a power
  of $\log t$.
authors:
- Liam Kruer
- Jensen Kohlmeyer
status: accepted
claim: disproved
scope: full
evidence:
- formalized
submitted: null
links:
- url: https://conjectures.io/results/e060355f-a728-4b06-af11-6302b5780d19
  kind: record
  date: 2026-09-18
- url: https://conjectures.io/results/e060355f-a728-4b06-af11-6302b5780d19/solution
  kind: formalization
  date: 2026-09-18
- url: https://conjectures.io/results/e060355f-a728-4b06-af11-6302b5780d19/solution/download
  kind: formalization
  date: 2026-09-18
- url: https://conjectures.io/papers/erdos859.pdf
  kind: preprint
  date: 2026-09-21
- url: https://www.erdosproblems.com/forum/thread/859/proof-claims#proof-claim-359
  kind: discussion
  date: 2026-09-27
created: 2026-10-07T06:53:16Z
updated: 2026-10-08T03:53:58Z
---

***

**Claim.** For $t\ge1$ let $d_t$ be the natural density of the integers $n$ for
which $t$ is a sum of distinct divisors of $n$. The answer to the question is
no: $d_t$ exists and is positive for every $t$, and there are no constants
$c_1,c_2>0$ with $d_t\sim c_1/(\log t)^{c_2}$. The proof gives two estimates
that no such asymptotic can satisfy at once. With
$\delta=1-(1+\log\log2)/\log2=0.0860\ldots$, the exponent in Ford's theorem on
integers with a divisor in a dyadic interval, the lower limit of
$-\log d_t/\log\log t$ equals $\delta$ exactly, while
$(\log t)^{\delta}d_t\to0$. The first forces the exponent $c_2$ of any
asymptotic to be $\delta$, and the second forces its constant $c_1$ to be $0$.
The upper estimate follows Erdős's 1970 split of the integers counted by $d_t$
into those with a divisor in a short interval below $t$ and a remainder of
density $O(1/\log t)$, an exact product-measure law for the capped valuations at
the primes up to $t$, and a Ford-type bound with a $(\log\log t)^{-5/4}$ saving
that pays for a dyadic union; the lower estimate builds practical seeds and a
tilted prime-pattern law, bounds a harmonic average of the densities from below
through Hölder's inequality, and passes to a single $t$ because a weighted
average has a term at least as large. The density exists because membership of
$n>0$ depends only on $n$ modulo $t!$, so $d_t$ is the average of the indicator
over one period.

**The formal statement.** The Lean file proves the negation of the
formal-conjectures statement `Erdos859.erdos_859`
([`FormalConjectures/ErdosProblems/859.lean`](https://github.com/google-deepmind/formal-conjectures/blob/6fbb54f24ccc2e64dcfaffc28c58950e377110d2/FormalConjectures/ErdosProblems/859.lean)
at the formal-conjectures commit of 18 September 2026; the record pins a catalog
commit that the public repository does not contain, and the statement it
displays is the one in this file):

```lean
∃ c₁ > 0, ∃ c₂ > 0, ∃ d, (∀ t > 0, (Erdos859.DivisorSumSet t).HasDensity (d t)) ∧
  Asymptotics.IsEquivalent Filter.atTop (fun t => d t) fun t => c₁ / Real.log ↑t ^ c₂
```

Here `DivisorSumSet t` is the set of $n$ with a subset of the positive divisors
of $n$ summing to $t$, `HasDensity` is the natural density (the limit of the
proportion of members below $N$), the existential over `d` with the density
conjunct packages "let $d_t$ be the density" (the natural density is unique when
it exists), and `Real.log ↑t ^ c₂` is $(\log t)^{c_2}$ with a real exponent, so
the formal statement is the site's wording clause for clause and its negation is
the disproof. The file proves the density conjunct rather than exploiting it,
identifies any `d` satisfying it with the density by uniqueness of limits, and
reaches the contradiction through an elementary lemma excluding
$d\sim c/(\log t)^{p}$ for every $c>0$ and real $p$. The record's solution page
(second link) holds the file, as of 2026-09-22, as its single source block:
36,197 lines and 1,721,167 bytes, with no import statement, inlining a
Mertens-type prime reciprocal estimate adapted from the Apache-2.0 Lean project
PrimeNumberTheoremAnd, whose license it reproduces. This corpus rebuilt and
replayed it, as **Acceptance.** records.

**Authorship and tools.** The record credits the submitter's handle, JenW1N.
The exposition published by Conjectures.io (third link) names the authors as
Liam Kruer and Jensen Kohlmeyer, follows their manuscript "Divisor sums and a
counterexample to Erdős problem 859" (dated 18 September 2026, 27 pages, not
public), and says it was prepared with Codex assistance from that manuscript
and the accepted Lean submission; the Lean file's header names no author and
declares no AI system, and the site's forum entry gives the system as
unknown, so which AI system, if any, generated the proof is not disclosed.

**Acceptance.** Formalized. This corpus's verification rebuilt the record's
solution file on the repository's pinned toolchain, `leanprover/lean4:v4.34.1`
with Mathlib at the revision `lean/lake-manifest.json` pins, after proof-only
changes for lemmas that Mathlib renamed or removed since the site's toolchain;
the target's statement is unchanged. The kernel replayed, from an empty
environment, every declaration the target `Bounty.target` depends on, Lean core,
Mathlib and formal-conjectures included, and accepted them all. The target's
axioms are exactly `propext`, `Classical.choice` and `Quot.sound`. Its type, and
every definition its statement reaches, are identical to the formal-conjectures
statement of the site's task, at the formal-conjectures commit the task pins,
which the site builds from a public catalog commit and an audit patch and the
replay reproduced exactly. **The formal statement.** above reads that statement
as the site's wording clause by clause; the replayed closure contains both
estimates and the proof that every density $d_t$ exists, so the negation is not
vacuous. Acceptance rests on this replay and that check.

The certification by the bounty site Conjectures.io is reported, not counted.
Its Lean kernel verified the proof on 18 September 2026 under Lean 4.33.1 with
the axioms `propext`, `Quot.sound` and `Classical.choice` permitted. Its review
approved the record on 21 September 2026 under its policy v3. The record was
certified on 23 September 2026 and shows the bounty as paid.

The review decision says the submission "refutes the proposed positive-constant
logarithmic power asymptotic for the natural density of integers whose distinct
divisors can sum to a prescribed target". It says that two agent assessments of
the Codex/GPT-6 family, using shared evidence and selected source checks,
supported approval, and that a human reviewer authorized the decision. It also
says the approval is "not an exhaustive novelty certification or fresh
independent kernel replay". Its verification report records a static scan with
"no imports, no axiom declarations, no sorry, no native_decide, no unsafe
options", together with "Statement unchanged" and "Lean kernel accepted". The
report gives a second kernel as "Not run", so "The verdict rests on a single
kernel implementation".

There is no refereed publication, and erdosproblems.com listed the problem as
open. The curator, Thomas Bloom, posted a proof-claim entry on the problem's
forum on 27 September 2026 (fourth link) to make the Conjectures.io claim known.
The entry lists the claimant as conjectures.io and gives the system as unknown.
In it the curator says they had not verified the proof or looked into it. They
say the entry is no endorsement of the Conjectures.io program, which in their
view uses the problems for its own ends without explaining its proofs or
engaging with the mathematical community. They also say the program is not
transparent about who runs the problems through an AI system, for how long, or
with which one. The entry's summary states the opposite direction (that the
constants exist). Its link points at an earlier, different Lean contribution of
1 September 2026, which proves only that each `DivisorSumSet t` has positive
density, a theorem of Erdős [Er70]. So neither the entry's summary nor its link
describes this result.

What else this corpus checked is on the problem page.
