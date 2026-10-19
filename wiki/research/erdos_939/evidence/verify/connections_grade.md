---
name: research/erdos_939/evidence/verify/connections_grade
title: "Distinct grade of the Problem 939 connections reviews"
desc: |
  The distinct grader's pass for all eight focused reviews of the connections
  page and the quintic lead as they stood on 2026-09-28T13:50:48Z: sixteen
  corrections (C1 to C16) are accepted, every other finding is downgraded to a
  note with its reason, the graded verdict is recorded per statement, and the
  lead counts as reviewed once the corrections are applied; no tier and no
  status change.
created: 2026-09-28T19:30:11Z
updated: 2026-09-28T19:30:11Z
---

***

## Subject

**Date and pages.** The source as it stood on 2026-09-28T13:50:48Z (called
"the commit" below).
The page `wiki/research/erdos_939/connections.md`
([[research/erdos_939/connections|the connections page]]), read whole from
git at that commit with its line numbering (585 lines; H2 headings at lines
58, 303, 339, 406, 427, 466, 488, 517, 561 and 574), and the lead
`wiki/research/leads/quintic_powerful_identity_route/_index.md`
([[research/leads/quintic_powerful_identity_route/_index|the quintic lead]])
at the same commit, read whole, together with its evidence index and the
header and gauge table of its retained script
`evidence/util/quintic_identity_search.py`, read to check the two
search-coverage sentences. Every line number below is a line of the
connections page at this commit.

**Reports graded.** The eight focused reviews filed in
`wiki/research/erdos_939/evidence/verify/`, each read whole:

- [[research/erdos_939/evidence/verify/connections_shared_results_review|Shared results]]
  (lines 58–302);
- [[research/erdos_939/evidence/verify/connections_problem_939_at_r_4_the_two_summand_case_review|Problem 939 at r = 4]]
  (lines 303–338);
- [[research/erdos_939/evidence/verify/connections_problem_939_at_r_5_three_summands_review|Problem 939 at r = 5]]
  (lines 339–405, and the lead);
- [[research/erdos_939/evidence/verify/connections_problem_939_the_remaining_parts_review|Problem 939, the remaining parts]]
  (lines 406–426);
- [[research/erdos_939/evidence/verify/connections_problem_940_sums_of_at_most_r_r_powerful_numbers_review|Problem 940]]
  (lines 427–465);
- [[research/erdos_939/evidence/verify/connections_problem_1107_every_large_integer_as_a_sum_of_at__review|Problem 1107]]
  (lines 466–487);
- [[research/erdos_939/evidence/verify/connections_problem_937_and_progressions_of_powerful_numbers_review|Problem 937]]
  (lines 488–516);
- [[research/erdos_939/evidence/verify/connections_other_powerful_number_problems_examined_review|Other problems examined]]
  (lines 517–560).

**Read, and at what depth.**

- `docs/verification.md`, the sections "Independence and the assignment",
  "Exact subjects and durable evidence", "Report contract", "Grading and
  claim standing", "Audit checklist" and, under "Erdos-specific",
  "Whole-claim report" and "Audit checklist".
- `wiki/research/erdos_939/theorem_1_reconstruction.md` at the commit,
  whole (the identity, the data $J$, $t$, $v_\ell$, $P$, $B$, the
  distinctness fill, the Boundary paragraphs); the folder index
  `wiki/research/erdos_939/_index.md`, its Open, Mechanism and Connections
  paragraphs.
- [[problems/diophantine_problems/E0939/_index|Problem 939]] whole, including the
  Status, Formalization, Current assessment and Known results text, read to
  check the sections' attributions to the page (the grader is not blind);
  the statement blocks and Current assessments of
  [[problems/diophantine_problems/E0940/_index|Problem 940]] and
  [[problems/diophantine_problems/E0937/_index|Problem 937]]; the status lines and
  the Current assessment heading of
  [[problems/diophantine_problems/E1107/_index|Problem 1107]],
  [[problems/diophantine_problems/E0941/_index|Problem 941]] and
  [[problems/diophantine_problems/E1081/_index|Problem 1081]]; the Statement
  paragraphs of Problems 364, 365, 366, 367, 137 and 935.
- `wiki/research/erdos_940/finite_core_reduction.md`, the section
  "Independent polynomial summands still reduce to fixed forms", statement
  and proof; the theorem statements on
  `wiki/research/erdos_940/powerful_subsum_counts.md` and
  `wiki/research/erdos_940/linear_collision_families.md`, as interfaces.
