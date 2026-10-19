---
name: research/erdos_18/evidence/verify/lead_lcm_divisor_gap_greedy_route_rereview
title: "Independent re-review of the lead lcm_divisor_gap_greedy_route and its connections section"
desc: |
  Blind refutation re-review, on 2026-10-02, of the lead
  lcm_divisor_gap_greedy_route and, on the connections page, Lemmas A and B with
  the Problem 18 question (a) section: every mathematical statement re-derived
  and the x <= 64 computation reproduced by an independent route; no statement
  refuted, the conclusion conditional on the unproved hypothesis (H_c); one
  required source disclosure (the 2000 corrigendum to Tenenbaum 1987), several
  suggested precision corrections.
created: 2026-10-02T17:14:37Z
updated: 2026-10-02T17:14:37Z
---

***

## Subject and independence

The reviewer acted as an independent reviewer in a fresh context, model
Claude Fable 5.1, given only the commissioning assignment, and took no part
in writing the lead page, the connections page or any reconstruction page of
the folder. The charge was refutation: of every mathematical statement the
lead's route rests on, and of every claim the lead makes about its
computation, its premises, its consequential gap and its next step.

Subject: the tree as it stood on 2026-10-02, read from a blind extraction kept
outside the repository and frozen on that date: the lead page
`wiki/research/leads/lcm_divisor_gap_greedy_route/_index.md` with its
review-status fields and its "Current review" section removed, and the
connections page `wiki/research/erdos_18/connections.md` with its review-report
sentences cut. Scope: the whole lead page; on the connections page the shared
Lemma A and Lemma B, the section "Problem 18, question (a), along the least
common multiples", the sentence about this lead under "Leads created" and the
source list. The other sections of the connections page were in the extraction
and were read, not reviewed.

A first attempt at this re-review, whose extraction carried the earlier
verdicts, was stopped before completion and its output discarded; this record is
from a blind extraction frozen on 2026-10-02 and kept outside the repository.

Also read from the tree of that date, mathematics only:

- `wiki/research/erdos_18/hughes_lemma_4_reconstruction.md`, Definitions
  through the factorial ratio proof (lines 32–111), in full.
- `wiki/research/erdos_18/hughes_theorem_1_reconstruction.md`, Definitions
  through Gaps and qualifications (lines 36–325), in full, for facts (i) and
  (ii) and the charging integral that Lemma B generalizes.
- `wiki/research/erdos_18/hughes_corollary_3_reconstruction.md`,
  Definitions through Statement (lines 31–104), for the windows and
  $\varepsilon_j$.
- `wiki/research/erdos_18/_index.md`, "What the folder holds" (lines
  64–105).
- `wiki/problems/divisors/E0018/_index.md`, the statement block through the
  Formalization paragraph (lines 15–118); the Current assessment was not
  read.
- The Hughes source folder under `library/divisors/`, named
  `hughes_2026_sums_distinct_divisors_factorials`: its result page
  `lemma_4.md` and the canonical conversion beside the held PDF, read for
  Section 1, Lemma 4 with its proof, the opening of Section 3, Remarks 5
  and 7, and the reference list.
- `wiki/research/leads/lcm_divisor_gap_greedy_route/evidence/_index.md` and
  `evidence/util/gap_profile.py`, as they stood on the frozen date,
  opened only after the independent computation described below had been
  written and run.
- The guidance pages of `wiki/` named by the assignment, for this record's
  form.

Not read: the live lead page and the live connections page; the Current
assessment of any problem page; the frontmatter, Source and Standing blocks
of the reconstruction pages; every file under any `evidence/verify/` folder,
with one exposure: to copy the frontmatter shape and the section skeleton,
the first 22 lines and the heading lines of the Problem 859 review record in
this folder were printed, and its `desc` carries that record's verdict
summary for the Problem 859 section, which has no transfer to this route.
Nothing in this record could have come from it and no attack direction
followed it. Tenenbaum (1987) and Berend–Harmse (1993) are not held and were
not read; the lead's statements about them are checked only for internal
consistency and against what the held Hughes conversion says second-hand.

Independence of the computation: the recomputation was designed and run before
the author's script was opened. It differs from the author's route in its window
test (exact integer comparisons $x^2\le db\le L_x$ against the author's
floating-point logarithms), in a 50-digit decimal recheck of every extremal
pair, and in a consecutiveness check of each binding pair by a pruned
depth-first search over the prime powers of $L_x$, which enumerates and sorts
nothing. The scripts were scratch work and are not retained; the witnesses they
produced and a compact rerunnable certificate are in the Notes, and the author's
stated rerun was performed verbatim from the tree of the frozen date.

## Restatement

Target. Problem 18, question (a): are there infinitely many practical $m$
with $h(m)<(\log\log m)^{O(1)}$, where $m$ is practical if every $1\le n<m$
is a sum of distinct divisors of $m$ and $h(m)$ is the least number of
distinct divisors that always suffice. The connections page's $h$ ranges over
$1\le m\le N$ with a fresh set for each $m$ and dominates the site's, so its
upper bounds hold for the site's $h$.

The route, in the reviewer's words, with $L_x=\mathrm{lcm}(1,\dots,x)$.

(A) For every $x\ge1$, consecutive divisors of $L_x$ have ratio at most $2$;
hence, by Lemma 4, $L_x$ is practical, the greedy expansion of every
$1\le m\le L_x$ uses distinct divisors, and $h(L_x)\le\log_2L_x+1$.

