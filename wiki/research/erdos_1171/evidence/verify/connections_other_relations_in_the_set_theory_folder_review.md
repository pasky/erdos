---
name: research/erdos_1171/evidence/verify/connections_other_relations_in_the_set_theory_folder_review
title: "Independent review of the connections section: Other relations in the set-theory folder"
desc: |
  Verdicts: the exponent-3 obstruction for Problems 70 and 1218 (S3) is
  refuted-as-stated; the mechanism's requirements (S1), the obstructions for
  Problems 1170, 1172 and 1219 (S2, S4) and the conditional corollary for
  Problem 1220 (S5) are refutation-failed; the cross-reference (S6) and the
  closing sentence (S7) are not claims. One required correction, two
  suggested corrections and three notes.
created: 2026-09-28T19:01:14Z
updated: 2026-09-28T19:01:14Z
---

***

## Subject and independence

**Role and independence.** The reviewer is an independent reviewer working
in a fresh context from the commissioning assignment alone, charged with
refutation. The reviewer took no part in writing the connections page, the
reconstruction pages or the folder index, and opened none of the folder's
existing reviews or grades.

**Subject.** Page `wiki/research/erdos_1171/connections.md` as it stood on
2026-09-28T13:50:48Z, section
"## Other relations in the set-theory folder", lines 658--677: the H2 heading
at line 658 through line 677, the last line before "## Outcomes" at line 678.
The assignment named no lead page beyond
[[research/erdos_1171/connections|the connections page]] itself.

**Reading.** In full: the section; the page's frontmatter, scope paragraph
and "## Tools" section (lines 1--124), taken as inputs whose proofs another
reviewer checks and whose interfaces are confirmed below at each use;
[[research/erdos_1171/lemma_2_1_reconstruction|the Lemma 2.1 page]] and
[[research/erdos_1171/theorem_3_1_reconstruction|the Theorem 3.1 page]], as
premises at their reviewed standing; the `**Statement.**` paragraphs, and
nothing else, of the six problem pages
[[problems/set_theory/E1170/_index|E1170]], [[problems/set_theory/E1172/_index|E1172]],
[[problems/set_theory/E0070/_index|E0070]], [[problems/set_theory/E1218/_index|E1218]],
[[problems/set_theory/E1219/_index|E1219]] and [[problems/set_theory/E1220/_index|E1220]];
`docs/verification.md` sections "Grading and claim standing", "Audit
checklist" (the shared list and the Erdos-specific list) and "Whole-claim
report"; `docs/approach_vetting.md`; `docs/evidence.md` section "Source
fidelity"; `docs/math_authoring.md`. Not read: the folder index, everything
under `evidence/`, the page's other problem sections, and the cross-referenced
page `research/erdos_1219/connections`, which lies outside the commissioned
read set. The section invokes no library source theorem, so no library card
or PDF was opened.

**Exposures.** Three incidental ones, none used. A heading listing of the six
problem pages displayed their one-line `**Status.**` fields; a heading listing
of the connections page displayed the titles of its other sections; and a
listing of the working tree showed the file names, not the contents, of other
reviewers' reports. Nothing below depends on any of them.

## Restatement

Notation is that of the Tools section: relations are read for colorings of
the pairs of a set of ordinals, a witness for a negative relation is a
coloring refuting it, and the resource is the ordinal or cardinal to the left
of the arrow. The section asserts the following.

- **S1.** The mechanism (T3)--(T5) applies only to a relation whose color-$0$
  target equals the ambient order type, or to a descending chain of relations
  as in (T4), with targets in the other colors that are given in advance and
  not tied to the ambient type.
- **S2.** The mechanism gives nothing for Problem 1170, whether it is
  consistent that $\omega_2\to(\alpha)^2_2$ for every $\alpha<\omega_2$, nor
  for Problem 1172, which the section describes by the one relation
  $\omega_2\to(\omega_1+\omega)^2_2$, because these relations are balanced,
  with equal targets, and both targets lie strictly below the resource
  $\omega_2$.
