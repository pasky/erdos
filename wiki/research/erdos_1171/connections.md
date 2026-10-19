---
name: research/erdos_1171/connections
title: "Connections: what the color-reduction proofs give elsewhere"
desc: |
  Assesses, target by target, what the reconstructed color-reduction
  induction and its restriction step give for other erdosproblems.com problems:
  the equivalences and corollaries that transfer, the conditional deductions
  with their premises, and the precise obstructions where the mechanism fails,
  including the ZFC question of Problem 1171 itself.
created: 2026-09-28T05:29:06Z
updated: 2026-10-19T04:19:07Z
---

[[research/erdos_1171/_index|..]]

***

**Scope.** This page carries the reconstructed mechanism of
[[research/erdos_1171/lemma_2_1_reconstruction|Lemma 2.1]] (the color-merging
induction) and [[research/erdos_1171/theorem_3_1_reconstruction|Theorem 3.1]]
(the restriction from $\omega_1^2$ to its initial segment $\omega_1\omega$) to
the other problems that use the same objects, and records for each what the
transfer gives, what it does not give, and why. Every statement here is
author-recorded, no problem status changes, and no tier is assigned. The
statements were independently reviewed as they stood on 2026-09-28T13:50:48Z by
eleven focused reviews graded in
[[research/erdos_1171/evidence/verify/connections_grade|the connections grade]],
which passes all eleven and accepts sixteen corrections, since applied. Sources
are cited at the standing their library pages record. Reading outside the held
corpus is limited to the erdosproblems.com pages named in each section, and one
arXiv abstract, named where it is used. Notation is that of the lemma page; a
*witness* for a negative relation is a coloring that refutes it.

## Tools

Five facts are used below. The first two are on the reconstruction pages,
the third is stated on the folder index, and the last two are recorded here
with their proofs.

**(T1) Transport.** Fact 1 of the lemma page is stated for ordinal targets;
the same proof gives it for a list of targets mixing order types and graphs.
Let $\gamma\to(\beta,H_1,\ldots,H_k)^2_{k+1}$ mean: every coloring of
$[\gamma]^2$ with the colors $0,\ldots,k$ has a subset of order type $\beta$
homogeneous in color $0$, or, for some $i$, a copy of $H_i$ in color $i$, a
copy being a subset of type $H_i$ all of whose pairs have color $i$ when
$H_i$ is an order type, and a subgraph isomorphic to $H_i$ all of whose
edges have color $i$ when $H_i$ is a graph. If $Y$ is a set of ordinals
with $\operatorname{otp}(Y)=\gamma$, the relation holds for colorings of
$[Y]^2$: an order isomorphism carries pairs to pairs, subsets of type
$\beta$ to subsets of type $\beta$, and copies of $H_i$ to copies of $H_i$.
Only order isomorphisms are used, so everything below also holds with the
ordinals replaced by arbitrary order types, the setting of Problem 118.

**(T2) Restriction and weakening.** If
$\gamma\to(\beta,H_1,\ldots,H_k)^2_{k+1}$ and $\gamma'$ has a subset of
type $\gamma$ (for ordinals, $\gamma'\ge\gamma$), then
$\gamma'\to(\beta,H_1,\ldots,H_k)^2_{k+1}$: restrict the coloring and read
the result in $\gamma'$, as in Steps 2 and 3 of the theorem page. If
$\beta'\le\beta$, then $\gamma\to(\beta',H_1,\ldots,H_k)^2_{k+1}$, since a
set of type $\beta$ has a subset of type $\beta'$; a target $H_i$ may be
replaced by any $H_i'$ that embeds in $H_i$; and a color may be left unused,
so a relation with fewer triangle colors is weaker.

**(T3) The induction with general targets.** If $\alpha\to(\alpha,H_i)^2$
for $i=1,\ldots,k$, then $\alpha\to(\alpha,H_1,\ldots,H_k)^2_{k+1}$. This is
the observation recorded on the folder index; it is the constant case
$\gamma_0=\cdots=\gamma_k=\alpha$ of (T4).

**(T4) Descent lemma.** Let $k\ge1$, let $\gamma_0,\ldots,\gamma_k$ be
ordinals and $H_1,\ldots,H_k$ targets, and suppose

$$
\gamma_{j-1}\to(\gamma_j,H_j)^2\qquad(j=1,\ldots,k).
$$

Then $\gamma_0\to(\gamma_k,H_1,\ldots,H_k)^2_{k+1}$, with color $j$ carrying
the target $H_j$.

*Proof.* Induction on $k$; for $k=1$ the conclusion is the hypothesis.
Assume the lemma for chains of length $k$ and let the $k+1$ relations hold
for $\gamma_0,\ldots,\gamma_{k+1}$. Let $c:[\gamma_0]^2\to\{0,\ldots,k+1\}$
and define $c'$ by $c'(p)=0$ if $c(p)\in\{0,k+1\}$ and $c'(p)=c(p)$
otherwise. Then $c'$ has the colors $0,\ldots,k$, and the lemma for the
first $k$ relations gives one of two things. Either there are $j\le k$ and a
copy of $H_j$ all of whose pairs have color $j$ under $c'$, hence under $c$,
which agrees with $c'$ on the colors $1,\ldots,k$. Or there is
$Y\subseteq\gamma_0$ with $\operatorname{otp}(Y)=\gamma_k$ and
$c(p)\in\{0,k+1\}$ for every $p\in[Y]^2$; then
$\gamma_k\to(\gamma_{k+1},H_{k+1})^2$, transported to $Y$ by (T1) and applied
to the two-coloring of $[Y]^2$ with the colors $0$ and $k+1$, gives a subset
of $Y$ of type $\gamma_{k+1}$ homogeneous in color $0$ or a copy of $H_{k+1}$
homogeneous in color $k+1$. In every case the conclusion for $k+1$ holds.
The lemma page merges the colors $0$ and $1$ and renames the rest; merging
$0$ with the last color is the same induction with the colors relabeled
(fact 2 of the lemma page). $\square$

