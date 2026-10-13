---
name: additive_combinatorics/openai_2026_power_saving_polynomial_differences_prime_arguments
desc: |
  A 42-page manuscript claiming that, for a fixed integer polynomial h of
  degree at least 2 with positive leading coefficient and a unit root modulo
  every positive integer, a subset of {1,...,N} with no difference equal to a
  nonzero h(p), p prime, has at most C_h N^(1-c_h) elements; the proof takes
  the release's claimed zero-free half-plane Re s > 7/8 for Dirichlet
  L-functions as input. It names no Erdős problem.
license: Apache-2.0
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

# additive_combinatorics/openai_2026_power_saving_polynomial_differences_prime_arguments

[[additive_combinatorics/_index|..]]

[[additive_combinatorics/openai_2026_power_saving_polynomial_differences_prime_arguments/theorem_1_1|theorem_1_1]]: The manuscript's main claim: for a fixed prime-intersective integer
polynomial h of degree at least 2 with positive leading coefficient, sets
in {1,...,N} whose differences avoid every nonzero h(p), p prime, have at
most C_h N^(1-c_h) elements; the proof rests on the release's claimed 7/8
zero-free half-plane. Claims checked only.

***

OpenAI, *A Power Saving for Polynomial Differences at Prime Arguments*, OpenAI
Math Release preprint, October 5, 2026. Released under the Apache License 2.0 at
<https://github.com/openai/math> (revision fd4aeeb2e), folder
`preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026`;
the held PDF, `prime-argument-polynomial-differences.pdf` in the release, is
retained as
[openai_2026_power_saving_polynomial_differences_prime_arguments.pdf](openai_2026_power_saving_polynomial_differences_prime_arguments.pdf),
and the release's TeX bundle in that folder is the TeX source cited on this
card. The license term was read in the release's root `LICENSE` file at that
revision on 2026-10-12.

```bibtex
@misc{OAI:A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026,
  author = {{OpenAI}},
  title = {{A Power Saving for Polynomial Differences at Prime Arguments}},
  howpublished = {OpenAI Math Release preprint
                  \href{https://github.com/openai/math/blob/main/preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026/prime-argument-polynomial-differences.pdf}{OAI:A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026}},
  year = {2026}
}
```

The held PDF has 42 pages with a text layer; its title page is dated October
5, 2026, and its metadata records no creation date (the TeX source sets the
pdfTeX switch that omits the date fields). The TeX source is
`build/main.tex` with seven section files under `build/sections/` and one
TikZ figure file, 3,171 lines in all, and the bibliography
`build/references.bib` (316 lines, 27 entries); it is the text read here.

**Attestation.** The release README states that the manuscripts were
"produced by an internal OpenAI model", that the collection "includes results
at different stages of verification", that "Not all have accompanying Lean
formalizations" and that "Some of the unformalized results could have
issues". Its account of the method says that "The vast majority of results
were obtained with the same procedure", and names as an exception "work on a
zero-free region for the Riemann zeta function", the subject of the
manuscript that supplies this one's analytic input; it does not say which
manuscripts the exception covers. The manuscript's own README carries only
the title, the author line "OpenAI", the date and the citation block, and
adds no sentence about authorship, assistance or verification. The title
page names OpenAI as the sole author, and the text has no acknowledgment.
These are the source's own statements, recorded as attestations and not as
this corpus's review. No refereed publication, arXiv version or independent
review of the manuscript is recorded here, and nothing on this card is
independently reviewed.

