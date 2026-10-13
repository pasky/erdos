---
name: arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/theorem_1_1
title: "Theorem 1.1: a power-of-logarithm saving for Liouville correlations along fixed affine forms"
desc: |
  The manuscript's quantitative claim: for fixed nonproportional affine forms
  the Liouville correlation sum up to X is O(X/(log X)^c) at every cutoff,
  with c absolute, its case n, n+h presented as the ordinary two-point Chowla
  conjecture. Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

Liouville's function is $\lambda(n)=(-1)^{\Omega(n)}$, where $\Omega(n)$ is
the number of prime factors of $n$ counted with multiplicity (p. 3). Two
affine forms $a_1n+b_1$ and $a_2n+b_2$, with integers $a_1,a_2\ge1$ and
$b_1,b_2\ge0$, are nonproportional when $a_1b_2\ne a_2b_1$.

**Theorem 1.1.** A single absolute exponent $c>0$ serves every pair of fixed
nonproportional affine forms, with no coprimality assumed among
$a_1,a_2,b_1,b_2$. For each such pair some constant $C_{a_1,a_2,b_1,b_2}$
bounds the Liouville correlation along the two forms at every real cutoff
$X\ge3$, not only at integers:

$$
\Bigl|\sum_{1\le n\le X}\lambda(a_1n+b_1)\lambda(a_2n+b_2)\Bigr|
\le C_{a_1,a_2,b_1,b_2}\,\frac{X}{(\log X)^c}.
$$

On p. 3 the manuscript adds that these constants "need not be effective" and
that nothing uniform is claimed when the coefficients grow with $X$. Its
headline case is $a_1=a_2=1$, $b_1=0$ and $b_2=h>0$, where the bound becomes
$\sum_{n\le X}\lambda(n)\lambda(n+h)=O_h(X/(\log X)^c)$ at every cutoff, with
no exceptional scales; the manuscript says this "resolves the ordinary
two-point Chowla conjecture, with a logarithmic saving". The proof yields
$c=\delta/(6WA)$, where $\delta=1/200$ and the absolute constants $A$ and $W$
are not computed (Section 8.4).

**Formalization.** The release's Lean page for the family describes a
formalization of this statement, with the comparator theorem
`OAI.OrdinaryTwoPointCorrelations.liouville_log_saving`. In words, it says
that some $c>0$ has this property: for all natural numbers $a_1,a_2\ge1$ and
$b_1,b_2$ with $a_1b_2\ne a_2b_1$ there is $C>0$ such that
$|\sum_{n=1}^{\lfloor X\rfloor}\lambda(a_1n+b_1)\lambda(a_2n+b_2)|$ is at
most $CX/(\log X)^c$ for every real $X\ge3$, with $\lambda$ taken from
Mathlib. It was read statically and not built or audited here, and the
catalog lists no entry for it at this revision (see the card).

**Source.** OpenAI, *Ordinary two-point correlations of multiplicative
functions*, release folder
`preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026`;
TeX file `build/introduction.tex`, label `thm:q-affine` (lines 20--34), PDF
p. 3. The proof is Section 9 (`build/quantitative/08-affine.tex`, lines
7--51, PDF pp. 43--44), from
[[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/proposition_2_1|Proposition 2.1]],
whose proof closes in Section 8.4 (`build/quantitative/07-spectral.tex`, lines
279--333, PDF pp. 42--43). Provenance and attestations are on
[[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/_index|the card]].

**Read depth.** Claims checked: the statement, the definition of $\lambda$ and
the statement of Proposition 2.1 were read clause by clause in the TeX
source. The deduction in Section 9 and the proof of Proposition 2.1 in
Sections 2--8 were read for their structure only; no step was checked.
Nothing here is independently reviewed.

## Proof pointer

The theorem is deduced from the progression estimate, Proposition 2.1. Put
$l=a_1a_2$, $c_0=\min(a_2b_1,a_1b_2)$ and $h=|a_1b_2-a_2b_1|$. Multiplying the
two arguments by $a_2$ and $a_1$ turns them into $ln+a_2b_1$ and $ln+a_1b_2$,
which are $ln+c_0$ and $ln+c_0+h$ in some order, so complete multiplicativity
gives
$\lambda(a_1n+b_1)\lambda(a_2n+b_2)=\lambda(l)\lambda(ln+c_0)\lambda(ln+c_0+h)$.
The integers $m\equiv c_0\pmod l$ with $c_0<m\le lX+c_0$ are exactly
$m=ln+c_0$ with $1\le n\le X$, so the affine sum equals $\lambda(l)$ times the
difference of the progression sums
$P(Y)=\sum_{m\le Y,\,m\equiv c_0\ (l)}\lambda(m)\lambda(m+h)$ at $Y=lX+c_0$
and $Y=c_0$. Proposition 2.1 applies to the class $c_0$ whatever
$\gcd(c_0,l)$ is, so the first is $\ll X/(\log X)^c$ with the same exponent,
and the second is at most $c_0$ in size.

Proposition 2.1 is proved in Sections 2--8 by a divisor-graph argument; its
page gives the outline. In brief, the progression average $F(X)$ is compared
with averages of dilated correlations $\lambda(n)\lambda(n+hqd)$ in which each
prime of the label $d$ enters through the centered factor
$\mathbf 1_{p\mid n}-1/p$; the centering errors are controlled by the
short-interval exponential-sum theorem of Matomäki, Radziwiłł and Tao, and the
centered sums by a high moment of a nonbacktracking operator on a weighted
divisor graph. The square-root dependence of that moment on the reciprocal
mass $W$ of each prime supply, against the full mass $W^J$ in the
normalization, gives a saving $e^{-J}$ with $J\asymp\log\log X$, which is a
power of $\log X$.

## Dependencies

Proposition 2.1 of the same manuscript, and through it the external inputs
listed on its page: Theorem 1.3 of Matomäki, Radziwiłł and Tao, Braverman's
bounded-independence theorem, and the prime number theorem modulo $5$. None
was checked here.

## Bears on

No problem page is identified as using this result; the manuscript names no
Erdős problem.
