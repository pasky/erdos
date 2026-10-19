---
name: research/erdos_939/evidence/verify/connections_problem_939_the_remaining_parts_review
title: "Independent review of the connections section: Problem 939, the remaining parts"
desc: |
  Refutation review of the section "Problem 939, the remaining parts" as it
  stood on 2026-09-28T13:50:48Z: seven statements survive (refutation-failed)
  and one cross-reference is not a claim; zero required corrections, two
  suggested rewordings and three notes.
created: 2026-09-28T18:54:26Z
updated: 2026-09-28T20:41:57Z
---

***

## Subject and independence

Role: the reviewer, working in a fresh context from the assignment alone. The
reviewer took no part in writing the connections page, the reconstruction page
or the library cards, and read no earlier review or grade of any of them.

Subject: the source as it stood on 2026-09-28T13:50:48Z (called "the subject
commit" below), page
`wiki/research/erdos_939/connections.md`, section
"## Problem 939, the remaining parts", lines 406–426: the heading at line 406,
the paragraph on the third question at lines 408–418, the paragraph on the
second question at lines 420–425; the next H2 is at line 427. The section
names no lead page. Charge: refutation of every author-recorded statement in
the section.

Reading, at the depth stated:

- The whole connections page at the subject commit: the subject section in
  full; the preamble, the Conventions and the shared results (Lemma 1,
  Corollary 1.1, Lemma 2, Theorem 3, Corollary 3.1, Proposition 4 and
  Corollary 4.1) at statement and hypothesis depth, as interfaces; the other
  connection sections (r = 4, r = 5, Problems 940, 1107 and 937, the other
  problems examined, the leads and the sources read) at reading depth, to
  locate the subject and to check its one cross-reference.
- `wiki/research/erdos_939/theorem_1_reconstruction.md` at the subject
  commit, in full, as a premise at its reviewed standing.
- The Statement of [[problems/diophantine_problems/E0939/_index|Problem 939]].
- The library cards of
  [[../library/diophantine_problems/nitaj_1995_conjecture_erdos_3_powerful_numbers/_index|Nitaj (1995)]],
  [[../library/diophantine_problems/cohn_1998_conjecture_erdos_3_powerful_numbers/_index|Cohn (1998)]]
  and
  [[../library/diophantine_problems/walsh_2024_question_erdos_powerful_numbers_elliptic_curve/_index|Walsh (2024)]],
  and [[../library/diophantine_problems/price_2026_infinite_r_powerful_sums/_index|the manuscript card]]
  behind Theorem 1.
- The held Walsh PDF in
  `library/diophantine_problems/walsh_2024_question_erdos_powerful_numbers_elliptic_curve/`,
  its text extracted and its page 2 read as an image: Theorem 1.1 and its
  proof at statement and proof depth.
- `docs/verification.md`, sections "Grading and claim standing", "Audit
  checklist — the canonical failure modes", "Whole-claim report" and "Audit
  checklist"; `docs/approach_vetting.md`; `docs/evidence.md`, section "Source
  fidelity"; `docs/math_authoring.md`.

Exposures, disclosed and used as premises nowhere:

1. The Problem 939 page keeps its Statement, Status, Source, References and
   Formalization paragraphs in one block above its first H2 (lines 18–74).
   Extracting the Statement (lines 18–25) brought the Status paragraph (lines
   27–36, standing text) and the Formalization paragraph (lines 56–74) into
   view. They record the same reading of the second and third questions as the
   section under review. Every finding below is derived from the
   reconstruction page, the cards, the held PDF and the page's own
   conventions, and would be unchanged without this exposure.
2. The four library cards were read in full, beyond their provenance
   paragraphs (digest, "Bears on" and "Read status" paragraphs included). None
   carries a review verdict.
3. The opening lines of the section "Durable reports and current standing" of
   `docs/verification.md` (guidance only).

Not read: the folder's `_index.md`, everything under its `evidence/` (the
existing review and grade), the Current assessment and Known results of any
problem page, anything among the private working files or outside the repository, and other
sections' reviews; no web search was made.

## Restatement

