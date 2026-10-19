---
name: research/erdos_939/evidence/verify/connections_other_powerful_number_problems_examined_review
title: "Independent review of the connections section: Other powerful-number problems examined"
desc: |
  Refutation-failed for the five exact statements of the section (Theorem 3
  with a constant term, the mixed 2/3 case for Problem 366, the absence of
  polynomial families of consecutive powerful numbers, the Pell consistency
  remark, and the r = 2 Pythagorean remark for Problem 943); the remaining
  sentences are scoping remarks and not claims. Zero required corrections,
  one suggested quantifier sharpening, three notes.
created: 2026-09-28T18:48:36Z
updated: 2026-09-28T18:48:36Z
---

***

## Subject and independence

**Role.** The reviewer is an independent reviewer in a fresh context, given
only the commissioning assignment, who took no part in writing the page, its
shared results, the reconstruction page, or any lead folder, and who read no
existing review or grade of this folder. The charge is refutation of the
author-recorded mathematics of one section.

**Subject.** Page `wiki/research/erdos_939/connections.md` as it stood on
2026-09-28T13:50:48Z, section
"## Other powerful-number problems examined", lines 517–560 (the H2 at line
517, content at lines 519–559, the next H2 "## Leads created" at line 561).
The section names no lead page; the "Leads created" section of the same page
attaches no lead folder to it.

**Reading.** Read in full: the subject section; the page's opening paragraph
and its "Conventions" paragraph (lines 17–56) and the whole "## Shared
results" section (lines 58–302: Lemma 1 with Corollary 1.1, Lemma 2, Theorem
3 with Corollary 3.1, Proposition 4 with Corollary 4.1) as inputs whose
interfaces were confirmed at each use and whose proofs another reviewer
checks; the reconstruction page
`wiki/research/erdos_939/theorem_1_reconstruction.md` in full as a premise
at its reviewed standing; the Statement paragraphs only (the text from
"**Statement.**" to the line before "**Status.**") of the thirteen problem
pages the section targets, `wiki/problems/diophantine_problems/E0364/_index.md`,
`E0365.md`, `E0366.md`, `E0938.md`, `E0943.md`, `E1081.md`, `E0941.md`,
`E0942.md`, `E0935.md`, `E0137.md`, `E0936.md`,
`wiki/problems/arithmetic_functions/E0367/_index.md` and
`wiki/problems/factorials_binomials/E1108/_index.md`; `docs/verification.md`
(Grading and claim standing, the shared and Erdos-specific Audit checklist,
Whole-claim report), `docs/approach_vetting.md` in full,
`docs/evidence.md` "Source fidelity", and `docs/math_authoring.md` in full.
The section invokes no library source theorem, so no library card, result
page, or PDF was read. The other connection sections of the page (Problem
939 at r = 4 and r = 5, the remaining parts, Problems 940, 1107 and 937)
were not read.

