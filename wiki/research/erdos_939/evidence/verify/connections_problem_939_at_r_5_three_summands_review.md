---
name: research/erdos_939/evidence/verify/connections_problem_939_at_r_5_three_summands_review
title: "Independent review of the connections section: Problem 939 at r = 5: three summands"
desc: |
  Refutation review of the r = 5 section and its lead. Refutation-failed for
  the transfer's value statement, the exclusion of proportional summands,
  the minimal complex degree and the degree-10 search normalization; proof
  defective, statement unresolved, for the infinitude clause and the closing
  implications from a binary-form nonexistence proof; refuted-as-stated for
  the degree-15 coverage sentence and the lead's restatement of the
  three-term obstruction. Two required corrections, six suggested.
created: 2026-09-28T18:44:49Z
updated: 2026-09-28T20:41:57Z
---

***

## Subject and independence

**Role.** The reviewer is an independent examiner in a fresh context, given
only this assignment, who took no part in writing the connections page, the
lead page or the reconstruction page, and who read no earlier review or grade
of this folder. The charge is refutation; no tier is assigned and no status is
changed.

**Subject.** The source as it stood on 2026-09-28T13:50:48Z (called "the
commit" below). The page
`wiki/research/erdos_939/connections.md`, section
"Problem 939 at r = 5: three summands", lines 339–405 (its H2 heading through
the line before the next H2 at line 406), and the lead page
`wiki/research/leads/quintic_powerful_identity_route/_index.md` at the same
commit, read in full; the lead's route rests on that section.

**Reading and depth.** The section was read in full and every sentence with
mathematical content was re-derived. The lead page was read in full. The
connections page's preamble and Conventions (lines 1–57) and its "Shared
results" section (lines 58–302: Lemma 1, Corollary 1.1, Lemma 2, Theorem 3,
Corollary 3.1, Proposition 4, Corollary 4.1) were read as inputs: their
statements, hypotheses and conventions were confirmed at every use below;
their proofs are another reviewer's subject and receive no credit here, except
that the identity of Corollary 4.1 was recomputed exactly as a sanity check.
The reconstruction page `wiki/research/erdos_939/theorem_1_reconstruction.md`
was read in full as a premise at its stated standing (reviewed as it stood
on 2026-09-28T05:03:27Z with corrections applied since). Of the problem page
`wiki/problems/diophantine_problems/E0939/_index.md` the Statement paragraph (lines
18–24) is the only part used. For the four-summand bound, the library card
`corvaja_zannier_2011_abcd_function_fields/_index.md`, its result page
`recalled_abc_abcd_bounds.md`, and printed page 438 of the held PDF (text
extraction of PDF page 3) were read. Guidance read: `docs/verification.md`
"Whole-claim report", "Audit checklist" and "Grading and claim standing",
`docs/approach_vetting.md`, `docs/evidence.md` "Source fidelity", and
`docs/math_authoring.md`.

**Not read.** The folder's `_index.md`; everything under any `evidence/`
folder, including the lead's two search scripts (both the section and the lead
name them, so the counts they report are treated below as author-recorded
exploratory statements and are not checked); the r = 4 section and every other
section of the connections page; any Current assessment, Known results,
standing or acceptance text; any review or grade; nothing outside the
repository and no web search.

**Exposure.** Two disclosures. First, the problem page's Statement paragraph is
followed on the same page by a "Status" paragraph (lines 27–36) that was
printed together with it and read before it could be skipped; it characterizes
the standing of the three parts of the problem at r = 4, 5 and at least 6 and
names formal records. Nothing from it is used below beyond what the section
itself states about the target. Second, the library card and result page were
read whole, so their "Extracted interface", "Reading coverage", "Attribution"
and "Bears on" paragraphs reached the reviewer in addition to the provenance
paragraph and statement section; they carry reading-depth and attribution
facts about the source and no standing text about the subject. Third, a
listing of the working tree's untracked files showed the file names of
parallel reviews of other sections and folders; none was opened. No other
exposure.

**Computation.** Elementary re-derivations, reproduced in the prose. One short
exact symbolic check (computer algebra, exact arithmetic over the field
$\mathbb Q(\omega)$) confirmed the Proposition 4 identity at $(a,b,c)=(1,1,-2)$,
the order and eigenvalues of the substitution $M$, the invariance of
$U^2-UV+V^2$ under $M$, and the linear independence of the coefficient vectors
of fifth powers of four linear forms with distinct roots. No script is retained
and no verdict depends on it.

## Restatement

Conventions as on the connections page: for $r\ge2$, a positive integer is
$r$-powerful if every prime dividing it does so to exponent at least $r$ ($1$
is $r$-powerful); a family is jointly coprime if the greatest common divisor of
all its members is $1$; a nonzero polynomial over a field of characteristic
zero is $r$-powerful if every root in an algebraic closure has multiplicity at
least $r$ (constants are $r$-powerful); $n_0(f)$ is the number of distinct
complex roots of $f\in\mathbb C[t]$. Hypotheses (i)–(iv) are those of Lemma 1.
A binary form is a homogeneous polynomial in $U,V$.

