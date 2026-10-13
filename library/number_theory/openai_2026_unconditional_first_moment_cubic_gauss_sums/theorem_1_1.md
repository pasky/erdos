---
name: number_theory/openai_2026_unconditional_first_moment_cubic_gauss_sums/theorem_1_1
title: "Theorem 1.1: the first moment of normalized cubic Gauss sums over all primary primes of Z[omega] is asymptotic to (6/5)c_* X^{5/6}/log X"
desc: |
  The manuscript's main claim: unconditionally and with a sharp cutoff, the
  normalized cubic Gauss sums over primary primes of Z[omega] of norm at most
  X sum to (6/5)c_* X^{5/6}/log X + o(X^{5/6}/log X), Patterson's first-moment
  conjecture in this normalization. Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

Let $\omega=e^{2\pi i/3}$ and $\mathcal O=\mathbb Z[\omega]$, and write
$N(z)=|z|^2$, $\operatorname{Tr}(z)=z+\bar z$ and $e(x)=e^{2\pi ix}$. An
element of $\mathcal O$ prime to $3$ is primary when it is congruent to $1$
modulo $3$; every ideal prime to $3$ has exactly one primary generator. The
primary primes therefore comprise both conjugate primes above each rational
prime $p\equiv1\pmod 3$ and, for each rational prime $q\equiv2\pmod 3$, the
element $-q$ of norm $q^2$; the prime above $3$ is not primary. For a primary
prime $\pi$ and $v\in\mathcal O$, the cubic residue symbol $\chi_\pi(v)$ is
the element of $\{1,\omega,\omega^2\}$ congruent to $v^{(N\pi-1)/3}$ modulo
$\pi$ when $\pi\nmid v$, and $0$ otherwise; it is extended multiplicatively in
the primary denominator. For primary $b$ the normalized cubic Gauss sum is
$$
G(b)=\frac1{\sqrt{N(b)}}
\sum_{v\bmod b}\chi_b(v)\,e\bigl(\operatorname{Tr}(v/b)\bigr),
\qquad
c_*=\frac{(2\pi)^{2/3}}{3\Gamma(2/3)}
$$
(equation (1.1), p. 1). For a primary prime, $|G(\pi)|=1$.

**Theorem 1.1.** As $X\to\infty$,
$$
\sum_{\substack{\pi\ \text{primary prime}\\ N\pi\le X}}G(\pi)
=\frac65\,c_*\,\frac{X^{5/6}}{\log X}+o\Bigl(\frac{X^{5/6}}{\log X}\Bigr).
$$

The cutoff $N\pi\le X$ is sharp, no smoothing weight is present, and no
hypothesis such as GRH is assumed. The error is stated only as little-oh,
with no rate. Partial
summation turns the theorem into the weighted form
$\sum_{N\pi\le X}G(\pi)\log N\pi=\frac65c_*X^{5/6}+o(X^{5/6})$ (equation
(1.3)).

The manuscript identifies the theorem with the all-primary-prime asymptotic
displayed after Equation (1.8) of Dunn and Radziwiłł (arXiv version 3), and
reads it as a positive answer to Patterson's first-moment conjecture in that
normalization. It converts to Kummer's sums $S_p=\sum_{x\bmod p}e(x^3/p)$
through $G(\pi)+G(\bar\pi)=S_p/\sqrt p$ for $p=\pi\bar\pi\equiv1\pmod3$
(equation (1.4)); since the inert primes contribute $O(\sqrt X)$, it obtains
$$
\sum_{\substack{p\le X\\ p\equiv1\ (3)}}\frac{S_p}{2\sqrt p}
\sim\frac35\,c_*\,\frac{X^{5/6}}{\log X}
=\frac{(2\pi)^{2/3}}{5\Gamma(2/3)}\frac{X^{5/6}}{\log X}
$$
(equation (1.5), p. 3), which it says is exactly the coefficient of Wan's
Conjecture 4.13. Remark 1.2 (p. 3) records that the cited version of Dunn
and Radziwiłł prints $\frac65c_*$ both in a rational-prime conjecture with
summand $S_p/(2\sqrt p)$ and in the all-primary-prime display, which (1.4)
makes incompatible; the manuscript proves the all-primary-prime display and
says it does not decide which printed coefficient is authoritative. Neither
cited source was read for this page.

The release's comparator file
`lean/ComparatorChallenges/PattersonFirstMoment.lean`
states this theorem as `patterson_firstMoment`; the card's Formalization
paragraph records what was read of it, and nothing was built or audited here.

**Source.** OpenAI, *An unconditional first moment for cubic Gauss sums*,
release folder
`preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026`;
TeX file `build/paper.tex`, label `thm:main` (lines 64--72), PDF p. 1, with the
definitions at lines 50--62, the weighted form (1.3) at lines 84--92 and the
conversion and Remark 1.2 at lines 151--192 (PDF pp. 2--3); the proof closes in
Section 7.5 (`build/sections/perron.tex` lines 412--543, PDF pp. 40--41).
Provenance and attestations are on
[[number_theory/openai_2026_unconditional_first_moment_cubic_gauss_sums/_index|the card]].

