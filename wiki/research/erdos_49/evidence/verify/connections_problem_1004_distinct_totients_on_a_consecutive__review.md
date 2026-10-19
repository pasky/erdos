---
name: research/erdos_49/evidence/verify/connections_problem_1004_distinct_totients_on_a_consecutive__review
title: "Independent review of the connections section: Problem 1004: distinct totients on a consecutive block"
desc: |
  Refutation-failed for Proposition 1, its corollary, its four steps, the
  exponent-2 barrier, the Poisson prediction, the computation and the
  standing sentences; refuted-as-stated for the "and no further" reach
  clause; proof defective, statement unresolved for the conditional
  "almost all blocks contain a collision" deduction. One required
  correction, two suggested, five notes.
created: 2026-09-28T18:17:15Z
updated: 2026-10-07T21:41:29Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, given only the
commissioning assignment. The reviewer took no part in writing the
connections page, the lead page, or the reconstruction pages, and had
read none of them, none of the folder's evidence, and no review of any
section before this assignment. Charge: refutation.

**Frozen subject.** The repository as it stood on 2026-09-28T13:50:48Z.
Page `wiki/research/erdos_49/connections.md`, section
`## Problem 1004: distinct totients on a consecutive block`, lines
112--254 (the heading is line 112; the next H2 is line 255). Lead page
`wiki/research/leads/distinct_totient_blocks_from_collision_bounds/_index.md`,
all 146 lines, whose route rests on that section.

**Reading and depth.**

- The section in full, every line, with every displayed inequality
  re-derived below.
- The page's shared sections as inputs only: lines 1--111 (frontmatter,
  preamble, the Standing paragraph, Outcomes at a glance, and "Notation
  and the inputs used"). Their proofs were not reviewed; the interfaces
  of (T1) and (T3) were confirmed against the held source at each use.
  Inputs (L4), (F) and (P) are not used by the section and were not
  checked.
- The reconstruction pages `theorem_3_1_reconstruction.md`,
  `theorem_3_3_reconstruction.md`, `lemma_3_2_reconstruction.md` and
  `theorem_1_2_reconstruction.md` in the same state, in full, as
  premises at their stated standing; the Lemma 4.1 and Lemma 5.1 pages
  were not read (not used by the section).
- `wiki/problems/arithmetic_functions/E1004/_index.md`, the Statement at line
  17 (see the exposure below).
- The card
  [[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/_index|Pollack, Pomerance and Treviño (2013)]]:
  its provenance and digest paragraphs (first 60 lines) and its
  `theorem_3_1.md` and `theorem_3_3.md` pages in full. The held 17-page
  manuscript, pages 5--7, read by text extraction: Theorem A, Theorem B,
  Theorem C, Theorem 3.1 with its sketch, Lemma 3.2, Theorem 3.3 with its
  proof, Remarks 3.1 and 3.2. The copy under the primes card was checked
  to be the same bytes as the copy under the arithmetic-functions card.
- `docs/verification.md` ("Grading and claim standing", the canonical
  audit checklist, "Whole-claim report", "Audit checklist", "Durable
  reports and current standing"), `docs/approach_vetting.md` in full,
  `docs/evidence.md` "Source fidelity", `docs/math_authoring.md` in full.

**Independent computation.** The exploratory computation quoted by the
section was rerun from a fresh implementation written for this review (a
totient sieve and a sliding window of pairwise distinct values), for
blocks inside $[1,N]$ and inside $[2,N]$, at $N=10^5,10^6,10^7$. The
script is not retained; its method is stated under Checklist item 8.

**Exposure.** The problem page was printed as the line range 1--80
instead of its Statement alone, so its Status, Source, References and
Formalization lines (21--43) and the first part of its "Current
assessment" section (lines 44--80) reached the reviewer. That text
contains no review, grade or standing of the subject; no finding rests on
it, and the section's characterization of the current assessment (lines
116--122) is not assessed here. The Standing paragraph of the connections
page preamble and the lead's "Current review state" section were read as
parts of the named subjects; both say author-recorded and unreviewed and
carry no verdict. No evidence-folder content, no other section's review,
no workspace content, and no web page was read; the section's statements
about the site's discussion thread and about the retained note's pages
are therefore outside this review. A working-tree status listing showed
the file names of other sections' review reports under the folder's
`evidence/verify/`; none was opened.

## Restatement

