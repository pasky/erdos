---
name: number_theory/openai_2026_fontaine_mazur_modularity_prime_2/theorem_1_1
title: "Theorem 1.1: every odd, irreducible, finitely ramified two-dimensional 2-adic representation of G_Q that is de Rham at 2 with distinct Hodge-Tate weights is modular up to Tate twist"
desc: |
  The manuscript's main claim: the odd, regular two-dimensional Fontaine-Mazur
  conjecture over Q at the prime 2, with no hypothesis on the residual
  representation, scalar and reducible residues included. Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

Let $G_{\mathbb Q}$ be the absolute Galois group of $\mathbb Q$ and $\epsilon$
the $2$-adic cyclotomic character. The manuscript calls a continuous
representation $r:G_{\mathbb Q}\to\mathrm{GL}_2(\overline{\mathbb Q}_2)$ odd
if $\det r(c)=-1$ for a complex conjugation $c$, and regular de Rham at $2$ if
its restriction to $G_{\mathbb Q_2}$ is de Rham with two distinct
Hodge--Tate weights (p. 1).

**Theorem 1.1.** Let $r:G_{\mathbb Q}\to\mathrm{GL}_2(\overline{\mathbb Q}_2)$
be continuous and irreducible. Assume that $r$ is odd, that it is unramified
at all but finitely many primes, and that it is de Rham at $2$ with distinct
Hodge--Tate weights. Then there are a classical cuspidal eigenform $f$ and an
integer $n$ such that $r$ is isomorphic to $V_f\otimes\epsilon^n$, where $V_f$
is the $2$-adic Galois representation attached to $f$.

No hypothesis is placed on the residual representation: the manuscript says the
theorem covers every semisimple residual representation, "including scalar and
reducible ones" (p. 1). It fixes the normalization in Section 2.1 (p. 8): for a
primitive form $f$ of weight $k$ and nebentype $\psi_f$, $V_f$ has trace
$a_q(f)$ at the arithmetic Frobenius of each good prime $q$, determinant
$\psi_f\epsilon^{k-1}$ and cyclotomic exponents $\{0,k-1\}$ (the negatives of
its Hodge--Tate weights, since $\epsilon$ has Hodge--Tate weight $-1$); a
realization of $r$ through the dual is converted to this form by
$V_f^\vee\simeq V_g\otimes\epsilon^{1-k}$, with $g$ the primitive form attached
to $f\otimes\psi_f^{-1}$. Read off from that normalization, and not part of the
theorem's wording: the weight $k$ of $f$ is one more than the gap between the
two Hodge--Tate weights of $r$.

The manuscript reads the theorem as settling the odd, regular two-dimensional
Fontaine--Mazur conjecture over $\mathbb Q$ at $2$, and says that together with
Pan (2022) and Zhang (2025) at odd primes it gives the modularity conclusion
at every prime (p. 1).

**Source.** OpenAI, *Fontaine--Mazur modularity at the prime 2*, release folder
`preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026`; TeX file
`build/sections/introduction.tex`, label `thm:main` (lines 20--30), PDF p. 1;
the proof closes in Section 8.8 (`build/sections/classicality.tex`, lines
707--758, PDF p. 67). Read 2026-10-12. Provenance and attestations are on
[[number_theory/openai_2026_fontaine_mazur_modularity_prime_2/_index|the card]].

**Read depth.** Claims checked: the statement, the definitions of odd and
regular de Rham (`introduction.tex` lines 9--18), the normalization of
Section 2.1 (`preliminaries.tex` lines 87--109), and the statements of
Lemma 2.2, Theorem 5.1, Theorem 7.1 and Lemma 8.5 were read clause by clause in
the TeX source. The proof, Sections 2--8 (pp. 7--67), was read for its structure
only, as summarized below; no step was checked. Nothing here is independently
reviewed.

## Proof pointer

The proof has three stages after a reduction. Lemma 2.2 disposes of the
virtually solvable case: the identity component of the image's Zariski closure
cannot be scalar, since the Hodge--Tate weights differ; if $r$ is induced from a
real quadratic field, the unit theorem forces equal weights; if from an
imaginary quadratic field, $r$ comes from a theta series. In every other case
the restriction of $r$ to any finite extension stays absolutely irreducible.
Section 2.1 also writes the determinant as $\chi_{\mathrm{fin}}\epsilon^w$ with
$\chi_{\mathrm{fin}}$ of finite order.

