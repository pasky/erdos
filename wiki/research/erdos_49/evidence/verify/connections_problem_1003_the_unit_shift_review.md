---
name: research/erdos_49/evidence/verify/connections_problem_1003_the_unit_shift_review
title: "Independent review of the connections section: Problem 1003: the unit shift"
desc: |
  Focused refutation review of the Problem 1003 section: the unit-shift
  upper bound, the emptiness of the structured family at the unit shift,
  the parity obstruction and the recorded failure of the transfer survive
  attack (refutation-failed on S1, S2, S3, S4, S5b, S6 and S7), while the
  direction clause of the obstruction (S5a) is refuted-as-stated. One
  required correction, two notes.
created: 2026-09-28T18:14:47Z
updated: 2026-09-28T20:43:42Z
---

***

## Subject and independence

- Role: independent reviewer in a fresh context, commissioned for
  refutation. The reviewer took no part in writing the page, the folder's
  reconstruction pages or any lead, and received only the assignment text.
- Subject: path `wiki/research/erdos_49/connections.md` as it stood on
  2026-09-28T13:50:48Z, section "## Problem 1003: the unit shift", lines
  255--282 (from the H2 heading to the line before the next H2 at line 283).
- Lead pages: none. The section records a failed transfer and names no
  lead.
- Read in the subject state, in full unless stated: the section; the
  page's preamble, Standing, Outcomes-at-a-glance and "Notation and the
  inputs used" (lines 1--111) as inputs whose interfaces were confirmed at
  each use; the reconstruction pages `theorem_3_1_reconstruction.md`,
  `theorem_3_3_reconstruction.md` and `theorem_1_2_reconstruction.md` in
  full, and the Standing and Statement sections of
  `lemma_4_1_reconstruction.md` and `lemma_5_1_reconstruction.md`, as
  premises; `wiki/problems/arithmetic_functions/E1003/_index.md` lines 1--35,
  the preamble that holds the statement (see Exposures); the cards and
  result pages of Pollack, Pomerance and Treviño (both cards, the Theorem
  3.1 and 3.3 pages), Graham, Holt and Pomerance (card, Theorem 2 and
  Theorem 4 pages), Erdős, Pomerance and Sárközy II (card, Theorem 2
  page), Ford 2020 (card, Theorem 1 page) and Li 2026 (card, Corollary 1.5
  and Theorem 1.4 pages); the held PDFs on their text layers: the
  Pollack--Pomerance--Treviño manuscript pp. 5--6, Ford 2020 pp. 1--4
  (p. 2 also as a page image), Erdős--Pomerance--Sárközy II printed
  p. 253, Li 2026 pp. 2--3; `docs/verification.md` sections "Grading and
  claim standing", "Audit checklist -- the canonical failure modes",
  "Whole-claim report" and "Audit checklist", `docs/approach_vetting.md`,
  `docs/evidence.md` section "Source fidelity" and
  `docs/math_authoring.md`.
- Exposures: the E1003 page has no "## Statement" heading; its statement
  sits in the preamble, which also carries the one-line site status
  ("Open"), the source line, the reference list and the formalization
  pointer, all seen while reading the statement. Nothing below the
  "## Current assessment" heading of that page was read. No `_index.md`
  of the folder, no `evidence/` content, no Known Results, standing or
  acceptance text, and no other review was read; a working-tree status
  listing showed the file names of other folders' untracked review files,
  none opened. No web search was made. Yamada's paper is not held, so the
  comparison with his bound was checked only through the quotations in
  Li 2026 (p. 2, equation (1.1)) and Ford 2020 (p. 2).

## Restatement

