---
name: research/erdos_354/evidence/verify/connections_problem_349_single_rays_and_the_digit_recurrence_review
title: "Independent review of the connections section: Problem 349: single rays and the digit recurrence"
desc: |
  Focused independent review, as of 2026-09-28T13:50:48Z, of the Problem 349
  section of the Problem 354 connections page: all six statements
  refutation-failed; zero required corrections, four suggested corrections
  and two notes.
created: 2026-09-28T18:30:56Z
updated: 2026-09-28T18:30:56Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, given only the
commissioning assignment. The reviewer took no part in writing the
connections page, the reconstruction pages, the library cards or the
problem page, and had no contact with their author. The charge is
refutation of the author-recorded statements of one section.

**Subject.** Page `wiki/research/erdos_354/connections.md` as it stood at
2026-09-28T13:50:48Z, section "Problem 349: single rays and the digit
recurrence", lines 441--489 (the H2 heading at line 441 through the line before
the next H2 at line 490), read from the committed bytes. Lead pages: none is
named for this section; the section names no lead of its own, and the lead that
the previous section records was not read.

**Reading and depth.**

- The section, in full, three times; the page's preamble (purpose,
  standing and notation, lines 1--58) as an input.
- Inside the same page but outside the section, two passages the section
  cites by name: the statement and proof of Lemma 354.4 (lines 194--212)
  and the "Next investigation" paragraph of the section on the second
  question at bases up to the plastic number (lines 292--440). Both were
  read only to check the section's cross-references; neither is reviewed
  here.
