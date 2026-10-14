---
name: problems/irrationality/E0263
title: Problem 263
desc: |
  Asks whether $a_n=2^{2^n}$ makes $\sum 1/b_n$ irrational for every sequence of
  positive integers $b_n$ with $b_n/a_n\to1$, and whether every $a_n$ with this
  property must satisfy $a_n^{1/n}\to\infty$.
tags:
- Irrationality
status: open
claim: none
parts: [two_tower_sequence, growth_necessary]
created: 2026-09-04T09:17:27Z
updated: 2026-10-14T01:12:01Z
---

# Problem 263

[[problems/irrationality/_index|..]]

[[problems/irrationality/E0263/claims/_index|claims/]]: The 5 claim pages of Problem 263, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $a_n$ be an increasing sequence of positive integers such
that for every sequence of positive integers $b_n$ with $b_n/a_n\to 1$ the sum

$$
\sum\frac{1}{b_n}
$$

is irrational. Is $a_n=2^{2^n}$ such a sequence? Must such a sequence satisfy
$a_n^{1/n}\to \infty$?

**Status.** Open. Bloom's catalog labeled the problem OPEN (page last edited
2026-04-02). The problem asks two questions, which are its two parts. The first,
whether $a_n=2^{2^n}$ is such a sequence, has no claim. The second asks whether
an irrationality sequence of this kind must satisfy $a_n^{1/n}\to\infty$. It has
one pending partial claim,
[[problems/irrationality/E0263/claims/2026_05_09_price|a disproof of the growth
question posted in 2026]], which asserts a counterexample.

**Source.** [erdosproblems.com/263](https://www.erdosproblems.com/263), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #263,
https://www.erdosproblems.com/263.

**References.**

- [Ko25c] J. Koizumi, Irrationality of the reciprocal sum of doubly exponential
  sequences. arXiv:2504.05933 (2025); published as INTEGERS 26 (2026), #A28.
  This page cites the preprint's labels, as the library card does; the
  preprint's Theorem 4 is the journal's Theorem 2.
- [KoTa24] Kovač, V. and Tao, T., On several irrationality problems for Ahmes
  series. arXiv:2406.17593 (2024); Acta Math. Hungar. 175 (2025), 572–608.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/6fbb54f24ccc2e64dcfaffc28c58950e377110d2/FormalConjectures/ErdosProblems/263.lean)