Conventions used throughout. $\varphi$ is Euler's function. For real $x$
and a natural number $k$, $P(x;k)$ counts the positive integers $n\le x$
with $\varphi(n)=\varphi(n+k)$; $P_0(x;k)$ counts those of the form of
Theorem A of the source for some admissible $j$ and $r$, and
$P_1=P-P_0$. For even $k$, $c(k)$ is the source's constant (3.2), and
$C_2$ is the source's normalization of the twin-prime constant. For real
$x\ge1$ and an integer $L\ge2$, $B(x,L)$ is the number of integers
$1\le n\le x$ for which some pair $1\le i<j\le L$ has
$\varphi(n+i)=\varphi(n+j)$, and $S(L)=\sum_{h\le L,\ h\text{ even}}c(h)$.
The inputs are (T1) and (T3) exactly as the shared section states them,
confirmed against the source in the Premises.

- **S1** (Proposition 1, main clause; author-recorded, relative to (T1)
  and (T3)). For every integer-valued function $L(x)$ with
  $2\le L(x)\le(\log x)^2/(\log\log x)^{50}$ for all large $x$,
  $B(x,L(x))=o(x)$ as $x\to\infty$.
- **S2** (Proposition 1, corollary). For every fixed $0<c<2$,
  $B(x,\lfloor(\log x)^c\rfloor)=o(x)$; hence for all large $x$ some
  $n\le x$ has $\varphi(n+1),\ldots,\varphi(n+\lfloor(\log x)^c\rfloor)$
  pairwise distinct, so the question of Problem 1004 has the answer yes
  for every fixed $c<2$, relative to (T1) and (T3).
- **S3** (Step 1; unconditional). For all real $x\ge1$ and integers
  $L\ge2$, with $y=x+L$,
  $B(x,L)\le\sum_{h=1}^{L-1}(L-h)P(y;h)\le L\sum_{h=1}^{L-1}P(y;h)$.
- **S4** (Step 2). There is an absolute $x_1$ such that for $x\ge x_1$,
  every integer $2\le L\le(\log x)^2$ and every $1\le h\le L-1$, with
  $y=x+L$: $P_1(y;h)<y\exp(-(\log y)^{1/3})$; $P_0(y;h)=0$ for odd $h$;
  and $P_0(y;h)\le(16C_2+1)c(h)y/(\log y)^2$ for even $h$. Consequently
  $\sum_{h=1}^{L-1}P(y;h)\le Ly\exp(-(\log y)^{1/3})+(16C_2+1)S(L)y/(\log y)^2$.
- **S5** (Step 3). There is an absolute constant $A_0$ with
  $S(L)\le A_0(\log L)^{49}$ for every integer $L\ge2$.
- **S6** (Step 4). For $x\ge x_1$ and $2\le L\le(\log x)^2/(\log\log x)^{50}$,
  $B(x,L)\le2x\bigl[(\log x)^4e^{-(\log x)^{1/3}}+(16C_2+1)A_0L(\log L)^{49}/(\log x)^2\bigr]$,
  and the bracket is at most
  $(\log x)^4e^{-(\log x)^{1/3}}+(16C_2+1)A_02^{49}/\log\log x$, which
  tends to $0$; this bound is uniform in $L$ over the range.
