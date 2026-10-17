---
name: problems/additive_combinatorics/E0656/claims/2022_06_24_kra_moreira_richter_robertson
title: Kra, Moreira, Richter and Robertson prove the B + B + t conjecture
desc: |
  Theorem 1.2 of Kra, Moreira, Richter and Robertson (Commun. Amer. Math. Soc.
  2024) shows that every set of positive upper Banach density contains
  $\{b_1+b_2+t:b_1\ne b_2\in B\}$ for some infinite set $B$ and shift $t$.
authors:
- Bryna Kra
- Joel Moreira
- Florian K. Richter
- Donald Robertson
status: accepted
claim: proved
scope: full
evidence:
- reviewed
- refereed
published: 2022-06-24
submitted: null
links:
- url: https://doi.org/10.1090/cams/34
  kind: paper
  date: 2024-08-01
- url: https://arxiv.org/abs/2206.12377
  kind: preprint
  date: 2022-06-24
- url: https://www.erdosproblems.com/656
  kind: discussion
- url: https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos656.lean
  kind: formalization
  date: 2026-08-18
- url: https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/ErdosProblems/Erdos656.md
  kind: record
created: 2026-10-07T04:35:55Z
updated: 2026-10-08T01:29:58Z
---

***

**Claim.** The answer to
[[problems/additive_combinatorics/E0656/_index|Problem 656]] is yes: every
$A\subseteq\mathbb N$ with positive upper density contains, for some infinite
$B\subseteq A$ and integer $t$, every sum $b_1+b_2$ of distinct
$b_1,b_2\in B$ shifted by $t$. The claimed result is Theorem 1.2 of B. Kra,
J. Moreira, F. K. Richter and D. Robertson, *A proof of Erdős's $B+B+t$
conjecture*: for any $A\subset\mathbb N$ with positive upper Banach density,
(i) there are an infinite $B\subset A$ and $t\in\mathbb N$ with

$$
\{b_1+b_2:b_1,b_2\in B,\ b_1\ne b_2\}\subset A-t,
$$

and (ii) there are an infinite $B\subset\mathbb N$ and $t$ with
$B\cup\{b_1+b_2:b_1\ne b_2\in B\}\subset A-t$. Positive upper density is
positive upper Banach density along the intervals $\{1,\ldots,N\}$, so part
(i) contains the erdosproblems.com statement, which the paper states as its
Conjecture 1.1 with Erdős's formulations of 1975, 1977 and 1980 cited. The
paper notes that neither the shift nor the condition $b_1\ne b_2$ can be
dropped, and Corollary 1.3 removes the shift when $A$ consists of even
integers. The proof is ergodic-theoretic: Theorem 1.4 is an equivalent
dynamical statement about an ergodic system, a point generic along a Følner
sequence and an open set of positive measure, proved in Section 3 by the
dynamical methods the authors developed for infinite sumset patterns, and
Section 2 proves the equivalence. The earlier $B+C$ theorem of Moreira,
Richter and Robertson, the special case Erdős also conjectured, is the
subject of [[problems/additive_combinatorics/E0109/_index|Problem 109]]. The
statement is recorded on the
[[../library/additive_combinatorics/kra_2024_proof_erdos_s_conjecture/_index|source card]]
(claims checked; proof not verified).

**Depends on.** Nothing in this wiki.

**Acceptance.** Refereed publication: Communications of the American
Mathematical Society 4 (2024), 480--494, doi:10.1090/cams/34, issued 1 August
2024 (Crossref record accessed 2026-10-07). The acknowledgements thank the
anonymous referee.

Reviewed: the erdosproblems.com curator (T. F. Bloom) states that the problem
was proved by Kra, Moreira, Richter and Robertson, citing [KMRR24]
(erdosproblems.com/656, page last edited 7 April 2026, accessed 2026-10-07), and
labeled it proved.

The preprint is arXiv:2206.12377. Its v1 was posted 24 June 2022, the date of
this page. The text cited here is dated 7 November 2023, and the journal text
was not compared.

A Lean 4 development declares itself a formalization of this solution. It is
`src/latest/ErdosProblems/Erdos656.lean` of Boris Alexeev's lean-proofs
repository, first added 2026-08-18 and pinned above at its commit of 2026-09-15.
Its header names Kra, Moreira, Richter and Robertson as informal authors and
Codex and GPT-5.6 Sol as formal authors (a second header says OpenAI Codex), and
it cites this paper. Its `erdos_656` is the erdosproblems.com statement. It
takes $A\subseteq\mathbb N$ of positive upper density, defined as the limit
superior of $|A\cap[0,N)|/N$. It gives an infinite $B\subseteq A$ and an integer
$t$ with $b_1+b_2+t\in A$ for all distinct $b_1,b_2\in B$. This corpus has not
built it, so no `formalized` evidence is listed.
