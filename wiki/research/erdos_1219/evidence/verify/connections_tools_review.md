---
name: research/erdos_1219/evidence/verify/connections_tools_review
title: "Independent review of the connections section: Tools"
desc: |
  Refutation review of the three tools (T1), (T2) and (T3) of the connections
  page as of 2026-09-28T13:50:48Z: all three statements are refutation-failed,
  the Komjáth attribution under (T2) is confirmed on the page image, and no
  required correction is filed (one suggested correction, three notes).
created: 2026-09-28T19:02:04Z
updated: 2026-09-28T19:02:04Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, given only the
commissioning assignment. The reviewer took no part in writing the reviewed
page or the reconstruction pages it cites, had no contact with their author,
and read no review, grade, assessment or standing text about the reviewed
section. Charge: refutation of author-recorded mathematics.

**Subject.** Page `wiki/research/erdos_1219/connections.md` as it stood at
2026-09-28T13:50:48Z, section `## Tools`, lines 39--108 (from the H2 heading to
the line before the next H2, `## Problem 1219 beyond the catalog question`). No
lead page is named; the section is itself the shared section that the page's
later sections consume. Its shared input is the page's Scope paragraph (lines
19--37: notation for the partition relation, $(\rho)_\gamma$, $\chi$, and block
decompositions), read as a convention whose own content is not under review
here.

**Premises read.** The three reconstruction pages of the folder as of the same
time, `lemma_1_1_reconstruction.md`, `theorem_1_2_reconstruction.md` and
`corollary_1_3_reconstruction.md`, read in full, including their Standing
paragraphs; their stated results are treated as established at their
standing (independently reviewed as of 2026-09-28T05:03:27Z, corrections applied
since), and each interface the section uses is confirmed in "Premises"
below. The `## Statement` section of the result page
`library/set_theory/shelah_1975_notes_partition_calculus/theorem_1_2.md`.
The provenance paragraphs of the library cards
[[../library/set_theory/shelah_1975_notes_partition_calculus/_index|Shelah (1975)]]
and
[[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|Komjáth (2025)]],
and the held Komjáth PDF at printed p. 419 (PDF p. 2), read on the text
layer and on the page image; the held conversion of the survey at the same
place. The Statement blocks of
[[problems/set_theory/E1219/_index|Problem 1219]],
[[problems/set_theory/E1218/_index|Problem 1218]],
[[problems/set_theory/E1220/_index|Problem 1220]] and
[[problems/set_theory/E1167/_index|Problem 1167]]. The wiki pages
`docs/verification.md` (sections "Whole-claim report", "Audit checklist",
"Grading and claim standing"), `docs/approach_vetting.md`,
`docs/evidence.md` (section "Source fidelity") and `docs/math_authoring.md`.
The Shelah scan itself was not consulted: the reconstruction pages are the
premises for the lemma and the theorem.

**Exposures.** Five over-reads, disclosed here; none concerns a statement of
the Tools section, which makes no status or standing claim.

- The Komjáth card `_index.md` was read in full, past its provenance
  paragraph: its digest and "Results to transcribe" list, including the
  sentence calling the survey the acceptance record for Problem 3 for
  Problem 1219.
- The Shelah card `_index.md`: its generated link rows and the part of its
  digest describing the paper's sections, past the provenance paragraph.
- The result page `theorem_1_2.md`: its Statement section contains a "Read
  depth" paragraph ending with a standing sentence about that result page.
- The problem pages: the `**Status.**` line after each Statement block
  (Proved, Open, Open, Open) and, for Problem 1219, its References list,
  which restates the survey's acceptance sentence; no Current assessment,
  Progress or Known Results section was read.
- The recent commit subjects visible in the environment, which carry no
  mathematical content.

## Restatement