Throughout, $\varphi$ is Euler's function,
$P(x;k)=\#\{n\le x:\varphi(n)=\varphi(n+k)\}$ for a natural number $k$, and
$P(x;k)=P_0(x;k)+P_1(x;k)$ is the split of
the Theorem 3.3 page: $P_0(x;k)$ counts the solutions $n\le x$ that have
the form of Theorem A for some admissible $j$ and $r$, and $P_1(x;k)$ the
rest. Theorem A (Graham, Holt and Pomerance, Theorem 1, as quoted on the
source's p. 5) supposes that $j$ and $j+k$ have the same set of prime
factors, puts $g=\gcd(j,j+k)$, and supposes that for a positive integer
$r$ both $(j/g)r+1$ and $((j+k)/g)r+1$ are primes not dividing $j$; then
$n=j(((j+k)/g)r+1)$ satisfies $\varphi(n)=\varphi(n+k)$.

- **S1 (target).** Problem 1003 asks whether there are infinitely many
  positive integers $n$ with $\varphi(n)=\varphi(n+1)$. The section also
  relays what the problem page's current assessment records: the question
  is open, the strongest upper bound is Li's Corollary 1.5, and Ford's
  infinitude results concern even shifts divisible by a fixed large
  integer.
- **S2 (the transported bound).** $P_0(x;1)=0$ for every $x$, so
  $P(x;1)=P_1(x;1)$, and there is an absolute $x_0$ such that
  $P(x;1)<x/\exp((\log x)^{1/3})$ for every $x>x_0$. This is the 1987
  bound of Erdős, Pomerance and Sárközy, and it is weaker than Yamada's
  bound and than Li's.
- **S3 (emptiness of the structured family).** No positive integer $j$
  has the same set of prime factors as $j+1$; hence no integer has the
  Theorem A form with $k=1$.
- **S4 (no construction).** No statement reconstructed in the folder
  (Theorems 3.1, 3.3 and 1.2, Lemmas 3.2, 4.1 and 5.1) produces an
  integer $n$ with $\varphi(n)=\varphi(n+1)$.
- **S5a (obstruction, direction clause, as written).** "Every
  reconstructed input bounds a count from above"; in the Outcome, "the
  inputs are upper bounds". Under its strongest reading, the universal
  ranges over the inputs the page declares as consumed ((T1), (T3), (L4),
  (F), (P)) and over the reconstructed statements.
- **S5b (obstruction, substance).** Infinitude is an existence statement,
  and no reconstructed input yields the existence of even one $n$ with
  $\varphi(n)=\varphi(n+1)$, let alone infinitely many.
- **S6 (obstruction, parity clause).** Theorem A, the only construction of
  shift solutions in the source chain, produces solutions of
  $\varphi(n)=\varphi(n+k)$ only from pairs $j$, $j+k$ with equal radicals;
  equal radicals force $k$ even; this requirement is the structural reason
  Ford's (2020) infinitude results concern even shifts and do not reach
  $k=1$; the reconstruction supplies no way around it.
- **S7 (outcome).** There is no next investigation from this mechanism,
  and the connection fails.

## Checklist

- **Quantifiers and scope.** Pass. (T1) is applied at the single value
  $k=1$, which lies in its range $k\le\exp((\log x)^{1/3})$ for every
  $x>1$; its threshold $x_0$ is absolute, matching "for large $x$"; the
  strict inequality matches the source's Theorem 3.1. $P_0(x;1)=0$ holds
  for every $x$, not only eventually. No almost-all or limit statement
  occurs.
- **Circularity.** Pass. Nothing about Problem 1003 is assumed; the section
  concludes that the mechanism gives nothing.
- **Model and convention changes.** Pass. $P$, $P_0$, $P_1$ and Theorem A
  are used with the conventions of the Theorem 3.3 page, which match the
  source's p. 5; "same prime factors" and "equal radicals" are the same
  condition ($\gamma(j)=\gamma(j+k)$ on the Theorem 3.3 page).
- **Finite and statistical overreach.** Not applicable: no finite
  verification or heuristic enters. The explicit totient (P) is not used
  here.
- **Uniformity.** Pass. Only the fixed instance $k=1$ of (T1) is consumed,
  so the uniformity of (T1) in $k$ carries no weight; the absolute
  threshold is what the sentence "for large $x$" needs.
- **Extremal conclusions.** Not applicable: no infimum, supremum or
  sharpness claim is made. The comparison "weaker than Yamada's and Li's"
  is an ordering of three explicit bounds and is checked under Weakest
  step W2.
- **Consequences and composition.** One defect. $P(x;1)=P_1(x;1)$ composes
  correctly with (T1). The consequence sentence "every reconstructed input
  bounds a count from above", read as the universal it is, fails on (L4)
  and Lemma 5.1, which are lower bounds (Finding F1). The obstruction
  itself survives under the corrected reason (W3).
- **Computation.** Not applicable: the section runs no computation.
- **Reproduction.** Not applicable: the section states no rerun command or
  coverage claim.
- **Source and verdict fidelity.** Pass with two limitations. Theorem 3.1
  and Theorem A were checked against the manuscript's pp. 5--6; the
  Erdős--Pomerance--Sárközy bound against printed p. 253; Li's Corollary
  1.5 against p. 3; Ford's parity remark and his Lemma 3 construction
  against pp. 2 and 4. Yamada's bound was checked only as quoted by Li and
  by Ford, since his paper is not held. The sentence relaying the problem
  page's current assessment could not be checked against that text, which
  is outside this review's read set; the mathematical content it relays
  (Li's Corollary 1.5, Ford's Theorem 1) matches the held sources.

## Weakest steps

**W1 (S3, and $P_0(x;1)=0$ in S2).** Suppose $j\ge1$ and the sets of prime
factors of $j$ and $j+1$ coincide; call the common set $S$. Every $p\in S$
divides both $j$ and $j+1$, hence divides $(j+1)-j=1$, so $S$ is empty.
Then $j$ has no prime factor, so $j=1$, and $j+1=2$ has the prime factor
$2$, so $S$ is not empty: a contradiction. Hence no $j$ is admissible for
$k=1$, the set of integers of the Theorem A form with $k=1$ is empty
whatever $r$ is, and $P_0(x;1)=0$ for every $x$. The Theorem 1.2 page,
step 2, reaches the same conclusion for every odd $k$ by parity (exactly
one of $j$, $j+k$ is even); the section's route through coprimality is a
different valid argument, and both use that $j+k\ge2$ has a prime factor.
Composition: with $P_0(x;1)=0$ the split gives $P(x;1)=P_1(x;1)$, which is
what S2 needs.

**W2 (S2).** (T1), as the source states it (Theorem 3.1, manuscript p. 6)
and as the Theorem 3.1 page records it: there is an absolute $x_0$ such
that $P_1(x;k)<x/\exp((\log x)^{1/3})$ for $x>x_0$, uniformly for natural
numbers $k\le\exp((\log x)^{1/3})$. At $k=1$ the range condition holds for
every $x>1$ because $\exp((\log x)^{1/3})>1$. With W1,
$P(x;1)<x/\exp((\log x)^{1/3})$ for $x>x_0$. Standing of the input: the
source proves Theorem 3.1 by a sketch, and the Theorem 3.1 page records an
unreconstructed case (solutions with $p\mid m$); the page's Standing
paragraph allows the use of source theorems as published, and at $k=1$
the same bound (with $\le$) is Theorem 2 of Erdős, Pomerance and Sárközy
(1987), a published theorem on its own, which the section names. The
ordering of the three bounds: Yamada's bound, as quoted by Li (p. 2,
equation (1.1)) and by Ford (p. 2), is
$x\exp\{-(2^{-1/2}+o(1))(\log x\log_3x)^{1/2}\}$ for each fixed odd shift;
Li's Corollary 1.5 is $x\exp\{-(\tfrac12-o(1))(\log x\log_2x)^{1/2}\}$.
Since

