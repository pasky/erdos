---
name: research/erdos_939/evidence/verify/connections_problem_937_and_progressions_of_powerful_numbers_review
title: "Independent review of the connections section: Problem 937 and progressions of powerful numbers"
desc: |
  Refutation review of the section's eight statements: five survive
  (refutation-failed), the unqualified finiteness sentence is
  refuted-as-stated, one closing sentence is a summary rather than a claim,
  and the written proof of the main obstruction applies Corollary 3.1
  outside its hypotheses (proof defective; statement unresolved as written,
  with the repair derived here). Two required corrections, one suggested,
  two notes.
created: 2026-09-28T18:53:49Z
updated: 2026-09-28T20:41:57Z
---

***

## Subject and independence

**Role.** The reviewer is an independent examiner in a fresh context who
took no part in writing the page, the reconstruction page or any lead of
the folder, and received only the assignment text. The examination is a
refutation review of author-recorded mathematics; it assigns no tier and
changes no status.

**Subject.** Path `wiki/research/erdos_939/connections.md`
([[research/erdos_939/connections|the connections page]]) as it stood on
2026-09-28T13:50:48Z, section
"Problem 937 and progressions of powerful numbers", lines 488 to 516 (the H2
heading through the line before the next H2). No lead page belongs to the
section: the page's own "Leads created" section states that the
progression obstruction is recorded on the page and needs no folder.

**Read, and at what depth.**

- The section, in full, repeatedly.
- The page's preamble (lines 1 to 57: the standing paragraph and the
  Conventions) and the whole "Shared results" section (lines 58 to 302) as
  inputs: Lemma 1, Corollary 1.1, Lemma 2, Theorem 3, Corollary 3.1 and
  Proposition 4, their statements read closely and their proofs only far
  enough to fix each interface; the two internal steps of the proof of
  Corollary 3.1 were re-derived because the repair below reuses them.
- [[research/erdos_939/theorem_1_reconstruction|The Theorem 1 reconstruction]]
  in full, as a premise at its reviewed standing.
- [[problems/diophantine_problems/E0937/_index|Problem 937]], statement block only
  (lines 12 to 42).
- The source card
  [[../library/diophantine_problems/bajpai_2024_arithmetic_progressions_squarefull_numbers/_index|Bajpai, Bennett and Chan (2024)]]:
  its provenance paragraphs; the Source and Statement paragraphs of the
  result pages for Proposition 5.2, Theorem 1.2 and Corollary 1.3; the held
  accepted-manuscript PDF at pages 2, 3 and 11 (page images) and 18 to 19
  (extracted text), where the definition of $A^\infty(k)$, Theorems 1.1
  and 1.2, Corollary 1.3, Sections 5.1 and 5.2 and Proposition 5.2 stand.
- `docs/verification.md` ("Grading and claim standing", "Audit checklist",
  and the Erdos-specific "Whole-claim report" and "Audit checklist"),
  `docs/approach_vetting.md`, `docs/evidence.md` ("Source fidelity") and
  `docs/math_authoring.md`.

**Exposures.** Five, none of which touched a verdict: (1) the heading names
and the frontmatter `status: proved` line of the Problem 937 page, a
standing field, were seen while locating the statement block; (2) the
page's "Leads created" and "Sources read for this page" sections (lines 561
to 586) were read to establish that no lead page belongs to the section;
(3) the generated one-line link rows at the top of the source card, which
summarize its result pages, were displayed together with the provenance
paragraphs; (4) the bold paragraph labels of the three result pages (among
them "Verification", "Source qualification", "Qualification" and "Method")
were seen while locating their Statement paragraphs, without their content;
(5) the file names, and only the names, of review reports on other sections
written in the same worktree appeared in a status listing. The folder
index, every evidence page other than this file, the Current assessment and
Known results of the problem page, and the Problem 940 research pages were
not read.

## Restatement

