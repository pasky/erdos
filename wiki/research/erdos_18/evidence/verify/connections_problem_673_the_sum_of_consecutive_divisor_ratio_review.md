---
name: research/erdos_18/evidence/verify/connections_problem_673_the_sum_of_consecutive_divisor_ratio_review
title: "Independent review of the connections section: Problem 673: the sum of consecutive divisor ratios"
desc: |
  Refutation-failed for the target restatement, the density-zero obstruction,
  the factorial bound, the even-n bound and the non-transfer verdict; the
  recorded bound tau(n/m)/m <= G(n) is refuted-as-stated at m = 1. One
  required correction (restrict that bound to m >= 2), one suggested, one
  note.
created: 2026-09-28T18:10:29Z
updated: 2026-09-28T18:11:28Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, given only the
assignment; the reviewer took no part in writing the page, the folder's
reconstruction pages, or their earlier reviews, and read none of the folder's
existing reviews or grades. Charge: refutation. This is a focused review of
one section; it assigns no tier and changes no status.

**Subject.** Page `wiki/research/erdos_18/connections.md` as it stood at
2026-09-28T13:50:48Z, section "## Problem 673: the sum of consecutive divisor
ratios", lines 693–715 (the heading at line 693, the Target paragraph at lines
695–702, the Outcome paragraph at lines 704–714, the next H2 at line 716). The
section names no lead page; the page's opening paragraphs (lines 19–45, the
conventions at lines 32–45) and its "Shared lemmas" section (lines 47–243) are
its inputs.

**Reading.** The section in full. The conventions paragraph and Lemma A
(statement, and the clause on $n!$ and $L_x$) as inputs whose interfaces were
confirmed at each use; Lemmas B, C, C′ and D only far enough to confirm that
every object they construct is practical; the page's "Sources read for this
page" section. The Lemma 4 reconstruction page in full, and the Proposition
4.1 reconstruction page's source and standing paragraphs, Statement, and the
iteration paragraph that defines $n_j=2^EV_j$; both as premises at their
recorded standing. The Statement block of `wiki/problems/divisors/E0673/_index.md`
(lines 11–37). The Weingartner card's provenance paragraph and the held PDF's
text layer, pp. 1–3 (Theorem 1, the definition of $D(x,t)$, the quoted Saias
bound, Theorem 3 and Corollaries 1–3). The held Erdős 1982 survey under
`library/discrete_geometry/erdos_1982_my_favourite_problems_which_recently_have`,
§6 (printed pp. 66–67, physical pages 8–9), in the text layer and on the page
images. The Erdős–Tenenbaum 1981 card's provenance paragraph and the text
layer of that paper's introduction and closing remarks. The named sections of
`docs/verification.md`, `docs/approach_vetting.md`, `docs/evidence.md` and
`docs/math_authoring.md`.

**Exposures.** The Statement block of the Problem 673 page carries the line
"**Status.** Proved." inside the block that was read; nothing else of that
page (no Current assessment, Known Results or library block) was read. No
evidence folder, review, grade or index page was read, and no web access was
used: the site page and the site comment that the section reports could not
be examined, and the held Erdős 1982 survey was used as the primary source in
their place.

## Restatement

- **S1 (target).** For $n\ge1$ with divisors $1=d_1<\cdots<d_{\tau(n)}=n$,
  $G(n)=\sum_{1\le i<\tau(n)}d_i/d_{i+1}$. Problem 673 asks (a) whether
  $G(n)\to\infty$ for almost all $n$, a density-one statement, and (b) for an
  asymptotic formula for $\sum_{n\le X}G(n)$ as $X\to\infty$. The section
  asserts that these are the two questions and that each quantifies over
  almost all $n$ or averages over $n\le X$.
- **S2 (record of sources).** The problem page records the status proved with
  no compiled assessment; the site page, read 2026-09-28, records (i) Erdős's
  1982 remark that question (a) is trivial, (ii) a site comment's bounds
  $\tau(n/m)/m\le G(n)\le\tau(n)$ for $m\mid n$, and (iii) the Erdős–Tenenbaum
  result that $G(n)/\tau(n)$ has a continuous distribution function. Read as
  mathematics, (ii) asserts: for every $n\ge1$ and every divisor $m$ of $n$,
  $\tau(n/m)/m\le G(n)\le\tau(n)$. This mathematical reading is S2b; the
  three records are S2a.
