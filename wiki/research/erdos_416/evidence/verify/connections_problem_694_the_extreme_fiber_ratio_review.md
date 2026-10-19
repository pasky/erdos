---
name: research/erdos_416/evidence/verify/connections_problem_694_the_extreme_fiber_ratio_review
title: "Independent review of the connections section: Problem 694: the extreme fiber ratio"
desc: |
  Refutation review of the section's nine statements: seven survive
  (refutation-failed), one is an informal pointer, and the sentence that
  the witness 54 propagates as Proposition 3.1's collisions do is refuted
  as stated (216 = phi(259)); one required correction, two suggested.
created: 2026-09-28T18:29:42Z
updated: 2026-10-07T21:41:29Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, commissioned for
refutation with only the assignment text. The reviewer took no part in
writing the connections page, the reconstruction pages or the library
pages read, and had no contact with their author. Nothing under the
folder's `evidence/` directory, no review, grade, standing or acceptance
text of the section, and no page outside the named read set was
consulted, except as the exposures below record. No web search was made.

**Subject.** The source as it stood on 2026-09-28T13:50:48Z (called "the
subject commit" below), page
`wiki/research/erdos_416/connections.md`, section
"## Problem 694: the extreme fiber ratio", lines 493–518 (the H2 at line
493 to the line before the next H2 at line 519). The section files no
lead page; its recorded outcome is "Fails".

**Read, and at what depth.**

- The section in full; every sentence is restated below.
- The page's shared sections (lines 1–90): the standing paragraph, the
  notation ($T$, $V$, $V'$, $f_{\min}$, $r$, $V(x;k)$, $S(k)$, $c_0$),
  the imported inputs (F), (F8), (W), (KK) and the search paragraph, read
  as inputs at interface level; their own proofs are another reviewer's.
- The Problem 417 section (lines 91–341) at interface level only, because
  the section under review cites its "bounded-record premise" and its
  Theorem 417.3: the statement of Theorem 417.3, its Step 1 (the witness
  $d=54$ with preimages $81$ and $162$) and Step 2 (every $v\in S(3)$ has
  $f_{\min}(v)\ge\tfrac32v$), and the pair-family bullet under "What it
  does not give" (lines 262–271), which states the premise.
- `wiki/research/erdos_416/kruer_kohlmeyer_theorem_1_1_reconstruction.md`
  in full, as the premise that defines the pair family and the estimates
  (3)–(5).
- The Statement of `wiki/problems/arithmetic_functions/E0694/_index.md`.
- The library card of the five-page note
  ([[../library/arithmetic_functions/gpt_5_5_pro_2026_totient_fibre_extremes/_index|card]]),
  its result page
  [[../library/arithmetic_functions/gpt_5_5_pro_2026_totient_fibre_extremes/theorem_2_1|theorem_2_1]]
  (Statement), and the held PDF at the card's path, pp. 4–5 on the
  rendered page images and in the text layer: Proposition 3.1 with its
  proof, read clause by clause and re-derived.
- The card of
  [[../library/arithmetic_functions/ford_1998_distribution_totients/_index|Ford (1998)]]
  and the held conversion: §1.3 (Theorem 8 and the sentence calling it a
  trivial corollary of the proof of Theorem 2) and §7 (the proof of
  Theorem 8 and the list of witnesses).
- The provenance paragraph of the card of
  [[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/_index|Pollack, Pomerance and Treviño (2013)]]
  and, in the held conversion of the 17-page manuscript, the definition of
  a number convenient for a totient (its p. 1) and Lemma 4.1 with the
  first paragraph of its proof (§4).
- `docs/verification.md` ("Grading and claim standing", the shared audit
  checklist, "Whole-claim report", "Audit checklist"),
  `docs/approach_vetting.md`, `docs/evidence.md` ("Source fidelity") and
  `docs/math_authoring.md`.

**Exposures.** Five over-wide reads, none of which is a review, grade or
standing text of the section: (1) in `E0694.md`, the Status, Source,
References and Formalization paragraphs and the first two paragraphs of
"Current assessment" (the question as imported and the status-defining
source) came through a read that ran past the Statement; the section's
second sentence was checked against that Status paragraph, which the
assignment excludes, and the check is marked as such below; (2) the whole
card of the five-page note beyond its provenance paragraphs (read status,
contents, compiled scope, formal artifacts, bears-on and results);
(3) the Ford card's bears-on line and results list; (4) the summary
paragraph of the 2013 manuscript's card; (5) the Statements of
`E0417.md` and `E0051.md`, read to test the section's sentence about the
catalog.

## Restatement

Notation as on the page: $T(x)$ is the set of totient values in $[1,x]$,
$V(x)=|T(x)|$, $f_{\min}(v)$ and $f_{\max}(v)$ are the least and greatest
preimages of a totient $v$, $S(k)$ is the set of totients all of whose
preimages are divisible by $k$, and $\varphi$ is Euler's function.

- **S1 (target).** Problem 694 asks to investigate
  $\max f_{\max}(n)/f_{\min}(n)$ over the totient values $n\le x$, the
  maximum restricted to $n\in\varphi(\mathbb N)$.
- **S2 (status characterization).** The problem page records the site's
  status solved (Lean) with the qualification that the asymptotic
  $(e^\gamma+o(1))\log\log x$ rests on the five-page note's Theorem 2.1
  and on two external Lean developments read as text, no refereed
  publication or independent review being held.
- **S3 (obstruction).** The reconstructed mechanism, the pair family of
  the write-up's Proposition 4.1 with its estimates (3)–(5) and the
  doubling-law and cluster-interval bookkeeping, gives nothing for the
  question, because (a) every retained pair $(b,p)$ supplies exactly one
  preimage $m_0p$ of its value $b(p-1)$, so nothing in the family sees
  $f_{\max}$; and (b) the values attaining the extreme ratio form a set
  that estimates of the form "all but $\varepsilon V(y)+o(V(y))$ totients
  $v\le y$" do not constrain.
- **S4 (conditional transfer).** Under the bounded-record premise of the
  Problem 417 section (the selected records $m_0$ satisfy
  $m_0/\varphi(m_0)\le K(\varepsilon)$, a premise stated in no held
  text), the mechanism gives: for every $\varepsilon\in(0,\tfrac12)$
  there is a constant, written $K(\varepsilon)$ here and
  $2K(\varepsilon)$ in the Problem 417 section, such that for all large
  $y$ all but $(\varepsilon+o(1))V(y)$ of the totients $v\le y$ satisfy
  $f_{\min}(v)\le K(\varepsilon)v$.
- **S5 (catalog).** No catalog problem asks for the statement S4.
- **S6 (pointer).** The statement S4 "is the object of Problem 417".
- **S7 (the shared device).** Proposition 3.1 of the note, as the section
  restates it: if $\varphi(a)=\varphi(b)=n$, then for every prime
  $r\nmid ab$ the value $(r-1)n$ is a totient with preimages $ra$ and
  $rb$; and this propagation is the multiplication by convenient integers
  behind Ford's Theorem 8 and Lemma 4.1 of the 2013 manuscript.
- **S8 (propagation of the witness).** The witness $d=54$ of Theorem
  417.3 propagates the same way: for every prime $r\nmid81\cdot162$,
  that is for every prime $r\ge5$, the value $54(r-1)$ carries the
  property that Theorem 417.3 uses at $d=54$, membership in $S(3)$, as
  $(r-1)n$ carries the collision in Proposition 3.1.
- **S9 (outcome).** The connection fails: the mechanism has no bearing on
  a question the page records as solved, and the shared device belongs to
  Ford's paper, not to the reconstructions.

## Checklist

- **Quantifiers and scope.** Fails at S8. The exact-preimage property
  behind Ford's Theorem 8 holds for at least half of Ford's set
  $\mathcal B$ and, in the form the 2013 manuscript attributes to Erdős,
  for almost all primes; S8 asserts it for every prime $r\nmid ab$, the
  almost-all-to-all upgrade, and the witness $r=5$ below refutes it.
  Elsewhere pass: S4's "$\varepsilon$-proportion" is an eventual
  statement over $v\le y$, and its $(\varepsilon+o(1))$ becomes
  $\varepsilon$ by running the premise at $\varepsilon/2$.
- **Circularity.** Pass. The section proves nothing from its own
  conclusions; S3 and S9 are negative claims argued from the shape of the
  inputs.
- **Model and convention changes.** Pass with a flag at S7's
  identification (F2). The multiplication in Proposition 3.1 is by an
  arbitrary prime coprime to $ab$ and uses only that $ra$ and $rb$ are
  preimages, while a multiplier is convenient for $d$ (the 2013
  manuscript's definition, Erdős's notion) when $d\varphi(n)$ has no
  preimages beyond the products of $n$ with the preimages of $d$; the
  section equates the two by vocabulary, and S8 is the consequence. The
  ratio convention (maximum over totient values) matches the problem's
  parenthetical and the note's $\mathcal R(x)$. The renaming of
  $2K(\varepsilon)$ as $K(\varepsilon)$ is a convention change without
  effect.
- **Finite and statistical overreach.** Pass. The section reports no
  computation and draws no statistical inference; the reviewer's
  enumeration below is exact and serves only as a counterexample.
- **Uniformity.** Pass. The only constant, $K(\varepsilon)$, is stated
  with its dependence; the obstruction S3 involves no constants.
- **Extremal conclusions.** Pass. S1 is in the problem's own units; the
  sparseness of the extreme fibers behind S3(b) is derived below in those
  units (a lower bound on the fiber ratio forces a lower bound on
  $M/\varphi(M)$ for $M=f_{\max}(n)$).
- **Consequences and composition.** Fails at S8, a consequence sentence
  attached to S7 that does not follow from it. S4 inherits three
  premises, estimate (3) of (KK), the write-up's description of the
  family with its actual-values property, and the record bound; the
  section names the third and carries the first two only through the
  pointer to the Problem 417 section (F5). S9 follows from S3.
- **Computation.** Pass for the section, which has none. The reviewer's
  witness is hand-checkable:
  $\varphi(259)=\varphi(7\cdot37)=6\cdot36=216=54\cdot(5-1)$.
- **Reproduction.** Not applicable: the section states no rerun
  instruction or coverage claim.
- **Source and verdict fidelity.** Pass with two notes. Proposition 3.1
  is restated faithfully against the page images of pp. 4–5; Theorem 8,
  the "trivial corollary" sentence and the witness list match Ford's §1.3
  and §7; Lemma 4.1(ii) of the 2013 manuscript is exactly the convenient
  property. The notes: the 2013 manuscript attributes the
  convenient-number observation to Erdős, so "the shared device is
  Ford's" is loose (F4); and "Theorem 2.1 on its card" links the result
  page, not the card (F6). The status characterization S2 matches the
  page's Status paragraph, read only through the exposure declared above.

## Weakest steps

**1. S8, re-derived, fails.** Take $n=54$, $a=162$, $b=81$, so that
$\varphi(a)=\varphi(b)=54$ and $ab=2\cdot3^8$. Proposition 3.1 gives, for
every prime $r\ge5$, the preimages $81r$ and $162r$ of $54(r-1)$, both
divisible by $3$. Membership in $S(3)$ needs every preimage divisible by
$3$. For $r=5$, $54(r-1)=216=2^3\cdot3^3$, and
$\varphi(7\cdot37)=6\cdot36=216$ with $3\nmid259$; also
$\varphi(13\cdot19)=12\cdot18=216$ and $\varphi(4\cdot109)=2\cdot108=216$.
So $216\notin S(3)$ although the collision propagates to it. For $r=7$,
$324=\varphi(4\cdot163)$ with $3\nmid652$; for $r=11$, $540=\varphi(541)$
with $541$ prime. An exact enumeration of the preimages of $54(r-1)$
(preimages listed by their largest prime factor; the routine was checked
against a complete sieve of $\varphi$ for every value up to $600$) over
the $44$ primes $5\le r<200$ finds $54(r-1)\in S(3)$ for $r=79$ and
$r=107$ only, where the preimages are exactly $81r$ and $162r$; every
other $54(r-1)$ in that range has a preimage coprime to $3$. What does
propagate is the collision, which is Proposition 3.1 with
$(a,b)=(162,81)$ and is not the property Theorem 417.3 uses. The property
that Theorem 417.3 uses propagates along the multipliers $b$ for which
$54\varphi(b)$ has only the preimages $81b$ and $162b$, Ford's "at least
half of the numbers $b\in\mathcal B$" in §7, which is Theorem 8 itself
and not the note's device.

**2. S3(b), re-derived, holds.** Let $c>0$ and let $n\le x$ be a totient
with $f_{\max}(n)/f_{\min}(n)\ge c\log\log x$; write $M=f_{\max}(n)$ and
$m=f_{\min}(n)$. Since $\varphi(M)=\varphi(m)=n\le m$,

$$
c\log\log x\le\frac Mm\le\frac M{\varphi(M)},
\qquad
M=n\cdot\frac M{\varphi(M)}\le x\max_{t\le2x^2}\frac t{\varphi(t)}
\le X:=2e^\gamma x\log\log x
$$

for large $x$, using $M\le2n^2$ (the note's p. 1) and the elementary
bound $t/\varphi(t)\ll\log\log t$ (Lemma 1.1 of the note gives the
constant). If $M$ has $k$ distinct prime factors $q_1<\dots<q_k$, then
$M/\varphi(M)\le\prod_{i\le k}(1-1/p_i)^{-1}\le C\log p_k$ with $p_i$ the
$i$-th prime (Mertens' product bound), so $\log p_k\ge(c/C)\log\log x$
and $k=\pi(p_k)\ge(\log x)^{c'}$ for any fixed $c'<c/C$ and large $x$.
An integer $M\le X$ with at least $k_0$ distinct prime factors has a
squarefree divisor with exactly $k_0$ of them, so their number is at most

$$
X\sum_{\substack{D\ \text{squarefree}\\ \omega(D)=k_0}}\frac1D
\le\frac X{k_0!}\Bigl(\sum_{p\le X}\frac1p\Bigr)^{k_0}
\le X\Bigl(\frac{e(\log\log X+1)}{k_0}\Bigr)^{k_0}
\le X\exp\bigl(-(\log x)^{c'}\bigr)
$$

for large $x$, with $k_0=\lceil(\log x)^{c'}\rceil$. Hence the totients
$n\le x$ whose fiber ratio is at least $c\log\log x$ number
$o(x/(\log x)^A)$ for every $A$, while $V(x)\ge\pi(x+1)\ge c_0x/\log x$;
the extreme fibers are $o(V(x))$ and lie inside the exceptional allowance
of estimate (3) for every $\varepsilon$. Estimate (3) does not average
anything; it tolerates an exceptional set, and the extreme fibers fit in
it (F7). S3(a) is the actual-values bullet of the reconstruction page:
$p\nmid m_0$ and $\varphi(m_0p)=b(p-1)$, one preimage per pair.

**3. S4, re-derived, holds as a conditional.** For a retained pair
$(b,p)$ with core $b=\varphi(m_0)$, value $v=b(p-1)$ and the top prime
$p$ exceeding every prime of $m_0$, the integer $m_0p$ is a preimage of
$v$, so

$$
f_{\min}(v)\le m_0p=\frac{m_0}{\varphi(m_0)}\cdot\frac p{p-1}\cdot v
\le2K(\varepsilon)\,v
$$

under the record bound $m_0/\varphi(m_0)\le K(\varepsilon)$, since
$p\ge2$. Estimate (3) with Step 2 of the reconstruction page
($V(y^{99/100})=o(V(y))$ by Chebyshev) leaves at most
$(\varepsilon+o(1))V(y)$ totients $v\le y$ outside the family for large
$y$. This is the Problem 417 section's bullet with its constant
$2K(\varepsilon)$; the section under review writes $K(\varepsilon)$ for
that constant. The deduction uses, besides the record bound, estimate (3)
of (KK) and the write-up's description of the family (the actual-values
property), which the abstract form of Proposition 4.1 on the
reconstruction page does not carry.

## Strongest attack

- **S1.** Compared clause by clause with the problem page's Statement
  (the maximum over $n\le x$ of the form $\varphi(m)$). No gap.
- **S2.** Compared with the note's result page (Theorem 2.1, read depth
  "read in full", "nothing here is independently reviewed") and, through
  the declared exposure, with the page's Status paragraph. The attack
  looked for a standing claim stronger than the page records; there is
  none.
- **S3.** The attack: collisions inside the pair family, two pairs
  $(b,p)\ne(b',p')$ with $b(p-1)=b'(p'-1)$, do exhibit two preimages
  $m_0p$ and $m_0'p'$ of one value, so the family is not blind to
  multiple preimages. It fails because the ratio of two such preimages is
  $(m_0/\varphi(m_0))(p/(p-1))$ divided by the same expression for the
  other pair, at most $2\max m_0/\varphi(m_0)$ over the selected records,
  bounded under the record premise and in any case tied to the records
  and not to $f_{\max}$; and estimate (4) makes such collisions
  $o(V(y))$, the same order as the extreme fibers (Weakest step 2), so
  no counting statement of the form (3)–(5) can reach the value
  $(e^\gamma+o(1))\log\log x$, whose upper bound is the extremal order of
  $t/\varphi(t)$ and whose lower bound is a Linnik-prime construction.
- **S4.** The attack looked for a case where the retained pair's product
  $m_0p$ is not a preimage ($p\mid m_0$) or where the family's values
  leave $[1,y]$; both are excluded by the family's definition
  ($f_y\colon P_y\to T(y)$; the top prime exceeds every prime of the
  record). The remaining weakness is the premise set, which the section
  carries by pointer; the conditional is stated as conditional.
- **S5.** The candidates in the catalog are Problems 417, 51 and 694.
  Problem 417 asks whether $\lim V(x)/V'(x)$ exists and exceeds $1$,
  which by Lemma 417.1(a) concerns the totients $v\le x$ with
  $f_{\min}(v)>x$; a typical bound $f_{\min}(v)\le Kv$ with $K\ge2$
  constrains none of them, as the Problem 417 section records. Problem 51
  asks whether $f_{\min}(a)/a\to\infty$ along an infinite set of
  totients, which a typical bound leaves open in both directions. Problem
  694 is S1. The sentence survives for these; the catalog beyond the
  problems the page's search names was not read.
- **S6.** Not a mathematical claim; read literally it conflicts with the
  Problem 417 section's own verdict that the typical-ratio statement
  "gives again only $R\ll1$" (F3).
- **S7.** Proposition 3.1 re-derived: for a prime $r\nmid ab$,
  $\varphi(ra)=(r-1)\varphi(a)=(r-1)n=\varphi(rb)$, the values $(r-1)n$
  are distinct for distinct $r$, and $ra/rb=a/b$; this matches pp. 4–5
  of the note. The identification with the convenient-integer device is
  where the attack lands: Ford's §7 proof of Theorem 8 needs that
  $\varphi(b)d$ "has only the pre-images $bm_i$", the 2013 manuscript's
  Lemma 4.1(ii) needs $n$ convenient for $d_1$ and $d_2$, and neither
  clause is in Proposition 3.1, which needs only existence. The
  identification is a vocabulary match of the operation, not an
  entailment; it is not false as a description of the operation, and it
  is what leads to S8 (F2).
- **S8.** Refuted by $r=5$; see Weakest step 1. The alternative reading,
  that only the collision between $81$ and $162$ propagates, is
  Proposition 3.1 itself and says nothing about the witness property of
  Theorem 417.3, so it does not rescue the sentence (F1).
- **S9.** The attack on "no bearing" is S3's attack and fails. The
  attribution "Ford's" is loose: the 2013 manuscript (p. 1) attributes
  the observation, and the almost-all-primes theorem, to Erdős and calls
  its Lemma 4.1 a variant proved by Ford's methods; Ford's §7 uses the
  device for Theorem 8. The substantive clause, that the device is not
  the reconstructions', stands (F4).

## Premises

- **Proposition 4.1 of the write-up and the pair family** (estimates
  (3)–(5), the pairs $(b,p)$, the actual-values property), from
  [[research/erdos_416/kruer_kohlmeyer_theorem_1_1_reconstruction|the Theorem 1.1 reconstruction]]
  at the subject commit: author-recorded; the proposition is imported
  from an accepted Lean file that is not held, and the family description
  is the write-up's prose. Read in full. Used within its hypotheses in
  S3 and S4; the review notes that the actual-values property is part of
  the family description, not of the abstract proposition.
- **Chebyshev's bound** $\pi(y)\ge c_0y/\log y$ (the page's notation; the
  reconstruction page's imported input), used in Weakest step 2.
- **Theorem 417.3 and the bounded-record premise**, from the Problem 417
  section of the same page: author-recorded, read at interface level
  (statement, Step 1, Step 2, the pair-family bullet). The witness
  $\varphi^{-1}(54)=\{81,162\}$ was confirmed by exact enumeration. Their
  proofs are another reviewer's subject.
- **Proposition 3.1 of the five-page note**, held PDF at the card's path,
  pp. 4–5, read on the page images and in the text layer; statement and
  proof re-derived. Standing: author-recorded on the card; no refereed
  publication is held.
- **Theorem 2.1 of the note**, statement only, from the result page; its
  proof was not read, and nothing here depends on it beyond the size
  bound $M\le2n^2$ and Lemma 1.1, used in Weakest step 2 and taken at
  statement level from the result page.
- **Ford (1998), Theorem 8**, held conversion §1.3 (statement; "a trivial
  corollary to the proof of Theorem 2") and §7 (the proof: for at least
  half of $b\in\mathcal B$ the totient $\varphi(b)d$ has only the
  preimages $bm_i$; the witnesses $2^{18}\cdot257$, $54$, $12500$, $294$
  and $110$). Refereed; statement level; the proof in §5 was not read.
- **Pollack, Pomerance and Treviño (2013), Lemma 4.1** and the
  definition of "convenient for $d$" (p. 1 of the held 17-page
  manuscript): a number $n$ is convenient for a totient $d$ with
  preimages $n_1,\dots,n_k$ when $d\varphi(n)$ is a totient with
  preimages $n_1n,\dots,n_kn$ and no others; the manuscript attributes to
  Erdős that for each fixed totient $d$ almost all primes are convenient
  for $d$, and Lemma 4.1 gives $\gg_DZ(x)$ integers $n$ with
  $\varphi(n)\le x/D$, convenient for two given totients, and
  $n/\varphi(n)\le K$. Statement level; the almost-all-primes attribution
  is used here only as the source's characterization, not as an input to
  any verdict.
- **Mertens' product bound** $\prod_{p\le z}(1-1/p)^{-1}\ll\log z$ and
  the prime-reciprocal sum $\sum_{p\le X}1/p\le\log\log X+1$, standard,
  used in Weakest step 2 only.
- **Problem statements** of E0694 (target), E0417 and E0051 (for S5).

## Findings

- **F1 (required).** Location: lines 513–514, "and the witness $d=54$ of
  Theorem 417.3 propagates the same way." Defect: read with the
  propagation just described, to $(r-1)n$ for every prime $r\nmid ab$,
  the sentence asserts $54(r-1)\in S(3)$ for every prime $r\ge5$, and
  that is false; the property Theorem 417.3 uses at $d=54$ propagates
  only along convenient multipliers, whose existence in quantity is
  Ford's Theorem 8 and not the note's Proposition 3.1. Witness: $r=5$,
  $54\cdot4=216=\varphi(259)$, $259=7\cdot37$, $3\nmid259$ (also
  $247=13\cdot19$ and $436=4\cdot109$); $r=7$, $324=\varphi(652)$,
  $652=4\cdot163$; $r=11$, $540=\varphi(541)$. Among the primes
  $5\le r<200$, only $r=79$ and $r=107$ give $54(r-1)\in S(3)$.
  Replacement: "The witness $d=54$ of Theorem 417.3 does not propagate
  this way: $54(r-1)$ lies in $S(3)$ only when $r$ is convenient for
  $54$, and $54\cdot(5-1)=216=\varphi(7\cdot37)$ shows that $r=5$ is
  not. The propagation Theorem 417.3 would need is the exact-preimage
  clause of Ford's §7, which is Theorem 8 itself."
- **F2 (suggested).** Location: lines 510–513, "The one shared device is
  the note's Proposition 3.1, that a collision ... propagates to the
  values $(r-1)n$ for primes $r\nmid ab$: this is the multiplication by
  convenient integers behind Ford's Theorem 8 and the Problem 49 folder's
  Lemma 4.1". Defect: Proposition 3.1 uses only that $ra$ and $rb$ are
  preimages, for every prime $r\nmid ab$; a convenient multiplier (the
  2013 manuscript's definition) is one for which these products are all
  the preimages, and that clause, the whole content of Ford's §7 argument
  and of Lemma 4.1(ii), is absent from Proposition 3.1. The
  identification is by vocabulary; F1 is its consequence. Witness: the
  same $r=5$, where the collision propagates to $216$ (preimages $405$
  and $810$) while $216$ has seventeen further preimages. Replacement:
  "The one shared device is the existence half of the multiplication by
  convenient integers behind Ford's Theorem 8 and the Problem 49 folder's
  Lemma 4.1: the note's Proposition 3.1 observes that a collision
  $\varphi(a)=\varphi(b)=n$ gives $(r-1)n$ the preimages $ra$ and $rb$
  for every prime $r\nmid ab$, and needs nothing about the other
  preimages of $(r-1)n$, whose absence is what 'convenient' means."
- **F3 (suggested).** Location: lines 509–510, "which no catalog problem
  asks and which is the object of Problem 417." Defect: Problem 417 asks
  whether $\lim V(x)/V'(x)$ exists and exceeds $1$, which concerns the
  totients $v\le x$ with $f_{\min}(v)>x$; the Problem 417 section itself
  records that the typical-ratio statement "gives again only $R\ll1$", so
  the statement is not that problem's object, and the two clauses read
  as contradicting each other. Witness: the page's own pair-family bullet
  (lines 262–271). Replacement: "which no catalog problem asks: Problem
  417 concerns the totients with $f_{\min}(v)>x$, which an upper bound on
  typical least preimages does not reach (the Problem 417 section's
  pair-family bullet), and Problem 51 asks whether $f_{\min}(a)/a$ is
  unbounded along an infinite set, which a typical bound leaves open."
- **F4 (note).** Location: lines 516–517, "the shared device is Ford's".
  The 2013 manuscript (p. 1) attributes the convenient-number observation
  and the almost-all-primes theorem to Erdős and describes its Lemma 4.1
  as a variant proved with Ford's methods; Ford's §7 uses the device for
  Theorem 8. Replacement: "the shared device is Erdős's, as Ford's
  Theorem 8 and the 2013 manuscript use it, not the reconstructions'."
- **F5 (note).** Location: lines 506–509. Three small imprecisions in the
  conditional: the constant is $2K(\varepsilon)$ in the Problem 417
  section and $K(\varepsilon)$ here, the same symbol for different
  constants (harmless, since neither is specified); "for all but an
  $\varepsilon$-proportion of totients" lacks its range, all but
  $(\varepsilon+o(1))V(y)$ of the totients $v\le y$ for all large $y$;
  and the premise set beyond the record bound, estimate (3) of (KK)
  together with the write-up's description of the family, is carried only
  by the pointer to the Problem 417 section. Replacement: "a
  typical-ratio statement, $f_{\min}(v)\le2K(\varepsilon)v$ for all but
  $(\varepsilon+o(1))V(y)$ of the totients $v\le y$, under (KK) and the
  write-up's family as the Problem 417 section states them".
- **F6 (note).** Location: line 499, "Theorem 2.1 on its card". The link
  resolves to the result page `theorem_2_1`, not to the card.
  Replacement: "Theorem 2.1 on its result page".
- **F7 (note).** Location: lines 505–506, "the extreme fibers that
  (3)–(5) average away". The estimates tolerate an exceptional set of
  $\varepsilon V(y)+o(V(y))$ values; they do not average. The extreme
  fibers number at most $x\exp(-(\log x)^{c})$ for some $c>0$ (Weakest
  step 2), so they fit inside that allowance. Replacement: "the extreme
  fibers, a set of $o(V(x))$ values that lies inside the exceptional
  allowance of (3)".

## Verdict

- **S1:** refutation-failed. The target is stated in the problem's own
  units.
- **S2:** refutation-failed. The characterization matches the result
  page and, through the declared exposure, the page's Status paragraph.
- **S3:** refutation-failed. The pair family supplies one preimage per
  value, and the extreme fibers are $o(V(x))$, inside the allowance of
  estimate (3); the collision attack fails.
- **S4:** refutation-failed, as a conditional whose constant is the
  Problem 417 section's $2K(\varepsilon)$ renamed; its premise set is
  named by pointer (F5).
- **S5:** refutation-failed for Problems 417, 51 and 694; the rest of the
  catalog was not read.
- **S6:** not a claim; an informal pointer whose literal reading
  conflicts with the Problem 417 section (F3).
- **S7:** refutation-failed for the restatement and proof of Proposition
  3.1; the identification with the convenient-integer device is a
  vocabulary match that omits the exact-preimage clause (F2).
- **S8:** refuted-as-stated. Witness $r=5$:
  $54\cdot(5-1)=216=\varphi(259)$ with $259=7\cdot37$ not divisible by
  $3$, so $216\notin S(3)$; the property of the witness $54$ used by
  Theorem 417.3 does not pass to $54(r-1)$ for every prime
  $r\nmid81\cdot162$.
- **S9:** refutation-failed for "no bearing" and for "not the
  reconstructions'"; the attribution to Ford is loose (F4).

Limitations. The section is a connections note, and S3, S5 and S9 are
negative claims; the review attacked them with the strongest positive
route it could find (collisions inside the pair family; the statements
of Problems 417 and 51) and reports that those attacks fail, which is
not a proof that no route exists. The proofs of (F), (F8), (KK), of
Theorem 417.3 and of the note's Theorem 2.1 were not reviewed here; the
section uses them at their stated interfaces, and the one place where it
uses an interface beyond its strength is S8. The enumeration behind F1
covers the primes $5\le r<200$; the refutation needs only $r=5$, which
is checkable by hand. This focused review assigns no tier and changes no
status.