- The library pages `recalled_abc_abcd_bounds.md` of the Corvaja–Zannier
  card, whole; the Bajpai–Bennett–Chan result pages for Corollary 1.3,
  Theorem 1.2 and Proposition 5.2, their Source and Statement paragraphs;
  the CrowdMath (2020) and Walsh (2024) cards, digest and result lists. No
  PDF was opened: every source fact ruled on below was checked by a
  reviewer on the held PDF, and the grader checked the reviewer's reading
  against the card or result page.
- The existence at the commit of the Problem 699 page that Lemma 2's
  cross-reference names.

**Grader's recomputation.** Exact arithmetic in a scratch directory outside
the repository, not retained: Proposition 4 over $\mathbb Q(\omega)$ at
$(a,b,c)=(1,1,-2)$ and at four rational triples with $ac=-2b^2$; the
factorization of the $Q_k$, the identity $Q_0+Q_1+Q_2=3UV$ and the
vanishing of $x^2+y^2+z^2+xy+yz+zx$ on $(Q_0,Q_1,Q_2)$; the hypotheses
(i)–(iv) and the conclusions of Lemma 1 for the Problem 1107 review's
Witness A on a sample of admissible points, and the number of its distinct
totals up to $X=10^{12},10^{14},\dots,10^{20}$, which is $0.18X^{7/20}$ to
two digits at every one of these $X$, against the section's $O(X^{1/5})$;
the two Problem 937 witnesses $49,289,529$ and $17^3,3^4\cdot7^3,37^3$ and
the scaled progressions $6^ks^k,2\cdot6^ks^k,3\cdot6^ks^k$; the five
partitions of $15$ into parts at least $5$; and the gauge representatives
$UV(U-V)$, $U^2V$, $U^3$ of the retained script at degree $3$. The
derivations in the reviews' weakest-step parts that the corrections rely on
(the Theorem 3 bridge at $r=5$, the progression bridge for Problem 937, the
density-zero count for Problem 1107) were re-derived by the grader line by
line.

**Role and independence.** The grader is distinct from the author of the
page and the lead (the compilation) and from each of the eight reviewers:
a fresh-context session given only this assignment, which read the reports
and the frozen subject and rebuilt the mathematics of every finding before
ruling. Each reviewer identifies itself as an independent examiner in a
fresh context given only its assignment, which took no part in writing the
page, the lead or the reconstruction page and read no earlier review or
grade of the folder; each records its allowed and actual reading and its
exposures. The grader is not blind and read standing text on purpose, as
the verifier-quotation rule assigns that check to the grader.

**Exposure rulings.** Each report discloses its exposures; the grader rules
every one immaterial by the content test, since nothing in any report could
only have come from the exposed text and no attack followed it:

- Shared results: the Problem 939 frontmatter and the other sections'
  summaries, seen while fixing section boundaries.
- Problem 939 at $r=4$: the Status paragraph of Problem 939. The References
  list, the witness of its F1, is bibliographic data that the section's own
  sentence is about; reading it was the source-fidelity check the charge
  requires, not an exposure.
- Problem 939 at $r=5$: the Status paragraph of Problem 939, and the
  Corvaja–Zannier card's reading-depth paragraphs.
- The remaining parts: the Status and Formalization paragraphs of Problem
  939 and the library cards' digests.
- Problem 940: the scope sentences of the two Problem 940 research pages and
  the Formalization paragraph of Problem 940.
- Problem 1107: the one-word status entries of Problems 1107 and 941.
- Problem 937: the `status` line of Problem 937 and the paragraph labels of
  the result pages.
- Other problems: the status line and empty sections of Problem 364.

File names of parallel reviews seen in directory listings, disclosed by
several reviewers, carried no content.

## Reports graded

Every report is graded **pass**. Each opens with a subject block that
resolves (the commit and the section's exact line range, which the grader
confirmed against the numbered page), records the reviewer's role,
independence facts, read set with depth and exposures, restates every
statement of its section with quantifiers and the page's conventions, gives
an explicit verdict on each of the ten checklist items, re-derives up to
three weakest steps in its own words, records a strongest attack per
statement that is a real attempt, lists its premises with interfaces and
reading depth, and files a verdict per statement in the full verdict words.
The reasons specific to each:

- **Shared results: pass.** All nine mathematical statements re-derived
  (Lemma 1's joint-coprimality step, Corollary 1.1's count with the Möbius
  estimate, the progression adaptation of the imported proof); the
  Mason–Stothers and Brownawell–Masser bounds confirmed on the held PDF;
  Proposition 4 and Corollary 4.1 recomputed by a different route, including
  an independent non-reality argument through the conic's $\mathbb Q$-model.
  Its four suggested findings and three notes are all sound; two become
  corrections (C1, C2).
