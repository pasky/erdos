---
name: research/erdos_354/evidence/verify/connections_no_further_consumer_review
title: "Independent review of the connections section: No further consumer"
desc: |
  Focused refutation review of the section "No further consumer" of the
  Problem 354 connections page. The descent's stated interface, the corpus
  inventory and the exclusion of two-ray sets and single rays from Problem
  347 survive (refutation-failed); the exclusion of two-ray sets from
  Problem 346 rests on a reason that does not bear on that problem's
  hypotheses (proof defective; statement unresolved). One required
  correction, one suggested correction, three notes.
created: 2026-09-28T18:33:44Z
updated: 2026-09-28T20:40:46Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, given only the
commissioning assignment. The reviewer took no part in writing the
connections page, the reconstruction pages, the lead pages or any filed
review or grade of this folder, and opened none of the folder's filed
reviews or grades.

**Subject.** The section "No further consumer" of
[[research/erdos_354/connections|the Problem 354 connections page]],
`wiki/research/erdos_354/connections.md` as it stood at 2026-09-28T13:50:48Z,
lines 611--652: the H2 heading at line 611 through the last line of the file.
The section holds no proof displays. Its content is one interface summary of the
descent, one recognition rule, one inventory of ten catalog problems with
descriptors, one obstruction sentence carrying two mathematical reasons, two
corpus-coverage sentences and an outcome line.

**Lead pages.** The section's "two leads named above" are
[[research/leads/rational_ratio_dyadic_floor_descent/_index|rational_ratio_dyadic_floor_descent]]
and
small_base_two_ray_distance_divergence,
both read in full as of the same time.

**Reading and depth.** All as of 2026-09-28T13:50:48Z. The section in full. The
page's preamble (lines 20--57: purpose and standing, the definition of
$A_{\alpha,\beta}$, complete and strongly complete sets, the normalized
pair and its weights, conversions, events, prefix sums, moduli and the run
invariant) as shared input. Reconstruction pages as premises: the
[[research/erdos_354/yu_chen_theorem_5_1_reconstruction|Theorem 5.1 page]],
the
[[research/erdos_354/yu_chen_normalization_reconstruction|normalization page]]
and the
[[research/erdos_354/yu_chen_theorem_reconstruction|theorem page]] in full;
the definitions and statements of the
[[research/erdos_354/yu_chen_lemma_2_1_reconstruction|erosion]],
[[research/erdos_354/yu_chen_lemma_2_2_reconstruction|mesh]] and
[[research/erdos_354/yu_chen_lemma_2_3_reconstruction|projection]] lemma
pages; the statements only of the Remark 4.1, Remark 4.2, Theorem 9,
Corollary 12 and (BG) pages. Problem pages, statement paragraphs only:
[[problems/additive_bases/E0343/_index|343]], [[problems/additive_bases/E0344/_index|344]],
[[problems/additive_bases/E0345/_index|345]], [[problems/additive_bases/E0346/_index|346]],
[[problems/additive_bases/E0347/_index|347]], [[problems/additive_bases/E0351/_index|351]],
[[problems/integer_sequences/E0253/_index|253]],
[[problems/diophantine_problems/E0246/_index|246]],
[[problems/diophantine_problems/E0123/_index|123]],
[[problems/diophantine_problems/E0125/_index|125]], and, as the targets the section
refers to, [[problems/additive_bases/E0354/_index|354]] (statement and its
formulation paragraph), [[problems/additive_bases/E0349/_index|349]],
[[problems/additive_bases/E0348/_index|348]], [[problems/integer_sequences/E0254/_index|254]]
and [[problems/diophantine_problems/E0124/_index|124]]. Guidance: the "Whole-claim
report", "Audit checklist" and "Grading and claim standing" sections of
`docs/verification.md`, `docs/approach_vetting.md` in full, the "Source
fidelity" section of `docs/evidence.md` and `docs/math_authoring.md` in
full. No library PDF was opened: the section invokes no source theorem
directly; its only imported mathematics is the reconstruction pages, which
the assignment makes premises.

