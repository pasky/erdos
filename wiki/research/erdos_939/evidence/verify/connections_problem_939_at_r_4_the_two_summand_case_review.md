---
name: research/erdos_939/evidence/verify/connections_problem_939_at_r_4_the_two_summand_case_review
title: "Independent review of the connections section: Problem 939 at r = 4: the two-summand case"
desc: |
  Fresh-context refutation review of the r = 4 section of the connections
  page as it stood on 2026-09-28T13:50:48Z: all six author-recorded statements
  survive (refutation-failed); one required correction, a false
  bibliographic sentence about the problem page's references, plus three
  suggested rewordings and one note. No tier assigned, no status changed.
created: 2026-09-28T18:49:01Z
updated: 2026-09-28T20:46:21Z
---

***

## Subject and independence

**Role and independence.** The reviewer is an independent examiner working
in a fresh context from the commissioned assignment alone. The reviewer
took no part in writing the connections page, its reconstruction page or
any other page of the folder, had not read them before this assignment,
and received no communication from an author of the section.

**Subject.** The source as it stood on 2026-09-28T13:50:48Z (called "the
reviewed commit" below), page
`wiki/research/erdos_939/connections.md`, section
"## Problem 939 at r = 4: the two-summand case", lines 303–338 (the H2 at
line 303 through the blank line before the next H2 at line 339). No
separate lead page was named; the section's Target paragraph names its
target, [[problems/diophantine_problems/E0939/_index|Problem 939]].

**Reading and depth.**

- The section, line by line, with every deduction re-derived.
- The page's opening conventions (lines 35–56) and its Shared results
  (lines 58–302), read in full as inputs. The interfaces of Lemma 1,
  Theorem 3 and Corollary 3.1 were confirmed at each use; their proofs are
  another reviewer's subject and are not graded here, though Theorem 3 was
  re-derived from Lemma 2 as an interface plausibility check.
- `wiki/research/erdos_939/theorem_1_reconstruction.md`, read in full as
  a premise at its reviewed standing: the conventions, the shape of the
  identity, and the Boundary section's count of summands at $r=4$.
- The Statement paragraph of the problem page (lines 18–25).
- The library cards of the two invoked sources (provenance paragraphs and
  result lists), the canonical conversions beside their PDFs, and the held
  PDFs themselves through text extraction: the CrowdMath note (2020),
  Theorem 2.1 with its proof on physical p. 2 of 5; Walsh (2024), the abc
  remark of the Introduction on physical p. 1 of 4 and the statement of
  Theorem 1.1 on p. 2.
- The named wiki guidance sections, for the report contract only.

**Exposures.** Two, disclosed here. First, the
problem page's top block was read as a whole (lines 16–74): besides the
Statement paragraph it holds a Status paragraph, the Source line, the
References list and a Formalization paragraph. The Status paragraph is
standing text; it says the $r=4$ case is open, which agrees with the
section's Target paragraph and changed no verdict. The References list is
the witness of finding F1. Second, the folder's `_index.md`, the page's
Current assessment and Known results, and everything under `evidence/`
were not read, so three attributions in the section (the dated Current
assessment, the "no example known" sentence and the reported search bound
$10^{14}$) are recorded as unverified rather than checked. No review,
grade, standing text beyond the disclosed paragraph, or web search reached
the reviewer.

## Restatement

The conventions are the page's: for $r\ge2$ a positive integer is
$r$-powerful when every prime dividing it does so to exponent at least $r$,
so $1$ is $r$-powerful; a family is jointly coprime when the greatest
common divisor of all its members is $1$; a nonzero polynomial over a field
of characteristic zero is $r$-powerful when every root in the algebraic
closure has multiplicity at least $r$.

- **S1 (target).** Problem 939's first two questions specialize at $r=4$
  ($r-2=2$ summands) to: (Q1) do positive coprime $4$-powerful integers
  $a,b$ with $a+b$ $4$-powerful exist, and (Q2) are there at most finitely
  many such pairs. For two summands joint and pairwise coprimality
  coincide. The section attributes to the problem page's Current
  assessment (dated 2026-09-27) that both are open, that no example is
  known, and that a forum-reported exhaustive search gives
  $\max(a,b)>10^{14}$ for any solution.
- **S2 (the transfer is excluded).** By Corollary 3.1 at $r=4$: there are
  no $a,b\in\mathbb Z[t]$ with $c=a+b$, not all constant, such that for
  every sufficiently large integer $t$ in some arithmetic progression the
  values $a(t),b(t),c(t)$ are positive $4$-powerful integers and
  $\gcd(a(t),b(t))=1$ for infinitely many such $t$; and the same exclusion
  holds for the restriction of an identity in several integer variables to
  any line $s\mapsto u+sw$ ($u,w$ integer vectors, $w\ne0$), read as a
  one-parameter identity in $s$.
- **S3 (interpretation).** The reconstruction's identity has one summand
  too many at $r=4$ (three where two are needed), and S2 subsumes this: no
  identity of the kind delimited in S2 can work at $r=4$, whatever the
  number and shape of its terms.
- **S4 (literature).** Assume the abc conjecture in its constant form: for
  every $\eta>0$ there is $\kappa(\eta)$ such that
  $c\le\kappa(\eta)\operatorname{rad}(abc)^{1+\eta}$
  for all coprime positive $a+b=c$. Then the coprime $4$-powerful
  solutions of $a+b=c$ are finite in number, because
  $\operatorname{rad}(abc)\le(abc)^{1/4}<c^{3/4}$ and the inequality
  $c<\kappa(\eta)c^{3(1+\eta)/4}$ bounds $c$. This is Theorem 2.1 of the
  CrowdMath note (2020), whose statement the card transcribes and whose
  proof the section did not read; Walsh (2024) makes the same remark; and
  neither source is cited on the problem page.
- **S5 (picture).** With Theorem 3, the situation at $r=4$ is that of a
  Fermat-type equation: any solution is sporadic, and infinitely many
  solutions would contradict abc.
- **S6 (next investigation).** Nothing proceeds through the folder's
  mechanism. An existence proof would be a non-polynomial construction of
  a single solution or a search beyond $10^{14}$; a finiteness proof would
  have to be unconditional where only the abc-conditional result is known;
  and "a negative outcome of either kind" is not obtainable from polynomial
  identities, by Theorem 3.

## Checklist

- **Quantifiers and scope.** S2 carries Corollary 3.1's quantifiers
  exactly (all large $t$ of a progression for powerfulness; infinitely many
  $t$ for coprimality). S4 leaves $\eta$ unrestricted where the displayed
  inequality bounds $c$ only for $\eta<1/3$ (F2). S5's "sporadic" is
  stronger than what Theorem 3 gives (F3). No almost-all/all slip and no
  dropped exceptional set.
- **Circularity.** None. Corollary 3.1 and Theorem 3 are proved on the
  page from Mason–Stothers and the polynomial-factor proposition, neither
  of which assumes anything about Problem 939.
- **Model and convention changes.** The passage from integer values to
  polynomial powerfulness is the bridge inside Corollary 3.1, used within
  its hypotheses; joint and pairwise coprimality coincide for two summands;
  the convention that $1$ is $4$-powerful is harmless because Corollary 3.1
  allows constant terms and excludes them too. No unbridged transfer.
- **Finite and statistical overreach.** None. The search bound is reported
  as a search bound, not as evidence of nonexistence.
- **Uniformity.** The only constant is $\kappa(\eta)$, depending on $\eta$
  alone; the resulting bound on $c$ depends on the fixed $\eta$, as it
  should. F2 records the missing range of $\eta$.
- **Extremal conclusions.** Inapplicable: the section asserts no infimum,
  supremum, attained value or sharpness (the sharpness remark belongs to
  Theorem 3's own text in the Shared results).
- **Consequences and composition.** Each "so" and "hence" was attacked
  separately: the line-restriction clause of S2 (verified, Weakest step
  2), "bounds $c$" in S4 (F2), "any solution is sporadic" in S5 (F3), and
  "a negative outcome of either kind is not obtainable ... by Theorem 3" in
  S6 (F4). Corollary 3.1 is consumed at exactly its stated strength.
- **Computation.** Inapplicable: the section runs no computation.
- **Reproduction.** Inapplicable: the section states no rerun command or
  coverage claim.
- **Source and verdict fidelity.** Theorem 2.1 of the CrowdMath note and
  Walsh's abc remark were checked against the held PDFs and match the
  section's characterizations. The sentence "neither is cited on the
  problem page" is false as written: Walsh (2024) is entry [Wa24] of the
  problem page's References list (F1). The three attributions to the
  Current assessment are outside the read set (F5).

## Weakest steps

**1. The abc deduction (S4).** Let $a,b,c$ be positive with $\gcd(a,b)=1$,
$a+b=c$ and all three $4$-powerful. Then $\gcd(a,c)=\gcd(b,c)=1$, so the
radical of $abc$ is the product of the three radicals. For a $4$-powerful
$n$, $\operatorname{rad}(n)^4$ divides $n$, so
$\operatorname{rad}(n)\le n^{1/4}$; hence
$\operatorname{rad}(abc)\le(abc)^{1/4}$, and $abc<c^3$ because
$1\le a,b<c$, so $\operatorname{rad}(abc)<c^{3/4}$. The constant form of
abc gives
$c\le\kappa(\eta)\operatorname{rad}(abc)^{1+\eta}<\kappa(\eta)c^{3(1+\eta)/4}$,
that is,

$$
c^{(1-3\eta)/4}<\kappa(\eta) .
$$

This bounds $c$ exactly when $\eta<1/3$; at $\eta=1/3$ it reads
$c<\kappa(1/3)\,c$ and bounds nothing. The section's sentence does not fix
$\eta$. The source proves the same theorem in the finitely-many-exceptions
form of abc with $\epsilon=1/3$, where equality of exponents suffices
because every solution is then an exception. The conclusion, finiteness
under abc, stands; the sketch needs "for any fixed $\eta<1/3$" (F2).

**2. The line-restriction clause of S2.** Let
$a,b\in\mathbb Z[U_1,\dots,U_k]$ with $c=a+b$, and let $L:s\mapsto u+sw$
with $u,w\in\mathbb Z^k$ and $w\ne0$. Composition gives
$a_L(s)=a(u+sw)\in\mathbb Z[s]$, likewise $b_L$ and $c_L$, with
$a_L+b_L=c_L$. If along $L$ the values are positive and $4$-powerful for
all large $s$ in a progression and coprime for infinitely many such $s$,
and $a_L,b_L,c_L$ are not all constant, Corollary 3.1 applies to the
one-parameter identity and yields $4=2$, a contradiction. If all three are
constant, the line carries one triple and no family. So the clause holds;
its content is that no line carries a one-parameter family, which is what
the section says.

**3. Corollary 3.1 at $r=4$ and the delimitation of "polynomial kind".**
Corollary 3.1 (page lines 205–229) hypothesizes $a,b\in\mathbb Z[t]$,
$c=a+b$, not all constant, positive $r$-powerful values at every
sufficiently large $t$ of some arithmetic progression, and coprime values
for infinitely many such $t$; it concludes $r=2$. At $r=4$ the conclusion
is false, so no such $a,b$ exist. The two-summand question at $r=4$ has
exactly this shape ($a$ and $b$ the summands, $c$ the sum, all positive),
so S2 is an instance of the corollary with nothing added. The device the
section says is excluded, a Lemma 1 identity with $n=3$, was also checked
directly: fixing $V=B$, the terms $K(U,B)^4$, $c_2B^bU^a$ (with $a=0$ or
$a\ge4$) and their sum are $4$-powerful in $\mathbb C[U]$ and pairwise
coprime, the only candidate common root $U=0$ being excluded by
$K(0,B)=\pm B^{d'}\ne0$; Theorem 3 then forces $r=2$ unless all three are
constant in $U$, which is a single triple. The sentence "every identity of
the polynomial kind fails" is therefore true in the sense the section
defines one sentence earlier (values $4$-powerful on all large integers of
a progression); identities whose terms share a nonconstant factor $D$ and
are used only where $D=\pm1$, or whose values are $4$-powerful only on a
thin set of parameters, are outside that sense, as the page's Shared
results say explicitly.

## Strongest attack

- **S1.** The problem statement (page lines 18–25) asks, for $r\ge4$,
  whether the sum of $r-2$ coprime $r$-powerful numbers can be
  $r$-powerful and whether there are at most finitely many such solutions;
  at $r=4$ this is two summands. The section says "finitely many such
  sums" where the site says "solutions"; the two are equivalent, because a
  given sum $N$ has finitely many decompositions $a+b=N$ in positive
  integers. Joint and pairwise coprimality coincide for two numbers. The
  attack found no discrepancy; the attributions to the Current assessment
  could not be checked.
- **S2.** Three attacks. (a) Integer-valued families in $\mathbb Q[t]$
  that are not in $\mathbb Z[t]$: if $f$ of degree $d$ is integer-valued
  on the progression $t\equiv t_0\pmod M$, then $g(s)=f(t_0+Ms)$ is
  integer-valued on $\mathbb Z$, hence an integer combination of the
  $\binom sk$ with $k\le d$; and each $\binom{d!\,s'}{k}$ lies in
  $\mathbb Z[s']$, because its coefficient of $s'^j$ is an integer
  multiple of $(d!)^j/k!$, an integer for $j\ge1$ and $k\le d$, while its
  constant term is $0$ or $1$. So the substitution $t=t_0+M\,d!\,s'$
  turns the family into one in $\mathbb Z[s']$ covered by Corollary 3.1
  on a sub-progression. The section's wording restricts to $\mathbb Z[t]$
  anyway. (b) Families whose powerfulness holds only on a
  thin parameter set, or identities with a common nonconstant factor $D$
  used where $D=\pm1$ (a nonconstant integer polynomial takes each value
  finitely often, so these give finitely many triples): both lie outside
  the sense S2 defines, and the page names the second as a construction of
  a different kind. (c) Two-parameter identities of Lemma 1's shape with
  two summands: excluded directly by Theorem 3 (Weakest step 3). No
  counterexample to S2 as delimited was found.
- **S3.** The reconstruction page's Boundary section gives the count
  $|J|+1=3>2$ at $r=4$, matching "one term too many"; S3 adds nothing
  beyond S2. The folder index the sentence cites is outside the read set.
- **S4.** The derivation was pushed to its edge: the exponent bookkeeping
  fails at $\eta\ge1/3$ (F2) but succeeds for every $\eta<1/3$, so the
  conclusion holds. Both source characterizations were checked against the
  PDFs: the CrowdMath theorem is stated exactly as the section says, under
  the paper's global abc assumption, and Walsh's Introduction states that
  abc implies finitely many pairwise coprime $4$-powerful triples with
  $a+b=c$ and that no example is known. The bibliographic clause fell: the
  problem page's References list contains Walsh (2024) as [Wa24] (F1).
- **S5.** The attack on "sporadic": Theorem 3 excludes polynomial families
  only. At $r=3$ the same theorem excludes polynomial families (the sum
  $k/r$ equals $1$ and is not greater), yet coprime $3$-powerful solutions
  of $a+b=c$ are abundant: Walsh's Introduction records the problem as
  solved by Nitaj and by Cohn, and Walsh's Theorem 1.1 gives, for any odd
  prime $p$ for which the curve $Y^2=X^3-432p^2$ has positive rank,
  infinitely many pairwise coprime solutions of $x^3+y^3=p^4z^3$ with
  $p\mid z$ from the multiples of a rational point, each giving coprime
  $3$-powerful $a=x^3$, $b=y^3$, $c=p^4z^3$ with $a+b=c$. So "no
  polynomial family" is compatible with infinitely many solutions of
  another kind, and Theorem 3 alone does not make solutions isolated or
  few. The sentence survives only under the reading "no
  solution belongs to a polynomial family", which its second clause (the
  abc-conditional finiteness) makes plausible as the intended one (F3).
- **S6.** The clause "a negative outcome of either kind is not obtainable
  from polynomial identities, by Theorem 3" was read both ways. A negative
  outcome (nonexistence, or finiteness) is not something a polynomial
  identity could ever supply, and Theorem 3 is not the reason; what
  Theorem 3 (through Corollary 3.1) excludes is a positive outcome from a
  polynomial identity, namely an example produced by a family or an
  infinitude. The rest of the paragraph is correct: an example must come
  from outside the delimited polynomial kind or from search, and the known
  finiteness is conditional (F4).

## Premises

- **Corollary 3.1** (connections page, Shared results, lines 205–229):
  interface as restated in Weakest step 3; author-recorded on the page;
  proved there from Theorem 3 and the polynomial-factor proposition of the
  Problem 940 folder, which the page reports as proved and
  author-recorded. Neither proof is graded here, and the Problem 940 page
  was not read. Depth: statement and proof read in full to confirm the
  interface.
- **Theorem 3** (lines 186–203): pairwise coprime $r$-powerful
  $a,b,c\in\mathbb C[t]$, not all constant, with $a+b=c$ force $r=2$ with
  none constant. Re-derived from Lemma 2 as an interface check:
  $n_0(f)\le\deg f/r$ for an $r$-powerful $f$, so
  $D\le n_0(abc)-1\le kD/r-1$ with $k\le3$ nonconstant terms, whence
  $r<k\le3$.
- **Lemma 2** (lines 148–184), Mason–Stothers in the form
  $\max\deg\le n_0(abc)-1$: used only through Theorem 3.
- **Lemma 1** (lines 60–121): used only to identify the device the section
  declares excluded.
- **Reconstruction page**
  `research/erdos_939/theorem_1_reconstruction.md`, independently
  reviewed as it stood on 2026-09-28T05:03:27Z with corrections applied
  since: read in
  full; consumed for the conventions, the identity's shape, and the
  Boundary count of summands at $r=4$. Used within its hypotheses (nothing
  at $r\le5$ is claimed from it).
- **Problem 939 statement** (`problems/diophantine_problems/E0939/_index.md`,
  lines 18–25): read.
- **CrowdMath (2020)**,
  [[../library/diophantine_problems/crowdmath_2020_applications_abc_conjecture_powerful_numbers/_index|card]]:
  provenance paragraph read; PDF held (5 pages); Theorem 2.1 and its proof
  read on physical p. 2 through text extraction and the canonical
  conversion. Interface: under abc, finitely many solutions of $x+y=z$
  with $(x,y)=1$ and $x,y,z$ all $4$-powerful.
- **Walsh (2024)**,
  [[../library/diophantine_problems/walsh_2024_question_erdos_powerful_numbers_elliptic_curve/_index|card]]:
  provenance paragraph read; PDF held (4 pages); the Introduction's abc
  remark (p. 1) and the statement of Theorem 1.1 (p. 2) read through text
  extraction and the canonical conversion. Theorem 1.1 and the
  Introduction's sentence recording the $r=3$ problem as solved are used
  only in the attack on S5, as an illustration; the theorem's proof was
  read for the divisibility $p\mid z$ and not verified.
- **The abc conjecture** in its constant form is a hypothesis of S4, not a
  premise; the section keeps it conditional throughout.

## Findings

- **F1 (required).** Location: "Walsh (2024) makes the same remark;
  neither is cited on the problem page." Defect: false as written.
  Witness: the References list of
  `wiki/problems/diophantine_problems/E0939/_index.md` at the reviewed commit
  carries the entry "[Wa24] P. Walsh, A question of Erdős on 3-powerful
  numbers and an elliptic curve analogue of the Ankeny-Artin-Chowla
  conjecture. arXiv:2404.03970 (2024)" (lines 52–54). Whether the page
  cites it for the abc remark is outside this review's read set.
  Replacement: "the CrowdMath note is not among the problem page's
  references; Walsh (2024) is ([Wa24])", with "though not for this remark"
  added only if the page's other sections bear it out. This is a
  bibliographic correction; no mathematics changes.
- **F2 (suggested).** Location: "so $c<\kappa(\eta)c^{3(1+\eta)/4}$
  bounds $c$." Defect: the inequality bounds $c$ only for $\eta<1/3$; the
  sentence leaves $\eta$ unrestricted. Witness: at $\eta=1/3$ it reads
  $c<\kappa(1/3)\,c$. Replacement: "so, for any fixed $\eta<1/3$,
  $c^{(1-3\eta)/4}<\kappa(\eta)$ bounds $c$."
- **F3 (suggested).** Location: "any solution is sporadic, and infinitely
  many would contradict abc." Defect: "sporadic" claims more than
  Theorem 3 gives; the theorem excludes polynomial families only, and at
  $r=3$ the same exclusion coexists with infinitely many solutions (the
  Introduction of Walsh 2024, and its Theorem 1.1 for the elliptic-curve
  mechanism). Replacement: "no solution lies in a polynomial family, and
  infinitely many would contradict abc."
- **F4 (suggested).** Location: "A negative outcome of either kind is not
  obtainable from polynomial identities, by Theorem 3." Defect: Theorem 3
  says nothing about negative outcomes; it excludes an example or an
  infinitude produced by a polynomial identity. Replacement: "Neither an
  example nor an infinite family at $r=4$ can come from a polynomial
  identity, by Corollary 3.1."
- **F5 (note).** The Target paragraph's attributions to the problem page's
  Current assessment (its date, "no example known", and the search bound
  $\max(a,b)>10^{14}$) were not checkable within the commissioned read set
  and are recorded as unverified; the page's Status paragraph, seen
  through the exposure disclosed above, agrees with them. The reference in
  S3 to "the folder index's count of monomials" was likewise not checked;
  the same count appears in the reconstruction page's Boundary section.

## Verdict

- **S1:** refutation-failed. The restatement of the target matches the
  problem page's Statement paragraph; the attributions to the Current
  assessment are unverified here.
- **S2:** refutation-failed. An exact instance of Corollary 3.1 at $r=4$,
  consumed within its hypotheses; the line clause holds by composition.
- **S3:** refutation-failed. An interpretation with no content beyond S2;
  the count it cites agrees with the reconstruction page.
- **S4:** refutation-failed for the mathematical claim (abc implies
  finiteness at $r=4$) and for both source characterizations; the sketch
  omits the range $\eta<1/3$ (F2), and the bibliographic clause about the
  problem page is false (F1).
- **S5:** refutation-failed under the reading "no solution lies in a
  polynomial family"; the word "sporadic" overstates (F3).
- **S6:** refutation-failed for its substantive content; the final clause
  is misworded (F4).

Limitations. The proofs of Lemma 2, Theorem 3, Corollary 3.1 and the
Problem 940 proposition are outside this review's charge and were not
graded; Theorem 3 was re-derived only as an interface check. The Current
assessment, Known results and folder index were not read. The abc
conjecture enters only as a stated hypothesis. This focused review assigns
no tier and changes no status.
