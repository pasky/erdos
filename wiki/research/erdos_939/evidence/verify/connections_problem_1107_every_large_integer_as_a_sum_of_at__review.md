---
name: research/erdos_939/evidence/verify/connections_problem_1107_every_large_integer_as_a_sum_of_at__review
title: "Independent review of the connections section: Problem 1107: every large integer as a sum of at most r+1 r-powerful numbers"
desc: |
  Refutation review of the Problem 1107 section. The target facts, the
  density-zero conclusion and the outcome survive (refutation-failed); the
  count bound O(X^(2/D)) for the totals of a Lemma 1 device and the
  s-parameter threshold are refuted-as-stated, with witnesses. Two required
  corrections, one suggested, one note.
created: 2026-09-28T18:57:32Z
updated: 2026-09-28T19:00:18Z
---

***

## Subject and independence

- **Role.** Independent reviewer in a fresh context, given only the
  assignment. The reviewer took no part in writing the connections page or
  the reconstruction page and consulted no author of either. Charge:
  refutation of the author-recorded mathematics of one section.
- **Date.** 2026-09-28T13:50:48Z, the source as it stood then (called "the
  commit" below).
- **Subject.** `wiki/research/erdos_939/connections.md`, the section whose
  H2 heading reads
  "Problem 1107: every large integer as a sum of at most r+1 r-powerful
  numbers", lines 466 to 487 (the H2 heading at line 466 to the line before
  the next H2 at line 488). No lead page is named; the section is
  self-contained on the connections page.
- **Read, and at what depth.** The section in full, line by line. The
  page's preamble and Conventions (lines 1 to 57) and the Shared results
  section (lines 58 to 302: Lemma 1, Corollary 1.1, Lemma 2, Theorem 3,
  Corollary 3.1, Proposition 4, Corollary 4.1) as inputs, read in full with
  Lemma 1's hypotheses and conclusion confirmed at every use the section
  makes of them; their own proofs are another reviewer's charge.
  `wiki/research/erdos_939/theorem_1_reconstruction.md` in full, as a
  premise at its reviewed standing. The statement blocks of
  `wiki/problems/diophantine_problems/E1107/_index.md` and
  `wiki/problems/diophantine_problems/E0941/_index.md`: the Statement, Status,
  Source, References and Formalization lines above each page's first H2;
  the Current assessment, Progress and Known Results sections were not
  read. The path listing of `library` at the commit (names only), to
  check whether a Heath-Brown 1988 source is held. The rule pages named in
  the assignment: `docs/verification.md` sections "Grading and claim
  standing", "Audit checklist" (general and Erdos-specific) and
  "Whole-claim report"; `docs/evidence.md` section "Source fidelity";
  `docs/approach_vetting.md`; `docs/math_authoring.md`.
- **Not read.** The folder's `_index.md`; everything under any `evidence/`
  folder; the page's other connection sections (lines 303 to 465 and 488
  to the end), except their H2 headings in a heading listing; every Current
  assessment, Known results, standing or acceptance text; anything outside
  the repository; no web search was made.
- **Exposures.** The one-word status entries "Open" and "Proved" on the
  problem pages' Status lines were read, because they sit inside the
  statement block between the statement and the references; nothing else
  about standing was read. Directory listings showed the file names, not
  the contents, of other untracked review files, in this folder's
  `evidence/verify/` directory and in another research folder. No other
  excluded content reached the reviewer.
- **Computation.** Exact-arithmetic sanity checks of the witnesses below
  (identity, positivity, powerfulness, coprimality, injectivity, and counts
  of distinct totals) were run in a scratch directory outside the
  repository. They support nothing on their own; every conclusion below is
  carried by the written derivation.

## Restatement

Conventions of the page, used throughout: for an integer $r\ge2$, a
positive integer is $r$-powerful when every prime dividing it does so to
exponent at least $r$; a nonzero polynomial is $r$-powerful when each of its
irreducible factors occurs with exponent at least $r$. A *Lemma 1 device* is
a tuple $(r,n,A_1,\dots,A_n,B)$ with $r\ge2$, $n\ge3$, nonzero
$A_i\in\mathbb Z[U,V]$ satisfying $A_1+\cdots+A_{n-1}=A_n$ and Lemma 1's
hypotheses (i) to (iv), and an integer $B\ge1$ divisible by every prime
dividing some coefficient $c_i$. Its *admissible points* are the pairs
$(m,B)$ with $m\ge1$, $\gcd(m,B)=1$ and $A_i(m,B)>0$ for every $i$; its
*totals* are the integers $A_n(m,B)$ at admissible points. "Values up to
$X$" is read as the number of distinct totals at most $X$; a reading as
lattice points would only weaken the statements.

