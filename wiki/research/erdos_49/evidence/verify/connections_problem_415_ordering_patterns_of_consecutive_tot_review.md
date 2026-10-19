---
name: research/erdos_49/evidence/verify/connections_problem_415_ordering_patterns_of_consecutive_tot_review
title: "Independent review of the connections section: Problem 415: ordering patterns of consecutive totients"
desc: |
  Refutation-failed for the transfer statement, the stated obstruction, the
  Theorem 1.5 restatement and the deduction that F(n) = o(log_3 n); the target
  and provenance sentences are not claims. Zero required corrections, one
  suggested wording correction and four notes.
created: 2026-09-28T18:16:00Z
updated: 2026-09-28T18:16:00Z
---

***

## Subject and independence

Role: independent reviewer in a fresh context, charged with refutation. The
reviewer took no part in writing the page under review, the reconstruction
pages of the folder, the library card or the problem page, received only the
assignment text, and read no review, grade, standing, assessment or
known-results text. No web source was consulted.

Subject: `wiki/research/erdos_49/connections.md` as it stood on
2026-09-28T13:50:48Z, the section headed "## Problem 415: ordering patterns of
consecutive totients", lines 562--598 (the H2 at line 562 through the line
before the next H2 at line 599). Lead pages: none. The section names no lead,
and the two leads named in the page header carry Problems 1004 and 417, not
Problem 415.

Reading, with depth:

- The section, clause by clause, every sentence attacked.
- The page's header (title, desc, introduction, Standing and Outcomes at a
  glance, lines 1--57) and its section "Notation and the inputs used" (lines
  58--111), as inputs; their interfaces confirmed where the section uses
  them, their proofs not checked.
- The page's section "Problem 1004: distinct totients on a consecutive
  block" (lines 112--254), read for the exact statement of Proposition 1
  (lines 128--135), which the section consumes; the proof of Proposition 1
  was not re-derived, being another reviewer's charge.
- [[problems/arithmetic_functions/E0415/_index|Problem 415]]: the statement block
  under the H1 (lines 13--51) only, clause by clause; the heading names of
  the rest of the page were seen in a heading listing, their content not
  read.
- The card
  [[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/_index|Pollack, Pomerance and Treviño (2013)]]:
  its provenance paragraph, its read-status paragraph and its Contents entry
  for Theorem 1.5; the card has no result page for Theorem 1.5.
- The held PDF (author manuscript, 17 pages): page 3 (Theorems 1.3--1.5 and
  the Notation paragraph) on the page image and the text layer; Section 8
  (pages 12--15, the proof of Theorem 1.5 and Remark 8.1) on the text layer,
  page 12 also on the page image.
- `docs/verification.md` ("Grading and claim standing", the shared and the
  repository audit checklists, "Whole-claim report"),
  `docs/approach_vetting.md`, `docs/evidence.md` ("Source fidelity") and
  `docs/math_authoring.md`.

Exposures, disclosed: (1) the whole Problem 1004 section was read to locate
Proposition 1, so its proof and its "What it does not give", "Relation to the
retained note" and "Next investigation" paragraphs reached the reviewer;
(2) the card's index page was read in full, so its Contents list beyond the
Theorem 1.5 entry and its "Relation to E49" section reached the reviewer;
(3) a file listing of the research folder showed the names, and only the
names, of the existing review files under its evidence folder. None of this
is review, grade, standing, assessment or known-results text, and none of it
bears on a verdict below.

## Restatement