- **S3 (obstruction).** Every mechanism of the folder concerns the members of
  a single sequence: $n!$, $L_x=\mathrm{lcm}(1,\dots,x)$, or the
  $n_j=2^EV_j$ constructed on the Proposition 4.1 page; each such member is
  practical; the practical numbers have counting function
  $P(x)\sim cx/\log x$ (Weingartner, Theorem 1), hence density zero;
  therefore no density-one statement and no asymptotic for
  $\sum_{n\le X}G(n)$ can be transported from them.
- **S4 (factorial bound).** For every $n\ge1$, consecutive divisors of $n!$
  have ratio at most $2$, so every term satisfies $d_i/d_{i+1}\ge1/2$ and
  $G(n!)\ge(\tau(n!)-1)/2$; since $\tau(n!)\to\infty$, $G(n!)\to\infty$. This
  is a statement along the sequence $n!$ only and needs no gap estimate.
- **S5 (even-$n$ bound).** For every even $n$, $\tau(n)/4\le G(n)$, obtained
  from S2b at $m=2$.
- **S6 (non-transfer verdict).** Nothing in the folder bears on
  $\sum_{n\le X}G(n)$; no transfer to either question exists; no next
  investigation is proposed.

## Checklist

- **Quantifiers and scope.** S2b fails at the boundary $m=1$ for every $n$
  (finding F1); the section's own use of the bound is at $m=2$ and survives.
  The almost-all versus thin-sequence distinction is kept explicitly: the
  section states that S4 holds along $n!$ and transfers to neither question.
  Otherwise pass.
- **Circularity.** None: the section proves nothing about the target and
  assumes nothing equivalent to it. Pass.
- **Model and convention changes.** $G$ is the problem page's $G$, with the
  same index range $1\le i<\tau(n)$; Lemma A is applied to $n!$ through its
  own clause; practicality of $n_j$ is the Proposition 4.1 page's statement.
  Pass.
- **Finite and statistical overreach.** The section uses no finite check and
  no heuristic. The reviewer's computations below are attacks, not evidence
  for the page. Pass.
- **Uniformity.** The only asymptotic imported is Weingartner's Theorem 1,
  quoted at the shape $\sim cx/\log x$ with no constant claimed; the
  obstruction uses only $P(x)=o(x)$. Pass.
- **Extremal conclusions.** None asserted. Inapplicable.
- **Consequences and composition.** "So $G(n!)\ge(\tau(n!)-1)/2\to\infty$"
  and "already gives $\tau(n)/4\le G(n)$ for even $n$" are re-derived in
  Weakest steps; "which have density zero" follows from $P(x)\sim cx/\log x$;
  "all inside the practical numbers" holds for $n!$ and $L_x$ by Lemma A's
  stated clause and for $n_j$ by the Proposition 4.1 statement, consumed at
  its claimed standing. The obstruction itself does not need practicality:
  any single sequence has density zero. Pass.
- **Computation.** The section carries none. The reviewer's exact-rational
  checks agree with every elementary bound: for $n\le3000$ the lower bound of
  S2b holds for every divisor $m\ge2$ of $n$ and fails at $m=1$ for every
  $n$; $\tau(n)/4\le G(n)$ for every even $n\le3000$, with equality at $n=2$;
  for $2\le n\le10$ the largest consecutive-divisor ratio of $n!$ is exactly
  $2$ and $G(n!)\ge(\tau(n!)-1)/2$. Pass.
- **Reproduction.** The section states no rerun commands and no coverage
  claims. Inapplicable.
