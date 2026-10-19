---
name: integer_sequences/li_2026_subexponential_good_sequence/theorem_1
title: "Theorem 1 (p. 1): a good sequence of primes with log u_n = √n + O(1/√n)"
desc: |
  The manuscript's main claim: a good sequence of primes exists with
  log u_n = √n + O(1/√n), so u_n = exp((1+o(1))√n) ≤ e^{o(n)}, found by
  drawing each large term at random among the primes just above e^√n;
  statement checked, proof unreviewed.
created: 2026-10-14T22:08:31Z
updated: 2026-10-14T22:08:31Z
---

***

## Statement

**Setting (p. 1).** Let $u=(u_i)_{i\ge1}$ be pairwise coprime integers with
$u_i>1$ and $\sum_i1/u_i<\infty$, and put

$$
D=D(u)=\prod_{i=1}^{\infty}\Bigl(1-\frac1{u_i}\Bigr),
$$

which is positive. Let $a_1<a_2<\cdots$ be the positive integers divisible by
no $u_i$, put $P_t=u_1u_2\cdots u_t$ and $P_0=1$, and for $x\ge1$ let $t_x$
be the index with $P_{t_x}\le x<P_{t_x+1}$. The sequence $u$ is *good* when,
for every $\varepsilon>0$, every sufficiently large $x$ satisfies

$$
\max_{a_k<x}(a_{k+1}-a_k)<(1+\varepsilon)\,t_x\,D^{-1}.
$$

**Theorem 1** (p. 1). There is a good sequence $u_1<u_2<\cdots$ of primes
with

$$
\log u_n=\sqrt n+O(n^{-1/2}).
$$

Consequently $u_n=\exp((1+o(1))\sqrt n)\le e^{o(n)}$.

The theorem asserts existence only: the proof draws a random sequence and
fixes one outcome with a property of probability one, so no explicit
sequence is given. The definition is the problem's, as erdosproblems.com
states it, with $D^{-1}$ written for $\prod_i(1-1/u_i)^{-1}$, and an
increasing sequence of primes with $\sum_n1/u_n<\infty$ meets the problem's
hypotheses. The manuscript has no reference list and does not mention Erdős.
Erdős's 1981 theorem, recorded at
[[additive_bases/erdos_1981_problems_results_additive_multiplicative_number_theory/display_3_5|display (3.5) of his 1981 paper]],
gives a good sequence of primes chosen to grow sufficiently fast; Theorem 1
claims one of subexponential growth.

**Source.** Peter Li, *A Subexponential Good Sequence*, manuscript dated
April 27, 2026, 7 pp.; the definitions and Theorem 1 on p. 1, the proof in
Sections 2--4, pp. 2--7. The edition read is identified on the
[[integer_sequences/li_2026_subexponential_good_sequence/_index|source card]].

**Read depth.** Claims checked: the definitions and the statement were read
clause by clause on the page image of p. 1. The proof was read through for
structure only; no step of it was checked.

## Proof sketch

The steps as the manuscript presents them; none was checked here.

1. **The random sequence (Section 2, pp. 2--3).** For large $n$ let
   $\mathcal P_n$ be the set of primes in
   $I_n=[e^{\sqrt n},e^{\sqrt n+1/(10\sqrt n)}]$. Since
   $\sqrt{n+1}-\sqrt n>1/(10\sqrt n)$ for large $n$, these intervals are
   disjoint and increasing, and the prime number theorem with error term
   $O(y\exp(-c\sqrt{\log y}))$ gives $|\mathcal P_n|\gg e^{\sqrt n}/n$, the
   paper's (1). For a large $n_0$, the terms $u_1<\cdots<u_{n_0-1}$ are
   fixed primes below $e^{\sqrt{n_0}}$, and each $u_n$ with $n\ge n_0$ is
   drawn uniformly from $\mathcal P_n$, independently. Every outcome is an
   increasing sequence of primes with the growth (2), so $D>0$; moreover
   $\log P_t=\frac23t^{3/2}+O(t^{1/2})$ (3), so that for a constant $B$ and
   all large $t$, $P_{t+1}\le N_t=\exp(\frac23(t+1)^{3/2}+B\sqrt t)$ (4).
2. **Excluding certificates (Section 3, pp. 3--5).**
   [[integer_sequences/li_2026_subexponential_good_sequence/lemma_1|Lemma 1]]
   rules out, almost surely and for all large $t$, an integer $0\le n<N_t$ with
   $\lceil(1+\eta)t\rceil$ distinct terms of index above $K_0(C,\eta)$
   dividing translates $n+j$, $1\le j\le Ct$. The pairs of an integer
   $C\ge1$ and a rational $\eta>0$ are countable, so some outcome satisfies
   the lemma for all of them at once; that outcome is fixed.
3. **From a long gap to a certificate (Section 4, pp. 5--7).** Given
   $0<\varepsilon\le1$, take an integer $C>2D^{-1}$ (12), a rational $\eta$
   with $0<\eta<\varepsilon/5$ (13), and $K\ge K_0(C,\eta)$ with
   $\sigma_K=\sum_{i>K}1/u_i<\varepsilon D/16$ (14); then
   $D_K=\prod_{i\le K}(1-1/u_i)\ge D$. Suppose that for arbitrarily large
   $x$ some $a_k<x$ has $a_{k+1}-a_k\ge(1+\varepsilon)tD^{-1}$, where
   $t=t_x$. Put $n=a_k$, so that $n<P_{t+1}\le N_t$, and
   $L=\lfloor(1+\varepsilon/2)tD^{-1}\rfloor$ (16): each of
   $n+1,\dots,n+L$ is divisible by some $u_i$, and $L\le Ct$ (17). By the
   Chinese remainder theorem, $R=D_KL+O_K(1)\ge(1+\varepsilon/3)t$ of these
   integers are divisible by none of $u_1,\dots,u_K$ (18), so each of them
   is divisible by some $u_i$ with $i>K$. Since $u_i$ divides at most
   $1+L/u_i$ of the $L$ integers, the set $S$ of these indices has
   $|S|\ge R-L\sigma_K\ge(1+23\varepsilon/96)t$ (19), which is at least
   $\lceil(1+\eta)t\rceil$ for large $t$. That many of these indices, each
   with a position $j\le L$ at which $u_i\mid n+j$, form a certificate that
   Lemma 1 rules out for large $t$; hence the defining inequality holds for
   all large $x$.

## Dependencies

[[integer_sequences/li_2026_subexponential_good_sequence/lemma_1|Lemma 1]]
(p. 3) of the same manuscript; the prime number theorem with the de la Vallée
Poussin error term, in the form
$\pi(y)=\operatorname{li}(y)+O(y\exp(-c\sqrt{\log y}))$ with an absolute
$c>0$, called standard and given without a reference (p. 2); the
Borel--Cantelli lemma (p. 5) and the Chinese remainder theorem (p. 6).

## Bears on

- [[../wiki/problems/integer_sequences/E1101/_index|Problem 1101]]: the
  theorem claims a good sequence with $u_n\le e^{o(n)}$, which would answer
  the problem's second question affirmatively. Its growth
  $\exp((1+o(1))\sqrt n)$ is far above $n^{O(1)}$, so the first question,
  whether some good sequence has $u_n<n^{O(1)}$, is untouched. The claim and
  its standing are recorded on
  [[../wiki/problems/integer_sequences/E1101/claims/2026_04_27_li|the problem's claim page]].
