---
name: irrationality/openai_2026_catalans_constant_irrational
desc: |
  A 44-page manuscript of the OpenAI mathematics release claiming that
  Catalan's constant G, the sum of (-1)^j/(2j+1)^2 over j >= 0, is irrational,
  by comparing a finite-place lower bound with a certified real-place upper
  bound for growing determinants of mixed moments; it names no Erdős problem.
license: Apache-2.0
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

# irrationality/openai_2026_catalans_constant_irrational

[[irrationality/_index|..]]

[[irrationality/openai_2026_catalans_constant_irrational/theorem_1_1|theorem_1_1]]: The manuscript's only theorem: Catalan's constant G, the sum of
(-1)^j/(2j+1)^2 over j >= 0, is irrational; a qualitative statement with no
irrationality measure. Claims checked only.

***

OpenAI, *Catalan's constant is irrational*, OpenAI Math Release preprint,
September 24, 2026. Released under the Apache License 2.0 at
<https://github.com/openai/math> (revision fd4aeeb2e), folder
`preprints/Catalans-constant-is-irrational-September-24-2026`; the held PDF,
`paper.pdf` in the release, is retained as
[openai_2026_catalans_constant_irrational.pdf](openai_2026_catalans_constant_irrational.pdf),
and the release's TeX bundle in that folder is the TeX source cited on this
card. The license term was read in the release's root `LICENSE` file at that
revision on 2026-10-12.

```bibtex
@misc{OAI:Catalans-constant-is-irrational-September-24-2026,
  author = {{OpenAI}},
  title = {{Catalan's constant is irrational}},
  howpublished = {OpenAI Math Release preprint
                  \href{https://github.com/openai/math/blob/main/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf}{OAI:Catalans-constant-is-irrational-September-24-2026}},
  year = {2026}
}
```

The held PDF has 44 pages with a text layer; its title page is dated 24
September 2026 and its metadata records a creation date of 24 September 2026.
The TeX source is `build/main.tex` (44 lines), which inputs eight section
files under `build/sections/` (2,957 lines in all: `introduction.tex` 208,
`foundations.tex` 434, `odd-primes.tex` 672, `nonvanishing.tex` 413,
`real-place.tex` 420, `energy.tex` 288, `certificate.tex` 471 and
`conclusion.tex` 51) and cites `build/references.bib` (28 entries); it is
the text read here.

**Attestation.** The release README states that the repository holds
manuscripts "produced by an internal OpenAI model", that the collection
"includes results at different stages of verification", that "Not all have
accompanying Lean formalizations" and that "Some of the unformalized results
could have issues". Its account of the method says that "The vast majority of
results were obtained with the same procedure using an unreleased internal
OpenAI model"; the exceptions it names (a zero-free region for the Riemann
zeta function and the Hodge conjecture for CM abelian varieties) do not
include this family. The manuscript's own README carries only the title, the
author line "OpenAI", the date and the citation block, and adds no sentence
about authorship, assistance or verification. The title page names OpenAI as
the sole author, and the manuscript carries no acknowledgment. These are the
source's own statements, recorded as attestations and not as this corpus's
review. No refereed publication, arXiv version or independent review of the
manuscript is recorded here and nothing on this card is independently
reviewed.

**Formalization.** The release's Lean page for its family, `lean/docs/005.md`,
says the formalization proves that $G=\sum_{j\ge0}(-1)^j/(2j+1)^2$ is
irrational, "the mathematical assertion in the paper's title", and links one
comparator statement, `lean/ComparatorChallenges/Catalan.lean`. That file
states, with its proof left as `sorry`, the theorem
`OAI.InternalCatalan.catalan_irrational`: in words, the real number obtained as
Mathlib's unconditional sum over all natural numbers $j$ of $(-1)^j/(2j+1)^2$
(an absolutely summable family, so this sum is $G$) is irrational. Its
configuration `Catalan.json` names the solution module
`OAI.NumberTheory.Catalan.Main`, no definitions, and the permitted axioms
`propext`, `Quot.sound` and `Classical.choice`. The comparator statement is
Theorem 1.1 alone; the manuscript's intermediate propositions and its
hyperbolic-volume consequences are not part of it. The release's catalog
`lean/formalization.yaml` at this revision lists no entry for this comparator
under its `status.main_results`, and the catalog's own `review` field reads
`status: unchecked`. All of this is read statically from the release's files;
nothing was built, replayed or audited for fidelity in this repository. No Lean
file here is a proof of any Erdős problem.

