---
name: research/erdos_49/evidence/verify/connections_problem_49_the_remaining_clause_review
title: "Independent review of the connections section: Problem 49: the remaining clause"
desc: |
  Refutation-failed for all six checked statements of the section: the
  clause identification, the nothing-transfers obstruction, the factor
  tending to infinity over the prime count, Tao's rate superseding it, the
  elementary strict bound, and the exact-question obstruction. Zero
  required corrections; one suggested correction to the sentence on the
  role of the reversed pairs; two notes.
created: 2026-09-28T18:26:11Z
updated: 2026-09-28T18:27:17Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, commissioned for
refutation and given only the assignment. The reviewer took no part in
writing the connections page, the reconstruction pages, the problem page or
any lead, and had read none of them before this assignment.

**Subject.** Page `wiki/research/erdos_49/connections.md` as it stood on
2026-09-28T13:50:48Z, section "Problem 49: the remaining clause", lines
626--637: the H2 heading is line 626 and the section runs to the end of the
file. The section names no lead page. The page's lead paragraph "Outcomes at a
glance" (lines 44--56) carries, at lines 49--50, the one-line summary "The open
clause of Problem 49: nothing transfers", reviewed here as the section's
restatement.

**Reading, at depth.**

- `wiki/research/erdos_49/connections.md`: frontmatter, lead, Standing,
  Outcomes at a glance and "Notation and the inputs used" (lines 1--111) in
  full; the section (lines 626--637) in full; of the other sections only
  the list of H2 headings.
- Reconstruction pages in the same state, taken as premises:
  [[research/erdos_49/theorem_1_2_reconstruction|Theorem 1.2]] and
  [[research/erdos_49/lemma_5_1_reconstruction|Lemma 5.1]] in full;
  Lemma 4.1, Theorem 3.1, Theorem 3.3 and Lemma 3.2: Statement sections
  only.
- [[problems/primes/E0049/_index|Problem 49]]: the Statement paragraph (the page
  has no Statement heading; see exposures).
- Library: the lead of the card
  [[../library/primes/tao_2024_monotone_nondecreasing_sequences_euler_totient_function/_index|Tao (2024)]]
  (the card has no headings, so its lead is its provenance paragraph); the
  statement and definition paragraphs of its
  [[../library/primes/tao_2024_monotone_nondecreasing_sequences_euler_totient_function/theorem_1_1|Theorem 1.1]],
  [[../library/primes/tao_2024_monotone_nondecreasing_sequences_euler_totient_function/strict_transfer|strict transfer]]
  and notation pages; the lead and contents list of the card
  [[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/_index|Pollack, Pomerance and Treviño (2013)]]
  and its
  [[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/theorem_1_2|Theorem 1.2 page]]
  (see exposures); the lead of the card
  [[../library/arithmetic_functions/ford_1998_distribution_totients/_index|Ford (1998)]].
- Held PDFs: the Pollack, Pomerance and Treviño author manuscript, pp. 1--2
  and 7--10 on the text layer and p. 10 on the page image; the published
  Tao paper, printed pp. 793--794 and 811 on the text layer and p. 794 on
  the page image.
- Rules: `docs/verification.md` ("Whole-claim report", both audit
  checklists, "Grading and claim standing"), `docs/approach_vetting.md`,
  `docs/evidence.md` ("Source fidelity"), `docs/math_authoring.md`.

Not read: the folder index, everything under any evidence folder, the other
sections of the connections page, the problem page below its first H2, and
the web.

**Exposures.**

1. The problem page has no `## Statement` heading, so locating the
   statement printed the region above its first H2. That region includes
   the frontmatter line `status: open` and the paragraphs Status, Tags,
   Source, References and Formalization; the Status paragraph is standing
   text. Only the Statement paragraph was used. The Status paragraph's
   account of which clauses are settled was not relied on; the review
   derives that below from the held statements.
2. The Theorem 1.2 result page of the Pollack, Pomerance and Treviño card
   was read whole, including its Consequence, Read depth, Proof pointer,
   Dependencies and Bears on parts; the Bears on part ends with an
   assessment sentence about the strict clause. The Tao card, having no
   headings, was read whole as its provenance paragraph; it carries a
   Bears on line and a sentence on what the strict transfer does not
   assert. Neither sentence was used as a premise.
