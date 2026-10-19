---
name: irrationality/openai_2026_irrationality_exponent_pi_2
desc: |
  A 23-page release manuscript claiming that the irrationality exponent of pi
  is 2, by an interpolation-determinant argument on logarithmic curves built
  from hypothetical good rational approximations to pi, and deducing that the
  Flint-Hills series sum 1/(n^3 sin^2 n) converges and that
  sum 1/(n^a |sin n|^b) converges exactly when a > max(1, b); it names no
  Erdős problem.
license: Apache-2.0
created: 2026-10-12T23:13:55Z
updated: 2026-10-14T07:41:33Z
---

# irrationality/openai_2026_irrationality_exponent_pi_2

[[irrationality/_index|..]]

[[irrationality/openai_2026_irrationality_exponent_pi_2/corollary_1_2|corollary_1_2]]: The manuscript's stated consequence: the Flint–Hills series, the sum over
n >= 1 of 1/(n^3 sin^2 n) with n in radians, converges, deduced from
Theorem 1.1 by a dyadic spacing argument. Claims checked only.

[[irrationality/openai_2026_irrationality_exponent_pi_2/corollary_5_2|corollary_5_2]]: The manuscript's generalized Flint–Hills criterion: for fixed a, b > 0 the
sum over n >= 1 of 1/(n^a |sin n|^b), n in radians, converges if and only
if a > max(1, b); the convergence half rests on Theorem 1.1. Claims
checked only.

[[irrationality/openai_2026_irrationality_exponent_pi_2/theorem_1_1|theorem_1_1]]: The manuscript's main claim: for every nu > 2, all large enough
denominators q satisfy |pi - p/q| >= q^(-nu) for every integer p, so the
irrationality exponent of pi is 2, with an ineffective threshold. Claims
checked only.

***

OpenAI, *The irrationality exponent of $\pi$ is $2$*, OpenAI Math Release
preprint, September 24, 2026. Released under the Apache License 2.0 at
<https://github.com/openai/math> (revision fd4aeeb2e), folder
`preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026`; the held
PDF, `paper.pdf` in the release, is retained as
[openai_2026_irrationality_exponent_pi_2.pdf](openai_2026_irrationality_exponent_pi_2.pdf),
and the release's TeX bundle in that folder is the TeX source cited on this
card. The license term was read in the release's root `LICENSE` file at that
revision on 2026-10-12.

```bibtex
@misc{OAI:The-irrationality-exponent-of-pi-is-2-September-24-2026,
  author = {{OpenAI}},
  title = {{The irrationality exponent of $\pi$ is $2$}},
  howpublished = {OpenAI Math Release preprint
                  \href{https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/paper.pdf}{OAI:The-irrationality-exponent-of-pi-is-2-September-24-2026}},
  year = {2026}
}
```

The held PDF has 23 pages with a text layer; its title page is dated
September 24, 2026 and its metadata records a creation date of
21 September 2026, three days earlier. The TeX source is `build/main.tex`
(264 lines), which inputs four section files under `build/sections/`:
`interpolation.tex` (584 lines), `determinant.tex` (432), `conclusion.tex`
(156) and `series.tex` (155), 1,591 lines in all, with the bibliography
`build/references.bib` (269 lines, 25 entries).

**Attestation.** The release README states that the collection holds
manuscripts "produced by an internal OpenAI model", that it "includes results at
different stages of verification", that "Not all have accompanying Lean
formalizations" and that "Some of the unformalized results could have issues".
Its account of the method says that "The vast majority of results were obtained
with the same procedure using an unreleased internal OpenAI model", with on
average three hours of "ChatGPT Pro thinking compute" per result; the exceptions
it names (a zero-free region for the Riemann zeta function and the Hodge
conjecture for CM abelian varieties) do not include this manuscript's subject.
The README also lists this manuscript's family among the families for which the
release gives "abridged summaries of the model's reasoning"
(`reasoning_traces/irrationality-exponent-of-pi.pdf` in the release); that file
is not held here and was not read. The manuscript's own README carries only the
title, the author line "OpenAI", the date and the citation block, and adds no
sentence about authorship or assistance. The title page names OpenAI as the sole
author, and the manuscript has no acknowledgment or funding note. These are the
source's own statements, recorded as attestations and not as this corpus's
review. No refereed publication, arXiv version or independent review of the
manuscript is recorded here, and nothing on this card is independently reviewed.

