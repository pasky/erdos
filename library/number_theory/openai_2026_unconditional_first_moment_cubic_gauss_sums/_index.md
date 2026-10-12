---
name: number_theory/openai_2026_unconditional_first_moment_cubic_gauss_sums
desc: |
  A 52-page release manuscript claiming Patterson's first-moment asymptotic
  unconditionally: normalized cubic Gauss sums over the primary primes of
  Z[omega] of norm at most X sum to (6/5)c_* X^{5/6}/log X + o(X^{5/6}/log X),
  sharp cutoff, with cancellation in each fixed nonzero angular mode, by
  corrected dispersion and an exact prime decomposition; it names no Erdős
  problem.
license: Apache-2.0
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

# number_theory/openai_2026_unconditional_first_moment_cubic_gauss_sums

[[number_theory/_index|..]]

[[number_theory/openai_2026_unconditional_first_moment_cubic_gauss_sums/theorem_1_1|theorem_1_1]]: The manuscript's main claim: unconditionally and with a sharp cutoff, the
normalized cubic Gauss sums over primary primes of Z[omega] of norm at most
X sum to (6/5)c_* X^{5/6}/log X + o(X^{5/6}/log X), Patterson's first-moment
conjecture in this normalization. Claims checked only.

[[number_theory/openai_2026_unconditional_first_moment_cubic_gauss_sums/theorem_a_1|theorem_a_1]]: The claimed angular extension: for each fixed integer l, the first moment
twisted by (pi/|pi|)^l equals the equally twisted model sum up to
o(X^{5/6}/log X), so each nonzero mode cancels; the fixed powers G^k with k
not divisible by 3 and |k| > 1 cancel likewise. Claims checked only.

***

OpenAI, *An unconditional first moment for cubic Gauss sums*, OpenAI Math
Release preprint, September 25, 2026. Released under the Apache License 2.0 at
<https://github.com/openai/math> (revision fd4aeeb2e), folder
`preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026`;
the held PDF, `paper.pdf` in the release, is retained as
[openai_2026_unconditional_first_moment_cubic_gauss_sums.pdf](openai_2026_unconditional_first_moment_cubic_gauss_sums.pdf),
and the release's TeX bundle in that folder is the TeX source cited on this
card. The license term was read in the release's root `LICENSE` file at that
revision on 2026-10-12.

```bibtex
@misc{OAI:An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026,
  author = {{OpenAI}},
  title = {{An unconditional first moment for cubic Gauss sums}},
  howpublished = {OpenAI Math Release preprint
                  \href{https://github.com/openai/math/blob/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf}{OAI:An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026}},
  year = {2026}
}
```

The held PDF has 52 pages with a text layer; its title page is dated
September 25, 2026, and `pdfinfo` reports no creation date, since the TeX
source suppresses the PDF date fields. The TeX source (`build/paper.tex`, 394
lines, which inputs six section files under `build/sections/` and one figure
file, 4,125 lines in all) is the text read here.

**Attestation.** The release README states that the manuscripts were "produced
by an internal OpenAI model", that the collection "includes results at different
stages of verification", that "Not all have accompanying Lean formalizations"
and that "Some of the unformalized results could have issues". Its account of
the method says that "The vast majority of results were obtained with the same
procedure using an unreleased internal OpenAI model"; the exceptions it names
(work on a zero-free region for the Riemann zeta function and on the Hodge
conjecture for CM abelian varieties) and its note that the writeup of the
$11/12$ zero-free region was human edited do not describe this manuscript's
subject. The manuscript's
own README carries only the title, the author "OpenAI", the date September 25,
2026 and the citation block above, and adds no sentence about authorship,
assistance or verification. The title page names OpenAI as the sole author and
prints no statement on how the manuscript was produced. These are the source's
own statements, recorded as attestations and not as this corpus's review. No
refereed publication, arXiv version or independent review of the manuscript is
recorded here, and nothing on this card is independently reviewed.

