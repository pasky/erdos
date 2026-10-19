---
name: research/erdos_644/algebraic_shifting
desc: A Cohen–Macaulay example for which every pure shifted complex with the same face numbers destroys the local seven-edge property.
tags: [proved, limitations, topology]
sources: []
created: 2026-09-22T22:02:32Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/algebraic_shifting

***

The elementary example below rules out a direct algebraic-shifting transfer for
the nontransversal complex. Its original hypergraph has $P_7$, rank four, and
transversal number three. Every pure shifted complex with the same face numbers
gives a complementary hypergraph of the same rank and transversal number that
fails $P_7$. The original complex is Cohen–Macaulay over every field, so
exterior algebraic shifting is among the transformations excluded.

This is a limitation of a proposed proof method, not a counterexample to either
assertion of Problem 644. It complements the ordinary-shift obstructions in
[Compression obstructions](compression_obstructions.md).

## The complementary-complex formulation

For a family $\mathcal H$ on a finite ground set $V$, its nontransversal complex
is

$$
K(\mathcal H)=\{S\subseteq V:S\cap E=\varnothing
\text{ for some }E\in\mathcal H\}.
$$

If $\mathcal H$ is uniform, its facets are precisely the complements of its
edges. A subfamily $E_1,\ldots,E_q$ has no two-point transversal if and only if
the corresponding facets $V\setminus E_i$ collectively contain every pair of
vertices. We use $P_7$ for the condition that every subfamily of at most seven
edges has a transversal of size at most two.

## A 30-edge family with the local property

Partition $V=[7]$ into $A,B$, where $|A|=3$ and $|B|=4$. Let $K$ consist of the
full one-skeleton and all triples meeting both $A$ and $B$, with no larger
faces. Its number of triangular facets is

$$
\binom73-\binom33-\binom43=30.
$$

Every pair has an extension to a mixed triple, so $K$ is pure of dimension two.
Put

$$
\mathcal H=\{V\setminus F:F\text{ is a triangular facet of }K\}.
$$

This family is 4-uniform, and $K=K(\mathcal H)$.

Every pair belongs to some facet of $K$, so no pair is a transversal of
$\mathcal H$. The triple $A$ belongs to no facet and therefore intersects every
edge of $\mathcal H$. Thus

$$
\tau(\mathcal H)=3.
$$


**Claim.** The family $\mathcal H$ has $P_7$.

Suppose that $q\le7$ of the complementary triangles cover all $\binom72=21$
pairs. Each triangle contains three pairs, forcing $q=7$ and forcing every pair
to occur exactly once. Each vertex consequently belongs to exactly three of the
triangles: its six incident pairs are covered two at a time.

The three pairs inside $A$ must lie in three different selected triangles, since
no selected triangle is $A$. These are exactly the selected triangles with two
vertices in $A$. Every other selected triangle has one vertex in $A$, since all
are mixed. The total number of incidences with $A$ is therefore

$$
3\cdot2+4\cdot1=10.
$$

But the three vertices of $A$ each occur three times, giving nine incidences.
This contradiction proves the claim.

## The elementary shifted-complex obstruction

For triples $S=\{s_1<s_2<s_3\}$ and $T=\{t_1<t_2<t_3\}$, write $S\le_P T$ if
$s_i\le t_i$ for all $i$. A complex is *shifted* if $T$ being a face and
$S\le_P T$ imply that $S$ is a face, in every cardinality.

**Proposition.** Every pure shifted complex $L$ with the same face numbers as
$K$ contains the seven triples

$$
123,\quad145,\quad167,\quad246,\quad257,\quad347,\quad356.
\tag{1}
$$

Consequently, the complementary family

$$
\mathcal H_L=\{V\setminus F:F\text{ is a facet of }L\}
$$

is 4-uniform, has transversal number three, and fails $P_7$.

