---
name: research/leads/concentric_polygon_census/sketch
title: Critical-parameter reduction and editable argument
desc: |
  Exact definitions, complete exceptional-parameter equations, convexity
  tests and remaining obligations for two bounded symmetric-family searches
  for a counterexample to Problem 982.
created: 2026-10-16T13:41:30Z
updated: 2026-10-16T13:41:30Z
---

***

This is the canonical argument for the
[[research/leads/concentric_polygon_census/_index|symmetric polygon census]].
The deductions below and the completed [census](census.md) are author-recorded
by Plasma AI. No independent proof review is asserted. The census exhausts
exactly the finite domains specified here and finds no counterexample.

## Target and specified domains

Write $D_v$ for the number of distinct positive distances from vertex $v$ to
the other vertices. A witness against
[[problems/distance_problems/E0982/_index|Problem 982]] must be strictly convex
and satisfy $\max_v D_v<\lfloor n/2\rfloor$.

The first domain consists of every integer $3\le m\le32$ and all real
$r>0$, with vertices

$$
 A_k=e^{2\pi i k/m},\qquad B_k=r e^{(2k+1)\pi i/m},
 \qquad 0\le k<m.
$$

All positive critical radii are enumerated, including nonconvex ones, then
filtered to $\cos(\pi/m)<r<\sec(\pi/m)$. There are $n=2m$ vertices and
two rotation orbits, so a witness needs $D_A<m$ and $D_B<m$ simultaneously.

The second domain consists of every integer $8\le n\le24$ and all real
$s>0$, with vertices

$$
 p_k=(\cos(2\pi k/n),\sqrt{s}\sin(2\pi k/n)),
 \qquad 0\le k<n.
$$

All positive critical values of $s$ are enumerated and every vertex is
checked. The generic complement is covered symbolically. Every positive $s$
preserves strict convexity by an invertible affine map of a regular polygon.
The stretching axes are exactly those in the displayed coordinates: arbitrary
orientations of those axes relative to the polygon are not included. Neither
finite order range exhausts unbounded orders or other families.

For $r=1$ or $s=1$ all vertices are on one circle. Any circle centered at a
vertex intersects that common circumcircle in at most two points. Therefore
$D_v\ge\lceil(n-1)/2\rceil=\lfloor n/2\rfloor$ at every vertex. This
argument disposes of the common-circle case without searching that family.

## Concentric distance and convexity reduction

Put $\theta=\pi/m$, $h=\lfloor m/2\rfloor$, and $q=\lceil m/2\rceil$.
The distinct within-ring squared distances at $A_0$ are

$$
 a_i=2-2\cos(2i\theta)\quad(1\le i\le h),
$$

and at $B_0$ they are $r^2a_i$. The cross-ring squared distances at both
orbits are

$$
 b_j(r)=1+r^2-2c_jr,\qquad
 c_j=\cos((2j+1)\theta)\quad(0\le j<q).
$$

Each displayed list is injective for $r>0$: its angles run strictly through
$(0,\pi]$ and cosine is strictly decreasing there. Reflection accounts for
all omitted vertices. Thus the generic count at either orbit is $h+q=m$.
Every exceptional radius is a positive real root of

$$
 P_{ij}(r)=r^2-2c_jr+1-a_i,\qquad
 Q_{ij}(r)=(1-a_i)r^2-2c_jr+1=r^2P_{ij}(1/r).
$$

There are no within-list exceptional equalities. Let $u$ count the pairs
$(i,j)$ with $P_{ij}(r)=0$, and $v$ those with $Q_{ij}(r)=0$. Injectivity
makes each matching a disjoint identification of two lengths, so

$$
 (D_A,D_B)=(m-u,m-v).
$$

In particular, a witness requires at least one event of each type at the
same radius. Radius reciprocity exchanges the two counts. Repeated roots,
linear equations, zero roots and repeated descriptions of one radius must
be handled exactly.

In increasing angular order the polygon is
$A_0,B_0,A_1,B_1,\ldots,A_{m-1},B_{m-1}$. Each edge stays inside its
angular sector, so nonadjacent edges do not meet. Its successive edge
determinants at the two vertex types are

$$
 2r\sin\theta(1-r\cos\theta),\qquad
 2\sin\theta(r-\cos\theta).
$$

The polygon is therefore strictly convex exactly when
$\cos\theta<r<1/\cos\theta$. Both endpoints are degenerate and excluded.
For any possible counterexample, reconstruct its full exact vertex list,
verify all supporting-edge inequalities, and retain the distance partition
at every vertex, as an additional check of the reduction.

The eight-point example in
[[research/distance_multiplicity_interfaces/exact_optimizers|the local
obstruction account]] has $m=4$, $r=(1+\sqrt3)/\sqrt2$ after similarity,
and counts $(3,3)$. Since $r>\sqrt2$, it fails the strict-convexity test.
It is a negative control, not a witness against Problem 982.