**Exposures.** Five, none used in a verdict. (1) The status line of the
Problem 347 page ("Proved (Lean)") was displayed while the statement
paragraph was located; the other fourteen problem pages were cut before
their status lines. (2) The two lead pages, which are allowed reading,
paraphrase the Problem 354 page's Current assessment in their "Target and
status evidence" sections. (3) The H2 headings and the one-line "Outcome"
sentences of the page's other six sections were seen while locating the
targets and leads the section refers to; no other line of those sections
was read, and none of their reviews was opened. (4) A file-name listing of
`wiki/theory/` and `wiki/research/` (paths only, no content) was taken
to check the coverage sentence S7. (5) The listing of the folder's
`evidence/verify/` directory shows that reviews of the other sections
exist; none was opened. The reviewer also ran a short exact-integer
computation for the attack on S5; its derivation is retained below and no
run log is kept.

## Restatement

Conventions carried from the page: for $\alpha,\beta>0$, $A_{\alpha,\beta}$
is the set of nonzero floors $\lfloor2^n\alpha\rfloor$,
$\lfloor2^n\beta\rfloor$, $n\ge0$; a *normalized pair* has
$N=\lfloor\beta\rfloor<M=\lfloor\alpha\rfloor<2N$, $N\ge2$, weights
$a_i=\lfloor2^i\alpha\rfloor$, $b_i=\lfloor2^i\beta\rfloor$, conversions
$u_i=a_{i+1}-2a_i$, $v_i=b_{i+1}-2b_i$, prefix sums $P_n$ (subset sums of
the $2n$ weights of indices below $n$), $D_n=\gcd(a_n,b_n)$ and
$h_n=h(P_n\bmod D_n)$, the longest run of missing residues. A set is
complete if every sufficiently large integer is a sum of distinct
elements, strongly complete if it stays complete after every finite
deletion.

- **S1** (interface of the descent). The folder's reusable mechanism is
  the Theorem 5.1 descent: for a normalized pair, if at layer $n$ the
  weights are $a_n=dp$, $b_n=dq$ with $d=D_n$, $\gcd(p,q)=1$, the
  conversions at indices $n,\ldots,n+\ell-2$ vanish, the conversion at
  index $n+\ell-1$ is nonzero, and $K=2^\ell\ge K_*(p,q)$ with
  $K_*(p,q)=2q(p-1)+4(p+q)+64$, then $h_t\le\max(0,h_n-1)$ for every
  $t\ge n+\ell+3$ and every choice of later conversions; the connection
  of the mesh nodes is a finite certificate valid for all $q<p<2q$; the
  inputs are the interlacing $b_i<a_i<2b_i\le b_{i+1}$, the base-2 digit
  recurrence $u_i,v_i\in\{0,1\}$, and the reduced ratio at the block's
  first layer.
- **S2** (recognition rule). A consumer of the descent is a set equal, up
  to finitely many elements, to a union of two rays $\lfloor2^n\alpha\rfloor$,
  $\lfloor2^n\beta\rfloor$, or a question about subset sums of such a set.
- **S3** (inventory). Beyond the targets of the earlier sections (354,
  349, 348, 254, 124), the corpus problems on complete sequences, subset
  sums of distinct terms, floors of geometric sequences and dyadic
  intervals are 343 and 344 (subcompleteness under a density condition),
  345 (thresholds of completeness of the powers $n^k$, open), 346
  (strongly complete sequences that lose completeness under every
  infinite deletion), 347 (a sequence with ratio tending to $2$ whose
  cofinite subsequences have subset sums of density $1$), 351 (strong
  completeness of $p(n)+1/n$), 253, 246 and 123 (sums of distinct
  $a^kb^l$ and $a^kb^lc^m$) and 125; all but 345 are resolved.
- **S4** (two-ray sets and Problem 347). No two-ray set with ratio not a
  power of $2$ is an example for Problem 347, because the consecutive
  ratios of its sorted terms alternate near $\alpha/\beta$ and
  $2\beta/\alpha$ (normalized values) and so do not tend to $2$.
- **S5** (two-ray sets and Problem 346). No two-ray set is an example for
  Problem 346, for the same reason.
