---
name: research/leads/equilateral_two_scale/rigidity_extension
title: Haar rigidity on a one-parameter real-closed plane
desc: |
  The function-field unit template replaces the number-field selection in
  the wild-character rigidity proof. The other steps use countability,
  real closedness and divisibility of the rotation group. This gives the
  residual-correlation vanishing required for two-scale binary transfer.
created: 2026-10-17T03:25:00Z
updated: 2026-10-17T03:25:00Z
---

***

Theorem 2, Corollary 3 and their field specialization are covered by the
[[research/leads/equilateral_two_scale/evidence/verify/whole_conclusion/grade|graded whole-conclusion review]].
The project argument is credited to Plasma AI. It adapts the prose proof
in Sections 2 and 3 of the
[[../library/discrete_geometry/openai_2026_euclidean_plane_not_five_colorable/_index|OpenAI plane-coloring manuscript]],
at its September 23, 2026 version, external release revision adc7f1241.
Those sections were read at proof depth for
this use. The new input is Theorem 1 of
[[research/leads/equilateral_two_scale/unit_templates|the finite-cover
account]]. No Lean formalization of this extension is asserted, and the
recorded standing of the separate algebraic Lean interface (R0) is not
changed by this argument.

Let $x>0$, let $F_x$ be the real closure of $\mathbb Q(x)$ inside
$\mathbb R$, put $L=F_x(i)$ and $K_x=\{u\in L:|u|=1\}$, and write
$D=\widehat{L_{\rm disc}}$. Let $C\subset D$ be the characters continuous
for the usual topology of $L\subset\mathbb C$.

**Theorem 2.** Every $K_x$-invariant Borel probability measure on $D$
giving $C$ measure zero is Haar probability on $D$.

**Corollary 3.** In a unitary representation of $L$ with covariant
$K_x$-rotations, let $f$ be rotation fixed and let $P$ be the orthogonal
projection onto the vectors continuous under translations in the usual
topology. Then

$$
\langle f,T_zf\rangle=\langle Pf,T_zPf\rangle
\qquad(z\in L\setminus\{0\}).
$$

*Deduction of the corollary.* The translation spectral measure of $f$ is
$K_x$-invariant. Its restriction to $C^c$, if nonzero, is a multiple of
Haar measure by Theorem 2. The spectral measure of $Pf$ is its restriction
to $C$: this is the spectral characterization of continuous vectors,
proved by extending continuous positive-definite coefficients from $L$
to $\mathbb C$, applying Bochner's theorem, and using Fourier uniqueness
on $D$. Haar coefficients vanish at nonzero $z$, giving the identity.

## Field hypotheses for the source lemmas

The field $L$ is countable and dense in $\mathbb C$, and $F_x$ is a dense
real-closed subfield of $\mathbb R$. Thus $D$ is compact metrizable. The
ordinary frequency map $\mathbb R^2\to D$ is continuous and injective;
its compact exhaustion makes $C$ and the inverse parametrization Borel.
Multiplication by a nonzero element of $L$ preserves $C$.
The group $K_x$ is countable abelian and divisible, since every complex
root of a unit lies in the algebraically closed field $L$ and is a unit.
It acts orthogonally on ordinary frequency parameters.

Here are the retained source lemmas, their roles and the field-dependent
points in their proofs. They are used with $F_x,L,K_x,D,C$ in place of
the manuscript's $F,E,K,D,C$.

- **Lemma 2.4, null cosets and real-line events.** A positive-mass coset
  of $C$ has finite rotation orbit. Divisibility makes that orbit trivial;
  one rotation $u\ne1$ then forces the coset to be $C$. Two independent
  samples therefore have a difference outside $C$ almost surely.
  For the event that a character is continuous on a real line $aF_x$,
  two nonparallel lines give an $F_x$-basis of $L$, so their intersection
  is contained in $C$. Infinitely many rotated lines make each line
  event null. These arguments use no algebraicity over $\mathbb Q$.
