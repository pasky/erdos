---
name: research/erdos_132/small_orders
title: Two rare distances for orders five through fourteen except eleven
desc: |
  Classifications and the unique-diameter theorem prove R at least two
  for orders 5 through 10 and 12 through 14; order 11 remains unexcluded.
sources: []
research_state: closed
created: 2026-09-23T00:27:00Z
updated: 2026-10-14T00:26:52Z
---


# Two rare distances for orders five through fourteen except eleven

***

This checks Section 2 and Appendix A of the
[independent input](independent/largest_distance_ranks_and_small_orders.md)
against the supplied source theorems and existing finite evidence. It proves

$$R(A)\ge2\qquad(5\le |A|\le10). \tag{1}$$

The later [unique-diameter theorem](unique_diameter_obstruction.md)
also proves $R(A)\ge2$ when $|A|=12$, as shown below.
The subsequently checked six-distance classification also settles orders
13 and 14. Thus the established range is $5\le n\le14$, except $n=11$.

All multiplicities count unordered pairs, with threshold the full
cardinality $n=|A|$. The general assertions of
[Problem 132](../../problems/distance_problems/E0132/_index.md) remain unresolved.

## Counting and the exact even-order boundary

If $R(A)=1$, the sole rare class is the diameter. With $q$ distinct
distances, the pair budget gives

$$\binom n2\ge1+(q-1)(n+1),\qquad q\le\lfloor n/2\rfloor. \tag{2}$$

If $n=2t$ and $q=t$, equality holds: the diameter occurs once and all
other distances occur exactly $n+1$ times. Deleting either endpoint of
the diameter leaves exactly $t-1$ classes, each of multiplicity at most
$n+1$. None disappears, since at most $n-1$ incident pairs are removed.
This is the same forced spectrum as in
[distance_partition_algebra](distance_partition_algebra.md); that note's
symmetry exclusions remain valid additional restrictions.

## Classification inputs and exact spectra

[Erdős--Fishburn (1996), Theorem 1](../../../library/distance_problems/erdos_fishburn_1996_maximum_planar_sets_that_determine_k_distances/_index.md)
gives $g(2)=5,g(3)=7,g(4)=9,g(5)=12$, where $g(k)$ is the largest size of a
planar set with exactly $k$ distances. It also classifies all extremizers for
$k\le4$: one type at five points, two at seven, and four at nine. The following
multiplicities are deductions from explicit models, not a table quoted from that
theorem.

| Points | Distances | All multiplicity multisets |
| --- | --- | --- |
| 5 | 2 | $(5,5)$ |
| 7 | 3 | $(7,7,7)$, $(12,6,3)$ |
| 9 | 4 | $(9,9,9,9)$, $(16,9,7,4)$, $(15,9,6,6)$, $(18,6,6,6)$ |

The five-point model is a regular pentagon. The seven-point models
are a regular heptagon and a regular hexagon with its center. Every
distance of a regular odd $m$-gon occurs $m$ times.

For completeness, the four nine-point types can be exhausted without
recovering coordinates from the source's omitted figures. The first
is a regular nonagon. For the next two use axial lattice coordinates

$$\phi(x,y)=(x+y/2,\sqrt3\,y/2),\qquad
 Q(u,v)=u^2+uv+v^2.$$

Define

$$H=\{(0,0),(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)\},$$

$$T_1=H\cup\{(1,1),(-1,2)\},$$

$$T_2=\{(0,0),(1,0),(0,1),(-1,1),(-1,2),(1,1),
 (2,0),(1,-1),(0,-1)\}.$$

Their squared-distance lists are both $(1,3,4,7)$, with respective
multiplicities $(16,9,7,4)$ and $(15,9,6,6)$. Here is an integer
certificate: distance-degree vectors in that order occur as follows;
sum each column and divide by two for the pair counts.

| Set | Degree vector | Number of vertices |
| --- | --- | --- |
| $T_1$ | $(6,2,0,0)$ | 1 |
| $T_1$ | $(4,2,2,0)$ | 2 |
| $T_1$ | $(5,2,1,0)$ | 1 |
| $T_1$ | $(3,2,2,1)$ | 2 |
| $T_1$ | $(3,2,1,2)$ | 1 |
| $T_1$ | $(2,2,2,2)$ | 2 |
| $T_2$ | $(5,2,1,0)$ | 3 |
| $T_2$ | $(3,2,2,1)$ | 3 |
| $T_2$ | $(2,2,1,3)$ | 3 |

For the last model put $s=\sqrt3$, $\zeta=e^{2\pi i/3}$, and

$$C=\{a\zeta^j:a\in\{1,1+s,-(2+s)\},\ j=0,1,2\}.$$