**Formalization.** The release's Lean page for its family (`lean/docs/017.md`)
says that the formalization proves the irrationality exponent of $\pi$ is
exactly two, in the form that for every $\nu>2$ all sufficiently large
positive denominators $q$ satisfy $|\pi-p/q|\ge q^{-\nu}$ for every integer
numerator $p$, and that it also states the supremum characterization through
infinitely many rational approximations; it adds that "The paper's
convergence consequence for the Flint–Hills series is outside this selected
statement", so Corollaries 1.2 and 5.2 are outside it. The comparator
statement `lean/ComparatorChallenges/PiExponent.lean` (theorem
`OAI.PiExponent.main`, its proof left as `sorry` as in a challenge file)
reads, in words: for every real $\nu>2$ there is an integer $Q\ge2$ with
$q^{-\nu}\le|\pi-p/q|$ for all integers $p$ and all integers $q\ge Q$; and
the supremum of the set of $\nu>0$ for which infinitely many rationals $r$
with reduced denominator at least $2$ satisfy
$0<|\pi-r|<\operatorname{den}(r)^{-\nu}$ equals $2$. Its configuration
`PiExponent.json` names the solution module `OAI.NumberTheory.PiExponent.Main`
and permits only the axioms `propext`, `Quot.sound` and `Classical.choice`;
the release tree holds that module as
`lean/OAI/NumberTheory/PiExponent/Main.lean`, whose contents were not read.
At revision fd4aeeb2e the release's catalog `lean/formalization.yaml` lists
no entry for this comparator under `status.main_results` and does not name
this manuscript among its sources; its own `review` field reads
`status: unchecked`. All of this is read statically from the release's
files; nothing was built, replayed or audited for fidelity in this
repository. No Lean file here is a proof of any Erdős problem.

**Companions.** The release files this manuscript as the only member of its
family, and at revision fd4aeeb2e it holds no earlier dated version of it, so
there is no companion to record.

Read status: claims checked for Theorem 1.1, Corollary 1.2 and Corollary 5.2,
together with the definition of the irrationality exponent and the
statements of Theorem 2.1 (separated-weight interpolation), Proposition 3.4
(determinant comparison), Lemma 4.1 (choice of constants) and Lemma 5.1
(dyadic spacing), read clause by clause in the release's TeX source: in
`main.tex`, the definition at lines 50--56, `thm:main` at lines 64--71 with the
remark at lines 73--78 and `thm:flinthills` at lines 90--92;
`geom:interpolation` at lines 24--57 of `sections/interpolation.tex`;
`det:comparison` at lines 353--370 of `sections/determinant.tex`;
`par:constants` at lines 9--21 of `sections/conclusion.tex`; and
`series:dyadic` at lines 11--21 and `series:generalized` at lines 97--104 of
`sections/series.tex`. The proofs were read for their structure only and no
step was checked; nothing here is independently reviewed.

## Contents

The numbering below is the PDF's (results are numbered within sections).

- Title page and Section 1, Introduction (pp. 1--4). Defines the
  irrationality exponent $\mu(x)$ of an irrational $x$ as the supremum of the
  $\nu>0$ for which $0<|x-p/q|<q^{-\nu}$ has infinitely many solutions in
  coprime $p,q$ with $q\ge2$, notes $\mu(x)\ge2$ by pigeonhole, and cites
  Waldschmidt's *Open Diophantine problems* (p. 265) for the conjecture
  $\mu(\pi)=2$. States
  [[irrationality/openai_2026_irrationality_exponent_pi_2/theorem_1_1|Theorem 1.1]]
  (p. 1), with the remarks that it covers unreduced fractions, that its
  threshold is ineffective, and that exponent $2$ is weaker than bounded
  partial quotients. Introduces the Flint–Hills question (popularized by
  Pickover, discussed by Alekseyev) and states
  [[irrationality/openai_2026_irrationality_exponent_pi_2/corollary_1_2|Corollary 1.2]]
  (p. 1), placing it between Alekseyev's necessary condition
  $\mu(\pi)\le5/2$ (his Corollary 4) and Meiburg's sufficient condition
  $\mu(\pi)<5/2$ (his Theorem 2.5), and previews Corollary 5.2. Section 1.1
  (p. 2) lists earlier upper bounds for $\mu(\pi)$ as context, not inputs:
  Mahler 1953 ($42$, eventually $30$), Mignotte 1974 ($21$, eventually
  $20$), Chudnovsky's Hermite–Padé work, Hata 1993 ($8.01604539\ldots$),
  Salikhov ($7.606308\ldots$), Zeilberger–Zudilin ($7.103205334137\ldots$)
  and a September 2026 preprint of Bai claiming $7.101862832357$. On the
  series it cites two separate 2026 preprints, Dan's on generalized series
  and López Zapata's continued-fraction criterion, as leaving convergence
  undecided, records the withdrawal in September 2026 of a convergence
  claim of Mantzakouras and López Zapata, and says Carella's 2022 claim of
  exponent two and bounded partial quotients is not used, with a footnote
  objecting to a sign in Carella's displayed proof of the stronger
  assertion. The
  outline in Section 1.2 (pp. 2--4) relates the proof to Laurent's
  interpolation determinants, Roth's separated denominators, Philippon's
  zero estimates, Farhi's Roth lemma and Demailly's Seshadri-constant
  viewpoint. The closing conventions list the algebraic-geometry inputs
  (Bézout with isolated local multiplicities, ordinary blowups, nef plus
  ample, Proj recovery, Serre vanishing, smooth projective models of curves)
  and state that no earlier irrationality bound for $\pi$ is assumed.
