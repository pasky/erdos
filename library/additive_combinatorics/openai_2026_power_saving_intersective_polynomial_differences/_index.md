---
name: additive_combinatorics/openai_2026_power_saving_intersective_polynomial_differences
desc: |
  A 47-page manuscript of the OpenAI mathematics release claiming that, for
  each degree k >= 2, every subset of {1, ..., N} with no difference equal to
  a nonzero value h(n), n >= 1, of an intersective integer polynomial h of
  degree k with positive leading coefficient has O_h(N^(1-c_k)) elements,
  with c_k > 0 depending only on k; it names no Erdős problem.
license: Apache-2.0
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

# additive_combinatorics/openai_2026_power_saving_intersective_polynomial_differences

[[additive_combinatorics/_index|..]]

[[additive_combinatorics/openai_2026_power_saving_intersective_polynomial_differences/theorem_1_1|theorem_1_1]]: The manuscript's main claim: for each degree k >= 2 an exponent c_k > 0,
depending only on k, such that subsets of {1, ..., N} with no difference
equal to a nonzero value h(n), n >= 1, of an intersective h of degree k with
positive leading coefficient have at most C_h N^(1-c_k) elements. Claims
checked only.

***

OpenAI, *A power saving for intersective polynomial differences with an exponent
depending only on the degree*, OpenAI Math Release preprint, October 5, 2026.
Released under the Apache License 2.0 at <https://github.com/openai/math>
(revision fd4aeeb2e), folder
`preprints/A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026`;
the held PDF, `power-saving-intersective-polynomial-differences.pdf` in the
release, is retained as
[openai_2026_power_saving_intersective_polynomial_differences.pdf](openai_2026_power_saving_intersective_polynomial_differences.pdf),
and the release's TeX bundle in that folder is the TeX source cited on this
card. The license term was read in the release's root `LICENSE` file at that
revision on 2026-10-12.

```bibtex
@misc{OAI:A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026,
  author = {{OpenAI}},
  title = {{A power saving for intersective polynomial differences with an exponent depending only on the degree}},
  howpublished = {OpenAI Math Release preprint
                  \href{https://github.com/openai/math/blob/main/preprints/A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026/power-saving-intersective-polynomial-differences.pdf}{OAI:A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026}},
  year = {2026}
}
```

The held PDF has 47 pages with a text layer; its title page is dated October
5, 2026 and its metadata records a creation date of 6 October 2026. The TeX
source is `build/manuscript/main.tex` (75 lines), which inputs seven section
files under `sections/` (`introduction.tex`, `local.tex`, `tuples.tex`,
`lifts.tex`, `kernel.tex`, `transfer.tex` and `induction.tex`), the third of
which inputs one figure file, `figures/list-regrouping.tex`; that is 3,566 TeX
lines in all, with a 14-entry bibliography `references/references.bib`.
`main.tex` also inputs a `glyphtounicode-cmex` file that the bundle does not
include. The bundle is the text read here.

**Attestation.** The release README states that the manuscripts were
"produced by an internal OpenAI model", that the collection "includes results
at different stages of verification", that "Not all have accompanying Lean
formalizations" and that "Some of the unformalized results could have
issues". Its account of the method says that "The vast majority of results
were obtained with the same procedure using an unreleased internal OpenAI
model", each using on average "three hours of ChatGPT Pro thinking compute";
the exceptions it names (a zero-free region for the Riemann zeta function and
the Hodge conjecture for CM abelian varieties) concern other families.
The manuscript's own README carries only the title, author ("OpenAI"), date
and citation block and adds no sentence about authorship or assistance. The
title page names OpenAI as the sole author, and the PDF has no
acknowledgment, affiliation or funding note. These are the source's own
statements, recorded as attestations and not as this corpus's review. No
refereed publication, arXiv version or independent review of the manuscript
is recorded here, and nothing on this card is independently reviewed.

