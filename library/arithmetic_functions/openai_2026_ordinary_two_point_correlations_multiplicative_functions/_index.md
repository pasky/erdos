---
name: arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions
desc: |
  An 87-page manuscript of the OpenAI mathematics release claiming the ordinary
  two-point Chowla conjecture, with a power-of-logarithm saving for Liouville
  correlations along fixed nonproportional affine forms, and the binary
  corrected Elliott conjecture for ordinary averages, both by divisor-graph
  trace bounds; it names no Erdős problem.
license: Apache-2.0
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

# arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions

[[arithmetic_functions/_index|..]]

[[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/corollary_1_3|corollary_1_3]]: The affine form of the qualitative claim: under the hypotheses of Theorem 1.2,
the ordinary average of f_1(a_1n+b_1)f_2(a_2n+b_2) tends to zero for fixed
nonproportional affine forms, intercepts zero and common factors allowed.
Claims checked only.

[[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/proposition_18_4|proposition_18_4]]: The progression form of the qualitative claim: under the hypotheses of
Theorem 1.2, the ordinary average of f_1(n+h_1)f_2(n+h_2) over n in any fixed
class b mod l, unit or not, tends to zero through all real cutoffs. Claims
checked only.

[[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/proposition_2_1|proposition_2_1]]: The progression form of the quantitative claim: lambda(n)lambda(n+h)
restricted to any fixed class b mod l, unit or not, has ordinary average
O((log X)^(-c)) at every real cutoff, with one absolute c; Theorem 1.1
follows from it. Claims checked only.

[[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/theorem_1_1|theorem_1_1]]: The manuscript's quantitative claim: for fixed nonproportional affine forms
the Liouville correlation sum up to X is O(X/(log X)^c) at every cutoff,
with c absolute, its case n, n+h presented as the ordinary two-point Chowla
conjecture. Claims checked only.

[[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/theorem_1_2|theorem_1_2]]: The manuscript's qualitative claim: for multiplicative f_1, f_2 with values
in the closed unit disk, one of them uniformly nonpretentious, and distinct
shifts, the ordinary average of f_1(n+h_1)f_2(n+h_2) tends to zero, with no
rate. Claims checked only.

***

OpenAI, *Ordinary two-point correlations of multiplicative functions*, OpenAI
Math Release preprint, September 24, 2026. Released under the Apache License 2.0
at <https://github.com/openai/math> (revision fd4aeeb2e), folder
`preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026`;
the held PDF, `final.pdf` in the release, is retained as
[openai_2026_ordinary_two_point_correlations_multiplicative_functions.pdf](openai_2026_ordinary_two_point_correlations_multiplicative_functions.pdf),
and the release's TeX bundle in that folder is the TeX source cited on this
card. The license term was read in the release's root `LICENSE` file at that
revision on 2026-10-12.

```bibtex
@misc{OAI:Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026,
  author = {{OpenAI}},
  title = {{Ordinary two-point correlations of multiplicative functions}},
  howpublished = {OpenAI Math Release preprint
                  \href{https://github.com/openai/math/blob/main/preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/final.pdf}{OAI:Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026}},
  year = {2026}
}
```

The held PDF has 87 pages with a text layer; its title page is dated
September 24, 2026, and its metadata records a creation date of the same day,
24 September 2026. The TeX source is `build/main.tex` (90 lines), which
inputs `build/introduction.tex` and sixteen section files, eight under
`build/quantitative/` and eight under `build/qualitative/`. That makes 18 TeX
files with 6,192 lines in all, with the bibliography `build/refs.bib` (21
entries). This source is the text read here.

