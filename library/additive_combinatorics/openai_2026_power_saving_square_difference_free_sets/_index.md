---
name: additive_combinatorics/openai_2026_power_saving_square_difference_free_sets
desc: |
  A 48-page release manuscript claiming absolute constants $c>0$ and $C$ with
  $|A|\le CN^{1-c}$ for every $A\subseteq\{1,\ldots,N\}$ with no difference
  equal to a positive square, the fixed power saving in the
  Furstenberg–Sárközy theorem asked for by Green and Sawhney, by a
  reflection-positive multilinear functional of Fourier lifts and an
  induction on scales; it names no Erdős problem.
license: Apache-2.0
created: 2026-10-12T23:13:55Z
updated: 2026-10-14T07:41:33Z
---

# additive_combinatorics/openai_2026_power_saving_square_difference_free_sets

[[additive_combinatorics/_index|..]]

[[additive_combinatorics/openai_2026_power_saving_square_difference_free_sets/theorem_1_1|theorem_1_1]]: The manuscript's main claim: absolute constants c > 0 and C such that every
subset of {1,...,N} in which no difference is a positive square has at
most C N^(1-c) elements, for every N >= 1. Claims checked only.

***

OpenAI, *A power saving for square-difference-free sets*, OpenAI Math Release
preprint, September 24, 2026. Released under the Apache License 2.0 at
<https://github.com/openai/math> (revision fd4aeeb2e), folder
`preprints/A-power-saving-for-square-difference-free-sets-September-24-2026`;
the held PDF, `paper.pdf` in the release, is retained as
[openai_2026_power_saving_square_difference_free_sets.pdf](openai_2026_power_saving_square_difference_free_sets.pdf),
and the release's TeX bundle in that folder is the TeX source cited on this
card. The license term was read in the release's root `LICENSE` file at that
revision on 2026-10-12.

```bibtex
@misc{OAI:A-power-saving-for-square-difference-free-sets-September-24-2026,
  author = {{OpenAI}},
  title = {{A power saving for square-difference-free sets}},
  howpublished = {OpenAI Math Release preprint
                  \href{https://github.com/openai/math/blob/main/preprints/A-power-saving-for-square-difference-free-sets-September-24-2026/paper.pdf}{OAI:A-power-saving-for-square-difference-free-sets-September-24-2026}},
  year = {2026}
}
```

The held PDF has 48 pages with a text layer; its title page is dated
September 24, 2026, and its metadata records no creation date (the TeX source
sets `\pdfinfoomitdate=1`, which omits it). The TeX source is the bundle's
`build/` directory: `main.tex` (60 lines), nine section files under
`sections/` (3,665 lines), three figure and table files under `figures/` (88
lines) and `references.bib` (203 lines, 16 entries), 4,016 lines in 14 files.
The TeX bundle and the PDF are the text read here.

**Attestation.** The release README states that the repository holds
manuscripts "produced by an internal OpenAI model", that the collection
"includes results at different stages of verification", that "Not all have
accompanying Lean formalizations" and that "Some of the unformalized results
could have issues". Its account of the method says that "The vast majority of
results were obtained with the same procedure using an unreleased internal
OpenAI model"; the exceptions it names (a zero-free region for the Riemann
zeta function and the Hodge conjecture for CM abelian varieties) concern other
subjects. The manuscript's own README carries only the title, the
author line "OpenAI", the date and the citation block, and adds no sentence
about authorship, assistance or verification. The title page names OpenAI as
the sole author, and the manuscript has no acknowledgment, affiliation or
funding note. These are the source's own statements, recorded as attestations
and not as this corpus's review. No refereed publication, arXiv version or
independent review of the manuscript is recorded here, and nothing on this
card is independently reviewed.