**Formalization.** The release's Lean page for this family,
`lean/docs/182.md` ("Power savings for intersective polynomial differences and
prime arguments"), names only *A power saving for square-difference-free sets*
as its accompanying paper. Its one comparator statement,
`lean/ComparatorChallenges/SquareDifference.lean` (theorem
`OAI.SquareDifference.power_saving`; `SquareDifference.json` names the solution
module `OAI.Combinatorics.SquareDifference.Main` and permits the axioms
`propext`, `Quot.sound` and `Classical.choice`), reads in words: there are real
numbers $c>0$ and $C$ such that, for every $N\ge1$, every finite set $A$ of
integers in $[1,N]$ in which no difference $a-b$ equals $m^2$ for an integer
$m\ge1$ has $|A|\le CN^{1-c}$. Read here, that is the consequence this
manuscript draws from its theorem with $h(x)=(x-1)^2$ (TeX
`build/sections/introduction.tex`, lines 94--96, p. 2), but the formalization
accompanies the square-difference companion's proof, not this one; nothing in
the release formalizes Theorem 1.1 here or any statement with prime arguments.
At this revision the release's catalog `lean/formalization.yaml` lists no
manuscript of this family among its sources and no comparator of the family
under `status.main_results`, and its `review` field reads `status: unchecked`.
The release does list the zero-free input, Theorem 5.1, as formalized under
another family: the same catalog lists under `status.main_results` the
comparator `ComparatorChallenges/DirichletSevenEighths.json` (declaration
`OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re`, file
`OAI/NumberTheory/DirichletL/Nonvanishing.lean`), whose statement file
`DirichletSevenEighths.lean` reads, in words: for every modulus $q\ge1$, every
Dirichlet character $\chi$ modulo $q$ and every $s$ with
$\operatorname{Re}s>7/8$, other than $s=1$ for the principal character,
$L(s,\chi)\ne0$. This card reads that as the statement of Theorem 5.1; the
release's page for it is `lean/docs/003.md`, recorded on
[[primes/openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_7_8/_index|the 7/8 card]].
All of this is read statically from the release; nothing was built, replayed or
audited in this repository.

**Companions.** The release groups this manuscript, in its family, with
*A power saving for intersective polynomial differences with an exponent
depending only on the degree* (October 5, 2026), filed at
[[additive_combinatorics/openai_2026_power_saving_intersective_polynomial_differences/_index|the intersective-differences card]],
which the release describes as a bound $O_h(N^{1-c_k})$ for sets whose
differences avoid the nonzero values $h(1),h(2),\ldots$, for every intersective
$h$ of degree $k\ge2$ with positive leading coefficient, with $c_k>0$ depending
only on $k$; this manuscript calls it its "direct methodological predecessor",
adapts its tuple laws, Fourier lifts, signed kernels and contracting induction
to prime arguments, and reproduces its Fourier-lift moment estimate with proof
(Proposition 4.4). The family's third manuscript is *A power saving for
square-difference-free sets* (September 24, 2026), filed at
[[additive_combinatorics/openai_2026_power_saving_square_difference_free_sets/_index|the square-difference card]],
whose theorem as the release states it, absolute constants $c,C$ with $|A|\le
CN^{1-c}$ for sets with no nonzero square difference, Theorem 1.1 here would
also give at $h(x)=(x-1)^2$, though here only given the zero-free input; Section
4 cites it for the square-difference counterparts of its signed-form and lift
estimates. The release holds no earlier dated version of this manuscript.
Outside the family, the analytic input (Theorem 5.1) is the Dirichlet part of
Theorem 1.1 of *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s)>7/8*
(September 30, 2026), filed at
[[primes/openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_7_8/_index|the 7/8 card]],
whose read status there is claims checked only; the manuscript says only that
assertion is needed, so the Hecke part over $\mathbb Q(\sqrt{-3})$ is not used,
and Theorem 5.1 spells out that imprimitive characters and $\zeta$ are covered.
The theorem here is proved only given that claim, whose Dirichlet statement the
release lists as formalized (see Formalization). The companions' arguments were
not read for this card.

Read status: claims checked for Theorem 1.1, together with the definition of
a prime-intersective polynomial and the remark after the theorem, and for
the statements of Theorem 5.1 (the zero-free input), Proposition 5.2 (primes
in residue classes) and Proposition 7.5 (uniform power decay), read clause by
clause in the release's TeX source (`build/sections/introduction.tex`, label
`thm:main` at lines 19--29, the definition at lines 10--17 and the remark at
lines 31--34; `build/sections/primes.tex`, labels `thm:zero-free-input` at lines
27--34 and `prop:prime-progressions` at lines 36--47;
`build/sections/descent.tex`, label `prop:uniform-descent` at lines 414--420);
the proofs were read for their structure only and no step was checked; nothing
here is independently reviewed.

## Contents

Results are numbered within sections in one sequence shared by theorems,
propositions and lemmas (Lemma 2.1, Proposition 3.1, Theorem 5.1); the PDF
and the TeX agree.

