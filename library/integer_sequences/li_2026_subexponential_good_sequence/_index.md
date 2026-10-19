---
name: integer_sequences/li_2026_subexponential_good_sequence
title: "Li: A Subexponential Good Sequence"
desc: |
  Peter Li's seven-page manuscript of April 2026, produced with use of
  GPT-5.5 Pro, claiming by a probabilistic proof a good sequence of primes
  with log u_n = √n + O(1/√n), so u_n ≤ e^{o(n)}, which would answer the
  second question of Problem 1101; unreviewed.
license: unstated
created: 2026-10-14T22:08:31Z
updated: 2026-10-14T22:24:01Z
---

# Li: A Subexponential Good Sequence

[[integer_sequences/_index|..]]

[[integer_sequences/li_2026_subexponential_good_sequence/lemma_1|lemma_1]]: For the manuscript's random sequence of primes and fixed C ≥ 1 and η > 0,
almost surely, for all large t, no integer 0 ≤ n < N_t has ⌈(1+η)t⌉ distinct
terms of index above K_0(C,η) dividing translates n + j with 1 ≤ j ≤ Ct;
statement checked, proof unreviewed.

[[integer_sequences/li_2026_subexponential_good_sequence/theorem_1|theorem_1]]: The manuscript's main claim: a good sequence of primes exists with
log u_n = √n + O(1/√n), so u_n = exp((1+o(1))√n) ≤ e^{o(n)}, found by
drawing each large term at random among the primes just above e^√n;
statement checked, proof unreviewed.

***

Peter Li, *A Subexponential Good Sequence*, manuscript dated April 27, 2026,
7 pp. The author line prints Peter Li alone, with no affiliation. No journal,
arXiv identifier or version number appears, and the manuscript has no
reference list. It names neither Erdős nor any problem: Section 1 (p. 1)
defines good sequences as the erdosproblems.com statement of Problem 1101
does, for integers $u_i>1$, and states the result in those terms. Below the
abstract, p. 1 prints "AI Disclosure. Produced with use of GPT-5.5 Pro."

**Edition read.** The copy read for this card is the PDF served on 2026-10-14
by the Google Drive download address
<https://drive.google.com/uc?export=download&id=1rRfKzo0JMjUYlzgJ0kGvj_HUVXiit9-M>,
seven pages with a full text layer, 290,669 bytes; two fetches that day
returned the same file. The PDF's information dictionary gives no title or
author and a creation time of 27 April 2026, 22:38 UTC. It is the Drive file
that the problem's claim page links through its share page,
<https://drive.google.com/file/d/1rRfKzo0JMjUYlzgJ0kGvj_HUVXiit9-M/view>. A
Drive file carries no version pin, and the file at that address can change;
this card describes the file as fetched on that date. No notice is printed in
the manuscript, and no terms came with the download; the term is unstated.

**Claim and method.**
[[integer_sequences/li_2026_subexponential_good_sequence/theorem_1|Theorem 1]]
(p. 1) asserts a good sequence $u_1<u_2<\cdots$ of primes with
$\log u_n=\sqrt n+O(n^{-1/2})$, so that
$u_n=\exp((1+o(1))\sqrt n)\le e^{o(n)}$. For pairwise coprime integers
$u_i>1$ with $\sum_i1/u_i<\infty$, let $D=\prod_i(1-1/u_i)$, let
$a_1<a_2<\cdots$ be the positive integers divisible by no $u_i$, and let
$t_x$ satisfy $u_1\cdots u_{t_x}\le x<u_1\cdots u_{t_x+1}$; the sequence is
good when, for every $\varepsilon>0$, every large $x$ has
$\max_{a_k<x}(a_{k+1}-a_k)<(1+\varepsilon)t_xD^{-1}$.

The abstract says the proof is probabilistic and uses only the prime number
theorem with the classical de la Vallée Poussin error term. Section 2
(pp. 2--3) fixes finitely many small primes and, for each large $n$, draws
$u_n$ uniformly and independently from the primes in
$[e^{\sqrt n},e^{\sqrt n+1/(10\sqrt n)}]$.
These intervals are disjoint for large $n$ and each holds $\gg e^{\sqrt n}/n$
primes, so every outcome has the stated growth and
$u_1\cdots u_{t+1}\le N_t=\exp(\frac23(t+1)^{3/2}+B\sqrt t)$ for a constant
$B$ and all large $t$.
[[integer_sequences/li_2026_subexponential_good_sequence/lemma_1|Lemma 1]]
(p. 3), proved by a first-moment count and the Borel--Cantelli lemma
(pp. 3--5), says that for fixed $C\ge1$ and $\eta>0$, almost surely, for all
large $t$, no integer $0\le n<N_t$ has $\lceil(1+\eta)t\rceil$ distinct terms
of index above $K_0(C,\eta)$ dividing translates $n+j$ with $1\le j\le Ct$.
One outcome is then fixed for which this holds for every integer $C\ge1$ and
rational $\eta>0$ (p. 5). Section 4 (pp. 5--7) shows, by the Chinese
remainder theorem and a count of the integers each term can divide, that
gaps $a_{k+1}-a_k\ge(1+\varepsilon)t_xD^{-1}$ with $a_k<x$ for arbitrarily
large $x$ would produce such configurations for arbitrarily large $t$, so
that outcome is good.

Read status: claims checked. Theorem 1 and the definitions it uses (p. 1),
and Lemma 1 and the construction it concerns (pp. 2--3), were read clause by
clause on the page images; the proofs (pp. 2--7) were read through for
structure only, and no step of them was checked. Nothing here is
independently reviewed, and nothing here awards proof coverage, acceptance or
a verification tier. The claim the manuscript makes on the problem is
recorded, with its standing, on
[[../wiki/problems/integer_sequences/E1101/claims/2026_04_27_li|its claim page]].

**Bears on.** [[../wiki/problems/integer_sequences/E1101/_index|#1101]]:
Theorem 1 claims a good sequence with $u_n\le e^{o(n)}$, which would answer
the problem's second question affirmatively; the claim is unreviewed. Its
sequence grows like $\exp((1+o(1))\sqrt n)$, so it does not bear on the first
question, whether some good sequence has $u_n<n^{O(1)}$.

**Results.**

- [[integer_sequences/li_2026_subexponential_good_sequence/theorem_1|Theorem 1]]
  (p. 1): a good sequence of primes with $\log u_n=\sqrt n+O(n^{-1/2})$, so
  $u_n=\exp((1+o(1))\sqrt n)\le e^{o(n)}$.
- [[integer_sequences/li_2026_subexponential_good_sequence/lemma_1|Lemma 1]]
  (p. 3): for fixed $C\ge1$ and $\eta>0$ there is $K_0(C,\eta)$ such that,
  almost surely, for all large $t$ no integer $0\le n<N_t$ has
  $\lceil(1+\eta)t\rceil$ distinct terms $u_i$, $i>K_0$, each dividing some
  $n+j$ with $1\le j\le Ct$.

No file of this source is held: no license on record permits its redistribution,
and the card cites the edition it names above.
