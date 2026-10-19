---
name: research/erdos_49/evidence/verify/connections_problem_694_the_ratio_of_the_largest_to_the_smal_review
title: "Independent review of the connections section: Problem 694: the ratio of the largest to the smallest preimage"
desc: |
  Refutation review of the Problem 694 section of the connections page.
  Proposition 5 and its transfer survive (refutation-failed); the sentence
  strengthening the note's Proposition 3.1 to a positive proportion with
  ratio exactly a/b is refuted-as-stated (witness a = 16, b = 15: no
  totient has extreme ratio 16/15). One required correction, two notes.
created: 2026-09-28T18:14:46Z
updated: 2026-09-28T20:43:42Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, given only the
commissioning assignment. The reviewer took no part in writing the
connections page, the reconstruction pages or any lead, and read no
review, grade, current assessment or standing text about them. Charge:
refutation.

**Subject.** Path `wiki/research/erdos_49/connections.md` as it stood on
2026-09-28T13:50:48Z, section "Problem 694: the ratio of the largest to the
smallest preimage", lines 468--508 (the H2 heading at line 468 through the line
before the next H2 at line 509). The section names no lead page of its own; its
outcome is "not a route", and the leads the page names for Problems 1004 and 417
belong to other sections and were not read.

**Read, and at what depth.**

- The section, clause by clause. The page's shared sections as inputs: the
  preamble and Standing paragraph, the "Outcomes at a glance" paragraph and
  "Notation and the inputs used" (lines 15--110), in full; the interfaces
  of (L4) and (F) and the definition of convenience were confirmed at each
  use.
- The folder's reconstruction pages in the same state, as premises:
  [[research/erdos_49/lemma_4_1_reconstruction|Lemma 4.1]],
  [[research/erdos_49/lemma_5_1_reconstruction|Lemma 5.1]] and
  [[research/erdos_49/theorem_1_2_reconstruction|Theorem 1.2]], in full.
  The Theorem 3.1, Theorem 3.3 and Lemma 3.2 pages were not read; the
  section consumes none of them.
- [[problems/arithmetic_functions/E0694/_index|Problem 694]]: the Statement
  paragraph.
- The library: the provenance paragraph of the note's card
  [[../library/arithmetic_functions/gpt_5_5_pro_2026_totient_fibre_extremes/_index|totient fiber extremes]]
  and the Statement section of its result page
  [[../library/arithmetic_functions/gpt_5_5_pro_2026_totient_fibre_extremes/theorem_2_1|Theorem 2.1]];
  the note's held PDF, pp. 1--5 on the text layer and p. 4 on the page
  image (Proposition 3.1 with its proof, and the end of the proof of
  Theorem 2.1); the author manuscript of Pollack, Pomerance and Treviño
  held by
  [[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/_index|its card]],
  pp. 2 and 7--9 on the text layer and p. 8 on the page image (the
  definition of convenience, Ford's order of magnitude as quoted, Lemma
  4.1 with its proof, Lemma 5.1); Ford (1998),
  [[../library/arithmetic_functions/ford_1998_distribution_totients/_index|card]]
  provenance and pp. 1--3 of the held PDF on the text layer (Theorem 1 and
  Theorem 2 as statements).
- `docs/verification.md`: "Grading and claim standing", "Audit checklist:
  the canonical failure modes", "Whole-claim report" and the
  Erdos-specific "Audit checklist"; `docs/evidence.md` "Source fidelity";
  `docs/approach_vetting.md`; `docs/math_authoring.md`.

**Exposures.** Four, all disclosed here.

1. The problem page's header block before its first H2 was displayed whole
   while its Statement was read, so its Status paragraph (the status label
   and a pointer to the Current assessment), its References and its
   Formalization paragraph were seen. Only the Statement paragraph is used.
2. The library card pages were displayed whole rather than their
   provenance paragraphs alone: the note's card with its Contents, Compiled
   scope, Formal artifacts, Bears-on and Results paragraphs, the result
   page's "Read depth" paragraph (which carries a standing sentence), the
   Ford card with its results list, and the source manuscript's card
   through its Read status paragraph. Only the provenance paragraphs and
   the statements are used.
3. A directory listing of `wiki/research/erdos_49/evidence/verify/` showed
   the file names of other reviews and of a grade file; none was opened.