**Formalization.** The release's Lean page for its family, `lean/docs/182.md`,
carries the family's title but names only this manuscript as its accompanying
paper. Its scope paragraph says the formalization proves the fixed power saving:
absolute constants $c>0$ and $C$ such that every $A\subseteq\{1,\ldots,N\}$ with
$a-b\ne m^2$ for all $a,b\in A$ and integers $m\ge1$ has $|A|\le CN^{1-c}$,
uniformly for every integer $N\ge1$. It links one comparator statement,
`lean/ComparatorChallenges/SquareDifference.lean`, which defines a finite set of
integers to be square-difference-free when no difference $a-b$ of two of its
elements equals $m^2$ for a natural number $m\ge1$, and states
`OAI.SquareDifference.power_saving` with its proof left open as the challenge.
In words, that statement says: there are real numbers $c>0$ and $C$ such that,
for every natural number $N\ge1$ and every square-difference-free finite set $A$
of integers contained in $\{1,\ldots,N\}$, $|A|\le C\,N^{1-c}$. The companion
`SquareDifference.json` names the solution module
`OAI.Combinatorics.SquareDifference.Main`, the theorem
`OAI.SquareDifference.power_saving` and the permitted axioms `propext`,
`Quot.sound` and `Classical.choice`; the release tree holds that library under
`lean/OAI/Combinatorics/SquareDifference/` (81 files). The release's catalog
`lean/formalization.yaml` lists no entry for this manuscript at this revision,
either among its `sources` or under its `status.main_results`,
and its own `review` field reads `status: unchecked`. All of this is
read statically from the release; nothing was built, replayed or audited for
fidelity in this repository. No Lean file here is a proof of any Erdős problem.

**Companions.** The release groups this manuscript with two manuscripts dated
October 5, 2026. The first, *A power saving for intersective polynomial
differences with an exponent depending only on the degree*, is filed at
[[additive_combinatorics/openai_2026_power_saving_intersective_polynomial_differences/_index|the intersective-polynomial card]];
the release's manuscript map describes it as a bound $O_h(N^{1-c_k})$ for
subsets of $\{1,\ldots,N\}$ whose differences avoid the nonzero values
$h(1),h(2),\ldots$ of an intersective integer polynomial $h$ (one with a root
modulo every positive integer) of degree $k\ge2$ with positive leading
coefficient, the exponent depending only on $k$. Taken as stated there, its case
$h(n)=n^2$ (intersective, since $0$ is a root modulo every integer) is Theorem
1.1; that reading is this card's inference, not the map's. The second, *A Power
Saving for Polynomial Differences at Prime Arguments*, is filed at
[[additive_combinatorics/openai_2026_power_saving_polynomial_differences_prime_arguments/_index|the prime-argument card]];
the map describes it as a bound $C_hN^{1-c_h}$ for sets whose differences avoid
the nonzero values $h(p)$ at primes $p$, for $h$ of degree at least two with
positive leading coefficient and a unit root modulo every positive integer,
proved with the release's zero-free half-plane theorem for Dirichlet
$L$-functions. This manuscript cites neither, and the release holds no earlier
dated version of it. The companions' arguments were not read for this card.

Read status: claims checked for Theorem 1.1 and Remark 1.2, with the
definitions of a square-difference-free set and of $s(N)$, read clause by
clause in the release's TeX source (`build/sections/introduction.tex` lines
4--46, label `thm:main` at lines 15--25), together with the statements of
Proposition 3.1 (`tuples.tex` lines 55--95), Proposition 4.1 and Lemma 4.2
(`functional.tex` lines 43--55 and 184--205), Lemma 4.3 (`functional.tex`
lines 271--288), Lemma 5.2 (`lifts.tex` lines 68--91), Proposition 6.1
(`kernel.tex` lines 34--61), Proposition 7.2 (`transfer.tex` lines 119--167),
Lemma 8.1 and Proposition 8.2 (`contraction.tex` lines 24--30 and 71--84),
Proposition 9.1 and Theorem 9.2 (`induction.tex` lines 39--55 and 201--207),
and the parameter choices they use (`tuples.tex` lines 14--23, `kernel.tex` line
16, `transfer.tex` lines 41--50, `induction.tex` lines 217--222); the proofs,
including the closing proof of Theorem 1.1 (`induction.tex` lines 303--318),
were read for their structure only and no step was checked; nothing here is
independently reviewed.

## Contents

The PDF has 48 pages: the title, abstract and table of contents on p. 1 and
nine sections on pp. 2--47. Results are numbered within sections
(Theorem 1.1, Lemma 2.1, Proposition 3.1), and the section files under
`build/sections/` follow the printed order.

