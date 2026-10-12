---
name: arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/proposition_18_4
title: "Proposition 18.4: ordinary Elliott cancellation on fixed residue classes"
desc: |
  The progression form of the qualitative claim: under the hypotheses of
  Theorem 1.2, the ordinary average of f_1(n+h_1)f_2(n+h_2) over n in any fixed
  class b mod l, unit or not, tends to zero through all real cutoffs. Claims
  checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

Multiplicative functions $f:\mathbb N\to\mathbb D$ and uniform
nonpretentiousness are as on the page for
[[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/theorem_1_2|Theorem 1.2]].

**Proposition 18.4.** Let $f_1,f_2:\mathbb N\to\mathbb D$ be multiplicative, at
least one of them uniformly nonpretentious. For fixed distinct nonnegative
integers $h_1,h_2$, an integer $l\ge1$ and any integer $b$,

$$
\frac1X\sum_{1\le n\le X}f_1(n+h_1)f_2(n+h_2)\,
\mathbf 1_{n\equiv b\ (\mathrm{mod}\ l)}\to0
\qquad(X\to\infty),
$$

the limit taken through all real $X$; residue classes that are not units are
included.

The introduction refers to this statement (p. 4) as the precise form of the
progression restriction permitted in Theorem 1.2. With
$f_1=f_2=\lambda$ it gives, without a rate, the conclusion of
[[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/proposition_2_1|Proposition 2.1]]
(p. 86), and by the closing paragraph of Section 18 it holds for every pair
$f_1,f_2\in\{\lambda,\mu\}$.

**Source.** OpenAI, *Ordinary two-point correlations of multiplicative
functions*, release folder
`preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026`;
TeX file `build/qualitative/affine-corollaries.tex`, label
`prop:affine-progression` (lines 181--194), PDF p. 84; the proof follows at
lines 196--214, on the same page. Read 2026-10-12. Provenance and attestations
are on
[[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/_index|the card]].

**Read depth.** Claims checked: the statement, and the statements of the Lemmas
numbered 18.1--18.3 on which the proof rests, were read clause by clause in the
TeX source. The proof was read for its structure only; no step was checked.
Nothing here is independently reviewed.

## Proof pointer

The residue condition is moved onto the argument of the nonpretentious factor
and expanded into multiplicative functions. Choose $j$ with $f_j$ uniformly
nonpretentious and write the condition as $n+h_j\equiv b+h_j\pmod l$. Lemma 18.3
expresses the indicator of a class $b'\bmod l$, with $d=\gcd(b',l)$ and $q=l/d$,
as an average over the Dirichlet characters $\chi$ modulo $q$ of
$\overline{\chi(b'/d)}$ times the dilate $m\mapsto\chi(m/d)\mathbf 1_{d\mid m}$,
and Lemma 18.2 writes each dilate as a signed sum of $2^{\omega(d)}$ normalized
multiplicative functions that agree with $\chi$ at prime powers coprime to $d$;
the case of a nonunit class, including the zero class, is handled by the same
formula. Multiplying each component by $f_j$ gives a multiplicative function
that agrees with $f_j\chi$ off a finite set of primes, and Lemma 18.1 shows it
is uniformly nonpretentious, since a twist by a fixed character and finitely
many prime changes move the squared distance by a bounded amount. Theorem 1.2,
applied to each such product at shift $h_j$ together with the other factor at
its own shift, and summed over the finitely many terms, gives the limit through
integers; passing to real $X$ changes the average by at most $1/X$.

## Dependencies

Theorem 1.2 and Lemmas 18.1--18.3 of the same manuscript, proved in the text;
Lemma 18.1 extends Lemma 12.1. Dirichlet character orthogonality on
$(\mathbb Z/q\mathbb Z)^\times$. None was checked here.

## Bears on

No problem page is identified as using this result; the manuscript names no
Erdős problem.