**Formalization.** The release lists no formalization of this manuscript.
Its family's Lean page, `lean/docs/182.md`, carries the family's title but
names as its accompanying paper only the square-difference-free companion
below; its one comparator, `lean/ComparatorChallenges/SquareDifference.lean`
(theorem `OAI.SquareDifference.power_saving`), states, in words, that there
are reals $c>0$ and $C$ such that every finite set of integers in $[1,N]$,
$N\ge1$, with no difference $a-b$ equal to $m^2$ for an integer $m\ge1$, has
at most $CN^{1-c}$ elements. That is the square case only, not Theorem 1.1
here. The release's catalog `lean/formalization.yaml` lists no entry for
either manuscript at this revision, and its `status.main_results` names no
comparator of this family. All of this is read statically from the release;
nothing was built, replayed or audited in this repository.

**Companions.** The release groups this manuscript in its family, "Power
savings for intersective polynomial differences and prime arguments", with two
others. *A power saving for square-difference-free sets* (September 24, 2026),
filed at
[[additive_combinatorics/openai_2026_power_saving_square_difference_free_sets/_index|the square-difference card]],
claims absolute constants $c>0$ and $C$ with $|A|\le CN^{1-c}$ for every
$A\subseteq\{1,\ldots,N\}$ with no nonzero square difference; this manuscript
cites it (its Theorem 1.1) as the immediate predecessor of its method and says
it adapts that paper's reflection-positive tuple laws and signed multilinear
functional, with all required proofs included. An observation of this card, not
a claim of either manuscript: the case $h(x)=x^2$ of Theorem 1.1 here has
exactly that hypothesis, and with the trivial bound $|A|\le N$ for $N<N_h$ it
gives a bound of that form for every $N\ge1$. *A Power Saving for Polynomial
Differences at Prime Arguments* (October 5, 2026), filed at
[[additive_combinatorics/openai_2026_power_saving_polynomial_differences_prime_arguments/_index|the prime-argument card]],
claims in its abstract, which the release's manuscript map `CONTENTS.md`
repeats, a power saving $|A|\le C_hN^{1-c_h}$ for sets whose differences avoid
the nonzero values $h(p)$ at primes $p$, for $h$ of degree at least two with
positive leading coefficient and a unit root modulo every positive integer, with
$c_h$ and $C_h$ depending on $h$, obtained through a companion zero-free
half-plane for Dirichlet $L$-functions. Its introduction (p. 2) calls this
manuscript its "direct methodological predecessor" and says it adapts this
manuscript's tuple laws, Fourier lifts, signed kernels and contracting induction
to prime arguments; this manuscript does not cite it. The release holds no
earlier dated version of this manuscript. The companions' arguments were not
read for this card.

Read status: claims checked for Theorem 1.1, read clause by clause in the
release's TeX source together with the definition of an intersective
polynomial and the notation it uses (`sections/introduction.tex`, label
`thm:main` at lines 14--26, definitions at lines 3--12, remarks at lines
28--31); also read clause by clause were the statements of Condition (U) and
Lemmas 2.1 and 2.2 (`sections/local.tex`, labels `local:unit-condition` at
lines 57--61, `local:normalization` at lines 66--84 and `local:family` at
lines 147--172), Corollary 4.6 (`sections/lifts.tex`, `lift:density` at lines
601--612) and Propositions 7.1 and 7.2 (`sections/induction.tex`,
`induction:recurrence` at lines 23--44 and `induction:decay` at lines
168--182). The statements of the other numbered results named under Contents
were read in their TeX files; the proofs were read for their structure only
and no step was checked; nothing here is independently reviewed.

## Contents

The numbering below is the PDF's (results are numbered within sections in
one sequence); the title page, abstract and table of contents occupy
pp. 1--2.

