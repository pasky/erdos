---
name: number_theory/openai_2026_fontaine_mazur_modularity_prime_2
desc: |
  A 72-page release manuscript claiming the odd, regular two-dimensional
  Fontaine-Mazur conjecture over Q at the prime 2: every continuous, odd,
  irreducible two-dimensional 2-adic representation of G_Q that is finitely
  ramified and de Rham at 2 with distinct Hodge-Tate weights is a Tate twist
  of the representation of a classical cuspidal eigenform, with no residual
  hypothesis; it names no Erdős problem.
license: Apache-2.0
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

# number_theory/openai_2026_fontaine_mazur_modularity_prime_2

[[number_theory/_index|..]]

[[number_theory/openai_2026_fontaine_mazur_modularity_prime_2/theorem_1_1|theorem_1_1]]: The manuscript's main claim: the odd, regular two-dimensional Fontaine-Mazur
conjecture over Q at the prime 2, with no hypothesis on the residual
representation, scalar and reducible residues included. Claims checked only.

***

OpenAI, *Fontaine--Mazur modularity at the prime 2*, OpenAI Math Release
preprint, October 6, 2026. Released under the Apache License 2.0 at
<https://github.com/openai/math> (revision fd4aeeb2e), folder
`preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026`; the held
PDF, `paper.pdf` in the release, is retained as
[openai_2026_fontaine_mazur_modularity_prime_2.pdf](openai_2026_fontaine_mazur_modularity_prime_2.pdf),
and the release's TeX bundle in that folder, under `build/`, is the TeX source
cited on this card. The license term was read in the release's root `LICENSE`
file at that revision on 2026-10-12.

```bibtex
@misc{OAI:Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026,
  author = {{OpenAI}},
  title = {{Fontaine--Mazur modularity at the prime 2}},
  howpublished = {OpenAI Math Release preprint
                  \href{https://github.com/openai/math/blob/main/preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/paper.pdf}{OAI:Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026}},
  year = {2026}
}
```

The held PDF has 72 pages with a text layer; its title page is dated 6 October
2026 and its metadata records a creation date of 7 October 2026. The TeX
source is `build/main.tex` (91 lines), which inputs eight section files under
`build/sections/` (`introduction.tex`, `preliminaries.tex`, `deformation.tex`,
`completed_forms.tex`, `patching.tex`, `fields.tex`, `connectedness.tex` and
`classicality.tex`, 5,434 lines together), with `build/references.bib` (64
entries, all printed, as [1]--[64]). TeX paths below are relative to `build/`.

**Attestation.** The release README states that the manuscripts were
"produced by an internal OpenAI model", that the collection "includes results
at different stages of verification", that "Not all have accompanying Lean
formalizations" and that "Some of the unformalized results could have
issues". Its account of the method says that "The vast majority of results
were obtained with the same procedure using an unreleased internal OpenAI
model"; the exceptions it names concern a zero-free region for the Riemann
zeta function and the Hodge conjecture for CM abelian varieties, not this
family's subject. The manuscript's own README carries the title, the author
line "OpenAI", the date, the citation block and a version note saying that
this version "updates citations to revised manuscripts in this collection",
with a link to the previous version; it adds no sentence about authorship,
assistance or verification. The title page and the PDF metadata name OpenAI
as the sole author. These are the source's own statements, recorded as
attestations and not as this corpus's review. No refereed publication, arXiv
version or independent review of the manuscript is recorded here, and nothing
on this card is independently reviewed.

**Formalization.** The release lists no formalization of this manuscript: its
Lean catalog `lean/formalization.yaml` has no entry for it or its family at
revision fd4aeeb2e, and there is no page `lean/docs/010.md`.