- **S6** (single rays). A single ray $\lfloor2^n\alpha\rfloor$ has ratios
  tending to $2$ and at most $2^n$ subset sums below
  $a_n\ge\lfloor\alpha\rfloor2^n$; together with the resolution of both
  problems this excludes single rays from Problems 346 and 347.
- **S7** (coverage). The theory tree holds no claim on complete
  sequences, and no research lead other than the folder's two concerns
  them.
- **S8** (outcome). No second consumer exists, so no method page is made;
  the two leads are the folder's only routes.

## Checklist

- **Quantifiers and scope.** One failure and one gap. S5 quantifies over
  all two-ray sets while its reason bears only on the conclusion of
  Problem 346, not on its hypotheses (F1). S6's displayed bound proves the
  intended density statement only when $\lfloor\alpha\rfloor\ge2$ (F2). In
  S1, "every later layer" means every $t\ge n+\ell+3$, the bound is
  relative to $h_n$, and no layer-to-layer monotonicity is asserted (F4).
  S4 is correctly quantified: the normalization removes finitely many
  elements and finitely many coincident values, neither of which changes
  the limit points of the ratio sequence.
- **Circularity.** None. The section derives nothing from its own
  conclusion; the descent is consumed only through the Theorem 5.1 page.
- **Model and convention changes.** Checked; no unproved transfer. Problem
  346 asks for a strictly increasing set and Problem 347 for a
  nondecreasing sequence; a normalized pair has pairwise distinct values
  (item 4 of the normalization page), and the finitely many
  pre-normalization coincidences contribute finitely many ratios equal to
  $1$. "Complete" in Problem 346 is defined in its statement exactly as on
  the page. The ratios "near $\alpha/\beta$ and $2\beta/\alpha$" are those
  of the normalized coefficients, as the page's notation paragraph makes
  standing; for an unnormalized pair they are the normalized ratio
  $\theta\in(1,2)$ and $2/\theta$.
- **Finite and statistical overreach.** None in the section. The
  reviewer's witness below uses an exact finite check only as the base of
  an induction whose step is proved by an explicit inequality.
- **Uniformity.** Pass. The dependence of the descent constant on the
  reduced ratio is displayed as $K_*(p,q)$; the certificate lemma of the
  Theorem 5.1 page is stated for all integers $q<p<2q$, all twelve
  templates and all four third-digit pairs, so "uniform" is warranted.
- **Extremal conclusions.** Inapplicable; the section states no infimum,
  supremum or sharpness. The count bound of S6 was checked in its own
  units (number of subset sums against $a_n$).
- **Consequences and composition.** "None consumes the descent" composes
  the descriptors of S3 with the obstructions S4--S6. The 347 link and the
  single-ray link hold (S4, S6 with F2); the 346 link is defective (F1)
  and, if Problem 346 is resolved in the negative, the composition still
  holds because a resolved problem needs no consumer; that dependence on
  the resolution is not visible in the sentence. "So no method page is
  made" is a convention consequence outside the read set.
- **Computation.** Inapplicable to the section, which runs nothing. The
  reviewer's computation is exact integer arithmetic (integer square
  roots and a bitset of subset sums) and is retained as a derivation.
- **Reproduction.** Inapplicable; the section states no rerun command or
  coverage claim.
- **Source and verdict fidelity.** The ten descriptors agree with the
  statement paragraphs of the problem pages (Problem 351's set is
  recorded there as $\{p(n)+1/n\}$, as the section writes). The interface
  summary agrees with the Theorem 5.1 page up to F4. The status words
  ("proved", "solved", "disproved", "open") are outside the read set and
  were not checked. The section claims author-recorded standing only, as
  the page's preamble states.

## Weakest steps