- **Source and verdict fidelity.** Weingartner's Theorem 1 was checked in the
  held PDF: for $x\ge3$, $P(x)=(cx/\log x)(1+O(\log\log x/\log x))$ with a
  positive constant $c$, which is the section's $\sim cx/\log x$. Erdős's
  remark was checked on the page images of the held 1982 survey, §6, printed
  p. 66: with $Q(n)=\sum_{i=1}^{\tau(n)-1}d_i/d_{i+1}$, which is $G$, "It is
  trivial that $Q(n)\to\infty$ for almost all $n$"; and printed p. 67: "In
  July 1981 at the number theory meeting in Budapest, Tenenbaum and I in fact
  proved that $Q(n)/\tau(n)$ has a continuous distribution function". Both
  match the section's characterizations. The site page and the site comment
  could not be read; the status "proved" does appear in the problem page's
  Statement block; the clause "no compiled assessment" was not checked. Pass
  for what could be checked, with F1 on the reported bound's range and F2 on
  provenance.

## Weakest steps

**W1: the lower bound of S2b, and its range.** Let $m\mid n$ with $m\ge2$.
Every divisor $e$ of $n/m$ is a divisor of $n$ with $e\le n/m<n$, and $em$ is
a divisor of $n$ with $em>e$; so the successor $e^+$ of $e$ among the divisors
of $n$ satisfies $e<e^+\le em$, that is, $e/e^+\ge1/m$. The $\tau(n/m)$
divisors of $n/m$ are distinct divisors of $n$ below $n$, so their terms are
distinct terms of $G(n)$ and $G(n)\ge\tau(n/m)/m$. The upper bound is
immediate: $G(n)$ has $\tau(n)-1$ terms, each below $1$, so
$G(n)<\tau(n)-1$ for $n\ge2$ and $G(1)=0$. This also shows that the lower
bound fails at $m=1$ for every $n$: it would read $\tau(n)\le G(n)$, while
$G(n)\le\tau(n)-1$. The step $em>e$ is exactly where $m\ge2$ is used.

**W2: S5 from W1.** Write an even $n$ as $2^ak$ with $a\ge1$ and $k$ odd.
Then $\tau(n)=(a+1)\tau(k)$ and $\tau(n/2)=a\,\tau(k)$, so
$\tau(n/2)/\tau(n)=a/(a+1)\ge1/2$. W1 at $m=2$ gives
$G(n)\ge\tau(n/2)/2\ge\tau(n)/4$. Equality holds at $n=2$
($G(2)=1/2=\tau(2)/4$). The bound composes with S4 as the section says: $n!$
is even for $n\ge2$, so $\tau(n!)/4\le G(n!)$ as well, weaker than
$(\tau(n!)-1)/2$ whenever $\tau(n!)\ge2$.

**W3: S4 and the ratio hypothesis.** Lemma A's clause states that its
hypothesis $v_2(N)\ge\lfloor\log_2p\rfloor$ for every odd prime $p\mid N$
holds for $N=n!$; the interface was checked at the small cases the clause
handles by inspection: $n=1,2$ have no odd prime factor, and $n=3$ has
$v_2(6)=1=\lfloor\log_23\rfloor$. Independently of Lemma A, the Lemma 4
reconstruction page supplies its own proof that consecutive divisors of $n!$
have ratio at most $2$ for $n\ge2$ ($n=1$ is vacuous). Either way
$d_{i+1}/d_i\le2$, so $d_i/d_{i+1}\ge1/2$ for each of the $\tau(n!)-1$
terms, and $G(n!)\ge(\tau(n!)-1)/2$; $\tau(n!)\ge n$ since $1,\dots,n$
divide $n!$, so the bound tends to infinity. The statement concerns the
sequence $n!$ alone, which has density zero, so it says nothing about
question (a); the section says exactly this.

## Strongest attack

- **S1.** Compared clause by clause with the Statement block of the problem
  page: the same $G$, the same index range, the same two questions. No
  discrepancy.
- **S2a.** The two attributions were attacked against the held primary
  source rather than the site: the 1982 survey confirms the remark and the
  announcement (Checklist, fidelity item). The survey announces the
  distribution result without a reference, and the held Erdős–Tenenbaum 1981
  paper does not contain it (its remarks on continuous distribution functions
  concern $\tau^+/\tau$ and $g/\tau$, both left conjectural there), so the
  published proof is not held; this is a provenance limitation (F2), not a
  contradiction. The site-record clauses themselves are unverifiable here.