**Formalization.** The release's Lean page `lean/docs/023.md`, read
statically, says that the formalization proves the sharp-cutoff asymptotic
with main term $\frac65c_*X^{5/6}/\log X$, the angular comparison for every
integer Fourier mode, and cancellation of order $o(X^{5/6}/\log X)$ for each
fixed nonzero mode, and that "All primary Eisenstein primes are included,
without an extra conjectural premise." It links one comparator statement file,
`lean/ComparatorChallenges/PattersonFirstMoment.lean`, whose sidecar JSON names
the solution module `OAI.NumberTheory.CubicMoment.Theta.CubicThetaMains`, the
three declarations `OAI.CubicFirstMoment.patterson_firstMoment`,
`patterson_angularComparison` and `patterson_angularCancellation`, and the
permitted axioms `propext`, `Quot.sound` and `Classical.choice`; the directory
that holds the solution module, `lean/OAI/NumberTheory/CubicMoment/`, contains
3,549 Lean files at this revision. In words, the statement file builds
$\mathbb Z[\omega]$ as the subring of $\mathbb C$ generated by
$\omega=e^{2\pi i/3}$, calls $a$ primary
when $3$ divides $a-1$, defines the cubic symbol at a prime $p$ by the cube
root of unity congruent to $v^{(N p-1)/3}$ (zero at nonunits), the Gauss sum
as $N(p)^{-1/2}$ times the sum over residues of that symbol times
$\exp(2\pi i(z+\bar z))$ at $z=v/p$, and the cutoff sum over primary primes of
norm at most $X$. Its three statements say that this sum of Gauss sums,
minus $\frac65c_*X^{5/6}/\log X$, is $o(X^{5/6}/\log X)$ as the real
$X\to\infty$ (Theorem 1.1); that for every integer $\ell$ the sum of
$(p/|p|)^\ell\,(G(p)-c_*N(p)^{-1/6})$ is $o(X^{5/6}/\log X)$ (equation (A.1));
and that for every nonzero integer $\ell$ the sum of $(p/|p|)^\ell G(p)$ is
$o(X^{5/6}/\log X)$ (equation (A.2)). The fixed-power consequence (A.14) is
not among them. The release's catalog `lean/formalization.yaml` names
neither this manuscript nor this comparator at this revision, so its
`status.main_results` lists no entry for them; the catalog's own `review`
field reads `status: unchecked`. Nothing was built, replayed or audited for
fidelity in this repository; no Lean file here is a proof of any Erdős
problem.

**Companions.** The release's manuscript map lists this manuscript as the
only member of its family, "Patterson's first moment for cubic Gauss sums", and
the release holds no earlier dated version of it at this revision. One other
release manuscript cites it: *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re(s)>7/8* (September 30, 2026), filed at
[[primes/openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_7_8/_index|the 7/8 card]],
works in the same cubic-theta setting (Patterson's theta series, the
Dunn--Radziwiłł cusp expansions, Heath-Brown's cubic large sieve), says that the
first-moment asymptotic "is proved unconditionally in an independent manuscript"
with a citation of Theorem 1.1 here, and states that the result is not used
there. That manuscript's argument was not read for this card.

Read status: claims checked for Theorem 1.1 and Theorem A.1 with its fixed-power
consequence (A.14), together with the definitions (1.1), the weighted form
(1.3), the conversion to Kummer sums (1.4)--(1.5) and Remark 1.2, read clause by
clause in the release's TeX source on 2026-10-12 (`build/paper.tex`, label
`thm:main` at lines 64--72, definitions at lines 50--62, the weighted form at
lines 84--92, Section 1.2 and `rem:normalization` at lines 151--192;
`build/sections/angular.tex`, label `thm:angular` at lines 19--35, definitions
at lines 10--16 and Section A.6 at lines 802--838); the statements of the
intermediate propositions and lemmas and all proofs were read for their
structure only and no step was checked; nothing here is independently reviewed.

## Contents

The numbering below is the PDF's (results are numbered within sections, the
appendix with the prefix A), and the printed page numbers equal the PDF's.

- Section 1, Introduction (pp. 1--4; `build/paper.tex`). Fixes
  $\mathcal O=\mathbb Z[\omega]$, primary elements (congruent to $1$ modulo
  $3$, one generator per ideal prime to $3$), the cubic residue symbol and
  the normalized Gauss sum $G(b)$ with the constant
  $c_*=(2\pi)^{2/3}/(3\Gamma(2/3))$ (equation (1.1)). States
  [[number_theory/openai_2026_unconditional_first_moment_cubic_gauss_sums/theorem_1_1|Theorem 1.1]]
  (p. 1), announces the angular extension and the fixed-power consequence,
  and derives the logarithmically weighted form (1.3) by partial summation.
  Identifies the theorem with the all-primary-prime display after Equation
  (1.8) of Dunn and Radziwiłł and, through the conversion of Section 1.2,
  with Wan's Conjecture 4.13, and calls it a resolution of Patterson's
  first-moment conjecture in those normalizations.
  Section 1.1 recalls Kummer's sums $S_p=\sum_{x\bmod p}e(x^3/p)$,
  Heath-Brown and Patterson's equidistribution of the normalized cubic Gauss
  sums on the unit circle, Patterson's predicted bias at scale
  $X^{5/6}/\log X$, Heath-Brown's unconditional bound $O(X^{5/6+\epsilon})$,
  and Dunn and Radziwiłł's GRH-conditional smoothed asymptotic, whose level
  Voronoi formula, unconditional in the manuscript's account, it imports
  while not using their GRH-dependent estimates. Section 1.2
  (pp. 2--3) proves $G(\pi)+G(\bar\pi)=S_p/\sqrt p$ for
  $p=\pi\bar\pi\equiv1\pmod 3$ (1.4) and deduces the rational-prime form
  (1.5) with constant $\frac35c_*$; Remark 1.2
  (p. 3) notes that the cited version of Dunn and Radziwiłł prints
  $\frac65c_*$ both in a rational-prime conjecture and in the
  all-primary-prime display, which (1.4) makes incompatible, and says the
  manuscript proves the latter display without deciding which printed
  coefficient is authoritative. Section 1.3
  (pp. 3--4) outlines the proof (Figure 1, p. 4, maps it) and lists the
  literature inputs, stating that no GRH-dependent cancellation result is
  one.
