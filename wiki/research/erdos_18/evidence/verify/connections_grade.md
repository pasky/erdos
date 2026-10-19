---
name: research/erdos_18/evidence/verify/connections_grade
title: "Distinct grade of the Problem 18 connections reviews"
desc: |
  Distinct grader's check of the nine focused reviews of the Problem 18
  connections page and its two leads as of 2026-09-28T13:50:48Z: all nine
  reports pass as focused review records, seventeen corrections are accepted,
  the other findings are downgraded or rejected with reasons, one lead is
  reviewed and one needs an update, and no tier is assigned.
created: 2026-09-28T19:36:12Z
updated: 2026-09-28T19:36:12Z
---

***

## Subject

The repository as it stood at 2026-09-28T13:50:48Z, the default branch's state
at the time of grading. The pages graded, each read in full as of that time:

- `wiki/research/erdos_18/connections.md`, the connections page: its
  preamble and Conventions, the nine sections from `## Shared lemmas` to
  `## Other divisor problems examined`, and its closing sections "Leads
  created" and "Sources read for this page";
- `wiki/research/leads/factorial_unit_fraction_transfer/_index.md`, the
  factorial lead;
- `wiki/research/leads/lcm_divisor_gap_greedy_route/_index.md`, the lcm
  lead.

The reports graded are the nine focused reviews filed beside this record in
`wiki/research/erdos_18/evidence/verify/`, one per section of the
connections page, each read in full:

- `connections_shared_lemmas_review.md`;
- `connections_problem_304_the_number_of_unit_fractions_for_a_b_review.md`,
  with the factorial lead;
- `connections_problem_293_the_least_denominator_missing_from_k_review.md`,
  with the factorial lead;
- `connections_problem_18_question_a_along_the_least_common_mul_review.md`,
  with the lcm lead;
- `connections_problem_18_question_c_what_the_greedy_route_woul_review.md`;
- `connections_problem_1099_sums_of_powers_of_consecutive_divis_review.md`;
- `connections_problem_673_the_sum_of_consecutive_divisor_ratio_review.md`;
- `connections_problem_859_the_density_of_n_representing_a_fixe_review.md`;
- `connections_other_divisor_problems_examined_review.md`.

The reports are focused reviews of author-recorded mathematics; they carry
no tier and this grade assigns none.

**Role and independence.** The grader is a distinct grader in a fresh
context: neither the author of the connections page, the leads or the
reconstruction pages, nor the reviewer who wrote any of the nine reports,
and not a participant in either piece of work. The grader received only
the grading assignment, which named the subject date, the page, the leads, the
reports and the sections of `docs/verification.md` to read. No working material
of the author or of the reviewers reached the grader, and nothing was read from
the web. The grader is not blind: the problem pages' Status and Current
assessment text, the library result pages and the earlier grade of the
reconstruction reviews in this folder were read where a finding needed them, and
are disclosed below.

**Read set and depth.**

- `docs/verification.md`: "Independence and the assignment", "Exact
  subjects and durable evidence", "Report contract", "Grading and claim
  standing", "Whole-claim report" and both "Audit checklist" sections, in
  full; `docs/approach_vetting.md` "Compare substance, not vocabulary", for
  the rule on novelty claims.
- The connections page and the two leads in full as of that time; the retained
  script `gap_profile.py` and the evidence index of the lcm lead in full.
- Reconstruction pages as of that time: the Remark 6 page in full (its Statement
  covers $h(n!)$ only and its proof gives $\log\tau(n!)\ll n/\log n$); the Lemma
  3.1 page's Definitions, Statement and Proof; the Theorem 1 page's symmetry
  facts (i) and (ii).
- Problem pages as of that time: Problem 304 (Statement, Formulation, Status,
  Origin, the Known results paragraphs on the van Doorn claim and on the
  deduced, unreviewed transfer, and the bullets on Vose and on Problem
  293); Problem 293 (Statement, Formulation, Status and the "Finite values"
  paragraph); Problem 1099 in full.
- Library: the Theorem 1.2 result page of
  [[../library/divisors/doorn_2026_practical_numbers_egyptian_fractions/_index|van Doorn (2026)]]
  in full; physical p. 171 of the held Erdős (1981) paper in the layout
  text extraction, for the candidates sentence.
- The earlier grade in this folder (`grade.md`) and the folder's review
  index, read for the record format and to update the index.
- Not read: the van Doorn note, the Hughes preprint, the van Doorn–Tang
  paper, the Weingartner paper and the Erdős (1982) survey. The reviewers'
  source-fidelity checks, made on page images and agreeing wherever two
  reports cover the same source, are accepted as filed; no finding turned
  on a source reading that this grade had to re-adjudicate.

**Independent computations.** Two findings turn on numbers, and both were
recomputed here from scratch by scripts written for this grade in a
temporary directory and not retained (the assignment permits writing only
this record and one index sentence); the descriptions and numbers below
let a reader rerun them.

- The divisor gaps of $L_x=\mathrm{lcm}(1,\dots,x)$ for
  $x=20,30,40,50,60,64$: every divisor enumerated as an exact integer from
  the prime-power factorization and sorted, the count checked against
  $\tau(L_x)$, and over the consecutive pairs $d<b$ with
  $x\le\sqrt{db}\le\sqrt{L_x}$ the value
  $\kappa(d,b)=(\log x)\log(1/\log(b/d))/\log\sqrt{db}$, with
  $\log(b/d)=\log(1+(b-d)/d)$ from the exact difference. Results:
  $\kappa_{\min}=1.116$, $1.257$, $1.311$, $1.298$, $1.348$, $1.358$, the
  page's values; the binding pairs at positions
  $\log\sqrt{db}/\log\sqrt{L_x}=1.000$, $0.956$, $0.989$, $0.962$, $0.995$,
  $0.996$, that is, $\sqrt{L_x}/\sqrt{db}=1.00$, $1.88$, $1.23$, $2.58$,
  $1.15$, $1.12$ (at $x=20$ the pair $15048<15470$ around
  $\sqrt{L_{20}}$); the largest $\log(b/d)$ in the top tenth of
  $[0,\log\sqrt{L_x}]$, the retained script's bands, is $2.77\cdot10^{-2}$
  at $x=20$ and $4.45\cdot10^{-5}$ at $x=64$, while the fifth and sixth
  tenths at $x=64$ have maxima $8.8\cdot10^{-4}$ and $3.1\cdot10^{-4}$
  (with tenths of $[\log x,\log\sqrt{L_x}]$, the lead's wording,
  $3.3\cdot10^{-4}$ and $1.9\cdot10^{-4}$, the reviewer's values).
- The series
  $C(\alpha)=4\sum_{j\ge2^{16}}(4\varepsilon_j)^{\alpha-1}(\tfrac12\log j+\log2)$
  with $\varepsilon_j=j^{-(\log_2j/2-\log_2\log_2j)}$: summed in floating
  point over $2^{16}\le j<3\cdot10^6$, the tail bounded by the integral of
  the decreasing summand. Results: $C(1.1)\approx7.9\cdot10^{4}$,
  $C(5/4)\approx20.3$, $C(3/2)\approx1.8\cdot10^{-4}$,
  $C(2)\approx3.7\cdot10^{-14}$, against $2\zeta(5/4)\approx9.19$; the
  per-term bound $(4\varepsilon_j)^{\alpha-1}\le2^{-62(\alpha-1)}$ holds
  with equality at $j=2^{16}$.

**Standard applied.** A finding is accepted as a correction when a
mathematical statement of the page (a display, an inequality, a
consequence sentence, a description of a computation) is false or
unsupported as written, whether or not a weaker true statement was
intended; when a result is cited outside its stated hypotheses; when an
assessment sentence misdescribes what the page's own mathematics shows; or
when the corpus's own rule requires the change (an undescribed search
behind a novelty claim). Wording with a true reading, optional labels and
locators, thresholds that sit under an explicit "for large" clause,
characterizations of sources or status text that the read set cannot
decide, and observations for which no exact replacement is warranted are
downgraded to notes. The reviewers graded severity unevenly (the same
missing bounded-seed clause is "required" in one report and "suggested" in
another); this grade applies the one standard above to all nine.