Notation as on the page: for $r\ge2$, a positive integer is $r$-powerful when
every prime dividing it does so to exponent at least $r$; a family of positive
integers is jointly coprime when the greatest common divisor of all its
members is $1$; a polynomial family, in the sense of Corollary 3.1, is a pair
$a,b\in\mathbb Z[t]$ with $c=a+b$, not all constant, such that for every
sufficiently large integer $t$ in some arithmetic progression the values
$a(t),b(t),c(t)$ are positive $r$-powerful integers, with $\gcd(a(t),b(t))=1$
for infinitely many such $t$.

- **S1** (third question, literature). For $r=3$ the third question of
  Problem 939, whether there are infinitely many triples of coprime
  $3$-powerful numbers $a,b,c$ with $a+b=c$, is answered affirmatively in the
  refereed literature, and the problem page records this.
- **S2** (Corollary 3.1 at $r=3$). No polynomial family of coprime
  $3$-powerful solutions of $a+b=c$ exists: for $r=3$ there are no
  $a,b\in\mathbb Z[t]$ with the properties above.
- **S3** (the constructions are non-polynomial). The constructions of Nitaj
  (1995), Cohn (1998) and Walsh (2024) of infinitely many coprime
  $3$-powerful triples are not polynomial families in the sense of S2. In
  particular Walsh's construction takes multiples $nP$ of a point $P$ of
  infinite order on the curve $Y^2=X^3-432p^2$, for an odd prime $p$ for which
  the curve has positive rank, and the heights of the points $nP$ grow
  quadratically in $n$.
- **S4** (limitation). The binomial identity with monomial substitution, the
  mechanism of the folder, contributes nothing to the third question at
  $r=3$.
- **S5** (second question at $r\ge6$). For each fixed $r\ge6$, the second
  question of Problem 939, whether there are at most finitely many sums of
  $r-2$ coprime $r$-powerful numbers that are themselves $r$-powerful, is
  answered in the negative by Theorem 1 of the reconstruction page, with
  "coprime" read as jointly coprime.
- **S6** (count of the family). For each fixed $r\ge6$ there are constants
  $c_r,C_r>0$ such that for all large $X$ the number of tuples with sum at
  most $X$ produced by the two-parameter family of Corollary 1.1 lies between
  $c_rX^{2/r^2}/\log\log X$ and $C_rX^{2/r^2}$. The section's sentence
  attaches this count to "the family it produces"; F2 treats the antecedent.
- **S7** (trivial upper bound and comparison). For each fixed $r\ge3$ the
  number of $(r-2)$-tuples of $r$-powerful positive integers with sum at most
  $X$ is $O_r(X^{(r-2)/r})$, and since $2/r^2<(r-2)/r$ the family of S6 is a
  vanishing proportion of that bound.
- **S8** (cross-reference). The Problem 940 section of the same page records
  the gap between the count of S6 and the shifted-target bound of the Problem
  940 folder. This is a pointer, not a mathematical claim.

## Checklist

- **Quantifiers and scope.** Pass with one qualifier. Every statement is for a
  fixed $r$, matching Theorem 1 ("for each fixed $r$ separately") and
  Corollary 1.1 (constants depending only on $r$, $X$ large depending on $r$).
  The only scope word the section leaves implicit is the coprimality
  convention in S5: the site's "coprime" is read as joint, as the page's
  Conventions and its $r=4$ section state, and Theorem 1's summands are not
  pairwise coprime (F1).
- **Circularity.** Pass. S2 rests on Corollary 3.1 (Mason–Stothers), S5 on
  Theorem 1 (a binomial identity and valuations); neither assumes anything
  about Problem 939. S3's consistency claim is a consequence of S2, not an
  input to it.
- **Model and convention changes.** Pass with the same qualifier. "Polynomial
  family" is used in exactly the sense Corollary 3.1 defines, and the page's
  $r=4$ section spells that sense out. Joint versus pairwise coprimality
  changes the truth of S5 (F1). "Heights" in S3 may be read as canonical or
  as naive logarithmic heights; both grow quadratically in the multiplier.
- **Finite and statistical overreach.** Pass. No finite computation or
  heuristic is used as a proof anywhere in the section.
- **Uniformity.** Pass. The constants in S6 and S7 depend on $r$ only, and
  the section's "up to constants" sits in a paragraph fixed at one $r$. The
  exponent comparison in S7 holds for every $r\ge3$.
