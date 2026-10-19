[cut]

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

[cut]

**Covers.** The first question, read with chromatic number exactly $3$ and
vertices counted in edges, as the problem page's formulation records: it has
a negative answer, also under the weaker $3$-colourability gloss. Theorem
8's upper bound is outside this coverage. Not covered: the second
question, whether two edges must meet in $\gg r$ vertices.

**Depends on.** No native claim or external theorem is used as a premise:
the construction and its properties are established directly above.

[cut]