- **S7** (the barrier at exponent 2). Since $c(h)\ge1/(2h)$ for even
  $h$ by (T3), the bound of S3 fed with (T3)'s termwise upper bound is at
  least of order $L\log L\cdot x/(\log x)^2$ whatever upper bound for
  $S(L)$ is used, so this route cannot give $B(x,L)=o(x)$ once
  $L\log L\gg(\log x)^2$. (The section attributes this order to "the
  second term of Step 2"; F2.)
- **S8** (reach with the sharper average). If $\sum_{h\le L}c(h)\ll\log L$
  held, the same argument would give S1 for every
  $L\le(\log x)^2/(\log\log x)^{1+\delta}$ with fixed $\delta>0$, "and no
  further".
- **S9** (scope of the barrier). The barrier is a limit of the union
  bound and not a proved obstruction to the target; it would become one
  only with a matching lower bound $P_0(x;h)\gg c(h)x/(\log x)^2$, a
  prime-pair statement that is not available.
- **S10** (conditional deduction). If that lower bound holds, the expected
  number of collisions inside a block of length $L$ at a uniformly random
  start $n\le x$ is of order $L\log L/(\log x)^2$; therefore, for
  $L=(\log x)^c$ with $c>2$, all but $o(x)$ of the starts $n\le x$ have a
  collision in their block, and only atypical starts can answer the
  question. (Lead page: "so for $c>2$ almost all blocks fail".)
- **S11** (Poisson prediction, stated as a heuristic). Under a Poisson
  model for the positions of collisions with the count of S10, the
  longest collision-free block below $x$ has length $(\log x)^{3+o(1)}$;
  under that model the every-$c$ form fails for $c>3$.
- **S12** (exploratory computation, author-recorded, not filed). The
  longest block of consecutive integers with pairwise distinct totients
  below $N=10^5,10^6,10^7$ has length $111$, $194$, $321$; for comparison
  $(\log N)^2=133,191,260$ and $(\log N)^3/\log\log N=625,1004,1506$.
- **S13** (relation to the retained note). Proposition 1 needs no average
  estimate beyond the $(\log L)^{49}$ of Step 3, which follows from the
  bound on $c(k)$ stated in (T3), so the $c<2$ answer rests on (T1) and
  (T3) alone.
- **S14** (lead page, route summary and provenance). The union bound
  costs at most $L\sum_{h<L}P(x+L;h)$ bad starts; the odd shifts and the
  unstructured part of the even shifts are $o(x)$ by Theorem 3.1 for every
  $L\le(\log x)^2$; the structured part is
  $(16C_2+o(1))L\sum_{h<L}c(h)x/(\log x)^2$; the upper bound on $c(k)$
  gives $\sum_{h\le L}c(h)\ll(\log L)^{49}$; the proposition has no
  provisional premise beyond the two published theorems and inherits the
  sketch status of Theorem 3.1 and the unreviewed status of the deduction.
- **S15** (structured shape, "Next investigation" (2) and the lead's next
  step 2). Every solution counted by $P_0(y;h)$ has the form $m=jq$,
  $m+h=(j+h)p$ with $q=br+1$ and $p=ar+1$ prime, where
  $g=\gcd(j,j+h)$, $a=j/g$, $b=(j+h)/g$ and $j$, $j+h$ have the same
  prime factors.
- **S16** (standing sentences). Proposition 1 is author-recorded, proved
  "complete relative to (T1) and (T3)", assigns no tier and changes no
  status; the outcome line reads "Transfers for every $c<2$; open for
  $c\ge2$"; the lead is marked candidate and unreviewed.

## Checklist

1. **Quantifiers and scope.** Proposition 1 is an almost-all statement
   and is consumed only as one; the passage to existence in S2 needs only
   $B(x,L)<x$ for large $x$, which $o(x)$ gives. Boundary $L=2$ is handled
   in Step 3. The hypothesis of S1 is written for all $x$ while the
   corollary meets it only for large $x$ (F7, note). The one place where
   "almost all" is asserted from a first moment is the conditional clause
   S10 (F1). Verdict: pass for S1--S9 and S11--S16; defect at S10.
2. **Circularity.** None. The inputs concern single shifts $h$ and
   nothing about blocks is assumed. Pass.
3. **Model and convention changes.** The move from blocks at $x$ to
   shifted collisions at $y=x+L$ is bridged by S3, and the return to $x$
   by $y\le2x$ and $\log y\ge\log x$. $P_0(y;h)=0$ for odd $h$ rests on
   the parity of $j$ and $j+h$ in Theorem A. $c(h)$ is defined for even
   $h$ only and the section's sums are over even $h$; the lead's sums are
   not restricted (F6, note). The Poisson model is labeled a heuristic;
   the first-moment-to-almost-all clause in S10 is the one unlabeled
   substitution (F1). Pass except S10.
4. **Finite and statistical overreach.** The computation is quoted with
   the disclaimer that its range cannot separate the exponents and with
   the statement that it was made after the heuristic; no inference is
   drawn from it. Pass.
5. **Uniformity.** (T1)'s $x_0$ is absolute; (T3)'s $o(1)$ is uniform in
   $k$ for the fixed choice $\varepsilon(y)=(\log y)^{-1/2}$; $A_0$ is
   absolute; every "large $x$" threshold in Steps 2--4 depends on $x$
   alone, so the bound in S6 is uniform in $L$ over the whole range,
   which is more than the proposition states. The uniformity in $k$ of
   the sieve term inside (T3) is imported by the Theorem 3.3
   reconstruction from the source and is a published-theorem premise
   here. Pass.
6. **Extremal conclusions.** The reach claim "and no further" in S8 is
   checked in its own units and fails in its fine print (F3, with
   witness). The barrier S7 is computed in the claim's own units and
   holds. Pass with F3.
7. **Consequences and composition.** S2 from S1: valid. "So the $c<2$
   answer rests on (T1) and (T3) alone": also Mertens' bound and parity
   (F5, note). S10's "so": does not follow (F1). Inherited premises (the
   sketch status of Theorem 3.1; the sieve constant and uniformity inside
   Theorem 3.3) are disclosed by the section and the lead. Pass except
   S10.
