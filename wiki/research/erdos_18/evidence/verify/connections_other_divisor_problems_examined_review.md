---
name: research/erdos_18/evidence/verify/connections_other_divisor_problems_examined_review
title: "Independent review of the connections section: Other divisor problems examined"
desc: |
  Refutation-charge review of the six no-transfer bullets of the section.
  Every no-transfer conclusion survives (refutation-failed for S1, S2, S3,
  S5, S6, S7 and S8; S4 is a source characterization the read set cannot
  check). Zero required corrections, four suggested corrections and three
  notes.
created: 2026-09-28T18:14:09Z
updated: 2026-09-28T18:14:09Z
---

***

## Subject and independence

The reviewer is an independent reviewer working in a fresh context from the
commissioning assignment alone; the reviewer took no part in writing the
connections page, the reconstruction pages, the shared lemmas or any problem
page, and read no earlier review or grade of any of them.

Subject: path `wiki/research/erdos_18/connections.md` as it stood at
2026-09-28T13:50:48Z, the H2 section "Other divisor problems examined", lines
736–778 (the next H2, "Leads created", starts at line 779). The section names no
lead page; the two lead folders named under "Leads created" belong to the
Problem 304/293 and Problem 18(a) sections and were not read.

Read, as of the time named above: the section in full; the page's opening
conventions paragraph (lines 19–45) and the Shared lemmas section (lines
47–243) in full, as inputs whose proofs are another reviewer's subject; the
reconstruction pages
[[research/erdos_18/hughes_corollary_3_reconstruction|Corollary 3]] (in full)
and [[research/erdos_18/hughes_lemma_4_reconstruction|Lemma 4]] (definitions,
statement, consequence and the factorial ratio proof), as premises; the
Statement paragraphs of the fourteen problem pages the section names,
[[problems/divisors/E0144/_index|E0144]], [[problems/divisors/E0886/_index|E0886]],
[[problems/divisors/E0887/_index|E0887]], [[problems/divisors/E1100/_index|E1100]],
[[problems/divisors/E0468/_index|E0468]], [[problems/divisors/E0469/_index|E0469]],
[[problems/divisors/E0470/_index|E0470]], [[problems/divisors/E1054/_index|E1054]],
[[problems/additive_combinatorics/E0350/_index|E0350]] (with its Formulation
paragraph, which sits inside the statement block),
[[problems/divisors/E0882/_index|E0882]], [[problems/divisors/E0446/_index|E0446]],
[[problems/divisors/E0448/_index|E0448]], [[problems/divisors/E0449/_index|E0449]] and
[[problems/divisors/E0450/_index|E0450]]; the provenance paragraph of the library
card
[[../library/divisors/hughes_2026_sums_distinct_divisors_factorials/_index|Hughes (2026)]]
and its result page
[[../library/divisors/hughes_2026_sums_distinct_divisors_factorials/theorem_2|Theorem 2 (quoted)]]
in full; the text layer of the held Hughes PDF, searched for every mention of
Berend–Harmse and of a Theorem 3 or Theorem 4; the commissioned sections of
`docs/verification.md`, `docs/approach_vetting.md`, `docs/evidence.md`
"Source fidelity" and `docs/math_authoring.md`. The Berend–Harmse 1993 paper
is not held and was not read.

Exposures: while locating the Statement paragraph of E0144, its Status line
(status, prize and tags) was displayed; while reading the provenance paragraph
of the Hughes card, its "Read status" and "Bears on" paragraphs and the first
lines of its Overview were displayed, including one sentence comparing the
paper's Theorem 1 with a site-accepted proof. File names (not contents) of the
folder's `evidence/verify/` directory and of untracked files in the worktree
were displayed by directory listings. Nothing from any review, grade, Current
assessment or Known results section reached the reviewer. Small exact
computations (divisor enumeration and subset-sum tables below $3000$, and
the two width comparisons at $n=2^{16}$ and $n=10^6$) were run as sanity
checks of derivations that are written out below; they are base-case
coverage only and carry no weight in the verdicts.