**S1 (Target).** At $r=5$ the two questions of Problem 939 are: (Q1) can a sum
of three coprime $5$-powerful positive integers be $5$-powerful, and (Q2) are
there at most finitely many such sums. Q1 is settled affirmatively by the two
examples recorded on the problem page; Q2 is open. A forum-reported search
found no further solution below $10^{16}$ except possibly ones in which every
pair of summands shares a factor. "Coprime" is read as joint coprimality.

**S2 (Transfer at r = 5).** Let $A_1+A_2+A_3=A_4$ in $\mathbb Z[U,V]$ satisfy
(i)–(iv) with $r=5$; let $B\ge1$ be divisible by every prime dividing some
$c_i$, with every $A_i(U,B)$, $1\le i\le4$, a polynomial in $U$ with positive
leading coefficient. (S2a) For every sufficiently large integer $m$ coprime to
$B$, the values $A_1(m,B),A_2(m,B),A_3(m,B)$ are jointly coprime $5$-powerful
positive integers whose sum $A_4(m,B)$ is $5$-powerful. (S2b) The sums take
infinitely many values, so Q2 has the answer "no". The section names the
hypothesis "(i)–(iv) and the positivity clause".

**S3 (Shape).** Under the hypotheses of S2 no two of $A_1,A_2,A_3,A_4$ are
proportional. Hence no proper subsum of $A_1+A_2+A_3-A_4$ vanishes, the four
terms have no common factor, and the four-summand bound
$\max\deg\le3(n_0-1)$ applies, $\deg$ and $n_0$ being the maximal degree and
the number of distinct roots of the product for the one-variable polynomials
obtained from the terms. That bound is satisfiable by $5$-powerful terms of any
degree $D\ge3$, so it does not exclude such identities.