The first stage, Theorem 7.1 (Sections 3--7), puts $r$ in the pro-modular locus
over some solvable, totally real Galois extension $F$ of even degree in which
$2$ splits completely: the closed locus, in the fixed-determinant
pseudodeformation space, cut out by a completed Hecke algebra of definite
quaternionic forms over $F$, with no local condition at $2$. Its main tool is
Theorem 5.1, localized propagation: a Taylor--Wiles--Kisin patching argument run
at a characteristic-two curve with residue field $k((t))$, using finite jets
over an ultrapower, Paškūnas--Tung's block finiteness to identify the local
action on completed forms with the Galois action (Proposition 4.2), a lower
bound $1+2d$ on every Hecke component (Proposition 4.4), and character twists
with a $\pm i$ tame comparison model to obtain full support. To reach the
target, Section 6 builds abelian totally real $2$-extensions
$\mathbb Q\subset A\subset F$ of growing degree with boundedly many allowed odd
places and a strict Selmer bound, marking some dyadic places when the residue is
reducible with its two characters equal at $2$. Section 7 takes a classical
cuspidal lift of the residue (Lemma 7.2), chooses a curve in a Hecke component
through it and a curve in a deformation component containing $r$, places both
in charts whose marked local lines avoid every globally invariant line, and
uses the geometric connectedness of that transverse residual fiber (Lemma 7.5)
to propagate pro-modularity from the first curve to the second and then, by
Theorem 5.1, to the whole component.

The second stage, Section 8, extracts a locally algebraic vector with the target
eigensystem. When $r|_{G_{\mathbb Q_2}}$ is absolutely irreducible this comes
from the $p$-adic local Langlands correspondence of Colmez and of
Colmez--Dospinescu--Paškūnas, which covers the scalar residual case at $2$. When
it is reducible, the line of larger cyclotomic exponent is recorded (Lemma 8.1)
in a family $\mathscr D$ of dimension at least two (Lemma 8.2); the ordinary
part of completed forms is finite over the torus Iwasawa algebra
(Proposition 8.3), which makes $\mathscr D$ finite over a one-dimensional weight
space (Lemma 8.4). At a dense set of weights a global twist gives
representations whose duals are ordinary and potentially crystalline with
Hodge--Tate weights $\{0,1\}$, hence modular by Thorne's Theorem D (Lemma 8.5).
These points fix the order of the two characters in the ordinary induction,
which the closed joint support carries to the target; specialization gives a
genuine ordinary eigenvector (Lemma 8.6), and a polynomial-orbit argument proves
it locally algebraic (Lemma 8.7).

The third stage, Section 8.8, turns the vector into a regular algebraic
automorphic form on the definite quaternion algebra over $F$, moves it by
Jacquet--Langlands to a Hilbert cusp form whose Galois representation matches
$r|_{G_F}$, and descends along a tower of prime-degree cyclic extensions to
$\mathbb Q$, correcting the finite-character discrepancy at each step by a
Hecke-character twist; over $\mathbb Q$ the result is a classical cusp
eigenform, up to the Tate twist fixed by the weights.

## Dependencies

External inputs, taken at statement level; none was checked here. Thorne's
Theorem D (arXiv 2608.07186v1, a 2026 preprint) on ordinary potentially
crystalline representations of weights $\{0,1\}$, the key input of the reducible
local branch; Paškūnas and Tung's finiteness theorems for the blocks of mod $2$
representations of $\mathrm{GL}_2(\mathbb Q_2)$, their Theorems 1.1--1.4; the
$p$-adic local Langlands correspondence (Colmez, Theorem 0.20; Colmez,
Dospinescu and Paškūnas, Theorems 1.1 and 1.3); Serre's modularity conjecture as
proved by Khare--Wintenberger and Kisin (through Kisin's survey, Theorem 0.2)
and Billerey--Menares (Theorem 2.1) for the residual seed; Böckle, Iyengar and
Paškūnas on local deformation rings with Laurent-series residue fields
(Section 3.5); Chenevier's determinants; the Galois representations and
local-global compatibility of Barnet-Lamb, Gee, Geraghty and Taylor;
Jacquet--Langlands; cyclic base change and descent (Langlands; Arthur--Clozel,
Chapter III); Breuil--Emerton's ordinary completion formula (Proposition 2.2.1);
Bloch--Kato and Berger for the local de Rham and potentially crystalline steps.
Pan (2022), Zhang (2025), Tung (2021), Pan's 2026 classicality theorem and
Emerton, Gee, Pan and Zhu (2026) are cited as precedents or comparisons, not as
inputs.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using this theorem; see
[[number_theory/openai_2026_fontaine_mazur_modularity_prime_2/_index|the card]].