**W1: the ratio pattern (S4, S5).** Item 4 of the normalization page gives
$b_i<a_i<2b_i\le b_{i+1}$, so the merged sorted list of a normalized pair
is $b_0<a_0<b_1<a_1<\cdots$ and its consecutive ratios are $a_i/b_i$ and
$b_{i+1}/a_i$. Since the floor error is below $1$, $2^{-i}a_i\to\alpha$
and $2^{-i}b_i\to\beta$, hence $a_i/b_i\to\theta=\alpha/\beta\in(1,2)$ and
$b_{i+1}/a_i\to2/\theta\in(1,2)$. The set of limit points of the ratio
sequence is $\{\theta,2/\theta\}$; it never contains $2$, and it is a
single point exactly when $\theta=\sqrt2$, in which case the ratio
converges to $\sqrt2$. For Problem 347, whose sequence must satisfy
$\lim a_{n+1}/a_n=2$, this excludes every pair whose ratio is not a power
of $2$: normalization multiplies each coefficient by a power of $2$, which
replaces each ray by a tail, so the unnormalized set differs by finitely
many elements and finitely many coincident values, and neither affects the
limit points. This is S4. For Problem 346 the hypotheses are (i) $A\setminus B$
complete for every finite $B$, (ii) $A\setminus B$ not complete for every
infinite $B$, (iii) $a_{n+1}/a_n\ge1+\varepsilon$ for all $n$, and the
question is whether the ratio tends to the golden ratio. The pattern shows
that (iii) holds (every ratio exceeds $1$ and both limit points exceed
$1$, so the infimum over $n$ is above $1$) and that the questioned
conclusion fails; it says nothing about (ii). So the pattern does not
establish S5; see the attack below.

**W2: the single-ray count (S6).** For a ray with coefficient $\alpha>0$,
the elements below $a_n=\lfloor2^n\alpha\rfloor$ are among
$a_0,\ldots,a_{n-1}$ (the sequence is nondecreasing), so the subset sums
below $a_n$ number at most $2^n$, and $a_n\ge\lfloor\alpha\rfloor2^n$
because $\lfloor\alpha\rfloor2^n$ is an integer not exceeding $2^n\alpha$.
Both displayed facts are correct. The lower density of the subset sums is
therefore at most $1/\lfloor\alpha\rfloor$, which is below $1$ exactly
when $\alpha\ge2$. The sharper bound $a_n>2^n\alpha-1$ gives lower density
at most $1/\alpha$, below $1$ whenever $\alpha>1$. Discarding the zero
terms puts the coefficient in $[1,2)$; the coefficient $1$ gives the
powers of $2$, whose cofinite subsequences obtained by deleting $r\ge1$
elements have subset sums of density $2^{-r}$ (the integers with zero
binary digits at the deleted positions). Hence no single ray is an example
for Problem 347, and no single ray is strongly complete as Problem 346
requires: for a coefficient in $(1,2)$ infinitely many integers are
unrepresented, and for the powers of $2$ one deletion leaves infinitely
many unrepresented. The conclusion of S6 holds for every ray; the
displayed inequality proves it only for $\lfloor\alpha\rfloor\ge2$.

**W3: the interface (S1).** The Theorem 5.1 page's hypotheses of Section 3
are exactly the layer data $a_n=dp$, $b_n=dq$, $\gcd(p,q)=1$, the zero
conversions at $n,\ldots,n+\ell-2$, the nonzero conversion at $n+\ell-1$,
and $K=2^\ell\ge K_*$. Its proof uses, beyond the certificate table and
the three finite lemmas: the interlacing $q<p<2q$ at layer $n$; the digit
bounds $u_i,v_i\in\{0,1\}$ (for the constant part at most $22$ and for
$b_r\le8dKq+15$); the prefix bound $S_n<L_n=d(p+q)$, which the
normalization page derives from the recurrence and positive initial
terms; $0\in P_n$ (so $k\le d$); and the doubling bound on all later
weights in sorted order, which is the interlacing at every later layer.
Each of these is an instance of "the interlacing" or "the digit
recurrence" of a normalized pair, so S1 names the inputs at their actual
strength. The conclusion is $h_t\le\max(0,h_n-1)$ for $t\ge n+\ell+3$,
uniform in the later conversions; the page's Scope note disclaims
monotonicity. S1's "every later layer" compresses this (F4) but changes
no quantifier that the folder relies on.