**Attestation.** The release README states that the collection's manuscripts
and supporting proof artifacts were "produced by an internal OpenAI model",
that the collection "includes results at different stages of verification",
that "Not all have accompanying Lean formalizations" and that "Some of the
unformalized results could have issues". Its account of the method says that
"The vast majority of results were obtained with the same procedure using an
unreleased internal OpenAI model", with on average "three hours of ChatGPT Pro
thinking compute" per result; the two exceptions it names concern other
subjects. The README also lists this family among ten for which the release
publishes "abridged summaries of the model's reasoning"; that file
(`reasoning_traces/ordinary-two-point-correlations.pdf` in the release) was
not read for this card and is not held here. The manuscript's own README
carries only the title, the author line "OpenAI", the date and the citation
block, and says nothing about authorship or assistance. The title page names
OpenAI as the sole author, and the manuscript has no acknowledgments. These are
the source's own statements, recorded as attestations and not as this corpus's
review. No refereed publication, arXiv version or independent review of the
manuscript is recorded here, and nothing on this card is independently
reviewed.

**Formalization.** The release's Lean page for this family, `lean/docs/007.md`
("Ordinary two-point correlations and the corrected Elliott conjecture"), names
this manuscript as its only paper. It says that the formalization proves the
bound $O(X/(\log X)^c)$, with $c>0$ absolute and the constant depending on the
forms, for Liouville correlation sums along every fixed pair of nonproportional
affine forms; and that for two one-bounded multiplicative functions, one of them
uniformly nonpretentious against all twists $\chi(n)n^{it}$ with $|t|\le N$, the
shifted and the affine correlation sums divided by $N$ tend to zero. It links
two comparator statement files. One,
`lean/ComparatorChallenges/OrdinaryTwoPointCorrelations.lean`, states three
theorems. In words, `liouville_log_saving` says there is $c>0$ such that for all
natural numbers $a_1,a_2\ge1$ and $b_1,b_2$ with $a_1b_2\ne a_2b_1$ there is
$C>0$ such that
$|\sum_{n=1}^{\lfloor X\rfloor}\lambda(a_1n+b_1)\lambda(a_2n+b_2)|$ is at most
$CX/(\log X)^c$ for every real $X\ge3$, where $\lambda$ is Mathlib's
`ArithmeticFunction.liouville`. `binary_corrected_elliott` takes complex
functions $f_1,f_2$ on the natural numbers that are multiplicative on coprime
positive arguments and bounded by one at positive arguments, one of them
uniformly nonpretentious, and natural numbers $h_1\ne h_2$, and says that
$N^{-1}\sum_{n=1}^Nf_1(n+h_1)f_2(n+h_2)$ tends to $0$. Uniform
nonpretentiousness there means that for every modulus $q\ge1$, every Dirichlet
character $\chi$ modulo $q$ and every real $K$, every large $N$ and every real
$t$ with $|t|\le N$ give
$\sum_{p\le N}(1-\operatorname{Re}(f(p)\overline{\chi(p)p^{it}}))/p\ge K$.
`affine_corrected_elliott` is the same statement for affine forms with
$a_1,a_2\ge1$ and $a_1b_2\ne a_2b_1$. The companion
`OrdinaryTwoPointCorrelations.json` names the solution module
`OAI.NumberTheory.TwoPointCorrelations.FinalMain` and permits the axioms
`propext`, `Quot.sound` and `Classical.choice`. The other,
`lean/ComparatorChallenges/OrdinaryElliott.lean`, states the binary theorem
alone, with the bound by one required at every argument and nonpretentiousness
written as the infimum of the distance over $|t|\le N$ tending to infinity; its
`OrdinaryElliott.json` names the solution module
`OAI.NumberTheory.OrdinaryCorrelations.Elliott.Main` with the same three axioms.
Both solution modules are present in the release's Lean tree at this revision.
Read in words, the comparator theorems restate Theorem 1.1, Theorem 1.2 and
Corollary 1.3; the progression forms, Proposition 2.1 and Proposition 18.4, and
the Möbius specializations have no comparator statement. The release's catalog
`lean/formalization.yaml` at this revision lists neither comparator, and no
entry for this manuscript, under its `status.main_results`, and its `review`
field reads `status: unchecked`. All of this is read statically from the
release's Lean page and comparator files; nothing was built, replayed or audited
for fidelity in this repository.

