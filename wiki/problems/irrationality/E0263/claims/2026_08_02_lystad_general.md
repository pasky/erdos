---
name: problems/irrationality/E0263/claims/2026_08_02_lystad_general
title: Lystad's Lean proof of the folklore root criterion without monotonicity
desc: |
  Does not address the Statement (whether $a_n=2^{2^n}$ is an irrationality
  sequence, and whether every such sequence has $a_n^{1/n}\to\infty$), so it
  does not count toward the problem's standing. Tinius Alexander Lystad's Lean
  development, generated with Kimi K3, proves that every sequence with
  $a_n^{1/2^n}\to\infty$ has irrational reciprocal sum.
authors:
- Tinius Alexander Lystad
status: rejected
claim: proved
scope: full
submitted: 2026-08-02
links:
- url: https://www.erdosproblems.com/forum/thread/263/proof-claims#proof-claim-181
  kind: discussion
  date: 2026-08-02
- url: https://github.com/arex1337/erdos-263-lean
  kind: formalization
  date: 2026-08-02
- url: https://doi.org/10.5281/zenodo.21760479
  kind: formalization
  date: 2026-08-02
created: 2026-10-14T01:10:33Z
updated: 2026-10-14T01:10:33Z
---

***

**Claim.** Tinius Alexander Lystad's proof claim of 2 August 2026 on the
proof-claims tab of [[problems/irrationality/E0263/_index|Problem 263]] gives
a Lean 4 and Mathlib proof of the folklore root criterion without
monotonicity: every sequence of positive integers with
$a_n^{1/2^n}\to\infty$ has $\sum1/a_n$ irrational. The proof sorts the
sequence, which keeps the sum and, by a counting lemma, the root condition,
and then applies his monotone theorem
([[problems/irrationality/E0263/claims/2026_08_02_lystad_monotone|its page]]).
The development, generated with Kimi K3 under Lystad's direction, is in the
repository linked above and archived on Zenodo; the write-up
`PROOF-1975.md` covers only the monotone step, and the entry notes that the
$\limsup$ analogue fails without monotonicity.

**Submission note.** Posted to erdosproblems.com as a proof claim by Tinius
Alexander Lystad (account alexander_lystad) on 2 August 2026, giving "Kimi K3"
as the AI used:

> A Lean 4 + Mathlib proof, zero 'sorry', of the folklore growth criterion
> stated on this page: every sequence of positive integers $a_n$ with
> $a_n^{1/2^n} \to \infty$ — no monotonicity assumption — has $\sum 1/a_n$
> irrational. Idea: sort the sequence into non-decreasing order (the sum is
> unchanged); the root condition survives the rearrangement by a counting lemma
> (at most $m-1$ indices can host terms $\le B^{2^m}$ once
> $a_i^{1/2^i} > 2B$ for $i \ge N$); then our previously posted
> monotone-sequence theorem applies. We are aware of no prior proof of the
> no-monotonicity form; published proofs (Erdős 1975, Hančl 1993) assume
> increasing. Q1 remains open. Notes: Verification: 'lake exe cache get && lake
> build' in the linked repository completes (8666 jobs) with zero 'sorry'
> outside the declared open Q1 obligation; axioms '[propext, Classical.choice,
> Quot.sound]' only, checkable with '#print axioms
> erdos_263_one_sided_folklore_proof'. Sharpness: the limsup analogue is false
> — an interleaved-Sylvester construction has $\limsup a_n^{1/2^n} = \infty$
> but rational sum $3/2$ (exact-arithmetic certificate
> 'code/limsup_counterexample.py' in the ai-math repo), so the $\lim$
> hypothesis is load-bearing; the criterion itself appears verbatim ("not hard
> to show") in Erdős–Graham 1980, p. 63. The limsup counterexample carries an
> exact-arithmetic certificate ('code/limsup_counterexample.py' in the ai-math
> repo; construction and verification also sketched in PROOF-1975.md's repo).
> Archived release: v2.0, DOI: https://doi.org/10.5281/zenodo.21760479 Produced
> with AI assistance (Kimi K3) under a machine-verification gate

**Why it is rejected.** It does not address the Statement.
[[problems/irrationality/E0263/_index|Problem 263]] asks whether
$a_n=2^{2^n}$ is an irrationality sequence and whether every irrationality
sequence has $a_n^{1/n}\to\infty$. The claim addresses instead the folklore
root criterion without monotonicity: a sufficient condition for irrationality
that $2^{2^n}$ does not meet, since $a_n^{1/2^n}=2$, and that says nothing about
whether growth is necessary. It decides neither question, so its mathematics
does not settle this problem. The value `proved` is its answer to that
criterion.

**Standing.** Rejected, as not addressing the Statement. The entry carries no
comments and no review; this corpus has neither read the repository nor built
the development, so it gives formalization links and no `formalized`
evidence.

**Depends on.** No page of this wiki.