- **Problem 939 at $r=4$: pass.** The abc sketch pushed to its edge, the
  line-restriction clause proved by composition, both source
  characterizations checked on the held PDFs; the required finding F1 is a
  true bibliographic defect (C4), and the grader adds what the excluded
  Current assessment shows.
- **Problem 939 at $r=5$: pass.** The strongest of the eight: it supplies
  the missing bridge to Theorem 3 (W1), exhibits the inhomogeneous
  admissible shape that defeats the closing implications (W2), finds the
  missing nonconstancy hypothesis (W3) and the false coverage sentence
  (F4), and grades the lead sentence by sentence. Its two required and four
  of its six suggested findings are accepted (C6–C9, C15, C16).
- **The remaining parts: pass.** Theorem 1's transfer under the joint
  reading, with the pairwise-coprimality witness at $r=6$; Walsh's Theorem
  1.1 read on the held PDF; the trivial bound derived from the count of
  $r$-powerful numbers; the count of Theorem 1's own family computed.
- **Problem 940: pass.** The one-summand representation, the consistency of
  the two folder bounds for every $r\ge6$ by an exact inequality, and the
  shape comparison with the rank theorem, all re-derived; the two imported
  theorems checked against their pages.
- **Problem 1107: pass.** Two refutations with exact witnesses, both
  recomputed by the grader; an independent proof of the density-zero
  conclusion by two routes, which the corrections adopt.
- **Problem 937: pass.** The misapplication of Corollary 3.1 exhibited with
  two witnesses, the repair derived through the corollary's own two steps
  and Theorem 3, the dropped primitivity qualifier witnessed by scaled
  progressions, and Corollary 1.3 checked on the held PDF.
- **Other problems examined: pass.** The constant-term case of Theorem 3
  re-derived from Lemma 2, the bridge for values checked with $b=1$, the
  Pell witness for the strongest reading exhibited, all thirteen problem
  descriptions compared with their statements.

## Corrections

The accepted corrections, numbered across the folder. Each names the page,
the location at the commit, and the exact replacement; none touches a
`statement:` field, since the pages carry no claim cards.

- **C1.** Page: connections page. Location: the `desc` field, lines 7–8,
  "a proved Mason-Stothers obstruction to every polynomial family with two
  summands", and the H3 heading at line 186, "Theorem 3: no polynomial
  family with two summands". Replacement: in the `desc`, "a proved
  Mason-Stothers obstruction to every polynomial family with two summands
  for r at least 3"; heading, "Theorem 3: no polynomial family with two
  summands for r at least 3". Reason: at $r=2$ such families exist, as line
  202 records; the statement carries the qualifier and the summaries do not
  (shared results F2).
- **C2.** Page: connections page. Location: lines 32–33, "the former is
  reproved below as Lemma 2, and the latter is used only to say what it
  does not exclude". Replacement: "the Mason–Stothers bound is reproved
  below as Lemma 2, the Brownawell–Masser bound is used only to say what it
  does not exclude, and the proposition is consumed in Corollary 3.1 with
  its proof adapted to a progression". Reason: with "the former" read as
  the proposition the sentence is false (shared results F4).
- **C3.** Page: connections page. Location: lines 324–325, "so
  $c<\kappa(\eta)c^{3(1+\eta)/4}$ bounds $c$". Replacement: "so, for any
  fixed $\eta<1/3$, $c^{(1-3\eta)/4}<\kappa(\eta)$ bounds $c$". Reason: the
  displayed inequality bounds $c$ only for $\eta<1/3$; at $\eta=1/3$ it
  reads $c<\kappa(1/3)\,c$ ($r=4$ review F2).
- **C4.** Page: connections page. Location: line 329, "makes the same
  remark; neither is cited on the problem page." Replacement: "makes the
  same remark; Walsh (2024) is entry [Wa24] of the problem page's
  References, cited there for its $r=3$ construction, and the CrowdMath note
  is cited in the page's Current assessment for this finiteness." Reason:
  false as written; the References list of `E0939.md` at the commit carries
  [Wa24] at lines 52–54 ($r=4$ review F1), and its Current assessment cites
  the CrowdMath card at lines 126–132, which the reviewer's read set
  excluded and the grader checked.
- **C5.** Page: connections page. Location: lines 336–337, "A negative
  outcome of either kind is not obtainable from polynomial identities, by
  Theorem 3." Replacement: "Neither an example nor an infinite family at
  $r=4$ can come from a polynomial identity, by Corollary 3.1." Reason:
  Theorem 3 excludes an example or an infinitude produced by a polynomial
  family; it says nothing about nonexistence or finiteness, which the
  sentence's plain reading attributes to it ($r=4$ review F4).
