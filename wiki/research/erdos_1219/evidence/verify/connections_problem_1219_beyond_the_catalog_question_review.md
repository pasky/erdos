---
name: research/erdos_1219/evidence/verify/connections_problem_1219_beyond_the_catalog_question_review
title: "Independent review of the connections section: Problem 1219 beyond the catalog question"
desc: |
  Refutation review of the section's dividing line for Σ_{μ<λ} 2^μ → (λ)^2_2
  at singular λ and its consequences: the characterization, its weakly
  compact reformulation and the ℵ_{ω_1} instance survive (refutation-failed);
  the inference about the site's "no for κ > ω" bullet is refuted-as-stated,
  as is the sentence that (T3) needs the non-constancy hypothesis; one
  required correction, two suggested, two notes.
created: 2026-09-28T19:12:06Z
updated: 2026-09-28T20:42:32Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, commissioned for
refutation. The reviewer took no part in writing the page, its reconstruction
pages, or any evidence under the folder, and received only the assignment
and the read set below; no author explanation, sibling verdict, grade, or
standing text was supplied or read.

**Subject.** Page `wiki/research/erdos_1219/connections.md` as it stood at
2026-09-28T13:50:48Z, section "## Problem 1219 beyond the catalog question",
lines 109--169 (the H2 at line 109; the next H2, "Problem 1220", at line 171).
Its paragraphs: Target (line 111), What transfers (line 119), Falsification
checks (line 158), Outcome (line 167). No separate lead page is named; the
section targets [[problems/set_theory/E1219/_index|Problem 1219]].

**Read, and at what depth.**

- The section: every sentence, each deduction re-derived.
- The page's frontmatter, Scope paragraph and Tools section as inputs.
  The interfaces of (T1)--(T3) were confirmed at each use; (T3)'s proof was
  re-derived in full because the section rests on it, and one observation
  about it is recorded under Findings for the Tools reviewer.
- The three reconstruction pages as of the same time as premises, read in full:
  [[research/erdos_1219/theorem_1_2_reconstruction|Theorem 1.2]] (statement,
  definitions, sum formula, imported results (ER) and (S), Step 1 and Step
  2(d)), [[research/erdos_1219/lemma_1_1_reconstruction|Lemma 1.1]] (interface
  only), and
  [[research/erdos_1219/corollary_1_3_reconstruction|Corollary 1.3]] (the
  identification of the catalog's sum with the sum over all $n$).
- `wiki/problems/set_theory/E1219/_index.md`, lines 1--25 only: frontmatter, the
  Statement paragraph and the Status line. Current assessment, Progress,
  Known Results and Linked library material were not read.
- The library card
  [[../library/set_theory/shelah_1975_notes_partition_calculus/_index|Shelah (1975)]],
  its result page
  [[../library/set_theory/shelah_1975_notes_partition_calculus/theorem_1_2|theorem_1_2]],
  the card
  [[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|Komjáth (2025)]],
  and PDF p. 4 (printed p. 1260) of the held Shelah scan as a page image:
  the printed statement of Theorem 1.2, Corollary 1.3 and the Remark after
  it were checked clause by clause.
- `docs/verification.md` (Report contract, Grading and claim standing,
  Audit checklist, and the Erdos-specific Whole-claim report and Audit
  checklist), `docs/approach_vetting.md`, `docs/evidence.md` "Source
  fidelity", `docs/math_authoring.md`.

**Exposure.** Two library cards and one result page were read in full
rather than only their provenance paragraphs and Statement sections: the
Shelah card's Contents, Compiled scope and Bears-on paragraphs (which carry
read-status and acceptance wording), the Komjáth card's Bears-on and results
list, and the result page's Proof pointer, Dependencies, Read depth and
Bears-on sections. Nothing there was used beyond the statement of
Theorem 1.2 and the card's provenance. The file names under
`wiki/research/erdos_1219/evidence/verify/` were listed (names only; no
review or grade was opened). No Current assessment, Known Results, standing
prose, review, grade, or web search reached the reviewer. The section's
account of what the problem page's Known Results say could therefore not be
checked against that page; where a finding depends on it, the dependence is
stated.

## Restatement

