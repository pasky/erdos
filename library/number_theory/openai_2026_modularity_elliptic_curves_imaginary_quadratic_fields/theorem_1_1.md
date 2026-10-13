---
name: number_theory/openai_2026_modularity_elliptic_curves_imaginary_quadratic_fields/theorem_1_1
title: "Theorem 1.1: every elliptic curve over an imaginary quadratic field is modular, with matching local parameters at every place"
desc: |
  The manuscript's main claim: every elliptic curve over every imaginary
  quadratic field K is realized by an isobaric weight-zero automorphic
  representation of GL_2 over K, cuspidal without CM, with local-global
  compatibility at every place and L(E/K,s) = L(pi_E,s-1/2). Claims checked
  only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

Let $K$ be an imaginary quadratic field and $E/K$ an elliptic curve. For a
prime $l$ and a field isomorphism $\iota:\overline{\mathbb Q}_l\to\mathbb C$,
write $H^1(E)=H^1_{\mathrm{et}}(E_{\overline K},\overline{\mathbb Q}_l)$ as a
representation of $G_K=\operatorname{Gal}(\overline K/K)$, and $r_\iota(\pi)$
for the semisimple $l$-adic Galois representation attached to a regular
algebraic cuspidal representation $\pi$ of $\mathrm{GL}_2$ over a CM field,
in the normalization of Harris--Lan--Taylor--Thorne, Scholze and
Caraiani--Newton (the CM case below extends it to an isobaric sum). The
manuscript
compares local parameters through the Tate-normalized local Langlands map
$\mathrm{rec}_{K_v}(\pi_v\otimes|\det|_v^{-1/2})$, with geometric Frobenius,
and calls the algebraic weight of trivial coefficients "weight zero" (Section
2, p. 4).

**Theorem 1.1.** There is an isobaric automorphic representation $\pi_E$ of
$\mathrm{GL}_2(\mathbb A_K)$, of weight zero and with trivial central
character, with the following properties.

- For every prime $l$ and every isomorphism $\iota$,
  $r_\iota(\pi_E)\simeq H^1(E)$.
- At every finite place $v$ of $K$ not above $l$, the Frobenius-semisimplified
  Weil--Deligne representation attached through $\iota$ to the restriction of
  $H^1(E)$ to the decomposition group at $v$ is isomorphic to
  $\mathrm{rec}_{K_v}(\pi_{E,v}\otimes|\det|_v^{-1/2})$.
- At the complex place the unitary parameter is
  $z\mapsto\operatorname{diag}(z/|z|,\bar z/|z|)$.
- Hence all local factors match, and $L(E/K,s)=L(\pi_E,s-1/2)$.
- When $E$ is without complex multiplication, $\pi_E$ is cuspidal. If $E$
  has CM, $\pi_E$ is the automorphic induction of a Hecke character, or an
  isobaric sum of two Hecke characters when the CM field is $K$ itself; in
  that last case $r_\iota(\pi_E)$ means the sum of the two characters'
  realizations, with the same Tate normalization (p. 1).

No hypothesis is placed on $K$, on the reduction of $E$, or on its residual
representations. The manuscript presents this as the modularity conjecture
for elliptic curves over imaginary quadratic fields, removing the remaining
restrictions left by Caraiani and Newton, whose results covered, among other
cases, every elliptic curve over an imaginary quadratic $K$ for which
$X_0(15)(K)$ has rank zero (p. 2). The theorem concerns modularity only: it
states nothing about ranks, Selmer groups or the Birch--Swinnerton-Dyer
conjecture over $K$. The last paragraph of the proof (p. 28) adds that the
finite local factors also agree when the Weil--Deligne representation is
taken at the residue-characteristic coefficient prime.

**Source.** OpenAI, *Modularity of elliptic curves over imaginary quadratic
fields*, release folder
`preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026`;
TeX file `build/sections/introduction.tex`, label `thm:main` (lines 17--43),
PDF p. 1; the proof runs through Sections 3--9 and closes at the end of
Section 9 (`build/sections/automorphy.tex` line 254, PDF p. 28). Read
2026-10-12. Provenance and attestations are on
[[number_theory/openai_2026_modularity_elliptic_curves_imaginary_quadratic_fields/_index|the card]].

**Read depth.** Claims checked: the statement and the conventions of Section
2 it rests on (`build/sections/conventions.tex` lines 1--39), and the
statements of Corollary 5.4 (the congruence chain), Definition 6.1
(decomposed genericity), Theorems 6.2--6.4 (the Caraiani--Newton inputs as
the manuscript specializes them), Proposition 8.4 (the specialization),
Proposition 9.3 (modularity of the twist over $F$) and Lemma 9.4 (cyclic
descent) were read clause by clause in the TeX source. Whether Theorems
6.2--6.4 follow from the cited results of Caraiani and Newton was not
checked against their preprint. The proof (Sections 3--9, pp. 4--28) was
read for its structure only, as summarized below; no step was checked.
Nothing here is independently reviewed.

## Proof pointer

The CM case is classical: the main theorem of complex multiplication writes
$H^1(E)$ over $KM$, with $M$ the CM field, through algebraic Hecke
characters, and the manuscript takes automorphic induction from $KM$ to $K$
when $M\ne K$ and the isobaric sum when $M=K$ (Section 9.4, pp. 27--28). The
work is the non-CM case, which proceeds by moving automorphy along a chain of
congruences between rank-two pieces of the cohomology of one curve.

