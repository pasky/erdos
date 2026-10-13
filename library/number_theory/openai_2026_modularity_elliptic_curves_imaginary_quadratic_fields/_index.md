---
name: number_theory/openai_2026_modularity_elliptic_curves_imaginary_quadratic_fields
desc: |
  A 30-page release manuscript claiming that every elliptic curve over every
  imaginary quadratic field is modular, with matching local parameters at
  every place, by a prime switch through character pieces of one family of
  cyclic covers and Caraiani-Newton's lifting theorem; it names no Erdős
  problem and no problem page is identified as using it.
license: Apache-2.0
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

# number_theory/openai_2026_modularity_elliptic_curves_imaginary_quadratic_fields

[[number_theory/_index|..]]

[[number_theory/openai_2026_modularity_elliptic_curves_imaginary_quadratic_fields/theorem_1_1|theorem_1_1]]: The manuscript's main claim: every elliptic curve over every imaginary
quadratic field K is realized by an isobaric weight-zero automorphic
representation of GL_2 over K, cuspidal without CM, with local-global
compatibility at every place and L(E/K,s) = L(pi_E,s-1/2). Claims checked
only.

***

OpenAI, *Modularity of elliptic curves over imaginary quadratic fields*, OpenAI
Math Release preprint, October 4, 2026. Released under the Apache License 2.0 at
<https://github.com/openai/math> (revision fd4aeeb2e), folder
`preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026`;
the held PDF, `paper.pdf` in the release, is retained as
[openai_2026_modularity_elliptic_curves_imaginary_quadratic_fields.pdf](openai_2026_modularity_elliptic_curves_imaginary_quadratic_fields.pdf),
and the release's TeX bundle in that folder is the TeX source cited on this
card. The license term was read in the release's root `LICENSE` file at that
revision on 2026-10-12.

```bibtex
@misc{OAI:Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026,
  author = {{OpenAI}},
  title = {{Modularity of elliptic curves over imaginary quadratic fields}},
  howpublished = {OpenAI Math Release preprint
                  \href{https://github.com/openai/math/blob/main/preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/paper.pdf}{OAI:Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026}},
  year = {2026}
}
```

The held PDF has 30 pages with a text layer; its printed page numbers equal
the PDF's, its title page is dated October 4, 2026, and its metadata records
a creation date of 5 October 2026. The TeX source is the text read here:
`build/main.tex` (89 lines) inputs nine section files under
`build/sections/` (2,100 lines in all), two of which input TikZ figure files
under `build/figures/`, and the bibliography is the 41-entry
`build/references.bib`.

**Attestation.** The release README states that the manuscripts were
"produced by an internal OpenAI model", that the collection "includes results
at different stages of verification", that "Not all have accompanying Lean
formalizations" and that "Some of the unformalized results could have
issues". Its account of the method says that "The vast majority of results
were obtained with the same procedure"; the two exceptions it names concern
other subjects (a zero-free region for the Riemann zeta function and the
Hodge conjecture for CM abelian varieties), and it does not say per
manuscript which procedure produced it. The manuscript's own README carries
only the title, the author line "OpenAI", the date and the citation block, and
adds no sentence about authorship or assistance; the title page names OpenAI
as the sole author, and the TeX source carries no statement on how the text
was produced. These are the source's own statements, recorded as attestations
and not as this corpus's review. No refereed publication, arXiv version or
independent review of the manuscript is recorded here and nothing on this
card is independently reviewed.

**Formalization.** The release lists no formalization of this manuscript: its
catalog `lean/formalization.yaml` has no entry for it and its family has no
page under `lean/docs/` at revision fd4aeeb2e.

**Companions.** The release files this manuscript alone in its family
("Modularity over imaginary quadratic fields" in the release overview), and it
holds no earlier dated version of it; there is no companion to read or link.

Read status: claims checked for Theorem 1.1, together with the statements of
Corollary 5.4, Definition 6.1, Theorems 6.2--6.4, Proposition 8.4,
Proposition 9.3 and Lemma 9.4, read clause by clause in the release's TeX
source (`build/sections/introduction.tex` label `thm:main` at lines 17--43;
`systems.tex` label `sys:congruences` at lines 256--267;
`automorphy-inputs.tex` labels `def:decomposed-generic` at lines 11--21,
`aut:lift` at lines 35--57, `aut:seed` at lines 65--71 and
`aut:elliptic-compat` at lines 80--93; `residual.tex` label
`res:specialization` at lines 199--218; `automorphy.tex` labels `aut:over-F`
at lines 94--98 and `aut:descent` at lines 153--160) on 2026-10-12. The rest
of the TeX was read once, and all proofs were read for their structure only;
no step was checked, and the specialized forms of Caraiani and Newton's
theorems (Theorems 6.2--6.4) were not compared with the preprint they cite.
Nothing here is independently reviewed.