**Exposure ruling.** Every report discloses incidental exposures of the
same kinds: the Status paragraph or frontmatter status line of a problem
page printed with its Statement; a library card's Read status, Bears on or
Overview paragraphs printed with its provenance paragraph; the Standing
paragraphs of the reconstruction pages; neighboring sections of the
connections page itself; file names of sibling reviews and of the earlier
grade in a directory listing. By the content test, nothing in any report
could only have come from these exposures and no attack direction followed
them: every finding cites the page's own text, a held source, or a
derivation made in the report. All disclosed exposures are ruled
immaterial.

## Reports graded

Each report has a subject block that resolves (the subject date above, the page,
the section by heading and line range, and the lead where one was
assigned), states its role, fresh context, allowed material actually read
and exposures, restates every statement of its section with quantifiers,
gives an explicit verdict on each of the ten audit-checklist items,
re-derives up to three weakest steps, records a strongest attack that
could have succeeded, lists its premises with interfaces and reading depth,
and closes with a verdict per statement that assigns no tier.

- `connections_shared_lemmas_review.md`: **pass**. Lemma D's asymptotic
  floor is re-derived to the exact point where the proof loses the seed
  term, and the attack carries the witness $n_0=2^k$, $A_0=3$, $L_0=1$
  that refutes the display as stated; Lemma B's upper-range partition,
  Lemma C′'s second case and the van Doorn accounting of the closing
  paragraph are re-derived; exhaustive exact checks of Lemmas A, C and C′
  are reported as attacks, not warrants. F1 and F2 are accepted (C1).
- `connections_problem_304_..._review.md`: **pass**. The three weakest
  steps (the Lemma 3.1 interface inside Lemma C′, the passage from
  $(n-1)!<b$ to $n<\log b$, the two obstructions) are re-derived, and the
  attack on the extension-chain obstruction carries its own witness
  $n_0=m!$, $A_0=2$, $L_0=1$; the lead's (293.1) is checked against the
  lead's sketch, the full proof being the Problem 293 report's charge. F1
  is accepted (C2); F2 (C3) and F6 (C4) are adopted under the standard
  above.
- `connections_problem_293_..._review.md`: **pass**. Lemma C′ is
  re-derived with an exact finite check of the construction for
  $3\le b\le5040$, the arithmetic of (293.1) and its corollary is
  re-derived with the exact threshold $k\ge25$, and the two caps are
  attacked at the non-factorial case and at the unbounded seed. F1 is
  accepted (C5) and F2 (C6).
- `connections_problem_18_question_a_..._review.md`: **pass**, with one
  limitation recorded. The proof of (18a.1) is re-derived and its slip
  found; the upper-range recurrence is re-derived to show the constant
  $2/c$; the window argument behind $c\le2\log2$ is re-derived; the
  computation was reproduced by an independent enumeration that is not
  retained with the report, which a focused review may do but which this
  grade therefore repeated (Subject, above) with the same results. F1 to
  F6 are accepted (C7 to C12).
- `connections_problem_18_question_c_..._review.md`: **pass**. The
  mean-gap floor is re-derived with the mirror argument at the top window,
  the necessity translation is re-derived, and the strongest attack
  exhibits an admissible capped profile with integral $O((\log n)^2)$ that
  the floor does not exclude, together with the counting bound that every
  admissible profile obeys. F1 and F2 are accepted (C13).
- `connections_problem_1099_..._review.md`: **pass**. The zone
  decomposition, the window bound and the corollary are re-derived clause
  by clause; the attack on the bound below the threshold $T$ is exact and
  correctly stopped by the hypothesis $n\ge T$; the divergence of
  $C(\alpha)$ as $\alpha\to1^+$ is exact and the witness $C(5/4)$ is
  confirmed here. F1 is accepted (C14).
- `connections_problem_673_..._review.md`: **pass**. The site comment's
  lower bound is re-derived with its true range, the even-$n$ bound and
  the factorial bound are re-derived, and the attack on the density-zero
  obstruction goes through the ratio-two integers and the order of the
  average. F1 is accepted (C15).
- `connections_problem_859_..._review.md`: **pass**. The transfer lemma,
  the existence of the density and the polynomial floor are re-derived,
  with the unconditional factorial and power-of-two seeds supplied; the
  attack seeks a transfer at logarithmic scale and explains why none is
  available. F1 is accepted (C16).
- `connections_other_divisor_problems_examined_review.md`: **pass**. The
  width comparison, the strictness gap in the Problem 144 bullet and the
  entailment between practicality and pseudoperfection are re-derived,
  each attack carrying its witness. F1 is accepted (C17).

## Corrections

Accepted corrections, numbered across the folder in page order. Each names
the page, the location and the exact replacement. "Section" means the
named H2 section of `wiki/research/erdos_18/connections.md`; "factorial
lead" and "lcm lead" are the two lead pages named in the Subject.

**C1.** Section "Shared lemmas", Lemma D, two places.

(a) Statement. Replace the display and the two sentences after it,

> $$
> \sum_{j<J}L_j\ \ge\ \sum_{j<J}\frac{\log A_j}{\log\bigl(\tau(n_j)+1\bigr)}
> \ \ge\ \Bigl(\frac1{2\log2}-o(1)\Bigr)(\log\log n_J)^2
> \qquad(n_J\to\infty),
> $$
>
> where the $o(1)$ tends to $0$ as $n_J\to\infty$ uniformly over all such
> chains. Hence the bound $h(n_0)+\sum_jL_j$ that such a chain certifies
> for $h(n_J)$ is never below $(1/(2\log2)-o(1))(\log\log n_J)^2$.

with

> $$
> \sum_{j<J}L_j\ \ge\ \sum_{j<J}\frac{\log A_j}{\log\bigl(\tau(n_j)+1\bigr)}
> \ \ge\ \frac{(\log\log n_J)^2-(\log\log n_0)^2}{2(\log2+\eta)}-C(\eta)
> $$
>
> for every $\eta>0$, with $C(\eta)$ depending on $\eta$ alone. Hence, for
> chains from a bounded seed, $n_0\le C$ with $C$ fixed, the bound
> $h(n_0)+\sum_jL_j$ that such a chain certifies for $h(n_J)$ is at least
> $(1/(2\log2)-o(1))(\log\log n_J)^2$, where the $o(1)$ tends to $0$ as
> $n_J\to\infty$ uniformly over the chains with $n_0\le C$. Without a
> bound on the seed the sum $\sum_jL_j$ has no floor in $n_J$ alone: the
> one-step chain $n_0=2^k$, $A_0=3$, $L_0=1$ satisfies the hypothesis of
> Lemma 3.1 and has $\sum_jL_j=1$.

