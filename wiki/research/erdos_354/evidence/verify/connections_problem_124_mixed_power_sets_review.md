---
name: research/erdos_354/evidence/verify/connections_problem_124_mixed_power_sets_review
title: "Independent review of the connections section: Problem 124: mixed power sets"
desc: |
  Refutation-focused review of the Problem 124 section of the Problem 354
  connections page as of 2026-09-28T13:50:48Z: the obstruction that nothing
  transports survives attack, while the section's rendering of Fan's
  Theorem 1.5 is refuted-as-stated. One required correction, two suggested,
  two notes.
created: 2026-09-28T18:33:29Z
updated: 2026-09-28T20:40:46Z
---

***

## Subject and independence

Role: independent reviewer in a fresh context, commissioned for refutation.
The reviewer took no part in writing the connections page, the
reconstruction pages or any other page in the folder, read no earlier review
or grade, and made no web search.

Subject: `wiki/research/erdos_354/connections.md` as it stood at
2026-09-28T13:50:48Z, section "Problem 124: mixed power sets", lines 580--609
(the H2 at line 580 through the line before the next H2 at line 611). No
separate lead page was named; the page's shared opening (lines 1--58: the
standing paragraph, the folder notation and the definitions of complete,
strongly complete, normalized pair, dyadic rational, Hegyvári's conjecture and
Fan's condition (1.5)) was read in full as input.

Reading, at depth:

- The section, in full, every sentence attacked.
- `wiki/problems/diophantine_problems/E0124/_index.md`, lines 1--52: frontmatter
  and the Statement, Status, Source, References and Formalization
  paragraphs. The H2 sections (Current assessment, Progress, Known Results,
  Linked library material) were not opened.
- The Fan card
  [[../library/additive_bases/fan_2026_strongly_complete_sets_conjecture_erdos/_index|fan_2026_strongly_complete_sets_conjecture_erdos]],
  in full (see exposures); its result page `remark_4_2.md` was not opened.
- The held PDF `fan_2026_strongly_complete_sets_conjecture_erdos.pdf` (v5;
  the checked-out file's SHA-256 equals the card's provenance line): pages 7
  and 34 read as page images (Theorem 1.5 with (1.13), the
  Bergelson--Simmons sentence, Lemma 2.1 and the definition of $\Delta$;
  Section 7 in full); pages 6--10 and 34--36 in the text layer ((1.12) and
  its footnote, Theorem 2.2, Lemma 2.3, Corollary 2.4, the appendix). The
  v4 PDF's text layer was searched only to confirm that the labels Theorem
  1.5, Lemma 2.1, Theorem 2.2 and Section 7 are the same in both versions.
- [[research/erdos_354/yu_chen_normalization_reconstruction|the normalization page]]:
  Definitions, Statement (items 1--6 and the Reduction) and the four proofs
  of item 6, as premises.
- [[research/erdos_354/fan_remark_4_2_reconstruction|the Remark 4.2 page]]:
  Statement and Step 3 of the proof (condition (1.5) for the two-ray set),
  as premises; the folder's other reconstruction pages were listed by name
  only.
- `docs/verification.md` ("Grading and claim standing", the canonical audit
  checklist, "Whole-claim report", "Audit checklist"),
  `docs/approach_vetting.md`, `docs/evidence.md` ("Source fidelity") and
  `docs/math_authoring.md`, in full.

