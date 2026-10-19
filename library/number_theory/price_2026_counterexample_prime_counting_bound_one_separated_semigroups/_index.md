---
name: number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups
title: "A Counterexample to a Prime-Counting Bound for 1-Separated Multiplicative Semigroups"
desc: |
  An 11-page note printing no author that gives five reals below 10 whose
  power products are at least 1 apart, certified by a norm bound in
  Q(2^(1/6)) and validated interval arithmetic, and a lemma extending such
  generator sets without end, so #{a_i <= x} <= pi(x) fails at x = 10;
  unrefereed.
license: unstated
created: 2026-10-14T22:08:11Z
updated: 2026-10-14T22:24:01Z
---

# A Counterexample to a Prime-Counting Bound for 1-Separated Multiplicative Semigroups

[[number_theory/_index|..]]

[[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/lemma_11|lemma_11]]: If reals 1 < a_1 < ... < a_n generate a multiplicative semigroup whose
distinct elements are at least 1 apart, some a_(n+1) > a_n can be adjoined
keeping that property; proved by bounding the measure of the excluded
points of an interval [R, 2R], with no computation.

[[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/proposition_1|proposition_1]]: Five reals e^(beta_i), each beta_i an explicit integer combination of the
powers of 2^(1/6), lie between 1 and 10 and generate a semigroup whose
products for distinct exponent vectors differ by at least 1; certified by a
norm bound and a validated interval-arithmetic enumeration, unreviewed.

[[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/theorem_1|theorem_1]]: A strictly increasing sequence of reals above 1 whose power products for
distinct exponent vectors are at least 1 apart can have five terms below
10, so #{a_i <= x} <= pi(x) for all x >= 1 fails at x = 10;
computer-assisted, from a note printing no author, unreviewed.

***

*A Counterexample to a Prime-Counting Bound for 1-Separated Multiplicative
Semigroups*, a note of 11 pages that prints no author, date, affiliation or
reference list and names neither Problem 951 nor erdosproblems.com. Its
attribution is the claim page's: the
[[../wiki/problems/number_theory/E0951/claims/2026_01_27_leeham|claim page for
the counterexample at x = 10]] credits it to Liam Price, the forum user Leeham.
That page's sources are the erdosproblems.com thread for Problem 951, where
Kevin Barreto posted the note on 27 January 2026 as the work of a chain of
ChatGPT-5.2 Pro instances prompted by Leeham, and the problem's
erdosproblems.com commentary, which credits the counterexample at $x=10$ to
ChatGPT-5.2 Pro prompted by Leeham. Sothanaphan's note dated 2 February 2026
cites it as by "K. Barreto and L. Price". The note is not refereed, and the
searches recorded on the problem page found no arXiv or journal version.

**Version and provenance.** The copy read for this card was fetched on
2026-10-14 from
<https://drive.google.com/uc?export=download&id=1CRBMOMCTdAuuVp8Wqace1AQ_dpK9BeTV>,
the direct-download address of the Google Drive file
<https://drive.google.com/file/d/1CRBMOMCTdAuuVp8Wqace1AQ_dpK9BeTV/view> that
the claim page records: 310,635 bytes, 11 pages, its metadata giving no title
or author and a creation time of 2026-01-27T20:03:01Z. A Google Drive file has
no version pin, so the file at that address can change; the card describes
the copy of that date. No notice is printed in the note, and no terms came
with the download; the term is unstated.