Conventions. $\varphi$ is Euler's function. $\log_k$ is the $k$-th iterate of
the natural logarithm (the source's Notation, p. 3), so $\log_3n$ is the
problem's $\log\log\log n$. Asymptotic symbols refer to $x\to\infty$ or
$n\to\infty$. A *pattern* of length $k$ is a permutation $\sigma$ of
$\{1,\ldots,k\}$; the block $\varphi(m+1),\ldots,\varphi(m+k)$ *realizes*
the pattern $\sigma$ when
$\varphi(m+\sigma(1))<\varphi(m+\sigma(2))<\cdots<\varphi(m+\sigma(k))$.
The problem's "any of the $k!$ possible ordering patterns appears" is read as
"each of them appears", the only reading under which $F(n)$ is not trivial;
the section reads it the same way. $R^\downarrow(x)$ denotes the maximum
number of consecutive integers contained in $[1,x]$ on which $\varphi$ is
nonincreasing, and $R^\uparrow(x)$ the same with nondecreasing.

- **S1 (target restatement; not a claim).** For $n\ge1$, $F(n)$ is the
  largest $k\ge1$ such that for every pattern $\sigma$ of length $k$ there is
  an integer $m\ge0$ with $m+k\le n$ whose block realizes $\sigma$. The
  problem asks (Q1) whether $F(n)=(c+o(1))\log_3n$ for some constant $c$;
  (Q2) whether the decreasing pattern
  $\varphi(m+1)>\varphi(m+2)>\cdots>\varphi(m+k)$ is always the first
  pattern to fail to appear; (Q3) whether the pattern of
  $\varphi(1),\ldots,\varphi(k)$ is the most frequent. The section adds that
  the corpus page is open, was accessed 2026-09-04, and is not compiled
  beyond the statement.
- **S2 (what transports).** Fix $c<2$. For all large $x$, with
  $L=\lfloor(\log x)^c\rfloor$, all but $o(x)$ of the starts $n\le x$ have
  $\varphi(n+1),\ldots,\varphi(n+L)$ pairwise distinct (Proposition 1,
  author-recorded, complete relative to (T1) and (T3)); every such block
  carries a strict total order and realizes exactly one of the $L!$ patterns.
- **S3 (obstruction, three clauses).** (a) Questions Q1--Q3 concern block
  lengths on the scale $\log_3n$, far below the block lengths $(\log x)^c$
  of S2. (b) Q1 requires every pattern to occur, and Q2, Q3 compare patterns;
  a collision bound, which constrains only how often $\varphi(m)=\varphi(m+h)$,
  says nothing about which pattern a block realizes. (c) Controlling the
  order of consecutive totients is a construction problem treating small,
  medium and large primes separately, the method of the source's Section 8,
  which is not among the reconstructed parts.
- **S4 (source restatement).** Theorem 1.5 of the source, recorded as a
  statement on the primes card, gives
  $R^\downarrow(x)=\log_3x/\log_6x+O(\log_3x/(\log_6x)^2)$.
- **S5 (deduction).** For all large $n$, $F(n)\le R^\downarrow(n)$, hence
  $F(n)\le(1+o(1))\log_3n/\log_6n$ and $F(n)=o(\log_3n)$; therefore
  $F(n)=(c+o(1))\log_3n$ fails for every constant $c>0$, so Q1 has a
  negative answer for every $c>0$.
- **S6 (provenance; not a claim).** The site's page for the problem, read
  2026-09-28 and last edited 28 May 2026, records the consequence S5; the
  corpus page, accessed 2026-09-04, does not.
- **S7 (outcome; not a claim).** The two mechanisms of the reconstruction
  transfer nothing to Q1--Q3; S5 is a library-level fact for the page
  compilers, not a transfer; the page header lists Problem 415 among the
  failures.

## Checklist

- **Quantifiers and scope.** Pass. S2 keeps Proposition 1's "all but $o(x)$"
  and its fixed $c<2$; nothing is upgraded to "all". S5 quantifies its
  conclusion over $c>0$ only, which is exactly what the bound supports, since
  the case $c=0$ is the bound itself (Finding F3). One wording overstatement
  in S3(a), "lengths of order $\log\log\log n$", where the section's own S5
  gives $o(\log_3n)$; not load-bearing (Finding F1).
- **Circularity.** Pass. S5 deduces a bound on $F$ from a published theorem
  about runs of monotonicity whose statement does not involve $F$ or the
  patterns; S2 consumes Proposition 1, which does not involve patterns.
- **Model and convention changes.** Pass. The only convention bridge is from
  the problem's strict decreasing pattern to the theorem's nonincreasing run,
  and the section states it ("a strictly decreasing run is nonincreasing").
  The reading of "ordering patterns" as strict orders is the problem's own
  and is stated in the Restatement above.
- **Finite and statistical overreach.** Inapplicable; the section contains no
  computation, sample or heuristic.
- **Uniformity.** Pass. The only asymptotics are in one variable ($x$ or
  $n$); Theorem 1.5's $o(1)$ is as $x\to\infty$ with no other parameter, and
  S5 applies it at $x=n$. Proposition 1's constant depends on the fixed $c$,
  and S2 does not claim uniformity in $c$.
- **Extremal conclusions.** Pass. $F(n)$ is a maximum; existence and
  finiteness are derived in Weakest step 1, and S5 uses only that the
  maximum belongs to the set it maximizes over. Theorem 1.5's maximum is used
  as an upper bound for one particular run, which is its weak direction.
- **Consequences and composition.** Pass. Each "hence" was re-derived
  separately: distinct values give exactly one pattern (S2); the run bound
  gives $F(n)\le R^\downarrow(n)$, the asymptotic form and $o(\log_3n)$, and
  the negative answer for $c>0$ (S5). The composition consumes Theorem 1.5 as
  published, at statement depth, and the section says so ("outside this
  reconstruction", "recorded as a statement").
- **Computation.** Inapplicable; none in the section.
- **Reproduction.** Inapplicable; no rerun instructions or coverage claims in
  the section.
- **Source and verdict fidelity.** Pass for everything inside the read set:
  Theorem 1.5 matches the PDF (p. 3 image and text layer) with the source's
  $(\alpha-\gamma+o(1))$ coefficient faithfully weakened to $O(\cdot)$; the
  card's Contents entry matches the PDF; the Section 8 characterization
  matches p. 12; the target restatement matches the problem page's statement
  except for the dropped phrase "for some constant $c$" (Finding F2). The
  site-page sentences (S6) and "not compiled beyond the statement" (S1) lie
  outside the read set and were not checked; they carry no mathematics.

## Weakest steps

**Weakest step 1: from the definition of $F(n)$ to a nonincreasing run.**
Let $n\ge1$ and let $K_n$ be the set of $k\ge1$ such that every pattern of
length $k$ is realized by some block with $m\ge0$ and $m+k\le n$. Then
$1\in K_n$ (take $m=0$; the single pattern of length 1 is realized by
$\varphi(1)$), and $K_n\subseteq\{1,\ldots,n\}$ because $k>n$ admits no
$m\ge0$ with $m+k\le n$. So $F(n)=\max K_n$ exists and $1\le F(n)\le n$. Put
$k=F(n)$. Since $k\in K_n$, the decreasing pattern $\sigma(i)=k+1-i$ is
realized: there is $m\ge0$ with $m+k\le n$ and
$\varphi(m+1)>\varphi(m+2)>\cdots>\varphi(m+k)$. The set
$\{m+1,\ldots,m+k\}$ consists of $k$ consecutive integers, lies in $[1,n]$
because $m+1\ge1$ and $m+k\le n$, and $\varphi$ is strictly decreasing on it,
hence nonincreasing. Therefore $F(n)=k\le R^\downarrow(n)$. This composes
with S5 as its first inequality. The step is robust to the direction of
monotonicity: had the problem's decreasing pattern been read with the
opposite sign, the run would be nondecreasing and Theorem 1.5 gives
$R^\uparrow$ the same estimate.

**Weakest step 2: the asymptotic form and the negative answer.** By Theorem
1.5, as $n\to\infty$,

$$
R^\downarrow(n)
=\frac{\log_3n}{\log_6n}\Bigl(1+\frac{\alpha-\gamma+o(1)}{\log_6n}\Bigr)
=(1+o(1))\frac{\log_3n}{\log_6n},
$$

because $\log_6n\to\infty$. With step 1, $F(n)\le(1+o(1))\log_3n/\log_6n$,
so $F(n)/\log_3n\le(1+o(1))/\log_6n\to0$, that is $F(n)=o(\log_3n)$. If
$F(n)=(c+o(1))\log_3n$ for a constant $c$, then $F(n)/\log_3n\to c$, so
$c=0$. Hence the relation fails for every $c>0$ (and for every $c<0$, since
$F(n)\ge1$ and $\log_3n>0$ for large $n$ give $F(n)/\log_3n\ge0$). The case
$c=0$ is the bound just proved, so the section's restriction to $c>0$ is
exact and not an omission. The section's "$O(\log_3x/(\log_6x)^2)$" is
implied by the source's $(\alpha-\gamma+o(1))\log_3x/(\log_6x)^2$, since
$\alpha-\gamma+o(1)$ is bounded.

**Weakest step 3: the interface of Proposition 1 and the pattern count.**
Proposition 1 (lines 128--135) states: for integer-valued $L(x)$ with
$2\le L(x)\le(\log x)^2/(\log\log x)^{50}$, the number of $1\le n\le x$ for
which $\varphi(n+1),\ldots,\varphi(n+L)$ are not pairwise distinct is $o(x)$;
in particular, for every fixed $c<2$ and all large $x$, all but $o(x)$ of the
$n\le x$ have $\varphi(n+1),\ldots,\varphi(n+\lfloor(\log x)^c\rfloor)$
pairwise distinct. The section's "for $c<2$ almost every block of length
$(\log x)^c$" is this "in particular" clause with the floor omitted, the
blocks being indexed by their starts $n\le x$; the hypothesis $L\ge2$ holds
for $c>0$ and large $x$, and for $c\le0$ a block of length at most 1 is
trivially tie-free. Given pairwise distinct reals $a_1,\ldots,a_L$, the
relation $a_i<a_j$ is a strict total order on $\{1,\ldots,L\}$, and a finite
strict total order has exactly one increasing enumeration; so exactly one
permutation $\sigma$ satisfies $a_{\sigma(1)}<\cdots<a_{\sigma(L)}$. A block
with a tie realizes no pattern under the strict reading, so the "exactly one"
uses the distinctness hypothesis and nothing else. The step composes with S3
only as context: the section draws no conclusion about $F$ from it.

## Strongest attack

- **S2.** Attempted: a block that realizes two patterns, or none, under the
  hypothesis; a use of Proposition 1 outside its stated range of $L$; a
  uniformity in $c$ read into "for $c<2$". All fail: distinctness forces a
  unique increasing enumeration (step 3); $L=\lfloor(\log x)^c\rfloor$ lies
  in the stated range for large $x$ when $c<2$, as Proposition 1 itself
  records; the section's quantifier matches the proposition's fixed $c$.
- **S3.** Attempted: to extract order information from the collision inputs.
  (T1) and (T3) bound $\#\{m\le x:\varphi(m)=\varphi(m+h)\}$ and Proposition 1
  bounds the number of starts whose block has a tie; every such statement is
  invariant under any relabeling of block values that preserves equalities,
  so none can distinguish one tie-free pattern from another, and S3(b) holds
  as a scope statement (the section claims no countermodel, so the
  countermodel test of the vetting page does not apply). S3(a): for every
  fixed $c>0$, $\log_3n/(\log n)^c\to0$, so the scales are separated; the
  only defect found is the wording "of order $\log\log\log n$" (Finding F1),
  which S5 itself shows to be an overstatement. S3(c): Section 8 of the PDF
  (p. 12) partitions the primes into small ($\le k$), medium-sized
  ($k<p\le\tfrac12\log x$) and large ($>\tfrac12\log x$) classes and builds
  the run by the Chinese remainder theorem; the upper bound (pp. 14--15) uses
  the same classes; the reconstruction pages of the folder cover Theorems
  3.1, 3.3, Lemma 3.2, Lemma 4.1, Lemma 5.1 and Theorem 1.2 only. The attack
  fails.
- **S4.** Attempted: a misstatement of the theorem's direction, error term,
  or object. The PDF (p. 3) states the nonincreasing case first and extends
  the same estimate to nondecreasing; "maximum size of a set of consecutive
  integers contained in $[1,x]$" is the section's "longest run of consecutive
  integers in $[1,x]$"; the error term is weakened, not changed. The card's
  Contents entry records the theorem with the source's coefficient and says
  Theorem 1.5 was read as a statement only, which is what "recorded as a
  statement" asserts. The attack fails.
- **S5.** Attempted: (i) the run might not lie in $[1,n]$ (it does, by
  $m\ge0$ and $m+k\le n$); (ii) $F(n)$ might not be attained or might not
  force the decreasing pattern (step 1); (iii) the direction of monotonicity
  (immaterial, both directions have the same estimate); (iv) the passage from
  $\log_3n/\log_6n$ to $o(\log_3n)$ (step 2); (v) the literal question admits
  $c=0$, for which the relation is true, so a flat "negative answer" would be
  wrong; the section says "for every $c>0$", which is exactly right (Finding
  F3 asks only that the degenerate case be named). The attack fails.
- **S1, S6, S7.** Not claims. S1 was checked against the problem page's
  statement block and is faithful apart from the dropped phrase "for some
  constant $c$" (Finding F2); its "open, accessed 2026-09-04" matches the
  statement block. S6 lies outside the read set. S7 restates S2--S5 and the
  header's outcome line consistently.

## Premises

- **Proposition 1** (`wiki/research/erdos_49/connections.md`, Problem 1004
  section, lines 128--135, in the subject state): author-recorded; the page
  states its proof is complete relative to (T1) and (T3). Interface used:
  fixed $c<2$, large $x$, all but $o(x)$ starts $n\le x$, block length
  $\lfloor(\log x)^c\rfloor$. Statement read; proof not re-derived (another
  reviewer's charge). The section consumes it at exactly this interface.
- **(T1), (T3)** (page's Notation section, lines 80--92): consumed by the
  section only through Proposition 1; interfaces read, not used directly.
- **Theorem 1.5 of Pollack, Pomerance and Treviño (2013)**, held as the
  author manuscript beside the card (the published pagination is not held,
  as the card's provenance paragraph states): statement on p. 3, read on the
  page image and the text layer; proof in Section 8, pp. 12--15, read on the
  text layer for its structure (three prime classes, Chinese remainder
  construction, Mertens-type products), p. 12 also on the image; Remark 8.1
  (p. 15) read on the text layer. Consumed as published; the proof was not
  verified, and the section does not claim otherwise.
- **The primes card**
  [[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/_index|Pollack, Pomerance and Treviño (2013)]]:
  provenance paragraph (journal, volume, pages, DOI, manuscript status,
  download provenance), read-status paragraph ("Theorems 1.1, 1.3, 1.4 and
  1.5 were read as statements only") and the Contents entry for Theorem 1.5,
  read in full and checked against the PDF: they agree.
- **[[problems/arithmetic_functions/E0415/_index|Problem 415]]**: the statement
  block under the H1 (lines 13--51), read clause by clause; it carries the
  definition of $F(n)$, the three questions, "Status. Open.", "accessed
  2026-09-04" and the reference [PPT13] with the same journal, year and
  pages as the card. Nothing else on the page was read.
- **Reconstruction pages** (`theorem_3_1_reconstruction.md`,
  `theorem_3_3_reconstruction.md`, `lemma_3_2_reconstruction.md`,
  `lemma_4_1_reconstruction.md`, `lemma_5_1_reconstruction.md`,
  `theorem_1_2_reconstruction.md`): not consumed by the section directly and
  not read; their file names were used only to confirm that Section 8 of the
  source is not among the reconstructed parts (S3(c)).
- **Lead pages**: none for this section; not read.
- **Explicit assumptions**: the reading of "any of the $k!$ possible
  ordering patterns appears" as "each of them appears", stated in the
  Restatement; no other assumption.

## Findings

- **F1 (suggested).** Location: "The pattern questions live at lengths of
  order $\log\log\log n$, far below the collision scale". Defect: "of order
  $\log\log\log n$" overstates the scale at which every pattern occurs; the
  section's own S5 gives $F(n)\le(1+o(1))\log_3n/\log_6n=o(\log_3n)$, so the
  sentence is true only of the problem's conjectured scale, not of the
  proved one, and a reader taking the strongest reading finds the two
  paragraphs in tension. Witness: S5 as re-derived in Weakest step 2. Not
  load-bearing: with $o(\log_3n)$ the separation from $(\log x)^c$ is only
  wider. Proposed replacement: "The pattern questions live at the problem's
  own scale $\log\log\log n$, and by the background note below at lengths at
  most $(1+o(1))\log_3n/\log_6n$, far below the collision scale".
- **F2 (note).** Location: "asks whether $F(n)=(c+o(1))\log\log\log n$".
  Defect: the problem page asks this "for some constant $c$"; the section
  drops the quantifier on $c$, which the later hedge "for every $c>0$"
  answers. Witness: the statement block of the problem page. Proposed
  replacement: "asks whether $F(n)=(c+o(1))\log\log\log n$ for some
  constant $c$".
- **F3 (note).** Location: "the first question has a negative answer for
  every $c>0$". Not a defect: the restriction to $c>0$ is exact. The literal
  question admits $c=0$, for which the displayed relation is the bound
  itself, so a compiler transcribing "negative answer" without the
  restriction would err. Proposed addition: "(for $c=0$ the relation is the
  bound itself, so the question survives only in that degenerate form)".
- **F4 (note).** Location: the background paragraph's first use of
  $\log_3x$ and $\log_6x$. Defect: the page nowhere defines $\log_k$ (it is
  also used undefined at line 104 of the Notation section), while the target
  paragraph writes $\log\log\log n$. Proposed replacement: add "with
  $\log_k$ the $k$-th iterated logarithm" at the first use in the section,
  or define it once in the page's Notation section.
- **F5 (note).** Location: "they ask that *every* pattern occur". Defect:
  only Q1, through the definition of $F(n)$, asks that every pattern occur;
  Q2 asks which pattern fails first and Q3 which is most frequent. The
  obstruction covers all three, since each is about which patterns occur and
  how often. Proposed replacement: "they ask which patterns occur, which
  fails first and which is most frequent".

## Verdict

- **S1** (target restatement): not a claim; faithful to the problem page's
  statement apart from F2.
- **S2** (what transports): refutation-failed.
- **S3** (obstruction): refutation-failed, with the wording correction F1
  suggested and F5 noted.
- **S4** (Theorem 1.5 restatement): refutation-failed.
- **S5** (deduction $F(n)=o(\log_3n)$, negative answer for every $c>0$):
  refutation-failed.
- **S6** (provenance): not a claim; outside the read set, not checked.
- **S7** (outcome): not a claim; consistent with S2--S5.

Required corrections: none. Suggested: one (F1). Notes: four (F2--F5).

Limitations. Theorem 1.5 is consumed as published; its proof was read only
for the structure that S3(c) describes and was not verified, and the corpus
records the theorem at statement depth, so S5 inherits exactly that
standing, as the section says. Proposition 1's proof was not re-derived
here. The sentences about the site's page (S6), the claim that the corpus
page is "not compiled beyond the statement", and the header's outcome line
for the other problems were not checked. The review is of one section; the
page's Standing paragraph governs the whole page and was read only as an
input.

This focused review assigns no tier and changes no status.