- **C6.** Page: connections page and the lead. Location: connections page
  lines 348–351, "that satisfies (i)–(iv) and the positivity clause would
  give infinitely many jointly coprime $5$-powerful triples with
  $5$-powerful sum and answer the second question negatively at $r=5$";
  lead, section "Route", the premise "(P) ... with positive leading
  coefficients in $U$ for some admissible $B$." Replacement: connections
  page, "that satisfies (i)–(iv), the positivity clause and the
  nonconstancy of $A_4(U,B)$ would give infinitely many jointly coprime
  $5$-powerful triples with $5$-powerful sum and answer the second
  question, read with joint coprimality, negatively at $r=5$"; lead, "(P)
  ... with positive leading coefficients in $U$ and $A_4(U,B)$ nonconstant
  for some admissible $B$." Reason: Lemma 1 derives the infinitude from the
  separate hypothesis that $A_n(U,B)$ is nonconstant, and (iii) admits
  $K=1+UV(V-B)$ with $K(U,B)=1$; the hypothesis is automatic for
  homogeneous identities of positive degree and must be carried for the
  general premise ($r=5$ review F3 and F9).
- **C7.** Page: connections page. Location: lines 351–354, "(that would be
  a three-term identity of $5$-powerful polynomials after combining them)".
  Replacement: "(combining them leaves a three-term identity that still
  contains a rational multiple of $A_1=K^5$ beside a rational multiple of
  the monomial $A_2$, which are coprime by (iii) and (iv), so its three
  terms are pairwise coprime; positivity at an admissible point excludes the
  merges with a vanishing coefficient; and Theorem 3 applies after
  specializing $V$, or $U$ when $a=0$, to a generic complex value, which
  preserves $5$-powerfulness, pairwise coprimality and the nonconstancy of
  the monomial)". Reason: Theorem 3 needs pairwise coprime polynomials in
  one variable, not all constant, and the parenthetical checks none of
  these ($2f+3f=5f$ is a three-term identity of $5$-powerful polynomials);
  the grader re-derived the reviewer's bridge, case by case over the six
  proportional pairs ($r=5$ review F2).
- **C8.** Page: connections page and the lead. Location: connections page
  lines 362–363, "The gap is therefore: *does a four-term identity of
  $5$-powerful binary forms with rational terms exist?*", and lines
  402–404, "a proof that no real four-term identity of $5$-powerful binary
  forms exists would close the polynomial route and leave $r=5$ to
  constructions of the kind that settled $r=3$."; lead, section "What is
  known about the premise", "Over $\mathbb C$ the premise's polynomial part
  is satisfiable"; section "Consequential gap", "A proof that no four-term
  identity of $5$-powerful binary forms with real terms exists would close
  this route"; section "Next step", "a proof of nonexistence in all degrees
  would close the route". Replacement: connections page, "The gap is
  therefore: *does a four-term identity in $\mathbb Z[U,V]$ satisfying
  (i)–(iv) with $r=5$ exist?* Lemma 1 does not need homogeneity; the
  homogeneous case, a four-term identity of $5$-powerful binary forms with
  rational terms, is the case the searches below and the lead treat." and
  "a proof that no real four-term identity of $5$-powerful binary forms
  exists would close the homogeneous case of the polynomial route, leaving
  inhomogeneous identities of the shape (i)–(iv), which nothing here
  examines, and constructions of the kind that settled $r=3$."; lead,
  "Over $\mathbb C$ a four-term identity of $5$-powerful forms with one
  fifth-power term and one monomial term exists", "A proof that no
  four-term identity of $5$-powerful binary forms with real terms exists
  would close the homogeneous case of this route; the transfer does not
  need homogeneity, and inhomogeneous identities satisfying its hypotheses
  are a separate possibility that nothing here examines", and "a proof of
  nonexistence in all degrees would close the homogeneous case of the
  route". Reason: (iii) is satisfied by inhomogeneous $K$, for instance
  $U^2+U^2V^3+V^2$, and no reduction of the inhomogeneous case to binary
  forms exists on either page, so the closing implications are unsupported
  as written ($r=5$ review F1).
