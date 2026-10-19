---
name: research/erdos_49/evidence/verify/connections_problems_850_and_931_pairs_with_the_same_prime_f_review
title: "Independent review of the connections section: Problems 850 and 931: pairs with the same prime factors"
desc: |
  Refutation-failed for the transported per-difference bound and for both
  stated obstructions; the target paraphrases and the corpus-state sentence
  are not claims. One required correction: the section quotes Lemma 3.2
  over integers j where it is stated for natural numbers j and applies it
  without fixing the sign convention. Two suggested rewordings, four notes.
created: 2026-09-28T18:21:14Z
updated: 2026-09-28T18:21:14Z
---

***

## Subject and independence

Role: independent reviewer in a fresh context, given only this assignment,
with no part in writing the connections page or the reconstruction pages;
the section's author, the reviewers of the reconstruction pages and their
grader are other roles. Charge: refutation of the author-recorded
mathematics of one section.

Subject: page `wiki/research/erdos_49/connections.md` as it stood on
2026-09-28T13:50:48Z ([[research/erdos_49/connections|the connections page]]),
section "Problems 850 and 931: pairs with the same prime factors", lines
599--625 (the heading is line 599; the next H2 is line 626). No lead page is
named for this section; the page's preamble names leads only for Problems 1004
and 417.

Reading: the section in full; the page's opening, standing and outcomes
paragraphs (lines 1--57) and its "Notation and the inputs used" (lines
58--111) as inputs; the Lemma 3.2 reconstruction page in full as a premise;
the Statement portions of the two problem pages, through their References
and Formalization entries; the source card's provenance and read-status
paragraphs and the held manuscript PDF, pp. 5--7 on the text layer
(Theorem A, Lemma 3.2 with its proof, Theorem 3.3 and the start of its
proof); `docs/verification.md` "Grading and claim standing", "Audit
checklist -- the canonical failure modes", "Whole-claim report" and "Audit
checklist"; `docs/approach_vetting.md` and `docs/math_authoring.md` in
full; `docs/evidence.md` "Source fidelity".

Exposures: (1) the range read that fetched the section also displayed the
following section, "Problem 49: the remaining clause" (lines 626--641),
which was not used; (2) the source card was displayed whole, so its
Contents and "Relation to E49" sections were seen; they concern Problem 49
and say nothing about Problems 850 or 931; (3) the H2 heading lists and the
frontmatter `status:` lines of the two problem pages were displayed to
locate their Statement portions; the content of their Current assessment,
Progress, Known Results and Linked library material sections was not read;
(4) the page's list of H2 headings. No folder index, no evidence folder
content, no review or grade, no other reconstruction page and no web search
reached this review.

## Restatement

Throughout, $\gamma(n)$ is the product of the distinct primes dividing $n$,
$\omega(n)$ is their number, and for a natural number $k$
$J_k=\{j\in\mathbb N:\gamma(j)=\gamma(j+k)\}$ and
$B(k)=3\cdot7^{3+2\omega(k)}$. Two nonzero integers have the same prime
factors exactly when their radicals agree, the radical of a negative
integer being that of its absolute value.

- **S1** (target paraphrase, Problem 850). The corpus Statement asks
  whether there exist two distinct integers $x,y$ such that $x+i$ and
  $y+i$ have the same prime factors for each of $i=0,1,2$. The section's
  paraphrase keeps "distinct integers" and the three pairs. Descriptive.
- **S2** (target paraphrase, Problem 931). The corpus Statement fixes
  lengths $k_1\ge k_2\ge3$ and asks whether only finitely many
  $n_2\ge n_1+k_1$ make $\prod_{i=1}^{k_1}(n_1+i)$ and
  $\prod_{j=1}^{k_2}(n_2+j)$ have the same prime factors. The section's
  paraphrase, "two disjoint products of at least three consecutive
  integers ... only finitely often", does not say that the lengths are
  fixed first. Descriptive.
- **S3** (corpus state). "Both corpus pages are open and not compiled
  beyond the statement." Not mathematics.
- **S4** (quoted lemma). For each $k$, at most $B(k)$ integers $j$ have
  $\gamma(j)=\gamma(j+k)$. The premise states this for natural numbers $j$
  and natural numbers $k$.