## Restatement

Conventions of the page: $h(N)$, $\tau(N)$, $v_p$, $L_x$,
$\varepsilon_j$ and the windows $[\sqrt{(j-1)!},\sqrt{j!}]$ are as in the
page's conventions paragraph and the Corollary 3 page; a number $N$ has the
*ratio-two property* when consecutive divisors of $N$ have ratio at most
$2$. Lemma A (shared) states: if $v_2(N)\ge\lfloor\log_2p\rfloor$ for
every odd prime $p\mid N$, then $N$ has the ratio-two property; the
hypothesis holds for $N=n!$ and $N=L_x$.

- **S0** (preamble). A search of the problems, research and theory trees for
  the objects of the proofs surfaced the pages listed, and each is a
  resemblance without a transfer. This is a process statement about a search
  and a summary of S1–S8; it is not a mathematical claim.
- **S1** (Problem 144). For every $n$ and every $x$, the numbers $n!$
  and $L_x$ have two divisors $d_1<d_2<2d_1$, and this is said to follow
  as "the trivial instance" of Lemma A. The target, that the set of integers
  with two such divisors has natural density $1$, is a density-one
  statement over all integers, which no statement about the sparse families
  $n!$ and $L_x$ reaches.
- **S2** (Problems 886 and 887, widths). For $N=n!$ and fixed
  $\eta>0$, $C>0$, the interval $(\sqrt N,\sqrt N+N^{1/2-\eta})$ is a
  multiplicative window of relative width $N^{-\eta}$ and
  $(\sqrt N,\sqrt N+CN^{1/4})$ one of relative width $CN^{-1/4}$; both
  are exponentially narrower, as $n\to\infty$, than the precision
  $\varepsilon_n=\exp(-(\log n)^2/(2\log2)\,(1-o(1)))$ of the imported
  Berend–Harmse estimate.
- **S3** (Problems 886 and 887, no transfer). The reconstructed estimate
  (Corollary 3: for $j\ge2^{16}$, $n\ge j$ and consecutive divisors
  $a<b$ of $n!$ with $\sqrt{ab}$ in the window of index $j$,
  $\log(b/a)\le3\varepsilon_j$) gives no information on the number of
  divisors of $n!$ in windows of relative width $N^{-\eta}$ or
  $CN^{-1/4}$; in particular nothing toward either problem's requested
  uniform upper bound ($O_\eta(1)$ for all large $n$, or an absolute
  $K$ valid for every $C$).
- **S4** (Problems 886 and 887, parenthetical). Theorems 3 and 4 of the
  Berend–Harmse 1993 paper concern the most balanced factorization of $n!$
  and are not reconstructed in the folder. This is a characterization of a
  source that is not held.
- **S5** (Problem 1100). With $\tau_\perp(N)$ the number of indices $i$
  with $\gcd(d_i,d_{i+1})=1$ among the sorted divisors of $N$, the pairs
  $(d,d+1)$ with $1\le d\le n-1$ give $\tau_\perp(n!)\ge n-1$ for every
  $n\ge1$; this lower bound is far below the threshold
  $\exp((\log n!)^{o(1)})$ of the problem's second question (whether
  $\tau_\perp(N)<\exp((\log N)^{o(1)})$ for all $N$); the folder's
  mechanisms bound divisor gaps and say nothing about coprimality of
  consecutive divisors; no transfer.
- **S6** (Problems 468, 469, 470 and 1054). The four problems concern
  whether a number $n$ itself, or a given $n$, has one representation of a
  prescribed shape (an initial partial sum of the divisor chain of some
  $m$; a sum of distinct proper divisors; the failure of that for abundant
  $n$; a sum of the $k$ smallest divisors of some $m$), not whether
  every $m\le N$ has a short representation; the practical-number
  mechanism (Lemma 3.1 extensions, greedy expansions, the ratio-two
  property) does not address them; no transfer.