Conventions used below. For an integer $r\ge2$ a positive integer $n$ is
$r$-powerful when $v_p(n)\ge r$ for every prime $p\mid n$, and $1$ is
$r$-powerful. A nonzero polynomial over a field of characteristic zero is
$r$-powerful when every root in an algebraic closure has multiplicity at
least $r$; constants are $r$-powerful. A three-term arithmetic progression
is a triple $(a,b,c)$ of positive integers with $a+c=2b$, pairwise coprime
when $\gcd(a,b)=\gcd(b,c)=\gcd(a,c)=1$. A *polynomial family* means what
Corollary 3.1 quantifies over: polynomials $a,b,c\in\mathbb Z[t]$ with
$a+c=2b$, not all constant, and an arithmetic progression
$P\subset\mathbb Z$ such that for every sufficiently large $t\in P$ the
values $a(t),b(t),c(t)$ are positive $r$-powerful integers, and
$\gcd(a(t),c(t))=1$ for infinitely many $t\in P$.

- **S1 (target and status).** Problem 937 asks whether there are infinitely
  many four-term arithmetic progressions of coprime powerful ($2$-powerful)
  numbers; the section reads "coprime" as pairwise coprime. The problem
  page records the status proved, by the elliptic-curve construction of
  Bajpai, Bennett and Chan, Proposition 5.2.
- **S2 (reduction).** A three-term progression $(a,b,c)$ of $r$-powerful
  numbers is a solution of $a+c=2b$; for a nonzero $b\in K[t]$, $2b$ is
  $r$-powerful as a polynomial if and only if $b$ is.
- **S3 (obstruction).** For every $r\ge3$ there is no polynomial family of
  pairwise coprime three-term progressions of $r$-powerful numbers,
  whatever the polynomials $a,b,c$ look like; consequently every
  construction of infinitely many such progressions with $r\ge3$ is
  non-polynomial in this sense. The section's proof is the sentence
  "Corollary 3.1 applies", with the polynomial remark of S2 as the bridge,
  under the heading "Outcome: fails, with the obstruction proved."
- **S4 (the case $r=2$).** At $r=2$ Theorem 3 permits $a$, $c$ and $2b$ all
  nonconstant, and the family $X^2+Y^2=2Z^2$ from the proof of Theorem 1.2,
  case $(m,k)=(3,2)$, realizes this: with $X=a^2-b^2+2ab$, $Y=a^2-b^2-2ab$
  and $Z=a^2+b^2$ the squares $Y^2,Z^2,X^2$ form a progression.
- **S5 (four terms at $r=2$).** "The four-term case needed the elliptic
  curve": the source's four-term construction is by an elliptic curve
  (Proposition 5.2) and, on the strongest reading, no other construction
  could do.
- **S6 (Corollary 1.3).** With $A^\infty(k)$ the largest $m$ for which
  infinitely many primitive ($\gcd(N,d)=1$) $m$-term progressions of
  $k$-full numbers exist, the abc conjecture implies $A^\infty(3)=3$ and
  $A^\infty(k)=2$ for all $k\ge4$.
- **S7 (finiteness sentence).** "Three-term progressions of $k$-powerful
  numbers with $k\ge4$ are conditionally finite": under abc there are only
  finitely many of them. As written the sentence carries no primitivity or
  coprimality qualifier.
- **S8 (closure).** The lead named in the folder index is closed in the
  negative for the polynomial mechanism, and the target needs nothing
  because it is settled.

## Checklist

- **Quantifiers and scope.** Fails on S7: the qualifier "primitive"
  (relatively prime), which the source's $A^\infty(k)$ carries, is dropped
  from the consequence sentence, and without it the sentence is false (F2).
  S3's scope word "polynomial family" is not defined in the section; the
  claim holds exactly at the scope of Corollary 3.1 (F4). S1 reads
  "coprime" as pairwise coprime, the strongest reading, which the source's
  construction satisfies (F5). Every other quantifier was found stated.
- **Circularity.** Passes. The section assumes nothing equivalent to its
  conclusions; Theorem 3 and Corollary 3.1 are proved on the page from
  Lemma 2 and the external polynomial-factor proposition, and neither
  mentions progressions.