- **C9.** Page: connections page and the lead. Location: connections page
  lines 378–379, "(the mixed shapes $L^6M^9$, $L^7M^8$, $L^5M^{10}$ were
  not searched)"; lead, section "What is known about the premise", "The
  mixed shapes of degree $15$ ($L^6M^9$, $L^7M^8$, $L^5M^{10}$ with $L,M$
  linear) and every degree above $15$ were not searched."; the same list in
  the docstring of `evidence/util/quintic_identity_search.py`, line 12.
  Replacement: connections page, "(the shapes $L^6M^9$ and $L^7M^8$, and
  identities mixing shapes among the four terms, were not searched;
  $L^5M^{10}=(LM^2)^5$ lies inside the searched shape)"; lead, "The shapes
  $L^6M^9$ and $L^7M^8$ of degree $15$ ($L,M$ linear), identities mixing
  shapes among the four terms, and every degree above $15$ were not
  searched; $L^5M^{10}=(LM^2)^5$ lies inside the searched shape."; script
  docstring, "not the mixed shapes L^6 M^9, L^7 M^8". Reason: the
  $5$-powerful shapes of degree $15$ are the partitions $(15)$, $(10,5)$,
  $(5,5,5)$, $(9,6)$, $(8,7)$; the first three are fifth powers of cubics,
  and the search at degree $3$ fixes $Q_4$ to $UV(U-V)$, $U^2V$ and $U^3$
  with $Q_1,Q_2,Q_3$ general, so $(10,5)$ was searched ($r=5$ review F4).
- **C10.** Page: connections page. Location: lines 463–464, "No route from
  this folder to either question of Problem 940 exists, and none is
  proposed." Replacement: "No route from this folder to either question of
  Problem 940 was found, and none is proposed." Reason: the section proves
  that the direct transport fails and that the two folder bounds are
  unthreatened; a universal negative about routes does not follow (Problem
  940 review F1).
- **C11.** Page: connections page. Location: lines 477–481, from "In the
  two-variable device of Lemma 1 the total $A_n(U,V)$" to "whose values
  also have density zero." Replacement: "In any device of Lemma 1 every
  total $A_n(m,B)$ is an $r$-powerful integer, and the $r$-powerful
  integers up to $X$ number $O_r(X^{1/r})$, so the totals have density zero
  for every $r\ge2$, whatever the degree of $A_n$; for the Theorem 1 total
  $(U^r+V^r)^r$ the count is $O(X^{2/r^2})$, since $N\le X$ forces
  $m,B\le X^{1/r^2}$." Reason: the device $(U^2-V^5)^2+4U^2V^5=(U^2+V^5)^2$
  at $r=2$ satisfies (i)–(iv), its total is not a form, and its distinct
  totals up to $X$ number $\gg X^{3/10}/\log X$ against the asserted
  $O(X^{1/5})$; the grader recomputed the count. The replacement also
  removes the word "form", so Problem 1107 review F3 is subsumed (Problem
  1107 review F1).
- **C12.** Page: connections page. Location: lines 481–484, from "With $s$
  parameters the count is $O(X^{s/D})$" to "and not an identity."
  Replacement: "An identity in any number of parameters whose total is
  $c\prod_jH_j^{e_j}$ with every $e_j\ge r$, as (i) requires, has totals of
  density zero as well: its positive values are $|c|\prod_j|h_j|^{e_j}$
  with nonzero integers $h_j$, and there are $O(X^{1/r}(\log X)^{k-1})$
  such products up to $X$. Without that shape the total is only the sum of
  its $r$-powerful summands, and representing a positive proportion of the
  integers by it is the Waring-type problem for $r$-powerful numbers
  itself, not a consequence of an identity." Reason: the degree of the
  total does not control the count; $U_1^2+U_2^2+(U_3U_4U_5)^2$ has five
  parameters, degree six, and totals of lower density at least
  $5/6-\pi/4$ by the three-square theorem, while under the $r$-powerful
  reading no number of parameters reaches a positive proportion (Problem
  1107 review F2).
- **C13.** Page: connections page. Location: lines 500–502, "so Corollary
  3.1 applies to any polynomial family of pairwise coprime three-term
  progressions and excludes it for every $r\ge3$, whatever the shape of the
  terms". Replacement: "so, once $a$, $b$ and $c$ are $r$-powerful as
  polynomials and $\gcd(a,c)=1$ in $\mathbb Q[t]$, which the first two
  steps of the proof of Corollary 3.1 give from the values on the
  progression, Theorem 3 applies to the triple $(a,c,2b)$ and excludes
  every polynomial family of pairwise coprime three-term progressions, in
  the sense of Corollary 3.1, for every $r\ge3$, whatever the shape of the
  terms". Reason: Corollary 3.1's statement requires the values of the sum
  to be $r$-powerful, and $2b(t)$ is not whenever $b(t)$ is odd, as at
  $49,289,529$ ($2\cdot289=2\cdot17^2$) and at $17^3,3^4\cdot7^3,37^3$; the
  polynomial-level remark cannot supply a value-level hypothesis. The
  statement is true by the reviewer's derivation, which the grader checked
  (Problem 937 review F1 and F4).
