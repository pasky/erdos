---
name: research/erdos_18/evidence/verify/lead_lcm_divisor_gap_greedy_route_rereview_grade
title: "Distinct grade of the re-review of lead lcm_divisor_gap_greedy_route"
desc: |
  Distinct grader's check of the blind re-review of the lead
  lcm_divisor_gap_greedy_route as it stood on 2026-10-02: the report passes as a
  focused review record, every verdict is re-derived and agreed, the computation
  is reproduced a third way, the required corrigendum disclosure and six of the
  nine suggested corrections are accepted with their exact text, three are
  rejected, the lead is reviewed and ready, and no tier is assigned.
created: 2026-10-02T17:34:40Z
updated: 2026-10-02T17:34:40Z
---

***

## Subject

The tree as it stood on 2026-10-02. The report graded is
`wiki/research/erdos_18/evidence/verify/lead_lcm_divisor_gap_greedy_route_rereview.md`,
read in full. Its subject, read here at proof depth from the same blind
extraction the reviewer used, kept outside the repository and frozen on that
date: the lead page
`wiki/research/leads/lcm_divisor_gap_greedy_route/_index.md` with its
review-status fields and its "Current review" section removed, and the
connections page `wiki/research/erdos_18/connections.md`, of which the sections
in scope are "Shared lemmas" (Lemma A and Lemma B), "Problem 18, question (a),
along the least common multiples", the sentence about this lead under "Leads
created" and "Sources read for this page". The other sections of the connections
page were read for context and are not graded here.

The extraction was checked against the pages of that date without printing the
removed text: the lead extraction is the committed page with 45 lines removed
and none added, and the connections extraction is byte-identical to the
committed page. The report's description of the connections extraction as having
"its review-report sentences cut" is therefore inexact (the committed page
carries none), which does not change what was reviewed.

The report is a focused re-review of author-recorded research; it carries no
tier and this grade assigns none.

## Independence

The grader is a distinct grader in a fresh context, model Claude Fable 5.1:
neither the author of the lead, the connections page or the reconstruction
pages, nor the reviewer who wrote the report, and not a participant in either
piece of work. The grader received only the grading assignment, which named the
frozen date, the extraction, the report, the record to write and the guidance
pages to read. No working material of the author or of the reviewer reached the
grader, and nothing was read from the web.

A first attempt at this re-review, whose extraction carried the earlier
verdicts, was stopped before completion and its output discarded; this record is
from a blind extraction frozen on 2026-10-02 and kept outside the repository.

**Read set and depth.** `docs/verification.md` in full; the review-record parts
of `docs/evidence.md`; `docs/research.md` ("Updating and checking",
"Erdos-specific", "Optional lead metadata"); `docs/approach_vetting.md`;
`docs/math_authoring.md` for page mechanics. The two extraction files in full.
From the tree of the frozen date, mathematics only: the Lemma 4 reconstruction
from its Definitions to the end (lines 32 on), the Theorem 1 reconstruction from
its Definitions through Gaps and qualifications (lines 36–325), the Corollary 3
reconstruction from its Definitions through its Statement (lines 31–104); the
held Hughes conversion in
`library/divisors/hughes_2026_sums_distinct_divisors_factorials/`: the
introduction sentence that cites references [3] and [4], Lemma 4 and the
reference list; the lead's `evidence/_index.md` and
`evidence/util/gap_profile.py`; the Problem 18 page's Statement paragraph (lines
15–30), and nothing of its Status paragraph or Current assessment.

**Exposure.** The existing grade in this folder, `connections_grade.md`, was
read in full for the shape of this record, as the assignment directed. It
carries the earlier grade's verdicts and corrections for this lead on
2026-09-28. By the content test, nothing in this record could only have come
from it: the frozen text already incorporates those corrections, and every
re-derivation, number and decision below is made from the extraction, the report
and the held sources named above. The exposure is ruled immaterial. Not read:
the live lead page, every other record under any `evidence/verify/` folder, and
all review-status, standing or "Current review" text. Tenenbaum (1987) and
Berend–Harmse (1993) are not held and were not read; statements about them are
checked only against the held Hughes conversion.