Exposures: (1) the Fan card was read in full, beyond its provenance
paragraph; its Bears-on paragraph carries Problem 354 standing text (the
site-accepted part (i) proof and a quoted phrase from the site's review),
which concerns another section's target and was not used here; (2) twelve
lines of the page's Problem 354 section (lines 59--70) were printed while
locating the page's conventions; they paraphrase that problem's Current
assessment and were not used; (3) the first fifteen lines of the page's
closing section "No further consumer" (from line 611) were printed with the
subject section, and their description of the descent's inputs was used to
read the word "descent" in S5; (4) a directory listing of
`wiki/research/erdos_354/evidence/verify/` showed the file names of the
folder's other reviews and its grade page; none was opened. Nothing else
outside the allowed set reached the reviewer.

## Restatement

Notation: $P(D)=\bigcup_{d\in D}\{d^n\}$ is Fan's mixed power set,
$P(d,k)$ is the problem page's set of sums of distinct powers $d^i$ with
$i\ge k$, and "the descent" is the folder's mechanism as the page's closing
section describes it: two interlaced base-$2$ rays with the digit
recurrence $a_{i+1}=2a_i+u_i$, $u_i\in\{0,1\}$, the interlacing
$b_i<a_i<2b_i\le b_{i+1}$ of item 4 of the normalization page, and a
reduced ratio at the block's first layer.

- **S1 (target).** Problem 124 asks, for integers $3\le d_1<\cdots<d_r$
  with $\sum_{i=1}^r1/(d_i-1)\ge1$, whether every sufficiently large
  integer is $\sum_ic_ia_i$ with $c_i\in\{0,1\}$ and $a_i\in P(d_i,0)$;
  and, when $\gcd(d_1,\ldots,d_r)=1$, whether the same holds with
  $a_i\in P(d_i,k)$ for every $k\ge1$. The section words the second
  hypothesis as "the $d_i$ are coprime" and does not state the quantifier
  over $k$.
- **S2 (page status).** The problem page's status is open, and its
  progress is not compiled.
- **S3 (Fan's Theorem 1.5 as the section renders it).** The Fan card
  records Theorem 1.5 at statement level, and the theorem says: $P(D)$ is
  strongly complete whenever $D=D_1\cup D_2\cup C$ with $\gcd(C)=1$ and
  $\sum_{d\in D_i}1/(d-1)\ge1$ for $i=1,2$; this needs one component fewer
  than the Bergelson--Simmons theorem. No hypothesis on $D$ beyond the
  partition is stated.
- **S4 (folder index).** The folder index names Problem 124 only as a
  further target of the same preprint.
- **S5 (obstruction).** Nothing transports from the folder to Problem 124:
  the problem's objects are the single-coefficient rays $\{d^n\}$ at
  distinct integer bases $d\ge3$ without floors; the descent needs two
  base-$2$ rays with the digit recurrence and the interlacing
  $b_i<a_i<2b_i\le b_{i+1}$; a power set has none of these.
- **S6 (proof route of Theorem 1.5).** Theorem 1.5 is not reconstructed in
  the folder, and its proof (the source's Section 7) runs through the
  three-component criterion (Theorem 2.2), using nothing from the folder.
- **S7 (shared step).** The only step common to that proof and the folder
  is elementary: the bounded-$\Delta$ argument giving syndetic subset sums,
  which is Fan's Lemma 2.1 and, for two rays, item 6 of the normalization
  page; this is a resemblance of tools, not a transfer of a result.
- **S8 (yield).** The folder's mechanism gives nothing about either
  question of Problem 124.
- **S9 (next step).** No investigation follows from the folder; the
  compilation task is a reconstruction of Theorem 1.5 from Theorem 2.2.
- **S10 (outcome).** The transfer fails.

## Checklist

- **Quantifiers and scope.** Defective in the descriptive sentences only.
  S1 drops "for every $k\ge1$" and blurs $\gcd(d_1,\ldots,d_r)=1$ into
  "the $d_i$ are coprime", which a reader can take as pairwise coprimality,
  a stronger hypothesis (F2). S3 drops three hypotheses of Theorem 1.5
  (F3). S5 and S8 quantify correctly: "nothing transports" is a universal
  claim over the descent's inputs, and the Strongest attack below confirms
  it.
- **Circularity.** Not applicable: the section proves nothing from the
  folder's results and assumes no target.
- **Model and convention changes.** Two conventions meet in the section
  without a claimed bridge: the problem's multiset formulation
  ($\sum_ic_ia_i$ with $a_i\in P(d_i,0)$, so each base contributes its own
  $d_i^0=1$) and Fan's set union $P(D)$, which the source itself calls a
  "slightly stronger set-theoretic formulation" (p. 6). The section asserts
  no equivalence and deduces nothing across them, so no unproved transfer
  is made. The descent's conventions (normalized pair, item 4) are cited at
  their actual hypotheses.
- **Finite and statistical overreach.** Not applicable: no finite
  verification or heuristic is used.
- **Uniformity.** Not applicable: no constant or bound is claimed.
- **Extremal conclusions.** The one comparative count, "one component fewer
  than Bergelson--Simmons", is checked in its own units against the source
  (p. 7): the cited Bergelson--Simmons theorem needs a partition
  $D_1\cup D_2\cup D_3\cup C$ with (1.12) for each $D_i$; Theorem 1.5 needs
  $D_1\cup D_2\cup C$ with (1.13) for $i=1,2$. Correct as a relay of the
  source; the Bergelson--Simmons paper is not held (F5).
- **Consequences and composition.** S8 and S10 follow from S5, and S5 is
  established independently below. S9's "with Theorem 2.2" is accurate but
  incomplete as a dependency list: Section 7 also consumes Lemma 3.1
  (bounded successive ratios give a countable $H_2$) and an elementary
  argument for $H_1(\mathcal C)=\{0\}$; nothing in the section claims
  otherwise.
- **Computation.** Not applicable in the section. The reviewer's one
  computation is the inequality $d_r\ge r+2$, hence $r/(d_r-1)<1$, in F1.
- **Reproduction.** Not applicable: no rerun instruction or coverage claim.
- **Source and verdict fidelity.** Defective in two places. S1's density
  condition is not the page's typed condition (F1). S3 attributes to the
  card a statement the card does not carry and renders Theorem 1.5 without
  its hypotheses (F3). S6 and S7 are faithful to pages 7--8 and 34 of the
  source, with the "only" of S7 overstated (F4). S2's second clause and S4
  concern excluded text and are unverified.

## Weakest steps

**W1: the obstruction, S5.** The section argues by shape only: a power set
lacks the descent's inputs. Since completeness passes to supersets, the
attack that matters is whether some two-ray set $A_{\alpha,\beta}\setminus F$
sits inside $P(D)$, or inside the multiset $\biguplus_i\{d_i^n\}$, so that
the descent applied to that subset would transfer. The derivation under
Strongest attack shows that for finite $D$ with $2\notin D$ no tail
$\{\lfloor2^n\alpha\rfloor:n\ge n_0\}$ of any base-$2$ ray lies in $P(D)$,
and that for finite $D$ with $2\in D$ only the ray $\{2^n\}$ can, so that
two such rays have a ratio that is a power of $2$ and fall outside every
hypothesis the descent carries. The obstruction therefore holds for subsets
as well as for the sets themselves, which the section does not say but does
not need.

**W2: the restatement of Theorem 1.5, S3.** Re-read on the page image of
p. 7: "Let $D\subseteq\mathbb N_{\ge2}$ be a nonempty finite subset with no
two elements being powers of the same integer. Suppose that
$D=D_1\cup D_2\cup C$ is a partition of $D$ into nonempty subsets such that
$\gcd(C)=1$ and (1.13) [$\sum_{d\in D_i}1/(d-1)\ge1$] for every $i=1,2$.
Then $P(D)$ is strongly complete." The section keeps the partition, the gcd
and (1.13) and drops finiteness, the no-common-power condition and the
nonemptiness of the parts. Finiteness is used in Section 7's bound
$b-\sum_{b'<b}b'\le\sum_{d\in D_i}d^k/(d-1)$, whose right side is finite
only for finite $D_i$; the no-common-power condition is what makes
$P_k(D)=\mathcal B_1\cup\mathcal B_2\cup\mathcal C$ a partition, as Section
7 says, and without it (1.13) can be met by proper powers whose union of
power sets is smaller than the count suggests (for instance
$D_1=\{4,8,\ldots,2^m\}$ has $P(D_1)\subsetneq\{2^n\}$). The weakened
statement is not shown false here; it is simply not the source's theorem.

**W3: the "only shared step", S7.** Section 7 has four steps:
$\Delta(\mathcal B_i)<\infty$ from (1.13) by a geometric sum;
$H_2(\mathcal C)$ countable from bounded successive ratios (Lemma 3.1);
$H_1(\mathcal C)=\{0\}$ from the exact recurrence $r_{n+1}(c)=c\,r_n(c)$
and $\gcd(C)=1$; and Theorem 2.2. Item 6 of the normalization page proves
$\operatorname{gap}(P_n)\le N$ from $c_{j+1}-\sum_{i\le j}c_i\le N$ on the
merged list, a bounded-$\Delta$ argument as the section says, and Lemma 2.1
is the same principle for infinite sets, so the first resemblance is real.
But Step 3 of the Remark 4.2 page proves (1.5) for $A_{\alpha,\beta}$ from
$c_{k+1}=2c_k+1$ infinitely often, which is the same kind of step as
Section 7's $H_1(\mathcal C)=\{0\}$ (a base recurrence pushed through
$\|\cdot\,\theta\|$), by a different argument. By the section's own
standard for "shared" (the two bounded-$\Delta$ arguments also differ in
detail), there are two shared steps, both tools and neither a result.

## Strongest attack

**On S5 and S8 (the obstruction).** The attack: find $\alpha,\beta>0$ with
$\alpha/\beta$ not a power of $2$ and a finite $F$ such that
$A_{\alpha,\beta}\setminus F\subseteq P(D)$ for some $D$ of Problem 124, or
the analogous inclusion in the multiset $\biguplus_i\{d_i^n\}$; the descent
on the subset would then give completeness of the larger set. It fails, by
the following derivation.

Let $D$ be finite with $\min D\ge2$, let $\alpha>0$, and write
$x_n=\lfloor2^n\alpha\rfloor$ and $u_n=x_{n+1}-2x_n\in\{0,1\}$. Suppose
$x_n\in P(D)$ for all $n\ge n_0$, each $x_n$ being some $d^m$ with
$d\in D$ and $m\ge1$ (the value $1=d^0$ is excluded once $x_n>1$).

Case A, $\alpha$ not a dyadic rational, so $u_n=1$ for infinitely many $n$
(if $u_n=0$ for all $n\ge n_1$ then $x_n=2^{n-n_1}x_{n_1}$ and
$\alpha=\lim2^{-n}x_n=x_{n_1}/2^{n_1}$). Take $n\ge n_0$ with $u_n=1$.
Then $x_{n+1}=2x_n+1$ is odd, so $x_{n+1}=d'^{m'}$ with $d'\in D$ odd. If
$u_{n+1}=0$, then $x_{n+2}=2d'^{m'}=d''^{m''}$ with $d''\in D$; comparing
$2$-adic valuations gives $m''v_2(d'')=1$, so $m''=1$ and
$d''=2d'^{m'}=2x_{n+1}$, whence $x_{n+1}\le\max D/2$, which fails once $n$
is large. So for all large $n$, $u_n=1$ forces $u_{n+1}=1$; hence
$u_n=1$ for all $n\ge n_1$ for some $n_1$, and then
$x_n+1=2^{n-n_1}(x_{n_1}+1)$ gives $\alpha=(x_{n_1}+1)/2^{n_1}$, so
$x_{n_1}=\lfloor2^{n_1}\alpha\rfloor=x_{n_1}+1$, a contradiction. No tail
of such a ray lies in $P(D)$.

