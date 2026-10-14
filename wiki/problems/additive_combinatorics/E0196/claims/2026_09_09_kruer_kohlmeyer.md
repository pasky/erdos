---
name: problems/additive_combinatorics/E0196/claims/2026_09_09_kruer_kohlmeyer
title: Kruer and Kohlmeyer's permutation without a monotone 4-term progression
desc: |
  Kruer and Kohlmeyer give a Lean-checked permutation of the natural numbers
  with no four-term arithmetic progression at increasing or decreasing indices.
  The bounty site Conjectures.io certified it in September 2026, and there is no
  refereed publication.
authors:
- Liam Kruer
- Jensen Kohlmeyer
status: accepted
claim: disproved
scope: full
evidence:
- formalized
submitted: 2026-09-14
links:
- url: https://conjectures.io/results/e73b95f7-1d1b-42b5-a442-c07077741d73
  kind: record
  date: 2026-09-14
- url: https://conjectures.io/results/e73b95f7-1d1b-42b5-a442-c07077741d73/solution
  kind: formalization
  date: 2026-09-09
- url: https://conjectures.io/results/e73b95f7-1d1b-42b5-a442-c07077741d73/solution/download
  kind: formalization
  date: 2026-09-09
- url: https://conjectures.io/papers/erdos196.pdf
  kind: preprint
  date: 2026-09-14
- url: https://www.erdosproblems.com/forum/thread/196/proof-claims#proof-claim-311
  kind: discussion
  date: 2026-09-14
- url: https://github.com/lkruer/conjectures/blob/8ede860e8fc90a300207a2c17e8aefe6167b3086/problems/erdos-196/paper/proof.pdf
  kind: preprint
  date: 2026-09-14
- url: https://github.com/lkruer/conjectures/blob/8ede860e8fc90a300207a2c17e8aefe6167b3086/problems/erdos-196/lean/Erdos196.lean
  kind: formalization
  date: 2026-09-14
- url: https://github.com/alejandrozu/erdos196-counterexample/tree/e74b85fe3a0c8066464313c8a5a63d43b6a02e21
  kind: code
  date: 2026-09-15
created: 2026-10-07T07:47:49Z
updated: 2026-10-08T03:53:16Z
---

***

**Claim.** There is a permutation of $\mathbb{N}$ with no indices $i<j<k<l$
or $i>j>k>l$ whose values form an arithmetic progression, so not every
permutation of $\mathbb{N}$ contains a monotone four-term arithmetic
progression. This answers the question as Bloom's catalog words it in the
negative; [DEGS77] had shown that a monotone three-term progression is
unavoidable and a five-term one is not, so four was the open length.

The construction builds the permutation as the union of nested finite lists.
Each stage is kept closed: whenever three values in position order form a
progression whose fourth term exists, that term already appears before the
third, which rules out a progression at any four increasing positions in either
direction. The block appended at each stage is a finite saturated set sorted by
a bit-preference order in which the middle term of a three-term progression
never lies between the outer two; injectivity and surjectivity are proved
separately. The formal statement proved is the negation of the
formal-conjectures catalog's `Erdos196.erdos_196`
(`FormalConjectures/ErdosProblems/196.lean` at the formal-conjectures commit the
bounty site pinned) with its open answer fixed to true, that is, of
`∀ f : ℕ ≃ ℕ, HasMonotoneAP f 4`; the problem page's Status records the
clause-by-clause comparison of that statement with the erdosproblems.com wording
(both directions, bijections as permutations, the shift from positive to
zero-based naturals). The pinned catalog revision is not public; Conjectures.io
builds it from a public catalog commit and an audit patch, and this corpus's
replay reproduced it exactly and found the target's type identical to its
statement. Conjectures.io's record prints the target in its unnegated template
form.

**Submission note.** Posted to erdosproblems.com as a proof claim by Liam Kruer
and Jensen Kohlmeyer (account lkruer) on 14 September 2026, giving "GPT-6 Astra"
as the AI used:

> negatively answers the problem; explicitly constructs a counterexample, a
> rearrangement of all natural numbers such that there exists no 4-term
> arithmetic progression in order, thus answering "no" to the problem statement.

**Postings.** The result is one proof published twice. The bounty site
Conjectures.io shows the solver as JenW1N and its exposition PDF names Liam
Kruer and Jensen Kohlmeyer as authors: Lean verification on 9 September 2026
(with a fresh isolated replay on 10 September), review approval on 11 September
2026 under its policy v2, certification on 14 September 2026 and the bounty
paid; its record offers the Lean file, the exposition and the verification
report. The erdosproblems.com forum carries a proof claim submitted on
2026-09-14 by Liam Kruer for Kruer and Jensen Kohlmeyer, naming GPT-6 Astra as
the AI system used, which links a manuscript dated 9 September 2026 and a Lean
file in a GitHub repository; that Lean file is byte-identical to the file the
bounty site accepted, so the two postings are one claim. The repository's notes
say that the manuscript credits substantial assistance from OpenAI Codex in the
mathematics, the formalization and the writing, and that the repository itself
has not rebuilt the proof; the Lean file's header declares no author. The
chronology as found: the bounty site's Lean verification of 9 September 2026 is
the earliest dated event; the repository was created, the forum claim submitted
and the certification published on 14 September 2026, the first public postings
found. Ho's arXiv preprint of 11 September 2026, recorded on
[[problems/additive_combinatorics/E0196/claims/2026_09_11_ho|its own claim page]],
answers the same question no by a construction of the same shape: both grow
nested finite prefixes whose completion by the binary order, in which the
middle term of a three-term progression never lies between its ends, is kept
free of four-term progressions. A third-party repository posted in the
erdosproblems.com proof-claim thread on 2026-09-15, linked above, reproduces the
construction: it compiles the authors' unchanged Lean source in a replacement
wrapper, audits its ten declarations against the standard axioms, credits the
argument to Kohlmeyer and Kruer, and disclaims priority; this corpus has not
built it, so it is not acceptance evidence.

**Acceptance.** Formalized. This corpus's verification rebuilt the record's
solution file, unchanged, on the repository's pinned toolchain,
`leanprover/lean4:v4.34.1` with Mathlib at the revision
`lean/lake-manifest.json` pins. The kernel replayed, from an empty environment,
every declaration the target `Bounty.target` depends on, Lean core, Mathlib and
formal-conjectures included, and accepted them all. The target's axioms are
exactly `propext`, `Classical.choice` and `Quot.sound`. Its type, and every
definition its statement reaches, are identical to the formal-conjectures
statement of Conjectures.io's task. In that statement `HasMonotoneAP` asks for a
progression at increasing indices, and the reversed list covers decreasing ones,
so it is the problem's Statement as the problem page's Status compares it clause
by clause. Acceptance rests on this replay and that check.

The bounty site Conjectures.io certified the result; the certification is
reported, not counted. Its decision finds that the submission refutes the exact
target for Problem 196, with both directions covered. It finds that the change
from positive integers to zero-based naturals is immaterial under translation
and that no unproved assumption remains. It also finds that the proof passed its
statement, dependency, permitted-axiom (`propext`, `Quot.sound`,
`Classical.choice`) and Lean-kernel checks, on Lean's default kernel only. The
decision records that, under the bounty site's policy, unresolved provenance
questions alone do not deny the reward. It describes the approval as a decision
on eligibility for the bounty, not a guarantee of originality.

No other body accepts the result. The erdosproblems.com curator kept the label
Open and lists the proof claim, but has not commented on it. The claim's three
forum comments are by other users. The formal-conjectures statement `erdos_196`
is tagged open on the formal-conjectures default branch (2026-10-07). So no
`refereed` evidence exists.

**Depends on.** No wiki page; the claim rests on the Lean file and its
exposition.
