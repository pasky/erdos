---
name: research/erdos_416/evidence/verify/connections_problem_821_large_fibers_versus_repeated_represe_review
title: "Independent review of the connections section: Problem 821: large fibers versus repeated representations"
desc: |
  Refutation-failed for the eight checked statements of the section; the
  outcome sentence is a research judgment, not a claim. No required
  corrections; one suggested precision (a missing "p does not divide m/p"
  in the collapse sentence) and four notes.
created: 2026-09-28T18:34:56Z
updated: 2026-09-28T18:34:56Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, given only the
commissioning assignment. The reviewer took no part in writing the
connections page or the reconstruction pages, and is distinct from their
author and from the grader who will read this report. Charge: refutation of
the author-recorded mathematics of one section.

**Subject.** Page `wiki/research/erdos_416/connections.md` as it stood on
2026-09-28T13:50:48Z, section
"## Problem 821: large fibers versus repeated representations", lines
454–492 (the H2 heading is line 454; the next H2, the Problem 694 section,
is line 493). The section names no lead page and records no next
investigation, so there is no lead page in this subject.

**Read, and at what depth.**

- The section in full, and the page's shared sections as inputs (lines
  1–90: purpose and standing, notation, the imported inputs (F), (F8), (W)
  and (KK), and the search). Only (KK) is used by the section; the
  interfaces of the others were noted and are not consumed here.
- The premise page
  [[research/erdos_416/kruer_kohlmeyer_theorem_1_1_reconstruction|the Theorem 1.1 reconstruction page]]
  in full, for the definition of a retained family, of the pair map and of
  the quantities in estimates (3)–(5). The Lemma 2.1, Lemma 5.1 and
  Zeraoulia reconstruction pages were not needed and were not read.
- The statement block of
  [[problems/arithmetic_functions/E0821/_index|Problem 821]] (lines 12–43: the
  statement, the status line, the source line and the reference list), and
  the page's frontmatter `status` field.
- The library cards of Baker–Harman (1998), Lichtman (2022), Ford (1998)
  and Erdős (1935) as card text (provenance paragraph and result list), the
  Kruer–Kohlmeyer card and its Proposition 4.1 result page (statement and
  proof-pointer paragraphs), and the held sources at the cited results: the
  conversions at Ford §1.2 (Theorem 2) and §1.3 (Theorem 8), Baker–Harman
  Theorem 1 and Corollaries 1–2, Lichtman Corollary 1.3, and Erdős Part 3
  (Lemmas 2–4 and the main theorem), each also checked against the PDF's
  extracted text at the same result. No proof in these sources was read
  beyond Erdős's one-paragraph deduction of his Part 3 theorem.
- The commissioned guidance pages: the verification guide's whole-claim
  report, audit checklist and grading sections, the approach-vetting page,
  the source-fidelity section of the evidence page, and the math-authoring
  page.

**Not read.** The folder's `_index.md`; everything under `evidence/`,
including the existing reviews and the grade; the Current assessment,
Progress, Known Results and Linked library material sections of the problem
page; the other sections of the connections page beyond their headings;
the accepted Lean file; anything outside the repository. No web search was
made.

**Exposures.** None beyond two disclosed borderline items: the heading
lines of the problem page (section titles only, no content) were listed to
locate its statement block, and its one-line frontmatter `status: open`
field was read to check the section's "Status open". Nothing of the
excluded assessment or standing text was read.

## Restatement

Throughout, $g(n)=\#\{m\ge1:\varphi(m)=n\}$ as on the problem page, $d(t)$
is the number of divisors of $t$, $\omega(t)$ its number of distinct prime
factors, and a *retained family* is the object of the premise page: a
finite set $P_y$ of pairs $(b,p)$, $b$ a numerical core (a totient value
$\varphi(m_0)$ with one record $m_0$ selected per core) and $p$ a top
prime, with value map $f_y(b,p)=b(p-1)\in T(y)$, and with
$A_y=|P_y|$, $E_y=A_y-|f_y(P_y)|$ and $M_y=V(y)-|f_y(P_y)|$.

