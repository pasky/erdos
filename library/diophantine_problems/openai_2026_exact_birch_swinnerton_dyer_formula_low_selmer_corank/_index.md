---
name: diophantine_problems/openai_2026_exact_birch_swinnerton_dyer_formula_low_selmer_corank
desc: |
  A 94-page release manuscript claiming the full Birch-Swinnerton-Dyer
  leading-term formula for every elliptic curve over Q whose q-power Selmer
  group has corank 0 or 1 at some prime q, by an integral comparison at each
  odd prime; the rank, finiteness and 2-primary parts are imported from two
  companion manuscripts, and it names no Erdős problem.
license: Apache-2.0
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

# diophantine_problems/openai_2026_exact_birch_swinnerton_dyer_formula_low_selmer_corank

[[diophantine_problems/_index|..]]

[[diophantine_problems/openai_2026_exact_birch_swinnerton_dyer_formula_low_selmer_corank/theorem_1_1|theorem_1_1]]: The claimed full Birch-Swinnerton-Dyer leading-term formula, with rank equal
to the Selmer corank and finite Sha, for every elliptic curve over Q whose
q-power Selmer group has corank 0 or 1 at some prime q. Claims checked only.

***

OpenAI, *Exact Birch--Swinnerton-Dyer Formula from Low Selmer Corank*, OpenAI
Math Release preprint, October 7, 2026. Released under the Apache License 2.0 at
<https://github.com/openai/math> (revision fd4aeeb2e), folder
`preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026`;
the held PDF, `exact-bsd-low-selmer-corank.pdf` in the release, is retained as
[openai_2026_exact_birch_swinnerton_dyer_formula_low_selmer_corank.pdf](openai_2026_exact_birch_swinnerton_dyer_formula_low_selmer_corank.pdf),
and the release's TeX bundle in that folder (under `build/`) is the TeX source
cited on this card. The license term was read in the release's root `LICENSE`
file at that revision on 2026-10-12.

```bibtex
@misc{OAI:Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026,
  author = {{OpenAI}},
  title = {{Exact Birch--Swinnerton-Dyer Formula from Low Selmer Corank}},
  howpublished = {OpenAI Math Release preprint
                  \href{https://github.com/openai/math/blob/main/preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/exact-bsd-low-selmer-corank.pdf}{OAI:Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026}},
  year = {2026}
}
```

The held PDF has 94 pages with a text layer; its title page is dated October
7, 2026 and its metadata records a creation date of 6 October 2026 (21:50
at UTC offset −07:00). The printed page numbers equal the PDF page numbers.
The TeX source is `build/main.tex` (82 lines), which inputs ten section files
`build/sections/01-introduction.tex` to `10-center.tex` (7,190 lines
together) and the bibliography `build/references.tex` (230 lines, 34
entries): 7,502 lines in 12 files.

**Attestation.** The release README states that the repository's manuscripts
were "produced by an internal OpenAI model", that "Some outputs build upon
earlier results produced by the models", that the collection "includes results
at different stages of verification", that "Not all have accompanying Lean
formalizations" and that "Some of the unformalized results could have issues".
Its account of the method says that the vast majority of results came from
one fixed procedure and names two exceptions, work on a zero-free region for
the Riemann zeta function and on the Hodge conjecture for CM abelian
varieties; neither concerns this family. The manuscript's own README carries
the title, the author line "OpenAI", the date, the citation block above and a
version note saying that this version "removes an obsolete supporting
citation and updates citations to revised manuscripts in this collection"; it
says nothing about authorship or assistance. The title page names OpenAI as
the sole author, and the TeX source carries no statement on how the
manuscript was produced. These are the source's own statements, recorded as
attestations and not as this corpus's review. No refereed publication, arXiv
version or independent review of the manuscript is recorded here and nothing
on this card is independently reviewed.

**Formalization.** The release lists no formalization of this manuscript: its
Lean catalog `lean/formalization.yaml` at revision fd4aeeb2e has no entry for
it, and there is no page `lean/docs/002.md` for its family.