4. Nothing under any `evidence/` folder was read, no `_index.md`, no
   Current assessment or Known results text and no other section's review,
   and no web search was made. The page `research/erdos_416/connections`,
   which the section cites, is outside the read set and was not read (see
   F3).

**Independent computation.** One exact enumeration by the reviewer, of the
fibers of every totient up to two million, corroborates the witness of F1;
its mathematics and its coverage argument are given under "Strongest
attack". It is not filed as evidence.

## Restatement

Conventions. $\varphi$ is Euler's function; a totient is a value of
$\varphi$; the preimages of a totient $v$ are the integers $m$ with
$\varphi(m)=v$, a finite nonempty set; $f_{\max}(v)$ and $f_{\min}(v)$ are
its largest and smallest preimage; $V(x)$ counts the totients in $[1,x]$;
$Z(x)$ is Ford's function as defined on the Theorem 1.2 page. An integer
$n$ is convenient for a totient $d$ with preimages $n_1,\ldots,n_k$ when
$d\varphi(n)$ is a totient whose preimages are exactly $n_1n,\ldots,n_kn$
(Lemma 5.1 page; the source's p. 2 says "and no others").

- **S1** (Target paragraph, lines 470--477). Problem 694 asks for the size
  of $\max f_{\max}(v)/f_{\min}(v)$ over totients $v\le x$. The note's
  Proposition 3.1 states: if $a>b$ and $\varphi(a)=\varphi(b)=n$, then
  infinitely many distinct totients $N$ satisfy
  $f_{\max}(N)/f_{\min}(N)\ge a/b$. Both are characterizations of sources.
- **S2** ("What transports", lines 479--481). For a fixed totient $d$ and
  an integer $n$ convenient for $d$, the preimage set of $d\varphi(n)$ is
  $n$ times the preimage set of $d$, so $f_{\max}/f_{\min}$ is preserved
  exactly; and by (L4) this happens for a positive proportion of the
  totients up to $x$, the proportion depending on $d$.
- **S3** (Proposition 5, author-recorded, lines 483--492). For every
  totient $d$ with preimages $n_1<\cdots<n_k$ ($k\ge1$) there are $c_d>0$
  and $x_0(d)$ such that for every $x\ge x_0(d)$ the number of totients
  $v\le x$ with $f_{\max}(v)/f_{\min}(v)=n_k/n_1$ is at least $c_dZ(x)$,
  and $c_dZ(x)\ge c'_dV(x)$ with $c'_d>0$ depending on $d$.
- **S4** (first consequence sentence, lines 494--495). Every value $r$
  that $f_{\max}/f_{\min}$ takes on some totient is taken on at least
  $c_rV(x)$ totients $v\le x$ for all large $x$, with $c_r>0$ depending on
  $r$.
- **S5** (second consequence sentence, lines 495--497). The section's
  result strengthens the note's Proposition 3.1, under that proposition's
  hypotheses ($a>b$, $\varphi(a)=\varphi(b)=n$), from "infinitely many
  totients with ratio at least $a/b$" to "a positive proportion of the
  totients up to $x$ with ratio exactly $a/b$". This is the literal
  reading; with $a=f_{\max}(n)$ and $b=f_{\min}(n)$ it is S4.
- **S6** (cross-reference, lines 497--500). The Problem 416 connections
  page identifies the note's device with multiplication by convenient
  integers. This attributes a claim to a page outside the read set; it is
  not audited as mathematics (F3).
- **S7** (obstruction, lines 502--504). Proposition 5 gives nothing about
  $\max_{v\le x}f_{\max}(v)/f_{\min}(v)$: (L4) fixes $d$ before $x$ grows,
  so the ratios it produces are the constants $n_k/n_1$, while the
  extremal ratio grows like $\log\log x$ (the note's Theorem 2.1) on seeds
  that grow with $x$.
- **S8** (Outcome, lines 506--507). The transfer holds; the target is
  recorded as solved; Proposition 5 is a further result for the problem
  page, not a route.

## Checklist

- **Quantifiers and scope.** S3 fixes $d$ first and then takes
  $x\ge x_0(d)$; $c_d$ and $x_0(d)$ depend on $d$ exactly as (L4)'s
  constants depend on $D$ (and possibly on $d_1,d_2$, here all equal to
  $d$). The case $k=1$ is allowed and asserts a positive proportion of
  multiplicity-one totients if one exists, consistent with Ford's
  Theorem 2. S5 changes "at least $a/b$" into "exactly $a/b$" for
  arbitrary preimages $a>b$: fails (F1). Otherwise pass.
- **Circularity.** None. Proposition 5 consumes (L4) and (F) only, and
  neither mentions the ratio. Pass.
- **Model and convention changes.** The section's convenience is the
  source's (p. 2: preimages $n_1n,\ldots,n_kn$ "and no others"); the (L4)
  interface is Lemma 4.1 as printed on p. 8 (natural numbers
  $d_1,d_2\in\mathcal V$, $D\ge\max\{d_1,d_2\}$, "for large $x$",
  $\gg_DZ(x)$, $K$ absolute), and $d_1=d_2=d$, $D=d$ meets it with
  equality; $f_{\max},f_{\min}$ are the problem page's and the note's.
  Pass.
- **Finite and statistical overreach.** The section makes no finite or
  statistical claim. The reviewer's enumeration corroborates a witness
  whose proof is algebraic (below). Pass.
- **Uniformity.** "Positive proportion" is per fixed $d$ in S2 and S3 and
  per fixed ratio in S4; no uniformity in $d$ is claimed, and S7 says why
  none is available. The step $c_dZ(x)\gg_dV(x)$ needs Ford's absolute
  threshold as well as $x_0(d)$; the section's "for $x\ge x_0(d)$" is read
  with $x_0(d)$ enlarged past it, which costs nothing. Pass.
- **Extremal conclusions.** S7 claims only that nothing follows about the
  maximum; in the claim's own units (exact ratios) Proposition 5 yields
  the constant $n_k/n_1$, and the trivial $\max\ge n_k/n_1$ for $x\ge d$
  needs no proposition. The growth clause is imported from the note (F2).
  Pass.
- **Consequences and composition.** S4 follows from S3 by applying S3 to
  a totient realizing $r$. S5 does not follow (F1). S8's status clause
  inherits the problem page's record and proves nothing. (L4) is supplied
  to S3 at its actual strength; no unproved bridge. Fails at S5 only.
- **Computation.** The section performs none and consumes (P) nowhere.
  Inapplicable to the section. The reviewer's check used exact rational
  ratios with the coverage argument stated below.
- **Reproduction.** No rerun commands or coverage claims appear in the
  section. Inapplicable.
- **Source and verdict fidelity.** The paraphrase of Proposition 3.1
  matches the page image ($a>b$, $\varphi(a)=\varphi(b)=n$, infinitely
  many distinct totient values $N$ with $f_{\max}(N)/f_{\min}(N)\ge a/b$);
  the (L4) interface matches Lemma 4.1 as printed; the problem statement
  matches. "The current assessment records it as solved" is an attribution
  to excluded text and was not checked. S7's "grows like $\log\log x$" is
  the note's Theorem 2.1 at the note's own standing, not a proved input of
  this page (F2). Pass, with F2.

## Weakest steps

**W1: from integers $n$ to totients $v$ (Proposition 5).** Re-derived. Fix
$d$ with preimages $n_1<\cdots<n_k$. (L4) with $d_1=d_2=d$ and $D=d$ is
within its hypotheses, since $D\ge\max\{d_1,d_2\}$ holds with equality. For
$x\ge x_0(d)$ it gives a set $\mathcal A$ of at least $c_dZ(x)$ integers
$n$ with (i) $\varphi(n)\le x/d$, (ii) $n$ convenient for $d$ and (iii)
$n/\varphi(n)\le K$. For $n\in\mathcal A$ put $v=d\varphi(n)$. By (ii) the
preimage set of $v$ is exactly $\{n_1n,\ldots,n_kn\}$, and since
$n_1n<\cdots<n_kn$, $f_{\min}(v)=n_1n$ and $f_{\max}(v)=n_kn$, so the ratio
is $n_k/n_1$. By (i), $v\le d\cdot x/d=x$. The map $n\mapsto d\varphi(n)$
is injective on $\mathcal A$: $v$ determines $f_{\min}(v)=n_1n$ and hence
$n$. So at least $c_dZ(x)$ totients $v\le x$ have ratio $n_k/n_1$. The
section's proof uses (i) and (ii) only; (iii), which Lemma 5.1 needs to
keep the preimages below $x$, is not needed here because only $v\le x$ is
required. This step composes with nothing else.

**W2: from $Z(x)$ to $V(x)$.** Re-derived from Ford's Theorem 1 as printed
on p. 2 of the held PDF:

$$
V(x)=\frac{x}{\log x}\exp\bigl\{C(\log_3x-\log_4x)^2+D\log_3x
-(D+\tfrac12-2C)\log_4x+O(1)\bigr\},
$$

with $C=0.81781\ldots$ and $D=2.17696\ldots$. The exponent without the
$O(1)$ is the exponent of $Z(x)$ on the Theorem 1.2 page, whose $C'$ is
Ford's $D$ (the printed digits agree). Hence there is an absolute $C_1$
with $V(x)\le C_1Z(x)$ for all $x$ beyond an absolute threshold, and
$c_dZ(x)\ge(c_d/C_1)V(x)$ there. Since the counted totients are among the
$V(x)$ totients up to $x$, the proportion lies in $[c_d/C_1,1]$, which is
consistent because Ford's lower bound $Z(x)\ll V(x)$ forces $c_d$ to be
small.

**W3: the strengthening sentence (S5).** This is where the section's
argument stops carrying its conclusion. Proposition 5 applied to
$n=\varphi(a)=\varphi(b)$ gives a positive proportion with ratio exactly
$f_{\max}(n)/f_{\min}(n)$, a number that is at least $a/b$ and equals $a/b$
only when $a$ and $b$ are the extreme preimages of $n$. The sentence
asserts "exactly $a/b$" for the collision of Proposition 3.1, whose $a,b$
are arbitrary preimages. The gap cannot be closed by another argument: the
witness under "Strongest attack" shows that the strengthened conclusion is
false for the collision $\varphi(16)=\varphi(15)=8$.

## Strongest attack

**S3 (Proposition 5).** Four attacks. (a) Weaken convenience: if the
source's notion only required $d\varphi(n)$ to have the preimages $n_in$,
extra preimages could change the extremes; the source's p. 2 says "and no
others", and the Lemma 5.1 page's definition says "exactly", so the
extremes are $n_1n$ and $n_kn$. Failed. (b) Break the (L4) interface with
$d_1=d_2$ or $D=d$: Lemma 4.1 as printed fixes "natural numbers
$d_1,d_2\in\mathcal V$" and "$D\ge\max\{d_1,d_2\}$" with no distinctness
or strictness, and its candidate set uses $D$ only through
$\varphi(n)\le x/D$, $p_L\ge\max\{D+2,17\}$ and $M$. Failed. (c) The
boundary seeds: $k=1$ would give a positive proportion of multiplicity-one
totients if one exists, which is Ford's Theorem 2 for $k=1$; $d=1$, the
only odd totient, has preimages $1,2$ and ratio $2$, and Lemma 4.1 with
$d_1=d_2=D=1$ is the source's argument for multiplicity $2$; no
contradiction with anything held. Failed. (d) Non-injectivity: two
integers $n\ne n'$ with $d\varphi(n)=d\varphi(n')$ would share the least
preimage $n_1n=n_1n'$. Failed.

**S4.** A ratio $r$ that occurs is $f_{\max}(d)/f_{\min}(d)$ for some
totient $d$; S3 for that $d$ gives $c_dZ(x)\gg_dV(x)$ totients $v\le x$
with ratio exactly $r$. Attempted to find a ratio realized only by
totients $d$ to which (L4) does not apply; (L4) applies to every totient.
Failed.

**S5.** Succeeded, on the literal reading. Witness: $a=16$, $b=15$,
$\varphi(16)=\varphi(15)=8$, so the hypotheses of the note's Proposition
3.1 hold with $n=8$ (whose preimages are $15,16,20,24,30$). Claim: no
totient $v$ has $f_{\max}(v)/f_{\min}(v)=16/15$. Proof. Suppose
$15f_{\max}(v)=16f_{\min}(v)$. Since $\gcd(15,16)=1$, $16\mid f_{\max}(v)$;
write $f_{\max}(v)=16u$, so $f_{\min}(v)=15u$ with $u\ge1$ an integer, and
$\varphi(16u)=\varphi(15u)=v$. Write $u=2^ew$ with $w$ odd and $e\ge0$,
and $w=3^a5^bw'$ with $\gcd(w',15)=1$. Then
$\varphi(16u)=2^{e+3}\varphi(w)$ and
$\varphi(15u)=\varphi(2^e)\cdot8\,r_3r_5\,\varphi(w)$, where
$r_3=3^a/\varphi(3^a)$ is $1$ if $a=0$ and $3/2$ if $a\ge1$, and
$r_5=5^b/\varphi(5^b)$ is $1$ if $b=0$ and $5/4$ if $b\ge1$. If $e=0$,
equality forces $r_3r_5=1$, so $\gcd(u,30)=1$; then
$\varphi(30u)=\varphi(2)\varphi(15u)=v$ and $30u>16u=f_{\max}(v)$, a
contradiction. If $e\ge1$, equality reads $2^{e+2}r_3r_5=2^{e+3}$, so
$r_3r_5=2$; but $r_3r_5\in\{1,3/2,5/4,15/8\}$. Contradiction. $\square$
Hence the sentence "a positive proportion with ratio exactly $a/b$" is
false at $(a,b)=(16,15)$, while the note's "infinitely many with ratio at
least $16/15$" is true (with ratio $2$, from Proposition 5 at $d=8$, and
already at $d=1$). Corroboration: an exact enumeration of the fiber of
every totient $v\le2\cdot10^6$ found no ratio $16/15$; it is exhaustive
because a preimage $m$ of such a $v$ has
$\varphi(m)\ge\prod_{i\le\omega(m)}(p_i-1)$, which exceeds $2\cdot10^6$
for $\omega(m)\ge9$, so $\omega(m)\le8$ and
$m/\varphi(m)\le\prod_{i\le8}p_i/(p_i-1)=323323/55296<5.85$, so
$m<1.2\cdot10^7$, inside the enumerated range. Under the reading
$a=f_{\max}(n)$, $b=f_{\min}(n)$ the sentence is S4 and survives.

