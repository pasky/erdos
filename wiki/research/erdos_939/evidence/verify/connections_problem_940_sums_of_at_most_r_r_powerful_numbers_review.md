---
name: research/erdos_939/evidence/verify/connections_problem_940_sums_of_at_most_r_r_powerful_numbers_review
title: "Independent review of the connections section: Problem 940: sums of at most r r-powerful numbers"
desc: |
  Refutation review of the Problem 940 section of the connections page as it
  stood on 2026-09-28T13:50:48Z. Verdicts: refutation-failed for the seven
  checked statements S1 to S7; the closing "no route exists" sentence S8 is
  an assessment, not a claim. Required corrections: none; one suggested
  rewording and four notes.
created: 2026-09-28T18:52:03Z
updated: 2026-09-28T18:52:03Z
---

***

## Subject and independence

This report was written by an independent reviewer in a fresh context, given
only the assignment. The reviewer took no part in writing the connections
page, the reconstruction page or any lead folder, had read none of them
before the assignment, and received no review, grade or standing text about
them. The charge is refutation of author-recorded mathematics; the review
assigns no tier.

- Date: 2026-09-28T13:50:48Z, the source as it stood then (called "the
  commit" below).
- Page: `wiki/research/erdos_939/connections.md`,
  [[research/erdos_939/connections|the connections page]], section
  "## Problem 940: sums of at most r r-powerful numbers", lines 427 to 465
  (the H2 at line 427; the next H2 at line 466).
- Lead pages: none. The page's "Leads created" section states that the
  Problem 940 comparison is recorded on the page and needs no folder.
- Read in full: the section; the page's preamble and Conventions (lines 1 to
  57); the page's Shared results (lines 58 to 302) as interfaces, of which
  the section consumes only Corollary 1.1 (lines 123 to 146), whose proof
  another reviewer checks and which is used here through its statement
  alone; the page's "Leads created" and "Sources read for this page"
  sections (lines 561 to 590), read to identify lead pages; the
  reconstruction page
  [[research/erdos_939/theorem_1_reconstruction|Theorem 1 reconstruction]],
  as a premise at its reviewed standing; the statement block of
  [[problems/diophantine_problems/E0940/_index|Problem 940]] (lines 1 to 47 of its
  page, the material before its Current assessment heading); the theorem
  statement of
  [[research/erdos_940/powerful_subsum_counts|the shifted-target page]]
  (lines 39 to 56) and the rank theorem with its counting consequences on
  [[research/erdos_940/linear_collision_families|the rank page]] (lines 23
  to 49 and 98 to 157), as interfaces; `docs/verification.md` sections
  "Grading and claim standing", both "Audit checklist" headings and the
  Erdos-specific "Whole-claim report"; `docs/approach_vetting.md`;
  `docs/evidence.md` "Source fidelity"; `docs/math_authoring.md`.
- Not read: the folder's `_index.md`; anything under any `evidence/` folder,
  including the existing reconstruction review and grade in the target
  directory; the Current assessment, Known Results, Research and Linked
  library material sections of the Problem 940 page; the claim cards L18 and
  L19; the library; no web search. The section invokes no source theorem
  directly, so no PDF was consulted.
- Exposures: five, none of them review, grade, Current assessment or Known
  results text, and none changed a verdict. (1) A search for the
  $\mathcal P_r$ convention on the shifted-target page returned lines 22 to
  28 and 33 to 35 of that page's "Status and scope" section: the definition
  of $\mathcal P_r$ as the positive $r$-powerful integers, and a display of
  canonical-core bounds. (2) A search for the collision convention on the
  rank page returned lines 19 to 21 of its "Status and scope" section: a
  scope sentence saying the results do not bound all collisions, prove
  positive density, or produce missing integers for $r\ge5$. (3) The
  Problem 940 statement block carries the frontmatter `status: open` and a
  Formalization paragraph recording L18 and L19 at tier 0. (4) The
  reconstruction page's Boundary paragraph "Relation to Problem 940"
  characterizes L18 and L19 and their summand convention. (5) The
  reconstruction page's Source and Standing paragraphs were read as part of
  the full read of that page.

## Restatement