(b) Proof. Replace

> With $\ell_j=\log n_j$ and $f(\ell)=\log\ell/\ell$, which decreases for
> $\ell>e$, let $j(\eta)$ be the least index with $n_{j(\eta)}\ge n(\eta)$.

with

> With $\ell_j=\log n_j$ and $f(\ell)=\log\ell/\ell$, which decreases for
> $\ell>e$, let $n(\eta)$ be a threshold beyond which $\eta'(n)\le\eta$ and
> $\log n>e$, and let $j(\eta)$ be the least index with
> $n_{j(\eta)}\ge n(\eta)$; if there is none, then $n_J<n(\eta)$ and the
> bound holds with any $C(\eta)\ge(\log\log n(\eta))^2/(2\log2)$.

and replace

> Hence $\sum_jL_j\ge(\log\ell_J)^2/(2(\log2+\eta))-O_\eta(1)$; let
> $\eta\to0$. $\square$

with

> If $j(\eta)=0$ the subtracted term is $(\log\ell_0)^2=(\log\log n_0)^2$
> and nothing compensates it. In either case
> $\sum_jL_j\ge\bigl((\log\ell_J)^2-(\log\ell_0)^2\bigr)/(2(\log2+\eta))-O_\eta(1)$,
> which is the second inequality. For $n_0\le C$ the subtracted term is
> $O_C(1)$, and letting $\eta\to0$ gives the floor
> $(1/(2\log2)-o(1))(\log\log n_J)^2$. $\square$

Verified: the witness meets Lemma 3.1's hypothesis ($2^k$ is practical by
binary expansion; the residues $0,1,2$ modulo $3$ are the empty sum, the
divisor $1$ and the divisor $2$, one summand each, total at most $2^k$,
none divisible by $3$), and its middle term is $\log3/\log(k+2)<1$ for
$k\ge2$ while the stated right side tends to infinity with $k$, so the
display as written is refuted; the Problem 304 report's witness $n_0=m!$,
$A_0=2$, $L_0=1$ refutes it likewise. The proof's case $j(\eta)\ge1$ gives
$(\log\ell_J)^2/(2(\log2+\eta))-O_\eta(1)$ as the page says, which is at
least the subtracted form; the case $j(\eta)=0$ gives exactly the
subtracted form; and the case with no $j(\eta)$ is trivial. The page's
"Hence" sentence at $J=0$ and unrestricted seed would assert
$h(n_0)\ge(1/(2\log2)-o(1))(\log\log n_0)^2$ for every practical $n_0$,
which nothing on the page proves and which the page itself disclaims two
paragraphs later; for bounded seeds it follows from the repaired display
and $h(n_0)\ge0$. The closing paragraph's "from a fixed seed" is exactly
the restored hypothesis and needs no change. This adopts the shared-lemmas
report's F1 and F2, its F3 for the definition of $n(\eta)$, and the
subtracted form proposed in the Problem 304 report's F1 and the Problem
293 report's F3.

**C2.** Two places.

(a) Section "Problem 304", paragraph "What it does not give, and why".
Replace

> Along the extension chains of the van Doorn note it is impossible too:
> Lemma D shows that every certificate built from Lemma 3.1 extensions is
> at least $(1/(2\log2)-o(1))(\log\log N)^2$.

with

> Along the extension chains of the van Doorn note it is impossible too:
> Lemma D shows that every certificate built from Lemma 3.1 extensions
> from a seed bounded independently of the scale, as the note's chain is,
> is at least $(1/(2\log2)-o(1))(\log\log N)^2$.

(b) Factorial lead, section "What the route cannot give". Replace

> and the counting floor (Lemma D of the connections page) shows that
> certificates built from Lemma 3.1 extensions are never below
> $(1/(2\log2)-o(1))(\log\log N)^2$.

with

> and the counting floor (Lemma D of the connections page) shows that
> certificates built from Lemma 3.1 extensions from a seed bounded
> independently of the scale are never below
> $(1/(2\log2)-o(1))(\log\log N)^2$.

Verified: both sentences consume Lemma D at the interface C1 removes; the
note's chain starts from $n_0=2^E(2Q(k_0))^{k_0}$, bounded independently
of $x$ and $p_*$ on the Proposition 4.1 page, so the section's conclusion
about the note's mechanism stands under the repaired lemma. Adopts the
Problem 304 report's F1.

**C3.** Section "Problem 304", the sentence after the proof of (304.1).
Replace

> This is below Vose's $\sqrt{\log b}$ for every $\varepsilon<\tfrac12$ and
> is the first consequence of the accepted part (b) outside Problem 18.

with

> This is below Vose's $\sqrt{\log b}$ for every $\varepsilon<\tfrac12$ and
> is the first consequence of the accepted part (b) drawn in this corpus;
> no search for an earlier one was made.

Verified: the page's "Sources read" lists no search bearing on the
priority claim, and `docs/approach_vetting.md` "Compare substance, not
vocabulary" requires an incomplete search behind a novelty claim to be
described as such; the note itself (p. 1, as both the Problem 304 and the
Problem 293 reports read it) says that bounds on $h$ transfer to $N(b)$,
so the consequence is immediate to anyone holding both results. Adopts
the Problem 304 report's F2.

**C4.** Two places.

(a) Section "Problem 304", paragraph "Next investigation". Replace

> A positive answer proves the conjecture through Lemma C; Lemma D and
> Remark 6 show that neither mechanism of this folder can supply it, so it
> needs a new certificate of practicality.

with

> A positive answer proves the conjecture through Lemma C. Remark 6 shows
> that factorials cannot supply it and Lemma D that Lemma 3.1 chains from
> a bounded seed cannot; the greedy count of Lemma B on another ratio-two
> family, such as $L_x$ under Lemma A, is excluded by neither, since its
> counting floor $h(N)\ge\log N/\log(\tau(N)+1)$ is only of order
> $\log\log N$ for $N=L_x$, but no gap input of the required strength is
> known.

(b) Factorial lead, section "What the route cannot give". Replace

> Both mechanisms stop at exponent $2$; the conjecture of Problem 304
> needs a practical $N\in[b,\exp((\log b)^{O(1)})]$ with
> $h(N)\ll\log\log N$, which needs a new certificate of practicality.

with

> Both mechanisms stop at exponent $2$; the conjecture of Problem 304
> needs a practical $N\in[b,\exp((\log b)^{O(1)})]$ with
> $h(N)\ll\log\log N$, which neither mechanism can supply; the greedy
> count of Lemma B on another ratio-two family is not excluded by
> counting, but no gap input of the required strength is known.

Verified: Remark 6 concerns $n!$ through $\tau(n!)$ and Lemma D concerns
Lemma 3.1 chains, while for $L_x$ one has $\log\tau(L_x)\asymp x/\log x$
and $\log L_x\asymp x$, so the subset-count floor
$\log L_x/\log(\tau(L_x)+1)$ is of order $\log x=\log\log L_x+o(1)$, and
the pigeonhole at the top window forces on Lemma B only
$\int d\ell/\sigma\ge(\tfrac12\log L_x-O(\log x)-\log(2T))/\log\tau(L_x)$,
again of order $\log x$; neither obstruction reaches exponent $1$ there.
Adopts the Problem 304 report's F6, with the replacement supplied here.

**C5.** Section "Problem 293", paragraph "What it does not give, and why".
Replace