Case B, $\alpha=c/2^s$ with $c$ an odd positive integer. Then
$x_n=2^{n-s}c$ for $n\ge s$. If $c>1$, then $2^{n-s}c=d^m$ forces $d=2^eg$
with $g$ odd, $g^m=c$ and $em=n-s$; for each $d\in D$ the equation $g^m=c$
has at most one solution $m$, so only finitely many $n$ qualify. If $c=1$,
the ray is $\{2^n\}$, and $2^{n-s}=d^m$ forces $d=2^e$; the exponents
$E=\{e\ge1:2^e\in D\}$ form a finite set, and $n-s$ must be a positive
multiple of some $e\in E$ for every large $n$, which fails at a prime
$n-s$ exceeding $\max E$ unless $1\in E$, that is, unless $2\in D$.

Hence for the problem's sets ($d_i\ge3$, so $2\notin D$) no base-$2$ ray
has a tail in $P(D)$, and the same holds elementwise in the multiset
formulation, since each element is still some $d_i^m$. No two-ray set, and
no set with a two-ray subset of the kind the descent takes, occurs. Under
Fan's wider hypothesis $D\subseteq\mathbb N_{\ge2}$, the only ray tail
available is $\{2^n\}$ itself, and two such rays have a ratio that is a
power of $2$, outside the descent's hypothesis of an irrational ratio
(normalization item 2) and outside the rational-ratio target of the page's
first section (neither coefficient a dyadic rational). S5 survives, and S8
and S10 with it.