Conventions: $\theta\to(\mu_\nu)^2_{\nu<\gamma'}$ means that every coloring
of the two-element subsets of a set of size $\theta$ with $\gamma'$ colors has,
for some color $\nu$, a subset of size $\mu_\nu$ all of whose pairs have color
$\nu$; a homogeneous set of size at least $\mu_\nu$ contains one of size
$\mu_\nu$, and colorings are transported along bijections, so only the
cardinal on the left matters. $\theta\not\to$ is the negation. A witness for
a negative relation is a coloring with no homogeneous set of the excluded
size in any color. $\chi=\sum_{\mu<\lambda}2^\mu$ sums over every cardinal
below $\lambda$, finite ones included.

**S1 (T1, the lemma's interface).** Let $\kappa$ be an infinite regular
cardinal; let $\langle\mu(i):i<\kappa\rangle$ be infinite cardinals, strictly
increasing, with $\mu(0)\ge\kappa$ and $\langle2^{\mu(i)}:i<\kappa\rangle$
strictly increasing; let $\lambda_i=(2^{\mu(i)})^+$; let $A_i$ ($i<\kappa$)
be pairwise disjoint sets with $|A_i|=\lambda_i$ and $A=\bigcup_iA_i$; let
$1\le n<\omega$ and $F:A^n\to2$. Let $P_\alpha$ ($\alpha<\kappa$) be any
properties of pairs $\langle B_i:i\le\alpha\rangle$,
$\langle a_i:\alpha<i<\kappa\rangle$ with $B_i\subseteq A_i$, $a_i\in A_i$,
satisfying (H): for every $\alpha<\kappa$, every $\langle B_i:i<\alpha\rangle$
with $B_i\subseteq A_i$ and $|B_i|\le\mu(i)$, every
$\langle a_i:\alpha<i<\kappa\rangle$ with $a_i\in A_i$, and every
$C\subseteq A_\alpha$ with $|C|=\lambda_\alpha$, there is $B_\alpha\subseteq C$
with $|B_\alpha|\le\mu(\alpha)$ for which $P_\alpha$ holds. Then every
hypothesis of the Canonization Lemma 1.1, as reconstructed, holds with its
$\chi=2$, $F_0=F_1=F$, these $\kappa$, $\lambda_i$, $\mu(i)$, $A_i$ and
$P_\alpha$; consequently there are $a^*_i\in A_i$ and $B_i\subseteq A_i$ with
$|B_i|\le\mu(i)$ satisfying the lemma's (1A), (1B) and (2), and when $n=2$,
$F(b,c)=F(b',c')$ for all $\alpha<\beta<\kappa$, $b,b'\in B_\alpha$,
$c,c'\in B_\beta$. The sentence also asserts that Step 2(a) and Step 5 of the
theorem page establish the lemma's hypotheses from these assumptions and
nothing about a cardinal $\lambda$.

**S2 (T2, composition with a witness at the cofinality).** For every
singular cardinal $\lambda$ with $\kappa=\operatorname{cf}\lambda$, every
$\gamma\ge1$ and every family of cardinals $\rho_\nu\ge2$ ($\nu<\gamma$): if
some $c:[\kappa]^2\to1+\gamma$ has no set of size $\kappa$ homogeneous in
color $0$ and, for every $\nu<\gamma$, no set of size $\rho_\nu$ homogeneous
in color $1+\nu$, then some $d:[\lambda]^2\to1+\gamma$ has no set of size
$\lambda$ homogeneous in color $0$ and, for every $\nu<\gamma$, no set of
size $\rho_\nu$ homogeneous in color $1+\nu$. In arrow notation:
$\kappa\not\to(\kappa,(\rho_\nu)_{\nu<\gamma})^2$ implies
$\lambda\not\to(\lambda,(\rho_\nu)_{\nu<\gamma})^2$.

**S3 (attribution under T2).** The instance $\gamma=1$, $\rho_0=\aleph_1$ of
S2 is the remark on necessity that Komjáth prints under Problem 4 on p. 419:
if $\operatorname{cf}(\kappa)\not\to(\operatorname{cf}(\kappa),\aleph_1)^2$
then $\kappa\not\to(\kappa,\aleph_1)^2$.

**S4 (T3, the converse of Theorem 1.2 at the cofinality).** For every
singular cardinal $\lambda$ with $\kappa=\operatorname{cf}\lambda$ such that
(i) for every cardinal $\nu<\lambda$ there is a cardinal $\mu$ with
$\nu<\mu<\lambda$ and $2^\mu>2^\nu$ (the sequence is not eventually
constant, in the theorem page's sense), and (ii) some $c:[\kappa]^2\to2$ has
no homogeneous set of size $\kappa$: there is $d:[\chi]^2\to2$ with no
homogeneous set of size $\lambda$, that is, $\chi\not\to(\lambda)^2_2$.

**S5 (cross-reference).** "The case $\gamma=\aleph_0$, $\rho_\nu=3$ is used
for Problem 1218 below" names a later use and asserts no mathematics; it is
not a claim of this section.

## Checklist

- **Quantifiers and scope.** Pass. S1 quantifies over every family
  $P_\alpha$ satisfying (H) and every $n$-place $F$; (H) is universal in
  $\alpha$, the admissible sequence, the points and the large subset $C$,
  exactly as the lemma page states it. S2 and S4 are universal in
  $\lambda$, $\gamma$, $\rho_\nu$ and the witness, and their conclusions are
  existence statements for one coloring. Boundary cases: $n=0$ in S1 is
  excluded by the lemma's $1\le n_i$ (Finding F4); $\rho_\nu>\kappa$ in S2
  makes the hypothesis on that color vacuous and the argument still
  contradicts $|J|\le\kappa$; $i_0=0$ in S4 gives $|H|=0$.
- **Circularity.** Pass. S4 does not use Theorem 1.2 or S1; S2 uses only
  the witness and a partition; S1 checks hypotheses of a lemma it does not
  invoke in its own proof.
- **Model and convention changes.** Pass with a note. Colorings are
  transported along bijections (a theorem-page convention). S2 states its
  relation for a sequence of targets with possibly infinitely many colors,
  $(\rho_\nu)_{\nu<\gamma}$, which neither the page's Scope paragraph
  (which defines only $(\rho)_\gamma$) nor the theorem page (finitely many
  colors) defines; it is the survey's own notation on p. 419 (Finding F3).
  The restatement above fixes the reading; the proof uses exactly it.
- **Finite and statistical overreach.** Inapplicable: no finite check or
  average stands in for a proof.
- **Uniformity.** Pass. The only per-index bounds are $|B_i|\le\mu(i)$ in
  S1 and $|H\cap X_i|\le\mu(i)$ in S4, each proved for every $i$ with no
  hidden dependence.
- **Extremal conclusions.** Inapplicable: no infimum, supremum or sharpness
  is claimed; the identification $\chi=\sup_i2^{\mu(i)}$ in S4 is an
  equality re-derived in W2.
- **Consequences and composition.** Pass. S1's composition with the lemma
  is checked hypothesis by hypothesis in W1 and "Premises"; S4's "so
  $|J|=\kappa$" and S2's two contradictions are each re-derived; the
  parenthetical "(S) on the theorem page" is used within its hypothesis
  (infinite $\mu$) once Step 1's bound $\mu(i)\ge\kappa$ is carried
  (Finding F1).
- **Computation.** Inapplicable: the section runs no computation.
- **Reproduction.** Inapplicable: no rerun command or coverage line.
- **Source and verdict fidelity.** Pass. The Komjáth remark under Problem 4
  reads, on the page image of p. 419, "The conditions are necessary, as
  $\tau^{\aleph_0}\not\to(\tau^+,\aleph_1)^2$ and if
  $\operatorname{cf}(\kappa)\not\to(\operatorname{cf}(\kappa),\aleph_1)^2$,
  then $\kappa\not\to(\kappa,\aleph_1)^2$"; the text layer drops the
  negation strokes and the Greek letters, the image and the held
  conversion carry them. The survey prints no proof; S2 supplies one for
  singular $\kappa$, the only case with content. The section's references
  to Step 1, Step 2(a), Step 5, Step 6, the sum formula and (S) of the
  theorem page name the places that hold those items.

## Weakest steps

**W1: the growth condition in S1.** The lemma needs
$\lambda^j=\prod_{i<j}\lambda_i^{\mu(i)}<\lambda_j$ for every $j<\kappa$ and
$2^{2+\kappa}<\lambda_0$. Re-derivation from S1's hypotheses alone. Since
$\mu(i)$ is infinite, $\mu(i)<2^{\mu(i)}<\lambda_i$, and $\lambda_i$ is a
successor cardinal, hence regular, so every function $\mu(i)\to\lambda_i$ is
bounded below $\lambda_i$; thus
$\lambda_i^{\mu(i)}\le\sum_{\theta<\lambda_i}|\theta|^{\mu(i)}\le\lambda_i\cdot(2^{\mu(i)})^{\mu(i)}=\lambda_i\cdot2^{\mu(i)}=\lambda_i$,
using $|\theta|\le2^{\mu(i)}$ for $\theta<\lambda_i$ and
$(2^\mu)^\mu=2^\mu$ for infinite $\mu$. For $i<j$,
$\lambda_i=(2^{\mu(i)})^+\le2^{\mu(j)}$ because $2^{\mu(i)}<2^{\mu(j)}$.
Hence for $1\le j<\kappa$,
$\lambda^j=\prod_{i<j}\lambda_i\le(2^{\mu(j)})^{|j|}\le(2^{\mu(j)})^{\mu(j)}=2^{\mu(j)}<\lambda_j$,
where $|j|\le\mu(j)$ holds because $j<\kappa\le\mu(0)\le\mu(j)$; and
$\lambda^0=1<\lambda_0$. Finally $2^{2+\kappa}=2^\kappa\le2^{\mu(0)}<\lambda_0$
by $\mu(0)\ge\kappa$. Nothing about a cardinal $\lambda$ or about the
$\mu(i)$ being cofinal anywhere was used, which is what S1's last sentence
asserts. Composition: with the lemma's other hypotheses (W1 covers the two
that need arithmetic; regularity and monotonicity of the $\lambda_i$,
$|A_i|=\lambda_i$, $\kappa$ infinite regular, and (H) are immediate or
assumed), the lemma's conclusion is available verbatim, and (1B) with the
empty parameter sequence is the two-place canonical form.

**W2: the identification of $\chi$ and the small-$J$ bound in S4.**
Re-derivation. Choose $\mu(i)$ as in Step 1 of the theorem page with
$\rho_i=\max(\kappa,\nu_i,\sup_{j<i}\mu(j))$: each $\rho_i<\lambda$ because
$\kappa<\lambda$ (singularity), $\nu_i<\lambda$, and a supremum of fewer
than $\operatorname{cf}\lambda$ cardinals below $\lambda$ is below
$\lambda$; hypothesis (i) gives a least cardinal $\mu(i)$ with
$\rho_i<\mu(i)<\lambda$ and $2^{\mu(i)}>2^{\rho_i}$. Then the $\mu(i)$ are
strictly increasing, cofinal in $\lambda$, at least $\kappa$ (so infinite),
and the powers $2^{\mu(i)}$ are strictly increasing. Since
$2^{\mu(i)}\ge\mu(i)^+>\mu(i)$, $\sup_i2^{\mu(i)}\ge\sup_i\mu(i)=\lambda$.
The index set of $\chi$ is infinite of size at most $\lambda$ and every term
is at least $1$, so $\chi=|\{\mu:\mu<\lambda\}|\cdot\sup_{\mu<\lambda}2^\mu$,
and the second factor is at least $\lambda$, so $\chi=\sup_{\mu<\lambda}2^\mu$.
Every cardinal $\mu<\lambda$ is at most some $\mu(i)$, so this supremum is
$\sup_i2^{\mu(i)}$, and $\sum_{i<\kappa}2^{\mu(i)}=\kappa\cdot\sup_i2^{\mu(i)}$
equals that supremum because the supremum is at least $\lambda>\kappa$. So a
set of size $\chi$ splits into blocks $X_i$ with $|X_i|=2^{\mu(i)}$. For the
bound: if $J\subseteq\kappa$ has $|J|<\kappa$, then, $\kappa$ being regular,
$J\subseteq i_0$ for some $i_0<\kappa$, and
$|H|\le\sum_{i<i_0}|H\cap X_i|\le\sum_{i<i_0}\mu(i)\le|i_0|\cdot\mu(i_0)$;
both factors are below $\lambda$ and $\mu(i_0)$ is infinite, so the product
is $\max(|i_0|,\mu(i_0))<\lambda$ (for $i_0=0$ the sum is $0$). The page's
stated reason, "since $\lambda$ is a limit cardinal", is not the operative
one (Finding F2), but the inequality holds.

**W3: the color $1+\nu$ case in S2.** Re-derivation. Let $H\subseteq\lambda$,
$|H|=\rho_\nu$, with $d$ constantly $1+\nu$ on $[H]^2$. Two points of $H$ in
one block $X_i$ would form a pair of color $0\ne1+\nu$, so $|H\cap X_i|\le1$
for every $i$, the block index map is injective on $H$, and its image
$J\subseteq\kappa$ has $|J|=\rho_\nu$. For $i\ne j$ in $J$, with $x_i$, $x_j$
the unique points of $H$ in $X_i$, $X_j$, $d(\{x_i,x_j\})=c(\{i,j\})=1+\nu$;
so $c$ is constantly $1+\nu$ on $[J]^2$, which the witness excludes (and
when $\rho_\nu>\kappa$ no such $J$ exists at all). The color $0$ case is W2's
small-$J$ argument with $|X_i|<\lambda$ in place of the Sierpiński bound:
fewer than $\operatorname{cf}\lambda$ sets of size below $\lambda$ cannot
cover $H$, so $|J|=\kappa$, and one point per block shows $c$ constantly $0$
on $[J]^2$. Composition: both cases together are exactly the negative
relation for $\lambda$ with $1+\gamma$ colors.

## Strongest attack

**S1.** Attack: find a hypothesis of the lemma that S1's list does not
supply. Candidates tried: (a) the lemma's $\kappa$ must be infinite for the
type count (B) ($\aleph_0\le\kappa$), supplied; (b) $|j|\le\mu(j)$ in the
growth computation, which the theorem page draws from Step 1 and S1 must
supply on its own: it follows from $j<\kappa\le\mu(0)\le\mu(j)$; (c) the
regularity of $\lambda_i$, needed in W1 and in the lemma's proof, supplied
by $\lambda_i$ being a successor; (d) the infinitude of every $\mu(i)$,
needed for $(2^{\mu(i)})^{\mu(i)}=2^{\mu(i)}$, supplied; (e) the lemma's
$1\le n_i$, not stated (F4, a note). A second attack: does (1B) with $n=2$
really need no parameter sequence? The lemma's (1B) quantifies over every
finite $\bar a$ of the length that fills the remaining places, which for
$n=2$ is the empty sequence; the lemma page's proof of (1B) uses the
patterns $(b,x)$ over $E_\beta$ and $(x,a^*_\beta)$ over $D_\alpha$, both
legitimate with no parameters. The attack fails.

**S2.** Attack: break the transfer with a witness $c$ whose excluded sizes
exceed $\kappa$, or with $\gamma$ infinite so that $1+\gamma$ colors and
$1+\nu$ indexing might misalign. Neither bites: $\nu\mapsto1+\nu$ is a
bijection from $\gamma$ onto the nonzero colors below $1+\gamma$, and
$\rho_\nu>\kappa$ only strengthens the contradiction. A second attack: with
$|J|<\kappa$, is it needed that $J$ be bounded? No; the covering fact uses
only $|J|<\operatorname{cf}\lambda$. The attack fails.

**S3.** Attack: the survey's remark might be conditional, might concern
regular $\kappa$ only, or might read $\to$ where the section reads
$\not\to$. On the page image the strokes are present in all three arrows of
the sentence, the remark is unconditional and printed for arbitrary
$\kappa$, and S2 restricted to $\gamma=1$, $\rho_0=\aleph_1$ is that
sentence for singular $\kappa$; for regular $\kappa$ the sentence is a
tautology. The attack fails.

**S4.** Attack: exhibit a large homogeneous set for $d$ by concentrating
$H$ inside few blocks. Inside one block, $e_i$ caps a homogeneous set at
$\mu(i)$, and $\sum_{i<i_0}\mu(i)<\lambda$ for every $i_0<\kappa$ by W2, so
$H$ must meet $\kappa$ blocks and then $c$ is defeated. A second attack:
break the identification of $\chi$ when every $2^\mu$ is below $\lambda$
(strong limit case): then $\chi=\lambda$ and S4 asserts
$\lambda\not\to(\lambda)^2_2$, true for every singular $\lambda$; the proof's
blocks and Sierpiński colorings still apply. A third attack: choose the
$\mu(i)$ with a finite first term so that (S) does not apply to $X_0$; the
proof forecloses this by invoking Step 1, whose $\rho_i\ge\kappa$ forces
$\mu(i)\ge\kappa$; the statement of the choice omits this bound (F1). The
attack fails; the omission is presentational.

## Premises

- **Lemma 1.1** ([[research/erdos_1219/lemma_1_1_reconstruction|page]],
  held, read in full). Interface consumed by S1: hypotheses ($\kappa$
  infinite regular; $\lambda_i$ regular strictly increasing; $\mu(i)$
  cardinals; $|A_i|=\lambda_i$; $F_i:A^{n_i}\to\chi$ with $1\le n_i<\omega$;
  growth $\lambda^j<\lambda_j$ and $2^{\chi+\kappa}<\lambda_0$; (H)) and
  conclusion ($a^*_i\in A_i$, $B_i\subseteq A_i$ with $|B_i|\le\mu(i)$,
  (1A), (1B), (2)). Standing: author-recorded reconstruction, reviewed as of
  2026-09-28T05:03:27Z; used within its hypotheses (W1).
- **Theorem 1.2** ([[research/erdos_1219/theorem_1_2_reconstruction|page]],
  held, read in full). Consumed: Step 1 (the choice of the $\mu(i)$, used
  by S4 without $\mu_0$), Step 2(a) (monotonicity of $\lambda_i$), Step 5
  (the growth verification), Step 6 (the two-place canonical form), the
  sum formula (infinite index set, terms at least $1$), the standard facts
  it lists, and the imported (S): for every infinite $\mu$,
  $2^\mu\not\to(\mu^+)^2_2$ (Sierpiński 1933, not held, taken as an
  external premise at the reading depth the theorem page records:
  statement only). Standing as for the lemma page; each item re-derived
  above where S1 or S4 relies on it.
- **Corollary 1.3**
  ([[research/erdos_1219/corollary_1_3_reconstruction|page]], held, read in
  full). Not consumed by the Tools section.
- **Komjáth (2025)**, held PDF, printed p. 419 = PDF p. 2, read on the page
  image and the text layer, and the held conversion at the same place;
  claims checked: the Problem 4 remark (S3) and the survey's notation
  $\lambda\to(\kappa_\nu)^r_\gamma$ for a family of targets (F3).
- **Shelah (1975)**, held scan without text layer; not consulted, the
  reconstruction pages standing in for it.
- **Standard cardinal arithmetic**, as listed on the theorem page: successor
  cardinals are regular; $(2^\mu)^\mu=2^\mu$ for infinite $\mu$; a union of
  fewer than $\operatorname{cf}\theta$ sets of size below $\theta$ has size
  below $\theta$; a subset of $\kappa$ of size below the regular $\kappa$ is
  bounded; Cantor's $2^\mu\ge\mu^+$.

## Findings

**F1 (suggested).** Location: (T3) proof, "Choose cardinals $\mu(i)<\lambda$
($i<\kappa$), strictly increasing and cofinal in $\lambda$, with $2^{\mu(i)}$
strictly increasing; Step 1 of the theorem page does this from the
non-constancy alone, the bound $\mu_0$ being unnecessary here." Defect: the
listed properties do not include infinitude, but the next sentences apply
(S), whose hypothesis is an infinite exponent, to every block. Witness: a
sequence satisfying the three listed properties may start with a finite
$\mu(0)$ (for instance $\mu(0)=5$), for which (S) says nothing. The proof is
nonetheless complete as written, because Step 1 as invoked keeps
$\kappa$ in its maximum and returns $\mu(i)\ge\kappa$. Proposed
replacement: "strictly increasing, cofinal in $\lambda$, each at least
$\kappa$ (so infinite), with $2^{\mu(i)}$ strictly increasing; Step 1 of the
theorem page does this from the non-constancy and $\kappa<\lambda$ alone,
the bound $\mu_0$ being unnecessary here."

**F2 (note).** Location: (T3) proof,
"$|H|\le\sum_{i<i_0}\mu(i)\le|i_0|\cdot\mu(i_0)<\lambda$, since $\lambda$ is a
limit cardinal". Defect: the reason given is not the one that yields the
last inequality; it holds because $|i_0|<\kappa<\lambda$
and $\mu(i_0)<\lambda$ with $\mu(i_0)$ infinite, so the product is the
larger factor. Proposed replacement: "$<\lambda$, both factors being below
$\lambda$ and $\mu(i_0)$ infinite". In the same proof, "the powers are
cofinal in $\lambda$" is loose when some $2^{\mu(i)}\ge\lambda$; what is
used and true is $\sup_i2^{\mu(i)}\ge\lambda$.

**F3 (note).** Location: (T2) statement,
"$\kappa\not\to(\kappa,(\rho_\nu)_{\nu<\gamma})^2$". Defect: the page's Scope
paragraph defines $(\rho)_\gamma$ for repetitions of one target and the
theorem page defines the relation for finitely many colors; the family form
with $\gamma$ possibly infinite is used without a definition. It is the
survey's notation of p. 419, and the proof uses exactly the natural reading
(colors $0$ and $1+\nu$, $\nu<\gamma$). Proposed replacement: one clause in
the Scope paragraph, "$(\rho_\nu)_{\nu<\gamma}$ for a family of targets, one
per color $1+\nu$, as in the survey's §1".

**F4 (note).** Location: (T1), "let $F:A^n\to2$ be a function of finitely
many places". Defect: the lemma's interface requires $1\le n_i$; a
zero-place $F$ is a constant and the canonical clauses are vacuous for it.
Proposed replacement: "of $n\ge1$ places".

No required correction.

## Verdict

- **S1 (T1):** refutation-failed. Every hypothesis of Lemma 1.1 is
  available from the listed assumptions, re-derived in W1, and the
  conclusion quoted is the lemma's.
- **S2 (T2):** refutation-failed. The lifting of a witness from the
  cofinality through a block decomposition is re-derived in W3.
- **S3 (attribution):** refutation-failed. The remark is printed on p. 419
  as characterized, confirmed on the page image.
- **S4 (T3):** refutation-failed. The construction and both cases are
  re-derived in W2 and "Strongest attack"; the infinitude of the exponents
  that (S) needs is supplied by the invoked Step 1 (F1).
- **S5:** not a claim.

Limitations. The review covers the Tools section and the interfaces it
draws from the reconstruction pages; it does not re-verify those pages,
which are premises at their recorded standing, and it does not examine the
later sections' uses of (T1)--(T3), including the use of (T2) announced for
Problem 1218, which lies outside the commissioned read set. The external
premise (S) is relied on as an identified literature statement at the
reading depth the theorem page records. This focused review assigns no tier
and changes no status.
