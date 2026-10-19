---
name: research/erdos_49/evidence/verify/connections_problem_51_totients_whose_smallest_preimage_is_l_review
title: "Independent review of the connections section: Problem 51: totients whose smallest preimage is large"
desc: |
  Refutation-failed for the bounded-ratio transport (S1), the stated
  obstruction (S2) and the target restatement (S3); the corpus-state
  sentence (S4) is stale. Zero required corrections, two suggested, two
  notes.
created: 2026-09-28T18:13:51Z
updated: 2026-09-28T20:43:42Z
---

***

## Subject and independence

The reviewer is an independent reviewer working in a fresh context from the
commissioned assignment alone, with no part in writing the connections page,
the reconstruction pages behind it or the problem page, and no earlier
reading of any of them. The charge is refutation.

**Subject.** Page `wiki/research/erdos_49/connections.md` as it stood on
2026-09-28T13:50:48Z, section "## Problem 51: totients whose smallest preimage
is large", lines 509--541 (the H2 heading through the line before the next H2 at
line 542). Neither the section nor the page's overview names a lead page for
Problem 51; the two leads named on the page carry Problems 1004 and 417 and were
not read.

**Reading and depth.**

- The section, clause by clause, every sentence treated as a claim surface.
- The page's opening paragraphs and its section "Notation and the inputs
  used" (lines 1--111), for the conventions and the inputs (T1), (T3),
  (L4), (F) and (P); the section consumes only (L4) and (F).
- The page's section "Problem 694" (lines 468--508) in full, because the
  section consumes "the totients of Proposition 5"; the proof of
  Proposition 5 was re-derived here only as far as the section relies on
  it, and its own review belongs to another reviewer.
- [[research/erdos_49/lemma_4_1_reconstruction|The Lemma 4.1 reconstruction]]
  in full (statement, candidate set, the imported counting steps
  (F1)--(F2), the proof of (iii)), as a premise at the standing the
  assignment grants.
- [[research/erdos_49/lemma_5_1_reconstruction|The Lemma 5.1 reconstruction]]
  for the definition of a convenient integer and the seed (P), and
  [[research/erdos_49/theorem_1_2_reconstruction|the Theorem 1.2 reconstruction]]
  for the definition of $Z(x)$ and the quotation of Ford's order of
  magnitude; both as premises.
- The Statement of [[problems/arithmetic_functions/E0051/_index|Problem 51]].
- The provenance and read-status paragraphs of the source card
  [[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/_index|Pollack, Pomerance and Treviño (2013)]]
  and the held author manuscript: p. 2 (the definition of a convenient
  integer), p. 7 (the definition of $Z(x)$ and the quoted order of
  magnitude), pp. 8--9 (Lemma 4.1 with its proof, Lemma 5.1); the text
  layer of pp. 8--9 was checked against the page images.
- The card
  [[../library/arithmetic_functions/ford_1998_distribution_totients/_index|Ford (1998)]]
  and the statement of its Theorem 1 on p. 2 of the held PDF (text layer).
- The commissioned parts of the verification guide ("Whole-claim report",
  "Audit checklist", "Grading and claim standing"), the approach-vetting
  guide, the evidence guide ("Source fidelity") and the math-authoring
  guide.

**Exposures.** Three, disclosed here.

1. The problem page is short, and the read of its Statement returned the
   whole page: its Current assessment, Progress and Known Results text
   reached the reviewer. That text records that the question is equivalent
   to unboundedness of the least-preimage ratio over all totients, points
   to another folder's observation about totients all of whose preimages
   share a divisor, and summarizes this very section. No argument from it
   is used below: the equivalence is elementary and is re-derived under
   S2, and the shared-divisor observation plays no part in any attack.
   Finding F3 rests on this exposure and says so.
2. The page-level "Standing" and "Outcomes at a glance" paragraphs (lines
   37--57) were read together with the notation section; they are the
   page's own author-recorded standing text and were used only to confirm
   that the section's outcome matches the overview.
3. The Ford card is one short body, and its result digest was read while
   locating its provenance paragraph.

Nothing under any `evidence/` folder, the folder's `_index.md`, any other
section's review, any lead page, any current assessment other than the one
in exposure 1, or any web source was read.

## Restatement

