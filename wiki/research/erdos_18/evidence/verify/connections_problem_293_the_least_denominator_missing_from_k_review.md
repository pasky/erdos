---
name: research/erdos_18/evidence/verify/connections_problem_293_the_least_denominator_missing_from_k_review
title: "Independent review of the connections section: Problem 293: the least denominator missing from k-term decompositions"
desc: |
  Refutation review of the Problem 293 section of the connections page as of
  2026-09-28T13:50:48Z: every author-recorded statement survives
  (refutation-failed), with zero required corrections, two suggested
  corrections (Remark 6 cited outside its stated scope for the non-factorial
  case of Lemma C', and a missing bounded-seed qualification on the Lemma D
  cap) and three notes.
created: 2026-09-28T18:02:47Z
updated: 2026-09-28T18:02:47Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, given only the
commissioning assignment. The reviewer took no part in writing the
connections page, the lead page, the reconstruction pages or the library
pages, consulted no author of them, and read no earlier review or grade.

**Subject.** Page `wiki/research/erdos_18/connections.md` as it stood at
2026-09-28T13:50:48Z, section
`## Problem 293: the least denominator missing from k-term decompositions of 1`,
lines 345–430 (from the H2 heading at line 345 to the line before the next
H2 heading at line 431). The page's preamble (conventions, lines 1–46) and
its `## Shared lemmas` section (lines 47–243) were read as inputs. Lead page:
[[research/leads/factorial_unit_fraction_transfer/_index|factorial_unit_fraction_transfer]]
(read in full).

**Reading.** Read in full: the section, the preamble and the shared lemmas
of [[research/erdos_18/connections|the connections page]]; the lead page;
the reconstruction pages
[[research/erdos_18/doorn_lemma_3_1_reconstruction|Lemma 3.1]],
[[research/erdos_18/doorn_proposition_4_1_reconstruction|Proposition 4.1]],
[[research/erdos_18/doorn_theorem_1_1_reconstruction|Theorem 1.1 (note)]],
[[research/erdos_18/hughes_lemma_4_reconstruction|Lemma 4]],
[[research/erdos_18/hughes_theorem_1_reconstruction|Theorem 1]] and
[[research/erdos_18/hughes_remark_6_reconstruction|Remark 6]], with the
definitions part of
[[research/erdos_18/hughes_corollary_3_reconstruction|Corollary 3]]; the
statement blocks of [[problems/unit_fractions/E0293/_index|Problem 293]],
[[problems/unit_fractions/E0304/_index|Problem 304]] and
[[problems/divisors/E0018/_index|Problem 18]]; the provenance paragraphs and result
pages of
[[../library/unit_fractions/doorn_2025_smallest_denominator_not_contained_unit_fraction/_index|van Doorn–Tang (2025)]]
(Theorem 1.1, Section 3, inequality (1.2)) and of
[[../library/divisors/doorn_2026_practical_numbers_egyptian_fractions/_index|van Doorn (2026)]]
(Theorem 1.2, Theorem 1.3, Proposition 4.1), and the target page and
provenance paragraphs of the library card for the accepted Lean proof of
part (b), linked from the Problem 18 page; the held PDFs of the two van Doorn
sources in the extracted text (note pp. 1–2 and 5–7; paper pp. 1–7) and on
the page images of note p. 6 and paper pp. 2 and 7; and the commissioned
sections of `docs/verification.md`, `docs/approach_vetting.md`,
`docs/evidence.md` and `docs/math_authoring.md`. The Hughes PDF was not
opened: the section consumes Theorem 1 and Remark 6 only through their
reconstruction pages, which are premises here.

**Exposures.** (1) The statement blocks of the three problem pages carry a
`**Status.**` paragraph inside the same top block as the statement; those
paragraphs, and on the Problem 18 page a provenance paragraph for the
accepted proof file, were displayed by the extraction. They restate the
bounds the section quotes and were not used beyond that. No Current
assessment, Known results or acceptance section was opened. (2) Item (304.1)
of the page's Problem 304 section (statement and proof, lines 258–281) was
read as the interface of an input consumed by the section's converse-flow
sentence. (3) A string count on the Problem 293 page (two lines contain
`v(8)`, none contains `v(4)`; no content displayed) was taken to test the
section's closing sentence. (4) The lead page's opening section summarizes
the two problem pages' Current assessments; it is part of the allowed lead
page. No review, grade, folder index, workspace file or web search was read.