Fix a prime $p>100$ for which the image of $G_K$ on $E[p]$ contains
$\mathrm{SL}_2(\mathbb F_p)$, put $n=3p$ and $F=K(\mu_n)$, a CM field without
$\zeta_5$. For a parameter $t$ the manuscript builds a genus-$n$ cyclic cover
$C_n(t)$ of the quadratic twist $B_t:h(t)y^2=h(x)$ of $E:y^2=h(x)$, totally
ramified over $\pm S_t$, where $S_t=[n](t,1)$ on $B_t$, and nowhere else,
with an involution $w$ that conjugates each rotation to its inverse
(Section 3). A slit description over $\mathbb C$ shows that its integral
$H^1$ is free of rank two over the group ring of $\mu_n$ (Proposition 4.2),
so evaluating at a character $\theta$ gives a stable lattice in a rank-two
piece $V_\theta$ whose reduction depends only on the reduced character
(Lemma 5.3).
Each $V_\theta$ has determinant $\epsilon_\ell^{-1}$ and Hodge--Tate weights
$0,1$ and forms a compatible system (Proposition 5.1). The trivial character
gives $H^1(B_t)$, and an order-three character $\eta$ gives $H^1$ of an
elliptic curve $A_t$ over $F$ (Proposition 5.2). With $\chi=\psi\eta$ of order
$3p$ the reductions match along
$V_\eta\equiv V_\chi\pmod p$, $V_\chi\equiv V_\psi\pmod 3$,
$V_\psi\equiv V_1\pmod p$ (Corollary 5.4): two characters that differ by a
character of $\ell$-power order agree modulo $\ell$.

The parameter $t$, a point of the open set $U\subset\mathbb A^1_K$ on which
the construction is defined, is then chosen so that every lifting hypothesis
holds. Locally at the places above $3p$, the compact-type degeneration to $E^n$
(Proposition 3.3) and local constancy of the semistable reduction type
(Proposition 7.3) make the Jacobian of $C_n(t)$ ordinary, of slope $1/2$ or
totally toric exactly as $E$ is, for all character pieces at once
(Proposition 7.5, Corollary 7.6; in the toric case the full-rank monodromy
of Lemma 7.4 splits as rank one on each piece). Globally, two
Picard--Lefschetz operators from a second degeneration (Theorem 4.5) give
absolute irreducibility and a regular semisimple element on every nontrivial
character space of the degree-$3$ cover mod $5$ and mod $p$ and of the
degree-$p$ cover mod $3$ (Lemma 8.1); Hilbert irreducibility for the Weil
restriction $\operatorname{Res}_{K/\mathbb Q}U$, an open subset of the plane
over $\mathbb Q$, keeps these elements for one $t\in U(K)$ inside the local
opens, and Chebotarev then gives decomposed genericity at all places above a
split rational prime, for both conjugate families together (Lemma 8.3,
Proposition 8.4). The
trivial character is handled by the large image of $E$ and of its Galois
conjugate (Lemma 8.2), and $A_t$ is shown to have no CM.

Automorphy then propagates (Proposition 9.3). Caraiani--Newton's mod-$5$
starting theorem (Theorem 6.3) makes $A_t$, hence $V_\eta$, modular over
$F$; their lifting theorem in the specialized form of Theorem 6.2 is applied
three times, $V_\eta\to V_\chi$ at $p$, $V_\chi\to V_\psi$ at $3$ and
$V_\psi\to V_1=H^1(B_t)$ at $p$. Lemma 9.1 moves automorphy between
coefficient primes, and Lemma 9.2 checks the local alternative at each place
above the lifting prime: zero automorphic monodromy in the potentially good
cases, and a quadratic or trivial twist of Steinberg, hence ordinary, in the
totally toric case. Lemma 9.4 descends along a tower of cyclic prime-degree
steps from $F$ to $K$ by cyclic base change, using absolute irreducibility
of $H^1(B_t)$ over $F$; twisting by the quadratic character of $h(t)$ returns
from $B_t$ to $E$. Theorem 6.4 gives trivial central character and the local
parameters at every finite place, the archimedean classification gives the
complex parameter, and the final paragraph treats the residue-characteristic
coefficient prime (pp. 27--28).

## Dependencies

External inputs, taken at statement level; none was checked here.
Caraiani and Newton, *On the modularity of elliptic curves over imaginary
quadratic fields*, arXiv:2301.10509v3 (Definition 2.1.27, Theorem 5.2 with
Remark 5.2.2, Theorem 6.1, Lemma 6.1.3), used in the specialized forms of the
manuscript's Theorems 6.2--6.4, and Geraghty's Lemma 5.6 through their Lemma
6.1.3(4); the Galois representations of Harris--Lan--Taylor--Thorne and
Scholze; Varma's local-global compatibility away from $l$ (Theorem 1);
Serre's open image theorem (Section 4.4, Théorème 3); Hilbert
irreducibility with weak approximation (Serre, *Topics in Galois Theory*,
Proposition 3.3.1 and Theorem 3.5.3); Faltings's semisimplicity theorem;
Tsuji's semistable comparison and Coleman--Iovita; Bloch--Kato's description
of the crystalline Kummer classes (Example 3.9); Grothendieck's semistable
reduction and monodromy pairing (SGA 7 I, Exposé IX) and the
Picard--Lefschetz formula (SGA 7 II, Exposé XV); the relative Picard results
of Bosch, Lütkebohmert and Raynaud (*Néron models*, Section 9.4 Theorem 1 and
Section 9.2 Proposition 10); cyclic base change (Langlands; Arthur and
Clozel); and the theory of complex multiplication of Shimura and Taniyama.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using this theorem.