## Affine distance reduction

With $\alpha_k=2\pi k/n$, every squared distance from pin $i$ has the form
$X_{ij}+sY_{ij}$, where

$$
\begin{aligned}
X_{ij}&=1+\tfrac12(\cos(2\alpha_i)+\cos(2\alpha_j))
           -\cos(\alpha_i-\alpha_j)-\cos(\alpha_i+\alpha_j),\\
Y_{ij}&=1-\tfrac12(\cos(2\alpha_i)+\cos(2\alpha_j))
           -\cos(\alpha_i-\alpha_j)+\cos(\alpha_i+\alpha_j).
\end{aligned}
$$

Equivalently these are the squares of the horizontal and vertical coordinate
differences before scaling. Two such lines coincide for every $s$ exactly
when both coefficients agree. Otherwise their only possible equality is

$$
 s=\frac{X_{ik}-X_{ij}}{Y_{ij}-Y_{ik}},
$$

provided the denominator is nonzero. Equal slopes and unequal intercepts
never meet. Enumerating these positive quotients for every pin and every
unordered pair of its other vertices covers every exceptional parameter.
Away from them the symbolic pairs $(X,Y)$ give the complete partition.
Specialization can only merge generic classes, so every generic pin count is
at least its count at $s=1$, which meets the target by the circle argument.
Only positive critical parameters can be counterexamples.

## Exact arithmetic and completeness

Use rational polynomials modulo $\Phi_{2m}$ for concentric coefficients and
modulo $\Phi_n$ for affine coefficients, with the embedding
$\zeta_N=e^{2\pi i/N}$. Polynomial remainders decide equality; certified
real enclosures select the intended embedding and decide strict signs.
Any unresolved enclosure must refine or fail, never count as equality.
Concentric radii are roots of degree-at-most-two equations over this field;
common-root tests and their selected real branches identify duplicates.
Affine parameters are exact field quotients.

For completeness of the common-root test, normalize two quadratics to
$f=x^2+bx+c$ and $g=x^2+dx+e$. If $b=d$, they have a common root only when
$c=e$, and their selected branches must agree. If $b\ne d$, their only
possible common root is $x=(e-c)/(b-d)$. Substitute this exact field value
in both polynomials. For a positive discriminant, its branch is determined
by the sign of $2x+b$. Linear and double-root cases are field values.
This covers reducible quadratics too; no irreducibility assumption on an
event polynomial is used. Disjoint certified intervals prove inequality;
overlap alone never identifies roots. The precision cap causes failure
if distinct values cannot be separated.

The [checker](evidence/_index.md) enumerates every equation or quotient
above, retains every positive real root, merges exact duplicates, and checks
the distance counts. Concentric counts use the complete matching lists;
the full $2m-1$ vertex labels are additionally partitioned directly at every
strictly convex event, every event lowering both orbits, and all events for
$m\le5$. For the affine family every one of the $n-1$ distances at every
pin is evaluated exactly at every critical parameter. The resulting new
equalities must agree exactly with the generated events. These checks and
the generic-complement arguments compose into the stated bounded exclusion.

## Outcome and remaining gap

The [census](census.md) contains no surviving counterexample. At each tested
concentric order the only admissible events are $P_{h,q-1}=0$ and its
reciprocal $Q_{h,q-1}=0$, at distinct radii. They give $(D_A,D_B)=(m-1,m)$
and $(m,m-1)$. The first radius has the explicit form

$$
 \rho_m=
 \begin{cases}
  \sqrt{3+\cos^2(\pi/m)}-\cos(\pi/m),&m\text{ even},\\
  2\cos(\pi/(2m))-1,&m\text{ odd}.
 \end{cases}
$$

These identities follow by solving the displayed farthest-distance equation.
The assertion that no other events are admissible is certified here only for
$3\le m\le32$. The two formulas do not extend that finite coverage.

For the affine family, the table gives the minimum of $\max_i D_i$ among
noncircular critical parameters. Together with the generic counts and the
circle argument this excludes every $s>0$ for each $8\le n\le24$.

The failed step in the intended disproof is constructing simultaneous
distance reductions at every vertex while preserving strict convexity.
That existence input is false in these two bounded domains according to
the author-recorded exact census. It remains unresolved outside them.
No external classification or provisional literature claim is a premise.
There is no remaining computation inside the specified domains and no
independent review of this account.

Reopening requires a different domain with a plausible source of more
simultaneous equalities: an order outside the bounds, a different angular
offset, or additional independently placed vertex orbits, for example. The
next discriminating test is whether such a construction can lower every
orbit's count at one exact parameter while passing all strict convexity
inequalities. Merely enlarging a floating grid would not answer it. This
bounded exclusion supplies no claim about all convex polygons.