8. **Computation.** Rerun independently: a sieve of $\varphi$ on
   $[1,N]$ and, for each right endpoint, the longest window ending there
   with pairwise distinct values (last-occurrence bookkeeping). Results:
   $111$ (start $73318$), $194$ (start $900979$), $321$ (start
   $9491695$), identical for windows inside $[1,N]$ and inside $[2,N]$;
   the comparison values recompute to $132.5$, $190.9$, $259.8$ and
   $624.5$, $1004.2$, $1506.3$, which round as quoted. Pass.
9. **Reproduction.** No rerun command is stated and no output is filed;
   the computation was reproduced from a fresh implementation, not from
   any cached output. Pass at the "author-recorded, not filed" scope.
10. **Source and verdict fidelity.** (T1) and (T3) as consumed match the
    manuscript, pages 6--7: absolute $x_0$ and $k\le\exp((\log x)^{1/3})$
    for all natural $k$; even $2\le k\le x^{\varepsilon(x)}$ with
    $\varepsilon(x)\to0$ and $x^{\varepsilon(x)}\to\infty$; the factor
    $(16C_2+o(1))$ "uniformly in $k$"; and
    $(2k)^{-1}\le c(k)\le3\cdot7^{3+2\omega(k)}\prod_{p\mid k,\,p>2}\frac{p-1}{p-2}\cdot k^{-1}$.
    Theorem A's shape matches S15. The lead's restatement of Theorem 3.3
    omits the two conditions on $\varepsilon$ (F6). The standing
    sentences claim author-recorded only. The section's statements about
    the site's discussion thread, the retained note's pages and the
    problem page's current assessment lie outside the read set and are
    not assessed. Pass with notes.

## Weakest steps

**W1. Step 2: applying (T3) to every even shift at once at the shifted
point.** Let $x$ be large, $2\le L\le(\log x)^2$ and $y=x+L$, so
$\log y\ge\log x$ and $y\to\infty$ with $x$. Put
$\varepsilon(y)=(\log y)^{-1/2}$: it is positive, tends to $0$, and
$y^{\varepsilon(y)}=\exp(\sqrt{\log y})\to\infty$, so (T3) applies with
this $\varepsilon$. Its range is $2\le h\le\exp(\sqrt{\log y})$, and every
even $h\le L-1$ lies in it because
$L\le(\log x)^2\le(\log y)^2\le\exp(\sqrt{\log y})$ once
$2\log\log y\le\sqrt{\log y}$, which holds for all large $y$. Uniformity
in $k$ means: there is $\delta(y)\to0$ with
$P_0(y;h)\le(16C_2+\delta(y))c(h)y/(\log y)^2$ for every even $h$ in the
range; for large $y$, $\delta(y)\le1$, and the threshold depends on $y$
alone, hence on $x$ alone. (T1) applies to every natural $h\le L-1$
because $L-1<(\log y)^2\le\exp((\log y)^{1/3})$ for large $y$, needing
$2\log\log y\le(\log y)^{1/3}$; and $y>x_0$. For odd $h$ no $j$ has the
same prime factors as $j+h$ (one of them is even and the other odd), so no
solution has Theorem A's form and $P_0(y;h)=0$, $P(y;h)=P_1(y;h)$.
Summing over $h$, with $\sum_{h\le L-1,\,h\text{ even}}c(h)\le S(L)$ by
nonnegativity, gives the display of S4. This composes with S3 by
multiplying by $L$, which loses only a constant against the sharper
$(L-h)$ weights.

