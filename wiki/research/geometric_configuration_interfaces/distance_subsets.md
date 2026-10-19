---
name: research/geometric_configuration_interfaces/distance_subsets
title: "Repeated distances and geometric Sidon subsets"
desc: "Isosceles triples govern bad four-sets; robust multiplicity and deletion estimates retain distinct exponents and dimension conventions."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/distance_problems/E1087/_index|E1087]],
[[problems/discrete_geometry/E1088/_index|E1088]],
[[problems/distance_problems/E1207/_index|E1207]],
[[problems/distance_problems/E1208/_index|E1208]].

## Repeated distances: E1087, E1088, E1207, E1208

Erdős--Purdy, Section 4 on printed page 251, describes bad four-sets by failure
of all six distances to be different. The repeated pairs may share an endpoint.
Define I(P) to count unordered distinct-point triples having two equal side
distances, including a collinear midpoint triple; D(P) the bad four-sets; and
Q(P) the ordered nonzero-distance energy
$$
 Q(P)=|\{(a,b,c,d)\in P^4:|a-b|=|c-d|>0\}|.
$$
The elementary inequalities
$$
\frac{(n-3)I(P)}4\le D(P)\le Q(P)+(n-3)I(P)
$$
are proved in
[[theory/discrete_geometry/L29_repeated_distance_counting/_index|L29]]. They
distinguish equalities sharing a vertex from disjoint-pair equalities.

Guth--Katz Proposition 2.2 states $Q(P)=O(n^3\log n)$; its definition and
statement were inspected in the published-version transcription, not the proof
of the energy estimate. It follows from L29 that the uniform E1087 bound
$D(P)\le n^{3+o(1)}$ is equivalent to the uniform bound $I(P)\le n^{2+o(1)}$. In
the forward direction divide the lower inequality by $n-3$; in the reverse
direction use the upper inequality and $n^3\log n=n^{3+o(1)}$. Degenerate
midpoint triples number at most binom(n,2), because their two outer points
determine the midpoint, so excluding them does not change this exponent
equivalence.

For an explicit failed disjoint-pair reduction, take (0,0),(1,0),(0,1),(3,4).
The six squared distances are 1,1,2,25,20,18. The sole equality shares the
vertex (0,0), so the four-set is bad but has no equal disjoint edge pairs. The
recent primary paper Geometric Sidon Problems, Section 4 after Lemma 4, also
explicitly leaves the analogous near-quadratic isosceles bound open; see
https://arxiv.org/html/2606.05841v1. The next test of any energy proof is its
treatment of arbitrary fourth-point extensions of isosceles triples.

E1088 reverses the asymptotic roles: k is fixed and dimension d grows. For k=3
an explicit lower construction is the set of all e_i+e_j, i<j, in R^(d+1). It
lies in the affine hyperplane with coordinate sum two, hence in a copy of R^d,
and has binom(d+1,2) points. Distances are sqrt(2) when index pairs meet and 2
when they are disjoint, so every triple is isosceles. Therefore
f_d(3)>binom(d+1,2). The Blokhuis theorem card gives the upper bound
f_d(3)<=binom(d+2,2)+1, yielding d squared/2+O(d), with the tract's standing
retained. For k>=4, inverting a fixed-d subset bound of scale N^(1/(3d-3))
yields, even with favorable constants, only an exponential-in-d threshold.
Unspecified d-dependent constants make the transfer weaker still. Abstract
edge-color patterns require positive-semidefinite Gram matrices of rank at most
d to become Euclidean configurations. The next test is a structure theorem for
no-rainbow-four-set configurations with explicit dimension dependence, not a
fixed-d asymptotic substitution.

For E1207 and E1208, the primary Lee--Pohoata--Zhu statement was inspected at
https://arxiv.org/html/2607.05374v1, Section 1 and Applications. Its proof was
not checked. It asserts an N-point planar set P such that for every A contained
in P of size at least two, the largest ordered multiplicity of a positive
distance satisfies
$$
 \mu(A)\geq c|A|^2/N^{1-\delta}
