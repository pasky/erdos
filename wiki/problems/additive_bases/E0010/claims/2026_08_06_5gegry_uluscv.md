---
name: problems/additive_bases/E0010/claims/2026_08_06_5gegry_uluscv
title: The Grechuk variant certified at Conjectures.io
desc: |
  A Lean 4 proof that infinitely many even integers are not a prime plus at most
  three powers of $2$, the Grechuk variant. It is credited to the solver address
  5GeGrY…uLUScV and was certified and paid by the bounty site Conjectures.io on
  6 August 2026.
authors: []
status: accepted
claim: disproved
scope: partial
evidence:
- formalized
submitted: null
links:
- url: https://conjectures.io/results/244ff2d0-399d-4e37-a307-4ff6f3cb3493
  kind: record
  date: 2026-08-06
- url: https://conjectures.io/results/244ff2d0-399d-4e37-a307-4ff6f3cb3493/solution
  kind: formalization
  date: 2026-08-06
- url: https://conjectures.io/results/244ff2d0-399d-4e37-a307-4ff6f3cb3493/solution/download
  kind: formalization
  date: 2026-08-06
created: 2026-10-07T10:51:47Z
updated: 2026-10-07T22:51:53Z
---

***

**Claim.** Let $S_k$ be the set of natural numbers that are a prime plus at
most $k$ powers of $2$, with the summand $2^0=1$ and repeated powers allowed.
The even numbers outside $S_3$ form an infinite set. The theorem proved is the
formal-conjectures catalog's `Erdos10.erdos_10.variants.grechuk`,
`({n | Even n} \ Erdos10.sumPrimeAndTwoPows 3).Infinite`, the formal target the
bounty site Conjectures.io published for the parenthetical remark of the
erdosproblems.com commentary on
[[problems/additive_bases/E0010/_index|Problem 10]], credited there to Bogdan
Grechuk. What it shows about the question is that $k=3$, and so every $k\le3$,
fails, so any $k$ answering it yes is at least $4$; since the question asks
whether some $k$ exists, the result is a partial no, the answer no for every
$k\le3$, which the claim value records. It does not decide whether a larger $k$
exists.

**Covers.** The Grechuk variant only: infinitely many even integers cannot be
written as a prime plus at most three powers of $2$, in the convention of the
formal-conjectures catalog's `sumPrimeAndTwoPows` (exponent zero and repeated
exponents allowed, which only enlarges the representable set); hence the lower
bound $k\ge4$ on any $k$ answering the question. Whether any $k$ exists is
untouched.

**Argument.** Crocker's construction
([[../library/additive_bases/crocker_1971_sum_prime_two_powers_two/theorem_i|Crocker 1971, Theorem I]])
gives infinitely many odd $t\equiv15\pmod{16}$ that are not a prime plus at
most two powers of $2$; the file proves this for every exponent $a\ge0$ through
a covering system of $28$ residue classes checked by `decide` and through
Fermat-number divisibility of $2^a+2^b$, its family being
$\mathrm{CA}\,j=\mathrm{CK}\cdot\mathrm{CP}(12(j+1))$ with
$\mathrm{CP}\,n=45592577\prod_{i<n,\,i\ne10}F_i$ over the Fermat numbers $F_i$,
Crocker's choice $k=10$. For each such $t$ the even number $N=t+1$ is outside
$S_3$: a representation using the summand $1$ would, after one $1$ is removed,
put $t$ in $S_2$, and otherwise the prime is $2$ and $t-1\equiv14\pmod{16}$
would be a sum of at most three powers of $2$, forcing $2+4+8$ and $t=15$. The
file's `theorem target` closes the formal-conjectures catalog's own type
(`fcTypeOfName% "Erdos10.erdos_10.variants.grechuk"`), and its
`SumPrimeThreePows` is an `abbrev` for the formal-conjectures catalog's
`sumPrimeAndTwoPows 3`, so no definition is restated.

**Claimant and posting.** The bounty site credits the proof to the solver
address it prints as 5GeGrY…uLUScV, the only name the result carries; the file
has no header, names no author and declares no AI system, and no paper,
preprint or write-up accompanies it. The erdosproblems.com Lean kernel accepted
the proof on 6 August 2026 (05:12:22 UTC, the time its decision on the later
duplicate record gives), the earliest posting of the result, which dates this
page. A second Lean proof of the same formal statement, submitted to
Conjectures.io later the same day and described by its author as independently
developed, has its own page,
[[problems/additive_bases/E0010/claims/2026_08_06_daryxx|Daryxx 2026]];
Conjectures.io set that record aside as a duplicate of this one.

**Acceptance.** Formalized. This corpus's verification rebuilt the record's
solution file, unchanged, on the repository's pinned toolchain,
`leanprover/lean4:v4.34.1` with Mathlib at the revision
`lean/lake-manifest.json` pins. The kernel replayed, from an empty environment,
every declaration the target `Bounty.target` depends on, Lean core, Mathlib and
formal-conjectures included, and accepted them all. The target's axioms are
exactly `propext`, `Classical.choice` and `Quot.sound`. Its type, and every
definition its statement reaches, are identical to the statement of
Conjectures.io's task, `Erdos10.erdos_10.variants.grechuk`. The task pins a
catalog commit that Conjectures.io built from a public catalog commit and an
audit patch; the replay reproduced it exactly, and its `10.lean` is
byte-identical to the file at the formal-conjectures commit of Conjectures.io's
later tasks, whose port to the pinned toolchain the file was built against. In
that statement `sumPrimeAndTwoPows 3` is the set of primes plus at most three
powers of $2$, exponent zero and repeats allowed, so the target is the claim
above. Acceptance rests on this replay and that check.

The bounty site Conjectures.io documented its acceptance of the exact statement;
that certification is reported, not counted. Its Lean kernel accepted the proof
on 6 August 2026, with `propext`, `Quot.sound` and `Classical.choice` as the
only axioms. Its static scan found no imports, axiom declarations, `sorry`,
`native_decide` or unsafe options. Its report records an unchanged canonical
statement and a sandboxed build. Its review approved the record the same day.
The review found that Lean verified the exact published task, and that the proof
establishes infinitely many even natural numbers that are not a prime plus at
most three powers of two, through Crocker's covering-congruence construction.
The record was certified on 6 August 2026 and the bounty was paid.
Conjectures.io's second kernel was not run, so the kernel verdict rests on one
implementation. Conjectures.io withdrew the target the same day as solved and
not open. It noted that the informal claim already follows from Crocker's
published theorem by the parity reduction.

No `refereed` evidence exists. The erdosproblems.com page labeled the problem
OPEN, since the variant does not settle it. Since 2026-09-14 the
formal-conjectures catalog has marked the variant `research solved`, citing the
second proof's gist as its `formal_proof`.

**Depends on.**
[[../library/additive_bases/crocker_1971_sum_prime_two_powers_two/theorem_i|Crocker 1971, Theorem I]],
the result page of Crocker's refereed theorem; the claim also rests on the
Lean file the bounty site's kernel accepted.