Throughout, $\lambda$ is a cardinal, $\kappa=\operatorname{cf}\lambda$,
$\chi=\sum_{\mu<\lambda}2^\mu$ is the cardinal sum over all cardinals
$\mu<\lambda$ (finite ones included), $\theta\to(\rho)^2_2$ means that every
two-coloring of the pairs of a set of size $\theta$ has a homogeneous set of
size $\rho$, and the sequence $\langle2^\mu:\mu<\lambda\rangle$ is *not
eventually constant* when for every cardinal $\nu<\lambda$ there is a
cardinal $\mu$ with $\nu<\mu<\lambda$ and $2^\mu>2^\nu$, and *eventually
$\ge\lambda$* when some $\mu_0<\lambda$ has $2^\mu\ge\lambda$ for all
cardinals $\mu$ with $\mu_0\le\mu<\lambda$ (the theorem page's conventions,
adopted by the section).

- **S0 (Target).** Problem 1219 has status proved; its assessment rests on
  Corollary 1.3 with Komjáth's survey as the acceptance record; its Known
  Results record, from the site, that with $\aleph_\kappa$ in place of
  $\aleph_\omega$ the answer is yes for $\kappa<\omega$ and no for
  $\kappa>\omega$; Hajnal's Conjecture 1A is a separate open question.
  Administrative; only the status is inside the read set.
- **S1 (the dividing line).** For every singular cardinal $\lambda$:
  $\chi\to(\lambda)^2_2$ holds if and only if all three of (a) there is a
  cardinal $\mu<\lambda$ with $2^\mu\ge\lambda$; (b)
  $\langle2^\mu:\mu<\lambda\rangle$ is not eventually constant; (c)
  $\kappa\to(\kappa)^2_2$. Proof offered: right to left is Theorem 1.2 with
  (a) read as "eventually $\ge\lambda$"; left to right by three cases: if (a)
  fails then $\chi=\lambda$ and $\lambda\not\to(\lambda)^2_2$ by the block
  coloring; if the powers are eventually constant with value
  $2^{\mu_0}\ge\lambda$ then $\chi=2^{\mu_0}$ and Sierpiński's
  $2^{\mu_0}\not\to(\mu_0^+)^2_2$ with $\mu_0^+\le\lambda$ applies; if (a)
  and (b) hold and (c) fails then (T3) applies.
- **S2 (reformulation).** Condition (c) holds exactly when $\kappa=\omega$
  or $\kappa$ is weakly compact, because an uncountable regular $\kappa$
  satisfies $\kappa\to(\kappa)^2_2$ exactly when it is weakly compact.
- **S3 (instance).** In ZFC, whatever the powers are,
  $\sum_{\mu<\aleph_{\omega_1}}2^\mu\not\to(\aleph_{\omega_1})^2_2$.
- **S4 (instance).** For $\lambda=\aleph_{\omega+\omega}$:
  $\sum_{\mu<\lambda}2^\mu\to(\lambda)^2_2$ holds exactly when the sequence
  $\langle2^{\aleph_{\omega+n}}:n<\omega\rangle$ is "unbounded below
  $\chi$" (read: every term is below $\chi$ and the terms are cofinal in
  $\chi$, that is, the sequence is not eventually constant) and the terms
  "exceed $\lambda$" (read, under the section's own convention, as
  eventually: some term is above $\lambda$; see F1 for the other reading).