- **S1 (target facts).** Problem 1107 asks, for each $r\ge2$, whether every
  sufficiently large integer is a sum of at most $r+1$ $r$-powerful numbers;
  its page records the status open and no compiled assessment; at $r=2$ the
  question is Problem 941 (every large integer a sum of at most three
  powerful numbers), whose page records the status proved; both pages cite
  Heath-Brown's 1988 paper, which the library does not hold.
- **S2 (totals of an identity).** A fixed polynomial identity
  $A_1+\cdots+A_{n-1}=A_n$ evaluated at integer points represents only the
  values of the one polynomial $A_n$ at those points.
- **S3 (count bound).** For every Lemma 1 device, the total $A_n$ is a
  nonconstant $r$-powerful *form*, hence of degree $D\ge r$, and the number
  of distinct totals at most $X$ is $O(X^{2/D})$, hence $O(X^{2/r})$, with
  the implied constant allowed to depend on the device.
- **S4 (density zero).** For every Lemma 1 device the totals have natural
  density zero: for $r\ge3$ because $O(X^{2/r})=o(X)$; for $r=2$ and $D\ge3$
  because $O(X^{2/D})=o(X)$; and for $r=2$, $D=2$ because a $2$-powerful
  polynomial of degree $2$ is a constant times the square of a linear
  polynomial, whose values are a constant times squares.
- **S5 (parameters).** For a fixed identity in $s$ integer parameters whose
  total has degree $D$, the number of distinct totals at most $X$ is
  $O(X^{s/D})$; hence the totals can have positive density only when
  $s\ge D$, and $D\ge r$, so at least $r$ free parameters are needed, at
  which point the question is the Waring-type problem for $r$-powerful
  numbers rather than a consequence of an identity.
- **S6 (outcome).** The folder's mechanism, a fixed identity with
  $r$-powerful summands under integer substitution, gives no information
  toward representing every large integer as a sum of at most $r+1$
  $r$-powerful numbers, and no next investigation is proposed.

## Checklist

- **Quantifiers and scope.** Fails at S3 and S5. S3 is quantified over
  every Lemma 1 device but holds only for devices whose total confines the
  parameters to a box of side $\asymp X^{1/D}$, such as the Theorem 1 total
  $(U^r+V^r)^r$; Lemma 1 does not require that. S5 is quantified over every
  $s$-parameter identity and fails already at $r=2$ (Findings F1, F2). S1,
  S2, S4 and S6 carry their quantifiers correctly.
- **Circularity.** None. Nothing in the section assumes Problem 1107 or an
  equivalent statement.
- **Model and convention changes.** One unproved transfer at S3: Lemma 1's
  class of polynomials (any nonzero $A_i\in\mathbb Z[U,V]$ meeting (i) to
  (iv)) is replaced by "form", and the count is then argued as if the form
  were definite; neither the homogeneity nor the definiteness is a
  hypothesis of Lemma 1 (Findings F1, F3). The powerfulness conventions of
  the page and of the problem pages agree ($1$ is $r$-powerful; $0$ is not
  used).
- **Finite and statistical overreach.** None. The section makes no finite
  check and no heuristic average; the reviewer's numerical checks are
  sanity checks and are not used as evidence.
- **Uniformity.** The $O$-constants in S3 and S5 are device-dependent,
  which the section leaves implicit; since the conclusions drawn are
  qualitative ($o(X)$), this does not affect them. No other constant or
  bound is claimed uniform in a family.
- **Extremal conclusions.** Only the degree bound $D\ge r$ for a nonconstant
  $r$-powerful polynomial, which is correct: a nonconstant irreducible
  factor of degree at least $1$ occurs with exponent at least $r$.
- **Consequences and composition.** Two "so" sentences fail: "so its values
  up to $X$ number $O(X^{2/D})$" lacks the definiteness bridge, and "so a
  positive proportion of the integers needs at least $D\ge r$ free
  parameters" is false as stated. The final "therefore" (S6) survives, but
  only through the corrected argument given under Weakest steps, not
  through S3 and S5 as written. Lemma 1 is used within its hypotheses
  except for the added words "nonconstant" and "form".
- **Computation.** Not applicable to the section, which has none. The
  reviewer's checks used exact integer arithmetic.