Conventions: $r$-powerful means $p^r\mid n$ for every prime $p\mid n$, so $1$
qualifies vacuously; $\mathcal P_r$ is the set of positive $r$-powerful
integers; "the construction" is the Theorem 1 identity evaluated at the
integer parameters that Corollary 1.1 describes.

- S1 (target). For each integer $r\ge3$: (a) are there infinitely many
  integers that are not a sum of at most $r$ $r$-powerful numbers; (b) does
  the set of integers that are such sums have density $0$.
- S2 (status record). The problem page records question (a) as proved in
  the repository's Lean for $r=3$ and $r=4$ (claims
  L18
  and
  L19,
  tier 0) and open for $r\ge5$, and question (b) as open for every $r$.
- S3 (transfer failure). For every $r\ge6$ and every $N=(m^r+B^r)^r$ that
  Corollary 1.1 produces ($B$ a positive multiple of $B_0$, $m>B$ coprime to
  $B$), $N$ is an $r$-th power, hence $r$-powerful, hence a sum of at most
  $r$ $r$-powerful numbers with one summand; the identity supplies a second
  representation of $N$ as a sum of $r-2$ $r$-powerful numbers; $N$ is never
  in the complement of the representable set.
- S4 (no consequence). Nothing follows for the complement or for the density
  of the representable set; the produced $N$ number $O(X^{1/r})$ below $X$,
  against the linear mass a density statement concerns.
- S5 (L18 and L19). Theorem 1 neither uses nor informs L18 and L19, as the
  reconstruction page records, and their convention that $0$ and $1$ are
  $r$-powerful summands does not interact with the positive summands of the
  construction.
- S6 (first comparison). The shifted-target theorem of the Problem 940
  folder, at shift $h=0$: for fixed $r\ge3$, $k\ge2$ and $\varepsilon>0$, the
  number of ordered $k$-tuples in $\mathcal P_r^k$ with sum at most $X$ and
  $r$-powerful sum is $O_{r,k,\varepsilon}(X^{k/r-\delta_r+\varepsilon})$
  with $\delta_r=(r-1)/(r^2(2r+1))$; Corollary 1.1 gives, for $k=r-2$ and
  $r\ge6$, the lower bound $X^{2/r^2-o(1)}$ for the same count; at $r=6$ the
  exponents are $0.0556$ and $0.6560$; the two bounds are consistent, far
  apart, and neither is threatened.
- S7 (second comparison). The rank theorem of the Problem 940 folder
  concerns relations $\sum_ia_iL_i^r=\sum_jb_jM_j^r$ among $r$-th powers of
  rational linear forms with positive rational coefficients and shows that a
  fixed finite list of such identities cannot supply collisions of linear
  mass; the binomial identity is not of that shape, its terms being
  multiples of $r$-th powers of monomials in $U$, $V$ and the $r$-th powers
  of $U^r\pm V^r$, and by the count in S6 it is even further from linear
  mass.
- S8 (closing assessment). No route from this folder to either question of
  Problem 940 exists, and none is proposed.

## Checklist

- Quantifiers and scope: pass. The range $r\ge6$ is stated wherever the
  construction is invoked; Problem 940's range $r\ge3$ is covered a fortiori
  because the reconstruction page's Boundary records that the construction
  gives nothing at $r\le5$ (F5). The $\varepsilon$ of S6 is left
  unquantified by the section; the imported theorem fixes it, and no other
  reading is available (F3).
- Circularity: pass. Nothing about Problem 940 is assumed; the section
  derives the representability of $N$ from its being an $r$-th power.
- Model and convention changes: pass. $\mathcal P_r$ means the positive
  $r$-powerful integers on both the section and the shifted-target page; the
  problem's own definition admits $1$ vacuously (and $0$, if numbers include
  $0$); the one-summand representation of $N$ uses neither, and every
  summand of the construction is at least $2$.
- Finite and statistical overreach: pass. The $r=6$ decimals illustrate a
  comparison that holds for every $r\ge6$ by the inequality re-derived under
  W2.