- **S5 (the site's bullet).** Because of S4, the site's "no for
  $\kappa>\omega$" cannot be read as a statement about every $\kappa>\omega$
  in the form the catalog prints the problem, and [ErHa71], p. 20 (not
  held) should be read before that bullet is sharpened.
- **S6 (necessity of a hypothesis).** (T3) needs the non-constancy
  hypothesis in order to place blocks of size $2^{\mu(i)}$ inside $\chi$
  with sum $\chi$.
- **S7 (coverage).** When the powers are eventually constant, Sierpiński's
  theorem alone gives $\chi\not\to(\lambda)^2_2$, so the case split of S1
  loses nothing.
- **S8 (comparison).** In (T3) the Sierpiński colorings act at
  $\mu(i)^+\le\lambda$, where they exclude homogeneous sets of size
  $\lambda$ inside a block; this is the only place where (T3)'s argument
  differs from (T2)'s.
- **S9 (regular case).** For regular $\lambda$ the relation
  $\chi\to(\lambda)^2_2$ reduces to "$\lambda$ is weakly compact"; the
  mechanism does not touch that case.
- **S10 (standing).** Everything in the section is author-recorded; (T3)
  and S1 are by-products; there is no lead, since Problem 1219 is proved
  and S1 has no open case.

## Checklist

- **Quantifiers and scope.** S1: the quantifiers are exact; "for a singular
  cardinal $\lambda$" is necessary (a weakly compact $\lambda$ satisfies the
  left side and fails (a)), and (a) is equivalent to "eventually
  $\ge\lambda$" by monotonicity. S4: "exceed $\lambda$" admits the reading
  "every $n$", under which the biconditional is false (F1). S5: fails, and
  the failure is one of scope: the sentence quantifies over the wrong sum
  (F2). S9: false at the boundary $\lambda=\omega$ (F4).
- **Circularity.** None. (T3) is proved from Sierpiński's theorem and a
  witness at $\kappa$, not from the negation of Theorem 1.2; the
  left-to-right direction of S1 never assumes the relation; the case split
  is exhaustive.
- **Model and convention changes.** The section keeps the theorem page's
  conventions. S5 substitutes the sum $\sum_{\mu<\aleph_\kappa}2^\mu$ for
  the catalog's sum $\sum_k2^{\aleph_{n_k}}$ over integers $n_k$ without a
  bridge; for $\kappa>\omega$ the two sums are different cardinals in
  general, and the conclusion changes with them (F2).
- **Finite and statistical overreach.** Inapplicable: no finite
  verification, sampling or heuristic is used.
