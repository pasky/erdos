---
name: research/erdos_354/evidence/verify/lead_rational_ratio_dyadic_floor_descent_rereview_grade
title: "Distinct grade of the blind re-review of the lead rational_ratio_dyadic_floor_descent"
desc: |
  Grades the blind re-review of the rational-ratio descent lead as it stood on
  2026-10-02: the report passes; every verdict is re-derived and agreed, one
  uncovered bullet is adjudicated by the grader; both required corrections are
  accepted, R1 sharpened and extended to the connections page, and the four
  suggested corrections are accepted, S1 with its standing clause replaced; the
  lead is reviewed once the corrections land, research state ready; no tier is
  assigned.
created: 2026-10-02T17:38:03Z
updated: 2026-10-02T17:38:03Z
---

***

## Subject and independence

**Paths and date.** The tree as it stood on 2026-10-02. The subject is the blind
extraction, kept outside the repository, of two pages on that date: the lead
page `wiki/research/leads/rational_ratio_dyadic_floor_descent/_index.md` with
its review-status fields and its "Current review" section removed, and the
connections page `wiki/research/erdos_354/connections.md`, whose section
"Problem 354: Hegyvári's conjecture at a rational ratio" (lines 59--304 of the
committed page) is the part the lead rests on. The grader checked the freeze
without reading the removed text, by a script that reports only counts: the
connections extraction and the committed page are byte-identical, so the
report's phrase "with its review-report sentences cut" describes a cut that
removed nothing from that page; every line of the lead extraction but one
occurs, in order, in the committed page, the exception being the paragraph of
"Provisional premises", whose two retained sentences the extraction joins into
one line, and 37 lines of the committed page are absent from the extraction,
consistent with the cut the report describes. Both paths are present in the tree
of that date.

**Report.**
[[research/erdos_354/evidence/verify/lead_rational_ratio_dyadic_floor_descent_rereview|The blind re-review]]
(552 lines): Subject and independence, Restatement, Statements and
verdicts S1--S17, Checklist, Weakest steps W1--W3, Strongest attack (a)--(d),
Premises, Required corrections R1--R2, Suggested corrections S1--S4, Notes
N1--N5, Verdict.

**What the grader read, and at what depth.** The extraction in full at proof
depth: the lead page and the section named above, with the proofs of Lemma
354.1, Proposition 354.2 (i)--(v), Corollary 354.3 and Lemma 354.4 re-derived.
The report in full. Reconstruction pages as they stood on that date, mathematics
only, their standing paragraphs skipped: the normalization page in full (items
1--6 and the reduction re-derived), the Theorem 5.1 page in full (Steps 1--6
re-derived, including (4.1) as $64d-42\ge22d$, (4.3) as $20d-13>0$ and the
certificate lemma's three conditions), the three lemma pages in full, the
theorem page's Step 2 (re-derived), the bounded-spacing page's Definitions,
Statement and Steps 1--2, the windows page's Definitions, Statement and Step 1,
the digit-budget page's Definitions, Statement and Steps 4--5, and the
finite-event page's Definitions and Statement. The lead's evidence index (its
closing standing sentence skipped) and its `main.py` in full. Library as it
stood on that date: the Yu--Chen canonical conversion at Section 3, Theorem 5.1
with (5.2), Sections 6--7 and Appendix A; the Yu--Chen theorem page; the Fan
canonical conversion at the paragraph after (1.9) and the Fan PDF text layer at
p. 4; the Hegyvári 1991 card in full; the `desc` lines of the Hegyvári 1994,
jenw1n and kitamura cards. Problem page: Statement, Formulation, Status, and the
Current assessment's quoted site commentary and "Remaining gaps" list. Operating
instructions: `docs/verification.md`, `docs/evidence.md`, `docs/research.md`,
`docs/approach_vetting.md`, `docs/math_authoring.md`. Not read: the live lead
page, every other record under an `evidence/verify/` folder except the section
shape of [[research/erdos_354/evidence/verify/connections_grade|the connections
grade]], all review-status, standing and "Current review" text, and the
reviewer's scratch code.

**Computation.** In exact integer arithmetic, with the grader's own
scripts in ignored scratch: subset sums kept as a Python set with a bitset
cross-check, a primitive different from the evidence's folded bitset and
the reviewer's bit string. Recomputed: the constants of S6; the five
pinned certificates with their normalization values; the
thirty-two-denominator sweep under the page's rule (least $T$ with
$2\le\lfloor2\gamma\rfloor<\lfloor3\gamma\rfloor<2\lfloor2\gamma\rfloor$);
the two controls and the residues modulo $5$ of the subset sums of
$(5/2,5)$; the zero runs of $16/5$, $16/7$, $16/9$ and of $1/d$ over the
sweep; at ratio $3/2$ the conversions, exact layers, maximal common zero
runs, $h_n$ and certificates of $\gamma=1/511$, $24/7$, $1/193$ and of
$(192/23,128/23)$; the two-event witness at four values of
$x\in[1/4,1/3)$; the periods of $1/9$ and $1/3$; and the certificate lemma
from the Appendix A table parsed from the conversion (twelve templates,
125 nodes, 113 links, 500 node instances, conditions 1--3 under the cone
criterion, with a negative control that flips one mask bit). Every figure
of the report reproduces. Both entry points were run from the repository
root: the lead's exits $0$ with 23 passing checks, the folder's exits $0$
with 12 passing checks.

