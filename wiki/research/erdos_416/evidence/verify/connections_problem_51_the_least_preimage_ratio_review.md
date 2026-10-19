---
name: research/erdos_416/evidence/verify/connections_problem_51_the_least_preimage_ratio_review
title: "Independent review of the connections section: Problem 51: the least-preimage ratio"
desc: |
  Refutation review of the Problem 51 section as it stood on
  2026-09-28T13:50:48Z. The reformulation, the S(k) lower bound, the account
  of Ford's section 7, the finite-range figures and the negative-answer
  consequence survive (refutation-failed); the cap sentence is
  refuted-as-stated; the necessity sentence of the next investigation is
  proof defective, statement unresolved. Three required corrections, two
  suggested, three notes.
created: 2026-09-28T18:31:55Z
updated: 2026-09-28T20:46:21Z
---

***

## Subject and independence

**Role and independence.** The reviewer is an independent examiner working
in a fresh context from the commissioned assignment alone. The reviewer took
no part in writing the connections page, the reconstruction pages it rests
on, or the Problem 51 page, and read no existing review or grade of any of
them. The charge is refutation of author-recorded mathematics.

**Subject.** The source as it stood on 2026-09-28T13:50:48Z (called "the
commit" below), page
`wiki/research/erdos_416/connections.md`, section
"## Problem 51: the least-preimage ratio", lines 519–561: the H2 heading at
line 519 through the Outcome paragraph ending at line 561; the next H2 is at
line 563. The section files no lead page; its outcome is "Fails".

**Read, and at what depth.**

- The section, every sentence, with each argument re-derived.
- The page's shared sections as inputs whose interfaces were confirmed at
  each use: the frontmatter, the purpose-and-standing paragraph, Notation,
  the imported inputs (F), (F8), (W) and (KK), and the search paragraph
  (lines 1–89), in full.
- The Problem 417 section (lines 91–341) as the input the section cites:
  Lemma 417.1(a) with its proof, the definition of $V_0$, the pair-family
  bullet (line 262) and the computation paragraph (lines 293–316), read
  closely; the rest of that section read once for definitions. Its own
  proofs belong to another reviewer.
- The reconstruction pages
  `wiki/research/erdos_416/zeraoulia_theorem_1_1_reconstruction.md` and
  `wiki/research/erdos_416/kruer_kohlmeyer_theorem_1_1_reconstruction.md`
  in full, as premises; the Lemma 2.1 and Lemma 5.1 pages were not needed
  and were not read.
- `wiki/problems/arithmetic_functions/E0051/_index.md`: the Statement section and
  its references entry for Guy's B36.
- The Ford (1998) card
  [[../library/arithmetic_functions/ford_1998_distribution_totients/_index|ford_1998_distribution_totients]]
  (provenance and results paragraphs), the held conversion at Theorem 8
  (lines 148–154) and the closing paragraphs of its §7 (lines 1573–1577),
  and PDF pages 4 and 39 of the held paper as page images.
- The Guy (2004) card
  [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]]
  (opening paragraph) and the text layer of PDF page 157 (printed p. 139),
  section B36.