- **Uniformity.** No constants. The ZFC claims (S3, and the ZFC negative
  result exhibited under F2) were checked to hold in every model, with the
  cardinal arithmetic they use (the sum formula, König's theorem)
  identified.
- **Extremal conclusions.** The suprema were checked in the section's own
  units: $\chi=\sup_{\mu<\lambda}2^\mu$ whenever the supremum is at least
  $\lambda$, which holds for every limit cardinal $\lambda$ because
  $2^\mu\ge\mu^+$; "not eventually constant" is exactly "the supremum is not
  attained", which is what S4's "unbounded below $\chi$" must mean.
- **Consequences and composition.** Each "so" and "in particular" was
  attacked separately. "In particular $\aleph_{\omega_1}$" follows (S3).
  "So the site's ... cannot be read" does not follow and is false under the
  catalog's form (F2). "So nothing is lost" holds, but the reason given for
  it ((T3) needs the hypothesis) is false (F3). The right-to-left direction
  of S1 consumes Theorem 1.2 within its hypotheses; the left-to-right
  direction consumes (T3) within its interface.
- **Computation.** Inapplicable; nothing is computed.
- **Reproduction.** Inapplicable; no rerun instructions or coverage claims.
- **Source and verdict fidelity.** The printed statement of Theorem 1.2 was
  checked on the page image: hypotheses $\kappa\to(\kappa)^2_2$,
  $\kappa=\operatorname{cf}\lambda$, "not eventually constant, but is
  eventually $\ge\kappa$", conclusion $\chi\to(\lambda)^2_2$ "(and in fact
  even $\chi\to(\lambda,\lambda,\omega)^2$)"; the section uses the result
  page's corrected bound $\ge\lambda$, which is the bound the printed proof
  uses ("$2^{\mu(i)}\ge\lambda$"). The Remark after Corollary 1.3, that
  "Theorem 2" completes the answer to when $\lambda\to(\mu)^2_2$ holds for
  infinite $\lambda,\mu$, is consistent with S1 being the completed answer
  at singular $\lambda$. Sierpiński's theorem, the weakly compact
  characterization, Erdős--Rado and Easton's theorem are not held; they are
  used at their standard statements. The section's quotation of the Known
  Results could not be checked (excluded); [ErHa71] is not held, as the
  section says.

## Weakest steps

**W1. The identification of $\chi$ in the three left-to-right cases.** Let
$I$ be the set of cardinals below $\lambda$; $I$ is infinite and
$|I|\le\lambda$. The sum formula gives $\chi=|I|\cdot\sup_{\mu<\lambda}2^\mu$.
Since $\lambda$ is a limit cardinal and $2^\mu\ge\mu^+$, the supremum is at
least $\sup_{\mu<\lambda}\mu^+=\lambda\ge|I|$, so $\chi=\sup_{\mu<\lambda}2^\mu$
in every case. If (a) fails, every $2^\mu<\lambda$, so the supremum is
exactly $\lambda$ and $\chi=\lambda$; the coloring of the pairs of
$\lambda=\bigsqcup_{i<\kappa}X_i$, $|X_i|<\lambda$, by "same piece or not"
has no homogeneous set of size $\lambda$ (one color confines the set to a
piece, the other to one point per piece, $\kappa<\lambda$ points), so
$\chi\not\to(\lambda)^2_2$. If the powers are eventually constant from
$\mu_0$ on, then $2^{\mu_0}=2^\mu\ge\mu^+$ for all $\mu_0\le\mu<\lambda$, so
$2^{\mu_0}\ge\lambda$ automatically, $\mu_0$ is infinite,
$\chi=2^{\mu_0}$, and Sierpiński's coloring of $[2^{\mu_0}]^2$ has no
homogeneous set of size $\mu_0^+\le\lambda$. The remaining case is (a) and
(b) with $\kappa\not\to(\kappa)^2_2$, which is (T3)'s interface. The three
cases exhaust the negation of "(a) and (b) and (c)", because the failure of
(b) forces (a). The composition with the right-to-left direction is exact:
(a) is "eventually $\ge\lambda$" by monotonicity, and Theorem 1.2 is stated
for infinite $\lambda$ with $\kappa=\operatorname{cf}\lambda$, so a singular
$\lambda$ satisfying (a), (b), (c) meets every hypothesis.

**W2. (T3), re-derived.** Let $\lambda$ be singular,
$\kappa=\operatorname{cf}\lambda$, and $c:[\kappa]^2\to2$ have no homogeneous
set of size $\kappa$. Choose cardinals $\mu(i)<\lambda$ ($i<\kappa$),
infinite, strictly increasing and cofinal in $\lambda$; this needs only
$\kappa=\operatorname{cf}\lambda<\lambda$, since $\sup_{j<i}\mu(j)<\lambda$
for $i<\kappa$. Then $\sum_{i<\kappa}2^{\mu(i)}=\kappa\cdot\sup_i2^{\mu(i)}$,
and $\sup_i2^{\mu(i)}=\sup_{\mu<\lambda}2^\mu=\chi\ge\lambda>\kappa$ by
cofinality and monotonicity and W1; so $\chi$ is the disjoint union of sets
$X_i$ with $|X_i|=2^{\mu(i)}$. Color pairs inside $X_i$ by a Sierpiński
coloring $e_i$ with no homogeneous set of size $\mu(i)^+$, and pairs across
blocks $i\ne j$ by $c(\{i,j\})$. If $H$ is homogeneous in color $\nu$ with
$|H|=\lambda$, then $|H\cap X_i|\le\mu(i)<\lambda$ for every $i$, so the set
$J$ of blocks met by $H$ has size $\kappa$: otherwise $J\subseteq i_0$ for
some $i_0<\kappa$ and $H$ is a union of fewer than $\operatorname{cf}\lambda$
sets of size below $\lambda$. One point of $H$ from each block in $J$ makes
$J$ a $c$-homogeneous set of size $\kappa$, a contradiction. Hence
$\chi\not\to(\lambda)^2_2$. The strict increase of the powers $2^{\mu(i)}$
is used nowhere; see F3.

**W3. From S4 to S5.** S4 concerns $\sum_{\mu<\aleph_{\omega+\omega}}2^\mu$,
whose terms include the powers $2^{\aleph_{\omega+n}}$. The catalog prints
Problem 1219 as: $(n_k)$ an increasing sequence of integers with
$2^{\aleph_{n_k}}$ strictly increasing and $2^{\aleph_{n_0}}>\aleph_\omega$;
is $\sum_k2^{\aleph_{n_k}}\to(\aleph_\omega)^2$? Putting $\aleph_\kappa$ in
place of $\aleph_\omega$ in that form changes the hypothesis to
$2^{\aleph_{n_0}}>\aleph_\kappa$ and the target to $(\aleph_\kappa)^2$; the
sum stays $\sum_k2^{\aleph_{n_k}}$ with integer indices. For $\kappa>\omega$
this sum and S4's sum are different cardinals in general, and S4 says
nothing about the first. The step "so" therefore has no bridge, and the
strongest attack below shows that its conclusion is false for the sum the
catalog's form names.

## Strongest attack

**S1.** Attempted to build a singular $\lambda$ with (a), (b), (c) and
$\chi\not\to(\lambda)^2_2$, or with one condition failing and
$\chi\to(\lambda)^2_2$. The first is excluded by Theorem 1.2 (premise; its
hypotheses are exactly (a)--(c) at singular $\lambda$). For the second, the
case analysis of W1 is exhaustive; each case was re-derived, including the
degenerate ones: a finite threshold $\mu_0$ is impossible because
$2^{\mu_0}\ge\lambda$; $2^\mu=\lambda$ with equality is possible for
$\mu<\operatorname{cf}\lambda$ (for instance
$2^{\aleph_0}=\aleph_{\omega_1}$ is consistent, $\aleph_{\omega_1}$ having
uncountable cofinality), and then (a) holds with equality and the case
split still decides the relation. No counterexample found.

**S2.** Attacked the boundary: $\kappa=\operatorname{cf}\lambda$ is regular;
for $\kappa=\omega$, (c) is Ramsey's theorem; for uncountable $\kappa$, "weakly
compact" is by its standard definition an uncountable $\kappa$ with
$\kappa\to(\kappa)^2_2$, and such a $\kappa$ is regular (a decomposition into
$\operatorname{cf}\kappa<\kappa$ pieces of size below $\kappa$, colored as in
W1, would have no homogeneous set of size $\kappa$). No defect.

**S3.** $\operatorname{cf}\aleph_{\omega_1}=\omega_1$, and
$\omega_1\not\to(\omega_1)^2_2$ in ZFC by restricting Sierpiński's coloring
of $[2^{\aleph_0}]^2$ to $\aleph_1\le2^{\aleph_0}$ points. Every case of W1
then yields the negative relation whatever the powers are: (a) failing,
eventual constancy, or (T3). No defect.

**S4.** Attacked the two quantifier readings of "exceed $\lambda$". Under
"some term" the sentence is S1 at $\lambda=\aleph_{\omega+\omega}$: (c) is
Ramsey; (b) is equivalent to the non-constancy of the tail
$\langle2^{\aleph_{\omega+n}}\rangle$ because that tail is cofinal; (a) is
equivalent to "some $2^{\aleph_{\omega+n}}\ge\lambda$", since
$2^{\aleph_n}\le2^{\aleph_{\omega+n}}$; and "$\ge\lambda$" is "$>\lambda$"
because $\operatorname{cf}(2^\mu)>\mu\ge\aleph_0=\operatorname{cf}\lambda$ by
König's theorem. Under "every term" the sentence is false: in the Easton
extension of a GCH ground with $2^{\aleph_n}=\aleph_{n+1}$,
$2^{\aleph_{\omega+n}}=\aleph_{\omega+\omega+n+1}$ for $n\ge1$, and hence
$2^{\aleph_\omega}=\aleph_{\omega+1}$ (the forcing is
$\aleph_{\omega+1}$-closed, since every factor sits above $\aleph_\omega$, so
it adds no subset of $\aleph_\omega$), the relation holds by S1 while
$2^{\aleph_\omega}<\lambda$. The section's own convention
supports the first reading, so the statement survives with F1 filed.

**S5.** Succeeded. Let $(n_k)_{k<\omega}$ be any sequence of integers with
$2^{\aleph_{n_k}}$ strictly increasing, and
$\chi'=\sum_{k<\omega}2^{\aleph_{n_k}}=\sup_k2^{\aleph_{n_k}}$ (sum formula;
the terms exceed $\aleph_0$). Write $\chi'=\bigsqcup_{k<\omega}X_k$ with
$|X_k|=2^{\aleph_{n_k}}$. Color the pairs inside $X_k$ by a Sierpiński
coloring $e_k$ of $[X_k]^2$ with no homogeneous set of size
$\aleph_{n_k+1}$, and every pair across two blocks with $0$. Let $H$ be
homogeneous with $|H|=\aleph_{\omega+1}$. If its color is $1$, all its pairs
lie inside one block, so $|H|\le\aleph_{n_k}$ for that $k$. If its color is
$0$, each $H\cap X_k$ is $e_k$-homogeneous, so $|H\cap X_k|\le\aleph_{n_k}$
and $|H|\le\sum_{k<\omega}\aleph_{n_k}\le\aleph_\omega$. Both contradict
$|H|=\aleph_{\omega+1}$. Hence, in ZFC,
$\sum_k2^{\aleph_{n_k}}\not\to(\aleph_{\omega+1})^2_2$, and so
$\sum_k2^{\aleph_{n_k}}\not\to(\aleph_\kappa)^2_2$ for every ordinal
$\kappa>\omega$, whatever the powers and whatever the hypothesis on
$2^{\aleph_{n_0}}$. So in the form the catalog prints the problem, with
$\aleph_\kappa$ in place of $\aleph_\omega$, the bullet "no for
$\kappa>\omega$" is a correct statement about every $\kappa>\omega$, and
S5's sentence is false. The same form also explains the bullet's "yes for
$\kappa<\omega$", which has no meaning for a sum re-indexed below a finite
$\kappa$: for $k\ge\kappa$,
$\chi'\ge(2^{\aleph_{n_k}})^+\ge(2^{\aleph_k})^+\to(\aleph_{k+1})^2_2$ by
Erdős--Rado ((ER) on the theorem page, first alternative shrunk), and
$\aleph_{k+1}>\aleph_\kappa$. The trichotomy yes below $\omega$, Problem 3
at $\omega$, no above $\omega$ is therefore the literal one. This finding
assumes only that the section quotes the bullet's wording correctly
("with $\aleph_\kappa$ in place of $\aleph_\omega$"); the excluded Known
Results were not read. Under the section's other possible intention, the
re-indexed sum $\sum_{\mu<\aleph_\kappa}2^\mu$, the sentence would need a
consistency witness that it does not give (the Easton model under S4
serves); either way the sentence cannot stand as printed.