## Strongest attack

**S1.** Sought a hypothesis of the descent absent from S1's list, by
listing every fact the Theorem 5.1 proof consumes (W3). All reduce to the
interlacing and the digit recurrence of a normalized pair plus the finite
certificate, which S1 names. Sought a strengthened quantifier: S1 does not
claim monotone descent, and its "every later layer" reads as the
permanent bound once the offset three is supplied. The attack failed.

**S3.** Compared each descriptor with the statement paragraph of its
problem page. Problem 343's density condition is $\gg N$, Problem 344's
is $\gg N^{1/2}$, both asking for subcompleteness; Problem 345 compares
thresholds of completeness of consecutive powers $n^k$; Problem 346 and
347 are as restated in W1; Problem 351 is recorded as strong completeness
of $\{p(n)+1/n\}$; Problems 246 and 123 are sums of distinct $a^kb^l$ and
$a^kb^lc^m$; Problem 125 concerns the lower density of a sum of two
digit-restricted sets; Problem 253 is an implication for sequences with
ratio tending to $1$. Every descriptor is faithful. The status words are
outside the read set. The attack failed on what could be read.

**S4.** Sought a two-ray set whose sorted ratios tend to $2$. By W1 the
limit points are $\theta$ and $2/\theta$, both in $(1,2)$; a pair whose
ratio is a power of $2$ is a single ray as a set, and as a multiset its
doubled values give ratios $1$ and about $2$ in alternation, so it has no
limit either. The attack failed.

**S5.** The attack succeeded against the argument and left the statement
unresolved. The reason offered, the ratio pattern, concerns the
conclusion of Problem 346 and not its hypothesis (ii). A witness that
(ii), not the pattern, decides membership: the normalized pair
$\alpha=3\sqrt2$, $\beta=3$ ($N=3<M=4<6$, ratio $\sqrt2$ irrational), whose
sorted ratios converge to $\sqrt2$, so a fragile such set would have been
a counterexample to the questioned implication rather than a non-example.
Its weights are $a_n=\lfloor2^n\cdot3\sqrt2\rfloor$, the integer square
root of $18\cdot4^n$, and $b_n=3\cdot2^n$: the weights of indices below
$3$ are $3,4,6,8,12,16$, and $a_3=33$ (since $33^2=1089\le1152<1156=34^2$),
$b_3=24$. An exact enumeration shows that the subset sums of
$\{3,4,6,8,12,16\}$ contain every integer of $[6,43]$ (and not $5$ or
$44$). Delete the infinite set $B=\{b_m:m\ge4,\ 4\mid m\}=\{48,768,\ldots\}$
and add the retained weights of indices $\ge3$ in increasing order to
$W_0=[6,43]$, whose span is $37$. The mesh lemma with $k=1$ keeps a full
interval and adds the weight to the span whenever the weight is at most
the current span. Let $s_m$ be the span before the weights of index $m$
are added; then $s_m\ge37+\sum_{i=3}^{m-1}a_i+\sum b_i$, the second sum
over retained $3\le i<m$. Since $a_{i+1}\ge2a_i$,
$\sum_{i=3}^{m-1}a_i\ge33(2^{m-3}-1)$, while
$a_m\le33\cdot2^{m-3}+2^{m-3}-1$ because $a_{i+1}\le2a_i+1$, and
$b_m=24\cdot2^{m-3}$. Hence $s_m\ge b_m$ for every $m\ge3$, and
$s_m-a_m\ge5-2^{m-3}+\sum b_i$ over retained $3\le i<m$; one of $m-1,m-2$
is retained for $m\ge4$, contributing at least $3\cdot2^{m-2}>2^{m-3}$
for $m\ge5$ and $24>2$ for $m=4$, and $s_3=37\ge33=a_3$. So every integer
$\ge6$ is a sum of distinct elements of $A_{3\sqrt2,3}\setminus B$: the
pair violates (ii) and is not an example for Problem 346, by an argument
unrelated to its ratios. The same construction applies to any pair for
which some $P_r$ contains a full interval longer than $a_r$, but the
section proves nothing of the kind for all pairs, and the descent yields
strong completeness, not the deletion structure, so the general statement
S5 stays unresolved within the read set. If Problem 346 was resolved by
proving the implication, S5 follows from that theorem and W1; the section
does not say so.