(B) Let $N$ have the ratio-two property, let $T\ge2$ with $2T\le\sqrt N$,
and let $\delta\colon[T,\sqrt N]\to(0,1/8]$ be nonincreasing with
$\log(b/d)\le\frac12\delta(\sqrt{db})$ for every pair of consecutive
divisors $d<b$ of $N$ with $T\le\sqrt{db}\le\sqrt N$. With
$\sigma(\ell)=\log(1/\delta(e^\ell/2))$ on $[\log(2T),\frac12\log N]$,

$$
h(N)\le3\int_{\log(2T)}^{\frac12\log N}\frac{d\ell}{\sigma(\ell)}
+\log_2\sigma\bigl(\tfrac12\log N\bigr)+2\log_2(2T)+5 .
$$

(H$_c$) There are $c>0$ and $x_0$ such that for every $x\ge x_0$ and every
pair of consecutive divisors $d<b$ of $L_x$ with $x\le\sqrt{db}\le\sqrt{L_x}$,
$\log(b/d)\le(db)^{-c/(2\log x)}$.

(18a.1) If (H$_c$) holds, then, after decreasing $c$ to at most $4$ if
necessary, $h(L_x)\le(3/c+o(1))(\log x)^2=(3/c+o(1))(\log\log L_x)^2$ as
$x\to\infty$; so (H$_c$) answers question (a) with exponent $2$ along $L_x$.

Side statements reviewed: the site comment's form of the hypothesis fails
for $Y$ near $L_x/k$ with $k$ bounded and the lower-half form is what the
greedy count needs; counting divisors in $[\sqrt{L_x}/x,\sqrt{L_x}]$ forces
$c\le2\log2+o(1)$; Tenenbaum's admissible sequences give through (B) only
$h(L_x)\ll_\beta x/(\log x)^\beta$ for $\beta<3/2$; the finite profile
$\kappa_{\min}(x)$ for $x\le64$ and the claims about it; the consequences of
a proof or a disproof of (H$_c$); the next computational and analytic step.

## Checklist

- **Quantifiers and scope.** (H$_c$) is for every $x\ge x_0$ and every pair
  in the window, with no exceptional pair; (18a.1) is eventual in $x$, which
  is what question (a) needs. The window $[x,\sqrt{L_x}]$ of (H$_c$) covers
  Lemma B's domain $[T,\sqrt{L_x}]$ with $T=x^{4/c}$ exactly when $c\le4$,
  and (H$_c$) implies (H$_{c'}$) for $c'<c$ since $\sqrt{db}\ge x\ge1$, so
  the reduction of $c$ is legitimate. The lead claims nothing for pairs above
  $\sqrt{L_x}$ and says that a profile tolerating exceptional pairs is open.
  One implicit quantifier, $m$ fixed in "at scale $x^m$", is a suggested
  correction. Pass.
- **Circularity.** None. (H$_c$) is carried as a hypothesis throughout and
  nowhere assumed proved; Lemma B's proof uses only Lemma 4 and facts (i)
  and (ii). Pass.
- **Model and convention changes.** The $h$ over $1\le m\le N$ dominates the
  site's $h$ over $m<N$; Lemma B replaces Theorem 1's factorial windows by a
  general profile and its two symmetry facts hold for every $N$;
  $\kappa(d,b)$ is exactly the largest $c$ at which (H$_c$) holds at the
  pair (checked by rearranging the inequality, which needs
  $\log(b/d)<1$, true by (A)). Pass.
- **Finite and statistical overreach.** The computation is labeled as
  proving nothing, and "approaches $2\log2$ from below" is an observation on
  six points marked as made after the fact. The finite-$x$ form of the
  counting bound allows $\kappa_{\min}(x)$ up to about $2.2$–$2.7$ in this
  range (Notes), so the nearness to $1.386$ is not forced at these $x$; a
  suggested wording. Pass.
- **Uniformity.** The $o(1)$ of (18a.1) depends on $c$ through the
  $O(\log x/c)$ terms and the threshold $x_0$ of (H$_c$) depends on $c$;
  both are visible in the proof. The Tenenbaum-based bound is $\ll_\beta$.
  No uniformity over a family is asserted from finitely many instances.
  Pass.
- **Extremal conclusions.** $\kappa_{\min}(x)$ is recomputed in the claim's
  own units (exact window, the stated formula, 50-digit recheck of the
  minimizers), and the necessary condition $c\le2\log2+o(1)$ is an infimum
  statement re-derived below. Pass.
- **Consequences and composition.** Each "hence" was attacked separately:
  practicality and $h(L_x)\le\log_2L_x+1$ from the ratio property; $c\le
  2\log2+o(1)$ from the pair count; "(18a.1) as stated gives nothing along
  a sequence with $\kappa_{\min}\to0$"; "a result near $\sqrt{L_x}$ alone
  covers $O(\log x)$ of the count". The composition (18a.1) consumes the
  ratio property, Lemma 4, facts (i) and (ii), all proved on the pages and
  re-derived here, and (H$_c$), which is stated as the hypothesis and never
  dropped. Pass.
- **Computation.** Inputs and formula are stated exactly; the author's
  window test compares floating-point logarithms, and at $x=20$ the binding
  pair has $db=L_x$ exactly, on the boundary (included by both routes); the
  script has no failing input by design and says so. The printed numbers
  are right. Pass, with the boundary fragility noted.
- **Reproduction.** The evidence index's command was rerun verbatim from the
  repository root, the tree as it stood on the frozen date: 7 seconds wall time, output equal to
  the lead's table and to its quoted top-tenth gaps. "Prints in a few
  seconds" holds. Pass.
- **Source and verdict fidelity.** Lemma 4 as reconstructed matches the held
  Hughes conversion word for word; facts (i) and (ii) match the Theorem 1
  reconstruction; the characterization of Berend–Harmse's Remark 2 matches
  Hughes's own Remark 5 second-hand; the bibliographic data of Tenenbaum
  (1987) match Hughes's reference [3]. Hughes's reference [4] is a published
  corrigendum to that paper (2000), cited for the deduction and Theorem 4
  from which the factorial gap input comes; the lead and the connections
  page do not mention it. Required disclosure below. The statements of
  Tenenbaum and Berend–Harmse themselves could not be checked here, and the
  lead's report of the problem page's assessment is outside the read set.
  Pass within the read set, with the required disclosure.

## Weakest steps

**1. The upper range of Lemma B.** For $\sqrt N<R\le N/(2T)$ put $U=N/R\in
[2T,\sqrt N)$. The bracketing divisors $d<R<b$ have $b\le2d$, so
$R/\sqrt2<\sqrt{db}<\sqrt2R$; fact (ii) ($b>R>\sqrt N$ gives $N/b<\sqrt N<b$,
so $N/b\le d$, so $db\ge N$) places the mirror pair's geometric mean
$N/\sqrt{db}$ in $(U/\sqrt2,\sqrt2U)\cap[\,\sqrt2T,\sqrt N\,]$, inside the
hypothesis's domain, and $\delta$ nonincreasing with $U/2\ge T$ gives
$\log(b/d)\le\frac12\delta(U/2)$. Lemma 4 at $R$ gives $R'\le2R\log(b/d)\le
R\,\delta(U/2)$, so $\log U'\ge\log U+\sigma(\log U)$. On $J_k=\{\ell:2^k\log8
\le\sigma(\ell)<2^{k+1}\log8\}$, an interval since $\sigma$ is nondecreasing,
consecutive starts are at least $2^k\log8$ apart, so a run of $M$ starts has
$(M-1)2^k\log8\le|J_k|$, while $\int_{J_k}d\ell/\sigma>|J_k|/(2^{k+1}\log8)$;
hence $M\le1+2\int_{J_k}d\ell/\sigma$. The number $K$ of nonempty $J_k$ is
at most $\log_2(\sigma(\frac12\log N)/\log8)+1$ because $\sigma\le
\sigma(\frac12\log N)$ on the range. With the lower range's $1+\int$ (the
charging integral: $\sigma\le\sigma(\log R)$ on $[\log R',\log R]$ gives
$\int\ge1$ per step, intervals disjoint, at most one crossing $\log(2T)$),
two endgames of at most $\log_2(2T)+1$ halving steps each, and the terminal
divisor, the total is $3\int+\log_2\sigma(\frac12\log N)+2\log_2(2T)+5-
\log_2\log8$, below the stated bound. Lemma B holds as stated.

**2. The transfer (18a.1).** With $T=x^{4/c}$ and $\delta(g)=2g^{-c/\log x}$:
$\delta\le2e^{-4}<1/8$ on $[T,\sqrt{L_x}]$; $T\ge x\ge2$ and $2T\le
\sqrt{L_x}$ for large $x$ since $\log L_x=\psi(x)\sim x$; (H$_c$) is
exactly Lemma B's hypothesis, as $\frac12\delta(\sqrt{db})=(db)^{-c/(2\log
x)}$; with $\kappa=c/\log x$, $\sigma(\ell)=\kappa\ell-(1+\kappa)\log2\ge
\kappa\ell-2$ for large $x$; $\kappa\log(2T)-2=2+\kappa\log2\ge2$; so the
integral is at most $\kappa^{-1}\log\bigl((\kappa x-2)/2\bigr)\le(\log x/c)
\log(cx/\log x)\le(\log x)^2/c$ once $x\ge e^c$, using $\frac12\log L_x\le
x$. The remaining terms are $O(\log x)$ and $O(\log x/c)$, and $\log\log
L_x=\log x+\log(\psi(x)/x)=\log x+o(1)$. The statement follows exactly as
written.

