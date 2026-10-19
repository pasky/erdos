---
name: research/erdos_18/evidence/verify/connections_problem_18_question_a_along_the_least_common_mul_review
title: "Independent review of the connections section: Problem 18, question (a), along the least common multiples"
desc: |
  Refutation-failed for the conditional transfer (18a.1), for the top-range
  failure of the site comment's form, for the necessary bound c at most
  2 log 2, and for the Tenenbaum transfer as a conditional; proof defective,
  statement unresolved, for the constant 1/c and for the obstruction drawn
  from a disproof; refuted-as-stated for the description of the computation
  and for the every-scale mean-gap gloss. Four required corrections, two
  suggested, one note.
created: 2026-09-28T18:04:45Z
updated: 2026-09-28T18:04:45Z
---

***

## Subject and independence

Role: independent reviewer in a fresh context, given only the commissioning
assignment. The reviewer took no part in writing the connections page, the
lead page, or the reconstruction pages, and read no review, grade, assessment,
known-results, or standing text about them. The charge is refutation.

Frozen subject: the repository as it stood at 2026-09-28T13:50:48Z. The section
"Problem 18, question (a), along the least common multiples" of
[[research/erdos_18/connections|the connections page]]
(wiki/research/erdos_18/connections.md), lines 431 to 550, from its H2
heading to the line before the next H2 at line 551; and the whole lead page
[[research/leads/lcm_divisor_gap_greedy_route/_index|lcm_divisor_gap_greedy_route]]
(wiki/research/leads/lcm_divisor_gap_greedy_route/_index.md) as of the same
time. The paths are what was read.