**S6.** Succeeded: W2 places blocks of size $2^{\mu(i)}$ with sum $\chi$
from any strictly increasing cofinal $\langle\mu(i)\rangle$, by the sum
formula alone, and uses nothing about the strict increase of the powers. So
(T3) holds for every singular $\lambda$ with
$\operatorname{cf}\lambda\not\to(\operatorname{cf}\lambda)^2_2$, and the
non-constancy hypothesis is superfluous rather than needed.

**S7.** Attacked the possibility of an eventually constant sequence with
constant value below $\lambda$, which Sierpiński's theorem would not cover:
impossible, since the constant value is at least $\mu^+$ for every
$\mu<\lambda$ (W1). No defect.

**S8.** Attacked the claim that excluding homogeneous sets of size $\lambda$
inside a block is all (T3) uses: it is, because $|H\cap X_i|<\lambda$ for
every $i$ already makes a union over fewer than $\operatorname{cf}\lambda$
blocks smaller than $\lambda$ (the standard fact on the theorem page); the
sharper bound $|H\cap X_i|\le\mu(i)$ in (T3)'s proof is not needed. The
remaining difference from (T2), block sizes $2^{\mu(i)}$ that may reach
$\lambda$, is the reason the Sierpiński colorings are needed at all, which
the sentence describes fairly. No defect.