- **S7** (Problems 350 and 882). Problem 350 concerns finite sets with
  pairwise distinct subset sums and Problem 882 sets whose nonempty subset
  sums contain no two distinct elements one dividing the other; these are
  "the opposite of the many-representations property that practicality
  asserts"; no transfer.
- **S8** (Problems 446, 448, 449 and 450). The four problems are density
  statements about the divisors of typical integers in short multiplicative
  intervals, and the families studied in the folder ($n!$, $L_x$, the
  extension chains, practical numbers) have natural density zero; no
  transfer.

## Checklist

- **Quantifiers and scope.** Defect found in S1: Lemma A's conclusion is the
  non-strict ratio bound $b\le2d$, while the Problem 144 property is the
  strict $d_2<2d_1$; the boundary cases $n\le2$ and $x\le2$ fail the
  property (F1). S5's comparison is loosely phrased, since
  $\exp((\log N)^{o(1)})$ is a growth class and $n-1$ lies inside it
  (F6). The almost-all targets of S1 and S8 are correctly kept apart from
  the density-zero families. Elsewhere clean.
- **Circularity.** Inapplicable: no bullet derives a target from itself; the
  only deductions are the width computations, the trivial coprime pairs and
  the appeal to Lemma A.
- **Model and convention changes.** The section's $\tau_\perp$ agrees with
  the E1100 definition; the window intervals agree with E0886 and E0887; the
  page's $h$ convention is not used in the section. The word "window" is
  used for the precision $\varepsilon_n$, whereas the Corollary 3 page
  reserves it for $[\sqrt{(j-1)!},\sqrt{j!}]$ (F5, note). The reason given
  in S6 substitutes a shape mismatch for the actual relation, which is an
  entailment (practical and abundant implies pseudoperfect; F3), and the
  reason in S7 asserts an opposition that the divisor set of $2^k$ refutes
  (F4); neither affects the no-transfer conclusions.
- **Finite and statistical overreach.** Clean: no finite case is cited as
  more than an example; the reviewer's own finite checks are not used as
  evidence.
- **Uniformity.** Clean: the width comparison in S2 holds for every fixed
  $\eta>0$ and $C>0$ with the explicit rate rederived below; the
  $(1-o(1))$ in $\varepsilon_n$ is the explicit factor
  $1-2\log(\log n/\log2)/\log n$ of the Corollary 3 page. The dropped
  constant $C$ in "relative width $(n!)^{-1/4}$" is harmless (F5).
- **Extremal conclusions.** Inapplicable: no bullet asserts sharpness or an
  attained extremum.
- **Consequences and composition.** S1 composes Lemma A's conclusion with
  the strict target without the bridge (a pair of consecutive divisors with
  ratio strictly below $2$), which exists for $n,x\ge3$ but is not
  supplied by Lemma A (F1). S6's and S7's "hence no transfer" survive
  separately from their reasons (F3, F4). S3's "says nothing" is an honest
  negative: an upper bound on consecutive gaps yields neither an upper bound
  on divisor counts nor a lower bound in windows narrower than the gap
  bound.
- **Computation.** Inapplicable to the section (no computation is claimed);
  the arithmetic of S2 and S5 was rederived by hand below.
- **Reproduction.** Inapplicable: the section states no rerun command or
  coverage claim.
- **Source and verdict fidelity.** The fourteen problem descriptions match
  the Statement paragraphs (checked clause by clause; the section's status
  labels were not checked, status text being outside the read set). The
  Berend–Harmse import is used at the form the Theorem 2 page and the
  Corollary 3 page print. S4 characterizes theorems of a paper that is not
  held; the held Hughes PDF does not mention them, and the page's own
  "Sources read" paragraph says text-layer statements are marked, yet this
  one is not marked (F2).

## Weakest steps