**Companions.** The release's family "The full BSD formula from low Selmer
corank" groups this manuscript with two others, both of which it cites as
inputs. *The Selmer converse for elliptic curves at every prime* (October 7,
2026, revising a September 24, 2026 version) supplies, as its Theorem 1.1, the
rank and finiteness half of Theorem 1.1 here (imported as Theorem 2.1), and
Sections 2, 4, 7 and 8 here reuse its auxiliary fields, anticyclotomic
character, theta, cusp-lifting and Galois-extraction constructions, cited by
section, lemma and equation number. It is filed at
[[diophantine_problems/openai_2026_selmer_converse_elliptic_curves_at_prime/_index|the Selmer-converse card]],
which holds the September 24 version; the manuscript README of the October 7
version, the one cited here, says only that it "updates a citation to a revised
manuscript in this collection", and a line comparison of the two TeX bundles at
revision fd4aeeb2e finds only the date and the link of the cited Goldfeld
manuscript changed, so the theorem, section, lemma and equation numbers cited
here are the same in both. *The two-primary Birch--Swinnerton-Dyer formula in
Selmer corank at most one* (October 6, 2026, revising a September 24, 2026
version) supplies, as its Theorem 1.1, the positivity, rationality and $2$-adic
valuation of the BSD quotient (imported as Theorem 2.2), and its finite-model,
switching, division, Siegel-class, CM-disk and inert-derivative arguments are
adapted at odd $p$ in Sections 2--6 here; it is not held in this library. A
third release manuscript, outside the family, *Goldfeld's analytic density
conjecture and the $2$-converse for elliptic curves* (October 7, 2026), supplies
the twist-density theorem (imported as Theorem 2.5) and is not held here either.
The release also keeps the earlier dated version of this manuscript, folder
`preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026`
(October 3, 2026, same file name, 94 pages). A line comparison of the two TeX
bundles at revision fd4aeeb2e finds only three changes: the date, the links of
the three cited release manuscripts (moved from their September versions to the
October ones), and one citation key in the introduction (`01-introduction.tex`
line 134) that has no bibliography entry and prints as the "?" in "[24, 23, ?]"
on p. 4 of the October 3 PDF. The release's history calls this the removal of
"an obsolete introductory citation to a removed supporting manuscript". The two
PDFs differ in text only on pp. 1, 4 and 93, so the labels and page locators on
this card apply to both versions. The companions' arguments were not read for
this card.

Read status: claims checked for Theorem 1.1 and the normalizations it rests on,
read clause by clause in the release's TeX source on 2026-10-12 (files under
`build/sections/`): `01-introduction.tex` lines 12--71 (the definitions of
$s_p$, $a$, $r$, $\mathrm{Sha}$, $\Omega_E$, $c_\ell$, $H$, $B$ and
$\mathrm{Reg}_E$, and `thm:main` at lines 47--62) and lines 141--167 (the
quotient $Q_E$ and the two outputs); the statements of `02-classical.tex` labels
`classical:low-corank` (lines 28--34), `classical:two-primary` (40--48),
`classical:analytic-low-rank` (60--63), `classical:isogeny` (72--83),
`classical:twist-density` (103--108), `classical:auxiliary-fields` (115--137),
`classical:gross-zagier` (228--240) and `classical:discrepancy-identity`
(261--283); `single:center` (`05-single.tex` lines 1276--1284),
`pair:interpolation` (`06-pair.tex` lines 250--290), `pair:integral-quotient`
(`06-pair.tex` lines 1048--1058), `extraction:theta-implication`
(`08-extraction.tex` lines 28--42), `unit:unit-comparison` (`09-unit.tex` lines
396--401), and in `10-center.tex` `center:exact-factor` (34--54),
`center:pair-discrepancy` (143--151), `center:cm-zero` (173--177),
`center:odd-valuations` (231--237) and the proof of Theorem 1.1 (254--271). The
final assembly proof was followed line by line; all other proofs were read for
their structure only and no step was checked; nothing here is independently
reviewed.

## Contents

The numbering below is the PDF's: results and most displayed equations are
numbered within sections, and 24 displays in Sections 4--10 carry separate
running tags (1)--(24), cited below as tags.