**S9.** Attacked the boundary. For $\lambda=\omega$,
$\sum_{n<\omega}2^n=\aleph_0\to(\aleph_0)^2_2$ by Ramsey's theorem, while
$\omega$ is not weakly compact under the standard convention that weakly
compact cardinals are uncountable; the sentence is false there. For
uncountable regular $\lambda$ it was verified: a successor $\mu^+$ has
$\chi=2^\mu\not\to(\mu^+)^2_2$; a weakly compact $\lambda$ is strongly
inaccessible, so $\chi=\lambda\to(\lambda)^2_2$; a regular limit $\lambda$
that is not weakly compact has $\lambda\not\to(\lambda)^2_2$, and then
either $\chi=\lambda$, or the powers are eventually constant with value at
least $\lambda$ and Sierpiński applies, or they are not and W2 applies with
$\kappa=\lambda$ (its choice of the $\mu(i)$ needs only that $\lambda$ is a
limit cardinal). Filed as F4.

**S10.** The standing sentences claim author-recorded standing only, call
(T3) and S1 by-products, and record no lead; nothing reads as more than
author-recorded. No defect.

## Premises

- **Theorem 1.2** (reconstruction page, premise at author-recorded standing
  reviewed as of 2026-09-28T05:03:27Z with corrections applied since).
  Interface: $\lambda$ infinite, $\kappa=\operatorname{cf}\lambda$,
  $\kappa\to(\kappa)^2_2$, $\langle2^\mu:\mu<\lambda\rangle$ not eventually
  constant and eventually $\ge\lambda$; conclusion $\chi\to(\lambda)^2_2$.
  Used once, in the right-to-left direction of S1, within its hypotheses.
  Source: Shelah (1975), Theorem 1.2, printed p. 1260, held; the printed
  statement was read on the page image, and the bound $\ge\lambda$ is the
  one the printed proof uses. Read depth: statement checked, reconstruction
  read in full; its proof is not re-verified here.