**Independent computation.** The divisor-gap profile was recomputed by a
script written for this grade from the lead's description, outside the
repository and not retained with this record; the description and the
numbers below let a reader rerun it. Every divisor of $L_x$ for
$x=20,30,40,50,60,64$ was generated from the prime-power factorization as an
exact integer and sorted; the ratio-two property $b\le2d$ was checked exactly
at every consecutive pair; the window was taken by the exact test
$x^2\le db\le L_x$; $\log(b/d)$ was computed as $\log(1+(b-d)/d)$ and
$\kappa(d,b)=(\log x)\log(1/\log(b/d))/\log\sqrt{db}$ in floating point, with
a 60-digit decimal recheck at each minimizer and a direct test of
$(\mathrm H_c)$ at the minimizer for $c=\kappa_{\min}(1\pm10^{-6})$; the
largest $\log(b/d)$ was taken in tenths of $[0,1]$ and in tenths of the
actual range $[\log x/\log\sqrt{L_x},1]$ of $\log\sqrt{db}/\log\sqrt{L_x}$.
Results: pairs in the window $461$, $3811$, $18393$, $221135$, $884677$,
$2064321$; $\kappa_{\min}=1.115794$, $1.256764$, $1.310676$, $1.297554$,
$1.347774$, $1.358251$, at the pairs $(15048,15470)$, $(807576,812889)$,
$(59374455,59477220)$, $(21557311776,21565368600)$,
$(2700266996700,2700485397828)$, $(30793652410950,30794863747120)$, with
$\log(b/d)=2.77\cdot10^{-2}$, $6.56\cdot10^{-3}$, $1.73\cdot10^{-3}$,
$3.74\cdot10^{-4}$, $8.09\cdot10^{-5}$, $3.93\cdot10^{-5}$ and
$\sqrt{L_x/db}=1.000$, $1.884$, $1.230$, $2.582$, $1.153$, $1.117$; the
minimizer at $x=20$ has $db=L_{20}$ exactly; the minimum restricted to
$\sqrt{db}\ge x^2$ is attained at the same pair at every $x$; the pair
satisfies $(\mathrm H_c)$ at the lower control value of $c$ and violates it
at the higher one; the top-tenth maxima in tenths of $[0,1]$ are
$2.77\cdot10^{-2}$, $6.71\cdot10^{-3}$, $1.87\cdot10^{-3}$,
$3.74\cdot10^{-4}$, $9.70\cdot10^{-5}$, $4.45\cdot10^{-5}$, and in tenths of
the actual range the same except $6.56\cdot10^{-3}$ and $1.76\cdot10^{-3}$
at $x=30,40$. The finite form of the counting bound,
$\kappa_{\min}(x)\le(\log x)\log(\tau(L_x)/\log x)/\log(\sqrt{L_x}/(\sqrt2\,x))$,
evaluates to $2.748$, $2.504$, $2.414$, $2.222$, $2.184$, $2.154$ on the
sample, $2.056$ at $x=100$, $1.714$ at $x=1000$ and $1.594$ at $x=10^4$,
and $\log\tau(L_x)/(x/\log x)$ is $0.97$–$1.03$ on the sample. Also
$\tau(L_{100})=660602880=315\cdot2^{21}$. Every one of these agrees with the
report's Notes and with the lead's table. The report's certificate was run
as printed and gives the six lines it describes; the author's command was
rerun verbatim from the repository root and printed the lead's table, in
about fifteen seconds of wall time including the environment start.

## Report checks

- **Subject block.** The date is named and the paths are the ones read;
  the extraction is the committed text minus the cuts named (checked above);
  the role, fresh context and model are stated; allowed and actually read
  material, exclusions and one exposure are listed. Pass.
- **History sentence.** Present verbatim in "Subject and independence".
  Pass.
- **Exposure.** The first 22 lines and the headings of the Problem 859 review
  record were printed for the frontmatter shape; its `desc` summarizes a
  verdict on a section with no transfer to this route. By the content test
  nothing in the report could only have come from it and no attack direction
  followed it. Ruled immaterial.
- **Restatement.** Target, (A), (B), $(\mathrm H_c)$, (18a.1) and the side
  statements restated with every quantifier and the convention on $h$. Pass.
- **Checklist.** An explicit verdict on each of the ten items, with the
  inapplicable parts said to be inapplicable. Pass.
- **Weakest steps.** Three, re-derived in the reviewer's words (Lemma B's
  upper range, the transfer, the necessary bound); each is re-derived again
  below and agreed. Pass.