## Contents

Theorems, lemmas, definitions and remarks share one counter within each
section; the numbers below are the PDF's.

- Section 1, Introduction (pp. 1--3). Describes the automorphy conjecture for
  an elliptic curve $E$ over an imaginary quadratic field $K$: an automorphic
  representation of $\mathrm{GL}_2(\mathbb A_K)$ with local parameters
  matching the cohomology of $E$ at every place, including inertia and
  monodromy at bad places and the Hodge types $(1,0),(0,1)$ at infinity.
  States
  [[number_theory/openai_2026_modularity_elliptic_curves_imaginary_quadratic_fields/theorem_1_1|Theorem 1.1]]
  (p. 1). Section 1.1 (p. 2) surveys the background: Bianchi groups (Bianchi,
  Swan, Harder), Langlands's problems paper, the computations of
  Grunewald--Helling--Mennicke, Cremona and Cremona--Whitley; Wiles,
  Taylor--Wiles and Breuil--Conrad--Diamond--Taylor over $\mathbb Q$ and
  Wiles's $3$--$5$ switch; Galois representations for Bianchi forms
  (Harris--Soudry--Taylor, Taylor, Berger--Harcos), Harris--Lan--Taylor--Thorne
  and Scholze; Calegari--Geraghty's patching; potential modularity over CM
  fields (Allen et al., Theorem 1.0.1) and Boxer--Calegari--Gee--Pilloni;
  Allen--Khare--Thorne; and Caraiani--Newton, whose results include
  modularity of every elliptic curve over an imaginary quadratic $K$ for which
  $X_0(15)(K)$ has rank zero. The manuscript says Theorem 1.1 removes the
  remaining restrictions and that Caraiani--Newton's lifting theorem and
  residual criterion "remain essential inputs" (p. 2). Section 1.2
  (pp. 2--3) outlines the "geometric prime switch": for non-CM $E$, a large
  prime $p$ with $\mathrm{SL}_2(\mathbb F_p)$ in the image on $E[p]$,
  $n=3p$, $F=K(\mu_n)$, a genus-$n$ cyclic cover $C_n(t)$ of a quadratic
  twist $B_t$ of $E$ with a dihedral involution, and rank-two pieces
  $V_\theta$ of its cohomology indexed by characters $\theta$ of $\mu_n$,
  linked by congruences modulo $p$, $3$ and $p$ from $H^1$ of an auxiliary
  elliptic curve $A$ to $H^1(B_t)$, the prime $5$ serving only to start from
  $A$. It names antecedents (Tautz--Top--Verberkmoes, Ellenberg, Mestre,
  Darmon, Darmon--Mestre, Taylor) and says the local-constancy and
  two-conjugate specialization arguments are stated so they can be used
  apart from the automorphy application.
- Section 2, Galois and automorphic conventions (p. 4). Étale $H^1$ with
  $\mathbb Q_l$ coefficients, the cyclotomic character of Hodge--Tate weight
  $-1$ (so an elliptic curve has weights $0,1$ and determinant
  $\epsilon_l^{-1}$), bars for semisimplified reductions; $r_\iota(\pi)$ for
  regular algebraic cuspidal $\pi$ over a CM field in the normalization of
  Harris--Lan--Taylor--Thorne, Scholze and Caraiani--Newton, with the
  Tate-normalized reciprocity map
  $\mathrm{rec}^T(\pi_v)=\mathrm{rec}(\pi_v\otimes|\det|_v^{-1/2})$ and
  geometric Frobenius; "weight zero"; the complex-place parameter; the shift
  $L(E/L,s)=L(\pi,s-1/2)$; and the definitions of potentially crystalline
  and potentially ordinary of weight zero.