**Companions.** The release lists this manuscript as the only member of its
family, in both its manuscript map and its overview, and holds no earlier dated
version of it; the release history records no revision of it. There are no
companions.

Read status: claims checked for Theorem 1.1, read clause by clause in the
release's TeX source (`build/sections/introduction.tex`, the definition of
$G$ at lines 3--8 and label `thm:main` at lines 16--18), together with the
definition of the determinant $\Delta_N$ (`foundations.tex` lines 9--89),
the statements of Proposition 2.1 (`prop:rationality`, `foundations.tex`
lines 243--247), Proposition 2.2 (`prop:two-adic`, lines 271--280),
Proposition 3.4 (`prop:finite-lower`, `odd-primes.tex` lines 516--526),
Proposition 4.1 (`prop:nonvanishing`, `nonvanishing.tex` lines 7--14) and
Proposition 7.1 (`prop:real-upper`, `certificate.tex` lines 7--16), the
closing proof (`conclusion.tex` lines 3--16) and the paragraph on hyperbolic
volumes (`conclusion.tex` lines 18--51), on 2026-10-12; the proofs were read
for their structure only and no step was checked; no certificate was
recomputed; nothing here is independently reviewed.

## Contents

Result numbers and page numbers below are the PDF's; results are numbered
within sections.

- Title page and Section 1, Introduction (pp. 1--3). Defines
  $G=\beta(2)=\sum_{j\ge0}(-1)^j/(2j+1)^2$, the value at $2$ of the
  Dirichlet beta function, equivalently $L(2,\chi_{-4})$, and states
  [[irrationality/openai_2026_catalans_constant_irrational/theorem_1_1|Theorem 1.1]]
  (p. 1). Section 1.1 reviews the family results that guarantee irrational
  even beta values without naming one (Rivoal--Zudilin, Theorems 1 and 2;
  Zudilin 2019, Theorem 1; Lai--Zhou, Theorem 6.1; Fischler 2020), the
  criterion that nonzero integer forms $A_mG-B_m$ must tend to zero, Apéry's
  and Beukers's proofs for $\zeta(2)$ and $\zeta(3)$, Zudilin's Apéry-like
  recurrences for $G$ whose integer forms do not tend to zero, the
  denominator bounds of Rivoal and of Krattenthaler--Rivoal, the identity of
  Krattenthaler--Zudilin, Nesterenko's approximations, the Viola--Marcovecchio
  exponent $0.6293\ldots$ and an Eskandari preprint (September 2026) with
  $0<|G-p_m/q_m|\le q_m^{-0.62}$, which the text calls bounds for particular
  constructions, not irrationality measures. It compares Calegari, Dimitrov
  and Tang's linear independence of $1,\pi^2,L(2,\chi_{-3})$ and Calegari's
  $2$-adic analogue of $G$, and records that Sun (arXiv, September 2026) has
  announced a proof of the same statement, from which nothing is used.
  Section 1.2 outlines the method: determinants $\Delta_N$ of size $n=48N$
  whose entries are combinations of moments in
  $\mathbb Q+\mathbb QG+\mathbb Q\zeta(2)$, rows with Taylor contact that
  cancels $\zeta(2)$, a product-formula lower bound against an integral
  upper bound, with Zudilin's determinantal criterion (2017) as precedent;
  it defines the normalized logarithm
  $\mathcal L_N=\log|\Delta_N|/(48N)^2-\tfrac12\log2$ and quotes the two
  constants $-2.29084$ and $-2.290939875$. It says the argument is
  qualitative and gives no irrationality measure. Section 1.3 states that
  the only prime-distribution input is the prime number theorem.