- **Lemma 1.1** (reconstruction page). Not consumed by the section except
  through Theorem 1.2; interface read only.
- **Corollary 1.3** (reconstruction page). Consumed only in the Target
  sentence; its fidelity section (the catalog's sum equals the sum over all
  $n$) was read because it fixes what "the form the catalog prints" is, and
  it bears on F2.
- **(T3)** (Tools section). Interface: $\lambda$ singular,
  $\kappa=\operatorname{cf}\lambda$, powers not eventually constant,
  $\kappa\not\to(\kappa)^2_2$; conclusion $\chi\not\to(\lambda)^2_2$.
  Re-derived in W2; the non-constancy hypothesis is superfluous.
- **Sum formula** (theorem page): for an infinite index set and terms at
  least $1$, the sum is the number of terms times their supremum.
  Re-derived.
- **Block coloring** $\lambda\not\to(\lambda)^2_2$ for singular $\lambda$
  (result page reading note). Re-derived in W1.
- **(S) Sierpiński (1933)**, not held: $2^\mu\not\to(\mu^+)^2_2$ for
  infinite $\mu$. Used at infinite $\mu$ throughout, as its statement
  requires.
- **Weakly compact characterization**, not held: standard definition, an
  uncountable $\kappa$ with $\kappa\to(\kappa)^2_2$; regularity derived in
  the attack on S2.
- **König's theorem**, not held: $\operatorname{cf}(2^\mu)>\mu$. Used only
  in this report, to justify "exceed" in S4.
- **Easton's theorem**, not held: used only in this report's witness for the
  strong reading of S4 and for the re-indexed reading of S5.
- **(ER) Erdős--Rado** as recorded on the theorem page, not held: used only
  in this report's remark on the bullet's "yes for $\kappa<\omega$".
- **Komjáth (2025)**: card read; the survey's p. 419 was not consulted, since
  the section's only reference to it is the excluded acceptance sentence.
- **[ErHa71]**, p. 20: not held, not read; the section says so.

## Findings

- **F1 (suggested).** Location: "the relation holds exactly when the powers
  $2^{\aleph_{\omega+n}}$ are unbounded below $\chi$ and exceed $\lambda$".
  Defect: the quantifier on "exceed $\lambda$" is unstated; read as "every
  $n$", the biconditional is false. Witness: the Easton model of the attack
  on S4, where $2^{\aleph_\omega}=\aleph_{\omega+1}<\lambda$ and the relation
  holds. Replacement: "the relation holds exactly when the sequence
  $\langle2^{\aleph_{\omega+n}}:n<\omega\rangle$ is not eventually constant
  and some $2^{\aleph_{\omega+n}}$ exceeds $\lambda$ (strictly, by König's
  theorem, since $\operatorname{cf}\lambda=\omega$)".