- Reconstruction pages of the folder as of the same time, as premises: the
  normalization page in full; the Lemma 2.2 (mesh lemma) page in full; the
  Theorem 9 page in full; the Theorem 5.1 page's Statement section and the
  opening of its Step 1 (the exact block's subset sums).
- [[problems/additive_bases/E0349/_index|Problem 349]]: the statement block only.
- Library: the provenance blocks of the
  [[../library/additive_bases/graham_nd_conjecture_erdos_additive_number_theory/_index|Graham card]]
  and the
  [[../library/additive_bases/doorn_2026_completeness_exponentially_increasing_sequences/_index|van Doorn (2026) card]];
  the
  [[../library/additive_bases/geneson_2026_deletion_thresholds_exponential_examples_complete_sequences/_index|Geneson (2026) card]]
  and its
  [[../library/additive_bases/geneson_2026_deletion_thresholds_exponential_examples_complete_sequences/theorem_9|Theorem 9 result page]]
  (see the exposures below).
- Held PDFs: Geneson's preprint, text layer of the abstract, the
  introduction (pp. 1--2) and Section 5 (pp. 11--12, Theorem 9, Lemma 10,
  Proposition 11 and the proof of Theorem 9); van Doorn's preprint, text
  layer of the definitions and conjecture (p. 1), Lemmas 3--5,
  Propositions 1, 2 and 8; Graham's paper, a scan without a text layer,
  read as page images of its first page (p. 63: the definition of
  $S_t(a)$, the conjecture and the square $0<t<1$, $1<a<2$) and its last
  page (p. 70: the conjecture for $1<a<(1+\sqrt5)/2$).
- Rules: the "Whole-claim report", "Audit checklist" and "Grading and claim
  standing" sections of the verification page, the approach-vetting page,
  the "Source fidelity" section of the evidence page and the math-authoring
  page.

**Exposures.** Four, none touching a review, grade or assessment of this
section:

1. The Geneson card was read whole, including its Overview and its
   "Bears on" paragraph, and the Theorem 9 result page was read whole,
   including its proof pointer, dependencies and "Bears on" list; the
   allowed reading was the card's provenance paragraph and the result
   page's statement. The "Bears on" text was used only to check S6, which
   quotes it.
2. The statement block of the Problem 349 page carries the line
   "Status. Open."; nothing further of that page was read.
3. A search for the objects named in the obstruction sentence returned
   three single lines of the folder's `_index.md` (lines 80, 190 and 207)
   and one line of an existing reconstruction review
   (`evidence/verify/yu_chen_theorem_5_1_reconstruction_review.md`,
   line 171); they concern the Theorem 5.1 objects and were not used.
4. A search for corpus records of van Doorn's Lemma 5 printed line
   fragments from unrelated research folders; they were not read further.

No evidence folder, folder index, current assessment, progress or known
results text and no web source was read otherwise.

## Restatement

The ray of coefficient $t>0$ at base $\gamma>0$ is
$(\lfloor t\gamma^n\rfloor)_{n\ge0}$ in the section's and the folder's
indexing; van Doorn indexes from $n=1$. A sequence is complete when every
sufficiently large integer is a sum of terms with distinct indices; for a
ray whose terms are all even the set and sequence conventions agree. For a
base-2 ray write $a_i=\lfloor2^i\alpha\rfloor$ and $u_i=a_{i+1}-2a_i$.

- **S1 (target and recorded literature).** Problem 349 asks for which
  $t,\alpha\in(0,\infty)$ the ray is complete. The held sources record:
  (a) Graham (1964) determines exactly which pairs in the square $0<t<1$,
  $1<\alpha<2$ give a complete ray; (b) van Doorn (2026) settles every base
  $\alpha\ge\varphi$; (c) van Doorn's Proposition 1: for $\alpha\notin[1,2]$
  no $t>0$ gives a complete ray, and his Proposition 2: at $\alpha=2$ the
  ray is complete if and only if $t=2^{-k}$ for an integer $k\ge1$ (his
  indexing from $n=1$); the section states the necessary direction "only
  $t=2^{-k}$" with no range for $k$; (d) Geneson's Theorem 9: at one Salem
  base $\gamma\in(6/5,13/10)$ there are arbitrarily large $t$ with every
  $\lfloor t\gamma^n\rfloor$ even, which refutes Graham's conjecture that
  every $t>0$ and $1<\alpha<\varphi$ give a complete ray. The section also
  says the problem page records the status open with progress not
  compiled and that the folder index suggests a bearing on integer bases;
  both are outside the read set.
- **S2 (what transports: nothing).** (a) For a base-2 ray with $a_0\ge1$
  and every $j\ge1$, $a_j-\sum_{i<j}a_i=a_0+\sum_{i<j}u_i>0$, with
  $u_i\in\{0,1\}$. (b) Hence the subset sums of the ray below $a_n$ number
  at most $2^n$, while $a_n\ge a_02^n$. (c) The hypothesis of the mesh
  lemma (Lemma 2.2 of the Yu--Chen reconstruction), that the span of the
  current subset sums is at least the next weight, holds for no prefix of
  a single base-2 ray. (d) For a normalized pair,
  $b_i<a_i<2b_i\le b_{i+1}$ for all $i$, so each merged weight is at most
  twice its predecessor; the Yu--Chen argument rests on this. (e) At a
  non-integer base the recurrence $a_{i+1}=2a_i+u_i$, $u_i\in\{0,1\}$,
  fails, and with it the exact doubling blocks, the coefficient interval
  $d\{px+qy\}$, the certificate and the modular invariant are unavailable.
  (f) The single-ray analog of Lemma 354.4 (a run of $b_n$ consecutive
  subset sums in $P_n$ forces completeness) is van Doorn's Lemma 5, which
  the section says the corpus already records.
- **S3 (the scope reading).** Proposition 11 on the Theorem 9 page holds
  for every Pisot or Salem number $\gamma$ whose minimal polynomial $P$ has
  $P(1)=-q$ with an integer $q\ge3$: there are arbitrarily large $t>0$ with
  $\lfloor t\gamma^n\rfloor$ even for every $n\ge0$, so the ray is
  incomplete. Hence, at every such base in $(1,\varphi)$ besides Geneson's,
  if one exists, the ray is incomplete for arbitrarily large $t$; the
  source states Proposition 11 in this generality and Theorem 9 at one
  base, so the reading adds no mathematics.
- **S4 (what it does not give).** No completeness result for any single
  ray, no classification of the pairs $(t,\alpha)$, and nothing about
  $1<\alpha<\varphi$ beyond the bases of S3.
- **S5 (next investigation).** None from the folder. If the previous
  section's investigation ends negatively, that is, some rational base
  $\gamma\in(1,\rho_0]$, some $q\ge2$ and some $t>0$ have
  $q\mid\lfloor t\gamma^n\rfloor$ for all sufficiently large $n$, then an
  incomplete single ray at a rational base results.
- **S6 (outcome).** The Yu--Chen mechanism fails for Problem 349 because
  the interlacing and the digit recurrence are missing; the Geneson
  reconstruction bears on Problem 349 exactly as its source card records:
  Theorem 9 refutes the conjecture at one base without classifying the
  pairs.

## Checklist

- **Quantifiers and scope.** One range dropped: "only $t=2^{-k}$" carries
  no range for $k$ (F1). The strict inequality in S2(a) needs $a_0\ge1$,
  which the section's ray has after the zero terms of a coefficient below
  $1$ are discarded (F6). "Arbitrarily large $t$" in S3 is existential and
  is used as such. Otherwise the quantifiers match their sources.
- **Circularity.** None. No statement of the section is assumed in its own
  support; the base-2 count and the mesh-hypothesis failure are derived
  from the recurrence alone.
- **Model and convention changes.** Two conventions meet: the folder's
  indexing from $n=0$ against van Doorn's from $n=1$, which moves the range
  of $k$ in Proposition 2 (F1); and set completeness against sequence
  completeness, which agree for all-even rays, the only case S3 uses. No
  relaxed or averaged system replaces the objects.
- **Finite and statistical overreach.** None. The section cites no finite
  verification and no heuristic.
- **Uniformity.** Not applicable: no constant or bound is claimed uniform
  over a family. Proposition 11 is applied base by base.
- **Extremal conclusions.** Not applicable: no infimum, supremum or
  sharpness claim.
- **Consequences and composition.** "And the sequence incomplete" in S3
  follows from all terms being even and nonnegative (W2). The consequence
  in S5 needs one unstated step, a shift of the coefficient (F5). The list
  in S2(e) includes the certificate, whose mechanism does survive at
  non-integer bases (F2). The analogy S2(f) is exact at the level of
  hypotheses (W3).
- **Computation.** The section claims none. The reviewer's own checks are
  exact integer arithmetic for the identities and a double-precision root
  computation with a wide margin for the witness of F4, described in the
  weakest steps.
- **Reproduction.** Not applicable: the section states no rerun line and
  no coverage claim.
- **Source and verdict fidelity.** Graham's square, van Doorn's range
  $\alpha\ge\varphi$, his Proposition 1, Geneson's Theorem 9 and the
  generality of Proposition 11 match the held PDFs; Proposition 2 is
  quoted without its range (F1); "which the corpus already records" has no
  page behind it (F3); the card's "Bears on" text for Problem 349 is
  characterized correctly in S6.

## Weakest steps

**W1: the base-2 count (S2(a)--(c)).** For real $x$,
$\lfloor2x\rfloor=2\lfloor x\rfloor+\lfloor2\{x\}\rfloor$ with the last
term in $\{0,1\}$; applied to $x=2^i\alpha$ this is $u_i\in\{0,1\}$. The
identity follows by induction on $j$: for $j=0$ both sides are $a_0$, and

$$
a_{j+1}-\sum_{i\le j}a_i=(2a_j+u_j)-a_j-\sum_{i<j}a_i
=\Bigl(a_j-\sum_{i<j}a_i\Bigr)+u_j .
$$

The right side $a_0+\sum_{i<j}u_i$ is positive as soon as $a_0\ge1$, that
is, $\alpha\ge1$; for $\alpha<1$ it is $0$ while the ray is still $0$, and
becomes positive at the first nonzero term, so discarding the zero terms
(as the problem's set convention does) restores the hypothesis (F6). A
subset containing some $a_j$ with $j\ge n$ sums to at least $a_j\ge a_n$
because the ray is nondecreasing, so every subset sum below $a_n$ is a
subset sum of $a_0,\ldots,a_{n-1}$: at most $2^n$ values, the empty sum
included. Unrolling the recurrence, $a_n=2^na_0+\sum_{i<n}2^{n-1-i}u_i$,
so $a_n\ge a_02^n$. The span of the subset sums of the first $n$ weights
is $\sum_{i<n}a_i=a_n-a_0-\sum_{i<n}u_i\le a_n-1$, so the mesh lemma's
hypothesis $\operatorname{span}\ge a_n$ fails for every $n\ge1$, as the
section says. The section stops there; the consequence it leaves implicit
is sound: if $a_0\ge2$, at least $a_n-2^n\ge2^n$ integers of $[0,a_n)$ are
not subset sums, and if $a_0=1$ and some $u_i=1$, at least $2^{n-1-i}$ are
for every $n>i$; either way the misses are unbounded and the ray is
incomplete, leaving only $\alpha=1$, the powers of two. This is van
Doorn's Proposition 2 in the folder's indexing, $t=2^{-k}$ with $k\ge0$,
and in his indexing from $n=1$ it reads $k\ge1$, so the count also
confirms that a range on $k$ is needed (F1): at $t=2$ (or $t=1$ in his
indexing) the ray $2,4,8,\ldots$ is all even and incomplete. All of this
was rechecked in exact arithmetic for the coefficients $1$, $3/2$, $7/3$,
$11/4$, $2$ and $5$ over twelve terms.

**W2: the scope reading (S3).** The Theorem 9 page states Proposition 11
for a Pisot or Salem $\gamma$ with $P(1)=-q$, $q\ge3$, with conclusion
"arbitrarily large real $t>0$ such that $\lfloor t\gamma^n\rfloor$ is even
for every integer $n\ge0$"; Geneson's text (p. 11) states it in the same
generality, and Theorem 9 only at the one base with $P(1)=-5$. So the
section's reading of scope is faithful. The added clause "and the sequence
incomplete" is a two-line deduction: the terms are nonnegative since
$t,\gamma>0$, so every finite sum of terms with distinct indices (or of
distinct values) is even, no odd integer is represented, and completeness
fails under both conventions. The hedge "if any besides Geneson's exists"
is where the sentence is weakest, because it can be replaced by a witness.
Let $\theta$ be the real root above $1$ of $P(x)=x^5-x^3-x^2-x-1$. Then
$P(1)=-3$. A root computation in double precision gives
$\theta\approx1.534158$ and all other roots of modulus at most $0.951$;
the margin is far above rounding error. Any monic integer factor of $P$
without the root $\theta$ would have all its roots strictly inside the
unit circle, hence a constant term of modulus below $1$, hence $0$, which
$P(0)=-1$ excludes; so $P$ is irreducible, $\theta$ is a Pisot number, and
$\theta<3/2<\varphi$. Proposition 11 with $q=3$ therefore gives
arbitrarily large $t$ with every $\lfloor t\theta^n\rfloor$ even, provided
Lemma 10 holds as the Theorem 9 page imports it (the Dubickas theorem is
not held; the page and the source state it for Pisot and Salem numbers
alike). A second witness is the root $\approx1.590005$ of
$x^7-x^5-x^4-x^3-x^2-x-1$, with $P(1)=-5$ and the other roots of modulus
at most $0.977$. So the conditional in S3 is true with a nonempty
antecedent, and the closing "adds no mathematics" is exact for the scope
reading alone but not for the reading with a witness (F4).

**W3: the two analogies (S2(e), S2(f), S5).** Van Doorn's Lemma 5 assumes
$t\ge1$, $1<\alpha<\varphi$, and positive integers $r,X$ with every $m$ in
$[X,X+s_{r+1})$ a subset sum of $s_1,\ldots,s_r$, and concludes that
$S_t(\alpha)$ is complete; its proof adjoins $s_{r+1}$ to lengthen the run
to $s_{r+1}+s_{r+1}\ge s_{r+2}$, the last inequality from his Lemma 4
($s_{n+1}\le2s_n$ for $n\ge1$ when $\alpha<3/2$, for $n\ge2$ when
$3/2\le\alpha<\varphi$, both under $t\ge1$), and iterates. Lemma 354.4
assumes a run of $b_n$ consecutive integers in $P_n$ and iterates the same
step with $c_{j+1}\le2c_j$ from item 4 of the normalization page. The two
are the same mechanism with different sources for the doubling bound, so
the analogy in S2(f) is exact. The same comparison shows that listing "the
certificate" among the objects lost with the digit recurrence overstates:
the recurrence supplies the doubling bound at base $2$, but the
certificate needs only that bound, and van Doorn's Lemma 4 supplies it for
single rays below $\varphi$ with $t\ge1$ (F2). For S5, if
$q\mid\lfloor t\gamma^n\rfloor$ for all $n\ge n_0$, the ray of coefficient
$t'=t\gamma^{n_0}$ has every term divisible by $q$, every subset sum
divisible by $q$, and is incomplete; the ray of coefficient $t$ itself
need not be, as $t=1$ at base $2$ shows ($1,2,4,\ldots$: all later terms
even, yet complete). The section's sentence names no coefficient, so it is
true with $t'$; the bridge is unstated (F5).

## Strongest attack

- **S1.** Each recorded result was compared clause by clause with the
  held PDF. Graham's square and conjecture (pp. 63 and 70), van Doorn's
  settlement of $\alpha\ge\varphi$ (p. 1), his Proposition 1 (p. 4) and
  Geneson's Theorem 9 and Proposition 11 (p. 11) match. The attack
  succeeded only against the range of $k$ in Proposition 2, where the
  source has $k\ge1$ under indexing from $n=1$ and the section has none;
  the literal sentence ("only ... gives") is the necessary direction and
  is true, so the statement stands with a suggested correction (F1). The
  claims about the problem page's progress line and the folder index
  could not be attacked within the read set.
- **S2.** The identity was attacked at the boundary $\alpha<1$, where the
  strict inequality fails while the ray is $0$; the section's ray is the
  problem's set with $0$ removed, so the attack finds a missing convention
  (F6), not an error. A base-2 ray with a prefix whose span reaches the
  next weight was sought and cannot exist, by the identity. The claim that
  the certificate is absent at non-integer bases was attacked with van
  Doorn's Lemma 5 itself, which the section names in its next sentence:
  the mechanism survives (F2). The claim "which the corpus already
  records" was attacked by searching the corpus pages for a record of
  Lemma 5: only the held PDF and its conversion carry it (F3). The
  interlacing and the failure of the recurrence at non-integer bases were
  rederived and checked in exact arithmetic at bases $3/2$, $4/3$ and
  $5/3$, where the differences $s_{i+1}-2s_i$ are negative.
- **S3.** The hypotheses of Proposition 11 on the reconstruction page and
  in the source were compared and match. A Pisot or Salem base with
  $P(1)\le-3$ whose ray could be complete for all large $t$ was sought;
  none can exist under Lemma 10 as imported. The hedge was attacked by
  exhibiting the witnesses of W2, which makes the antecedent true (F4);
  the statement, being conditional, is not thereby refuted.
- **S4.** A completeness result for a single ray that the folder does
  supply was sought; the folder's mechanisms all need two interlaced
  rays, so none exists, and the negative claims stand.
- **S5.** The deduction was attacked with the base-2 example $t=1$, which
  shows that divisibility of all late terms does not make the ray at that
  coefficient incomplete; the shifted coefficient repairs it, and the
  sentence names no coefficient (F5).
- **S6.** The card's "Bears on" paragraph for Problem 349 was read; the
  section's characterization neither strengthens nor weakens it.

## Premises

- [[research/erdos_354/yu_chen_normalization_reconstruction|Normalization page]]
  (author-recorded reconstruction, independently reviewed as of
  2026-09-28T05:03:27Z): item 4 (interlacing $b_i<a_i<2b_i\le b_{i+1}$ and the
  doubling bound on the merged list, for a normalized pair with $N<M<2N$,
  $N\ge2$), item 6 (the identities $a_j-\sum_{i<j}a_i=M+\sum_{i<j}u_i$ and its
  $b$ counterpart), and the use of the mesh lemma inside the gap-bound proof
  under the hypothesis $c_j\le\operatorname{span}(W_j)$. Read in full; the
  section uses items 4 and 6 within their hypotheses, the identity being
  valid for any single ray with $a_0\ge1$.
- [[research/erdos_354/yu_chen_lemma_2_2_reconstruction|Mesh lemma page]]:
  Lemma 2.2, hypothesis $\operatorname{span}(W)\ge c>0$ and
  $\operatorname{gap}(W)\le k$, conclusion gap preserved and span increased
  by $c$; consequence under $c_{i+1}\le2c_i$. Read in full; the section's
  phrase "a span at least the next weight" is this hypothesis.
- [[research/erdos_354/yu_chen_theorem_5_1_reconstruction|Theorem 5.1 page]]:
  Statement section and the opening of Step 1, where the exact block's
  subset sums are $d\{px+qy:0\le x,y<K\}$ from weights $2^jdp$, $2^jdq$;
  read only to identify the objects named in S2(e). They need exact
  doubling and two rays, as the section says.
- [[research/erdos_354/geneson_theorem_9_reconstruction|Theorem 9 page]]:
  Lemma 10 imported as quoted (Pisot or Salem, $P(1)=-q$, $q\ge2$, a real
  $\xi\in\mathbb Q(\gamma)$ with $\{\xi\gamma^n\}$ within $\epsilon$ of
  $1/q$ for $n\ge1$, sign unspecified); Proposition 11 ($q\ge3$, some
  $\eta>0$ with $3/(4q)<\{\eta\gamma^n\}<5/(4q)$, hence arbitrarily large
  $t$ with all floors even for $n\ge0$); Theorem 9 at the one Salem base.
  Read in full; the section uses Proposition 11 exactly at its stated
  hypotheses. Dubickas's theorem is not held.
- Lemma 354.4 on the connections page (author-recorded, another section's
  subject): statement and proof read; used here only as the object of the
  analogy in S2(f).
- Geneson (2026), held preprint: Section 5 read in the text layer;
  Proposition 11 stated for every Pisot or Salem number with $P(1)=-q$,
  $q\ge3$; Theorem 9 at one base; the introduction's account of Graham's
  conjecture and of van Doorn's range.
- Van Doorn (2026), held preprint, text layer: the definition
  $s_n=\lfloor t\alpha^n\rfloor$ for $n\ge1$; the sentence settling
  $\alpha\ge\varphi$; Proposition 1 ($\alpha\notin[1,2]$: never complete;
  $\alpha=1$: complete if and only if $t\in[1,2)$); Proposition 2
  ($\alpha=2$: complete if and only if $t=2^{-k}$, $k\ge1$); Lemma 4 and
  Lemma 5 as restated in W3; Proposition 8 (its second clause is the range
  $1.2<\alpha\le1.3$, $t\le5$ that the Theorem 9 page quotes; its first
  clause is the range the van Doorn card summarizes; both are in the
  source).
- Graham (1964), held scan without a text layer: page images of p. 63 and
  p. 70; the square $0<t<1$, $1<a<2$ and the conjecture for
  $1<a<(1+\sqrt5)/2$ confirmed.
- Problem 349 statement block: the question as restated in S1.
- Library cards as listed under reading; the van Doorn card's provenance
  block lists results to transcribe (main characterization, the
  non-completeness range, Lemma 1 and Corollary 1, Propositions 7, 8 and
  9) and not Lemma 5.

## Findings

- **F1 (suggested).** Location: "at base $2$, only $t=2^{-k}$ gives a
  complete sequence" (Target paragraph). Defect: the source's Proposition
  2 reads "if and only if $t=1/2^k$ for some $k\ge1$" under indexing from
  $n=1$; the section drops the range, and under the folder's indexing from
  $n=0$ the correct range is $k\ge0$. Witness: $t=2$ (any indexing) or
  $t=1$ (indexing from $n=1$) gives the all-even ray $2,4,8,\ldots$, which
  is incomplete, so a reader who fills in $k\in\mathbb Z$ gets a false
  characterization. Replacement: "at base $2$, the ray is complete exactly
  for $t=2^{-k}$ with $k\ge1$ in his indexing from $n=1$, that is, exactly
  for the rays whose nonzero terms are the powers of two."
- **F2 (suggested).** Location: "and with it the exact doubling blocks,
  the coefficient interval $d\{px+qy\}$, the certificate and the modular
  invariant." Defect: the certificate's mechanism (a run of consecutive
  subset sums of length the next weight, propagated under growth by at
  most doubling) does not depend on the digit recurrence, only on the
  doubling bound, and the section's next sentence names its single-ray
  form at non-integer bases, van Doorn's Lemma 5. Witness: W3. Replacement:
  drop "the certificate" from the list, or write "the two-ray derivation
  of the certificate's doubling bound".
- **F3 (suggested).** Location: "van Doorn's Lemma 5 (held), which the
  corpus already records." Defect: no corpus page records Lemma 5; the van
  Doorn card's list of results to transcribe omits it, and the only
  occurrences are the held PDF and its conversion. Witness: a search of
  the research, problem, theory and library pages as of that time finds the
  lemma only on the connections page itself. Replacement: "van Doorn's
  Lemma 5, in the held preprint and not yet transcribed on its card."
- **F4 (suggested).** Location: "so at every such base in $(1,\varphi)$,
  if any besides Geneson's exists" and "so this adds no mathematics".
  Defect: the antecedent is true and the hedge can be replaced by a
  witness, after which the scope reading does add a concrete instance to
  Problem 349. Witness: the Pisot number $\theta\approx1.5342$, root of
  $x^5-x^3-x^2-x-1$ with $P(1)=-3$ (W2), and the Pisot number
  $\approx1.5900$, root of $x^7-x^5-x^4-x^3-x^2-x-1$ with $P(1)=-5$; at
  either base Proposition 11 gives arbitrarily large $t$ with every floor
  even, conditional on Lemma 10 as imported. Replacement: name one witness
  with its polynomial and the conditionality on Lemma 10, and change "adds
  no mathematics" to "adds one instance, at author-recorded standing".
- **F5 (note).** Location: "the negative outcome of the previous section's
  investigation would add an incomplete ray at a rational base." Defect:
  the negative outcome is divisibility of all late terms by $q$, which
  makes the ray incomplete only after the coefficient is shifted to
  $t\gamma^{n_0}$; the sentence is true with that ray and names no
  coefficient. Witness: base $2$, $t=1$. Replacement: "would add an
  incomplete ray at a rational base, the ray of coefficient
  $t\gamma^{n_0}$ whose every term is divisible by $q$."
- **F6 (note).** Location: "$a_j-\sum_{i<j}a_i=a_0+\sum_{i<j}u_i>0$".
  Defect: the strict inequality needs $a_0\ge1$; for a coefficient below
  $1$ the ray opens with zero terms, on which both sides vanish. Witness:
  $\alpha=1/4$, $j=1$. Replacement: add "with the zero terms of a
  coefficient below $1$ discarded, so $a_0\ge1$".

## Verdict

- **S1:** refutation-failed. The recorded literature is stated faithfully
  except for the missing range on $k$ (F1), which does not falsify the
  sentence as written; the two claims about the problem page's progress
  line and the folder index are unverified here because their sources lie
  outside the read set.
- **S2:** refutation-failed. The identity, the count, the failure of the
  mesh hypothesis, the interlacing and the loss of the recurrence at
  non-integer bases are rederived; the list of lost objects overstates by
  one item (F2), the corpus-record claim has no page behind it (F3), and
  the identity needs its convention (F6).
- **S3:** refutation-failed. The scope reading is faithful to the
  reconstruction page and to the source; the conditional is true, and its
  antecedent is satisfied by explicit Pisot witnesses (F4).
- **S4:** refutation-failed.
- **S5:** refutation-failed, with the unstated coefficient shift (F5).
- **S6:** refutation-failed.

Limitations: the witnesses of F4 rest on Lemma 10 as the Theorem 9 page
imports it from a source that is not held, and on a double-precision root
computation with a wide margin rather than a certified enclosure; no
statement of this review depends on them. The reviewer could not check
the two sentences that quote the problem page's progress line and the
folder index. This focused review assigns no tier and changes no status.