- **Reproduction.** Not applicable: the section states no rerun command and
  no coverage claim.
- **Source and verdict fidelity.** S1 is faithful where checkable: the
  section's paraphrase of Problem 1107 matches the page's Statement; the
  $r=2$ case is the Statement of Problem 941; both reference lists carry
  the same Heath-Brown 1988 entry; no library folder at the commit holds
  that paper (the held Heath-Brown items are from 1997, 2000, 2009 and a
  2018 joint paper). The clause "no compiled assessment" concerns the
  excluded Current assessment section and was not verified. No external
  theorem is invoked by the section.

## Weakest steps

**W1: the count bound of S3, re-derived.** The bound $O(X^{2/D})$ follows
when $A_n(m,B)\le X$ at admissible points forces $\max(m,B)\le CX^{1/D}$ for
a constant $C$: the totals are then among the values at $O(X^{2/D})$ lattice
points. That confinement holds for the Theorem 1 device: $N=(m^r+B^r)^r\le X$
gives $m^r+B^r\le X^{1/r}$, so $m,B\le X^{1/r^2}$, and the totals at most
$X$ number $O(X^{2/r^2})$ with $D=r^2$, as Corollary 1.1 also records for
its tuples. It fails as soon as the total does not confine the parameters,
and Lemma 1 admits such totals. Witness A: $r=2$, $n=3$,

$$
A_1=(U^2-V^5)^2,\qquad A_2=4U^2V^5,\qquad A_3=(U^2+V^5)^2 .
$$

The identity $A_1+A_2=A_3$ is $(x-y)^2+4xy=(x+y)^2$ at $x=U^2$, $y=V^5$.
Hypothesis (i): $A_1=1\cdot(U^2-V^5)^2$, $A_2=4\cdot U^2V^5$ with exponents
$2,5\ge2$, $A_3=1\cdot(U^2+V^5)^2$. Hypothesis (ii): the only coefficient of
absolute value above $1$ is $c_2=4$, and $V^2\mid A_2$. Hypothesis (iii):
$K=U^2-V^5$ has $K(U,0)=U^2$ and $K(0,V)=-V^5$. Hypothesis (iv):
$A_2=c_2U^aV^b$ with $(a,b)=(2,5)$, $a+b\ge1$. The admissible $B$ are the
even integers; the admissible $m$ are the odd integers coprime to $B$, and
$A_1(m,B)>0$ for all of them because $m^2$ is odd and $B^5$ even. Lemma 1
then makes $(m^2-B^5)^2$ and $4m^2B^5$ jointly coprime $2$-powerful integers
with $2$-powerful sum; this was also confirmed directly on samples. The
total $A_3$ is nonconstant and $2$-powerful but not homogeneous, of degree
$D=10$, so S3 asserts $O(X^{1/5})$ distinct totals up to $X$.

Lower bound. Put $Y=X^{1/2}$, so a total $(m^2+B^5)^2$ is at most $X$ exactly
when $n:=m^2+B^5\le Y$. Take $B=2q$ for an odd prime $q\ge5$ with
$B\le(Y/2)^{1/5}$, and odd $m\le2B^2$ with $q\nmid m$. There are $B^2$ odd
integers in $[1,2B^2]$, at most $2B^2/q+1=4B+1$ of them divisible by $q$, so
at least $B^2-4B-1\ge B^2/2$ admissible $m$ (as $B\ge10$). For these,
$m^2+B^5\le4B^4+B^5\le2B^5\le Y$. The map $(m,B)\mapsto m^2+B^5$ is injective
on the set $\{m\le2B^2\}$, because $B^5<m^2+B^5\le B^5+4B^4<(B+1)^5$ forces
$B=\lfloor n^{1/5}\rfloor$ and then $m=(n-B^5)^{1/2}$. Hence the distinct
totals at most $X$ number at least $\sum_q(2q)^2/2=2\sum_qq^2$ over the odd
primes $5\le q\le Z:=(Y/2)^{1/5}/2$. Restricting to $q\in(Z/2,Z]$ and using
Chebyshev's bound $\pi(Z)-\pi(Z/2)\gg Z/\log Z$, the count is
$\gg Z^3/\log Z\asymp Y^{3/5}/\log Y=X^{3/10}/\log X$, which is not
$O(X^{1/5})$. (The true order is $X^{7/20}$: the sanity count of all
admissible distinct totals up to $X$ was about $0.18\,X^{7/20}$ for each
$X=10^{12},10^{15},\dots,10^{24}$, against $X^{1/5}\approx6.3\cdot10^4$ at
$X=10^{24}$.) So S3 is false for this device. The homogeneous inference
alone, "an $r$-powerful form of degree $D$ has $O(X^{2/D})$ values up to
$X$", also fails: $U^{r+1}V^r$ has degree $2r+1$ and takes the
$\lfloor X^{1/r}\rfloor$ values $B^r\le X$ at the points $(1,B)$, and
$1/r>2/(2r+1)$. This form is not a Lemma 1 total; it shows that
definiteness, not degree, carries the bound.