- Section 2, Polynomial rows and mixed moments (pp. 3--10). Fixes
  $n=48N$, $a=11N$, $b=7N$, $q=g=4N$, $h=2N$, $L=59N$, $C=63N$, $H=65N$,
  $A=19N$, the parametrization $t=2w/(1+w^2)$, $f=\sqrt{1-t^2}$, and rows
  $R_r=(1-t)^ht^{C-1}w^{r-g}$ for $0\le r<n$. Averaging $R_r$ with its image
  under $w\mapsto1/w$ gives $P_r$, and the image minus $R_r$, times
  $t/(2f)$, gives $D_r$; both are integer polynomials (Chebyshev
  polynomials $T_d$, $U_{d-1}$ at $1/t$, $d=|r-g|$, times
  $(1-t)^ht^{C-1}$, with the sign of $r-g$ on $D_r$), and
  $tP_r/f-D_r=O(t^L)$. Defines the two moment functionals $M(i,j)$ (a
  double integral over $t\in(-1,1)$, $s\in(0,1)$ with weight
  $|t|/\sqrt{1-t^2}$ and kernel $t^is^j/(1-ts)$) and $Z(i,j)$ (over
  $(0,1)^2$), the raw columns $F_j(r)=M(P_r,j)-\tfrac32Z(D_r,j)$, and
  $\Delta_N$ as the $n\times n$ determinant against the filtered columns
  $s^{b+k}(1-s)^q$ (eq. (7), p. 5), an integer binomial filter of the raw
  columns. Section 2.1 evaluates $M$ as a rational array plus $4G$ and
  $\tfrac32\zeta(2)$ times central-binomial kernels, from the starting
  values $4G$ and $\pi^2/4$, and $Z$ as a rational array plus $\zeta(2)$
  on the diagonal. Proposition 2.1 (p. 7): every raw entry lies in
  $\mathbb Q+\mathbb QG$, so $G\in\mathbb Q$ makes every $\Delta_N$
  rational. Section 2.2, Proposition 2.2 (p. 8): under
  $G\in\mathbb Q$, $v_2(\Delta_N)\ge-\tfrac{505}{4608}n^2-O_G(n\log(n+2))$,
  and the same for every full raw minor.
- Section 3, Odd primes and the finite-place lower bound (pp. 10--19).
  Assuming $G\in\mathbb Q$: Lemma 3.1 (digit reductions, p. 11) gives the
  residues of $p^2$ times the rational moment arrays modulo $p$ for
  $2\sqrt H<p\le H$; Section 3.2 pairs raw columns whose sum has at most
  one power of $p$ in its denominator, giving a bound for
  $2\sqrt H<p\le H/2$; Lemma 3.2 (central
  layer, p. 14) and Lemma 3.3 (elimination over the local integers, p. 15)
  give $v_p(\Delta_N)\ge-\min(2n,n+R,2R+S)$ for $H/2<p\le H$ with explicit
  counts $R,S$. Proposition 3.4 (finite-place bound, p. 17): along any
  sequence $N\to\infty$ with $\Delta_N\ne0$, the lower limit of
  $\log|\Delta_N|/n^2-\tfrac12\log2$ is at least
  $-\tfrac{8609}{4608}-\tfrac{2809}{4608}\log2$, which exceeds $-2.29084$.
  The proof tabulates a piecewise-linear loss $d(p/N)$ on $[0,65]$ with
  integral $8609/2$, shows the primes below $2\sqrt H$ cost $o(n^2)$, sums
  with the prime number theorem (cited to Zagier's account of Newman's
  proof), adds the prime $2$ and applies the product formula.
- Section 4, Nonvanishing along the prime sequence (pp. 19--25).
  Proposition 4.1 (p. 19): under $G\in\mathbb Q$, for every sufficiently
  large prime $p$, $v_p(\Delta_p)=-96p$, so $\Delta_p\ne0$. The first
  three subsections take $N=p$, use two bases of a space of palindromic
  polynomials over $\mathbb F_p$ and Frobenius to express each scaled row
  through two rows of a fixed rational $49\times48$ matrix $\mathcal B$
  built at $N=1$, and factor the reduced determinant as a power of $2$ times
  $\det\mathcal B_0$, $\det(\mathcal B_0+\mathcal B_1)^{(p-1)/2}$ and
  $\det(\mathcal B_0-\mathcal B_1)^{(p-1)/2}$. Section 4.4 certifies the
  three fixed determinants nonzero by Gaussian elimination modulo $101$,
  with rational recipes for the entries and the full pivot list (Table 1,
  p. 24).
