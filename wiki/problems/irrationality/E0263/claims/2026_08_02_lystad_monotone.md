---
name: problems/irrationality/E0263/claims/2026_08_02_lystad_monotone
title: Lystad's Lean proof of the folklore root criterion for monotone sequences
desc: |
  Does not address the Statement (whether $a_n=2^{2^n}$ is an irrationality
  sequence, and whether every such sequence has $a_n^{1/n}\to\infty$), so it
  does not count toward the problem's standing. T. Alexander Lystad's Lean
  development, generated with Kimi K3, proves that a monotone sequence with
  $a_n^{1/2^n}\to\infty$ has irrational reciprocal sum.
authors:
- T. Alexander Lystad
status: rejected
claim: proved
scope: full
submitted: 2026-08-02
links:
- url: https://www.erdosproblems.com/forum/thread/263/proof-claims#proof-claim-179
  kind: discussion
  date: 2026-08-02
- url: https://github.com/arex1337/erdos-263-lean
  kind: formalization
  date: 2026-08-02
- url: https://doi.org/10.5281/zenodo.21752787
  kind: formalization
  date: 2026-08-02
created: 2026-10-14T01:10:33Z
updated: 2026-10-14T01:10:33Z
---

***

**Claim.** T. Alexander Lystad's proof claim of 2 August 2026 on the
proof-claims tab of [[problems/irrationality/E0263/_index|Problem 263]] gives
a Lean 4 and Mathlib proof, following Erdős's 1975 argument, that every
monotone sequence of positive integers with $a_n^{1/2^n}\to\infty$ has
$\sum1/a_n$ irrational: the monotone case of the folklore root criterion the
site's remarks state. The development, generated with Kimi K3 under Lystad's
direction, is in the repository linked above and archived on Zenodo, with the
write-up `PROOF-1975.md`; the entry reports the axioms `propext`,
`Classical.choice` and `Quot.sound` only.

**Submission note.** Posted to erdosproblems.com as a proof claim by T.
Alexander Lystad (account alexander_lystad) on 2 August 2026, giving "Kimi K3"
as the AI used:

> Lean 4 + Mathlib proof, zero sorry, of Erdős's Theorem 1 (1975) at the lim
> level for monotone sequences: for every monotone sequence of positive
> integers $a_n$ with $a_n^{1/2^n} \to \infty$, the sum $\sum 1/a_n$ is
> irrational — the monotone case of the folklore lim-criterion stated on this
> page. Main ideas, following Erdős's original argument: if
> $\sum 1/a_n = r \in \mathbb{Q}$, then
> $r.\mathrm{den} \cdot \prod_{n \le N} a_n \cdot \sum_{n>N} 1/a_n$ is a
> positive integer for all $N$; where spikes $a_{j+1} > P_j^l$ occur infinitely often
> the tail collapses directly; otherwise a dyadic-counting tail bound
> $T_k \le c \log a_{k+1}/a_{k+1}$ plus Borel escape records
> ($L_{k+1} > (1+1/k^2)\max_{j\le k} L_j$ infinitely often,
> $L_k = a_k^{1/2^k}$) drives the product×tail below $1/r.\mathrm{den}$ at a
> timed index, contradicting the cap-induced tower. The no-monotonicity form of
> the criterion and Q1 ($2^{2^n}$) remain open. Notes: Verification: lake exe
> cache get && lake build in the linked repository completes (8664 jobs) with
> zero sorry outside the declared open obligation (Q1 stated with an honest
> sorry); axioms [propext, Classical.choice, Quot.sound] only, checkable with
> #print axioms irrational_of_oneSidedGrowth_monotone. The development follows
> Erdős's original argument (J. Math. Sci. 10 (1975), 1–7, renyi.hu scan) via a
> disclosed page-image transcription of equations (10)–(25). Archived release:
> v1.1, DOI: https://doi.org/10.5281/zenodo.21752787 (v1.0:
> 10.5281/zenodo.21736956). Produced with AI assistance under a
> machine-verification gate; every artifact is third-party-checkable.

**Why it is rejected.** It does not address the Statement.
[[problems/irrationality/E0263/_index|Problem 263]] asks whether
$a_n=2^{2^n}$ is an irrationality sequence and whether every irrationality
sequence has $a_n^{1/n}\to\infty$. The claim addresses instead the folklore
root criterion, in its monotone case: a sufficient condition for irrationality
that $2^{2^n}$ does not meet, since $a_n^{1/2^n}=2$, and that says nothing about
whether growth is necessary. It decides neither question, so its mathematics
does not settle this problem. The value `proved` is its answer to that
criterion.

**Standing.** Rejected, as not addressing the Statement. The entry carries no
comments and no review; this corpus has neither read the repository nor built
the development, so it gives formalization links and no `formalized`
evidence.

**Depends on.** No page of this wiki.