## Restatement

**Conventions confirmed at the inputs.** For practical $N$, $h(N)$ is the
least $k$ such that every integer $1\le m\le N$ is a sum of at most $k$
distinct divisors of $N$, a fresh set for each $m$. This is the reading of
the accepted formal statement (its `practicalH` takes the supremum over
`Finset.Icc 1 n`, per the accepted-proof target page), of the note's Lemma
5.1 and Lemma 3.1 (note p. 1: "every positive integer $m\le n$"), and of
Lemma C and Lemma C′. $D_k$ is the set of denominators occurring in some
identity $1=1/n_1+\cdots+1/n_k$ with $1\le n_1<\cdots<n_k$ and exactly $k$
terms; $v(k)=\min\{m>1:m\notin D_k\}$, so every integer $2\le b<v(k)$ lies
in $D_k$. $N(a,b)$ and $N(b)$ are as on the Problem 304 page (denominators
above $1$). $\log$ is natural; $c_0=14/\log2$.

- **S1 (transfer observation).** Let $b\ge2$ and let $N$ be practical with
  $N\ge b$ and $b\nmid N$. Then $1$ is a sum of $j$ distinct unit fractions
  with denominators above $1$, one of them $1/b$, for some $j\le2h(N)+1$;
  and $b\in D_k$ for every integer $k\ge2h(N)+1$. Inputs: Lemma C at
  $a=b-1$ and the nesting $D_k\subseteq D_{k+1}$ for $k\ge2$.
- **S2 ((293.1), conditional).** Premise: for every $\varepsilon>0$ there
  is $n_0(\varepsilon)$ with $h(n!)<n^{\varepsilon}$ for all
  $n\ge n_0(\varepsilon)$, at the standing of the site-accepted proof.
  Conclusion: for every $\varepsilon>0$ there is $k_0(\varepsilon)$ such
  that $v(k)\ge\exp((k/5)^{1/\varepsilon})$ for every integer
  $k\ge k_0(\varepsilon)$; the constant $5$ is absolute and
  $k_0(\varepsilon)$ is ineffective.
- **S3 (corollary of S2 and its calibration).** Under the same premise, for
  every fixed $A>0$, $v(k)\ge\exp(k^{A})$ for all large $k$; the bound lies
  strictly between $e^{ck^2}$ and the claimed $e^{e^{ck}}$; its standing is
  that of part (b) plus Lemmas C and C′.
- **S4 ((293.2)).** With Hughes's Theorem 1 at its standing,
  $h(N)\le(2\log2+o(1))n/\log n+O(\log n)$ for the $N$ of Lemma C′ as
  $b\to\infty$, so $b\in D_k$ for every
  $k\ge(4\log2+o(1))\log b/(\log\log b)^2$, whence
  $\log v(k)\ge(1/(4\log2)-o(1))\,k(\log k)^2$ as $k\to\infty$; weaker than
  $e^{ck^2}$.
- **S5 ((293.3), conditional on the claimed chain).** If Proposition 4.1
  holds as reconstructed, then for all large $k$ every integer
  $2\le b\le\exp\exp\sqrt{k/(2c_0)}$ lies in $D_k$, i.e. the note's Theorem
  1.3; the route is $x=b$ with $p_*$ an odd prime factor of $b$, or $b$ a
  power of two above $2^E$, then Lemma C and the nesting; Lemma C′ is not
  needed. The chain stays claimed.
- **S6 (obstruction, exponent one).** $v(k)\ge e^{e^{ck}}$ needs $b\in D_k$
  whenever $k\gg\log\log b$, i.e. decompositions of $1$ containing $1/b$
  with $O(\log\log b)$ terms, which through S1 needs a practical $N\ge b$
  with $b\nmid N$ and $h(N)\ll\log\log b$.
