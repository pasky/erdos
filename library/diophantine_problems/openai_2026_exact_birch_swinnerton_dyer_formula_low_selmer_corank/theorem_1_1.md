---
name: diophantine_problems/openai_2026_exact_birch_swinnerton_dyer_formula_low_selmer_corank/theorem_1_1
title: "Theorem 1.1: Selmer corank 0 or 1 at one prime gives the exact Birch–Swinnerton-Dyer formula"
desc: |
  The claimed full Birch-Swinnerton-Dyer leading-term formula, with rank equal
  to the Selmer corank and finite Sha, for every elliptic curve over Q whose
  q-power Selmer group has corank 0 or 1 at some prime q. Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

Let $E/\mathbb Q$ be an elliptic curve. For a prime $p$, the manuscript takes
$\mathrm{Sel}_{p^\infty}(E/\mathbb Q)$ to be the full $p$-power Selmer group,
cut out by the local Kummer images at every place, and writes $s_p(E)$ for its
$\mathbb Z_p$-corank, $a(E)=\operatorname{ord}_{s=1}L(E,s)$ for the uncompleted
Hasse--Weil $L$-function with all its finite Euler factors (center $s=1$), and
$r(E)=\operatorname{rank}E(\mathbb Q)$; $\mathrm{Sha}(E/\mathbb Q)$ is the
kernel of $H^1(\mathbb Q,E)\to\prod_vH^1(\mathbb Q_v,E)$.

The normalizations are fixed before the theorem (p. 3). Let $\omega_E$ be the
Néron differential of a global minimal Weierstrass equation. The real period
is $\Omega_E=\int_{E(\mathbb R)}|\omega_E|$, taken over the whole real locus
(both components when there are two), with no separate component factor; the
Tamagawa numbers are $c_\ell(E)=[E(\mathbb Q_\ell):E_0(\mathbb Q_\ell)]$. For
$x(P)=a/b$ in lowest terms with $b>0$ put $h_x(P)=\log\max\{|a|,b\}$ and
$h_x(O)=0$; then $H(P)=\lim_{n\to\infty}4^{-n}h_x([2^n]P)$ and
$B(P,Q)=\tfrac12\bigl(H(P+Q)-H(P)-H(Q)\bigr)$, so that $B(P,P)=H(P)$. The
regulator $\mathrm{Reg}_E$ is $\det(B(P_i,P_j))$ for a basis
$P_1,\dots,P_r$ of $E(\mathbb Q)/E(\mathbb Q)_{\rm tors}$, and $1$ in rank
zero.

**Theorem 1.1.** Let $q$ be any prime. If $s_q(E)\in\{0,1\}$, then
$r(E)=a(E)=s_q(E)$, the group $\mathrm{Sha}(E/\mathbb Q)$ is finite, and, with
$r=r(E)$,