- Section 1, Introduction (pp. 2--5; `introduction.tex`). Writes
  $[N]=\{1,\ldots,N\}$, calls $A\subseteq[N]$ square-difference-free when no
  difference of two of its elements is the square of a positive integer, and
  lets $s(N)$ be the largest size of such a set. States
  [[additive_combinatorics/openai_2026_power_saving_square_difference_free_sets/theorem_1_1|Theorem 1.1]]
  (p. 2): absolute $c>0$ and $C<\infty$ with $|A|\le CN^{1-c}$ for every
  $N\ge1$ and every such $A$; the exponent is called "extremely small" and
  the argument gives no useful numerical value. Remark 1.2 (p. 2) draws the
  coloring form: with $c$ reduced below $1$ if necessary, once
  $N>(Cr)^{1/c}$, every $r$-coloring of $[N]$ has one color containing some
  $a$ and $a+d^2$ with $d\ge1$, and the graph on $[N]$ joining integers at
  square distance has chromatic number at least
  $N/s(N)\ge C^{-1}N^c$ (cited to Beigel and Gasarch, Section 4, as the
  classical square-difference coloring problem). Section 1.1 (pp. 2--3)
  traces the problem to a question of Lovász and lists the upper bounds:
  $s(N)=o(N)$ by Furstenberg (Theorem 1.2) and by Sárközy, Sárközy's
  $N/(\log N)^{1/3+o(1)}$, Pintz, Steiger and Szemerédi's
  $N/(\log N)^{c\log\log\log\log N}$ (Theorem 1), Bloom and Maynard's
  $N/(\log N)^{c\log\log\log N}$, and Green and Sawhney's
  $N\exp(-c\sqrt{\log N})$ (Theorem 1.1), whose Section 1.1 poses the
  fixed-power question that the manuscript says it answers; Adajar and
  coauthors extend the level-$d$ method to intersective polynomials with a
  saving $\exp(-c(\log N)^\mu)$, $\mu<1/2$. The lower bounds are Ruzsa's
  exponent $\tfrac12(1+\log7/\log65)=0.7330\ldots$, the exponent
  $\tfrac12(1+\log12/\log205)=0.7334\ldots$ of Beigel--Gasarch and Lewko, and
  Krachun's $\liminf\log s(N)/\log N\ge0.7527\ldots$. Multilinear inequalities
  from reflection positivity are traced to the chessboard method of Fröhlich
  and Lieb (Theorem 2.2) and its abstract form by Fröhlich, Israel, Lieb and
  Simon (Theorem 4.1), with Hatami and Conlon--Lee on graph seminorms.
  Section 1.2 (pp. 3--5) outlines the proof, with Figure 1 as its dependency
  map; Section 1.3 (p. 5) fixes conventions, among them that the conductor
  of a rational frequency is its reduced denominator.
- Section 2, finite-field square constraints (pp. 6--7; `graph.tex`). For an
  odd prime $p$, Lemma 2.1 (p. 6): if independent uniform labels in
  $\mathbb F_p$ sit on the vertices of a directed graph with $m$ edges, no
  loops and at most one edge per pair, the probability that every edge has a
  nonzero square difference is $2^{-m}$ up to $m(\sqrt p+1)/(2p)$, by a
  Gauss-sum bound for the single-constraint kernel. Lemma 2.2 (p. 7): for
  constraints only between two disjoint lists, the constraint kernel differs
  from the constant $2^{-m}$ by at most $(32m)^{1/4}p^{-1/8}$ in operator
  norm, by a four-cycle count.
- Section 3, finite reflection-positive probability laws (pp. 7--18;
  `tuples.tex`). Fixes $h=24$, $t_0=80$, $\ell=161$, the slot set $V$ of
  $\ell$-tuples of permutation words on $24$ symbols, of size
  $d=(24!)^{161}$, and a designated directed $24$-cycle of slots; a
  reflection swaps two symbols in one block. Proposition 3.1 (Tuple laws,
  p. 8): for every prime $p$ at least an absolute threshold $P$ there are a
  probability law $\mu_p$ on labelings $V\to\mathbb F_p$ and a submeasure
  $\varepsilon_p\le\mu_p$ of mass at most $p^{-4}$ such that $\mu_p$ is
  reflection positive, both are invariant under $z\mapsto qz+a$ with $q$ a
  nonzero square, single labels are uniform, the normalized nonexceptional
  law forces a nonzero square difference along each designated cycle edge
  with each edge pair uniform among such pairs, and the full law and the
  normalized nonexceptional law both mix conditionally with rate
  $p^{-1/64}$. The law is a weighted mixture over sets of marked blocks, in
  which slots agreeing outside the marked blocks draw from shared lists with
  an index weight. Lemmas 3.2--3.5 (pp. 10--14: symmetry of each component,
  a lower bound at a marked cut, an error bound at an unmarked cut, and
  domination after marking a block) show that a marked component dominates
  the negative part of the cut form at the corresponding unmarked cut, and
  the pairing of components that follows (pp. 14--15) makes the mixture
  reflection positive; Lemma 3.6 (p. 16) proves the conditional mixing and
  the pair marginals.