**W2: the density-zero conclusion of S4, re-derived independently.** Lemma
1's conclusion states that every total $A_n(m,B)$ of a Lemma 1 device is an
$r$-powerful integer. The $r$-powerful integers up to $X$ number
$O_r(X^{1/r})$: every $r$-powerful $n$ can be written as
$n=a_0^ra_1^{r+1}\cdots a_{r-1}^{2r-1}$ with positive integers $a_i$ (for a
prime $p$ with $v_p(n)=rk+i$, $k\ge1$, $0\le i\le r-1$, put $p^{k}$ into
$a_0$ if $i=0$ and otherwise $p^{k-1}$ into $a_0$ and $p$ into $a_i$), so the
count is at most

$$
\sum_{a_1,\dots,a_{r-1}\ge1}\bigl(X/(a_1^{r+1}\cdots a_{r-1}^{2r-1})\bigr)^{1/r}
=X^{1/r}\prod_{i=1}^{r-1}\zeta(1+i/r).
$$

Hence the totals of every Lemma 1 device have density zero for every
$r\ge2$, whatever the degree, homogeneity or definiteness of $A_n$, and the
same holds for the Theorem 1 device with the sharper count of W1. A second
route needs no arithmetic conclusion of Lemma 1 at all and covers any number
of parameters: if $A_n=c\prod_{j=1}^kH_j^{e_j}$ with every $e_j\ge r$, each
positive value is $|c|\prod_j|h_j|^{e_j}$ with nonzero integers $h_j$, and
the number of $k$-tuples of positive integers with
$\prod_jh_j^{e_j}\le X/|c|$ is at most the number with
$\prod_jh_j\le(X/|c|)^{1/r}$, which is at most
$(X/|c|)^{1/r}(1+\tfrac1r\log(X/|c|))^{k-1}$ by induction on $k$; with the
$2^k$ sign patterns this is $O(X^{1/r}(\log X)^{k-1})=o(X)$. The $r=2$,
$D=2$ clause of S4 is true as stated (a $2$-powerful polynomial of degree $2$
is $c\,\ell^2$ with $\ell$ of degree $1$, and its values are $c$ times
squares); whether a Lemma 1 device with such a total exists was not
examined, since the clause is harmless either way. S4 therefore holds, but
by an argument the section does not give; its own route passes through S3.

**W3: the parameter threshold of S5, re-derived.** For a polynomial
$F\in\mathbb Z[U_1,\dots,U_s]$ of degree $D$, the count $O(X^{s/D})$ follows
when $F\le X$ at the relevant points confines every parameter to
$O(X^{1/D})$, a definiteness property that the degree alone never supplies.
Witness B, at $r=2$: the identity $A_1+A_2+A_3=A_4$ with

$$
A_1=U_1^2,\qquad A_2=U_2^2,\qquad A_3=(U_3U_4U_5)^2,\qquad
A_4=U_1^2+U_2^2+(U_3U_4U_5)^2 ,
$$