- **S7 (obstruction, factorial route).** For the $N$ of Lemma C′,
  $2h(N)+1\ge2c(\log n)^2\approx2c(\log\log b)^2$ by Remark 6, so S1 with
  that $N$ places $b$ in $D_k$ only when $\log\log b\le\sqrt{k/(2c)}$; the
  route is capped at $v(k)\ge\exp\exp(C\sqrt k)$.
- **S8 (obstruction, extension chains).** Certificates built from Lemma 3.1
  chains are capped at the same shape by Lemma D, which is why Theorem 1.3
  has the form it has.
- **S9 (converse flow).** $b<v(k)$ gives $N(b-1,b)\le k-1$ (van
  Doorn–Tang, Section 3); applied to S2 this gives
  $N(b-1,b)\le5(\log b)^{\varepsilon}$ for large $b$, which (304.1) already
  gives; nothing new flows back.
- **S10 (falsification paragraph).** (i) When $b\mid n!$ the divisor $n!/b$
  can occur in a representation of $(b-1)n!/b$, so the naive transfer with
  $N=n!$ can repeat $1/b$; (ii) the three requirements of Lemma C′ hold;
  (iii) the nesting is applied only from $k\ge2$ and the constructed
  decomposition has at least two terms; (iv) small $b$ are handled by the
  published growth of $v(k)$.
- **S11 (closing sentence).** A computation cannot test (293.1); the known
  finite values $v(3),\dots,v(8)$ on the problem page are consistent with
  every bound of the section.
- **T (target paragraph).** The Problem 293 page records the status open
  with $e^{ck^2}\le v(k)\le c_0^{(1/5+o(1))2^k}$, the monograph's guess of
  doubly exponential growth, and the note's Theorem 1.3 as not adopted.

## Checklist

- **Quantifiers and scope.** Pass. S2 carries the premise's order
  ($\forall\varepsilon\,\exists n_0\,\forall n\ge n_0$) into
  $\forall\varepsilon\,\exists k_0\,\forall k\ge k_0$ with an ineffective
  threshold, stated as such; the eventual clauses of S4, S5 and S9 are
  explicit; the "so" of S3 needs $\varepsilon<1/A$, not $\varepsilon=1/A$
  (F4). No almost-all statement is upgraded.
- **Circularity.** Pass. The small-$b$ range in S2 and S5 is covered by the
  refereed $v(k)\to\infty$, never by the conclusion; nothing else about
  $v(k)$ is assumed.
- **Model and convention changes.** Pass. The $h$ convention ($m\le N$,
  fresh set) is the same in the accepted statement, Lemma 3.1, Lemma 5.1,
  Lemma C and Lemma C′; the exact-$k$-term definition of $D_k$ is bridged
  by Lemma 2.1 for $k\ge2$, and every constructed decomposition has at
  least three terms; the note's $v(k)$ is the page's $v(k)$.
- **Finite and statistical overreach.** Pass. No finite evidence is used as
  proof; the consistency claim of S11 is vacuous for asymptotic bounds
  (F5).
- **Uniformity.** Pass with two qualifications. The constant $5$ of S2 is
  absolute; the $o(1)$ of S4 is the one of Theorem 1 plus the inversion
  $n/\log n=(1+o(1))\log b/(\log\log b)^2$, re-derived; the "$\approx$" of
  S7 hides a $(1+o(1))$ factor that the cap sentence should carry (F1);
  the cap of S8 is uniform only over chains from a bounded seed, which is
  the reading of Lemma D's closing paragraph but not of its displayed
  statement (F2, F3).
- **Extremal conclusions.** Not applicable beyond the two caps, which are
  budget statements in the route's own unit (the certified term count
  $2h(N)+1$) and were checked in that unit.
- **Consequences and composition.** Pass with F1. Each "hence" was attacked
  separately: S1's placement in $D_k$, S3's exponent switch, S7's cap, S8's
  cap, S9's return through (304.1). In S7 the cited statement of Remark 6
  covers only $N=n!$; the second case of Lemma C′ needs the argument of
  Remark 6, not its statement, and that argument closes it (Weakest steps).
- **Computation.** Not applicable: the section claims no computation. A
  finite sanity check of the Lemma C′ construction run by the reviewer is
  reported under Weakest steps as a check, not as evidence.
- **Reproduction.** Not applicable: no rerun command or coverage line is
  stated. The sentence "were each checked" of S10 was re-checked here.