$$
\frac{(\log x\log_3x)^{1/2}}{(\log x)^{1/3}}
=(\log x)^{1/6}(\log_3x)^{1/2}\to\infty,
\qquad
\frac{\tfrac12(\log x\log_2x)^{1/2}}{2^{-1/2}(\log x\log_3x)^{1/2}}
=2^{-1/2}\Bigl(\frac{\log_2x}{\log_3x}\Bigr)^{1/2}\to\infty,
$$

the exponent of (T1) is the smallest of the three for large $x$: the
section's "weaker than Yamada's and Li's" is correct, and Li's is the
strongest of the three, consistent with the relayed assessment.

**W3 (S5a and S5b).** The direction clause fails under its strongest
reading. (L4), as the page's Notation lists it and as the Lemma 4.1 page
states it, concludes that at least $c_DZ(x)$ integers $n$ satisfy
$\varphi(n)\le x/D$, convenience for $d_1$ and $d_2$, and
$n/\varphi(n)\le K$, for $x\ge x_0(D)$: a lower bound on a count. Lemma
5.1 concludes $\#(\mathcal W(x)\setminus\varphi(S))\ge cW(x)$: a lower
bound. (F) is two-sided. So "every reconstructed input bounds a count from
above" is false as stated. The obstruction nevertheless holds, for a
reason the section does not give: the lower bounds count other objects.
Convenience of $n$ for a totient $d$ with preimages $n_1,\ldots,n_k$ says
that $d\varphi(n)$ is a totient whose preimages are exactly
$n_1n,\ldots,n_kn$; this constrains the multiples $n_in$ and says nothing
about $\varphi(n+1)$ for any $n$ it counts. Lemma 5.1 says which totient
values a nondecreasing set misses and constrains no pair of consecutive
integers. Theorem 1.2 bounds a maximum from above. Hence no reconstructed
statement has, or implies, a conclusion of the form "there is $n$ with
$\varphi(n)=\varphi(n+1)$", which is exactly what S5b asserts.