- **Lemma 2.5, vanishing line averages.** An invariant mean on
  $F_x/\mathbb Z$ defines a positive translation-invariant functional $I$
  on bounded, boundedly supported functions on $F_x$. It agrees with
  Lebesgue integration on restrictions of continuous compactly supported
  functions. For a wild law $\nu$,
  $I(\phi(t)\widehat\nu(at))=0$ for $a\ne0$ and $\phi\in C_c(\mathbb R)$.
  The proof convolves the multiplication representation with $\phi$ using
  $I$; the resulting vector is continuous on the real line and hence zero
  by the preceding null event. Density of $F_x$ permits the Bochner
  extension to $\mathbb R$; countability and amenability provide all the
  means and Borel spaces used.
- **Lemmas 2.6 and 2.7, centers and relative singularity.** Lemma 2.6 is
  solely a Borel, translation- and orthogonally-equivariant location rule
  for probability measures on $\mathbb R^2$. Lemma 2.7 uses it to turn
  a positive-mass conditional $C$-coset into finitely many equivariant
  centers, then contradicts compact approximation by conditional phase
  collisions. Its induction uses the null-coset and line-average lemmas.
  The only additional field operation in the collision argument is, for
  $t\in F_x$ with $|t|<2$, the decomposition
  $t=(t/2+i\sqrt{1-t^2/4})+(t/2-i\sqrt{1-t^2/4})$ into two units.
  Real closedness supplies it. Small test parameters are chosen by the
  invariant line mean, with all finite test counts fixed first, so no
  rational or algebraic choice of those parameters is required.
- **Lemma 3.1, compact tower.** This is a countable-group construction on
  a standard probability space. Invariant Hilbert--Schmidt kernels on a
  nonergodic relative product produce finite-rank modules; adjoining their
  bounded bases gives the prescribed compact approximation at a successor.
  Separability stops the increasing tower at a countable ordinal, with
  ergodic relative product. No field coordinates enter the proof.
- **Lemma 3.2, conditional multiple averages.** The relative-product
  argument, its finite-set van der Corput estimate and its every-Følner
  conclusion use only a countable divisible abelian group. In particular
  nonzero power maps have the same invariant vectors as the full action,
  and translates of Følner sequences remain Følner. These properties hold
  for $K_x$.
- **Lemma 3.3, radial identities.** Equal nonzero moduli in $L$ differ by
  a member of $K_x$. The polynomial identity in its proof uses
  $\sqrt{AB}\in F_x$ for $A,B>0$ and the exponents $0,1,2$; its circle
  average uses exponents $1,-1$. Real closedness and the preceding
  multiple-average lemma provide exactly these inputs.
- **Lemma 3.5, addition under a cap.** This is a finite manipulation of
  nonnegative real numbers and a difference inequality, so it holds on
  $F_x$ without further field assumptions.

The source's Lemma 3.4 is not retained over $L$: a finite number field
need not contain the cover rotations. The next section replaces that
selection step, including its uniform bounds.

## The radial function and the replacement selection

First suppose the wild law $\mu$ is ergodic under $K_x$. Let $Y$ be the
terminal factor of Lemma 3.1 and $P_Y$ its conditional expectation.
For the character coordinate $\psi_z(d)=d(z)$ put

$$
g_z=P_Y\psi_z,\qquad m(z)=\|g_z\|_2^2.
$$

Conditional independence identifies $m$ as the Fourier transform of the
relative difference law over $Y$. That law is wild by Lemma 2.7.
The function $m$ is radial, takes values in $[0,1]$, and has $m(0)=1$.
With $w(r)=-\log m(r)$, Lemma 3.3 gives

$$
w(|A-B|)\le w(A)+w(B),\qquad
\operatorname{Avg}_{u\in\Phi_n}m(2r|\operatorname{Re}u|)
\longrightarrow m(r)^2
$$

for $A,B,r\in F_x$, $A,B\ge0$, $r>0$, and every Følner sequence in
$K_x$. These are the manuscript's equations (3.12) and (3.13).

Suppose $m(r)>0$. Choose finite $H>0$ with $e^{-H}<m(r)^2$. The set

$$
Z=\{u\in K_x:w(2r|\operatorname{Re}u|)\le H\}
$$

