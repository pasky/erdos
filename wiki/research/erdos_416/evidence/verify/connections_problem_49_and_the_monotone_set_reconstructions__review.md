---
name: research/erdos_416/evidence/verify/connections_problem_49_and_the_monotone_set_reconstructions__review
title: "Independent review of the connections section: Problem 49 and the monotone-set reconstructions: shared inputs"
desc: |
  Refutation review of the section's ten statements: nine survive
  (refutation-failed) and one bookkeeping sentence about the Problem 49
  folder index is refuted-as-stated at the pinned commit; zero required
  corrections, three suggested, one note.
created: 2026-09-28T18:37:28Z
updated: 2026-09-28T20:40:27Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, commissioned for
refutation only. The reviewer took no part in writing the page under
review or any page of the Problem 416 or Problem 49 folders, had no
contact with their authors, and read no review, grade, current assessment
or acceptance text except as disclosed under Exposures below.

**Subject.** The source as it stood on 2026-09-28T13:50:48Z (called "the
commit" below), file
`wiki/research/erdos_416/connections.md`, section "Problem 49 and the
monotone-set reconstructions: shared inputs", lines 563--591 (the H2
heading is line 563; the next H2 is line 592). The commission named no
lead page; the section itself names the pages of the Problem 49 folder
about which it makes its claims, and those pages were read as the
subjects of the claims (see Exposures).

**Read, and at what depth.**

- The section, every sentence, against the page's Notation and "Imported
  inputs" paragraphs before its first H2, whose interfaces (F), (F8) and
  (W) were confirmed at each use; their proofs were not checked here.
- The Problem 417 section of the same page (lines 91--341): only the
  statements of Lemma 417.1(a), Proposition 417.2, Theorem 417.3 with its
  input line and Remarks (i)--(iii), and Proposition 417.4, as the
  interfaces the section cites; none of their proofs.