**3. The necessary condition $c\le2\log2+o(1)$.** $\log\tau(L_x)=\sum_{p\le
x}\log(\lfloor\log x/\log p\rfloor+1)$; the primes in $(\sqrt x,x]$ each
contribute $\log2$ and number $(1+o(1))x/\log x$, the primes up to $\sqrt x$
contribute $O(\sqrt x\log\log x/\log x)$, so $\log\tau(L_x)=(\log2+o(1))x/
\log x$. The consecutive pairs meeting the window $[\sqrt{L_x}/x,\sqrt{L_x}]$
number fewer than $\tau(L_x)$ and their log-spans cover a length $\log x$,
so one has $\log(b/d)\ge\log x/\tau(L_x)=\exp(-(\log2+o(1))x/\log x)$. That
pair may straddle an end of the window; since $b\le2d$, either it or its
mirror has geometric mean in $[\sqrt{L_x}/(\sqrt2\,x),\sqrt{L_x}]\subset
[x,\sqrt{L_x}]$ with the same ratio, where (H$_c$) allows at most
$\exp(-(c/\log x)(\frac12\psi(x)-\log x-\frac12\log2))=\exp(-(c/2+o(1))x/
\log x)$. Hence $c/2\le\log2+o(1)$. Holds as stated.

## Strongest attack

