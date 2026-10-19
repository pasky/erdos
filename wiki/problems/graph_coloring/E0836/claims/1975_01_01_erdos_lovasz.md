---
name: problems/graph_coloring/E0836/claims/1975_01_01_erdos_lovasz
title: Erdős and Lovász's 3-chromatic cliques with exponentially many points
desc: |
  Theorem 8 of Erdős and Lovász (1975) bounds the largest number of points of a
  $3$-chromatic $r$-uniform clique below by $\frac12\binom{2r-2}{r-1}+2r-2$, so
  the first question's $O(r^2)$ bound fails. Plasma AI's internal whole-statement review and separate grade pass its self-contained construction and negative answer; it stays claimed until Jacob Parish at Plasma AI signs off.
authors:
- P. Erdős
- L. Lovász
status: claimed
claim: disproved
scope: partial
settles:
- vertex_count
published: 1975
submitted: null
links:
- url: https://users.renyi.hu/~p_erdos/1975-34.pdf
  kind: paper
- url: https://www.erdosproblems.com/836
  kind: discussion
created: 2026-10-07T21:33:46Z
updated: 2026-10-18T00:09:26Z
---

***

**Claim.** For every integer $r\geq2$ there is a finite $r$-uniform
hypergraph $G_r$ in which every two edges meet, every vertex lies in an
edge, the chromatic number is exactly $3$, and

$$
|V(G_r)|=2r-2+\frac12\binom{2r-2}{r-1}.
$$

In particular, $|V(G_r)|/r^2\longrightarrow\infty$, giving a negative
answer to the first question of
[[problems/graph_coloring/E0836/_index|Problem 836]].

**The argument.** A proper vertex colouring means one with no
monochromatic edge. Let $S$ have $2r-2$ elements. For each unordered
partition $P=\{A,S\setminus A\}$ with $|A|=r-1$, take a distinct new
vertex $x_P$ outside $S$. The vertex set is $S$ together with these new
vertices. The edges are all $r$-subsets of $S$ and, for each $P$, both
$A\cup\{x_P\}$ and $(S\setminus A)\cup\{x_P\}$.

Every edge has size $r$. Two edges contained in $S$ meet in at least two
vertices. An $r$-subset of $S$ meets every $(r-1)$-subset of $S$, so it
meets each edge containing a new vertex. The two edges from the same
partition share $x_P$. If edges from distinct partitions had disjoint
parts in $S$, those two parts would be complementary $(r-1)$-subsets of
$S$ and would define the same partition, a contradiction. Thus every two
edges meet.

Since $r\leq2r-2$, every point of $S$ lies in an $r$-subset of $S$.
Each new vertex lies in its two partition edges, so there are no isolated
vertices. In a proper $2$-colouring, each colour class inside $S$ would
have at most $r-1$ vertices; hence the two classes would each have exactly
$r-1$ vertices. They define a partition $P$, and whichever of the two
colours is assigned to $x_P$ makes one of its partition edges
monochromatic. No proper $2$-colouring exists. For a proper $3$-colouring,
split $S$ into any two $(r-1)$-sets, colour them with colours $1$ and $2$,
and give every new vertex colour $3$. Every $r$-subset of $S$ meets both
colour classes, and every partition edge has a new vertex and at least
one vertex of $S$. This proves that the chromatic number is exactly $3$,
including when $r=2$.

Choosing one part of an unordered partition counts it twice. Its two
parts are distinct because $r-1\geq1$, so there are
$\frac12\binom{2r-2}{r-1}$ new vertices, giving the stated count. The
central entry is the largest of the $2r-1$ binomial coefficients in row
$2r-2$, whose sum is $4^{r-1}$. Consequently

$$
\frac{|V(G_r)|}{r^2}
\geq\frac{4^{r-1}}{2(2r-1)r^2}
\longrightarrow\infty.
$$

For example, the ratio of consecutive terms of the last lower bound tends
to $4$, so it is eventually at least $2$; this proves the displayed
divergence. The construction therefore rules out a uniform $O(r^2)$
bound under the exact chromatic-number and incident-vertex conventions,
and also under the weaker condition of mere $3$-colourability.

**Source context.** This is construction (b) on printed p. 620 of P.
Erdős and L. Lovász, *Problems and results on $3$-chromatic hypergraphs and
some related questions*, Infinite and Finite Sets (Colloq., Keszthely,
1973), Vol. II, Colloq. Math. Soc. János Bolyai 10, North-Holland, 1975,
609–627; its
[[../library/graph_coloring/erdos_1975_problems_results_3_chromatic_hypergraphs_related/_index|library card]]
records the source. The source calls an intersecting hypergraph a clique.
Writing $N(r)$ for the maximum number of incident vertices in an exact
$3$-chromatic $r$-uniform clique, its Theorem 8 (printed p. 613, proof
p. 621) states

$$
\frac12\binom{2r-2}{r-1}+2r-2\ \le\ N(r)\ \le\ \frac r2\binom{2r-1}{r-1}.
$$

The construction supplies the lower bound. The upper bound is source
context; its proof is not reconstructed here or needed for the negative
answer. For the second question, the paper proves that some two edges
meet in at least $r/\log r$ vertices, an observation it credits to Shelah
and the authors jointly (p. 613), and asks whether $cr$ or even $r-c$
holds.

**Covers.** The first question, read with chromatic number exactly $3$ and
vertices counted in edges, as the problem page's formulation records: it has
a negative answer, also under the weaker $3$-colourability gloss. Theorem
8's upper bound is outside this coverage. Not covered: the second
question, whether two edges must meet in $\gg r$ vertices.

**Depends on.** No native claim or external theorem is used as a premise:
the construction and its properties are established directly above.

**Standing.** Claimed, with the sign-off of Jacob Parish at Plasma AI pending. Plasma AI's independent examination of the self-contained reconstruction is coverage and lists no evidence. The
[[research/erdos_836/evidence/verify/vertex_count/report|whole-statement report]]
and its [[research/erdos_836/evidence/verify/vertex_count/grade|separate grade]],
both dated 14 October 2026, give **refutation-failed** and **pass** for
all stated properties, the exact count, superquadratic growth and the
negative answer under both first-question formulations. An independent
reviewer and a distinct independent grader, each using model gpt-6-astra
in a fresh context, performed the examination and grading. The preserved
mathematical extracts match the Claim, The argument, Covers and Depends
on sections above exactly.

The grade accepts independence on the supplied record while retaining its
limits: the historical native read trace is incomplete and two private
helper bodies were unavailable. It does not certify every historical
operation. No essential mathematical repair or unproved consumed premise
remains. The
[[research/erdos_836/evidence/verify/vertex_count/_index|retained warrant]]
contains the exact subjects and full qualifications.

That examination covers this construction and its first-question consequences.
It excludes Theorem 8's upper bound, the second question, fidelity to an
external publication, historical credit and all Lean artifacts. The
proceedings volume has no evidence of refereeing on record, so `refereed`
is not listed. The construction remains credited to Erdős and Lovász;
Plasma AI supplies the reconstruction and independent examination.
erdosproblems.com credits the matching counterexample to Alon; that
commentary is separate from this review warrant.