**Exposures.** Four, none of them a review, grade, or assessment of the
subject: (1) lines 561–585 of the page ("## Leads created" and "## Sources
read for this page") were read because the extraction ran to the end of the
file; (2) one exploratory read of `E0364.md` showed, beyond its Statement,
the frontmatter `status:` line, the references block, the "Progress" and
"Known Results" sections (both "Not yet compiled"), and the generated
library-links block; (3) `docs/verification.md` lines 639–660, the opening
of "Durable reports and current standing", were read past the named
sections; (4) a file listing of `wiki/research/erdos_939/` showed the names
of the two files under `evidence/verify/` (a reconstruction review and a
grade); neither was opened. The reconstruction page's own "Standing" and
"Boundary" paragraphs were read as part of that allowed premise page. The
status words for Problems 1081 and 941 that the section quotes were not
checked against those pages, since their status text lies outside the read
set.

## Restatement

The section's conventions are the page's: for $r\ge2$, an integer is
$r$-powerful when every prime dividing it does so to exponent at least $r$
($1$ is $r$-powerful); a nonzero $f\in\mathbb C[t]$ is $r$-powerful when every
root in an algebraic closure has multiplicity at least $r$, so constants are
$r$-powerful; "powerful" means $2$-powerful. Theorem 3 (shared) reads: for
$r\ge2$ and pairwise coprime $r$-powerful $a,b,c\in\mathbb C[t]$, not all
constant, with $a+b=c$, one has $r=2$ and none of $a,b,c$ constant; more
generally, if $a,b,c$ are $r_a$-, $r_b$-, $r_c$-powerful with all
$r_f\ge2$, the sum of $1/r_f$ over the nonconstant members exceeds $1$.

- **S0** (opening sentences). The listed pages were surfaced by a search of
  the problems, research, and theory trees for the objects of the proofs;
  each is a resemblance without a transfer of the mechanism, and where
  Theorem 3 says something exact it is stated. A process statement.
- **S1** (Problems 364, 365, 366; "Theorem 3 with a constant term"). For
  every integer $r\ge2$ there is no identity $a+1=c$ in $\mathbb C[t]$ with
  $a$ nonconstant and $a$, $c$ both $r$-powerful polynomials: such an
  identity has only two nonconstant terms, which Theorem 3 forbids.
- **S2** (Problem 366, "the mixed version"). There is no identity $a+1=c$
  in $\mathbb C[t]$ with $a$ nonconstant, $a$ $2$-powerful and $c$
  $3$-powerful, because the general clause of Theorem 3 would require
  $1/2+1/3>1$, and $1/2+1/3<1$.
- **S3** (consequence). No polynomial family of consecutive powerful
  numbers exists. Read under the page's convention for a one-parameter
  polynomial family (Corollary 3.1 and the paragraph after it): there is no
  nonconstant $a\in\mathbb Z[t]$ such that $a(t)$ and $a(t)+1$ are both
  powerful for every sufficiently large integer $t$ in some arithmetic
  progression; a fortiori no identity of powerful polynomials of that
  shape; pairs, and hence triples.
- **S4** (consistency remark). S3 is consistent with the Pell-equation
  families of Problem 365, whose members grow exponentially in their index.
- **S5** (scoping sentence). Problems 364, 365 and 366 ask for specific
  pairs and triples, which polynomial identities cannot supply.
- **S6** (Problem 938). Consecutiveness of terms in the powerful sequence is
  a gap condition; identities produce progressions (of squares) and give no
  control of gaps, so the mechanism has no transfer. A stated obstruction
  without a witness; no proof is claimed.
- **S7** (Problem 943). At $r=2$ the binomial identity of the reconstruction
  is the Pythagorean parametrization
  $(m^2+B^2)^2=(m^2-B^2)^2+(2mB)^2$; it yields representations of squares
  as sums of two squares, in number bounded by a divisor-function quantity,
  so it neither strengthens nor threatens the conjecture
  $1_A\ast1_A(n)=n^{o(1)}$ for every $n$.
- **S8** (Problems 1081 and 941). Both are settled, the first disproved and
  the second proved as the section characterizes them, and one-parameter
  families have no bearing on either.
- **S9** (Problems 942, 935, 367, 137, 936, 1108). These concern short
  intervals, consecutive products, and special sequences, none of which an
  identity among $r$-powerful values addresses. A scoping judgment.

The section contains no transfer lemma of its own and no conditional
deduction; its only exact mathematics is S1, S2, S3, S4 and S7, all
consequences of the shared results or of elementary facts.

## Checklist

- **Quantifiers and scope.** S1 is stated without the words "$a$
  nonconstant", which the phrase "only two nonconstant terms" presupposes
  (Finding F2, note; the trivial identity $1+1=2$ among constants is the
  witness for the literal reading). S3 does not carry the convention under
  which it holds: for values at infinitely many parameters it is false
  (Finding F1, suggested; witness $a(t)=8t^2$ on the Pell set). Under the
  page's convention both are correct. S7's "for every $n$" is the problem's
  quantifier and is preserved. Pass, with F1 and F2.
- **Circularity.** None. The section assumes nothing equivalent to its
  conclusions; Theorem 3 and Corollary 3.1 are external to it. Pass.
- **Model and convention changes.** The section transports an obstruction
  about polynomials over $\mathbb C$ to questions about integers. The
  polynomial-level statements (S1, S2) need no bridge. The values-level
  statement S3 needs the bridge of Corollary 3.1 (the polynomial-factor
  proposition of the Problem 940 folder), which the shared section supplies
  and the section does not cite; the bridge's hypotheses hold with $b=1$
  (Weakest step W2). Pass, with F1 asking for the citation.
- **Finite and statistical overreach.** No finite verification or heuristic
  average stands in for a proof; the small exact checks in this report are
  the reviewer's controls, not evidence. Inapplicable.
- **Uniformity.** No constants, error terms, or family-uniform bounds are
  asserted. The only quantity, "divisor-function size" in S7, is
  $n^{o(1)}$ in the problem's own normalization. Inapplicable.
- **Extremal conclusions.** No infimum, supremum, or sharpness claim is
  made in the section. Inapplicable.
- **Consequences and composition.** Each "so" and "hence" was checked
  separately: "so it is impossible for every $r\ge2$" (S1) follows from
  Theorem 3's conclusion that no term is constant; "impossible as well"
  (S2) follows from the general clause; "No polynomial family ... exists"
  (S3) follows from Corollary 3.1 with $b=1$; "neither strengthens nor
  threatens" (S7) follows from the family giving lower bounds only and
  contributing at most $n^{o(1)}$ representations. The composition consumes
  Theorem 3 and Corollary 3.1 at author-recorded standing. Pass.
- **Computation.** The two arithmetic facts, the identity
  $(m^2+B^2)^2-(m^2-B^2)^2=(2mB)^2$ and $1/2+1/3=5/6<1$, were recomputed by
  hand and in exact integer and rational arithmetic. Pass.
- **Reproduction.** The section states no rerun command, count, or coverage
  claim. Inapplicable.
- **Source and verdict fidelity.** The thirteen problem descriptions were
  compared with the Statement paragraphs: all match, except that the
  parenthetical "powerful parts of products of consecutive integers"
  describes Problem 935 exactly but Problem 367 (a product of powerful
  parts) and Problem 137 (whether the product is itself powerful) only
  loosely (Finding F4, note). Problem 365's statement does name Pell
  equations, as S4 uses. The status words "disproved" (Problem 1081) and
  "proved" (Problem 941) are characterizations of status text outside the
  read set and are left to the grader (Verdict, limitations). Pass within
  the read set.

## Weakest steps

**W1. Theorem 3 with a constant term (S1 and S2).** Re-derived directly
from Lemma 2 rather than through Theorem 3's proof. Let $a\in\mathbb C[t]$ be
nonconstant of degree $D$, $c=a+1$, so $\deg c=D$ and $\gcd(a,c)=1$ because a
common root of $a$ and $a+1$ would be a root of $1$. With $b=1$ the Wronskian
of Lemma 2 is $W=ab'-a'b=-a'$, also $W=ac'-a'c=aa'-a'(a+1)=-a'$, nonzero since
$a$ is nonconstant. A root of $a$ of multiplicity $\mu$ is a root of $a'$ of
multiplicity $\mu-1$, and a root of $c$ of multiplicity $\nu$ is a root of
$c'=a'$ of multiplicity $\nu-1$; the roots of $a$ and $c$ are distinct, so the
product of $(t-\alpha)^{\mu_\alpha-1}$ over the roots of $ac$ divides $a'$,
whence $2D-n_0(ac)\le D-1$, that is, $D\le n_0(ac)-1$. If $a$ is
$r_a$-powerful and $c$ is $r_c$-powerful then $n_0(a)\le D/r_a$ and
$n_0(c)\le D/r_c$, so

$$
D\le\frac{D}{r_a}+\frac{D}{r_c}-1 .
$$

For $r_a=r_c=r\ge2$ this reads $D\le2D/r-1\le D-1$, impossible; for
$r_a=2$, $r_c=3$ it reads $D\le5D/6-1<D$, impossible. Hence S1 for every
$r\ge2$ and S2. The interface of Lemma 2 is met: $a$, $1$, $c$ are nonzero,
pairwise coprime, and not all constant. Characteristic zero is essential and
is part of the page's convention: over $\mathbb F_p$ the identity
$t^p+1=(t+1)^p$ is a $p$-powerful counterexample, which is why the
convention must be carried whenever S1 is quoted.

**W2. The bridge from polynomials to integer families (S3).** The section
cites Theorem 3, which speaks about polynomial identities; the claim "no
polynomial family of consecutive powerful numbers" speaks about values. The
bridge is Corollary 3.1 of the shared section with $b=1$. Its hypotheses
with $a\in\mathbb Z[t]$ nonconstant, $b=1$, $c=a+1$: not all constant, yes;
for all large $t$ in a progression the values $a(t)$, $1$, $a(t)+1$ are
positive $r$-powerful integers, where $1$ is $r$-powerful by the page's
convention, so this is exactly the family hypothesis; $\gcd(a(t),1)=1$ for
infinitely many $t$, trivially. Its conclusion, that $a$, $b$, $c$ are all
nonconstant, contradicts $b=1$, so no such family exists, for any $r\ge2$
and in particular for $r=2$. Triples $a,a+1,a+2$ contain the pair $a,a+1$.
Two-parameter families of the Lemma 1 kind reduce to this along lines
$V=B$, as the paragraph after Corollary 3.1 records. The corollary's own
proof consumes the polynomial-factor proposition of the Problem 940 folder
at author-recorded standing; that page is outside this read set and its
interface was taken from the corollary's quotation of it. What the bridge
does not cover is a polynomial whose values are consecutive powerful numbers
only on a sparse parameter set: $a(t)=8t^2$ has $a(t)$ and $a(t)+1=x^2$ both
powerful exactly when $(x,t)$ solves $x^2-8t^2=1$, at
$t\in\{1,6,35,204,1189,6930,40391,\dots\}$, giving the pairs $(8,9)$,
$(288,289)$, $(9800,9801)$, $(332928,332929)$ and so on. These are the Pell
families of S4, and S3 is true only because the page's convention runs the
parameter over a progression; see Finding F1.

**W3. The r = 2 identity and its size (S7).** The unsplit binomial identity
of the reconstruction,
$(X+Y)^r=(X-Y)^r+\sum_{j\ \mathrm{odd}}2\binom rjX^{r-j}Y^j$, at $r=2$ is
$(X+Y)^2=(X-Y)^2+4XY$, and $X=m^2$, $Y=B^2$ gives
$(m^2+B^2)^2=(m^2-B^2)^2+(2mB)^2$; the $j=3$ split of Theorem 1 does not
arise since $3>r$. Each summand is a square, so each is powerful, and the
sum is the square $n=(m^2+B^2)^2$. The number of parameter pairs $(m,B)$
producing a given $n$ is at most the number of representations of
$\sqrt n=m^2+B^2$ as a sum of two squares, $r_2(\sqrt n)\le4d(\sqrt n)$,
and $d(k)=k^{o(1)}$, so the family contributes $n^{o(1)}$ ordered
representations of $n$ as a sum of two powerful numbers. Problem 943 asks
for an upper bound for all $n$; a construction supplies lower bounds only,
and this one is below the conjectured size, so it neither proves nor
contradicts the conjecture. S7 is exact as stated.

## Strongest attack

- **S1.** Sought $r$-powerful $a,c\in\mathbb C[t]$, $a$ nonconstant, with
  $c=a+1$: for squares, $g^2-f^2=1$ factors as $(g-f)(g+f)=1$, forcing
  constants; for general $r$-powerful shapes such as $f^2g^3$ the abc
  bookkeeping of W1 leaves no degree $D\ge1$; positive characteristic gives
  counterexamples but is excluded by the convention. Failed.
- **S2.** Sought $a$ $2$-powerful and $a+1$ $3$-powerful; W1 with
  $(r_a,r_c)=(2,3)$ gives $D\le5D/6-1$; the reverse assignment $(3,2)$ is
  the same inequality. Failed.
- **S3.** Sought a polynomial family. The Pell witness $a(t)=8t^2$ refutes
  the strongest reading (infinitely many parameters) but not the page's
  reading, since $8t^2+1$ is a square on no arithmetic progression of large
  $t$ (by Corollary 3.1's bridge, a polynomial that is $2$-powerful at all
  large $t$ in a progression is $2$-powerful as a polynomial, and $8t^2+1$
  is squarefree). Failed under the page's convention; Finding F1 asks the
  sentence to carry that convention.
- **S4.** The solutions of a Pell equation $x^2-Dy^2=1$ are the powers of
  the fundamental unit, so the $k$-th pair has size exponential in $k$;
  consecutive powerful pairs of this kind are $(Dy^2,x^2)$ with $D$
  powerful. No attack available beyond confirming the fact.
- **S5.** Attacked the reasoning rather than the conclusion: Problems 364
  and 366 ask whether one triple or pair exists at all, and Problem 365
  whether every pair contains a square, so a polynomial family, had one
  existed, would have supplied infinitely many objects and answered the
  first two positively and the third negatively; the reason none is
  supplied is S1, not the specificity of the questions. The conclusion
  stands; the wording is Finding F3.
- **S6.** Sought a transfer: an identity $a+c=2b$ among powerful
  polynomials exists at $r=2$ (three squares in progression), but a
  three-term progression of consecutive terms of the powerful sequence
  needs no powerful number strictly between the terms, and no polynomial
  identity controls the powerful numbers in an interval. No transfer was
  found, so the obstruction is not defeated; the sentence claims no
  theorem.
- **S7.** Sought a family of representations exceeding $n^{o(1)}$ from the
  identity: the count is bounded by $r_2(\sqrt n)$ (W3). Failed.
- **S8.** Sought bearing of a one-parameter family on Problem 1081 or 941:
  a family $n=f(t)$ of degree $d\ge1$ contributes $O(x^{1/d})$ integers up
  to $x$, negligible against an asymptotic of size $x/\sqrt{\log x}$ and
  irrelevant to a statement about all large integers. Failed. The status
  words were not attackable within the read set.
- **S9.** Sought a use of an identity among $r$-powerful values for one of
  the six problems. For Problem 935's question whether
  $Q_2(n(n+1)\cdots(n+\ell))/n^2$ is unbounded, three consecutive integers
  with large square factors would suffice, but that needs large powerful
  parts, not powerful values, and S1 shows two consecutive terms cannot
  both be powerful polynomials; the mechanism of the folder produces only
  fully powerful values. For Problem 942, a family gives $O(1)$ powerful
  numbers per interval $[n^2,(n+1)^2)$, against a target of $(\log n)^c$.
  For Problems 137, 936 and 1108 the objects are not polynomial in a
  parameter. No transfer was found; the sentence claims no theorem.

## Premises

- Theorem 3 and its general clause, shared section of the subject page
  (lines 186–203), author-recorded, read in full; interface used: $r\ge2$,
  $a,b,c\in\mathbb C[t]$ pairwise coprime, $r$-powerful in the page's sense
  with constants $r$-powerful, not all constant, $a+b=c$; characteristic
  zero. Its proof is another reviewer's subject; W1 re-derives the
  constant-term case from Lemma 2 independently.
- Lemma 2, the Mason–Stothers inequality, shared section (lines 148–184),
  classical, proof recorded on the page, read in full; interface: nonzero,
  pairwise coprime, not all constant.
- Corollary 3.1, shared section (lines 205–238), author-recorded, read in
  full; interface: $a,b\in\mathbb Z[t]$, $c=a+b$, not all constant, values
  positive and $r$-powerful for all large $t$ in an arithmetic progression,
  $\gcd(a(t),b(t))=1$ infinitely often. It consumes the polynomial-factor
  proposition of `wiki/research/erdos_940/finite_core_reduction.md` at
  author-recorded standing; that page was not read (outside the read set),
  and its interface is taken from the corollary's quotation of it. Used
  only for the values reading of S3.
- The Theorem 1 reconstruction,
  `wiki/research/erdos_939/theorem_1_reconstruction.md`, premise at its
  reviewed standing (reviewed as it stood on 2026-09-28T05:03:27Z with
  corrections applied since), read in full; used only for the form of the
  unsplit binomial
  identity, which is the binomial theorem.
- The Statement paragraphs of the thirteen problem pages listed under
  Reading, read in full; used for source fidelity only.
- Elementary inputs: Pell solutions as powers of the fundamental unit;
  $r_2(k)\le4d(k)$ and $d(k)=k^{o(1)}$; a polynomial family of degree $d$
  has $O(x^{1/d})$ values up to $x$.
- No library card, result page, or PDF is invoked by the section, and none
  was read.

## Findings

- **F1 (suggested).** Location: "No polynomial family of consecutive
  powerful numbers exists, consistent with the Pell-equation families of
  Problem 365 growing exponentially." Defect: the sentence does not carry
  the convention that makes it true, and the result it cites, Theorem 3,
  covers polynomial identities but not values; the values reading rests on
  Corollary 3.1 with $b=1$. Under the strongest reading, a nonconstant
  $a\in\mathbb Z[t]$ with $a(t)$ and $a(t)+1$ both powerful for infinitely
  many $t$, the sentence is false. Witness: $a(t)=8t^2$ at
  $t=1,6,35,204,1189,6930,\dots$, the $y$-coordinates of $x^2-8y^2=1$,
  where $(a(t),a(t)+1)=(8,9),(288,289),(9800,9801),(332928,332929),\dots$
  are consecutive powerful pairs. Proposed replacement: "No one-parameter
  polynomial family of consecutive powerful numbers exists: by Corollary
  3.1 with $b=1$, no nonconstant $a\in\mathbb Z[t]$ has $a(t)$ and $a(t)+1$
  both powerful for all large $t$ in an arithmetic progression. The
  Pell-equation families of Problem 365, such as $(8y^2,x^2)$ on
  $x^2-8y^2=1$, are not of this kind: their parameter runs over the
  exponentially sparse solution set of a Pell equation."
- **F2 (note).** Location: "an identity $a+1=c$ with $a,c$ $r$-powerful
  polynomials has only two nonconstant terms, so it is impossible for
  every $r\ge2$". Defect: the hypothesis "$a$ nonconstant" is used (it is
  Theorem 3's "not all constant") but not written; constants are
  $r$-powerful under the page's convention, so $1+1=2$ is an identity of
  the literal shape. Proposed replacement: "an identity $a+1=c$ with $a$
  nonconstant and $a,c$ $r$-powerful polynomials".
- **F3 (note).** Location: "The problems ask for specific pairs and
  triples, which polynomial identities cannot supply." Defect: Problem
  365's first question is universal (must every pair contain a square?),
  and a polynomial family, had one existed, would have supplied infinitely
  many pairs or triples and answered all three problems; the reason none
  is supplied is Theorem 3, not the form of the questions. Proposed
  replacement: "Problems 364 and 366 ask whether a single triple or pair
  exists and Problem 365 whether every pair contains a square; a polynomial
  family would have answered all three at once, and Theorem 3 rules every
  such family out."
- **F4 (note).** Location: "Problem 935, Problem 367 and Problem 137
  (powerful parts of products of consecutive integers)". Defect: the
  parenthetical describes Problem 935 exactly; Problem 367 bounds the
  product of the $2$-full parts of consecutive integers, which differs
  from the $2$-full part of their product ($B_2(2)B_2(3)B_2(4)=4$ against
  $Q_2(24)=8$), and Problem 137 asks whether the product of $k\ge3$
  consecutive integers is itself powerful. Proposed replacement: "(the
  powerful part of a product of consecutive integers, the product of their
  powerful parts, and whether such a product is itself powerful)".