- Section 3, Cyclic covers and two degenerations (pp. 4--8). For $E:y^2=h(x)$
  over a number field and odd $n\ge3$, the twist $B_t:h(t)y^2=h(x)$ with the
  point $R_t=(t,1)$ and $S_t=[n]R_t$. Lemma 3.1 (p. 5): for each divisor
  $m>1$ of $n$, a smooth proper family of genus-$m$ curves, the Kummer cover
  $Y^m=f_t$ with $\operatorname{div}f_t=(S_t)-(-S_t)-n(R_t)+n(-R_t)$, with
  an involution inverting the rotations and quotient maps to smaller covers
  and to $B_t$. Lemma 3.2 (p. 6): regular semistable models at two boundary
  parameters, with nodes of smoothing order one. Proposition 3.3 (p. 6): at
  the first boundary point the fiber is of compact type, a rational curve
  carrying $m$ copies of $E$, so the Jacobian family extends to an abelian
  scheme with fiber $E^m$ (Bosch--Lütkebohmert--Raynaud). Remark 3.4 (p. 7)
  confines this to characteristic zero. Lemma 3.5 (p. 7): at the second
  point the fiber is an unramified degree-$m$ cover of $E$ joined to a
  rational curve at $m$ nodes, with explicit local node equations. Figure 1
  (p. 8) draws the two dual graphs.
- Section 4, Integral homology and explicit monodromy (pp. 8--11). Over
  $\mathbb C$, a slit model (Lemma 4.1, p. 8) and an integral symplectic
  basis permuted by the deck group, Proposition 4.2 (p. 9): $H_1$ and $H^1$
  of each smooth fiber are free of rank two over the group ring
  $\mathbb Z[\Gamma_m]$, and étale $H^1$ with $\mathbb Z_\ell$ coefficients
  is free of rank two over $\mathbb Z_\ell[\Gamma_m]$ for every $\ell$,
  including $\ell\mid m$. Lemma 4.4 (p. 9) computes the vanishing classes at
  the second degeneration (Figure 2, p. 10), and Theorem 4.5 (p. 10), by the
  Picard--Lefschetz formula (SGA 7 II, Exposé XV), gives two monodromy
  operators in one basis whose off-diagonal entries over the group ring are
  $\pm(2-u-u^{-1})$.
