---
name: research/erdos_1221/evidence/verify/connections_the_span_to_count_transfer_has_no_second_consume_review
title: "Independent review of the connections section: The span-to-count transfer has no second consumer"
desc: |
  Focused refutation review of the section's fourteen author-recorded
  statements: eleven refutation-failed, one refuted-as-stated (the scope
  sentence's implication omits the range r >= C A that both counting
  propositions assume; a witness is given), two inventory sentences that
  are not mathematical claims; one required correction, two suggested,
  three notes.
created: 2026-09-28T19:23:26Z
updated: 2026-09-28T19:23:26Z
---

***

## Subject and independence

Role: independent reviewer in a fresh context, commissioned for
refutation; the reviewer took no part in writing the page, the folder's
reconstructions or their reviews, and read no review or grade of any of
them. Subject: page `wiki/research/erdos_1221/connections.md` as it stood on
2026-09-28T13:50:48Z, section "The span-to-count transfer has no second
consumer", lines 519--587 (the last H2 heading to the end of the file). No lead
page is named for this section and none was read.

Read, and at what depth:

- The section, lines 519--587, read in full, every sentence.
- The page's preamble, lines 1--44 (purpose, standing, notation), read in
  full as the shared conventions.
- The page's three other sections, lines 45--518, read in full as inputs,
  because the section cites "the section above" (Problem 255),
  Proposition 480.1, and "the only transfer ... proved here"; only the
  statements and directions of Propositions 255.1, 480.1, 1221.1 and
  1221.2 are used, and their proofs are another reviewer's subject and are
  not checked.
- The folder's reconstruction pages, read in full as premises at their
  reviewed standing: Lemma 2.1, Lemma 4.2, Lemma 6.1, Lemma 6.2, Lemma
  6.3, Proposition 3.1, Proposition 6.4, Lemma 7.2 and Theorem 1.1 of the
  2026 preprint, Theorem 2 of the balanced-stick preprint, and inequality
  (4.3) of the 1949 note.
- The Statement paragraphs, statement only, of the fifteen problem pages
  the section names: E0255, E0997, E0987, E0998, E0992, E0994, E0995,
  E0996, E0988, E0989, E0991, E0208, E0153, E1221 and E0480.
- The provenance paragraphs of the three library cards, and the Statement
  sections of the result pages theorem_1_1 (2026 preprint), theorem_2
  (balanced-stick preprint), inequality_4_3 and section_2_r_equals_1
  (1949 note).
- The held PDFs: the 2026 preprint's text layer for the introduction and
  the statements of (2.1), Lemma 2.1, Proposition 3.1, (6.1), Lemma 6.1,
  Proposition 6.4, Theorem 7.1 and Lemma 7.2; the balanced-stick
  preprint's Theorems 2 and 3 on p. 2 and its derivation paragraph on
  p. 9; the 1949 note's printed pages 14--16 on the page images (Sections
  1, 2 and 4, display (4.3)).
