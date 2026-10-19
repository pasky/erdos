---
name: number_theory/sothanaphan_2026_one_separated_semigroups_prime_minimality
title: "Sothanaphan: One-separated multiplicative semigroups and prime minimality"
desc: |
  Nat Sothanaphan's note of 28 January 2026, joint with ChatGPT, proving that
  101/42, 367/103 and 113/24 generate a free multiplicative semigroup whose
  elements are at least 1 apart, so three such generators fit below the third
  prime 5; certified by Matveev's bound, LLL reduction and an exact finite
  check; unrefereed.
license: unstated
created: 2026-10-14T22:08:11Z
updated: 2026-10-14T22:24:01Z
---

# Sothanaphan: One-separated multiplicative semigroups and prime minimality

[[number_theory/_index|..]]

[[number_theory/sothanaphan_2026_one_separated_semigroups_prime_minimality/theorem_2|theorem_2]]: The reals 101/42, 367/103 and 113/24 generate a free multiplicative
semigroup whose distinct elements differ by at least 1, so m(3) <= 113/24 <
5 = p_3; proved by Matveev's bound, de Weger's LLL reduction and an exact
finite check, computer-assisted and unreviewed.

***

Nat Sothanaphan, *One-separated multiplicative semigroups and prime
minimality*, a note dated "Jan 28, 2026" on its title page, 15 pages, of which
pp. 5--15 print a verification script and a sample run. It was posted to the
erdosproblems.com thread for Problem 951 on 28 January 2026, as the
[[../wiki/problems/number_theory/E0951/claims/2026_01_28_sothanaphan|claim
page for Sothanaphan's notes]] records. It is not refereed, and the searches
recorded on the problem page found no arXiv or journal version.

**Version and provenance.** The copy read for this card was fetched on
2026-10-14 from
<https://drive.google.com/uc?export=download&id=1gykR98vV0FiWwUl_S9SLy33vb9loN8-P>,
the direct-download address of the Google Drive file
<https://drive.google.com/file/d/1gykR98vV0FiWwUl_S9SLy33vb9loN8-P/view> that
the claim page records: 313,616 bytes, 15 pages, with a creation time of
2026-01-28T16:20:31Z in its metadata. A Google Drive file has no version pin,
so the file at that address can change; the card describes the copy of that
date. No notice is printed in the note, and no terms came with the
download; the term is unstated.

**What it claims.** For reals $1<x_1<\cdots<x_n$ the note studies the
semigroup $\mathcal S(x_1,\dots,x_n)$ of products $x_1^{a_1}\cdots x_n^{a_n}$
with nonnegative integer exponents, called free when distinct exponent vectors
give distinct products and one-separated when distinct elements differ by at
least 1 (Definition 1, p. 1), and the infimum $m(n)$ of $x_n$ over $n$-tuples
whose semigroup is both (Definition 2, p. 1). The first $n$ primes give
$m(n)\le p_n$, and the note reads "prime minimality" as the conjectured
equality $m(n)=p_n$. Theorem 1 (p. 2) proves $m(2)=3$: one-separation forces
$x_1-1\ge1$ and $x_2-x_1\ge1$, and $(2,3)$ attains $x_2=3$. Theorem 2 (p. 3)
answers $n=3$ in the negative: the semigroup of $101/42$, $367/103$ and
$113/24$ is free and one-separated, so $m(3)\le113/24<5$. The triple was found
by a random search over rational triples that checked separation only up to
exponent 10 (p. 3); the proof combines exact freeness (Lemma 3, p. 4), a
reduction of a gap below 1 to an exponentially small linear form in logarithms
(Lemmas 1 and 2, pp. 2--3), Matveev's explicit lower bound, three rounds of de
Weger's LLL reduction and an exact enumeration of the products with exponents
at most 21 (Section 5.2, pp. 4--5). Section 6 (p. 5) leaves open whether
$m(n)<p_n$ for any $n\ge4$, and whether an infinite increasing sequence whose
finite prefixes all generate free one-separated semigroups can have
$x_n<p_n$ for infinitely many $n$. Section 7 (pp. 5--15) prints the Python
script `verify_n3.py`, which uses mpmath and exact fractions, and a sample run
that ends by reporting all gaps at least 1.

**AI disclosure.** The note states "This work is joint with ChatGPT." (p. 1),
with a footnote giving a shared ChatGPT conversation,
<https://chatgpt.com/share/697a36cd-2590-8010-b278-db07751f70be>; it names no
model version.

**Read status.** Claims checked. The statement of Theorem 2, with Definitions 1
and 2, Theorem 1 and Lemmas 1 to 3, was read clause by clause on the page
images of the PDF; the proofs were read only to write the summaries here and
on the result page. No proof step, bound or computation was checked, and the
script was not run. Nothing here awards verification, acceptance or a tier.

**Relation to the other two notes.** The note does not cite the note posted a
day earlier and credited to Liam Price
([[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/_index|filed
here]]), whose five generators, all below $10<11=p_5$, give $m(5)<11$, as
Sothanaphan's note dated 2 February 2026
([[number_theory/sothanaphan_2026_probabilistic_box_certification_one_separated_semigroups/_index|filed
here]]) points out; so its open case $n=5$ had a claimed answer before it
appeared.
That later note cites this one for $m(2)=3$ and $m(3)<5$, centers its own
$n=3$ box at this triple and proves $m(n)<p_n$ for $3\le n\le7$ by box
certification, its $n=3$ case by a different route. This note does not use
the extension step,
[[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/lemma_11|Lemma 11]]
of the 27 January note; the claim page applies it to this triple.

**Bears on.** [[../wiki/problems/number_theory/E0951/_index|#951]]: the note
relates only its infinite question to Problem 951 (p. 1) and states no failure
of the inequality. Extended by Lemma 11 of the 27 January note, its triple
begins an infinite sequence with the separation property and three terms at
most $x$ for $113/24\le x<5$, where $\pi(x)=2$, which answers the part
`every_x`, the reading for every $x$, in the negative there; the problem page
records this as a
[[../wiki/problems/number_theory/E0951/claims/2026_01_28_sothanaphan|pending
partial claim]]. The note's open infinite question is the same as asking for
a counterexample to the part `large_x`, the reading for all large $x$ (an
observation of this card): when $x_n<p_n$, the $n$ terms up to $x_n$ exceed
$\pi(x_n)\le n-1$, and the inequality fails at arbitrarily large $x$ exactly
when this happens for infinitely many $n$. The note leaves the question open,
so it does not bear on that part.

**Results.**

- [[number_theory/sothanaphan_2026_one_separated_semigroups_prime_minimality/theorem_2|Theorem 2]]
  (p. 3): the semigroup of $101/42$, $367/103$ and $113/24$ is free and
  one-separated, so $m(3)\le113/24<5=p_3$.

Theorem 1 (p. 2), $m(2)=3$, is elementary, and Lemmas 1 to 3 (pp. 2--4) are
steps of the proof of Theorem 2; they are recorded above and on that page and
get no pages of their own.

No file of this source is held: no license on record permits its redistribution,
and the card cites the edition it names above.