## Strongest attack

- **S1.** The section's phrasing was compared with the problem page's
  statement, "Are there infinitely many solutions to $\phi(n)=\phi(n+1)$";
  they agree. The relayed descriptions of Li's Corollary 1.5 (an upper
  bound at the unit shift) and of Ford's Theorem 1(a) (infinitude whenever
  $442720643463713815200\mid k$, an even modulus) match the held sources.
  The claim about what the assessment "records", and its date, cannot be
  attacked inside the read set. Attack failed.
- **S2.** Three attacks: exhibit a solution of $\varphi(n)=\varphi(n+1)$
  of the Theorem A form, which W1 rules out; place $k=1$ outside the range
  of (T1), impossible since the range contains every natural number up to
  a quantity exceeding $1$; reverse the ordering with Yamada's or Li's
  bound, which W2 rules out. The strict inequality was checked against
  the source (strict in Theorem 3.1; the 1987 theorem has $\le$, the
  weaker form). Attack failed.
- **S3.** W1 is the attack and its failure: a common prime factor of $j$
  and $j+1$ would divide $1$.
- **S4.** Each reconstructed statement was inspected for an existence
  conclusion about consecutive integers: Theorems 3.1 and 3.3 bound
  $P_1$ and $P_0$ from above; Lemma 3.2 bounds the number of admissible
  $j$; Lemma 4.1 counts convenient integers; Lemma 5.1 counts missing
  totient values; Theorem 1.2 bounds $M^\uparrow(x)$. The two constructions
  inside them, the candidate set of Lemma 4.1 and the reversed pairs of
  Lemma 5.1, produce totient values with prescribed preimages, never a
  pair $n$, $n+1$; the only shift construction in the source chain,
  Theorem A, produces $n$, $n+k$ with $k$ even (S6). Attack failed.
- **S5a.** The witness (L4) defeats the sentence as written: it is a lower
  bound on a count, declared on the same page as a consumed input. Attack
  succeeded; Finding F1.
- **S5b.** The attack was to build a solution of $\varphi(n)=\varphi(n+1)$
  from the reconstruction's lower bounds. Convenience controls
  $\varphi(n_in)$, a multiple of $n$; Lemma 5.1 controls the image of a
  nondecreasing set; neither reaches $n+1$ (W3). Attack failed.