- `docs/verification.md` ("Grading and claim standing", "Audit checklist —
  the canonical failure modes", "Whole-claim report", "Audit checklist"),
  `docs/approach_vetting.md`, `docs/evidence.md` ("Source fidelity") and
  `docs/math_authoring.md`.

**Independent computation.** Three short programs were written for this
review from the section's description and kept outside the repository,
since the assignment allows writing only this report; the method is stated
so that the figures can be redone. The first sieves Euler's function for
all $n\le6.2\cdot10^7$ (coverage re-derived under Computation below),
records the least preimage of every totient $v\le10^7$ as the first
argument attaining it, and computes $S(k)\cap[1,10^7]$ as the totients not
among the values of arguments $n\le6.2\cdot10^7$ with $k\nmid n$. The
second computes, for every totient $v\le10^7$, the greatest common divisor
$g(v)$ of all its preimages, so that $v\in S(k)$ exactly when $k\mid g(v)$.
The third enumerates all preimages of a given $d$ by recursion over the
primes $p$ with $p-1\mid d$, doubling every odd preimage found; it was
checked against the sieve on $54$, $110$, $294$, $12500$, $580$, $46240$,
$116964$ and $2037248$. Results are stated where they are used; no run log
is retained.

**Exposures.** Two, disclosed here.

1. The Problem 51 page was read whole, so its "Current assessment",
   "Progress" and "Known Results" sections reached the reviewer. "Current
   assessment" records nothing; "Progress" paraphrases the section under
   review; "Known Results" records a failed transfer from the Problem 49
   folder's connections page. None carries a verdict on this section. They
   are used only for the note F8 below, which is marked as resting on
   exposed text.
2. The two reconstruction pages carry "Standing" paragraphs, read as part
   of those pages. They state author-recorded standing and no verdict on
   this section.

## Restatement

Throughout, $T(x)$ is the set of totient values in $[1,x]$, $V(x)=|T(x)|$,
$f_{\min}(v)$ the least $m$ with $\varphi(m)=v$, $r(v)=f_{\min}(v)/v\ge1$,
$S(k)$ the set of totients all of whose preimages are divisible by $k$, and
$V(x;k)=|S(k)\cap[1,x]|$; $V'(x)$ counts the distinct values $\varphi(m)$
with $m\le x$ and $V_0(x)=V(x)-V'(x)$. $\omega(k)$ is the number of
distinct prime factors of $k$.

- **S1 (target, descriptive).** Problem 51 asks whether an infinite set $A$
  of totients exists with $r(a)\to\infty$ as $a\to\infty$ through $A$;
  Guy's B36 form asks whether for every $\epsilon>0$ some $n$ has
  $\varphi(n)=m<\epsilon n$ with $\varphi(t)\ne m$ for all $t<n$. Status
  open. The section adds that the problem page is not compiled beyond Guy's
  form.
- **S2 (reformulation).** Problem 51 has a positive answer if and only if
  $r$ is unbounded on the set of all totients. Proof offered: if for every
  positive integer $K$ some totient $v_K$ has $r(v_K)>K$, then a given
  totient serves as $v_K$ for only finitely many $K$, so an increasing
  subsequence of the $v_K$ with $r\to\infty$ is such an $A$; conversely,
  $r\to\infty$ along an infinite $A$ makes $r$ unbounded.
- **S3 (what the pair family gives).** For every retained pair $(b,p)$ of
  the write-up's family, the covered value $v=b(p-1)$ has the preimage
  $m_0p$, so $f_{\min}(v)\le m_0p$; this is an upper bound on $r$, and
  Problem 51 needs lower bounds. Nothing transfers.
- **S4 (the $S(k)$ lower bound).** For every $k\ge1$ and every
  $v\in S(k)$, $r(v)\ge k/\varphi(k)$.
- **S5 (route restriction).** The $S(k)$ device can certify $r\to\infty$
  only through moduli $k$ with many (distinct) prime factors, that is, only
  if $S(k)\ne\emptyset$, equivalently $V(x;k)>0$ for some $x$, for such $k$.
- **S6 (Ford's §7, source account).** Ford's search finds witnesses $d$ for
  every $k\le11$ except $k=6$ and $k=10$ (witnesses at $k\in\{2,4,8\}$,
  $\{3,9\}$, $5$, $7$, $11$, all prime powers); Ford writes that there may
  be no totient all of whose preimages are divisible by $6$ and cannot prove
  it; its nonexistence would imply Carmichael's conjecture because a totient
  with a unique preimage has that preimage divisible by $6$.
- **S7 (the cap).** The $S(k)$ device is capped at the ratio $2$ (that of
  $k=4$) unless a modulus with two odd prime factors admits a witness, and
  no held source or computation supplies such a witness.
- **S8 (finite range).** No totient $v\le10^7$ has all its preimages
  divisible by $6$, $10$, $12$, $15$, $20$, $21$, $35$ or $45$;
  $\max_{v\le10^7}r(v)=2.0414$; in this range the least-preimage ratio does
  not grow at all. The figures are attributed to the computation of the
  Problem 417 section.
- **S9 (necessity, next investigation).** A positive answer to Problem 51
  needs totients all of whose preimages carry small prime factors without a
  common one, a structure outside the $V(x;k)$ classification; whether some
  totient has all preimages divisible by $15$ (or $6$) is the natural first
  test.
- **S10 (proposed computation).** A segmented computation of $\max r(v)$ to
  $10^9$–$10^{10}$ would show whether the ratio ever exceeds the level of
  Ford's witnesses.
- **S11 (negative answer).** If $r\le K$ on all totients, then every totient
  counted by $V_0(x)$ lies in $(x/K,x]$, by Lemma 417.1(a).
- **S12 (outcome, descriptive).** No transfer; the shared object yields only
  the $S(k)$ cap and a finite-range observation.

## Checklist

- **Quantifiers and scope.** Fails at S7 and S9. S7 names the wrong class of
  moduli in both directions (F1) and presents as unsupplied a kind of
  witness that its own sieve range contains (F2). S9 asserts a necessity
  ("needs") that the section's own $S(k)$ route contradicts as a logical
  possibility (F3). S2, S4, S5 and S11 carry their quantifiers correctly; in
  S2 the index $K$ must range over the positive integers for the finiteness
  step, which is how the proof reads.
- **Circularity.** Pass. No statement assumes an answer to Problem 51; S11
  is explicitly conditional.
- **Model and convention changes.** Pass. $V(x;k)$ and $S(k)$ agree with
  Ford's definition (PDF p. 4, "the number of totients up to $x$, all of
  whose pre-images are divisible by $k$"); Guy's B36 form and the catalog
  form both say that $r$ is unbounded, since an $n$ with $\varphi(n)=m$ and
  $\varphi(t)\ne m$ for all $t<n$ is $f_{\min}(m)$, and $m<\epsilon n$ is
  $r(m)>1/\epsilon$; the pair family is used at the interface the Theorem
  1.1 reconstruction states (value $b(p-1)$, preimage $m_0p$).
- **Finite and statistical overreach.** Pass with notes. S8 is labeled as a
  finite-range observation and draws no universal conclusion; its phrase
  "does not grow at all" overreads two data points (F6). S9 leans on Ford's
  stated belief about $k=6$, which Ford says he cannot prove (F3). The
  eight moduli of S8 were chosen by hand; the sieve behind them decides the
  membership of every modulus at once, and the choice hid the witnesses of
  F2.
- **Uniformity.** Pass. S4 is an exact inequality with no constant; S11
  uses one bound $K$ for all totients, as its hypothesis states; nothing in
  the section depends on the implied constants of (F8).
- **Extremal conclusions.** Partial. The cap $2$ is the exact maximum of
  $k/\varphi(k)$ over Ford's witnessed moduli ($2$ at $k\in\{2,4,8\}$, then
  $3/2$, $5/4$, $7/6$, $11/10$), and $\max_{v\le10^7}r(v)$ was recomputed in
  the claim's own units as the exact ratio $4158795/2037248=2.04138\ldots$;
  but the sentence stating when the cap lifts is wrong (F1), and the
  device's actual maximum certificate up to $10^7$, which is
  $\max_vg(v)/\varphi(g(v))=19/12$ at $v=116964$, is not stated.
- **Consequences and composition.** Fails at S9 and S10. The Carmichael
  implication in S6 and the confinement in S11 were re-derived and hold. S9
  drops one branch of a dichotomy (F3); S10 poses as open a question the
  section's own figure closes (F5).
- **Computation.** Pass on the figures. The coverage argument was
  re-derived: an argument $n$ with at most nine distinct prime factors has
  $n/\varphi(n)\le\prod_{p\le23}p/(p-1)=6.1129\ldots<6.12$, and one with ten
  or more has $\varphi(n)\ge\prod_{i\le10}(p_i-1)=1021870080>10^9$, so
  every preimage of every $v\le10^7$ is at most $6.12\cdot10^7$. The
  independent sieve reproduces every figure the section quotes and the ones
  it inherits (below). The section gives no rerun instruction and retains no
  code, consistent with the exploratory label in the 417 section, but the
  moduli figures are recorded nowhere but in this sentence (F4).
- **Reproduction.** Pass on substance. Reproduced from the description:
  $(V,V',V_0)$ at $10^4,\dots,10^7$ equal $(2374,2160,214)$,
  $(20254,18412,1842)$, $(180184,163861,16323)$ and
  $(1634372,1485793,148579)$; $\max r=2.0355$ at $v=5888$ up to $10^6$ and
  $2.0414$ at $v=2037248$, $f_{\min}=4158795$, up to $10^7$;
  $|S(3)\cap[1,10^7]|=2069$, proportion $0.00127$; $S(k)\cap[1,10^7]$ empty
  for $k\in\{2,4,6,8,10,12,15,20,21,35,45,105\}$; the proportions with
  $r\ge1.1,1.25,1.5,2$ in $(5\cdot10^6,10^7]$ are $0.319$, $0.266$, $0.194$,
  $0.00001$; the preimages of $54$ are $81$ and $162$.
- **Source and verdict fidelity.** Pass for the sources; one note for the
  page description. Ford's Theorem 8 and its definition of $V(x;k)$ (PDF
  p. 4) and the §7 passage (PDF p. 39: the witnesses, "It appears that there
  might not be any totient, all of whose pre-images are divisible by 6, but
  I cannot prove this", and the Carmichael sentence) were read on the page
  images and match the section and the (F8) import. Guy's sentence on
  printed p. 139 matches the section's paraphrase. The section's standing
  sentences claim author-recorded status only. The clause "not compiled
  beyond Guy's B36 form" is stale at the reviewed commit (F8, from exposed
  text).

## Weakest steps

**W1: which moduli lift the cap (S7).** On $S(k)$ the device certifies
exactly $r\ge k/\varphi(k)=\prod_{p\mid k}p/(p-1)$, a function of the
distinct primes of $k$ alone. The cap $2$ lifts exactly when some $k$ with
$k/\varphi(k)>2$ admits a witness. If $k$ is odd with two distinct prime
factors, then $k/\varphi(k)\le\frac32\cdot\frac54=\frac{15}8<2$, so a
witness for $15$, $21$, $35$ or $45$, or for any odd modulus with two prime
factors, would not lift the cap; an odd modulus needs at least three
distinct prime factors, and small ones: $105$ gives $35/16$, $165$ gives
$33/16$, $195$ gives $65/32$, and $3\cdot7\cdot11=231$ already gives only
$77/40<2$. If $k$ is even with an odd prime factor $q$, then
$k/\varphi(k)\ge2q/(q-1)>2$, so a witness for $6$ (ratio $3$) or $10$
(ratio $5/2$) would lift it, with one odd prime factor. The clause "unless
a modulus with two odd prime factors admits a witness" is therefore neither
necessary nor sufficient for the cap to lift. Moreover such witnesses exist
inside the section's own sieve range: $v=580$ has exactly the preimages
$649=11\cdot59$ and $1298$ (every prime $p$ with $p-1\mid580$ is one of
$2,3,5,11,59$, and the only products of $\varphi(p^e)$ over these primes
equal to $580$ are $10\cdot58$ and $1\cdot10\cdot58$), so $580\in S(649)$;
likewise $46240\in S(11\cdot17^3)$, $116964\in S(3^3\cdot19^3)$ with
$r(116964)=19/12$, and $103240\in S(11\cdot59\cdot179)$, a modulus with
three odd prime factors. Up to $10^7$ the gcd $g(v)$ of the preimages is
odd for every totient $v$ (so no even modulus has a witness there, in
agreement with Ford's $2^{18}\cdot257$), it has two distinct prime factors
for $129005$ values of $g$ and three for $977$, and
$\max_{v\le10^7}g(v)/\varphi(g(v))=19/12$. What holds the device below $2$
in that range is not the absence of composite moduli but the size of their
primes. The section's narrower conclusion, that no held source or
computation supplies a witness with $k/\varphi(k)>2$, is true as a
statement about the corpus.

**W2: the necessity sentence (S9).** Suppose $r$ is unbounded and choose
totients $v_K$ with $r(v_K)>K$. Let $g_K$ be the greatest common divisor of
all preimages of $v_K$. Either $\omega(g_K)$ is unbounded along a
subsequence, in which case $v_K\in S(g_K)$ with $g_K$ having many prime
factors, exactly the $V(x;k)$ route of S5; or $\omega(g_K)$ is bounded, in
which case the common part contributes a bounded factor to every
$m/\varphi(m)$ and the large ratio comes from primes not shared by all
preimages. A positive answer therefore needs one of two structures, and the
section asserts only the second as necessary. Nothing held excludes the
first: Ford's remark about $k=6$ is a belief he says he cannot prove, it
concerns one modulus, and W1 shows that moduli with two and three odd prime
factors do admit witnesses. The step from "many small prime factors in
every preimage", which is necessary since $r(v)>K$ forces
$\prod_{p\mid m}p/(p-1)>K$ for every preimage $m$, to "without a common
one" is not made and cannot be made from the held inputs.

**W3: the reformulation and its use (S2, S11).** Forward direction: given
$v_K$ with $r(v_K)>K$ for every positive integer $K$, the set
$\{K:v_K=v\}$ is contained in $\{K<r(v)\}$, finite. Hence the set
$A=\{v_K\}$ is infinite, and for every real $M$ the elements $a\in A$ with
$r(a)\le M$ lie in $\{v_K:K<M\}$, a finite set, so $r(a)\to\infty$ along
$A$; choosing $K_1<K_2<\cdots$ with $v_{K_{j+1}}>v_{K_j}$, possible because
only finitely many $K$ have $v_K\le v_{K_j}$, gives the increasing
subsequence the section names. Converse: $r\to\infty$ along an infinite set
is unboundedness. Guy's form is the same statement, as under Model and
convention changes. S11: by Lemma 417.1(a), whose proof was re-derived
($v\in T(x)$ is a value of some $m\le x$ exactly when $f_{\min}(v)\le x$),
$V_0(x)$ counts the $v\in T(x)$ with $f_{\min}(v)>x$; if $r\le K$ then
$x<f_{\min}(v)\le Kv$, so $v>x/K$. Both hold.

## Strongest attack

- **S1.** Checked against the problem page's Statement and Guy's printed
  p. 139; both match. Not a mathematical claim. The clause about
  compilation is addressed in F8.
- **S2.** Attempted: a totient serving as $v_K$ for infinitely many $K$
  (blocked, since $r(v)$ is finite); real $K$ (the proof needs integer $K$,
  which is how it reads); a set $A$ on which $r\to\infty$ but $r$ bounded
  (contradictory). The attack fails; W3 is the derivation.
- **S3.** Attempted: a retained pair whose value is not a totient or whose
  preimage $m_0p$ is not a preimage. The reconstruction's interface states
  that for large $y$ the top prime exceeds every prime of the record, so
  $p\nmid m_0$ and $\varphi(m_0p)=(p-1)\varphi(m_0)=b(p-1)$; the section
  says "on covered values", which is exactly this scope. The attack fails.
- **S4.** Attempted: a preimage $m$ of $v\in S(k)$ with $m/\varphi(m)$ below
  $k/\varphi(k)$. Impossible: $k\mid m$ makes every prime of $k$ a prime of
  $m$, and $m/\varphi(m)=\prod_{p\mid m}p/(p-1)$ is a product over a
  superset of the primes of $k$ of factors exceeding $1$. Applied to
  $m=f_{\min}(v)$ this is the claim. The attack fails.
- **S5.** Attempted: unbounded $k/\varphi(k)$ with bounded $\omega(k)$.
  Impossible: $k/\varphi(k)\le\prod_{i\le\omega(k)}p_i/(p_i-1)$. The attack
  fails; the word "distinct" is implicit (F7).
- **S6.** Attempted: a mismatch with Ford's text, or a false parenthetical.
  Ford's PDF p. 39 says exactly what the section reports. The parenthetical
  was re-derived: if $m$ is the unique preimage of $v$, then $m$ is even
  (else $\varphi(2m)=\varphi(m)$), $4\mid m$ (else $m=2m'$ with $m'$ odd and
  $\varphi(m')=\varphi(m)$), and $3\mid m$ (else, with $m=2^am'$, $a\ge2$,
  $\varphi(3m/2)=2\cdot2^{a-2}\varphi(m')=\varphi(m)$); so $12\mid m$, in
  particular $6\mid m$, and all preimages of $v$ are then divisible by $6$,
  so the nonexistence of totients in $S(6)$ leaves no totient with a unique
  preimage. The attack fails.
- **S7.** Succeeds: $k=15$ has two odd prime factors and
  $15/\varphi(15)=15/8<2$; $k=6$ has one and $6/\varphi(6)=3>2$; and
  $v=580$ is a witness for the two-odd-prime modulus $649$ that the sentence
  says no computation supplies. Refuted-as-stated (W1).
- **S8.** Attempted: a wrong figure or an incomplete argument range. Every
  figure was reproduced and the coverage bound re-derived (Checklist,
  Computation and Reproduction). The attack on the numbers fails; the
  attribution and the phrase "at all" are F4 and F6.
- **S9.** Succeeds against the argument, not the statement: W2 exhibits the
  dropped branch. Whether a positive answer can avoid the $V(x;k)$ route is
  unknown, so the statement is unresolved.
- **S10.** Not a mathematical claim; its premise is contradicted by the
  section's own figure (F5).
- **S11.** Attempted: a totient counted by $V_0(x)$ with $v\le x/K$ under
  $r\le K$. Impossible, as in W3. The attack fails.
- **S12.** Descriptive summary, consistent with S3–S8.

## Premises

- **Ford (1998), Theorem 8 and §7**, held PDF (pages 4 and 39 read as page
  images; conversion lines 148–154 and 1573–1577), refereed source at
  statement level. Interface used: the definition of $V(x;k)$; the list of
  witnesses and the two sentences about $k=6$ and Carmichael's conjecture.
  The theorem's implied constant is not used by the section.
- **(F8) import paragraph** of the page: statement-level import of the
  above; the witness $d=54$ is verified in the Problem 417 section and was
  re-verified here (preimages $81$ and $162$, by the sieve and by the
  inverse-totient enumeration).
- **Theorem 1.1 reconstruction page** (author-recorded, reviewed as it stood
  on 2026-09-28T05:03:27Z with corrections since): the pair family's
  interface, value
  $b(p-1)$ with preimage $m_0p$ for actual pairs. Used within its
  hypotheses in S3.
- **The preprint's Theorem 1.1 reconstruction page**: only the definitions
  of $T(x)$ and $V(x)$ are used.
- **Problem 417 section** of the same page (author-recorded; another
  reviewer's subject): Lemma 417.1(a), re-derived here; the computation
  paragraph, reproduced here; the pair-family bullet, read for S3.
- **Problem 51 page**, Statement section: the formulation of S1; its
  references entry for Guy's B36, checked against the held PDF's text layer
  at PDF page 157.
- **Guy (2004)**, B36, printed p. 139: the $\epsilon$ form of the question.
- **Elementary facts** used without source: $\varphi(m)\le m$;
  $m/\varphi(m)=\prod_{p\mid m}p/(p-1)$; $\varphi(2m)=\varphi(m)$ for odd
  $m$; $\varphi(2^am')=2^{a-1}\varphi(m')$ for odd $m'$ and $a\ge1$;
  $\varphi(k)\mid\varphi(m)$ when $k\mid m$.
- No batch acceptance order applies; the section is examined alone.

## Findings

**F1 (required).** Location: "So the $S(k)$ device is capped at the ratio
$2$ of $k=4$ unless a modulus with two odd prime factors admits a witness".
Defect: the condition is wrong in both directions. Witness: $k=15$ has two
odd prime factors and $15/\varphi(15)=15/8<2$, so a witness for it would
not lift the cap; $k=6$ has one odd prime factor and $6/\varphi(6)=3>2$, so
a witness for it would. Proposed replacement: "So the $S(k)$ device is
capped at the ratio $2$ of $k\in\{2,4,8\}$ unless a modulus $k$ with
$k/\varphi(k)>2$ admits a witness, that is, an even modulus with an odd
prime factor (the least are $6$, ratio $3$, and $10$, ratio $5/2$) or an
odd modulus with at least three distinct prime factors, small enough (the
least is $105$, ratio $35/16$)".

**F2 (required).** Location: "which no held source or computation
supplies: the computation of the Problem 417 section finds no totient up to
$10^7$ all of whose preimages are divisible by $6$, $10$, $12$, $15$, $20$,
$21$, $35$ or $45$", together with "the finite question whether some
totient has all preimages divisible by $15$ (or by $6$) is the natural
first test". Defect: the sentence presents the existence of a witness for a
modulus with two odd prime factors as unknown, and the next investigation
proposes it as the first open test, while the section's own sieve range
contains such witnesses; the eight moduli were chosen by hand and the
smallest witnesses have larger primes. Witness: $580\in S(649)$,
$649=11\cdot59$, preimages $649$ and $1298$ only (W1); also
$46240\in S(11\cdot17^3)$, $116964\in S(3^3\cdot19^3)$ with $r=19/12$, and
$103240\in S(11\cdot59\cdot179)$ with three odd prime factors; in all,
$129005$ values of $g(v)$ with two distinct prime factors and $977$ with
three occur for $v\le10^7$, and $\max_{v\le10^7}g(v)/\varphi(g(v))=19/12$.
Proposed replacement: after the corrected F1 sentence, "No held source or
computation supplies one. Moduli with two or three distinct odd prime
factors do admit witnesses in the sieve's range ($580$ with preimages
$649=11\cdot59$ and $1298$; $116964$ with preimages $3^3\cdot19^3$ and its
double, ratio $19/12$; $103240$ with preimages $11\cdot59\cdot179$ and its
double), but their primes are large, and up to $10^7$ the device certifies
at most $r\ge19/12$; no totient up to $10^7$ has all preimages divisible by
$6$, $10$, $12$, $15$, $20$, $21$, $35$ or $45$." The first test should
then be a modulus with $k/\varphi(k)>2$, that is $6$ or $10$ (Ford's open
case) or $105$, not $15$.

**F3 (required).** Location: "A positive answer needs totients all of whose
preimages carry small prime factors without a common one, a structure
outside the $V(x;k)$ classification". Defect: the necessity of "without a
common one" is asserted without argument; a positive answer through
$S(k)$ with $\omega(k)$ unbounded would have all preimages sharing $k$, and
nothing held excludes it (Ford's belief about $k=6$ is stated as unproved
and concerns one modulus; composite moduli do admit witnesses, F2).
Witness: the dichotomy in W2. Proposed replacement: "A positive answer
needs totients all of whose preimages carry many small prime factors:
either the preimages share a divisor $k$ with many prime factors, the
$V(x;k)$ classification, where the witnessed moduli so far have
$k/\varphi(k)\le2$, or they do not, a structure outside that
classification".

**F4 (suggested).** Location: "the computation of the Problem 417 section
finds no totient up to $10^7$ all of whose preimages are divisible by $6$,
$10$, $12$, $15$, $20$, $21$, $35$ or $45$". Defect: the Problem 417
section's computation paragraph (lines 293–316) records $\max r$, the $V$,
$V'$ and $V_0$ counts, the ratio proportions, $V(10^7;3)/V(10^7)$ and the
emptiness of $S(4)$ up to $10^7$, and nothing about the eight moduli; the
figure is recorded only in this sentence and attributed elsewhere. The
figure itself is true (reproduced). Proposed replacement: "the sieve of the
Problem 417 section, extended for this section, finds ..." and a sentence
here recording the moduli checked, so that the figure has a home.

**F5 (suggested).** Location: "a segmented computation of $\max r(v)$ to
$10^9$–$10^{10}$ would show whether the ratio ever exceeds the level of
Ford's witnesses". Defect: whichever level is meant, the section's own
figure already exceeds it: $r(2037248)=4158795/2037248=2.0414\ldots$
exceeds the cap $2$ and every witness's own ratio, which the
inverse-totient enumeration gives as $r(2^{18}\cdot257)=257/128=2.0078\ldots$
(least preimage $2^{11}\cdot257^2$; eight preimages, all divisible by
$16$), $r(54)=3/2$, $r(12500)=5/4$, $r(294)=7/6$ and $r(110)=11/10$.
Proposed replacement: "would show whether $\max_{v\le x}r(v)$ grows with
$x$ at all beyond its value $2.0414$ at $10^7$, and in particular whether
it reaches $5/2$ or $3$, the ratios a witness for $10$ or $6$ would force".

**F6 (note).** Location: "In this range the least-preimage ratio does not
grow at all." The section's inputs give $\max r=2.0355$ up to $10^6$ and
$2.0414$ up to $10^7$ (reproduced), so the maximum grows, slightly.
Proposed replacement: "In this range the maximum ratio moves only from
$2.0355$ to $2.0414$ between $10^6$ and $10^7$."

**F7 (note).** Location: "reaches $r\to\infty$ only through moduli $k$ with
many prime factors" and "finds witnesses for $k\le11$ only at the prime
powers and at $k=11$". The first should say "many distinct prime factors",
since $k/\varphi(k)$ depends only on the distinct primes of $k$ ($k=2^a$
gives $2$ for every $a$). In the second, $11$ is a prime power; "and at
$k=11$" is redundant.

**F8 (note, from exposed text).** Location: "the page is not compiled beyond
Guy's B36 form of the question". At the reviewed commit the Problem 51 page
carries a Progress paragraph paraphrasing this section and a Known Results
paragraph recording a failed transfer from the Problem 49 folder, so the
clause describes an earlier state of that page. This rests on the exposure
disclosed above and is recorded for the integrator, who is not blind.

## Verdict

- S1: not a mathematical claim; its description of the target matches the
  problem page and Guy; the compilation clause is stale (F8).
- S2: refutation-failed.
- S3: refutation-failed.
- S4: refutation-failed.
- S5: refutation-failed.
- S6: refutation-failed.
- S7: refuted-as-stated (F1, F2).
- S8: refutation-failed for the figures, each reproduced; the attribution
  is F4 and the phrase "at all" is F6.
- S9: proof defective; statement unresolved (F3).
- S10: not a mathematical claim; its premise is contradicted by the
  section's own figure (F5).
- S11: refutation-failed.
- S12: not a mathematical claim; consistent with S3–S8 once F1–F3 are
  applied, since the device's cap and the finite-range observation remain
  all that the shared object yields.

Limitations. The proofs of Lemma 417.1 and the standing of the imported
inputs (F), (F8), (W) and (KK) belong to other reviewers; here only their
interfaces were confirmed at each use, and the only ones this section
consumes are the definition behind (F8), Lemma 417.1(a), which was
re-derived, and the pair family's interface. The reproduction covers
$v\le10^7$ with all preimages up to $6.2\cdot10^7$ and says nothing beyond
that range; the witnesses of F2 are finite facts and decide no asymptotic
question. Ford's Theorem 8 was read at statement level. No literature
beyond the held corpus was consulted.

This focused review assigns no tier and changes no status.
