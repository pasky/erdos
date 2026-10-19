---
name: problems/integer_sequences/E0423
title: Problem 423
desc: |
  Asks for the asymptotic behaviour of the sequence with $a_1=1$, $a_2=2$ in
  which each later term is the least integer above the previous one that is a
  sum of at least two consecutive earlier terms.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 423

[[problems/integer_sequences/_index|..]]

[[problems/integer_sequences/E0423/claims/_index|claims/]]: The 2 claim pages of Problem 423, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $a_1=1$ and $a_2=2$ and for $k\geq 3$ choose $a_k$ to be the
least integer $>a_{k-1}$ which is the sum of at least two consecutive terms of
the sequence. What is the asymptotic behaviour of this sequence?

**Status.** Open. Bloom's catalog labeled the problem OPEN (page last edited 23
March 2026). It credits Bolan and Tang [Ta26], independently, with the sequence
omitting infinitely many integers. It credits Tang with the bounds
$n+\Omega(\log\log n)\le a_n\ll n^{688/413+o(1)}$. The exponent $688/413$ is
Sothanaphan's observation recorded in the paper, not one of its theorems. The
omission result and Tang's bounds with upper exponent $4175/2506$ are pending
partial claims on
[[problems/integer_sequences/E0423/claims/2026_01_15_tang|Tang's page]] and
[[problems/integer_sequences/E0423/claims/2026_01_15_bolan|Bolan's page]]. The
standing in the frontmatter derives from the claim pages.

**Source.** [erdosproblems.com/423](https://www.erdosproblems.com/423), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #423,
https://www.erdosproblems.com/423.

**References.**

- [Cu25] A. Cushman, A Note on the Sum-Product Problem and the Convex Sumset
  Problem. arXiv:2512.13849 (2025).
- [Er77c] Erdős, Paul, Problems and results on combinatorial number theory. III.
  Number theory day (Proc. Conf., Rockefeller Univ., New York, 1976) (1977),
  43-72.
- [Ta26] Q. Tang, The Hofstadter consecutive-sum sequence omits infinitely many
  positive integers. arXiv:2603.09939 (2026).

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/6fbb54f24ccc2e64dcfaffc28c58950e377110d2/FormalConjectures/ErdosProblems/423.lean),
linked at its commit of 18 September 2026, with `sorry`; the file marks the
main statement research open and five variants research solved, as the
Current assessment records.

## Current assessment

The question, as erdosproblems.com states it (page last edited 23 March 2026):
what is the asymptotic behavior of the sequence $1,2,3,5,6,8,10,11,\ldots$ (OEIS
A005243) in which each term is the least integer above the last that is a
sum of at least two consecutive earlier terms? It is open. The known bounds
are

$$
n+\Omega(\log\log n)\le a_n\ll n^{688/413+o(1)},
$$

from Tang's arXiv paper [Ta26]: its Theorem 1.4 is the lower bound, its
Theorem 1.5 gives $a_n\ll n^{4175/2506+o(1)}$ from Bloom's lower bound for
difference sets of convex sets, and its Section 6.2 records Sothanaphan's
observation that Cushman's sharper convex-set bound [Cu25] improves the
exponent to $688/413<1.6659$ by the same argument. The qualitative statement
that $a_n-n$ is nondecreasing and unbounded, so that the sequence omits
infinitely many positive integers, was proved independently by Tang (note of
15 January 2026, Theorem 1.3 of the paper) and by Bolan (note of 15 January
2026, with the explicit form that every interval $[N,2^{3N+2}]$ misses some
integer); the two claim pages record the results. The conjecture of Erdős and
Hegyvári that convex sets satisfy $|A-A|\ge|A|^{2-o(1)}$ would give
$a_n\le n^{1+o(1)}$, and erdosproblems.com and Tang's paper expect $a_n=n+o(n)$;
neither is proved. None of the results is refereed, and the erdosproblems.com
label was OPEN, so both claims are pending. The formal-conjectures statement
file (linked at its commit in the Formalization line) marks the main statement
$a_n=n+o(n)$ research open and five variants research solved: the
nondecreasing, unbounded and infinite-complement variants credit Bolan and
Tang, and the upper-bound and lower-bound variants credit Tang; all have
`sorry` bodies, and the community database lists the problem as open with
its statement formalized and no formal proof. The thread's other posts
(numerical plots of $a_n-n$ up to $n=30000$, suggesting growth like
$n^\alpha$ with $1/5<\alpha<1/2$, and discussion of the AI systems used) are
comments without a manuscript and have no pages.

## Research

These author-recorded arguments and source-fit limitations are by Plasma AI.
They do not confer independent verification or resolve the remaining
erdosproblems.com question.

The sequence starts with 1,2 and chooses the least larger integer expressible as
a sum of at least two consecutive earlier terms. Its prefix sums are strictly
convex.

Tang's held transcription, §5.1 and the proofs of Lemmas 5.1–5.3 in
§5.2, were read for the transfer from convex difference sets to
$a_n=(1+o(1))n$. A represented integer cannot acquire its representation
only after it has been passed: all its positive summands are smaller
than it. This underlies the source's greedy correspondence.
For the first $m+1$ prefix sums with difference set $D_m$,
the source counts positive represented sums of length at least two by
$$
 |R_m|\ge(|D_m|-1)/2-m.
$$
The subtraction of the singleton terms is necessary.

The held Theorem 1.5 account transfers a difference exponent $|D_m|\gg
m^\delta$, $\delta>1$, into an earlier-index recursion and an exponent
$1/(\delta-1)$ for $a_n$. The full iteration was not audited. Even a
near-quadratic count $\delta=2-o(1)$ yields only $a_n=n^{1+o(1)}$, weaker than
$a_n=(1+o(1))n$: $n\log n$ illustrates the distinction.

The unresolved obligation is to convert many represented differences into
near-complete coverage of an interval, rather than a power-law count. A useful
test is to test whether a proposed strengthening controls the missing proportion
below x, not merely the logarithmic growth exponent. Stop at n^(1+o(1))
presented as n+o(n), or a convex-set theorem with an unproved exponent.

Source interfaces:
[[../library/integer_sequences/tang_2026_hofstadter_consecutive_sum_sequence_omits_infinitely/_index|Section
5.1 and Lemmas 5.1-5.3 in Section 5.2]];
[[../library/integer_sequences/tang_2026_hofstadter_consecutive_sum_sequence_omits_infinitely/theorem_1_5|Theorem
1.5, proof pointer, Section 6.2 and exponent transfer]];
[[../library/integer_sequences/tang_2026_hofstadter_consecutive_sum_sequence_omits_infinitely/lemma_2_1|Lemma
2.1: powers of two versus consecutive integers]].

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/integer_sequences/tang_2026_hofstadter_consecutive_sum_sequence_omits_infinitely/_index|tang_2026_hofstadter_consecutive_sum_sequence_omits_infinitely]]
- [[../library/integer_sequences/tang_2026_hofstadter_consecutive_sum_sequence_omits_infinitely/lemma_2_1|tang_2026_hofstadter_consecutive_sum_sequence_omits_infinitely / lemma_2_1]]
- [[../library/integer_sequences/tang_2026_hofstadter_consecutive_sum_sequence_omits_infinitely/theorem_1_3|tang_2026_hofstadter_consecutive_sum_sequence_omits_infinitely / theorem_1_3]]
- [[../library/integer_sequences/tang_2026_hofstadter_consecutive_sum_sequence_omits_infinitely/theorem_1_4|tang_2026_hofstadter_consecutive_sum_sequence_omits_infinitely / theorem_1_4]]
- [[../library/integer_sequences/tang_2026_hofstadter_consecutive_sum_sequence_omits_infinitely/theorem_1_5|tang_2026_hofstadter_consecutive_sum_sequence_omits_infinitely / theorem_1_5]]

<!-- END problem library links -->