- **C14.** Page: connections page. Location: lines 511–513, "three-term
  progressions of $k$-powerful numbers with $k\ge4$ are conditionally
  finite". Replacement: "primitive three-term progressions of $k$-powerful
  numbers with $k\ge4$ are finite under abc". Reason: $6^ks^k$,
  $2\cdot6^ks^k$, $3\cdot6^ks^k$ is a three-term progression of $k$-full
  numbers for every $k\ge2$ and $s\ge1$; the source's $A^\infty(k)$ counts
  primitive progressions, as the result page states (Problem 937 review
  F2).
- **C15.** Page: the lead. Location: section "Route", the bullet "The
  three-term obstruction", "No identity $a+b=c$ of pairwise coprime
  $r$-powerful polynomials with $r\ge3$ exists". Replacement: "No identity
  $a+b=c$ of pairwise coprime $r$-powerful polynomials, not all constant,
  with $r\ge3$ exists". Reason: constants are $r$-powerful under the page's
  convention, so $1+1=2$ refutes the sentence as written; Theorem 3 carries
  the hypothesis ($r=5$ review F6).
- **C16.** Page: the lead. Location: section "Target and status evidence",
  "its $r=4$ case is excluded from every polynomial route by the theorem
  recalled below". Replacement: "its $r=4$ case is excluded from the
  polynomial-identity route of Corollary 3.1 of the connections page,
  one-parameter families and polynomially parametrized parameter curves, by
  the theorem recalled below". Reason: Corollary 3.1 and its scope
  paragraph name what the recorded result does not cover; "every polynomial
  route" claims more ($r=5$ review F7).

## Rejected and downgraded findings

No finding is rejected as wrong; each finding below is sound as a note and
is downgraded from a correction for the reason given.

- **Shared results F1** (the constant $c_2$ in (iv)): downgraded to a
  note. The statement is correct as written, since (iv) reuses the symbol
  $c_2$ of the presentation (i), which forces $\prod_jH_{2j}^{e_{2j}}=U^aV^b$;
  the reviewer's rewording is optional.
- **Shared results F3** ("version" in Corollary 4.1): downgraded to a note.
  The preceding sentence fixes the scope (projective change of variables
  and rescaling), and the $r=5$ section restates the corollary as "this one
  is not real"; the more precise sentence is optional.
- **Shared results F5, F6, F7**: notes. The third expression
  $-W=bc'-b'c$ gives the bound for $\deg a$; the conic of Corollary 4.1 has
  the $\mathbb Q$-model $x^2+y^2+z^2+xy+yz+zx=0$, $w=x+y+z$, positive
  definite, which the grader verified and which strengthens the page
  without correcting it; the Problem 699 page named at line 163 exists at
  the commit, and its use of the statement was not checked.
- **$r=4$ review F3** ("sporadic"): downgraded to a note. The sentence is a
  picture, true under the reading "no solution lies in a polynomial family"
  that its second clause makes natural; at $r=3$ the same theorem coexists
  with infinitely many solutions, so the reviewer's rewording is the
  clearer one and is recommended, not required.
- **$r=4$ review F5** (unverified attributions): resolved by the grader.
  The Current assessment of Problem 939 is read 2026-09-27 and its Known
  results record no example at $r=4$ and the forum-reported bound
  $\max(a,b)>10^{14}$; the folder index records the summand count
  $\lceil r/2\rceil+1>r-2$ for $r\le5$.
- **$r=5$ review F5** (minimal degree): downgraded to a note. "Smallest
  possible degree, $10$" is true: in degrees $5$ to $9$ a $5$-powerful form
  is $cL^D$, $D$-th powers of distinct linear forms are independent, and the
  degenerate cases are a vanishing proper subsum or four proportional forms
  with a common factor; the parenthetical's sketch treats degree $5$ and
  the first exception only, and the fuller sentence is recommended.