**(T5) Witness extraction.** Suppose $c:[\alpha]^2\to\{0,\ldots,k\}$
witnesses $\alpha\not\to(\alpha,3,\ldots,3)^2_{k+1}$: no subset of type
$\alpha$ is homogeneous in color $0$, and no triangle is homogeneous in a
color $j\ge1$. Then there are $Y\subseteq\alpha$ with
$\operatorname{otp}(Y)=\alpha$ and $j\in\{1,\ldots,k\}$ such that the
two-coloring of $[Y]^2$ giving color $1$ to the pairs of $c$-color $j$ and
color $0$ to all other pairs witnesses $\alpha\not\to(\alpha,3)^2$ after
transport. *Proof.* Induction on $k$; for $k=1$ take $Y=\alpha$ and $j=1$.
For $k\ge2$ merge the colors $0$ and $k$ of $c$ into a coloring $c'$ with the
colors $0,\ldots,k-1$. If $c'$ has a subset $Y$ of type $\alpha$ homogeneous
in color $0$, then $c$ takes only the values $0$ and $k$ on $[Y]^2$, and the
two-coloring with $j=k$ has no color-$0$ subset of type $\alpha$, since $c$
has none, and no color-$1$ triangle. Otherwise $c'$ witnesses the relation
with $k-1$ triangle colors, and the induction hypothesis gives $Y$ and
$j\le k-1$; the two-colorings built from $c'$ and from $c$ with this $j$
coincide, since $c'$ agrees with $c$ on the colors $1,\ldots,k-1$. $\square$

Together with Lemma 2.1 and (T2), (T5) gives, for every order type $\alpha$
and every finite $k\ge1$,

$$
\alpha\to(\alpha,3)^2
\iff
\alpha\to(\alpha,\underbrace{3,\ldots,3}_{k})^2_{k+1},
$$

and adds that a many-color witness contains a two-color witness on a subset
of full type: adding triangle colors changes neither the positive nor the
negative relation.

## Problem 1171 in ZFC: descent chains and their obstruction

**Target.** [[problems/set_theory/E1171/_index|Problem 1171]] asks, for every
finite $k$, whether $\omega_1^2\to(\omega_1\omega,3,\ldots,3)^2_{k+1}$ with
$k$ triangle targets. Its current assessment records the status `open`: the
relation holds under $\mathrm{MA}_{\aleph_1}$ for every $k$, so ZFC does not
refute it; the cases $k\le2$ are theorems of ZFC, by the relation of
Baumgartner and Hajnal for $k=2$
([[../library/set_theory/baumgartner_1987_remark_partition_relations_infinite_ordinals/positive_relation|the positive relation]]),
which contains $k=1$ (Komjáth attributes $k=1$ to a 1970 paper of Erdős
and Hajnal, where the problem page does not find it); and the case $k=3$
is recorded by
[[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|Komjáth 2025]]
(Problem 54 discussion) as unknown. Bloom's catalog labeled the problem not
disprovable, a change prompted by the deposit that this folder reconstructs;
its author withdrew the deposit, as
[[problems/set_theory/E1171/claims/2026_09_05_gao|its claim page]] records,
and the consistency rests on Baumgartner's theorem without it. The question
the reconstructed route leaves open is the ZFC question for $k\ge3$.

**What the mechanism can do.** The folder index records that the induction
cannot run inside $\omega_1^2$ with the target $\omega_1\omega$, because it
needs the self-similar shape $\alpha\to(\alpha,3)^2$. The descent lemma (T4)
removes that restriction at a price: one two-color relation per added color,
each lowering the large target. Applied to the problem, if there are
ordinals

$$
\omega_1^2=\gamma_0\ge\gamma_1\ge\cdots\ge\gamma_k\ge\omega_1\omega
$$

with $\gamma_{j-1}\to(\gamma_j,3)^2$ a theorem of ZFC for each $j$, then
$\omega_1^2\to(\omega_1\omega,3,\ldots,3)^2_{k+1}$ is a theorem of ZFC, by
(T4) and (T2). The first link is available:
$\omega_1^2\to(\omega_1\alpha,3)^2$ for every $\alpha<\omega_1$, which
Komjáth 2025 (Problem 13 commentary) attributes to a 1970 paper of Erdős
and Hajnal; the problem page does not find it in that paper, and its case
$\alpha=\omega$ is contained in the relation of Baumgartner and Hajnal. So
$\gamma_1=\omega_1\alpha$ may be taken for any $\omega\le\alpha<\omega_1$.
With $k=1$ this recovers the ZFC case $k=1$. For $k=2$ the route needs one
further theorem of ZFC of the form $\gamma_1\to(\gamma_2,3)^2$ with
$\omega_1\omega\le\gamma_2\le\gamma_1\le\omega_1^2$.

**The obstruction.** No chain of length two has both links theorems of ZFC,
because under CH one of them fails:

- (a) Under CH, $\omega_1^2\not\to(\omega_1^2,3)^2$ (Hajnal 1971, [Ha71] on
  the page of [[problems/set_theory/E1169/_index|Problem 1169]] and on its
  erdosproblems.com page; the paper is not held). This excludes
  $\gamma_1=\omega_1^2$, since then the first link would be
  $\omega_1^2\to(\omega_1^2,3)^2$. A source qualification: Komjáth's Problem 13
  commentary states Hajnal's hypothesis as $\kappa^{<\kappa}=\kappa$ for the
  relation $(\kappa^+)^2\not\to((\kappa^+)^2,3)^2$, which at $\kappa=\omega$
  holds in ZFC and would contradict a later sentence of the same commentary,
  that the consistency of $\omega_1^2\to(\omega_1^2,3)^2$ is open; the CH form,
  which Bloom's catalog and the booklet item [Va99, 7.85] give, is used here.
- (b) *Under CH, $\gamma\not\to(\omega_1\omega,3)^2$ for every ordinal
  $\gamma<\omega_1^2$* (author-recorded here). This excludes every
  $\gamma_1<\omega_1^2$, since $\gamma_1\to(\gamma_2,3)^2$ with
  $\gamma_2\ge\omega_1\omega$ gives $\gamma_1\to(\omega_1\omega,3)^2$ by
  (T2).