- Section 1, Introduction (pp. 2--7). Fixes the normalizations: the full
  $p$-power Selmer group, $s_p(E)$ its $\mathbb Z_p$-corank, $a(E)$ the order of
  the uncompleted $L(E,s)$ at $s=1$, $r(E)$ the Mordell--Weil rank, the total
  real period $\Omega_E$ over all of $E(\mathbb R)$, the Tamagawa numbers
  $c_\ell(E)$, and a height $H$ and pairing $B$ with $B(P,P)=H(P)$ defining
  $\mathrm{Reg}_E$. States
  [[diophantine_problems/openai_2026_exact_birch_swinnerton_dyer_formula_low_selmer_corank/theorem_1_1|Theorem 1.1]]
  (p. 3) and says its rank and finiteness assertions are the Selmer converse and
  its $2$-primary equality the two-primary companion, so that "The new assertion
  proved here is the exact valuation of the leading-term formula at every odd
  prime" (p. 3). Surveys Birch--Swinnerton-Dyer, Tate, Cassels, modularity
  (Wiles, Taylor--Wiles, Breuil--Conrad--Diamond--Taylor), Gross--Zagier,
  Kolyvagin, and the Iwasawa-theoretic results of Rubin, Kato, Skinner--Urban
  and Jetchev--Skinner--Wan, which it says are not used as unrestricted
  odd-primary formulas; Burungale--Flach is the CM rank-zero input. Section 1.3
  (pp. 4--5) defines the BSD quotient $Q_E$ (the derivative $L^{(r)}(E,1)$
  times $\#E(\mathbb Q)_{\rm tors}^2$ over
  $r!\,\Omega_E\mathrm{Reg}_E\prod c_\ell$)
  and the discrepancy $X_p(E)=v_p(Q_E)-v_p(\#\mathrm{Sha}(E/\mathbb Q))$, and
  names the two outputs at a fixed odd $p$: $X_p(E)\ge0$ for non-CM $E$ with
  $a(E)\le1$, and $X_p(E)+X_p(E^D)=0$ for a suitable imaginary quadratic twist
  with $a(E)+a(E^D)=1$. Section 1.4 (pp. 5--6) sketches the integral comparison
  over $R=\mathbb Z_p[\![t,u_1,\dots,u_m]\!]$, with $t$ a genuine cyclotomic or
  anticyclotomic variable and the $u_i$ tame variables at moving auxiliary
  primes, and the quotients $U_w=B_w/L_w$ of an analytic series by a Selmer
  determinant, first shown integral, then units (Figure 1, p. 6).
- Section 2, Arithmetic inputs and exact normalizations (pp. 7--11).
  Theorem 2.1 (the low-corank Selmer converse) and Theorem 2.2 (the
  two-primary leading term for $s_2\le1$) are imported from the two
  companions' Theorems 1.1; Theorem 2.3 is Gross--Zagier--Kolyvagin with
  modularity; Proposition 2.4 is isogeny invariance of $Q_A/\#\mathrm{Sha}$
  (Cassels, Milne); Theorem 2.5, imported from the Goldfeld manuscript's
  Theorem 1.2, gives density $1/2$ to each of analytic ranks $0$ and $1$
  among quadratic twists (squarefree $d$ ordered by $|d|$). Lemma 2.6 (p. 8)
  chooses coprime negative odd fundamental discriminants $D,D'<-4$ with
  every prime of $2Np$ split in both, $(D/|D'|)=1$, twists
  $E^D,E^{D'},E^{DD'}$ of analytic ranks $1-r,1-r,r$, and
  $L=\mathbb Q(\sqrt D,\sqrt{D'})$ CM over $F=\mathbb Q(\sqrt{DD'})$,
  unramified at finite places, meeting $\mathbb Q(E[p])$ only in
  $\mathbb Q$ and, when $E$ has CM, not containing its CM field. Theorem 2.7
  (p. 10) is the split Gross--Zagier formula with the Manin constant $c_E$
  kept, and
  Proposition 2.8 (p. 10) the real identity: the product of
  $Q/\#\mathrm{Sha}$ for $E$ and $E^D$ equals
  $[E(K):\mathbb ZP_K]^2/(c_E^2\prod c_\ell(E)^2\,\#\mathrm{Sha}(E/K))$ for
  the Heegner trace $P_K$ over $K=\mathbb Q(\sqrt D)$, with its $p$-adic
  valuation form.
- Section 3, Integral cohomology and determinant comparisons (pp. 11--19).
  Selmer complexes over power-series rings as fibers of localization (full
  condition the identity, strict the zero map); finite free models with
  ultrafilter limits retaining cup products and homotopies (Lemma 3.1,
  adapted from the two-primary companion), exact local complements and
  duality (Lemma 3.2), evaluation detection (Lemma 3.3), line and square
  switches and the strict-versus-finite volume formula (Lemmas 3.4--3.6),
  the local Haar identities $\tau_\ell=v_p(c_\ell P_\ell(1))$ and
  $\tau_p-l=v_p(c_pP_p(1))$ (Lemma 3.7), the global Kummer volume
  $2n_P+2\tau_g-s_K$ (Lemma 3.8), and integral division from high finite
  characters (Lemma 3.9), with Lemmas 3.10--3.11.
- Section 4, Auxiliary primes and residual concentration (pp. 20--27). Builds
  tame variables from sequences of auxiliary primes, cyclotomic over $\mathbb Q$
  and ring-class over $K$ (Lemma 4.1), and proves Proposition 4.2 (p. 22, tag
  (1)): after finitely many more tame variables, for both the rational and
  the imaginary tuple the global complex $G$ localized at the prime $(p)$ is a
  free line in degree one, and the strict determinants $L_w,L'_w$ of $E$ and
  of the companion twist are nonzero modulo $(p,t)$ at both places $w\mid p$;
  Lemmas 4.3--4.8 (scalar localization, conjugate parity, a first-order lift
  test, spanning of the obstruction matrices, preservation under enlargement,
  directions at horizontal tests) carry the proof. Inputs: Serre's open image
  theorem and the two companions.
- Section 5, The single-curve determinant and its central value (pp. 28--44).
  For non-CM $E$ with $a(E)\le1$ and odd $p$: integral Siegel-unit classes in
  Kato's construction, normalized as in the two-primary companion and rechecked
  at odd $p$ (Lemma 5.1, Propositions 5.2 and 5.4, with Kato's dual-exponential
  formula, his Theorem 9.5, in Lemma 5.3), an integral normalized coordinate
  $U\in R\setminus\{0\}$ (Proposition 5.5, tag (3)), horizontal line comparisons
  (Lemma 5.6), an exact rank-one logarithmic comparison
  $\log z_b/(\log P)^2=\pm d_0L'(E,1)/(\Omega_0H(P))$, with $\Omega_0$ the
  connected real period (Proposition 5.7, tag (5), proved through an
  auxiliary imaginary quadratic field and Lemmas 5.8--5.10),
  and Proposition 5.11 (p. 43, tag (8)): $X(E)=v_p(U(0))\ge0$ for all reduction
  types and residual representations.
- Section 6, The analytic series and the pair comparison (pp. 45--57).
  Over $K$ with $p=w\bar w$, $L_w$ is the determinant of the complex strict
  at $w$ and full at $\bar w$. An integral logarithmic primitive on the
  ordinary locus (Proposition 6.1) gives bounded CM measures and the series
  $B_w$; Proposition 6.2 (p. 48) interpolates them at finite characters and
  gives the central value (tag (12))
  $B_w^{s=1}(0)=\pm c_E^{-2}\log_{\omega_E}(P_K)^2P_p(1)^2\prod_qP_q(1)^2$,
  the product over the fixed split support $S^\circ$; Lemma 6.3 removes tame
  conductor variables and Lemma 6.4 descends the analytic ideals;
  Proposition 6.5 (p. 49) gives $p\nmid B_w$ by a tame-stalk independence
  argument on the ordinary modular curve (Chai's canonical coordinates,
  Hida's $\mu$-invariant method, Zarhin); Proposition 6.6 (p. 52) gives
  divisibility of $B_w$ by $L_w$ at high finite characters after inverting
  $p$, with the $w$ and $\bar w$ quotients associate, through the local
  Kummer lines (Lemma 6.7) and inert derivative coordinates (Lemma 6.8,
  using Bogomolov's homothety theorem). Corollary 6.9 (p. 57):
  $U_w=B_w/L_w$ is an integral series with $p\nmid U_w$.
- Section 7, Theta congruences at a characteristic-zero point (pp. 57--71).
  Theta lifts from a compact unitary group carrying the Jacquet--Langlands
  transfer of the real quadratic base change of $E$'s form to a unitary
  group of signature $(3,1)$ at both real places of $F$. At a
  characteristic-zero zero $z_0$ of the undepleted series $b_w^0$: test
  data and the point (Lemmas 7.1--7.2), canonical ordinary levels and the
  two $p$-operators (Lemmas 7.3--7.4), a moment bound uniform in the
  position cut (Lemma 7.5), integral theta sections (Proposition 7.6), CM
  translations and toric weight limits (Lemma 7.7, Proposition 7.8), and
  Proposition 7.9 (p. 70): all constant Fourier--Jacobi coefficients tend
  uniformly to zero at $z_0$. Inputs: the Siegel--Weil and Rallis
  identities (Yamana; Gan--Qiu--Takeda), Waldspurger, Godement--Jacquet,
  and the Selmer converse's conventions and theta constructions (its
  Sections 2, 4 and 5, Lemmas 6.2, 6.4, 7.1 and 8.6).
- Section 8, Content at a character and extraction of a primitive class
  (pp. 71--83). Proposition 8.1 (p. 71), the theta implication: if $b_w^0$
  lies in a horizontal height-one prime, then over its residue field a
  one-sided primitive Selmer group of $V\chi$ or of the twisted plane
  $V'\chi$ is nonzero. The proof, by contradiction at a chosen point,
  exhibits a coefficient of bounded valuation (Lemma 8.2), lifts to cusp
  forms with increasing $p$-depth (Lemma 8.3), attaches four-dimensional
  Galois representations with local controls (the Selmer converse's
  Proposition 8.5; Lemma 8.4), builds limiting corner modules (its
  Section 9; Lemmas 8.5--8.6) and extracts a class unramified at the fixed
  bad places, descended from $L$ to $K$.
- Section 9, Removing the divisors of the integral quotient (pp. 83--89).
  Every divisor of $U_w$ is horizontal and nonzero modulo $(p,t)$
  (Lemma 9.1); the two quotient ideals coincide (Lemma 9.2); after adding
  tame directions, simultaneous jumps have codimension at least two
  (Lemmas 9.3--9.4, Proposition 9.5); Theorem 9.6 (p. 88): the $U_w$ are
  units, giving an integral unit comparison on the anticyclotomic line.
- Section 10, The central value and the exact formula (pp. 89--92).
  Proposition 10.1 (p. 89, tag (23)):
  $2(n_P+\tau_g)=s_K+2v_p(c_E)+2\sum_qv_p(c_q(E))$; Corollary 10.2
  (p. 90): $X(E)+X(E^D)=0$ for every curve of analytic rank $0$ or $1$, CM
  included, with $E^D$ the twist of Lemma 2.6; Lemma 10.3 (p. 91): exact BSD
  for CM curves with $L(E,1)\ne0$, from Burungale--Flach (Theorem 1.1 and
  Corollary 1) after an isogeny to maximal-order CM, then their Corollary 2
  descent with positivity from Theorem 2.2; Proposition 10.4 (p. 91):
  $v_p(Q_E)=v_p(\#\mathrm{Sha}(E/\mathbb Q))$ for every curve of analytic
  rank $0$ or $1$ and every odd $p$; the proof of Theorem 1.1 (p. 92).
- References (pp. 92--94), 34 entries, three of them release manuscripts.

Conditional and external components flagged here: Theorems 2.1, 2.2 and 2.5 are
imported from three release manuscripts that are themselves unreviewed; Sections
2, 4, 7 and 8 rest on the Selmer converse's constructions by reference, and
Sections 2--6 adapt the two-primary companion's arguments; the CM rank-zero case
rests on Burungale--Flach (cited with locators to arXiv:2206.09874v3); the
primitivity argument cites an author-hosted 2003 preprint of Chai; Smith's arXiv
preprint enters only through the twist-density input. The manuscript contains no
numerical or computer-assisted component, and the release folder holds only
`build/`, the PDF and `README.md`, with no `verification/` directory.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using it. A search of the problem pages for elliptic curves, Selmer groups,
Tate--Shafarevich groups and the Birch--Swinnerton-Dyer conjecture found no page
whose recorded argument uses a leading-term formula; the two nearest pages were
read. Problem 939's page records, for its already answered third part, Walsh's
construction conditional on positive rank of $Y^2=X^3-432\ell^2$, which the
page and the Selmer-converse card record as claimed by that manuscript's
Corollary 10.1 for primes $\ell\equiv4,7,8\pmod 9$; here the rank statement
enters only as the
imported Theorem 2.1, and the leading-term formula proved here adds nothing that
the construction uses. Problem 829, on the number of representations of $n$ as a
sum of two cubes, concerns integral points on the curves $x^3+y^3=n$, which
Theorem 1.1 does not control.