**W2. Step 3: the average of $c(h)$.** By (T3),
$c(h)\le3\cdot7^3\cdot49^{\omega(h)}\prod_{p\mid h,\,p>2}\frac{p-1}{p-2}\cdot h^{-1}=3\cdot7^3g(h)/h$
with $g$ multiplicative, $g(1)=1$, $g(2^a)=49$ and
$g(p^a)=49\frac{p-1}{p-2}$ for $p>2$, $a\ge1$. Since $g\ge0$ and every
$h\le L$ has all prime factors at most $L$, expanding the product
$\prod_{p\le L}(1+\sum_{a\ge1}g(p^a)p^{-a})$ produces every term $g(h)/h$
with $h\le L$ at least once, and
$\sum_{a\ge1}g(p^a)p^{-a}=g(p)\sum_{a\ge1}p^{-a}=g(p)/(p-1)$ because
$g(p^a)=g(p)$. The factor at $p=2$ is $1+49=50$ and at $p\ge3$ it is
$1+49\cdot\frac{p-1}{p-2}\cdot\frac1{p-1}=1+\frac{49}{p-2}$. With
$1+t\le e^t$ and $\frac1{p-2}=\frac1p+\frac{2}{p(p-2)}$,
$\sum_{3\le p\le L}\frac1{p-2}\le\sum_{p\le L}\frac1p+\sum_{p\ge3}\frac{2}{p(p-2)}\le\log\log L+O(1)$
for $L\ge3$ by Mertens' bound, the second sum converging. So
$\sum_{h\le L}g(h)/h\le50e^{O(1)}(\log L)^{49}$ and
$S(L)\le3\cdot7^3\sum_{h\le L}g(h)/h\le A_0(\log L)^{49}$ for $L\ge3$;
at $L=2$ the left side is $c(2)$, finite by (T3), and $\log2>0$, so a
larger absolute $A_0$ covers it. This composes with S4 by substitution and
with S6 through $\log L\le2\log\log x$, which follows from
$L\le(\log x)^2$.

**W3. Step 1: the union bound and the return to $x$.** If $n$ is counted
by $B(x,L)$, choose the least pair $(i,j)$ with $1\le i<j\le L$ and
$\varphi(n+i)=\varphi(n+j)$; set $m=n+i$, $h=j-i$. Then $1\le h\le L-1$,
$\varphi(m)=\varphi(m+h)$, and $m=n+i\le x+j-h\le x+L-h<y$, so $m$ is
counted by $P(y;h)$. The map $n\mapsto(m,h,i)$ is injective ($n=m-i$),
and for fixed $(m,h)$ the index $i$ ranges over $1\le i\le L-h$ (from
$j=i+h\le L$), so at most $L-h$ values of $n$ share a pair $(m,h)$. This
is S3. In Step 4, $y=x+L\le x+(\log x)^2\le2x$ and $\log y\ge\log x$ give
$L^2ye^{-(\log y)^{1/3}}\le2x(\log x)^4e^{-(\log x)^{1/3}}$ and
$L(16C_2+1)S(L)y/(\log y)^2\le2x(16C_2+1)A_0L(\log L)^{49}/(\log x)^2$;
the first tends to $0$ relative to $x$, and the second is at most
$2x(16C_2+1)A_02^{49}/\log\log x$ under
$L\le(\log x)^2/(\log\log x)^{50}$ and $(\log L)^{49}\le(2\log\log x)^{49}$,
both factors being nonnegative. This is S6, and S1 follows.

## Strongest attack

**S1--S6.** Attacks tried: (a) push the largest shift $h=L-1$ outside
(T3)'s range, defeated because $(\log y)^2\le\exp(\sqrt{\log y})$ for
large $y$ with an absolute threshold; (b) push it outside (T1)'s range,
defeated likewise by $(\log y)^2\le\exp((\log y)^{1/3})$; (c) make
(T3)'s $o(1)$ depend on $h$, defeated by the theorem's stated uniformity
in $k$ for a fixed $\varepsilon$; (d) make the threshold "large $x$"
depend on $L$, defeated because every threshold is a condition on $x$ or
$y$ alone; (e) inflate $S(L)$, defeated by the Euler product, which caps
it at $(\log L)^{49}$, against which the hypothesis spends a
$(\log\log x)^{50}$ with a margin of $2^{49}/\log\log x$; (f) the case
$L=2$, covered; (g) odd shifts, covered by parity and by (T1)'s
statement for all natural $k$; (h) overcount in S3, defeated by the
injectivity of $n\mapsto(m,h,i)$; (i) the passage from $o(x)$ bad starts
to the target's existence form, which needs only $B(x,L)<x$. No attack
succeeded. Everything is relative to (T1) and (T3) as published.

**S7.** Replacing the crude factor $L$ by the sharper weights $L-h$ does
not help, since for $L\ge4$
$\sum_{h<L,\,h\text{ even}}(L-h)c(h)\ge\sum_{h\le L/2,\,h\text{ even}}\frac L2\cdot\frac1{2h}\gg L\log L$
by the lower bound $c(h)\ge1/(2h)$. The barrier holds.