- **S6.** First, equal radicals force $k$ even: if $k$ is odd then $j$ and
  $j+k$ have different parity, so $2$ divides exactly one of them and their
  prime supports differ; this uses only $j\ge1$. Second, the attribution
  to Ford was checked against the held PDF. Ford's Lemma 1 (p. 2) is
  Theorem A, and the text after it says that for odd $k$ there are no such
  $j$. Theorem 1 is proved (p. 4) through Lemma 3: with $a'=a/\gcd(a,b)$,
  $b'=b/\gcd(a,b)$ and $s$ the product of the primes dividing $a'b'$, the
  solutions are $m_1=b'\ell s(a'r+1)$ and $m_2=a'\ell s(b'r+1)$, whose
  shift is $m_1-m_2=\ell\kappa(a,b)$ with $\kappa(a,b)=(b'-a')s$. The pair
  $b'\ell s$, $a'\ell s$ has equal radicals, and $\kappa(a,b)$ is even: if
  $a'$ and $b'$ are both odd then $b'-a'$ is even, and otherwise $2\mid s$.
  So every shift Ford's Theorem 1 reaches is even, for exactly the
  equal-radical reason the section names; his Theorems 2 and 3 also
  produce only multiples of even numbers or simultaneous equations at
  shifts $\ell h_i$, none at $k=1$. Attack failed.
- **S7.** Follows from S4 and S6. Attack failed.

## Premises

- **(T1), Theorem 3.1 of Pollack, Pomerance and Treviño.** Interface: an
  absolute $x_0$; $P_1(x;k)<x/\exp((\log x)^{1/3})$ for $x>x_0$, uniformly
  for natural numbers $k\le\exp((\log x)^{1/3})$. Held: the 17-page author
  manuscript, statement and sketch on p. 6, read on the text layer. The
  reconstruction page was read in full; it records the sketch, one written
  deduction, and an unreconstructed case; treated as established at that
  standing. Used here at $k=1$ only.
- **Theorem A (Graham, Holt and Pomerance, Theorem 1) and the split
  $P=P_0+P_1$.** Interface as restated above. Held: quoted on the
  manuscript's p. 5, read on the text layer; the corpus's verification on
  the Theorem 3.3 page was read. The Graham--Holt--Pomerance PDF was not
  opened; its card and its Theorem 2 and 4 pages were read.
- **Theorem 1.2 page, step 2.** $P_0(x;k)=0$ for odd $k$; re-derived in
  W1. Read in full.
- **(L4), Lemma 4.1, and Lemma 5.1.** Not consumed by the section; their
  Standing and Statement sections were read because their direction is the
  witness of F1. Interface of (L4): for fixed totients $d_1,d_2$ and fixed
  $D\ge\max\{d_1,d_2\}$, at least $c_DZ(x)$ integers $n$ with
  $\varphi(n)\le x/D$, convenient for both, and $n/\varphi(n)\le K$, for
  $x\ge x_0(D)$. Interface of Lemma 5.1: absolute $c>0$, $x_0$ with
  $\#(\mathcal W(x)\setminus\varphi(S))\ge cW(x)$ for every nondecreasing
  $S\subseteq[1,x]$, $x\ge x_0$.
- **(T3), (F), (P).** Not consumed by the section; their listed scopes
  were read on the page.
- **Erdős, Pomerance and Sárközy (1987), Theorem 2.** Interface: for large
  $x$, at most $x/\exp\{(\log x)^{1/3}\}$ solutions $n\le x$ of
  $\varphi(n)=\varphi(n+1)$. Held: printed p. 253 read on the text layer;
  card and Theorem 2 page read.
- **Li (2026), Corollary 1.5.** Interface:
  $\#\{n\le x:\varphi(n)=\varphi(n+1)\}\ll x\exp\{-(\tfrac12-o(1))(\log x\log_2x)^{1/2}\}$
  as $x\to\infty$. Held: arXiv v2, p. 3 read on the text layer; p. 2 read
  for its quotation (1.1) of Yamada's bound; card, Corollary 1.5 and
  Theorem 1.4 pages read. A preprint; used only as the stated bound.
- **Ford (2020), Theorem 1, Lemma 1 and Lemma 3.** Interfaces as used in
  the attack on S6. Held: arXiv v5, pp. 1--4 read on the text layer and
  p. 2 as a page image; card and Theorem 1 page read.
