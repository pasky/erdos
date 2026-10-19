---
name: research/leads/lcm_divisor_gap_greedy_route
title: A Divisor-Gap Route to Exponent Two Along the Least Common Multiples
desc: |
  Reduces h(lcm(1, ..., x)) = O((log x)^2), exponent two in question (a) of
  Problem 18 along a classical sequence, to an explicit lower-half
  divisor-gap hypothesis at the mean-gap scale, with the proved greedy
  transfer, a correction of the erdosproblems.com comment's form of the
  hypothesis, and an exploratory computation of its constant up to x = 64.
problems:
- 18
research_state: ready
review_status: reviewed
created: 2026-09-28T06:15:52Z
updated: 2026-10-19T04:19:07Z
---

# A Divisor-Gap Route to Exponent Two Along the Least Common Multiples

[[research/leads/_index|..]]

[[research/leads/lcm_divisor_gap_greedy_route/evidence/_index|evidence/]]: One exploratory script profiling the consecutive divisor gaps of
lcm(1, ..., x); no entry point, no checks, and no evidence for any claim.

***

This lead's notes that cite no source are author-recorded research, not claims.

## Target and status evidence

Question (a) of [[problems/divisors/E0018/_index|Problem 18]]: are there infinitely
many practical $m$ with $h(m)<(\log\log m)^{O(1)}$, where $h(m)$ is the least
number of distinct divisors of $m$ that always suffice to represent every
smaller positive integer? The problem page records part (a) as claimed by
van Doorn, graded sound by Plasma AI's internal review with its sign-off
pending, with exponent $2$. The remaining target of this lead is the more
specific bound along $\mathrm{lcm}(1,\ldots,x)$, which that claim does not
give.
Questions (b) and (c) concern $n!$ and are untouched by this divisor-gap
argument; the separate
[[research/erdos_18/dyadic_representative_route|dyadic route]] addresses
part (c).

## Route

Write $L_x=\mathrm{lcm}(1,\dots,x)$, so $\log L_x=\psi(x)\sim x$ and
$\log\log L_x=\log x+o(1)$. Erdős named $L_x$, with $n!$ and the primorials,
as a candidate for small consecutive divisor ratios (Tenenbaum 1987, p. 2),
and the erdosproblems.com discussion of 14 September 2026 proposes reducing
$h(L_x)=O((\log x)^2)$ to a divisor-gap bound. The route is that reduction,
made exact:

- *Lemma A* (proved on
  [[research/erdos_18/connections|the connections page]]): consecutive
  divisors of $L_x$ have ratio at most $2$, so $L_x$ is practical, the greedy
  expansion of every $m\le L_x$ uses distinct divisors, and
  $h(L_x)\le\log_2L_x+1$.