- **F2 (required).** Location: "so the site's 'no for $\kappa>\omega$'
  cannot be read as a statement about every $\kappa>\omega$ in the form the
  catalog prints it". Defect: the inference passes from S4, about
  $\sum_{\mu<\aleph_{\omega+\omega}}2^\mu$, to the catalog's form, whose
  sum $\sum_k2^{\aleph_{n_k}}$ has integer indices and is unchanged by the
  substitution; no bridge connects the two sums, and for that sum the
  bullet is a ZFC theorem for every $\kappa>\omega$. Witness: the coloring
  in the attack on S5 gives
  $\sum_k2^{\aleph_{n_k}}\not\to(\aleph_{\omega+1})^2_2$. Replacement: "In
  the catalog's form with $\aleph_\kappa$ in place of $\aleph_\omega$ the sum
  $\sum_k2^{\aleph_{n_k}}$ is unchanged, and the bullet is a ZFC theorem for
  every $\kappa>\omega$: the sum is $\sup_k2^{\aleph_{n_k}}$, and blocks of
  size $2^{\aleph_{n_k}}$ carrying Sierpiński colorings, with one color
  across blocks, admit no homogeneous set of size $\aleph_{\omega+1}$; the
  yes for $\kappa<\omega$ is Erdős--Rado. The characterization above
  concerns the different sum $\sum_{\mu<\aleph_\kappa}2^\mu$, for which the
  answer at $\kappa=\omega+\omega$ is yes under consistent cardinal
  arithmetic (Easton) and no in ZFC at $\kappa=\omega_1$." The
  recommendation to read [ErHa71], p. 20 can stay. If the section instead
  intends the re-indexed sum, it must say so and supply the consistency
  witness; the sentence cannot stand as printed under either intention.
- **F3 (suggested).** Location: "(T3) needs the non-constancy to place
  blocks of size $2^{\mu(i)}$ inside $\chi$ with sum $\chi$". Defect: false
  as a necessity claim; W2 places the blocks from the sum formula alone and
  never uses the strict increase of the powers, so (T3) holds without that
  hypothesis. Replacement: "(T3) carries the non-constancy hypothesis only
  to match Theorem 1.2's; its proof does not use it, since blocks of size
  $2^{\mu(i)}$ sum to $\chi$ for any cofinal $\langle\mu(i)\rangle$. When
  the powers are eventually constant the conclusion also follows from
  Sierpiński alone, so the case split loses nothing." For the Tools
  reviewer: the hypothesis can be dropped from (T3)'s statement.
- **F4 (note).** Location: "for regular $\lambda$ the relation reduces to
  $\lambda$ weakly compact". Defect: false at $\lambda=\omega$, where
  $\sum_{n<\omega}2^n=\aleph_0\to(\aleph_0)^2_2$. Replacement: "for
  uncountable regular $\lambda$" (verified in the attack on S9), or
  "$\lambda=\omega$ or weakly compact".
- **F5 (note).** The sentence "Together with two classical facts" counts
  Sierpiński's theorem and the block coloring; the reformulation S2 uses a
  third, the weakly compact characterization, which carries no citation.
  The Target paragraph's account of the problem page's assessment and Known
  Results is outside this review's read set and was not checked.

## Verdict

- **S0:** not a claim; the status `proved` matches the Statement section,
  the rest is excluded standing text.
- **S1:** refutation-failed.
- **S2:** refutation-failed.
- **S3:** refutation-failed.
- **S4:** refutation-failed under the section's eventual reading; its
  strongest reading is false (F1).
- **S5:** refuted-as-stated (F2).
- **S6:** refuted-as-stated (F3).
- **S7:** refutation-failed.
- **S8:** refutation-failed.
- **S9:** refuted-as-stated at the boundary $\lambda=\omega$; true for
  uncountable regular $\lambda$ (F4).
- **S10:** refutation-failed.

**Limitations.** Theorem 1.2 and the reconstruction pages were taken as
premises at their recorded standing and not re-verified. Sierpiński's
theorem, the weakly compact characterization, König's theorem, Easton's
theorem and Erdős--Rado are not held and were used at their standard
statements. The site's bullet and the problem page's Known Results were not
read; F2 rests on the section's own quotation of the bullet's wording.
Corrections: one required (F2), two suggested (F1, F3), two notes (F4, F5).
This focused review assigns no tier and changes no status.