## Verdict

- S0: not a claim (a process statement; the completeness of the search was
  not checked and is outside the read set).
- S1: refutation-failed (with F2, a note on the unwritten hypothesis).
- S2: refutation-failed.
- S3: refutation-failed under the page's convention for a one-parameter
  polynomial family (with F1, suggested); under the strongest reading the
  sentence would be refuted-as-stated by the Pell witness, which is why
  the convention should be written into it.
- S4: refutation-failed.
- S5: refutation-failed for its conclusion (with F3, a note on the
  reasoning).
- S6: not a claim (a stated obstruction with no proof asserted; no transfer
  was found that would defeat it).
- S7: refutation-failed.
- S8: refutation-failed for the "no bearing" assertion; the status words
  "disproved" and "proved" were not verified within the read set.
- S9: not a claim (a scoping judgment; no transfer was found).

**Limitations.** The status characterizations of Problems 1081 and 941 and
the completeness of the tree search were not checked, since the status
text and the trees lie outside the read set. The Problem 937 section, to
which the phrase "identities produce progressions of squares" alludes, was
not read; S6 was assessed on its own terms. The proofs of Theorem 3, Lemma
2 and Corollary 3.1 belong to another reviewer; this report re-derived the
constant-term case of Theorem 3 from Lemma 2 (W1) and confirmed Corollary
3.1's interface at $b=1$ (W2) but did not audit the polynomial-factor
proposition the corollary consumes. No required correction was found.
This focused review assigns no tier and changes no status.