(pinned at the repository's commit of 2026-09-18).

## Current assessment

erdosproblems.com records Problem 263 as OPEN (page last edited 2026-04-02). On
that date erdosproblems.com added the hypothesis that the sequence be
increasing, which Erdős's formulation carries: a DeepMind prover agent had
posted on 2026-02-27
([post](https://www.erdosproblems.com/forum/thread/263#post-4521)) a Lean
disproof of the second question for the statement without that hypothesis, the
sequence $a_n=2^{3^n}$ except $a_n=2^n$ on a sparse set of indices. That
counterexample is not increasing and refutes only the superseded statement, so
it answers a variant and settles no instance of the current problem;
[[problems/irrationality/E0263/claims/2026_02_27_deepmind|its claim page]]
records it as rejected. The erdosproblems.com remarks credit it, and
the formal-conjectures catalog preserves its formal proof at
[the commit before the correction](https://github.com/google-deepmind/formal-conjectures/blob/c8cf651906abe91051cf835d4232ad5648412113/FormalConjectures/ErdosProblems/263.lean#L298).
For the corrected statement, the one pending claim is a claimed disproof of
the second question recorded on
[[problems/irrationality/E0263/claims/2026_05_09_price|the Price claim page]],
an increasing sequence that GPT-5.5 Pro is said to have found as a
counterexample; the first question has no claim, and the formal-conjectures file
at its commit of 2026-09-18 tags both questions research open. The Progress note
below records Koizumi's theorem and Kovač and Tao's theorem and why neither
settles a question; the corpus records no check of their proofs and no
literature search beyond the cited sources and the erdosproblems.com threads.

## Progress

Koizumi's [[../library/unit_fractions/koizumi_2025_irrationality_reciprocal_sum_doubly_exponential_sequences/_index|Theorem 4]]
proves that, for all real $\alpha>1$ outside a countable set, all
positive-integer sequences asymptotic to $\alpha^{2^n}$ have irrational
reciprocal sums. This does not resolve the specified base $\alpha=2$ or the
growth question in the statement.

Kovač and Tao's Theorem 2.4 (Acta Math. Hungar. 175 (2025), 572--608;
[[../library/irrationality/kovac_2024_several_irrationality_problems_ahmes_series/_index|card]]),
which the erdosproblems.com remarks credit, proves that no strictly increasing
sequence with convergent reciprocal sum and $a_{n+1}/a_n^2\to0$ is an
irrationality sequence of this kind. It settles neither question. The sequence
$a_n=2^{2^n}$ has $a_{n+1}/a_n^2=1$, and the theorem says nothing about
sequences whose ratio $a_{n+1}/a_n^2$ does not tend to $0$, such as the claimed
counterexample. So it has no claim page.

## Known Results

The second question has a claimed negative answer. Liam Price posted in the
problem's discussion thread on 2026-05-09 that GPT-5.5 Pro disproves it, with
a write-up and a Lean file auto-formalized with Aristotle and cleaned up with
Claude Opus 4.7: a strictly increasing sequence, built from blocks of
consecutive integers, that is an irrationality sequence in the problem's sense
yet has $\liminf a_n^{1/n}=1$. Nat Sothanaphan replied the same day that a
standard check found no issues and that the Lean matched the paper; that is a
forum remark, not acceptance, and the erdosproblems.com label was OPEN. The
claim page
[[problems/irrationality/E0263/claims/2026_05_09_price|records the posting]].

Three forum proof claims by T. Alexander Lystad, posted on
[2026-08-01](https://www.erdosproblems.com/forum/thread/263/proof-claims#proof-claim-176)
and on 2026-08-02
([claim 179](https://www.erdosproblems.com/forum/thread/263/proof-claims#proof-claim-179)
and
[claim 181](https://www.erdosproblems.com/forum/thread/263/proof-claims#proof-claim-181)),
have rejected claim pages
([[problems/irrationality/E0263/claims/2026_08_01_lystad|claim 176]],
[[problems/irrationality/E0263/claims/2026_08_02_lystad_monotone|claim 179]],
[[problems/irrationality/E0263/claims/2026_08_02_lystad_general|claim 181]]),
since they do not address the Statement: they are Lean 4 developments generated
with Kimi K3 under Lystad's direction, archived on Zenodo, of the folklore
sufficient criteria for being an irrationality sequence, and they settle no
instance of either question, as the claimant states. The first claims that a strictly increasing
sequence with $c\,a_n^{2+\epsilon}\le a_{n+1}$ for all large $n$ is an
irrationality sequence in the problem's sense, the consequence of the folklore
result the erdosproblems.com remarks state; $a_n=2^{2^n}$ has $a_{n+1}=a_n^2$
and misses the hypothesis by the $\epsilon$. The other two claim that every
sequence of positive integers with $a_n^{1/2^n}\to\infty$ has irrational
reciprocal sum, first for monotone sequences after Erdős's 1975 argument and
then without monotonicity by sorting the sequence; the claimant's write-up
`PROOF-1975.md` (at its commit of 2026-08-02) covers only the monotone step, and
the claimant notes that the $\limsup$ analogue fails without monotonicity, an
interleaved Sylvester construction having $\limsup a_n^{1/2^n}=\infty$ and sum
$3/2$. The repository's adapter to the formal-conjectures catalog's variant
`folklore` was produced by Codex Proof Forge, as its README says. In the thread
Vjekoslav Kovač remarked on 2026-08-02 that Badea's criterion (the main Theorem
of the 1987 paper, Theorem A of the 1993 paper; on the cards
[[../library/irrationality/badea_1987_irrationality_certain_infinite_series/_index|badea_1987_irrationality_certain_infinite_series]]
and
[[../library/irrationality/badea_1993_theorem_irrationality_infinite_series_applications/_index|badea_1993_theorem_irrationality_infinite_series_applications]])
is a stronger classical criterion of the first kind, and on 2026-08-03 that
the Erdős paper the claimant cites already has a non-monotone form of the
second. The formal-conjectures file for the problem at its commit of 2026-09-18
states the first criterion twice, both tagged research solved: in a $\liminf$
form, citing `Folklore.lean` of the claimant's repository at an earlier commit
as its formal proof, and in the eventual form that matches the claim, citing no
proof; its variant `folklore` states the second criterion without a proof
link. The formal-conjectures catalog links proofs without refereeing them.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/irrationality/badea_1987_irrationality_certain_infinite_series/_index|badea_1987_irrationality_certain_infinite_series]]
- [[../library/irrationality/badea_1987_irrationality_certain_infinite_series/theorem|badea_1987_irrationality_certain_infinite_series / theorem]]
- [[../library/irrationality/kovac_2024_several_irrationality_problems_ahmes_series/_index|kovac_2024_several_irrationality_problems_ahmes_series]]
- [[../library/unit_fractions/koizumi_2025_irrationality_reciprocal_sum_doubly_exponential_sequences/_index|koizumi_2025_irrationality_reciprocal_sum_doubly_exponential_sequences]]
- [[../library/unit_fractions/koizumi_2025_irrationality_reciprocal_sum_doubly_exponential_sequences/remark_22|koizumi_2025_irrationality_reciprocal_sum_doubly_exponential_sequences / remark_22]]
- [[../library/unit_fractions/koizumi_2025_irrationality_reciprocal_sum_doubly_exponential_sequences/theorem_1|koizumi_2025_irrationality_reciprocal_sum_doubly_exponential_sequences / theorem_1]]
- [[../library/unit_fractions/koizumi_2025_irrationality_reciprocal_sum_doubly_exponential_sequences/theorem_4|koizumi_2025_irrationality_reciprocal_sum_doubly_exponential_sequences / theorem_4]]

<!-- END problem library links -->
