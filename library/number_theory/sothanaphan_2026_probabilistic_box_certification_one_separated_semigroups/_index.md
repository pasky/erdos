---
name: number_theory/sothanaphan_2026_probabilistic_box_certification_one_separated_semigroups
title: "Sothanaphan: Probabilistic box-certification for one-separated multiplicative semigroup problem"
desc: |
  Nat Sothanaphan's note dated 2 February 2026, joint with ChatGPT, proving
  by box certificates, an interval check of the small products and a union
  bound for the rest, that for each n from 3 to 7 some n reals below the n-th
  prime generate a free semigroup with elements at least 1 apart; no
  generators are exhibited; unrefereed.
license: unstated
created: 2026-10-14T22:08:11Z
updated: 2026-10-14T22:24:01Z
---

# Sothanaphan: Probabilistic box-certification for one-separated multiplicative semigroup problem

[[number_theory/_index|..]]

[[number_theory/sothanaphan_2026_probabilistic_box_certification_one_separated_semigroups/theorem_1|theorem_1]]: For each n with 3 <= n <= 7 some reals 1 < x_1 < ... < x_n < p_n generate a
free multiplicative semigroup whose elements are at least 1 apart, located
in explicit small boxes by the note's box certificate; no generators are
exhibited and the runs are not printed; unreviewed.

[[number_theory/sothanaphan_2026_probabilistic_box_certification_one_separated_semigroups/theorem_2|theorem_2]]: If a log-box of generators passes a finite interval check on all products
below a height cutoff and a computable union bound for the higher products
is below 1, then some point of the box generates a semigroup whose
products for distinct exponent vectors are at least 1 apart.

***