**S7.** Attempted to extract information about the maximum by letting $d$
depend on $x$ in Proposition 5: (L4)'s $c_D$ and $x_0(D)$ depend on $D$
(and on $d_1,d_2$), no uniform version is recorded on the Lemma 4.1 page,
and the source's proof builds $M$ from $D$; so the section's reason is
exact at the recorded interface. The clause "grows like $\log\log x$" is
the note's Theorem 2.1 (read on the page images), used here as
attribution; the obstruction needs only that $d$ is fixed. Failed, with F2
on the gloss.

**S1, S8.** Fidelity checks only: the paraphrases match the page image of
the note's p. 4 and the problem page's Statement. Nothing to refute.

## Premises

- **(L4)**, Lemma 4.1 of Pollack, Pomerance and Treviño, from the
  [[research/erdos_49/lemma_4_1_reconstruction|Lemma 4.1 page]]
  (author-recorded partial reconstruction: the two counting steps (F1) and
  (F2) are imported from Ford's argument as the source cites them and not
  checked; (iii) is written out), read in full, and confirmed against the
  printed statement on p. 8 of the held manuscript (page image): fixed
  natural numbers $d_1,d_2\in\mathcal V$, fixed $D\ge\max\{d_1,d_2\}$, for
  large $x$ at least $\gg_DZ(x)$ integers $n$ with (i)--(iii), $K$
  absolute. Interface used: $d_1=d_2=d$, $D=d$; only (i) and (ii) are
  consumed. Held.