- **Model and convention changes.** Fails on S3 as written (F1). The section
  passes from integer progressions to polynomials by citing Corollary 3.1,
  whose hypotheses concern integer values, and substitutes a
  polynomial-level fact ("$2b$ is $r$-powerful as a polynomial") for the
  value-level hypothesis that the sum's values are $r$-powerful; the values
  $2b(t)$ are not $r$-powerful whenever $b(t)$ is odd. The transfer is valid
  through Theorem 3 with the two internal steps of the proof of Corollary
  3.1, re-derived under Weakest steps.
- **Finite and statistical overreach.** Passes; the section uses no finite
  check or heuristic, and the reviewer's exact instances below serve only
  as witnesses against hypotheses, never as proofs.
- **Uniformity.** Inapplicable: no constant, error term, limit or bound
  over a family appears in the section, and Theorem 3 is degree-free.
- **Extremal conclusions.** Passes. The only extremal sentences are the
  quoted values of $A^\infty(k)$, which the section attributes to the
  source under abc and does not sharpen; the definition and the values were
  checked against the PDF.
- **Consequences and composition.** Fails on three sentences: "so Corollary
  3.1 applies" (F1, required); "three-term progressions of $k$-powerful
  numbers with $k\ge4$ are conditionally finite" (F2, required); "the
  four-term case needed the elliptic curve" (F3, suggested, since
  necessity is proved nowhere). The composition "the non-polynomial
  constructions are the only ones possible" inherits the proof of S3.
- **Computation.** Inapplicable to the section, which computes nothing. The
  reviewer's witnesses are exact integer instances written out in full
  below.
- **Reproduction.** Inapplicable: the section states no rerun line, count
  or coverage claim.
- **Source and verdict fidelity.** Passes for the recorded status, for the
  identity of Proposition 5.2 as an elliptic-curve construction, for the
  family $X^2+Y^2=2Z^2$ and for the values in Corollary 1.3, all checked
  against the held PDF and the result pages; "primitive" for the source's
  "relatively prime" is exact because the greatest common divisor of all
  terms of a progression is $\gcd(N,d)$. Fails only in degree on S5, where
  "needed" characterizes the source more strongly than the source does
  (F3).

## Weakest steps

**W1. The bridge from integer progressions to Theorem 3 (S3).** Let
$r\ge2$, let $a,b,c\in\mathbb Z[t]$ satisfy $a+c=2b$ and not all be
constant, and let $P=\{t_0+Mk:k\ge0\}$ be an arithmetic progression such
that for every sufficiently large $t\in P$ the values $a(t),b(t),c(t)$ are
positive $r$-powerful integers, with $\gcd(a(t),c(t))=1$ for infinitely
many $t\in P$.

*Step 1, each polynomial is $r$-powerful.* Fix a nonconstant
$f\in\{a,b,c\}$. It is positive at all large $t\in P$, so its leading
coefficient is positive and $f$ is eventually positive on all integers, and
it is $r$-powerful at every sufficiently large $t\in P$. The
polynomial-factor proposition, in the form on a progression that the proof
of Corollary 3.1 records (a prime $p\nmid M$ outside the finite bad set, a
residue class modulo $p^2$ intersected with $P$ by the Chinese remainder
theorem), gives every nonconstant irreducible factor of $f$ over
$\mathbb Q$ multiplicity at least $r$; irreducible polynomials over
$\mathbb Q$ are separable, so every complex root of $f$ has multiplicity at
least $r$. A constant $f$ is $r$-powerful by convention. Hence $a$, $b$,
$c$, and therefore $2b$, are $r$-powerful polynomials. This step is applied
to each polynomial on its own; nothing is asked of the values $2b(t)$.

*Step 2, the polynomials are pairwise coprime.* If $\gcd(a,c)$ in
$\mathbb Q[t]$ had positive degree, a primitive associate
$D_0\in\mathbb Z[t]$ would divide $a$ and $c$ in $\mathbb Z[t]$ by Gauss's
lemma, so $D_0(t)$ would divide $\gcd(a(t),c(t))$ for every integer $t$;
as $|D_0(t)|\to\infty$, $|D_0(t)|\ge2$ for all large $t$, against
$\gcd(a(t),c(t))=1$ infinitely often. So $\gcd(a,c)=1$ in $\mathbb Q[t]$,
hence in $\mathbb C[t]$, and $\gcd(a,2b)=\gcd(a,a+c)=1$, and likewise
$\gcd(c,2b)=1$.