- Section 4, signed multilinear forms and conductor decay (pp. 18--23;
  `functional.tex`). With $\mu_{\mathcal P}$ the product of the laws over a
  finite prime set $\mathcal P$ and
  $Z_{\mathcal P}(g)=\mathbb E\prod_{v\in V}g(z_v)$, Proposition 4.1 (Signed
  Hölder inequality, p. 19) gives $Z_{\mathcal P}(g)\ge0$ and bounds the
  multilinear form with inputs $g_v$ by $\prod_vZ_{\mathcal P}(g_v)^{1/d}$ in
  absolute value, for real inputs of any sign, by a finite folding argument
  along sorting sequences of reflections. Lemma 4.2 (p. 20):
  $Z_{\mathcal P}(g)^{1/d}$ is a seminorm bounding $|\mathbb E g|$,
  invariant under coordinatewise maps
  $x_p\mapsto r_px_p+a_p$ with $r_p$ a nonzero square, and contracted by
  averaging out coordinates. Lemma 4.3 (Conductor decay, p. 21): if one input
  has no Fourier coefficient of conductor at most $R$, the multilinear
  integral is at most $R^{-1/64}$ times $L^2$ and $L^{2(d-1)}$ norms of the
  inputs, for any choice of full or nonexceptional law at each prime.
- Section 5, uniform moment bounds for Fourier lifts (pp. 23--28;
  `lifts.tex`). The Fourier lift of a function on an interval keeps its
  rational coefficients at squarefree denominators at most $Q$ built from a
  prime set $\mathcal P$, read as a function on
  $\prod_{p\in\mathcal P}\mathbb F_p$; Remark 5.1 (p. 23) shows that the
  lift of an indicator can be negative. Lemma 5.2 (p. 24): for interval
  length at least $10Q^6$ and $|f|\le M$, the $L^{2r}$ norm of any lift built
  from complete denominator classes is at most $MQ^{o(1)}$ for each fixed
  $r$, uniformly in the interval, the function, the prime set and the classes
  kept, by a conditional square-sum bound, square-function moments and a
  symmetrization over random colorings of the primes. Lemma 5.3 (p. 27)
  bounds the cost of fixing coordinates on a prime set $B$ by
  $q_B^{1/p}$ in $L^p$.
- Section 6, a signed kernel for actual square differences (pp. 28--35;
  `kernel.tex`). Fixes $\beta=10^{-5}$, the normalized unit quadratic sum
  $\mathfrak g(\xi)$ and strict square classes modulo $D=8d_0$ ($1$ modulo $8$
  and a nonzero square at each prime of the odd squarefree $d_0$).
  Proposition 6.1 (Ordered square-kernel estimate, p. 28): for $D\le N^\beta$
  and two functions on $[N]$ bounded by $1$, supported in residue classes
  modulo $D$ whose difference is a strict square class, with the first
  support entirely before the second and no positive square difference from
  the first to the second, $D$ times their bilinear Fourier sum weighted by
  $\mathfrak g$ over squarefree conductors at most $H=N^{\beta/2}$ coprime
  to $D$ is $O(H^{-1/3})$ with an absolute constant; the proof compares
  the model kernel with a signed kernel supported on actual squares, by
  Weyl differencing on minor arcs and Gauss sums on major arcs. Remark 6.2
  (p. 35) records the normalization for interval restrictions.