Within each three-point orbit, squared distances are $3a^2$, occurring
three times. Between distinct signed radii $a,b$, the three same-index
pairs have square $(a-b)^2$, and the six other pairs have square
$a^2+ab+b^2$. Thus the three within-orbit squares are
$3,12+6s,21+12s$; the same-index squares for the three orbit pairs
are these same three values; and all other squares equal $6+3s$.
In increasing order the spectrum is therefore

$$3:6,\quad6+3s:18,\quad12+6s:6,\quad21+12s:6.$$

The four sorted multiplicity multisets differ, so the models are
pairwise nonsimilar. The classification allows only four types, hence
these exhaust them. Every nonregular nine-point type has a class
of multiplicity at least fifteen.

## Proof of (1)

Suppose $R(A)=1$. For $n=5,7,9$, (2) and the bounds on $g(k)$ force
respectively $q=2,3,4$. The table rules out each case.

For $n=6,8,10$, the same bounds force respectively $q=3,4,5$.
The even-order equality case applies. Each of the two endpoint
deletions must therefore be a regular $(n-1)$-gon: for $n=6$ this
is the unique five-point type; for $n=8$ the nonregular seven-point
type has multiplicity $12>9$; for $n=10$ each nonregular nine-point
type has multiplicity at least $15>11$.

These two regular polygons share $n-2\ge4$ vertices. Three common
vertices determine their circumcircle, and one common vertex on that
circle determines the regular polygon of a specified order. Hence
the polygons coincide, contradicting deletion of distinct endpoints.
This proves (1).

The introduction of the supplied Clemen--Dumitrescu--Liu paper mentions
the earlier results for $n=5,6$ and describes the range $n\ge7$ as open.
We do not interpret that informal wording as a theorem about each
fixed order: (1) is a checked deduction from the complete classifications,
not a claim attributed to that introduction or a resolution for all $n$.

## Twelve-point uniqueness and the existing eleven-point motif

Let

$$U=\{(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),
 (2,0),(2,1),(2,2),(3,0),(3,1)\}.$$

Its squared-distance spectrum is

$$1:24,\qquad3:15,\qquad4:12,\qquad7:12,\qquad9:3. \tag{3}$$

An exact certificate is the following grouped degree table in that order.

| Vertices | Degree vector | Number |
| --- | --- | --- |
| $(1,1),(1,2),(2,1)$ | $(6,3,2,0,0)$ | 3 |
| $(0,2),(2,0),(2,2)$ | $(4,3,2,2,0)$ | 3 |
| All others | $(3,2,2,3,1)$ | 6 |

The column sums are $(48,30,24,24,6)$, yielding (3).
[Shinohara (2008), Theorem 1.2(b)](../../../library/distance_problems/shinohara_2008_uniqueness_maximum_planar_five_distance_sets/_index.md)
states uniqueness up to similarity of the twelve-point five-distance set. Thus
every such set has exactly three rare distances.

Deleting $(1,1)$ gives the input's eleven-point spectrum
$(18,12,10,12,3)$. The existing [motif note](eisenstein_motif.md)
deletes $(2,1)$ instead; the isometry $(x,y)\mapsto(4-x-y,x)$
preserves $U$ and carries the first deletion to the second.
Thus these are congruent examples, not different candidate families.

Every eleven-point deletion of $U$ retains exactly ten pairs at
square four, two or three at square nine, and at least eighteen at
square one. All such deletions therefore have at least two rare
distances. The motif note now gives a direct five-candidate certificate
for its one-point extension obstruction, removing its former dependence
on the exhaustive grid enumeration.

## Twelve points and the remaining order eleven

The conditions below remain only necessary conditions at order eleven.
Orders twelve through fourteen are excluded completely.

For $n=11$, (2) and $g(4)=9$ force exactly five distances. The four
nondiameter classes have multiplicity at least twelve, and the diameter
has at most seven pairs. No one vertex covers the diameter graph:
deleting it would leave ten points with at most four distances.
The twelve-point uniqueness theorem does not classify arbitrary
eleven-point five-distance sets.

For $n=12$, $g(4)=9$ and (2) leave only five or six distances.
The five-distance case is excluded by (3) and Shinohara's uniqueness
theorem. In the six-distance case the forced multiplicities are
$(13,13,13,13,13,1)$, with unique diameter. The new
[unique-diameter theorem](unique_diameter_obstruction.md) excludes
that case. Thus **every twelve-point planar set has at least two
rare distances**. This uses no classification of eleven-point
five-distance sets. The source uniqueness statement and the integer
pair spectrum (3) were rechecked for this deduction.

## Thirteen and fourteen points via the six-distance classification