- Title page and Section 1, Introduction (pp. 1--3). The abstract, then the
  definition: $h\in\mathbb Z[x]$ is prime-intersective if every modulus $q$
  has a root $r$ of $h$ with $(r,q)=1$. States
  [[additive_combinatorics/openai_2026_power_saving_polynomial_differences_prime_arguments/theorem_1_1|Theorem 1.1]]
  (p. 1) and notes that a prime root ($h(p)=0$) restricts nothing. The
  history runs from Furstenberg and Sárközy for squares, Kamae and Mendès
  France for intersective polynomials and Lucier's quantitative form, through
  Pintz--Steiger--Szemerédi, Bloom--Maynard, Green--Sawhney
  ($N\exp(-c\sqrt{\log N})$ for squares), Rice and Arala, to Adajar and
  coauthors ($N\exp(-c(\log N)^\mu)$, $\mu<1/2$). For prime arguments it cites
  Sárközy for $p\pm1$; Lucier, Ruzsa--Sanders and Wang; Green's power saving
  for $p-1$ and Thorner--Zaman's explicit exponent; Li--Pan for nonlinear $h$
  with $h(1)=0$; and Rice's bound $|A|\ll N(\log N)^{-c}$, $c<1/(2k-2)$, for
  every prime-intersective $h$ of degree $k\ge2$, with Wierdl's qualitative
  characterization by the unit-root condition as Rice records it. It names
  the intersective companion as the method's source, observes that
  $h(x)=(x-1)^2$ yields the square-difference case, outlines the mechanism,
  and calls the 7/8 manuscript's Dirichlet half-plane, cited as Theorem 1.1
  there, "a theorem input".
- Section 2, auxiliary polynomials and local admissibility (pp. 3--8). Fixes
  a unit $p$-adic root of $h$ at every prime, a completely multiplicative
  $\lambda$ recording its multiplicity, and for each $l$ the affine map
  $T_l(x)=r_l+lx$ with $(r_l,l)=1$ and the integral polynomial
  $h_l=h\circ T_l/\lambda(l)$ (Lemma 2.1, p. 4). A set avoids at $l$ when no
  nonzero $h_l(m)$ with $m\ge1$ and $T_l(m)$ prime is a difference;
  restriction to a progression of step $\lambda(D)$ carries avoidance at $l$
  to avoidance at $lD$. Lemma 2.2 bounds local exponential sums at large
  primes over arguments $x$ with $p\nmid T_l(x)$, with savings
  $p^{-8\delta j}$ and $p^{-4\delta}$, $\delta=1/(100k2^k)$; Lemma 2.3 gives
  uniform lifting classes at the finitely many small primes; Lemma 2.4 fixes
  one cycle length $L$ for which $L$ admissible local values sum to zero at
  every prime.
- Section 3, reflection-positive laws on residue tuples (pp. 8--15).
  Proposition 3.1 (p. 8): for all large primes $p$, uniformly in $l$, a
  probability law on labels in $\mathbb F_p$ indexed by a fixed finite slot
  set, reflection positive across every cut, translation invariant,
  covariant under $l\mapsto lD$, conditionally mixing with rate $p^{-\gamma}$
  ($\gamma=\delta/10$), and, off an exceptional part of mass at most $p^{-4}$,
  with admissible increments along a designated $L$-cycle of slots. It is a
  mixture of components in which marked blocks are forgotten, with index
  interactions supplying positivity (Lemma 3.2 gives the graph estimates;
  Figure 1, p. 13, illustrates the list concatenation).
- Section 4, multilinear estimates and Fourier lifts (pp. 15--22). The signed
  Hölder inequality, by repeated folding in the chessboard manner of
  Fröhlich, Israel, Lieb and Simon (Proposition 4.1); the resulting seminorm
  and its transport under $l\mapsto lD$ (Lemma 4.2); decay at large Fourier
  denominators from conditional mixing (Lemma 4.3); lifts of functions on an
  integer interval to products of the fields $\mathbb F_p$, keeping
  frequencies with squarefree denominator at most $Q$, with each $L^{2r}$ norm
  at most $C_{r,\epsilon}\|f\|_\infty Q^\epsilon$ when the interval has length
  at least $10Q^6$ (Proposition 4.4); and specialization of coordinates
  (Lemma 4.5).