- **Source and verdict fidelity.** Pass. Lemma 2.1 (range $k\ge2$), Theorem
  1.1 (all positive integers $k$) and the Section 3 converse were read on
  paper pp. 2 and 7; Lemma 5.1, the proof of Theorem 1.3 and the statement
  of Proposition 4.1 on note pp. 5–6; each matches its use. The standing
  labels (refereed; claimed; site-accepted, not refereed) match the library
  cards. T's description of the Current assessment is outside the read set;
  the visible Status paragraph agrees on the two bounds. S11's "on the
  problem page" was tested only by a string count (F5).

## Weakest steps

**W1: the interface of Lemma C′ inside S2.** Re-derived. Let $n$ be the
least integer with $n!\ge b$, so $(n-1)!<b\le n!$. First case, $b\nmid n!$:
$N=n!$, practical with the ratio-two property by Lemma A, $N\ge b$, and
$h(N)=h(n!)$. Second case, $b\mid n!$: let $p$ be the least prime not
dividing $n$. For $n\ge3$, $p\le n-1$, since $n=3$ gives $p=2$ and for
$n\ge4$ the product of all primes up to $n-1$ exceeds $n$, so they cannot
all divide $n$. Put $j=\lceil\log n/\log p\rceil$, so $p^{j}\ge n$ and
$N=p^{j}(n-1)!\ge n!\ge b$. For $0\le i<j$ the number $p^{i}(n-1)!$ has, for
each residue $c\in\{1,\dots,p-1\}$, the single divisor $c$ (as
$c\le p-1\le n-2$, $c$ divides $(n-1)!$), not divisible by $p$, with total
$c\le p^{i}(n-1)!$, and the residue $0$ is the empty sum; Lemma 3.1 with
$A=p$ and $L=1$ therefore carries practicality from $(n-1)!$ (Lemma A) to
$N$ with $h(N)\le h((n-1)!)+j$, and $j\le\lceil\log_2n\rceil$ since
$p\ge2$. If $b\mid N$ then, with $b\mid n!$,
$b\mid\gcd(n!,p^{j}(n-1)!)=(n-1)!\gcd(n,p^{j})=(n-1)!<b$, impossible. The
bound $h(N)\le\max(h(n!),h((n-1)!)+\lceil\log_2n\rceil)$ follows. The
requirement "$b$ large" is needed: at $b=2$ one has $n=2$, no prime
$p\le n-1$, and the construction gives $N=3$, not practical. A finite
sanity check for every $3\le b\le5040$ (ten distinct $N$, with $h$
computed exactly by a knapsack over the divisors) found $N$ practical,
$N\ge b$, $b\nmid N$, the Lemma C representation of $(b-1)/b$ free of the
denominator $b$ with distinct denominators above $1$, the completed sum
equal to $1$ with at most $2h(N)+1$ terms, and the cost bound holding in
each second-case instance; for example $b=8$ gives $N=54$, $h(54)=4$ and
$1=1/2+1/3+1/8+1/27+1/216$.

**W2: the arithmetic of S2 and S3.** Re-derived. For $b>7!$ the least $n$
with $n!\ge b$ satisfies $n<\log b$: the worst case is $b=(n-1)!+1$, and
$\log(n-1)!\ge(n-1)(\log(n-1)-1)>n$ for every $n\ge10$ (the page's
threshold $n\ge14$ is weaker and also true). For
$n\ge n_0(\varepsilon)+1$ the premise gives $h(n!)<n^{\varepsilon}$ and
$h((n-1)!)<(n-1)^{\varepsilon}$, so
$h(N)\le n^{\varepsilon}+\log_2n+1\le2n^{\varepsilon}$ once
$\log_2n+1\le n^{\varepsilon}$, whence $2h(N)+1\le4n^{\varepsilon}+1$. When
$\log b\ge1$ this is below $5(\log b)^{\varepsilon}$, since
$4n^{\varepsilon}+1<4(\log b)^{\varepsilon}+1\le5(\log b)^{\varepsilon}$; so
every integer $k\ge5(\log b)^{\varepsilon}$ satisfies $k\ge2h(N)+1$ and S1
places $b$ in $D_k$. Fix $k$. Every $b$ with
$b_0(\varepsilon)\le b\le\exp((k/5)^{1/\varepsilon})$ has
$5(\log b)^{\varepsilon}\le k$, hence lies in $D_k$; every
$2\le b<b_0(\varepsilon)$ lies in $D_k$ once $v(k)>b_0(\varepsilon)$, which
Theorem 1.1 gives for $k\ge k_1(\varepsilon)$. So $v(k)$, the least integer
above $1$ outside $D_k$, exceeds $\exp((k/5)^{1/\varepsilon})$. For S3,
take $\varepsilon=1/(2A)$: $(k/5)^{2A}\ge k^{A}$ exactly when $k\ge25$, so
$v(k)\ge\exp(k^{A})$ for $k\ge\max(k_0(1/(2A)),25)$; the choice
$\varepsilon=1/A$ would give only $\exp(k^{A}/5^{A})$.