*Proof of (b).* Assume CH and let $W$ be a triangle-free graph on
$\omega_1\omega$ with no independent set of order type $\omega_1\omega$: a
witness for $\omega_1\omega\not\to(\omega_1\omega,3)^2$, which CH supplies by
the Erdős--Hajnal theorem cited on
[[../library/set_theory/baumgartner_1989_remarks_partition_ordinals/main_theorem|Baumgartner's result page]].
Let $\alpha$ be a countable ordinal and fix an injection $f:\alpha\to\omega$.
Write the elements of $\omega_1\alpha$ as $\omega_1\eta+\zeta$ with
$\eta<\alpha$ and $\zeta<\omega_1$, calling $\eta$ the block index, and those
of $\omega_1\omega$ as $\omega_1n+\zeta$. Put
$\varphi(\omega_1\eta+\zeta)=\omega_1f(\eta)+\zeta$; $\varphi$ is injective
and carries the block $\eta$ into the block $f(\eta)$ preserving order. Let
$G$ be the graph on $\omega_1\alpha$ with $\{x,y\}\in G$ if and only if
$\{\varphi(x),\varphi(y)\}\in W$. A triangle of $G$ maps to a triangle of
$W$, so $G$ is triangle-free. Let $X\subseteq\omega_1\alpha$ be independent
in $G$ with $\operatorname{otp}(X)=\omega_1\omega$, and let $X_\eta$ be its
intersection with the block $\eta$. Then $\operatorname{otp}(X)$ is the sum,
in the order of $\alpha$, of the $\operatorname{otp}(X_\eta)$, each at most
$\omega_1$. If only $m$ of the $X_\eta$ were uncountable, the sum would be
$\omega_1m+\rho$ for a countable $\rho$, because a sum of countably many
countable ordinals is countable and $\rho'+\omega_1=\omega_1$ for countable
$\rho'$; that is below $\omega_1(m+1)\le\omega_1\omega$. So infinitely many
$X_\eta$ are uncountable, and $\varphi[X]$ meets infinitely many distinct
blocks of $\omega_1\omega$ in uncountable sets, since $f$ is injective. The
order type of $\varphi[X]$ is the sum over $n<\omega$ of the types of its
intersections with the blocks; infinitely many terms equal $\omega_1$ (an
uncountable subset of a block of type $\omega_1$ has type $\omega_1$), the
rest are countable, and every term is at most $\omega_1$, so the sum is
exactly $\omega_1\omega$. Thus $\varphi[X]$ is an independent set of $W$ of
type $\omega_1\omega$, a contradiction. Hence
$\omega_1\alpha\not\to(\omega_1\omega,3)^2$. For $\gamma<\omega_1^2$ write
$\gamma=\omega_1\alpha_0+\zeta$ with $\alpha_0,\zeta<\omega_1$; then
$\gamma<\omega_1(\alpha_0+1)$, and the restriction of $G$ for
$\alpha=\alpha_0+1$ to the initial segment $\gamma$ is a witness for
$\gamma\not\to(\omega_1\omega,3)^2$. $\square$

*Conclusion.* A chain of length $k\ge2$ needs $\gamma_1$ with both
$\omega_1^2\to(\gamma_1,3)^2$ and $\gamma_1\to(\gamma_2,3)^2$,
$\gamma_2\ge\omega_1\omega$; (a) refutes the first for
$\gamma_1=\omega_1^2$ and (b) the second for $\gamma_1<\omega_1^2$, in
every model of CH. So (T4) with triangle targets yields, from two-color
relations that are theorems of ZFC, exactly the case $k=1$. In particular
the ZFC case $k=2$ of Baumgartner and Hajnal cannot be obtained by (T4)
from two-color relations $\gamma\to(\gamma',3)^2$ between ordinals in
$[\omega_1\omega,\omega_1^2]$ that are theorems of ZFC, and (T4) cannot
reduce the open case $k=3$ to such theorems. This sharpens the folder
index's remark: not only the constant chain through $\omega_1\omega$ but
every descending chain of length at least two has a link that fails under
CH, so none consists of theorems of ZFC.

**By-products.** Statement (b) extends the two CH failures the review of
Baumgartner's chapter cites, $\omega_1\omega\not\to(\omega_1\omega,3)^2$ and
$\omega_1\omega^2\not\to(\omega_1\omega^2,3)^2$: under CH,
$\gamma\not\to(\gamma,3)^2$ for every $\gamma$ with
$\omega_1\omega\le\gamma<\omega_1^2$, by (T2). With Baumgartner's theorem,
which under $\mathrm{MA}_{\aleph_1}$ gives $\gamma\to(\omega_1\omega,3)^2$
for every $\gamma\ge\omega_1\omega$ by (T2), the relation
$\gamma\to(\omega_1\omega,3)^2$ is independent of ZFC for every $\gamma$
with $\omega_1\omega\le\gamma<\omega_1^2$, and the least $\gamma$ with the
relation is $\omega_1\omega$ under $\mathrm{MA}_{\aleph_1}$ and $\omega_1^2$
under CH. A second by-product of the theorem page: Step 1 uses
$\mathrm{MA}_{\aleph_1}$ only through Theorem A, so
$\omega_1\omega\to(\omega_1\omega,3)^2$ alone implies the relation of
Problem 1171 for every $k$. Hence a model of
$\omega_1^2\not\to(\omega_1\omega,3,3,3)^2$, if there is one, is a model of
$\omega_1\omega\not\to(\omega_1\omega,3)^2$, and the search for a consistent
negative answer to the case $k=3$ can be confined to such models, for
instance models of CH.

**Next investigation.** The mechanism is exhausted for the ZFC question.
What remains useful is (i) to acquire the paper of Baumgartner and Hajnal
(1987, not held) and identify the ingredient of the case $k=2$ that is not a
two-color descent, since any attack on $k=3$ starts from that ingredient;
and (ii) on the negative side, to look for a $4$-coloring of
$[\omega_1^2]^2$ in a model of CH with no color-$0$ set of type
$\omega_1\omega$ and no triangle in the other colors, CH being the simplest
hypothesis under which such a witness can live. A positive outcome of (ii)
would settle the case $k=3$ consistently in the negative; a proof that no
such coloring exists under CH would leave the ZFC question open but exclude
the natural models.

**Outcome.** Fails, with the obstruction (a)+(b); by-products recorded.

## Problem 1169: two-color and finite-color negative relations on omega_1^2

**Target.** [[problems/set_theory/E1169/_index|Problem 1169]] asks whether
$\omega_1^2\not\to(\omega_1^2,3)^2$. The page carries the status `open` and
a compiled assessment: ZFC does not refute the relation, and whether ZFC
proves it is open. The erdosproblems.com page (accessed
2026-09-28; last edited 25 January 2026) states the problem with a quantifier
"for all finite $k<\omega$" that the displayed relation does not use,
records that Hajnal proved the negative relation from CH [Ha71], and lists no
proof claim. The booklet item [Va99, 7.85], read in the
transcription of
[[../library/number_theory/various_1999_some_pauls_favorite_problems/_index|the booklet]],
has no quantifier: "Is it true that $\omega_1^2\not\to(\omega_1^2,3)^2$?
[Hajnal show[ed] this follows from CH.]" (the verb is cut at the scan's right
edge). The open part is whether the negative
relation is a theorem of ZFC, equivalently whether
$\omega_1^2\to(\omega_1^2,3)^2$ is consistent, which Komjáth 2025 (Problem
13 commentary) calls open as far as the author knows.

**What transfers.** (T5) at $\alpha=\omega_1^2$: for every finite $k\ge1$,

$$
\omega_1^2\not\to(\omega_1^2,3)^2
\iff
\omega_1^2\not\to(\omega_1^2,\underbrace{3,\ldots,3}_{k})^2_{k+1}.
$$

So the stray quantifier is harmless: read with $k$ triangle colors, the
erdosproblems.com statement is equivalent to the booklet's for every $k$, and a
witness for the many-color relation contains a two-color witness on a subset
of type $\omega_1^2$. Second, by (T3) and (T2), every model of
$\omega_1^2\to(\omega_1^2,3)^2$ satisfies
$\omega_1^2\to(\omega_1^2,3,\ldots,3)^2_{k+1}$ for every $k$, hence the
relation of Problem 1171 with the target $\omega_1^2$ in place of
$\omega_1\omega$. This is the folder index's remark, now with its proof. The
conclusion is stronger than what $\mathrm{MA}_{\aleph_1}$ gives for Problem
1171, but its premise is Komjáth's open consistency question, and nothing
here attacks that premise.

**What does not transfer.** Nothing bears on the ZFC question. The
mechanism produces positive relations from positive relations; toward the
negative relation it says only, through (T5), that adding colors does not
make a witness easier to build. Context, not used: an arXiv preprint
(Golshani, arXiv:2608.13213, August 2026; unrefereed, not held; its abstract
was read) states that a finite-support iteration of
$\sigma$-centered forcings over a model of CH carrying Hajnal's coloring
yields a model of $\mathrm{MA}_{\omega_1}(\sigma\text{-centered})$,
$2^{\aleph_0}=\aleph_2$ and $\omega_1^2\not\to(\omega_1^2,3)^2$, and that
under $\mathrm{MA}_{\omega_1}$ every c.c.c. forcing preserves an existing
witness. If so, the negative relation is compatible with the fragment
$\mathrm{MA}_{\omega_1}(\sigma\text{-centered})$, whereas
$\omega_1\omega\not\to(\omega_1\omega,3)^2$ contradicts full
$\mathrm{MA}_{\aleph_1}$ (Theorem A on the theorem page); whether that
fragment alone excludes $\omega_1\omega\not\to(\omega_1\omega,3)^2$ is not
settled by anything held here; and the iteration the abstract describes
does not reach a model of the positive relation. The search log on the
Problem 1171 page lists the preprint.

**Next investigation and outcome.** None from this mechanism. Outcome:
transfers conditionally, an equivalence and a conditional strengthening; no
lead, since the premise is the open problem itself and the unconditional
conclusion for Problem 1171 is already known by the $\mathrm{MA}_{\aleph_1}$
route.

## Problem 597: graph targets

**Target.** [[problems/set_theory/E0597/_index|Problem 597]] asks two things:
(Q1) for every graph $G$ on at most $\aleph_1$ vertices with no $K_4$ and no
$K_{\aleph_0,\aleph_0}$, is $\omega_1^2\to(\omega_1\omega,G)^2$; and (Q2)
what about finite $G$. The page carries the status `open` and a compiled
account of its claim pages. The erdosproblems.com page (accessed 2026-09-28;
last edited 23 January 2026) records that Erdős and Hajnal proved
$\omega_1^2\to(\omega_1\omega,3)^2$, that Erdős first asked the question for
$K_4$-free $G$ only, and that Baumgartner proved
$\omega_1^2\not\to(\omega_1\omega,K_{\aleph_0,\aleph_0})^2$ (no hypothesis is
stated on the page), which is why $K_{\aleph_0,\aleph_0}$ is excluded; the
exclusion of $K_4$ is forced by $\omega_1^2\not\to(\omega_1\omega,4)^2$ under CH
([[../library/set_theory/baumgartner_1987_remark_partition_relations_infinite_ordinals/negative_relation|the negative relation]]).

**(Q2) under Martin's axiom: transfers, without the lemma.** Under
$\mathrm{MA}_{\aleph_1}$, Baumgartner's theorem at full strength gives
$\omega_1\omega\to(\omega_1\omega,n)^2$ for every finite $n$
([[../library/set_theory/baumgartner_1989_remarks_partition_ordinals/main_theorem|main theorem]];
the statement is taken from the zbMATH review and one held restatement (an
arXiv preprint), the chapter is not held, and the deposit cites only the
case $n=3$). For a finite graph $G$ on $n$ vertices, $G$ embeds in $K_n$, so
$\omega_1\omega\to(\omega_1\omega,G)^2$ by (T2), and restriction to the
initial segment, Steps 2 and 3 of the theorem page, gives
$\omega_1^2\to(\omega_1\omega,G)^2$. Hence under $\mathrm{MA}_{\aleph_1}$
the answer to (Q2) is yes for every finite $G$, whether or not $G$ is
$K_4$-free; with the relative consistency of $\mathrm{MA}_{\aleph_1}$
(Theorem C on the theorem page), (Q2) is not disprovable in ZFC. This is a
deduction from the imported theorem and the restriction step alone; the
color-merging induction is not needed. What the induction adds are the
finite-color variants: by (T3) at $\alpha=\omega_1\omega$, under
$\mathrm{MA}_{\aleph_1}$,
$\omega_1^2\to(\omega_1\omega,G_1,\ldots,G_k)^2_{k+1}$ for any finite
graphs $G_i$, which also follows from Baumgartner's theorem with $n$ the
multicolor Ramsey number of the cliques on the $G_i$; and, under any
hypothesis giving $\omega_1\omega\to(\omega_1\omega,G_i)^2$ for infinite
$G_i$, the same relation with those $G_i$, which the Ramsey bridge cannot
give.

**(Q2) in ZFC: the mechanism does not apply, but an implication does.**
(Q2) is a two-color relation whose large target $\omega_1\omega$ lies below
the resource $\omega_1^2$. The induction adds colors and cannot enlarge a
triangle target to $G$, and (T4) would need a two-color relation with the
target $G$ on some ordinal at most $\omega_1^2$, which is (Q2) itself or
stronger. So the mechanism is orthogonal to the question. In the other
direction (author-recorded): for each finite $k$ let $F_k$ be a finite
$K_4$-free graph such that every $k$-coloring of its edges has a
monochromatic triangle, which exists for $k=2$ by
[[../library/set_theory/folkman_1970_graphs_monochromatic_complete_subgraphs_every_edge/theorem_1|Folkman's Theorem 1]]
and for every $k$ by the theorem of Nešetřil and Rödl recorded on
[[problems/ramsey_theory/E0924/_index|Problem 924]]. If
$\omega_1^2\to(\omega_1\omega,F_k)^2$, then
$\omega_1^2\to(\omega_1\omega,3,\ldots,3)^2_{k+1}$ with $k$ triangle
targets: given a coloring with the colors $0,\ldots,k$, merge the colors
$1,\ldots,k$ into one; a color-$0$ set of type $\omega_1\omega$ is what is
wanted, and a copy of $F_k$ in the merged color carries a $k$-coloring of
its edges, hence a monochromatic triangle. So a positive answer to (Q2) in
ZFC for the graphs $F_k$ would answer Problem 1171 in ZFC for every $k$, and
every model of $\omega_1^2\not\to(\omega_1\omega,3,\ldots,3)^2_{k+1}$ is a
model in which (Q2) fails for the $K_4$-free graph $F_k$. (Q2) for
Folkman-type graphs is therefore at least as strong as the open case $k=3$
of Problem 1171. The converse implication gives nothing: the relation of
Problem 1171 yields (Q2) only for subgraphs of a triangle.

**(Q1): not reached.** The route under $\mathrm{MA}_{\aleph_1}$ would need
$\omega_1\omega\to(\omega_1\omega,G)^2$ for infinite $G$ with the stated
exclusions; Baumgartner's theorem is stated for finite $n$ only, and nothing
held decides the infinite case. A necessary condition for (Q1) in a model is
that every graph on $\omega_1^2$ without an independent set of type
$\omega_1\omega$ contains, as a subgraph, every such $G$; the
$K_{\aleph_0,\aleph_0}$ exclusion is exactly the failure of that condition
at $K_{\aleph_0,\aleph_0}$.

**Next investigation.** (i) Acquire Baumgartner's chapter and check the
full-strength statement on its page images; until then the answer to (Q2)
under $\mathrm{MA}_{\aleph_1}$ rests on the review and the restatement.
(ii) Under $\mathrm{MA}_{\aleph_1}$, whether the proof of
$\omega_1\omega\to(\omega_1\omega,n)^2$ extends to countable, then
$\aleph_1$-sized, $K_4$-free and $K_{\aleph_0,\aleph_0}$-free $G$: a
positive outcome makes (Q1) not disprovable for the $G$ covered; a negative
outcome shows only that this route does not cover $G$; (Q1) has no positive
answer in ZFC, and $G$ is a third necessary exclusion, only if some model
satisfies $\omega_1^2\not\to(\omega_1\omega,G)^2$ for a $G$ with the
exclusions of (Q1), which a failure on $\omega_1\omega$ does not give: under
CH, $\omega_1\omega\not\to(\omega_1\omega,3)^2$ while
$\omega_1^2\to(\omega_1\omega,3)^2$ is a theorem of ZFC.
(iii) For (Q2) in ZFC, test the smallest Folkman-type graphs first, knowing
that a positive answer for $F_3$ settles the case $k=3$ of Problem 1171 and
that a consistent negative answer for that case refutes (Q2) at $F_3$.

**Outcome.** Transfers conditionally for (Q2) under $\mathrm{MA}_{\aleph_1}$,
from the imported theorem and the restriction step; fails for the ZFC
question and for (Q1), with the implication to Problem 1171 recorded.

## Problems 590, 591, 592 and 118: countable partition ordinals

**Targets.** [[problems/set_theory/E0590/_index|Problem 590]] (status
`solved`, claim `proved`; the erdosproblems.com label PROVED (LEAN)):
$\omega^\omega\to(\omega^\omega,3)^2$, Chang's theorem
([[../library/set_theory/chang_1972_partition_theorem_complete_graph_omega_omega/theorem_p396|theorem_p396]]),
with $\omega^\omega\to(\omega^\omega,m)^2$ for every finite $m$ reported
from Milner and Larson on the same page.
[[problems/set_theory/E0591/_index|Problem 591]] (status `solved`, claim
`proved`): $\omega^{\omega^2}\to(\omega^{\omega^2},3)^2$, the case $\beta=2$
of Schipperus's
[[../library/set_theory/schipperus_2010_countable_partition_ordinals/theorem_28|Theorem 28]].
[[problems/set_theory/E0592/_index|Problem 592]] (status `open`): determine the
countable $\beta$ with $\omega^{\omega^\beta}\to(\omega^{\omega^\beta},3)^2$;
known are yes for $\beta$ a sum of one or two indecomposables (Theorem 28)
and no for four or more
([[../library/set_theory/schipperus_2010_countable_partition_ordinals/theorem_29|Theorem 29]],
part 3), with three undecided. [[problems/set_theory/E0118/_index|Problem 118]]
(status `solved`, claim `disproved`): whether $\alpha\to(\alpha,3)^2$ forces
$\alpha\to(\alpha,n)^2$ for every $n$, refuted by
$\omega^{\omega^2}\not\to(\omega^{\omega^2},6)^2$ (Theorem 29, part 1) and,
per Schipperus's report, by Larson's $\not\to(\omega^{\omega^2},5)^2$
together with Larson's $\omega^{\omega^2}\to(\omega^{\omega^2},4)^2$ (not
held). Each of these pages carries a compiled assessment.

**What transfers.** Lemma 2.1 applies verbatim to every countable
partition ordinal: if $\alpha\to(\alpha,3)^2$ then
$\alpha\to(\alpha,3,\ldots,3)^2_{k+1}$ for every finite $k$, and by (T5)
conversely. Three consequences:

- *Problem 592 is unchanged by adding triangle colors.* For every
  countable $\beta$ and every $k\ge1$,
  $\omega^{\omega^\beta}\to(\omega^{\omega^\beta},3)^2$ if and only if
  $\omega^{\omega^\beta}\to(\omega^{\omega^\beta},3,\ldots,3)^2_{k+1}$.
  This is an equivalent reformulation, and it enables nothing new: the
  extracted witness of (T5) lives on a subset of full type and needs no new
  construction, and a positive many-color relation is no easier to prove
  than the two-color one it contains. The undecided case is treated in the
  next section.
- *Problem 591's relation strengthens in the color direction where it
  stops in the clique direction.* By Theorem 28,
  $\omega^{\omega^2}\to(\omega^{\omega^2},3,\ldots,3)^2_{k+1}$ for every
  $k$, although $\omega^{\omega^2}\not\to(\omega^{\omega^2},6)^2$. Here the
  deposit's bridge is strictly stronger than the finite-Ramsey bridge of
  Baumgartner's result page: already the case $k=2$,
  $\omega^{\omega^2}\to(\omega^{\omega^2},3,3)^2_3$, would need
  $\omega^{\omega^2}\to(\omega^{\omega^2},6)^2$ through the Ramsey number
  $R(3,3)=6$, which is false. For Problem 590 the two bridges agree, since
  $\omega^\omega\to(\omega^\omega,m)^2$ holds for every finite $m$.
- *Problem 118's color sibling has a positive answer.* The disproved
  question asks whether $\alpha\to(\alpha,3)^2$ forces
  $\alpha\to(\alpha,n)^2$; its sibling, whether $\alpha\to(\alpha,3)^2$
  forces $\alpha\to(\alpha,3,\ldots,3)^2_{k+1}$, holds for every cardinal,
  ordinal or order type $\alpha$ and every finite $k$, by Lemma 2.1 with
  (T1). Raising the clique target is not free; adding triangle colors is.

**A ZFC instance and its finite corollary.** At $\alpha=\omega^{\omega^2}$,
Theorems 28 and 29(1) with Lemma 2.1 give, in ZFC and from held sources,

$$
\alpha\not\to(\alpha,6)^2
\quad\text{and}\quad
\alpha\to(\alpha,3,3,3,3,3)^2_6,
$$

and with Larson's sharpening (not held) the same with $5$ and four triangle
colors. This is a cousin of the question Komjáth records (next section),
which asks for $4$ against three triangle colors. It has a finite
corollary in the pattern of Hajnal's forcing-and-compactness argument
(Komjáth 2025, Problem 54 discussion), without the forcing: let $X$ be the
color-$1$ graph of a witness for $\alpha\not\to(\alpha,6)^2$, so $X$ is
$K_6$-free with no independent set of type $\alpha$. Every $5$-coloring of
the edges of $X$ has a monochromatic triangle: extend it by the color $0$ on
the non-edges; a color-$0$ set of type $\alpha$ would be independent in $X$,
so some color $1,\ldots,5$ has a triangle. By compactness some finite
subgraph of $X$ has the same property. The finite statement is weaker than
the theorem of Nešetřil and Rödl on Problem 924, which gives $K_4$-free
graphs for every number of colors; only the derivation through a countable
ordinal is new here.

**Outcome.** Transfers, as an equivalence for Problem 592 and as
corollaries for Problems 590, 591 and 118; no route to the undecided case
of Problem 592 and no lead from this section.

## Problems 592 and 1171: four-clique versus triangle colors

**Target.** Komjáth 2025 (Problem 54 discussion) records, next to the
unknown case $k=3$ of Problem 1171, that it is unknown "at least" whether it
is consistent that $\alpha\not\to(\beta,4)^2$ and $\alpha\to(\beta,3,3,3)^2$
hold together for some ordinals $\alpha,\beta$; the Problem 1171 page
quotes this in its assessment. The undecided case of Problem 592 is
$\omega^{\omega^\beta}\to(\omega^{\omega^\beta},3)^2$ for $\beta$ a sum of
exactly three indecomposable ordinals, the smallest being $\beta=3$ and
$\alpha=\omega^{\omega^3}$; the outside status was checked
against the report on the Isabelle formalization of ordinal partition
relations by Džamonja, Koutsoukou-Argyraki and Paulson (arXiv:2011.13218,
2020; not held in the library, its text layer read from a downloaded copy),
which states Schipperus's theorem as its Theorem 2.2 and then says that the
case of at least three summands in the Cantor normal form is still open; a
web search found no later result.

**The deduction (author-recorded).** If an ordinal $\alpha$ satisfies
$\alpha\to(\alpha,3)^2$ and $\alpha\not\to(\alpha,4)^2$, then by Lemma 2.1
$\alpha\to(\alpha,3,3,3)^2_4$, so the pair $(\alpha,\alpha)$ answers
Komjáth's question, in ZFC rather than merely consistently. Theorem 29(2)
supplies the second half for every $\alpha=\omega^{\omega^\beta}$ with
countable $\beta$ a sum of three indecomposables (read on the page images
at statement depth; the proofs of Theorems 31--33 were read and not
checked); the first half is exactly the undecided case of Problem 592. So:
*if $\omega^{\omega^\beta}\to(\omega^{\omega^\beta},3)^2$ for some
countable $\beta$ that is a sum of three indecomposables, then Komjáth's
question has a positive answer in ZFC.* The pair with
$\alpha=\omega^{\omega^2}$ does not serve, since
$\omega^{\omega^2}\to(\omega^{\omega^2},4)^2$ by Larson's theorem; and any
answer $(\alpha,\beta)$ has $\beta\not\to(\beta,4)^2$, because
$\beta\to(\beta,4)^2$ would give $\alpha\to(\beta,4)^2$ by (T2). The other
shape of an answer, with $\beta<\alpha$, contains the case $k=3$ of Problem
1171 under CH: $(\omega_1^2,\omega_1\omega)$ is an answer in a model of CH
exactly when $\omega_1^2\to(\omega_1\omega,3,3,3)^2$ holds there, by the
negative relation of Baumgartner and Hajnal.

**Falsification checks.** The quantifiers match: Komjáth asks for some
$\alpha,\beta$ and some model; the deduction gives one pair in every model.
The targets match: Theorem 29's $\not\to(\cdot,4)^2$ is the two-color
negative relation with a four-element homogeneous set, the same convention
as the lemma page. Nothing here decides the premise.

**Next investigation.** Settle
$\omega^{\omega^\beta}\to(\omega^{\omega^\beta},3)^2$ for $\beta$ a sum of
three indecomposables, starting at $\beta=3$. Schipperus's proof of Theorem
28 says that only its triangle-in-color-$1$ step, Lemma 26, is sensitive to
the number of indecomposables, so the first task is to see whether that
step, or a replacement, survives a third summand. A positive outcome
answers Komjáth's question in ZFC and extends the positive boundary of
Problem 592; a negative outcome for every such $\beta$ completes the
classification of Problem 592 as "at most two indecomposables" ($\beta=0$
included, since $\omega\to(\omega,3)^2$) and leaves Komjáth's question to
the other shape of answer, or to the shape $(\alpha,\alpha)$ at a partition
ordinal whose four-clique relation is undecided, such as
$\omega^{\omega^\omega}$, where Theorem 28 gives the $3$-relation and
nothing held decides the $4$-relation.

**Outcome.** Transfers conditionally; filed as the lead
[[research/leads/four_clique_versus_triangle_colors/_index|four-clique versus triangle colors]].

## Problems 1174, 595 and 596: countably many colors

**Targets.** [[problems/set_theory/E1174/_index|Problem 1174]] (status
`open`, each part with one consistency side settled): a $K_4$-free graph
every countable edge coloring of which has a monochromatic triangle, and a
$K_{\aleph_1}$-free graph every countable edge coloring of which has a
monochromatic $K_{\aleph_0}$.
[[problems/set_theory/E0595/_index|Problem 595]] (status `open`): a $K_4$-free
graph that is not a union of countably many triangle-free graphs, which is
the first question of Problem 1174 in other words, since a countable union
of triangle-free graphs is a countable edge coloring without monochromatic
triangles. Komjáth 2025 (Problem 53) records Shelah's consistency proof
([[../library/set_theory/shelah_1989_consistency_positive_partition_theorems_graphs_models/_index|Shelah 1989]],
Lemma 5.1, relative to a measurable cardinal or the weaker partition
hypothesis the lemma allows in its place) and that existence in ZFC is
open.
[[problems/set_theory/E0596/_index|Problem 596]] (status `open`): the pairs
$(G_1,G_2)$ for which $G_1$-free graphs force a monochromatic $G_2$ under
every finite number of colors but not under $\aleph_0$ colors; the pair
$(K_4,K_3)$ is Problem 595.

**Why the mechanism fails.** The induction adds one color per step and has
no limit step: the case $k$ is used once to reach a set of full type
two-colored by $\{0,1\}$, and for $\aleph_0$ colors the corresponding
merging leaves infinitely many colors on that set, with nothing to apply.
The obstruction is not a defect of the proof but of the statement: for
every order type $\alpha$ with $2\le|\alpha|\le2^{\aleph_0}$,

$$
\alpha\not\to(\alpha,\underbrace{3,3,\ldots}_{\aleph_0})^2_{\aleph_0}
$$

(author-recorded; the fact is the one Komjáth states for Problems 51 and
52, that $K_{2^{\aleph_0}}$ is a union of $\aleph_0$ bipartite graphs). Fix
an injection $\iota:\alpha\to2^\omega$ and color $\{x,y\}$ by $1+n$, where
$n$ is the least position at which $\iota(x)$ and $\iota(y)$ differ; leave
the color $0$ unused. A triangle homogeneous in color $1+n$ would need three
pairwise distinct values at position $n$, and there are two. So on
$\omega_1^2$, on $\omega_1\omega$ and on every countable ordinal the
countable-color relation with triangle targets fails outright, and no
ordinal partition relation on these ordinals can supply the graph of Problem
1174 or 595, which must have more than $2^{\aleph_0}$ vertices; Shelah's
consistent example has $2^\lambda$ vertices for a suitable $\lambda$. The
same coloring, with the color $0$ unused, refutes the countable-color form
of every relation on this page whose ordinal has at most $2^{\aleph_0}$
elements and whose targets in the colors $\ge1$ each contain an odd cycle
(a triangle, a larger clique, an ordinal $\ge3$, or a graph containing a
triangle): its color classes are bipartite, so it says nothing about the
bipartite targets of Problems 597 and 601, and nothing above the continuum,
where $(2^{\aleph_0})^+\to((2^{\aleph_0})^+,(\aleph_1)_{\aleph_0})^2$ holds
(Erdős and Rado, displayed by Komjáth 2025 under Problem 53). For Problem
596 the mechanism says only that the two-color finite side of the pair
$(K_4,K_3)$ is reachable from ordinal relations, by Hajnal's argument; that
for three or more colors the same route needs $\alpha\not\to(\beta,4)^2$
and $\alpha\to(\beta,3,3,3)^2$ in one model, which Komjáth 2025 (p. 443)
records as unknown (see the section on Problems 582 and 924); and that the
countable side is out of reach, by the cardinality obstruction.

**Outcome.** Fails, with the cardinality obstruction; no lead.

## Problem 1168

**Target.** [[problems/set_theory/E1168/_index|Problem 1168]] (status `open`):
prove $\aleph_{\omega+1}\not\to(\aleph_{\omega+1},3,\ldots,3)^2_{\aleph_0}$
without GCH. The library card of
[[../library/set_theory/garti_2025_problem_erdos_hajnal/_index|Garti, Hayut and Shelah]]
records the classical case $2^\lambda=\lambda^+$ and the consistency of the
negative relation with $2^\lambda>\lambda^+$ under pcf and guessing
hypotheses.

**What transfers.** Only the finite-color positives, which are trivial: by
the Erdős--Dushnik--Miller theorem $\kappa\to(\kappa,\omega)^2$ for every
infinite cardinal $\kappa$, so $\kappa\to(\kappa,3)^2$ and, by Lemma 2.1,
$\kappa\to(\kappa,3,\ldots,3)^2_{k+1}$ for every finite $k$; the Ramsey
bridge gives the same from $\kappa\to(\kappa,n)^2$. The problem asks for the
failure at $\aleph_0$ colors, where the induction has no limit step. One
remark of the previous section applies: if $\aleph_{\omega+1}\le2^{\aleph_0}$
the bit coloring refutes the relation at once, so the content of the problem
is the case $2^{\aleph_0}<\aleph_{\omega+1}$, which is where the cited work
operates.

**Outcome.** Fails; no lead.

## Problem 601: the infinite-path target

**Target.** [[problems/set_theory/E0601/_index|Problem 601]] (status `open`): for
which limit ordinals $\alpha$ does every graph on $\alpha$ have an infinite
path or an independent set of order type $\alpha$; in the notation of (T1),
$\alpha\to(\alpha,P)^2$ with $P$ the one-way infinite path as a subgraph.

**What transfers.** (T3) with $H_1=\cdots=H_k=P$: if $\alpha$ has the
property, then for every finite $k$, whenever $X_1,\ldots,X_k$ are graphs on
$\alpha$ none of which contains an infinite path, their union has an
independent set of type $\alpha$. Proof: color a pair by the least $i$ with
the pair in $X_i$, and by $0$ if there is none; a color-$i$ infinite path is
a path of $X_i$, so (T3) gives a color-$0$ set of type $\alpha$, independent
in every $X_i$. The union of two graphs without infinite paths can contain
one, so this is not immediate from the definition, but it says nothing about
which $\alpha$ have the property, which is the whole question; the
$\mathrm{MA}$ side of the problem (Larson 1990, [La90] on the page, not
held) is not in the corpus.

**Outcome.** Transfers, without bearing on the question; no lead.

## Problems 582 and 924: finite Folkman graphs

Both are proved: [[problems/ramsey_theory/E0582/_index|Problem 582]] by Folkman's
Theorem 1 and Problem 924 by Nešetřil and Rödl. Hajnal's argument (Komjáth
2025, Problem 54 discussion) derives Folkman's two-color graph from the ZFC
relation $\omega_1^2\to(\omega_1\omega,3,3)^2$, the CH witness for
$\omega_1^2\not\to(\omega_1\omega,4)^2$, compactness, and the absoluteness
of finite graphs. Its $k$-color analog through Problem 1171 would need the
ZFC relation with $k$ triangle targets, open for $k\ge3$, and the CH witness
in the same model; under $\mathrm{MA}_{\aleph_1}$, where the relation is
known, no $K_4$-free witness exists, since Baumgartner's theorem gives
$\omega_1^2\to(\omega_1\omega,4)^2$ there. So a positive answer to the open
case of Problem 1171 would only re-derive, by the same argument, the
triangle case of finite theorems already proved, and the finite theorems
give nothing back to Problem 1171; the only derivation of a Folkman-type
finite graph from the material here is the $K_6$-free, five-color instance
at $\omega^{\omega^2}$ above, which the finite theorems exceed. Outcome:
nothing to transfer in either direction; no lead.

## Other relations in the set-theory folder

The mechanism needs a color-$0$ target equal to the ambient order type, or a
descending chain as in (T4), fixed targets in the other colors, and finitely
many colors; the exponent plays no part in its proofs. It does not apply to
[[problems/set_theory/E1170/_index|Problem 1170]] and
[[problems/set_theory/E1172/_index|Problem 1172]], whose relations, one for Problem
1170 and five under GCH for Problem 1172, all have both targets below the
resource; nor to [[problems/set_theory/E0070/_index|Problem 70]],
$\mathfrak{c}\to(\beta,n)^3_2$ for countable $\beta$ and finite $n$, whose
color-$0$ target lies below the resource; nor to
[[problems/set_theory/E1219/_index|Problem 1219]], a cardinal relation with both
targets below the resource. For [[problems/set_theory/E1218/_index|Problem 1218]],
$\lambda\not\to(\lambda,4,4,\ldots)^3$ with countably many colors under GCH,
the mechanism runs in exponent $3$: for every finite $k$ the negative
relation with $k$ colors carrying $4$ is equivalent to
$\lambda\not\to(\lambda,4)^3$, which implies the asked relation by (T2); the
induction does not reach countably many colors, and that, not the exponent,
is the obstruction. For [[problems/set_theory/E1220/_index|Problem 1220]],
$\lambda\to(\lambda,\aleph_1)^2$ for a singular cardinal $\lambda$ with
$\lambda$ and $\mathrm{cf}(\lambda)$ both $\aleph_0$-inaccessible, (T3)
would give $\lambda\to(\lambda,\aleph_1,\ldots,\aleph_1)^2_{k+1}$ from the
relation asked. The problem page records the question as independent of
ZFC: under GCH the relation holds for every such $\lambda$ (Erdős, Hajnal
and Rado), and in a model of Shelah and Stanley it fails for one; so (T3)
gives the $(k+1)$-color relation for every such $\lambda$ under GCH, a
corollary that plays no part in settling the problem. The canonization
mechanism of
[[research/erdos_1219/connections|the Problem 1219 connections page]] handles
Problem 1220's strong-limit case and records the obstruction beyond it. None of
these is pursued.

## Outcomes

- Problem 1171, ZFC case $k\ge3$: fails. The descent lemma (T4) reduces the
  case $k$ to a chain of $k$ two-color relations, and under CH no chain of
  length two exists, by Hajnal's theorem and statement (b); by-products are
  the CH failure $\gamma\not\to(\omega_1\omega,3)^2$ for all
  $\gamma<\omega_1^2$ and the reduction of a consistent negative answer to
  models of $\omega_1\omega\not\to(\omega_1\omega,3)^2$.
- Problem 1169: transfers conditionally. The two-color and $k$-color
  negative relations on $\omega_1^2$ are equivalent for every $k$, and a
  model of the positive relation would satisfy Problem 1171's relation with
  target $\omega_1^2$.
- Problem 597: transfers conditionally for finite $G$ under
  $\mathrm{MA}_{\aleph_1}$, from Baumgartner's theorem and the restriction
  step; fails for the ZFC question and for infinite $G$; (Q2) for
  Folkman-type graphs implies Problem 1171 in ZFC.
- Problems 590, 591, 592, 118: transfers as an equivalence (592) and as
  corollaries (590, 591, 118); the ZFC instance "$6$ against five triangle
  colors" at $\omega^{\omega^2}$ is recorded.
- Komjáth's question "$4$ against three triangle colors" (Problems 1171 and
  592): transfers conditionally on the undecided three-indecomposable case
  of Problem 592. Lead filed.
- Problems 1174, 595, 596 and 1168: fail; countably many colors are out of
  reach of the induction, and the countable-color relation is false on every
  order type of size at most the continuum.
- Problem 601: transfers without bearing on the question.
- Problems 582, 924 and the relations of the last section: not applicable,
  Problem 1218 by the countable color count.