- [[research/erdos_416/zeraoulia_theorem_1_1_reconstruction|The preprint's page]]:
  only the definitions of $\Psi$ and $M$, to confirm that the $M(x)$ of
  (F) is Ford's $Z(x)$.
- [[problems/primes/E0049/_index|Problem 49]] and
  [[problems/arithmetic_functions/E0417/_index|Problem 417]]: the Statement
  paragraphs.
- The Problem 49 folder at the same commit:
  [[research/erdos_49/lemma_4_1_reconstruction|Lemma 4.1]] in full,
  [[research/erdos_49/theorem_1_2_reconstruction|Theorem 1.2]] in full,
  [[research/erdos_49/lemma_5_1_reconstruction|Lemma 5.1]] in full, and
  [[research/erdos_49/connections|its connections page]] at its opening,
  "Notation and the inputs used", the Problem 417 and Problem 416
  sections and the closing "Problem 49: the remaining clause" section; of
  [[research/erdos_49/_index|its index]] only the lines mentioning 416 or
  417 (lines 19 and 148--158), found by search.
- Library, against the held files: the Ford (1998) conversion at §1.2,
  §1.3 (Theorem 8), §5 (the candidate set (5.13)--(5.16), (5.17), the
  trivial solutions of (5.18) and (5.19)) and §7.3, with Theorem 8, the
  §5 trivial-solution passage and the §7.3 witness list also read on the
  PDF text layer; the Pollack--Pomerance--Treviño manuscript at p. 7 (the
  order-of-magnitude sentence), Lemma 4.1 (pp. 8--9) and Lemma 5.1 (p. 9),
  read on the page images of pp. 7 and 9 and on the text layer; the
  Maier--Pomerance paper's closing section (pp. 274--275), read on the
  page image, the PDF having no text layer. The provenance paragraphs of
  the four cards were read.
- Guidance: `docs/verification.md` ("Whole-claim report", "Audit
  checklist", "Grading and claim standing"), `docs/approach_vetting.md`,
  `docs/evidence.md` ("Source fidelity"), `docs/math_authoring.md`.

**Independent computation.** The preimage sets of $2^{18}\cdot257$, of
$2^{18}\cdot257+28$ and of $54$ were enumerated by the reviewer's own
divisor recursion in exact integer arithmetic (every prime $p$ dividing a
preimage of $d$ has $p-1\mid d$; exponents are enumerated), cross-checked
against brute force over $n\le10^5$ for every $d\le3000$ with no
mismatch. A first version of the recursion stopped at remainder $1$
without trying the prime $2$, so it missed the double of every odd
preimage; the mismatch with the Lemma 5.1 page's list for $d_2$ exposed
it, and the corrected version is the one cross-checked. Primality of
$67371037$ was decided by trial division to its square root.

**Exposures.** (1) The Statement paragraph of Problem 49 is followed on
the same page by a Status paragraph (standing text), which was read
because the section's Target sentence characterizes it. (2) The one-line
Status of Problem 417 was read in the same way. (3) The four Problem 49
folder pages named above lie outside the commissioned read set; they are
the subjects of the section's claims and were read to check those
claims, including each page's own "Standing" paragraph and the
connections page's "Outcomes at a glance" paragraph, all author-recorded
standing text. (4) The directory
`wiki/research/erdos_416/evidence/verify/` was listed to see whether it
existed; its existing files were not opened. Nothing else outside the
allowed set reached the reviewer; no web search was made.

## Restatement

Conventions: $\varphi$ is Euler's function; a totient is a value of
$\varphi$ on the positive integers, so $1=\varphi(1)$ is a totient; the
preimages of a totient $v$ are the $m$ with $\varphi(m)=v$. $T(x)$ is the
set of totients in $[1,x]$ and $V(x)=|T(x)|$; Problem 417's count is
$V'(x)=\#\{\varphi(m):1\le m\le x\}$; $S(k)$ is the set of totients all
of whose preimages are divisible by $k$; Ford's function is

$$
Z(x)=\frac{x}{\log x}\exp\bigl(C(\log_3x-\log_4x)^2+C'\log_3x
-(C'+\tfrac12-2C)\log_4x\bigr),
$$

which is the $M(x)$ of (F) (the preprint's page writes $D$ for $C'$).

- **S1** (target). Problem 49 asks, for $A\subseteq\{1,\ldots,N\}$ with
  $\varphi$ strictly increasing on $A$, whether the primes are a largest
  such $A$, whether $|A|<(1+o(1))\pi(N)$, and whether $|A|=o(N)$. The
  section asserts that the first clause is open, that the second and
  third are proved, and that Theorem 1.2 of Pollack, Pomerance and
  Treviño is reconstructed in the Problem 49 folder.
- **S2** (obstruction). Nothing in the Problem 416 reconstructions (the
  doubling law, the cluster interval, the Problem 417 statements of the
  same page) transfers to the open first clause: for every $N$, whether
  the primes are a largest strictly increasing set in $\{1,\ldots,N\}$ is
  not decided by any statement about the counting functions $V$, $V'$.
- **S3** (identity of counts). The function $W(x)=\#\{\varphi(n):n\le x\}$
  of the Problem 49 folder equals Problem 417's $V'(x)$ for every real
  $x$.
- **S4** (a third count). The $V'(x)$ of Maier and Pomerance's closing
  section, $\#\{\varphi(n)\le x:n>x\}$, is a count different from both
  $V$ and Problem 417's $V'$.
- **S5** (shared input). The Theorem 1.2 reconstruction of the Problem 49
  folder consumes the same input (W), the order of magnitude
  $V(x)\asymp V'(x)$ quoted from p. 7 of the manuscript, as the
  boundedness $\beta=\limsup V/V'<\infty$ of Proposition 417.2.
- **S6** (reversed pair). With $d_1=2^{18}\cdot257=67371008$ and
  $d_2=d_1+28=67371036$: $d_1<d_2$, and the least preimage of $d_1$
  exceeds the largest preimage of $d_2$.
- **S7** (witness membership). $d_1$ is the $d$ that Ford's §7 lists for
  $k=4$, and $d_1\in S(4)$: every preimage of $d_1$ is divisible by $4$.
- **S8** (the route). There is a proof of $V(x)\ll V'(x)$ that rests on
  Lemma 4.1 of the manuscript as reconstructed in the Problem 49 folder,
  namely clause (iii), $n/\varphi(n)\le K$ on the candidate set, together
  with the two counts (F1), (F2) that page imports from Ford's §5, and
  that does not rest on (W) as the cited authors' reading of Ford.
- **S9** (index bookkeeping). At the pinned commit, the Problem 49
  folder index names Problems 416 and 417 as leads, and its lead sentence
  for 416 and 417 is answered by the page under review.
- **S10** (closing paragraph). At the pinned commit the Problem 49 index
  no longer names 416 and 417 as bare leads; the Problem 49 connections
  page assesses them, reaches the Problem 417 statements independently
  from Lemma 4.1, and points at the lead distinct_totient_preimage_ratio
  as the single carrier of that route.

## Checklist

- **Quantifiers and scope.** Pass. S2 is stated for every finite $N$ and
  is checked for every $N$ (W2). S6 and S7 are finite exact facts. S3 is
  an identity for all real $x$; S4 needs one $x$ and is given one. S8
  asserts the existence of a proof of an eventual bound with an absolute
  constant, and the reconstructed bridge has that shape.
- **Circularity.** Pass. The S8 route uses Lemma 4.1 (its (i)--(iii)) and
  Ford's Theorem 1, not the p. 7 quotation, and the p. 7 quotation is not
  used to prove anything in the section. One nuance: (F1), (F2) and (W)
  are all the same authors' readings of Ford's §5, at different levels
  (adapted proof versus bare attribution); this is provenance, not
  circularity.
- **Model and convention changes.** Pass. $W$, $V'$ and $V$ were compared
  by their defining sets, not by name; both folders take totients over
  the positive integers with $1$ included. Maier and Pomerance's $V'$ and
  $V_0$ were read on the page image.
- **Finite and statistical overreach.** Pass. The only finite computations
  (S6, S7) support finite claims and are complete enumerations; Ford's
  "short search" is used only to identify a witness.
- **Uniformity.** Pass with a precision remark. The section makes no
  uniformity claims of its own; in the S8 bridge the constants are
  absolute ($K$, $c_K$ with $D=K$, Ford's $C_1$). S5's identification is
  exact only up to the clause and strength consumed (F1).
- **Extremal conclusions.** Pass. S6 is an extremal sentence (least and
  largest preimage) and was checked in its own units by complete
  enumeration: $\min\varphi^{-1}(d_1)=135268352$ and
  $\max\varphi^{-1}(d_2)=134742074$, difference $526278$.
- **Consequences and composition.** Pass with two findings. S8 names
  clause (iii) as "the route", while the bridge needs clause (ii) for
  injectivity and Ford's upper bound for the last step (F2). S5 names (W)
  where the consuming page names $W\asymp Z$ and uses only
  $x/\log x=o(W(x))$ (F1).
- **Computation.** Pass. Exact integer arithmetic; the enumerator was
  validated against brute force; the one bug found in the reviewer's own
  first draft is disclosed above and did not affect the corrected
  results.
- **Reproduction.** Not applicable to the section, which states no rerun
  commands; the page's own computations of these preimages are
  author-recorded and unfiled, and were reproduced independently here.
- **Source and verdict fidelity.** Pass with one refuted bookkeeping
  sentence. Ford's witness sentence, Theorem 8, the manuscript's p. 7
  sentence and its p. 9 pair, Lemma 4.1's statement and the proof of its
  (iii), and Maier and Pomerance's definitions were checked against the
  held files and match the section. The Target sentence's description of
  the Problem 49 index does not match the index at the pinned commit
  (F3).

## Weakest steps

**W1: the bridge behind S8, re-derived.** Lemma 4.1, as reconstructed,
says: for fixed totients $d_1,d_2$ and fixed $D\ge\max\{d_1,d_2\}$ there
are an absolute $K\ge1$, a $c_D>0$ and $x_0(D)$ such that for
$x\ge x_0(D)$ at least $c_DZ(x)$ integers $n$ satisfy (i)
$\varphi(n)\le x/D$, (ii) $n$ convenient for $d_1$ and $d_2$, (iii)
$n/\varphi(n)\le K$. Take $d_1=d_2=1$, whose preimages are exactly $1$
and $2$, and $D=K$ (allowed since $K\ge1$). For each of the $\ge c_KZ(x)$
integers $n$ supplied: by (ii), $\varphi(n)$ is a totient with preimages
exactly $n$ and $2n$; by (iii) and (i), $n\le K\varphi(n)\le x$; so
$\varphi(n)\in\{\varphi(m):m\le x\}$. If $\varphi(n)=\varphi(n')$ for two
supplied $n,n'$, the preimage sets $\{n,2n\}$ and $\{n',2n'\}$ coincide,
so $n=n'$. Hence $V'(x)\ge c_KZ(x)$. By (F), $V(x)\le C_1Z(x)$ for large
$x$, so $V(x)\le(C_1/c_K)V'(x)$. Every step is elementary; the load is
carried by (ii) and (iii) jointly and by (F). Clause (iii) alone gives
$n\le x$ but no injectivity: a count of integers bounds the number of
distinct totients only after a multiplicity bound, which is exactly what
convenience supplies. Ford's §5 makes the same move: an $n$ in his
candidate set for which $d\varphi(n)=\varphi(n_1)$ has only the trivial
solutions $n_1=nd_i$ has $\varphi(n')\ne\varphi(n)$ for every other $n'$
in the set. This bridge is Proposition 2 of the Problem 49 connections
page, which the section reaches only through its closing paragraph.

**W2: the obstruction S2, re-derived.** Let $A\subseteq\{1,\ldots,N\}$
have $\varphi$ strictly increasing on $A$. The only implication from the
counting functions to $|A|$ is: the values $\varphi(a)$, $a\in A$, are
distinct and are totients of integers $\le N$, so $|A|\le V'(N)$. No
statement of the Problem 416 folder improves this: the doubling law
$V(2x)/V(x)\to2$, the cluster intervals of $V(cx)/V(x)$ and of
$V(x)/V'(x)$, and Theorem 417.3 are statements about limits and limit
points, with no content at a fixed $N$. And $V'(N)/\pi(N)\to\infty$: by
the Theorem 1.2 page's deduction from its input (C), or by Erdős's 1935
lower bound $W(x)\gg x\log_3x/\log x$ as that page notes,
$V'(N)/(N/\log N)\to\infty$, while $\pi(N)\ll N/\log N$. So the bound
$|A|\le V'(N)$ exceeds $\pi(N)$ by a factor tending to infinity and cannot
decide whether the maximum equals $\pi(N)$ at any large $N$; at small $N$
the exact clause is a finite check untouched by asymptotics. The reversed
pairs of Lemma 5.1 constrain sets on which $\varphi$ is nondecreasing,
that is sets with repeated values; a strict set has none, so they add
nothing either. The obstruction holds at the scope claimed.

**W3: the shared input S5, re-derived.** The Theorem 1.2 page lists as
its input (C) "$W(x)\asymp Z(x)$ for large $x$", sourced to p. 7, and
uses it only through $x/\log x=o(W(x))$. The page under review defines
(W) as "$V(x)\asymp V'(x)$", sourced to the same p. 7 sentence
"$V(x)\asymp W(x)\asymp Z(x)$" (confirmed on the page image). Given (F),
$V\asymp M=Z$, so (W) and (C) are equivalent modulo (F), and both are
clauses of one sentence. But they are different clauses, and Proposition
417.2 needs the upper bound $V\ll V'$ for $\beta<\infty$, whereas the
Theorem 1.2 page needs only a lower bound for $W$ beyond $x/\log x$,
which it says Erdős (1935) supplies equally. The sharing is of a source
sentence, not of a load-bearing dependency.

## Strongest attack

- **S1.** Attack: find a clause misdescribed. The Statement paragraph of
  Problem 49 has the three clauses as restated; the page records the
  first as open and the other two as proved; the Theorem 1.2
  reconstruction exists in the folder and covers the third clause and
  the weak maximum. Failed.
- **S2.** Attack: exhibit a counting-function statement with finite-$N$
  content, or a route from $V$, $V'$ to the maximum of a strict set
  sharper than $|A|\le V'(N)$. W2 shows that bound is the only bridge and
  is off by an unbounded factor; the doubling law and the cluster
  interval are limit statements. Failed.
- **S3.** Attack: a range mismatch ($n\le x$ versus $1\le m\le x$, real
  versus integer $x$). Both sets are the values of $\varphi$ on the
  positive integers $\le x$, for real $x$. Failed.
- **S4.** Attack: the three counts might coincide as functions. Witness
  $x=6$: $T(6)=\{1,2,4,6\}$, so $V(6)=4$; $\{\varphi(m):m\le6\}=\{1,2,4\}$,
  so $V'(6)=3$; $\{\varphi(n)\le6:n>6\}=\{4,6\}$, from
  $n\in\{7,8,9,10,12,14,18\}$, so Maier and Pomerance's count is $2$.
  Three different values; and their count omits $1$ for every $x\ge2$,
  since $1$ has preimages $1$ and $2$ only. Failed.
- **S5.** Attack: the literal label. The Theorem 1.2 page nowhere states
  $V\asymp V'$; it states $W\asymp Z$ and uses less. The attack succeeds
  against the literal wording and fails against the charitable reading
  (one source sentence, equivalent clauses under (F)); recorded as F1.
- **S6.** Attack: an incomplete enumeration, a missed candidate prime, or
  a wrong primality. Candidate primes for $d_1$ are those $p$ with
  $p-1\mid2^{18}\cdot257$: $2,3,5,17,257,65537$, and no prime of the form
  $2^a\cdot257+1$ with $a\le18$ (all composite, checked); $65537$ cannot
  occur, since the factor $257$ must then come from $257^2$, which
  overshoots the power of $2$. The eight preimages, all with $257^2$,
  match the Lemma 5.1 page and the manuscript's $n_1$. For $d_2$,
  $67371037$ is prime and $\varphi(2\cdot67371037)=d_2$; no other
  preimage exists. Failed.
- **S7.** Attack: an odd preimage, or one $\equiv2\pmod4$, of $d_1$; or a
  wrong attribution in Ford's list. The least $2$-adic valuation among
  the eight preimages is $4$, at $2^4\cdot3\cdot5\cdot17\cdot257^2$; an
  odd preimage would need $257$ from $257^2$ plus $2^{10}$ from distinct
  Fermat primes other than $257$, and no subset of $\{1,2,4,16\}$ sums to
  $10$. Ford's §7.3 reads "for $k\in\{2,4,8\}$, take $d=2^{18}\cdot257$".
  Failed.
- **S8.** Attack: the count-of-integers versus distinct-totients gap, and
  the $n\le x$ gap. Both close, by (ii) and by (iii) with $D=K$ (W1); the
  last step needs (F). The attack on "does not rest on (W)" fails: the
  bridge cites (L4) and (F) only. The residual imprecision is F2.
- **S9.** Attack: read the index at the pinned commit. Its lines 148--158
  record outcomes for 417 and 416 and name the Problem 49 connections
  page and the lead as carriers; no sentence names 416 and 417 as leads.
  The attack succeeds: refuted-as-stated at the pinned commit (F3).
- **S10.** Attack: check the three characterizations. The index's
  wording is as just described; Propositions 2--4 of the Problem 49
  connections page use (L4), (P) and (F) only; that page names the lead
  as the carrier and says no second lead is opened. Failed.

## Premises

- **(F)** Ford's Theorem 1 in the form of the preprint's page:
  $V(x)=M(x)e^{E(x)}$ with $|E|\le K$ and $M=(x/\log x)e^{\Psi}$, $\Psi$
  Ford's exponent; used as $V\le C_1Z$ and $V\asymp Z$. Refereed source
  at statement level; held
  ([[../library/arithmetic_functions/ford_1998_distribution_totients/_index|card]]).
  Read: §§1.1--1.3 and §5 of the conversion, Theorem 8 and §5's
  trivial-solution passage on the text layer.
- **(F8)** Ford's Theorem 8 and the §7.3 witness list: used only to
  identify $d_1$ as the $k=4$ witness. Held; the sentence read on the
  text layer.
- **(W)** $V\asymp V'$, the manuscript's p. 7 attribution to Ford's
  §§4--5; held
  ([[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/_index|card]]);
  p. 7 read on the page image. Standing as the page records: the cited
  authors' reading of Ford, not checked against Ford's §5 here.
- **Lemma 4.1 page** (Problem 49 folder): statement with (i)--(iii),
  candidate set, imported counts (F1), (F2), proof of (iii). Read in
  full; treated as established at its recorded standing (author-recorded
  partial reconstruction). The manuscript's Lemma 4.1 and its proof of
  (iii) were read on the p. 9 image; the statement matches the page.
- **Theorem 1.2 page** (Problem 49 folder): inputs (A)--(D), in particular
  (C) $W\asymp Z$ and its use. Read in full.
- **Lemma 5.1 page** (Problem 49 folder): the explicit pair and its
  enumeration. Read in full; the enumeration reproduced independently.
- **Problem 49 connections page**: (L4), (P), Proposition 2 (the bridge
  of W1), Propositions 3 and 4, the Problem 416 section and the closing
  section. Read at those sections.
- **Maier and Pomerance (1988)**, closing section: the definitions of
  $V'$ and $V_0$. Held
  ([[../library/arithmetic_functions/maier_1988_number_distinct_values_euler_s_function/_index|card]]);
  read on the page image, the PDF having no text layer.
- **Problem pages** E0049 and E0417: Statement paragraphs.
- **(KK)** is listed among the page's inputs but is not used by the
  section; not read beyond its bullet.

## Findings

- **F1** (suggested). Location: "its Theorem 1.2 reconstruction consumes
  the same input (W) as the boundedness in Proposition 417.2". Defect:
  the Theorem 1.2 page's input is (C) "$W(x)\asymp Z(x)$", the other
  clause of the same p. 7 sentence, and it is consumed only through
  $x/\log x=o(W(x))$, for which that page says Erdős (1935) serves
  equally; Proposition 417.2 consumes the upper bound $V\ll V'$. Witness:
  the Theorem 1.2 page, "Imported inputs", item (C), and its deduction of
  $x/\log x=o(W(x))$ from (C). Replacement: "its Theorem 1.2
  reconstruction rests on the same p. 7 sentence as (W), there as
  $W\asymp Z$, equivalent to (W) under (F), and used only for
  $W(x)/(x/\log x)\to\infty$, which Erdős's 1935 lower bound also gives;
  the boundedness in Proposition 417.2 needs the clause $V\ll V'$
  itself".
- **F2** (suggested). Location: "Lemma 4.1(iii) of that folder, ..., is
  the route to $V\ll V'$". Defect: the route needs clause (ii)
  (convenience for the totient $1$, giving injectivity of
  $n\mapsto\varphi(n)$ through the least preimage) and Ford's upper bound
  $V\le C_1Z$ as well as (iii); the bridge is written on the Problem 49
  connections page as its Proposition 2, which the section does not
  name. Witness: W1 above. Replacement: "Lemma 4.1 of that folder, its
  clauses (ii) and (iii) with the seed $d=1$ and $D=K$, together with the
  two counts imported from Ford's §5 and Ford's upper bound (F), is the
  route to $V\ll V'$ (Proposition 2 of that folder's connections page)
  that does not rest on (W) as the cited authors' reading".
- **F3** (suggested). Location: "whose index names Problems 416 and 417
  as leads" (Target) and "the lead sentence of the Problem 49 index for
  416 and 417 is answered by this page" (Outcome), against the closing
  paragraph "no longer names 416 and 417 as bare leads". Defect: at the
  pinned commit the index records outcomes for 417 and 416 and names the
  Problem 49 connections page and the lead as their carriers (index lines
  148--158); the Target and Outcome sentences describe an earlier state,
  and the closing paragraph corrects them with a chronology ("no
  longer"), which a retained page should not carry. Witness: the index
  lines cited in the S9 attack. Replacement: state the present relation
  once, for example "whose index records the outcomes for 416 and 417 and
  points to its connections page and the lead
  distinct_totient_preimage_ratio", and drop the Outcome clause about
  answering a lead sentence.
- **F4** (note). Location: "an element of the set $S(4)$ of Theorem
  417.3". $S(4)$ does not occur in Theorem 417.3, whose witness is
  $d=54\in S(3)$; it occurs in Remark (ii) after it and is defined in the
  page's Notation. Replacement: "of Remark (ii) to Theorem 417.3" or "in
  the page's notation".

## Verdict

- S1: refutation-failed.
- S2: refutation-failed.
- S3: refutation-failed.
- S4: refutation-failed.
- S5: refutation-failed under the reading that (W) names the p. 7
  sentence; the literal label is corrected by F1.
- S6: refutation-failed.
- S7: refutation-failed.
- S8: refutation-failed; the bridge is supplied in W1, and F2 asks the
  section to name it.
- S9: refuted-as-stated at the pinned commit (F3).
- S10: refutation-failed.

Limitations: the proofs of (F), (F8), (W) and of the Problem 49 folder's
pages were not checked; Ford's §5 was read only for the trivial-solution
mechanism and (5.17), not re-derived; the preimage enumerations are the
reviewer's own and are not filed as evidence; nothing outside the held
corpus was consulted. Zero required corrections, three suggested, one
note.

This focused review assigns no tier and changes no status.