- **Convenience**, from the
  [[research/erdos_49/lemma_5_1_reconstruction|Lemma 5.1 page]]
  (author-recorded reconstruction, read in full) and the source's p. 2
  (text layer): $d\varphi(n)$ is a totient with preimages
  $n_1n,\ldots,n_kn$ and no others. Held.
- **$Z(x)$**, from the
  [[research/erdos_49/theorem_1_2_reconstruction|Theorem 1.2 page]] (read
  in full); its constants $C$, $C'$ agree with the source's (4.2) on p. 8
  and with Ford's $C$, $D$ on p. 2 of the held Ford PDF to the digits
  printed. Held.
- **(F)**, Ford (1998) Theorem 1,
  [[../library/arithmetic_functions/ford_1998_distribution_totients/_index|card]]
  provenance and pp. 1--3 of the held PDF on the text layer:
  $V(x)=Z(x)e^{O(1)}$; consumed as $V(x)\le C_1Z(x)$ for large $x$.
  Theorem 2 was read as a statement for the $k=1$ consistency check only.
  Held; statement level.
- **The note's Proposition 3.1**, held PDF p. 4 (page image): $a>b$ and
  $\varphi(a)=\varphi(b)=n$ imply infinitely many distinct totient values
  $N$ with $f_{\max}(N)/f_{\min}(N)\ge a/b$; proof by $N_r=(r-1)n$ for
  primes $r\nmid ab$, read in full. Its standing is the card's (not
  independently reviewed); consumed only as the statement that S1
  characterizes and S5 strengthens.