The route's conclusion is conditional, so the attack with the largest payoff
was a disproof of (H$_c$) for every $c>0$, which would leave (18a.1) empty.
Three directions were tried. First, structurally forced large gaps: near
$L_x/k$ for bounded $k$ the divisors are $L_x/j$ for integers $j$ near $k$,
with gaps of order $L_x/k^2$, and this is exactly where the site comment's
all-$Y$ form fails; but these pairs have geometric mean above $\sqrt{L_x}$
and their mirrors sit near $k\le x$, where gaps are $1$, so (H$_c$) is not
touched. Second, the pigeonhole bound above, which only gives $c\le2\log2+
o(1)$; its finite-$x$ form gives $\kappa_{\min}(x)\le2.15$ at $x=64$ and
$\le1.59$ at $x=10^4$ (Notes), far from the observed $1.36$ and from $0$. No
scale below the top forces anything: at $g=x^m$ with $m$ fixed the divisors
of $L_x$ in $[g/e,g]$ number at least $\gg_m(x/\log x)^m$ (products of $m$
primes in $(x/2,x]$ chosen so that the last prime's interval meets
$(\sqrt x,x]$), so the mean gap is $x^{-m}$ up to a power of $\log x$ while
(H$_c$) allows $e^{-cm}$. Third, the computation: an independent
enumeration with exact window tests, a pruned depth-first consecutiveness
check of each minimizer, 50-digit recomputation of $\kappa$ at the
minimizers, and direct inequality controls at $c=\kappa_{\min}(1\pm10^{-6})$
(the pair satisfies (H$_c$) at the lower $c$ and violates it at the higher
one) all agree with the author's table. The attack failed: (H$_c$) is
unproved and unrefuted, and the lead presents it as exactly that.

On the proved part, the sharpest attack was on the domains inside Lemma B
(the mirror pair's geometric mean below $T$, or $R/2$ and $U/2$ outside the
domain of $\delta$); each is excluded by $R\ge2T$, $U\ge2T$ and facts (i) and
(ii), as re-derived above.

## Premises

- **Local claims.** No `L`-claim is consumed; dependency item (e) is
  inapplicable. The route consumes author-recorded research pages: Lemma A
  and Lemma B on the connections page, Lemma 4 and facts (i) and (ii) on the
  Hughes reconstruction pages. Each was re-derived here from first
  principles, so the verdicts do not rest on their standing text, which was
  not read.
- **Hughes (2026), Lemma 4.** Held; statement read on the canonical
  conversion and on the result page; the inequality $R-d\le2R\log(b/d)$ was
  re-proved ($b-d=d(b/d-1)\le R(b/d-1)$ and $t-1\le2\log t$ on $[1,2]$).
  Reading depth: proof verified.
- **Prime number theorem.** $\psi(x)\sim x$ and $\pi(x)\sim x/\log x$, used
  for $\log L_x\sim x$, $\log\log L_x=\log x+o(1)$ and $\log\tau(L_x)$.
  Standard, assumed.
- **Tenenbaum (1987).** Ann. Inst. Fourier 37, no. 2, 1–18; not held, not
  read here. Interface: for $\beta<3/2$ and large $k$, every $z\in
  (\sqrt{L_{k-1}},\sqrt{L_k}]$ has a divisor of $L_k$ in $(z,(1+\varepsilon_k)
  z]$ with $\varepsilon_k=\exp(-(\log k)^\beta)$. Granting it, the deduction
  $h(L_x)\ll_\beta x/(\log x)^\beta$ through Lemma B is correct: divisors of
  $L_k$ divide $L_x$ for $k\le x$, so a consecutive pair of $L_x$ with $d$ in
  the window of index $k$ has $\log(b/d)\le\varepsilon_k$; taking $\delta(g)
  =2\varepsilon_{k(g/\sqrt2)}$, nonincreasing since $\varepsilon_k$
  decreases, gives $\sigma(\ell)=(\log(2\ell)+O(1))^\beta-\log2$ and an
  integral of order $x/(\log x)^\beta$. The lead consumes this only for
  "known inputs fall far short" and "the route's best bound without
  (H$_c$)". Hughes cites a corrigendum to this paper (Ann. Inst. Fourier
  50 (2000), no. 1, 317–319) for the deduction on pp. 6–7 and Theorem 4;
  neither the paper nor the corrigendum was read, and the lead does not
  mention the corrigendum.
- **Berend–Harmse (1993).** Not held, not read. Interface: their statement
  that the factorial method does not apply to $L$ (p. 572) and Remark 2;
  the latter matches Hughes's second-hand Remark 5. Not load-bearing.
- **The site comment of 14 September 2026.** Not read; its form
  $\Delta_x(Y)+1\le Y^{1-c/\log x}$ is taken as the lead quotes it, and the
  refutation of that form is checked as mathematics.
- **The explicit hypothesis (H$_c$).** Unproved. Necessary: $c\le2\log2+
  o(1)$. Consistent with every $x\le64$, where $\kappa_{\min}(x)\in[1.11,
  1.36]$. No known input approaches it: every known profile has $\sigma$
  polylogarithmic in $\ell$ where (H$_c$) needs $\sigma=c\ell/\log x-O(1)$.

The premises that remain unproved are (H$_c$), the only mathematical
hypothesis of the route, and, as external facts rather than hypotheses, the
two text-layer source statements. The route as written stands on (H$_c$)
alone: the proved part turns (H$_c$) into the exponent-$2$ bound, and
without (H$_c$) the route gives nothing beyond the Tenenbaum-conditional
$x/(\log x)^{3/2-\eta}$, which is not of the shape question (a) asks for.

## Statement verdicts

Lead page sections are named first; the connections page carries the same
mathematics in its "Shared lemmas" and "Problem 18, question (a)" sections,
and each verdict applies to both texts.

1. *Target and status evidence*, the whole paragraph. Not a mathematical
   claim. Question (a) and the definition of $h$ match the problem page's
   statement block; the two site claims with exponent $2$ and the OPEN
   label appear in that block's Status paragraph; the assessment and Vose's
   bound are outside the read set.
2. *Route*, "$\log L_x=\psi(x)\sim x$ and $\log\log L_x=\log x+o(1)$".
   Refutation-failed; prime number theorem.