- **S1 (target and literature).** Problem 821 asks whether, for every
  $\epsilon>0$, $g(n)>n^{1-\epsilon}$ for infinitely many $n$; its catalog
  status is open. The section reads the page's references as a chain:
  Erdős (1935) gives infinitely many $m$ with $g(m)>m^{c}$ for some fixed
  $c>0$; Baker–Harman (1998), Corollary 1, gives infinitely many $m$ with
  more than $m^{1-\delta}$ preimages for a fixed $\delta$ (the source's
  $\beta=0.2961$); Lichtman (2022), Corollary 1.3, gives infinitely many
  $m$ with at least $m^{0.7156}$ preimages; all three come from counts of
  primes $p$ with $p-a$ free of large prime factors; the open gap is the
  exponent $1-\epsilon$ for every $\epsilon$. The section also says the
  page is not compiled.
- **S2 (content of (4)).** Estimate (4) of the premise, $E_y=o(V(y))$,
  bounds $\sum_{t\in f_y(P_y)}\bigl(|f_y^{-1}(t)|-1\bigr)$, the sum over
  the fibers of the pair map.
- **S3 (fiber bound).** For every set of pairs $(b,p)$ with $b$ a positive
  integer and $p$ prime, under the value map $(b,p)\mapsto b(p-1)$, the
  fiber over an integer $t\ge1$ consists of pairs with $(p-1)\mid t$ and
  has at most $\#\{p\text{ prime}:(p-1)\mid t\}\le d(t)$ elements; and
  $d(t)=t^{o(1)}$, meaning that for every $\eta>0$ there is $t_0(\eta)$
  with $d(t)\le t^{\eta}$ for all $t\ge t_0(\eta)$.