- **$r=5$ review F6**, the Lemma 1 part ($a+b\ge1$ and $m\ge1$ dropped in
  the lead's restatement): note; neither omission changes a deduction.
- **$r=5$ review F8, F9, F10**: notes. The symbol $d$ at line 344 is the
  problem page's name for the sum and is undefined on the connections
  page; the joint reading is now named by C6; the degree-$10$ plan in the
  lead needs a real-algebraic step after the Gröbner or resultant
  computation, which the lead should name when the computation is run.
- **Remaining parts F1** ("Settled negatively by Theorem 1" without the
  coprimality convention): downgraded to a note. The page's Conventions
  define joint coprimality and its $r=4$ section states that the site
  question's coprimality is joint; "settled" describes the mathematics and
  the preamble disclaims any status change. The pairwise-coprimality
  witness ($12X^5Y$ and $40X^3Y^3$ share $X^3Y$) is correct and worth
  recording.
- **Remaining parts F2** (the pronoun "it"): downgraded. In "Corollary 1.1
  records the size of the family it produces" the antecedent is the
  subject, Corollary 1.1, under which the sentence is correct; the
  reviewer's count of Theorem 1's one-parameter family, of order
  $r^2X^{1/r^2}/\log X$ and $78{,}488$ at $r=6$, $X=10^{216}$, is right and
  may be added.
- **Remaining parts F3, F4, F5**: notes (the warrant for Nitaj and Cohn is
  Corollary 3.1, whose texts are not held; the first question at $r\ge6$
  goes unmentioned; the trivial bound rests on the $O_r(X^{1/r})$ count).
- **Problem 940 F2** ("$r$-th powers of monomials"): downgraded to a note.
  The parenthetical describes the shape up to the coefficients $2\binom rj$
  and $v_\ell$, which is what the comparison with the rank theorem's shape
  needs; "positive integer multiples of $r$-th powers of monomials" is more
  exact and optional.
- **Problem 940 F3, F4, F5**: notes; the imported theorem's "for fixed
  $r$, $k$, $\varepsilon$" and the sharper $O(X^{2/r^2})$ are correct and
  optional; the outcome at $r=3,4,5$ follows from the reconstruction page's
  Boundary.
- **Problem 1107 F3** ("form"): subsumed by C11.
- **Problem 1107 F4**: resolved by the grader; the Problem 1107 page at the
  commit records "No current assessment is recorded".
- **Problem 937 F3** ("needed the elliptic curve"): downgraded to a note.
  The sentence reads as narrative of the source's construction; the
  necessity reading is unproved, and "the source's four-term construction
  uses an elliptic curve" is recommended.
- **Problem 937 F5** (pairwise versus joint coprimality): note; for a
  three-term progression of $r$-powerful numbers the two readings coincide,
  as the reviewer's argument shows and the grader checked.
- **Other problems F1** (the Pell witness): downgraded to a note. The
  sentence holds in the page's sense of a polynomial family, which its
  $r=4$ section defines and which the sentence's own clause about the Pell
  families presupposes; citing Corollary 3.1 with $b=1$ rather than
  Theorem 3 for the values statement is recommended.
- **Other problems F2, F3, F4**: notes; the grader checked F4 against the
  Statement paragraphs of Problems 935, 367 and 137 and confirms the
  parenthetical fits Problem 935 exactly and the other two loosely.

## Graded verdicts

**Shared results.** S1 (Lemma 1): refutation-failed. S2 (application to
the Theorem 1 identity): refutation-failed. S3 (Corollary 1.1):
refutation-failed. S4 (Lemma 2 with its normalization remark):
refutation-failed. S5 (Theorem 3, weighted form and sharpness):
refutation-failed. S6 (Corollary 3.1): refutation-failed, standing at the
author-recorded standing of the Problem 940 proposition it adapts. S7
(coverage paragraph): refutation-failed. S8 (Proposition 4):
refutation-failed. S9 (Corollary 4.1): refutation-failed. S10 (provenance
sentence): not a claim.

**Problem 939 at $r=4$.** S1 (target): refutation-failed; the attributions
to the Current assessment are verified by the grader. S2 (the transfer is
excluded): refutation-failed. S3 (interpretation): refutation-failed; the
folder index's count is verified. S4 (literature): the mathematical claim
that abc implies finiteness at $r=4$ and both source characterizations are
refutation-failed; the sketch's inference needs C3; the bibliographic
clause is refuted-as-stated and replaced by C4. S5 (picture):
refutation-failed under the reading "no solution lies in a polynomial
family" noted above. S6 (next investigation): refutation-failed for its
content, with its last sentence replaced by C5.

**Problem 939 at $r=5$ (section).** S1 (target): not a claim; the two
examples and the $10^{16}$ bound are on the problem page, as the grader
checked. S2a (values of the transfer): refutation-failed. S2b (infinitude):
proof defective; statement unresolved as written, for want of the
nonconstancy hypothesis; refutation-failed after C6. S3 (no two summands
proportional): refutation-failed, with its justification supplied by C7.
S4 (minimal complex degree $10$): refutation-failed. S5 (non-reality):
refutation-failed, as graded under the shared results. S6 (the gap is the
binary-form question): proof defective; statement unresolved as written;
refutation-failed after C8. S7a (degree-$10$ normalization):
refutation-failed. S7b (degree-$15$ coverage): refuted-as-stated, corrected
by C9. S7c (search outcomes): not a claim. S8 (what it does not give):
refutation-failed as a labeled heuristic. S9a (a found identity refutes
finiteness): refutation-failed. S9b (a nonexistence proof for forms closes
the route): proof defective; statement unresolved as written;
refutation-failed after C8.

**The lead.** L1 (target and conventions): proof defective; statement
unresolved as written, for "every polynomial route"; refutation-failed
after C16. L2 (transfer restated): refutation-failed for the value
statement; the infinitude phrase follows S2b and C6. L3 (obstruction
restated): refuted-as-stated as written, by $1+1=2$; refutation-failed
after C15. L4 (complex identity restated): as S4 and S5. L5 (premise and
deduction): (P) is a provisional premise, not a claim; the deduction under
(P) is proof defective; statement unresolved as written and
refutation-failed after C6; the distinctness clause is refutation-failed.
L6 (known about the premise): refutation-failed after C8 and C9. L7
(exploratory computation): not a claim. L8 (consequential gap): proof
defective; statement unresolved as written; refutation-failed after C8. L9
(next step): the closing implication as L8, refutation-failed after C8 and
C9; the remaining sentences refutation-failed, with the real-algebraic step
noted. L10 (standing): refutation-failed.

**Problem 939, the remaining parts.** S1 (third question, literature):
refutation-failed; the clause "as the problem page records" is verified by
the grader against the page's Status and Current assessment. S2 (Corollary
3.1 at $r=3$): refutation-failed. S3 (the constructions are
non-polynomial): refutation-failed. S4 (limitation): refutation-failed. S5
(second question at $r\ge6$, coprimality joint): refutation-failed. S6
(count of the family): refutation-failed. S7 (trivial bound and
comparison): refutation-failed. S8 (cross-reference): not a claim.

