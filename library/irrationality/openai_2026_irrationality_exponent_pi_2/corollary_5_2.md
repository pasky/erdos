---
name: irrationality/openai_2026_irrationality_exponent_pi_2/corollary_5_2
title: "Corollary 5.2: sum 1/(n^a |sin n|^b) converges exactly when a > max(1, b)"
desc: |
  The manuscript's generalized Flint–Hills criterion: for fixed a, b > 0 the
  sum over n >= 1 of 1/(n^a |sin n|^b), n in radians, converges if and only
  if a > max(1, b); the convergence half rests on Theorem 1.1. Claims
  checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

**Corollary 5.2.** Let $a,b>0$ be fixed real numbers. The series

$$
\sum_{n=1}^{\infty}\frac{1}{n^a|\sin n|^b},
$$

with $n$ read as an angle in radians, converges if and only if
$a>\max\{1,b\}$.

The case $a=3$, $b=2$ is
[[irrationality/openai_2026_irrationality_exponent_pi_2/corollary_1_2|Corollary 1.2]].
The criterion includes both boundary cases: the series diverges at $a=1$ and
at $a=b>1$. The introduction credits the whole criterion to Theorem 1.1
and the spacing argument. On this page's reading, only the convergence half
depends on
[[irrationality/openai_2026_irrationality_exponent_pi_2/theorem_1_1|Theorem 1.1]];
the divergence half uses only the comparison with $\sum n^{-a}$ and the
continued-fraction convergents of $\pi$, which need no more than the
classical irrationality of $\pi$ (a fact the manuscript also recovers from
Theorem 1.1).

**Source.** OpenAI, *The irrationality exponent of $\pi$ is $2$*, release
folder `preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026`;
TeX file `build/sections/series.tex`, label `series:generalized` (lines
97--104), PDF p. 20; the proof is at lines 106--155 and closes on PDF p. 21.
The introduction announces the criterion at `build/main.tex` lines 102--109 (PDF
p. 2). Provenance and attestations are on
[[irrationality/openai_2026_irrationality_exponent_pi_2/_index|the card]].

**Read depth.** Claims checked: the statement was read clause by clause in
the TeX source. The proof was read for its structure only; no step was
checked. Theorem 1.1, on which the convergence half rests, is itself claims
checked only. Nothing here is independently reviewed.

## Proof pointer

Convergence. Suppose $a>\max\{1,b\}$ and choose $\varepsilon>0$ with
$a>\max\{1,b\}+b\varepsilon$. Theorem 1.1, with the finitely many small
denominators absorbed into a constant, gives
$\|q\pi\|\ge c_\varepsilon q^{-1-\varepsilon}$ for all $q\ge1$, where
$\|x\|$ is the distance to the nearest integer. The spacing count of the
dyadic Lemma 5.1, run with $d=c_\varepsilon(2K)^{-1-\varepsilon}$ on the at
most $K$ points of the block $K\le q<2K$, bounds the block's part of
$\sum_qq^{-a}\|q\pi\|^{-b}$ by a constant times
$K^{-a}d^{-b}\sum_{j\le K}j^{-b}$. This is of order
$K^{1-a+b\varepsilon}$ for $b<1$, $K^{1-a+\varepsilon}\log(2K)$ for $b=1$
and $K^{b-a+b\varepsilon}$ for $b>1$, each summable over $K=1,2,4,\dots$
by the choice of $\varepsilon$. Grouping each $n$ by a nearest integer $q$
to $n/\pi$, as in the proof of Corollary 1.2, bounds the group of $q\ge1$
by $4(2/\pi)^a(\pi/2)^bq^{-a}\|q\pi\|^{-b}$.

Divergence. If $a\le1$ the series dominates $\sum n^{-a}$. If $1<a\le b$,
take the convergents $p_j/q_j$ of $\pi$: then $|\sin p_j|\le|p_j-\pi q_j|<1/q_j$
and eventually $p_j\le(\pi+1)q_j$, so the term at $n=p_j$ exceeds
$(\pi+1)^{-b}p_j^{b-a}$, which does not tend to zero.

## Dependencies

[[irrationality/openai_2026_irrationality_exponent_pi_2/theorem_1_1|Theorem 1.1]]
for the convergence half; the spacing argument of Lemma 5.1, proved in the
text; and the classical facts that the convergents $p_j/q_j$ of $\pi$
satisfy $|p_j-\pi q_j|<1/q_j$ with $p_j\to\infty$.

## Bears on

No problem page is identified as using this result; the card's Bears on
section records the pages read for a possible use.