**Companions.** The release groups this manuscript alone in its family; it has
no companion manuscript and no earlier dated version in the release. In a
separate family, the release holds a manuscript of the same date, *The joint
Dickman law for consecutive integers* (September 24, 2026), filed at
[[arithmetic_functions/openai_2026_joint_dickman_law_consecutive_integers/_index|the joint Dickman card]],
which claims an ordinary-density law for the largest prime factors of $n$ and
$n+1$ by reducing it to the decorrelation of two scale-dependent bin characters
and amplifying a failure of that decorrelation into a divisor graph controlled
by short-interval estimates. Neither manuscript cites the other, and that
argument was not read for this card.

Read status: claims checked for Theorem 1.1, Theorem 1.2, Corollary 1.3,
Proposition 2.1 and Proposition 18.4, together with the definitions (1.1) and
(1.2) and the statements of Lemma 3.1 (finite residue comparison), Theorems 4.3
and 12.2 (the two imported short-interval theorems), Theorem 5.4
(nonbacktracking moment), Proposition 10.1 (divisor graph estimate),
Proposition 11.4 (analytic centering), Theorem 13.3 (high trace), the Lemmas
numbered 18.1--18.3 and Lemma 18.5, read clause by clause in the release's TeX
source on 2026-10-12. The labels and lines are: in `build/introduction.tex`,
`thm:q-affine` (lines 20--34), `eq:distance` (lines 51--55), `eq:unp` (lines
58--61), `thm:elliott` (lines 64--72) and `cor:affine` (lines 81--89); in
`build/quantitative/01-setup.tex`, `q:progression` (lines 7--18); in
`build/quantitative/02-finite-law.tex`, `q:finite-law` (lines 24--41); in
`build/quantitative/03-analytic.tex`, `q:MRT-short` (lines 127--138); in
`build/quantitative/04-paths-trace.tex`, `q:trace` (lines 208--218); in
`build/qualitative/graph-setup.tex`, `prop:graph-estimate` (lines 86--102); in
`build/qualitative/analytic-transfer.tex`, `prop:analytic-centering` (lines
232--249) and `thm:mrt` (lines 399--414); in `build/qualitative/paths.tex`,
`thm:high-trace` (lines 103--117); in
`build/qualitative/affine-corollaries.tex`, `lem:affine-stability` (lines
14--28), `lem:affine-dilation` (lines 56--72), `lem:affine-residue` (lines
127--145), `prop:affine-progression` (lines 181--194) and
`lem:affine-liouville-unp` (lines 268--278). The proofs, including the short
deductions of Sections 9 and 18, were read for their structure only and no
step was checked; nothing here is independently reviewed.

## Contents

The numbering below is the PDF's: theorems, lemmas, propositions, corollaries
and definitions share one counter within each section. The title, abstract and
table of contents take pp. 1--3. Part I (Sections 2--9) proves the
quantitative Liouville estimate; Part II (Sections 10--17) proves the
qualitative theorem with new parameters and prime sets; Part III (Section 18)
derives the progression and affine forms. Here $\lambda(n)=(-1)^{\Omega(n)}$,
$\mathbb D$ is the closed unit disk, and a multiplicative function satisfies
$f(mn)=f(m)f(n)$ for coprime $m,n$.