- **Extremal conclusions.** Pass. "Far below" is an exponent comparison,
  $2/r^2$ against $(r-2)/r$, checked exactly: $2/r^2<(r-2)/r$ is
  $2<r(r-2)$, true for $r\ge3$. No sharpness is claimed.
- **Consequences and composition.** Pass with two notes. S5 composes Theorem 1
  (hypothesis $r\ge6$; conclusion: infinitely many tuples of $r-2$ positive,
  pairwise distinct, jointly coprime $r$-powerful integers with $r$-powerful
  sum) with the site question; the composition is exact under the joint
  reading. S2 is the "in particular" clause of Corollary 3.1 at $r=3$. S6 is
  correct for Corollary 1.1's family and misattributed if its pronoun is read
  as Theorem 1 (F2).
- **Computation.** Inapplicable to the section, which runs no computation.
  The reviewer's own checks (the exponent comparison, the
  joint-but-not-pairwise witness at $r=6$, the count of Theorem 1's own
  family) are exact integer arithmetic and are recorded under Weakest steps
  and Findings.
- **Reproduction.** Inapplicable. The section states no rerun command and
  cites no evidence run.
- **Source and verdict fidelity.** Pass for Walsh (2024): the curve
  $Y^2=X^3-432p^2$, the hypothesis "odd prime $p$ with positive rank" and the
  multiples $(3pk)P$ of a generator $P$ of infinite order are exactly Theorem
  1.1 on page 2 of the held PDF. The quadratic growth of heights is a gloss,
  not a sentence of the paper; it is a standard property of the multiples of
  a non-torsion point. For Nitaj (1995) and Cohn (1998) no text is held; their
  characterization as non-polynomial is entailed by S2 and the cards'
  recorded results, not read from the sources (F3). "Refereed literature":
  Bull. London Math. Soc. 27 (1995) and Math. Comp. 67 (1998), as the cards
  record.

## Weakest steps