**W1 (S1): from the ratio-two property to two divisors $d_1<d_2<2d_1$.**
Lemma A gives, for every divisor $d<N$, a divisor in $(d,2d]$. For
$N=2^k$ the hypothesis of Lemma A holds vacuously and every pair of
consecutive divisors has ratio exactly $2$, so $N=2^k$ has the ratio-two
property and no pair $d_1<d_2<2d_1$; hence the strict property is not a
consequence of Lemma A's conclusion. For $N=n!$ with $n\ge3$ and for
$N=L_x$ with $x\ge3$ the pair $(2,3)$ divides $N$ and $3<2\cdot2$,
so the property holds directly; for $n\le2$ and $x\le2$ the divisor sets
are $\{1\}$ or $\{1,2\}$ and it fails. So the bullet's content is right
for $n,x\ge3$, by a witness rather than by Lemma A.

**W2 (S2): the width comparison.** The relative width of
$(\sqrt N,\sqrt N+N^{1/2-\eta})$ is $N^{1/2-\eta}/N^{1/2}=N^{-\eta}$ and
that of $(\sqrt N,\sqrt N+CN^{1/4})$ is $CN^{-1/4}$. With $N=n!$,
$\log(1/N^{-\eta})=\eta\log n!\ge\eta(n\log n-n)$, while the Corollary 3
page's display (1) gives $\log(1/\varepsilon_n)\le(\log n)^2/(2\log2)$.
Hence

$$
\frac{N^{-\eta}}{\varepsilon_n}
\le\exp\Bigl(\frac{(\log n)^2}{2\log2}-\eta(n\log n-n)\Bigr)\to0
$$

at a rate exponential in $n\log n$, and the same holds with $C N^{-1/4}$
in place of $N^{-\eta}$. At $n=2^{16}$ the two logarithms are about
$6.6\cdot10^5\eta$ against $44.4$.

**W3 (S6): the relation between practicality and pseudoperfection.** Let
$n$ be practical (every $1\le m\le n$, or every $m<n$, is a sum of
distinct divisors of $n$) with sorted divisors
$1=d_1<\cdots<d_\tau=n$. For $i<\tau$ the target $m=d_{i+1}-1<n$ is a
sum of distinct divisors, each at most $m<d_{i+1}$, hence among
$d_1,\dots,d_i$; so $d_{i+1}\le1+d_1+\cdots+d_i$ for every $i<\tau$.
The standard completeness lemma (if $a_1=1$ and
$a_{i+1}\le1+a_1+\cdots+a_i$ for $i<k$, then every integer in
$[0,a_1+\cdots+a_k]$ is a sum of distinct $a_i$; induction on $k$,
subtracting $a_k$ from targets above $a_1+\cdots+a_{k-1}$) applied to
the proper divisors $d_1,\dots,d_{\tau-1}$ shows that every integer in
$[0,\sigma(n)-n]$ is a sum of distinct proper divisors of $n$. Two
consequences: $\sigma(n)\ge2n-1$ for every practical $n$ (take
$i=\tau-1$), and if $\sigma(n)\ge2n$ then $n$ itself is such a sum, so
$n$ is pseudoperfect and, in the terms of Problem 470, no weird number is
practical. So the "shape" reason of S6 is wrong for Problems 469 and 470:
the every-target property entails the one-representation property whenever
$n$ is abundant or perfect. The no-transfer conclusion still holds: odd
$n>1$ is never practical (the target $2$ is not a sum of divisors of an
odd $n$), so nothing is learned about odd weird numbers; primitive weird
numbers are non-practical by the above, so the mechanism cannot produce or
count them; and the convergence of $\sum1/n$ over primitive pseudoperfect
numbers is untouched, since the mechanism says nothing about which
pseudoperfect numbers are primitive.

## Strongest attack

- **S1.** Attack: find $N$ satisfying Lemma A's hypothesis without the
  strict property. Witness $N=2^k$ (and $N=1!,2!,L_1,L_2$ within the
  named families). The attack succeeds against the sentence's appeal to
  Lemma A and against the boundary cases, and fails against the content for
  $n,x\ge3$ (witness $2<3<4$) and against the no-transfer conclusion (a
  density-one statement over all integers is untouched by two sparse
  families). Recorded as F1.