- **S5** (transfer). With $k=y-x$, each of the three conditions of Problem
  850 places $j=x,x+1,x+2$ in $J_k$; hence for each fixed $k$ the number of
  candidates $x$ is finite and at most $B(k)$, a bound depending on $k$
  only through $\omega(k)$.
- **S6** (obstruction, Problem 850). S5 gives neither existence nor
  nonexistence: "the union over all $k$ is unbounded", and the lemma
  bounds $|J_k|$ without constraining whether some $J_k$ contains three
  consecutive integers.
- **S7** (obstruction, Problem 931). Nothing transports: the objects are
  pairs of block products with no fixed difference, "so the lemma's
  hypothesis is not even met".
- **S8** (assessment). Evertse's bound is a standard input for such
  problems and the transported statement adds nothing to it. Not
  mathematics.
- **S9** (outcome). "Fails": nothing bearing on either question transfers,
  in agreement with the page's "Outcomes at a glance".

## Checklist

- **Quantifiers and scope: defect (F1).** S4 quotes the lemma over
  integers $j$ where the premise and the source state it for natural
  numbers $j$; S5 fixes neither $x<y$ nor the sign of $x$, while the
  target's Statement says "integers". The bound survives both readings
  (Weakest steps, 1), but the text's warrant, the lemma as stated, covers
  only natural $j$. The referent of "the union over all $k$" in S6 is
  also unnamed (F2).
- **Circularity: clear.** The transfer is a one-step specialization of an
  external lemma.
- **Model and convention changes: clear, with a convention to fix (F1).**
  "Same prime factors" and equal radicals are the same condition on
  nonzero integers, so the section's identification is exact; the
  convention for entries $0$ and $\pm1$ has to be fixed under the integer
  reading. The Problem 931 paraphrase drops the fixed lengths (F4).
- **Finite and statistical overreach: clear.** The section declines to
  infer existence or nonexistence from per-difference finiteness.
- **Uniformity: clear.** The transported bound is explicit and depends on
  $k$ only through $\omega(k)$; no hidden dependence and no further
  uniformity is claimed.
- **Extremal conclusions: inapplicable.** None claimed.
- **Consequences and composition: one imprecise reason (F3).** The "so" of
  S5 is re-derived below and holds. The "not even met" of S7 is
  imprecise: every single pair of distinct natural numbers with equal
  radicals meets the lemma's hypothesis at their own difference; what
  Problem 931 lacks is one difference across the family.
- **Computation: inapplicable.** The section contains none. The exact
  checks in this report are the reviewer's own derivations, each
  hand-checkable.
- **Reproduction: inapplicable.** The section states no rerun line and no
  coverage.
- **Source and verdict fidelity: defect (F1); notes (F5, F7).** Lemma 3.2
  was checked against the reconstruction and against manuscript p. 6:
  both count natural numbers $j$, and the section's "integers $j$" widens
  the domain. The section claims nothing beyond the page's author-recorded
  standing. S8's "standard input" is a literature characterization outside
  the commissioned read set; S3's compilation clause was not checked.

## Weakest steps

**1. Lemma 3.2 applied to Problem 850 (S4 to S5).** Let $k\ge1$ and let
$j$ be an integer with $j\ne0$, $j\ne-k$ and $\gamma(|j|)=\gamma(|j+k|)$.
A prime dividing $j$ divides $j+k$ and hence $k$; the same for a prime
dividing $j+k$. With $S$ the infinite place together with the primes
dividing $k$, the rationals $u=(j+k)/k$ and $v=-j/k$ are nonzero
$S$-units with $u+v=1$, and $j=-kv$ recovers $j$, so distinct $j$ give
distinct solutions. Evertse's count is over all solutions in $S$-units,
of either sign, so the number of such $j$ is at most
$3\cdot7^{1+2(1+\omega(k))}=B(k)$. For $j\ge1$ this is the lemma; for
$j\le-k-1$ and for $-k<j<0$ the same injection applies, so the bound holds
over all integers $j\notin\{0,-k\}$. The sets differ: for $k=6$ the
natural solutions are $2,3,6,12,18,48$ and the further integer solutions
are $-54,-24,-18,-12,-9,-8,-4,-3,-2$ (the first six are the reflections
$j\mapsto-j-6$ of the natural ones; the last three have $j$ and $j+6$ of
opposite sign); for $k=2$ they are $2$ and $-4,-1$.