- **S3.** The mechanism gives nothing for Problem 70, whether
  $\mathfrak{c}\to(\beta,n)^3_2$ for every countable ordinal $\beta$ and every
  finite $n\ge2$, with $\mathfrak{c}$ the initial ordinal of the continuum,
  nor for Problem 1218, whether under GCH and for
  $\lambda=\aleph_{\omega_{\omega+1}+1}$ the negative relation
  $\lambda\not\to(\lambda,4,4,\ldots)^3$ holds with countably infinitely many
  colors carrying the target $4$, because the exponent of both is $3$.
- **S4.** The mechanism gives nothing for Problem 1219, whether
  $\sum_k 2^{\aleph_{n_k}}\to(\aleph_\omega)^2$ for the sequences $(n_k)$ the
  problem specifies, because it is a balanced relation between cardinals.
- **S5.** For Problem 1220, restated by the section as
  "$\lambda\to(\lambda,\aleph_1)^2$ for singular $\lambda$", (T3) with
  $\alpha=\lambda$ and $H_1=\cdots=H_k=\aleph_1$ turns the asked relation into
  $\lambda\to(\lambda,\aleph_1,\ldots,\aleph_1)^2_{k+1}$ for every finite
  $k\ge1$; this is a corollary of a positive answer and no help toward one.
- **S6.** The canonization mechanism on the Problem 1219 connections page
  handles the strong-limit case of Problem 1220 and records the obstruction
  beyond that case.
- **S7.** None of the problems named is pursued on the page.

## Checklist

- **Quantifiers and scope.** Two lapses, neither fatal. Problem 1172's
  statement lists five relations, three of them unbalanced; the section names
  one and calls the problem's relations balanced (F2). Problem 1220 restricts
  $\lambda$ by two hypotheses that the section drops, and the unrestricted
  sentence is false for countable cofinality (F3). S5 survives both, since
  the deduction holds for each $\lambda$ separately, and its unquantified $k$
  is every finite $k\ge1$, as (T3) states.
- **Circularity.** None. S5 assumes the asked relation and says so; no
  obstruction sentence assumes its own conclusion.
- **Model and convention changes.** One defect. S3 treats the exponent as a
  change of setting that blocks the mechanism; the proofs behind (T1)--(T5)
  never use the exponent, so nothing is blocked (F1, W1). The passage from
  the cardinal relations of Problems 1219 and 1220 to the order-type relations
  of the Tools section is unstated but valid, because the resources and
  targets are initial ordinals (F5, W2).
- **Finite and statistical overreach.** One defect. The mechanism's
  inductions run over a finite number of colors; S1 omits this requirement,
  and for Problem 1218 it is the operative obstruction (F1). No statistical
  content.
- **Uniformity.** Not applicable: no constants, bounds or error terms. The
  corollary in S5 is stated for each finite $k$, and (T3) delivers exactly
  that.
- **Extremal conclusions.** Not applicable: no extremal statement.
- **Consequences and composition.** S5's deduction is re-derived and holds
  (W2). S3's "does not apply" does not follow from its stated reason, and the
  section's own criterion S1 does not exclude Problem 1218 (F1, W1). S2 and S4
  hold on the ground that the color-$0$ target lies below the resource (W3);
  the word "balanced" carries no weight (F4). S6 rests on a page outside the
  read set (F6).
- **Computation.** Not applicable: the section computes nothing.
- **Reproduction.** Not applicable: no rerun instructions or coverage claims.
- **Source and verdict fidelity.** The problem statements were checked
  against the Statement paragraphs of the problem pages. Problems 1170, 70,
  1218 and 1219 are characterized correctly as to shape; Problem 1172 is
  reduced to one of five relations (F2); Problem 1220's hypotheses are
  dropped (F3). The section quotes no source theorem and characterizes no
  verdict. What it attributes to the Problem 1219 connections page was not
  checked (F6).