**W1: the transfer behind S5.** Theorem 1 gives, for each $r\ge6$, infinitely
many tuples $(a_1,\dots,a_{r-2},N)$ with $a_1+\cdots+a_{r-2}=N$, all entries
positive, pairwise distinct and $r$-powerful, and $\gcd(a_1,\dots,a_{r-2})=1$.
The site asks whether there are at most finitely many sums of $r-2$ coprime
$r$-powerful numbers that are $r$-powerful. Under the joint reading each tuple
of Theorem 1 is such a sum, and distinct tuples have distinct $N$ (the
reconstruction's "Infinitely many tuples" step), so the answer is no. Under a
pairwise reading the tuples do not qualify: at $r=6$, with $X=q^6$ and
$Y=30^6$, the summands are $(X-Y)^6$, $12X^5Y$, $40X^3Y^3$ and $12XY^5$, and
$X^3Y$ divides both $12X^5Y$ and $40X^3Y^3$ (with $q=31$ the greatest common
divisor of these two is exactly $12X^3Y$), while the joint gcd is $1$. In
general every summand other than $(X-Y)^r$ is divisible by $XY$, so pairwise
coprimality fails for every $r\ge6$. The transfer is therefore valid exactly
under the reading the page declares.

**W2: the characterization of Walsh's construction in S3.** Theorem 1.1 of the
held paper: for an odd prime $p$ such that $E:Y^2=X^3-432p^2$ has positive
rank, and $P$ a generator of infinite order, the multiples $(3pk)P$, $k\ge1$,
yield pairwise coprime integer solutions of $x^3+y^3=p^4z^3$; the triple
$(x^3,y^3,p^4z^3)$ is then a coprime $3$-powerful solution of $a+b=c$. For a
non-torsion point the canonical height satisfies $\hat h(nP)=n^2\hat h(P)$
with $\hat h(P)>0$, and the naive logarithmic height differs from it by a
constant depending only on $E$; so the heights of the multiples grow
quadratically in the multiplier, whether the multiplier is $k$ or $3pk$. A
one-parameter polynomial family, listed along its progression, has $n$-th
member of logarithmic size $O(\log n)$, so this growth is incompatible with a
polynomial family. Independently of the growth, S2 already forces every
construction of infinitely many coprime $3$-powerful triples to be
non-polynomial in the corollary's sense, which is what makes S3 true for the
two sources whose texts are not held.

**W3: the counts in S6 and S7.** Corollary 1.1's interface was confirmed: it
counts ordered tuples from pairs $(m,B)$ with $B$ a positive multiple of $B_0$
and $m>B$ coprime to $B$, with $N=(m^r+B^r)^r\le X$; its bounds are
$c_rX^{2/r^2}/\log\log X$ and $C_rX^{2/r^2}$ for large $X$. Theorem 1's own
family, $B=B_0$ fixed and $m=q$ a prime above $B_0$, is smaller: $N\le X$
forces $q\le X^{1/r^2}(1+o(1))$, so its count is asymptotic to
$r^2X^{1/r^2}/\log X$ by the prime number theorem, and Chebyshev's bounds give
the same order. At $r=6$ and $X=10^{216}$ the exact count is $78{,}488$
against a lower-bound scale $X^{2/36}/\log\log X\approx1.6\times10^{11}$. For
S7: every $r$-powerful $n$ can be written $n=A^r\prod_{j=1}^{r-1}B_j^{r+j}$
with each $B_j$ squarefree (for each prime $p$ write $v_p(n)=rm+j$ with $m\ge1$
and $0\le j\le r-1$; put $p^m$ into $A$ when $j=0$, otherwise $p^{m-1}$ into
$A$ and $p$ into $B_j$), so the number of $r$-powerful $n\le X$ is at most
$X^{1/r}\prod_{j=1}^{r-1}\zeta(1+j/r)$; an $(r-2)$-tuple with sum at most $X$
has every entry at most $X$, which gives $O_r(X^{(r-2)/r})$ tuples. Both
counts compose with the exponent comparison of S7 exactly as the section
says.

## Strongest attack

- **S1.** Attack: find that a cited construction is unrefereed or answers a
  different question. The cards record Nitaj (1995) in Bull. London Math.
  Soc. 27, no. 4, 317–318 and Cohn (1998) in Math. Comp. 67, no. 221,
  439–440, both refereed venues, both for the exact third question. Walsh
  (2024) is an arXiv preprint, but the section does not call it refereed. The
  attack fails. Limitation: the clause "as the problem page records" concerns
  text outside the allowed read set; it was seen only through the disclosed
  exposure and is not relied on.
- **S2.** Attack: exhibit a polynomial family at $r=3$, or a family outside
  the corollary's hypotheses that the sentence would still cover. Any
  $a,b,c\in\mathbb C[t]$, pairwise coprime, not all constant, with every root
  of multiplicity at least $3$ and $a+b=c$, gives $n_0(abc)\le D$ with
  $D=\max\deg$, against Mason–Stothers $D\le n_0(abc)-1$; so no such
  polynomials exist, and the arithmetic hypotheses transfer to the polynomial
  ones through Corollary 3.1's proof (its interface: values $3$-powerful and
  positive for all large $t$ in a progression, coprime infinitely often).
  Integer-valued polynomials with rational coefficients reduce to
  $\mathbb Z[s]$ on a subprogression, and a several-parameter identity
  restricts to a line, so widening the sense of "polynomial family" does not
  produce a counterexample. The attack fails.
- **S3.** Attack: find a discrepancy with the held text (a different curve, a
  different set of multiples, a different growth). Theorem 1.1 uses exactly
  $Y^2=X^3-432p^2$ and the multiples $(3pk)P$ of a generator; the heights of
  $nP$ grow like $n^2\hat h(P)$. For Nitaj and Cohn no text is held, so the
  only available attack is the logical one, and S2 closes it. The attack
  fails; the fidelity limitation is F3.
- **S4.** Attack: extract a two-summand identity from the mechanism at $r=3$.
  The binomial identity at $r=3$ reads $(X+Y)^3=(X-Y)^3+6X^2Y+2Y^3$, three
  summands; merging the last two gives $2Y(3X^2+Y^2)$, which is $3$-powerful
  at $(m^3,B^3)$ only under a Diophantine condition on $3m^6+B^6$ that holds
  on no arithmetic progression, and S2 excludes every polynomial family. The
  attack fails.
- **S5.** Attack: read "coprime" as pairwise. Then Theorem 1's tuples do not
  qualify (the W1 witness), and the sentence would be false. Under the page's
  declared joint reading the attack fails. Attack on the range: Theorem 1
  requires $r\ge6$ and the section claims exactly $r\ge6$. The attack fails;
  the missing qualifier is F1.