**On S3.** The attack: check the rendered statement against the source. It
succeeds against the sentence as stated: the card's only mention of the
theorem is "Theorem 1.5, mixed power sets; all at statement level only
here", and the source's theorem carries three hypotheses the section omits
(W2). The mathematical content of the weakened statement was not disproved;
see Findings.

**On S6 and S7.** The attack: find a step of Section 7 that consumes a
folder result, or a second shared step. The first fails: Section 7 cites
Theorem 2.2, Lemma 3.1 and (1.13) only, neither Remark 4.1 nor Remark 4.2
nor any Yu--Chen or Geneson result, and the folder holds no reconstruction
of Theorem 1.5 (its pages are the two Fan remarks, the two Geneson results
and the Yu--Chen pages). The second succeeds against the word "only" (W3,
F4) but not against the sentence's operative content, since the second
shared step is also a tool and not a result.

**On S1.** The attack: compare with the page's typed statement. The page
reads $\sum_{1\le i\le r}1/(d_r-1)\ge1$, that is, $r/(d_r-1)\ge1$; with
$3\le d_1<\cdots<d_r$ one has $d_r\ge r+2$, so $r/(d_r-1)\le r/(r+1)<1$
and the typed condition is never satisfied. The section's
$\sum_i1/(d_i-1)\ge1$ is the source's (1.12), attributed there to the
Burr--Erdős--Graham--Li paper. The section therefore describes the intended
problem and silently departs from the page it links (F1); the mathematics
of the sentence is not refuted.