- **Strongest attack.** A disproof of $(\mathrm H_c)$ attempted in three
  directions, with the reason each failed; the domain attack on Lemma B
  recorded. Pass.
- **Premises.** No local claim consumed; Hughes's Lemma 4 at proof depth
  against the held conversion (checked here: the conversion's Lemma 4 is the
  reconstruction's statement); the prime number theorem assumed; Tenenbaum,
  Berend–Harmse and the site comment unread with their interfaces stated;
  $(\mathrm H_c)$ as the explicit unproved hypothesis. Pass.
- **Coverage.** Twenty-seven lead items and the connections sentences in
  scope each carry a verdict; every mathematical statement of the
  extraction's scope is covered. The re-derivation printed for Lemma A spells
  out the $L_x$ case only; the factorial and $p^{j}M$ clauses are covered by
  the verdict and are re-derived below. Pass.
- **Verdict words.** "Refutation-failed" written in full throughout; no
  abbreviation; no tier asserted. Pass.
- **Computation.** The author's rerun performed verbatim; the independent
  route described, its witnesses tabulated and a standalone certificate
  retained in the record; scratch scripts not retained, which a focused
  review may do. Pass.
- **Record hygiene.** Frontmatter, separator and sections as the folder's
  records carry them; no person, seat, session, harness or private path
  named. Pass.

The report **passes** as a focused review record.

## Verdicts re-derived

Numbered as the report's "Statement verdicts"; each verdict applies to the
lead page and to the connections text it names.

1. Target paragraph: not a mathematical claim. Agree. The Statement paragraph of
   the Problem 18 page gives question (a) and defines $h(m)$ as the lead does;
   the lead's report of the dated assessment is outside the read set. 2. $\log
   L_x=\psi(x)\sim x$, $\log\log L_x=\log x+o(1)$: refutation-failed. Agree;
   $\log L_x=\sum_{p\le x}\lfloor\log x/\log p\rfloor\log p=\psi(x)$ and
   $\psi(x)\sim x$ is the prime number theorem. 3. Attributions to Tenenbaum p.
   2 and to the site discussion: not mathematical. Agree; both sources are
   outside the read set. 4. Lemma A: refutation-failed. Agree; re-derived. For
   $d\mid N$, $d<N$, $q=N/d$: if $q$ is even, $2d\mid N$. If $q$ is odd, take an
   odd prime $p\mid q$ and $c=\lfloor\log_2p\rfloor$, so $2^c<p<2^{c+1}$; $q$
   odd gives $v_2(d)=v_2(N)\ge c$, $p\mid q$ gives $v_p(d)<v_p(N)$, so
   $d'=dp/2^c$ is an integer dividing $N$ with $d<d'<2d$. Hence the divisor
   following $d$ is at most $2d$. The consequence: a nonterminal greedy step at
   $R$ with bracketing $d<R<b$ has $d\ge b/2>R/2$, so remainders halve, at most
   $\lfloor\log_2m\rfloor$ nonterminal steps and one terminal divisor; with
   Lemma 4's distinctness every $m\le N$ is a sum of distinct divisors, so $N$
   is practical and $h(N)\le\log_2N+1$. Hypothesis for $L_x$:
   $v_2(L_x)=\lfloor\log_2x\rfloor\ge\lfloor\log_2p\rfloor$ for $p\le x$. For
   $n!$: $v_2(n!)\ge\lfloor n/2\rfloor\ge\lfloor\log_2n\rfloor$ for $n\ge4$, and
   $1$, $2$, $6$ have consecutive ratios at most $2$. For $p^{j}M$:
   $v_2(p^{j}M)=v_2(M)$, and the odd primes dividing $p^{j}M$ are those of $M$
   together with $p$, so the hypothesis is that of $M$ plus
   $\lfloor\log_2p\rfloor\le v_2(M)$. 5. Lemma B: refutation-failed. Agree;
   re-derived in full. Lower range $2T\le R\le\sqrt N$:
   $R/\sqrt2<\sqrt{db}<\sqrt2R$; fact (i) ($d<\sqrt N$ makes $N/d>R$ a divisor,
   so $b\le N/d$) gives $\sqrt{db}\le\sqrt N$; $\sqrt{db}>R/\sqrt2\ge\sqrt2T$;
   $R/2\in[T,\sqrt N/2]$; so
   $\log(b/d)\le\tfrac12\delta(\sqrt{db})\le\tfrac12\delta(R/2)$ and Lemma 4
   gives $R'\le R\,\delta(R/2)$, $\log R'\le\log R-\sigma(\log R)$; the charging
   integral over $[\log R',\log R]$ is at least $1$ since $\sigma\le\sigma(\log
   R)$ there, the intervals are adjacent and lie in $[\log(2T),\tfrac12\log N]$
   except the last: at most $1+\int$ steps. Upper range $\sqrt N<R\le N/(2T)$:
   $U=N/R\in[2T,\sqrt N)$; the mirror pair $N/b<U<N/d$ is consecutive with ratio
   $b/d$ and geometric mean $N/\sqrt{db}\in(U/\sqrt2,\sqrt2U)$; fact (ii)
   ($N/b<\sqrt N<R$ is a divisor below $R$, so $N/b\le d$) gives
   $N/\sqrt{db}\le\sqrt N$; so $\log(b/d)\le\tfrac12\delta(U/2)$ and Lemma 4 at
   $R$ gives $\log U'\ge\log U+\sigma(\log U)$. On $J_k$ consecutive starts are
   $2^k\log8$ apart while $1/\sigma>1/(2^{k+1}\log8)$, so $J_k$ holds at most
   $1+2\int_{J_k}d\ell/\sigma$ starts, and the number of nonempty $J_k$ is at
   most $\log_2(\sigma(\tfrac12\log N)/\log8)+1$. Endgames: halving gives at
   most $\log_2(2T)+1$ steps each. Total with the terminal divisor:
   $3\int+\log_2\sigma(\tfrac12\log N)+2\log_2(2T)+5-\log_2\log8$, below the
   display. The hypotheses $\delta\le1/8$, $T\ge2$ and $2T\le\sqrt N$ are used
   ($\sigma\ge\log8>0$, the domain of $\delta$, a nonempty range). 6. "Step
   count of Theorem 1 with a profile, using only Lemma 4 and the mirror
   symmetry": refutation-failed. Agree; checked against the Theorem 1
   reconstruction, whose inputs are facts (i), (ii), Lemma 4 and Corollary 3's
   window bound, the last replaced by the profile; the upper range's dyadic
   blocks of window indices become dyadic blocks of $\sigma$. 7. $(\mathrm H_c)$
   and $\kappa$ as the largest admissible $c$ at a pair: refutation-failed.
   Agree; with $g=\sqrt{db}\ge x>1$ and $0<\log(b/d)\le\log2<1$, $\log(b/d)\le
   g^{-c/\log x}$ is equivalent to $c\le(\log x)\log(1/\log(b/d))/\log g$. 8.
   (18a.1): refutation-failed as a conditional statement. Agree; re-derived.
   $T=x^{4/c}\ge x\ge2$ for $c\le4$; $\delta(g)=2g^{-c/\log x}$ is nonincreasing
   with $\delta\le\delta(T)=2e^{-4}<1/8$; $2T\le\sqrt{L_x}$ once
   $\log2+(4/c)\log x\le\tfrac12\psi(x)$; $(\mathrm H_c)$ on
   $[x,\sqrt{L_x}]\supseteq[T,\sqrt{L_x}]$ is Lemma B's hypothesis since
   $\tfrac12\delta(\sqrt{db})=(db)^{-c/(2\log x)}$; with $\kappa=c/\log x$,
   $\sigma(\ell)=\kappa\ell-(1+\kappa)\log2\ge\kappa\ell-2$ for $x\ge9$;
   $\kappa\log(2T)-2=2+\kappa\log2\ge2$; the integral is at most
   $\kappa^{-1}\log((\kappa x-2)/2)\le(\log x/c)\log(cx/\log x)\le(\log x)^2/c$
   for $x\ge e^{c}$, using $\tfrac12\psi(x)\le x$; the other terms are $O(\log
   x)$ and $O(\log x/c)$; $(\log\log L_x)^2=(\log x)^2+o(\log x)$. The $o(1)$
   depends on $c$, as the statement allows. Decreasing $c$ is legitimate because
   $(db)^{-c/(2\log x)}$ increases as $c$ decreases. 9. "Answers question (a)
   with exponent $2$ along $L_x$": refutation-failed as a conditional. Agree;
   under $(\mathrm H_c)$ the $L_x$ are infinitely many practical integers with
   $h\le(3/c+o(1))(\log\log L_x)^2$. 10. The comment's form fails in the top
   range: refutation-failed. Agree; $(L_x/2,L_x)$ is a consecutive pair by Lemma
   A, so $\Delta_x(L_x)+1\ge L_x/2$ while $L_x^{1-c/\log x}=L_xe^{-c\psi(x)/\log
   x} =o(L_x)$; for $Y\in(L_x/2+2L_x^{1-c/\log x},L_x]$ the capped gap exceeds
   $2L_x^{1-c/\log x}-1\ge Y^{1-c/\log x}$; the divisors near $L_x/k$ are the
   $L_x/j$ with $j$ near $k$ (a divisor between $L_x/(k+1)$ and $L_x/k$ would be
   $L_x/q$ with $q$ an integer strictly between $k$ and $k+1$), with gaps
   $L_x/(k(k+1))\gg(L_x/k)^{1-c/\log x}$ for bounded $k$. 11. The lower-range
   recurrence and the direct count $2/c$: refutation-failed. Agree; re-derived.
   With the profile of (18a.1) the lower-range step is $R'\le
   R\,\delta(R/2)=2^{1+\kappa}R^{1-\kappa}$, the comment's recurrence up to the
   factor $2^{1+\kappa}$; iterating $\log R'\le(1-\kappa)\log R+(1+\kappa)\log2$
   from $\tfrac12\log L_x$ to $\log(2T)$ takes $(1+o(1))(\log x)^2/c$ steps; the
   mirror recurrence $\log U'\ge(1+\kappa)\log U-(1+\kappa)\log2$ becomes
   $v'\ge(1+\kappa)v$ for $v=\log U-(1+\kappa)\log2/\kappa$, which is at least
   $(4-\log2)\log x/c>0$ on the range, and takes $(1+o(1))(\log x)^2/c$ steps;
   so the direct count is $(2/c+o(1))(\log x)^2$ and Lemma B's $3/c$ loses the
   factor $2$ of its upper-range dyadic count. The word "exactly" is wrong by
   the constant factor; correction G5 below. 12.
   $\log\tau(L_x)=(\log2+o(1))x/\log x$: refutation-failed. Agree; the primes in
   $(\sqrt x,x]$ contribute $\log2$ each and number $(1+o(1))x/\log x$; the
   primes up to $\sqrt x$ contribute $O(\sqrt x\log\log x/\log x)$. 13.
   $c\le2\log2+o(1)$: refutation-failed. Agree, with the reviewer's repair of
   the straddling pair. Fewer than $\tau(L_x)$ consecutive pairs meet the window
   $[\sqrt{L_x}/x,\sqrt{L_x}]$ and their spans cover its logarithmic length
   $\log x$, so one has $\log(b/d)\ge\log x/\tau(L_x)$. Its geometric mean may
   fall outside the window; since $b\le2d$, either it or its mirror has
   geometric mean in $[\sqrt{L_x}/(\sqrt2\,x),\sqrt{L_x}]\subset [x,\sqrt{L_x}]$
   with the same ratio, where $(\mathrm H_c)$ allows at most $\exp(-(c/\log
   x)(\tfrac12\psi(x)-\log x-\tfrac12\log2))$. Comparing exponents gives
   $c/2\le\log2+o(1)$. The page's "contains a consecutive pair" is loose for a
   pair whose span merely meets the window; the conclusion is unaffected (note,
   no correction). 14. Scale $x^m$: refutation-failed for fixed $m$. Agree; at
   $g=x^m$ the allowance is $x^{-mc/\log x}=e^{-cm}$, and products of $m$
   distinct primes in $(x/2^{1/m},x]$ put $\gg_m(x/\log x)^m$ divisors of $L_x$
   in $(x^m/2,x^m]$, so the mean logarithmic gap there is $\ll_m(\log x)^m/x^m$.
   For $m$ growing with $x$ the mean gap is far larger than $x^{-m}$ (at the
   top, $m\approx x/(2\log x)$ and $x^{-m}=e^{-x/2}$ against the mean gap
   $\exp(-(\log2+o(1))x/\log x)$), so "$m$ fixed" is needed; correction G4. 15.
   Known inputs fall far short: refutation-failed for the deductions. Agree.
   Granting Tenenbaum's admissibility statement, a consecutive pair $d<b$ of
   $L_x$ with $d$ in the window of index $k\le x$ has a divisor of $L_k\mid L_x$
   in $(d,(1+\varepsilon_k)d]$, so $\log(b/d)\le\varepsilon_k$; since
   $d>g/\sqrt2$ for $g=\sqrt{db}$, the profile
   $\delta(g)=2\varepsilon_{k(g/\sqrt2)}$ is nonincreasing and admissible for
   large $T$, with $\sigma(\ell)=(\log(2\ell)+O(1))^\beta-\log2$ at
   $\ell\approx\tfrac12\psi(k)$, and Lemma B's integral is of order $x/(\log
   x)^\beta$; a profile $\sigma\asymp(\log\ell)^2$ gives $x/(\log x)^2$
   likewise. The source statements are external and unread. The held Hughes
   conversion cites, for "the deduction on pp. 6–7 and Theorem 4 of [3]", "the
   corrections in [4]", where [3] is the 1987 paper and [4] is G. Tenenbaum,
   *Corrigendum: Sur un problème extrémal en arithmétique*, Ann. Inst. Fourier
   50 (2000), no. 1, 317–319. The required disclosure is warranted; corrections
   G1 and G2. 16. Linear descent against polylogarithmic: refutation-failed.
   Agree; $\sigma(\ell)=\kappa\ell-(1+\kappa)\log2$ for the profile of (18a.1),
   $(\log\ell)^\beta$ and $(\log\ell)^2$ up to constants for the inputs. 17.
   Description of the script: refutation-failed. Agree; read as it stood on that
   date: all divisors generated and sorted, the window filtered by
   floating-point logarithms, $\kappa$ computed, the minimum restricted to $\log
   g\ge2\log x$, and the largest $\log(b/d)$ in tenths of $[0,1]$ for $\log
   g/\log\sqrt{L_x}$. 18. The table: refutation-failed. Agree; every entry
   reproduced (Independent computation above), the restricted minimum at the
   same pair at every $x$. 19. The observations: refutation-failed as
   observations. Agree; the top-tenth maxima $2.77\cdot10^{-2}$ and
   $4.45\cdot10^{-5}$, the positions $\sqrt{L_x/db}\le2.58$, the single dip at
   $x=50$ are reproduced. The clause "the largest value the mean-gap bound
   allows" is true of the limiting constant and not of the finite bound, which
   allows $2.75$ at $x=20$ and $2.15$ at $x=64$; correction G6. 20. The rerun
   claim: refutation-failed. Agree on the output; the wall time was $7$ seconds
   for the reviewer and about fifteen seconds here with the environment start,
   so "a few seconds" is loose but of the right order (note, no correction). 21.
   The scope sentence: not a claim. Agree. 22. Consequential gap, $3/c$ or
   $2/c$, independence from the claimed chains: refutation-failed. Agree; item
   11 and the absence of any input from the Price or van Doorn claims. 23. The
   consequences of a disproof: refutation-failed. Agree; $(\mathrm H_c)$ holds
   at $x$ exactly when $c\le\kappa_{\min}(x)$, so $\kappa_{\min}\to0$ along a
   sequence excludes every fixed $c>0$ while leaving scale-dependent or
   exception-tolerant profiles open; the Tenenbaum clause is conditional on the
   unread statement. 24. Nothing about $n!$: refutation-failed. Agree. 25. Next
   step, the windowed computation: not a claim. Agree;
   $\tau(L_{100})=315\cdot2^{21}$ is confirmed. 26. Next step, Tenenbaum's
   method: not a claim. Agree; the corrigendum concerns that deduction according
   to Hughes; correction G8. 27. Factor-of-$e$ ranges: refutation-failed. Agree;
   $\int_{\ell}^{e\ell}d\ell'/(\kappa\ell')=1/\kappa=\log x/c$ and the range
   holds $\log x-\log\log x+O(1)$ such factors.