- **S2b.** The boundary $m=1$ falsifies the bound as written: $n=2$, $m=1$
  gives $\tau(2)/1=2>G(2)=1/2$; W1 shows the failure is universal in $n$. The
  restricted bound ($m\ge2$) survives the same attack and the exact
  computation to $n\le3000$.
- **S3.** The attack tried to enlarge the mechanism's reach beyond the three
  sequences. Lemma A's conclusion and Lemma B's hypotheses concern every $N$
  whose consecutive divisors have ratio at most $2$, a set far larger than
  $\{n!\}\cup\{L_x\}\cup\{n_j\}$ (and not comparable with the practical
  numbers: $78=2\cdot3\cdot13$ is practical, since $13\le\sigma(6)+1$, but
  has the consecutive divisors $6<13$). Its counting function $D(x,2)$ still
  satisfies $c_3x\log2/\log2x\le D(x,2)\le c_4x\log2/\log2x$ (Saias's bound
  as quoted in Weingartner, with Weingartner's Corollary 1 giving the
  asymptotic), so it has density zero, and the only information on $G$ the
  mechanism yields there is the one-sided bound $G(N)\ge(\tau(N)-1)/2$. For
  the average, $\sum_{n\le X}G(n)$ has order $X\log X$ (from W2,
  $\sum_{n\le X,\,2\mid n}G(n)\ge\sum_{m\le X/2}\tau(2m)/4\ge\sum_{m\le X/2}\tau(m)/4$,
  and from the upper bound $G(n)\le\tau(n)$), so an asymptotic formula needs
  two-sided control of $G$ on a set carrying that sum, which no mechanism of
  the folder supplies: Lemma B consumes upper bounds on the ratios
  $\log(b/d)$ as its hypothesis and produces bounds on $h$, not on $G$, and
  the extension lemmas control $h$ only. The attack found no bridge to either
  question; the obstruction stands at the scope the section claims.
- **S4.** Attacked by exact computation for $n\le10$ (largest ratio exactly
  $2$ for $n\ge2$, the bound holding with room) and by re-deriving the ratio
  property's interface at $n\le3$ (W3). Fails to refute.
- **S5.** Attacked at the boundary $n=2$ (equality) and by exact computation
  to $n\le3000$; the derivation W2 is independent of the site. Fails to
  refute.
- **S6.** A scope statement; every route tried under S3 ends in a one-sided
  bound on a density-zero set. Fails to refute.

## Premises

- **Lemma A** (shared lemma of the reviewed page, lines 52–79): hypothesis
  $v_2(N)\ge\lfloor\log_2p\rfloor$ for every odd prime $p\mid N$; conclusion
  ratio at most $2$, $N$ practical, $h(N)\le\log_2N+1$; clause that the
  hypothesis holds for $n!$ and $L_x$. Used for the ratio property of $n!$
  and the practicality of $n!$ and $L_x$. Its proof belongs to another
  reviewer; the interface was confirmed at the use.
- **Lemma 4 reconstruction**
  ([[research/erdos_18/hughes_lemma_4_reconstruction|Lemma 4]], premise
  reviewed as of 2026-09-28T05:03:27Z, read in full): the greedy step for $N$
  with ratio at most $2$, its consequence clause (the greedy expansion writes
  every $1\le m\le N$ as a sum of distinct divisors, so such $N$ is practical),
  and the compilation-supplied proof that consecutive divisors of $n!$ have
  ratio at most $2$ for $n\ge2$. Used as an independent route to S4.
- **Proposition 4.1 reconstruction**
  ([[research/erdos_18/doorn_proposition_4_1_reconstruction|Proposition 4.1]],
  premise at *claimed* standing; source and standing paragraphs, Statement and
  the iteration paragraph read): defines $n_j=2^EV_j$ and states that each
  $n_j$ is practical. Used only for "inside the practical numbers"; S3 does
  not depend on it.