*Step 3, Theorem 3.* The polynomials $a$, $c$ and $2b$ are pairwise
coprime, $r$-powerful, not all constant, and $a+c=2b$. Theorem 3 gives
$r=2$ and all three nonconstant. So for $r\ge3$ no polynomial family
exists, and at $r=2$ none with a constant term; this is S3 together with
the $r=2$ half of S4.

*Why the sentence as written does not do this.* Corollary 3.1 asks, for
its triple $(A,B,A+B)$, that the values of all three, including the sum, be
$r$-powerful integers at all large $t\in P$. With $(A,B)=(a,c)$ the sum is
$2b$, and for $b(t)$ $r$-powerful, $2b(t)$ is $r$-powerful exactly when
$b(t)$ is even: if $b(t)$ is odd then $v_2(2b(t))=1<r$. A pairwise coprime
progression has at most one even term, and its middle term is odd whenever
$a(t)+c(t)\equiv2\pmod4$. No other assignment fits the corollary: $a+c=2b$
is the only linear relation, and multiplying through by $2^r$ makes every
value $r$-powerful but destroys the coprimality hypothesis. The section's
own $r=2$ family (W2) has $b(t)=(t^2+1)^2$ odd for every even $t$; at $t=4$
the progression is $49,289,529$ with $2b=578=2\cdot17^2$. For $r=3$ the
source's progression $17^3,\ 3^4\cdot7^3,\ 37^3$, which comes from
$37^3+17^3=2\cdot3^4\cdot7^3$, has sum $2\cdot3^4\cdot7^3$ with $v_2=1$. So
Corollary 3.1, as stated, excludes only families whose middle term is even
on the progression, and the words "for every $r\ge3$, whatever the shape
of the terms" are earned by Theorem 3 through Steps 1 to 3, not by the
corollary's statement.

**W2. The realization at $r=2$ (S4).** With $X=a^2-b^2+2ab$,
$Y=a^2-b^2-2ab$ and $Z=a^2+b^2$,

$$
X^2+Y^2=2(a^2-b^2)^2+8a^2b^2=2(a^4+2a^2b^2+b^4)=2Z^2 .
$$

Along the line $b=1$, $a=t$: $X=t^2+2t-1$, $Y=t^2-2t-1$, $Z=t^2+1$, and
$(Y^2,Z^2,X^2)$ is a progression with difference
$Z^2-Y^2=(Z-Y)(Z+Y)=4t(t-1)(t+1)$, positive for $t\ge2$, with $Y>0$ for
$t\ge3$. As polynomials, $X-Y=4t$ and $X(0)=-1$ give $\gcd(X,Y)=1$;
$X-Z=2(t-1)$ and $Z(1)=2$ give $\gcd(X,Z)=1$; $Z-Y=2(t+1)$ and $Z(-1)=2$
give $\gcd(Y,Z)=1$. So $Y^2$, $Z^2$, $X^2$ are pairwise coprime
$2$-powerful polynomials, all nonconstant, with $Y^2+X^2=2Z^2$: the case
$r=2$, $k=3$ of Theorem 3. As integers on the progression
$t\equiv0\pmod2$, $X,Y,Z$ are odd; $\gcd(X,Y)$ divides
$\gcd(X,4t)=\gcd(X,t)=1$ since $X\equiv-1\pmod t$; $\gcd(X,Z)$ divides
$\gcd(Z,t-1)=\gcd(2,t-1)=1$ since $Z\equiv2\pmod{t-1}$ and $t-1$ is odd;
$\gcd(Y,Z)$ divides $\gcd(Z,t+1)=\gcd(2,t+1)=1$. So the values form
pairwise coprime progressions of squares for every even $t\ge4$, and the
family satisfies the hypotheses of Corollary 3.1 in the sense of the
definition above. Instances: $t=4$ gives $49,289,529$; $t=6$ gives $X=47$,
$Y=23$, $Z=37$ and $529,1369,2209$ with difference $840$.