in $s=5$ parameters, whose total has degree $D=6$, and whose summands are
positive $2$-powerful integers at every point of $\mathbb Z_{\ge1}^5$. Its
totals contain every sum of three positive squares (take $U_4=U_5=1$). By
the three-square theorem (Legendre), an integer is a sum of three squares of
integers exactly when it is not of the form $4^a(8b+7)$; the integers up to
$X$ of that form number at most
$\sum_{a\ge0}(X/(8\cdot4^a)+1)\le X/6+O(\log X)$, so at least
$\tfrac56X-O(\log X)$ integers up to $X$ are sums of three squares. Those
among them that are not sums of three *positive* squares are sums of two
squares, and there are at most $\tfrac\pi4X+O(X^{1/2})$ pairs
$(a,b)$ of nonnegative integers with $a^2+b^2\le X$. Hence at least
$(\tfrac56-\tfrac\pi4)X-O(X^{1/2})$ integers up to $X$ are totals, and
$\tfrac56-\tfrac\pi4>0.047$: the totals have positive lower density with
$s=5<6=D$ (the sanity count gave $83.3$ percent of the integers up to
$2\cdot10^5$). Both halves of S5 fail: the count is not $O(X^{5/6})$, and a
positive proportion does not need $D$ free parameters. Under the other
possible reading, in which the total must itself be an $r$-powerful
polynomial as in Lemma 1, the second route of W2 gives
$O(X^{1/r}(\log X)^{k-1})$ totals for every $s$, so no number of parameters
reaches a positive proportion, and the sentence's threshold "at least
$D\ge r$ free parameters, at which point the question is a Waring-type
problem" describes a transition that does not occur. The padding in Witness
B is deliberate: it isolates the claim that the degree of the total controls
the count, which is the claim S5 makes.

## Strongest attack

- **S1.** Attempted to find a discrepancy between the section's paraphrases
  and the problem pages: the exponent range $r\ge2$, the phrase "at most
  $r+1$", the definition of $r$-powerful, the $r=2$ specialization to three
  powerful numbers, and the reference entries were compared word by word
  with the statement blocks; the library path listing was searched for a
  1988 Heath-Brown source. No discrepancy. The clause "no compiled
  assessment" could not be attacked within the read set.
- **S2.** No attack applies: at a point of $\mathbb Z^s$ the summands of the
  identity add to the value of $A_n$ there, by the identity.
- **S3.** Refuted by Witness A (W1). Before finding it, the reviewer tried
  to save the statement for homogeneous totals: for a form with no real
  root direction in the closed positive quadrant the bound holds, and for
  the squares or higher powers of an irreducible binary form of degree at
  least $3$ it also holds because the region $|F|\le1$ has finite area; but
  neither property is a hypothesis of Lemma 1, and $U^{r+1}V^r$ shows the
  homogeneous inference itself is false.
- **S4.** Attempted to build a Lemma 1 device whose totals have positive
  density: impossible, since every total is $r$-powerful and the
  $r$-powerful integers have density zero (W2). Attempted to break the
  $r=2$, $D=2$ clause: a $2$-powerful polynomial of degree $2$ has exactly
  one irreducible factor, of degree $1$ and exponent $2$, so the clause
  stands. Refutation failed.
- **S5.** Refuted by Witness B (W3); the alternative reading was also
  attacked and found to make the threshold sentence describe a transition
  that never happens.
- **S6.** Attempted to read "the mechanism" so widely that Witness B counts
  as an instance: it does not, since the folder's mechanism is defined by
  hypotheses (iii) and (iv), which force an $r$-powerful total, and even
  under the widest reading the identity of Witness B contributes nothing
  beyond the classical theorem it restates. Refutation failed; the sentence
  survives through W2, not through S3 and S5.

## Premises

- **Lemma 1 (the monomial-substitution transfer), connections page lines 60
  to 127.** Interface used: hypotheses (i) to (iv) define the class of
  devices; the conclusion "the sum $A_n(m,B)$ is $r$-powerful" for every
  admissible point. Confirmed at each use. The section adds "nonconstant"
  and "form" to the total, neither of which the lemma states. Read in full;
  its proof is another reviewer's charge and was not relied on beyond its
  stated conclusion.
- **Corollary 1.1 (two free parameters), lines 129 to 155.** Used only to
  cross-check the count $O(X^{2/r^2})$ for the Theorem 1 device. Read in
  full; not otherwise relied on.
- **Theorem 1 reconstruction page**
  (`research/erdos_939/theorem_1_reconstruction.md`). Premise at its
  reviewed standing: the identity, its total $(U^r+V^r)^r$ after the
  substitution $X=U^r$, $Y=V^r$, and the point set. Read in full. The
  section uses it only as the concrete instance of Lemma 1.
- **Problem pages E1107 and E0941.** Statement blocks only, as listed under
  Subject. Held in the repository.
- **Heath-Brown 1988.** Cited by both problem pages; not held in the
  library at the commit (path listing checked); not needed by the section,
  which invokes no result from it.
- **Classical inputs used by the reviewer's witnesses,** stated exactly
  where used: the three-square theorem (Legendre) in W3; Chebyshev's lower
  bound for the number of primes in $(Z/2,Z]$ in W1; the elementary
  representation of $r$-powerful integers and the tuple count in W2, both
  proved inline. No held PDF was needed.