**W3: the two caps, S7 and S8.** For S7 the cited Remark 6 states
$h(n!)\ge c(\log n)^2$ for large $n$, which covers the first case of Lemma
C′ only. The second case follows from the argument of Remark 6: every
$1\le m\le N$ is a sum of at most $h(N)$ of the $\tau(N)$ divisors, distinct
$m$ need distinct subsets, and $\sum_{i\le h}\binom{\tau}{i}\le(\tau+1)^{h}$,
so $h(N)\ge\log N/\log(\tau(N)+1)$. With $N=p^{j}(n-1)!$ and
$v=v_p((n-1)!)$, $\tau(N)=\tau((n-1)!)\,(v+j+1)/(v+1)\le(j+1)\tau((n-1)!)$, so
$\log(\tau(N)+1)\le\log\tau((n-1)!)+\log(\lceil\log_2n\rceil+1)+1\ll n/\log n$
by the divisor count of Remark 6 at $n-1$, while
$\log N\ge\log(n-1)!\gg n\log n$; hence $h(N)\gg(\log n)^2$ in both cases.
Since $\log b=n\log n-n+O(\log n)$, one has
$\log\log b=\log n+\log\log n+O(1/\log n)$ and
$(\log n)^2=(1+o(1))(\log\log b)^2$, so the cap reads
$\log\log b\le(1+o(1))\sqrt{k/(2c)}$; the section's "$\approx$" and its
unqualified "$\le\sqrt{k/(2c)}$" hide this factor (F1). For S8, Lemma D is
consumed as an input; its interface was tested with the chain $n_0=2^{a}$,
$A_0=3$, $L_0=1$ (residues $0,1,2$ modulo $3$ as the empty sum, the divisor
$1$ and the divisor $2$, none divisible by $3$, total at most $n_0$), which
satisfies the hypotheses of Lemma 3.1 with $n_1=3\cdot2^{a}$. Here
$\sum_jL_j=1$ while $(\log\log n_1)^2/(2\log2)$ equals $3.1$, $13.1$, $30.9$
and $89.6$ at $a=10,100,1000,10^5$, so the displayed second inequality of
Lemma D is not uniform over all chains; it holds for chains from a bounded
seed (the subtracted term $(\log\log n_0)^2$ is then $O(1)$), which is the
reading of Lemma D's closing paragraph ("from a fixed seed") and the only
reading S8 needs, since the claimed chain starts from
$n_0\le2^{E}(2Q(k_0))^{k_0}$, bounded independently of $x$ and $p_*$ (F2,
F3).

## Strongest attack

- **S1.** Attempted to make the adjoined $1/b$ collide with a Lemma C
  denominator or to break the nesting's base. A collision needs $b=N/d_i$
  (a divisor of $N$, excluded by $b\nmid N$) or $b=bN/e_j>N\ge b$
  (impossible); the base needs $j\ge2$, and $j\ge3$ since $D_2=\emptyset$
  and $1/b<1$. Failed.
- **S2.** Attempted the case $b\mid n!$ (the naive transfer with $N=n!$ can
  indeed repeat $1/b$: with $r=0$ a representation of $q=(b-1)n!/b$ may use
  the divisor $n!/b$), then the case $b\mid p^{j}(n-1)!$ (W1's gcd shows it
  cannot occur), then a convention mismatch of $h$ (none), then the small
  $b$ below the ineffective threshold (covered by Theorem 1.1), then the
  arithmetic constants (W2). Failed.