**Companions.** The release groups this manuscript in its family, "Unrestricted
pro-modularity at the prime two", with two others; neither has a card in this
library, so neither is linked. The first, *Unrestricted pro-modularity at the
prime two* (October 6, 2026, with an earlier version dated October 4, 2026), is
described by the release as a completed-Hecke occurrence result for every
continuous, odd, absolutely irreducible two-dimensional $2$-adic representation
of $G_{\mathbb Q}$ unramified outside finitely many primes, with no de Rham
hypothesis and no claim of classical modularity; its introduction cites Theorem
1.1 here to make a regular de Rham point classical. *The Dimension of the
Two-Adic Hecke Algebra at Odd Level* (October 5, 2026) is described by the
release as proving that every irreducible component of the full $2$-adic Hecke
algebra of level $\Gamma_1(N)$, $N$ odd, has Krull dimension four, the case
$p=2$ of Emerton's dimension conjecture; it and this manuscript do not cite each
other. The release also keeps an earlier dated version of this manuscript,
*Fontaine--Mazur modularity at the prime 2* (September 23, 2026, folder
`preprints/Fontaine-Mazur-modularity-at-the-prime-2-September-23-2026`, 72
pages), which this version's README links as the previous version; its TeX
bundle differs from this one only in the date line and in the bibliography link
to the release's Hilbert's tenth problem manuscript (the earlier version links
that manuscript's September 24 version, this one its October 6 version), so the
statements and labels cited on this card are the same in both. Outside the
family, *Hilbert's tenth problem over the rational numbers* (October 6, 2026),
filed at
[[diophantine_problems/openai_2026_hilberts_tenth_problem_rational_numbers/_index|the Hilbert's tenth problem card]],
cites Theorem 1.1 as the modularity input of its height argument (its
Section 4), for a two-dimensional $2$-adic representation built from the Tate
module of an abelian surface with quaternionic multiplication, and reads weight
two off the normalization of Section 2.1 here. The companions' arguments were
not read for this card.

Read status: claims checked for Theorem 1.1, together with the statements of
Lemma 2.2 (the virtually solvable case), Theorem 5.1 (localized propagation),
Theorem 7.1 (potential pro-modularity) and Lemma 8.5 (the dense modular points
obtained from Thorne's theorem), read clause by clause in the release's TeX
source (`sections/introduction.tex` label `thm:main` at lines 20--30,
`sections/preliminaries.tex` label `lem:solvable-reduction` at lines 146--152,
`sections/patching.tex` label `thm:localized-propagation` at lines 23--38,
`sections/connectedness.tex` label `thm:potential-promodularity` at lines
11--24 and `sections/classicality.tex` label `lem:dense-Thorne-points` at
lines 395--399) on 2026-10-12; the statements of most other numbered results
were read, not clause by clause, for the account below; the proofs were read
for their structure only and no step was checked; nothing here is
independently reviewed.

## Contents

The numbering below is the PDF's: theorems, propositions, lemmas, corollaries
and remarks share one counter within each section.

- Section 1, Introduction (pp. 1--5). Calls a continuous
  $r:G_{\mathbb Q}\to\mathrm{GL}_2(\overline{\mathbb Q}_p)$ odd if
  $\det r(c)=-1$ for a complex conjugation $c$, and regular de Rham at $p$ if
  its restriction to $G_{\mathbb Q_p}$ is de Rham with two distinct Hodge--Tate
  weights, and states
  [[number_theory/openai_2026_fontaine_mazur_modularity_prime_2/theorem_1_1|Theorem 1.1]]
  (p. 1), the case $p=2$ of the conjecture, with every semisimple residual
  representation included. Together with the results of Pan (2022,
  Theorems 1.0.2 and 1.0.4) and Zhang (2025, Theorem 1.0.2) at odd primes, it
  says, the conclusion holds at every prime. It names the release's Hilbert's
  tenth problem manuscript as a user of the theorem. Section 1.1 (pp. 2--3)
  reviews Wiles and Taylor--Wiles, Serre's conjecture (Khare--Wintenberger,
  Kisin), Skinner--Wiles, Allen's nearly ordinary dyadic theorem with solvable
  residual image, Kisin and Emerton, and Tung's dyadic lifting theorem, whose
  global residual image is nonsolvable. It credits Thorne's Theorem D (a 2026
  arXiv preprint) with an "essential set of classical points": ordinary,
  potentially crystalline representations with weights $\{0,1\}$ are modular at
  every prime with no residual irreducibility hypothesis. Section 1.2
  (pp. 3--5) defines a pro-modular locus, a closed trace locus cut out by a
  completed Hecke algebra of definite quaternionic forms with no local
  condition at $2$, and lays out the three stages (potential occurrence for a
  whole family, classical vectors at the target, solvable descent) with the
  roadmap Figure 1 (p. 4). Section 1.3
  (p. 5) lists the constructions: the Laurent-series deformation theory of
  Böckle--Iyengar--Paškūnas, patching after Taylor--Wiles, Kisin,
  Khare--Wintenberger, Pan and Zhang with finite jets, and marked local lines. A
  table of contents fills p. 6.
- Section 2, Conventions and initial reductions (pp. 7--10). Table 1 (p. 7)
  fixes geometric Frobenius, $\epsilon=x|x|$ with Hodge--Tate weight $-1$,
  weights counted as cyclotomic exponents, the central character
  $\psi=\chi\epsilon$ and the block parameter $r\otimes\epsilon$. Section 2.1
  writes $\det r=\chi_{\mathrm{fin}}\epsilon^w$ and fixes the arithmetic
  normalization $V_f$ of an eigenform's representation, with cyclotomic
  exponents $\{0,k-1\}$ in weight $k$, and the conversion of a dual realization.
  Lemma 2.1 (p. 8) shows that any continuous representation of a profinite
  group on $\overline{\mathbb Q}_2^n$ is defined over a finite extension of
  $\mathbb Q_2$ and has a stable lattice there. Lemma 2.2 (p. 8) proves
  Theorem 1.1 for virtually solvable $r$ (scalar identity component excluded by
  distinct weights, induction from a real quadratic field excluded by
  regularity, induction from an imaginary quadratic field given by a theta
  series) and shows that otherwise $r$ stays absolutely irreducible over every
  finite extension. Section 2.3 (pp. 9--10) fixes the
  base fields $F$ (totally real, solvable over $\mathbb Q$, of even degree, $2$
  split completely), $d=[F:\mathbb Q]$, $s=2d+u$ with $u$ the number of allowed
  odd finite places, two-dimensional determinants in Chenevier's sense, the
  pseudodeformation ring $R_F^{\mathrm{ps},\chi}$, the quaternion algebra $D_F$
  ramified exactly at the real places, and characteristic-two curves.
- Section 3, Deformations and local geometry (pp. 10--24). Proposition 3.1
  (p. 10) on representation spaces under Mazur's condition $\Phi_2$, with
  recorded invariant lines; Lemma 3.2 bounds the dimension lost in passing to
  traces by three plus the undistinguished lines; Lemma 3.3 gives dense curves
  and coefficient points; Lemma 3.4 (p. 13) identifies deformations at a curve
  with residue field $k((t))$ through an enhanced coefficient ring, following
  Böckle--Iyengar--Paškūnas, and Lemma 3.5 computes curve-field cohomology.
  Proposition 3.6 (p. 15) bounds generators minus relations over the local
  framed base below by $3-6m-h^0(D^\vee(1))$; Corollary 3.7 gives a local line
  chart of dimension at least five at $\mathbb Q_2$. Lemma 3.8 (p. 17) shows
  dihedral and reducible loci are small and Lemma 3.9 kills inertia by solvable
  base change. Proposition 3.10 (p. 19) describes the real--dyadic local base (a
  normal complete intersection domain of dimension $1+8d$) and two tame models,
  unipotent and with inertia eigenvalues $\pm i$, sharing a special fiber;
  Lemma 3.12 (p. 22) shows that marked scalar dyadic factors give an integral
  base of dimension $2d+5m$.
- Section 4, Completed forms and their local parameters (pp. 24--32).
  Proposition 4.1 (p. 24): completed definite forms over $F$ are finite free
  over an Iwasawa algebra, their locally algebraic vectors are classical, the
  regular non-character eigenpackets transfer to Hilbert cusp forms with Galois
  representations, regular classical vectors are dense, and each Hecke factor
  is a reduced torsion-free quotient of $R_F^{\mathrm{ps},\chi}$.
  Proposition 4.2 (p. 26), from Paškūnas--Tung's block finiteness: the local
  block action on completed forms is the restriction of the global Galois
  action, the Hecke algebra is finite over the local pseudodeformation ring, and
  absolutely irreducible regular de Rham local parameters give locally algebraic
  vectors. Proposition 4.4 (p. 29) bounds every Hecke component's dimension
  below by $1+2d$; Lemma 4.5 (p. 30) gives exact auxiliary-level identities and
  Lemma 4.6 (p. 32) forward solvable base change.
- Section 5, Propagation from a characteristic-two curve (pp. 32--43).
  Theorem 5.1 (p. 32): a potentially pro-modular, non-virtually-solvable
  characteristic-two curve with finite local images at the allowed odd places
  makes every irreducible closed locus containing it potentially pro-modular,
  with no local condition at $2$. Lemmas 5.2--5.3 choose auxiliary primes and
  twist characters; Lemma 5.4 (p. 38) patches finite jets over an ultrapower
  with a uniform Artin--Rees bound; Proposition 5.5 (p. 40) gives the patched
  regular sequence and support dimension at least $2d+4s+h$; Proposition 5.6
  (p. 41) gives full support through character twists, the irreducible $\pm i$
  comparison model and sign intertwiners. The proof of Theorem 5.1 closes on
  p. 43.
- Section 6, Fields with controlled Selmer groups (pp. 43--53). Proposition 6.1
  (p. 43) builds abelian totally real $2$-extensions
  $\mathbb Q\subset A\subset F$, split completely at $2$, of arbitrarily large
  degrees with a bounded number of allowed odd places, preserving the residual
  data, with marked dyadic places when the residual character ratio is trivial
  at $2$, a dual Selmer vanishing and a strict Selmer bound. The construction
  uses cyclic subfields of $\mathbb Q(\zeta_r)$ and a one-prime genus argument
  (Lemma 6.2), switching of local conditions in the manner of Ramakrishna, with
  the needed variant proved in the text (Lemma 6.3), Chebotarev evaluations
  (Lemma 6.4), the distinct-character construction (Section 6.4, with
  Lemma 6.5) and an explicit conductor count (Section 6.5).
- Section 7, Connectedness and potential pro-modularity (pp. 53--58).
  Theorem 7.1 (p. 53): for $r$ as in Theorem 1.1 and not virtually solvable,
  $r$ is pro-modular over a solvable totally real Galois extension of even
  degree split completely at $2$, and so is the closed trace image of any
  complete integral framed deformation family over $\mathbb Q$ through $r$, with
  determinant $\det r$ and finite ramification, over one field and at one tame
  level. Lemma 7.2 (p. 53) gives a classical cuspidal lift of
  the residue (Serre's conjecture when absolutely irreducible; when reducible,
  existence is credited to Billerey--Menares and an Eisenstein-difference
  argument is given). Lemmas 7.3--7.5 (pp. 55--56) show that charts with
  transverse marked lines have large components joined by large intersections,
  that potential pro-modularity holds on all or none of a chart's components,
  and that the transverse residual fiber is geometrically connected. The proof
  (pp. 57--58) joins a seed curve and a target curve through that fiber and
  propagates.
- Section 8, Classicality and descent (pp. 58--67). For reducible
  $r|_{G_{\mathbb Q_2}}$: Lemma 8.1 (p. 59) picks the invariant line of larger
  cyclotomic exponent; Lemma 8.2 builds a family $\mathscr D$ of dimension at
  least two recording that line's character; Proposition 8.3 (p. 61) proves the
  ordinary part finite over the torus Iwasawa algebra; Lemma 8.4 (p. 62) makes
  $\mathscr D$ finite over a one-dimensional weight space; Lemma 8.5 (p. 63)
  shows that at a dense set of its points the representation, after a global
  twist and dualizing, is ordinary and potentially crystalline with Hodge--Tate
  weights $\{0,1\}$, hence modular by Thorne's Theorem D; Section 8.5 (p. 64)
  carries the resulting inducing order to the target; Lemmas 8.6--8.7 (pp.
  65--66) give a genuine ordinary eigenvector and prove it locally algebraic by
  a polynomial-orbit argument. Section 8.8 (p. 67) treats absolutely irreducible
  $r|_{G_{\mathbb Q_2}}$ by the $p$-adic local Langlands correspondence (Colmez;
  Colmez--Dospinescu--Paškūnas), passes by Jacquet--Langlands to a Hilbert cusp
  form over $F$, and descends along prime-degree cyclic steps with
  finite-character corrections to conclude Theorem 1.1.
- References (pp. 68--72), 64 items, among them the 2026 preprints of Thorne
  (arXiv 2608.07186v1) and Emerton--Gee--Pan--Zhu and the release's Hilbert's
  tenth problem manuscript.

The manuscript flags nothing as numerical, computer-assisted or conditional.
Its reducible local branch rests on Thorne's Theorem D, a 2026 preprint cited
at statement level; Emerton--Gee--Pan--Zhu and Pan's 2026 classicality theorem
are discussed for comparison and are not used as inputs. The release folder
for this manuscript holds only the PDF, the TeX build directory and the
README; there is no `verification/` folder.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using it. Where a problem page or one of its claim pages records an argument
through elliptic curves or modularity, as for Problems 364, 368, 937, 939 and
960, the curves are over $\mathbb Q$; for Problem 368 the argument is the
modular approach through Shimura curves that its Pasten claim page records.
Elliptic curves over $\mathbb Q$ are already known to be modular by Breuil,
Conrad, Diamond and Taylor, so Theorem 1.1 adds no step there.