- Uniformity: pass. Corollary 1.1's constants depend on $r$ as its statement
  says; the $O(X^{1/r})$ of S4 is the count of all $r$-th powers, with an
  absolute constant; the shifted-target constant depends on $r$, $k$ and
  $\varepsilon$, which the section omits without using (F3).
- Extremal conclusions: inapplicable. No infimum, supremum, attained value
  or sharpness sentence appears in the section.
- Consequences and composition: pass, with one suggested finding. Each
  "hence" of S3 is re-derived under W1; the composition of Corollary 1.1
  with the shifted-target count is re-derived under W2; the closing sentence
  S8 claims more than the argument composes (F1).
- Computation: pass. $2/36=0.0556$ and $4/6-5/468=307/468=0.65598$, which
  rounds to $0.6560$, recomputed in exact rational arithmetic.
- Reproduction: inapplicable. The section states no rerun command and
  retains no computation; the two decimals are its only numbers.
- Source and verdict fidelity: pass for the two imported theorems, whose
  restatements match their statements at the commit without strengthening,
  and for the tier-0 characterization of L18 and L19, which matches the
  Problem 940 Formalization paragraph and the reconstruction page. The
  clauses "open for $r\ge5$" and "the density question open for every $r$",
  attributed to the Current assessment, lie outside the read set and remain
  unverified here (a limitation, not a finding).

## Weakest steps

**W1 (S3, the one-summand representation).** Put $n=m^r+B^r\ge1$, so
$N=n^r$. For a prime $p\mid N$, $p\mid n$ and $v_p(N)=r\,v_p(n)\ge r$; thus
$p^r\mid N$ for every prime $p\mid N$, and $N$ is $r$-powerful under the
problem's definition. A single $r$-powerful number is a sum of at most $r$ of
them, so $N$ is representable; under a convention that counts $0$ as a
summand, $N=N+0+\cdots+0$ is a sum of exactly $r$. Hence $N$ is never in the
complement, and the $(r-2)$-summand representation of Corollary 1.1 is a
second representation of an integer already in the representable set.
Composition: the construction adds no integer to the representable set and
none to the complement, so no count in either question moves.

**W2 (S6, the lower bound for the same count).** Fix $r\ge6$ and
$k=r-2\ge4$. A Corollary 1.1 tuple $(a_1,\ldots,a_{r-2})$ with sum $N\le X$
has every $a_i$ a positive $r$-powerful integer, so it lies in
$\mathcal P_r^k$; its sum is $N\le X$; and $N\in\mathcal P_r$ by W1. The
tuple is therefore counted by the shifted-target set at $h=0$, and
$|0|\le X$. Distinct pairs $(m,B)$ give distinct ordered tuples by Corollary
1.1's statement, so the count is at least
$c_rX^{2/r^2}/\log\log X=X^{2/r^2-o(1)}$. The theorem's hypotheses $r\ge3$,
$k\ge2$, $\varepsilon>0$ hold. The bounds are consistent for every $r\ge6$,
not only at $r=6$: since $\delta_r<1/(r(2r+1))\le1/78$, $(r-2)/r\ge2/3$ and
$2/r^2\le1/18$,

$$
\frac{r-2}{r}-\delta_r-\frac{2}{r^2}\ \ge\ \frac23-\frac1{78}-\frac1{18}
=\frac{70}{117}>0 .
$$

**W3 (S7, the shape).** Every term of the Theorem 1 identity has degree
$r^2$ in $(U,V)$: $(U^r\pm V^r)^r$, $2\binom rj(U^{r-j}V^j)^r$ and
$v_\ell(U^{r-3}V^3)^r$. An $r$-th power of a linear form in $(U,V)$ has
degree $r<r^2$, so no term is one. After $x=U^r$, $y=V^r$ the two binomial
terms become $(x\pm y)^r$, but a monomial $x^{r-j}y^j$ with $0<j<r$ is not a
multiple of $(\alpha x+\beta y)^r$: with $\alpha\beta\ne0$ that power has
every monomial $x^{r-i}y^i$, $0\le i\le r$, with a nonzero coefficient, and
with $\alpha\beta=0$ it is a multiple of $x^r$ or $y^r$. So in neither
coordinate system is the identity, as written, a relation among $r$-th
powers of linear forms. The rank page's counting consequence, one
non-matching family contributing $O_r(B^{r-1})$ collision pairs with target
at most $X=B^r$, gives $O(X^{(r-1)/r})=o(X)$ for a fixed finite list, which
is what "cannot supply collisions of linear mass" says; the binomial
family's $X^{2/r^2+o(1)}$ collisions are fewer still, since $2/r^2<(r-1)/r$.
The section's parenthetical calls the monomial terms $r$-th powers of
monomials; they are positive integer multiples of such, since $2\binom rj$
and $v_\ell$ need not be $r$-th powers ($2r$ at $j=1$ is none for $r\ge3$,
as $1<2r<2^r$ and an integer with a rational $r$-th root has an integer
one). The conclusion is unaffected because the theorem's shape allows
positive rational coefficients and the obstruction is the degree (F2).