- **The note's Theorem 2.1**,
  [[../library/arithmetic_functions/gpt_5_5_pro_2026_totient_fibre_extremes/theorem_2_1|result page]]
  Statement section and the held PDF pp. 2--4 (text layer, p. 4 on the
  page image): $\mathcal R(x)=(e^\gamma+o(1))\log\log x$. Consumed by S7's
  gloss only; not verified here; author-recorded at most on its page.
- **Problem 694 Statement**,
  [[problems/arithmetic_functions/E0694/_index|problem page]]: investigate
  $\max_{n\le x}f_{\max}(n)/f_{\min}(n)$ over totients $n$. Held.
- **(P)** and the Theorem 3.1, Theorem 3.3 and Lemma 3.2 pages: not
  consumed by this section.

## Findings

**F1** (required). Location, lines 495--497: "which strengthens the note's
Proposition 3.1 from 'infinitely many with ratio at least $a/b$' to 'a
positive proportion with ratio exactly $a/b$'". Defect: under Proposition
3.1's hypotheses $a,b$ are any two preimages of $n$, and Proposition 5
yields ratio exactly $f_{\max}(n)/f_{\min}(n)$, which equals $a/b$ only
for the extreme pair; the strengthened conclusion is false in general.
Witness: $a=16$, $b=15$, $n=8$; no totient has extreme ratio $16/15$
(proof under "Strongest attack"). Proposed replacement: "... to 'a
positive proportion with ratio exactly $f_{\max}(n)/f_{\min}(n)$, hence at
least $a/b$'", or restrict $a$, $b$ to the extreme preimages of $n$ before
saying "exactly".

