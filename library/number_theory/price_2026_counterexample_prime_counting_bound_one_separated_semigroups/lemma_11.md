---
name: number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/lemma_11
title: "Lemma 11 (p. 6): a finitely generated 1-separated semigroup takes one more, larger generator"
desc: |
  If reals 1 < a_1 < ... < a_n generate a multiplicative semigroup whose
  distinct elements are at least 1 apart, some a_(n+1) > a_n can be adjoined
  keeping that property; proved by bounding the measure of the excluded
  points of an interval [R, 2R], with no computation.
created: 2026-10-14T22:08:11Z
updated: 2026-10-14T22:08:11Z
---

***

## Statement

For reals $1<a_1<\cdots<a_n$ let
$\mathcal M_n=\{\prod_{i=1}^na_i^{k_i}:(k_1,\dots,k_n)\in\mathbb Z_{\ge0}^n\}$
(p. 2).

**Lemma 11** (Extension step, p. 6). Let $n\ge1$ and let $1<a_1<\cdots<a_n$ be
such that $\mathcal M_n$ is 1-separated, that is, $|x-y|\ge1$ for all
distinct $x,y\in\mathcal M_n$. Then there is $a_{n+1}>a_n$ such that
$\mathcal M_{n+1}$ is also 1-separated.

As printed, the lemma's 1-separation concerns distinct elements of the set
$\mathcal M_n$, while the note's condition (1) (p. 1) concerns distinct
exponent vectors; Corollary 1 (p. 8) applies the lemma inductively, starting
from the five generators of
[[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/proposition_1|Proposition 1]],
to obtain (1) for the infinite sequence.

**Source.** A Counterexample to a Prime-Counting Bound for 1-Separated
Multiplicative Semigroups, note (2026), 11 pp., printing no author; Lemma 11 on
p. 6, proved on pp. 6--8 with Lemmas 9 and 10 (pp. 5--6). The edition read is
identified on the
[[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/_index|source card]].

**Read depth.** Claims checked: the statements of Lemmas 9, 10 and 11 were
read clause by clause on the page images of the PDF. No step of the proof was
checked.

## Proof pointer

pp. 6--8. Write $\beta_i=\log a_i$ and $\beta_{\min}=\min_i\beta_i$. Lemma 9
(p. 5) bounds $N_n(X)=\#\{s\in\mathcal M_n:s\le X\}$ by
$(1+\log X/\beta_{\min})^n$ for $X\ge1$, and Lemma 10 (p. 6) gives
$\sum_{s\in\mathcal M_n}(1+\log s)^m/s<\infty$ for every integer $m\ge0$. Fix
$R>\max\{a_n,2\}$ and $I=[R,2R]$. For $s,t\in\mathcal M_n$ and an integer
$d\ge1$ the excluded set $F_{s,t,d}=\{x\in I:|sx^d-t|<1\}$ has measure at
most $2/(dsR^{d-1})$, since $x\mapsto sx^d$ has derivative at least
$dsR^{d-1}$ on $I$, and it is empty unless $t<s(2R)^d+1$. A point
$a_{n+1}\in I$ outside the union $F$ of these sets has $|a_{n+1}^ds-t|\ge1$
for all such $s$, $t$ and $d$, and comparing $a_{n+1}^ks$ with
$a_{n+1}^{\ell}t$ in the cases $k=\ell$ and $k>\ell$ then makes
$\mathcal M_{n+1}$ 1-separated. Counting the admissible $t$ by Lemma 9 and
summing over $s$ by Lemma 10 bounds the measure of $F$ by $C_3(\log R)^n$ for
all large $R$, with $C_3$ depending on $n$ and $a_1,\dots,a_n$. For $R$ with
$C_3(\log R)^n<R$ the set $I\setminus F$, closed in the compact $I$, is
nonempty, and the note takes $a_{n+1}=\min(I\setminus F)\ge R>a_n$.

## Dependencies

Lemmas 9 and 10 (pp. 5--6) of the same note; no computation (Remark 1,
p. 8).

## Bears on

- [[../wiki/problems/number_theory/E0951/_index|Problem 951]]: the lemma turns
  a finite set of generators with the separation property into an infinite
  sequence with it, so more than $\pi(x)$ such generators, all at most $x$,
  refute the inequality at $x$ on the reading in which it must hold for every
  $x$ (the part `every_x`); the problem's erdosproblems.com commentary gives
  such an extension as the reason that reading fails by a finite calculation. It
  is the step
  [[number_theory/price_2026_counterexample_prime_counting_bound_one_separated_semigroups/theorem_1|Theorem 1]]
  uses at $x=10$, and the
  [[../wiki/problems/number_theory/E0951/claims/2026_01_28_sothanaphan|claim
  for Sothanaphan's two notes]] depends on it for its failures just below 5,
  7, 11, 13 and 17. Each new generator lies in $[R,2R]$ for a large $R$, so
  the lemma gives no control of the count at large $x$ and does not bear on
  the part `large_x`.