## Strongest attack

- S1. Compared clause by clause with the Problem 940 statement: same range
  $r\ge3$, same definition, same two questions, same "at most $r$". Failed.
- S2. Attacked the standing words "proved ... tier 0" for a Lean proof.
  Under the tier law a Lean proof without the independent fidelity audit is
  tier 0, which is exactly what the section says, and the Problem 940
  Formalization paragraph uses the same words; the reconstruction page's
  characterization of L18 and L19 (positive lower density of the complement
  at $r=3$ and $r=4$) implies the infinitude the section attributes, so the
  section claims no more than its premises. The two "open" clauses could
  not be checked, the Current assessment being excluded. Failed within the
  read set.
- S3. Sought a reading of Problem 940 under which an $r$-th power is not
  automatically representable. Only "a sum of exactly $r$ $r$-powerful
  numbers each exceeding $1$" would do it, and that is neither the problem's
  wording ("at most $r$") nor the corpus convention, which counts $0$ and
  $1$ as summands so that exactly-$r$ and at-most-$r$ coincide. Also checked
  that Corollary 1.1 produces $N=(m^r+B^r)^r$ for every $r\ge6$ under its
  stated hypotheses. Failed.
- S4. Attacked the count: the produced $N$ are $r$-th powers, and there are
  $\lfloor X^{1/r}\rfloor$ of those up to $X$, so $O(X^{1/r})$ holds; the
  sharper $O(X^{2/r^2})$ also holds since $N\le X$ forces $m,B\le X^{1/r^2}$
  (F4). Attacked "nothing follows" by trying to extract a consequence for
  question (b) from the collisions: the number of ordered $r$-tuples in
  $\mathcal P_r^r$ with sum at most $X$ is of order $X$, a density-zero
  conclusion would need those sums to collapse to $o(X)$ distinct values,
  and $X^{2/r^2+o(1)}$ exhibited coincidences remove at most that many. No
  consequence. Failed.
- S5. L18 and L19 concern $r=3$ and $r=4$, where the reconstruction page
  records that the construction gives nothing, so no statement of theirs is
  touched. Every summand of the construction is at least $2$: for $r\ge6$
  and $m>B\ge2$, $(m^r-B^r)^r\ge((B+1)^r-B^r)^r>1$, and each monomial term
  is at least $2r$; so a convention about $0$ and $1$ cannot change which
  sums the construction exhibits. The characterization of the convention of
  L18 and L19 rests on the reconstruction page and was not checked against
  the claim cards, which are outside the read set. Failed within the read
  set.