- **Yamada.** Not held. His bound is taken from Li's (1.1) and Ford's p. 2,
  which agree.
- **Problem 1003.** Statement read from the page preamble.
- No batch acceptance order applies; no explicit assumption beyond the
  standings above was needed.

## Findings

- **F1 (required).** Location: lines 271--272, "Infinitude is an
  existence statement; every reconstructed input bounds a count from
  above.", and lines 279--281, "Fails: the inputs are upper bounds, and
  the only constructive ingredient needs an even shift." Defect: the
  universal is false over the inputs the page declares. Witness: (L4),
  listed under "the inputs consumed below", concludes that at least
  $c_DZ(x)$ integers satisfy its three conditions, a lower bound; Lemma
  5.1 concludes $\#(\mathcal W(x)\setminus\varphi(S))\ge cW(x)$, a lower
  bound; (F) is two-sided. The obstruction survives for the reason given
  in W3, which the section does not state. Proposed replacement for lines
  271--272: "Infinitude is an existence statement. The reconstructed
  bounds on $P(x;k)$, (T1) and (T3), are upper bounds; the reconstructed
  lower bounds, (L4) and Lemma 5.1, count convenient integers and missing
  totient values, and neither constrains $\varphi(n+1)$ for any $n$ it
  counts." Proposed replacement for the Outcome: "Fails: the bounds on
  $P(x;k)$ are upper bounds, the lower-bound inputs count other objects,
  and the only constructive ingredient needs an even shift." The verdict
  "fails" and the Outcomes-at-a-glance entry are unaffected.
- **F2 (note).** Location: line 260, "Li's Corollary 1.5"; lines 260--261,
  "Ford's infinitude results"; line 266, "weaker than Yamada's and Li's";
  line 276, "Ford (2020)". The three sources are named without links. The
  library holds a card for Li (2026) with a Corollary 1.5 page and a card
  for Ford (2020) with a Theorem 1 page; Yamada's paper is not held, so
  the comparison with his bound is checkable inside the corpus only
  through Li's quotation (p. 2, equation (1.1)) and Ford's (p. 2).
  Proposed: link the two cards, and either state Yamada's bound with that
  in-corpus locator or drop the comparison with it.
- **F3 (note).** Location: lines 263--266, "(T1) with $k=1$ gives ...".
  The bound is anchored on (T1), whose proof in the source is a sketch
  with an unreconstructed case recorded on the Theorem 3.1 page; at $k=1$
  the identical bound is Theorem 2 of Erdős, Pomerance and Sárközy (1987),
  a published theorem the section already names. Proposed: say that (T1)
  at $k=1$ recovers that theorem, so that the sentence rests on the
  published unit-shift theorem rather than on the sketch. No conclusion
  changes.

## Verdict

- S1: refutation-failed. The statement matches the problem page; the
  relayed assessment content is outside the read set except for its
  mathematical descriptions, which match the held sources.
- S2: refutation-failed. $P(x;1)=P_1(x;1)<x/\exp((\log x)^{1/3})$ for
  $x>x_0$ follows from (T1) at $k=1$ and W1; the ordering against Yamada's
  and Li's bounds holds (W2).
- S3: refutation-failed (W1).
- S4: refutation-failed.
- S5a: refuted-as-stated. The direction clause is false as a universal
  over the page's declared inputs; witness (L4). Finding F1 gives the
  replacement.
- S5b: refutation-failed. The obstruction holds for the corrected reason
  (W3).
- S6: refutation-failed. Equal radicals force an even shift, and the
  attribution to Ford (2020) is faithful to his Lemma 1 and Lemma 3.
- S7: refutation-failed.

Limitations. The sentence relaying the problem page's current assessment
was not checked against that text, which this review was not allowed to
read. Yamada's paper is not held; his bound was taken from two held
quotations that agree. The proof sketch behind (T1) was not re-derived;
at $k=1$ the bound rests independently on the 1987 theorem. The
Graham--Holt--Pomerance PDF was not opened, since Theorem A enters only
through its hypothesis, which the manuscript's p. 5 states. This focused
review assigns no tier and changes no status.
