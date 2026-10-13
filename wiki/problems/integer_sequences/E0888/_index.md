---
name: problems/integer_sequences/E0888
title: Problem 888
desc: |
  Asks for the size of the largest $A\subseteq\{1,\ldots,n\}$ in which any
  $a\le b\le c\le d$ in $A$ with $abcd$ a square satisfy $ad=bc$.
tags:
- Number theory
- Squares
status: solved
claim: answered
created: 2026-09-04T09:17:27Z
updated: 2026-10-08T02:16:54Z
---

# Problem 888

[[problems/integer_sequences/_index|..]]

[[problems/integer_sequences/E0888/claims/_index|claims/]]: The 2 claim pages of Problem 888, one per claimant's result; the problem's standing derives from them.

***

**Statement.** What is the size of the largest $A\subseteq \{1,\ldots,n\}$ such
that if $a\leq b\leq c\leq d\in A$ are such that $abcd$ is a square then
$ad=bc$?

**Formulation.** The wording asks for the size $F(n)$ of the largest such set.
The site reads it as asking for the order of magnitude and marked the problem
solved on $F(n)\asymp n\log\log n/\log n$, and the formal-conjectures
statement asserts the same $\Theta$ bound; this page takes that reading.

**Status.** SOLVED (LEAN): the site labeled the problem SOLVED (LEAN). The
"(Lean)" suffix refers to a Lean proof registered by the formal-conjectures
catalog, which was not built here. The order is $n\log\log n/\log n$. Erdős
credits Sárközy with the bound $o(n)$, and a proof was posted in the thread on
22 January 2026. The primes give $\gg n/\log n$. The primes together with the
squarefree semiprimes give $(1+o(1))\,n\log\log n/\log n$ (posted in the thread
in August 2025). The matching upper bound $\ll n\log\log n/\log n$ is the result
of a manuscript of 25 April 2026 credited to GPT-5.5 Pro prompted by Chojecki.
The site's curator, Thomas Bloom, accepted it
([[problems/integer_sequences/E0888/claims/2026_04_25_chojecki|claim page]]). A
research note released on 16 September 2026, its proof credited to GPT-6 Astra,
sharpens the order to the asymptotic $F(n)\sim n\log\log n/\log n$, with a Lean
development of its own. It is the site's one proof-claim entry and has no reply
or review
([[problems/integer_sequences/E0888/claims/2026_09_16_rogerhu|claim page]]). A
thread post of 18 January 2026 claimed the exact value
$\pi(n)+\#\{pq\le n: p<q\text{ primes}\}$, plus one for $n\le14$, with a working
document as its write-up. Replies in the same week showed that products of seven
distinct primes can be added for large $n$, and that its Lemma 2 fails. The post
is not a dated manuscript, so it gets no claim page. The site's commentary was
last edited 28 May 2026. Its thread and proof-claim form stand as described here
as of 2026-10-07.

**Source.** [erdosproblems.com/888](https://www.erdosproblems.com/888), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #888,
https://www.erdosproblems.com/888.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/888.lean).

## Progress

Not yet compiled.

## Known Results

Not yet compiled.