- Section 2, Arithmetic and analytic preliminaries (pp. 4--10;
  `sections/background-type1.tex`). Multiplicativity $|G(a)|=\mu^2(a)$,
  $G(ab)=G(a)G(b)\overline{\chi_b(a)}$ (2.1); conventions on divisor-bounded
  coefficients and Mellin inversion; the Hecke functional equation in the
  completion of Watkins (Section 3.6); a Siegel--Walfisz bound for cubic
  Hecke characters of polylogarithmic conductor derived from Thorner and
  Zaman (Theorem 1.4); the Montgomery--Vaughan mean value. Theorem 2.1 is
  Heath-Brown's cubic large sieve (Theorem 2 of the Kummer paper); Lemma 2.2
  is an ordinary character large sieve over $\mathbb Q(\omega)$ with bound
  $Z+Q^2$ and no $Q^\epsilon$ loss, proved in the text; Lemma 2.3 extends the
  cubic large sieve to inner and outer variables that need not be
  squarefree. Theorem 2.4
  (p. 8) restates Dunn and Radziwiłł's level Voronoi formula (their arXiv
  version 3, Proposition 5.3) for the cube-completed sum
  $\mathcal C_r(V;W)$, with main term
  $A_0\mathcal MW(5/6)V^{5/6}\varphi(r)R^{-7/6}$ and remainder
  $O(X^\epsilon R^{1/2})$; Theorem 2.5 (p. 9) is Heath-Brown's metaplectic
  mean square for $f_r(s)=\sum_uG(ru)(Nu)^{-s}$ on
  $\operatorname{Re}s=1/2+\epsilon$ (Section 3, Lemma 3 there), with the
  residue at $5/6$ and the growth bounds for contour shifts assembled from
  that paper and Dunn and Radziwiłł's Proposition 5.2.
- Section 3, Type I estimates (pp. 10--13). Proposition 3.1 (p. 10): for
  $RU\asymp X$, $R\ll X^{0.51}$ and divisor-bounded outer coefficients, the
  sum of $G(ru)-c_*\mu^2(ru)N(ru)^{-1/6}$ against a smooth inner weight is
  $\ll X^{5/6-1/100}$, by inverting the cube completion with Möbius and using
  Theorem 2.4 at small cube divisors and counting or the cubic large sieve at
  the rest.
  Proposition 3.2 (p. 12): a height-averaged Type I bound
  $X^{1/2+\epsilon}R^{3/4}T^{1/2}$ plus a pole term, from Theorem 2.5.