- S6. Attacked every hypothesis of the shifted-target theorem at the use:
  $r\ge6\ge3$, $k=r-2\ge4\ge2$, $\varepsilon>0$ fixed, $h=0$ within
  $|h|\le X$, $\mathcal P_r$ the same set, no primitivity hypothesis needed;
  attacked "ordered" (the theorem counts tuples, hence ordered ones, and
  Corollary 1.1's tuples are pairwise distinct as ordered tuples); attacked
  the decimals and the all-$r$ consistency (W2). Failed.
- S7. Attacked the characterization of the rank theorem's consequence
  against the rank page's own consequence (3): a fixed list of $K$ families
  contributes $O_r(KB^{r-1})=o(X)$ collision pairs, so "cannot supply
  collisions of linear mass" is the page's statement, not a strengthening.
  Attacked "not of that shape" (W3). The parenthetical misdescribes the
  coefficients without affecting the conclusion (F2). Failed.
- S8. Not a mathematical claim. The section's argument establishes that the
  direct transport fails and that the two folder bounds are unthreatened; it
  does not and cannot establish that no route from the mechanism exists.
  Recorded as F1.

## Premises

- Corollary 1.1, connections page lines 123 to 146, author-recorded, proof
  checked by another reviewer. Interface used: for $r\ge6$, every positive
  multiple $B$ of $B_0$ and every integer $m>B$ coprime to $B$, the identity
  at $(m,B)$ is an ordered tuple of $r-2$ pairwise distinct, positive,
  jointly coprime $r$-powerful integers with sum $N=(m^r+B^r)^r$; distinct
  pairs give distinct tuples; the number of such tuples with $N\le X$ lies
  between $c_rX^{2/r^2}/\log\log X$ and $C_rX^{2/r^2}$ for all large $X$,
  with constants depending only on $r$. Read at statement depth; its proof
  was not re-derived here.
- The reconstruction page,
  [[research/erdos_939/theorem_1_reconstruction|Theorem 1 reconstruction]],
  read in full and treated as established at its reviewed standing
  (independently reviewed as it stood on 2026-09-28T05:03:27Z with
  corrections applied since, as the assignment states). Used: Theorem 1 for
  $r\ge6$ with its
  identity (1) and $r-2$ summands; the Boundary paragraph "What the theorem
  does not give" (nothing at $r=4$ or $r=5$; the theorem needs $r\ge6$); the
  Boundary paragraph "Relation to Problem 940" (L18 and L19 at tier 0 prove
  positive lower density of the complement for $r=3$ and $r=4$; they count
  $0$ and $1$ as vacuous summands; Theorem 1 uses positive summands). The
  page's source manuscript was not consulted; the section invokes nothing
  from it beyond what the reconstruction page carries.
- The shifted-target theorem,
  [[research/erdos_940/powerful_subsum_counts|the shifted-target page]]
  lines 39 to 56: fix $r\ge3$, $k\ge2$, $\varepsilon>0$; uniformly for
  integers $|h|\le X$, the number of $(a_1,\ldots,a_k)\in\mathcal P_r^k$
  with $\sum a_i\le X$ and $\sum a_i+h\in\mathcal P_r$ is
  $\ll_{r,k,\varepsilon}X^{k/r-\delta_r+\varepsilon}$, with no primitivity
  hypothesis; $\mathcal P_r$ the positive $r$-powerful integers (line 23).
  Corpus page, not a held source; standing not read; used at statement
  depth as a comparison, never as a step in a proof.
- The rank theorem,
  [[research/erdos_940/linear_collision_families|the rank page]] lines 23
  to 49 and 98 to 157: for $r\ge3$, positive rationals $a_i$, $b_j$ and
  rational linear forms with a real parameter point where all $2r$ forms
  are positive, a relation $\sum_ia_iL_i^r=\sum_jb_jM_j^r$ whose summands do
  not match pairwise has its forms spanning at most $r-1$ dimensions
  ($\lfloor r/2\rfloor+1$ when a nonzero relation survives combining
  proportional forms); consequence (3): a non-matching family contributes
  $O_r(B^{r-1})$ collision pairs with target at most $B^r$, and a fixed
  finite list is ruled out as a linear-mass mechanism. Corpus page; standing
  not read; used at statement depth as a comparison only.
- The Problem 940 statement, [[problems/diophantine_problems/E0940/_index|E0940]]
  statement block: the definition of $r$-powerful and the two questions for
  $r\ge3$; its Formalization paragraph records L18 and L19 at tier 0.
- L18 and L19: not read. Their content and convention enter only through
  the Problem 940 Formalization paragraph and the reconstruction page.
- No library PDF was needed or read.

## Findings

- F1, suggested. Location, lines 463 to 464: "No route from this folder to
  either question of Problem 940 exists, and none is proposed." Defect: the
  sentence asserts the nonexistence of every route from the folder's
  mechanism, but the section establishes only that the direct transport
  fails, because every produced $N$ is already representable, and that the
  two folder bounds are unthreatened. A universal negative about routes is
  not a consequence of that argument, and the approach-vetting guidance asks
  that a precise failure not become a ban on a research direction. Witness:
  the argument's content is the pair of facts "$N$ is representable with one
  summand" and "the exhibited collisions number $X^{2/r^2+o(1)}$"; neither
  speaks to a use of the identity other than direct transport. Replacement:
  "No route from this folder to either question of Problem 940 was found,
  and none is proposed."
- F2, note. Location, lines 461 to 462: "(its terms are $r$-th powers of
  monomials in $U$, $V$ and of the binomials $U^r\pm V^r$)". Defect: the
  monomial terms carry the coefficients $2\binom rj$ and $v_\ell$, which are
  not $r$-th powers of rationals in general; the terms are positive integer
  multiples of $r$-th powers of monomials. Witness: at $j=1$ the coefficient
  is $2r$, and $1<2r<2^r$ for $r\ge3$. The conclusion "not of that shape" is
  unaffected (W3). Replacement: "(its terms are positive integer multiples
  of $r$-th powers of monomials in $U$, $V$, and the $r$-th powers of the
  binomials $U^r\pm V^r$)".