**S8.** The attack succeeded on the clause "and no further". With
$S(L)\ll\log L$ the bound is $\ll L\log L\cdot x/(\log x)^2+o(x)$, which is
$o(x)$ exactly when $L\log L=o((\log x)^2)$. The witness
$L=\lfloor(\log x)^2/(\log\log x\cdot\log\log\log x)\rfloor$ satisfies
$L\log L\le2(\log x)^2/\log\log\log x=o((\log x)^2)$, so the same union
bound gives $B(x,L)=o(x)$ for it, while it exceeds
$(\log x)^2/(\log\log x)^{1+\delta}$ for every fixed $\delta>0$ and all
large $x$. The exponent-2 content survives: for
$L\ge\kappa(\log x)^2/\log\log x$ with fixed $\kappa>0$ the bound is
$\gg\kappa x$, not $o(x)$.

**S9.** Read as a necessity claim ("only with"), it survives: any
obstruction along this route needs many collisions. Read as sufficiency,
it has the defect of S10.

**S10.** The attack succeeded on the deduction. The hypothesis controls a
first moment, the expected number of collision pairs per block. The
number of collision-free starts depends on how the collision points are
distributed, which a first moment does not control. Abstract witness: put
$\rho x$ points of $[1,x]$ in runs of $K$ consecutive integers,
$\rho x/K$ runs. At most $(\rho x/K)(L+K)=\rho x(L/K+1)$ starts have a
window of length $L$ meeting a run; with $\rho=\log L/(\log x)^2$,
$L=(\log x)^c$ and $K=(\log x)^{c-1}$ this is
$\ll x\log L/\log x=o(x)$, while the number of points, hence the
first-moment count per block, equals that of an evenly spread
configuration. So the conclusion needs an input on the spacing of
collision points at scale $L$ (a second moment, or the Poisson model that
the next clause introduces), which the stated hypothesis does not supply.
The section itself says under "Next investigation" (2) that a gap
statement needs more than first moments. The conditional statement
concerns the actual function $\varphi$ and cannot be refuted by a
configuration; only its supplied deduction fails.

**S11.** Re-derived under the model. Collision points below $x$ number
$\asymp x\Sigma(L)/(\log x)^2$ with $\log L\ll\Sigma(L)\ll(\log L)^{49}$
under (T3) and the lower bound, so the density is
$\rho=(\log x)^{-2+o(1)}$; the longest gap of $\rho x$ Poisson points in
$[1,x]$ is $\rho^{-1}\log(\rho x)=(\log x)^{3+o(1)}$, and a collision-free
block of length $(\log x)^c$ exists under the model exactly when this
exceeds $(\log x)^c$, that is for $c<3$ and not for $c>3$. The $o(1)$
absorbs the uncertainty in $\Sigma(L)$. Survives as a model statement.

**S12.** Reproduced; see Checklist item 8.