3. *Route*, "Erdős named $L_x$ ... (Tenenbaum 1987, p. 2)" and "the site's
   discussion of 14 September 2026 proposes ...". Not a mathematical claim;
   both sources outside the read set.
4. *Route*, Lemma A as summarized, and connections "Lemma A" with proof.
   Refutation-failed; re-derived: for $d\mid N$, $d<N$, $q=N/d$ even gives
   $2d\mid N$; $q$ odd gives an odd prime $p\mid q$ with $2^c<p<2^{c+1}$,
   $v_2(d)=v_2(N)\ge c$, and $d'=dp/2^c\mid N$ with $d<d'<2d$;
   $v_2(L_x)=\lfloor\log_2x\rfloor\ge\lfloor\log_2p\rfloor$. The consequence
   (nonterminal remainders halve, so at most $\lfloor\log_2m\rfloor$ of
   them plus one terminal divisor) holds.
5. *Route*, Lemma B as summarized, and connections "Lemma B" with proof.
   Refutation-failed (Weakest step 1). The lead's summary omits the
   hypotheses $\delta\le1/8$, $T\ge2$ and $2T\le\sqrt N$ that the proof uses;
   suggested correction.
6. *Route*, "it is the step count of Hughes's Theorem 1 with the factorial
   windows replaced by a profile, using only Lemma 4 and the mirror symmetry".
   Refutation-failed; checked against the Theorem 1 reconstruction: facts
   (i) and (ii) and Lemma 4 are the only inputs; Lemma B's upper range is
   partitioned dyadically in $\sigma$ rather than in window index, the same
   device at a different grain.
7. *Route*, the hypothesis (H$_c$), and *Exploratory computation*,
   "$\kappa(d,b)$ ... the largest $c$ for which (H$_c$) holds at that pair".
   Refutation-failed; $\log(b/d)\le g^{-c/\log x}$ with $g=\sqrt{db}$ is
   equivalent to $c\le(\log x)\log(1/\log(b/d))/\log g$ since $0<\log(b/d)
   \le\log2<1$.
8. *Route*, "Conclusion (author-recorded; conditional on (H$_c$))", the
   display, and connections (18a.1) with proof. Refutation-failed as a
   conditional statement (Weakest step 2); its antecedent is unproved and
   the text says so.
9. *Route*, "which answers question (a) with exponent $2$ along $L_x$".
   Refutation-failed as a conditional: under (H$_c$) the $L_x$ are
   infinitely many practical $m$ with $h(m)\le(3/c+o(1))(\log\log m)^2$.
10. *Provisional premise*, "The comment's form fails in the top range", and
    connections "The comment's form of the hypothesis, and where it fails".
    Refutation-failed; at $Y=L_x$ the pair $(L_x/2,L_x)$ is consecutive by
    (A) and gives $\Delta_x(L_x)+1\ge L_x/2$ against $L_x e^{-c\psi(x)/\log
    x}=o(L_x)$; for $Y\in(L_x/2+2L_x^{1-c/\log x},L_x]$ the gap below $Y$ is
    at least $2L_x^{1-c/\log x}-1>Y^{1-c/\log x}$; near $L_x/k$ the
    consecutive divisors $L_x/(k+1)<L_x/k<L_x/(k-1)$ have gaps of order
    $L_x/k^2$.
11. *Provisional premise*, "the lower-half form is what the greedy count
    needs, because the mirror symmetry handles the upper half; the comment's
    lower-range recurrence is the lower-range step of Lemma B", and
    connections "the comment's recurrence $R'\le R^{1-c/\log x}$ is exactly
    the lower-range step ... gives $1/c$ there; the mirror recurrence gives
    another $1/c$ ... only the factor $3/2$ ... is a bookkeeping loss".
    Refutation-failed. The lower-range step with this $\delta$ is $R'\le
    2^{1+\kappa}R^{1-\kappa}$, the comment's recurrence up to a constant
    factor; iterating it from $\frac12\log L_x$ down to $\log(2T)$ takes
    $(1+o(1))(\log x)^2/c$ steps, and the mirror recurrence $\log U'\ge
    (1+\kappa)\log U-(1+\kappa)\log2$ takes $(1+o(1))(\log x)^2/c$ steps
    (substitute $v=\log U-(1+\kappa)\log2/\kappa$, which stays positive on
    the range), so the direct count is $(2/c+o(1))(\log x)^2$ and Lemma B's
    $3/c$ loses only the factor $2$ in its upper-range dyadic count. The word
    "exactly" is loose by the constant factor; suggested correction.
12. *Provisional premise*, "$\log\tau(L_x)=(\log2+o(1))x/\log x$".
    Refutation-failed (Weakest step 3).
13. *Provisional premise*, "the window $[\sqrt{L_x}/x,\sqrt{L_x}]$ contains a
    consecutive pair with $\log(b/d)\ge\exp(-(\log2+o(1))x/\log x)$, so
    (H$_c$) forces $c\le2\log2+o(1)$", and the connections "Scale of the
    hypothesis" through "necessarily $c\le2\log2+o(1)$". Refutation-failed
    (Weakest step 3); the pair found may straddle an end of the window, and
    the mirror argument closes that gap without changing the conclusion.
14. *Provisional premise*, "with $c$ near $2\log2$ it is at the mean-gap
    scale near $\sqrt{L_x}$ ... while at scale $x^m$ it allows gaps $e^{-cm}$
    of constant size against a mean gap of order $x^{-m}$ up to powers of
    $\log x$". Refutation-failed for fixed $m$ (Strongest attack, second
    direction); for $m\to\infty$ the mean gap exceeds $x^{-m}$ by a factor
    $e^{(1+o(1))m\log m}$, not a power of $\log x$. Suggested correction:
    say "$m$ fixed".