- Section 1, Introduction (pp. 3--7). Contrasts ordinary averages
  $X^{-1}\sum_{n\le X}a(n)$ with logarithmic ones and states
  [[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/theorem_1_1|Theorem 1.1]]
  (p. 3), the bound $\ll X/(\log X)^c$ for Liouville correlations along fixed
  nonproportional affine forms, with $c$ absolute; the case of shifts $0$ and
  $h$ is presented as resolving the ordinary two-point Chowla conjecture.
  Defines the pretentious distance (1.1), whose square
  $D(f,\chi n^{it};X)^2$ is the sum over primes $p\le X$ of
  $(1-\operatorname{Re}(f(p)\overline{\chi(p)p^{it}}))/p$,
  and uniform nonpretentiousness (1.2), divergence of
  $\inf_{|t|\le N}D(f,\chi n^{it};N)$ for every fixed Dirichlet character, and
  states
  [[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/theorem_1_2|Theorem 1.2]]
  (p. 4), the binary corrected Elliott conjecture for ordinary averages, and
  [[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/corollary_1_3|Corollary 1.3]]
  (p. 4), its affine form. Section 1.1 (pp. 4--5) places these against
  Chowla (1965), Elliott (1992), Halász, Granville--Harper--Soundararajan and
  Granville--Soundararajan; the correction of Elliott's condition by
  Matomäki, Radziwiłł and Tao (2015), whose corrected condition is said to be
  equivalent to (1.2); the bound $1-\delta(h)$ of
  [[primes/matomaki_2016_multiplicative_functions_short_intervals/corollary_2|Matomäki and Radziwiłł, Corollary 2]];
  Tao's logarithmically averaged binary Elliott theorem (2016, Theorem 1.3 and
  Corollary 1.5); the logarithmically weighted bounds of Helfgott and
  Radziwiłł, $\log x/\sqrt{\log\log x}$, and of Pilatte, $(\log x)^{1-c_0}$;
  binary cancellation outside a set of scales of logarithmic density zero by
  [[arithmetic_functions/tao_2019_structure_correlations_multiplicative_functions_at_almost/_index|Tao and Teräväinen (2019)]],
  Corollary 1.13; Klurman, Mangerel and Teräväinen (2023, Theorem 1.2), along
  scales of full upper logarithmic density under a weaker hypothesis; and the
  logarithmic savings outside a controlled exceptional set of scales of
  [[arithmetic_functions/tao_2025_quantitative_correlations_problems_prime_factors_consecutive/_index|Tao and Teräväinen (2026)]],
  Theorem 3.1 and Remarks 3.2. It also names the line of bounded-independence
  results for Boolean circuits (Linial--Nisan, Bazzi, Razborov, Braverman) and
  the almost-to-exact independence construction of Alon, Goldreich and
  Mansour. Sections 1.2 and 1.3 (pp. 5--7) sketch both arguments and the
  organization.
- Section 2, Prime supplies and the quantitative target (pp. 7--9). States
  [[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/proposition_2_1|Proposition 2.1]]
  (p. 7), the same saving for $\lambda(n)\lambda(n+h)$ in any fixed residue
  class. Fixes absolute $A\ge1000$ and $W\ge10$, $L=(\log X)^{1/A}$,
  $\delta=1/200$, $J=\lfloor\delta\log L/(6W)\rfloor$, $\eta=e^{-J}$ and
  $K=e^{4J}$. The centered supplies $P_1,\dots,P_J$ are primes
  $p\equiv1\pmod5$ not dividing $lh$ with $\log p$ in consecutive windows
  starting at $L^{1-\delta}$, each of reciprocal mass between $W$ and $2W$ (the
  prime number theorem modulo $5$, cited to Theorem 12.1 of Koukoulopoulos's
  book); the padding primes $Q$ are the primes $p\not\equiv1\pmod5$ up to $e^L$
  not dividing $lh$, with weight $u(q)=4^{\omega(q)}$ on squarefree
  $Q$-products. A label $d$ takes one prime from each supply; bins collect
  pairs $(d,q)$ with $\log(dq)$ in a window of width $\eta$ and
  $\omega(q)\le100\log L$, and Lemma 2.2 (p. 8) says they keep at least half
  the harmonic mass. The centered
  divisor sums $C_j$ carry the factors $\mathbf 1_{p\mid n}-1/p$; their
  full-divisibility term returns the target average $F(X)$ by the substitution
  $n=qdm$. The section ends with the auxiliary model of independent uniform
  residues.