**What it claims.** For a strictly increasing sequence of reals $a_i>1$ the
note calls the set of its power products $A(k)=\prod_ia_i^{k_i}$, over
finitely supported vectors $k$ of nonnegative integers, 1-separated when
$|A(k)-A(\ell)|\ge1$ for all distinct $k$ and $\ell$ (its condition (1),
p. 1). Theorem 1 (p. 8) refutes the implication from (1) to
$\#\{i:a_i\le x\}\le\pi(x)$ for all $x\ge1$ (its (2), p. 1), which the
abstract calls a question of Erdős. Section 2 (p. 2) defines five generators
$a_i=e^{\beta_i}$ with $\beta_i\in\mathbb Z[2^{1/6}]$, and Lemma 1 places them
between 1 and 10, the largest about $9.84133$. Section 3 (pp. 2--5) proves
their semigroup 1-separated (Proposition 1, p. 5): the $\beta_i$ are linearly
independent over $\mathbb Q$, a norm bound in $\mathbb Q(2^{1/6})$ keeps every
nonzero integer combination of them away from 0, so two products less than 1
apart would need exponents differing by at most 29 and logarithms below 43,
and a validated interval-arithmetic enumeration of the 85,838 exponent vectors
in that range finds every gap above 1, the least about $1.1067$. Section 4
(pp. 5--8) proves the extension step (Lemma 11, p. 6): a finitely generated
1-separated semigroup takes one more, larger generator and stays 1-separated,
by a bound on the measure of the excluded points of an interval $[R,2R]$;
iterating it gives the infinite sequence of Corollary 1 (p. 8). Remark 1
(p. 8) states that Proposition 1 is computer-assisted and Lemma 11 is not.
Appendix A (pp. 8--11) prints a Python script using mpmath interval arithmetic
for the numerical facts behind Lemmas 1, 6, 7 and 8, without its output.

**AI disclosure.** None is printed. The thread post and the erdosproblems.com
commentary, as the claim page records them, attribute the note to ChatGPT-5.2
Pro prompted by Leeham.

**Read status.** Claims checked. The statements of Theorem 1, Proposition 1 and
Lemma 11, with Lemma 1 and Corollary 1, were read clause by clause on the page
images of the PDF; the proofs were read only to write the pointers on the
result pages. No proof step, bound or computation was checked, and the script
of Appendix A was not run. Nothing here awards verification, acceptance or a
tier.

**Relation to the other two notes.** Sothanaphan's notes write $m(n)$ for the
infimum of $x_n$ over reals $1<x_1<\cdots<x_n$ whose semigroup is free with
elements at least 1 apart, so that the first $n$ primes give $m(n)\le p_n$.
His note of 28 January 2026
([[number_theory/sothanaphan_2026_one_separated_semigroups_prime_minimality/_index|filed
here]]), posted a day after this one, does not cite it; it proves $m(3)<5$
with three rational generators and lists $m(n)<p_n$ as unknown for every
$n\ge4$. His note dated 2 February 2026
([[number_theory/sothanaphan_2026_probabilistic_box_certification_one_separated_semigroups/_index|filed
here]]) cites this note for $m(5)<11=p_5$, from the five generators here, all
below 10, and for linking $m(n)<p_n$ to a formulation of Problem 951; it
proves $m(n)<p_n$ for $3\le n\le7$ by another method. Neither restates
[[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/lemma_11|Lemma 11]];
the claim page for both applies it to their generators.

**Bears on.** [[../wiki/problems/number_theory/E0951/_index|#951]]: Theorem 1
answers the part `every_x`, the reading in which the inequality must hold for
every $x$, in the negative at $x=10$; the problem page records it as a
[[../wiki/problems/number_theory/E0951/claims/2026_01_27_leeham|pending partial
claim]]. The note does not address the part `large_x`, the reading for all
large $x$; the curator's reply recorded on that claim page notes that the
construction may satisfy the inequality for all large $x$.

**Results.**

- [[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/theorem_1|Theorem 1]]
  (p. 8): the separation condition (1) does not imply
  $\#\{i:a_i\le x\}\le\pi(x)$ for all $x\ge1$, since an infinite sequence
  satisfying (1) can have five terms below 10.
- [[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/proposition_1|Proposition 1]]
  (p. 5): the five explicit generators $e^{\beta_i}$ with
  $\beta_i\in\mathbb Z[2^{1/6}]$, all between 1 and 10 by Lemma 1, generate a
  1-separated semigroup.
- [[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/lemma_11|Lemma 11]]
  (p. 6): if $1<a_1<\cdots<a_n$ generate a 1-separated semigroup, some
  $a_{n+1}>a_n$ can be adjoined keeping it 1-separated.

No file of this source is held: no license on record permits its redistribution,
and the card cites the edition it names above.