is syndetic. Otherwise one could translate each set of a Følner sequence
to avoid $Z$, contradicting the every-sequence average. Choose a finite
cover $Q=\{q_1,\ldots,q_J\}$ with
$K_x=\bigcup_jq_j^{-1}Z$.

There is a finite $\Sigma\subset K_x$ such that every choice of one
$q_j s$ for each $s\in\Sigma$ has rational span containing $1$ and $i$.
For transcendental $x$, this is Theorem 1 of the finite-cover account,
followed by the algebraic-to-rational coefficient reduction in
Propositions 6--8 of the transcendental account. For algebraic $x$,
$L=E$; take a number field containing $i$ and $Q$, and use the original
Lemma 3.4 and pigeonhole. This uses the number-field argument only where
its hypotheses hold.

For each $v\in K_x$, choose at each $s\in\Sigma$ a multiplier $q_j$
with $q_j s v\in Z$, and call the resulting finite set of $q_j s$ a
selection $\mathcal T$. There are finitely many selections. Clear the
rational denominators of expressions for $1$ to obtain a common positive
integer $D_0$ and finite $M_0$ such that every selection has an expression

$$
D_0=\sum_{k\in\mathcal T}a_k k,
\qquad a_k\in\mathbb Z,
\qquad \sum_k|a_k|\le M_0.
$$

Because its rational span contains both $1$ and $i$, every selection
also has a positive lower bound for
$\max_{k\in\mathcal T}|\operatorname{Re}(kv)|$ as $v$ ranges over the
ordinary unit circle. Compactness and the finite number of selections
give one common $c_0>0$, which may be decreased to be at most one.

For $v\in K_x$ with $|\operatorname{Re}v|<c_0/D_0$, the numbers
$p_k=2r|\operatorname{Re}(kv)|$ of its selection satisfy $w(p_k)\le H$
and $p=\max p_k\ge2rc_0$. Taking real parts in the expression for
$D_0$, and adjusting signs, expresses
$z=2rD_0|\operatorname{Re}v|<p$ as an integer combination of the $p_k$
with coefficient length at most $M_0$. Lemma 3.5 gives $w(z)\le4M_0H$.
Every $t\in F_x\cap[-1,1]$ is the real part of
$t+i\sqrt{1-t^2}\in K_x$. Hence

$$
m(s)\ge e^{-4M_0H}>0\qquad(0<s<2rc_0, s\in F_x).
$$

Choose a nonnegative continuous test function with positive integral
supported in this interval. Positivity of $I$ makes its $I$-integral
against $m$ positive, contradicting Lemma 2.5 for the wild relative
difference law. Thus $m(z)=0$ for every $z\ne0$.
Since $|\widehat\mu(z)|\le\|g_z\|_2$, all nonzero Fourier coefficients
of $\mu$ vanish. Fourier uniqueness identifies $\mu$ with Haar measure.
Finally ergodically decompose an arbitrary wild invariant law. Almost
every component is still wild, since $C$ is invariant Borel. The ergodic
conclusion applies to each component and proves Theorem 2. $\square$

## Composition with the triangle argument

The proof of the
[[research/leads/equilateral_two_scale/binary_transfer|binary transfer]]
uses only a countable dense carrier containing the placed triangle
vertices, its dense rotation group, and the correlation identity of
Corollary 3. For the equilateral triangles of sides $1$ and $x$, these
vertices lie in $L$. It therefore yields a weakly avoiding measurable
two-coloring from any arbitrary coloring avoiding both sides, for every
real $x>0$. Theorem 4 of the
[[research/leads/equilateral_two_scale/circle_exclusion|circle account]]
excludes such a measurable coloring when $x\ne1$. The reduction through
Jelínek et al., Lemma 1.3 and Corollary 1.4, stated on the
[[research/leads/equilateral_two_scale/_index|canonical whole proof sketch]],
then gives the full triangle conclusion. The graded whole-conclusion
review covers this composition, including the template, source-lemma
extension, measurable argument and exact conclusion. It supplies no Lean
fidelity or catalog-status decision.