- Section 3, Comparing finite integer averages with independent residues
  (pp. 10--13). Lemma 3.1 (p. 10): an event given by an AND--OR--NOT circuit of
  depth at most $20$ and size at most $\exp(L^6)$ in residue equalities has
  frequency within $e^{-L^{10}}$ of its product-law probability on every
  interval of at least $\exp(L^A/2)$ integers. The proof encodes residues by
  jittered bits, corrects the nearly bounded-independent bit law to an exactly
  $t$-wise uniform one by a Fourier calculation in the manner of Alon,
  Goldreich and Mansour, and applies Braverman's theorem (Corollary 2 of his
  2010 paper). Corollaries 3.2 and 3.3 extend this to signed scalar expansions
  and to truncated padding weights.
- Section 4, Centering and deleting a small edge mass (pp. 13--21). Lemma 4.1
  (p. 13), the centering estimate, rests on Lemma 4.2 (sup and fourth-moment
  bounds for exponential sums over rough integers, by a truncated sieve),
  Theorem 4.3 (p. 15, imported from Theorem 1.3 of Matomäki, Radziwiłł and
  Tao) and Lemma 4.4 (p. 15, correlation averaged over rough shifts, saving
  $L^{-21/20}$, with the fourth-moment approach of Pilatte's Appendix C).
  Lemma 4.5 (p. 17) bounds the concentration of padding divisors in one bin by a
  characteristic-function estimate; Lemma 4.6 (p. 19) bounds the cost of
  deleting sites with too many padding primes, concentrated padding mass, high
  $P$-degree or a prescribed rare residue event.
- Section 5, Prohibited paths and centered traces (pp. 21--26). Definition 5.1
  (p. 21) defines forward prohibited words (length $3$ to
  $\lfloor L^{1/10}\rfloor$, unequal consecutive labels, each prime occurring
  on an interval of steps, and a first-step prime dividing a suffix
  displacement) and the deleted set of sites where a witness starts; Lemma 5.3
  bounds its density by $\exp(-L^{1-\delta}/2)$. On blocks of
  $\lceil e^{103L}\rceil$ sites it builds symmetric matrices $A_d$, normalized
  by $\sqrt{w(n)w(n')}$, and the nonbacktracking operator
  $H_{d,d'}=\mathbf 1_{d\ne d'}A_{d'}$. Theorem 5.4 (p. 24):
  $\mathbb E\|H^k\|_{\mathrm{HS}}^2\le[K(C_2\sqrt W)^J]^{2k}$ with
  $k=\lfloor L\rfloor$ and $C_2$ absolute. Lemma 5.5 (p. 26) integrates
  singleton primes exactly before absolute values are taken; Lemma 5.6 discards
  words with many unlit occurrences.
- Section 6, Arithmetic savings for exceptional words (pp. 27--33). Lemma 6.1
  (p. 27), a rank estimate for random prime divisors, and Lemma 6.2 discard
  words whose consistency congruences have large rank over $\mathbb R$; the
  Lemmas numbered 6.3--6.5 show that many singleton primes force many positive
  witnesses with private primes, whose congruences are summed in a triangular
  order (adapting Pilatte's Lemmas 11.6, 13.1 and 13.6).
- Section 7, Counting the remaining words (pp. 33--38). Lemma 7.1 gives the
  geometry of perfect blocks; Lemma 7.2 (p. 35) codes the surviving equality
  patterns by a forest, at most $e^{Ck}$ per column uniformly in the padding;
  Lemma 7.3 (p. 37) sums the padding weights in one residue environment; and
  Section 7.4 completes Theorem 5.4, the square root of $W$ coming from repeated
  prime labels.
- Section 8, Spectral transfer and the bound at every scale (pp. 38--43).
  Lemma 8.1 (p. 39) bounds the norm of a projected sum of self-adjoint
  matrices, which need not commute, by three times the largest of the spectral
  radius of the associated nonbacktracking operator, a norm bound for each
  matrix and a square-sum bound on the range of the projection; Lemma 8.2
  supplies the last two for the edge matrices; Proposition 8.3 (p. 41) bounds
  the projected edge operator by $K(C_3\sqrt W)^J$ outside a fraction
  $e^{-2k}$ of blocks; Proposition 8.4 (p. 41) turns this into a bound for each
  retained bin sum. Section 8.4 (pp. 42--43) proves Proposition 2.1, with the
  exponent $c=\delta/(6WA)$.
- Section 9, The quantitative affine bound (pp. 43--44): the proof of
  Theorem 1.1 from Proposition 2.1.
- Section 10, The weighted divisor graph (pp. 44--46). At an auxiliary scale
  $B$ it fixes $\varepsilon=10^{-4}$, a core band of primes with
  $B^{1-\varepsilon/100}<\log p\le B$, weighted $A=\exp(2\kappa)$, and a center
  band with $B^{1-\varepsilon}<\log p\le B^{1-\varepsilon/100}$, weighted $1$;
  admissible divisor families of squarefree band products in a short interval
  $(H,\tau H]$; residue cutoffs $w_d$ on the number of core primes dividing a
  vertex; edge weights with uncentered core factors and center factors
  $\mathbf 1_{p\mid x}-\theta/p$, $\theta=1/4$; and a vertex weight $W(x)$ of
  mean $L_0$. Proposition 10.1 (p. 45): for arbitrary test functions
  $F,G:\mathbb N\to\mathbb D$ and coefficients $|a_d|\le1$ the centered
  bilinear sum is $\ll L_0B^{-1-c_*/2}$ in the long limit, with
  $c_*=\varepsilon/100$, uniformly in the family and the cutoffs.
- Section 11, Reduction to the graph estimate (pp. 46--49). Lemma 11.1 (p. 46)
  disposes of functions with $\sum_p(1-|f(p)|)/p=\infty$. A biased sequence
  $|S(N_j)|\ge\gamma N_j$ is assumed; Lemma 11.2 (p. 47) finds one short
  interval of divisors carrying mass $\gg L_0/B$, and Lemma 11.3 (p. 48) turns
  the bias into a raw dilated sum of that size. Proposition 11.4 (p. 49)
  bounds the cost of centering by $O(L_0(B^{-1-\varepsilon}+J/P_0))$, and the
  reduction of Theorem 1.2 (p. 49) reaches a contradiction for large fixed
  $B$.
- Section 12, The analytic centering estimate (pp. 50--55). Expands the center
  factors into sums over rough integers, removes the residue cutoffs by
  Fourier inversion (Lemma 12.1: finitely many prime changes keep uniform
  nonpretentiousness), imports Theorem 12.2 (p. 51, Matomäki--Radziwiłł--Tao,
  Theorem 1.7 in its corrected version), bounds the rough-number multiplier
  (Lemma 12.3, p. 52), and completes Proposition 11.4 by a split into large
  and small frequencies (p. 55).
- Section 13, Forbidden paths and arithmetic savings (pp. 55--60). Closed lines
  of length $\ell=2\lfloor B\rfloor$, path specifications and primitive ones
  (Definition 13.1, p. 56), the periodic set $Y$ of vertices where none
  qualifies, and Theorem 13.3 (p. 56): $Y$ misses a proportion at most
  $P_0^{-1+o(1)}$, $P_0=\exp(B^{1-\varepsilon})$, and the absolute closed-line
  sum with $Y$-restricted vertices is at most $B^{-(1+c_*)\ell}$. The Lemmas
  numbered 13.4--13.7 give the density bound, the structure of primitive
  specifications, a crude reciprocal count and a triangular arithmetic saving.
- Section 14, Connected activity on the first-visit tree (pp. 60--65).
  Proposition 14.1 (p. 61) keeps lines with few unlit repeated center
  occurrences, few disconnected active components and few corrupted singleton
  labels, at negligible cost; Lemma 14.4 uses the Erdős--Szekeres
  monotone-subsequence theorem.
- Section 15, A conditional cylinder sieve (pp. 65--71). Replaces the vertex
  restrictions by short lists of qualifying specifications through a truncated
  expansion over an intersection poset (Lemma 15.1, with Rota's Möbius
  function), private-prime constraints (Lemma 15.2) and Proposition 15.3
  (p. 70).
- Section 16, Summing the trace (pp. 71--79). A weighted-subtree identity, a
  record of prime labels, primewise integration in which a center prime on a
  single good edge cancels because $\theta=1/4$ is the square of the
  center-band vertex factor $\beta_Z=1/2$, pivot savings from the
  core band and the divisor interval, and the final count (Lemma 16.6) giving
  $B^{-(1+2c_*)\ell}$; Theorem 13.3 is completed on p. 79.
- Section 17, From high traces to the graph estimate (pp. 79--81). Block
  matrices on intervals of length about $B^{10}H$, a singular-value moment
  averaged over residues, a negligible set of exceptional blocks, and a
  Cauchy--Schwarz bilinear bound prove Proposition 10.1 and so Theorem 1.2
  (p. 81).
- Section 18, Local factors and affine correlations (pp. 81--86). Lemma 18.1
  (p. 81): twisting by a fixed character off a finite prime set, and
  conjugation, preserve uniform nonpretentiousness. Lemma 18.2 (p. 82): the
  dilate $m\mapsto f(m/a)\mathbf 1_{a\mid m}$ is a signed sum of $2^{\omega(a)}$
  normalized multiplicative functions agreeing with $f$ off the primes of
  $a$. Lemma 18.3 (p. 83): every residue indicator is a character sum of such
  dilates. Then
  [[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/proposition_18_4|Proposition 18.4]]
  (p. 84) and the proof of Corollary 1.3 (p. 84). Lemma 18.5 (p. 85) bounds
  $\inf_{|t|\le X}D(\lambda,\chi n^{it};X)$ below by
  $\frac14\sqrt{\log\log X}-O_\chi(1)$, from Lemma C.1 of
  Matomäki--Radziwiłł--Tao and the prime number theorem in progressions. The
  closing paragraph (p. 86) notes that $\mu$ has the same distances as
  $\lambda$, so Proposition 18.4 and Corollary 1.3 hold for any
  $f_1,f_2\in\{\lambda,\mu\}$, without a rate when $\mu$ is present.
- References (pp. 86--87), 21 items; five are cited at dated arXiv versions,
  among them Pilatte's paper, cited at arXiv v3 of 25 August 2026 and as
  published electronically in the Journal of the AMS on 10 September 2026.

The manuscript flags nothing as numerical, computer-assisted or conditional.
It says that the implied constants in Theorem 1.1 "need not be effective"
(p. 3), and the exponent $c=\delta/(6WA)$ is not given numerically: $A$
depends on the constant in Braverman's theorem at depth $22$ and $W$ on the
absolute trace constant. The release folder for this manuscript holds only the
PDF, the TeX build directory and the README; there is no `verification/`
folder.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using it. The nearest pages were read and none gives a row of the allowed
kinds. Problems 371 and 928, on the largest prime factors of $n$ and $n+1$,
are recorded as solved through the release's joint Dickman manuscript, which
does not cite this one. The open natural-density variant of Problem 1201 is
reached on its page only by a rejected conditional claim, under an unproven
hypothesis (named LPD there) on the joint distribution of the large prime
divisors of many consecutive integers at every scale, and only for
$\epsilon<1/2$; Theorem 1.2 concerns two fixed multiplicative functions and
supplies no such asymptotic.