Connections sentences in scope: $h(L_x)\le\log_2L_x+1=(1/\log2+o(1))x$
(refutation-failed; $\log_2L_x=\psi(x)/\log2$); the Berend–Harmse Remark 2
characterization (consistent with Hughes's Remark 5 in the held conversion,
not checkable against the source); the "What it does not give" sentence
(refutation-failed; $(\mathrm H_c)$ gives $g^{-c/\log x}$, not $g^{-\eta}$);
the "Leads created" sentence (accurate description). Agree with each.

No verdict is changed.

## Corrections accepted

Numbered G1 to G8, each with the page, the location and the exact text to land.
"Lead" is `wiki/research/leads/lcm_divisor_gap_greedy_route/_index.md` and
"Connections" is `wiki/research/erdos_18/connections.md`, both as they stood on
the date above; quoted strings are given modulo line wrapping.

**G1** (the report's required correction 1, accepted as required). Lead,
section "Provisional premise", third bullet. Replace

> Tenenbaum's admissible sequences $\exp(-(\log k)^{\beta})$, $\beta<3/2$
> (his Théorème 1, read in the Numdam text layer, page images not read),
> give through Lemma B only $h(L_x)\ll_\beta x/(\log x)^{\beta}$;

with

> Tenenbaum's admissible sequences $\exp(-(\log k)^{\beta})$, $\beta<3/2$
> (his Théorème 1, read in the Numdam text layer, page images not read; the
> paper has a published corrigendum, Ann. Inst. Fourier 50 (2000), no. 1,
> 317–319, which Hughes cites for the deduction on pp. 6–7 and Theorem 4 and
> which was not read), give through Lemma B only
> $h(L_x)\ll_\beta x/(\log x)^{\beta}$;

Verified against the held Hughes conversion (item 15). The source-fidelity
rule of `docs/evidence.md` asks that a published correction be distinguished
and that a consumed result be identified with its version; a page that
consumes the 1987 statement from a garbled text layer while a held source
records a corrigendum to it must say so.

**G2** (the report's required correction 2, accepted as required with the
insertion moved inside the parenthesis, where the report's placement would
have broken the sentence). Connections, section "Problem 18, question (a),
along the least common multiples", item (18a.2), first sentence. Replace

> where the displayed formulas are garbled and the page images were not
> read)