- **S4 (the literature bound).** $g(t)>t^{0.7}$ for infinitely many $t$.
- **S5 (collapse).** If $m\ne m'$ are preimages of $t$ with the same
  largest prime factor $p$, with $p\nmid m/p$ and $p\nmid m'/p$, and
  $\varphi(m/p)=\varphi(m'/p)$, then both correspond to the single pair
  $(\varphi(m/p),p)$ of the fiber over $t$; hence the map
  $m\mapsto(\varphi(m/p),p)$ sends the preimages of $t$ whose largest prime
  factor divides them exactly into the pair fiber over $t$, a set of at
  most $d(t)$ elements, so the $\varphi$-fiber of size $g(t)$ collapses to
  a divisor-bounded set of pairs. (The section's sentence omits the
  hypothesis $p\nmid m/p$; see F2.)
- **S6 (the obstruction).** Estimate (4) concerns a sum whose term at $t$
  is at most $d(t)-1=t^{o(1)}$; it neither yields a lower bound for $g$ nor
  is contradicted by one. Estimate (3),
  $M_y\le\varepsilon V(y)+V(y^{99/100})$ eventually, counts the values not
  represented by any retained pair and says nothing about how often a
  value is represented. The family's estimates keep fibers small on
  average, whereas Problem 821 asks for lower bounds on extreme fibers.
  Therefore the reconstructed mechanism gives nothing toward Problem 821.
- **S7 (Ford's Theorem 2).** For every $\varepsilon>0$, if $A(d)=k$ then
  $V_k(x)\gg_\varepsilon d^{-1-\varepsilon}V(x)$ for $x\ge x_0(d)$, so
  every multiplicity that occurs is attained by a positive proportion of
  totients; this is consistent with (4) because the multiplicity of a
  value under $\varphi$ is not its multiplicity under $f_y$.
- **S8 (the route on the problem page).** The known lower bounds for
  extreme fibers come from many primes $p$ with $p-1$ free of large prime
  factors, by the pigeonhole argument of Erdős and Pomerance over
  squarefree products of such primes, which produces many preimages of one
  value and does not count the set of values.
- **S9 (outcome).** "Next investigation: none through this mechanism" and
  "Outcome: fails" are research judgments; they assert no mathematics
  beyond S3–S8 and are not claims.

## Checklist

- **Quantifiers and scope.** Pass, with note F1. "For every family" in S3
  is read, from its context, as every set of pairs under the pair map; the
  abstract retained family of the premise (any finite set with a map into
  $T(y)$) would not satisfy the bound, and the sentence should say which it
  means. "Infinitely often" for the literature bounds and "for every
  $\epsilon$" for the target are kept distinct; "$t^{o(1)}$ for every
  value" is the standard eventual reading of the divisor bound.
- **Circularity.** Pass. The section derives nothing from the truth of
  (3)–(5); it uses only their shape, and its own bound S3 is elementary.
- **Model and convention changes.** Pass, with the precision F2. $g(n)$ is
  the problem page's count, with $m$ unrestricted; $T(y)$, $V(y)$, $P_y$,
  $f_y$, $E_y$ and $M_y$ are the premise page's; "top prime" and "core" are
  the write-up's, in which the top prime does not divide the core. The
  section's collapse sentence uses "top prime" for an arbitrary preimage
  without stating that hypothesis.
- **Finite and statistical overreach.** Pass. No finite computation is
  cited as evidence, and "consistent with" in S7 is not presented as a
  proof of anything.
- **Uniformity.** Pass. The divisor bound is absolute and independent of
  $y$, $\varepsilon$ and the family; (4)'s $o(V(y))$ depends on
  $\varepsilon$ through the family, and the section draws no uniform
  statement from it.
- **Extremal conclusions.** Inapplicable; none is claimed.
- **Consequences and composition.** Pass, with note F5. The "hence"
  sentence of S6 was attacked separately (see the strongest attack). The
  composition S3 with S4 is the obstruction and needs only the elementary
  bound and one refereed source. Each imported statement is used at its
  recorded standing: the premise only for its definitions, Baker–Harman
  and Ford as refereed statements, Lichtman as a held preprint, Erdős as a
  refereed statement.
- **Computation.** Inapplicable to the section, which cites none. The
  reviewer's own exact enumeration below serves only to supply witnesses;
  every witness quoted is small enough to check by hand.
- **Reproduction.** Inapplicable; the section states no rerun command and
  no coverage claim.
- **Source and verdict fidelity.** Pass, with notes F3 and F4. Ford's
  Theorem 2, Baker–Harman's Corollary 1 (with $\beta=0.2961$ from its
  Theorem 1), Lichtman's Corollary 1.3 and Erdős's Part 3 theorem read as
  the section characterizes them; "Corollary 1 on the card" and
  "Corollary 1.3 on the card" name the right results. The section leaves
  $\delta$ unnamed, and its "the page is not compiled" lies outside this
  review's read set.

## Weakest steps

**W1: the fiber bound (S3).** Let $(b,p)$ and $(b',p')$ lie in the fiber
over $t$, so $b(p-1)=t=b'(p'-1)$. If $p=p'$ then $b=b'$; hence the fiber
injects into $\{p\text{ prime}:(p-1)\mid t\}$ by $(b,p)\mapsto p$, and
$p\mapsto p-1$ injects that set into the divisors of $t$. So the fiber has
at most $d(t)$ elements, for every set of pairs, since restricting the
domain only shrinks fibers. For $d(t)=t^{o(1)}$: fix $\eta>0$ and write
$t=\prod p_i^{a_i}$, so $d(t)/t^{\eta}=\prod_i(a_i+1)p_i^{-\eta a_i}$. A
prime $p_i\ge2^{1/\eta}$ contributes $(a_i+1)2^{-a_i}\le1$; a prime
$p_i<2^{1/\eta}$ contributes at most $\max_{a\ge0}(a+1)2^{-\eta a}$, a
constant depending only on $\eta$, and there are fewer than $2^{1/\eta}$
such primes. Hence $d(t)\le C(\eta)t^{\eta}$, and $d(t)\le t^{2\eta}$ once
$t^{\eta}\ge C(\eta)$. Composition: S3 is the whole content of the
obstruction's first half, and it holds for every value and every family.

