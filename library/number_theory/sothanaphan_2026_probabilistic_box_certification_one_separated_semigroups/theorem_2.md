---
name: number_theory/sothanaphan_2026_probabilistic_box_certification_one_separated_semigroups/theorem_2
title: "Theorem 2 (p. 6): a box certificate for a 1-separated semigroup with generators in a log-box"
desc: |
  If a log-box of generators passes a finite interval check on all products
  below a height cutoff and a computable union bound for the higher products
  is below 1, then some point of the box generates a semigroup whose
  products for distinct exponent vectors are at least 1 apart.
created: 2026-10-14T22:08:11Z
updated: 2026-10-14T22:08:11Z
---

***

## Statement

Fix $n\ge1$, a center $\tilde b\in(0,\infty)^n$ and a radius $r>0$, and let
$\mathcal J=\prod_{i=1}^n[\tilde b_i-r,\tilde b_i+r]$ carry the uniform
probability measure, with corners $b^\pm=\tilde b\pm r(1,\dots,1)$ (pp.
3--4). For $b\in\mathcal J$ the generators are $e^{b_1},\dots,e^{b_n}$, and
the product with exponent vector $k\in\mathbb N_0^n$ is
$X_k(b)=\exp(\langle k,b\rangle)$; the semigroup is 1-separated at $b$ when
$|X_k(b)-X_\ell(b)|\ge1$ for all distinct $k,\ell\in\mathbb N_0^n$. Write
$L_k=\langle k,b^-\rangle$ and
$U_k=\langle k,b^+\rangle=L_k+2r\|k\|_1$, so that
$X_k(b)\in[e^{L_k},e^{U_k}]$ on $\mathcal J$; for $T\ge0$ let
$K(T)=\{k\in\mathbb N_0^n:\langle k,b^-\rangle\le T\}$ and
$N(T)=\prod_{i=1}^n(\lfloor T/b_i^-\rfloor+1)$, which bounds $|K(T)|$. Fix a
cutoff $T_0\ge0$ and put $T_{\rm small}=T_0+\delta$ with a padding
$\delta>\log2$ (the note's `small_extra`, 1 in the implementation). The
small-regime condition, the note's (4) (p. 4), is that when $K(T_{\rm small})$
is listed by increasing $L_k$, each adjacent pair $k_j,k_{j+1}$ has
$e^{L_{k_{j+1}}}-e^{U_{k_j}}\ge1$.

**Theorem 2** (Box certificate, p. 6). Fix a log-box $\mathcal J$ of radius
$r$ about $\tilde b$ and a cutoff $T_0$. Assume

- the small-regime check succeeds, that is, (4) holds for $K(T_{\rm small})$,
  the hypothesis of Proposition 1 (p. 4); and
- the tail bound of Proposition 2 (p. 6) is strictly less than 1:
  $\sum_{t=\lceil T_0\rceil}^{\infty}N(t+2)^2\min(1,e^{-t}/r)<1$.

Then there is at least one $b\in\mathcal J$ at which the semigroup
$\{X_k(b):k\in\mathbb N_0^n\}$ is 1-separated.

The note stresses that this is an existence statement that identifies no such
$b$ (p. 6). The counting function needs $b^->0$ coordinatewise, which the
implementation secures by choosing $r$ small enough that
$\mathcal J\subset(0,\infty)^n$ (p. 4).

**Source.** N. Sothanaphan, Probabilistic box-certification for one-separated
multiplicative semigroup problem, note dated 2 February 2026, 8 pp.; Theorem 2
on p. 6, with Lemmas 1 to 3 and Propositions 1 and 2 of Section 3
(pp. 3--6), and the description of the program in Section 4 (pp. 6--7). The
edition read is identified on the
[[number_theory/sothanaphan_2026_probabilistic_box_certification_one_separated_semigroups/_index|source card]].

**Read depth.** Claims checked: the statements of Theorem 2, Lemmas 1 to 3
and Propositions 1 and 2 were read clause by clause on the page images and
text layer of the PDF. No proof step was checked.

## Proof pointer

Section 3, pp. 3--6. Lemma 1 (p. 4): if $|X_k(b)-X_\ell(b)|<1$ and $m$ is
the smaller of $\langle k,b\rangle$ and $\langle\ell,b\rangle$, the larger is
at most $m+\log(1+e^{-m})<m+\log2$. Proposition 1 (p. 4): under (4) no
$b\in\mathcal J$ has a pair less than 1 apart with $m<T_0$, since both
exponent vectors then lie in $K(T_{\rm small})$ and the enclosures
$[e^{L_k},e^{U_k}]$, sorted, are pairwise at least 1 apart. Lemma 2 (p. 5):
such a pair has $|\langle k-\ell,b\rangle|\le\log(1+e^{-m})\le e^{-m}$.
Lemma 3 (p. 5): for $s\in\mathbb Z^n\setminus\{0\}$ and $\eta>0$, a uniform
$b\in\mathcal J$ has $\mathbb P(|\langle s,b\rangle|\le\eta)\le\min(1,\eta/r)$.
Proposition 2 (p. 6): splitting by $m\in[t,t+1)$ for integers
$t\ge\lceil T_0\rceil$, both vectors lie in $K(t+2)$, each pair has
probability at most $\min(1,e^{-t}/r)$ by Lemmas 2 and 3, and a union bound
over at most $N(t+2)^2$ pairs gives the series. The theorem follows: pairs with
$m<T_0$ are excluded everywhere on $\mathcal J$, and the others occur with
probability below 1. Section 4 (pp. 6--7) says how `interval_certify.py`
checks the two hypotheses: corners widened by a precision-dependent
$\varepsilon$, an optional double-precision sort whose order is checked
against the exact $L_k$, and the series cut off once the remainder is
guaranteed at most a tolerance (default $10^{-40}$) or at a hard cap; the
note does not say how a run that stops at the cap is treated.

## Dependencies

Lemmas 1 to 3 and Propositions 1 and 2 (pp. 4--6) of the same note; nothing
outside it.

## Bears on

- [[../wiki/problems/number_theory/E0951/_index|Problem 951]]: the
  certificate behind
  [[number_theory/sothanaphan_2026_probabilistic_box_certification_one_separated_semigroups/theorem_1|Theorem 1]],
  whose generator sets give failures of the inequality just below 5, 7, 11,
  13 and 17 on the reading for every $x$ (the part `every_x`); on its own it
  concerns one box and bears on the problem only through that theorem.