Nat Sothanaphan, *Probabilistic box-certification for one-separated
multiplicative semigroup problem*, a note dated "Feb 2, 2026" on its title
page, 8 pages. The creation time in its metadata is 2026-02-01T20:38:51Z, and
the [[../wiki/problems/number_theory/E0951/claims/2026_01_28_sothanaphan|claim
page for Sothanaphan's notes]] gives 1 February 2026 as the date it was posted
to the erdosproblems.com thread for Problem 951. It is not refereed, and the
searches recorded on the problem page found no arXiv or journal version.

**Version and provenance.** The copy read for this card was fetched on
2026-10-14 from
<https://drive.google.com/uc?export=download&id=1SIATgVENtE5696MERLjesEmKgNWh5wFK>,
the direct-download address of the Google Drive file
<https://drive.google.com/file/d/1SIATgVENtE5696MERLjesEmKgNWh5wFK/view> that
the claim page records: 282,719 bytes, 8 pages. A Google Drive file has no
version pin, so the file at that address can change; the card describes the
copy of that date. No notice is printed in the note, and no terms came with
the download; the term is unstated.

**What it claims.** The note takes up the question of Sothanaphan's note of 28
January 2026 (its reference [3]): with $m(n)$ the infimum of $x_n$ over reals
$1<x_1<\cdots<x_n$ that generate a free multiplicative semigroup whose
elements differ pairwise by at least 1, is $m(n)=p_n$? Theorem 1 (p. 1)
proves $m(n)<p_n$ for each $3\le n\le7$. No generators are exhibited: for
each $n$, Section 2 (pp. 2--3) gives a center $a$ and a radius $r$, and the
note asserts generators $1<x_1<\cdots<x_n<p_n$ in the box
$|\log x_i-\log a_i|\le r$, by Theorem 2 (p. 6), which certifies that such a
box contains a tuple whose semigroup is 1-separated. The certificate splits
the pairs of products at a cutoff $T_0$ on the logarithm of the smaller one:
below it, interval arithmetic over the whole box shows every gap at least 1
(Proposition 1, p. 4); above it, a union bound shows that the points of the
box with some pair less than 1 apart have probability below 1, for the uniform
distribution of $(\log x_i)$ on the box (Proposition 2, p. 6). The note
follows a probabilistic approach that it credits to a sketch by Terence Tao in
the erdosproblems.com thread. Its $n=3$ box is centered at the triple of the
28 January note, its $n=4$ box at a candidate from Tao's comment, and its
$n=5$, $6$, $7$ boxes at arithmetic progressions with difference $1.02$
ending at $p_n-0.001$, found by search; the cutoffs are $T_0=50$ for $n\le5$,
65 for $n=6$ and 72 for $n=7$ (p. 3). The note stops at $n=7$ because
certification grows harder, expects larger $n$ to be within reach, and
conjectures $m(n)<p_n$ for every $n\ge3$ without proof (pp. 1, 3).

**Supplementary code.** The note says that it "contains substantive
supplementary code" (p. 1), located at
<https://drive.google.com/file/d/16pg7BrDIrPKzx-fEm4m7gx8dK3R_xNg6/view?usp=sharing>.
Section 4 (pp. 6--7) describes how the program `interval_certify.py`
implements the two hypotheses of Theorem 2 and lists its command-line
parameters. The note prints no output of the runs, neither the small-regime
gaps nor the tail bounds. The code was not fetched or run for this card.

**AI disclosure.** The note states "This work is joint with ChatGPT." (p. 1),
with a footnote giving a shared ChatGPT conversation,
<https://chatgpt.com/share/697fb5fc-3e3c-8010-9900-2ef3c15f9abd>; it names no
model version.

**Read status.** Claims checked. Theorems 1 and 2, with Lemmas 1 to 3,
Propositions 1 and 2 and the box data of Section 2, were read clause by clause
on the page images and text layer of the PDF; the proofs were read only to
write the pointers on the result pages. No proof step or box was checked, and
the supplementary code was neither fetched nor run. Nothing here awards
verification, acceptance or a tier.

**Relation to the other two notes.** The note cites both earlier notes: the
note of 27 January 2026 credited to Liam Price
([[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/_index|filed
here]]) as [2], by "K. Barreto and L. Price", for an example giving
$m(5)<11$ and for linking $m(n)<p_n$ to one formulation of Problem 951, and
the note of 28 January 2026
([[number_theory/sothanaphan_2026_one_separated_semigroups_prime_minimality/_index|filed
here]]) as [3], for $m(2)=3$ and $m(3)<5$. Its own $n=3$ and $n=5$ cases come
from its box certificates, not from the certificates of those notes. It does
not restate the extension step,
[[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/lemma_11|Lemma 11]]
of the 27 January note, which the claim page applies to its boxes.

**Bears on.** [[../wiki/problems/number_theory/E0951/_index|#951]]: extended
by that Lemma 11, Theorem 1 gives for each $3\le n\le7$ an infinite sequence
with the separation property and $n$ terms below $p_n$, so the inequality
fails for $x$ between the largest of them and $p_n$, just below 5, 7, 11, 13
and 17, on the part `every_x`, the reading for every $x$; the problem page
records this as a
[[../wiki/problems/number_theory/E0951/claims/2026_01_28_sothanaphan|pending
partial claim]]. The note itself says only that the 27 January note linked
$m(n)<p_n$ to one formulation of the problem. Its conjecture that $m(n)<p_n$
for every $n\ge3$ would give, for each $n$, a sequence failing just below
$p_n$, not one sequence failing at arbitrarily large $x$, so neither it nor
Theorem 1 bears on the part `large_x`, the reading for all large $x$.

**Results.**

- [[number_theory/sothanaphan_2026_probabilistic_box_certification_one_separated_semigroups/theorem_1|Theorem 1]]
  (p. 1): for each $3\le n\le7$, $m(n)<p_n$; the generators lie in explicit
  small boxes and are not exhibited.
- [[number_theory/sothanaphan_2026_probabilistic_box_certification_one_separated_semigroups/theorem_2|Theorem 2]]
  (p. 6): a log-box that passes the small-regime interval check and whose tail
  bound is below 1 contains a point at which the semigroup is 1-separated.

Lemmas 1 to 3 and Propositions 1 and 2 (pp. 4--6) are the steps of the proof
of Theorem 2 and are summarized on its page.

No file of this source is held: no license on record permits its redistribution,
and the card cites the edition it names above.