Read, all as of that time: the section in full at proof depth; the lead page in
full; the connections page's frontmatter, opening paragraph, Conventions
paragraph, and the shared section "Shared lemmas" (Lemmas A, B, C, C' and D)
as inputs, at interface depth only, their proofs being another reviewer's
subject; the four reconstruction pages
[[research/erdos_18/hughes_lemma_4_reconstruction|Lemma 4]],
[[research/erdos_18/hughes_theorem_1_reconstruction|Theorem 1]],
[[research/erdos_18/hughes_corollary_3_reconstruction|Corollary 3]] and
[[research/erdos_18/hughes_remark_6_reconstruction|Remark 6]] in full, as
premises at the standing the assignment states; the Statement paragraph of
[[problems/divisors/E0018/_index|Problem 18]]; and the commissioned wiki pages
(verification: report contract, whole-claim report, audit checklist, grading;
approach_vetting; evidence, Source fidelity; math_authoring). The library was
searched for holdings: the Tenenbaum (1987) and Berend and Harmse (1993)
papers are not held, so their statements were not read from any source. The
retained script under the lead's evidence folder was neither read nor run;
evidence folders are excluded. The computation was reproduced from an
independent script written for this review, described under Checklist,
Computation; that script is not retained, since the assignment permits
writing only this report.

Exposures: (1) while locating the section boundary the reviewer read the
neighboring section "Problem 18, question (c)" (lines 551 to 585) and the
closing sections "Leads created" and "Sources read for this page" (lines 779
to 807) of the connections page; they hold author-recorded mathematics of
another section and a reading log, no review or standing text; (2) a heading
listing of the problem page displayed its frontmatter line `status: open`;
(3) the file names under wiki/research/erdos_18/evidence/verify/ were listed
to confirm that the target directory exists, and none of those files was
opened. No web search was made.

## Restatement

Conventions. $L_x=\mathrm{lcm}(1,\dots,x)$; $\log$ is natural;
$\psi(x)=\log L_x$; $\tau$ counts divisors; $h(N)$ is the page's: the least
$k$ such that every $1\le m\le N$ is a sum of at most $k$ distinct divisors
of $N$, so the site's $h$, ranging over $m<N$, is at most it. Consecutive
divisors $d<b$ of $L_x$ are adjacent in the sorted divisor list. The
hypothesis $(\mathrm H_c)$: there exist $c>0$ and $x_0$ such that for every
$x\ge x_0$ and every pair of consecutive divisors $d<b$ of $L_x$ with
$x\le\sqrt{db}\le\sqrt{L_x}$, $\log(b/d)\le(db)^{-c/(2\log x)}$.

- S1 (Lemma A at $L_x$). For every $x\ge2$: consecutive divisors of $L_x$
  have ratio at most $2$; $L_x$ is practical; the greedy expansion of every
  $1\le m\le L_x$ uses distinct divisors; and
  $h(L_x)\le\log_2L_x+1=(1/\log2+o(1))\,x$.
- S2 (item (18a.1)). Fix $c$ with $0<c\le4$ for which $(\mathrm H_c)$ holds
  (if $(\mathrm H_c)$ holds for some $c>4$ then $(\mathrm H_4)$ holds). Then
  $h(L_x)\le(3/c+o(1))(\log x)^2=(3/c+o(1))(\log\log L_x)^2$ as
  $x\to\infty$, the $o(1)$ depending on $c$; hence under $(\mathrm H_c)$ the
  numbers $L_x$, $x\ge x_0$, are infinitely many practical $m$ with
  $h(m)\le(\log\log m)^{2+o(1)}$, exponent $2$ in question (a).
- S3 (the comment's form fails in the top range). With
  $\Delta_x(Y)=\max_{d_i<Y}(\min\{d_{i+1},Y\}-d_i-1)$ over consecutive
  divisors $d_i<d_{i+1}$ of $L_x$, the bound $\Delta_x(Y)+1\le Y^{1-c/\log x}$
  for all large $x$ and all $x<Y\le L_x$ fails for every $c>0$: at $Y=L_x$,
  on $(L_x/2+2L_x^{1-c/\log x},L_x]$, and near $L_x/k$ for every bounded $k$.
- S4 (the lower-range constant). The comment's recurrence
  $R'\le R^{1-c/\log x}$ is the lower-range step of Lemma B and gives
  $(1/c+o(1))(\log x)^2$ steps in the lower range $T\le R\le\sqrt{L_x}$.
- S5 (the constant $1/c$). The factor $3$ in $3/c$ is a bookkeeping loss,
  not a mathematical one; on the lead, the constant $1/c$ is obtained "with
  the comment's recurrence in the lower range and the same mirror argument".
- S6 (item (18a.2)). If for every $\beta<3/2$ and all large $k$ every
  $z\in(\sqrt{L_{k-1}},\sqrt{L_k}]$ has a divisor of $L_k$ in
  $(z,(1+\varepsilon_k)z]$ with $\varepsilon_k=\exp(-(\log k)^\beta)$, then
  $h(L_x)\ll_\beta x/(\log x)^\beta$; a profile $\sigma(\ell)\asymp(\log\ell)^2$
  would give order $x/(\log x)^2$; neither profile approaches
  $(\mathrm H_c)$, whose $\sigma(\ell)=c\ell/\log x$ is linear in $\ell$.
- S7 (the necessary bound). $\log\tau(L_x)=(\log2+o(1))\,x/\log x$; the
  window $[\sqrt{L_x}/x,\sqrt{L_x}]$ forces a consecutive pair with
  $\log(b/d)\ge\log x/\tau(L_x)$ inside the scope of $(\mathrm H_c)$; hence
  $(\mathrm H_c)$ can hold only if $c\le2\log2$.
- S8 (the mean-gap gloss). $(\mathrm H_c)$ with $c$ near $2\log2$ says that
  the largest gap matches the mean gap up to a polynomial factor at every
  scale above $x$.
- S9 (the computation). For $x=20,30,40,50,60,64$: $\tau(L_x)=960$, $7680$,
  $36864$, $442368$, $1769472$, $4128768$; $\log L_x=19.27$, $28.48$,
  $36.21$, $49.49$, $57.53$, $62.34$; $\kappa_{\min}(x)=1.116$, $1.257$,
  $1.311$, $1.298$, $1.348$, $1.358$, with the same values over the pairs
  with $\sqrt{db}\ge x^2$, where
  $\kappa(d,b)=(\log x)\log(1/\log(b/d))/\log\sqrt{db}$ is the largest $c$
  for which $(\mathrm H_c)$ holds at the pair; $\kappa_{\min}$ does not
  decrease over the range and approaches $2\log2$ from below; the binding
  pairs sit in the middle of the range, where the largest $\log(b/d)$ falls
  from $2.8\cdot10^{-2}$ at $x=20$ to $4.5\cdot10^{-5}$ at $x=64$ (the lead:
  "in the middle tenth").
- S10 (the obstruction drawn from a disproof). A sequence of $x$ along which
  $\kappa_{\min}(x)\to0$ shows that the greedy route along $L_x$ gives only
  $(\log x)^2/\kappa_{\min}(x)$; on the lead, that the greedy route "cannot
  give $(\log x)^2$", leaving $x/(\log x)^{3/2-\eta}$ as the route's best.
- S11 (the lead's next step). A result for "the middle" alone would already
  cover the range that dominates the integral of Lemma B.
- S12 (what it does not give). Nothing about $h(n!)$; nothing unconditional
  beyond $h(L_x)\ll x/(\log x)^{3/2-\eta}$; no bound on $h_\alpha(L_x)$.

## Checklist

- Quantifiers and scope. S2 is stated for fixed $c$ and $x\to\infty$, and
  the proof uses $x\ge x_0(c)$ only; the scope of $(\mathrm H_c)$ (pairs with
  $x\le\sqrt{db}\le\sqrt{L_x}$) covers Lemma B's range $[T,\sqrt{L_x}]$
  because $T=x^{4/c}\ge x$ when $c\le4$; S7 checks that the extremal pair it
  produces lies in that scope. S10 quantifies over a disproof it does not
  prove anything from (F2). Verdict: pass for S1 to S7; fail for S10.
- Circularity. None. $(\mathrm H_c)$ is a statement about the divisor set;
  the conclusions are step counts; Lemmas A and B are consumed at their
  interfaces and neither uses the target. Verdict: pass.
- Model and convention changes. The two conventions for $h$ are reconciled
  (the site's is at most the page's); Lemma B's $\delta$, $\sigma$, $T$ and
  the natural logarithm are matched exactly in S2; the comment's
  $\Delta_x$ form translates to the log-ratio form as the page says
  ($R-d\le\Delta_x(R+1)$). S8 uses "mean gap" and "polynomial factor" with
  no fixed meaning (F5). Verdict: pass except S8.
- Finite and statistical overreach. The computation is labeled exploratory
  and the approach to $2\log2$ as observed after the fact. But "does not
  decrease" is contradicted by the table it describes, and the lead's "The
  computation distinguishes a quickly vanishing constant ... from a stable
  one" claims a discrimination six values at $x\le64$ cannot make (F3, F7).
  Verdict: fail for those sentences.
- Uniformity. The $o(1)$ of S2 depends on $c$ through $T=x^{4/c}$ and
  $x_0(c)$; no uniformity in $c$ is claimed. S6's implied constant depends
  on $\beta$, as the notation $\ll_\beta$ says. S7's $o(1)$ is absolute.
  Verdict: pass.
- Extremal conclusions. $\kappa_{\min}(x)$ is an infimum in the claim's own
  units and was recomputed; every printed value agrees to the printed
  precision. The location of the extremum is misdescribed (F3). The
  necessary bound $c\le2\log2$ is derived in the right units (log-gaps at
  the top scale). Verdict: pass for the values, fail for the location.
- Consequences and composition. "Answers (a) with exponent 2" follows from
  S2. "The constant $3/c$ is a bookkeeping loss" and the lead's "$1/c$" do
  not follow (F1). "Shows that the greedy route gives only ..." and "cannot
  give $(\log x)^2$" do not follow (F2). "Would already cover the range that
  dominates the integral" is false for the route's own profile (F6).
  "Nothing unconditional beyond ..." consumes the unverified Tenenbaum
  import without saying so (F7). Verdict: fail for S5, S10, S11.
- Computation. The reviewer's script enumerates every divisor of $L_x$ as an
  exact integer from the prime-power factorization, sorts them, and for each
  consecutive pair with $x\le\sqrt{db}\le\sqrt{L_x}$ evaluates
  $\log(b/d)=\log(1+(b-d)/d)$ in double precision and $\kappa(d,b)$; it
  reports the minimum, the pair attaining it with its position
  $\log\sqrt{db}/\log\sqrt{L_x}$, the minimum over pairs with
  $\sqrt{db}\ge x^2$, and the largest $\log(b/d)$ in each tenth of the range
  of $\log\sqrt{db}$ over $[\log x,\log\sqrt{L_x}]$. The divisor counts
  equal $\tau(L_x)$ from the factorization, which is a failing check for an
  incomplete enumeration; a mutated $\kappa$ changes every value. Verdict:
  pass for the table; the descriptive sentences fail (F3).
- Reproduction. The lead's rerun line names a script in an excluded folder,
  so it was not run; the table was reproduced independently as above. The
  connections page's statement that the script and command are retained on
  the lead page was checked only as a cross-reference. Verdict: pass for
  the numbers; the retained script itself is outside this review.
- Source and verdict fidelity. Tenenbaum (1987) and Berend and Harmse (1993)
  are not held, and the section says it read garbled text layers; the
  quoted admissibility statement, the remark that the factorial method does
  not apply to $L$, and Remark 2 could not be checked, nor could the wording
  of the site comment of 14 September 2026 (web excluded). The section's
  account of the problem page's status was not checked (excluded). The
  target matches the Statement paragraph of Problem 18. Verdict: pass on
  what is checkable; three imports remain unverified premises.

## Weakest steps

W1 (the proof of S2, rederived). Lemma A gives $L_x$ the ratio-two property
because $v_2(L_x)=\lfloor\log_2x\rfloor\ge\lfloor\log_2p\rfloor$ for every
odd prime $p\le x$. Take $T=x^{4/c}\ge x\ge2$ and
$\delta(g)=2g^{-c/\log x}$ on $[T,\sqrt{L_x}]$, nonincreasing, positive, and
at most $\delta(T)=2\exp(-(c/\log x)(4/c)\log x)=2e^{-4}<1/8$. The written
"$\delta\le2x^{-4}$" is false ($2e^{-4}\approx0.037$ against
$2\cdot64^{-4}\approx1.2\cdot10^{-7}$), but the needed conclusion
$\delta\le1/8$ holds (F4). Since $\log(2T)=\log2+(4/c)\log x$ and
$\tfrac12\log L_x=\tfrac12\psi(x)\sim x/2$, $2T\le\sqrt{L_x}$ for
$x\ge x_1(c)$. $(\mathrm H_c)$ gives, for consecutive $d<b$ with
$T\le\sqrt{db}\le\sqrt{L_x}$, $\log(b/d)\le(\sqrt{db})^{-c/\log x}$, which is
$\tfrac12\delta(\sqrt{db})$: Lemma B's hypothesis. With $\kappa=c/\log x$,
$\sigma(\ell)=\log(1/\delta(e^\ell/2))$ equals
$\kappa\ell-\kappa\log2-\log2\ge\kappa\ell-2$ for $x\ge16$. On
$[\log(2T),\tfrac12\log L_x]$, $\kappa\ell-2\ge2$ because
$\kappa\log(2T)=4+c\log2/\log x$, so

$$
\int_{\log(2T)}^{\frac12\log L_x}\frac{d\ell}{\sigma(\ell)}
\le\frac1\kappa\log\frac{\kappa\cdot\frac12\log L_x-2}{2}
\le\frac{\log x}{c}\log\frac{cx}{\log x}
\le\frac{(\log x)^2}{c},
$$

using $\tfrac12\psi(x)\le x$ and $c\le\log x$. Also
$\sigma(\tfrac12\log L_x)\le cx/\log x$, so $\log_2\sigma=O(\log x)$, and
$2\log_2(2T)=2+(8/c)\log_2x$. Lemma B yields
$h(L_x)\le3(\log x)^2/c+O_c(\log x)$, which is S2, and
$(\log\log L_x)^2=(\log x+o(1))^2$ by $\psi(x)\sim x$. Decreasing $c$ only
weakens $(\mathrm H_c)$ since $db>1$. The step survives.

W2 (the upper-range constant, rederived to test S5). Let $R>\sqrt{L_x}$ be a
nonterminal remainder with bracketing divisors $d<R<b$ and put $U=L_x/R$.
The mirror pair $L_x/b<U<L_x/d$ has the same ratio and geometric mean
$L_x/\sqrt{db}\in(U/\sqrt2,\sqrt2U)$, inside $[T,\sqrt{L_x}]$ when
$2T\le U<\sqrt{L_x}$, so $(\mathrm H_c)$ and Lemma 4 give
$R'\le2R\log(b/d)\le R\,\delta(U/2)=2^{1+\kappa}R\,U^{-\kappa}$, that is,
$\log U'\ge(1+\kappa)\log U-(1+\kappa)\log2$. With $A=(1+\kappa)\log2/\kappa$
the quantity $\log U-A$ grows by a factor at least $1+\kappa$ per step, from
at least $\log(2T)-A\ge(4-\log2-o(1))\log x/c>0$ to at most
$\tfrac12\psi(x)$; so the upper range holds at most

$$
\frac{\log\bigl(\tfrac12\psi(x)\big/((4-\log2-o(1))\log x/c)\bigr)}{\log(1+\kappa)}
=\Bigl(\frac1c+o(1)\Bigr)(\log x)^2
$$

steps, and no fewer can be excluded from $(\mathrm H_c)$ alone, since the
hypothesis allows every step to descend by exactly its bound. The lower
range costs another $(1/c+o(1))(\log x)^2$ by S4. Thus the direct
recurrences on both sides give the constant $2/c$; only the factor $2$ that
Lemma B's dyadic partition puts on the upper-range integral is bookkeeping.
The constant $1/c$ of S5 is not produced by the argument S5 names.

W3 (the window argument of S7, rederived). The consecutive-pair intervals
$[\log d_i,\log d_{i+1}]$ cover the log-window
$[\log(\sqrt{L_x}/x),\log\sqrt{L_x}]$ of length $\log x$ with at most
$\tau(L_x)-1$ intervals, so one has length at least $\log x/\tau(L_x)$. Each
covering pair lies in the scope of $(\mathrm H_c)$: a pair straddling
$\sqrt{L_x}$ is a mirror pair, $b=L_x/d$, with $\sqrt{db}=\sqrt{L_x}$
exactly ($\sqrt{L_x}$ is not a divisor, since a prime in $(\sqrt x,x]$ has
exponent $1$); a pair straddling $\sqrt{L_x}/x$ has $d\ge b/2$, so
$\sqrt{db}>\sqrt{L_x}/(\sqrt2x)\ge x$ for large $x$. For such a pair
$(\mathrm H_c)$ gives $\log(b/d)\le\exp(-(c/2\log x)(\psi(x)-2\log x-\log2))$,
and $\log\tau(L_x)=(\log2)(\pi(x)-\pi(\sqrt x))+O(\sqrt x\log\log x)$ by
counting prime exponents, so $\log x/\tau(L_x)=\exp(-(\log2+o(1))x/\log x)$;
comparing exponents gives $c/2\le\log2+o(1)$, and for a fixed $c$ this is
$c\le2\log2$. The step survives.

## Strongest attack

- S1. Attempted to break the interface of Lemma A at $L_x$: the hypothesis
  needs $v_2(L_x)\ge\lfloor\log_2p\rfloor$ for every odd prime $p\mid L_x$,
  and $v_2(L_x)=\lfloor\log_2x\rfloor$ with $p\le x$ makes it hold. Failed.
- S2. Attempted to violate each hypothesis of Lemma B: $T\ge2$ and $T\ge x$
  (needs $c\le4$, supplied); $2T\le\sqrt{L_x}$ (for large $x$); $\delta$
  nonincreasing into $(0,1/8]$ (true, with the corrected value $2e^{-4}$);
  the hypothesis on every pair in $[T,\sqrt{L_x}]$ (supplied by
  $(\mathrm H_c)$ since $T\ge x$). Attempted to make the $o(1)$ hide a
  $c$-dependent main term: the extra terms are $O(\log x)$ and
  $O(\log x/c)$, lower order for fixed $c$. Attempted the vacuity route
  ($c>2\log2$ is impossible by S7): the statement remains a correct
  conditional for the admissible $c$. Failed; only the slip F4 remains.
- S3. Attempted to rescue the comment's bound at $Y=L_x$: the largest proper
  divisor of $L_x$ is $L_x/2$, so $\Delta_x(L_x)+1\ge L_x/2$, while
  $L_x^{1-c/\log x}=L_x\exp(-c\psi(x)/\log x)=o(L_x)$. For
  $Y\in(L_x/2+L_x^{1-c/\log x},L_x]$ the same pair gives
  $\Delta_x(Y)+1\ge Y-L_x/2>L_x^{1-c/\log x}\ge Y^{1-c/\log x}$, which covers
  the page's narrower interval; near $L_x/k$ the consecutive pair
  $L_x/k<L_x/(k-1)$ gives a gap $L_x/(k(k-1))$. Failed.
- S4. Checked that Lemma B's lower-range step is
  $R'\le R\,\delta(R/2)=2^{1+\kappa}R^{1-\kappa}$, the comment's recurrence
  up to the constant, and that the charging integral gives
  $1+(\log x)^2/c$. Failed.
- S5. Succeeded: W2 shows the argument named gives $2/c$, not $1/c$.
- S6. Attempted to break the transfer: a divisor of $L_k$ in
  $(z,(1+\varepsilon_k)z]$ with $z=\sqrt{db}$ and $k\le x$ divides $L_x$, so it
  is at least $b$, giving $\log(b/d)\le2\varepsilon_k$; the profile
  $\delta(g)=4\varepsilon_{k(g)}$ is nonincreasing and at most $1/8$ above a
  fixed $T$; $\sigma(\ell)=(\log k)^\beta-\log4$ with $k=(2+o(1))\ell$; the
  integral is $\ll_\beta x/(\log x)^\beta$; the windows of non-prime-powers
  are empty and harmless. Failed as a transfer. The imported statement
  itself could not be attacked (not held).
- S7. Attempted to place the forced pair outside the scope of
  $(\mathrm H_c)$ (W3): impossible. Failed.
- S8. Succeeded under the reading in which the sentence has content: at
  scale $g=x^2$, $(\mathrm H_c)$ with $c=2\log2$ allows
  $\log(b/d)\le e^{-2c}\approx0.06$ while the products of two primes at most
  $x$ alone put $\gg x^2/(\log x)^2$ divisors of $L_x$ in $[x^2,2x^2]$, a
  mean log-gap $\ll(\log x)^2/x^2$; at the top scale the allowance
  $\exp(-(\log2)\psi(x)/\log x)$ exceeds $\log x/\tau(L_x)$ by
  $\exp((\log2)(\pi(x)-\psi(x)/\log x)+O(\sqrt x))=\exp(\Theta(x/(\log x)^2))$,
  and for any fixed $c<2\log2$ by $\exp(\Theta(x/\log x))$. Under the other
  reading, a factor polynomial in the scale $g$, the sentence is true and
  empty, since every gap is at most $\log2$ and the mean log-gap at $g$ is
  at least $1/g$.
- S9. The values were reproduced exactly. The description failed: the
  binding pairs sit at positions $1.000$, $0.956$, $0.989$, $0.962$, $0.995$,
  $0.996$ of $\log\sqrt{db}/\log\sqrt{L_x}$, that is, within a factor $2.6$
  of $\sqrt{L_x}$ (at $x=20$ it is the mirror pair $15048<15470$ around
  $\sqrt{L_{20}}$); the maxima $2.77\cdot10^{-2}$ and $4.45\cdot10^{-5}$ are
  those of the top tenth of the range, the middle tenths at $x=64$ having
  maxima $3.3\cdot10^{-4}$ and $1.9\cdot10^{-4}$; and $1.311$ at $x=40$ is
  followed by $1.298$ at $x=50$.
- S10. Succeeded in showing the implication is unsupported: a single pair
  with small $\kappa$ costs the greedy expansion at most one step in the
  lower range, since the next remainder lies below the pair, and at most
  one in the upper range through its mirror; a refined charging count
  excludes such pairs at a cost of one step each, so
  $\kappa_{\min}(x)\to0$ does not bound the route from below. What it does
  show is that no fixed $c$ satisfies $(\mathrm H_c)$.
- S11. Succeeded: under $\sigma(\ell)=c\ell/\log x$ the integral is
  $(\log x/c)\log(\ell_1/\ell_0)$, uniform in $\log\ell$, so the top tenth of
  the range contributes a share $\log(10/9)/\log(\ell_1/\ell_0)$, about
  $0.035$ at $x=1000$ and tending to $0$, and even $[\ell_1/2,\ell_1]$ only
  $(\log2)(\log x)/c$ of the $(\log x)^2/c$ total.
- S12. Attempted to find an unconditional bound the section overlooks or
  overstates: $x/(\log x)^{3/2-\eta}$ is exactly S6 and rests on the
  unverified import (F7). Otherwise failed.

## Premises

- [[research/erdos_18/hughes_lemma_4_reconstruction|Lemma 4]]: for $N$ with
  the ratio-two property and nonterminal $R$ with bracketing $d<R<b$,
  $R-d<d$ and $R-d\le2R\log(b/d)$; chosen divisors strictly decrease;
  termination and the representation of $m$. Read in full; consumed by
  Lemmas A and B and in W2. Standing as the assignment states.
- [[research/erdos_18/hughes_theorem_1_reconstruction|Theorem 1]]: facts (i)
  and (ii) (a remainder at most $\sqrt N$ has $db\le N$, above it $db\ge N$)
  and the charging integral. Read in full; consumed by Lemma B and W2.
- [[research/erdos_18/hughes_corollary_3_reconstruction|Corollary 3]]: the
  notation $\varepsilon_j$ and the windows only. Read in full.
- [[research/erdos_18/hughes_remark_6_reconstruction|Remark 6]]: not used by
  this section. Read in full.
- Lemma A and Lemma B of the shared section: interfaces confirmed at each
  use (W1, W2); proofs not reviewed here.
- [[problems/divisors/E0018/_index|Problem 18]], Statement: question (a) as
  targeted.
- Tenenbaum, Ann. Inst. Fourier 37 (1987), no. 2, Théorème 1 and the
  admissible sequences $\exp(-(\log k)^\beta)$, $\beta<3/2$: not held,
  unread; consumed only in the form the section quotes from a text layer.
- Berend and Harmse, Ann. Inst. Fourier 43 (1993), no. 3: the statement on
  p. 572 and Remark 2 as quoted: not held, unread.
- The site comment of 14 September 2026: not read; its form is consumed as
  the section quotes it.
- Chebyshev and prime number theorem facts, $\psi(x)\sim x$ and
  $\pi(x)\sim x/\log x$, standard and used as stated.

## Findings

- F1 (required). Lead, "Consequential gap": "with a constant $3/c$ (or $1/c$
  with the comment's recurrence in the lower range and the same mirror
  argument)"; connections, after S3: "so the constant $3/c$ above is a
  bookkeeping loss, not a mathematical one". Defect: the mirror argument's
  upper range costs $(1/c+o(1))(\log x)^2$ under $(\mathrm H_c)$ (W2), so
  the named argument gives $2/c$; only $3/c$ against $2/c$ is bookkeeping.
  Replacement: "with a constant $3/c$, or $2/c$ when the upper range is
  counted by the recurrence on $U=L_x/R$ instead of Lemma B's dyadic
  partition"; and "the factor $3/2$ is a bookkeeping loss".
- F2 (required). Connections, "Next investigation": "a disproof (a sequence
  of $x$ with $\kappa_{\min}(x)\to0$) shows that the greedy route along
  $L_x$ gives only $(\log x)^2/\kappa_{\min}(x)$"; lead, "Consequential
  gap": "would show that the greedy route along $L_x$ cannot give
  $(\log x)^2$, leaving Lemma B's $x/(\log x)^{3/2-\eta}$ from Tenenbaum's
  input as the route's best". Defect: no argument is given and the
  implication does not follow; an isolated pair with small $\kappa$ costs
  the greedy count one step per range (Strongest attack, S10), and Lemma
  B's bound depends on the whole profile through $3\int d\ell/\sigma$.
  Replacement: "would show that no hypothesis of the form $(\mathrm H_c)$
  with a fixed $c$ holds, so (18a.1) as stated gives nothing; whether a
  scale-dependent profile still gives $(\log x)^2$ through Lemma B would
  remain open".
- F3 (required). Connections, "Exploratory computation": "It does not
  decrease over this range" and "the binding pairs sit in the middle of the
  range, where the largest $\log(b/d)$ falls from $2.8\cdot10^{-2}$ at
  $x=20$ to $4.5\cdot10^{-5}$ at $x=64$"; lead, "Exploratory computation":
  "The largest $\log(b/d)$ in the middle tenth falls from ... and the
  binding pairs sit in the middle of the range", "$\kappa_{\min}(x)$ does
  not decrease over the sample". Defect: the binding pairs sit at the top of
  the range in which $\kappa$ is computed, within a factor $2.6$ of
  $\sqrt{L_x}$; the two maxima quoted are those of the top tenth of the
  range of $\log\sqrt{db}$ over $[\log x,\log\sqrt{L_x}]$, the lead's own
  definition of the tenths, while the middle tenths at $x=64$ have maxima
  $3.3\cdot10^{-4}$ and $1.9\cdot10^{-4}$; and the table itself shows
  $1.311$ at $x=40$ followed by $1.298$ at $x=50$. Witness: the positions
  listed under Strongest attack, S9. Replacement: "the binding pairs sit at
  the top of the range, within a factor of about $2.6$ of $\sqrt{L_x}$ (the
  middle of the full divisor range of $L_x$), where the largest
  $\log(b/d)$ in the top tenth falls from $2.8\cdot10^{-2}$ at $x=20$ to
  $4.5\cdot10^{-5}$ at $x=64$"; "$\kappa_{\min}(x)$ shows no downward trend
  over the sample; it dips once, from $1.311$ at $x=40$ to $1.298$ at
  $x=50$".
- F4 (required). Connections, proof of (18a.1): "$\delta\le2x^{-4}\le1/8$".
  Defect: $\delta(T)=2T^{-c/\log x}=2e^{-4}$, and $2e^{-4}>2x^{-4}$ for every
  $x\ge3$. Replacement: "$\delta\le2e^{-4}<1/8$". The conclusion and the
  verdict on S2 are unaffected.
- F5 (suggested). Connections, "Scale of the hypothesis", and lead,
  "Mean-gap scale": "says that the largest gap matches the mean gap up to a
  polynomial factor at every scale above $x$". Defect: at scale $x^m$ the
  hypothesis allows a gap $e^{-cm}$ of constant size against a mean log-gap
  of order $x^{-m}$, and at the top scale its allowance exceeds the mean
  gap by $\exp(\Theta(x/(\log x)^2))$ even at $c=2\log2$ (Strongest attack,
  S8); the content of $(\mathrm H_c)$ is concentrated near $\sqrt{L_x}$.
  Replacement: "with $c$ near $2\log2$, $(\mathrm H_c)$ is at the mean-gap
  scale near $\sqrt{L_x}$, where the exponent $-(c/2)x/\log x$ it allows and
  the exponent $-(\log2)x/\log x$ of the mean gap agree to first order; at
  scale $x^m$ it allows gaps $e^{-cm}$ of constant size against a mean gap
  of order $x^{-m}$, so it is far from a mean-gap statement below the top".
- F6 (suggested). Lead, "Next step": "A result for the middle alone would
  already cover the range that dominates the integral of Lemma B." Defect:
  under the route's profile $\sigma(\ell)=c\ell/\log x$ the integral is
  uniform in $\log\ell$ and no range dominates (Strongest attack, S11); the
  sentence also conflates the middle of the full divisor range, $\sqrt{L_x}$,
  which is the top of Lemma B's range, with the middle of that range.
  Replacement: "under $(\mathrm H_c)$ every factor-of-$e$ range of scales
  contributes equally to the integral, so a result near $\sqrt{L_x}$ alone
  covers only $O(\log x)$ of the $(\log x)^2$ count; it is nevertheless the
  range where $(\mathrm H_c)$ is tightest and where the computation finds
  the binding pairs".
- F7 (note). Connections, "What it does not give": "nothing unconditional
  beyond $h(L_x)\ll x/(\log x)^{3/2-\eta}$"; lead, "Provisional premise":
  "Three facts about it are established on the connections page" (the third
  rests on the text-layer readings the page itself marks for verification);
  lead, "Exploratory computation": "The computation distinguishes a quickly
  vanishing constant ... from a stable one". Replacement: "unconditional on
  $(\mathrm H_c)$, modulo the Tenenbaum import"; "two facts are proved and
  one is read from unverified text layers"; "would begin to distinguish".

## Verdict

- S1: refutation-failed.
- S2: refutation-failed; its written proof carries the slip F4, whose
  corrected form was verified.
- S3: refutation-failed, given the form of the comment's bound as the
  section quotes it.
- S4: refutation-failed.
- S5: proof defective; statement unresolved. The argument named gives
  $2/c$; whether $1/c$ can be reached from $(\mathrm H_c)$ by another count
  is open.
- S6: refutation-failed as a conditional deduction from the quoted
  admissibility statement; the imported statements are unverified here.
- S7: refutation-failed.
- S8: refuted-as-stated, under the reading in which the sentence has
  content; its precise part, $c\le2\log2$, stands as S7.
- S9: refutation-failed for every printed value; refuted-as-stated for the
  location of the binding pairs, the labeling of the quoted maxima, and
  "does not decrease".
- S10: proof defective; statement unresolved. The obstruction is asserted
  without proof and its witness does not defeat the route it names.
- S11: refuted-as-stated for the route's own profile.
- S12: refutation-failed, with the qualification of F7.

Limitations. The three external imports (Tenenbaum 1987, Berend and Harmse
1993, the site comment) were consumed as quoted; the papers are not held and
the web was excluded. The retained script was not run; the values were
reproduced by an independent enumeration that is not retained. The proofs of
Lemmas A and B were checked at their interfaces only. The section's account
of the problem page's status and of the accepted bounds was not checked.
This focused review assigns no tier and changes no status.