with

> where the displayed formulas are garbled and the page images were not
> read; its corrigendum, Ann. Inst. Fourier 50 (2000), no. 1, 317–319, cited
> by Hughes for the deduction on pp. 6–7 and Theorem 4, was not read)

and, in the section "Sources read for this page", after its last sentence,
add

> The 2000 corrigendum to Tenenbaum's paper (Ann. Inst. Fourier 50, no. 1,
> 317–319), which Hughes cites for the deduction on pp. 6–7 and Theorem 4 of
> the 1987 paper, was not read.

**G3** (suggested correction 1, accepted). Lead, section "Route", Lemma B
bullet. Replace

> over the consecutive divisor pairs with geometric mean in $[T,\sqrt N]$
> gives

with

> over the consecutive divisor pairs with geometric mean in $[T,\sqrt N]$,
> with $\delta$ taking values in $(0,1/8]$, $T\ge2$ and $2T\le\sqrt N$, gives

Verified: the proof uses all three (item 5), and without the range of
$\delta$ the summary admits $\delta>1$, for which $\sigma<0$ and the displayed
bound is false. The report's insertion point, before "over the consecutive
divisor pairs", would read awkwardly; the clause is placed after the range.

**G4** (suggested correction 3, accepted), two places. Lead, section
"Provisional premise", second bullet: replace