## Weakest steps

**W1. The exponent is not a hypothesis of the mechanism.** Fix $r\ge1$. For
a set $X$ of ordinals let $[X]^r$ be the set of its $r$-element subsets, and
read $\gamma\to(\beta,H_1,\ldots,H_k)^r_{k+1}$ as: every coloring of
$[\gamma]^r$ with the colors $0,\ldots,k$ has a subset of type $\beta$
homogeneous in color $0$ or, for some $i$, a subset of type $H_i$ all of
whose $r$-subsets have color $i$. For $r=2$ and order-type targets this is
the relation of the Tools section; the two problems at issue have ordinal
targets, so graph targets are not needed. The four tools re-derived:

1. *Transport.* Let $\pi:\gamma\to Y$ be an order isomorphism. Then
   $p\mapsto\pi[p]$ is a bijection of $[\gamma]^r$ onto $[Y]^r$, and $\pi$
   carries a subset of type $\beta$ onto a subset of type $\beta$. Given a
   coloring $d$ of $[Y]^r$, put $d'(p)=d(\pi[p])$. A set $X\subseteq\gamma$
   homogeneous under $d'$ in color $i$ has image $\pi[X]$ of the same type,
   and every $r$-subset of $\pi[X]$ is the image of an $r$-subset of $X$, so
   $\pi[X]$ is homogeneous under $d$ in color $i$. The relation for $\gamma$
   thus holds for colorings of $[Y]^r$.