**Problem 940.** S1 (target): refutation-failed. S2 (status record):
refutation-failed; the two "open" clauses are verified by the grader
against the Current assessment. S3 (transfer failure): refutation-failed.
S4 (no consequence): refutation-failed. S5 (L18 and L19):
refutation-failed. S6 (first comparison): refutation-failed. S7 (second
comparison): refutation-failed. S8 (closing assessment): the universal
negative as written is unsupported; refutation-failed after C10.

**Problem 1107.** S1 (target facts): refutation-failed; "no compiled
assessment" is verified by the grader. S2 (totals of an identity):
refutation-failed. S3 (count bound): refuted-as-stated, replaced by C11. S4
(density zero): refutation-failed as a statement; its proof on the page is
replaced by C11. S5 (parameters): refuted-as-stated, replaced by C12. S6
(outcome): refutation-failed.

**Problem 937.** S1 (target and status): refutation-failed; the status is
verified by the grader against the Current assessment. S2 (reduction):
refutation-failed. S3 (obstruction): proof defective; statement unresolved
as written; refutation-failed after C13, which writes the reviewer's
derivation into the page. S4 (the case $r=2$): refutation-failed. S5 (four
terms at $r=2$): refutation-failed on the reading that the source's
construction uses an elliptic curve. S6 (Corollary 1.3):
refutation-failed. S7 (finiteness sentence): refuted-as-stated as written;
refutation-failed after C14. S8 (closure): not a claim; the folder index at
the commit records the outcome the section reports.

**Other powerful-number problems examined.** S0 (opening sentences): not a
claim. S1 (Theorem 3 with a constant term): refutation-failed. S2 (the
mixed case for Problem 366): refutation-failed. S3 (no polynomial family of
consecutive powerful numbers, in the page's sense): refutation-failed. S4
(Pell consistency): refutation-failed. S5 (specific pairs and triples):
refutation-failed for its conclusion. S6 (Problem 938): not a claim. S7
(Problem 943 at $r=2$): refutation-failed. S8 (Problems 1081 and 941):
refutation-failed; the status words are verified by the grader. S9
(Problems 942, 935, 367, 137, 936, 1108): not a claim.

**Lead outcomes.** `quintic_powerful_identity_route`: **reviewed**. The
route rests on Lemma 1 (S1 of the shared results), on the transfer at
$r=5$ (S2a and S2b of the $r=5$ section, L2 and L5 of the lead) under the
joint-coprimality reading, and, for its shape constraints, on Theorem 3,
Proposition 4 and Corollary 4.1 (S5, S8 and S9 of the shared results);
after C6, C7, C8, C9, C15 and C16 every one of these statements is
refutation-failed. The premise (P) stays a provisional premise that nothing
establishes, the searches stay exploratory, and the corrections C6, C8, C9,
C15 and C16 change the lead's own text and are to be applied to it.

No tier is assigned and no status changes.