- **S2.** Attack: seek $\eta$ or $n$ for which $N^{-\eta}$ is not
  below $\varepsilon_n$. Fails: W2 gives the explicit inequality for every
  fixed $\eta>0$ once $\eta(n\log n-n)>(\log n)^2/(2\log2)$, which holds
  for all large $n$ and, for instance, for every $\eta\ge10^{-3}$ at
  $n\ge2^{16}$.
- **S3.** Attack: extract from Corollary 3 either an upper bound on the
  number of divisors in a window or a lower bound in a window narrower than
  $3\varepsilon_n$. Fails: the estimate is an upper bound on the ratio of
  consecutive divisors only; it implies at least one divisor in every
  multiplicative window of relative width above the gap bound and nothing
  else. The problem windows lie just above $\sqrt{n!}$, outside the range
  $\sqrt{ab}\le\sqrt{n!}$ of the statement, but the map $d\mapsto n!/d$
  mirrors the divisor set, so this changes nothing.
- **S4.** Attack: check the characterization against a held source. Not
  possible: the 1993 paper is not held, and the held Hughes PDF cites only
  its Theorem 2 and Remark 2. Recorded as F2.
- **S5.** Attack: find a pair $(d,d+1)$, $1\le d\le n-1$, that is not a
  coprime pair of consecutive divisors of $n!$, or two such pairs sharing
  an index. Fails: $d,d+1\le n$ both divide $n!$, no integer lies
  strictly between them, $\gcd(d,d+1)=1$, and distinct $d$ give distinct
  indices; so $\tau_\perp(n!)\ge n-1$ (with equality of the count of
  witnesses, and the true value larger from $n=5$ on). The comparison with
  the problem's threshold is loose (F6) but not false: for every fixed
  $c>0$, $n-1=\exp(\log(n-1))$ is far below $\exp((\log n!)^c)$.
- **S6.** Attack: exhibit a transfer from the practical-number mechanism to
  one of the four problems. W3 exhibits an entailment (practical and
  abundant implies pseudoperfect) that the bullet's reason denies, but no
  transfer to the questions asked: Problems 469 and 470 ask about primitive
  pseudoperfect numbers, odd weird numbers and primitive weird numbers, all
  outside the reach of a statement about practical numbers (W3); Problems
  468 and 1054 ask about initial-segment sums of a divisor chain, a shape
  the mechanism never produces. The conclusion survives; the reason is
  corrected in F3.
- **S7.** Attack: exhibit a set that is at once dissociated and the divisor
  set of a practical number. Witness: the divisors $\{1,2,\dots,2^k\}$ of
  the practical number $2^k$, which is also the extremal set of Problem
  350. So the properties are compatible, and practicality asserts a covering
  property (every target hit at least once), not "many representations". The
  attack succeeds against the word "opposite" and fails against the
  no-transfer conclusion: nothing in the folder bounds $\sum1/a$ over
  dissociated sets or the size of a divisibility-free subset-sum set; for
  Problem 882 the divisor set of any $n\ge2$ contains $1\mid2$ and is
  never admissible. Recorded as F4.
- **S8.** Attack: find one of the four problems for which a density-zero
  family could bear on the question. Fails for 446, 448 and 449, which are
  statements about natural density or almost all $n$, unchanged by any
  density-zero set; for 450, a uniform statement over all short intervals
  $(x,x+y)$, the reason applies only indirectly (a sparse family gives no
  upper bound valid for every interval), and there is still no transfer
  (F7, note). That $n!$, $L_x$ and the extension chains have density
  zero is immediate from their growth; that practical numbers do is a known
  theorem not established in the folder, and the bullet does not depend on
  it.

## Premises

- **Lemma A** (shared, connections page lines 52–78): hypothesis
  $v_2(N)\ge\lfloor\log_2p\rfloor$ for every odd prime $p\mid N$;
  conclusion the ratio-two property (non-strict), practicality, distinct
  greedy divisors and $h(N)\le\log_2N+1$; the hypothesis is stated to hold
  for $n!$ and $L_x$. Author-recorded; its proof is another reviewer's
  subject. Used in S1 only for the non-strict ratio bound, within its
  hypothesis; the interface confirmed at the use, with the strictness gap
  noted in F1.
