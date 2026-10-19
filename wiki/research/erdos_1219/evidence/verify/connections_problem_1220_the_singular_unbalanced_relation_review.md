---
name: research/erdos_1219/evidence/verify/connections_problem_1220_the_singular_unbalanced_relation_review
title: "Independent review of the connections section: Problem 1220: the singular unbalanced relation"
desc: |
  Refutation review of the Problem 1220 section of the connections page as of
  2026-09-28T13:50:48Z. The transfer lemma, its equivalence with the cofinality
  relation, the strong-limit composition, the type-count obstruction and
  the color-merging consequence survive (refutation-failed); two
  characterizations are refuted-as-stated, the universal thinning sentence
  of the obstruction and the attribution of the general strong-limit case
  to the survey. Two required corrections, three suggested, three notes.
created: 2026-09-28T19:11:29Z
updated: 2026-09-28T20:42:32Z
---

***

## Subject and independence

Role: independent reviewer in a fresh context, given only the assignment;
took no part in writing the page or the folder's reconstructions. Charge:
refutation of the author-recorded mathematics of one section.

Subject: page `wiki/research/erdos_1219/connections.md` as it stood at
2026-09-28T13:50:48Z, section "## Problem 1220: the singular unbalanced
relation", lines 171--285 (from its H2 heading to the line before "## Hajnal's
Conjecture 1A: triples" at line 286). No separate lead page was named; the
section is the subject.

Read, at the depth stated:

- the section, every sentence, with each proof re-derived;
- the page's Scope paragraph and its Tools section ((T1), (T2), (T3)) as
  inputs: their interfaces were confirmed at each use and their proofs
  were read for the interface only, since another reviewer checks them;
- the three reconstruction pages of the folder (Lemma 1.1, Theorem 1.2,
  Corollary 1.3) in full, as premises established at their standing;
- the Statement section of `wiki/problems/set_theory/E1220/_index.md`;
- the provenance paragraph of the Komjáth 2025 card and, for Problem 4,
  the held conversion and the page images of printed pp. 419--420 (PDF
  pp. 2--3) of the held PDF;
- the provenance paragraph of the Erdős and Rado 1956 card and the page
  image of printed p. 432 (PDF p. 6) of the held PDF, where the theorem
  the section imports as "not held" is printed;
- the Statement section of the Shelah 1975 result page `theorem_1_2`;
- `docs/verification.md` ("Whole-claim report", "Audit checklist",
  "Grading and claim standing"), `docs/approach_vetting.md`,
  `docs/evidence.md` ("Source fidelity") and `docs/math_authoring.md`.

Exposures, disclosed: (1) while reading the problem page for its Statement,
its Current assessment and Progress sections (lines 1--80 of the page) were
displayed; they paraphrase the section under review and carried nothing
that is not in the subject. (2) While reading the page head and Tools, the
neighboring section "Problem 1219 beyond the catalog question" (lines
109--170) was displayed; nothing from it is used. (3) The Shelah 1975
result page was read past its Statement (proof pointer, dependencies and
bears-on parts); nothing from those parts is used. No evidence folder,
index page, review, grade, standing or acceptance text, workspace content
or web page was read. The catalog page and the Problem 1171 connections
page named in the section were not read; the sentences resting on them
are marked unverified below.

## Restatement

Notation: $\theta\to(\mu_0,\mu_1)^2$ means that every two-coloring of the
pairs of a set of size $\theta$ has a set of size $\mu_0$ homogeneous in
color $0$ or a set of size $\mu_1$ homogeneous in color $1$; a cardinal
$\kappa$ is $\aleph_0$-inaccessible when $\mu^{\aleph_0}<\kappa$ for every
cardinal $\mu<\kappa$; $\lambda$ is strong limit when $2^\mu<\lambda$ for
every cardinal $\mu<\lambda$.