- Section 1, Introduction (pp. 2--5). Calls $h\in\mathbb Z[x]$ intersective
  when it has a root modulo every integer $q\ge1$. The condition is
  necessary, since without a root modulo $q$ the multiples of $q$ form a set
  of positive density whose differences all miss $h(\mathbb N_+)$, and it
  does not require a rational root. States
  [[additive_combinatorics/openai_2026_power_saving_intersective_polynomial_differences/theorem_1_1|Theorem 1.1]]
  (p. 2) and remarks that its constants may depend on every coefficient of
  $h$ while the exponent depends only on the degree. The history cites
  Furstenberg and Sárközy for square differences, Kamae and Mendès France for
  intersective polynomials, Pintz, Steiger and Szemerédi, Bloom and Maynard
  ($N(\log N)^{-c\log\log\log N}$ for squares), Lucier, Rice, Arala (the
  Bloom--Maynard bound for every intersective polynomial of degree at least
  two), Green and Sawhney ($N\exp(-c\sqrt{\log N})$ for squares, their
  Theorem 1.1) and Adajar et al. (arXiv:2605.16216v2, Theorem 1.1:
  $N\exp(-c_{h,\mu}(\log N)^\mu)$ for every fixed intersective $h$ and
  $0<\mu<1/2$), and the release's square-difference manuscript as the
  immediate predecessor, with Hatami and Conlon--Lee for related reflection
  arguments. The overview (pp. 3--5) names the five steps that the later
  sections carry out, and the notation subsection (p. 5) fixes the
  uniformity conventions: a bound written $O_k$ is uniform over all data of
  degree $k$ satisfying the unit condition of Section 2.
- Section 2, auxiliary polynomials and local estimates (pp. 5--12). Fixes a
  compatible root $\mathfrak z_p\in\mathbb Z_p$ of $h$ at every prime, with
  multiplicity $m_p$ and first nonzero Taylor coefficient $b_{m_p,p}$ there,
  a unit for all but finitely many $p$; Condition (U) asks that it be a unit
  at every prime. Lemma 2.1 (p. 6) normalizes: $g(x)=h(r+D_0x)/M$ is an
  intersective integer polynomial of degree $k$ with positive leading
  coefficient satisfying (U), with $Mg(n)=h(r+D_0n)$ and $r+D_0n\ge1$ for
  $n\ge1$.
  Following Lucier's auxiliary-polynomial construction (Section 8 of his
  paper), it defines the completely multiplicative $\lambda$ with
  $\lambda(p)=p^{m_p}$ and $h_l(x)=h(r_l+lx)/\lambda(l)$; Lemma 2.2 (p. 7)
  says each $h_l$ is an intersective integer polynomial of degree $k$ with
  the same root multiplicities, keeps (U) when $h$ has it, and satisfies
  $h_l(Dx-i)=\lambda(D)h_{lD}(x)$ for some $0\le i<D$, with
  $D\mid\lambda(D)\le D^k$, so a set in a progression of step $\lambda(D)$
  avoiding $h_l$-differences becomes, in progression coordinates, a set
  avoiding $h_{lD}$-differences. With $\delta=1/(100k2^k)$ and
  $\gamma=\delta/10$, Lemma 2.3 (p. 9) bounds complete sums of $h_l$ modulo
  $p^j$ by $p^{-8\delta j}$, and over regular arguments ($h_l'\ne0$ modulo
  $p$) by $p^{-4\delta}$, for $p\ge P_1$; Lemma 2.4 (p. 10) bounds the
  derivative valuation at some small argument at each small prime. The
  admissible residues modulo $p^{E_p}$ are then defined (p. 11) as values of
  $h_l$ at arguments whose derivative valuation is within that bound when
  $p<P_1$, and at regular arguments when $p\ge P_1$; Lemma 2.5 (p. 11) is
  the uniform lifting lemma that explains this modulus;
  Lemma 2.6 (p. 11) gives $L$ admissible residues summing to zero, for one
  cycle length $L$. Under (U), $P_1$ and $L$ depend only on $k$, and each
  exponent $E_p$ only on $k$ and $p$. Rice's revised version (Sections
  2.4--2.5 and 4) is cited for similar restrictions.