15. *Provisional premise*, "Known inputs fall far short": Tenenbaum's
    sequences give through Lemma B only $h(L_x)\ll_\beta x/(\log x)^\beta$;
    Berend and Harmse state their method does not apply to $L$; a bound of
    their strength would give $x/(\log x)^2$; and connections (18a.2).
    Refutation-failed for the deductions (Premises); the two source
    statements are external and unread here, and the 2000 corrigendum is
    undisclosed. Required correction.
16. *Provisional premise*, "(H$_c$) has a linear descent $\sigma(\ell)=
    c\ell/\log x$ where every known input has a polylogarithmic one".
    Refutation-failed; $\sigma(\ell)=\kappa\ell-(1+\kappa)\log2$ for the
    profile of (18a.1), and the Tenenbaum and Berend–Harmse profiles are
    $(\log\ell)^\beta$ and $(\log\ell)^2$ up to constants.
17. *Exploratory computation*, the description of what the script computes.
    Refutation-failed; checked against the committed script: it enumerates
    all divisors, filters the window by logarithms, computes $\kappa$, the
    restricted minimum over $\sqrt{db}\ge x^2$ and the largest $\log(b/d)$ in
    each tenth of $[0,1]$ for $\log\sqrt{db}/\log\sqrt{L_x}$.
18. *Exploratory computation*, the table ($\tau(L_x)$, $\log L_x$,
    $\kappa_{\min}$, $\kappa_{\min}$ over $\sqrt{db}\ge x^2$) and the
    connections' list of six values. Refutation-failed; every entry
    reproduced by the independent route to the printed precision, the
    restricted minimum attained at the same pair as the full one at every
    $x$ (Notes).
19. *Exploratory computation*, "the largest $\log(b/d)$ in the top tenth
    falls from $2.8\cdot10^{-2}$ at $x=20$ to $4.5\cdot10^{-5}$ at $x=64$",
    "the binding pairs sit at the top of the range, within a factor of about
    $2.6$ of $\sqrt{L_x}$", "shows no downward trend ... dips once, from
    $1.311$ at $x=40$ to $1.298$ at $x=50$", "approaches $2\log2$ from
    below, the largest value the mean-gap bound allows". Refutation-failed
    as observations: top-tenth maxima $2.77\cdot10^{-2}$ and $4.45\cdot
    10^{-5}$, decreasing through the sample; $\sqrt{L_x/db}$ at the
    minimizers $1.00,1.88,1.23,2.58,1.15,1.12$; the one dip is at $x=50$.
    The clause "the largest value the mean-gap bound allows" is true only
    in the limit; suggested correction.
20. *Exploratory computation*, "Run from the repository root with the
    arguments ... it prints in a few seconds". Refutation-failed; rerun
    verbatim, 7 seconds.
21. *Exploratory computation*, "can only begin to distinguish ... cannot
    prove (H$_c$) ... far from asymptotic ... not evidence for any claim".
    Not a mathematical claim; a correct scope statement.
22. *Consequential gap*, "A proof for any $c>0$ gives exponent $2$ ... with a
    constant $3/c$ (or $2/c$ when the upper range is counted by the
    recurrence on $U=L_x/R$ ...), independently of the claimed chains".
    Refutation-failed; $3/c$ is (18a.1) and $2/c$ is item 11; the route
    uses nothing from the Price or van Doorn claims.
23. *Consequential gap*, "A disproof, a sequence of $x$ along which
    $\kappa_{\min}(x)\to0$, would show that no hypothesis of the form (H$_c$)
    with a fixed $c$ holds, so (18a.1) as stated gives nothing along that
    sequence; whether a scale-dependent profile, or one that tolerates a few
    exceptional pairs, still gives $(\log x)^2$ through Lemma B would remain
    open, with Lemma B's $x/(\log x)^{3/2-\eta}$ from Tenenbaum's input the
    route's best bound without (H$_c$)". Refutation-failed; (H$_c$) holds at
    $x$ exactly when $c\le\kappa_{\min}(x)$, so $\kappa_{\min}(x_j)\to0$
    excludes every fixed $c>0$; the last clause is conditional on the unread
    Tenenbaum statement.
24. *Consequential gap*, "Neither outcome bears on $n!$ or on questions (b)
    and (c)". Refutation-failed; nothing in the route concerns $n!$.
25. *Next step*, the windowed enumeration to $x$ near $100$. Not a
    mathematical claim. Apt: $\tau(L_{100})=315\cdot2^{21}\approx6.6\cdot
    10^8$. Caveat for the Notes: windows at sampled scales give only upper
    bounds on $\kappa_{\min}(x)$ unless they tile $[x,\sqrt{L_x}]$.
26. *Next step*, "attempt (H$_c$) near the middle with Tenenbaum's method
    (... his displays (6)–(8))". Not a mathematical claim; source unread;
    the corrigendum concerns that deduction according to Hughes.
27. *Next step*, "every factor-of-$e$ range of $\ell=\log(2g)$ contributes
    $\log x/c$ to the integral of Lemma B, so a result near $\sqrt{L_x}$
    alone covers only $O(\log x)$ of the $(\log x)^2$ count".
    Refutation-failed; $\int_{\ell_0}^{e\ell_0}d\ell/(\kappa\ell)=1/\kappa=
    \log x/c$, the range $[\log(2T),\frac12\log L_x]$ holds $\log x-\log\log
    x+O(1)$ such factors, and a bounded number of them near the top is
    $O(\log x/c)$.