**S6.** Sought a coefficient for which the displayed bound is vacuous:
$\alpha=3/2$ has $a_n=3\cdot2^{n-1}$ for $n\ge1$, $\lfloor\alpha\rfloor=1$,
and the bound reads $a_n\ge2^n$, giving density at most $1$; the sharper
bound gives at most $2/3$ (F2). The conclusion survives for every ray by
W2; the attack succeeded only against the displayed inequality's
sufficiency.

**S7.** Scanned the file names of the theory tree (claims L1 to L22 on
covering systems, additive bases, powerful complements, unit distances,
extremal graphs, roots of unity, totients, dissociated sets and rainbow
cycles) and of the research leads; none names complete sequences other
than the folder's two leads, which are filed under `research/leads/`,
outside the folder's directory (F5). A page could concern complete
sequences under another name; the read set does not allow opening them.
The attack found nothing.

**S8.** Consistent with the outcome lines of the other sections (one
transfer and one conditional transfer, each recorded as a lead, three
failures, and one transfer to Problem 254); whether the Problem 254
transfer is a "route" in the section's sense could not be checked
without reading that section. No refutation.

## Premises

- [[research/erdos_354/yu_chen_theorem_5_1_reconstruction|Theorem 5.1 page]]:
  hypotheses of Section 3, statement $h_t\le\max(0,h_n-1)$ for
  $t\ge n+\ell+3$, the certificate lemma, the length condition (5.2) and
  the Scope note; read in full. Independently reviewed as of
  2026-09-28T05:03:27Z with corrections applied since; treated as established at
  that standing.
- [[research/erdos_354/yu_chen_normalization_reconstruction|Normalization page]]:
  items 1--6 and the reduction; used for the interlacing, the distinct
  values, the digit bounds, the prefix bound $S_n<L_n$ and the fact that
  normalization takes tails; read in full; same standing.
- [[research/erdos_354/yu_chen_theorem_reconstruction|Theorem page]]:
  strong completeness of $A_{\alpha,\beta}$ for irrational ratio, used
  only to note that a two-ray set with irrational ratio meets hypothesis
  (i) of Problem 346; read in full; same standing.
- [[research/erdos_354/yu_chen_lemma_2_2_reconstruction|Mesh lemma page]]:
  Lemma 2.2 and its consequence, used in the S5 witness; definitions and
  statement read; same standing. The erosion and projection lemma pages
  were read for definitions only.
- Statements of the Remark 4.1, Remark 4.2, Theorem 9, Corollary 12 and
  (BG) pages, read to assess F3; not otherwise used.
- The two lead pages: author-recorded and unreviewed by their own
  "Current review" sections; used only to identify the leads and the
  mechanisms the page reused (F3).
- Problem statements as listed under Reading; no external source and no
  PDF.
- No batch acceptance order applies; the review is focused and stands
  alone.

## Findings

- **F1 (required).** Location, lines 641--643: "the two-ray sets are not
  examples for Problem 346 or 347, since their sorted terms have ratios
  alternating near $\alpha/\beta$ and $2\beta/\alpha$". Defect: for
  Problem 346 the ratio pattern bears on the questioned conclusion (a
  ratio tending to the golden ratio), not on the hypotheses (strong
  completeness, loss of completeness under every infinite deletion,
  ratios bounded away from $1$). A two-ray set with irrational ratio
  meets the first and third by the folder's theorem and the pattern
  itself, so the pattern cannot exclude it; had such a set been fragile
  under every infinite deletion it would have been a counterexample. The
  obstruction therefore does not block what it claims for Problem 346.
  Witness: the pair $(3\sqrt2,3)$ of the attack on S5, whose ratios
  converge to $\sqrt2$ and which fails the deletion hypothesis by an
  explicit infinite deletion. Proposed replacement: "the two-ray sets are
  not examples for Problem 347, whose sequence must have ratio tending to
  $2$, since their sorted terms have ratios with limit points $\alpha/\beta$
  and $2\beta/\alpha$; Problem 346 asks about sequences that lose
  completeness under every infinite deletion, a property the descent does
  not address, and a two-ray set with that property would be a
  counterexample rather than an example, so nothing is transferred either
  way and the problem is resolved". If Problem 346 was resolved by
  proving its implication, write instead that the exclusion follows from
  that theorem because the ratios of a two-ray set do not tend to the
  golden ratio.