- Section 5, prime estimates (pp. 22--29). Theorem 5.1 (p. 23) quotes the
  7/8 manuscript's half-plane for Dirichlet $L$-functions: no such function,
  for any modulus and character, imprimitive ones and $\zeta$ included,
  vanishes in $\operatorname{Re}s>7/8$. Proposition 5.2 (p. 23) derives,
  uniformly in the modulus $b$, the count of primes up to $x\le Y$ in a
  reduced class weighted by $\log p$ as $x/\varphi(b)$ plus
  $O(Y^{31/32}\log^2(2bY))$, through a bound for $L'/L$ on
  $\operatorname{Re}s=15/16$, a smoothed Mellin integral and differencing of
  a nonnegative sum; as stated, the error is smaller than the main term only
  for $\varphi(b)$ below about $x^{1/32}$ (an observation made here, not in
  the manuscript). Proposition 5.3 (p. 24) gives a power saving for
  prime-weighted polynomial exponential sums when $(k!)^2$ times the leading
  coefficient has a rational approximation with denominator between $Y^\rho$
  and $Y^{k-\rho}$, by Vaughan's identity and Weyl differencing (Lemmas 5.4
  and 5.5), with the product cutoff $mn\in I$ kept inside the differenced
  sums.
- Section 6, a kernel on differences at prime arguments (pp. 29--35). Fixes
  the exponents ($\eta=1/(10000k)$ down to $\tau$, $\sigma$) and the cutoffs
  $Q=N^\beta$, $H=N^{\beta/2}$. Proposition 6.1 (p. 29): for $l\le N^\zeta$
  and two functions bounded by $1$ on residue classes modulo $D\le N^\beta$
  with admissible difference, whose ordered differences avoid the forbidden
  values at $l$, $D$ times the pairing of their Fourier coefficients
  weighted by a cycle edge's multiplier is $O(H^{-\gamma/2})$. The proof
  compares a model kernel with a signed kernel supported on values $h_l(m)$
  with $T_l(m)$ prime (Lemma 6.2, p. 31), using Proposition 5.2 on major arcs
  and Proposition 5.3 on minor arcs.
- Section 7, descent to shorter intervals (pp. 35--41). Defines
  $\mathcal Y_l(N)$, the largest diagonal tuple integral of the lift of
  $\mathbf 1_A$ over sets avoiding at $l$, which bounds $(|A|/N)^d$ from
  above. Residue specialization (Lemma 7.1), comparison with shorter
  intervals at parameter $lD$ (Proposition 7.2), cancellation for residue
  assignments with admissible cycle increments (Proposition 7.3), the
  recurrence (Proposition 7.4), and Proposition 7.5 (p. 40):
  $\mathcal Y_l(N)\le C_0l^{b_0}N^{-a_0}$ for all $l,N\ge1$. The proof of
  Theorem 1.1 (p. 41) takes $l=1$ and $c_h=a_0/d$.
- References (pp. 41--42), 27 items, including the three release manuscripts
  named above.

The manuscript flags nothing as numerical, computer-assisted or conditional;
it treats the quoted zero-free half-plane as "a theorem input" (p. 3). No
constant is evaluated, and $c_h$ is given only as $a_0/d$ with $a_0$ chosen
small after all other parameters. On dependence the manuscript says only
that $c_h$ and $C_h$ "depend only on $h$" (abstract, p. 1, and in other
words the remark after the theorem); it does not claim, as the
integer-argument companion does, an exponent depending only on the degree,
and the release's family description says the exponent is "allowed to
depend on h". Read here, the proof as written gives no degree-only exponent:
$d$ and $a_0$ are fixed through the cycle length $L$ and the modulus $M_0$,
which depend on $h$ itself through its lifting exponents at small primes
(Lemmas 2.3 and 2.4) and the prime thresholds. The release folder for this
manuscript holds only the PDF, the TeX build directory and the README; there
is no `verification/` folder.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using it. The leads of its analytic input, the zero-free half-plane, are
recorded on
[[primes/openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_7_8/_index|the 7/8 card]].