Now let $x\ne y$ be integers satisfying the three conditions. The
conditions are symmetric in $x,y$, so take $x<y$ and $k=y-x\ge1$. If some
entry $x+i$ or $y+i$ lies in $\{0,\pm1\}$, a check of the cases shows that
either $x=y$ or one of the three pairs compares an element of $\{0,\pm1\}$
with an element of $\{\pm2\}$, whose prime factors differ under either
convention for $0$; so all six entries lie outside $\{0,\pm1\}$, and
$x+i\notin\{0,-k\}$ with $\gamma(|x+i|)=\gamma(|x+i+k|)$ for $i=0,1,2$.
Hence the number of $x$ for fixed $k$ is at most $B(k)$. For positive $x$
this is the lemma as stated; for the literal integer reading it is the
lemma's proof, not its statement. Either way S5 holds, and "boundedly many
in terms of $\omega(k)$" is exact. In passing, $k$ must be even ($j$ and
$j+k$ of opposite parity cannot share their primes) and $3\mid k$ (one of
$x,x+1,x+2$ is a multiple of $3$), so $6\mid k$; the section does not use
this.

**2. The Problem 931 obstruction (S7).** For one pair $A\ne B$ of natural
numbers with $\gamma(A)=\gamma(B)$, the lemma with $k=|B-A|$ says that
$\min(A,B)$ is one of at most $B(k)$ natural numbers $j$ with
$\gamma(j)=\gamma(j+k)$: true and empty for a single pair. A finiteness
statement for Problem 931 would need control across pairs of block
products whose differences vary without bound, and nothing in the lemma
relates the differences of different pairs; nor does the condition on the
products imply any factor-wise condition at the fixed difference
$n_2-n_1$. The obstruction stands; only the sentence's reason is imprecise
(F3).

**3. The "union unbounded" clause (S6).** Every $j\ge2$ lies in some
$J_k$: choose a prime $p\mid j$ and $k=j(p-1)$, so $j+k=jp$ and
$\gamma(jp)=\gamma(j)$. So $\bigcup_kJ_k=\{2,3,4,\ldots\}$ and no
per-difference count can exclude a solution. Sharper: the two-condition
analog has infinitely many solutions, $x=2^n-2$ and $y=2^nx$ for $n\ge2$,
the family recorded from Guy's section B29 in the E0850 reference list:
$y=2^nx$ with $x$ even gives $\gamma(y)=\gamma(x)$, and
$y+1=2^{2n}-2^{n+1}+1=(2^n-1)^2=(x+1)^2$ gives $\gamma(y+1)=\gamma(x+1)$,
while $y+2=2(2^{2n-1}-2^n+1)$ has an odd factor exceeding $1$, so the
third condition fails. Hand-checked for $n=2,\ldots,7$: $(2,8)$, $(6,48)$,
$(14,224)$, $(30,960)$, $(62,3968)$, $(126,16128)$. Thus $J_k$ contains
two consecutive integers for infinitely many $k$, and a bound on $|J_k|$
says nothing about whether some $J_k$ contains three. No pair $x<y<3000$
satisfies all three conditions, by an exhaustive exact check. The clause
itself has an unnamed referent: read as the union of the sets the lemma
bounds, it is the true statement above; read as the union of the sets of
solutions at each difference, it would assert that Problem 850 has
infinitely many solutions, which is open (F2).

## Strongest attack

- **S4 and S5.** The attack was to break the bound on the widened domain
  the section quotes, integers $j$, where the count is visibly larger than
  the lemma's ($15$ against $6$ for $k=6$). It fails because the lemma's
  injection into $S$-unit solutions covers every integer $j\notin\{0,-k\}$,
  so Evertse's constant is unchanged; only the attribution to Lemma 3.2 is
  inexact. The second attack, $x>y$ making $k$ negative and the entries
  $0,\pm1$ breaking the radical convention, fails by the symmetry and the
  case check in Weakest steps 1. A refutation would need a $k$ with more
  than $B(k)$ solutions, which Evertse's theorem excludes.
- **S6.** The attack was to extract a nonexistence proof from the lemma's
  consequence, fewer than $k^\epsilon$ elements of $J_k$ for large $k$,
  together with $6\mid k$. It fails: a set of fewer than $k^\epsilon$
  natural numbers can contain three consecutive ones, and the lemma
  controls size, not structure. An existence proof cannot come from an
  upper bound. The two-condition family shows that the interaction of the
  conditions is where the content lies, as the section says. The strongest
  reading of "the union over all $k$ is unbounded" is an open assertion;
  the weaker reading is what the argument needs (F2).