**W3. The reading of Corollary 1.3 (S6, S7).** The source defines
$A^\infty(k)$ as the largest integer for which there are infinitely many
sets of $A^\infty(k)$ relatively prime $k$-full numbers in arithmetic
progression (PDF p. 2), and Corollary 1.3 states that abc implies
$A^\infty(2)=4$, $A^\infty(3)=3$ and $A^\infty(k)=2$ for all $k\ge4$ (PDF
p. 3). For a progression $N,N+d,\dots,N+(m-1)d$ the greatest common divisor
of all terms is $\gcd(N,d)$: $\gcd(N,N+d)=\gcd(N,d)$, and $\gcd(N,d)$
divides every term. So "relatively prime" read jointly is "primitive", the
result page's word and the section's. Read pairwise, the values are
unchanged: the upper bounds only weaken, and the lower-bound constructions
are pairwise coprime (W2 for $(3,2)$; for $(3,3)$, a prime dividing two of
$X^3$, $3^4Z^3$, $Y^3$ with $X^3+Y^3=2\cdot3^4Z^3$ and $\gcd(X,Y)=1$ divides
the third, and $3\mid X$ would force $3\mid Y$; for $(4,2)$ the result page
of Proposition 5.2 states pairwise coprimality). S6 is therefore exact. The
sentence S7 omits the qualifier: for every $k\ge2$ and every $s\ge1$ the
triple

$$
6^ks^k,\qquad 2\cdot6^ks^k,\qquad 3\cdot6^ks^k
$$

is a three-term progression of $k$-full numbers with difference $6^ks^k$
(the $2$-adic and $3$-adic valuations of each term are at least $k$), so
unqualified three-term progressions of $k$-powerful numbers are infinite
for every $k$, unconditionally. With "primitive" restored, S7 is exactly
$A^\infty(k)=2$ under abc.

## Strongest attack

- **S1.** Attempted: a reading of "coprime" under which the recorded status
  would not answer the question. Failed: for four-term progressions the
  joint and pairwise readings differ, but the source's construction is
  pairwise coprime by the statement of its Proposition 5.2, so the
  strongest reading is settled, and the problem page's statement block
  records "Proved".
- **S2.** Attempted: none possible beyond checking that a nonzero constant
  changes no root and no multiplicity. Survives.
- **S3.** Attempted, in order: (i) a family with a constant term, defeated
  by the general form of Theorem 3, since two nonconstant $r$-powerful
  terms give $2/r>1$, impossible for $r\ge2$; (ii) values $r$-powerful
  without the polynomials being so, defeated on a full progression by Step
  1 of W1, while values on a thinner set, such as the primes, lie outside
  the definition of a polynomial family and outside the claim; (iii)
  two-parameter families, which reduce to W1 along a line on which the
  hypotheses hold, as the page's device does with $B$ fixed and $m$ in a
  residue class prime to $B$; (iv) the literal invocation of Corollary 3.1,
  which fails on the value hypothesis for the sum, with the witnesses in
  W1. The statement survived every attack through W1; the written proof
  did not survive (iv).
- **S4.** Attempted: a common factor among $X,Y,Z$ as polynomials or as
  integers on the even progression, and a sign failure. None exists (W2).
- **S5.** Attempted, against the necessity reading: exhibiting a
  four-term polynomial family at $r=2$ would refute the strongest reading,
  and the reviewer found none; proving necessity would need more than the
  section has, since Theorem 3 treats three summands, and Lemma 2 applied
  to a three-term relation of a four-term family of pairwise coprime
  $2$-powerful polynomials of common degree $D$ gives only $D\le3D/2-1$.
  The "used" reading survives; the necessity reading is unproved (F3).
- **S6.** Attempted: a mismatch between "primitive" and the source's
  "relatively prime", and a misquoted value. Neither occurs (W3).
- **S7.** Refuted as literally written by the scaled progressions of W3;
  the qualified sentence is the source's.
- **S8.** Not attacked as mathematics; it summarizes S3 and the recorded
  status. The folder index it refers to is outside the read set.

## Premises