> while at scale $x^m$ it allows gaps $e^{-cm}$

with

> while at scale $x^m$ with $m$ fixed it allows gaps $e^{-cm}$

Connections, paragraph "Scale of the hypothesis": replace

> at scale $x^m$ it allows gaps $e^{-cm}$

with

> at scale $x^m$ with $m$ fixed it allows gaps $e^{-cm}$

Verified in item 14.

**G5** (suggested correction 4, accepted), two places. Lead, section
"Provisional premise", first bullet: replace

> the comment's lower-range recurrence is the lower-range step of Lemma B

with

> the comment's lower-range recurrence is, up to the constant factor
> $2^{1+c/\log x}$, the lower-range step of Lemma B

Connections, paragraph "The comment's form of the hypothesis, and where it
fails": replace

> is exactly the lower-range step of Lemma B

with

> is, up to a constant factor, the lower-range step of Lemma B

Verified in item 11: the step with the profile of (18a.1) is
$R'\le2^{1+\kappa}R^{1-\kappa}$, $\kappa=c/\log x$.

**G6** (suggested correction 5, accepted for the lead with the finite bound
made explicit and its values corrected; the connections page carries no
clause "the largest value the mean-gap bound allows", so the report's second
half has nothing to apply to). Lead, section "Exploratory computation".
Replace

