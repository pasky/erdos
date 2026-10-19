---
name: research/erdos_416/evidence/verify/connections_shifted_collisions_problems_1003_and_1004_and_th_review
title: "Independent review of the connections section: Shifted collisions: Problems 1003 and 1004 and the two totient leads"
desc: |
  Refutation review of the section's eight author-recorded statements: all
  eight survive (refutation-failed), with zero required corrections, two
  suggested clarifications and five notes.
created: 2026-09-28T18:33:16Z
updated: 2026-10-07T21:41:29Z
---

***

## Subject and independence

**Role.** The reviewer is an independent reviewer in a fresh context, given
only the commissioned assignment. The reviewer took no part in writing the
section, its page, the folder's reconstruction pages or the two lead pages,
and had read none of them before this assignment.

**Subject.** The source as it stood on 2026-09-28T13:50:48Z (called "the
commit" below), page
[[research/erdos_416/connections|connections]]
(`wiki/research/erdos_416/connections.md`), section "Shifted collisions:
Problems 1003 and 1004 and the two totient leads", lines 592–621: the H2 at
line 592, the Targets paragraph (lines 594–602), the paragraph "Why nothing
transfers" (lines 604–618) and the Outcome paragraph (lines 620–621); the
next H2 is at line 623. Lead pages:
[[research/leads/totient_blocks_native_note/_index|totient_blocks_native_note]]
and [[research/leads/totient_binary_series/_index|totient_binary_series]]
at the same commit.

**Reading and depth.**

- The section in full, re-read against each source below. The page's shared
  sections (Purpose and standing, Notation, Imported inputs, The search;
  lines 1–89) as inputs; only the interface of (KK) is consumed here.
- [[research/erdos_416/kruer_kohlmeyer_theorem_1_1_reconstruction|The Theorem 1.1 reconstruction page]]
  in full, as a premise: the statement of Proposition 4.1 with the
  definitions of $A_y$, $E_y$, $M_y$ and $D_y$, the description of the
  retained family, Step 2 (the lower bound $V(y)\ge c_0y/\log y$) and the
  paragraph "Collisions, estimate (4)".
- The native-note lead in full; the binary-series lead at its heading map,
  its section "Target and standing" and its section "Notation and the tail
  integers" (Lemmas 1 and 2, Propositions 3 and 3′, the carry dynamics);
  its other sections and subpages were not read.
- The statement blocks (H1 to the line before "Current assessment") of
  [[problems/arithmetic_functions/E1003/_index|Problem 1003]],
  [[problems/arithmetic_functions/E1004/_index|Problem 1004]] and
  [[problems/irrationality/E0249/_index|Problem 249]].
- Library: the provenance paragraphs of
  [[../library/arithmetic_functions/kruer_kohlmeyer_2026_doubling_law_distinct_totient_values/_index|the write-up's card]]
  and its result page
  [[../library/arithmetic_functions/kruer_kohlmeyer_2026_doubling_law_distinct_totient_values/proposition_4_1|proposition_4_1]];
  the held five-page write-up at pp. 2–4 (the application of Lemma 2.1,
  §3 "Concrete core records", Proposition 4.1, §§4.1–4.3, the start of §5)
  by text extraction. The provenance paragraphs of
  [[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/_index|the 2013 manuscript's card]]
  and its result pages
  [[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/theorem_3_1|theorem_3_1]]
  and
  [[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/theorem_3_3|theorem_3_3]];
  the held 17-page manuscript at local pp. 5–6 (Section 3: the definition
  of $P(x;k)$, Theorems A, B and C, Theorem 3.1 with its proof sketch,
  Lemma 3.2, Theorem 3.3) and local p. 10 (the proof of Theorem 1.2) by
  layout text extraction, the displayed bounds checked twice.
- Guidance: the verification guide's sections "Grading and claim
  standing", "Audit checklist — the canonical failure modes", "Whole-claim
  report" and "Audit checklist"; the approach-vetting guide in full; the
  evidence guide's "Source fidelity"; the math-authoring guide in full.

**Exposures.** Standing text reached the reviewer incidentally while the
allowed pages were printed whole: the native-note lead's "Current review
state" paragraph and "Living verification" line; the binary-series lead's
"Target and standing" section, which records the standing of its own
arguments and of a theory claim; the "Standing" paragraphs of the
reconstruction page and of the proposition_4_1 result page; the "Living
verification" lines of the theorem_3_1 and theorem_3_3 result pages; and
the "Status" paragraph inside the Problem 249 statement block, which names
a dated search. None of it concerns the section under review, none was
used, and no evidence folder, current assessment, known-results or progress
section, grade or other review was opened. In particular the Problem 1004
page's own record of the shifted-collision bound, which lies outside its
statement block, was not read; the Verdict states the resulting limitation.

## Restatement

**Conventions.** $\varphi$ is Euler's function; $T(y)$ is the set of
totient values in $[1,y]$ and $V(y)=|T(y)|$, as on the reconstruction page.
The retained family of Proposition 4.1 at endpoint $y$ is a finite set
$P_y$ of pairs $(b,p)$: $b=\varphi(m_0)$ is a core, $m_0=a\prod_jp_j$ the
one record selected for $b$, and $p$ a prime exceeding every prime factor
of $m_0$, with value $f_y(b,p)=b(p-1)\in T(y)$. An argument $n$ is *of pair
form* when $n=m_0p$ for such a pair with its selected record, so that
$\varphi(n)=b(p-1)$. The excess is
$E_y=A_y-|f_y(P_y)|=\sum_t(|f_y^{-1}(t)|-1)$ over the values $t$ of the
family, and estimate (4) reads $E_y=o(V(y))$ as real $y\to\infty$, for the
family attached to each fixed $0<\varepsilon<1/2$, with no rate. For real
$x$ and an integer $k\ge1$, $P(x;k)=\#\{n\le x:\varphi(n)=\varphi(n+k)\}$.

- **S1 (targets).** Problem 1003 asks whether $\varphi(n)=\varphi(n+1)$
  has infinitely many solutions $n$; it is open. Problem 1004 asks
  whether, for every fixed $c>0$ and all sufficiently large $x$, some
  $n\le x$ has $\varphi(n+1),\dots,\varphi(n+\lfloor(\log x)^c\rfloor)$
  pairwise distinct; it is open, and the folder's candidate for it is the
  native-note lead, whose record is unreviewed. Problem 249 asks whether
  $\sum_{n\ge1}\varphi(n)/2^n$ is irrational; it is open, and its editable
  proof sketch is the binary-series lead.
- **S2 (two equations).** A collision in the write-up's sense is an
  equality $b(p-1)=b'(p'-1)$ between two distinct pairs of the retained
  family, two representations of one value; a collision in the problems'
  sense is an equality $\varphi(n)=\varphi(n+k)$ of the values at two
  arguments at distance $k$ ($k=1$ for Problem 1003, $1\le k<L$ inside a
  block of length $L$ for Problem 1004).
- **S3.** If $n=m_0p$ and $n+k=m_0'p'$ are both of pair form, the
  equation $\varphi(n)=\varphi(n+k)$ is a pair collision only if the pairs
  $(b,p)$ and $(b',p')$ differ.
- **S4.** Estimate (4) bounds the excess $E_y$ by $o(V(y))$ with no rate
  and no dependence on a shift, summed over the fibers of $f_y$; therefore
  (4) gives no bound on $P(x;k)$.
- **S5.** The 2013 manuscript gives $P(x;k)\ll x/(\log x)^2$ uniformly for
  $k\le\log x$; the section cites this bound as recorded on the Problem
  1004 page.
- **S6.** Conversely, the bounds on $P(x;k)$ do not yield (4), because a
  pair collision joins two arguments $m_0p$ and $m_0'p'$ whose distance is
  not bounded.
- **S7.** Both leads use $n\mapsto\varphi(n)$ as an indexed sequence, the
  binary-series lead through $2$-adic valuations of its tail sums and the
  native-note lead through pairwise distinctness on consecutive arguments,
  while $V$ is a function of the value set alone and carries no information
  about the index; the objects are shared and the mechanism is not.
- **S8 (outcome).** Nothing in the reconstructed mechanism transfers to
  Problems 1003, 1004 or 249; the obstruction is that representation
  collisions and argument collisions are different equations.

## Checklist

- **Quantifiers and scope.** Pass. S4's "no rate" and "no reference to
  $k$" match (4) as imported; S5's range $k\le\log x$ matches the source
  (Premises); S1 paraphrases the three statements with two glosses that
  change no quantifier, "below $x$" (F5) and "for every $c$" in place of
  "for every fixed $c>0$ and all sufficiently large $x$"; S3's qualifier is
  vacuous rather than wrong (F3).
- **Circularity.** Pass. The section assumes no target and uses (4) only
  through what it counts, never through its truth.
- **Model and convention changes.** Pass. The section distinguishes the
  two collision equations instead of substituting one for the other, and
  the one transport it discusses (S3) is stated with its hypothesis, both
  arguments of pair form.
- **Finite and statistical overreach.** Inapplicable: no finite check or
  heuristic average is offered as a proof; the reviewer's witnesses below
  are exact and illustrate existence only.
- **Uniformity.** Pass. (4) is carried as $o(V(y))$ without a rate; the
  bound $\ll x/(\log x)^2$ is carried with the source's range, and the
  reviewer re-derived its uniformity in $k$, including odd $k$ (Strongest
  attack, S5).
- **Extremal conclusions.** Inapplicable: the section asserts no infimum,
  supremum or sharpness.
- **Consequences and composition.** Pass with one suggested clarification.
  The two "so" clauses (S4, S6) and the closing inference (S7, S8) were
  re-derived (Weakest steps); S4's stated reasons omit the primary one
  (F1).
- **Computation.** Inapplicable to the section. The reviewer's totient
  values are exact small integers.
- **Reproduction.** Inapplicable: the section carries no rerun command or
  coverage claim.
- **Source and verdict fidelity.** Pass with notes. The write-up's
  collision description (§4.2), the 2013 manuscript's sentence (local
  p. 10), the three problem statements and the two leads' self-descriptions
  ("candidate" and "unreviewed"; "editable proof sketch") were checked
  against the sources; "records at" is loose (F2), and the attribution to
  the Problem 1004 page could not be checked (Verdict).

## Weakest steps

**W1: from (4) to no bound on $P(x;k)$ (S4).** Fix $1\le k\le x$ and
$n\le x$ with $\varphi(n)=\varphi(n+k)$, and take the endpoint $y=2x$, so
that both values lie in $T(y)$. Either both $n$ and $n+k$ are of pair form
at endpoint $y$, or not. In the first case the pairs differ (S3; with one
selected record per core, equal pairs force $m_0=m_0'$, $p=p'$ and $k=0$),
so both lie in one fiber of $f_y$ of size at least two. The map from such
$n$ to its pair is injective: if $m_0p=m_0'p'$ with $p\ne p'$, then
$p\mid m_0'$ and $p'\mid m_0$, against each top prime exceeding the primes
of its own record. So the number of such $n$ is at most the number of pairs
in nonsingleton fibers, which is at most $2E_y$. In the second case
Proposition 4.1 says nothing: (3) constrains missing values, not arguments,
and a covered value $t=b(p-1)$ has all its preimages other than $m_0p$
outside the pair form; (5) is a balance of pair counts. Hence

$$
P(x;k)\le 2E_{2x}+\#\{n\le x:\varphi(n)=\varphi(n+k),\ n\text{ or }n+k\text{ not of pair form}\},
$$

and the second term is unconstrained by (3)–(5). Which arguments are of pair
form depends on the accepted file's record selection, which no held prose
states, so the second term cannot even be identified here. The first term
is $o(V(2x))$ with no rate, and by Step 2 of the reconstruction
$V(2x)\ge\pi(2x)\ge c_0\cdot2x/\log(2x)$, so $x/(\log x)^2=o(V(2x))$: the
bound $o(V(2x))$ is weaker than the recorded $x/(\log x)^2$ even on the
pair-form part. S4 stands on both counts. The only sense in which (4) says
anything about shifted collisions is the useless one that the pair-form
part of $P(x;k)$ is $o(V(2x))$.

**W2: from the $P(x;k)$ bounds to no proof of (4) (S6).** Let
$(b,p)\ne(b',p')$ be pairs with $b(p-1)=b'(p'-1)$, with arguments $n=m_0p$
and $n'=m_0'p'$. Since $b=\varphi(m_0)$ and $b'=\varphi(m_0')$,

$$
\frac{n}{n'}=\frac{m_0/\varphi(m_0)}{m_0'/\varphi(m_0')}\cdot\frac{p}{p-1}\cdot\frac{p'-1}{p'} .
$$

The first factor is $1$ exactly when $m_0$ and $m_0'$ have the same
radical: writing $m/\varphi(m)=\prod_{q\mid m}q/(q-1)$ and clearing
denominators, the largest prime in the symmetric difference of the two
prime sets divides one side and not the other, so equal ratios force equal
radicals. When the radicals differ, $n/n'$ tends to a limit $\rho\ne1$ as
$p,p'\to\infty$, so $|n-n'|\ge\tfrac12|\rho-1|\,n'$ for all large top
primes, a distance growing linearly and outside every range
$k\le\exp((\log x)^{1/3})$ in which the 2013 manuscript bounds $P(x;k)$.
Exact witnesses with cores $1$ and $2$, records $1$ and $4$: $(1,13)$ and
$(2,7)$ share the value $12$ at arguments $13$ and $28$; $(1,37)$ and
$(2,19)$ share $36$ at $37$ and $76$; $(1,61)$ and $(2,31)$ share $60$ at
$61$ and $124$; and the value $24$ carries the three pairs $(2,13)$ with
record $4$, $(4,7)$ with record $5$ and $(6,5)$ with record $9$, at
arguments $52$, $35$ and $45$. When the radicals agree, $b(p-1)=b'(p'-1)$
is equivalent to $m_0(p-1)=m_0'(p'-1)$, so $n-n'=m_0-m_0'$: the distance
is then a difference of cores, bounded only by the cores' size, which the
write-up controls as $\log b\le G(y)=o(\log y)$ and not by $\log\log y$.
To obtain (4) from the shifted-collision bounds one would need every
collision of the retained family to fall in a covered range and a bound on
their total, neither of which any held source supplies; "those bounds do
not give (4)" is the correct record of this. Whether the small cores of the
witnesses are retained by the accepted file is not known here and is not
needed: S6 asserts "need not", an existence statement about pair
collisions, and the linear-distance mechanism holds for any two retained
cores of different radical.

**W3: the value set carries no index information (S7).** $V$ is determined
by the set $\varphi(\mathbb N)$. For a bijection $\sigma$ of the positive
integers put $g=\varphi\circ\sigma$; then $g$ has the same value set and the
same counting function $V$. (i) Some $\sigma$ gives $g(n)\ne g(n+1)$ for
every $n$: at step $n$ choose the least unused integer whose value differs
from $g(n-1)$, which exists since the fiber of $g(n-1)$ is finite; every
integer $u$ is used, because at the first step at which $u$ is the least
unused integer it is chosen unless $\varphi(u)=g(n-1)$, and then the
integer chosen instead has a different value and $u$ is chosen at the next
step. Choosing instead the least unused integer whose value differs from
the previous $\lfloor\sqrt n\rfloor$ values gives, by the same argument
(the value $\varphi(u)$ leaves the window finitely many steps after its
last occurrence, and no new occurrence can be placed while $u$ is the least
unused integer), a $\sigma$ for which every block starting at position $s$
of length at most $\lfloor\sqrt s\rfloor$ has pairwise distinct values.
(ii) Some $\sigma$ gives a collision inside every window of four
consecutive positions: fill positions $3i+1$ and $3i+2$ with the preimages
$m$ and $2m$ of $\varphi(m)$ for the odd $m\ge3$ in increasing order, and
positions $3i+3$ with the remaining integers ($1$, $2$ and the multiples of
$4$) in increasing order; any four consecutive positions contain a full
pair. So for $g$ the question of Problem 1003 has the answer no under (i)
and yes under (ii), and the question of Problem 1004 has the answer yes for
every $c>0$ under the second choice in (i) and no for every $c>0$ under
(ii), with the same $V$ throughout. No statement about $V$, and no
statement about the set of totient values, can therefore decide either
problem; the series of Problem 249 is likewise a function of the indexed
sequence, not of its value set. The pair family does carry arguments, and
that is exactly what W1 and W2 examine.

## Strongest attack

- **S1.** Each paraphrase was checked clause by clause against the
  statement blocks and the leads' frontmatter and self-descriptions. The
  attack fails; the residue is two glosses (F5, and the dropped "fixed
  $c>0$, sufficiently large $x$"), neither of which changes the question,
  and one omission of a sibling lead (F7).
- **S2.** The write-up's §4.2 states that different pairs may produce the
  same integer $b(p-1)$ after one record per core is chosen; the problem
  statements are equalities of values at arguments $n$ and $n+1$, or on a
  block. No misreading found.
- **S3.** The attack sought a shifted collision between two pair-form
  arguments that is not a pair collision. None exists for $k\ge1$: equal
  pairs force equal selected records and $k=0$ (W1). The statement is
  therefore true and its qualifier vacuous (F3).
- **S4.** The attack tried to extract any bound on $P(x;k)$ from
  (3)–(5): it produces only $o(V(2x))$ for the pair-form part, which is
  weaker than the recorded bound, and nothing for the rest (W1). The
  attack on the wording found that the sentence's stated reasons are the
  secondary ones (F1).
- **S5.** The attack checked the source. The 17-page manuscript states on
  local p. 10, in the proof of Theorem 1.2, that by Theorems 3.1 and 3.3 the
  number of $n\le x$ with $\varphi(n)=\varphi(n+k)$ is $\ll x/(\log x)^2$
  uniformly for $k\le\log x$. The reviewer re-derived it. For odd $k$,
  Theorem A's hypothesis that $j$ and $j+k$ have the same prime factors
  forces $k$ even, so $P_0(x;k)=0$ and
  $P(x;k)=P_1(x;k)<x/\exp((\log x)^{1/3})$ for $x>x_0$ uniformly for
  $k\le\exp((\log x)^{1/3})$ by Theorem 3.1. For even $k$, Theorem 3.3
  with $\epsilon(x)=1/\log\log x$ covers $k\le\log x$ for large $x$ and gives
  $P_0(x;k)\le(16C_2+o(1))c(k)x/(\log x)^2$ uniformly, where
  $c(k)\le3\cdot7^{3+2\omega(k)}k^{-1}\prod_{p\mid k,\,p>2}(p-1)/(p-2)$;
  since $k\ge\prod_{p\mid k}p$, this is at most
  $3\cdot7^3\prod_{p\mid k}(49/p)\prod_{p\mid k,\,p>2}(p-1)/(p-2)$, and
  the factor $(49/p)\cdot(p-1)/(p-2)$ is below $1$ for every prime
  $p\ge53$, so $c(k)$ is bounded by an absolute constant. The bound is
  uniform for all $k\le\log x$; the attack fails. Its residue is the word
  "at" (F2) and the unverifiable attribution to the problem page.
- **S6.** The attack tried to confine pair collisions to a range of shifts
  that the manuscript covers, so that summing $P(y;k)$ over that range would
  give (4). W2 shows collisions between cores of different radical sit at
  linear distance, and that the retained family's collisions are described
  in no held prose. The attack fails.
- **S7.** The attack sought an index property recoverable from $V$. W3
  gives reindexings with the same $V$ and opposite answers to Problems 1003
  and 1004. The attack fails. On the gloss "tail sums" see F6.
- **S8.** The outcome composes S4, S6 and S7; each survived. The attack
  fails.

## Premises

- **Proposition 4.1 of the write-up, interface only.** Statement as on the
  reconstruction page and the proposition_4_1 result page; source the held
  five-page write-up of Kruer and Kohlmeyer (2026), p. 3, with §3 for the
  family (cores from records with a bounded tail and a decreasing prime
  list, one record selected per core, top prime above the record's primes,
  value $b(p-1)$, value window with lower cutoff $y^{99/100}$) and §4.2
  for the collisions; standing: kernel acceptance of a Lean file that is
  not held, no prose proof. Used here only for what (4) counts; its truth
  is never consumed. Read at statement level, pp. 2–4.
- **The reconstruction page's Step 2.** $V(y)\ge\pi(y+1)\ge c_0y/\log y$
  for $y\ge2$ by the injection $p\mapsto p-1$ and Chebyshev's lower bound
  for $\pi$; the page was independently reviewed as it stood on
  2026-09-28T05:03:27Z with corrections applied since; used in W1. Read in
  full.
- **The 2013 manuscript** of Pollack, Pomerance and Treviño, held 17-page
  copy, whose card records its provenance and states that the journal
  pagination is not assigned to the copy. Consumed: the definition of
  $P(x;k)$ and the split $P=P_0+P_1$ through Theorem A (local p. 5);
  Theorem 3.1 with its range $k\le\exp((\log x)^{1/3})$ (local p. 6);
  Lemma 3.2 and Theorem 3.3 with the bounds on $c(k)$ (local p. 6); the
  sentence in the proof of Theorem 1.2 (local p. 10). Statement level, with
  the derivation on p. 10 re-done. Refereed source; the result pages
  theorem_3_1 and theorem_3_3 restate Theorems 3.1 and 3.3 faithfully.
- **Problem statements** of E1003, E1004 and E0249, statement blocks only,
  read in full.
- **Lead pages.** The native-note lead: frontmatter (`candidate`,
  `unreviewed`), Theorem 1 of the note as recorded, the pointer to a
  sibling lead; the binary-series lead: frontmatter, its self-description
  as the editable proof sketch, $\Phi_N$, $T_N$, $I_N$ and Propositions 3
  and 3′. Author-recorded, unreviewed; consumed only for what they use.
- **Elementary facts proved here.** Equal ratios $m/\varphi(m)$ force
  equal radicals (W2); the reindexing constructions (W3); the totient
  values of the witnesses (W2), computed exactly.

## Findings

- **F1 (suggested).** Lines 607–611, "A shifted collision between two
  arguments of pair form ... and (4) counts pair collisions with no rate
  and no reference to $k$, summed over all values up to $y$, so it does not
  bound $P(x;k)$". Defect: the "so" rests on three secondary features of
  (4) and leaves the primary reason implicit, that $P(x;k)$ counts
  arguments of every shape while (4) sees only the arguments of pair form,
  a set no held prose identifies; and it does not say that even on that
  part (4) gives only $o(V(x))$, weaker than $x/(\log x)^2$. Witness: W1.
  Replacement: "...and (4) bounds only the excess over the retained pairs,
  with no rate and no reference to $k$: an $n$ counted by $P(x;k)$ need not
  be of pair form, and the pair-form part is bounded only by $o(V(x))$,
  which is weaker than $x/(\log x)^2$ since $V(x)\ge c_0x/\log x$; so (4)
  does not bound $P(x;k)$...".
- **F2 (suggested).** Lines 611–613, "which the Problem 1004 page records
  at $x/(\log x)^2$ uniformly for $k\le\log x$ from the 2013 manuscript".
  Defect: "records at" reads as an order of magnitude; the source states an
  upper bound $\ll x/(\log x)^2$, and for odd $k$ the count is below
  $x/\exp((\log x)^{1/3})$. Witness: the source sentence and its derivation
  (Strongest attack, S5). Replacement: "which the 2013 manuscript bounds by
  $\ll x/(\log x)^2$ uniformly for $k\le\log x$ (from its Theorems 3.1 and
  3.3, in the proof of its Theorem 1.2), as the Problem 1004 page records".
- **F3 (note).** Lines 607–609, "is a pair collision only when the pairs
  differ". The qualifier is vacuous for $k\ge1$: with one selected record
  per core, equal pairs force $m_0=m_0'$ and $p=p'$, hence $k=0$.
  Replacement: "is a pair collision between two distinct pairs".
- **F4 (note).** Line 610, "summed over all values up to $y$". The
  write-up's family retains only values above the cutoff $y^{99/100}$
  (p. 3), so the fibers of $f_y$ run over the retained values; the phrase
  follows the reconstruction's interface $f_y\colon P_y\to T(y)$ and is
  harmless. Replacement: "summed over the fibers of $f_y$".
- **F5 (note).** Lines 596–597, "a block of length $(\log x)^c$ below
  $x$". The statement asks for $n\le x$ with
  $\varphi(n+1),\dots,\varphi(n+\lfloor(\log x)^c\rfloor)$ pairwise
  distinct; the block starts at or below $x$ and may end above it. For the
  every-$c$ question the readings are equivalent (pass from $x$ to
  $x-\lfloor(\log x)^c\rfloor$ and enlarge $c$ slightly). Replacement: "a
  block of length $(\log x)^c$ starting at some $n\le x$".
- **F6 (note).** Lines 615–616, "the $2$-adic valuations of tail sums for
  Problem 249". The lead's criterion (its Proposition 3) is stated for
  $v_2(\Phi_N)$ with $\Phi_N=\sum_{n\le N}\varphi(n)2^{N-n}$, a scaled
  partial sum, and passes through the tail integers $I_N=bT_N$, whose
  valuation equals $v_2(b\Phi_N)$ under rationality (its Proposition 3′).
  The gloss is accurate about what the lead uses, the sequence in its
  index order; "partial and tail sums" would be exact.
- **F7 (note).** Lines 598–599. The section names the native-note lead as
  the Problem 1004 candidate; that lead's page states that the note's
  $c<2$ corollary is carried by a sibling lead on distinct totient blocks
  from collision bounds, through a proposition on the Problem 49
  connections page, neither in this review's read set. The obstruction of
  S7 applies to any lead built on consecutive distinctness, so the outcome
  is unaffected; naming the sibling would complete the target list.

## Verdict

- **S1:** refutation-failed. The targets and leads are described as the
  statement blocks and lead pages state them, up to the glosses in F5 and
  the omission in F7.
- **S2:** refutation-failed. The two equations are stated as the write-up
  and the problem pages state them.
- **S3:** refutation-failed. True, with a vacuous qualifier (F3).
- **S4:** refutation-failed. Re-derived in W1; the stated reasons deserve
  the completion in F1.
- **S5:** refutation-failed as to the source, whose sentence and range the
  reviewer confirmed and re-derived, including odd shifts; the attribution
  to the Problem 1004 page was not checked (limitation below); wording in
  F2.
- **S6:** refutation-failed. Re-derived in W2 with exact witnesses.
- **S7:** refutation-failed. Re-derived in W3 by reindexing.
- **S8:** refutation-failed. The outcome is the composition of S4, S6 and
  S7, each of which survived.

**Limitations.** The clause "which the Problem 1004 page records" was
checked against the 2013 manuscript and not against the problem page, whose
text outside its statement block is excluded from this review. The exact
membership of the retained family, hence the set of pair-form arguments, is
stated in no held prose, so W1 and W2 treat the family through its
interface only; this cannot rescue a transfer, since the section claims
none. No computation beyond exact small totient values was needed. The
section's statements are non-transfer records and citations, not theorems
with proofs; the verdicts say that no attack refuted them, not that a
transfer is impossible by an argument stronger than W1–W3.

This focused review assigns no tier and changes no status.
