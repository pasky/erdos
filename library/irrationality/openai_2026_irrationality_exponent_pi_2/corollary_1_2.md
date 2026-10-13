---
name: irrationality/openai_2026_irrationality_exponent_pi_2/corollary_1_2
title: "Corollary 1.2: the Flint–Hills series sum 1/(n^3 sin^2 n) converges"
desc: |
  The manuscript's stated consequence: the Flint–Hills series, the sum over
  n >= 1 of 1/(n^3 sin^2 n) with n in radians, converges, deduced from
  Theorem 1.1 by a dyadic spacing argument. Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

**Corollary 1.2.** The series

$$
\sum_{n\ge1}\frac{1}{n^3\sin^2n},
$$

with $n$ read as an angle in radians, converges.

Every term is finite because $\pi$ is irrational, so $\sin n\ne0$ for
$n\ge1$. The manuscript places the statement between two earlier criteria
(pp. 1--2): Alekseyev showed that convergence forces $\mu(\pi)\le5/2$ (his
Corollary 4), and Meiburg that $\mu(\pi)<5/2$ suffices (his Theorem 2.5),
where $\mu$ is the irrationality exponent; neither settles the boundary case
$\mu(\pi)=5/2$. The corollary uses
[[irrationality/openai_2026_irrationality_exponent_pi_2/theorem_1_1|Theorem 1.1]]
only through the weaker consequence $\mu(\pi)<5/2$, and the manuscript gives
its own short deduction rather than citing Meiburg's.

The deduction runs through Lemma 5.1, stated for any irrational number. Let
$\|x\|$ be the distance from $x$ to the nearest integer. **Lemma 5.1.** If
$\alpha>0$ is irrational and, for some $c>0$ and some $1<\nu<5/2$,
$\|q\alpha\|\ge cq^{1-\nu}$ for every integer $q\ge1$, then
$\sum_{q\ge1}q^{-3}\|q\alpha\|^{-2}<\infty$ (p. 19).

**Source.** OpenAI, *The irrationality exponent of $\pi$ is $2$*, release
folder `preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026`;
TeX file `build/main.tex`, label `thm:flinthills` (lines 90--92), PDF p. 1,
with the series defined at lines 80--88; Lemma 5.1 is `series:dyadic` in
`build/sections/series.tex` (lines 11--21, PDF p. 19); the proof of the
corollary is at lines 47--91 of that file and closes on PDF p. 20. Read
2026-10-12. Provenance and attestations are on
[[irrationality/openai_2026_irrationality_exponent_pi_2/_index|the card]].

**Read depth.** Claims checked: the corollary, the definition of the series
and the statement of Lemma 5.1 were read clause by clause in the TeX source.
The proofs of Lemma 5.1 and of the corollary were read for their structure
only; no step was checked. Theorem 1.1, on which the corollary rests, is
itself claims checked only. Nothing here is independently reviewed.

## Proof pointer

Fix $\nu$ with $2<\nu<5/2$. Theorem 1.1, applied with the nearest-integer
numerator, gives $\|q\pi\|\ge q^{1-\nu}$ for every $q\ge Q(\nu)$; since
$\pi$ is irrational, the finitely many smaller $q$ are absorbed into a
constant $c>0$, so $\|q\pi\|\ge cq^{1-\nu}$ for all $q\ge1$.

Lemma 5.1 is a spacing count over dyadic blocks. For $K\le q<2K$ the points
$q\alpha$ on the circle $\mathbb R/\mathbb Z$ lie at distance at least
$d=c(2K)^{1-\nu}$ from $0$, and, by the hypothesis applied to the
difference of two indices, at least $d$ from one another. Ordered by
distance from $0$ on each half of the circle, the $k$th point is at
distance at least $kd$, so the block contributes
$O(K^{-3}d^{-2})=O(K^{2\nu-5})$, which sums over $K=1,2,4,\dots$ because
$\nu<5/2$.

The transfer to the series groups each $n\ge1$ by a nearest integer $q$ to
$n/\pi$. The group of $q=0$ is finite. For $q\ge1$ the group has at most
four members, each with $n\ge\pi q/2$ and, by concavity of sine on
$[0,\pi/2]$, $|\sin n|=|\sin(n-q\pi)|\ge(2/\pi)\|q\pi\|$; so the group
contributes at most $(8/\pi)q^{-3}\|q\pi\|^{-2}$, and the sum over $q$
converges by Lemma 5.1.

## Dependencies

[[irrationality/openai_2026_irrationality_exponent_pi_2/theorem_1_1|Theorem 1.1]],
in the form $\mu(\pi)<5/2$, and Lemma 5.1, proved in the text. Alekseyev's
and Meiburg's criteria are cited for context and are not used in the
deduction.

## Bears on

No problem page is identified as using this result; the card's Bears on
section records the pages read for a possible use.
