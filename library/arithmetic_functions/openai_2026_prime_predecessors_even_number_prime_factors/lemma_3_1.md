---
name: arithmetic_functions/openai_2026_prime_predecessors_even_number_prime_factors/lemma_3_1
title: "Lemma 3.1: long prime polynomial, saving any power of log x for (log x)^B0 <= |t| <= x^2"
desc: |
  Any fixed log-power saving in the sum of chi(p)p^(-1+it) over primes in an
  interval inside [N,2N], x^tau/2 <= N <= x^eta, for characters of modulus at
  most a power of log x and (log x)^B0 <= |t| <= x^2; the release's
  Artin-conjecture manuscript cites it. Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

Throughout, $x$ is the large parameter, $L=\log x$, the letter $p$ runs over
primes, and Dirichlet characters need not be primitive; they are extended by
zero on integers not coprime to the modulus (pp. 2 and 8).

**Lemma 3.1.** Fix $0<\tau<\eta<1$, $C>0$ and $A>0$. There is a constant
$B_0=B_0(\tau,\eta,C,A)$ such that

$$
\Big|\sum_{p\in I}\chi(p)\,p^{-1+it}\Big|\ll_{\tau,\eta,C,A}L^{-A},
$$

uniformly for every real $N$ with $x^\tau/2\le N\le x^\eta$, every modulus
$q\le L^C$, every Dirichlet character $\chi$ modulo $q$, every interval
$I\subset[N,2N]$ and every real $t$ with $L^{B_0}\le|t|\le x^2$.

The sum over a whole dyadic interval has trivial size of order
$1/\log N\asymp1/L$, so the lemma saves an arbitrary fixed power of $L$ (an
observation made here). Nothing is claimed for $|t|<L^{B_0}$, a range that
includes the small $|t|$ at which the principal character has a main term;
the upper limit $x^2$ is the height that the correlation argument of
Section 4 needs (p. 4). The manuscript's
conventions assert no effective threshold for $x$ (p. 2).

**Source.** OpenAI, *Prime Predecessors with an Even Number of Prime
Factors*, release folder
`preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026`;
TeX file `build/sections/02-long-prime.tex`, label `lp:prime-polynomial`
(lines 8--21), PDF p. 4; the proof is at lines 483--579 (PDF pp. 10--11),
after Lemmas 3.2--3.6 (lines 48--481, PDF pp. 5--10). Provenance and
attestations are on
[[arithmetic_functions/openai_2026_prime_predecessors_even_number_prime_factors/_index|the card]].

**Read depth.** Claims checked: the statement, with the conventions of
Section 2 (`build/sections/01-preliminaries.tex` lines 3--17) and the
paragraph on characters before Lemma 3.4 (`02-long-prime.tex` lines
312--323), was read clause by clause in the TeX source. The statements of
Lemmas 3.2 and 3.4--3.6 were read as statements; the proof and those lemmas'
proofs were read for their structure only, and no step was checked. Nothing
here is independently reviewed.

## Proof pointer

The route runs from a mean-value estimate to a zero-free strip at large
height and then to primes. Write $T=\log L$ and $D(s,\chi)$ for the Dirichlet
$L$-function.

Lemma 3.2 is a Vinogradov mean-value bound with explicit dependence on the
degree: absolute constants $C_1,C_2$ such that every $k\ge2$ has some $s$
with $k\le s\le C_1k^4$ and
$J_{s,k}(M)\le\exp(C_1k^{C_2})M^{2s-k(k+1)/2+1/100}$ for all $M\ge1$. It is
proved by Linnik's $p$-adic iteration, with auxiliary primes near $M^{1/k}$
supplied by the prime number theorem; each step cuts the excess exponent by
the factor $1-1/k$, and the constants are tracked through the $O(k\log 2k)$
steps. Lemma 3.2 feeds
[[arithmetic_functions/openai_2026_prime_predecessors_even_number_prime_factors/lemma_3_3|Lemma 3.3]],
a saving of $\exp(-L/T^{C_3})$ for sums of $n^{iv}$ over progressions at
heights from $\exp(L/(2T^2))$ to $4x^3$.

Lemma 3.4 bounds $\log|D(\sigma+iv,\chi)|\ll T^2$ for
$|\sigma-1|\le10T^4/L$ and $1/2\le|v|\le3x^3$: the Dirichlet series is
truncated by partial summation, and its long part is split into progressions
modulo $q$, where Lemma 3.3 applies. Lemma 3.5 uses Jensen's formula and
Blaschke factors on a disk of radius about $T^4/L$ to write $D'/D$ as a sum
over $O(T^2)$ nearby zeros plus an error $O(L/T^2)$. Lemma 3.6 combines this
with the inequality $3+4\cos\theta+\cos2\theta\ge0$ to exclude zeros from
$\operatorname{Re}s\ge1-cT^2/L$, $1\le|\operatorname{Im}s|\le x^3$, for every
modulus up to $L^C$, and to bound $|D'/D|\ll L$ on the thin strip
$1-cT^2/(2L)\le\operatorname{Re}s\le1+1/L$ at heights from $2$ to $x^3/2$.
The introduction calls this a weak strip. Since it starts at height $1$, it
says nothing about real exceptional zeros and needs no input on them (an
observation made here).

For Lemma 3.1 itself, the interval is smoothed at relative scale
$L^{-A-4}$, and the sum with weight $\Lambda(n)$ is written by Mellin
inversion as an integral of $-D'/D(1-it+z,\chi)$ against the transform of the
smoothing. The integral is truncated at $|\operatorname{Im}z|\le L^{C_5}$ and
shifted to $\operatorname{Re}z=-cT^2/(2L)$. Because $|t|\ge L^{B_0}$ with
$B_0>C_5+2$, the shifted contour stays at heights between $2$ and $x^3/2$,
where Lemma 3.6 applies and no pole is crossed, and on the new line
$|N^z|\ll\exp(-c\tau T^2/2)$, smaller than every fixed power of $1/L$.
Prime powers and the weight $\log p$ are then removed by trivial bounds and
partial summation.

## Dependencies

Proved in the manuscript: Lemmas 3.2--3.6. Used at statement level: the
prime number theorem of Proposition 2.1 (for the auxiliary primes of the
mean-value lemma) and the first derivative test of Proposition 2.3 (in the
proof of Lemma 3.3), both classical and recorded in the forms of the
companion S; Linnik's $p$-adic form of Vinogradov's mean-value method, with
Wooley (2012, Section 2,
pp. 1583--1585) cited for an exposition and the efficient congruencing
theorem not used. None was checked here.

The Poisson--Dirichlet companion
([[arithmetic_functions/openai_2026_poisson_dirichlet_law_prime_predecessors/_index|card]])
states the same estimate in the same ranges as its Lemma 2.3 and proves it in
its own Appendix A, where it calls the method classical and points to
stronger estimates of Ford (2002) and Khale (2024); that proof was not read
or compared.

Uses in the release. Within this manuscript, Lemma 3.1 bounds the long prime
polynomial in the proof of Theorem 4.1 at heights from a fixed power of $L$
up to below $x^2$ (PDF p. 21). The Artin-conjecture manuscript
([[integer_sequences/openai_2026_primitive_roots_admissible_integer_base/_index|card]])
applies it, after partial summation, in one prime slot of each box of the
prime-product sequence in the proof of its Proposition 10.3, for frequencies
$L^{B_0}\le|u|\le x^2$ (its `sections/08-type-ii.tex` line 456, PDF p. 69).

## Bears on

No problem page is identified as using this lemma. It reaches problem pages
only through the Artin manuscript's Theorem 1.1, whose card records its own
rows.
