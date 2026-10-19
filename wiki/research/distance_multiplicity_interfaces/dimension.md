---
name: research/distance_multiplicity_interfaces/dimension
title: "Realization rank and dimension-sensitive constructions"
desc: "Euclidean rank, few-distance examples and extremal unit-distance products explain why abstract or growing-dimensional constructions do not transfer automatically."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/distance_problems/E0503/_index|E0503]],
[[problems/distance_problems/E0670/_index|E0670]],
[[problems/distance_problems/E0668/_index|E0668]],
[[problems/distance_problems/E1085/_index|E1085]],
[[problems/distance_problems/E0660/_index|E0660]].

## Dimension, extremal constructions and realization rank

## E0503: the elementary family and the rank condition

For $d\ge2$, take the vectors $e_i+e_j$, $i<j$, in $\mathbb R^{d+1}$. They lie
in the affine hyperplane $\sum x_i=2$, of dimension $d$. Distinct vectors have
squared distance two or four, according as their two-element supports intersect
or are disjoint. Their centroid is $c=(2/(d+1),\ldots,2/(d+1))$; each original
vector has squared distance $2-4/(d+1)>0$ to it. Adding $c$ preserves the
isosceles-triple property. This proves $f(d)\ge\binom{d+1}{2}+1$. Blokhuis's
held upper bound $\binom{d+2}{2}$ leaves exactly $d$ points of slack.

To turn a proposed two-distance edge coloring into Euclidean points, let $S$ be
its proposed squared-distance matrix and $H=I-\mathbf1\mathbf1^T/N$. The
necessary and sufficient realization condition is $-HSH/2\succeq0$ of rank at
most $d$, with positive off-diagonal distances and zero diagonal. Necessity
follows from centering coordinates; for sufficiency factor the PSD matrix into a
Gram matrix and recover $S_{ij}=B_{ii}+B_{jj}-2B_{ij}$. Thus the residual step
is Euclidean rank and positivity, not simply a triangle coloring. The Blokhuis
result page was read at statement/account depth, not the tract proof. The
pending general reduction was not re-audited; this account does not depend on
accepting it.

## E0670: a dimension obstruction and an exact line bound

This problem separates all $\binom n2$ pair lengths by at least one, in a fixed
ambient dimension. For $n\ge3$, take any pair $a,b$ and a third point $c$. The
two distinct lengths $|a-c|,|b-c|$ differ by at least one; the reverse triangle
inequality gives $|a-b|\ge1$. Sorting all pair lengths now gives the elementary
diameter bound $\binom n2$, with coefficient one half.

In dimension one write $x_1<\cdots<x_n$. For any integer $1\le k<n$, take all
lengths $x_{i+j}-x_i$ with $1\le j\le k$. There are $T=kn-k(k+1)/2$ of them.
They are distinct, mutually one-separated and at least one, so their sum is at
least $T(T+1)/2$. Each adjacent gap $x_{i+1}-x_i$ enters at most $j$ terms with
index gap $j$, hence at most $k(k+1)/2$ terms altogether. If $\Delta=x_n-x_1$,
then
$$
 \Delta\ge\frac{T(T+1)}{k(k+1)}.
$$
Taking $k=\lfloor\sqrt n\rfloor$ proves $\Delta\ge n^2-O(n^{3/2})$. This is a
complete line argument, not a proof in an arbitrary fixed dimension.

Ho's inspected construction uses all nontrivial Fourier modes on an odd cyclic
group of order $m$, with positive weights $W_r$:
$$
 v_t=(\sqrt{W_r}\cos(2\pi rt/m),
       \sqrt{W_r}\sin(2\pi rt/m))_{r=1}^{(m-1)/2}.
$$
Any affine relation among a selected subset extends to real coefficients
$\alpha_t$ on all $m$ indices, zero elsewhere, with $\sum_t\alpha_t=0$. The
relation among the vectors annihilates all nonzero Fourier coefficients because
every $W_r$ is positive; reality also supplies the conjugate modes. The zero
coefficient vanishes by the affine condition. Fourier inversion gives
$\alpha_t=0$ for all $t$. Thus every selected $n$-point subset is affinely
independent and has intrinsic dimension $n-1$.

