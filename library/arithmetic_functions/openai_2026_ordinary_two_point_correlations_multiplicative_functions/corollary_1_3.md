---
name: arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/corollary_1_3
title: "Corollary 1.3: ordinary Elliott cancellation along fixed nonproportional affine forms"
desc: |
  The affine form of the qualitative claim: under the hypotheses of Theorem 1.2,
  the ordinary average of f_1(a_1n+b_1)f_2(a_2n+b_2) tends to zero for fixed
  nonproportional affine forms, intercepts zero and common factors allowed.
  Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

Multiplicative functions $f:\mathbb N\to\mathbb D$ and uniform
nonpretentiousness are as on the page for
[[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/theorem_1_2|Theorem 1.2]]:
for every fixed Dirichlet character $\chi$,
$\inf_{|t|\le N}D(f,\chi n^{it};N)\to\infty$, where $D(f,\chi n^{it};X)^2$
is the sum over primes $p\le X$ of
$(1-\operatorname{Re}(f(p)\overline{\chi(p)p^{it}}))/p$.

**Corollary 1.3.** Let $f_1,f_2:\mathbb N\to\mathbb D$ be multiplicative, at
least one of them uniformly nonpretentious. For all fixed integers
$a_1,a_2\ge1$ and $b_1,b_2\ge0$ with $a_1b_2-a_2b_1\ne0$,

$$
\frac1N\sum_{n=1}^Nf_1(a_1n+b_1)f_2(a_2n+b_2)\to0
\qquad(N\to\infty).
$$

The proof remarks (p. 84) that zero intercepts and coefficients with common
factors are included. By Lemma 18.5 and the closing paragraph of Section 18
(pp. 85--86) the corollary applies to every pair $f_1,f_2\in\{\lambda,\mu\}$.
For $f_1=f_2=\lambda$ it recovers, without a rate, the conclusion of
[[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/theorem_1_1|Theorem 1.1]];
the text says that with a Möbius factor it gives convergence without a rate.

**Source.** OpenAI, *Ordinary two-point correlations of multiplicative
functions*, release folder
`preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026`;
TeX file `build/introduction.tex`, label `cor:affine` (lines 81--89), PDF p. 4.
The proof is in Section 18.2 (`build/qualitative/affine-corollaries.tex`, lines
216--258, PDF p. 84). Read 2026-10-12. Provenance and attestations are on
[[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/_index|the card]].

**Read depth.** Claims checked: the statement, and the statements of the Lemmas
numbered 18.1--18.3, Proposition 18.4 and Lemma 18.5, were read clause by clause
in the TeX source. The proof was read for its structure only; no step was
checked. Nothing here is independently reviewed.

## Proof pointer

The corollary is deduced from
[[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/proposition_18_4|Proposition 18.4]],
the progression form of Theorem 1.2, without assuming complete
multiplicativity. Zero factors are trivial. Put $l=a_1a_2$,
$c_0=\min(a_2b_1,a_1b_2)$ and $h=|a_1b_2-a_2b_1|$, and for an integer $a\ge1$
let $F_{a,f}(m)$ be $f(m/a)$ when $a\mid m$ and $0$ otherwise. With $U,V$ the
dilates $F_{a_2,f_1}$ and $F_{a_1,f_2}$, in the order fixed by the sign of
$a_1b_2-a_2b_1$, one has the exact identity
$U(ln+c_0)V(ln+c_0+h)=f_1(a_1n+b_1)f_2(a_2n+b_2)$. Lemma 18.2 writes each
dilate as a signed sum of $2^{\omega(a)}$ normalized multiplicative functions,
built prime by prime from local factors, that agree with the original function
at every prime power coprime to $a$; by Lemma 12.1 each component inherits
uniform nonpretentiousness from the original factor. Proposition 18.4, applied
to each pair of components with shifts $0$ and $h$ and the class
$c_0\bmod l$, makes the average of $U(m)V(m+h)$ over $m\equiv c_0\pmod l$ tend
to zero, and the integers $m=ln+c_0$, $1\le n\le N$, are exactly that class in
$(c_0,lN+c_0]$, which gives the corollary after an initial segment of at most
$c_0$ terms.

## Dependencies

Theorem 1.2 through Proposition 18.4, and Lemmas 12.1 and 18.1--18.3 of the
same manuscript, all proved in the text. For the Liouville and Möbius cases,
Lemma 18.5 uses Lemma C.1 of Matomäki, Radziwiłł and Tao and the prime number
theorem in progressions. None was checked here.

## Bears on

No problem page is identified as using this result; the manuscript names no
Erdős problem.
