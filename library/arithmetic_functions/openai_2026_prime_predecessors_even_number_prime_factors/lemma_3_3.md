---
name: arithmetic_functions/openai_2026_prime_predecessors_even_number_prime_factors/lemma_3_3
title: "Lemma 3.3: logarithmic phases on progressions, saving exp(-log x/(log log x)^C3) up to height 4x^3"
desc: |
  Sums of n^(iv) over an arithmetic progression of modulus at most a power of
  log x in an interval inside [N',2N'], exp(log x/(log log x)^2) <= N' <=
  2x^5, save exp(-log x/(log log x)^C3) for heights
  exp(log x/(2(log log x)^2)) <= |v| <= 4x^3; it feeds Lemma 3.1, and the
  release's Artin-conjecture manuscript cites it. Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

Throughout, $x$ is the large parameter, $L=\log x$ and $T=\log L$ (p. 2).

**Lemma 3.3.** Fix $C>0$. There is an absolute constant $C_3>0$ such that,
once $x$ is large enough in terms of $C$, the bound

$$
\Big|\sum_{\substack{n\in I\\ n\equiv a\ (\mathrm{mod}\ q)}}n^{iv}\Big|
\ll\frac{N'}{q}\exp\!\big(-L/T^{C_3}\big)
$$

holds uniformly for all real $N'$, positive integers $q$ and real $v$ with

$$
\exp(L/T^2)\le N'\le2x^5,\qquad q\le L^C,\qquad
\exp\!\big(L/(2T^2)\big)\le|v|\le4x^3,
$$

every residue class $a$ modulo $q$ and every interval $I\subset[N',2N']$.
The residue class need not be coprime to $q$. The exponent $C_3$ is
absolute; the implied constant is written without a subscript, and by the
convention of Section 2 it may depend on the fixed $C$ (p. 2).

The trivial bound is of order $N'/q$, so the saving
$\exp(-L/T^{C_3})$ is smaller than every fixed power of $1/L$. The lower
limit on $|v|$ is far above any power of $L$; this lemma alone does not
cover the moderate heights.

**Source.** OpenAI, *Prime Predecessors with an Even Number of Prime
Factors*, release folder
`preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026`;
TeX file `build/sections/02-long-prime.tex`, label `lp:log-phase` (lines
185--197), PDF p. 7; the proof is at lines 199--310 (PDF pp. 7--8). Read
2026-10-12. Provenance and attestations are on
[[arithmetic_functions/openai_2026_prime_predecessors_even_number_prime_factors/_index|the card]].

**Read depth.** Claims checked: the statement, with the conventions of
Section 2 (`build/sections/01-preliminaries.tex` lines 3--17), was read
clause by clause in the TeX source, and the statement of Lemma 3.2 (lines
48--55) was read as a statement. The proof was read for its structure only,
and no step was checked. Nothing here is independently reviewed.

## Proof pointer

Put $H=N'/q$ and $y=\log|v|/\log H$; the ranges give $\log H\gg L/T^2$ and
$y\ll T^2$. Writing $n=q(b+a/q)$ turns the sum into a sum of
$(b+a/q)^{iv}$ over an interval of integers $b$ with $H\le b+a/q\le2H$.

If $y<4/5$, the phase has a monotone derivative of size about $|v|/H<1/2$,
and the first derivative test (Proposition 2.3) bounds the sum by
$O(H/|v|)$, which the lower bound on $|v|$ makes small enough.

If $y\ge4/5$, take $M=\lfloor H^{3/4}\rfloor$ and degree
$k=\lceil4y+8\rceil$, so $k\ll T^2$. Averaging over shifts $1\le h\le M$
costs $O(M)$, and Taylor expansion of $v\log(b+h+a/q)$ in $h$ to degree $k$
has remainder $O(H^{-2})$ uniformly in the growing degree. The sum is thus
bounded by an average over $b$ of Weyl sums $S(\boldsymbol\alpha(b))$ of
degree $k$ and length $M$. The coefficient vectors $\boldsymbol\alpha(b)$
fall at most $\exp(O(k))H^{4/5}$ times into any box with side $M^{-j}$ in
coordinate $j$, by monotonicity of one well-chosen coordinate. A bound for
the suprema of $|S|^{2s}$ over boxes reduces the box sum to $J_{s,k}(M)$, and
Hölder's inequality with Lemma 3.2 (with $s\ll T^8$) gives the saving
$\exp(-c_1L/T^{10})$; increasing the exponent to $C_3>10$ absorbs $c_1$.

## Dependencies

Proved in the manuscript: Lemma 3.2, the degree-uniform Vinogradov
mean-value bound, by Linnik's $p$-adic iteration (Wooley 2012, Section 2,
cited for an exposition). Used at statement level: the first derivative test
of Proposition 2.3, recorded in the form of the companion S. None was checked
here. The Poisson--Dirichlet companion
([[arithmetic_functions/openai_2026_poisson_dirichlet_law_prime_predecessors/_index|card]])
states the same estimate in the same ranges as its Lemma 2.4 and proves it in
its own Appendix A; that proof was not read or compared.

Uses in the release. Within this manuscript, Lemma 3.3 bounds the long part
of the truncated Dirichlet series in Lemma 3.4, and so enters
[[arithmetic_functions/openai_2026_prime_predecessors_even_number_prime_factors/lemma_3_1|Lemma 3.1]].
The Artin-conjecture manuscript
([[integer_sequences/openai_2026_primitive_roots_admissible_integer_base/_index|card]])
cites it as "valid for arbitrary residue classes and subintervals" (its
`sections/08-type-ii.tex` lines 499--502, PDF p. 69), for the range
$\exp(L/(\log L)^2)\le|u|<x^2$ of the high-frequency bound on its comparison
weight in the proof of its Proposition 10.3.

## Bears on

No problem page is identified as using this lemma. It reaches problem pages
only through the Artin manuscript's Theorem 1.1, whose card records its own
rows.