- S1 (fidelity). Problem 1220 asks whether $\lambda\to(\lambda,\aleph_1)^2$
  for every singular $\lambda$ such that $\lambda$ and
  $\operatorname{cf}\lambda$ are both $\aleph_0$-inaccessible; it is
  Problem 4 of the Erdős--Hajnal list; the survey's commentary on Problem 4
  records the necessity of both hypotheses, the simplest case
  $\lambda=\aleph_{\mathfrak c^+}$ with the reported theorem of Shelah, an
  Erdős--Rado theorem [45, Theorem 35.4], and the two consistency results
  [170] and [171] of Shelah and Stanley, as the section lists them.
  S1b, separated for its verdict: the survey attributes to
  [45, Theorem 35.4] the positive relation for every strong limit
  $\lambda$ ("gives the positive relation when $\lambda$ is strong limit";
  "the strong-limit case of the problem, the case Komjáth attributes to
  [45, Theorem 35.4]").
- S2 (conditional). If the survey's summary of [170] is accurate, the
  universal question, read in ZFC, has a consistent negative answer at
  $\lambda=\aleph_{\mathfrak c^+}$.
- S3 (transfer lemma). For every singular strong limit cardinal $\lambda$
  with $\kappa=\operatorname{cf}\lambda$ and every cardinal $\theta\le\kappa$
  with $\kappa\to(\kappa,\theta)^2$: $\lambda\to(\lambda,\theta)^2$.
- S4 (equivalence). For every singular strong limit $\lambda$:
  $\lambda\to(\lambda,\aleph_1)^2$ if and only if
  $\operatorname{cf}\lambda\to(\operatorname{cf}\lambda,\aleph_1)^2$; the
  forward direction is (T2) with $\gamma=1$, $\rho_0=\aleph_1$.
- S5 (composition with an imported theorem). For every regular
  $\aleph_0$-inaccessible $\kappa$, $\kappa\to(\kappa,\aleph_1)^2$ (the
  Erdős--Rado theorem for pairs, imported as not held); hence S3 with
  $\theta=\aleph_1$ proves the problem's relation for every singular strong
  limit $\lambda$ whose cofinality is $\aleph_0$-inaccessible.
- S6 (obstruction). S6a: Lemma 1.1, applied to a block decomposition of
  $\lambda$ into $\operatorname{cf}\lambda$ blocks with the union of the
  chosen $B_\alpha$ as the homogeneous set, is available exactly when
  $\lambda$ is strong limit: for non-strong-limit $\lambda$ the sizes
  $|E_\alpha|$ of the parameter sets are cofinal in $\lambda$, the type
  bound $2^{|E_\alpha|}$ reaches $\lambda>\lambda_\alpha$, and bounding the
  $\mu(i)$ below the least $\mu$ with $2^\mu\ge\lambda$ leaves a final set
  of size below $\lambda$. S6b, separated for its verdict: "no block inside
  $\lambda$ can be thinned to a single type".
- S7 (consequence). For every cardinal $\lambda$ and every finite $k\ge1$,
  $\lambda\to(\lambda,\aleph_1)^2$ implies
  $\lambda\to(\lambda,(\aleph_1)_k)^2$, by merging colors.
- S8 (assessment, not claims). The reported [170] and [171] show that the
  open part is not decided by "cardinal arithmetic of this kind"; any
  proof must use the $\aleph_0$-inaccessibility of $\lambda$ without
  passing through $2^{|E_\alpha|}$; the next-investigation items (i) and
  (ii); the Outcome.

## Checklist

- Quantifiers and scope: pass for S2--S5 and S7 (the transfer lemma
  carries $\theta\le\kappa$ and "singular strong limit" explicitly, and the
  corollary's hypothesis $\kappa\to(\kappa,\aleph_1)^2$ already forces
  $\aleph_1\le\kappa$); pass for S6a once "the mechanism" is read as
  Lemma 1.1 on blocks inside $\lambda$ with the union of the $B_\alpha$ as
  the homogeneous set, which is how the section uses it; fail for S1b,
  whose "$\lambda$" widens the survey's $\aleph_{\mathfrak c^+}$ (F2), and
  for S6b, whose strongest reading is a universal impossibility that the
  argument does not show (F1).
- Circularity: pass; no proof assumes its conclusion, and the transfer
  lemma's inputs ((T1), (ER), the cofinality relation) do not mention
  $\lambda\to(\lambda,\theta)^2$.
- Model and convention changes: pass; the two-place symmetric $\tilde f$ of
  Step 5 represents the pair coloring, blocks are sets and the relation
  depends only on cardinality, and (T1)'s interface is met clause by clause
  (Premises).
- Finite and statistical overreach: inapplicable; no finite sample or
  heuristic average is used.
- Uniformity: inapplicable; no constants or error terms.
- Extremal conclusions: inapplicable; no infimum, supremum or sharpness
  sentence beyond "exactly when", which is checked under S6a.
- Consequences and composition: pass for S4, S5 and S7 after supplying the
  two links the section leaves to unheld sources (the regular-case theorem
  is re-derived under Premises, the color merging under Strongest attack);
  fail for S6b (F1). The composition S3 with S5 inherits S5's unheld
  standing.
- Computation: inapplicable; the section computes nothing.
- Reproduction: inapplicable; no rerun instructions or coverage claims.
- Source and verdict fidelity: fail for S1b (F2); at suggested level, the
  page citation "p. 419" covers text printed on p. 420 (F4) and "not held"
  is said of a theorem whose successor case is printed in the held
  Erdős--Rado 1956 paper (F5); the reports of Problem 4's statement, of the
  necessity remark and of [170] and [171] match the page images; the
  catalog-page sentence and the Problem 1171 page's note are outside the
  read set and stay unverified (F8).

## Weakest steps

W1. The realizability hypothesis (H) in the transfer lemma. Re-derived:
fix $\alpha<\kappa$ and $C\subseteq A_\alpha$ with
$|C|=\lambda_\alpha=(2^{\mu(\alpha)})^+$; $\mu(\alpha)$ is infinite, so (ER)
transported to $C$ gives $H\subseteq C$ with $|H|=\lambda_\alpha$ and $f$
constantly $0$ on $[H]^2$, or $|H|=\mu(\alpha)^+$ and $f$ constantly $1$;
since $\mu(\alpha)\ge\mu(0)\ge\kappa\ge\theta$, the second $H$ contains a
$1$-homogeneous set of size $\theta$, excluded by the standing assumption;
any $B\subseteq H$ with $|B|=\mu(\alpha)$ satisfies $P_\alpha$. The property
depends on $B_\alpha$ alone, so (H) holds for every admissible sequence and
every choice of the points $a_i$. The lemma's clause (2) then gives
$|B_\alpha|=\mu(\alpha)$ exactly, which the size count W2 needs.

W2. The sizes. $\lambda_i=(2^{\mu(i)})^+<\lambda$ needs $\lambda$ strong
limit and a limit cardinal, both given; $\sum_{i<\kappa}\lambda_i$ equals
$\kappa\cdot\sup_i\lambda_i$ by the sum formula, and
$\mu(i)<\lambda_i<\lambda$ with $\sup_i\mu(i)=\lambda$ gives
$\sup_i\lambda_i=\lambda$, so the sum is $\lambda$. For $I\subseteq\kappa$
of size $\kappa$, $I$ is unbounded in the regular $\kappa$ and the
$\mu(\alpha)$ increase, so $\sup_{\alpha\in I}\mu(\alpha)=\lambda$ and, the
blocks being disjoint,
$|\bigcup_{\alpha\in I}B_\alpha|=\sum_{\alpha\in I}\mu(\alpha)=\lambda$.
Both agree with the section.

W3. The obstruction as a statement about Lemma 1.1. Re-derived from the
lemma's growth condition rather than from the type count: the lemma
requires $\prod_{i<\alpha}\lambda_i^{\mu(i)}<\lambda_\alpha$ with each
$\lambda_i$ regular. Blocks lie inside $\lambda$ and $\lambda$ is singular,
so every regular $\lambda_\alpha\le\lambda$ is below $\lambda$. Since
$\lambda_i\ge2$, the condition gives
$2^{\sum_{i<\alpha}\mu(i)}\le\prod_{i<\alpha}\lambda_i^{\mu(i)}<\lambda_\alpha<\lambda$.
The final homogeneous set is $\bigcup_{\alpha\in I}B_\alpha$ with
$|B_\alpha|\le\mu(\alpha)$, for an $I$ that the cofinality relation
chooses, so its size $\lambda$ forces $\sup_{\alpha<\kappa}\mu(\alpha)=\lambda$.
Then for every $\mu<\lambda$ there is $i$ with
$\mu\le\mu(i)\le\sum_{j\le i}\mu(j)$, whence $2^\mu<\lambda$: the lemma's
hypotheses force $\lambda$ strong limit. The number of blocks must be
$\operatorname{cf}\lambda$: a strictly increasing sequence of regular
cardinals below $\lambda$ with supremum $\lambda$ has length of cofinality
$\operatorname{cf}\lambda$, and the lemma's $\kappa$ is regular, while a
bounded sequence covers fewer than $\lambda$ points. So S6a holds in the
form "the lemma's hypotheses can be met for such a decomposition exactly
when $\lambda$ is strong limit"; nothing stronger is proved (F1).

## Strongest attack

S1: each listed item was compared with the page images of printed
pp. 419--420 of the survey. The problem statement, the definition of
$\aleph_0$-inaccessibility, the necessity remark
($\tau^{\aleph_0}\not\to(\tau^+,\aleph_1)^2$ and the cofinality
implication, which is (T2) at $\gamma=1$, $\rho_0=\aleph_1$), the simplest
case with the reported theorem of Shelah, the [170] forcing "preserving
$2^\tau$ up to a predetermined $\mu<\aleph_{\mathfrak c^+}$", and the [171]
model from $\mathfrak c^+$ measurable cardinals are reported faithfully.
The attack succeeded only against S1b: the survey's sentence is "the
positive relation holds if $\aleph_{\mathfrak c^+}$ is strong limit", an
instance, not the general strong-limit case (F2). The page citation is off
by one page for the [170] and [171] sentences (F4).

S2: the inference "a counterexample at $\aleph_{\mathfrak c^+}$ in the
[170] model, hence a consistent negative answer to the universal question"
needs both hypotheses at $\lambda=\aleph_{\mathfrak c^+}$ in that model:
$\operatorname{cf}\lambda=\mathfrak c^+$ is $\aleph_0$-inaccessible in ZFC
($\mu\le\mathfrak c$ gives
$\mu^{\aleph_0}\le\mathfrak c^{\aleph_0}=\mathfrak c$),
$\lambda$ is $\aleph_0$-inaccessible by the theorem of Shelah that the
survey reports as a theorem of ZFC, and $\lambda$ is singular since
$\aleph_{\mathfrak c^+}>\mathfrak c^+$ ($\mathfrak c^+$ is a successor, not
a fixed point of the aleph function). The inference stands, conditional on
the two reports; the section hedges on [170] only, and its item (i) then
asks a question that the reported ZFC theorem answers (F6). Observed in
addition: under GCH every singular cardinal is strong limit, so S3 with S5
gives the universal positive answer under GCH; with the [170] summary
accurate, the universal question is independent of ZFC.

S3: the four places where a hypothesis could be missing were attacked.
(a) The non-constancy of the powers: the section's reason
"$2^\mu\ge\mu^+$" does not give it by itself (powers constantly equal to
$\lambda^+$ from some point on are compatible with it); it holds because
for a cardinal $\nu<\lambda$ the cardinal $\mu=2^\nu$ is below $\lambda$
by strong limit and $2^\mu\ge\mu^+>2^\nu$ (F3). (b) Step 1 without
$\mu_0$: it needs $\kappa<\lambda$ for $\rho_i<\lambda$, given by
singularity. (c) The (T1) interface: confirmed clause by clause
(Premises). (d) The two cases of the cofinality relation: W1 and W2.
Boundary cases: $\theta\le1$ makes the standing assumption contradictory
and the conclusion trivial; $\theta=\omega$ recovers the
Erdős--Dushnik--Miller relation for singular strong limit $\lambda$;
$\kappa=\omega$ runs with $\mu(0)\ge\omega$. No counterexample was found: a
singular strong limit $\lambda$ with $\operatorname{cf}\lambda=\aleph_1$
has $\lambda\not\to(\lambda,\aleph_1)^2$ by (T2), but there
$\aleph_1\not\to(\aleph_1,\aleph_1)^2$ (Sierpiński), so the hypothesis
fails too.

S4: the forward direction is (T2) at $\gamma=1$, $\rho_0=\aleph_1\ge2$ with
$\lambda$ singular; the backward direction is S3 with $\theta=\aleph_1$,
whose side condition $\aleph_1\le\kappa$ follows from
$\kappa\to(\kappa,\aleph_1)^2$ (for $\kappa=\omega$ the coloring with every
pair in color $1$ has no $0$-homogeneous set of size $\omega$ and no set of
size $\aleph_1$ at all). No gap.

S5: the imported theorem cannot be checked against a held source in its
regular-limit case, so it was re-derived (Premises, Claim R) for every
regular $\kappa$ with $\mu^{\aleph_0}<\kappa$ for all $\mu<\kappa$,
successor or limit; the successor case is Theorem 7(i) of the held
Erdős--Rado 1956 paper (F5). The composition then proves the strong-limit
case of the problem for every such $\lambda$, as the section says.

S6: Lemma 1.1 was tried on a non-strong-limit $\lambda$ with other choices
of blocks, of the number of blocks, of the $\mu(i)$ and of the lemma's
$\chi$; every choice is caught by the growth condition (W3), so S6a
survives. Against S6b the witness is the constant coloring $f\equiv0$: over
every parameter set every element of every block has the same type, so
every block is already "a single type"; more generally $2^{|E_\alpha|}$ is
an upper bound on the number of types (bound (A)), and a fiber of
$a\mapsto\operatorname{tp}(a,E_\alpha)$ of size $\lambda_\alpha$ may exist
for a particular $f$. What fails when $2^{|E_\alpha|}\ge\lambda$ is the
pigeonhole that guarantees such a fiber, not its existence (F1). The
sentence "Choosing the $\mu(i)$ below the least such $\mu$ keeps the count"
was checked: with $\mu^*$ the least $\mu$ with $2^\mu\ge\lambda$ and all
$\mu(i)<\mu^*$, either $\sup_i\mu(i)<\mu^*$ or
$\operatorname{cf}\mu^*=\kappa$, and in both cases
$\sum_{i<\alpha}\mu(i)<\mu^*$ for $\alpha<\kappa$, so the count is kept and
the final set has size at most $\kappa\cdot\mu^*<\lambda$.

S7: re-derived by induction on $k$. For $f:[\lambda]^2\to k+1$ let $g$ mark
the pairs of color $k$; $\lambda\to(\lambda,\aleph_1)^2$ gives a set of
size $\aleph_1$ homogeneous in color $k$ or a set $H$ of size $\lambda$ on
which $f$ omits $k$, and the induction hypothesis transported to $H$
finishes. The naive merge of the colors $1,\ldots,k$ into one would need
$\aleph_1\to(\aleph_1)^2_k$, which is false; the induction avoids it. The
attribution to the Problem 1171 page is unverified within the read set.

## Premises

- (T1), the lemma interface (page Tools; its proof is another reviewer's):
  needs $\kappa$ infinite regular; $\mu(i)$ infinite, strictly increasing,
  $\mu(0)\ge\kappa$, $2^{\mu(i)}$ strictly increasing;
  $\lambda_i=(2^{\mu(i)})^+$; disjoint $A_i$ with $|A_i|=\lambda_i$; $F$ of
  finitely many places into $2$; properties with (H). In the transfer
  lemma: $\kappa=\operatorname{cf}\lambda$ regular infinite; the $\mu(i)$
  from Step 1 without $\mu_0$; $A_i$ the blocks; $F=\tilde f$; (H) by W1.
  Met.
- (T2) (page Tools; its proof is another reviewer's): $\lambda$ singular,
  $\gamma\ge1$, $\rho_\nu\ge2$ and $\kappa\not\to(\kappa,(\rho_\nu)_\nu)^2$
  give $\lambda\not\to(\lambda,(\rho_\nu)_\nu)^2$. Used at $\gamma=1$,
  $\rho_0=\aleph_1$ (S1, S4). Met.
- [[research/erdos_1219/lemma_1_1_reconstruction|Lemma 1.1 reconstruction]]
  (premise, reviewed as of 2026-09-28T05:03:27Z): clauses (1B) and (2), bound
  (A), the growth condition and the role of (B) in the second thinning; read in
  full.
- [[research/erdos_1219/theorem_1_2_reconstruction|Theorem 1.2 reconstruction]]
  (premise): Step 1 (choice of the $\mu(i)$; used without $\mu_0$, which
  needs only non-constancy and $\kappa<\lambda$), the sum formula, Step 5
  ($\tilde f$; growth and $2^{2+\kappa}<\lambda_0$ from $\mu(0)\ge\kappa$
  and $|j|\le\mu(j)$), Steps 6--7 (the argument for $g$ and for $|B|$),
  and (ER): for infinite $\mu$, $(2^\mu)^+\to((2^\mu)^+,\mu^+)^2$, not
  held; read in full.
- [[research/erdos_1219/corollary_1_3_reconstruction|Corollary 1.3 reconstruction]]
  (premise): not used by the section; read in full for the folder's
  conventions.
- [[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|Komjáth 2025]],
  Problem 4 commentary, printed pp. 419--420: held; the conversion and the
  page images were read. Interface used: the problem statement, the
  necessity remark, the simplest case, [45, Theorem 35.4] stated for
  $\aleph_{\mathfrak c^+}$, the summaries of [170] and [171].
- [45] (Erdős, Hajnal, Máté and Rado 1984), [170] and [171] (Shelah and
  Stanley 1987 and 1993), [158] (the theorem of Shelah): not held; used
  only as the survey reports them.
- The regular-case theorem of S5. Not held in the generality the section
  needs. The successor case is Theorem 7(i) of
  [[../library/set_theory/erdos_1956_partition_calculus_set_theory/_index|Erdős and Rado 1956]]
  (printed p. 432, PDF p. 6, read on the page image): for $a\ge\aleph_0$
  and $b$ minimal with $a^b>a$, $a^+\to(b,a^+)^2$; with $a^{\aleph_0}=a$
  one has $b\ge\aleph_1$, hence $a^+\to(a^+,\aleph_1)^2$ after exchanging
  the colors. Theorem 8 there gives the regular-limit case under GCH only.
  Claim R supplies the general case.

Claim R. Let $\kappa$ be regular with $\mu^{\aleph_0}<\kappa$ for every
cardinal $\mu<\kappa$. Then $\kappa\to(\kappa,\aleph_1)^2$.

Proof. $2^{\aleph_0}<\kappa$, so $\kappa\ge\aleph_2$. Let
$f:[\kappa]^2\to2$ have no $0$-homogeneous set of size $\kappa$; a
$1$-homogeneous set of size $\aleph_1$ is to be found. Write
$N(x,X)=\{y\in X:y>x,\ f(\{x,y\})=1\}$.

(1) For $X\subseteq\kappa$ with $|X|=\kappa$ the set
$X^-=\{x\in X:|N(x,X)|<\kappa\}$ has size below $\kappa$. Otherwise choose
$y_\xi\in X^-$ by recursion on $\xi<\kappa$, above every $y_\eta$
($\eta<\xi$) and outside $\bigcup_{\eta<\xi}N(y_\eta,X)$, a set of size
below $\kappa$ by regularity; then $f(\{y_\eta,y_\xi\})=0$ for $\eta<\xi$,
a $0$-homogeneous set of size $\kappa$.

(2) There is $M\prec(H(\Theta),\in)$ with $f,\kappa\in M$, $|M|<\kappa$,
${}^\omega M\subseteq M$ and $\delta:=M\cap\kappa\in\kappa$. Let
$M_0\prec H(\Theta)$ be countable with $f,\kappa\in M_0$; let
$M_{i+1}\prec H(\Theta)$ contain
$M_i\cup{}^\omega M_i\cup\sup(M_i\cap\kappa)$ with
$|M_{i+1}|\le|M_i|^{\aleph_0}+|\sup(M_i\cap\kappa)|<\kappa$, by
$\aleph_0$-inaccessibility and regularity; take unions at limits; put
$M=\bigcup_{i<\omega_1}M_i$. Then $|M|<\kappa$ ($\kappa$ regular and above
$\aleph_1$); a countable subset of $M$ lies in some $M_i$, hence in
$M_{i+1}$; and $M\cap\kappa$ is an ordinal, since $\gamma\in M_i\cap\kappa$
gives $\gamma\subseteq\sup(M_i\cap\kappa)\subseteq M_{i+1}$. By induction
every countable ordinal is a countable subset of $M$ and so an element of
$M$; thus $\omega_1\subseteq M$, and every sequence of countable length
from $M$ lies in $M$.

(3) Choose $x_\alpha\in M\cap\kappa$ for $\alpha<\omega_1$, increasing,
with $f(\{x_\beta,x_\alpha\})=1$ for $\beta<\alpha$ and
$f(\{x_\alpha,\delta\})=1$. Given $\langle x_\beta:\beta<\alpha\rangle\in M$,
let $\gamma=\sup_{\beta<\alpha}x_\beta\in M\cap\kappa$ and
$X=\{y<\kappa:y>\gamma,\ f(\{x_\beta,y\})=1\text{ for all }\beta<\alpha\}$;
$X\in M$ and $\delta\in X$ by the invariant, so $X$ is unbounded in
$\kappa$ (a bound would be definable in $M$, hence below $\delta$) and
$|X|=\kappa$. Put $G=X\setminus X^-\in M$; $|X\setminus G|<\kappa$ by (1).
If $f(\{x,\delta\})=0$ for every $x\in G\cap\delta$, then $\delta$ lies in
$Q=\{y\in X:f(\{x,y\})=0\text{ for all }x\in G\cap y\}\in M$, so $Q$ is
unbounded, $|Q\cap G|=\kappa$, and $Q\cap G$ is $0$-homogeneous ($x<y$ in
$Q\cap G$ gives $x\in G\cap y$ and $y\in Q$), a contradiction. So some
$x\in G\cap\delta=G\cap M$ has $f(\{x,\delta\})=1$; let $x_\alpha=x$. Then
$x_\alpha>\gamma$, $x_\alpha\in X$ gives $f(\{x_\beta,x_\alpha\})=1$ for
$\beta<\alpha$, and $\delta$ stays in the next $X$.

The set $\{x_\alpha:\alpha<\omega_1\}$ is $1$-homogeneous of size
$\aleph_1$. $\square$

The proof uses regularity, $\kappa>\aleph_1$ and $\mu^{\aleph_0}<\kappa$
for $\mu<\kappa$ only; no tree property, so it covers weakly inaccessible
$\kappa$ as well as successors.

## Findings

F1 (required). Location: lines 254--256, "then $2^{|E_\alpha|}\ge\lambda$
for every $\alpha$ with $|E_\alpha|\ge\mu$, and no block inside $\lambda$
can be thinned to a single type", and lines 258--259, "This is an
obstruction to canonization over full parameter sets". Defect: in its
strongest reading the first sentence asserts that no block has a subset of
full size with one type over $E_\alpha$; the argument shows only that the
counting bound (B) fails, so that the pigeonhole of the second thinning is
unavailable. Witness: the constant coloring, for which every block is a
single type over every parameter set; for a general $f$, bound (A) is an
upper bound and a large fiber may exist. Replacement: "and the count that
the second thinning uses no longer yields a fiber of size
$\lambda_\alpha$" and "This is an obstruction to the counting of Lemma 1.1,
not to canonization as such and not a proof of the negative relation".
S6a is unaffected.

F2 (required). Location: lines 184--185, "an Erdős--Rado theorem ([45,
Theorem 35.4] in the survey's numbering) gives the positive relation when
$\lambda$ is strong limit", and lines 244--245, "the strong-limit case of
the problem, the case Komjáth attributes to [45, Theorem 35.4]". Defect:
the survey's sentence (printed p. 419) is "the positive relation holds if
$\aleph_{\mathfrak c^+}$ is strong limit", an instance; the section
reports it as the general strong-limit case, and [45] is not held to check
the theorem's own generality. Replacement: "gives the positive relation
when $\aleph_{\mathfrak c^+}$ is strong limit" and "the case whose instance
$\lambda=\aleph_{\mathfrak c^+}$ Komjáth attributes to [45, Theorem 35.4]";
the Outcome's "a known theorem" then rests on S3 with S5 (and, for
successor cofinalities, on Theorem 7(i) of the held Erdős--Rado 1956
paper) rather than on the survey.

F3 (suggested). Location: lines 209--210, "Since $2^\mu\ge\mu^+$ for
$\mu<\lambda$, the powers below $\lambda$ are not eventually constant".
Defect: the reason as written does not use strong limit and is
insufficient alone (powers constantly $\lambda^+$ from some $\mu$ on
satisfy $2^\mu\ge\mu^+$). Replacement: "Since $\lambda$ is strong limit,
for every cardinal $\nu<\lambda$ the cardinal $\mu=2^\nu$ lies below
$\lambda$ and $2^\mu\ge\mu^+>2^\nu$, so the powers are not eventually
constant".

F4 (suggested). Location: line 178, "Komjáth's commentary (p. 419, read in
the held conversion)". Defect: the sentences on [170] and [171] are
printed on p. 420. Replacement: "(pp. 419--420, read in the held
conversion)".