**Independence facts, by role.** The grader is a distinct grader in a fresh
context (model: Claude Fable 5.1), given only the grading assignment, distinct
from the author of the lead and the connections page and from the reviewer; the
grader took no part in writing any page, the report, the reconstruction pages or
the evidence, and did not read the reviewer's scratch code. The grader is not
blind, as a grader need not be. A first attempt at this re-review, whose
extraction carried the earlier verdicts, was stopped before completion and its
output discarded; this record is from a blind extraction frozen on 2026-10-02
and kept outside the repository.

**Materiality rulings.** The report announces four exposures and lists five;
each is ruled on here by the content test of `docs/verification.md`. (1) The
`desc`, heading and finding-location lines of an existing record of this folder,
summarizing verdicts on an earlier revision of the same pages: immaterial.
Nothing in the report could only have come from it: R2 is forced by the
extraction's own paragraph, which calls $\gamma=1/511$ covered while its literal
definition excludes it, and R1 by the open normality of $\sqrt2$, which the
extraction's own connections sentence states ("not known to have"); the
direction of attack, recomputing every figure and testing the hypotheses of
Proposition 354.2 at the gap set's boundary, is the one a refutation charge on
this lead takes without prompting; and the sentence R2 corrects entered the lead
only in the correction change of 2026-09-28, the last change to this folder
before the re-review, so no record of the folder could have assessed it, while
R1's phrase is older but its defect is read off the extraction's own clause. (2)
The problem page's Status paragraph and `desc`: immaterial, the lead states the
same fact. (3) One line of the folder's evidence index naming a report count and
"no tier is assigned": immaterial, no mathematics. (4) The black-box run of the
lead's entry point: not an exposure to excluded material, since the evidence
outside `evidence/verify/` is part of the subject; the report compares its
independent figures to the printed ones, which is the right use. (5) The `desc`
lines of two re-review records on other leads, printed by a read-only lint run
after the report was written: immaterial, other subjects, after the verdict. The
report may be edited in place to say "five exposures" and to drop the phrase
about a cut on the connections page; neither edit touches its subject, scope or
verdict.

## Report checks