> approaches $2\log2=1.386\ldots$ from below, the largest value the mean-gap
> bound allows; this was observed after the fact, not predicted.

with

> approaches $2\log2=1.386\ldots$ from below, the largest value the mean-gap
> bound allows in the limit (its finite form,
> $\kappa_{\min}(x)\le(\log x)\log(\tau(L_x)/\log x)/\log(\sqrt{L_x}/(\sqrt2\,x))$,
> only forces $\kappa_{\min}(x)\le2.75$ at $x=20$ and
> $\kappa_{\min}(x)\le2.15$ at $x=64$); this was observed after the fact, not
> predicted.

Verified by the independent computation: the finite bound is $2.748$ at
$x=20$ and $2.154$ at $x=64$, so the report's "$2.2$–$2.7$" misstates both
ends by rounding; the bound follows from item 13 at finite $x$ with
$\log(1/\log(b/d))\le\log(\tau(L_x)/\log x)$ and
$\log g\ge\log(\sqrt{L_x}/(\sqrt2\,x))$ at the pair found.

**G7** (suggested correction 6, accepted). Lead, section "Exploratory
computation". Replace

> the largest $\log(b/d)$ in each tenth of the range of
> $\log\sqrt{db}/\log\sqrt{L_x}$

with

> the largest $\log(b/d)$ in each tenth of $[0,1]$ for
> $\log\sqrt{db}/\log\sqrt{L_x}$