**S13.** "Alone" overlooks Mertens' bound and the parity fact, both
classical and elementary; the mathematical content (no average estimate
beyond (T3)'s own bound is needed) survives.

**S14.** Re-derived from S3--S6; the sentence "The structured part is
..." states an upper bound as an equality (F6). Survives otherwise.

**S15.** From Theorem A with $k=h$: $n=jq$, $q=br+1$, and
$(j+h)p=(j+h)(ar+1)=gabr+j+h=jbr+j+h=n+h$. Survives.

**S16.** Every standing sentence claims author-recorded and no more.
Survives.

## Premises

- **(T1) Theorem 3.1** of Pollack, Pomerance and Treviño, *Sets of
  monotonicity for Euler's totient function*, Ramanujan J. 30 (2013);
  held manuscript page 6; read by text extraction. Interface: there is an
  absolute $x_0$ with $P_1(x;k)<x/\exp((\log x)^{1/3})$ for $x>x_0$,
  uniformly for natural numbers $k\le\exp((\log x)^{1/3})$. The source
  marks the argument a sketch; the reconstruction page records the sketch
  and its one written deduction and notes that solutions with the largest
  prime factor dividing its cofactor are not disposed of by the sketch.
  Used within hypotheses (every $h\le L-1$, at $y>x_0$).
- **(T3) Theorem 3.3** of the same source, pages 6--7; held; read.
  Interface: for positive $\varepsilon(x)\to0$ with
  $x^{\varepsilon(x)}\to\infty$ and even $2\le k\le x^{\varepsilon(x)}$,
  $P_0(x;k)\le(16C_2+o(1))c(k)x/(\log x)^2$ uniformly in $k$; and
  $(2k)^{-1}\le c(k)\le3\cdot7^{3+2\omega(k)}\prod_{p\mid k,\,p>2}\frac{p-1}{p-2}\cdot k^{-1}$.
  The reconstruction imports Selberg's sieve with its constant and its
  uniformity as the source states them and Evertse's bound through Lemma
  3.2. Used within hypotheses with $\varepsilon(y)=(\log y)^{-1/2}$.
- **Lemma 3.2** of the source, page 6; enters only through (T3)'s upper
  bound on $c(k)$; reconstruction page read in full.
- **Theorem A** of the source, page 5 (quoted there from Graham, Holt and
  Pomerance); supplies the parity fact $P_0(x;k)=0$ for odd $k$ (also
  step 2 of the Theorem 1.2 reconstruction page, read) and the structured
  shape of S15.
- **Mertens' bound** $\sum_{p\le L}1/p\le\log\log L+O(1)$ for $L\ge3$:
  classical, not held, used as stated.
- **Reconstruction pages** as they stood on 2026-09-28T13:50:48Z:
  author-recorded, taken as premises at their stated standing per the assignment
  (reviewed as they stood on 2026-09-28T05:03:27Z with corrections applied
  since). The section uses them within their hypotheses.
- **Problem 1004** statement, `E1004.md` line 17: for fixed $c>0$ and
  all large $x$, is there $n\le x$ with $\varphi(n+k)$, $1\le k\le(\log x)^c$,
  pairwise distinct; the block has length $\lfloor(\log x)^c\rfloor$ and
  S2 addresses exactly this form.
- Not used by the section: (L4), (F), (P) of the shared inputs.
- No batch acceptance order; no other assumptions.

## Findings

**F1** (required). Location: section lines 210--215, "If that lower
bound holds, as the Hardy--Littlewood heuristic predicts, the expected
number of collisions inside a block of length $L$ at a random start
$n\le x$ is of order $L\log L/(\log x)^2$, so for $c>2$ almost all blocks
contain a collision and only atypical starts can answer the question";
lead lines 110--113, "a random block of length $L$ contains of order
$L\log L/(\log x)^2$ collisions, so for $c>2$ almost all blocks fail and
only atypical starts can answer the question". Defect: the conclusion
"almost all blocks contain a collision" does not follow from the stated
hypothesis; a lower bound for a first moment does not bound the number
of collision-free starts, which depends on the spacing of the collision
points at scale $L$. Witness: the clustered configuration under S10 in
"Strongest attack", with the same first moment and $o(x)$ bad starts. The
lead's "contains of order" also states a typical value where only an
expectation is available, and "of order" needs the unverified average
$\sum_{h\le L}c(h)\ll\log L$ for its upper half; (T3) alone gives "at
least of order". Proposed replacement (section): "If that lower bound
holds, as the Hardy--Littlewood heuristic predicts, the expected number of
collisions inside a block of length $L$ at a random start $n\le x$ is at
least of order $L\log L/(\log x)^2$. A first moment does not decide how
many blocks are collision-free. Under a Poisson model for the positions
of collisions, for $c>2$ almost all blocks contain a collision and only
atypical starts can answer the question, and the same model predicts a
longest collision-free block below $x$ of length $(\log x)^{3+o(1)}$, so
under it the every-$c$ form would fail for $c>3$." The lead's sentence
takes the same repair.

**F2** (suggested). Location: section lines 202--204, "so whatever
average bound for $c(h)$ is used, the second term of Step 2 is at least
of order $L\log L\cdot x/(\log x)^2$". Defect: the second term of the
Step 2 display is $(16C_2+1)S(L)y/(\log y)^2$, which is at least of order
$\log L\cdot x/(\log x)^2$; the order $L\log L\cdot x/(\log x)^2$ belongs
to the bound on $B(x,L)$ after Step 1's factor $L$, that is to the second
term of Step 4. The barrier itself is correct. Proposed replacement: "so
whatever average bound for $c(h)$ is used, the bound on $B(x,L)$ obtained
in Step 4 is at least of order $L\log L\cdot x/(\log x)^2$".

**F3** (suggested). Location: section lines 205--207, "would extend
Proposition 1 to $L\le(\log x)^2/(\log\log x)^{1+\delta}$ and no
further"; lead lines 95--96, the same clause. Defect: the reach of the
union bound with the sharper average is exactly the $L$ with
$L\log L=o((\log x)^2)$; the witness
$L=\lfloor(\log x)^2/(\log\log x\cdot\log\log\log x)\rfloor$ lies beyond
$(\log x)^2/(\log\log x)^{1+\delta}$ for every fixed $\delta>0$ and is
still covered. Proposed replacement: "would extend Proposition 1 exactly
to the $L$ with $L\log L=o((\log x)^2)$, for instance
$L\le(\log x)^2/(\log\log x)^{1+\delta}$ for fixed $\delta>0$, and to no
$L\ge\kappa(\log x)^2/\log\log x$ with fixed $\kappa>0$". A further
observation for the lead: at $L=\kappa(\log x)^2/\log\log x$ with a small
fixed $\kappa$, that union bound would still leave a positive proportion
of good starts, which answers the target's existence form though not
the almost-all form; the exponent-2 barrier is unchanged by either
remark.

**F4** (note). Location: section line 124 and lead line 63, "the union
bound over the $\binom L2$ shifts of a block of length $L$". A block of
length $L$ has $\binom L2$ pairs and $L-1$ shifts. Replacement: "over the
$\binom L2$ pairs, grouped by their $L-1$ shifts,".

**F5** (note). Location: section line 232, "the $c<2$ answer rests on
(T1) and (T3) alone"; lead lines 93--95, "rests on the two published
theorems alone". Step 3 also uses Mertens' bound and Step 2 the parity
fact; both are classical and elementary. Replacement: "rests on (T1) and
(T3) together with Mertens' bound and the parity of Theorem A's shape".

**F6** (note). Lead page. Lines 49--51 restate Theorem 3.3 as "uniformly
for even $k\le x^{\varepsilon(x)}$" without the conditions
$\varepsilon(x)\to0$ and $x^{\varepsilon(x)}\to\infty$ that the section
states; add them. Line 66, "The structured part is
$(16C_2+o(1))L\sum_{h<L}c(h)\,x/(\log x)^2$": an upper bound, so "is at
most". Lines 64--68 write $\sum_{h<L}c(h)$ and $\sum_{h\le L}c(h)$ over
all $h$ while $c(h)$ is defined for even $h$ only; restrict the sums to
even $h$ as the section does.

**F7** (note). Location: section lines 128--130, the hypothesis
"$2\le L(x)\le(\log x)^2/(\log\log x)^{50}$", read for all $x$, and
lines 195--196, "For fixed $c<2$, $L=\lfloor(\log x)^c\rfloor$ satisfies
the hypothesis for large $x$". Either write the hypothesis "for all large
$x$" or remark that the conclusion is insensitive to $L$ on a bounded
range. The proof also gives more than the statement: the bound of Step 4
is uniform in $L$ over the range, so
$\sup_{2\le L\le(\log x)^2/(\log\log x)^{50}}B(x,L)=o(x)$, which the
proposition could state.

**F8** (note). The section's statements about the site's discussion
thread (lines 232--235), the retained note's pages 2--3 (lines
226--229) and the problem page's current assessment (lines 116--122) are
outside this review's read set and carry no verdict here.