**W2: the collapse (S5).** For $m\ge2$ let $p$ be its largest prime factor
and $m_0=m/p$. If $p\nmid m_0$ then $\varphi(m)=\varphi(m_0)(p-1)$, so
$(\varphi(m_0),p)$ lies in the pair fiber over $t=\varphi(m)$, and two
preimages with the same $p$ and $\varphi(m_0)=\varphi(m_0')$ give the same
pair. If $p\mid m_0$ then $\varphi(m)=p\,\varphi(m_0)$, the pair
$(\varphi(m_0),p)$ has value $\varphi(m_0)(p-1)=t(p-1)/p\ne t$, and $m$ is
not a pair of the family at all; but then $p\mid t$ and
$\varphi(m_0)=t/p$, so these preimages give at most $\omega(t)$ distinct
pairs. Hence the map $m\mapsto(\varphi(m/p),p)$ sends the whole fiber
$\varphi^{-1}(t)\setminus\{1\}$ onto at most $d(t)+\omega(t)$ pairs, of
which at most $d(t)$ lie in the pair fiber over $t$: the divisor-bounded
collapse holds under either reading of the sentence. Witness for the
size of the collapse: $t=48$ has $g(48)=11$, preimages
$65,104,105,112,130,140,144,156,168,180,210$. The ten with the largest
prime factor dividing exactly fall onto three pairs: $(4,13)$ from
$65,104,130,156$; $(8,7)$ from $105,112,140,168,210$; $(12,5)$ from
$180$. The eleventh, $144=2^4\cdot3^2$, has largest prime factor $3$ with
$3^2\mid144$ and gives no pair over $48$. The bound of S3 is
$\#\{p:(p-1)\mid48\}=6$ (the primes $2,3,5,7,13,17$) and $d(48)=10$; the
actual pair count is $3$ against $g(48)=11$. Witness for the omitted
hypothesis: $t=6$ has preimages $7,9,14,18$; $m=9$ and $m'=18$ share the
largest prime factor $3$ and have $\varphi(3)=\varphi(6)=2$, so the
section's sentence makes them "one pair" $(2,3)$, whose value is $4\ne6$.

**W3: the logic of the obstruction (S6).** Suppose, toward the section's
"neither implying nor implied by", that some bound on $g$ were related to
(4). For $t\in f_y(P_y)$ the fiber size satisfies
$1\le|f_y^{-1}(t)|\le\min\bigl(\#\{p:(p-1)\mid t\},\,g(t)\bigr)$, the
second bound because, when every top prime of the family exceeds every
prime factor of every selected record, the map $(b,p)\mapsto m_0(b)\,p$ is
injective on the fiber and lands in $\varphi^{-1}(t)$; the premise page
records this as eventually true for each pair's own record, and it holds
across records for large $y$ if, as that page's glosses of (3) and (5)
indicate, the retained values exceed $y^{99/100}$ while the cores satisfy
$\log b=o(\log y)$. The first bound is the section's and is what makes (4)
silent about $g$: no upper bound on the fibers of $f_y$, however strong,
constrains $g(t)$ from below, since $g(t)\ge t^{0.7}$ infinitely often
while the fibers stay below $t^{o(1)}$. Conversely a lower bound on $g$
cannot contradict (4): a value $t=p-1$ with preimages $p$ and $2p$ has
$g(t)\ge2$ and the single pair $(1,p)$, and the family retains one record
per core in any case. The only hypothetical bound that would imply (4) is
the uniform upper bound $g\le1$, which is false for every odd prime $p$ by
the same witness; see F5 for the wording.

## Strongest attack

- **S1.** Each attribution was checked against the held sources. Erdős's
  Part 3 theorem produces an $m\le n$ with more than $m^{C_5}$
  representations, $C_5>0$ fixed, from primes $p\le\mu^{1+\rho}$ with
  $p-1$ composed of primes below $\mu$ (his Lemma 4), so "some positive
  exponent" and "from smooth shifted primes" are exact. Baker–Harman's
  Corollary 1 is stated with the exponent $1-\beta$ and Theorem 1 fixes
  $\beta=0.2961$; the card writes $\delta$ for $\beta$ and the section
  follows the card without naming the value (F3). Lichtman's Corollary 1.3
  reads "at least $m^{0.7156}$ solutions", as the section says, and the
  paper derives it from its Theorem 1.1 by the Erdős–Pomerance method.
  The reference list of the problem page contains exactly these three
  sources and a fourth (Luca–Pollack) that the section does not mention;
  omitting it is not an error. "The page is not compiled" could not be
  checked (F4). The attack found no misstatement.
- **S2.** $E_y=A_y-|f_y(P_y)|$ and $A_y=\sum_{t\in f_y(P_y)}|f_y^{-1}(t)|$,
  so $E_y=\sum_t(|f_y^{-1}(t)|-1)$ exactly; (4) asserts $E_y=o(V(y))$.
  Nothing to refute.
- **S3.** The attack sought a family with a fiber larger than $d(t)$. For sets
  of pairs $(b,p)$ with numerical $b$ this is impossible (W1). The one escape
  would be a family indexed by records rather than by core values, with several
  records sharing a core value $b$: the fiber over $t$ could then reach the
  number of records whose core value is $t/(p-1)$, summed over the primes $p$
  with $(p-1)\mid t$, which is no longer divisor-bounded and could approach
  $g(t)$. The premise page and the Proposition 4.1 result page both state one
  record per core and a family of pairs $(b,p)$, so under the premise the escape
  is closed; the report records this dependence under Premises. The other
  attack, reading "every family" as the abstract retained family (for instance
  the integers $m$ with $\varphi(m)\le y$ under $\varphi$, whose fibers are the
  $\varphi$-fibers), is excluded by the sentence's own reference to the pair
  map; F1 asks for the qualifier to be explicit.
- **S4.** Checked against the two PDFs: for $m\ge2$, more than $m^{0.7039}$
  (Baker–Harman) and at least $m^{0.7156}$ (Lichtman) both exceed
  $m^{0.7}$, and each corollary gives infinitely many $m$. The refereed
  corollary alone supports S4; the preprint is not load-bearing.
- **S5.** The witness $t=6$, $m=9$, $m'=18$ (W2) shows the literal sentence
  names a pair outside the fiber over $t$ when the largest prime factor
  divides the preimage more than once. The conclusion drawn from the
  sentence survives under either reading, so the defect is one of
  precision (F2), not of deduction.
- **S6.** The attack tried to exhibit an implication in either direction
  between (4) and a bound on $g$. The two-sided inequality of W3 is the
  complete relation between the pair fiber and the $\varphi$-fiber, and it
  runs the wrong way for Problem 821. The only bound on $g$ that would
  imply (4) is a false one ($g\le1$), so "nor implied by" is read for the
  lower bounds Problem 821 concerns (F5). The reading of (3) was checked
  against the premise page's definition of $M_y$: it counts unrepresented
  values, and no multiplicity enters. The attack failed.
- **S7.** Ford's Theorem 2 needs a $d$ with $A(d)=k$; the section's "every
  possible multiplicity" carries that hypothesis. For consistency with
  (4), take $k=2$: a positive proportion of totients $t\le y$ have exactly
  two preimages, yet no retained collision is forced, because two
  preimages can give one pair (the witness $p$, $2p$) and because the
  family keeps one record per core. "For the same reason" is the same
  distinction as S5. The attack failed.
- **S8.** Erdős's argument (Lemmas 2–4 and the main theorem of Part 3)
  counts squarefree products of primes with smooth shift and bounds the
  number of distinct $\varphi$-values of such products from above, so one
  value receives many preimages by pigeonhole; nothing in it counts $V$.
  The cards record Baker–Harman's and Lichtman's corollaries as the same
  deduction from their smooth-shifted-prime counts. The description holds.
- **S9.** Not a claim; no attack applies.

## Premises

- **Proposition 4.1 of the write-up**, via
  [[research/erdos_416/kruer_kohlmeyer_theorem_1_1_reconstruction|the Theorem 1.1 reconstruction page]]
  and the statement of
  [[../library/arithmetic_functions/kruer_kohlmeyer_2026_doubling_law_distinct_totient_values/proposition_4_1|its result page]].
  Interface used: a retained family is a finite set of pairs $(b,p)$, $b$ a
  numerical core with one record selected per core, $p$ a top prime,
  value $f_y(b,p)=b(p-1)\in T(y)$; $E_y=A_y-|f_y(P_y)|$;
  $M_y=V(y)-|f_y(P_y)|$; (3) $M_y\le\varepsilon V(y)+V(y^{99/100})$
  eventually; (4) $E_y=o(V(y))$. Standing: the bounty site's kernel
  acceptance of a Lean file that is not held, with no prose proof. The
  section and this review consume only the definitions and the shape of
  (3) and (4), not their truth. S3 depends on the family being indexed by
  core values; the premise page and the result page both state it. Read in
  full (premise page) and at statement depth (result page).
- **Ford (1998), Theorem 2**
  ([[../library/arithmetic_functions/ford_1998_distribution_totients/_index|card]],
  held PDF and conversion, §1.2): for every $\varepsilon>0$, if $A(d)=k$
  then $V_k(x)\gg_\varepsilon d^{-1-\varepsilon}V(x)$ for $x\ge x_0(d)$.
  Refereed. Read at statement depth with its surrounding paragraph, which
  also records the exponent $0.7039$ for Baker–Harman; proof not read.
  Theorem 8 (§1.3) was read in passing to confirm the shared input (F8)
  and is not used by the section.
- **Baker and Harman (1998), Theorem 1 and Corollary 1**
  ([[../library/arithmetic_functions/baker_1998_shifted_primes_without_large_prime_factors/_index|card]],
  held PDF and conversion, pp. 1–2): $\beta=0.2961$; the integers $m$ with
  more than $m^{1-\beta}$ solutions of $\varphi(n)=m$ form an infinite
  sequence with $\log m_{i+1}/\log m_i\to1$. Refereed. Statement depth.
- **Lichtman (2022), Corollary 1.3**
  ([[../library/arithmetic_functions/lichtman_2022_primes_arithmetic_progressions_large_moduli_shifted/_index|card]],
  held PDF and conversion, p. 2): the integers $m$ with at least
  $m^{0.7156}$ solutions of $\varphi(n)=m$ form an infinite sequence with
  $\log m_{i+1}/\log m_i\to1$. Held as an arXiv preprint; not load-bearing
  here since the refereed corollary suffices for S4. Statement depth.
- **Erdős (1935), Part 3**
  ([[../library/arithmetic_functions/erdos_1935_normal_number_prime_factors_related_problems/_index|card]],
  held PDF and conversion): there are $m$ with more than $m^{C_5}$
  representations as $\varphi$ of an integer, $C_5>0$; Lemma 4 supplies
  many primes $p\le\mu^{1+\rho}$ with $p-1$ composed of primes below
  $\mu$. Refereed. Lemmas 2–4 at statement depth and the short deduction
  of the main theorem read.
- **Problem 821, statement block** of
  [[problems/arithmetic_functions/E0821/_index|the problem page]]: $g(n)$ counts
  the $m$ with $\varphi(m)=n$; the question is whether for every
  $\epsilon>0$ infinitely many $n$ have $g(n)>n^{1-\epsilon}$; status
  open; references Baker–Harman, Erdős, Lichtman and Luca–Pollack.
- **Textbook facts.** The divisor bound $d(t)=t^{o(1)}$, re-proved in W1;
  $\varphi(m_0p)=(p-1)\varphi(m_0)$ for a prime $p\nmid m_0$ and
  $\varphi(m_0p)=p\,\varphi(m_0)$ for $p\mid m_0$.
- **Reviewer's enumeration.** All $m$ with $\varphi(m)\le300000$ were
  enumerated exactly (complete, since $m/\varphi(m)<7$ throughout the
  range that matters), and for every totient value $t$ in that range the
  count $\#\{p:(p-1)\mid t\}$ never exceeded $d(t)$, the largest such
  count was $67$, and the largest fiber $g(t)$ was $1023$; the value
  $t=276480=2^{11}\cdot3^3\cdot5$ has $g(t)=769$ against the pair-fiber
  bound $34$ and $d(t)=96$. These figures illustrate S3 and S5 and are not
  evidence for any statement; the hand-checkable witnesses are in W2.

## Findings

- **F1 (note).** Location:
  "$|f_y^{-1}(t)|\le\#\{p:p-1\mid t\}\le d(t)=t^{o(1)}$ for every family".
  Defect: the premise's abstract retained family is any
  finite set with a map into $T(y)$, and the bound holds only for families
  of pairs under the pair map. Witness: the family of integers $m$ with
  $\varphi(m)\le y$ under $\varphi$ has the $\varphi$-fibers themselves.
  Proposed replacement: "for every family of such pairs".
- **F2 (suggested).** Location: "Two preimages $m,m'$ with the same top
  prime $p$ and cores of equal totient, $\varphi(m/p)=\varphi(m'/p)$, are
  one pair". Defect: the sentence needs $p\nmid m/p$ and $p\nmid m'/p$;
  when the largest prime factor divides the preimage more than once the
  value is $p\,\varphi(m/p)$ and the named pair lies outside the fiber
  over $t$. Witness: $t=6$, $m=9$, $m'=18$, both with largest prime factor
  $3$ and $\varphi(3)=\varphi(6)=2$; the pair $(2,3)$ has value $4$. The
  conclusion survives (at most $d(t)+\omega(t)$ pairs for the whole fiber,
  W2). Proposed replacement: "Two preimages $m,m'$ of $t$ with the same
  top prime $p$, $p\nmid m/p$ and $p\nmid m'/p$, and cores of equal
  totient, $\varphi(m/p)=\varphi(m'/p)$, are one pair; a preimage whose
  top prime divides it more than once is no pair at all".
- **F3 (note).** Location: "Baker–Harman 1998 (values with more than
  $m^{1-\delta}$ preimages, Corollary 1 on the card)". Defect: $\delta$ is
  never given a value, although the later "exceeds $t^{0.7}$" rests on
  the exponents. Witness: the source's Theorem 1 fixes $\beta=0.2961$, so
  Corollary 1 gives more than $m^{0.7039}$ preimages. Proposed
  replacement: "more than $m^{1-\delta}$ preimages with $\delta=0.2961$".
- **F4 (note).** Location: "Status open; the page is not compiled". Defect:
  none found; the compilation remark lies outside this review's read set
  (the problem page's assessment and progress sections were excluded) and
  is recorded as unverified here. No replacement proposed.
- **F5 (note).** Location: "neither implying nor implied by a bound on
  $g$". Defect: read literally, a uniform upper bound $g\le1$ would imply
  (4); the bound is false, so the sentence is true for every bound that
  exists, but its intended sense is the lower bounds Problem 821 concerns.
  Witness: $t=p-1$ for an odd prime $p$ has preimages $p$ and $2p$ and the
  single pair $(1,p)$. Proposed replacement: "neither yielding a lower
  bound for $g$ nor contradicted by one".

No required corrections: one suggested precision (F2) and four notes (F1,
F3, F4, F5).

## Verdict

- S1 (target and literature): refutation-failed; the literature chain is
  characterized as the held sources state it, with $\delta$ unnamed (F3)
  and the compilation remark unverified (F4).
- S2 (content of (4)): refutation-failed; an identity of definitions.
- S3 (fiber bound): refutation-failed; re-derived in W1 for every set of
  pairs under the pair map, which the premise's family is.
- S4 (the literature bound): refutation-failed; supported by the refereed
  corollary alone.
- S5 (collapse): refutation-failed under the reading with $p\nmid m/p$,
  the write-up's own convention; the sentence as written needs that
  hypothesis (F2), and its conclusion holds under either reading.
- S6 (the obstruction): refutation-failed; the witness is the two-sided
  inequality of W3, which places the quantity of (4) below $d(t)$ at every
  value regardless of $g$.
- S7 (Ford's Theorem 2 and (4)): refutation-failed; the hypothesis of the
  theorem is carried and the consistency claim has its witness.
- S8 (the route on the problem page): refutation-failed; matches Erdős's
  Part 3 and the cards' descriptions of the two corollaries.
- S9 (outcome): not a claim.

**Limitations.** The review treats the premise page's description of the
retained family, in particular one record per core and pairs indexed by
core values, as established; the accepted Lean file was not read, and if
its family were indexed by records with repeated core values the bound S3
would need re-examination. The sources were read at statement depth only.
The standing of Lichtman's corollary is that of a held preprint and is not
load-bearing. The review examined one section and no other part of the
connections page beyond its shared inputs.

This focused review assigns no tier and changes no status.
