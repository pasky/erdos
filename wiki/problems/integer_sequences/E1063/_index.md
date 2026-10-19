---
name: problems/integer_sequences/E1063
title: Problem 1063
desc: |
  Asks for an estimate of the least $n\ge2k$ such that $n-i$ divides
  $\binom{n}{k}$ for all but one $0\le i<k$.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-18T10:11:03Z
---

# Problem 1063

[[problems/integer_sequences/_index|..]]

[[problems/integer_sequences/E1063/claims/_index|claims/]]: The 5 claim pages of Problem 1063, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $k\geq 2$ and define $n_k\geq 2k$ to be the least value of
$n$ such that $n-i$ divides $\binom{n}{k}$ for all but one $0\leq i<k$. Estimate
$n_k$.

**Status.** Open. The erdosproblems.com label was OPEN (page last edited 01
February 2026).

The erdosproblems.com proof-claims tab carried two partial proof claims by Ricky
Cipollini. Both attribute the proof to the model GPT-5.6 Sol, and both point to
one write-up on a collaborative editing service. The first, submitted
2026-07-27, is an upper bound of the shape
$\log n_k\le (1+o(1))\,k\log\log k/\log k$ with explicit second-order terms. It
is recorded on
[[problems/integer_sequences/E1063/claims/2026_07_27_cipollini|its claim page]].
The second, submitted 2026-08-04, is a lower bound of the shape
$\log n_k\ge c(\log k)^2$. It is recorded on
[[problems/integer_sequences/E1063/claims/2026_08_04_cipollini|its claim page]].
Neither of Cipollini's claims settles the problem, and neither has acceptance
evidence. The erdosproblems.com label was unchanged, and these claims are
recorded without being adopted.

Two further upper bounds lie outside the tab. Patrick White's repository of 25
July 2026 gives $n_k\le\exp(Ck\log\log k/\log k)$ for large $k$,
graded sound by an independent whole-proof examination and a separate passing
grade under explicit classical interfaces; it stays claimed until Jacob Parish
at Plasma AI signs off. It is recorded on
[[problems/integer_sequences/E1063/claims/2026_07_25_white|its claim page]].
A Lean 4 proof of 1 October 2026 by the LEAP prover agent, linked by the
formal-conjectures catalog, gives the stronger bound
$n_k=O(\exp(\frac{k}{\log k}(\log\log k+\log\log\log k+\log2)))$. It is recorded
on [[problems/integer_sequences/E1063/claims/2026_10_01_leap|its claim page]].
Monier's published bound $n_k\le k!$ for $k\ge3$ (Amer. Math. Monthly 1985),
which the erdosproblems.com commentary credits, is an accepted partial claim on
[[problems/integer_sequences/E1063/claims/1985_06_01_monier|its claim page]].

**Source.** [erdosproblems.com/1063](https://www.erdosproblems.com/1063),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1063,
https://www.erdosproblems.com/1063.

**References.**

- [ErSe83] Erdos, P. and Selfridge, J. L., Problem 6447. Amer. Math. Monthly
  (1983), 710.
- [Gu04] Guy, Richard K., Unsolved problems in number theory, 3rd ed. Problem
  Books in Mathematics, Springer (2004), xviii+437 pp. B31 "Binomial
  coefficients", printed p. 130:
  "Erdős & Selfridge noted that if $n\ge2k\ge4$, then there is at least one
  value of $i$, $0\le i\le k-1$, such that $n-i$ does not divide
  $\binom nk$, and asked for the least $n_k$ for which there was only one
  such $i$", with $n_2=4$, $n_3=6$, $n_4=9$, $n_5=12$ and $n_k\le k!$ for
  $k\ge3$; no proofs. Library home:
  [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]].
- [Mo85] Monier, Jean-Marie, Problems and Solutions: Solutions of Advanced
  Problems: 6447. Amer. Math. Monthly (1985), 435-436.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/6fbb54f24ccc2e64dcfaffc28c58950e377110d2/FormalConjectures/ErdosProblems/1063.lean).
The file states the question as the search for an upper bound on $n_k$ that is
$o(k[1,\ldots,k-1])$. It also states the Erdős–Selfridge exception, the four
small values, the bounds of Monier and Cambie, and $n_k\le e^{(1+o(1))k}$. Only
the small values carry a formal proof there; it is a statement file, not a
formalization of any solution. On 7 October 2026 the formal-conjectures catalog
added the variant `erdos_1063.variants.subexponential_upper_bound` and linked
Lean proofs of it and of the four companion statements, produced by the LEAP
prover agent and recorded on
[[problems/integer_sequences/E1063/claims/2026_10_01_leap|its claim page]].

## Current assessment

[[problems/integer_sequences/E1063/claims/2026_07_25_white|White's partial result]], claimed pending the sign-off of Jacob Parish at Plasma AI, proves the eventual upper bound $n_k\le\exp(Ck\log\log k/\log k)$,
$\log n_k=o(k)$ and $n_k=o(k\operatorname{lcm}(1,\ldots,k-1))$.
The [whole-proof examination](claims/evidence/verify/white_upper_bound/report.md)
and [separate PASS grade](claims/evidence/verify/white_upper_bound/grading.md)
preserve the least-value definition, exactly one failed divisor and every
sufficiently large integer. Their explicit classical interfaces and source
provenance limits remain on the claim page. This does not determine the
sharp growth of $n_k$, so Problem 1063 remains open.

The [[research/arithmetic_construction_interfaces/sequence_upper_bound_scope|statement comparison]]
relates these upper-bound conclusions to the formal little-o improvement
question, whose comparator uses the natural-number least common multiple.
White's pending lcm consequence supplies that improvement. The stronger
LEAP formula and Cipollini claims keep their own stated standing; this review
does not inspect their proofs or transfer acceptance to them.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]]

<!-- END problem library links -->