- **S6.** Attack: read "the family it produces" as Theorem 1's own family.
  Its count is of order $X^{1/r^2}/\log X$, below the stated lower bound for
  all large $X$ (W3). Under the reading "the family of Corollary 1.1" the
  bounds are the corollary's own and the attack fails. The ambiguity is F2.
- **S7.** Attack: find that $X^{(r-2)/r}$ is not an upper bound, or that the
  exponents are misordered. The bound follows from the $O_r(X^{1/r})$ count of
  $r$-powerful numbers (W3), and $2/r^2<(r-2)/r$ for $r\ge3$. The attack
  fails.
- **S8.** Not a claim; the pointer resolves. The Problem 940 section quotes
  $0.0556$ against $0.6560$ at $r=6$, which the reviewer recomputed from
  $2/36$ and $4/6-5/468$.

## Premises

- **Corollary 3.1** of the connections page (shared result, another
  reviewer's proof). Interface used: $r\ge2$, $a,b\in\mathbb Z[t]$, $c=a+b$,
  not all constant, values positive and $r$-powerful for all sufficiently
  large $t$ in some arithmetic progression, $\gcd(a(t),b(t))=1$ for
  infinitely many such $t$; conclusion $r=2$ with all three nonconstant, hence
  no family for $r\ge3$. Consumed at $r=3$ only.
- **Theorem 1** of
  [[research/erdos_939/theorem_1_reconstruction|the Theorem 1 reconstruction]]
  (premise at its reviewed standing). Interface used: for each fixed $r\ge6$,
  infinitely many tuples of $r-2$ positive, pairwise distinct, jointly coprime
  $r$-powerful integers with $r$-powerful sum; its proof's family is $X=q^r$
  and $Y=B^r$ with $B$ the product of the coefficient primes and $q>B$ prime;
  every summand other than $(X-Y)^r$ is divisible by $XY$.
- **Corollary 1.1** of the connections page (shared result). Interface used:
  $r\ge6$; pairs $(m,B)$ with $B$ a positive multiple of $B_0$ and $m>B$
  coprime to $B$; distinct pairs give distinct tuples; count with $N\le X$
  between $c_rX^{2/r^2}/\log\log X$ and $C_rX^{2/r^2}$ for large $X$.
- **Walsh (2024)**, held PDF, Theorem 1.1 with its proof (pp. 1–3), read at
  statement and proof depth from the extracted text and the page-2 image.
  Interface used: odd prime $p$, $E:Y^2=X^3-432p^2$ of positive rank,
  generator $P$, multiples $(3pk)P$, pairwise coprime solutions of
  $x^3+y^3=p^4z^3$.
- **Nitaj (1995)** and **Cohn (1998)**: texts not held; their results
  (infinitely many coprime $3$-powerful triples with $a+b=c$; in Cohn's
  construction none a cube) consumed through the cards' recorded statements
  only. Their methods were not read.
- **Problem 939**, Statement only: the three questions restated above.
- Standard facts supplied by the reviewer: the Néron–Tate height is a
  quadratic form with $\hat h(nP)=n^2\hat h(P)$ and $\hat h(P)>0$ for
  non-torsion $P$, at bounded distance from the naive height; the
  $O_r(X^{1/r})$ count of $r$-powerful numbers, derived in W3; Chebyshev's
  bounds for the prime counting function.

## Findings

- **F1** (suggested). Location: line 420, "**The second question at
  $r\ge6$.** Settled negatively by Theorem 1". Defect: the sentence carries no
  coprimality convention, and its truth depends on one. Witness: at $r=6$
  the summands $12X^5Y$ and $40X^3Y^3$ of the Theorem 1 tuple share the factor
  $X^3Y$; in general all summands but $(X-Y)^r$ share $XY$, so under a
  pairwise reading of the site's "coprime" Theorem 1 answers nothing. The
  page declares the joint reading elsewhere (Conventions; the $r=4$ section),
  and the reconstruction states joint coprimality, so the sentence is correct
  as the page reads the question. "Settled" is also a status word on a page
  whose preamble changes no status. Proposed replacement: "Answered in the
  negative, for each $r\ge6$, by Theorem 1, under the joint-coprimality
  reading of the question that this page adopts; the summands of Theorem 1
  are not pairwise coprime, since all but $(X-Y)^r$ are divisible by $XY$."
- **F2** (suggested). Location: lines 421–423, "Corollary 1.1 records the
  size of the family it produces, between $X^{2/r^2}/\log\log X$ and
  $X^{2/r^2}$ tuples with sum at most $X$, up to constants". Defect: the
  pronoun "it" most naturally refers to Theorem 1, whose proof's family
  ($B=B_0$ fixed, $m=q$ prime) has about $r^2X^{1/r^2}/\log X$ members with
  sum at most $X$, not the stated order. Witness: at $r=6$ and $X=10^{216}$
  the primes $30<q\le10^6$ give $78{,}488$ tuples, while
  $X^{2/36}/\log\log X\approx1.6\times10^{11}$. The bounds are those of
  Corollary 1.1's own two-parameter family, which contains Theorem 1's.
  Proposed replacement: "Corollary 1.1 records the size of the two-parameter
  family that extends it: between $X^{2/r^2}/\log\log X$ and $X^{2/r^2}$
  tuples with sum at most $X$, with constants depending on $r$; Theorem 1's
  one-parameter family alone has order $X^{1/r^2}/\log X$."
- **F3** (note). Location: lines 410–417, "the constructions of Nitaj, Cohn
  and Walsh are non-polynomial (Walsh's runs through ...)". The
  characterization is checked against the held text for Walsh only; the Nitaj
  and Cohn texts are not held, as their cards record. The sentence is true
  because Corollary 3.1 forces every construction of infinitely many coprime
  $3$-powerful triples to be non-polynomial in its sense, but the reader is
  not told that this, and not a reading of the two papers, is the warrant.
  Proposed replacement: after "are non-polynomial", add "as Corollary 3.1
  requires of any such construction; only Walsh's text is held, and his runs
  through ...".
- **F4** (note). Location: the section heading and its two paragraphs. The
  first question at $r\ge6$ (can such a sum ever be $r$-powerful?) is also
  answered, affirmatively, by Theorem 1, and the section titled "the
  remaining parts" does not mention it; the page's $r=4$ and $r=5$ sections
  cover the first question only at those exponents. No statement is wrong;
  one sentence would make the coverage complete.
- **F5** (note). Location: lines 423–424, "the trivial upper bound
  $X^{(r-2)/r}$". The bound rests on the $O_r(X^{1/r})$ count of
  $r$-powerful numbers, which the page nowhere derives or cites. The
  three-line derivation in W3, or a citation of the classical asymptotic,
  would make "trivial" self-contained.

## Verdict

- **S1** (third question answered in the refereed literature):
  refutation-failed.
- **S2** (no polynomial family of coprime $3$-powerful $a+b=c$):
  refutation-failed.
- **S3** (the three constructions are non-polynomial; Walsh's through
  multiples of a point on $Y^2=X^3-432p^2$ with quadratically growing
  heights): refutation-failed.
- **S4** (the mechanism adds nothing at $r=3$): refutation-failed.
- **S5** (second question answered in the negative for each $r\ge6$ by
  Theorem 1, coprimality joint): refutation-failed.
- **S6** (Corollary 1.1's family has between $X^{2/r^2}/\log\log X$ and
  $X^{2/r^2}$ tuples with sum at most $X$, up to constants depending on $r$):
  refutation-failed as an interface use of Corollary 1.1; the sentence's
  pronoun is F2.
- **S7** (trivial bound $X^{(r-2)/r}$ and the exponent comparison):
  refutation-failed.
- **S8** (cross-reference to the Problem 940 section): not a claim.

No statement is refuted-as-stated and no proof in the section is defective;
the count of required corrections is zero. Limitations: the proofs of
Corollary 1.1, Corollary 3.1 and Theorem 1 were not re-verified here beyond
their interfaces, since they belong to other reviewers or stand at their
reviewed standing; the Nitaj and Cohn texts are not held, so their methods
were not checked; the clause "as the problem page records" lies outside the
allowed read set and is neither confirmed nor denied by this review; the
quadratic growth of heights in S3 is verified as standard mathematics, not as
a sentence of the Walsh paper. This focused review assigns no tier and changes
no status.