**F2** (note). Location, lines 503--504: "while the extremal ratio grows
like $\log\log x$ through seeds that grow with $x$". The growth rate is the
note's Theorem 2.1 at the note's own standing (its result page is
author-recorded at most); the obstruction needs only that (L4) fixes $d$.
Proposed: attribute the clause ("by the note's Theorem 2.1, as filed") or
weaken it to "is not bounded by any fixed $n_k/n_1$".

**F3** (note). Location, lines 497--500: "identifies the note's device
with the same multiplication by convenient integers". The note multiplies
the pair $a,b$ by a prime $r\nmid ab$ and concludes only that $(r-1)n$ "has
at least the two preimages $ra$ and $rb$" (p. 4); it does not use, and
does not need, that $r$ is convenient for $n$, which is why it obtains "at
least $a/b$" where Proposition 5 obtains "exactly". The identification is
attributed to a page outside this review's read set and was not checked
there. Proposed: "the same kind of multiplication, without the exactness
clause of convenience", or leave the sentence to the cited page.

## Verdict

- S1: refutation-failed (the source characterizations match the held
  pages).
- S2: refutation-failed.
- S3 (Proposition 5): refutation-failed.
- S4: refutation-failed.
- S5: refuted-as-stated, on the literal reading with Proposition 3.1's
  hypotheses; witness $(a,b)=(16,15)$. Under the extreme-pair reading it is
  S4, which stands.
- S6: not audited; an attribution to a page outside the read set (F3).
- S7: refutation-failed; the growth-rate gloss is attributed, not proved,
  on this page (F2).
- S8: refutation-failed for the transfer clause; the status clause records
  the problem page and is not a claim of this section.

Limitations. Proposition 5 is verified relative to (L4) at the Lemma 4.1
page's standing, which imports Ford's two counting steps unchecked, and to
Ford's Theorem 1 read at statement level; this review raises neither. The
note's Theorem 2.1 was not verified and enters only S7's gloss. The
reviewer's enumeration is corroboration; the refutation of S5 rests on the
algebraic proof. This focused review assigns no tier and changes no status.