- Section 3, weighted reflection-positive tuple laws (pp. 12--22). Takes
  slots $V=\Pi^w$, words of $w=2t+1$ blocks each a permutation of $[L]$, so
  $d=|V|=(L!)^{2t+1}$ is even, with reflection cuts that swap two symbols in
  one block; a law on $\mathbb F_p^V$ is reflection positive when every cut
  matrix is positive semidefinite. The edge weight counts the regular
  arguments $x$ with $h_l(x)=y$ in $\mathbb F_p$, divided by $k$. Lemma 3.1
  (p. 13) is a graph-counting and list-mixing bound; measures indexed by
  sets of marked blocks are compared in Lemmas 3.2--3.4 (pp. 15--16).
  Proposition 3.5
  (p. 17): for large $p$, uniformly in $l$, a mixture $\mu_{l,p}$ is a
  reflection-positive, translation-invariant probability law with uniform
  single-slot marginals, and outside an exceptional part of mass at most
  $p^{-4}$ every increment along a designated $L$-cycle of slots is a value
  of $h_l$ at a regular argument. Lemma 3.6 (p. 18) is the covariance: the
  map $z\mapsto\lambda(D)^{-1}(z-a')$ carries the law for $l$ to the law for
  $lD$ when $p\nmid D$. Lemma 3.7 (p. 19) is conditional mixing with saving
  $p^{-\gamma}$, and Proposition 3.8 (p. 20) shows that the prime threshold
  $P$ and the small-prime modulus $M_0=\prod_{p<P}p^{E_p}$ depend only on
  $k$ under (U). The section adapts Lemmas 2.1--2.2 and Section 3 of the
  square manuscript.
- Section 4, multilinear estimates and Fourier lifts (pp. 22--30).
  Proposition 4.1 (p. 23) is a signed Hölder inequality for the product laws
  over a finite set of primes at least $P$, proved by repeated folding across
  cuts after the chessboard method of Fröhlich, Israel, Lieb and Simon
  (their Theorem 4.1); Lemma 4.2 (p. 24) makes its $d$th root a seminorm
  that dominates the mean, contracts under coordinate averaging and is
  carried exactly from $l$ to $lD$ by the covariance map. Lemma 4.3 (p. 24)
  gives decay $R^{-\gamma}$ when one slot has no Fourier mass at denominators
  at most $R$. Proposition 4.4 (p. 26) bounds the $L^{2r}$ norm of the
  Fourier lift of a function $f$ on an interval of length at least $10Q^6$
  (its Fourier coefficients at the frequencies whose squarefree denominators,
  at most $Q$, are built from the chosen primes, moved to the product of
  residue fields) by $C_{r,\epsilon}\|f\|_\infty Q^\epsilon$, and Lemma 4.5
  (p. 28) prices the fixing of coordinates. Section 4.4 (p. 29) fixes
  $\eta=1/(100k)$, $\zeta=\eta/(20k)$, $\nu=\eta/(10\cdot2^k)$,
  $\beta=\nu/100$, $\tau=\beta\gamma/(1000k(d+1))$ and $\sigma=\gamma\tau/4$,
  the cutoff $Q=N^\beta$ and the density quantity $Y_l(N,A)$, the
  multilinear form of the lift of $1_A$; Corollary 4.6 (p. 29) gives
  $(|A|/N)^d\le Y_l(N,A)\le C_\epsilon N^\epsilon$. The section adapts the
  square manuscript's Proposition 4.1 and Lemmas 4.2--4.3 and its two lift
  lemmas, which this manuscript cites as Lemmas 5.1--5.2; in the released
  square manuscript they are Lemmas 5.2--5.3.
- Section 5, a signed kernel for polynomial differences (pp. 30--37). The
  pair multiplier $\Gamma$ of a cycle edge satisfies
  $|\Gamma(\xi)|\le q(\xi)^{-\gamma}$. Proposition 5.1 (p. 30): for
  $l\le N^\zeta$, a modulus $D=M_0\prod_{p\in B}p\le N^\beta$ and two
  functions on $[N]$ bounded by one, supported in residue classes modulo $D$
  with admissible difference, with the first support entirely below the
  second and no difference between them in $h_l(\mathbb N_+)$, the
  $\Gamma$-weighted pair sum over squarefree denominators up to
  $H=N^{\beta/2}$ coprime to $D$, times $D$, is $\ll H^{-\gamma/2}$. The proof
  builds a signed kernel supported on positive values of $h_l$, with
  derivative weights and a truncated divisor expansion, whose Fourier
  transform matches a model kernel uniformly (Lemma 5.2, p. 32): Weyl
  differencing on the minor arcs (Lemma 5.3, p. 33) and a comparison of
  local coefficients on the major arcs (Lemma 5.4, p. 35); its bilinear form
  vanishes on avoiding pairs (Section 5.5, p. 36). It adapts Section 6 of
  the square manuscript (Proposition 6.1).
- Section 6, comparison and cancellation (pp. 37--42). Defines the maximal
  functional $\mathcal Y_l(N)$, the largest $Y_l(N,A)$ over $A\subseteq[N]$
  avoiding nonzero $h_l$-differences. Lemma 6.1 (p. 37): fixing prime
  coordinates of a lift restricts to a residue class. Proposition 6.2
  (p. 38) bounds, uniformly in $l$, the multilinear form of lifts with the
  prime coordinates in $B$ fixed, for $q_B\le N^\tau$, by
  $\Lambda_B^d\mathcal Y_{lD}(n_B)+O(N^{-\sigma})$ at the shorter scale
  $n_B=\lceil N/\lambda(D)\rceil$, $D=M_0q_B$, with
  $1\le\Lambda_B\le1+M_0^kN^{k\tau-1}$. Lemma 6.3 (p. 39): the residue
  assignments modulo $M_0$ whose cycle increments are admissible have
  proportion at least $\rho_*=M_0^{1-L}$. Proposition 6.4 (p. 40): for these
  and $l\le N^\zeta$, the integral against the nonexceptional laws is
  $\ll N^{-\sigma}$, by locating an ordered cycle edge and applying
  Proposition 5.1. The section adapts Sections 7--8 of the square
  manuscript, whose comparison and contraction results this manuscript cites
  as Propositions 7.2 and 8.1; in the released square manuscript they are
  Propositions 7.2 and 8.2.
- Section 7, exceptional terms and the power-saving induction (pp. 42--46).
  Proposition 7.1 (p. 42) is a recurrence bounding $\mathcal Y_l(N)$, for
  $l\le N^\zeta$, by $C_1N^{-\sigma}$ plus $1+u_N$ times a sum, with weights
  $1-\rho_l$ and $\rho_l\eta_{l,B}$, of values $\mathcal Y_{lD_B}(n_B)$ at
  shorter scales, where $u_N\to0$ and the exceptional masses $\eta_{l,B}$
  sum to at most $1/4$. Proposition 7.2 (p. 44) gives
  $\mathcal Y_l(N)\le C_0l^{b_0}N^{-a_0}$ for all positive $l,N$, with $a_0$,
  $b_0$ explicit in $k,\zeta,\sigma,M_0,\rho_*$ and depending only on $k$
  under (U). The proof of Theorem 1.1 (pp. 45--46) sets $c_k=a_0/d$. The
  section adapts the square manuscript's recurrence and decay results, which
  this manuscript cites as Proposition 9.2 and Theorem 9.3; in the released
  square manuscript they are Proposition 9.1 and Theorem 9.2.
- References (p. 47): fourteen entries, eleven with DOIs and three as arXiv
  versions or a release citation (Green--Sawhney, Adajar et al., the square
  manuscript).

The manuscript flags nothing as numerical, computer-assisted or
conditional, and it states that all estimates it needs from the
reflection-positive method are proved in the text. All structural
parameters are explicit functions of $k$ except the prime thresholds $P_1$
and $P$, fixed only as large enough in terms of $k$; no numerical value of
$c_k$ is given.
The release folder for this manuscript holds only the PDF, the TeX build
directory and the README; there is no `verification/` folder.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using it. The problem pages found by searching for square and polynomial
differences concern other objects: Problems 438 and 439 ask about squares
among sums of two elements, and Problem 894 about differences lying in a
lacunary sequence; Theorem 1.1 says nothing about either kind of set.