- **S3.** Attempted the exponent switch with $\varepsilon=1/A$, which does
  fail by the factor $5^{A}$ in the exponent; the sentence survives with
  $\varepsilon<1/A$ (W2). Failed as a refutation; recorded as F4.
- **S4.** Attempted the inversion from $n$ to $b$: at $b=n!$ the ratio
  $(n/\log n)/(\log b/(\log\log b)^2)$ is $2.2$, $2.1$, $1.8$, $1.7$ at
  $n=20,100,1000,10^4$, converging to $1$ only like
  $1+O(\log\log n/\log n)$; the statement is asymptotic and its constant
  $4\log2$ is the limit, so the slow convergence refutes nothing. Failed.
- **S5.** Attempted $b$ a power of two at most $2^{E}$ (then $b\nmid n$ is
  not arranged): excluded by $b>\max(2^{E},x_0)$, which $v(k)\to\infty$
  supplies; then $n<b$ (excluded by $x\le n$); then a term count above $k$
  (excluded by $2h(n)+1\le2c_0(\log\log b)^2-1<k$ on the stated range).
  Failed; the deduction is exactly the note's proof on p. 6.
- **S6.** Attempted to read "needs" as a necessary condition for the
  target rather than for the route: the sentence says "through this
  route", and both directions of the equivalence between
  $v(k)\ge e^{e^{ck}}$ and $O(\log\log b)$-term decompositions containing
  $1/b$ hold by the definition of $v$ and the nesting. Failed.
- **S7.** Attempted the non-factorial $N$ of Lemma C′, where the cited
  statement of Remark 6 does not apply; the cap survives by W3. Recorded
  as F1.
- **S8.** Attempted an unbounded seed, where Lemma D's displayed
  inequality fails (W3); the cap survives for chains from a bounded seed,
  which is the case the sentence concerns. Recorded as F2 and F3.
- **S9.** Attempted to find something new in the return: with
  $k=\lfloor5(\log b)^{\varepsilon}\rfloor+1\ge k_0(\varepsilon)$ one gets
  $b<v(k)$ and $N(b-1,b)\le\lfloor5(\log b)^{\varepsilon}\rfloor$, while
  (304.1) gives $N(b)\le2(\log b)^{\varepsilon}$; nothing new. Failed.
- **S10.** Each of the four assertions was re-derived (W1, W2). Failed.
- **S11.** The consistency claim cannot fail: every bound of the section
  holds only beyond an unspecified threshold. The listing claim is outside
  the read set. Not refutable here; recorded as F5.
- **T.** Descriptive; the visible Status paragraph and the lead page agree
  with it; the Current assessment itself is excluded. Not refutable here.

## Premises

- **Lemma C** (connections page, shared; author-recorded, proof owned by
  another reviewer). Interface used: $n\ge b\ge2$ integers, $n$ practical,
  $1\le a<b$; at most $2h(n)$ distinct unit fractions with denominators
  above $1$, none equal to $b$ when $b\nmid n$. Confirmed against Lemma 5.1
  on note p. 6 (page image); the proof was also re-read and is elementary.
- **Lemma C′** (connections page, shared; author-recorded). Interface used:
  for large $b$, $N$ practical, $N\ge b$, $b\nmid N$,
  $h(N)\le\max(h(n!),h((n-1)!)+\lceil\log_2n\rceil)$. Re-derived in W1.
- **Lemma A** (connections page, shared). Used only through Lemma C′: $n!$
  is practical for every $n\ge1$.
- **Lemma D** (connections page, shared; author-recorded). Interface used
  by S8: chains certified by Lemma 3.1 from a bounded seed cost at least
  $(1/(2\log2)-o(1))(\log\log n_J)^2$. Its displayed uniformity clause over
  all chains fails for unbounded seeds (W3); the bounded-seed reading is
  what S8 consumes.
- **Lemma 3.1 reconstruction** (labeled claimed because the note is a
  claim; the proof on the page is complete and elementary). Used with
  $A=p$, $L=1$ in Lemma C′ and as the certificate class of Lemma D.
