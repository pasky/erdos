---
name: number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/theorem_1
title: "Theorem 1 (p. 8): separated power products do not force the prime-counting bound at every x"
desc: |
  A strictly increasing sequence of reals above 1 whose power products for
  distinct exponent vectors are at least 1 apart can have five terms below
  10, so #{a_i <= x} <= pi(x) for all x >= 1 fails at x = 10;
  computer-assisted, from a note printing no author, unreviewed.
created: 2026-10-14T22:08:11Z
updated: 2026-10-14T22:08:11Z
---

***

## Statement

Let $(a_i)_{i\ge1}$ be a strictly increasing sequence of reals with $a_i>1$,
and for a finitely supported vector $k=(k_i)_{i\ge1}$ of nonnegative integers
put $A(k)=\prod_{i\ge1}a_i^{k_i}$ (p. 1). The note's condition (1) asks
$|A(k)-A(\ell)|\ge1$ for all distinct finitely supported $k$ and $\ell$, and
the note then calls the set of these monomials 1-separated; its condition (2)
is the bound
$\#\{i:a_i\le x\}\le\pi(x)$ for all $x\ge1$, with $\pi$ the prime-counting
function (p. 1).

**Theorem 1** (p. 8). The implication (1) $\Rightarrow$ (2) is false.

The witness is the sequence of Corollary 1 (p. 8), an infinite strictly
increasing sequence $1<a_1<a_2<\cdots$ satisfying (1) whose first five terms
are the generators $a_i=e^{\beta_i}$, $1\le i\le5$, of
[[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/proposition_1|Proposition 1]].
Lemma 1 (p. 2) gives $1<a_1<\cdots<a_5<10$, so
$\#\{i:a_i\le10\}\ge5>4=\pi(10)$. The abstract (p. 1) puts the question it
answers as whether the separation hypothesis forces the bound "for all $x$";
the note addresses no other reading.

**Source.** A Counterexample to a Prime-Counting Bound for 1-Separated
Multiplicative Semigroups, note (2026), 11 pp., printing no author; Theorem 1,
Corollary 1 and Remark 1 on p. 8, Lemma 1 on p. 2. The edition read is
identified on the
[[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/_index|source card]].

**Read depth.** Claims checked: the statements of Theorem 1, Corollary 1 and
Lemma 1 were read clause by clause on the page images of the PDF. No proof
step or computation was checked.

## Proof pointer

p. 8. Corollary 1 takes the five generators of Section 2, whose semigroup is
1-separated by
[[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/proposition_1|Proposition 1]],
and adjoins $a_6,a_7,\dots$ one at a time by
[[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/lemma_11|Lemma 11]];
any two monomials of the resulting sequence involve finitely many generators,
so they lie in one of the finitely generated semigroups of the construction
and are at least 1 apart. Lemma 1 rests on interval enclosures computed by
the script of Appendix A (pp. 8--11), with $a_1\approx4.23968$,
$a_2\approx5.78422$, $a_3\approx6.89100$, $a_4\approx8.55119$ and
$a_5\approx9.84133$ (p. 2). Remark 1 (p. 8) calls Proposition 1
computer-assisted and Lemma 11 purely analytic.

## Dependencies

[[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/proposition_1|Proposition 1]]
(p. 5) and
[[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/lemma_11|Lemma 11]]
(p. 6), with Lemma 1 (p. 2) and Corollary 1 (p. 8) of the same note.

## Bears on

- [[../wiki/problems/number_theory/E0951/_index|Problem 951]]: on the reading
  in which the inequality must hold for every $x$ (the problem page's part
  `every_x`), the theorem is a counterexample at $x=10$, recorded on the
  [[../wiki/problems/number_theory/E0951/claims/2026_01_27_leeham|claim
  page]] as a pending partial claim. It says nothing about the reading for all
  sufficiently large $x$ (the part `large_x`).