F5 (suggested). Location: lines 240--243, "For a regular
$\aleph_0$-inaccessible $\kappa$ the hypothesis
$\kappa\to(\kappa,\aleph_1)^2$ is the Erdős--Rado theorem for pairs (not
held; ...)". Defect: the successor case is printed in the held
Erdős--Rado 1956 paper, Theorem 7(i) (printed p. 432), and covers the
simplest instance $\operatorname{cf}\lambda=\mathfrak c^+$; only the
regular-limit case lacks a held source (its GCH form is Theorem 8 there).
Replacement: cite Theorem 7(i) of the held paper for successor $\kappa$
and either a source or a recorded argument (Claim R above is one) for
regular limit $\kappa$.

F6 (note). Location: lines 271--273, "whether the model of [170] keeps
both $\aleph_0$-inaccessibility hypotheses, which decides whether the
universal question is independent of ZFC". The section has already
accepted, from the survey, that both hypotheses hold at
$\aleph_{\mathfrak c^+}$ in ZFC, so the model keeps them automatically;
the open point is whether the summary of [170] is accurate. The positive
side of independence is available: under GCH every singular cardinal is
strong limit, so S3 with S5 gives the universal positive answer. No text
change is required.

F7 (note). Location: lines 261--264, "show that the open part is not
decided by cardinal arithmetic of this kind, and any proof must use the
$\aleph_0$-inaccessibility of $\lambda$ in a way that does not pass
through $2^{|E_\alpha|}$", and lines 276--278, "a positive outcome would
need a canonization that uses only countable parameter sets". The first
sentence holds for the strong-limit dichotomy only; the survey does not
say that the two models share a continuum function. The "must" and "would
need" sentences are programmatic and not proved; a positive proof need not
be a canonization. Suggested wording: "the strong-limit dichotomy alone
does not decide the open part" and "one route would be".