- **S7.** The attack was to find a fixed difference in Problem 931: the
  difference of the two products is a polynomial in $n_1,n_2$ that is
  unbounded for fixed lengths, and a factor-wise reduction is not implied
  by a condition on the products. Guy's example on the E0931 page,
  $2\cdot3\cdots10=3628800$ and $14\cdot15\cdot16=3360$, with prime factors
  $\{2,3,5,7\}$, has difference
  $3625440=2^5\cdot3\cdot5\cdot7\cdot13\cdot83$, so the lemma bounds the
  pairs at that difference by $3\cdot7^{15}$, a statement about a family
  the problem does not ask about. The obstruction holds.
- **S9.** "Fails" was attacked as inconsistent with a recorded transfer.
  It is consistent with the page's vocabulary, under which the outcome
  records whether anything bears on the target's question; S5 bears on
  neither question.

## Premises

- [[research/erdos_49/lemma_3_2_reconstruction|Lemma 3.2 reconstruction]] in the
  subject state. Interface: for each natural number $k$, the number of natural
  numbers $j$ with $\gamma(j)=\gamma(j+k)$ is at most $3\cdot7^{3+2\omega(k)}$;
  consequently fewer than $k^\epsilon$ for $k>k_0(\epsilon)$. Standing per the
  commission: independently reviewed as it stood on 2026-09-28T05:03:27Z with
  corrections applied since; taken as established at that standing; read in
  full. The section consumes it outside its stated domain (F1).
- Pollack, Pomerance and Treviño, *Sets of monotonicity for Euler's
  totient function*, Lemma 3.2, p. 6 of the held author manuscript on
  [[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/_index|its card]];
  pp. 5--7 read on the text layer. The statement there counts natural
  numbers $j$ and matches the reconstruction; its proof is the injection
  used above.