**S4 (Minimal complex degree).** Over $\mathbb C$, a four-term identity
$F_1+F_2+F_3+F_4=0$ of $5$-powerful binary forms with no vanishing proper
subsum and no common factor exists in degree $10$ (Proposition 4 at
$(a,b,c)=(1,1,-2)$, imported) and in no smaller degree; the section's
justification treats degree $5$ by the linear independence of the coefficient
vectors of fifth powers of linear forms with distinct roots ("the Vandermonde
determinant of their roots").

**S5 (Non-reality, imported).** The degree-$10$ identity of Corollary 4.1
cannot be made real by any projective linear change of variables combined
with rescaling of the four forms, so it yields no four-term identity in
$\mathbb Q[U,V]$.

**S6 (The gap).** The route's remaining gap is exactly whether a four-term
identity of $5$-powerful binary forms with rational terms exists.

**S7 (Search coverage).** (S7a) Every $5$-powerful binary form of degree $10$
is a constant times the fifth power of a quadratic form; over $\mathbb C$
constants are fifth powers and over $\mathbb R$ signs times fifth powers, so a
search of $Q_1^5+Q_2^5+Q_3^5+Q_4^5=0$ in quadratic forms, with $Q_4$ fixed to
one representative of each orbit of the projective linear group, covers every
four-term identity of degree $10$ with no vanishing proper subsum and no
common factor. (S7b) The degree-$15$ search covered only the shape "fifth
power of a cubic"; the shapes $L^6M^9$, $L^7M^8$, $L^5M^{10}$ were not
searched. (S7c) The cyclic search uses $M(U,V)=(-V,U-V)$, of order three and
the rational form of the diagonal substitution of Proposition 4; the reported
outcomes (one nondegenerate complex class in degree $10$ matching Proposition
4, nothing over $\mathbb R$, nothing in degree $15$, nothing for cubics in the
cyclic shape) are exploratory and not evidence.

**S8 (What it does not give).** No solution at $r=5$ and no bound on their
number; the two known examples are values of no identity found; the forum
bound is mild evidence against a rational identity of degree $10$ with small
coefficients.

**S9 (Consequences).** (S9a) A rational identity found by search, checked
against (i)–(iv) and positivity, refutes finiteness at $r=5$. (S9b) A proof
that no real four-term identity of $5$-powerful binary forms exists closes the
polynomial route, leaving $r=5$ to constructions of the kind that settled
$r=3$.

Lead page:

**L1 (Target and conventions).** As S1, with "coprime" read as joint
coprimality "as the problem page records the site and the formal catalog read
it"; Q2 is answered negatively for every $r\ge6$ by the reconstructed binomial
construction; "its $r=4$ case is excluded from every polynomial route by the
theorem recalled below".

**L2 (Transfer restated).** Lemma 1 at $r=5$, with (iv) restated as "$A_2$ is
a monomial" (no $a+b\ge1$), no $m\ge1$, and "then infinitely many distinct
sums arise" drawn from positive leading coefficients alone.

**L3 (Obstruction restated).** "No identity $a+b=c$ of pairwise coprime
$r$-powerful polynomials with $r\ge3$ exists"; consequence as S3; the bound
with $n_0$ the number of distinct linear factors of the product permits every
degree at least $3$.

**L4 (Complex identity restated).** As S4 and S5.

**L5 (Premise and deduction).** (P): an identity $A_1+A_2+A_3=A_4$ in
$\mathbb Z[U,V]$ satisfying the transfer's hypotheses with $r=5$, with positive
leading coefficients in $U$ for some admissible $B$. Under (P) the transfer
produces infinitely many jointly coprime triples of $5$-powerful integers with
$5$-powerful sum; pairwise distinctness of the summands holds for all but
finitely many $m$ whenever $A_i(U,B)\ne A_j(U,B)$.

**L6 (Known about the premise).** Over $\mathbb C$ the premise's polynomial
part is satisfiable in the least possible degree $10$; over $\mathbb R$ no
identity of degree $10$ and none in the degree-$15$ pure shape was found; the
mixed shapes of degree $15$ and all degrees above $15$ were not searched.

**L7 (Exploratory computation).** Description of the two scripts, the gauge
representatives, the acceptance thresholds and the table of runs.

**L8 (Consequential gap).** (P) is not established; "A proof that no four-term
identity of $5$-powerful binary forms with real terms exists would close this
route".

**L9 (Next step).** Two bounded computations; a Gröbner-basis or resultant
computation in degree $10$ "would turn the numerical absence of a real
degree-$10$ identity into a proof"; a found and checked rational identity
refutes finiteness; "a proof of nonexistence in all degrees would close the
route"; a bounded negative result establishes nothing about the target.

**L10 (Standing).** Author-recorded, unreviewed, no tier, no status change.

## Checklist

- **Quantifiers and scope.** One defect. The closing implications S9b, L8 and
  L9 quantify over binary forms, which are homogeneous, while Lemma 1 and the
  premise (P) quantify over all of $\mathbb Z[U,V]$ (F1). The infinitude in
  S2b and L5 needs the nonconstancy of $A_4(U,B)$, a separate hypothesis of
  Lemma 1 that "the positivity clause" and (P) do not carry (F3). Elsewhere
  "for all sufficiently large $m$", "infinitely many" and "at most finitely
  many" are used at their correct strength.
- **Circularity.** None. No statement assumes the finiteness question or its
  negation; the transfer's conclusion enters no hypothesis; the searches are
  labeled as not evidence in both documents.
- **Model and convention changes.** One defect. Theorem 3 concerns pairwise
  coprime polynomials in one variable over $\mathbb C$, not all constant; the
  section applies it to two-variable integer polynomials with no coprimality
  checked (F2). The bridge exists and is written out in W1. The passage from
  the integer question to polynomial identities goes through Lemma 1, whose
  interface is confirmed at each use; the joint-coprimality reading of the
  problem statement is stated in the lead, not in the section (F9). The
  translation of the $S$-unit height bound to polynomials (height equal to the
  maximal degree when there is no common factor; support the distinct roots
  together with infinity) matches the library page and printed page 438.
- **Finite and statistical overreach.** None as a mathematical claim; both
  documents say the finite searches leave the universal question open. "Mild
  evidence" in S8 is heuristic and labeled so (F8). The description of the
  degree-$15$ coverage misstates one shape (F4).
- **Uniformity.** Not applicable in substance: the only constants are the
  coefficients $1$ and $3$ of the recalled bounds, used exactly as recalled,
  and no bound over an infinite family is claimed.
- **Extremal conclusions.** "Smallest possible degree, $10$" (S4, L6) was
  checked in its own units: the common degree $D$ of the four forms is an
  integer at least $5$, and $5\le D\le9$ is excluded once the independence
  argument is stated for $D$-th powers of linear forms; the parenthetical
  treats only $D=5$ and omits the common-factor exception (F5). The conclusion
  survives.
- **Consequences and composition.** Each "hence" was attacked separately.
  S2b composes Lemma 1 with the nonconstancy hypothesis it does not name
  (F3) and with the joint-coprimality reading (F9). S3's "so all four terms
  are genuinely distinct and the bound applies" composes Theorem 3 through an
  unwritten bridge (F2). S9b, L8 and L9's closing implications do not follow
  from anything on either page (F1). L2 and L3 restate imported results with
  hypotheses dropped (F6). L1's "every polynomial route" exceeds Corollary
  3.1's recorded scope (F7). L9's "would turn ... into a proof" omits the
  real-algebraic step (F10).
- **Computation.** The section's arithmetic was re-derived exactly: eleven
  coefficient equations in degree $10$ and $5d+1$ in degree $d$; the bound
  $D\le3(4D/5-1)$ holding exactly for $D\ge15/7$, hence for integers $D\ge3$;
  the partitions of $15$ into parts at least $5$; the identity of Corollary
  4.1 over $\mathbb Q(\omega)$; the order and eigenvalues of $M$. The numerical
  searches are floating-point iterations with acceptance thresholds, labeled
  exploratory and outside the read set; no claim about their coverage of the
  complex or real solution set is checked here.
- **Reproduction.** The section states no rerun command; the lead's usage line
  and its table refer to scripts under an excluded evidence folder and were
  not rerun. The reported counts are treated as author-recorded exploratory
  statements; no verdict below rides on them.
- **Source and verdict fidelity.** The four-summand bound is characterized as
  the library page records it and as printed page 438 recalls it:
  $H(1:u:v:z)\le3\chi$ when "no subsum on the right vanishes", the three-term
  bound $H(1:u:v)\le\chi$ when $u,v$ are not both constant, with
  $\chi=2g-2+|S|$. The lead's gloss with $n_0$ the number of distinct linear
  factors is a valid weakening of the sharp form $3(n_0-2)$ for forms (see
  Premises). Theorem 1 of the reconstruction is cited within its scope
  ($r\ge6$). Lemma 1, Theorem 3, Proposition 4 and Corollary 4.1 are cited at
  their stated standing. The lead's literal restatement of Theorem 3 omits
  "not all constant" (F6). The standing sentences ("author-recorded",
  "assigns no tier", "changes no status") are accurate.

## Weakest steps

**W1. The shape constraint (S3, L3) — the bridge to Theorem 3.** Let
$A_1+A_2+A_3=A_4$ satisfy (i)–(iv) with $r=5$ and let $(m,B)$ be admissible
with all four values positive.

*Step 1: $A_1$ and $A_2$ are coprime in $\mathbb C[U,V]$.* $A_1=K^5$ and
$A_2=c_2U^aV^b$, whose only prime factors are $U$ and $V$. If $U$ divided $K$
then $K(0,V)=0$, against $K(0,V)=\pm V^{d'}$; if $V$ divided $K$ then
$K(U,0)=0$, against $K(U,0)=\pm U^d$. In particular $A_1$ and $A_2$ are not
proportional, since $a+b\ge1$ makes $A_2$ nonconstant.

*Step 2: merging a proportional pair leaves a coprime pair.* Suppose
$A_j=\lambda A_i$ for some $i\ne j$; then $\lambda\in\mathbb Q$ because both
lie in $\mathbb Z[U,V]$. If the pair is $(A_1,A_3)$, $(A_1,A_4)$, $(A_2,A_3)$
or $(A_2,A_4)$, merging gives a three-term identity whose terms are
$(1\pm\lambda)A_1$ or $(1\pm\lambda)A_2$, the other of $A_1,A_2$, and the
remaining term; the merged coefficient is nonzero, since $1\pm\lambda=0$ would
mean $A_1+A_3=0$, $A_4=A_1$ (so $A_2+A_3=0$), $A_2+A_3=0$ or $A_4=A_2$ (so
$A_1+A_3=0$), each a two-term subsum that vanishes identically and so at
$(m,B)$, impossible for positive values. If the pair is $(A_3,A_4)$, the
identity becomes $A_1+A_2=(\lambda-1)A_3$, and $\lambda=1$ would give
$A_1+A_2=0$, impossible likewise. In every case the three-term identity
contains a rational multiple of $A_1$ and a rational multiple of $A_2$, a
coprime pair by Step 1; in a three-term identity $a+b=c$ a common factor of
two terms divides the third, so the three terms are pairwise coprime. Each
term is a rational constant times a $5$-powerful polynomial, hence
$5$-powerful.

*Step 3: specialization to one variable.* Theorem 3 is stated over
$\mathbb C[t]$. Every $H_{ij}$ and $K$ is a nonzero polynomial in
$\mathbb Z[U,V]$; viewed as a polynomial in $U$ with coefficients in
$\mathbb Z[V]$ it vanishes identically in $U$ only at the finitely many roots of
its nonzero coefficients. Choose $v_0\in\mathbb C\setminus\{0\}$ outside these
finite sets. Then each term specialized at $V=v_0$ is a nonzero constant times
a product of powers, with exponents at least $5$, of nonzero polynomials in
$\mathbb C[U]$, so every root has multiplicity at least $5$: the specialized
terms are $5$-powerful in $\mathbb C[U]$. The specialized multiples of $A_1$
and $A_2$ are coprime because $K(0,v_0)=\pm v_0^{d'}\ne0$, so the specialized
three-term identity is pairwise coprime as in Step 2. If $a\ge1$ the
specialized monomial $c_2v_0^bU^a$ is nonconstant. If $a=0$ then $b\ge5$;
specialize $U=u_0\ne0$ instead, where $c_2u_0^0V^b$ is nonconstant and
$K(u_0,0)=\pm u_0^d\ne0$ gives the coprimality. Theorem 3 now yields $r=2$,
against $r=5$. So no two of the four terms are proportional. $\square$

The same specialization serves the four-summand bound: the specialized terms
are nonzero (so no proper subsum vanishes, a vanishing subsum being a
polynomial identity in $U,V$ that a generic specialization would preserve
only if it held identically), and the specialized $A_1,A_2$ are coprime, so
the four have no common factor; the height is then the maximal degree and the
support is the set of distinct roots together with infinity.

**W2. The closing implications (S6, S9b, L8, L9) — the homogeneity gap.**
Lemma 1 requires nothing of the degrees of the monomials in the $A_i$, and
(iii) is satisfied by inhomogeneous $K$: $K=U^2+U^2V^3+V^2$ has
$K(U,0)=U^2$, $K(0,V)=V^2$, is not homogeneous for any assignment of weights
to $U$ and $V$ (the monomials $U^2$, $U^2V^3$, $V^2$ would need
$2p=2p+3q=2q$), and its top-degree part is the monomial $U^2V^3$. So the
class of identities admissible in Lemma 1 strictly contains the binary-form
identities, and so does the premise (P) as written. No reduction from the
inhomogeneous class to forms is available on the page: taking top-degree
parts of an inhomogeneous identity gives a homogeneous relation among those
terms of maximal degree, which may have fewer than four terms, a vanishing
proper subsum or a common factor (the example $K$ shows the fifth power of a
monomial as a top part), and the substitutions $U\mapsto U^p$, $V\mapsto V^q$
homogenize only weighted-homogeneous identities. A nonexistence theorem for
real four-term identities of $5$-powerful binary forms therefore leaves the
inhomogeneous part of the route open. The implication is unsupported, not
disproved: no admissible identity of either kind is known.

**W3. The infinitude clause (S2b, L5) — nonconstancy.** Lemma 1 derives
"infinitely many values" from the hypothesis that $A_n(U,B)$ is nonconstant,
stated separately from the positive-leading-coefficient clause. For a
homogeneous identity of degree $D\ge5$ this is automatic: $K$ is homogeneous
of degree $d=D/5\ge1$ with $U^d$-coefficient $\pm1$ by (iii), so $K(U,B)$ has
$U$-degree exactly $d$, $A_1(U,B)$ has degree $5d$, and a sum of polynomials
with positive leading coefficients has the maximal degree among them. For an
inhomogeneous identity it is not: $K=1+UV(V-B)$ satisfies (iii) with
$d=d'=0$ and $K(U,B)=1$; with $a=0$ in (iv) the monomial $A_2=c_2V^b$ is also
constant in $U$, and nothing in (i)–(iv) or positivity prevents $A_3(U,B)$
and hence $A_4(U,B)$ from being constant, in which case one triple arises.
Whether an identity realizing this degenerate case exists is not known; the
hypothesis is simply missing from the clause as written.

## Strongest attack

- **S1.** A target description; it agrees with the problem statement (three
  summands at $r=5$, both questions). The recorded examples and the forum
  bound live outside the read set and are not checked. Not a mathematical
  claim.
- **S2a.** Attacked by seeking an admissible identity whose values fail the
  conclusion: every route (a common prime of the three values, a value that is
  $1$, negative $m$) is closed by Lemma 1's proof, whose hypotheses the
  section restates exactly. Failed.
- **S2b.** Attacked through the degenerate constant case of W3: the attack
  finds a missing hypothesis, not a counterexample, and the case is empty for
  homogeneous identities. The deduction as written is defective (F3); the
  statement stands under the added hypothesis. Attacked also through the
  pairwise reading of "coprime": the values of an admissible identity are not
  pairwise coprime in general (the monomial $A_2$ shares the primes of $m$
  and $B$ with any other term divisible by $U$ or $V$), so the deduction is
  specific to the joint reading (F9), which the lead states.
- **S3.** Attacked by trying to build an admissible identity with two
  proportional terms whose merged three-term identity escapes Theorem 3
  through a shared factor: impossible, since the merged identity always keeps
  a rational multiple of $A_1$ next to a rational multiple of $A_2$, and these
  are coprime by (iii) and (iv) (W1). Attacked through Theorem 3's
  one-variable scope: generic specialization preserves all hypotheses (W1).
  The statement survives; the page's one-line justification does not (F2).
- **S4.** Attacked at the minimality: degrees $6$ to $9$ are not mentioned, and
  the exception structure is stated as "vanishing subsums" only. With four
  $D$-th powers of linear forms, $5\le D\le9$, distinct roots give the
  independent rows $(\alpha_i^D,\alpha_i^{D-1}\beta_i,\ldots,\beta_i^D)$ (a
  generalized Vandermonde matrix, of rank $4$ for four distinct points of the
  projective line); with coincident roots, the pattern $3+1$ forces a zero
  coefficient, $2+2$ gives two vanishing subsums, and $4$ gives
  $\sum c_i=0$, which admits $(1,2,3,-6)$ with no vanishing proper subsum but
  the common factor $L^D$. The statement survives with the fuller
  justification (F5).
- **S5.** Imported from Corollary 4.1; not attacked here. The identity itself
  was recomputed exactly.
- **S6 and S9b, L8, L9.** Attacked with the inhomogeneous admissible class of
  W2. The attack succeeds against the deduction: nothing on either page
  supports "would close the route" for identities that are not binary forms.
  No counterexample is exhibited, since no admissible identity is known, so
  the verdict is proof defective; statement unresolved (F1).
- **S7a.** Attacked at the normalization: a $5$-powerful form of degree $10$
  has root multiplicities $(10)$ or $(5,5)$, hence is $cQ^5$ with $Q$
  quadratic, also over $\mathbb Q$ and $\mathbb R$ (an irreducible quadratic
  to the fifth power); constants and signs are absorbed as stated; fixing
  $Q_4$ to one representative per orbit loses nothing because scaling all
  $Q_i$ by one constant, negating all of them, and a common linear
  substitution preserve the equation, and the orbit lists on the lead
  (rank-$2$ and rank-$1$ forms over $\mathbb C$; indefinite, definite and
  rank-$1$ over $\mathbb R$; for cubics the root patterns three distinct,
  double, triple, and over $\mathbb R$ one real root with a complex pair) are
  complete. Failed.
- **S7b.** Attacked at the listed shapes: the partitions of $15$ into parts at
  least $5$ are $(15)$, $(10,5)$, $(5,5,5)$, $(9,6)$, $(8,7)$; the first three
  are fifth powers of cubics ($L^3$, $LM^2$, $LMN$), and $L^5M^{10}=(LM^2)^5$
  lies in the searched shape, indeed at the representative $U^2V$ the search
  uses. The sentence is false as stated (F4).
- **S7c.** Exploratory outcomes outside the read set; not attacked.
- **S8.** Attacked at "mild evidence": a degree-$10$ identity gives values of
  size about $m^{10}$, below $10^{16}$ only for $m$ below about $40$, and only
  values beyond the positivity threshold are solutions, a caveat the sentence
  does not name (F8); the sentence is labeled heuristic and survives as such.
- **S9a.** Attacked by asking whether a rational identity with (i)–(iv),
  positivity and nonconstancy could fail to refute finiteness: it cannot, by
  S2. Failed.
- **L1.** "Every polynomial route": the recorded result (Corollary 3.1 and
  its scope paragraph) excludes one-parameter families and polynomially
  parametrized parameter curves and names what it does not cover; the
  sentence claims more (F7). Proof defective; statement unresolved.
- **L2.** Dropping $a+b\ge1$ yields a statement that is still true (Lemma 1's
  proof never uses it: a constant $A_2$ with $|c_2|>1$ violates (ii), and
  $A_2=\pm1$ makes joint coprimality trivial), and dropping $m\ge1$ is
  harmless; the infinitude phrase inherits F3. Failed except for F3.
- **L3.** The literal sentence is refuted by $1+1=2$: constants are
  $r$-powerful and pairwise coprime for every $r$. The intended statement is
  Theorem 3, which carries "not all constant" (F6).
- **L5.** As S2b; and "for some admissible $B$" is enough for the transfer.
- **L6.** "The premise's polynomial part is satisfiable over $\mathbb C$" is
  loose: (ii) has no meaning over $\mathbb C$, and (iii) holds for the complex
  identity only after a diagonal rescaling of $V$ (Corollary 4.1's $Q_0$ has
  $Q_0(0,V)=-2V^2$). Read as "a four-term identity of $5$-powerful forms with
  one fifth-power term and one monomial term exists over $\mathbb C$" it is
  true. Noted under F1's replacement.
- **L9.** "Would turn the numerical absence ... into a proof": a
  Gröbner-basis or resultant computation over $\mathbb Q$ describes the
  complex solution set; the real question needs a further step (F10).

## Premises

- **Lemma 1** (connections page, Shared results; author-recorded). Interface:
  $r\ge2$, $n\ge3$, nonzero $A_1,\ldots,A_n\in\mathbb Z[U,V]$ with
  $A_1+\cdots+A_{n-1}=A_n$ and (i)–(iv); $B\ge1$ divisible by every prime of
  every $c_i$; $m\ge1$ coprime to $B$ with all $A_i(m,B)>0$. Conclusion: the
  first $n-1$ values are jointly coprime and $r$-powerful, the sum is
  $r$-powerful; with positive leading coefficients in $U$ positivity holds for
  large $m$; with $A_n(U,B)$ nonconstant the sums take infinitely many values;
  with $A_i(U,B)\ne A_j(U,B)$ the summands are pairwise distinct for all but
  finitely many $m$. Used with $r=5$, $n=4$. Held; statement confirmed, proof
  not credited here.
- **Theorem 3** (same page; author-recorded, from Lemma 2). Interface:
  $a,b,c\in\mathbb C[t]$ pairwise coprime, $r$-powerful, not all constant,
  $a+b=c$; then $r=2$ and none is constant. Used at $r=5$ after the bridge of
  W1. Held; statement confirmed.
- **Corollary 3.1** (same page). Used only through the lead's L1 sentence;
  its scope paragraph on the page names what it does not cover.
- **Proposition 4 and Corollary 4.1** (same page; author-recorded). Interface:
  $\sum_{k=0}^2Q(\omega^kU,\omega^{-k}V)^5=(3bUV)^5$ when $ac=-2b^2$; at
  $(1,1,-2)$ the four forms have no vanishing proper subsum, no common factor,
  and no real form under projective linear substitution and rescaling. Used
  as stated; the identity recomputed exactly.
- **Theorem 1 reconstruction** (`theorem_1_reconstruction.md`; reviewed as it
  stood on 2026-09-28T05:03:27Z, corrections applied since; treated as
  established at that standing). Interface: for each $r\ge6$, infinitely many
  tuples of $r-2$ pairwise distinct positive jointly coprime $r$-powerful
  integers with
  $r$-powerful sum; nothing at $r=4,5$. Used by the lead's L1 within scope.
  Read in full.
- **Recalled abc and abcd bounds** (library card and result page,
  claims-checked; printed page 438 of the held PDF read by text extraction).
  Interface: $\kappa$ algebraically closed of characteristic zero, a smooth
  complete curve of genus $g$, finite $S$ with $|S|\ge2$, $\chi=2g-2+|S|$;
  for $S$-units $u,v$ not both constant with $1+u+v=0$, $H(1:u:v)\le\chi$;
  for $S$-units $u,v,z$ with $z=1+u+v$ and no vanishing subsum among $1,u,v$,
  $H(1:u:v:z)\le3\chi$. Genus zero: $\chi=|S|-2$; a polynomial tuple with no
  common factor has height its maximal degree. Independent check of the
  form-version: for binary forms of one degree $D$ with no common factor, the
  support may be taken as the set of points of the projective line where some
  form vanishes, of size $n_0$ (the number of distinct linear factors of the
  product), the height is $D$, and the bound reads $D\le3(n_0-2)$; the page's
  $3(n_0-1)$, with $n_0$ counting affine roots after dehomogenization, and
  the lead's $3(n_0-1)$ with linear factors, are both valid and weaker. Held.
- **Problem 939 statement** (problem page, lines 18–24). Exact text used for
  S1. Held.
- **The polynomial-factor proposition of the Problem 940 folder** is consumed
  by Corollary 3.1 only and was not read; the section does not use it
  directly.

## Findings

**F1 (required).** Location: section, "The gap is therefore: *does a four-term
identity of $5$-powerful binary forms with rational terms exist?*" and "a
proof that no real four-term identity of $5$-powerful binary forms exists would
close the polynomial route"; lead, "A proof that no four-term identity of
$5$-powerful binary forms with real terms exists would close this route" and
"a proof of nonexistence in all degrees would close the route". Defect: Lemma 1
and the premise (P) admit every polynomial in $\mathbb Z[U,V]$, homogeneous or
not, and no reduction of the inhomogeneous case to binary forms is given or
available on the page (W2). Witness: the admissible inhomogeneous shape
$K=U^2+U^2V^3+V^2$ of W2; the implication is unsupported, not disproved.
Proposed replacement: either add "homogeneous" to (P), to the gap sentence
and to the closing sentences, with one sentence recording that the transfer
does not need homogeneity and that inhomogeneous identities are a separate,
unexamined possibility; or keep (P) general and write "would close the
homogeneous case of the polynomial route" in the three closing sentences. In
L6, replace "the premise's polynomial part is satisfiable" by "a four-term
identity of $5$-powerful forms with one fifth-power term and one monomial term
exists over $\mathbb C$".

**F2 (required).** Location: section, "Theorem 3 constrains its shape: the
summands cannot include two proportional polynomials (that would be a
three-term identity of $5$-powerful polynomials after combining them)"; lead,
"so the three summands of the premise cannot include two proportional
polynomials". Defect: Theorem 3 requires pairwise coprime polynomials in one
variable over $\mathbb C$, not all constant; the parenthetical checks none of
these, and a three-term identity of $5$-powerful polynomials is not
contradictory by itself ($2f+3f=5f$ for any $5$-powerful $f$; Theorem 3 says
nothing about identities whose terms share a factor). Witness: that trivial
identity, and the two-variable setting of the $A_i$. The conclusion is true:
W1 supplies the bridge from (iii), (iv) and positivity. Proposed replacement:
after "combining them", add "the merged identity still contains a rational
multiple of $A_1=K^5$ beside a rational multiple of the monomial $A_2$, which
are coprime by (iii), so its three terms are pairwise coprime; positivity
excludes the merges with a vanishing coefficient; and Theorem 3 applies after
specializing $V$, or $U$ when $a=0$, to a generic value, which preserves
$5$-powerfulness, coprimality and nonconstancy".

**F3 (suggested).** Location: section, "satisfies (i)–(iv) and the positivity
clause would give infinitely many jointly coprime $5$-powerful triples"; lead,
(P) "with positive leading coefficients in $U$ for some admissible $B$" and
"Under (P) the transfer produces infinitely many". Defect: Lemma 1 derives the
infinitude from the separate hypothesis that $A_4(U,B)$ is nonconstant;
positive leading coefficients alone allow all $A_i(U,B)$ to be constant (W3),
in which case one triple arises. Automatic for homogeneous identities of
positive degree (W3), so the F1 repair that restricts (P) to forms removes
this gap as well. Proposed replacement: add "and $A_4(U,B)$ nonconstant" to
the clause and to (P), or adopt the homogeneous form of (P).

**F4 (suggested).** Location: section, "(the mixed shapes $L^6M^9$, $L^7M^8$,
$L^5M^{10}$ were not searched)"; lead, "The mixed shapes of degree $15$
($L^6M^9$, $L^7M^8$, $L^5M^{10}$ with $L,M$ linear) ... were not searched" and
the Next step's plan to search them. Defect: $L^5M^{10}=(LM^2)^5$ is the fifth
power of the cubic $LM^2$ and lies inside the searched shape, at the
representative $U^2V$ the search uses. The $5$-powerful shapes of degree $15$
are the partitions $(15)$, $(10,5)$, $(5,5,5)$, all fifth powers of cubics,
and $(9,6)$, $(8,7)$, the two outside the search; identities mixing shapes
among the four terms were not searched either. Proposed replacement: "(the
shapes $L^6M^9$ and $L^7M^8$, and identities mixing shapes among the four
terms, were not searched)", in both documents and in the Next step.

**F5 (suggested).** Location: section, "(degree $5$ would need four fifth
powers of linear forms with zero sum, which the Vandermonde determinant of
their roots excludes except with vanishing subsums)"; lead, the same sentence.
Defect: the exceptions are vanishing proper subsums or a common factor (four
proportional forms with coefficients summing to zero, such as $(1,2,3,-6)$,
have no vanishing proper subsum), and "smallest possible degree, $10$" also
needs degrees $6$ to $9$, where a $5$-powerful form is $cL^D$ and the same
independence argument applies. Proposed replacement: "(in degrees $5$ to $9$
a $5$-powerful form is a constant times the $D$-th power of a linear form, and
$D$-th powers of linear forms with distinct roots are linearly independent, so
a four-term identity there has a vanishing proper subsum or a common factor)".