- *Lemma B* (proved there): for any $N$ with the ratio-two property, a
  nonincreasing bound $\tfrac12\delta(\sqrt{db})$ on $\log(b/d)$ over the
  consecutive divisor pairs with geometric mean in $[T,\sqrt N]$, with
  $\delta$ taking values in $(0,1/8]$, $T\ge2$ and $2T\le\sqrt N$, gives
  $h(N)\le3\int_{\log(2T)}^{\frac12\log N}d\ell/\sigma(\ell)$ plus
  $O(\log\sigma+\log T)$, with $\sigma(\ell)=\log(1/\delta(e^\ell/2))$; it
  is the step count of
  [[research/erdos_18/hughes_theorem_1_reconstruction|Hughes's Theorem 1]]
  with the factorial windows replaced by a profile, using only
  [[research/erdos_18/hughes_lemma_4_reconstruction|Lemma 4]] and the mirror
  symmetry of the divisor set.
- *The hypothesis.* $(\mathrm H_c)$: there are $c>0$ and $x_0$ such that for
  every $x\ge x_0$, every pair of consecutive divisors $d<b$ of $L_x$ with
  $x\le\sqrt{db}\le\sqrt{L_x}$ satisfies $\log(b/d)\le(db)^{-c/(2\log x)}$.

**Conclusion (author-recorded; conditional on $(\mathrm H_c)$).** With
$c\le4$,

$$
h(L_x)\le\Bigl(\frac3c+o(1)\Bigr)(\log x)^2
=\Bigl(\frac3c+o(1)\Bigr)(\log\log L_x)^2,
$$

which answers question (a) with exponent $2$ along $L_x$. The proof is item
(18a.1) of the connections page: Lemma B with $T=x^{4/c}$ and
$\delta(g)=2g^{-c/\log x}$.

## Provisional premise

$(\mathrm H_c)$ is unproved. Three facts about it are established on the
connections page.

- *The comment's form fails in the top range.* The erdosproblems.com comment
  states its bound for the largest gap below $Y$ for all $x<Y\le L_x$; at
  $Y=L_x$ the pair $(L_x/2,L_x)$ violates it, as does every $Y$ near $L_x/k$ for
  bounded $k$. The lower-half form $(\mathrm H_c)$ is what the greedy count
  needs, because the mirror symmetry $d\mapsto L_x/d$ handles the upper half;
  the comment's lower-range recurrence is, up to the constant factor
  $2^{1+c/\log x}$, the lower-range step of Lemma B.
- *Mean-gap scale.* Since $\log\tau(L_x)=(\log2+o(1))x/\log x$, the window
  $[\sqrt{L_x}/x,\sqrt{L_x}]$ contains a consecutive pair with
  $\log(b/d)\ge\exp(-(\log2+o(1))x/\log x)$, so $(\mathrm H_c)$ forces
  $c\le2\log2+o(1)$, and with $c$ near $2\log2$ it is at the mean-gap scale
  near $\sqrt{L_x}$, where the exponents of its allowance and of the mean gap
  agree to first order, while at scale $x^m$ with $m$ fixed it allows gaps
  $e^{-cm}$ of constant size against a mean gap of order $x^{-m}$ up to
  powers of $\log x$.
- *Known inputs fall far short.* Tenenbaum's admissible sequences
  $\exp(-(\log k)^{\beta})$, $\beta<3/2$ (Théorème 1, read in the Numdam
  text layer, page images not read; the paper has a published corrigendum,
  Ann. Inst. Fourier 50 (2000), no. 1, 317–319, which Hughes cites for the
  deduction on pp. 6–7 and Theorem 4 and which was not read), give through
  Lemma B only $h(L_x)\ll_\beta x/(\log x)^{\beta}$; Berend and Harmse state
  that their factorial method does not apply to $L$; and even a bound of
  their strength would give order $x/(\log x)^2$. $(\mathrm H_c)$ has a
  linear descent $\sigma(\ell)=c\ell/\log x$ where every known input has a
  polylogarithmic one.

## Exploratory computation

The retained script [`gap_profile.py`](evidence/util/gap_profile.py) under
this lead's evidence folder enumerates every divisor of $L_x$ and, over the
consecutive pairs $d<b$ with $x\le\sqrt{db}\le\sqrt{L_x}$,
computes the least value of
$\kappa(d,b)=(\log x)\log(1/\log(b/d))/\log\sqrt{db}$, the largest $c$ for
which $(\mathrm H_c)$ holds at that pair; it also reports the least value
over the pairs with $\sqrt{db}\ge x^2$ and the largest $\log(b/d)$ in each
tenth of $[0,1]$ for $\log\sqrt{db}/\log\sqrt{L_x}$. Run from the
repository root with the arguments `20 30 40 50 60 64`, as
[the evidence index](evidence/_index.md) records, it prints in a few
seconds:

| $x$ | $\tau(L_x)$ | $\log L_x$ | $\kappa_{\min}$ | $\kappa_{\min}$, $\sqrt{db}\ge x^2$ |
| --- | --- | --- | --- | --- |
| 20 | 960 | 19.27 | 1.116 | 1.116 |
| 30 | 7680 | 28.48 | 1.257 | 1.257 |
| 40 | 36864 | 36.21 | 1.311 | 1.311 |
| 50 | 442368 | 49.49 | 1.298 | 1.298 |
| 60 | 1769472 | 57.53 | 1.348 | 1.348 |
| 64 | 4128768 | 62.34 | 1.358 | 1.358 |

The largest $\log(b/d)$ in the top tenth falls from $2.8\cdot10^{-2}$ at
$x=20$ to $4.5\cdot10^{-5}$ at $x=64$, and the binding pairs sit at the top
of the range, within a factor of about $2.6$ of $\sqrt{L_x}$.
$\kappa_{\min}(x)$ shows no downward trend over the sample (it dips once,
from $1.311$ at $x=40$ to $1.298$ at $x=50$) and approaches
$2\log2=1.386\ldots$ from below, the largest value the mean-gap bound allows
in the limit (its finite form,
$\kappa_{\min}(x)\le(\log x)\log(\tau(L_x)/\log x)/\log(\sqrt{L_x}/(\sqrt2\,x))$,
only forces $\kappa_{\min}(x)\le2.75$ at $x=20$ and $\kappa_{\min}(x)\le2.15$
at $x=64$); this was observed after the fact, not predicted. The computation
can only begin to distinguish a quickly vanishing constant, which would show
that no fixed $c$ satisfies $(\mathrm H_c)$, from a stable one; it cannot
prove $(\mathrm H_c)$, and $x\le64$ is far from asymptotic. The script is
exploratory and is not evidence for any claim.

## Consequential gap

$(\mathrm H_c)$ itself. A proof for any $c>0$ gives exponent $2$ in question
(a) along an explicit classical sequence, with a constant $3/c$ (or $2/c$
when the upper range is counted by the recurrence on $U=L_x/R$ instead of
Lemma B's dyadic partition), independently of the claimed chains of Price and
of the van Doorn note. A disproof, a sequence of $x$ along which
$\kappa_{\min}(x)\to0$, would show that no hypothesis of the form
$(\mathrm H_c)$ with a fixed $c$ holds, so (18a.1) as stated gives nothing
along that sequence; whether a scale-dependent profile, or one that tolerates
a few exceptional pairs, still gives $(\log x)^2$ through Lemma B would
remain open, with Lemma B's $x/(\log x)^{3/2-\eta}$ from Tenenbaum's input
the route's best bound without $(\mathrm H_c)$. Neither outcome bears on $n!$
or on questions (b) and (c).

## Next step

Push the computation to $x$ near $100$ by enumerating only the divisors of
$L_x$ in a window around each scale (products of prime powers at most $x$
within a fixed factor of a target), rather than all $\tau(L_x)$ divisors, and
track $\kappa_{\min}(x)$ and the scale at which it is attained. In parallel,
attempt $(\mathrm H_c)$ near the middle with Tenenbaum's method (the Fourier
integral over the divisor-counting function at the saddle point near
$\sqrt N$, the paper's displays (6)–(8), read together with the 2000
corrigendum), which is where Tenenbaum's admissible sequences come from and
where the density of divisors is largest; the middle is also where the
computation finds the binding pairs. Under $(\mathrm H_c)$ every factor-of-$e$ range of
$\ell=\log(2g)$ contributes $\log x/c$ to the integral of Lemma B, so a
result near $\sqrt{L_x}$ alone covers only $O(\log x)$ of the $(\log x)^2$
count; it is nevertheless the range where $(\mathrm H_c)$ is tightest and
where the computation finds the binding pairs.

## Current review

Reviewed. The route was first independently reviewed on 2026-09-28 in the review
record
[[research/erdos_18/evidence/verify/connections_problem_18_question_a_along_the_least_common_mul_review|the
question (a) review]] (which covered this lead with the question (a) section of
the connections page, re-derived the proof of (18a.1), the upper-range
recurrence and the window argument behind $c\le2\log2$, and reproduced the
computation by an independent enumeration), with Lemmas A and B re-derived in
[[research/erdos_18/evidence/verify/connections_shared_lemmas_review|the shared
lemmas review]], and graded in
[[research/erdos_18/evidence/verify/connections_grade|the grade]], which
repeated the enumeration and recorded this lead as needing an update; the
corrections of that grade, C7 and C8(a) to C11(a) on the connections page and
C8(b), C9(b), C10(b), C11(b), C11(c) and C12 in the sections "Provisional
premise", "Exploratory computation", "Consequential gap" and "Next step" above,
were applied, so the page then differed from the text those records reviewed at
those places.

The corrected page was re-reviewed as it stood on 2026-10-02, from a blind
extraction kept outside the repository and frozen on that date: this page with
its review-status fields and this section removed, and the connections page. A
first attempt at the re-review, whose extraction carried the earlier verdicts,
was stopped before completion and its output discarded. The re-review is the
record
[[research/erdos_18/evidence/verify/lead_lcm_divisor_gap_greedy_route_rereview|the
lead re-review]] (the whole of this page, with Lemmas A and B and the question
(a) section of the connections page, every mathematical statement re-derived and
the computation reproduced by an independent route), graded in
[[research/erdos_18/evidence/verify/lead_lcm_divisor_gap_greedy_route_rereview_grade|the
re-review grade]], which re-derives every verdict and reproduces the computation
a third way. The graded verdicts are these. Lemma A at $L_x$: refutation-failed.
Lemma B: refutation-failed, its hypotheses $\delta\le1/8$, $T\ge2$ and
$2T\le\sqrt N$ stated in the summary above. The conditional transfer (18a.1)
and its answer to question (a): refutation-failed as conditional statements,
their antecedent $(\mathrm H_c)$ unproved. The failure of the comment's form in
the top range, the lower-range recurrence up to a constant factor, and the
direct count $2/c$: refutation-failed. The necessary bound $c\le2\log2+o(1)$ and
the scale comparison at $x^m$ with $m$ fixed: refutation-failed. What the known
gap inputs give: refutation-failed as deductions from Tenenbaum's admissibility
statement and Berend and Harmse's remark, both external and unread, with the
2000 corrigendum to Tenenbaum's paper disclosed. The description of the
computation, every printed value, the observations drawn from it and the rerun
claim: refutation-failed. The consequences of a proof or a disproof of $(\mathrm
H_c)$ and the factor-of-$e$ count in the next step: refutation-failed. The
target paragraph, the attributions and the plans are not mathematical claims. No
statement was refuted. The accepted corrections G1 to G8 of the grade, the
disclosure of the corrigendum and precision repairs to sentences the route does
not rest on, were applied to the sections "Route", "Provisional premise",
"Exploratory computation" and "Next step" above and, for G2, G4 and G5, to the
connections page, so the current text differs from the reviewed text at those
places; none touches the proved part or the premise. $(\mathrm H_c)$ remains
unproved, the exploratory computation carries no evidence, and the next step is
unchanged. Since the re-review, "Target and status evidence" was restated
against the current problem page without a date; this touches no examined
statement, proof, code or input. No tier is assigned and the status of the
problem does not change.