F8 (note). Location: lines 195--197 (the catalog page) and lines 264--268
(the Problem 1171 page's note). Both are outside the read set; the
mathematics of S7 is verified above, the attributions are not.

## Verdict

- S1: refutation-failed for the problem statement and the listed records
  of the survey other than S1b. S1b: refuted-as-stated, as a
  characterization of the held survey (F2); the mathematics it points to,
  the strong-limit case, is proved in the section by S3 with S5.
- S2: refutation-failed, as the conditional it is; F6 records a redundancy
  in the follow-up item.
- S3: refutation-failed; F3 asks the stated reason to name strong limit.
- S4: refutation-failed.
- S5: refutation-failed; the imported theorem was re-derived here
  (Claim R) because its regular-limit case is not held; F5 corrects "not
  held" for the successor case.
- S6a: refutation-failed, in the form "the hypotheses of Lemma 1.1 can be
  met for a block decomposition of $\lambda$ with the union of the
  $B_\alpha$ as the homogeneous set exactly when $\lambda$ is strong
  limit".
- S6b: refuted-as-stated (F1); the paragraph's conclusion survives with
  the replacement wording.
- S7: refutation-failed.
- S8: not a claim; F7 and F8 record the wording and the unverified
  attributions.

Limitations: [45], [170], [171] and [158] are not held, so every sentence
about them is checked only against the survey's text; the catalog page and
the Problem 1171 connections page were not read; the proofs of (T1) and
(T2) were not re-derived here beyond their interfaces. Two required
corrections (F1, F2), three suggested (F3, F4, F5), three notes (F6, F7,
F8). This focused review assigns no tier and changes no status.