- Section 5, Rank-two systems and integral congruences (pp. 11--14). For
  non-CM $E/K$, chooses $p>100$ with $\mathrm{SL}_2(\mathbb F_p)$ in the
  mod-$p$ image (Serre's open image theorem), sets $n=3p$ and
  $F=K(\mu_n)$, a CM field abelian over $\mathbb Q$ that does not contain
  $\zeta_5$, and defines the character spaces $V_{\theta,\ell}$ in
  $H^1(C_n(t))$. Proposition 5.1 (p. 12): each is semisimple of dimension
  two with determinant $\epsilon_\ell^{-1}$ and Hodge--Tate weights $\{0,1\}$,
  potentially semistable, and the family over $\ell$ is a compatible system
  (Tsuji's comparison, Faltings's semisimplicity). Proposition 5.2 (p. 13):
  the trivial character gives $H^1(B_t)$, and an order-three character gives
  $H^1$ of the elliptic curve $A_t=\operatorname{Jac}(C_3(t)/\langle w\rangle)$
  over $F$. Lemma 5.3 (p. 13): evaluating the free group-ring module at a
  character gives a stable lattice whose reduction depends only on the
  reduced character. Corollary 5.4 (p. 14): for every parameter, with
  $\chi=\psi\eta$ of order $3p$, the congruences
  $\overline V_{\eta,p}\simeq\overline V_{\chi,p}$,
  $\overline V_{\chi,3}\simeq\overline V_{\psi,3}$ and
  $\overline V_{\psi,p}\simeq\overline V_{1,p}$.
- Section 6, Automorphy inputs (pp. 14--16). Definition 6.1 (p. 14):
  decomposed genericity, as in Caraiani--Newton's Definition 2.1.27.
  Theorem 6.2 (p. 15), a specialized form of Caraiani--Newton's Theorem 5.2
  (their third arXiv version), the automorphy lifting theorem used three
  times; Theorem 6.3 (p. 15), their Theorem 6.1 with Lemma 6.1.3, the
  mod-$5$ starting point for a non-CM elliptic curve over a CM field without
  $\zeta_5$; Theorem 6.4 (p. 15), their Lemma 6.1.3, local-global
  compatibility for a modular non-CM elliptic curve. Also cited:
  Harris--Lan--Taylor--Thorne and Scholze for the Galois representations and
  Varma's Theorem 1 for local-global compatibility away from $l$. The
  section lists the conditions still to be arranged at one parameter $t$.
- Section 7, Prescribing the local reduction type (pp. 16--20). Lemma 7.1
  (p. 16): finite torsion of an abelian scheme over a local field is locally
  constant in the parameter. Lemma 7.2 (p. 16): semistable Frobenius
  polynomials of fixed dimension over a fixed residue field form a finite set
  and determine the toric rank, and the Newton polygon when that rank is
  zero. Proposition 7.3 (p. 17): hence the semistable reduction type is
  locally constant after a fixed finite extension; near a fiber $E_0^g$, nearby
  fibers are ordinary, have all slopes $1/2$, or are totally toric, as $E_0^g$
  is. Lemma 7.4 (p. 18): a
  potentially totally toric abelian variety of dimension $g$ has monodromy of
  rank $g$ at every coefficient prime, the residue characteristic included
  (through Bloch--Kato's crystalline subspace and the valuation matrix of the
  periods). Proposition 7.5 (p. 19) gives open sets of parameters at the
  places above $3p$ on which $\operatorname{Jac}(C_n(t))$ has the reduction
  type of $E^n$, and Corollary 7.6 (p. 20) transfers it to every character
  piece at once.
- Section 8, One specialization with all residual properties (pp. 20--25).
  Lemma 8.1 (p. 21): for $(m,\ell)=(3,p),(3,5),(p,3)$ the geometric
  monodromy on every nontrivial character space mod $\ell$ is absolutely
  irreducible, contains opposite unipotents, and has one element regular
  semisimple on all of them, for $E$ and its conjugate. Lemma 8.2 (p. 22):
  $\overline V_{1,p}$ is absolutely irreducible over $F(\zeta_p)$ and
  decomposed generic, by a count of trace-$\pm2$ elements in
  $\mathrm{SL}_2(\mathbb F_p)$ applied to $E$ and its conjugate together.
  Lemma 8.3 (p. 23): Hilbert irreducibility with weak approximation (Serre's
  *Topics in Galois Theory*) for a finite quotient of the fundamental group
  of an open subset of affine space, with constant field. Proposition 8.4
  (p. 23): one $t\in U(K)$, inside prescribed local opens, at which every
  needed residual representation is absolutely irreducible over the
  cyclotomic extension and decomposed generic and $A_t$ has no CM; the proof
  specializes the restriction of scalars $\operatorname{Res}_{K/\mathbb Q}U$
  so that both conjugate families are controlled.
- Section 9, Propagation of automorphy and descent (pp. 25--28). Lemma 9.1
  (p. 25): automorphy of one member of a compatible system gives all
  members. Lemma 9.2 (p. 25): the local automorphic conditions at $3$ and
  $p$ (zero monodromy in the potentially good case; a quadratic or trivial
  twist of Steinberg, hence ordinary, in the totally toric case), from Varma
  and Caraiani--Newton's Lemma 6.1.3(4) with Geraghty's Lemma 5.6.
  Proposition 9.3 (p. 26): $B_t$ is modular over $F$, by the seed Theorem 6.3
  and three applications of Theorem 6.2. Lemma 9.4 (p. 27): descent along a
  cyclic prime-degree extension of CM fields (strong multiplicity one, cyclic
  base change of Langlands and Arthur--Clozel, a character twist). The section
  then descends from $F$ to $K$, untwists from $B_t$ to $E$, matches the local
  parameters, and treats CM curves through Hecke characters and the theory of
  complex multiplication of Shimura and Taniyama (pp. 27--28).
- References (pp. 28--30): 41 items; the one unpublished item is
  Caraiani--Newton's preprint, arXiv:2301.10509v3 (27 March 2025), whose
  third version's numbering the manuscript uses. No release manuscript is
  cited.

The manuscript has no numerical or computer-assisted component and flags
no conditional step; its external inputs are cited at statement level, the
Caraiani--Newton theorems in specialized forms the manuscript states itself.
The release folder holds only the PDF, the TeX build directory and the
README; there is no `verification/` folder.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using it. Where a problem page, one of its claim pages or a library card it
links records an elliptic-curve argument, for example for Problems 157, 158,
364, 368, 672, 829, 937, 939, 960 and 976, the curves are defined over
$\mathbb Q$, or over a finite field for Problems 157 and 158. For Problems 157
and 158 the curve is the one in Hasse's bound on the linked Cilleruelo card;
for Problem 368 the claim page records Pasten's modular approach through
Shimura curves; for Problem 672 the Frey-curve arguments are on the linked
Bennett--Bruin--Győry--Hajdu and Bennett--Siksek cards; and for Problems 829
and 976 the curves are on the linked Stewart and Cuevas Barrientos--Pasten
cards. Over $\mathbb Q$ modularity is already known by
Breuil--Conrad--Diamond--Taylor and is not the open point; Problems 157, 937
and 960 are solved. No page records a route through elliptic curves over an
imaginary quadratic field; Problem 1214's claim page notes an elliptic-curve
analogue over number fields only as not needed for that solved question.