$$
for absolute positive c,delta. If A is isosceles-free, every graph of edges of
one distance has maximum degree at most one, so mu(A)<=|A|. Thus
|A|<=c^(-1)N^(1-delta). If all unordered-pair distances in A differ, mu(A)=2 and
|A|<=sqrt(2/c)N^((1-delta)/2). Renaming a smaller positive constant absorbs
prefactors for all sufficiently large N. The exponent saving in the second
conclusion is half the displayed delta, before any renaming. These are checked
specializations of an external pending theorem, not audits of that theorem or
complete order estimates.

If the target instead excludes only noncollinear isosceles triangles, each
fixed-distance graph has degree at most two: three distinct neighbors on a
circle about one vertex contain a pair not opposite through that vertex. They
would form a noncollinear equal-side triple. Then mu(A)<=2|A| gives the same
exponent with constant 2/c. Thus the particular polynomial-saving specialization
survives either degeneracy convention.

There is also an elementary obstruction to a claimed square-root upper
construction for E1207 using regular polygons. Label the vertices of a regular
m-gon by Z/mZ. Equal chords from apex a to different b,c occur exactly when
b+c=2a modulo m, since a chord is determined by its cyclic separation up to
sign. For any positive t, take m=2 times 3^t and
$$
 B_t=\left\{\sum_{i=0}^{t-1}\epsilon_i3^i:
                 \epsilon_i\in\{0,1\}\right\}.
$$
This has 2^t elements in [0,(3^t-1)/2]. An equality b+c=2a modulo m within this
interval cannot wrap, so is an integer equality. Base-three addition of b+c and
doubling a involve no carries; every digit of 2a is zero or two. Thus the
corresponding digits of b and c must be equal, and b=c=a. The polygon vertices
indexed by B_t are isosceles-free and have size (m/2)^(log_3 2), with exponent
greater than one half. In particular these regular polygons do not have maximum
isosceles-free subset O(sqrt(m)). This does not give a general lower bound for
arbitrary planar sets.

Finally, E1208 is read in the intended largest-guaranteed-subset sense stated in
its assessment, not the literal trivial minimum of the displayed wording. The
Charalambides Section 2 deletion proof uses at most aN^(7/3) equal-side triples
and bN cubed log N equal-distance quadruples. Sampling with probability q and
deleting one point from each surviving bad pattern leaves expected size at least
$$
 qN-aq^3N^{7/3}-bq^4N^3\log N.
$$
For q=epsilon N^(-2/3)(log N)^(-1/3), the main term is epsilon N^(1/3)(log
N)^(-1/3), the triple error divided by that term is a epsilon squared (log
N)^(-2/3), and the quadruple error ratio is b epsilon cubed. Choose epsilon with
the latter ratio below one quarter and then take N large enough for the former
to be below one quarter. This proves Omega(N^(1/3)/(log N)^(1/3)) directly from
the source's inputs. The primary Theorem 1 of Geometric Sidon Problems gives a
newer Omega(N^(1/3)) lower bound; its statement and hypergraph-independence
setup were read but not its whole proof. Even with the conditional LPZ upper
bound above, the planar exponents do not match. A useful next test must verify
all codegree hypotheses of a stronger independence theorem on the exact
rank-three/rank-four collision hypergraph, including shared endpoints.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/distance_problems/blokhuis_1984_few_distance_sets/_index|blokhuis
  1984 few distance sets]]: Statement, definitions and proof pointer (account
  reading).
- [[../library/distance_problems/charalambides_2013_note_distinct_distance_subsets/_index|charalambides
  2013 note distinct distance subsets]]: Section 2, Proposition 2.1 and deletion
  proof (proof reading).
- [[../library/distance_problems/erdos_1971_extremal_problems_geometry/_index|Erdős–Purdy:
  Some extremal problems in geometry]]: Section 4, p. 251: all six distances
  condition (statement reading).
- [[../library/distance_problems/guth_2015_erdos_distinct_distance_problem_plane/_index|On
  the Erdős distinct distance problem in the plane]]: Section 2, definition
  (2.1), Lemma 2.1 and Proposition 2.2; Proposition 2.2 proof not inspected
  (statement reading).