- Section 4, Character moments at the two exceptional configurations
  (pp. 13--19; `sections/dual.tex`). Defines admissible prime convolutions
  (squarefree products of a bounded number of primes, each of norm at least a
  fixed power of the length, on independent smooth dyads). Proposition 4.1
  (p. 13) gains a power $Y^{-\eta}$ over the benchmark $Y^{7/3}$, which both
  large sieves reach, for $\sum_{p,q}|\sum_b\beta(b)N(b)^{iu}\chi_b(vpq^2)|^2$
  when the lengths of $p,q$ are near $(Y,1)$ or $(Y^{1/3},Y^{1/3})$; Lemma 4.2
  dualizes a full smooth character sum by the functional equation and Lemma 4.3
  is an off-diagonal Gram estimate. The proof (pp. 16--19) argues by
  contradiction along limiting exponents: a short Möbius identity for the von
  Mangoldt function, moments of products of several lengths, and the
  Bombieri--Halász--Montgomery inequality (in Harcos's note) with Lemma 4.3. The
  constants $\delta,\eta$ come from this compactness argument and are not made
  explicit.
- Section 5, Corrected dispersion (pp. 19--28; `sections/dispersion.tex`).
  Following Dunn and Radziwiłł's Section 9, Proposition 5.1 (p. 20) bounds
  $\sum_a W_A(a)|F_u(a)|^2$ with
  $F_u(a)=\sum_b\beta_b(Nb)^{iu}G(b)\overline{\chi_b(a)}$ for $AB\asymp X$,
  $X^{0.32}\le B\ll X^{1/2}$: a coarse bound, a corrected bound with
  $c_*\overline{G(a)}(Na)^{-1/6}S(u)$ subtracted under a Siegel--Walfisz
  property (SW) of $\beta$ and roughness, an uncorrected bound at small
  $H=B^2/A$, and height-averaged bounds reduced to the exact diagonal. In
  Poisson summation the cube frequencies give the model square
  through a Riesz-kernel integral equal to $c_*^2$, and the two exceptional
  large-conductor ranges are passed to Proposition 4.1. Remark 5.2 isolates
  the three-prime transition, where a bound $X^{5/6}(\log X)^{-3/2}$
  suffices.
- Section 6, An exact decomposition of the prime sum (pp. 28--35;
  `sections/decomposition.tex`). Proposition 6.1 (p. 28) writes the prime sum,
  for the kernel $G(n)N(n)^{it}$ or the model, as polylogarithmically many
  Type I and bilinear terms with the coefficient properties the earlier sections
  need: an exact prime detector with bounded prime tuples and a grouping of
  prime scales (Lemmas 6.2--6.3), a stopping rule over norm bins with a binomial
  weight that separates the two variables exactly (Lemma 6.4), a sparse
  late-stop family with a power saving, and property (SW) for the rough
  coefficients (Lemma 6.5).
- Section 7, Bilinear sums and the sharp prime cutoff (pp. 35--41;
  `sections/perron.tex`). Table 1 (p. 35) lists three height ranges.
  Proposition 7.1 (p. 35) is the low-height bilinear comparison with
  arbitrary logarithmic saving and the transition bound
  $X^{5/6}(\log X)^{-3/2}$; Proposition 7.2 (p. 37) bounds the
  height-integrated Gauss-sum bilinear form by localizing both norm variables
  into cells. Section 7.3 fixes the order of all parameters, Lemma 7.3
  (p. 39) truncates the interval indicator in Fourier space, and Section 7.5
  (pp. 40--41) proves Theorem 1.1.
- Appendix A, Fixed angular twists (pp. 42--51; `sections/angular.tex`).
  States
  [[number_theory/openai_2026_unconditional_first_moment_cubic_gauss_sums/theorem_a_1|Theorem A.1]]
  (p. 42). Lemma A.2 gives the functional equation and a prime estimate for
  Hecke characters of $\mathbb Q(\omega)$ with infinity type $\ell$ (from
  Rajan and Kaneko--Thorner); Section A.2 gives an angular Voronoi formula
  from Dunn and Radziwiłł's Propositions 5.2--5.3, Lemma A.3 (p. 44) and the
  angular Type I estimates, Proposition A.4 (p. 45); Proposition A.5
  (p. 47) extends Proposition 4.1 to angularly twisted prime convolutions;
  Lemma A.6 and Proposition A.7 (pp. 48--50) extend (SW), dispersion and the
  bilinear estimates; Section A.5 (pp. 50--51) proves Theorem A.1; Section
  A.6 (p. 51) derives the fixed-power moments (A.14) from
  $G(\pi)^3=-\pi/|\pi|$.
- References (pp. 51--52), 18 items, all but Harcos's note with DOIs, among
  them Dunn and Radziwiłł (Annals 2024, cited by arXiv version 3),
  Heath-Brown (Israel J. Math. 2000), Heath-Brown and Patterson (1979),
  Patterson (1977, 1978), Kummer
  (1846), Wan (2021), Thorner and Zaman (2019), Kaneko and Thorner (2025),
  Rajan (1998), Watkins (2011), Gao and Zhao (2022) and Huxley (1968). No
  other release manuscript is cited.

The manuscript flags nothing as numerical, computer-assisted or conditional.
Theorems 1.1 and A.1 state their errors only as little-oh, and the manuscript
gives no rate. Several of its constants are not explicit: the small exponents
$\gamma,\kappa,\rho$ are fixed only as sufficiently small, and the constants
$\delta,\eta$ of Propositions 4.1 and A.5 come from a compactness argument.
The release folder for this manuscript holds only the README, the PDF and the
TeX build directory; there is no `verification/` folder.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using it. The pages nearest in objects were screened and give no row:
Problem 436 asks about runs of consecutive $k$th power residues modulo each
large prime, which a first moment of complete Gauss sums averaged over primes
does not control. For the case $k=3$ of Problem 979, two of the pending
claims (Kitamura's and Wang and Zhang's) report a route through Hecke
equidistribution for the Fermat cubic; this manuscript takes prime estimates
of that kind for Hecke characters of $\mathbb Q(\omega)$ from the literature
(Lemma A.2) rather than proving them.