The construction can therefore be compressed from its displayed $n^2-n$ ambient
dimension to $n-1$, but not below that. The pair-distance matrix determines the
centered Gram rank, so a different isometric embedding cannot repair the
dimension. This is a precise obstruction to using this construction against the
fixed-$d$ question. The entire short primary text was read, and positivity of
the weights was checked on PDF page 3. Its [arXiv
record](https://arxiv.org/abs/2604.15305) was consulted for identity; no
independent review or Lean check was performed.

## E0668: finite families of optimal unit-distance sets

Let $T$ be a unit equilateral triangle. For a unit segment with direction $v$,
the Minkowski sum $T+\{0,v\}$ generically has six distinct points, six unit
edges inside the two copies of $T$, and three matching unit edges. The inspected
value $u(6)=9$ makes it optimal. Relative rotation changes some cross distances
continuously, so the family has continuum many congruence classes: a fixed
finite distance multiset cannot contain a continuously varying edge value.

Likewise let $W_7$ be the centered regular unit hexagon, with 12 unit edges.
Generically $T+R_\theta W_7$ has 21 distinct points, $3\cdot12$ unit edges
within copies of the wheel and $3\cdot7$ matching triangle edges. The inspected
value $u(21)=57$ makes this family optimal. A relative rotation again supplies
continuum many congruence classes. These constructions and the flexibility
warning were inspected in Alexeev--Mixon--Parshall's Appendix A, with the
extremal counts in Theorem 1/Table 1. The source's exhaustive computation was
not rerun. More generally, an equality $u(3m)=3u(m)+3m$ would make this product
strategy useful, subject to distinctness of the points. No eventual family of
such equalities was obtained.

At order four, five unit edges are attainable by two equilateral triangles on
opposite sides of a shared unit edge. Six are impossible: the fourth point
cannot be unit distance from all vertices of a unit triangle. Any five-edge
graph is $K_4$ minus one edge, so its two remaining vertices must occupy the two
intersections of the unit circles about the common edge's endpoints. They must
be distinct, hence on opposite sides. The resulting diamond is unique up to
congruence. This disproves the all-$n>3$ subassertion already discussed on the
problem page, while the eventual-divergence question remains. No standing
promotion is made.

## E1085: why the high-dimensional construction does not descend

Swanepoel's inspected Lenz theorem has $d\ge4$ as a hypothesis. Its populated
orthogonal circles need two orthogonal two-dimensional linear subspaces. They
cannot both occur in $\mathbb R^3$. Replacing one circle by the orthogonal axis
does not give a large second part: if the circle has radius $r$, every axis
point at unit distance from all its points satisfies $z^2=1-r^2$, allowing at
most two points. Thus this complete-bipartite mechanism does not give quadratic
unit-distance growth in dimensions two or three. A different construction is
needed; this does not exclude all other geometries. Minimum-one packing contact
bounds are linear because of the extra separation hypothesis, which E1085 does
not have.

## E0660: a spatial source gap

E0660 is an explicit source gap. The held planar Altman theorem does not state
the three-dimensional convex-polyhedron result. Erdős's 1975 Section 1, page
101, reports a bound $cn$ in three dimensions but gives neither the constant
needed here nor a located proof. The target coefficient is $1/2-o(1)$; an
unspecified positive $c$ does not imply it. Nor does projection provide a
transfer: projecting can split equal spatial lengths and can turn vertices into
interior planar points. The scoped primary-source search found the historical
attribution, not the original three-dimensional argument. The needed primary
spatial argument remains unidentified here.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/distance_problems/alexeev_2024_erdos_unit_distance_problem_small_point/_index|alexeev
  2024 erdos unit distance problem small point]]: Appendix A geometric
  discussion of n=6 and n=21 Minkowski sums; not the computational
  extremal-count proof (proof reading). Section 1 Theorem 1 and Table 1
  (statement reading).
- [[../library/distance_problems/altman_1963_problem_p_erdos/_index|altman 1963
  problem p erdos]]: Theorem on printed p.149; planar domain and proof scope
  (account reading).
- [[../library/distance_problems/blokhuis_1984_few_distance_sets/_index|blokhuis
  1984 few distance sets]]: Statement and equality condition of Theorem 7.2.5;
  source proof pointer (account reading).
- [[../library/distance_problems/erdos_1975_problems_elementary_combinatorial_geometry/_index|erdos
  1975 problems elementary combinatorial geometry]]: Section 1,
  higher-dimensional attribution on printed p.101 (account reading).
- [[../library/distance_problems/ho_2026_erdos_s_diameter_conjecture_separated_distances/_index|ho
  2026 erdos s diameter conjecture separated distances]]: Sections 2-4,
  Proposition 4, equation (4), Propositions 5 and 8; Remark 9 (proof reading).
- [[../library/distance_problems/swanepoel_2009_unit_distances_diameters_euclidean_spaces/_index|swanepoel
  2009 unit distances diameters euclidean spaces]]: Section 1.1; Section 2 Lenz
  definitions and Theorem 1 (statement reading).