- Section 5, The real-place determinant estimates (pp. 25--30). Without any
  rationality hypothesis: Andréief's identity, applied twice (cited to
  Forrester), and Cauchy's double alternant (cited to Krattenthaler) write
  $\Delta_N$ as a multiple integral whose row determinant mixes evaluations
  at $x_i$ and $1/x_i$, $x=t/(1+\sqrt{1-t^2})$. Lemma 5.1 (p. 26) builds,
  when $\sum_i(1-x_i^2)/(1+x_i^2)\le40N-1$, an interpolating function
  bounded by $10e^{12}n$ on the closed unit disk; Proposition 5.2
  (interpolation estimate, p. 28) bounds the row determinant in that case by
  a compression of the multiplication operator to an $n$-dimensional
  subspace of $H^2$, avoiding any inverse Vandermonde bound; Proposition 5.3
  (Hadamard estimate, p. 29) covers every configuration. Section 5.4
  reduces $\log|\Delta_N|/n^2-\tfrac12\log2$ to the larger of two suprema
  of explicit integrand majorants, up to $O(\log n/n)$.
- Section 6, A uniform energy bound (pp. 30--34). Proposition 6.1 (p. 31)
  bounds the limit superior of each supremum by $-\tfrac{11}{16}\log2$ plus
  quadratic norms of two freely chosen trial sequences and two one-variable
  suprema, through the Chebyshev expansion of the logarithmic kernel (cited
  to Garoufalidis--Popescu, Lemma 3.1), damping, completed squares, and the
  inequality $-a^2\le b^2-2ab$.
- Section 7, An exact certificate for the two barriers (pp. 34--42).
  Proposition 7.1 (p. 34): without hypothesis, the upper limit of
  $\log|\Delta_N|/n^2-\tfrac12\log2$ is at most $-2.290939875<-2.2909$. The
  section gives explicit rational trial sequences, counts the stationary
  points of the two one-variable functions by Descartes' rule of signs
  (proved in the text), isolates them in brackets of width $2\cdot10^{-10}$,
  evaluates logarithms and arctangents by rational series with explicit
  remainders, lists fifty certified value bounds (Table 2, pp. 39--40), and
  passes to global suprema by a derivative bound.
- Section 8, Conclusion (p. 42). The proof of Theorem 1.1 combines
  Propositions 2.1, 4.1, 3.4 and 7.1 along large primes and compares the
  rounded constants $-2.29084>-2.2909$. The manuscript states no margin;
  computed for this card, the exact lower constant of Proposition 3.4,
  about $-2.29081$, exceeds the upper constant $-2.290939875$ of
  Proposition 7.1 by about $1.3\cdot10^{-4}$. A closing paragraph deduces,
  from Agol's identification of $4G$ as the least volume of an orientable
  complete finite-volume hyperbolic 3-manifold with exactly two cusps, that
  this minimum is irrational, and, from Voight's
  volume formula, that every orientable arithmetic hyperbolic 3-orbifold
  defined over $\mathbb Q(i)$ has volume a positive rational multiple of $G$,
  hence irrational.
- References (pp. 42--44), 28 items, including the Sun and Eskandari
  preprints named above.

The manuscript presents its finite checks (the pivots modulo $101$ in
Section 4.4; the trial sequences, root brackets and value bounds in
Section 7) as exact rational computations specified in the text, and says
that
"supplementary programs reproduce them" (p. 3). The release folder at this
revision holds only the README, the PDF and the TeX build directory: no
programs and no `verification/` folder. Nothing was recomputed here. The
manuscript flags no input as conditional.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using it. The problem pages were searched for Catalan's constant, the
Dirichlet beta function, $L(2,\chi_{-4})$ and hyperbolic volumes, and the
statements of the irrationality problems were read; none asks about $G$ or
these values, and none records an argument that takes the irrationality of
$G$ or this determinant method as an input.