## Findings

- **F1 (required).** Location, lines 477 to 480: "In the two-variable
  device of Lemma 1 the total $A_n(U,V)$ is a nonconstant $r$-powerful form,
  hence of degree $D\ge r$, so its values up to $X$ number
  $O(X^{2/D})\le O(X^{2/r})$, which is $o(X)$ for $r\ge3$". Defect: the
  bound $O(X^{2/D})$ needs the total to confine the parameters to a box of
  side $\asymp X^{1/D}$; Lemma 1 requires neither homogeneity nor
  definiteness, and the bound fails for admissible devices. Witness: the
  device $(U^2-V^5)^2+4U^2V^5=(U^2+V^5)^2$ at $r=2$, whose distinct totals
  up to $X$ number $\gg X^{3/10}/\log X$ against the asserted $O(X^{1/5})$
  (W1). Proposed replacement: "In any device of Lemma 1 every total
  $A_n(m,B)$ is an $r$-powerful integer, and the $r$-powerful integers up to
  $X$ number $O_r(X^{1/r})$, so the totals have density zero for every
  $r\ge2$, whatever the degree of $A_n$; for the Theorem 1 total
  $(U^r+V^r)^r$ the count is $O(X^{2/r^2})$, because $N\le X$ forces
  $m,B\le X^{1/r^2}$." The clause about $r=2$ and degree $2$ then becomes
  unnecessary.
- **F2 (required).** Location, lines 481 to 484: "With $s$ parameters the
  count is $O(X^{s/D})$, so a positive proportion of the integers needs at
  least $D\ge r$ free parameters, at which point the question is a
  Waring-type problem for $r$-powerful numbers and not an identity." Defect:
  false as stated; the degree of the total does not control the count.
  Witness: $U_1^2+U_2^2+(U_3U_4U_5)^2$, five parameters, degree six, with
  totals of lower density at least $\tfrac56-\tfrac\pi4$ (W3). Under the
  reading in which the total must be $r$-powerful, no number of parameters
  yields a positive proportion, so the stated threshold does not exist.
  Proposed replacement: "An identity whose total is an $r$-powerful
  polynomial, in any number of parameters, has totals of density zero by
  the same count. Without that requirement the total is only the sum of
  its $r$-powerful summands, and representing a positive proportion of the
  integers by it is the Waring-type problem for $r$-powerful numbers
  itself, not a consequence of the identity."
- **F3 (suggested).** Location, line 478: "a nonconstant $r$-powerful
  form". Lemma 1 admits non-homogeneous polynomials (Witness A) and does
  not exclude a constant total, which would give a single value. Replace
  "form" by "polynomial" and either drop "nonconstant" or say that a
  constant total gives one value; with F1 applied the degree plays no role.
- **F4 (note).** Location, lines 468 to 474, the Target paragraph. The
  paraphrase of Problem 1107, the coincidence with Problem 941 at $r=2$, the
  shared reference and "not held here" were verified against the statement
  blocks and the library path listing. The clause "no compiled assessment"
  refers to the excluded Current assessment section and is unverified by
  this review. No correction is proposed.

## Verdict

- **S1 (target facts): refutation-failed** for every clause within the
  read set; the clause "no compiled assessment" is unverified, not refuted.
- **S2 (totals of an identity): refutation-failed.**
- **S3 (count bound): refuted-as-stated.** Witness A is a Lemma 1 device
  with $\gg X^{3/10}/\log X$ distinct totals up to $X$ where $O(X^{1/5})$ is
  asserted.
- **S4 (density zero): refutation-failed.** The statement is true, but the
  section's argument for it passes through S3; W2 supplies an independent
  proof, so the verdict is on the statement and the section's own proof
  needs the replacement in F1.
- **S5 (parameters): refuted-as-stated.** Witness B has five parameters, a
  total of degree six, and totals of positive lower density.
- **S6 (outcome): refutation-failed.** The mechanism's totals are
  $r$-powerful integers, a set of density zero, so the mechanism cannot
  address Problem 1107; the section's conclusion stands on that ground.

Limitations. The review covers only the Problem 1107 section and the
interfaces it consumes; the proofs of Lemma 1 and of the other shared
results, and the other connection sections, were not examined. The
witnesses use two classical theorems, stated exactly where used, and no
held source. The numerical checks were sanity checks and are not retained
as evidence. This focused review assigns no tier and changes no status.