- Section 2, Interpolation with separated weights (pp. 4--11). For positive
  rational weights $W=(w_0,\dots,w_m)$ on $Y,X_1,\dots,X_m$ and
  $V=(v_0,\dots,v_m)$ on $t,u_1,\dots,u_m$, defines the polynomials of
  $W$-degree at most $H$ and the coefficient packets of $V$-weight below
  $H$. Theorem 2.1 (p. 4), stated for arbitrary complex centers: under
  $K\theta^m<1$ and $Kw_0\theta^m/v_0<1$, weights $w_1,\dots,w_m$ chosen in
  turn above thresholds that do not depend on the centers make the jet map
  along the logarithmic curves $Y=1+t$, $X_i=c_{ji}+u_i+\log(1+t)$
  surjective at any $K$ centers with coordinatewise distinct entries, for
  all large, suitably divisible $H$. Lemma 2.2 (p. 5) compares the weights of
  coordinate and vector-field normal bases on a component where many
  derivatives vanish, through a simplex count and a weighted Bézout bound
  (cited to Mondal's notes, Corollary VIII.3). Proposition 2.3 (p. 7), the
  curve inequality, bounds the total weighted contact of an irreducible
  curve with the logarithmic curves at the centers by its weighted degree
  divided by $1+\sigma$. Section 2.3 (pp. 9--11) passes from curves to jets
  by a blowup of a weighted projective compactification, the nef-plus-ample
  criterion (Lazarsfeld, Corollary 1.4.10) and Serre vanishing, with the
  Stacks Project cited for blowups, Rees algebras and vanishing.
- Section 3, The arithmetic and analytic determinant estimates (pp. 12--17).
  Assumes $m$ approximations $|\pi-p_i/q_i|\le q_i^{-\nu}$, sets
  $w_i=\lceil\log q_i\rceil$ and centers $2\mathrm ijp_i/q_i$ in
  $\mathbb Q(\mathrm i)$, truncates the logarithms, and takes a nonzero square
  minor $\Delta_H$ of the interpolation matrix using every row, with a
  simplex count for the number $M$ of rows. Lemma 3.1 (p. 13), the
  arithmetic lower bound for $\log|\Delta_H|/(MH)$, proves the needed bound
  $\log\operatorname{lcm}(1,\dots,n)\le4n\log2$ in the text. Lemma 3.2 (p.
  14), exact row translation to Taylor tests of entire functions at the
  periods $2\pi\mathrm ij$. Lemma 3.3 (p. 15), the collision estimate, after
  Laurent's Taylor-expansion mechanism (his 2000 paper, Theorem 1).
  Proposition 3.4 (p. 16), the determinant comparison giving three
  sufficient numerical conditions for a contradiction.
- Section 4, Choice of parameters and proof of Theorem 1.1 (pp. 17--19).
  Lemma 4.1 (p. 17) supplies the rational constants; the proof (pp. 18--19)
  fixes the dimension, then the approximations, then lets the degree grow,
  and closes with the irrationality of $\pi$ and the lower bound
  $\mu(\pi)\ge2$.
- Section 5, Flint–Hills series and its generalization (pp. 19--21). The
  dyadic spacing estimate Lemma 5.1 (p. 19), a summability bound for any
  irrational $\alpha>0$ with $\|q\alpha\|\ge cq^{1-\nu}$ for all $q\ge1$,
  where $1<\nu<5/2$; the proof of Corollary 1.2
  (pp. 19--20); and
  [[irrationality/openai_2026_irrationality_exponent_pi_2/corollary_5_2|Corollary 5.2]]
  (p. 20), the criterion for $\sum_n n^{-a}|\sin n|^{-b}$, with its proof
  (pp. 20--21).
- References (pp. 21--23), 25 entries, including the 2026 preprints of Bai,
  Dan and López Zapata named above.

The manuscript flags nothing as numerical, computer-assisted or
conditional; every constant in the proof is chosen in the text, and the
threshold $Q(\nu)$ of Theorem 1.1 is ineffective. The release folder holds
only the PDF, the TeX build directory and the README; there is no
`verification/` folder.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using it. The pages of the irrationality area and those tagged Diophantine
approximation were read for a possible use. The nearest is Problem 495,
which asks whether $\liminf_{n\to\infty}n\|n\alpha\|\|n\beta\|=0$ for all
real $\alpha,\beta$ (Littlewood's conjecture). That equality would hold for
every pair containing $\pi$ if $\pi$ had unbounded partial quotients, but
exponent $2$ is consistent with bounded and with unbounded partial
quotients, and the manuscript's remark after Theorem 1.1 distinguishes
exponent $2$ from bounded partial quotients; the result decides neither
case, so it supplies nothing there. The other pages in those areas ask
about almost every real number, about every irrational number, or about
series and integer sequences unrelated to $\pi$, and a statement about one
constant does not enter them.