**Read depth.** Claims checked: the statement, the definitions (1.1) it rests
on, the weighted form (1.3), the conversion (1.4)--(1.5) and Remark 1.2 were
read clause by clause in the TeX source. The proof, Sections 2--7 (PDF
pp. 4--41), was read for its structure only, as summarized below; no step
was checked. Nothing here is independently reviewed.

## Proof pointer

The target is a comparison, on each dyadic range $X<N\pi\le2X$, of $G(\pi)$ with
the model $c_*N(\pi)^{-1/6}$ (equation (7.12)); the prime ideal theorem and
partial summation then turn the model's sum into $\frac65c_*X^{5/6}/\log X$.
Both the Gauss sum and the model vanish off squarefree arguments. Lemma 7.3
replaces the sharp interval by a smooth weight times a Fourier integral
truncated at height $T_{\max}=X^{1/6+\rho}$, at a cost
$X^\epsilon(1+X/T_{\max})$, which is $o(X^{5/6}/\log X)$. The heights are then
treated in ranges.

At low heights, $|t|\le(\log X)^{C_t}$, Proposition 6.1 decomposes the prime sum
exactly, with the same coefficients for the Gauss sum and the model, into
polylogarithmically many Type I terms (outer length at most $X^{0.40}$),
bilinear terms (shorter side $B$ between a constant times $X^{1/3}$ and
$\sqrt X$, with prime-convolution coefficients when $B>X^{0.40}$), sparse terms
with a power saving, and a three-prime transition with all three primes near
$X^{1/3}$. The Type I terms are compared with the model by Proposition 3.1,
which inverts the cube completion in Dunn and Radziwiłł's level Voronoi formula
(Theorem 2.4) and bounds the discarded cube divisors by counting or by
Heath-Brown's cubic large sieve, saving $X^{-1/100}$. The bilinear terms go
through Proposition 7.1, which applies Cauchy's inequality and the corrected
dispersion estimate of Proposition 5.1: after Poisson summation the cube
frequencies reproduce exactly the square of the model, the mixed term is matched
to it by Proposition 3.1, so the three main terms cancel, and the remaining
frequencies are bounded by large sieves, or at small conductors by the
Siegel--Walfisz property (SW) of the coefficients, except in two
large-conductor configurations at $B\approx X^{1/2}$, where Proposition 4.1
supplies a power saving for prime-convolution coefficients by moments of
several lengths and an off-diagonal Gram estimate. The three-prime transition
is bounded by $X^{5/6}(\log X)^{-3/2}$ per configuration through the
uncorrected dispersion estimate, which beats the $O((1+\log\log X)^{C})$
configurations.

At heights from $(\log X)^{C_t}$ to $X^{1/6+\rho}$ the model is discarded before
decomposing, by the mean-value inequality, which gives a factor $T^{-1/2}$. For
the Gauss sum alone, Type I terms are bounded by Proposition 3.2 through
Heath-Brown's metaplectic mean square (Theorem 2.5), with outer length at most
$X^{0.40}$ on ordinary blocks and $X^{1/3-\kappa/2}$ on upper blocks,
$T\gg X^{0.01}$. Bilinear terms are bounded by Proposition 7.2: for $B>X^{0.40}$
the averaged dispersion diagonal saves a power; for smaller $B$ both norm
variables are cut into cells of logarithmic width $1/J$, cell pairs near the
product boundary gain $J^{-1/2}$ from the localized diagonal, and far pairs gain
from integration by parts in the height. Sections 7.2--7.3 fix the order of the
constants, starting from $\gamma<10^{-3}$, $\kappa<\gamma/100$ and
$\rho<\kappa/100$, so that no choice depends on a later one. Summing the pieces
and the $O(\log X)$ height blocks gives (7.12), and dyadic summation gives the
theorem.

## Dependencies

External inputs, taken at statement level; none was checked here. Dunn and
Radziwiłł's level Voronoi formula (arXiv version 3, Proposition 5.3, with
equations (5.7), (5.13)--(5.14), (5.74) and (5.79)--(5.81)), which the
manuscript says is unconditional, their Proposition 5.2 for the continuation of
$\sum_uG(ru)(Nu)^{-s}$, and their recorded forms of cubic reciprocity and its
supplementary laws (Section 2); the dispersion mechanism of their Section 9
guides Section 5. Heath-Brown's cubic large sieve (Theorem 2 of the Kummer
paper) and his metaplectic mean square (Section 3, Lemma 3, with Lemma 1 and
equation (19) for the growth bounds). The Hecke functional equation in Watkins's
completion (Section 3.6) and entireness from Thorner and Zaman (Section 2C); a
Siegel--Walfisz bound for cubic Hecke characters of polylogarithmic conductor,
derived from Thorner and Zaman's Theorem 1.4; the prime ideal theorem for
$\mathbb Q(\omega)$; the Montgomery--Vaughan mean-value inequality; and the
Bombieri--Halász--Montgomery inequality in Harcos's note. The ordinary character
large sieve (Lemma 2.2) and the extensions of the cubic large sieve (Lemma 2.3)
are proved in the text, the former compared with Huxley and with Gao and Zhao.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using this theorem.