- **Weingartner (2015)**
  ([[../library/divisors/weingartner_2015_practical_numbers_distribution_divisors/_index|card]],
  PDF held; provenance paragraph and text layer pp. 1–3): Theorem 1,
  $P(x)=(cx/\log x)(1+O(\log\log x/\log x))$ for $x\ge3$; the definition of
  $D(x,t)$, Saias's two-sided bound (2), Theorem 3 and Corollaries 1–3, used
  only in the attack on S3.
- **Erdős (1982)**
  ([[../library/discrete_geometry/erdos_1982_my_favourite_problems_which_recently_have/_index|card]],
  PDF held; §6, printed pp. 66–67, physical pages 8–9, text layer and page
  images): the definition of $Q(n)$, the "trivial" remark, and the announced
  Erdős–Tenenbaum distribution result. Used for S2a.
- **Erdős–Tenenbaum (1981)**
  ([[../library/divisors/erdos_1981_sur_la_structure_de_la_suite/_index|card]],
  PDF held; provenance paragraph and the text layer of the introduction and
  closing remarks): does not contain the $G/\tau$ distribution result. Used
  for provenance only.
- **Problem 673 page** ([[problems/divisors/E0673/_index|Problem 673]], Statement
  block, lines 11–37): the definitions and the two questions.
- **Not held or not read:** the site page and the site comment reported by
  the section; the paper carrying the published proof of the distribution
  result; the problem page's assessment sections.

## Findings

- **F1** — required — lines 699–700, "a site comment's bounds
  $\tau(n/m)/m\le G(n)\le\tau(n)$ for $m\mid n$". Defect: the lower bound is
  false at $m=1$ for every $n$, since $G(n)$ is a sum of $\tau(n)-1$ terms
  each below $1$ (W1). Witness: $n=2$, $m=1$: $\tau(2)/1=2>G(2)=1/2$; the
  exact check fails at $m=1$ for all $n\le3000$. Replacement: "for
  $1<m\mid n$" (equivalently $m\ge2$), which is the range the derivation in
  W1 needs and the range the section's own use at $m=2$ occupies. The
  section's conclusions are unaffected. If the site comment itself states
  the bound without the restriction, the page should still carry it, since
  the corpus restates a source's bound with its range preserved.
- **F2** — suggested — lines 698–702, the record of Erdős's 1982 remark and
  of the Erdős–Tenenbaum result through the site page. The primary source of
  both is held: the 1982 survey, §6, printed pp. 66–67, where the remark
  reads "It is trivial that $Q(n)\to\infty$ for almost all $n$" and the
  distribution result is announced as proved in July 1981 without a
  reference; the held Erdős–Tenenbaum 1981 paper does not contain it. Cite
  the held survey for the remark, and describe the distribution result as
  announced there, since its published proof is not among the held sources.
- **F3** — note — line 706, "the constructed $2^EV_j$". The notation is not
  introduced in the page's conventions paragraph; it is the $n_j=2^EV_j$ of
  the Proposition 4.1 reconstruction. A link to that page, or the name
  $n_j$, would make the sentence self-contained.

## Verdict

- **S1 (target restatement):** refutation-failed.
- **S2a (records of the site page and the held survey):** refutation-failed
  for the two attributions, checked against the held 1982 survey; the
  site-record clauses are unverifiable within the read set.
- **S2b (the bound $\tau(n/m)/m\le G(n)\le\tau(n)$ for $m\mid n$):**
  refuted-as-stated at $m=1$ (F1); the restricted bound for $m\ge2$ is
  re-derived in W1 and survives.
- **S3 (density-zero obstruction):** refutation-failed.
- **S4 (factorial bound):** refutation-failed.
- **S5 (even-$n$ bound):** refutation-failed.
- **S6 (non-transfer verdict):** refutation-failed.

**Limitations.** The site page and the site comment were not read, so the
section's sentence about what the site records is checked only against the
held primary source; the clause "no compiled assessment" was not checked
because the problem page's assessment sections were excluded; the
Proposition 4.1 page was consumed at its claimed standing, which S3 does not
need; Lemma A's proof was not re-derived beyond its interface. The
mathematics of the section is elementary, and the outcome it records (no
transfer to either question) survives every attack tried.

This focused review assigns no tier and changes no status.