Verified against the script (item 17); the two quoted maxima are the same
under either reading, the values at $x=30,40$ are not.

**G8** (suggested correction 9, accepted). Lead, section "Next step", second
sentence. Replace

> his displays (6)–(8))

with

> his displays (6)–(8), read together with the 2000 corrigendum)

Verified: Hughes cites the corrigendum for the deduction the next step would
follow (item 15); the pointer follows from G1.

## Corrections rejected

- Suggested correction 2 ("Three facts about it are established on the
  connections page" to "Two facts ... proved ..., and a third rests on a
  text-layer reading of two sources not held"): rejected. The third bullet
  itself marks its inputs as a text-layer reading of a paper not held, and
  G1 adds the corrigendum to the same bullet; "established on the
  connections page" has the true reading that the three facts are set out
  there with the standing of their inputs marked. Optional wording.
- Suggested correction 7 (frontmatter `desc`, "at the mean-gap scale" to
  "that reaches the mean-gap scale at the top of its range"): rejected. The
  `desc` is a summary; the body states exactly where $(\mathrm H_c)$ is at
  the mean-gap scale and where it asks less, and the phrase is true of the
  range where the hypothesis binds and where the computation finds the
  minimizers. Optional wording.
- Suggested correction 8 (windows at sampled scales bound $\kappa_{\min}(x)$
  from above only unless they tile $[x,\sqrt{L_x}]$): rejected as a
  correction. The sentence is a plan, not a mathematical claim; the caveat
  is correct and may be added at the author's discretion.

Notes carried without a correction: the loose "contains a consecutive pair"
of item 13; the runtime "in a few seconds" of item 20; the report's inexact
description of the connections extraction and its superfluous branch name
(Subject above).

## Outcome

- [[research/leads/lcm_divisor_gap_greedy_route/_index|lcm_divisor_gap_greedy_route]]:
  review_status **reviewed**. Every statement the route rests on is
  refutation-failed: Lemma A, Hughes's Lemma 4 with facts (i) and (ii),
  Lemma B, and the transfer (18a.1), each re-derived here; the one remaining
  premise, $(\mathrm H_c)$, is stated as an unproved hypothesis throughout,
  with the necessary bound $c\le2\log2+o(1)$ refutation-failed. The accepted
  corrections G1 to G8 are disclosures and precision repairs to sentences
  the route does not rest on; none touches the proved part or the premise.
  The exploratory computation carries no evidence, as the lead says.
- research_state **ready**: the lead names a bounded next investigation (the
  windowed enumeration toward $x$ near $100$, and the attack on
  $(\mathrm H_c)$ near the middle by Tenenbaum's method) whose inputs are
  available (the retained script; the open-access paper and its corrigendum);
  the missing $(\mathrm H_c)$ is the lead's consequential gap, not a
  prerequisite of that investigation.

No tier is assigned and no problem status changes.