- **F2 (suggested).** Location, lines 644--645: "a single ray, whose
  ratios tend to $2$, has at most $2^n$ subset sums below
  $a_n\ge\lfloor\alpha\rfloor2^n$". Defect: the displayed bound gives a
  subset-sum density below $1$ only when $\lfloor\alpha\rfloor\ge2$; for
  a coefficient in $(0,2)$ it is vacuous. Witness: $\alpha=3/2$ (W2, S6
  attack). Proposed replacement: "has at most $2^n$ subset sums below
  $a_n>2^n\alpha-1$, so once its zero terms are discarded, which puts
  $\alpha$ in $[1,2)$, its subset sums have lower density at most
  $1/\alpha<1$ unless $\alpha=1$, when the ray is the powers of $2$ and
  deleting $r\ge1$ elements leaves subset sums of density $2^{-r}$".
- **F3 (note).** Location, line 613: "The reusable content of the folder
  is a descent". The folder also reconstructs the all-even floor
  mechanism at Pisot and Salem bases (the Theorem 9 and Corollary 12
  pages) and the one-per-dyadic-interval example (the Remark 4.1 page),
  and the lead pages record that this page reused both (Proposition
  354.7; the transfer to Problem 254). The recognition rule of the next
  sentence is tailored to the descent, while the search terms ("floors of
  geometric sequences", "dyadic intervals") do cover the other
  mechanisms, so the inventory is not narrowed. Suggested wording: "The
  reusable content of the folder not consumed above is a descent".
- **F4 (note).** Location, lines 614--615: "lowers the modular run
  invariant of every later layer". Precisely, $h_t\le\max(0,h_n-1)$ for
  every $t\ge n+\ell+3$, relative to the invariant at the block's first
  layer; the layers $n+1,\ldots,n+\ell+2$ are not covered and no
  monotonicity from layer to layer is asserted. Suggested wording: "of
  every layer from three past the block".
- **F5 (note).** Location, lines 648--649: "no research lead outside this
  folder concerns them". The two leads are filed under `research/leads/`,
  outside `research/erdos_354/`; the sentence is true only in the reading
  "no lead other than the two named above". Suggested wording to that
  effect. The check was by file names only.

## Verdict

- S1: refutation-failed. The interface names the descent's inputs at
  their actual strength; F4 is a wording note.
- S2: not a claim; a recognition heuristic.
- S3: refutation-failed for the content descriptors, each faithful to
  its statement paragraph; the status words were not checkable within
  the read set.
- S4: refutation-failed. The limit points of the sorted ratios are the
  normalized ratio and its complement to $2$, never $2$.
- S5: proof defective; statement unresolved. The ratio pattern does not
  bear on the deletion hypothesis of Problem 346; the witness pair shows
  membership is decided by that hypothesis, and the general statement is
  not established by the section (F1).
- S6: refutation-failed for the displayed bound; the exclusion it is
  meant to carry holds for every ray by the sharper bound, which the
  section should state (F2).
- S7: refutation-failed on a names-only check, with the wording note F5.
- S8: not a claim; an outcome record consistent with what was read.

Limitations: the status words of the ten inventoried problems, the
direction in which Problem 346 was resolved, the convention that a method
page needs two consumers, and the content of the other sections of the
page were outside the read set; the coverage sentence S7 was checked by
file names only; the S5 witness settles one pair and any pair with a
finite full-interval certificate, not the general statement. No tier is
warranted or withheld by this review; every statement of the section
remains author-recorded. This focused review assigns no tier and changes
no status.