A report passes when its subject block resolves (date, paths and the
extraction's relation to them), it states independence facts and exposures,
restates the route with its quantifiers, gives a verdict on every mathematical
statement of the extraction with the verdict words in full, carries the history
sentence, and names no person, seat, session or harness. **The report passes**,
with the gaps noted here closed by the grader.

- Independence: stated by role and model, with the charge, the allowed and
  actual reading from the tree of the frozen date, the exclusions and the exposures.
- Subject: frozen by paths and date, with the extraction's cut described;
  the two inaccuracies of description found above (no line was cut from
  the connections page; four exposures announced, five listed) do not
  change what was assessed.
- Coverage: S1--S17 cover every statement of the lead and of the section
  except the third bullet of "What it does not give" ("No uniformity over
  pairs", with the exceptional set's rational members and the Hegyvári
  1991 dichotomy) and the section's Outcome paragraph; neither has its own
  verdict. Both are adjudicated under Verdicts below. The report's
  sentences reporting the problem page's Current assessment, which the
  blind reviewer could not open, are checked below under S1.
- Verdict words: refutation-failed, refuted-as-stated and proof defective;
  statement unresolved are written in full at every occurrence.
- History sentence: present, in the Subject paragraph of "Subject and
  independence".
- Names: none of a person, seat, session or harness; the model is named as
  the existing records name it.
- The checklist gives a verdict on all ten items; the three weakest steps
  are re-derived rather than paraphrased; the strongest attack is real
  (the boundary coefficients $1/511$, $192/23$, $1/193$ and the sharper
  threshold $v<p2^{L_0}$), and the grader reproduced its computations.

## Verdicts re-derived

Each verdict of the report was re-derived by the grader; "agree" records
that the grader's derivation reaches the same verdict.

**S1, the target.** Agree, refutation-failed. The Fan conversion states
Hegyvári's conjecture after its display (1.9) exactly as the lead does and
records his proved case as "exactly one of $\alpha,\beta$ is a dyadic
rational"; the dyadic rationals with $0$ form $\mathbb Z[1/2]$, so the
Bézout remark holds; multiplying one coefficient by a nonnegative power of
$2$ passes to a subset. The reporting sentences the reviewer left to the
grader check against the problem page: its Status paragraph records the
first question answered yes on the Lean proof accepted by the bounty site,
its quoted commentary attributes the one-dyadic case to Hegyvári 1989,
which the page lists as not held and site-attested, and its remaining gap
(5) says the rational-ratio cases are untouched by every 2026 source.

**S2, the inventory of irrationality.** Agree, refutation-failed. Items
1--3 of the normalization page exclude only $2^k\alpha_0/\beta_0=1$; items
4 and 6 use $N<M<2N$, $N\ge2$; item 5 uses that the conversions are not
eventually zero, which fails exactly for two dyadic rationals. Theorem
5.1's Steps 1--5 use $\gcd(p,q)=1$, $q<p<2q$, $S_n<d(p+q)$, the interlacing
and the certificate table; the grader re-derived them and checked the
source's Section 3 (the same $K_*=2q(p-1)+4(p+q)+64$ and hypotheses) and
(5.2). Only (5.2) brings in the layer index.

**S3, Lemma 354.1.** Agree, refutation-failed. Conversions vanishing from
$n_0$ on give $\alpha=a_{n_0}2^{-n_0}$, $\beta=b_{n_0}2^{-n_0}$; Step 2 of
the theorem page consumes Theorem 5.1, (5.2), infinitely many events and
incompleteness (for $h\ge2$), and the bound $m<3n'+C_M\le4n$ for
$n\ge\max(t_1,C_M)$ gives the event in $(n,4n]$.

**S4, Proposition 354.2.** Agree, refutation-failed. (ii)
$\delta_s=-q\{2^s\alpha\}+p\{2^s\beta\}$ and $|\delta_s|<p2^{-L'}\le1$ on a
common run of length $L'\ge\log_2p$; (iii) $p\{2^s\gamma\}<2^{-L_0}$ with
$L_0=L-\lceil\log_2p\rceil$, and $L_0>\log_2p$ since $K_*>4p$; (iv) the
maximal run's start is exact, $\ell=L'+1$, $K=2^{L'+1}\ge2^{\lceil\log_2
K_*\rceil}\ge K_*$, bound from $t\ge s'+L'+4$; (v) infinitely many maximal
runs and a strictly decreasing integer sequence bounded below by $2$. The
equivalence "exact iff $\{2^s\gamma\}<1/p$" follows from
$\delta_s=q\lfloor px\rfloor-p\lfloor qx\rfloor$ and $\gcd(p,q)=1$.

**S5, Corollary 354.3.** Agree, refutation-failed. The normalized pair's
$\gamma$ is $2^v\gamma$, a shift; Borel's theorem is the lead's named
import; normal numbers are irrational and contain every block infinitely
often.

**S6, the constants.** Agree, refutation-failed: $K_*=92,132,120$;
$\lceil\log_2K_*\rceil=7,8,7$; $L=8,10,9$; $2^{\lceil\log_2K_*\rceil}=128$
at ratio $3/2$ and $256$ at $5/4$.

**S7, Lemma 354.4.** Agree, refutation-failed, including the remark that
"the mesh lemma with gap $1$" is loose by one: $b_n$ consecutive integers
have span $b_n-1$, and the proof's count argument, adjoining $c_j\le
\Lambda_j$ to get $\Lambda_j+c_j$ consecutive integers with
$\Lambda_{j+1}\ge2c_j\ge c_{j+1}$, needs no lemma. The digit-budget page's
Step 4 applies the lemma with an interval of width exceeding the next
weight, as the report says.

**S8, the pinned certificates.** Agree, refutation-failed; recomputed
exactly: $(48/5,32/5)$ ($N=6$, $M=9$) at depth $9$ from $1423$ with
$b_9=3276$; $(48/7,32/7)$ ($4$, $6$): $9$, $577$, $2340$; $(80/9,64/9)$
($7$, $8$): $7$, $445$, $910$; $(6\sqrt2,4\sqrt2)$ ($5$, $8$): $7$, $183$,
$724$; $(5\sqrt2,3\sqrt2)$ ($4$, $7$): $3$, $18$, $33$; each the least
depth and least start.

**S9, the sweep.** Agree, refutation-failed: thirty-two denominators,
twenty-nine certified by depth $9$, greatest depth $12$; $d=23$ with
$T=6$ at depth $10$ from $2139$, $b_{10}=5698$; $d=89$ with $T=8$ at depth
$12$ from $11036$, $b_{12}=23563$; $d=91$ with $T=8$ at depth $11$ from
$4323$, $b_{11}=11522$.

**S10, the controls.** Agree, refutation-failed: $(\sqrt{50},\sqrt{20})$
($N=4$, $M=7$) certifies at depth $6$ from $77$ with $b_6=286$; $(5/2,5)$
has no certificate to depth $16$, and its subset sums are $\equiv0,2
\pmod5$, so none at any depth.

**S11, "outside every held source".** Agree, refutation-failed within the
read set: the Yu--Chen theorem and the accepted Lean statement require an
irrational ratio, the other Lean proof concerns base $\sqrt\varphi$, Fan
proves no two-ray completeness, Hegyvári 1991 gives the measure dichotomy
and a finite completeness criterion, Hegyvári 1994 incompleteness and
typicality results; none covers a rational ratio with two non-dyadic
coefficients.

**S12, "outside Corollary 354.3".** Agree: refutation-failed for the
thirty-five rational pairs (zero runs of $2$, $2$, $3$ for $16/5$, $16/7$,
$16/9$ and at most $6$ for every $1/d$ of the sweep, against $8$, $8$,
$10$ and $8$ required), and proof defective; statement unresolved for the
two square-root pairs, since whether $2\sqrt2$ has infinitely many runs of
eight zeros, or $\sqrt2$ of nine, is open. The grader extends the finding:
the connections page's consequence clause "so none of these pairs is
covered by Proposition 354.2" draws non-coverage from "not known to have"
and shares the lead's defect for those two pairs; the report read that
sentence as supported on the strength of its premise clause. The companion
edit is part of R1 below.

**S13, the gap paragraph.** Agree: refuted-as-stated under the literal
reading and correct with "at least". Recomputed for $\gamma=1/511$ at
ratio $3/2$, normalized $(1536/511,1024/511)$ with $N=2$, $M=3$: the
conversions vanish on $[9j,9j+6]$ and are $(1,1),(1,0)$ at $9j+7$, $9j+8$,
so every maximal common zero run has length exactly $7$, each starts at
an exact layer ($\delta=0$), $h_n=0$ for $n\le20$ and a certificate
exists at depth $2$; the literal sentence, asking for maximal runs of
length exactly $6$, puts $1/511$ in the gap set that the same paragraph
says Corollary 354.3 covers. The paragraph's other claims agree:
$\gamma=24/7$ has $\{2^s\gamma\}\in\{3/7,6/7,5/7\}$ and $\delta_s=2,1,1$;
a common run of length at least $L_0$ at an exact layer forces
$p\{2^s\gamma\}<2^{-L_0}$, hence $\{2^s\gamma\}<2^{-(L_0+1)}$; a rational
$\gamma$ with odd denominator part $v$ has $\{2^s\gamma\}\ge1/v$ for large
$s$, so $v\le128$ at ratio $3/2$ is excluded, which covers $v=5,7,9$ and
every $d\le99$; uncountably many irrationals have no run of seven zeros.

**S14, the two obstructions.** Agree, refutation-failed. A reduced
$p'/q'\ne p/q$ has $|p/q-p'/q'|\ge1/(qq')$, so good denominators are
$<q$ apart from $q$ itself; (DB) and $D(b)$ for $b>q$ are unavailable.
With $2^J\le p<2^{J+1}$, $p/2^J$ and $q/2^J$ are sums of at most $k$
elements of $\mathcal A$ and $q/2^J>1/2$, so $p/q\in\mathcal C_k$. The
witness: for $x=\{2^s\gamma\}\in[1/4,1/3)$ the conversions are $(1,1)$,
$(1,0)$, $\delta_s=0$, $\delta_{s+1}=-1$ and
$\delta_{s+2}=4\delta_s+2\cdot3-3\cdot2=0$, two events per return (checked
at $x=1/4$, $5/18$, $3/10$, $33/100$). Under bounded spacing (FE) bounds
the missing count by
$C_02^ne^{-aK_n}$ with $K_n\gg\log n$, a polynomially small fraction.

**S15, "pair by pair certifiable but not uniformly proved".** Agree,
refutation-failed as a statement about this route.

**S16, the next step.** Agree. $a_{n+i}=\lfloor2^i(a_n+\{2^n\alpha\})
\rfloor=2^ia_n+\lfloor2^i\{2^n\alpha\}\rfloor$, so $r_i$ has binary digits
$u_n,\ldots,u_{n+i-1}$ and grows with $i$; the digits, not $r_i$, are
eventually periodic. "Each positive case is a proved instance" is
refutation-failed through Lemma 354.4; the outcome sentences are plans.

**S17, "Provisional premises".** Agree, refutation-failed for the Borel
sentence; the section names none of the reconstruction inputs the route
consumes (S1 below).

**The third bullet, not covered by the report.** Grader's verdict:
refutation-failed. For a rational $\gamma$ with odd denominator part $v$
and $s$ past the $2$-adic part of the denominator, $\{2^s\gamma\}$ is a
nonzero multiple of $1/v$, so a run of $L$ zeros from position $s$, which
needs $\{2^s\gamma\}<2^{-L}$, requires $v>2^L$; with $v\le2^{L(p,q)}$ the
runs of $L(p,q)$ zeros are finitely many and $\gamma$ lies in the
corollary's exceptional set, as the bullet says ($v=5,7,99$ at $L=8$ and
$v=9$ at $L=10$ excluded; $v=511$ and $257$ not, consistent with $1/511$
being covered). The held Hegyvári 1991 card records the theorem the
bullet names, that for fixed $\alpha$ the incomplete $\beta$ form a
measurable set of measure $0$ or $\infty$, and the page neither uses nor
sharpens it. The Outcome paragraph is a list of the transfers, consistent
with S3--S9 and S13--S14, its "every non-dyadic normalized pair" read
against the hypothesis of Lemma 354.1.

**Weakest steps and strongest attack.** W1--W3 agree with the grader's
derivations; the certificate lemma holds under the grader's own check of
the Appendix A table. The attack's figures reproduce: $(1536/511,
1024/511)$ with runs on $[0,6]$, $[9,15]$, $h_n=0$, certificate at depth
$2$; $(192/23,128/23)$ with $h_n=0,0,2,2,0,1,1,1,0,\ldots$, no common
zero run longer than $2$ through index $29$, certificate at depth $10$;
$\gamma=1/193$ with $2$ of order $96$ modulo $193$, exact layers at
$s\equiv88\pmod{96}$ preceded by the conversion $(1,0)$ and followed by a
common zero run of length exactly $6=L_0$, longest zero run $7<8$, and a
certificate for $(768/193,512/193)$ at depth $5$. N1's threshold
$v<p2^{L_0}$ ($v\le191$ at $3/2$, $v\le639$ at $5/4$) is right and
implies the page's bound.

## Corrections

Each correction was adjudicated against the extraction and, where a source or a
computation decides it, against the held text or the grader's exact
recomputation. Locations quote the extraction, which is the committed text of
that date.

**R1 (required).** Accepted, with the text sharpened and extended. Lead,
"Route and established inputs", fourth bullet: replace "all outside every
held source and outside Corollary 354.3." with

"all outside every held source, and none of them known to be covered by
Corollary 354.3: the rational coefficients have no zero run of the
required length, and $\sqrt2$ is not known to have infinitely many."

Connections page, paragraph after the proof of Lemma 354.4: replace "so
none of these pairs is covered by Proposition 354.2;" with "so none of
these pairs is known to be covered by Proposition 354.2;". Basis: the
rational pairs are excluded by their zero runs (S12); for the two
square-root pairs the claim of exclusion is an open statement about
$\sqrt2$, and the reviewer's proposed text, "none covered by Corollary
354.3", still asserted the exclusion before explaining it as unknown.

**R2 (required).** Accepted as proposed. Lead, "The consequential gap",
first sentence: replace "Coefficients $\gamma$ with only finitely many
maximal common zero runs of length $\lceil\log_2K_*\rceil-1$ at exact
layers:" with "Coefficients $\gamma$ with only finitely many maximal
common zero runs of length at least $\lceil\log_2K_*\rceil-1$ at exact
layers:". Basis: S13; the connections page's own first bullet carries "at
least".

**S1 (suggested).** Accepted with the standing clause replaced. Lead,
"Provisional premises", after the first sentence add:

"The transport imports items 1--6 and the reduction of the normalization
page, Lemmas 2.1--2.3, Theorem 5.1 with the Appendix A certificate (finite
data rechecked by the folder's evidence) and Step 2 of the theorem page,
each at the standing its own page records; Lemma 354.4 and the
certificates rest on the normalization page alone."

The reviewer's clause "as author-recorded reconstructions of an
unrefereed manuscript" is not landed: it would make the lead carry a
standing claim about other pages, which the lead does not maintain and
which this grade, whose assignment excludes standing text, cannot
adjudicate; the inventory itself is right (S2, S7).

**S2 (suggested).** Accepted. Connections page, paragraph after the proof
of Lemma 354.4, first sentence, keeping its two wiki-links: replace "This
is the mesh lemma of the Lemma 2.2 page with gap $1$, as the digit-budget
page uses it, and it turns completeness of one pair into a finite
computation." with

"This is the abutting case of the mesh lemma of the Lemma 2.2 page with
gap $1$: the $b_n$ consecutive integers have span $b_n-1$, one short of
the lemma's hypothesis, which the count argument above replaces, while the
digit-budget page applies the lemma with span at least the next weight;
it turns completeness of one pair into a finite computation."

Basis: S7; the digit-budget page's Step 4 applies the consequence of the
mesh lemma from an interval whose width exceeds $b_{n+k}$.

**S3 (suggested).** Accepted for both pages. Lead, "Next step", first
sentence: replace "with a periodic correction $r_i$" with "with the
correction $r_i=\lfloor2^i\{2^n\alpha\}\rfloor$, the integer whose binary
digits are the eventually periodic conversions". Connections page, "Next
investigation", first direction: the same replacement. Basis: S16.

**S4 (suggested).** Accepted. Lead, "Target and status evidence": replace
"as Hegyvári's (site-attested, paper not held)" with "as Hegyvári's
(site-attested, paper not held; Fan's preprint, held, records it as his
on p. 4)". Basis: the Fan PDF text layer places the sentence "confirmed
the case where exactly one of $\alpha,\beta$ is a dyadic rational" on the
page headed 4, and the canonical conversion carries it after (1.9).

**Notes N1--N5.** No correction is required by any of them. N1 (the
mechanism reaches further than the corollary's hypothesis; $v<p2^{L_0}$)
and N3 (a period, not the least) are right and are observations; N2 is
right by the held card (Lemma 1 of Hegyvári 1991 is a finite completeness
criterion for the same sets), and the author may cite it beside Lemma
354.4 at will; N4 and N5 are right.

**Rejected.** Nothing is rejected outright; the one rejected clause is
S1's standing characterization, replaced as stated above.

## Outcome

- [[research/leads/rational_ratio_dyadic_floor_descent/_index|rational_ratio_dyadic_floor_descent]]:
  **reviewed**, once R1 and R2 and the accepted suggested texts are
  landed. Every statement the route rests on is refutation-failed under
  the report and the grader's re-derivation: Lemma 354.1, Proposition
  354.2, Corollary 354.3 with Borel's theorem as its explicitly imported
  premise, Lemma 354.4 and the certificate figures of all thirty-nine
  pairs; the reconstruction
  inputs the transport consumes were re-derived by both reviewer and
  grader at the deductions consumed and are named, with their own pages
  carrying their standing, by the landed S1. The two findings, R1 and R2,
  are wording defects outside the route's load-bearing statements, and
  the lead's conclusion, that Hegyvári's conjecture stays open on this
  route for the gap coefficients, pair by pair certifiable and not
  uniformly proved, stands.
- research_state: **ready**. The body names two bounded next
  investigations with their inputs in the folder: the periodic-block
  analog of Step 1 and Step 4 of the Theorem 5.1 page, with the stated
  positive and negative outcomes, and the exact certificate search, whose
  entry point runs in seconds and whose each positive case is a proved
  instance by Lemma 354.4. No prerequisite is missing and nothing is
  deferred or closed.

No tier is assigned and no status changes.