Connections page, additional sentences in scope: "$h(L_x)\le\log_2L_x+1=
(1/\log2+o(1))x$" (refutation-failed, $\log_2L_x=\psi(x)/\log2$); "Near the
top it is a statement of the kind no factorial gap estimate reaches (Berend
and Harmse's Remark 2 ...)" (not checkable against the source; consistent
with Hughes's Remark 5); the "What it does not give" sentence
(refutation-failed: the $h_\alpha$ remark needs gaps $\ll g^{-\eta}$ at
every scale, and (H$_c$) gives $g^{-c/\log x}$); the "Leads created"
sentence about this lead (not a mathematical claim; accurate description).

## Required corrections

1. Lead page, section "Provisional premise", third bullet, first sentence.
   Replace "Tenenbaum's admissible sequences $\exp(-(\log k)^{\beta})$,
   $\beta<3/2$ (his Théorème 1, read in the Numdam text layer, page images
   not read), give through Lemma B only $h(L_x)\ll_\beta x/(\log x)^{\beta}$;"
   with "Tenenbaum's admissible sequences $\exp(-(\log k)^{\beta})$,
   $\beta<3/2$ (his Théorème 1, read in the Numdam text layer, page images
   not read; the paper has a published corrigendum, Ann. Inst. Fourier 50
   (2000), no. 1, 317–319, which Hughes cites for the deduction on pp. 6–7
   and Theorem 4 and which was not read), give through Lemma B only
   $h(L_x)\ll_\beta x/(\log x)^{\beta}$;".
2. Connections page, section "Problem 18, question (a), along the least
   common multiples", item (18a.2), first sentence. After "where the
   displayed formulas are garbled and the page images were not read)" insert
   "; its corrigendum, Ann. Inst. Fourier 50 (2000), no. 1, 317–319, cited by
   Hughes for the deduction on pp. 6–7 and Theorem 4, was not read". Add the
   corrigendum to "Sources read for this page" as not read.

## Suggested corrections

1. Lead page, "Route", Lemma B bullet: after "a nonincreasing bound
   $\tfrac12\delta(\sqrt{db})$ on $\log(b/d)$" insert "with $\delta$ taking
   values in $(0,1/8]$, $T\ge2$ and $2T\le\sqrt N$".
2. Lead page, "Provisional premise", opening: replace "Three facts about it
   are established on the connections page." with "Two facts about it are
   proved on the connections page, and a third rests on a text-layer
   reading of two sources not held."
3. Lead page, "Provisional premise", second bullet, and connections "Scale
   of the hypothesis": replace "at scale $x^m$ it allows" with "at scale
   $x^m$ with $m$ fixed it allows".
4. Lead page, "Provisional premise", first bullet: replace "the comment's
   lower-range recurrence is the lower-range step of Lemma B" with "the
   comment's lower-range recurrence is, up to the constant factor
   $2^{1+c/\log x}$, the lower-range step of Lemma B"; connections, same
   passage: replace "is exactly the lower-range step" with "is, up to a
   constant factor, the lower-range step".
5. Lead page, "Exploratory computation", and connections "Exploratory
   computation": after "the largest value the mean-gap bound allows" insert
   "in the limit; at $x\le64$ that bound itself only forces
   $\kappa_{\min}(x)\le2.2$–$2.7$".
6. Lead page, "Exploratory computation": replace "the largest $\log(b/d)$
   in each tenth of the range of $\log\sqrt{db}/\log\sqrt{L_x}$" with "the
   largest $\log(b/d)$ in each tenth of $[0,1]$ for
   $\log\sqrt{db}/\log\sqrt{L_x}$", which is what the script computes.
7. Lead page, frontmatter `desc`: replace "divisor-gap hypothesis at the
   mean-gap scale" with "divisor-gap hypothesis that reaches the mean-gap
   scale at the top of its range".
8. Lead page, "Next step", first sentence: after "track $\kappa_{\min}(x)$
   and the scale at which it is attained" add "; windows at sampled scales
   bound $\kappa_{\min}(x)$ from above only, unless they tile
   $[x,\sqrt{L_x}]$".
9. Lead page, "Next step", second sentence: after "his displays (6)–(8)"
   add ", read together with the 2000 corrigendum".

## Notes

**Independent computation.** For each $x\in\{20,30,40,50,60,64\}$ the prime
powers $p^{e}\le x<p^{e+1}$ were listed, all $\tau(L_x)$ divisors generated
and sorted, the window taken by the exact test $x^2\le db\le L_x$, and
$\log(b/d)$ computed as $\log(1+(b-d)/d)$. The ratio-two property was
checked exactly at every consecutive pair ($b\le2d$) for every $x$. Results,
with the author's top-tenth values from the verbatim rerun in the last
column:

| $x$ | $\tau(L_x)$ | $\log L_x$ | pairs in window | $\kappa_{\min}$ | minimizer $d,b$ | $\log(b/d)$ | $\sqrt{L_x/db}$ | top tenth |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20 | 960 | 19.2657 | 461 | 1.115794 | 15048, 15470 | $2.77\cdot10^{-2}$ | 1.000 | $2.77\cdot10^{-2}$ |
| 30 | 7680 | 28.4765 | 3811 | 1.256764 | 807576, 812889 | $6.56\cdot10^{-3}$ | 1.884 | $6.71\cdot10^{-3}$ |
| 40 | 36864 | 36.2146 | 18393 | 1.310676 | 59374455, 59477220 | $1.73\cdot10^{-3}$ | 1.230 | $1.87\cdot10^{-3}$ |
| 50 | 442368 | 49.4854 | 221135 | 1.297554 | 21557311776, 21565368600 | $3.74\cdot10^{-4}$ | 2.582 | $3.74\cdot10^{-4}$ |
| 60 | 1769472 | 57.5332 | 884677 | 1.347774 | 2700266996700, 2700485397828 | $8.09\cdot10^{-5}$ | 1.153 | $9.70\cdot10^{-5}$ |
| 64 | 4128768 | 62.3372 | 2064321 | 1.358251 | 30793652410950, 30794863747120 | $3.93\cdot10^{-5}$ | 1.117 | $4.45\cdot10^{-5}$ |