3. Working-tree listings showed the file names of parallel review reports
   for another folder and for the other sections of this page; none was
   opened.

No other exposure.

## Restatement

Notation as on the page: $\mathcal W(x)=\{\varphi(n):n\le x\}$ and
$W(x)=\#\mathcal W(x)$; $M^\uparrow(x)$ is the largest size of a set of
integers in $[1,x]$ on which $\varphi$ is nondecreasing; $M_<(N)$ is the
largest size of a set $A\subseteq\{1,\ldots,N\}$ on which $\varphi$ is
strictly increasing (the strict-transfer page's notation); $Z(x)$ is Ford's
function; $\pi(x)$ is the prime count.

- **S1 (clause identification).** The statement of Problem 49 asks three
  things about sets $A=\{a_1<\cdots<a_t\}\subseteq\{1,\ldots,N\}$ with
  $\varphi(a_1)<\cdots<\varphi(a_t)$: (i) whether the primes are a largest
  such set, that is, whether $M_<(N)=\pi(N)$; (ii) whether
  $|A|<(1+o(1))\pi(N)$; (iii) whether $|A|=o(N)$. The section asserts that
  (i) is the only clause still open and paraphrases it as "whether the
  primes are a largest subset of $\{1,\ldots,N\}$ with strictly increasing
  totients", with the range of $N$ left unstated. "A largest" is read as
  "of maximum cardinality", not as unique.
- **S2 (obstruction).** No statement on the connections page gives any
  information about clause (i); in the lead's words, nothing transfers.
- **S3.** Let $c>0$ and $x_0$ be the absolute constants of the
  reconstructed Theorem 1.2, so that $M^\uparrow(x)\le(1-c)W(x)$ for all
  $x\ge x_0$. Then $(1-c)W(x)/\pi(x)\to\infty$ as $x\to\infty$.
- **S4.** Tao's rate, $M^\uparrow(x)\le(1+O((\log_2x)^5/\log x))\pi(x)$
  for all $x\ge10$, supersedes that bound: it concerns the same weak
  maximum, holds at every $x\ge10$, and is smaller than $(1-c)W(x)$ for all
  large $x$.
- **S5.** The reversed pairs of Lemma 5.1 constrain nondecreasing sets,
  whose totients may repeat; a strict set $A\subseteq\{1,\ldots,N\}$ has
  pairwise distinct totients, hence $|A|\le W(N)$ by the elementary
  injectivity argument, which the section attributes to the folder index
  and this review re-derives.
- **S6.** Clause (i) is, for each $N$, an exact question about a finite
  set, and none of the page's mechanisms addresses it: the collision bounds
  (T1) and (T3), the convenient-integer lemma (L4) and Ford's order (F) are
  asymptotic, with unspecified thresholds and constants.
- **S7.** "The folder index maps the three clauses" is a pointer, not a
  claim; the index is outside the read set.

## Checklist

- **Quantifiers and scope.** Pass, with two notes. The constant in
  $M^\uparrow(x)\le(1-c)W(x)$ is existential and eventual ("for some $c>0$
  and all large $x$", the source's own form on manuscript p. 10); the
  reconstruction states it as $(1-c+o(1))W(x)$ with $c$ the Lemma 5.1
  constant, equivalently $(1-c')W(x)$ for every fixed $c'<c$ and large $x$,
  and the section binds the letter $c$ to nothing else, so no constant is
  changed. The clause (i) paraphrase omits the range of $N$: at $N=1$ the
  set $\{1\}$ is a strict example of size $1>\pi(1)=0$, so the clause is
  false there and must be read for $N\ge2$ (Finding F2). "A largest" is the
  only tenable reading of the statement's "the largest possible": at $N=3$
  both $\{2,3\}$ and $\{1,3\}$ are strict sets of size $2=\pi(3)$, so the
  primes are not the unique largest set.
- **Circularity.** Pass. The section proves negative statements about its
  own inputs and assumes nothing about clause (i).
- **Model and convention changes.** Pass. Tao's $M(x)$ is the largest
  cardinality of a subset of $\{n\in\mathbb N:n\le x\}$ on which $\varphi$
  is nondecreasing (published p. 793), the object the manuscript's p. 1
  calls $M^\uparrow(x)$; the strict maximum satisfies
  $M_<(N)\le M^\uparrow(N)$ because a strictly increasing set is
  nondecreasing. No other transfer between conventions is used.
- **Finite and statistical overreach.** Pass. The section uses no finite
  evidence. The reviewer's exact count below is reported as a consistency
  check on the framing, not as evidence for clause (i).
- **Uniformity.** Pass. The limit in S3 is in $x$ alone with absolute
  constants; Tao's $O$-constant is absolute and his bound holds for every
  $x\ge10$; Lemma 5.1's bound is uniform in $S$, as its page states.
- **Extremal conclusions.** Pass. The section asserts no extremum. Clause
  (i) is extremal; the reviewer checked it in its own units (cardinalities)
  for $2\le N\le10^7$, where the maximum equals $\pi(N)$ exactly.
- **Consequences and composition.** Pass with Finding F1. The section gives
  three reasons for S2. Reason one (S3 with S4) and reason three (S6) each
  establish S2 on their own. Reason two (S5) draws a contrast that inverts
  the reconstruction's division of labor: Lemma 5.1 applies to strict sets
  and improves the elementary bound by a constant factor, while repeated
  values are handled by the collision bounds. The conclusion is unaffected.
- **Computation.** Inapplicable to the section, which runs none and does
  not consume (P). The reviewer's own computation is described under
  Strongest attack with its method and coverage.
- **Reproduction.** Inapplicable: the section carries no rerun instructions
  or coverage claims.
- **Source and verdict fidelity.** Pass with Finding F1. Tao's Theorem 1.1
  was checked on the page image of published p. 794: exponent $5$, range
  $x\ge10$, weak maximum, and the derivation of the $\pi(x)$ form from the
  prime number theorem. The manuscript's Theorem 1.2 (p. 2), Lemma 5.1
  (p. 9) and the p. 10 proof match the reconstruction pages. The
  characterization of Tao's result as a rate that supersedes the
  reconstructed bound is faithful; the characterization of Lemma 5.1's role
  is not (F1).

## Weakest steps

**W1: the factor tending to infinity (S3).** Three inputs. (a) A lower
bound $W(x)\ge c_1Z(x)$ for large $x$ with $c_1>0$: this is (C) on the
Theorem 1.2 page, and manuscript p. 7 indeed quotes Ford for
$V(x)\asymp W(x)\asymp Z(x)$; independently of that quotation, Step 1 of
the Lemma 5.1 reconstruction exhibits $\#\mathcal A\ge c_DZ(x)$ pairwise
distinct totients $d_1\varphi(n)=\varphi(n_1n)$ with $n_1n\le x$, so
$W(x)\ge c_DZ(x)$ for $x\ge x_0(D)$ follows from Lemma 4.1 alone. (b)
$Z(x)/(x/\log x)=e^{E(x)}$ with
$E(x)=C(\log_3x-\log_4x)^2+C'\log_3x-(C'+\tfrac12-2C)\log_4x$; since
$C>0$, $\log_3x-\log_4x\to\infty$ and the two linear terms are
$O(\log_3x)$, $E(x)\to\infty$. (c) $\pi(x)\le2x/\log x$ for $x\ge2$, a
Chebyshev bound; the held Tao paper's display (1.1), p. 794, gives the
sharper $\pi(x)=(1+O(1/\log x))x/\log x$ from the prime number theorem.
Composing, for large $x$,

$$
\frac{(1-c)W(x)}{\pi(x)}\ \ge\ \frac{(1-c)c_1}{2}\,e^{E(x)}\ \to\ \infty ,
$$

where $1-c>0$ because $\pi(x)\le M^\uparrow(x)\le(1-c)W(x)$ forces it.
The step holds.

**W2: Tao's rate supersedes the bound (S4).** The two bounds concern the same
function (checklist, Model and convention changes). With $C_T$ the
absolute constant in Tao's Theorem 1.1, for all large $x$,
$(1+C_T(\log_2x)^5/\log x)\pi(x)\le2\pi(x)\le4x/\log x<(1-c)W(x)$ by (b)
and (a) of W1. So Tao's bound is strictly below the reconstructed bound for
all large $x$, holds at every $x\ge10$ where the reconstructed bound holds
only for $x\ge x_0$ with $x_0$ unspecified, and Tao's own p. 794 places
$M(x)\le(1-c+o(1))W(x)$ as the prior upper bound it improves. For the
problem's strict clause (ii), $M_<(N)\le M^\uparrow(N)$ carries the rate
across, which is the strict-transfer page. The step holds.

**W3: the elementary strict bound and the role of the reversed pairs
(S5).** If $\varphi$ is strictly increasing on $A\subseteq\{1,\ldots,N\}$,
then $\varphi$ is injective on $A$ and $\varphi(A)\subseteq\mathcal W(N)$,
so $|A|=\#\varphi(A)\le W(N)$; this is the elementary reason, re-derived
without the folder index. It also settles clause (iii) from the shared
input (F) alone: $W(N)\le V(N)\le C_1Z(N)$ and, since $E(N)=O((\log_3N)^2)$
is $o(\log_2N)$, $Z(N)=N/(\log N)^{1+o(1)}=o(N)$. The reversed pairs,
however, do not stop at nondecreasing sets with repeats: Lemma 5.1's
hypothesis is only that $\varphi$ is nondecreasing on $S\subseteq[1,x]$,
which every strict set satisfies, and its conclusion
$\#(\mathcal W(x)\setminus\varphi(S))\ge cW(x)$ gives, for strict $A$ and
$N\ge x_0$,

$$
|A|=\#\varphi(A)\le(1-c)W(N),
$$

a constant-factor improvement on the elementary bound. In the Theorem 1.2
reconstruction the indices with repeated values ($I_2$) are bounded by the
collision bounds (B), and the reversed pairs (A) bound the distinct-value
indices ($I_3$); the source's p. 10 proof has the same division. So the
contrast drawn in S5 is inverted, though its conclusion for clause (i) is
right for the reason in W1: both $W(N)$ and $(1-c)W(N)$ exceed $\pi(N)$ by
a factor tending to infinity.

## Strongest attack

**S1.** The attack was a disproof of the framing: a counterexample to
clause (i) at some $N$ would make the section's "one open clause" wrong.
The maximum size of a strict set in $\{1,\ldots,N\}$ equals the length of
the longest strictly increasing subsequence of $\varphi(1),\ldots,\varphi(N)$,
since a strict set is exactly an index-increasing subsequence with strictly
increasing values. The reviewer computed $\varphi$ by a sieve up to $10^7$
and that length for every prefix $N$ by patience sorting, against a running
prime count: the two agree for every $2\le N\le10^7$ (the first twelve
values $1,1,2,2,3,3,4,4,4,4,5,5$ were confirmed by hand), and disagree
only at $N=1$, where the length is $1$ and $\pi(1)=0$. The attack failed
except at the trivial boundary, which yields Finding F2. This computation
is reviewer-recorded and not filed as evidence. Whether clause (i) is open
in the literature cannot be certified from the read set; what the read set
shows is that the manuscript's p. 2 asks even the weaker weak-maximum
question (whether $M^\uparrow(x)-\pi(x)\to\infty$) as open, that Tao's
Theorem 1.1 is a rate and not an exact bound, and that the Tao card's lead
disclaims exact strict extremality.

**S2 and S6.** The attack was to build a transfer from the page's inputs.
Lemma 5.1 applied to strict sets gives $|A|\le(1-c)W(N)$, of order
$Z(N)$, which exceeds $\pi(N)$ by a factor tending to infinity (W1). The
collision bounds count solutions of $\varphi(n)=\varphi(n+k)$, that is,
repeated values, which a strict set cannot contain, so they constrain
nothing about strict sets beyond what the reversed pairs already give. The
convenient-integer lemma and Ford's order produce totients, of order
$Z(x)\gg\pi(x)$, in the wrong direction for an upper bound of order
$\pi(N)$. The explicit pair (P) forbids a strict set from holding
preimages of both $d_1$ and $d_2$, which the primes respect (all eight
preimages of $d_1$ are even; $d_2+1$ is prime), so it neither bounds nor
enlarges a strict set. No input is exact: (T1) holds for $x>x_0$ with
$x_0$ unspecified, (T3) carries $o(1)$, (L4) carries $c_D$ and $x_0(D)$,
(F) carries $O(1)$. Every proposition on the page is deduced from these
inputs (page Standing paragraph), so no result on the page can decide an
exact inequality at any specific $N$, and none is of order $\pi(N)$ even
eventually. The attack failed. A supporting derivation, the reviewer's own
from Tao's Proposition 4.1 on published p. 811 read in strict form: if $p$
is a prime with no prime in $((p-1)^2,p^2)$, then for $N\ge p^2$ the set
of primes up to $N$ together with $p^2$ is strictly increasing under
$\varphi$, because a prime $q<p^2$ has $q<(p-1)^2$ (the latter is not
prime) and so $\varphi(q)=q-1<p^2-2p<p^2-p=\varphi(p^2)$, while a prime
$q>p^2$ has $\varphi(q)=q-1\ge p^2>\varphi(p^2)$; hence
$M_<(N)\ge\pi(N)+1$. So clause (i) at $N$ implies Legendre's conjecture at
every prime $p\le\sqrt N$, which the source records as open even for large
arguments and even restricted to primes. Any unconditional transfer to
clause (i) for all large $N$ would therefore settle that conjecture at all
large primes; nothing on the page concerns prime gaps.

**S3 and S4.** The attack was on the order of $W$: if $W(x)$ were only of
order $x/\log x$, the factor would be bounded and Tao's bound would not
supersede. Both the source's quotation of Ford and, inside the premises,
Lemma 4.1 through Step 1 of Lemma 5.1 give $W(x)\gg Z(x)$, and
$Z(x)\log x/x\to\infty$ because $C>0$ (W1). A second attack was a mismatch
of objects between Tao's $M(x)$ and $M^\uparrow(x)$, or a range gap; both
were excluded on the page images (checklist). The attacks failed.

**S5.** The attack succeeded against the sentence's mechanism description
and failed against its conclusion (W3): Lemma 5.1 does constrain strict
sets, by the factor $1-c$, and the repeated values are the collision
bounds' business. This is Finding F1.

## Premises

- **Theorem 1.2 reconstruction** (author-recorded; read in full).
  Interface: absolute $c>0$ and $x_0$ with $M^\uparrow(x)\le(1-c)W(x)$ for
  $x\ge x_0$; its input (C), $W(x)\asymp Z(x)$, quoted from manuscript
  p. 7 and confirmed there on the text layer; its input (D), Erdős's
  $W(x)=x/(\log x)^{1+o(1)}$, not needed here since (F) gives $W(N)=o(N)$.
  Source: Pollack, Pomerance and Treviño, author manuscript, Theorem 1.2
  p. 2, proof p. 10; held; p. 2 on the text layer, p. 10 on the page
  image.
- **Lemma 5.1 reconstruction** (author-recorded; read in full). Interface:
  absolute $c>0$, $x_0$; for $x\ge x_0$ and every $S\subseteq[1,x]$ with
  $\varphi$ nondecreasing on $S$,
  $\#(\mathcal W(x)\setminus\varphi(S))\ge cW(x)$.
  Used here for strict $S$, which satisfy the hypothesis. Its Step 1 also
  gives $W(x)\ge c_DZ(x)$. Source: manuscript p. 9; held; text layer.
- **Lemma 4.1, Theorem 3.1, Theorem 3.3, Lemma 3.2 reconstructions**
  (Statement sections only): consumed only through the two pages above;
  interfaces as the page's (L4), (T1), (T3) record them. Lemma 4.1 and
  Theorem 3.1 are partial reconstructions, which the section inherits by
  citation and does not strengthen.
- **(F) Ford's Theorem 1**: $V(x)=Z(x)e^{O(1)}$ for large $x$, from the
  Ford (1998) card lead; PDF held, not reread. Used for $W\le V\ll Z$ and
  $W(N)=o(N)$.
- **Tao's Theorem 1.1**: for all $x\ge10$,
  $M(x)\le(1+O((\log_2x)^5/\log x))\,x/\log x$, hence
  $\pi(x)\le M(x)\le(1+O((\log_2x)^5/\log x))\pi(x)$, $M$ the weak
  maximum over $\{n\in\mathbb N:n\le x\}$. Source: published version,
  p. 794; held; page image. Its (1.1) supplies the prime number theorem
  form of $\pi(x)$ used in W1. Its Proposition 4.1, p. 811, text layer,
  underlies the reviewer's Legendre derivation.
- **Strict transfer** (library compilation page): $M_<(N)\le M^\uparrow(N)$
  and $\pi(N)\le M_<(N)$; re-derived in one line each.
- **Chebyshev's bound** $\pi(x)\le2x/\log x$: classical, external to the
  read set, and replaceable by Tao's (1.1) above.
- **Problem 49 statement**: the three clauses as restated in S1.

## Findings

- **F1 (suggested).** Location, lines 632--635: "the reversed pairs of
  Lemma 5.1 constrain sets whose totients may repeat, while a strict set
  already has distinct totients and is bounded by $W(x)$ for the
  elementary reason on the folder index". Defect: the contrast assigns the
  reversed pairs to sets with repeated totients and implies they add
  nothing for strict sets; in fact Lemma 5.1's only hypothesis is that
  $\varphi$ is nondecreasing on $S$, which every strict set satisfies, and
  in the Theorem 1.2 reconstruction the repeated values ($I_2$) are bounded
  by the collision bounds while the reversed pairs bound the distinct
  values ($I_3$). Witness: for strict $A\subseteq\{1,\ldots,N\}$ and
  $N\ge x_0$, Lemma 5.1 gives $|A|=\#\varphi(A)\le(1-c)W(N)$, strictly
  below the elementary $W(N)$. Proposed replacement: "the reversed pairs of
  Lemma 5.1 apply to strict sets too and give $|A|\le(1-c)W(N)$, a
  constant factor below the elementary bound $|A|\le W(N)$ that distinct
  totients give directly, while the collision bounds of Theorems 3.1 and
  3.3 only count repeated values, which a strict set lacks; both bounds
  exceed $\pi(N)$ by a factor tending to infinity". The section's
  conclusion is unchanged.
- **F2 (note).** Location, lines 628--630: "whether the primes are a
  largest subset of $\{1,\ldots,N\}$ with strictly increasing totients".
  The range of $N$ is unstated; at $N=1$ the clause fails ($\{1\}$ has
  size $1>\pi(1)=0$), and the reviewer's exact count gives equality with
  $\pi(N)$ for every $2\le N\le10^7$. Proposed replacement: add "for every
  $N\ge2$". The indefinite article is right: uniqueness fails already at
  $N=3$.
- **F3 (note).** Location, line 632: "Tao's rate" is invoked without a
  link or locator, and lines 634--635 refer the elementary reason to the
  folder index. Proposed replacement: link Tao's Theorem 1.1 and the strict
  transfer as the Theorem 1.2 reconstruction does, and state the one-line
  reason ($\varphi$ is injective on a strict set) in place, so the section
  stands without the index.

## Verdict

- **S1** (clause identification): refutation-failed. The paraphrase of
  clause (i) is faithful to the statement under its only tenable reading,
  modulo the $N\ge2$ range (F2); clauses (ii) and (iii) are settled by the
  held statements (Tao's Theorem 1.1 with the strict transfer; the
  injectivity bound with (F)). Whether clause (i) is open is not certified
  by this review, which ran no literature search; no held source in the
  read set settles it and the exact count to $10^7$ found no counterexample.
- **S2** (nothing on the page bears on clause (i); the lead's "nothing
  transfers"): refutation-failed. Checked against every shared input and
  the section's own argument; the other sections were not read, and their
  propositions are covered by the Standing paragraph's statement that all
  are deduced from those inputs.
- **S3** (the reconstructed bound exceeds $\pi(x)$ by a factor tending to
  infinity): refutation-failed.
- **S4** (superseded by Tao's rate): refutation-failed.
- **S5** (the reversed pairs constrain nondecreasing sets; a strict set is
  bounded by $W(N)$ elementarily): refutation-failed for each literal
  clause and for the conclusion drawn; the mechanism description between
  them is inverted (F1, suggested).
- **S6** (exact finite question, unaddressed by the asymptotic
  mechanisms): refutation-failed.
- **S7** (the folder index maps the three clauses): not a claim.

Limitations: the folder index and the other sections were outside the read
set, so "the elementary reason on the folder index" was re-derived rather
than compared; Lemma 4.1 and Theorem 3.1 stand as partial reconstructions,
and the section inherits that standing through the two results it cites;
the openness of clause (i) rests on the held sources and the reviewer's
finite check, not on a dated search. This focused review assigns no tier
and changes no status.