- **Theorem 3** (page, Shared results; author-recorded; its proof is
  another reviewer's remit). Interface used: pairwise coprime $r$-powerful
  $a,b,c\in\mathbb C[t]$, not all constant, with $a+b=c$, force $r=2$ with
  none constant; general form with the sum of $1/r_f$ over the nonconstant
  $f$ exceeding $1$. Used in Step 3 of W1 and in attack (i) on S3.
- **Corollary 3.1** (page, Shared results; author-recorded). Interface: the
  three values, including the sum, positive and $r$-powerful on all large
  points of a progression, and the two summands' values coprime infinitely
  often. Its two internal steps (the polynomial-factor proposition on a
  progression; Gauss's lemma for the polynomial gcd) were re-derived in W1
  because the repair reuses them; the corollary's statement is not what the
  section needs (F1).
- **Polynomial-factor proposition** of the Problem 940 folder, consumed
  only through the proof of Corollary 3.1 at the standing the page records
  (proved there, author-recorded); its page was not read. Interface: a
  nonconstant $f\in\mathbb Z[t]$, eventually positive and $r$-powerful at
  every sufficiently large integer input, has every nonconstant irreducible
  factor over $\mathbb Q$ with multiplicity at least $r$; the progression
  variant is the page's.
- **Lemma 1 and Corollary 1.1** (page): read for the interface only; the
  section consumes neither, and they enter only the reduction of the
  two-parameter device to a line (attack (iii) on S3).
- **Lemma 2** (page): interface only, used in the attack on S5.
- [[research/erdos_939/theorem_1_reconstruction|The Theorem 1 reconstruction]]
  (folder premise, independently reviewed as it stood on 2026-09-28T05:03:27Z
  with corrections applied since): read in full; the section uses only the
  shape of its identity as "the monomial device" and none of its results,
  so its hypothesis $r\ge6$ is not consumed.
- **Bajpai, Bennett and Chan (2024)**, held accepted-manuscript PDF of
  [[../library/diophantine_problems/bajpai_2024_arithmetic_progressions_squarefull_numbers/_index|the source card]]:
  the definition of $A^\infty(k)$ (p. 2), Theorems 1.1 and 1.2 and
  Corollary 1.3 (p. 3), and Sections 5.1 and 5.2 (p. 11) read as page
  images; Proposition 5.2 (pp. 18 to 19) read as extracted text. Result
  pages
  [[../library/diophantine_problems/bajpai_2024_arithmetic_progressions_squarefull_numbers/proposition_5_2|Proposition 5.2]],
  [[../library/diophantine_problems/bajpai_2024_arithmetic_progressions_squarefull_numbers/theorem_1_2|Theorem 1.2]]
  and
  [[../library/diophantine_problems/bajpai_2024_arithmetic_progressions_squarefull_numbers/corollary_1_3|Corollary 1.3]]:
  Source and Statement paragraphs. Corollary 1.3 is conditional on abc;
  Theorem 1.2 and Proposition 5.2 are unconditional.
- [[problems/diophantine_problems/E0937/_index|Problem 937]]: statement block.

## Findings

- **F1 (required).** Location: "so Corollary 3.1 applies to any polynomial
  family of pairwise coprime three-term progressions and excludes it for
  every $r\ge3$, whatever the shape of the terms", under the heading
  "Outcome: fails, with the obstruction proved." Defect: Corollary 3.1 is
  applied outside its hypotheses. Its statement requires the values of the
  sum to be $r$-powerful integers; here the sum is $2b(t)$, which is not
  $r$-powerful whenever the middle term $b(t)$ is odd, and the remark that
  $2b$ is $r$-powerful *as a polynomial* is a polynomial-level fact that
  cannot supply a value-level hypothesis. Witness: the section's own family
  at $t=4$, the progression $49,289,529$ with $2\cdot289=578=2\cdot17^2$;
  and, at $r=3$, the source's progression $17^3,\ 3^4\cdot7^3,\ 37^3$ with
  sum $2\cdot3^4\cdot7^3$. Proposed replacement: "so, once $a$, $b$ and $c$
  are $r$-powerful as polynomials and $\gcd(a,c)=1$ in $\mathbb Q[t]$, which
  the first two steps of the proof of Corollary 3.1 give from the values on
  the progression, Theorem 3 applies to the triple $(a,c,2b)$ and excludes
  every polynomial family of pairwise coprime three-term progressions for
  every $r\ge3$, whatever the shape of the terms"; the derivation is W1.
  Alternatively, restate Corollary 3.1 for a relation
  $\alpha a+\beta b=\gamma c$ with nonzero integer coefficients, which its
  proof already supports since Theorem 3 ignores constants; that change
  lies outside this section.
- **F2 (required).** Location: "three-term progressions of $k$-powerful
  numbers with $k\ge4$ are conditionally finite." Defect: the qualifier
  "primitive" (relatively prime), which defines $A^\infty(k)$ and which the
  first half of the same sentence carries, is dropped; without it the
  sentence is false unconditionally. Witness: $6^ks^k$, $2\cdot6^ks^k$,
  $3\cdot6^ks^k$ for $s=1,2,3,\dots$, a three-term progression of $k$-full
  numbers for every $k\ge2$. Proposed replacement: "primitive three-term
  progressions of $k$-full numbers with $k\ge4$ are finite under abc."
- **F3 (suggested).** Location: "the four-term case needed the elliptic
  curve." Defect: "needed" asserts that no other construction is possible,
  which neither the section (Theorem 3 treats three summands, and Lemma 2
  gives no contradiction for four $2$-powerful terms of a common degree)
  nor the source (which says examples "appear rather harder to come by")
  proves. Proposed replacement: "the source's four-term construction uses
  an elliptic curve."
- **F4 (note).** Location: "any polynomial family". The scope is that of
  Corollary 3.1: one integer parameter, $r$-powerful values at every
  sufficiently large point of an arithmetic progression, coprime values
  infinitely often. Families evaluated only on thinner parameter sets, such
  as the primes $q$ of the reconstruction, or in several parameters, are
  covered only through a line of this kind; the page's device has one ($B$
  fixed, $m$ in a residue class prime to $B$). Proposed addition: name the
  scope in the sentence, for example "any polynomial family in the sense
  of Corollary 3.1".
- **F5 (note).** Location: "pairwise coprime powerful numbers" in the
  target. The problem page says "coprime". For three-term progressions of
  $r$-powerful numbers the readings coincide: $\gcd(a,b,c)=\gcd(a,b)$ and
  $\gcd(b,c)=\gcd(a,b)$, and if $\gcd(a,b)=1$ then $\gcd(a,c)$ divides
  $2$, while $2\mid\gcd(a,c)$ would give $4\mid a$ and $4\mid c$, so
  $4\mid2b$ and $2\mid b$. For four terms they differ, the section's
  reading is the strongest, and it is settled by the source's pairwise
  coprime construction. Proposed addition: a parenthesis noting the
  problem page's wording, or none.

## Verdict

- **S1**: refutation-failed. The target and the recorded status are
  reported faithfully; "pairwise" is the strongest reading and is settled.
- **S2**: refutation-failed.
- **S3**: proof defective; statement unresolved as the section proves it.
  The obstruction is true, and W1 derives it from Theorem 3 and the
  polynomial-factor proposition at their recorded standing, but the
  section's proof consists of an application of Corollary 3.1 outside its
  hypotheses (F1); the consequence "the non-polynomial constructions are
  the only ones possible" and the closure of the lead inherit this verdict
  until the invocation is repaired.
- **S4**: refutation-failed.
- **S5**: refutation-failed on the reading that the source's four-term
  construction uses an elliptic curve; the necessity reading of "needed"
  is unproved and should be reworded (F3).
- **S6**: refutation-failed.
- **S7**: refuted-as-stated. The literal sentence is false for every
  $k\ge2$ by the scaled progressions of W3; with the qualifier "primitive"
  restored it is the source's conditional statement (F2).
- **S8**: not a claim; it summarizes S3 and the recorded status. Whether
  the folder index asked the question the section attributes to it was not
  checked, the index being outside the read set.

**Limitations.** The polynomial-factor proposition of the Problem 940
folder was consumed at the page's recorded standing and not re-verified;
the proofs of Theorem 3 and Corollary 3.1 belong to another reviewer, and
only their interfaces, plus the two steps of the proof of Corollary 3.1
that the repair reuses, were re-derived here. No web search was made. This
focused review assigns no tier and changes no status.