- **Corollary 3 reconstruction** (folder page, read in full): defines
  $\varepsilon_x=(1/x)^{\lg x/2-\lg\lg x}$ for $x\ge2^{16}$ with
  $\log(1/\varepsilon_x)=(\log x)^2/(2\log2)\,(1-2\log(\log x/\log2)/\log x)$,
  and states $\log(b/a)\le3\varepsilon_j$ for consecutive divisors of
  $n!$ with geometric mean in the window of index $j\le n$, $j\ge2^{16}$.
  Independently reviewed as of 2026-09-28T05:03:27Z per the assignment; consumed
  at that standing. Used in S2 (form of $\varepsilon_n$; rederived the
  expansion of display (1)) and S3 (what the estimate says).
- **Lemma 4 reconstruction** (folder page; definitions, statement,
  consequence and the factorial ratio proof read): not used by the section
  directly; it is the source of Lemma A's consequence clause.
- **Hughes (2026)** library card provenance paragraph and Theorem 2 page:
  the Berend–Harmse estimate is quoted second-hand from the held preprint
  (arXiv:2609.10902v1, p. 2); the 1993 paper is not held. Held PDF: text
  layer searched for the cited theorems (only Theorem 2 and Remark 2 of
  Berend–Harmse appear). Reading depth: the Theorem 2 page in full, the card
  to its Overview.
- **Problem pages**: the Statement paragraphs of the fourteen pages listed
  above, read in full and compared clause by clause with the section's
  descriptions; nothing else on those pages was read except the exposures
  disclosed.
- **Standard facts used by the reviewer**: the completeness lemma for
  sequences with $a_{i+1}\le1+a_1+\cdots+a_i$ (proved inline in W3);
  $\log n!\ge n\log n-n$; the mirror symmetry $d\mapsto n!/d$ of the
  divisor set.

## Findings