**F6 (suggested).** Location: lead, "No identity $a+b=c$ of pairwise coprime
$r$-powerful polynomials with $r\ge3$ exists", and the transfer bullet "and
$A_2$ is a monomial" with "for every $m$ coprime to $B$". Defect: Theorem 3
carries "not all constant" ($1+1=2$ is an identity of pairwise coprime
$r$-powerful constants), and Lemma 1 carries $a+b\ge1$ in (iv) and $m\ge1$.
Neither omission changes any deduction ($A_2$ is nonconstant in every use;
Lemma 1's proof does not use $a+b\ge1$ or $m\ge1$). Proposed replacement:
restate both with the hypotheses as on the connections page.

**F7 (suggested).** Location: lead, "its $r=4$ case is excluded from every
polynomial route by the theorem recalled below". Defect: Corollary 3.1 excludes
one-parameter polynomial families of coprime $r$-powerful solutions of $a+b=c$
for $r\ge3$ (and polynomially parametrized parameter curves through them),
and the connections page records what it does not cover, an identity whose
terms share a nonconstant factor used only where that factor is $\pm1$.
"Every polynomial route" claims more than the recorded result. Proposed
replacement: "excluded from the polynomial-identity route of Corollary 3.1
(one-parameter families and polynomially parametrized parameter curves)".

**F8 (note).** Location: section, "no further solution with $d<10^{16}$" and
"a degree-$10$ identity with small coefficients would place solutions below
$10^{16}$ unless the constants absorbed by $V$ are large". The symbol $d$ is
not defined in the section (the sum, presumably), and the values of an
identity are solutions only beyond the positivity threshold in $m$, a second
caveat to the "mild evidence" sentence, which is heuristic and labeled so.

**F9 (note).** Location: section, "answer the second question negatively at
$r=5$". The deduction reads "coprime" in the problem statement as joint
coprimality; the lead states this reading and its source, the section does
not, and the values of an admissible identity are not pairwise coprime in
general. Record the reading in the section.

**F10 (note).** Location: lead, "this would turn the numerical absence of a
real degree-$10$ identity into a proof". A Gröbner-basis or resultant
computation over $\mathbb Q$ describes the complex solution set; excluding real
solutions needs a further real-algebraic step (for instance, the complex
solutions fall into finitely many gauge orbits and each is tested for a real
point as in Corollary 4.1). The plan is sound with that step named.

## Verdict

- **S1** — not a mathematical claim (target description); consistent with the
  problem statement; the recorded examples and the forum bound lie outside
  the read set.
- **S2a** — refutation-failed.
- **S2b** — proof defective; statement unresolved, as written: the infinitude
  needs the nonconstancy of $A_4(U,B)$, which "the positivity clause" does not
  carry (F3); with that hypothesis, or for homogeneous identities of positive
  degree, the deduction holds under the joint-coprimality reading (F9).
- **S3** — refutation-failed; the page's justification omits the coprimality
  and one-variable bridge that Theorem 3 needs (F2), supplied in W1.
- **S4** — refutation-failed; the parenthetical justification is incomplete
  (F5).
- **S5** — imported, not reviewed here; used within its statement.
- **S6** — proof defective; statement unresolved, as the assertion that the
  route's gap is exactly the binary-form question (F1).
- **S7a** — refutation-failed.
- **S7b** — refuted-as-stated: $L^5M^{10}$ is a fifth power of a cubic and was
  inside the searched shape (F4).
- **S7c** — not a claim (exploratory outcomes, outside the read set,
  unchecked).
- **S8** — refutation-failed as a labeled heuristic (F8).
- **S9a** — refutation-failed.
- **S9b** — proof defective; statement unresolved (F1).
- **L1** — proof defective; statement unresolved, for "every polynomial route"
  (F7); the remainder restates S1 and the reconstruction within scope.
- **L2** — refutation-failed for the value statement; the infinitude phrase
  inherits S2b (F3, F6).
- **L3** — refuted-as-stated by $1+1=2$; the intended statement is Theorem 3
  and holds (F6). The consequence drawn from it is S3.
- **L4** — as S4 and S5.
- **L5** — (P) is a stated provisional premise, not a claim; the deduction
  under (P) is proof defective; statement unresolved, as S2b (F3), and
  refutation-failed once (P) is restricted to forms or carries nonconstancy;
  the distinctness clause is refutation-failed.
- **L6** — refutation-failed with the loose phrase noted under F1; "the least
  possible degree" as S4.
- **L7** — not a claim (description of exploratory scripts outside the read
  set).
- **L8** — proof defective; statement unresolved (F1).
- **L9** — the closing implication proof defective; statement unresolved
  (F1); the proof plan for degree $10$ needs the step of F10; the remaining
  sentences refutation-failed.
- **L10** — refutation-failed (accurate standing sentences).

**Limitations.** The proofs of the shared results are another reviewer's
subject and were not credited here; the two search scripts and their counts
were excluded and are unchecked; the recorded examples at $r=5$, the forum
search and the site's reading of "coprime" were not examined beyond the
problem statement. This focused review assigns no tier and changes no status.