$$
\frac{L^{(r)}(E,1)}{r!}
=\frac{\Omega_E\,\mathrm{Reg}_E\,\#\mathrm{Sha}(E/\mathbb Q)
\prod_{\ell}c_\ell(E)}{\#E(\mathbb Q)_{\rm tors}^{2}},
$$

the product running over all finite primes $\ell$. The theorem states that it
places no further hypothesis on the reduction type, rational torsion,
isogenies, complex multiplication or the residual Galois representations.

The paragraph after the theorem (p. 3) assigns the rank and finiteness
assertions to the Selmer converse and the $2$-adic part of the formula to the
two-primary companion (both imported, Section 2), and names as new "the exact
valuation of the leading-term formula at every odd prime, independently of
the prime $q$ in the hypothesis". It adds that the Selmer-corank hypothesis
"is not replaced here by a hypothesis on Mordell--Weil rank alone".

A reading noted here, not stated in the manuscript as a separate result: when
$a(E)\le1$, Theorem 2.3 (Gross--Zagier--Kolyvagin) gives $r(E)=a(E)$ and
finite $\mathrm{Sha}$, and the Kummer sequence then gives $s_p(E)=r(E)$ at
every prime $p$, so every curve of analytic rank $0$ or $1$ meets the
hypothesis at every $q$. Conversely the theorem's own conclusion gives
$a(E)\le1$, so its hypothesis picks out exactly the curves of analytic rank at
most one, the converse direction resting on the imported Theorem 2.1. The
manuscript takes the same Kummer step at $p=2$ in Section 1.3 and after
Theorem 2.3, and Proposition 10.4 states the odd-primary half for exactly these
curves.

**Source.** OpenAI, *Exact Birch--Swinnerton-Dyer Formula from Low Selmer
Corank*, release folder
`preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026`;
TeX file `build/sections/01-introduction.tex`, label `thm:main` (lines
47--62), with the normalizations at lines 12--45; PDF p. 3. The proof closes
at the end of Section 10 (`build/sections/10-center.tex` lines 254--271, PDF
p. 92). The label, lines and pages are the same in the October 3 version.
Read 2026-10-12. Provenance and attestations are on
[[diophantine_problems/openai_2026_exact_birch_swinnerton_dyer_formula_low_selmer_corank/_index|the card]].

**Read depth.** Claims checked: the statement and its normalizations, the
definitions of $Q_E$ and $X_p(E)$, and the statements of Theorems 2.1--2.3,
Proposition 2.4, Theorem 2.5, Lemma 2.6, Theorem 2.7, Proposition 2.8,
Proposition 5.11, Proposition 6.2, Corollary 6.9, Proposition 8.1, Theorem 9.6,
Proposition 10.1, Corollary 10.2, Lemma 10.3 and Proposition 10.4 were read
clause by clause in the TeX source. The closing assembly (lines 254--271) was
followed line by line; the argument behind Proposition 10.4, Sections 3--10, was
read for its structure only, as summarized below, and no step was checked.
Nothing here is independently reviewed.

## Proof pointer

The assembly (p. 92). Theorem 2.1, the imported Selmer converse applied at
$q$, gives $a(E)=r(E)=s_q(E)\in\{0,1\}$ and finite $\mathrm{Sha}$; the Kummer
sequence then gives $s_p(E)=r(E)$ at every $p$, so $s_2(E)\le1$. Theorem 2.2,
the imported two-primary formula, makes the BSD quotient
$Q_E=L^{(r)}(E,1)\,\#E(\mathbb Q)_{\rm tors}^2/(r!\,\Omega_E\mathrm{Reg}_E
\prod c_\ell(E))$ a positive rational number with
$v_2(Q_E)=v_2(\#\mathrm{Sha})$. Proposition 10.4, the manuscript's own
contribution, gives $v_p(Q_E)=v_p(\#\mathrm{Sha})$ at every odd $p$ for every
curve of analytic rank at most one, without reference to $q$. A positive
rational number with zero valuation at every prime is $1$, so
$Q_E=\#\mathrm{Sha}(E/\mathbb Q)$, which is the formula.

Proposition 10.4 combines two statements about the discrepancy
$X(E)=v_p(Q_E)-v_p(\#\mathrm{Sha}(E/\mathbb Q))$ at a fixed odd $p$: an
inequality $X(E)\ge0$ for non-CM curves of analytic rank at most one
(Proposition 5.11), and a pair identity $X(E)+X(E^D)=0$ for an imaginary
quadratic twist $E^D$ of complementary analytic rank chosen by Lemma 2.6
(Corollary 10.2, CM curves included). For a non-CM curve the twist is non-CM
too, so both discrepancies are nonnegative with sum zero. A CM curve of
analytic rank zero is handled by Lemma 10.3, which deduces exact BSD from
Burungale--Flach after an isogeny to a curve with CM by the maximal order and
a restriction-of-scalars descent; in analytic rank one its twist is a CM curve
of rank zero, and the pair identity finishes.

The inequality (Sections 3--5). Over $R=\mathbb Z_p[\![t,u_1,\dots,u_m]\!]$,
with $t$ cyclotomic and the $u_i$ tame variables from moving auxiliary primes
chosen in Section 4 so that the Selmer complex is a free line at the prime $(p)$
(Proposition 4.2), Kato-type Siegel-unit classes give a normalized coordinate
$U$ that is shown integral (Proposition 5.5) by that residual concentration,
horizontal line comparisons at characteristic-zero divisors and the removal of
smoothing and Euler divisors. Its central value is identified through the dual
exponential and the $L$-value in rank zero (Proposition 5.4) and through an
exact logarithm-and-height comparison in rank one (Proposition 5.7); integral
Poitou--Tate and the local Haar identities (Lemma 3.7) turn $v_p(U(0))$ into
$X(E)$, giving $X(E)=v_p(U(0))\ge0$ (Proposition 5.11).

The pair identity (Sections 2 and 6--10). Over $K=\mathbb Q(\sqrt D)$, where $p$
splits as $w\bar w$, Proposition 2.8 combines the split Gross--Zagier formula
(Theorem 2.7) with restriction of scalars and isogeny invariance to write
$X(E)+X(E^D)$ as
$2(n_P+\tau_g)-2v_p(c_E)-2\sum_\ell v_p(c_\ell(E))-v_p(\#\mathrm{Sha}(E/K))$,
where $n_P$ is the $p$-adic valuation of the index of the Heegner trace $P_K$ in
$E(K)/E(K)_{\rm tors}$ and $\tau_g$ that of $\#E(K)_{\rm tors}$. To evaluate the
right side, the manuscript compares the determinant $L_w$ of the Selmer complex
strict at $w$ and full at $\bar w$ with an analytic series $B_w$ built from
bounded CM measures attached to an integral primitive of the newform on the
ordinary locus, whose central value is $\pm c_E^{-2}\log_{\omega_E}(P_K)^2$
times Euler factors (Proposition 6.2). The quotient $U_w=B_w/L_w$ is integral
and prime to $p$ (Corollary 6.9), from divisibility at high finite characters
(Proposition 6.6), integral division (Lemma 3.9) and vertical primitivity
$p\nmid B_w$ (Proposition 6.5). A remaining horizontal divisor of $U_w$ would be
a zero of the undepleted series; there the theta congruences on a unitary group
of signature $(3,1)$ (Section 7) and the extraction of a Galois class
(Section 8) give the theta implication (Proposition 8.1), a nonzero one-sided
Selmer group for $E$ or its companion twist, and Section 9 adds tame directions
so that such simultaneous jumps have codimension at least two (Proposition 9.5);
hence $U_w$ is a unit (Theorem 9.6). Specializing at the center and computing
the determinant on the full Kummer lattice (Lemmas 3.6--3.8) gives
Proposition 10.1, $2(n_P+\tau_g)=s_K+2v_p(c_E)+2\sum_qv_p(c_q(E))$, which makes
the right side of Proposition 2.8 vanish.

## Dependencies

Imported release results, all unreviewed: Theorem 2.1 is Theorem 1.1 of the
Selmer converse,
[[diophantine_problems/openai_2026_selmer_converse_elliptic_curves_at_prime/theorem_1_1|its result page]]
(claims checked there, on the September 24 version, whose TeX differs from the
October 7 version cited here only in its date and one citation link); Theorem
2.2 is Theorem 1.1 of the two-primary companion, *The two-primary
Birch--Swinnerton-Dyer formula in Selmer corank at most one*; Theorem 2.5 is
Theorem 1.2 of *Goldfeld's analytic density conjecture and the $2$-converse for
elliptic curves*, whose proof this manuscript's introduction says uses Smith's
Selmer-distribution results. Sections 2, 4, 7 and 8 also reuse the Selmer
converse's constructions (its Sections 2 and 4--9, by section, lemma and
equation number), and Sections 2--6 adapt the two-primary companion's. External
inputs: modularity (Wiles; Taylor--Wiles; Breuil--Conrad--Diamond--Taylor);
Gross--Zagier (Chapters I and V) and Kolyvagin; Cassels and Milne for isogeny
invariance and restriction of scalars; Kato's Euler system (his Theorems 9.5
and 13.5(2) and Proposition 3.11(1)); Burungale--Flach (Theorem 1.1, Corollaries
1 and 2) for CM curves of analytic rank zero; Serre's open image theorem and
Bogomolov; Chai's 2003 preprint on ordinary families, Hida's $\mu$-invariant
paper (Proposition 3.11, Corollary 3.13) and Zarhin (Theorems 1.2 and 1.4) for
vertical primitivity; Manin and Drinfeld, Deligne--Rapoport and Katz--Mazur for
the modular curves; Yamana, Gan--Qiu--Takeda, Waldspurger and Godement--Jacquet
for the theta comparison; the Selmer-complex and duality framework of
Bloch--Kato, Milne and Nekovář. External premises are taken at statement level;
none was checked here.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using this theorem; the
[[diophantine_problems/openai_2026_exact_birch_swinnerton_dyer_formula_low_selmer_corank/_index|card]]
records the pages that were checked.