## Premises

- Fan, *Strongly complete sets and a conjecture of Erdős*,
  arXiv:2607.14071v5, held as the card's folder-name PDF (36 pages; the
  checked-out file's SHA-256 matches the card's provenance line).
  Interfaces used: (1.12) and the footnote on its necessity (p. 6, text
  layer); Theorem 1.5 and the Bergelson--Simmons sentence (p. 7, page
  image); Lemma 2.1 and $\Delta(S)$ (p. 7, page image); Theorem 2.2,
  Lemma 2.3 and Corollary 2.4 (pp. 8--10, text layer); Section 7 (p. 34,
  page image); the appendix (pp. 34--35, text layer). None of its proofs
  was reviewed. The v4 PDF (held) was consulted in its text layer only for
  label stability.
- Bergelson and Simmons, *New examples of complete sets, with connections
  to a Diophantine theorem of Furstenberg*, Acta Arith. 177 (2017),
  Theorem 1.23: not held; its content is known here only as Fan states it
  on p. 7.
- Burr, Erdős, Graham and Li, *Complete sequences of sets of integer
  powers*, Acta Arith. (1996): not held; the problem page lists it as
  [BEGL96] and Fan cites its Theorem 1.
- [[research/erdos_354/yu_chen_normalization_reconstruction|the normalization page]]
  as of 2026-09-28T13:50:48Z (author-recorded reconstruction, independently
  reviewed as of 2026-09-28T05:03:27Z per the assignment): items 4 and 6 for a
  normalized pair ($N=\lfloor\beta\rfloor<M=\lfloor\alpha\rfloor<2N$,
  $N\ge2$), read with their proofs of item 6; used as the interface the
  section cites.
- [[research/erdos_354/fan_remark_4_2_reconstruction|the Remark 4.2 page]] as of
  the same time: Statement and Step 3 (condition (1.5) for $A_{\alpha,\beta}$),
  used only to test S7.
- [[problems/diophantine_problems/E0124/_index|Problem 124]]: the Statement
  paragraph and the frontmatter `status: open`; nothing below the first
  H2.
- The connections page's shared opening (lines 1--58) for notation and the
  standing paragraph; the opening of its "No further consumer" section for
  its description of the descent's inputs, which the reading of S5 relies
  on.
- No explicit assumption beyond these; no batch acceptance order.

## Findings

- **F1 (suggested).** Location: "asks whether, for integers
  $3\le d_1<\cdots<d_r$ with $\sum_i1/(d_i-1)\ge1$". Defect: the linked
  page types the condition as $\sum_{1\le i\le r}1/(d_r-1)\ge1$, which no
  admissible $d_1<\cdots<d_r$ satisfies (witness: $d_r\ge r+2$, so the sum
  is $r/(d_r-1)\le r/(r+1)<1$); the section uses the source's (1.12)
  without saying that it departs from the page. Replacement: after the
  condition add "(the source's (1.12); the problem page types the
  denominator as $d_r-1$, a condition no admissible tuple meets)", and
  flag the page's statement to its owner for a check against the catalog
  entry, which this review could not consult.
- **F2 (note).** Location: "and the same with $P(d_i,k)$ when the $d_i$
  are coprime". Defect: the page's hypothesis is $\gcd(d_1,\ldots,d_r)=1$,
  which "coprime" can be read as pairwise coprimality, and the page's "for
  any $k\ge1$" is absent. Witness: the page's second question paragraph.
  Replacement: "and, when $\gcd(d_1,\ldots,d_r)=1$, the same with
  $P(d_i,k)$ for every $k\ge1$".