- F3, note. Location, lines 450 to 454: "the folder's shifted-target bound
  states that the number of ordered $k$-tuples ... is
  $O(X^{k/r-\delta_r+\varepsilon})$". Defect: "the folder" has no
  antecedent in the section, and the preamble uses "this folder" for the
  Problem 939 folder; the wikilink resolves it to the Problem 940 folder.
  The restatement omits the theorem's "for fixed $r\ge3$, $k\ge2$ and
  $\varepsilon>0$" and the dependence of the implied constant on $r$, $k$
  and $\varepsilon$; the use at fixed $(r,k)$ is unaffected. Replacement:
  "the Problem 940 folder's shifted-target bound states that, for fixed
  $r\ge3$, $k\ge2$ and $\varepsilon>0$, the number of ordered $k$-tuples ...
  is $O_{r,k,\varepsilon}(X^{k/r-\delta_r+\varepsilon})$".
- F4, note. Location, lines 444 to 445: "the $N$ produced number
  $O(X^{1/r})$ below $X$". Defect: none; the bound is correct, since every
  $N$ is an $r$-th power, but it is not the sharpest available: $N\le X$
  forces $m,B\le X^{1/r^2}$, so the produced $N$ number $O(X^{2/r^2})$, as
  Corollary 1.1's upper bound also gives, and $2/r^2<1/r$. Optional
  replacement: "number $O(X^{2/r^2})$ below $X$".
- F5, note. Location, line 439: "for each $r\ge6$". Defect: none; Problem
  940 asks for every $r\ge3$, and the section's "fails" holds at $r=3$, $4$
  and $5$ as well because the reconstruction page's Boundary records that
  the construction gives nothing there, but the section does not say so.
  Optional sentence after line 448: "At $r=3$, $4$ and $5$ the construction
  does not exist, as the reconstruction page records, so the outcome is the
  same."

## Verdict

- S1: refutation-failed.
- S2: refutation-failed, within the read set; the two "open" clauses
  attributed to the Current assessment were not checked.
- S3: refutation-failed.
- S4: refutation-failed.
- S5: refutation-failed, within the read set; the convention attributed to
  L18 and L19 was taken from the reconstruction page.
- S6: refutation-failed.
- S7: refutation-failed.
- S8: not a claim; an assessment sentence that overstates the argument's
  reach (F1).

No statement is refuted-as-stated, and for none is the verdict proof
defective; statement unresolved. Required corrections: none. Suggested: one
(F1). Notes: four (F2 to F5).

Limitations: the Current assessment and the claim cards L18 and L19 lie
outside the read set; Corollary 1.1 was used through its statement, its
proof being another reviewer's subject; the shifted-target theorem and the
rank theorem were used as stated interfaces for a consistency comparison,
and neither their proofs nor their standing were examined; the only
computations are exact rational arithmetic on the two exponents and the
consistency inequality, re-derived by hand under W2.

This focused review assigns no tier and changes no status.