- **Proposition 4.1 reconstruction** (claimed; reviewed as of
  2026-09-28T05:03:27Z with corrections since). Used in S5 within its
  hypotheses: $x=b\ge x_0$ real, $p_*$ any odd prime; gives $b\le n<b^2$,
  $2^{E}\parallel n$, $p_*\nmid n$, $h(n)\le c_0(\log\log b)^2-1$.
- **Theorem 1 reconstruction** (Hughes, proved modulo the second-hand
  Berend–Harmse import). Used in S4 at $n$ and $n-1$.
- **Remark 6 reconstruction** (Hughes, elementary). Statement covers
  $h(n!)$ only; S7 needs its argument for $N=p^{j}(n-1)!$ (F1).
- **Accepted part (b).** Interface from the accepted-proof target page:
  for every $\varepsilon>0$ there is $n_0$ with $h(n!)<n^{\varepsilon}$ for
  all $n\ge n_0$, $h$ over $1\le m\le n!$ with a fresh set per $m$.
  Standing: documented acceptance of the formal statement by the bounty
  site, not refereed, a single kernel, not built in this repository;
  thresholds not extracted.
- **van Doorn–Tang (2025), held PDF (arXiv:2512.22083v2), refereed.**
  Lemma 2.1 ($D_k\subseteq D_{k+1}$ for all $k\ge2$, p. 2), Theorem 1.1
  ($v(k)\ge e^{ck^2}$ for all positive integers $k$, p. 2) and the Section
  3 converse ($b<v(k)$ gives $N(b-1,b)\le k-1$, p. 7): read clause by
  clause on the page images; proofs not re-verified (the Lemma 2.1 proof
  was read for structure).
- **van Doorn (2026), held PDF, claimed.** Lemma 5.1 with proof, the proof
  of Theorem 1.3 (p. 6) and the statement of Proposition 4.1 (p. 5): read
  on the page image (p. 6) and in the text layer (p. 5).
- **(304.1)** (connections page, Problem 304 section; author-recorded,
  reviewed separately). Interface used by S9: $N(b)\le2(\log b)^{\varepsilon}$
  for $b\ge b_0(\varepsilon)$ under the same premise.

## Findings

- **F1 (suggested).** Location: "The factorial route is capped at
  $\exp\exp(C\sqrt k)$: Remark 6 gives
  $2h(N)+1\ge2c(\log n)^2\approx2c(\log\log b)^2$ for the $N$ of Lemma C′,
  so it can only place $b$ in $D_k$ when $\log\log b\le\sqrt{k/(2c)}$."
  Defect: Remark 6 is stated for $h(n!)$;
  in the second case of Lemma C′, $N=p^{j}(n-1)!$ is not a factorial, so
  the citation applies the statement outside its hypotheses, and the
  "$\approx$" drops a $(1+o(1))$ factor from the cap. Witness: any $b$
  with $b\mid n!$, e.g. $b=8$, $N=54$. The inequality itself is true by the
  argument of W3, so the cap stands. Proposed replacement: "the counting
  argument of Remark 6, applied to $N$ (for $N=p^{j}(n-1)!$ one has
  $\tau(N)\le(j+1)\tau((n-1)!)$ and $\log N\ge\log(n-1)!$), gives
  $2h(N)+1\ge2c(\log n)^2=(2c+o(1))(\log\log b)^2$ for the $N$ of Lemma C′,
  so it can only place $b$ in $D_k$ when
  $\log\log b\le(1+o(1))\sqrt{k/(2c)}$."