> The factorial route is capped at $\exp\exp(C\sqrt k)$: Remark 6 gives
> $2h(N)+1\ge2c(\log n)^2\approx2c(\log\log b)^2$ for the $N$ of Lemma C′,
> so it can only place $b$ in $D_k$ when $\log\log b\le\sqrt{k/(2c)}$.

with

> The factorial route is capped at $\exp\exp(C\sqrt k)$: the counting
> argument of Remark 6, applied to $N$ (for $N=p^{j}(n-1)!$ one has
> $\tau(N)\le(j+1)\tau((n-1)!)$ and $\log N\ge\log(n-1)!$), gives
> $2h(N)+1\ge2c(\log n)^2=(2c+o(1))(\log\log b)^2$ for the $N$ of Lemma
> C′, so it can only place $b$ in $D_k$ when
> $\log\log b\le(1+o(1))\sqrt{k/(2c)}$.

Verified: the Remark 6 page states $h(n!)\gg(\log n)^2$ for factorials
only, and the second case of Lemma C′ has $N=p^j(n-1)!$; with
$v=v_p((n-1)!)\ge1$,
$\tau(N)=\tau((n-1)!)\,(v+j+1)/(v+1)\le(j+1)\tau((n-1)!)$, so
$\log(\tau(N)+1)\ll n/\log n$ by the divisor count on the Remark 6 page,
while $\log N\ge\log(n-1)!\gg n\log n$, and the page's subset counting
gives $h(N)\gg(\log n)^2$ in both of its cases; and
$(\log n)^2=(1+o(1))(\log\log b)^2$ from $(n-1)!<b\le n!$. Adopts the
Problem 293 report's F1.

**C6.** Section "Problem 293", same paragraph. Replace

> The extension chains are capped at the same shape by Lemma D, which is
> why the claimed Theorem 1.3 has the form it has.

with

> Certificates built from Lemma 3.1 extensions of a bounded seed are
> capped at the same shape by Lemma D, which is why the claimed Theorem
> 1.3 has the form it has.

Verified as for C2. Adopts the Problem 293 report's F2.

**C7.** Section "Problem 18, question (a)", proof of (18a.1). Replace
"$\delta\le2x^{-4}\le1/8$" with "$\delta\le2e^{-4}<1/8$".

Verified: $\delta$ is nonincreasing with $\delta(T)=2T^{-c/\log x}$ and
$T=x^{4/c}$, so $\delta(T)=2x^{-4/\log x}=2e^{-4}\approx0.037$, which
exceeds $2x^{-4}$ for every $x\ge3$; the needed conclusion $\delta\le1/8$
holds. Adopts the question (a) report's F4.

**C8.** Two places.

(a) Section "Problem 18, question (a)", paragraph "The comment's form of
the hypothesis, and where it fails". Replace

> the comment's recurrence $R'\le R^{1-c/\log x}$ is exactly the
> lower-range step of Lemma B and gives the constant $1/c$ there, so the
> constant $3/c$ above is a bookkeeping loss, not a mathematical one.

with

> the comment's recurrence $R'\le R^{1-c/\log x}$ is exactly the
> lower-range step of Lemma B and gives the constant $1/c$ there; the
> mirror recurrence on $U=L_x/R$ gives another $1/c$ in the upper range,
> so the direct count gives $2/c$, and only the factor $3/2$ between it
> and the $3/c$ above is a bookkeeping loss.

(b) Lcm lead, section "Consequential gap". Replace

> with a constant $3/c$ (or $1/c$ with the comment's recurrence in the
> lower range and the same mirror argument)

with