Conventions of the page, confirmed at each use: $\varphi$ is Euler's
function; a totient is a value of $\varphi$; the preimages of a totient $v$
are the integers $m$ with $\varphi(m)=v$, a finite nonempty set; $V(x)$
counts the totients in $[1,x]$; $Z(x)$ is Ford's function as defined on the
Theorem 1.2 page, which matches the source's p. 7; an integer $n$ is
convenient for a totient $d$ with preimages $n_1,\ldots,n_k$ when
$d\varphi(n)$ is a totient whose preimages are exactly $n_1n,\ldots,n_kn$
and no others (the source's p. 2, restated on the Lemma 5.1 page); $K\ge1$
is the absolute constant of (L4)(iii); $C_1$ and $x_1$ are the absolute
constants with $V(x)\le C_1Z(x)$ for $x\ge x_1$ supplied by (F).

**S1 (transport; lines 516--526).** Let $d$ be any totient, with preimages
$n_1<\cdots<n_k$, so $n_1$ is its least preimage. There are $c_d>0$ and
$x_0(d)$ such that for every $x\ge x_0(d)$: the integers $n$ supplied by
(L4) for $d_1=d_2=D=d$ number at least $c_dZ(x)$; for each of them
$v=d\varphi(n)$ is a totient with $v\le x$, with least preimage $n_v=n_1n$,
and with

$$
\frac{n_v}{v}=\frac{n_1}{d}\cdot\frac{n}{\varphi(n)}
\in\Bigl[\frac{n_1}{d},\,K\frac{n_1}{d}\Bigr];
$$

distinct $n$ give distinct $v$; hence, for $x\ge\max\{x_0(d),x_1\}$, at
least $(c_d/C_1)V(x)$ totients $v\le x$ have least-preimage ratio in
$[n_1/d,Kn_1/d]$. The proportion $c_d/C_1$ and the threshold depend on
$d$; $K$ does not.

**S2 (obstruction; lines 528--540).** (a) For a fixed seed $d$, every
totient the mechanism produces has least-preimage ratio at most $Kn_1/d$.
(b) Hence an infinite set of produced totients with ratio tending to
infinity requires seeds $d_j$ with $n_1(d_j)/d_j\to\infty$, and a family of
such seeds is itself the question of Problem 51. (c) The bound (iii) is not
incidental: it comes from the sizes of the primes in the candidate set
$\mathcal B$, and replacing those primes by small ones to make
$n/\varphi(n)$ large would break the count of convenient integers, which is
Ford's argument for exactly that set. (d) Boundedness of the ratio on the
produced totients is consistent with either answer to Problem 51. Outcome:
the mechanism transports a ratio within a bounded factor and cannot create
unbounded ratios; the transfer fails.

**S3 (target; lines 511--513).** Problem 51 asks whether there is an
infinite set $A$ of totients such that, with $n_a$ the least preimage of
$a$, $n_a/a\to\infty$ as $a\to\infty$ through $A$.

**S4 (corpus state; lines 513--514).** "The corpus page is not compiled
beyond the statement (open)." A description of the corpus, not a
mathematical claim.

## Checklist

- **Quantifiers and scope.** Pass. S1 fixes $d$ before $x$, and the
  section writes the count as $\gg_dV(x)$, so the $d$-dependence of the
  proportion and of the threshold is on the surface; $K$ is absolute in
  the source and on the Lemma 4.1 page. S2(a) is explicitly "for a fixed
  seed". S3 carries the problem's quantifiers exactly. The one scope
  question is whether "the mechanism" in S2 includes repeated application;
  see F1 and W3.
- **Circularity.** Pass. Nothing equivalent to Problem 51 is assumed;
  S2(b) states an equivalence and uses it only to locate where growth
  would have to come from.
- **Model and convention changes.** Pass. The objects are the actual
  totients and their actual preimage sets; "convenient" is used as the
  source defines it, and the least preimage of $d\varphi(n)$ is read off
  from the exact preimage set that convenience supplies, not from a relaxed
  model.
- **Finite and statistical overreach.** Pass; nothing finite or heuristic
  is used. The seed enumeration (P) is not consumed by this section.
- **Uniformity.** Pass. $K$ is absolute (source p. 8, and the Lemma 4.1
  page's proof of (iii) from the imported Ford inequality); $c_d$ and
  $x_0(d)$ depend on $d$ and are so labeled; $C_1$ and $x_1$ are absolute.
  Under repeated application the compounding of $K$ is addressed in W3.
- **Extremal conclusions.** Pass. "Least preimage $n_1n$" is checked
  against the exact preimage set $\{n_in\}$; the interval $[n_1/d,Kn_1/d]$
  is a containment, both endpoints justified ($n/\varphi(n)\ge1$ and
  (iii)); no attainment or sharpness is claimed.
- **Consequences and composition.** Pass with two remarks. "So every
  attained ratio ... positive proportion" follows from S1 and (F). "Fails"
  follows from S2(a)--(b) for one application and, for repeated
  application, from the derivation in W3 that the section does not contain
  (F1). The section consumes the construction inside the proof of
  Proposition 5 rather than its statement (F4). The composition inherits
  the standing of (L4), whose counting steps (F1)--(F2) are imported from
  Ford and not reconstructed; the page's inputs list says so.
- **Computation.** Inapplicable: the section performs no computation and
  consumes none.
- **Reproduction.** Inapplicable: no rerun instruction or coverage claim.
- **Source and verdict fidelity.** Pass for the three imports: (L4) matches
  the source's Lemma 4.1 on the page images (fixed $d_1,d_2\in\mathcal V$,
  fixed $D\ge\max\{d_1,d_2\}$, $\gg_DZ(x)$ integers, (i)--(iii) with $K$
  absolute); the definition of convenient matches p. 2; (F) matches Ford's
  Theorem 1 and the source's p. 7. S3 matches the problem's Statement. The
  sentence characterizing what "would break" Ford's argument overstates
  what the corpus has read (F2).

## Weakest steps

**W1 (least preimage and injectivity, S1).** Fix $n$ from (L4) with
$d_1=d_2=D=d$. By (ii), $d\varphi(n)$ is a totient whose preimages are
exactly $n_1n,\ldots,n_kn$. Multiplication by $n$ preserves order, so the
least is $n_1n$ and $n_v=n_1n$. If $d\varphi(n)=d\varphi(n')$ for two such
integers, the totients coincide, so their least preimages coincide:
$n_1n=n_1n'$ and $n=n'$. By (i), $v=d\varphi(n)\le d\cdot x/d=x$. So
$n\mapsto v$ is injective into the totients of $[1,x]$. Nothing here uses
more than (i) and (ii) at the parameters $d_1=d_2=d$, $D=d$; (L4) allows
$d_1=d_2$ (the source says "fix natural numbers $d_1,d_2\in\mathcal V$",
with no distinctness) and allows $D=\max\{d_1,d_2\}$ (the inequality is not
strict). Composition: this is the first half of the proof of Proposition 5,
re-derived, and the section's "least preimage $n_1n$" is its output.

**W2 (the count, S1).** (L4) gives at least $c_dZ(x)$ such $n$ for
$x\ge x_0(d)$; by W1 as many distinct totients $v\le x$. (F), read from
Ford's Theorem 1 ($V(x)=Z(x)e^{O(1)}$ for large $x$), gives absolute $C_1$
and $x_1$ with $V(x)\le C_1Z(x)$ for $x\ge x_1$. Hence for
$x\ge\max\{x_0(d),x_1\}$ the number of such $v$ is at least
$(c_d/C_1)V(x)$: a positive proportion of the totients up to $x$, the
proportion depending on $d$. The ratio identity
$n_v/v=(n_1n)/(d\varphi(n))=(n_1/d)(n/\varphi(n))$ is arithmetic, and
$1\le n/\varphi(n)\le K$ by the trivial lower bound and (iii).

**W3 (the obstruction under repeated application, S2).** The section's
argument for S2(a) is one line: one application multiplies the seed's
ratio by $n/\varphi(n)\in[1,K]$. The strongest reading of "the mechanism"
allows applying (L4) again to the totient just produced, because
convenience composes. Independent derivation of the composition and of the
bound that closes it; the integers (L4) supplies are, on the Lemma 4.1
page, elements of the candidate set $\mathcal B$, and only that page's
recorded properties of $\mathcal B$ are used.

*Composition.* Let $N$ be convenient for $d$, so $d'=d\varphi(N)$ has
preimages exactly $n_iN$, and let $n$ be supplied by (L4) for the seed $d'$
(as $d_1=d_2$) with some $D\ge d'$. Every prime $q\mid N$ has
$q-1\mid\varphi(N)\mid d'$, so $q\le d'+1<D+2\le p_L$, the least prime of
$n$; hence $\gcd(N,n)=1$ and $\varphi(Nn)=\varphi(N)\varphi(n)$. Since $n$
is convenient for $d'$, the totient $d'\varphi(n)=d\varphi(Nn)$ has
preimages exactly $n_iNn$: $Nn$ is convenient for $d$. So a $j$-fold
iteration produces $d^{(j)}=d\varphi(N_j)$ with
$N_j=n^{(0)}\cdots n^{(j-1)}$ convenient for $d$, least preimage $n_1N_j$,
and ratio $r_j=(n_1/d)\prod_{l<j}n^{(l)}/\varphi(n^{(l)})$. The section's
bound compounds to $K^jn_1/d$, unbounded in $j$, so S2(a) as written does
not by itself bound $r_j$.

*Bound.* Let $n=p_0\cdots p_L$ be any element of $\mathcal B$ for the
parameter $D$. Then $p_i\ge p_L\ge D+2$ for every $i$, and the Lemma 4.1
page's proof of (iii), from the imported inequality (4.4), gives
$p_i\ge\exp(\exp(0.2\cdot1.8^{L-i}))$ for $1\le i\le L$. Put
$a_t=\exp(-\exp(0.2\cdot1.8^t))$ and

$$
S(D)=\sum_{t\ge0}\min\Bigl\{a_t,\frac1{D+2}\Bigr\},\qquad
\varepsilon(D)=e^{4S(D)}-1 .
$$

Then $\sum_{i=0}^L1/p_i\le2\sum_{i=1}^L1/p_i\le2S(D)$ (the factor $2$
covers $p_0>p_1$, as on the Lemma 4.1 page), and with
$-\log(1-1/p)\le2/p$, $n/\varphi(n)\le e^{4S(D)}=1+\varepsilon(D)$. Here
$\varepsilon(1)\le e^{4\sum_ta_t}-1=K-1$ recovers the page's $K$, and
$S(D)$ is nonincreasing in $D$ with $S(D)\to0$: $a_t\ge1/(D+2)$ only for
$t\le T(D):=\log(5\log_2(D+2))/\log1.8$ (once $\log_2(D+2)>0.2$), and
$a_{t+1}/a_t<0.63$ for $t\ge1$, so $S(D)\le(T(D)+3.8)/(D+2)=O(\log_3D/D)$.
Along an iteration, $\varphi(n^{(j)})\ge p_L-1\ge D_j+1\ge d^{(j)}+1\ge2$,
so $d^{(j+1)}\ge2d^{(j)}$ and $D_j\ge d^{(j)}\ge2^jd\ge2^j$. Therefore

$$
r_j\le\frac{n_1}{d}\prod_{l<j}\bigl(1+\varepsilon(D_l)\bigr)
\le\frac{n_1}{d}\prod_{l\ge0}\bigl(1+\varepsilon(2^l)\bigr)=:K'\frac{n_1}{d},
$$

and $K'$ is finite and absolute because $\varepsilon(D)\le4KS(D)$ and
$\sum_lS(2^l)<\infty$. So unlimited iteration still transports the seed's
ratio within an absolute factor, and S2(a) holds in the strong reading
with $K'$ in place of $K$. The same computation shows more than the section
says: the factor contributed by a seed $d$ is at most $1+\varepsilon(d)$,
which tends to $1$ as the seed grows, so the mechanism does not even
multiply the ratio of a large seed by a fixed amount. Composition with
S2(b): the only remaining source of growth is the seeds, as the section
says.

## Strongest attack

**S1.** Attack: find a produced $v$ whose least preimage is not $n_1n$, or
two $n$ with the same $v$, or a $v>x$, so that the count or the ratio
interval fails. Each is excluded by W1 from (i) and (ii) alone; the
interval uses only $n/\varphi(n)\ge1$ and (iii). A second attack, that (L4)
might not admit $d_1=d_2$ or $D=d$ exactly, fails against the source's
statement on the page image (no distinctness, non-strict inequality). A
third, that "positive proportion" hides a dependence, fails because the
section writes $\gg_dV(x)$ and W2 exhibits the constant $c_d/C_1$. The
attack failed.

**S2.** Attack: iterate the transfer, using the composition of convenience
(W3), so that the bound $Kn_1/d$ compounds to $K^jn_1/d$ and the section's
one-line reason no longer bounds the ratio; then hope that a positive
proportion of the (L4) integers have $n/\varphi(n)\ge1+\delta$ for a fixed
$\delta>0$, which would make the iterated ratios grow geometrically and
answer Problem 51. The attack failed at the second step: every prime of an
(L4) integer exceeds $D+1$, hence the seed, and the derivation in W3 shows
$n/\varphi(n)\le1+\varepsilon(D)$ with $\varepsilon(D)=O(\log_3D/D)$,
summable along the at-least-doubling seeds, so the iterated ratio stays
below an absolute multiple of the seed's ratio. The statement survives,
but the section's written argument does not cover this reading (F1). A
second attack, choosing the seed as a function of $x$, is absorbed by
S2(b): the produced ratio is within a bounded factor of the seed's, so
growth must already be present in the seeds, and seeds with unbounded
ratio are a positive answer to Problem 51 by themselves ($A=\{d_j\}$). The
converse is equally elementary: if $n_a/a$ is unbounded over totients,
choosing $a_j$ with $n_{a_j}/a_j>j$ gives an infinite $A$ with
$n_a/a\to\infty$, so "no such $A$" is the same as "the ratio is bounded
over all totients", and S2(d) is right that bounded ratios on a positive
proportion of totients decide nothing.

**S3.** Attack: compare with the Statement of the problem page clause by
clause (infinite set, every member a totient, least preimage, ratio
tending to infinity along the set). They agree. The attack failed.

**S4.** Not a mathematical claim; see F3.

## Premises

- **(L4), Lemma 4.1 of the source.** Interface used: for fixed totients
  $d_1,d_2$ and fixed $D\ge\max\{d_1,d_2\}$, an absolute $K\ge1$, a
  $c_D>0$ and $x_0(D)$ with at least $c_DZ(x)$ integers $n$ satisfying (i)
  $\varphi(n)\le x/D$, (ii) $n$ convenient for $d_1$ and $d_2$, (iii)
  $n/\varphi(n)\le K$, for $x\ge x_0(D)$; used at $d_1=d_2=D=d$. Source
  held (author manuscript, statement and proof pp. 8--9, read on the page
  images). Reconstruction page read in full; its standing is a partial
  author-recorded reconstruction with the counting steps (F1)--(F2)
  imported from Ford and the inequality (4.4) imported as quoted; W3 uses
  the candidate set's definition ($p_L\ge D+2$, decreasing primes) and the
  page's derivation from (4.4), nothing more.
- **Definition of a convenient integer.** Source p. 2 (text layer),
  restated on the Lemma 5.1 page; the two agree ("and no others").
- **(F), Ford's Theorem 1.** Interface used: $V(x)\le C_1Z(x)$ for
  $x\ge x_1$ with $Z(x)$ as on the Theorem 1.2 page. Held; the statement
  was read on p. 2 of the held PDF (text layer) and agrees with the
  Theorem 1.2 page's $Z(x)$ (the source's $C'$ is Ford's $D$). Ford's proof
  was not read and is not needed at this interface.
- **Proposition 5** (the page's Problem 694 section). Author-recorded; the
  section consumes the construction in its proof, re-derived in W1--W2 at
  the strength consumed. Its own review is another reviewer's.
- **Problem 51.** Statement read on the problem page; S3 agrees with it.
- **Explicit assumptions.** None beyond the above. No batch acceptance
  order applies.

## Findings

**F1 (suggested).** Location, lines 528--530: "The transported ratio is
bounded by $Kn_1/d$ for a fixed seed, and a family of seeds $d_j$ with
$n_1(d_j)/d_j\to\infty$ is the question itself." Defect: the argument
bounds one application; convenience composes (W3), so the mechanism can be
applied to the totients it produces, and the stated bound then compounds
to $K^jn_1/d$, which does not bound the ratio. Witness: for $N$ convenient
for $d$ and $n$ supplied by (L4) for the seed $d\varphi(N)$, $Nn$ is
convenient for $d$ (W3, composition). The statement survives because every
prime of an (L4) integer exceeds its parameter $D$, hence the seed, giving
$n/\varphi(n)\le1+\varepsilon(D)$ with $\varepsilon(D)=O(\log_3D/D)$,
summable along the at-least-doubling seeds (W3, bound). Proposed
replacement: after the quoted sentence add "Repeating the construction
does not help: if $N$ is convenient for $d$ and $n$ is supplied by (L4)
for the seed $d\varphi(N)$, then $Nn$ is convenient for $d$, so the ratio
is multiplied once more by $n/\varphi(n)$; but every prime of $n$ exceeds
$D+1\ge d\varphi(N)$, so $n/\varphi(n)-1\ll\log_3D/D$, and along any
iteration the seeds at least double, so the product of the factors
converges: the ratio stays within an absolute factor of $n_1/d$, however
often the construction is repeated."

**F2 (suggested).** Location, lines 532--534: "replacing those primes by
small ones to make $n/\varphi(n)$ large would break the convenience count,
which is Ford's argument for exactly that set." Defect: the sentence
asserts how Ford's argument behaves under a modification, but the corpus
has not read that argument: the Lemma 4.1 page imports (F2) exactly as the
source cites it and records that Ford's paper was not read for that page.
What the record supports is weaker and sufficient. Witness: the Lemma 4.1
page's "Imported counting steps (not reconstructed)". Proposed
replacement: "and the count of convenient integers, (F2), is recorded only
for that candidate set; no count is recorded for a set admitting small
primes, and the corpus has not read the argument that would have to be
adapted." Optionally add the stronger fact from W3 that the factor
$n/\varphi(n)$ of an (L4) integer is at most $1+O(\log_3D/D)$, so the
candidate set's primes force the factor toward $1$ for large seeds.

**F3 (note; rests on exposure 1).** Location, lines 513--514: "The corpus
page is not compiled beyond the statement (open)." In the reviewed state the
problem page carries Progress text (an equivalence and a pointer to another
folder's computation) and Known Results text summarizing this section, both
landed in the same change series as the page. Witness: the problem page as it
stood on 2026-09-28T13:50:48Z, sections Progress and Known Results. Proposed
replacement: drop the sentence, or replace it by "The corpus page records the
statement (open) and author-recorded transfers; no assessment is recorded." The
reviewer saw the page's text only through the disclosed exposure and reports it
for the integrator's judgment.

**F4 (note).** Location, lines 516--518: "the $\gg_dV(x)$ totients
$v=d\varphi(n)\le x$ of Proposition 5 have least preimage $n_1n$". Defect:
the statement of Proposition 5 exposes neither the form $v=d\varphi(n)$
nor convenience; the section consumes the construction inside its proof
((L4) at $d_1=d_2=D=d$). Witness: Proposition 5's statement, lines
482--485. Proposed replacement: "the $\gg_dV(x)$ totients
$v=d\varphi(n)\le x$ constructed in the proof of Proposition 5, from (L4)
with $d_1=d_2=D=d$, have least preimage $n_1n$ by (ii)".

## Verdict

- **S1** (transport within $[n_1/d,Kn_1/d]$ on $\gg_dV(x)$ totients):
  **refutation-failed**. Re-derived in W1--W2 from (L4)(i)--(iii) and (F)
  at their recorded interfaces; the constants depend on $d$ exactly as the
  section writes them.
- **S2** (the obstruction and the outcome "fails"): **refutation-failed**.
  The written argument covers one application of (L4) to a fixed seed,
  which is the mechanism as the page defines it; under the strong reading
  that admits repeated application the section is silent, and the
  statement holds by the independent derivation in W3 (F1). S2(c) is right
  in substance and overstated in wording (F2). S2(b) and S2(d) are
  elementary and correct.
- **S3** (the target restated): **refutation-failed**; faithful to the
  problem's Statement.
- **S4** (corpus state): not a mathematical claim; stale in the reviewed state
  (F3).

Limitations. S1 and S2 inherit the standing of (L4), whose counting steps
(F1)--(F2) are imported from Ford's paper and were neither reconstructed by
the corpus nor read by this reviewer; W3 uses the imported inequality (4.4)
exactly as the Lemma 4.1 page does. Proposition 5 and the page's shared
inputs were checked at their interfaces only. Required corrections: none.
This focused review assigns no tier and changes no status.