- Guidance: `docs/verification.md` ("Whole-claim report", "Audit
  checklist", "Grading and claim standing"), `docs/approach_vetting.md`,
  `docs/evidence.md` ("Source fidelity") and `docs/math_authoring.md`.

Exposures. (1) The Problem 998 page carries a bold "Formulation and
status" paragraph between its Statement and Status lines, and it reached
the reviewer with the statement extraction; it is status text, it is not
relied on here, and for the record it agrees with the section's
description of that problem. (2) The Problem 1221 and Problem 480 pages
carry "Formulation" paragraphs after their statements, read as part of
the statement. (3) The provenance paragraphs of the library cards end
with one-line standing sentences, and the page's own sections on Problems
255 and 480 report those problems' statuses; both are on allowed surfaces
and are not relied on. No review, grade, index page, Current assessment
or Known results section was read, and no web search was made.

## Restatement

The notation is the folder's: distinct points $x_1,x_2,\ldots$ on the
circle $\mathbb T$ of circumference $1$ (the reconstruction pages assume
distinctness; the page's preamble allows coincident terms), the nested
sets $P_t=\{x_1,\ldots,x_{\lfloor t\rfloor}\}$, the $r$-spans of $P_t$
(the clockwise distance from a point to the point $r$ places later),
$N_t(I)=\#(P_t\cap I)$, and, for $A\ge1$, $\Lambda=\log(r/A)$ and
$S=\sqrt{Ar}/\Lambda^2$.

- **S1 (hypothesis form).** The mechanism's hypothesis is one of two
  eventual span bounds at scale $1/t$. Two-sided, (2.1): a fixed $A\ge1$
  such that for every sufficiently large real $t$ there are $a_t,b_t\ge0$
  with $a_t+b_t\le A$ and every $r$-span of $P_t$ in
  $[(r-a_t)/t,(r+b_t)/t]$. One-sided, (6.1): a fixed $A\ge1$ and one
  fixed alternative, $nM_n^{(r)}-r\le A$ or $r-nm_n^{(r)}\le A$, holding
  at every sufficiently large integer $n$. The family is nested and grows
  by one point per integer step.
- **S2 (conclusion form).** Under (2.1), for every sufficiently large
  $t$, every $x\in\mathbb T$ and every $0\le D\le S$,
  $|N_t((x,x+D/t])-D|\le CA$ (Proposition 3.1); under (6.1), for every
  sufficiently large integer $n$ and every $0\le D\le S$,
  $\int_{\mathbb T}|N_n((x,x+D/n])-D|\,dx\le CA$ (Proposition 6.4); $C$
  is absolute, and the time threshold depends on $r$, $A$ and the
  sequence but not on $x$ or $D$. As written, the section states no
  restriction on $r$ relative to $A$, so the strongest reading is the
  implication for every $A\ge1$ and every $r$.
- **S3 (nesting).** The mechanism cannot run on a family that is not
  nested: the walk comparison of Lemma 2.1 (and its averaged form, Lemma
  6.2) uses the inclusions $P_t\subseteq P_s\subseteq P_{(1+q)t}$, and
  the localizations of Lemma 4.2 and Lemma 7.2 use the insertion index as
  a coordinate.
- **S4 (converse).** The passage from counting control to span control
  is elementary, and it is what Theorem 2 of the balanced-stick preprint
  takes from that preprint's Theorem 3.
- **S5 (search).** The problems, research and theory trees were searched
  for the named topics, and no open problem consumes the mechanism.
- **S6 (Problem 255).** Problem 255 is an input of the mechanism's
  consumers, not a consumer of the mechanism.
- **S7 (Problem 997).** Well-distribution counts the terms of every index
  block $n<m\le n+k$ in every interval, for one sequence; the mechanism
  counts prefixes on arcs of length $D/n$; and the problem is proved.
- **S8 (Problems 987 and 998).** Both are resolved (987 proved; 998
  disproved as worded, the correct theorem being the length criterion
  the section attributes to Kesten), and the Kronecker sequence enters
  the folder only through the imported Theorem 3 of the balanced-stick
  preprint, which is not reconstructed.
- **S9 (Problems 992, 994, 995 and 996).** These are statements for
  almost every $\alpha$; the mechanism concerns one sequence and carries
  no metric information.
- **S10 (Problems 988, 989 and 991).** These concern finite point sets
  on the sphere or an infinite sequence in the plane, without the
  one-insertion-per-step structure, and are resolved.
- **S11 (Problems 208 and 153).** These concern the gaps of one fixed
  set, not of a growing family, and the theory tree holds no claim about
  sequences in the unit interval.
- **S12 (outcome).** There is no second consumer in the corpus, so no
  method page is made.
- **S13 (recognizer).** A future consumer is recognized by a hypothesis
  controlling the $r$-th neighbor distances of a nested growing family
  uniformly in position and a conclusion counting terms in short arcs.
- **S14 (only transfer).** The 1949 count behind (4.3), rerun on the
  interval as Proposition 480.1, is the only transfer of the folder's
  mechanisms to another setting proved on the page.

## Checklist

- **Quantifiers and scope.** Defect found. S2 omits the range hypothesis
  of both counting propositions, $r\ge C_0A$ (Proposition 3.1) and
  $r\ge C_2A$ (Proposition 6.4); without it the implication is false (F1;
  witness under S2 in "Strongest attack"). The eventual quantifiers ("for
  every sufficiently large $t$"; threshold independent of $x$ and $D$)
  are stated correctly. "Arcs holding at most $S$ terms" is a length
  condition in the propositions (F4). The pairing of the two hypothesis
  forms with the two conclusion forms must be read respectively (F3).
- **Circularity.** None. S6 states the direction of dependence between
  Problem 255 and the mechanism correctly: the preprint's consumers of
  the counting bound (Lemma 4.2, Lemma 7.2) import discrepancy lower
  bounds, and the elementary direction (Proposition 255.1 on the page)
  runs from counting control to span control.
- **Model and convention changes.** The section describes the preprint's
  model (distinct points, sets $P_t$) while the page's preamble allows
  coincident terms; the page's Problem 1221 section carries that
  transfer, and the section does not claim it. The phrase "converse
  passage" changes the scale silently (F2): the elementary direction
  runs at one scale, while the mechanism descends from scale $r$ to scale
  $S$.
- **Finite and statistical overreach.** None; the section proves nothing
  from finite cases.
- **Uniformity.** The dependence of the thresholds on $r$, $A$ and the
  sequence is stated as on the reconstruction pages. The implied constant
  in "$O(A)$" is absolute only in the range $r\ge C_0A$, which is the
  omission of F1.
- **Extremal conclusions.** Not applicable: the section states no
  infimum, supremum or sharpness.
- **Consequences and composition.** Each bullet of "The search" was
  checked against the problem's Statement paragraph; the
  characterizations of the statements are accurate. The status words
  ("proved", "resolved", "disproved as worded") and the inventory
  sentences (S5, the theory-tree clause of S11, S12) are outside the read
  set and are not verified here. S14 holds under the reading "another
  ambient space" (F5).
- **Computation.** Not applicable to the section; the reviewer's
  witnesses are derived analytically below, with one numeric confirmation
  stated.
- **Reproduction.** Not applicable; the section states no rerun commands
  or coverage.
- **Source and verdict fidelity.** The descriptions of (2.1), (6.1),
  Propositions 3.1 and 6.4 and Lemmas 4.2 and 7.2 match the
  reconstruction pages and the preprint's text layer at the displayed
  constants; the description of the balanced-stick derivation matches the
  p. 9 paragraph, whose "Theorem 2 implies" slip the reconstruction page
  already records; "(4.3)" is the display on printed p. 16 of the 1949
  note. No verifier's ruling is characterized in the section.

## Weakest steps

**W1: the implication of S1--S2 needs $r\ge C_0A$.** Re-derived from
the Proposition 3.1 page: the terminal bounds (3.2) need
$K=\sqrt{Ar}<r-A$, the one-step multipliers need
$\theta=\sqrt{A/r}\le1/12$, and the descent needs
$\theta\Lambda^2=\sqrt{A/r}\log^2(r/A)$ bounded so that
$A\theta\Lambda=O(A/\Lambda)$; all three are conditions on $r/A$, and
all fail when $A$ is comparable to $r$. Proposition 6.4 needs the same
($\theta$ and $\theta\Lambda$ small). The section states the hypothesis
and the conclusion of the transfer without this range; the witness under
S2 shows that the conclusion is then false, so the range is a hypothesis
and not a convenience.

**W2: "the nesting is essential".** Re-derived. In the proof of (2.2)
the map $T_u=B_s\circ F_t$ is an injection of $P_t$ into $P_{t_+}$ only
because $P_t\subseteq P_s\subseteq P_{t_+}$, and the displacement
bookkeeping uses (2.1) at the intermediate times $s(u)$; the same
inclusions carry Lemma 6.2. The conclusion, not only the proof, needs
the family: take one set of $N=rm$ points, $r$ even, whose consecutive
gaps are $(1+\epsilon_i)/N$ with $\epsilon_i=+1/2$ when $i\bmod r$ lies
in $\{1,\ldots,r/2\}$ and $\epsilon_i=-1/2$ otherwise. Every window of
$r$ consecutive gaps meets each residue class once, so every $r$-span
equals $r/N$ exactly, the strongest form of (2.1) at that one time. The
arc of length $D/N$ starting at the first point of a $+1/2$ block
contains the points at cumulative distances $1.5j/N$, so it holds
$\lfloor2D/3\rfloor$ points for $D\le3r/4$: the counting error is about
$D/3$, and at $D=S$ about $S/3$, which exceeds $(3+C_1)A$ as soon as
$\sqrt{r/A}$ exceeds a constant times $\log^2(r/A)$. Span control at one
time gives no short-arc counting control; the eventual hypothesis on the
nested family is what the mechanism consumes.

**W3: "the converse passage ... is the elementary direction".**
Re-derived from the balanced-stick reconstruction: with $R^+$ the least
integer with $R^+-c\log R^+\ge r+2$ and $R^-$ the largest integer $\ge2$
with $R^-+c\log R^-\le r$, Theorem 3 at $R^+$ forbids an $r$-span of
length at least $R^+/n$ (it would contain a closed arc of length $R^+/n$
holding at least $r+2$ terms, against the $r+1$ terms of the span), and
Theorem 3 at $R^-$ forbids an $r$-span of length at most $R^-/n$; the
ratio is below $R^+/R^-\le1+c'\log r/r$. This is counting control at
the scales $R^\pm\approx r$ giving span control at scale $r$, and it is
elementary. It is not the converse of the mechanism, which starts from
span control at scale $r$ and ends at counting control at scale
$S\ll r$; that strict converse is false (F2).

## Strongest attack

**S1.** Attack: find a hypothesis the mechanism uses that the sentence
does not state. Distinctness of the points is used on the reconstruction
pages (positivity of spans; the least distance $\delta$ in Lemma 4.2)
and is not stated, but the page's Problem 1221 section is where that
scope is handled, and the section does not claim the coincident-point
extension. The range $r\ge C_0A$ is the hypothesis the sentence lacks;
it is charged to S2 (F1). Otherwise the description of (2.1) and (6.1)
is exact, including that the alternative of (6.1) is fixed and eventual.
Refutation of the description itself failed.

**S2.** Attack: exhibit a sequence satisfying (2.1) with some $A$ whose
short-arc counting error is not $O(A)$. Witness: the 1949 note's Section
2 sequence $a_k=\log_2(2k-1)$ reduced mod $1$. By Section 2 of the note
(printed pp. 14--15), its first $n$ terms are the numbers $\log_2k$ mod
$1$ for $n\le k\le2n-1$, in cyclic order, with gaps $\log_2((k+1)/k)$;
since $\log_2k$ increases by less than $1$ over this range, the points
wind once around the circle, no two coincide, and the last-to-first gap
is $\log_2(2n/(2n-1))$. Every gap at time $n$ therefore lies in
$[\log_2(2n/(2n-1)),\log_2((n+1)/n)]\subseteq[1/(2n\log2),1/(n\log2)]$,
and every $r$-span in $[0.72r/n,1.45r/n]$. For $t\in[n,n+1)$ with
$n\ge2r$, (2.1) holds with $a_t=0.28r$ and $b_t=0.45r+1$, hence with
$A=r-1$ for every $r\ge16$. Then
$\Lambda=\log(r/(r-1))\le1/(r-1)$ and $S\ge(r-1)^3$. At the times
$n=2^m$ the first $n$ terms are exactly $\log_2(j/n)$ for $n\le j\le2n-1$,
so the arc $(0,D/n]$ holds $\lfloor n2^{D/n}\rfloor-n$ terms, at most
$0.694D+0.48D^2/n$; for $D=(r-1)^3\le S$ and $n\ge D^2$ the count is at
most $0.7D+1$ and the counting error is at least $0.3(r-1)^3-1$, while
the claimed bound is $C(r-1)$. (Numeric confirmation at $r=40$: the sums
$a_t+b_t$ at $n=2^{14}$ and $n=2^{16}$ are $28.8$ against $A=39$, and
the errors on $(0,D/n]$ with $D=n/4\le S$ are $997$ and $3985$.) The
pointwise conclusion thus fails at infinitely many times for every
absolute $C$ once $r$ is large. The same sequence satisfies (6.1) with
the same $A$ and defeats the $L^1$ conclusion in the same way, since the
density of its terms varies by the factor $2$ around the circle. The
propositions themselves are untouched: they assume $r\ge C_0A$ and
$r\ge C_2A$. Verdict: refuted-as-stated for the unrestricted
implication; the repair is to carry the range.

**S3.** Attack: run the transfer on a non-nested family, or without the
insertion order. The single-set witness of W2 defeats the one-time
implication; the localizations of Lemmas 4.2 and 7.2 define their list
and planar objects by the index of insertion (the prefix $j$ of Lemma
4.2 is $P_{m_j}\cap J$; the second coordinate in Lemma 7.2 is $i/N$), so
removing the insertion order removes the object to which the imported
theorems apply. Refutation failed.

**S4.** Attack: read "converse passage" as the converse of the transfer
just described, from counting control at scale $S$ to span control at
scale $r$, and refute it. That converse is false: for the Section 2
sequence, the count on an arc of length $D/n$ lies between about
$0.69D$ and $1.39D$ (its density lies between $\log2$ and $2\log2$
times uniform), so the counting error is at most about $0.39D+1$ for
$D\le S$, while the span deviation $nM_n^{(r)}-r$ is about $0.44r$, far
above $0.39S$ when $S\ll r$. Under the reading the sentence intends, the
reverse direction at one scale, the derivation of W3 confirms the
statement and its attribution to the p. 9 paragraph of the balanced-stick
preprint. Refutation of the intended reading failed; the wording is F2.

**S5, S12 and the theory-tree clause of S11.** Inventory sentences
about the corpus; the read set excludes the trees they describe, so no
attack is possible here. Not mathematical claims.

**S6.** Attack: make Problem 255 a consumer. A consumer would derive
Problem 255's conclusion (a fixed interval with unbounded discrepancy)
from span control; the mechanism's contrapositive gives large span
deviation from large counting error, the wrong direction, and Problem
255's conclusion concerns a fixed interval, which no page of the folder
reaches (the page's Problem 255 section says so). The elementary
direction, Proposition 255.1, is the 1949 remark and yields the 1945
form, not the fixed interval. Refutation failed.

**S7.** Attack: bridge prefix counts to block counts. A block count is
$N_{n+k}(I)-N_n(I)$, so prefix control on an arc gives block control on
that arc; but well-distribution needs every interval $I$, including long
ones, with error $\epsilon k$, while the mechanism controls only arcs of
length at most $S/n\to0$. The statement's block structure is as the
section says. Refutation failed; the status word is not checked.

**S8--S11.** Each characterization was checked against the Statement
paragraph: Problem 987 concerns $\limsup_n|\sum_{j\le n}e(kx_j)|$;
Problem 998 concerns $\#\{m\le n:\{\alpha m\}\in[u,v)\}=n(v-u)+O(1)$;
Problems 992, 994, 995 and 996 each quantify over almost every $\alpha$;
Problem 988 is a minimum over $n$-point subsets of the sphere, Problem
991 a maximal-product configuration on the sphere, Problem 989 an
infinite planar set counted in circles of radius $r\to\infty$ against
$\pi r^2$, with no prefix and no insertion time; Problem 208 is the gap
sequence of the squarefree numbers, Problem 153 the gaps of $A+A$ for one
Sidon set at a time. The clause that the Kronecker sequence enters only
through the imported Theorem 3 matches the balanced-stick reconstruction
page, which imports Theorem 3 and reconstructs neither of its proofs.
Refutation failed; the status words are not checked.

**S13.** Attack: find a consumer meeting the recognizer that the
mechanism does not serve. The recognizer omits that the neighbor-distance
error must be small compared with $r$ (W1), so a hypothesis with
$A\approx r$ meets it and gets nothing; this is a consequence of F1 and
no separate finding. Otherwise the recognizer names the hypothesis and
conclusion shapes correctly.

**S14.** Attack: name another transfer proved on the page. Proposition
255.1 stays on the circle; Propositions 1221.1 and 1221.2 rerun folder
mechanisms on the circle for the coincident-point family. Under "another
setting" as another ambient space, the interval count of Proposition
480.1 is the only one; under "another family" it is not (F5). Refutation
of the ambient-space reading failed.

## Premises

- [[research/erdos_1221/ko26b_lemma_2_1_reconstruction|Lemma 2.1 reconstruction]]:
  hypothesis (2.1) with $A\ge1$; comparison (2.2)--(2.3) with a threshold
  uniform for $D$ in a bounded range. Read in full; used for (2.1), the
  injection structure and the uniformity clause. Source [Ko26b] held; the
  statements of (2.1) and Lemma 2.1 checked in the text layer.
- [[research/erdos_1221/ko26b_proposition_3_1_reconstruction|Proposition 3.1 reconstruction]]:
  under (2.1), $A\ge1$ and $r\ge C_0A$, the pointwise bound
  $3A+C_1A/\Lambda$ for $0\le D\le S$, threshold depending on $r$, $A$ and
  the sequence only. Read in full; the three range conditions of W1 taken
  from its proof. Source statement checked in the text layer.
- [[research/erdos_1221/ko26b_lemma_6_1_reconstruction|Lemma 6.1 reconstruction]],
  [[research/erdos_1221/ko26b_lemma_6_2_reconstruction|Lemma 6.2 reconstruction]] and
  [[research/erdos_1221/ko26b_lemma_6_3_reconstruction|Lemma 6.3 reconstruction]]:
  hypothesis (6.1) with $A\ge1$ and a fixed alternative; (6.2); the
  averaged comparison (6.5) through the same injection; $Z_t(r)\le A$.
  Read in full for the interfaces; (6.1) and Lemma 6.1 checked in the
  text layer.
- [[research/erdos_1221/ko26b_proposition_6_4_reconstruction|Proposition 6.4 reconstruction]]:
  under (6.1), $A\ge1$ and $r\ge C_2A$, the $L^1$ bound $C_3A$ at all
  late integer times for $0\le D\le S$. Read in full; statement checked
  in the text layer.
- [[research/erdos_1221/ko26b_lemma_4_2_reconstruction|Lemma 4.2 reconstruction]] and
  [[research/erdos_1221/ko26b_lemma_7_2_reconstruction|Lemma 7.2 reconstruction]]:
  the localizations, with the imported Theorem 4.1 and Theorem 7.1 (not
  held; standing as recorded there). Read in full for the use of the
  insertion index; the statements of Theorem 7.1 and Lemma 7.2 checked in
  the text layer.
- [[research/erdos_1221/ko26b_theorem_1_1_reconstruction|Theorem 1.1 reconstruction]]:
  read for the assembly and the distinct-point scope; not used beyond
  that.
- [[research/erdos_1221/clst25_theorem_2_reconstruction|Theorem 2 reconstruction]]:
  Theorem 3 imported (arcs of length $R/n$ hold $R\pm c\log R$ terms for
  $n\ge n_0(R)$), Theorem 2 derived for $r\ge2+c\log2$. Read in full;
  source [ClSt25] held; Theorems 2 and 3 and the p. 9 paragraph checked
  in the text layer.
- [[research/erdos_1221/dber49_inequality_4_3_reconstruction|Inequality (4.3) reconstruction]]:
  the Section 4 count. Read in full; source [dBEr49] held, image-only;
  Sections 1, 2 and 4 and display (4.3) read on the page images (printed
  pp. 14--16). The Section 2 description of the sequence $\log_2(2k-1)$
  mod $1$ (first $n$ terms $\log_2k$ mod $1$ for $n\le k\le2n-1$, gaps
  $\log_2((k+1)/k)$) is used for the witnesses of S2 and S4 and was
  checked by direct computation for $n\le8$.
- The page's preamble and its Problem 255, 480 and 1221 sections:
  Proposition 255.1 (bounded counting error $K$ on arcs gives
  $nM_n^r\le r+K-1$ and $nm_n^r\ge r-K+1$), Proposition 480.1 (the
  Section 4 count on the interval), Propositions 1221.1 and 1221.2 and
  deduction 1221.3; used only as named items, not checked.
- Library cards:
  [[../library/analysis/korsky_2026_resolution_debruijn_erdos_consecutive_gap_problem/_index|the 2026 preprint's card]],
  [[../library/analysis/clement_steinerberger_2025_balanced_stick_breaking/_index|the balanced-stick card]] and
  [[../library/analysis/debruijn_erdos_1949_sequences_points_circle/_index|the 1949 note's card]];
  provenance paragraphs read; artifacts as identified there.
- Sources: [Ko26b] S. Korsky, *A resolution of the de Bruijn--Erdős
  consecutive-gap problem*, arXiv:2609.07196v2; [ClSt25] F. Clément and
  S. Steinerberger, *Balanced stick breaking*, arXiv:2511.14637v1;
  [dBEr49] N. G. de Bruijn and P. Erdős, *Sequences of points on a
  circle*, Proc. 52 (1949), 14--17.
- Explicit assumptions of this review: the reconstruction pages are taken
  as established at their reviewed standing; the status words of the
  problem bullets and the corpus inventory are not checked.

## Findings

- **F1 (required).** Location: lines 524--535, "the hypothesis is an
  eventual bound on the $r$-spans at scale $1/t$ ... The conclusion is a
  counting error $O(A)$ ... on arcs holding at most
  $\sqrt{Ar}/\log^2(r/A)$ terms". Defect: the range hypothesis of both
  propositions, $r\ge C_0A$ (Proposition 3.1) and $r\ge C_2A$
  (Proposition 6.4), is omitted, and the implication is false without it.
  Witness: the 1949 Section 2 sequence with $A=r-1$ and $r\ge16$, as
  derived under S2 in "Strongest attack" (span sums $a_t+b_t\le0.73r+1$;
  counting error at least $0.3(r-1)^3-1$ on the arc $(0,D/n]$ with
  $D=(r-1)^3\le S$ at the times $n=2^m$). Proposed replacement: after
  "(only $nM_n^{(r)}-r\le A$, or only $r-nm_n^{(r)}\le A$)" add "with
  $A\ge1$ and $r\ge C_0A$ for an absolute $C_0$, that is, a span error
  small compared with $r$"; and in the Outcome, after "uniformly in the
  position", add "to within an error small compared with $r$".
- **F2 (suggested).** Location: lines 540--543, "The converse passage,
  from counting control to span control, is the elementary direction".
  Defect: read as the converse of the transfer just described it is false
  (S4 attack: counting error at most about $0.39D$ on arcs of length
  $D/n$, span error about $0.44r$, for the Section 2 sequence); the
  intended statement is the reverse direction at a single scale.
  Proposed replacement: "The reverse passage at a single scale, from
  counting control on arcs of length about $r/n$ to span control at scale
  $r$, is the elementary direction and is what Theorem 2 of the
  balanced-stick preprint takes from its Theorem 3; the mechanism's
  content is the descent from scale $r$ to scale $S$, whose strict
  converse fails."
- **F3 (suggested).** Location: lines 529--533, "The conclusion is a
  counting error $O(A)$, pointwise (Proposition 3.1) or in spatial $L^1$
  (Proposition 6.4)". Defect: the pairing with the two hypothesis forms
  is left to the parenthetical references, and under a one-sided
  hypothesis the pointwise conclusion fails. Witness: let $y$ be any
  sequence of distinct points with $r-nm_n^{(r)}(y)\le A_0$ for all large
  $n$ (for instance either sequence of the balanced-stick preprint, by
  its Theorem 2 with $A_0=c'\log r$, since $M_n^{(r)}\ge r/n$), and let
  $x_k=(1-H)y_k$ with $H=A_0/r$, read in $[0,1)$. The map preserves the
  cyclic order, every gap of $x$ is at least $1-H$ times the
  corresponding gap of $y$ (the gap through $0$ gains $H$), so every
  $r$-span of $x$ is at least $(1-H)(r-A_0)/n\ge(r-2A_0)/n$, and the
  second alternative of (6.1) holds with $A=2A_0$. No term lies in
  $[1-H,1)$, so for $n\ge S/H$ the arc $(1-H,1-H+S/n]$ has counting
  error $S$, and $S/A=\sqrt{r/A}/\log^2(r/A)\to\infty$ as $r/A\to\infty$.
  The $L^1$ error of these arcs is at most $SH\le A_0$, consistent with
  Proposition 6.4; the preprint's Section 6 and the Lemma 6.1 page say
  the same in words. Proposed replacement: "pointwise under the two-sided
  hypothesis (Proposition 3.1) and in spatial $L^1$ under either
  one-sided hypothesis (Proposition 6.4); a one-sided bound gives no
  pointwise conclusion".
- **F4 (note).** Location: line 534, "on arcs holding at most
  $\sqrt{Ar}/\log^2(r/A)$ terms". The propositions restrict the arc
  length, $D\le S$ with $D/t$ the length, not the count; an arc of length
  $S/t$ may hold up to $S+CA$ terms. The folder's page descriptions use
  the same shorthand. Proposed replacement: "on arcs of length at most
  $S/t$, $S=\sqrt{Ar}/\log^2(r/A)$".
- **F5 (note).** Location: lines 585--587, "is the only transfer of the
  folder's mechanisms to another setting proved here". Propositions
  1221.1 and 1221.2 on the same page rerun folder mechanisms for the
  coincident-point family; the sentence is true for "another ambient
  space". Proposed replacement: "to the interval".
- **F6 (note).** The status words in the bullets (lines 552--575), the
  search sentence (lines 545--548) and the theory-tree clause (lines
  579--580) are corpus-inventory statements outside this review's read
  set; they are recorded as unverified, not as defective.

## Verdict

- S1: refutation-failed, as a description of (2.1) and (6.1); the range
  clause is charged to S2.
- S2: refuted-as-stated, for the unrestricted implication the sentence
  states; the propositions it paraphrases stand, and the statement with
  the range $r\ge C_0A$ carried is refutation-failed.
- S3: refutation-failed.
- S4: refutation-failed under the single-scale reading; the converse
  reading is false, and the wording should change (F2).
- S5: not a claim (inventory).
- S6: refutation-failed.
- S7: refutation-failed; the status word is not checked.
- S8: refutation-failed for the folder-structure clause; the status words
  are not checked.
- S9: refutation-failed.
- S10: refutation-failed; the status words are not checked.
- S11: refutation-failed for the fixed-set characterization; the
  theory-tree clause is not a claim (inventory).
- S12: not a claim (a decision resting on S5).
- S13: refutation-failed, with the omission of F1 inherited.
- S14: refutation-failed under the ambient-space reading (F5).

Limitations. The status of each named problem and the completeness of
the corpus search are outside the read set and remain unverified here.
The witnesses for F1 and F2 use the 1949 Section 2 sequence and are
self-contained; the witness for F3 assumes a base sequence with
one-sided span error $A_0$ small compared with $r$, whose existence rests
on the balanced-stick preprint's Theorem 2 as reconstructed, with its
imported Theorem 3. An observation outside the subject, for the owner of
the page's Problem 480 section and not reviewed here: its sharpness
paragraph says the first $n$ terms of $\log_2(2k-1)$ mod $1$ are
$\log_2(k/n)$ for $n\le k\le2n-1$; by Section 2 of the note they are
$\log_2k$ mod $1$ for $n\le k\le2n-1$, which coincides with $\log_2(k/n)$
only when $n$ is a power of two (at $n=3$ the terms are $\log_2$ of $1$,
$5/4$ and $3/2$), and the smallest interior gap is $\log_2(2n/(2n-1))$
unless $n$ is a power of two; the limit $ng_n\to1/\log4$ is unaffected.

This focused review assigns no tier and changes no status.