- Section 7, comparison along square-step progressions (pp. 35--39;
  `transfer.tex`). Enlarges $P$, sets $M_0=8\prod_{3\le p<P}p$, $Q=N^\beta$,
  the prime set $\mathcal P_N$ of primes in $[P,Q]$, the exponents $\tau$ and
  $\sigma_0$, and the quantity $Y(N,A)$, the functional of the lift of
  $1_A$. Lemma 7.1 (p. 36) makes the low coefficients exact averages over a
  residue class once the coordinates at a prime set $B$ are fixed.
  Proposition 7.2 (Comparison with a shorter interval, p. 36): for $N$
  beyond a fixed threshold and a square-difference-free $A$, when the
  primes of $B$ have product $q_B\le N^\tau$, the specialized functional,
  also with mixed inputs, is at most $\lambda^d$ times the largest $Y$ at
  length $\lceil N/(M_0q_B)^2\rceil$ plus $O(N^{-\sigma_0})$, with
  $1\le\lambda<1+(M_0q_B)^2/N$, by splitting into progressions of square
  step.
- Section 8, contraction on ordered intervals (pp. 39--43;
  `contraction.tex`). A residue tuple modulo $M_0$ is good when every
  designated cycle difference is a strict square class. Lemma 8.1 (p. 40):
  good tuples have proportion at least $M_0^{-23}$, which the text says
  explains the cycle length $24$. Proposition 8.2 (p. 40): for $N$ beyond a
  fixed threshold and good tuples, the integral against the product of the
  nonexceptional parts $\mu_p-\varepsilon_p$ is $O(N^{-\sigma_0})$,
  uniformly in the square-difference-free set, by partition into short
  ordered intervals and Proposition 6.1.
- Section 9, exceptional terms and the power-saving induction (pp. 43--47;
  `induction.tex`). Proposition 9.1 (p. 44) is the recurrence for the
  largest value $\mathcal Y(N)$ of $Y(N,A)$, from an inclusion--exclusion over
  the exceptional submeasures. Theorem 9.2 (p. 46): $Y(N,A)\le C_0N^{-a_0}$
  for absolute $a_0>0$, $C_0$, by strong induction; Table 1 (p. 46) lists the
  order in which the parameters are fixed. The proof of Theorem 1.1 (p. 47)
  takes $c=a_0/d$ and $C=C_0^{1/d}$.
- References (pp. 47--48): 16 entries, from Furstenberg 1977 and Sárközy 1978
  to Krachun (arXiv:2608.01325v1, 2026) and Adajar and coauthors
  (arXiv:2605.16216v2, 2026).

The manuscript flags nothing as numerical, computer-assisted or conditional.
Its constants are fixed in a stated order but are not numerically explicit
(the threshold $P$ is taken large enough for finitely many stated conditions
and never computed). Its estimates are proved in the
text from standard facts (quadratic Gauss sums, Dirichlet approximation, the
Chinese remainder theorem); the chessboard method, the large sieve,
decoupling by symmetrization and the work of Green--Sawhney, Bloom--Maynard
and Pintz--Steiger--Szemerédi are cited as precedents for its methods rather
than imported as results. The release folder
holds only the README, the PDF and the TeX build directory; there is no
`verification/` folder.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using it. Its target is the Furstenberg--Sárközy problem on $s(N)$ and the
fixed-power question Green and Sawhney pose in Section 1.1 of their paper,
neither of which is a problem page in this corpus. The pages nearest in subject,
Problems 438 and 439, were read and do not qualify: they ask about squares among
sums $a+a'$ (of two elements of one set, or of two integers of one color), not
among differences; a set of positive density can have no square sum (the residue
class $1\bmod3$), and no deduction between the two settings is known to this
card. The library card
[[integer_sequences/erdos_1977_differences_sums_integers_ii/_index|Erdős and Sárközy, On differences and sums of integers, II]]
records, in its account of that paper's Section 1, the authors' guess that
Sárközy's density threshold forcing a square difference could be lowered to
$N^{1/2+\varepsilon}$. Theorem 1.1 is a claimed threshold $CN^{1-c}$ for the
same quantity, with an unspecified tiny $c$; it neither confirms nor refutes
that guess, whose literal form already fails for $\varepsilon<0.23$ by Ruzsa's
lower bound, which the manuscript cites. That comparison is this card's
inference, not the manuscript's.