- **F1** (suggested; S1, lines 744–746: "Lemma A is the trivial instance for
  $n!$ and $L_x$"). Defect: Lemma A concludes the non-strict bound
  $b\le2d$, and the Problem 144 property needs $d_2<2d_1$; the two
  differ, and the named families fail the property at $n\le2$ and
  $x\le2$. Witness: $N=2^k$ satisfies Lemma A's hypothesis and has no
  divisors $d_1<d_2<2d_1$; $2!$ and $L_2$ likewise. Replacement: "For
  $n,x\ge3$ the divisors $2<3<4$ of $n!$ and $L_x$ give the property
  outright (Lemma A's non-strict bound alone does not, as $N=2^k$ shows);
  the target is a density-one statement over all $n$."
- **F2** (suggested; S4, lines 753–755: "Berend and Harmse's Theorems 3 and
  4 concern the most balanced factorization of $n!$ and are not
  reconstructed here"). Defect: a characterization of a source that is not
  held, taken (per the page's "Sources read" paragraph) from a text layer
  with garbled displays, and not marked as such although that paragraph says
  such statements are marked; the held Hughes PDF cannot confirm it.
  Witness: no held source mentions those theorems. Replacement: either drop
  the parenthetical or mark it, e.g. "(Berend and Harmse's Theorems 3 and 4,
  read in the Numdam text layer and not verified on the page images, concern
  the most balanced factorization of $n!$ and are not reconstructed
  here.)"
- **F3** (suggested; S6, lines 765–767: "Each concerns whether $n$ itself,
  or a given $n$, has one representation of a prescribed shape, not whether
  every $m\le N$ has a short one; the practical-number mechanism does not
  address them"). Defect: for Problems 469 and 470 the two properties are
  not disjoint shapes but related by entailment: every practical $n$ with
  $\sigma(n)\ge2n$ is pseudoperfect, so no weird number is practical (W3).
  Witness: the derivation W3; for instance every $2^ap$ with $p$ an odd
  prime below $2^{a+1}$ is practical, abundant or perfect, and
  pseudoperfect. The no-transfer conclusion stands for the questions asked.
  Replacement: "Problems 468 and 1054 concern initial-segment sums of a
  divisor chain, a shape the mechanism never produces. For Problems 469 and
  470, practicality is stronger than pseudoperfection on abundant numbers
  (every practical $n$ with $\sigma(n)\ge2n$ is a sum of distinct proper
  divisors, so weird numbers are never practical), but the questions asked,
  about odd weird numbers (odd $n>1$ is never practical), primitive weird
  numbers and the reciprocal sum of primitive pseudoperfect numbers, lie
  outside what a statement about practical numbers can reach."
- **F4** (suggested; S7, lines 770–771: "the opposite of the
  many-representations property that practicality asserts"). Defect:
  practicality asserts that every target $m\le n$ is hit at least once,
  not that it has many representations, and dissociation is compatible with
  it. Witness: the divisor set $\{1,2,\dots,2^k\}$ of the practical number
  $2^k$ has pairwise distinct subset sums and is the extremal set of
  Problem 350. Replacement: "Problem 350 asks for the extremal reciprocal sum
  under distinct subset sums and Problem 882 for the extremal size under
  divisibility-free subset sums; practicality asks only that every target be
  hit, which is compatible with distinct subset sums (the divisors of
  $2^k$), and none of the mechanisms here bounds either extremal
  quantity."
- **F5** (note; S2, lines 750–752). The phrase "the Berend–Harmse window
  $\varepsilon_n$" uses "window" for the precision, whereas the Corollary
  3 page reserves "window" for $[\sqrt{(j-1)!},\sqrt{j!}]$; and the second
  relative width is $C(n!)^{-1/4}$, the constant being dropped. Neither
  affects the comparison. Replacement: "the Berend–Harmse precision
  $\varepsilon_n$" and "relative width $(n!)^{-\eta}$ or
  $C(n!)^{-1/4}$".
- **F6** (note; S5, line 758: "far below the question's
  $\exp((\log n!)^{o(1)})$"). $\exp((\log N)^{o(1)})$ is a growth class,
  and $n-1=\exp(\log(n-1))$ belongs to it at $N=n!$; the intended
  comparison is with $\exp((\log n!)^c)$ for fixed $c>0$, below which
  $n-1$ indeed lies. Replacement: "well inside the bound the second
  question conjectures".
- **F7** (note; S8, lines 775–777). Problem 450 is a uniform statement over
  all short intervals $(x,x+y)$ rather than a density statement, so the
  density-zero reason applies to it only indirectly; the no-transfer
  conclusion is unaffected.

## Verdict

- S0: not a mathematical claim; no verdict.
- S1: refutation-failed for the content restricted to $n,x\ge3$, by the
  witness $2<3<4$ and the density-one nature of the target; the appeal to
  Lemma A does not supply the strict inequality, and the boundary cases fail
  (F1, suggested).
- S2: refutation-failed.
- S3: refutation-failed.
- S4: no mathematical verdict; a characterization of a source outside the
  read set, unverifiable here and unmarked (F2, suggested).
- S5: refutation-failed (F6, note).
- S6: refutation-failed for the no-transfer conclusion; the stated reason is
  inaccurate for Problems 469 and 470 and is replaced in F3 (suggested).
- S7: refutation-failed for the no-transfer conclusion; the word "opposite"
  is false as a mathematical characterization, witness the divisor set of
  $2^k$, and is replaced in F4 (suggested).
- S8: refutation-failed (F7, note).

Limitations: the section's status labels for the fourteen problems were not
checked, status text being outside the read set; the Berend–Harmse 1993
paper is not held, so S4 and the second-hand import behind
$\varepsilon_n$ were taken at the standing the Corollary 3 page records;
the proofs of the shared lemmas and of the reconstruction pages were not
re-examined beyond their interfaces. Required corrections: none. Suggested:
F1–F4. Notes: F5–F7. This focused review assigns no tier and changes no
status.
