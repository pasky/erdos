---
name: number_theory/sothanaphan_2026_one_separated_semigroups_prime_minimality/theorem_2
title: "Theorem 2 (p. 3): three rational generators below 5 with a free one-separated semigroup"
desc: |
  The reals 101/42, 367/103 and 113/24 generate a free multiplicative
  semigroup whose distinct elements differ by at least 1, so m(3) <= 113/24 <
  5 = p_3; proved by Matveev's bound, de Weger's LLL reduction and an exact
  finite check, computer-assisted and unreviewed.
created: 2026-10-14T22:08:11Z
updated: 2026-10-14T22:08:11Z
---

***

## Statement

For reals $1<x_1<\cdots<x_n$ let
$\mathcal S(x_1,\dots,x_n)=\{x_1^{a_1}\cdots x_n^{a_n}:a_i\in\mathbb N_0\}$.
The note calls it free when the map
$(a_1,\dots,a_n)\mapsto x_1^{a_1}\cdots x_n^{a_n}$ is injective on
$\mathbb N_0^n$, and one-separated when $|u-v|\ge1$ for all distinct
$u,v\in\mathcal S(x_1,\dots,x_n)$ (Definition 1, p. 1). It writes $m(n)$ for
the infimum of $\max\{x_1,\dots,x_n\}$ over all $n$-tuples
$1<x_1<\cdots<x_n$ whose semigroup is free and one-separated (Definition 2,
p. 1); the first $n$ primes give $m(n)\le p_n$.

**Theorem 2** (p. 3). The triple

$$
x_1=\frac{101}{42}\approx2.4047619,\qquad
x_2=\frac{367}{103}\approx3.5631068,\qquad
x_3=\frac{113}{24}\approx4.7083333
$$

has a free one-separated semigroup. In particular $m(3)\le113/24<5=p_3$.

Free and one-separated together say that products for distinct exponent
vectors differ by at least 1, which is the separation hypothesis of Problem
951 for these three generators.

**Source.** N. Sothanaphan, One-separated multiplicative semigroups and prime
minimality, note dated 28 January 2026, 15 pp.; Theorem 2 on p. 3, proved in
Section 5 (pp. 3--5) with Lemmas 1 and 2 of Section 4 (pp. 2--3), and the
script and sample run of Section 7 (pp. 5--15). The edition read is
identified on the
[[number_theory/sothanaphan_2026_one_separated_semigroups_prime_minimality/_index|source card]].

**Read depth.** Claims checked: the statement, with Definitions 1 and 2 and
Lemmas 1 to 3, was read clause by clause on the page images of the PDF. No
proof step, bound or computation was checked, and the script was not run.

## Proof pointer

Section 5, pp. 3--5. The triple came from a random search: 20,000 trials of
rational triples with prime numerators in $[101,400]$ and integer denominators
in $[2,200]$, filtered by $2.3<x_1<3$, $x_1+1.01<x_2<4$ and
$x_2+1.01<x_3<4.999$, each tested for separation up to exponent 10 (p. 3);
the proof does not depend on the search. Freeness (Lemma 3, p. 4): after
clearing denominators, comparing the powers of the primes 101, 367 and 113
forces equal exponents. One-separation (Section 5.2, pp. 4--5): by Lemma 1
(p. 2) a gap in $(0,1)$ in a free semigroup moves to a pair of elements with
disjoint supports, dividing out their common factor; for such a pair $u>v$,
Lemma 2 (p. 3), which assumes $x_1\ge2$, gives $0<L<c_0e^{-d_0X}$ for
$L=\log(u/v)=\sum_id_i\log x_i$, $X=\max_i|d_i|$,
$d_0=(\log x_1)^2/\log x_n$ and $c_0=\exp(\log x_1\log2/\log x_n)$. Step 1
(p. 4) sets this against an explicit Matveev lower bound
$\log|L|>-K(1+\log X)$ for $X\ge2$, with
$K=1.4\cdot30^{t+3}t^{4.5}D^2(1+\log D)\prod_iA_i$, $t=3$, $D=1$,
$A_i\ge\max(Dh(x_i),|\log x_i|,0.16)$ and $h(a/b)=\log\max\{|a|,|b|\}$,
which caps $X$ at an $X_0$ above $10^{15}$. Step 2 (p. 4) applies de Weger's
reduction (§3.7 of the note's [3]: his Lemma 3.7, once LLL and his Lemma 3.4
show that the lattice has no too-short vectors) to a 3-dimensional
approximation lattice built from $\log x_1,\log x_2,\log x_3$ with scaling
$C=32X_1^3$, doubled until the lemma's condition holds, and lowers the cap to
149, 29 and then 21. Step 3 (p. 5) sorts the $22^3=10{,}648$ products with
exponents in $[0,21]$ exactly and finds the least consecutive gap
$3791/3528\approx1.0745$, between $x_3$ and $x_1^2$. Section 7 prints the
script that runs the three steps and a sample run, whose fourth reduction
round leaves the cap at 21, ending in its success line.

## Dependencies

Lemmas 1 to 3 (pp. 2--4) of the same note; Matveev's explicit lower bound for
linear forms in logarithms (E. M. Matveev, Izvestiya: Mathematics 64 (2000),
1217--1269, the note's [2], with the constants as stated in P. Tiebekabe,
arXiv:2209.07871, Thm. 2.1, its [4]); de Weger's reduction (B. M. M. de Weger,
Algorithms for Diophantine equations, CWI Tract 65, 1989, §3.7, its [3]).
None of the three is held or was checked here.

## Bears on

- [[../wiki/problems/number_theory/E0951/_index|Problem 951]]: extended to an
  infinite sequence by
  [[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/lemma_11|Lemma 11]]
  of the note credited to Liam Price, the triple gives three terms at most $x$
  for $113/24\le x<5$, where $\pi(x)=2$, refuting the inequality there on the
  reading in which it must hold for every $x$ (the part `every_x`); the note
  itself states only $m(3)<5$, and the deduction is the
  [[../wiki/problems/number_theory/E0951/claims/2026_01_28_sothanaphan|claim
  page's]]. It does not bear on the reading for all large $x$ (the part
  `large_x`).