- **F3 (required).** Location: "the Fan card records Theorem 1.5 at
  statement level: $\bigcup_{d\in D}\{d^n\}$ is strongly complete when
  $D=D_1\cup D_2\cup C$ with $\gcd(C)=1$ and $\sum_{d\in D_i}1/(d-1)\ge1$
  for $i=1,2$". Defect: the card carries no statement of Theorem 1.5 (its
  only mention is "Theorem 1.5, mixed power sets; all at statement level
  only here"), so the content is the section author's own reading of the
  source; and the content omits three hypotheses of the theorem as printed
  on p. 7 of v5: $D$ is a nonempty finite subset of $\mathbb N_{\ge2}$
  with no two elements being powers of the same integer, and the three
  parts are nonempty. Section 7 uses finiteness (the bound on
  $b-\sum_{b'<b}b'$) and the no-common-power condition (to make
  $\mathcal B_1,\mathcal B_2,\mathcal C$ a partition). Witness: the page
  image of p. 7 and the card's Overview paragraph. Replacement: "the Fan
  card records Theorem 1.5 (v5, p. 7) at statement level only; the theorem
  says that for a nonempty finite $D\subseteq\mathbb N_{\ge2}$ with no two
  elements powers of the same integer, $\bigcup_{d\in D}\{d^n\}$ is
  strongly complete whenever $D=D_1\cup D_2\cup C$ is a partition into
  nonempty parts with $\gcd(C)=1$ and $\sum_{d\in D_i}1/(d-1)\ge1$ for
  $i=1,2$". The consequence for the section is confined to this sentence:
  nothing is deduced from the theorem.
- **F4 (suggested).** Location: "The only shared step is elementary: the
  bounded-$\Delta$ argument that makes subset sums syndetic". Defect: a
  second step of the same kind is shared, the verification of Fan's
  condition (1.5): Section 7 proves $H_1(\mathcal C)=\{0\}$ from
  $r_{n+1}(c)=c\,r_n(c)$ and $\gcd(C)=1$, and Step 3 of the Remark 4.2
  page proves (1.5) for $A_{\alpha,\beta}$ from $c_{k+1}=2c_k+1$
  infinitely often; the arguments differ as much as the two
  bounded-$\Delta$ arguments do. Witness: p. 34 of v5 and the Remark 4.2
  page's Step 3. Replacement: "The shared steps are elementary: the
  bounded-$\Delta$ argument that makes subset sums syndetic, which is
  Fan's Lemma 2.1 and, for two rays, item 6 of the normalization page, and
  the verification of condition (1.5), which the Remark 4.2 page does for
  two rays and Section 7 does for $P_k(C)$ by a different argument; both
  are resemblances of tools, not transfers of results."
- **F5 (note).** Location: "one component fewer than Bergelson--Simmons".
  Defect: none in substance; the comparison is relayed from p. 7 of the
  source, and the Bergelson--Simmons paper is not held, so the section
  should say whose statement of that theorem it compares. Replacement:
  "one component fewer than the Bergelson--Simmons theorem as the source
  states it (p. 7; that paper is not held)".

Unverified, not findings: S2's "with progress not compiled" and S4 (the
folder index's wording) concern text outside the allowed reading.

## Verdict

- S1: refutation-failed. The described problem is the intended one and the
  source's; the section departs silently from the page's defective typed
  condition (F1, F2).
- S2: refutation-failed for "status open" (frontmatter); the clause
  "progress not compiled" was not examined.
- S3: refuted-as-stated. The card does not record the statement, and the
  statement is not Theorem 1.5: three hypotheses are missing (F3). The
  weakened mathematical statement itself is unresolved here.
- S4: no verdict; the sentence describes excluded content and was not
  examined.
- S5: refutation-failed. The obstruction holds, and holds for two-ray
  subsets as well, by the derivation under Strongest attack.
- S6: refutation-failed.
- S7: refutation-failed for its operative content (a resemblance of tools,
  not a transfer); the word "only" does not survive (F4).
- S8: refutation-failed.
- S9: refutation-failed; the reconstruction would also consume Lemma 3.1.
- S10: refutation-failed.

Limitations: the catalog entry for Problem 124 and the Bergelson--Simmons
paper were not consulted, so F1 cannot say whether the typed condition is
the catalog's or the page's; the folder index and the problem page's
Progress section were excluded; Fan's proofs, including Section 7, were
read for their dependencies and not reviewed; the derivation under
Strongest attack is the reviewer's own and is author-recorded like the
section.

This focused review assigns no tier and changes no status.