- Evertse, *On equations in $S$-units and the Thue--Mahler equation*,
  Invent. Math. 75 (1984), Theorem 1: not held; imported at the interface
  the reconstruction records, at most $3\cdot7^{1+2\#S}$ solutions of
  $u+v=1$ in $S$-units of the rationals with $S$ containing the infinite
  place; not verified here; used only to note that the same injection
  covers integer $j$.
- [[problems/primes/E0850/_index|Problem 850]] and
  [[problems/diophantine_problems/E0931/_index|Problem 931]], Statement portions read
  in the subject state. The Guy 2004 entries in their reference lists supplied
  the two-condition family and the block example used as witnesses; both were
  verified by hand arithmetic, and the held Guy PDF was not opened.
- The connections page's opening, standing, outcomes and Notation
  sections, read as inputs; they define neither $\gamma$ nor $\omega$
  (F6).

## Findings

- **F1** (required). Location, lines 609--612: "Lemma 3.2 says that for
  each $k$ at most $3\cdot7^{3+2\omega(k)}$ integers $j$ have
  $\gamma(j)=\gamma(j+k)$. With $k=y-x$, each of the three conditions of
  Problem 850 says that $(j,j+k)$ is such a pair for $j=x,x+1,x+2$".
  Defect: the lemma, in the reconstruction and in the source, counts
  natural numbers $j$; the quotation widens the domain to integers, and
  the application then rests on the widened form, since the target's
  Statement says "integers" and the section fixes neither $x<y$ nor
  $x\ge1$. Witness: for $k=6$ the natural solutions are $2,3,6,12,18,48$
  while the integer solutions add $-54,-24,-18,-12,-9,-8,-4,-3,-2$; the
  two statements count different sets. The widened statement is true with
  the same constant by the lemma's own injection (Weakest steps 1), but
  that is a derivation the page does not give and the lemma does not
  state. Replacement: "Lemma 3.2 says that for each natural number $k$ at
  most $3\cdot7^{3+2\omega(k)}$ natural numbers $j$ have
  $\gamma(j)=\gamma(j+k)$. Take $x<y$, the conditions being symmetric, and
  $k=y-x\ge1$; for positive $x$ each of the three conditions says that
  $j=x,x+1,x+2$ is such a $j$. Under the Statement's literal reading over
  all integers the same bound holds, because an entry $0$ or $\pm1$ forces
  $x=y$ or a failing pair, and the lemma's injection
  $j\mapsto((j+k)/k,-j/k)$ counts every integer $j\notin\{0,-k\}$ with
  $\gamma(|j|)=\gamma(|j+k|)$. So for each fixed difference $k$ there are
  at most $3\cdot7^{3+2\omega(k)}$ candidates $x$, boundedly many in terms
  of $\omega(k)$."
- **F2** (suggested). Location, lines 615--616: "Existence or
  nonexistence: the union over all $k$ is unbounded". Defect: the set
  whose union is taken is unnamed. Read as the union of the sets the lemma
  bounds, the sentence is true (every $j\ge2$ lies in some $J_k$) and
  explains why no finiteness follows; read as the union of the solution
  sets of Problem 850 at each difference, it asserts that the problem has
  infinitely many solutions, which is open. Witness: no solution exists
  with $x<y<3000$. Replacement: "Existence or nonexistence: the sets the
  lemma bounds are finite at each $k$ but their union over $k$ is
  infinite, so no total finiteness follows, and the lemma counts pairs at
  one difference ...".
- **F3** (suggested). Location, lines 618--620: "For Problem 931 the
  objects are products of blocks, not pairs at a fixed difference, so the
  lemma's hypothesis is not even met." Defect: the reason is imprecise;
  any pair of distinct natural numbers with equal radicals meets the
  lemma's hypothesis at its own difference, and what the family lacks is
  one difference shared by its members. Witness: Guy's example
  $2\cdot3\cdots10$ and $14\cdot15\cdot16$ on the E0931 page, to which the
  lemma applies at the difference $3625440$ with the bound $3\cdot7^{15}$,
  a statement about a family the problem does not ask about. Replacement:
  "For Problem 931 the two products have no fixed difference across the
  family, so the lemma, which counts pairs at one difference, bounds
  nothing there."
- **F4** (note). Location, lines 604--606: the paraphrase of Problem 931
  omits that the lengths $k_1\ge k_2\ge3$ are fixed before finiteness is
  asked; "products of at least three consecutive integers ... only
  finitely often" reads as finiteness over all lengths, a stronger
  question. Not load-bearing, since nothing transfers. Replacement: "asks
  whether, for fixed block lengths $k_1\ge k_2\ge3$, only finitely many
  pairs of disjoint blocks have products with the same prime factors."
- **F5** (note). Location, lines 606--607: "Both corpus pages are open and
  not compiled beyond the statement." A corpus-state sentence outside the
  mathematical charge. Both pages carry `status: open`; the compilation
  clause was not checked, because the pages' later sections are excluded
  from this review, and both pages carry sections named Current
  assessment, Progress, Known Results and Linked library material in the subject
  state. The integrator can check it.
- **F6** (note). The section uses $\gamma$ and $\omega$, which the page's
  Notation section does not define; they are defined on the Lemma 3.2
  page. One clause in Notation would close the gap.
- **F7** (note). Location, lines 620--622: "is a standard input for such
  problems" is a literature characterization not checkable within the
  commissioned read set; it carries no deduction.

## Verdict

- S1: not a claim; the paraphrase is faithful to the Statement.
- S2: not a claim; the paraphrase drops the fixed lengths (F4).
- S3: not a claim; the compilation clause is unverified (F5).
- S4: refutation-failed. The statement survives even on the widened domain
  the section quotes; the quotation of Lemma 3.2 is inexact (F1).
- S5: refutation-failed. The per-difference bound holds for positive $x<y$
  from the lemma as stated and for the literal integer reading from the
  lemma's proof; the convention must be written down (F1).
- S6: refutation-failed. The per-difference bound decides neither
  existence nor nonexistence, and the two-condition family shows why; the
  union sentence should name its set (F2).
- S7: refutation-failed. Nothing transports to Problem 931; the sentence's
  reason should be reworded (F3).
- S8: not a claim.
- S9: refutation-failed. "Fails" is consistent with the page's outcome
  vocabulary.

Limitations: Evertse's theorem is not held and enters only at the
interface the premise records; the corpus-state sentence S3 was not
checked; the page's other sections and the reconstruction pages other than
Lemma 3.2 were not read, and the preamble and Notation were consumed only
as inputs. This focused review assigns no tier and changes no status.