- **F2 (suggested).** Location: "The extension chains are capped at the
  same shape by Lemma D, which is why the claimed Theorem 1.3 has the form
  it has." Defect: the cap holds for certificates whose seed is bounded
  (Lemma D's closing paragraph says "from a fixed seed"); the sentence
  drops the qualification, and Lemma D's displayed statement claims
  uniformity over all chains, which fails for unbounded seeds (F3).
  Witness: W3's chain $n_0=2^{a}$, $A_0=3$, $L_0=1$. Proposed replacement:
  "Certificates built from Lemma 3.1 extensions of a bounded seed are
  capped at the same shape by Lemma D, which is why the claimed Theorem 1.3
  has the form it has."
- **F3 (note, outside the section; for the reviewer of the shared
  lemmas).** Location: Lemma D, "where the $o(1)$ tends to $0$ as
  $n_J\to\infty$ uniformly over all such chains" and the following
  "Hence" sentence. Defect: for the chain $n_0=2^{a}$, $A_0=3$, $L_0=1$
  (hypotheses of Lemma 3.1 satisfied), $\sum_jL_j=1$ while
  $(\log\log n_1)^2/(2\log2)\to\infty$ with $a$; the proof's step
  "$j(\eta)-1$, if it exists" compensates the subtracted
  $(\log\ell_{j(\eta)})^2$ only when the seed lies below $n(\eta)$.
  Proposed replacement: state the bound as
  $\sum_jL_j\ge((\log\log n_J)^2-(\log\log n_0)^2)/(2\log2)-o((\log\log n_J)^2)$,
  or restrict the uniformity clause to chains with $n_0\le n_*$ for a fixed
  $n_*$ (the closing paragraph's "fixed seed").
- **F4 (note).** Location: "so $v(k)\ge\exp(k^{A})$ for every fixed $A>0$
  and all large $k$." The step needs $\varepsilon<1/A$; with
  $\varepsilon=1/A$ the displayed bound gives only $\exp(k^{A}/5^{A})$.
  Proposed replacement: "so (taking $\varepsilon=1/(2A)$ and $k\ge25$)
  $v(k)\ge\exp(k^{A})$ for every fixed $A>0$ and all large $k$."
- **F5 (note).** Location: "the known finite values $v(3),\dots,v(8)$ on
  the problem page are consistent with every bound here." The consistency
  claim is vacuous: every bound of the section holds only for
  $k\ge k_0$ with $k_0$ unspecified or ineffective, so no finite value can
  contradict it. The listing claim could not be checked inside the read set
  (the page's statement block gives $v(1)=v(2)=2$ and $v(3)=4$ only; a
  string count finds "v(8)" elsewhere on the page and no "v(4)"). Proposed
  replacement: "no finite value of $v$ bears on the bounds here, whose
  thresholds are unspecified."

## Verdict

- S1 (transfer observation): **refutation-failed**.
- S2 ((293.1)): **refutation-failed**, as a conditional statement whose
  premise is the site-accepted part (b) at its recorded standing; the
  conclusion is ineffective in $k$.
- S3 (corollary and calibration): **refutation-failed**, with the
  one-line justification of F4; the standing sentence could also name the
  refereed inputs (Lemma 2.1 and Theorem 1.1 of van Doorn–Tang), consumed
  at their published standing.
- S4 ((293.2)): **refutation-failed**, at the standing of Hughes's Theorem
  1 (second-hand Berend–Harmse import).
- S5 ((293.3)): **refutation-failed** as a conditional deduction from the
  claimed Proposition 4.1; the chain stays claimed and this review does not
  examine it.
- S6 (exponent-one obstruction): **refutation-failed**.
- S7 (factorial-route cap): **refutation-failed**; the cap holds, and its
  cited justification needs the widening of F1.
- S8 (extension-chain cap): **refutation-failed** for certificates from a
  bounded seed, the case the sentence concerns; the qualification of F2
  should be written.
- S9 (converse flow): **refutation-failed**.
- S10 (falsification paragraph): **refutation-failed**.
- S11 (closing sentence): not refutable within the read set; the
  consistency claim is vacuous (F5).
- T (target paragraph): descriptive; consistent with the visible Status
  paragraph; the Current assessment it summarizes is outside the read set.

**Limitations.** The premises were consumed at their recorded standing and
not re-verified: the proofs of Lemma C, Lemma D and Lemma A belong to the
shared-lemma review; the reconstruction pages are established at the
standing of the review as of 2026-09-28T05:03:27Z; the accepted part (b) was not
built or replayed; Proposition 4.1 and the note's chain are claimed. The Hughes
PDF was not opened. The finite sanity check of Lemma C′ covers $3\le b\le5040$
and bears only on the construction, never on the asymptotic statements.
Required corrections: none. This focused review assigns no tier and changes
no status.