[Szöllősi--Östergård (2020), Theorem 16](https://doi.org/10.37236/8565)
proves $g(6)=13$ and classifies the three maximum types: a regular
13-gon, a regular 12-gon with its center, and a regular hexagram with
its center. This is a published computer-assisted classification, not
a new exhaustion performed here. The author checked the full primary
statement and its continuation on pp. 15--16.
It concerns arbitrary planar sets, not just spherical sets. The theorem's
normalized isometry statement is used up to similarity.

For $n=13$, (2) and $g(5)=12$ force exactly six distances. The regular
13-gon has six classes of multiplicity 13. For the unit-circumradius
12-gon with its center, the squared-distance spectrum is

$$2-\sqrt3:12,\quad1:24,\quad2:12,\quad3:12,\quad
2+\sqrt3:12,\quad4:6.$$

For the hexagram use the axial norm $Q(x,y)=x^2+xy+y^2$ and the set

$$\begin{split}
H={}&\{(0,0),(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1),\\
& (1,1),(-1,2),(-2,1),(-1,-1),(1,-2),(2,-1)\}.
\end{split}$$

Its exact spectrum is

$$1:24,\quad3:18,\quad4:15,\quad7:12,\quad9:6,\quad12:3.$$

The degree vectors in that order are $(6,6,0,0,0,0)$ at the center,
$(5,2,3,2,0,0)$ at each of the six unit-radius points, and
$(2,3,2,2,2,1)$ at each of the six other points. Summing and halving
gives the displayed unordered multiplicities. Thus the three types have
respectively 6, 5, and 3 rare distances, contradicting $R=1$.

For $n=14$, (2) gives $q\le7$, while the known maxima through six
distances force $q\ge7$. The even counting boundary therefore gives a
unique diameter, ruled out by the
[unique-diameter theorem](unique_diameter_obstruction.md). This proves
$R(A)\ge2$ for every fourteen-point planar set.

The [finite certificate](evidence/util/continuation_checks.py) recomputes all 78
hexagram pairs exactly. Classification completeness is an external theorem; the
finite pair check alone would not establish exhaustion. The archived
[rotational thirteen-point report](independent/c3_13_unreviewed.md) is not
needed to exclude order thirteen and is unreviewed.

## Verification scope

The author checked the pair-budget and endpoint-deletion arguments,
the model formulas, and the source theorem statements, read the
relevant full-source passages after the digests, and verified all
finite spectra and grouped degree tables with exact integer or
$\mathbb Q(\sqrt3)$ arithmetic; the arguments are author-recorded.
Those computations check explicit models;
the exhaustion of types relies on the stated published classifications.
No new grid enumeration, eleven-point classification, or unrestricted
proof is claimed.

## Comparison with the second independent input

Sections 4 and 7 of the
[second independent input](independent/large_distance_graph_and_convex_extension.md)
agree with the checked classifications, pair budgets, and spectra above. Its
displayed $T_2$ is carried to this note's $T_2$ by the axial-coordinate isometry
$(a,b)\mapsto(b,a)$; it is not an additional nine-point type. The lattice counts
and the twelve-point degree and diameter-pair claims were rechecked exactly. Its
regular odd-polygon extension lemma is valid, but the two endpoint deletions
above already avoid that extra lemma.

The input leaves the twelve-point six-distance spectrum
$(1,13,13,13,13,13)$ unresolved. That is a limitation of the independent
argument, not of the current research state: the unique-diameter theorem
excludes it without classifying eleven-point five-distance sets.
The warning that arbitrary eleven-point five-distance sets need not
extend to $U$ remains essential; no such extension theorem is established.

## Comparison with the third independent input

Sections 2 and 7.1 of the
[third independent report](independent/layer_bound_and_circular_majority.md)
repeat the valid finite proof and exact spectra. Its lattice model $P$
is taken to $T_1$ by $(x,y)\mapsto(y,x)$, and its $Q$ is taken to
$T_2$ by $(x,y)\mapsto(y-1,x-1)$. These are isometries of the
axial norm $x^2+xy+y^2$, not additional classified types.
The signed-radius exceptional model is identical to the one above.
Its eight-point example, scaled by $1/(1+\sqrt3)$, is exactly the
two-square model in [circular configurations](circular_configurations.md).
The displayed multiplicities were rechecked by bounded exact pair counts.

Its twelve-point spectrum and eleven-point deletion spectrum agree
with (3) and the deletion of $(1,1)$ from $U$. The report's reference
to deleting $(0,-2)$ cannot itself be checked without its absent
companion coordinate file; the explicit $U$-model supplies the needed
certificate instead. Its endpoint-deletion approach stopping at ten
does not reopen the twelve-point case settled above. No classification
of arbitrary eleven-point five-distance sets is inferred.