**Proof.** The complex $L$ has seven vertices, all 21 pairs, exactly 30 triples,
and no larger faces. There are therefore exactly five missing triples. If a
triple is missing, all triples above it in the order $\le_P$ are missing. The
upper sets of three particular triples are

$$
\begin{aligned}
\{T:257\le_P T\}
 &=\{257,267,357,367,457,467,567\},\\
\{T:347\le_P T\}
 &=\{347,357,367,457,467,567\},\\
\{T:356\le_P T\}
 &=\{356,357,367,456,457,467,567\}.
\end{aligned}
$$

Each has more than five members. Thus $257,347,356$ are faces. Shiftedness also
gives $246,145,123$, each of which lies below $257$.

The edge $67$ is present. Purity extends it to a triangle $i67$ with $i\le5$,
and shiftedness gives $167$. This proves (1).

The seven triples in (1) contain every pair of $V$ exactly once; they are the
lines of a Fano plane. Their seven complementary edges thus have no two-point
transversal.

All facets of $L$ have size three by purity, so $\mathcal H_L$ is 4-uniform.
Every pair belongs to a facet of $L$, so $\tau(\mathcal H_L)>2$. Any of the five
missing triples is a transversal: if it missed a complementary edge, it would be
contained in the corresponding triangular facet and hence equal that facet.
Therefore $\tau(\mathcal H_L)=3$. $\square$

The proposition is independent of any definition or theorem concerning algebraic
shifting. In particular, preserving purity, all face numbers, uniformity, and
the transversal number does not suffice to preserve $P_7$ under a transfer to a
shifted complex.

## Cohen–Macaulayness and exterior algebraic shifting

Here is a direct homological verification that $K$ is Cohen–Macaulay over every
field. For a pure two-dimensional complex, the relevant conditions are
connectedness, vanishing first homology, and connected vertex links; edge links
must also be nonempty.

The full one-skeleton makes $K$ connected, and all edge links are nonempty
because every pair extends to a mixed triangle. For a vertex in $A$, its link
contains every edge between $A\setminus\{v\}$ and $B$, and every edge within
$B$; it is connected. For a vertex in $B$, the symmetric description gives all
edges between $A$ and $B\setminus\{v\}$ and every edge within $A$, again a
connected graph.

Finally, cycles in a complete graph are generated, over any field, by boundaries
of triangles. The boundary of a mixed triangle already bounds in $K$. If
$\{a,b,c\}$ is monochromatic, choose a vertex $v$ of the other part. The three
triangles $vab,vbc,vca$ all belong to $K$, and their oriented boundaries sum to
the boundary of $abc$. Hence every one-cycle bounds and $H_1(K)=0$. These
verifications establish Cohen–Macaulayness through its homological link
criterion.

We now invoke the external algebraic-shifting facts only to apply the elementary
proposition. In Art M. Duval, *Algebraic Shifting and Sequentially
Cohen-Macaulay Simplicial Complexes*, Electronic Journal of Combinatorics **3**
(1996), R21, Section 4 defines the exterior algebraic shift $\Delta(K)$.
Proposition 4.1, on page 7, states preservation of the face numbers; the
construction gives a shifted complex. Proposition 4.4, on page 8, states that
$K$ is Cohen–Macaulay if and only if $\Delta(K)$ is pure. Duval attributes these
results to Kalai. The definition and both propositions were checked in the
[full paper](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v3i1r21/pdf).

It follows that the exterior algebraic shift of this $K$, over any field, is a
pure shifted complex with the same face numbers. The proposition applies: its
complementary family preserves rank four and transversal number three but fails
$P_7$.

The original complex can also be recognized as the independence complex of the
rank-three truncation of $U_{2,3}\oplus U_{2,4}$. Thus the original hypergraph
consists of the bases of the dual rank-four matroid. The example lies exactly at
$\tau/k=3/4$; it supplies no asymptotic counterexample, whether for matroid base
families or arbitrary families.