## Verdict

- S1 (Proposition 1, main clause): **refutation-failed**, relative to
  (T1) and (T3) as published.
- S2 (corollary; the answer yes for every fixed $c<2$): **refutation-failed**,
  relative to (T1) and (T3).
- S3 (Step 1): **refutation-failed**.
- S4 (Step 2): **refutation-failed**.
- S5 (Step 3): **refutation-failed**.
- S6 (Step 4): **refutation-failed**.
- S7 (the barrier at exponent 2): **refutation-failed**; the term named
  in the sentence is wrong (F2).
- S8 (reach with the sharper average, "and no further"):
  **refuted-as-stated** in its "no further" clause, by the witness
  $L=\lfloor(\log x)^2/(\log\log x\cdot\log\log\log x)\rfloor$ (F3); the
  exponent-2 content survives.
- S9 (scope of the barrier): **refutation-failed** as the necessity
  claim it states.
- S10 (conditional deduction of "almost all blocks contain a
  collision"): **proof defective; statement unresolved** (F1).
- S11 (Poisson prediction, as a model statement): **refutation-failed**.
- S12 (computation): **refutation-failed**; reproduced.
- S13 (relation to the note): **refutation-failed**; "alone" omits two
  elementary inputs (F5).
- S14 (lead route summary and provenance): **refutation-failed**; wording
  notes (F4, F6).
- S15 (structured shape): **refutation-failed**.
- S16 (standing sentences): **refutation-failed**; no sentence claims
  more than author-recorded.

**Limitations.** Every survival is relative to (T1), whose proof the
source gives as a sketch that the reconstruction page does not complete,
and to (T3), whose reconstruction imports the sieve constant and its
uniformity from the source; the section and the lead disclose both. The
retained note's claimed average, the site's discussion thread and the
characterization of the problem page's current assessment were not
examined. The required correction (F1) touches a heuristic paragraph and
leaves Proposition 1, its proof and the outcome line unchanged. This
focused review assigns no tier and changes no status.