2. *Restriction, weakening, unused colors.* If $Y\subseteq\gamma'$ has type
   $\gamma$, a coloring of $[\gamma']^r$ restricts to $[Y]^r$, and a subset
   of $Y$ homogeneous under the restriction is homogeneous under the original
   coloring with the same type, since $Y$ carries the inherited order. A set
   of type $\beta$ has a subset of type $\beta'$ for every $\beta'\le\beta$.
   A coloring with the colors $0,1$ is a coloring with the colors
   $0,\ldots,k$ in which $2,\ldots,k$ are unused, and a set with at least $r$
   elements has an $r$-subset, so it is not homogeneous in an unused color;
   hence a witness for $\gamma\not\to(\beta,H)^r$ is a witness for
   $\gamma\not\to(\beta,H,\ldots,H)^r_{k+1}$ for every finite $k$, and
   equally for countably many colors.
3. *Descent.* Suppose $\gamma_{j-1}\to(\gamma_j,H_j)^r$ for $j=1,\ldots,k$.
   Then $\gamma_0\to(\gamma_k,H_1,\ldots,H_k)^r_{k+1}$. Induction on $k$;
   $k=1$ is the hypothesis. For the step let
   $c:[\gamma_0]^r\to\{0,\ldots,k+1\}$ and let $c'$ send the colors $0$ and
   $k+1$ to $0$ and fix the others. The case $k$ applied to $c'$ gives either
   $j\le k$ and a subset of type $H_j$ all of whose $r$-subsets have
   $c'$-color $j$, hence $c$-color $j$, as $c'$ and $c$ agree on the colors
   $1,\ldots,k$; or a set $Y\subseteq\gamma_0$ of type $\gamma_k$ with
   $c(p)\in\{0,k+1\}$ for every $p\in[Y]^r$. In the second case the relation
   $\gamma_k\to(\gamma_{k+1},H_{k+1})^r$, transported to $Y$ by item 1 and
   applied to the two-coloring of $[Y]^r$ that sends $c$-color $k+1$ to $1$
   and $c$-color $0$ to $0$, gives a subset of $Y$ of type $\gamma_{k+1}$
   homogeneous in $c$-color $0$ or a subset of type $H_{k+1}$ homogeneous in
   $c$-color $k+1$. No step uses the value of $r$.
4. *Witness extraction.* Let $c:[\alpha]^r\to\{0,\ldots,k\}$ have no subset
   of type $\alpha$ homogeneous in color $0$ and no subset of type $H$
   homogeneous in a color $j\ge1$. Then there are $Y\subseteq\alpha$ of type
   $\alpha$ and $j\ge1$ such that the two-coloring of $[Y]^r$ sending
   $c$-color $j$ to $1$ and every other color to $0$ has no color-$0$ subset
   of type $\alpha$ and no color-$1$ subset of type $H$; by item 1 it
   witnesses $\alpha\not\to(\alpha,H)^r$. Induction on $k$; for $k=1$ take
   $Y=\alpha$ and $j=1$. For $k\ge2$ let $c'$ merge the colors $0$ and $k$.
   If $c'$ has a color-$0$ subset $Y$ of type $\alpha$, then $c$ takes only
   the values $0$ and $k$ on $[Y]^r$, and with $j=k$ the two-coloring has no
   color-$0$ set of type $\alpha$, since $c$ has none, and no color-$1$ set
   of type $H$, since $c$ has none in color $k$. Otherwise $c'$ has no
   color-$0$ set of type $\alpha$ and, agreeing with $c$ on the colors
   $1,\ldots,k-1$, no set of type $H$ homogeneous in one of them, so the
   induction hypothesis gives $Y$ and $j\le k-1$, and the two-colorings built
   from $c'$ and from $c$ with this $j$ coincide. Again no step uses $r$.

*Problem 1218.* Take $r=3$, $\alpha=\lambda=\aleph_{\omega_{\omega+1}+1}$ and
$H=4$. Item 3 in its constant case $\gamma_0=\cdots=\gamma_k=\lambda$ and
item 2 give, for every finite $k\ge1$,

$$
\lambda\to(\lambda,4)^3
\iff
\lambda\to(\lambda,\underbrace{4,\ldots,4}_{k})^3_{k+1},
$$

and item 4 adds that a finite-color witness contains a two-color witness on
a subset of type $\lambda$. Item 2 gives, with no induction at all, that
$\lambda\not\to(\lambda,4)^3$ implies the relation Problem 1218 asks,
$\lambda\not\to(\lambda,4,4,\ldots)^3$ with countably many colors. All of
this holds in ZFC, hence under GCH. What the tools do not give is the reverse
step from a witness with countably many colors to one with two: items 3 and
4 run over finite $k$ and never reach $\omega$ colors; merging the colors
$j\ge1$ of such a witness into one color can create a homogeneous $4$-set in
the merged color (a $4$-set whose four triples carry four distinct colors),
and merging color $0$ with infinitely many other colors can create a
color-$0$ set of type $\lambda$. The countable color count, not the exponent,
is what the mechanism cannot pass. On the section's own criterion S1 the
relation has the mechanism's shape, so S3's reason is wrong for it and its
conclusion is wrong for the finite-color forms.

*Problem 70.* Take $r=3$ with resource $\mathfrak{c}$. The color-$0$ target
$\beta$ is countable, so $\beta<\omega_1\le\mathfrak{c}$ lies below the
resource; the constant case of item 3 and item 4 are unavailable for the
reason of W3, and the chain form of item 3 with the asked relation as its
first link needs further relations $\beta\to(\beta',n')^3$ among countable
ordinals and yields only consequences of the kind S5 records. S3's conclusion
for Problem 70 therefore stands, on the ground the section gives for Problem
1170 and not on the exponent.

**W2. The corollary for Problem 1220.** (T3) is invoked with $\alpha=\lambda$
and $H_1=\cdots=H_k=\aleph_1$; its hypothesis $\alpha\to(\alpha,H_i)^2$ for
$i=1,\ldots,k$ is the asked relation, used $k$ times, so the interface
matches. Re-derived directly: given $c:[\lambda]^2\to\{0,\ldots,k+1\}$, merge
the colors $0$ and $k+1$; the case $k$ gives a color-$j$ copy of $\omega_1$
for some $j\le k$, or a set $Y$ of type $\lambda$ on which $c$ takes the
values $0$ and $k+1$; on $Y$ the asked relation, transported by (T1), gives a
color-$0$ set of type $\lambda$ or a color-$(k+1)$ copy of $\omega_1$. The
problem's relation is between cardinals: a color-$0$ homogeneous set of
cardinality $\lambda$ or a color-$1$ homogeneous set of cardinality
$\aleph_1$. The bridge to the order-type reading holds because $\lambda$ and
$\aleph_1$ are initial ordinals: a subset of the initial ordinal $\lambda$ of
cardinality $\lambda$ has order type at most $\lambda$, being a subset, and
at least $\lambda$, since every ordinal below $\lambda$ has cardinality below
$\lambda$, so its type is exactly $\lambda$; a set of ordinals of cardinality
$\aleph_1$ has order type at least $\omega_1$ and so contains a subset of
type $\omega_1$, and a set of type $\omega_1$ has cardinality $\aleph_1$. The
same bridge reads the $(k+1)$-color conclusion back as a cardinal relation.
The deduction uses nothing about $\lambda$ beyond the asked relation, so it
holds for every cardinal $\lambda$, singular or not, with or without the
problem's hypotheses (F3). "No help" is correct in a precise sense: by (T2)
the $(k+1)$-color relation implies the two-color one (colors left unused), so
the corollary is equivalent to the hypothesis and neither direction offers a
new attack.

**W3. What a color-$0$ target below the resource blocks.** Let
$\gamma\to(\beta,H)^2$ be asked with $\beta<\gamma$; Problems 1170, 1172 and
1219 have this shape with $H=\beta$, and Problem 70 has it with exponent $3$.
The merging induction of (T3) reaches, after one merge, a set $Y$ of type
$\beta$ on which the coloring takes two values, and to continue it would need
a relation with resource $\beta$; the asked relation concerns $\gamma$ and
says nothing about $\beta$. The Lemma 2.1 page records exactly this in its
check "Where the hypothesis is used". Extraction fails the same way: from a
witness $c$ of $\gamma\not\to(\beta,H,H)^2_3$, merging the colors $0$ and $2$
gives $c'$, and either $c'$ witnesses $\gamma\not\to(\beta,H)^2$ or $c'$ has
a color-$0$ set $Y$ of type $\beta$ on which $c$ takes the values $0$ and $2$
with no color-$0$ set of type $\beta$ and no color-$2$ copy of $H$, a witness
for $\beta\not\to(\beta,H)^2$, a relation with a different resource. So a
three-color negative relation is not reduced to the two-color one asked, and
there is no equivalence to record. Whether the two targets are equal plays no
part in either failure. What remains is the consequence direction of (T4): in
any model of the asked relation together with a second link
$\beta\to(\gamma_2,H_2)^2$, the relation $\gamma\to(\gamma_2,\beta,H_2)^2_3$
holds. For Problem 1170 and infinite $\alpha$ the second link
$\alpha\to(\omega,\omega)^2$ holds by Ramsey's theorem on a subset of type
$\omega$ with (T2), so any model of $\omega_2\to(\alpha)^2_2$ satisfies
$\omega_2\to(\omega,\alpha,\omega)^2_3$. This is a corollary of the kind S5
records for Problem 1220 and gives no more help than that one.

## Strongest attack

- **S1.** The attack looked for a hypothesis of (T3)--(T5) that the sentence
  omits, or a condition it names that the tools do not need. The tools need a
  finite number of colors, since both inductions run over $k$, and S1 omits
  this; they do not need exponent $2$ (W1). S1 survives as a list of
  necessary conditions; its omission is the root of the defect in S3 (F1).
- **S2.** The attack tried to build, for a balanced relation
  $\gamma\to(\beta,\beta)^2$ with $\beta<\gamma$, either a many-color
  corollary by the constant induction or a two-color witness from a
  three-color witness; both fail for the reason re-derived in W3. The only
  output is the consequence direction of (T4), which is not a reduction. The
  non-applicability claim survives on the ground "both targets below the
  resource", which holds for Problem 1170 and for all five relations of
  Problem 1172, including the three unbalanced ones the section does not
  mention: $\omega_2<\omega_3$, $\omega_1+2<\omega_3$,
  $\omega_2+\omega_1<\omega_3$, $\omega_2+\omega<\omega_3$, and
  $\omega_1^{\omega+2}+2<\omega_2$, since $\omega_1^{\omega+2}$ is a countable
  supremum and product of ordinals of cardinality $\aleph_1$. The description
  of Problem 1172 is corrected in F2; the idle word "balanced" is noted in F4.
- **S3.** The attack succeeded. W1 re-derives transport, restriction,
  descent and witness extraction for an arbitrary exponent and applies them
  at exponent $3$: for Problem 1218 the finite-color negative relations are
  equivalent to $\lambda\not\to(\lambda,4)^3$, which in turn implies the asked
  countable-color relation by (T2); the obstruction is the countable color
  count. For Problem 70 the conclusion survives on a different ground.
- **S4.** As for S2, with resource $\kappa=\sum_k 2^{\aleph_{n_k}}$ and
  target $\aleph_\omega$: the problem's hypothesis
  $2^{\aleph_{n_0}}>\aleph_\omega$ puts the target below the resource, and
  the bridge of W2 reads the cardinal relation as the order-type relation
  $\kappa\to(\omega_\omega,\omega_\omega)^2$ on the initial ordinal
  $\kappa$. The claim survives; "balanced" again does no work (F4).
- **S5.** The attack checked the interface of (T3), the unstated bridge from
  cardinals to order types, the possibility that the many-color form is
  strictly stronger than the asked relation (it is not, by (T2)), and the
  section's restatement of the problem. The deduction survives (W2); the
  restatement drops two hypotheses and is false without them (F3); the bridge
  is a note (F5).
- **S6.** Not attacked: the page it describes lies outside the read set
  (F6).
- **S7.** Not a claim.

## Premises

- **(T1)--(T5) and the displayed equivalence**, Tools section of the
  connections page, lines 32--124, read in full; author-recorded. Interfaces
  confirmed at each use: (T3) in S5 with $\alpha=\lambda$ an initial ordinal
  and $H_i=\omega_1$; (T2) for unused colors and for restriction in W1--W3;
  (T4) and (T5) re-derived in W1 in exponent-free form, because S3 turns on
  the exponent. Their exponent-$2$ proofs on the page are another reviewer's
  charge and were not graded here.
- **Lemma 2.1 reconstruction**,
  [[research/erdos_1171/lemma_2_1_reconstruction|the Lemma 2.1 page]], read in
  full; independently reviewed as it stood on 2026-09-28T05:03:27Z with
  corrections applied since, per the assignment, and treated as established
  at that standing.
  Used: the relation convention, facts 1 and 2 (transport and relabeling),
  and the checks "Where the hypothesis is used" and "What the number $3$
  contributes".
- **Theorem 3.1 reconstruction**,
  [[research/erdos_1171/theorem_3_1_reconstruction|the Theorem 3.1 page]],
  read in full at the same standing; the section uses nothing from it beyond
  the restriction remark that (T2) restates.
- **Problem statements**: the Statement paragraphs of the six problem pages
  named above, read in full and nothing else on those pages.
- **External theorems**: the section invokes none. This report uses Ramsey's
  theorem once, in W3, for an illustration of (T4)'s consequence direction;
  it is classical and was not read from a held source. The definition of an
  $\aleph_0$-inaccessible cardinal in Problem 1220 was not read from a source
  (F3, F6).
- **Not read**: `research/erdos_1219/connections`, which S6 cites.

## Findings

**F1 (required).** Location: lines 665--667, "nor to Problem 70 and Problem
1218, whose exponent is $3$;", together with the criterion sentence at lines
660--661. Defect: the exponent is not an obstruction, since every proof
behind (T1)--(T5) is exponent-free (W1); and Problem 1218's relation has the
shape S1 describes, a color-$0$ target equal to the ambient type and a fixed
target in every other color, so the criterion of S1 does not exclude it.
What actually applies and what actually blocks: for every finite $k\ge1$,
$\lambda\not\to(\lambda,4,\ldots,4)^3_{k+1}$ is equivalent to
$\lambda\not\to(\lambda,4)^3$, and $\lambda\not\to(\lambda,4)^3$ implies the
asked relation with countably many colors by (T2); the induction does not
reach $\omega$ colors, and that is the obstruction. For Problem 70 the
operative obstruction is the color-$0$ target $\beta<\omega_1\le\mathfrak{c}$
below the resource, as for Problem 1170. Witness: W1. Proposed replacement:
in the criterion sentence add "finitely many colors" to the list of what the
mechanism needs; replace the clause by "Problem 70, $\mathfrak{c}\to(\beta,n)^3$
for countable $\beta$ and finite $n$, has its color-$0$ target below the
resource, the obstruction of Problem 1170; its exponent is no obstruction,
since the proofs of (T1)--(T5) never use the exponent. Problem 1218,
$\lambda\not\to(\lambda,4,4,\ldots)^3$ with countably many colors under GCH,
has the mechanism's shape in exponent $3$: for every finite $k$ the negative
relation with $k$ colors carrying $4$ is equivalent to
$\lambda\not\to(\lambda,4)^3$, which implies the asked relation by (T2); the
induction does not reach countably many colors, and that, not the exponent,
is the obstruction. Whether $\lambda\not\to(\lambda,4)^3$ holds is not
examined here."

**F2 (suggested).** Location: lines 660--665, "Problem 1172, whose relations
... $\omega_2\to(\omega_1+\omega)^2_2$ are balanced with both targets below
the resource". Defect: the problem page states five relations under GCH,
$\omega_3\to(\omega_2,\omega_1+2)^2$,
$\omega_3\to(\omega_2+\omega_1,\omega_2+\omega)^2$,
$\omega_2\to(\omega_1^{\omega+2}+2,\omega_1+2)^2$, and the consistency of
$\omega_2\to(\omega_1+\omega)^2_2$ or of $\omega_2\to(\xi)^2_2$ for all
$\xi<\omega_2$; the section names one and describes the problem's relations
as balanced, which three of them are not. The conclusion survives, since all
five have both targets below the resource (see S2 under Strongest attack).
Proposed replacement: "Problem 1172, whose five relations under GCH all have
both targets below the resource".

**F3 (suggested).** Location: lines 669--670, "For Problem 1220,
$\lambda\to(\lambda,\aleph_1)^2$ for singular $\lambda$". Defect: the problem
page asks the relation for a singular cardinal $\lambda$ such that $\lambda$
and $\mathrm{cf}(\lambda)$ are both $\aleph_0$-inaccessible; the section drops
both hypotheses. The unrestricted sentence is false: for singular $\lambda$
of countable cofinality write $\lambda=\sup_n\lambda_n$ with $\lambda_0=0$
and $\lambda_n$ increasing, and color a pair by $0$ when both elements lie in
the same block $[\lambda_n,\lambda_{n+1})$ and by $1$ otherwise; a color-$0$
homogeneous set lies in one block and has cardinality, hence type, below
$\lambda$, and a color-$1$ homogeneous set has at most one element per block
and type at most $\omega$, so $\lambda\not\to(\lambda,\omega+1)^2$ and a
fortiori $\lambda\not\to(\lambda,\aleph_1)^2$. On the usual reading of
$\aleph_0$-inaccessible, $\mu^{\aleph_0}<\kappa$ for every $\mu<\kappa$, which
$\aleph_0$ fails, the problem's hypothesis on $\mathrm{cf}(\lambda)$ excludes
this case. The conditional deduction S5 is unaffected, since it holds for
each $\lambda$ separately (W2). Proposed replacement: "For Problem 1220,
$\lambda\to(\lambda,\aleph_1)^2$ for a singular cardinal $\lambda$ with
$\lambda$ and $\mathrm{cf}(\lambda)$ both $\aleph_0$-inaccessible".

**F4 (note).** Location: lines 664 and 668, "balanced with both targets
below the resource" and "a balanced cardinal relation". The word "balanced"
names no obstruction: (T3) and (T5) fail because the color-$0$ target lies
below the resource, whether or not the targets are equal (W3), and (T4) with
the asked relation as its first link gives conditional many-color
consequences for Problems 1170, 1172 and 1219 of the same kind that S5
records for Problem 1220. Proposed replacement: state the one operative
ground, "whose color-$0$ targets lie below the resource, so that (T3) and
(T5) do not apply and (T4) gives only conditional corollaries", for the three
problems together.

**F5 (note).** Location: lines 669--672, the corollary for Problem 1220, and
line 668, Problem 1219. The relations on the problem pages are between
cardinals, and the Tools section is stated for order types; the bridge holds
because the resources and targets are initial ordinals (W2) but is not
stated. One sentence would close it.

**F6 (note).** Location: lines 673--676, "The canonization mechanism of the
Problem 1219 connections page handles Problem 1220's strong-limit case and
records the obstruction beyond it." This is a cross-reference to a page
outside the read set and was not checked. Two things the sentence should tie
to the problem's statement when it is next edited: the problem's hypothesis
is $\aleph_0$-inaccessibility of $\lambda$ and of $\mathrm{cf}(\lambda)$, not
strong-limitness, and on the usual reading a strong limit $\lambda$ is
$\aleph_0$-inaccessible while the hypothesis on $\mathrm{cf}(\lambda)$ is a
separate condition that "strong-limit case" does not mention.

## Verdict

- **S1.** Refutation-failed, as a statement of necessary conditions; it
  omits the finite color count, which decides Problem 1218 (F1).
- **S2.** Refutation-failed: the mechanism gives no reduction for Problems
  1170 and 1172 because their color-$0$ targets lie below the resource; the
  description of Problem 1172 needs the correction in F2, and "balanced" is
  idle (F4).
- **S3.** Refuted-as-stated: the exponent-$3$ obstruction does not block the
  mechanism, whose proofs are exponent-free; for Problem 1218 the exponent-$3$
  mechanism reduces every finite-color form of the asked negative relation to
  $\lambda\not\to(\lambda,4)^3$, which implies the asked countable-color
  relation, and the countable color count is the actual obstruction; for
  Problem 70 the conclusion survives on the ground given for Problem 1170
  (F1).
- **S4.** Refutation-failed, on the same ground as S2 (F4).
- **S5.** Refutation-failed: the conditional deduction by (T3) is correct
  and its "no help" reading is exact; the restatement of the problem drops
  two hypotheses (F3) and the cardinal-to-order-type bridge is implicit (F5).
- **S6.** Not a claim examined here: a cross-reference outside the read set,
  unverified (F6).
- **S7.** Not a claim.

Limitations: the page `research/erdos_1219/connections` was not read, so S6
and the "strong-limit case" it mentions were not checked; the definition of
$\aleph_0$-inaccessible was not read from a source and is used only in a
hedged remark; the exponent-free re-derivations in W1 are the reviewer's own
and are author-recorded in this report, not independently verified; Ramsey's
theorem is used once from general knowledge, for an illustration only. This
focused review assigns no tier and changes no status.