> with a constant $3/c$ (or $2/c$ when the upper range is counted by the
> recurrence on $U=L_x/R$ instead of Lemma B's dyadic partition)

Verified: in the lower range
$R'\le R\,\delta(R/2)=2^{1+\kappa}R^{1-\kappa}$ with $\kappa=c/\log x$, so
$\log R$ falls by the factor $1-\kappa$ per step, from
$\tfrac12\log L_x\sim x/2$ to $\log(2T)$, in $(1/c+o(1))(\log x)^2$ steps;
in the upper range the mirror pair gives $R'\le R\,\delta(U/2)$, so
$\log U$ grows by the factor $1+\kappa$ per step over the same range,
again $(1/c+o(1))(\log x)^2$ steps. The comment's form, stated up to
$Y=L_x$, would give $1/c$ over the whole range, but it is false in the top
range, as the page itself shows; under the lower-half hypothesis the upper
range costs its own $1/c$. Adopts the question (a) report's F1.

**C9.** Two places.

(a) Section "Problem 18, question (a)", paragraph "Scale of the
hypothesis". Replace

> so necessarily $c\le2\log2+o(1)$, and $(\mathrm H_c)$ with $c$ near
> $2\log2$ says that the largest gap matches the mean gap up to a
> polynomial factor at every scale above $x$: a statement at the mean-gap
> scale, of the kind no factorial gap estimate reaches (Berend and
> Harmse's Remark 2 says their bound is the best their method gives up to
> a bounded power of $\log_2n$).

with

> so necessarily $c\le2\log2+o(1)$. With $c$ near $2\log2$, $(\mathrm H_c)$
> is at the mean-gap scale near $\sqrt{L_x}$, where the exponent
> $-(c/2)x/\log x$ it allows and the exponent $-(\log2)x/\log x$ of the
> mean gap agree to first order; at scale $x^m$ it allows gaps $e^{-cm}$
> of constant size against a mean gap of order $x^{-m}$ up to powers of
> $\log x$, so below the top it asks much less than mean-gap matching.
> Near the top it is a statement of the kind no factorial gap estimate
> reaches (Berend and Harmse's Remark 2 says their bound is the best their
> method gives up to a bounded power of $\log_2n$).

(b) Lcm lead, section "Provisional premise", second bullet. Replace

> and with $c$ near $2\log2$ it says that the largest gap equals the mean
> gap up to a polynomial factor at every scale above $x$.

with

> and with $c$ near $2\log2$ it is at the mean-gap scale near
> $\sqrt{L_x}$, where the exponents of its allowance and of the mean gap
> agree to first order, while at scale $x^m$ it allows gaps $e^{-cm}$ of
> constant size against a mean gap of order $x^{-m}$ up to powers of
> $\log x$.

Verified: at $\sqrt{db}=x^m$ the hypothesis reads
$\log(b/d)\le x^{-mc/\log x}=e^{-cm}$, while the products of $m$ distinct
primes in $(x/2^{1/m},x]$ alone put $\gg_m x^m/(\log x)^m$ divisors of
$L_x$ in $(x^m/2,x^m]$, so the mean logarithmic gap there is
$\ll_m(\log x)^m/x^m$; at the top the allowance is
$\exp(-(c/2)\psi(x)/\log x)$ against the mean gap
$\exp(-(\log2)\pi(x)+O(\sqrt x\log\log x))$, whose exponents agree to first
order exactly when $c=2\log2$. Read with "polynomial in $x$" the page's
sentence is true at scales $x^{O(1)}$ and false at the top, where the
ratio is $\exp(\Theta(x/(\log x)^2))$; read with "polynomial in the scale"
it holds for every hypothesis, since every gap is at most $\log2$ and the
mean gap at scale $g$ is at least $1/g$. Adopts the question (a) report's
F5.

**C10.** Two places.

(a) Section "Problem 18, question (a)", paragraph "Exploratory
computation". Replace

> It does not decrease over this range and approaches $2\log2=1.386\ldots$
> from below; the binding pairs sit in the middle of the range, where the
> largest $\log(b/d)$ falls from $2.8\cdot10^{-2}$ at $x=20$ to
> $4.5\cdot10^{-5}$ at $x=64$.

with

> It shows no downward trend over this range (it dips once, from $1.311$
> at $x=40$ to $1.298$ at $x=50$) and approaches $2\log2=1.386\ldots$ from
> below; the binding pairs sit at the top of the range, within a factor of
> about $2.6$ of $\sqrt{L_x}$ (the middle of the full divisor range of
> $L_x$), where the largest $\log(b/d)$ in the top tenth falls from
> $2.8\cdot10^{-2}$ at $x=20$ to $4.5\cdot10^{-5}$ at $x=64$.

(b) Lcm lead, section "Exploratory computation", the two sentences after
the table. Replace

> The largest $\log(b/d)$ in the middle tenth falls from $2.8\cdot10^{-2}$
> at $x=20$ to $4.5\cdot10^{-5}$ at $x=64$, and the binding pairs sit in
> the middle of the range. $\kappa_{\min}(x)$ does not decrease over the
> sample and approaches $2\log2=1.386\ldots$ from below, the largest value
> the mean-gap bound allows; this was observed after the fact, not
> predicted.

with

> The largest $\log(b/d)$ in the top tenth falls from $2.8\cdot10^{-2}$ at
> $x=20$ to $4.5\cdot10^{-5}$ at $x=64$, and the binding pairs sit at the
> top of the range, within a factor of about $2.6$ of $\sqrt{L_x}$.
> $\kappa_{\min}(x)$ shows no downward trend over the sample (it dips
> once, from $1.311$ at $x=40$ to $1.298$ at $x=50$) and approaches
> $2\log2=1.386\ldots$ from below, the largest value the mean-gap bound
> allows; this was observed after the fact, not predicted.

Verified by the independent enumeration described in the Subject: the six
values of $\kappa_{\min}$ are reproduced, the table itself shows the dip
from $1.311$ to $1.298$, the binding pairs lie within a factor $2.58$ of
$\sqrt{L_x}$, and the two quoted maxima are those of the top tenth under
both the retained script's bands and the lead's wording, the middle
tenths at $x=64$ being an order of magnitude larger. Adopts the question
(a) report's F3.

**C11.** Three places.

(a) Section "Problem 18, question (a)", paragraph "Next investigation".
Replace

> a disproof (a sequence of $x$ with $\kappa_{\min}(x)\to0$) shows that
> the greedy route along $L_x$ gives only $(\log x)^2/\kappa_{\min}(x)$.

with

> a disproof (a sequence of $x$ with $\kappa_{\min}(x)\to0$) shows that no
> hypothesis of the form $(\mathrm H_c)$ with a fixed $c$ holds, so
> (18a.1) as stated gives nothing along that sequence; whether a
> scale-dependent profile, or one that tolerates a few exceptional pairs,
> still gives $(\log x)^2$ through Lemma B would remain open.

(b) Lcm lead, section "Consequential gap". Replace

> A disproof, a sequence of $x$ along which $\kappa_{\min}(x)\to0$, would
> show that the greedy route along $L_x$ cannot give $(\log x)^2$, leaving
> Lemma B's $x/(\log x)^{3/2-\eta}$ from Tenenbaum's input as the route's
> best.

with

> A disproof, a sequence of $x$ along which $\kappa_{\min}(x)\to0$, would
> show that no hypothesis of the form $(\mathrm H_c)$ with a fixed $c$
> holds, so (18a.1) as stated gives nothing along that sequence; whether a
> scale-dependent profile, or one that tolerates a few exceptional pairs,
> still gives $(\log x)^2$ through Lemma B would remain open, with Lemma
> B's $x/(\log x)^{3/2-\eta}$ from Tenenbaum's input the route's best
> bound without $(\mathrm H_c)$.

(c) Lcm lead, section "Exploratory computation", last sentences. Replace

> The computation distinguishes a quickly vanishing constant, which would
> show the route gives only $(\log x)^2/\kappa_{\min}(x)$, from a stable
> one; it cannot prove $(\mathrm H_c)$, and $x\le64$ is far from
> asymptotic.

with

> The computation can only begin to distinguish a quickly vanishing
> constant, which would show that no fixed $c$ satisfies $(\mathrm H_c)$,
> from a stable one; it cannot prove $(\mathrm H_c)$, and $x\le64$ is far
> from asymptotic.

Verified: a single pair with small $\kappa$ costs the greedy expansion at
most one nonterminal step in the lower range, since the remainder after
that step lies below the pair's lower divisor and remainders decrease, and
at most one in the upper range through its mirror (after the step
$N/R'>N/d$, so the mirror pair never brackets $U$ again); the charging
argument of Lemma B counts such steps separately at cost $1$ each and
keeps the disjointness of the remaining intervals. So $\kappa_{\min}(x)\to0$
bounds nothing from below; it shows only that no fixed $c$ satisfies
$(\mathrm H_c)$. Adopts the question (a) report's F2 and the third part of
its F7.

**C12.** Lcm lead, section "Next step", last sentence. Replace

> A result for the middle alone would already cover the range that
> dominates the integral of Lemma B.

with

> Under $(\mathrm H_c)$ every factor-of-$e$ range of $\ell=\log(2g)$
> contributes $\log x/c$ to the integral of Lemma B, so a result near
> $\sqrt{L_x}$ alone covers only $O(\log x)$ of the $(\log x)^2$ count; it
> is nevertheless the range where $(\mathrm H_c)$ is tightest and where
> the computation finds the binding pairs.

Verified: with $\sigma(\ell)=c\ell/\log x$ the integral over $[\ell,e\ell]$
is $\log x/c$ for every $\ell$, and the range from $L_x^{1/4}$ to
$\sqrt{L_x}$ contributes $(\log2)\log x/c$ of the total $(\log x)^2/c$.
Adopts the question (a) report's F6.

**C13.** Section "Problem 18, question (c)", paragraph "What transports",
the sentence beginning "Hence $C=2$ is impossible". Replace

> Hence $C=2$ is impossible for the greedy route, consistent with Remark
> 6, and $C=3$ asks the largest gap to match this mean gap up to a
> constant in the exponent at every scale: the factorial analog of
> $(\mathrm H_c)$, with the same mean-gap character.

with

> Hence the natural profile with $C=2$ is inadmissible, and no admissible
> profile does better than exponent $2$: the pair above forces
> $\sigma\le\log\tau(n!)$ on all but the last $\tfrac12\log n+O(1)$ of the
> range, so the integral is at least
> $(\tfrac12\log n!-O(\log n)-\log(2T))/\log\tau(n!)\gg(\log n)^2$ whenever
> $\log T\le(\tfrac12-\eta)\log n!$, and otherwise the term $2\log_2(2T)$
> is $\gg n\log n$; this is consistent with Remark 6. Whether a profile
> capped at $\sigma=cn/\log n$ for a small constant $c$, whose integral is
> $O((\log n)^2)$, satisfies the hypothesis of Lemma B is a maximal-gap
> question that this counting leaves open. The natural profile with $C=3$
> asks the largest gap to match this mean gap up to a constant in the
> exponent throughout the windows of index $j\asymp n$, while asking much
> less below them: the factorial analog of $(\mathrm H_c)$, with the same
> mean-gap character near the top.

Verified: the page's argument shows only that the natural profile
$\sigma(\ell)=\ell/\log n$ violates Lemma B's hypothesis at the window of
index $n$. The profile $\sigma(\ell)=\min(\ell/\log n,\,cn/\log n)$ with
$\log(2T)=\log8\cdot\log n$ is admissible (nondecreasing, at least
$\log8$), has integral at most $(1+1/(2c))(\log n)^2$, and demands at the
top windows only $\log(b/d)\le\tfrac12\exp(-cn/\log n)$, which the floor
$\tfrac12\log n/\tau(n!)=\exp(-\Theta(n/\log n))$ does not contradict for
small $c$; so "impossible for the greedy route" is unproved as written.
The counting bound for every admissible profile is as stated: the pair
found at the top window forces $\delta(g)\ge\log n/\tau(n!)$ at some
$g\ge\sqrt{(n-1)!/2}$, hence $\sigma\le\log\tau(n!)$ up to $\log(2g)$. For
$C=3$ the demand $\exp(-\ell/(\log n)^2)$ at $\ell\asymp n\log n$ is
$\exp(-\Theta(n/\log n))$, the mean-gap order, while at $\ell=n$ it is
$\exp(-n/(\log n)^2)$ against a mean gap of $\exp(-\Theta(n/\log n))$ (the
subsets of the primes in $(n/2,n]$ alone give $\exp(\Theta(n/\log n))$
divisors in every $[e^\ell,2e^\ell]$ with $\ell\ge\theta(n)-\theta(n/2)$).
Adopts the question (c) report's F1, with the constant $c_\tau$ of its
replacement left out so that the page keeps Chebyshev as its only
prime-count import, and its F2.

**C14.** Section "Problem 1099", two places.

(a) The sentence after the display of the two-sided bound. Replace

> For $\alpha\ge1+\eta$ the correction is tiny:
> $(4\varepsilon_j)^{\alpha-1}\le2^{-62(\alpha-1)}$, and $C(2)<10^{-10}$.

with

> The correction is small only when $\alpha$ is bounded away from $1$: for
> every $j$, $(4\varepsilon_j)^{\alpha-1}\le2^{-62(\alpha-1)}$, so
> $C(\alpha)\le2^{62\eta}C(1+\eta)\,2^{-62(\alpha-1)}$ for
> $\alpha\ge1+\eta$, with $C(2)<10^{-10}$ and $C(3/2)<10^{-3}$; but
> $C(5/4)\approx20$ exceeds $2\zeta(5/4)$, and $C(\alpha)\to\infty$ as
> $\alpha\to1^+$.

(b) Paragraph "What it does not give", last sentence. Replace

> Only the explicit value $2\zeta(\alpha)+O(2^{-62(\alpha-1)})$ appears to
> be new, and no search for it in the later literature was made.

with

> Only the explicit bound $2\zeta(\alpha)+C(\alpha)$, with
> $C(\alpha)=O_\eta(2^{-62(\alpha-1)})$ for $\alpha\ge1+\eta$, appears to
> be new, and no search for it in the later literature was made.

Verified by the independent evaluation described in the Subject:
$C(5/4)\approx20.3>9.19\approx2\zeta(5/4)$, $C(3/2)\approx1.8\cdot10^{-4}$,
$C(2)\approx3.7\cdot10^{-14}$, and every term of $C(\alpha)$ increases to
$4(\tfrac12\log j+\log2)$ as $\alpha\to1^+$, a divergent series, so
$C(\alpha)\to\infty$ by monotone convergence; the factor
$\tfrac12\log j+\log2$ is not summable, so the per-term bound says nothing
uniform in $\alpha$. The inequality
$C(\alpha)\le2^{62\eta}C(1+\eta)2^{-62(\alpha-1)}$ follows from
$4\varepsilon_j\le2^{-62}$. Adopts the Problem 1099 report's F1.

**C15.** Section "Problem 673", Target paragraph. Replace

> a site comment's bounds $\tau(n/m)/m\le G(n)\le\tau(n)$ for $m\mid n$

with

> a site comment's bounds $\tau(n/m)/m\le G(n)\le\tau(n)$ for $1<m\mid n$
> (the lower bound fails at $m=1$, since $G(n)<\tau(n)$ for every $n$)

Verified: $G(n)$ is a sum of $\tau(n)-1$ terms each below $1$, so
$G(n)<\tau(n)-1$ for $n\ge2$ and $G(1)=0$; at $n=2$, $m=1$ the bound would
read $2\le\tfrac12$. For $m\ge2$ every divisor $e$ of $n/m$ has a
successor at most $em$ among the divisors of $n$, which gives the bound;
the section's own use is at $m=2$. If the site comment states the bound
without the restriction, the page still carries the true range. Adopts
the Problem 673 report's F1.

**C16.** Section "Problem 859", Outcome paragraph. Replace

> which is $\ge1/t^{2}$ at best (Proposition 4.1 places $N$ in $[t,t^2)$)
> and says nothing at the scale $(\log t)^{-\delta}$.

with

> which is at least $1/t^{2}$ (Proposition 4.1 places $N$ in $[t,t^2)$
> once $t\ge x_0$) and at most $1/t$ for any seed $N\ge t$, so polynomial
> in $1/t$ whatever the construction, and says nothing at the scale
> $(\log t)^{-\delta}$.

Verified: $N\in[t,t^2)$ gives $1/N>1/t^2$, so "at best" names the wrong
extremum; the folder's other seeds do better (the least $n!\ge t$ has
$n!<nt$, and $2^{\lceil\log_2t\rceil}<2t$ is practical), and every seed
$N\ge t$ gives at most $1/t$; the conclusion holds for every polynomial
floor since $t^{-1}=o((\log t)^{-\delta})$. Adopts the Problem 859
report's F1.

**C17.** Section "Other divisor problems examined", first bullet. Replace

> Lemma A is the trivial instance for $n!$ and $L_x$;

with

> for $n,x\ge3$ the divisors $2<3<4$ of $n!$ and $L_x$ give the property
> outright (Lemma A's non-strict ratio bound alone does not, as $N=2^k$
> shows);

Verified: Lemma A concludes $b\le2d$ for consecutive divisors, and the
Problem 144 property needs $d_2<2d_1$; $N=2^k$ satisfies Lemma A's
hypothesis vacuously, has every consecutive ratio equal to $2$, and has no
such pair; $2!$ and $L_2$ fail the property likewise. Adopts the other
divisor problems report's F1.

## Rejected and downgraded findings

Findings are cited by report and label. "Downgraded to note" means the
observation is correct and the change is optional, or no exact replacement
is warranted; "rejected" means the claimed defect is not one.

Shared lemmas report.

- F3 (suggested; $n(\eta)$ undefined): accepted inside C1(b).
- F4 (note; the aside "whence $p\ll\log n$" imports a Chebyshev-type
  bound unnamed): downgraded to note; the proof uses only $p\le n-1$,
  which the reviewer shows holds for every $n\ge3$, and the aside is true.
- F5 (note; "as the Problem 304 page records" outside the read set):
  downgraded to note, verified here: the Problem 304 page's Origin
  paragraph records Erdős's 1950 route through $n!$ with $(n-1)!<b\le n!$,
  and its Upper bounds bullet records Vose's bound as restated by van
  Doorn and Tang, with denominators dividing, or $b$ times divisors of, a
  number $N_K$; the attribution is right.

Problem 304 report.

- F3 (note; "once $b>(n_0-1)!$" omits $n\ge14$): downgraded to note; the
  statement asserts an existential threshold $b_0(\varepsilon)$, the proof
  says "for large $b$" before naming the threshold, and $n\ge10$ already
  suffices for $n<\log b$; the reviewer's "$b>\max(n_0-1,13)!$" is the
  exact threshold and is optional.
- F4 (note; "which is the note's Theorem 1.2" for a bound stronger by
  $2$): downgraded to note; the result page states
  $N(b)\le2c_0(\log\log b)^2$, which the derived bound implies, and "is"
  reads as "recovers".
- F5 (note; "Its standing is that of part (b)"): downgraded to note; the
  sentence goes on to list that standing and to name the transfer as
  Lemma C, which the page's preamble labels author-recorded.
- F6 (note; the greedy count on non-factorial ratio-two integers is not
  blocked): accepted as C4 with the replacement supplied here.
- F7 (note; "exact site questions" while Problem 293 is read with $m>1$):
  downgraded to note; the Problem 293 page's Formulation records the $m>1$
  reading as the intended statement of the monograph, the site's
  discussion and the van Doorn–Tang paper, and every bound on that page
  uses it.

Problem 293 report.

- F3 (note; outside the section): accepted as C1.
- F4 (note; "so $v(k)\ge\exp(k^{A})$" needs $\varepsilon<1/A$): downgraded
  to note; the deduction is immediate with $\varepsilon=1/(2A)$ and
  $k\ge25$, and the page does not say $\varepsilon=1/A$.
- F5 (note; the consistency sentence is vacuous and the listing was not
  checked): downgraded to note; the consistency claim is indeed empty for
  bounds with unspecified thresholds, and the Problem 293 page does list
  $v(3),\dots,v(8)$ in its "Finite values (unreviewed leads)" paragraph,
  as values reported in a site comment and not reviewed, which "known" on
  the connections page overstates by a word.

Problem 18, question (a) report.

- F7 (note; "nothing unconditional beyond", "Three facts ... are
  established", "The computation distinguishes"): the third part is
  accepted inside C11(c); the first two are downgraded to note, since
  "unconditional" reads as "not conditional on $(\mathrm H_c)$" while the
  same paragraph marks the Tenenbaum reading as a text-layer reading, and
  since the lead's third fact names Tenenbaum's paper, whose page on the
  connections page carries the mark.

Problem 18, question (c) report.

- F3 (suggested; "does not run through a gap profile" outruns the read
  record): downgraded to note; the same sentence says the structure was
  "read only at the level of theorem statements", which is the
  qualification the reviewer asks for.
- F4 (suggested; "at least as hard as $(\mathrm H_c)$" without a
  reduction): downgraded to note; the clause is an informal assessment of
  difficulty, not a claimed implication, and the reviewer's own transfer
  (a consecutive pair of $n!$ sits inside a consecutive pair of $L_n$ of
  comparable geometric mean, so $(\mathrm H_c)$ at $x=n$ reaches only the
  bottom of the factorial range) supports rather than refutes it; the
  replacement "of the same mean-gap character; neither hypothesis is known
  to imply the other" is optional.
- N1 to N4 (notes): downgraded to notes; the dropped $(1\pm o(1))$ factors
  do not affect the comparisons, $\ell_0$ is Lemma B's $\log(2T)$, "the
  only mechanism aimed at $n!$" means the only one that could reach
  question (c), and the lower bound $\log\tau(n!)\gg n/\log n$ is unused.

Problem 1099 report.

- F2 (note; a sharper form of the corollary): downgraded to note; the
  stated interval is correct.
- F3 (note; "would be good candidates" against the held wording):
  downgraded to note; the section attributes the quotation to the site
  page, which was not read here, and the held paper (p. 171, checked here
  in the layout text) reads "seem to be good candidates for integers with
  (1.1) bounded above"; quoting the held wording is preferable.
- F4 (note; "has no compiled assessment" while the page carries a Current
  assessment heading): rejected. As of 2026-09-28T13:50:48Z the Problem 1099
  page's Current assessment section reads "No current assessment is recorded",
  so the sentence and the Next investigation item are accurate; the later
  `updated` stamp reflects the page's Progress paragraph, which records this
  very transfer.
- F5 (note; unheld-source characterizations): downgraded to note, a
  limitation the section itself states.

Problem 673 report.

- F2 (suggested; cite the held 1982 survey instead of the site):
  downgraded to note; the section reports what the site page records, and
  the reviewer verified both attributions against the held survey, so
  nothing is false; citing the survey is preferable.
- F3 (note; the notation $2^EV_j$): downgraded to note.

Problem 859 report.

- F2 (suggested; "No transfer exists" is a universal negative): downgraded
  to note; the sentence is the page's outcome vocabulary for a section
  whose Outcome line reads "fails", and the reviewer's own attack finds no
  transfer bearing on the target.
- F3 (note; status text unverified): downgraded to note, a limitation.

Other divisor problems report.

- F2 (suggested; the Berend–Harmse parenthetical is an unmarked text-layer
  characterization): downgraded to note; the page's "Sources read for this
  page" discloses that every Berend–Harmse statement comes from the Numdam
  text layer, which is the mark for this parenthetical as for the
  page-numbered citations in the Problem 1099 section; a per-statement
  mark is optional.
- F3 (suggested; for Problems 469 and 470 practicality entails
  pseudoperfection): downgraded to note; the entailment (every practical
  $n$ with $\sigma(n)\ge2n$ is a sum of distinct proper divisors, so no
  weird number is practical) is correct and was re-derived here from the
  completeness lemma, and the bullet's reason is loose, but its
  no-transfer conclusion holds for the questions asked, which concern
  primitive pseudoperfect numbers, odd weird numbers and primitive weird
  numbers.
- F4 (suggested; "opposite" against the divisor set of $2^k$): downgraded
  to note; the divisor set of $2^k$ has distinct subset sums and is
  practical, so "opposite" is loose, but the conclusion holds.
- F5 to F7 (notes): downgraded to notes.

## Graded verdicts

Per statement, with the reports' labels, as graded, with the corrections
that apply. "Refutation-failed" and "refuted-as-stated" are written in
full throughout.

Shared lemmas.

- S1 (Lemma A): refutation-failed.
- S2 (Lemma B): refutation-failed.
- S3 (Lemma C): refutation-failed.
- S4 (Lemma C′): refutation-failed.
- S5 (Lemma D, first inequality): refutation-failed.
- S6 (Lemma D, second inequality, uniform over all chains):
  refuted-as-stated, by the witness of C1; the subtracted form and the
  bounded-seed floor that C1 writes are refutation-failed.
- S7 (Lemma D, "Hence" sentence, unrestricted seeds): proof defective;
  statement unresolved; for bounded seeds, as C1 writes it,
  refutation-failed.
- S8 (closing paragraph): refutation-failed.

Problem 304.

- S1 (Lemma C): refutation-failed.
- S2 (Lemma C′): refutation-failed.
- S3 ((304.1)): refutation-failed, as a deduction conditional on the
  accepted part (b) at its recorded standing.
- S4 ((304.2)): refutation-failed, conditional on Theorem 1 at its
  standing.
- S5 ((304.3)): refutation-failed as a deduction from Proposition 4.1,
  which stays claimed.
- S6 (reduction): refutation-failed.
- S7 (factorial obstruction): refutation-failed.
- S8 (extension-chain obstruction, as written): proof defective;
  statement unresolved; with the bounded-seed clause of C2,
  refutation-failed.
- S9 (consequence sentences): refutation-failed at the two reconstructed
  mechanisms, the scope C4 writes.
- S10 ((293.1) on the lead): refutation-failed, conditional on part (b).
- S11 (standing and input sentences): refutation-failed for the input
  sentences; the priority sentence is replaced by C3.

Problem 293.

- S1 (transfer observation): refutation-failed.
- S2 ((293.1)): refutation-failed, conditional on part (b).
- S3 (corollary and calibration): refutation-failed.
- S4 ((293.2)): refutation-failed at the standing of Theorem 1.
- S5 ((293.3)): refutation-failed as a deduction from the claimed
  Proposition 4.1.
- S6 (exponent-one obstruction): refutation-failed.
- S7 (factorial-route cap): refutation-failed, with the citation repaired
  by C5.
- S8 (extension-chain cap): refutation-failed for bounded seeds, as C6
  writes it.
- S9 (converse flow): refutation-failed.
- S10 (falsification paragraph): refutation-failed.
- S11 (closing sentence): not a mathematical claim; its consistency
  clause is vacuous (note).
- T (target paragraph): descriptive; consistent with the Problem 293 page
  read here.

Problem 18, question (a).

- S1 (Lemma A at $L_x$): refutation-failed.
- S2 ((18a.1)): refutation-failed; its proof carried the slip repaired by
  C7.
- S3 (the comment's form fails in the top range): refutation-failed.
- S4 (the lower-range constant $1/c$): refutation-failed.
- S5 (the constant $1/c$ from the mirror argument): proof defective;
  statement unresolved as written; the constant $2/c$ that C8 writes is
  refutation-failed.
- S6 ((18a.2)): refutation-failed as a conditional deduction from the
  quoted admissibility statement, which is unverified here.
- S7 (the necessary bound $c\le2\log2$): refutation-failed.
- S8 (the mean-gap gloss): refuted-as-stated under the reading in which
  it has content; replaced by C9.
- S9 (the computation): refutation-failed for every printed value;
  refuted-as-stated for the location of the binding pairs, the labeling
  of the quoted maxima and "does not decrease"; replaced by C10.
- S10 (the obstruction drawn from a disproof): proof defective; statement
  unresolved; replaced by C11.
- S11 (the lead's "dominates"): refuted-as-stated; replaced by C12.
- S12 (what it does not give): refutation-failed.

Problem 18, question (c).

- S1 (target): refutation-failed for the two bounds.
- S2 (necessary condition and natural profile): refutation-failed.
- S3 (demand at the middle): refutation-failed.
- S4 (mean-gap floor): refutation-failed.
- S5 ("$C=2$ is impossible for the greedy route"): proof defective;
  statement unresolved as written; refutation-failed on the narrow
  reading and for the counting bound that C13 writes.
- S6 ($C=3$ at every scale): refuted-as-stated for "at every scale";
  refutation-failed at the windows of index $j\asymp n$, as C13 writes it.
- S7 (Berend–Harmse comparison): refutation-failed.
- S8 (the accepted proof's structure): refutation-failed as the hedged
  description the sentence gives.
- S9 (outcome): "open" refutation-failed; the hardness comparison is an
  informal assessment (note).
- S10: not a claim.

Problem 1099.

- S1 (convergence of $C(\alpha)$): refutation-failed.
- S2 (two-sided bound for $n\ge T$): refutation-failed.
- S3 (limits along $n!$): refutation-failed.
- S4(a), S4(b): refutation-failed.
- S4(c) (the correction uniformly tiny): refuted-as-stated; replaced by
  C14.
- S5 (corollary on (1.2)): refutation-failed.
- S6 (scope): refutation-failed.
- S7 (attributions): the parts checkable against held sources agree; the
  rest is not a mathematical claim.

Problem 673.

- S1 (target): refutation-failed.
- S2a (records): refutation-failed for the two attributions.
- S2b (the site comment's bound for $m\mid n$): refuted-as-stated at
  $m=1$; refutation-failed for $m\ge2$, as C15 writes it.
- S3 (density-zero obstruction): refutation-failed.
- S4 (factorial bound): refutation-failed.
- S5 (even-$n$ bound): refutation-failed.
- S6 (non-transfer verdict): refutation-failed.

Problem 859.

- S1 (target): refutation-failed.
- S2 (recorded status): a report of status text; the deduction it
  carries is refutation-failed.
- S3 (outcome): refutation-failed.
- S4 (transfer lemma): refutation-failed.
- S5 (consequence): refutation-failed.
- S6 (polynomial floor): refutation-failed for the inequality; the
  wording is repaired by C16.
- S7 (not through $h$): refutation-failed.
- S8 ("No transfer exists"): refutation-failed as the section's
  conclusion.

Other divisor problems examined.

- S0: not a claim.
- S1 (Problem 144): refutation-failed for $n,x\ge3$, as C17 writes it.
- S2 (widths): refutation-failed.
- S3 (no transfer to Problems 886 and 887): refutation-failed.
- S4 (Berend–Harmse Theorems 3 and 4): a characterization of an unheld
  source; no verdict.
- S5 (Problem 1100): refutation-failed.
- S6 (Problems 468, 469, 470 and 1054): refutation-failed for the
  no-transfer conclusion.
- S7 (Problems 350 and 882): refutation-failed for the no-transfer
  conclusion.
- S8 (Problems 446, 448, 449 and 450): refutation-failed.

**Lead outcomes.**

- [[research/leads/factorial_unit_fraction_transfer/_index|factorial_unit_fraction_transfer]]:
  **reviewed**. Every statement its route rests on is refutation-failed:
  Lemma A, Lemma C, Lemma C′ with the Lemma 3.1 interface it consumes, the
  refereed nesting lemma and $v(k)\to\infty$, and (304.1) and (293.1),
  each conditional on part (b) at its recorded standing. The corrections
  that touch the lead (C2(b), C4(b)) repair its obstruction paragraph, on
  which the route does not rest; the note on "exact site questions" is
  optional. Its next step, the fresh-context review of Lemma C, Lemma C′,
  (304.1) and (293.1), is what these reports supply.
- [[research/leads/lcm_divisor_gap_greedy_route/_index|lcm_divisor_gap_greedy_route]]:
  **needs_update**. The conditional transfer (18a.1), Lemma A and Lemma B
  are refutation-failed, and the necessary bound $c\le2\log2$ stands; but
  the lead's Consequential gap rests on the constant $1/c$ (S5, proof
  defective; statement unresolved) and on the obstruction drawn from a
  disproof (S10, proof defective; statement unresolved), its Exploratory
  computation section is refuted-as-stated in its description of the
  binding pairs, the quoted maxima and the trend of $\kappa_{\min}$ (S9),
  its mean-gap gloss is refuted-as-stated (S8), and its Next step rests on
  the dominance claim (S11, refuted-as-stated). C8(b), C9(b), C10(b),
  C11(b), C11(c) and C12 rewrite those sentences; once they are applied,
  every statement the route rests on is refutation-failed, the premise
  $(\mathrm H_c)$ remains unproved, and the exploratory computation
  carries no evidence.

No tier is assigned and no status changes.