The restricted minimum over $\sqrt{db}\ge x^2$ is attained at the same pair
at every $x$. At $x=20$ the minimizer satisfies $db=L_{20}$ exactly (it is its
own mirror), so it sits on the window's boundary; the author's floating-point
test happened to include it, and the exact test includes it by definition.
The author's tenths are tenths of $[0,1]$; tenths of the actual range
$[\log x/\log\sqrt{L_x},1]$ give the same top-tenth maximum at $x=20$, $50$,
$60$ and $64$ and $6.56\cdot10^{-3}$, $1.76\cdot10^{-3}$ at $x=30$, $40$; the
lead quotes only $x=20$ and $x=64$.

**Finite form of the counting bound.** The argument of Weakest step 3 gives,
for each $x$, $\kappa_{\min}(x)\le(\log x)\log(\tau(L_x)/\log x)/\log(
\sqrt{L_x}/(\sqrt2\,x))$: $2.75$, $2.50$, $2.41$, $2.22$, $2.18$, $2.15$ at
the six sample points, $2.06$ at $x=100$, $1.71$ at $x=1000$, $1.59$ at
$x=10^4$, with limit $2\log2=1.386$; here $\log\tau(L_x)/(x/\log x)$ is
still $0.97$–$1.03$ on the sample against its limit $\log2$.

**Certificate for the minimizers.** The following stands alone and needs
only the standard library; each line should print the value of $x$, `True`
(both numbers divide $L_x$), `0` (no divisor of $L_x$ strictly between them,
found by pruned depth-first search rather than enumeration), `True` (the pair
is in the window) and $\kappa$ to six places.

```python
from decimal import Decimal, getcontext

PAIRS = {
    20: (15048, 15470),
    30: (807576, 812889),
    40: (59374455, 59477220),
    50: (21557311776, 21565368600),
    60: (2700266996700, 2700485397828),
    64: (30793652410950, 30794863747120),
}


def prime_powers(x):
    out = []
    for p in range(2, x + 1):
        if all(p % q for q in range(2, int(p ** 0.5) + 1)):
            e = 1
            while p ** (e + 1) <= x:
                e += 1
            out.append((p, e))
    return out


def divisors_strictly_between(pp, lo, hi):
    pp = sorted(pp, reverse=True)
    rest = [1] * (len(pp) + 1)
    for i in range(len(pp) - 1, -1, -1):
        rest[i] = rest[i + 1] * pp[i][0] ** pp[i][1]
    count, stack = 0, [(0, 1)]
    while stack:
        i, prod = stack.pop()
        if prod >= hi or prod * rest[i] <= lo:
            continue
        if i == len(pp):
            count += 1
            continue
        p, e = pp[i]
        stack.extend((i + 1, prod * p ** k) for k in range(e + 1))
    return count


getcontext().prec = 50
for x, (d, b) in PAIRS.items():
    pp = prime_powers(x)
    L = 1
    for p, e in pp:
        L *= p ** e
    half_log_db = (Decimal(d) * b).ln() / 2
    kappa = Decimal(x).ln() * (1 / (Decimal(b) / d).ln()).ln() / half_log_db
    print(x, L % d == 0 and L % b == 0, divisors_strictly_between(pp, d, b),
          x * x <= d * b <= L, round(kappa, 6))
```

**Rerun of the author's script.** From the repository root, the tree as it stood
on the frozen date, `uv run --no-sync python
wiki/research/leads/lcm_divisor_gap_greedy_route/evidence/util/gap_profile.py
20 30 40 50 60 64` printed the six rows of the lead's table (the $\kappa$
columns to three places, $\log L_x$ to two) in 7 seconds of wall time.

**On (H$_c$).** The hypothesis asks, at the top of the range, that the
largest gap between consecutive divisors of $L_x$ near $\sqrt{L_x}$ be at
most the mean gap raised to the power $c/(2\log2)$; for small $c$ this is
far weaker than mean-gap matching, and at every scale $x^m$ with $m$ fixed
it asks only for a constant. Nothing found here bears on its truth beyond
the counting bound and the sample. It is of a different kind from the
factorial gap estimates in the literature, whose exponents are powers of
$\log n$ where the mean gap's is $n/\log n$; the lead's assessment that no
known input approaches it is right on the inputs it names.

## Verdict

No statement of the lead or of the reviewed connections sections is refuted.
Lemma A, Lemma B and the transfer (18a.1) survive attack as written, so the
route is a correct conditional reduction: (H$_c$) for any $c\in(0,4]$ gives
$h(L_x)\le(3/c+o(1))(\log\log L_x)^2$, exponent $2$ in question (a) along
$L_x$, with the direct recurrence giving $2/c$. The route stands on (H$_c$)
alone, which is unproved, necessarily at most $2\log2+o(1)$, beyond every gap
input the lead names, and consistent with the computation to $x=64$, which
proves nothing. The computation's every stated number and rerun claim is
reproduced. One required correction, the disclosure of the 2000 corrigendum
to the Tenenbaum paper the lead cites for the known inputs and for its next
analytic step; nine suggested precision corrections. This is a focused
re-review of a research lead and asserts no tier; it is author-independent
in the sense stated above and awaits any grading the maintainers commission.
