---
name: problems/distance_problems
title: Distance Problems
desc: |
  Distinct, repeated and unit distances among finite point sets, diameters and
  nearest-neighbor conditions, and distance problems for points in convex
  position.
created: 2026-09-04T09:17:27Z
updated: 2026-10-12T00:09:36Z
---

# Distance Problems

[[problems/_index|..]]

[[problems/distance_problems/E0089/_index|E0089/]]: Asks whether every set of
$n$ distinct points in the plane determines $\gg n/\sqrt{\log n}$ distinct
distances.

[[problems/distance_problems/E0090/_index|E0090/]]: Asks whether every set of
$n$ distinct points in the plane has at most $n^{1+O(1/\log\log n)}$ pairs at
distance $1$.

[[problems/distance_problems/E0091/_index|E0091/]]: Asks whether, for large $n$,
there are at least two non-similar $n$-point sets in the plane that minimize the
number of distinct distances.

[[problems/distance_problems/E0092/_index|E0092/]]: Asks for the largest $f(n)$
such that some $n$-point set in the plane has, for each of its points $x$, at
least $f(n)$ points of the set equidistant from $x$, and whether $f(n)\le
n^{o(1)}$.

[[problems/distance_problems/E0093/_index|E0093/]]: States that $n$ points in
the plane forming a convex polygon determine at least $\lfloor n/2\rfloor$
distinct distances.

[[problems/distance_problems/E0094/_index|E0094/]]: States that if $n$ points in
the plane form a convex polygon and $f(u)$ pairs of them are at distance $u$,
then $\sum_u f(u)^2\ll n^3$.

[[problems/distance_problems/E0095/_index|E0095/]]: States that if $f(u)$ pairs
among $n$ points in the plane are at distance $u$, then $\sum_u
f(u)^2\ll_\epsilon n^{3+\epsilon}$ for every $\epsilon>0$.

[[problems/distance_problems/E0096/_index|E0096/]]: Asks whether $n$ points in
the plane forming a convex polygon have only $O(n)$ pairs at distance $1$. The
answer is no, by Kruer and Kohlmeyer's Lean construction of convex point sets
with unboundedly many unit distances per point.

[[problems/distance_problems/E0097/_index|E0097/]]: Asks whether every convex
polygon has a vertex with no four other vertices equidistant from it. Erdős
first asked it with three in place of four, and Danzer's convex nonagon refutes
that version.

[[problems/distance_problems/E0098/_index|E0098/]]: Asks whether the least
number $h(n)$ of distinct distances among $n$ points in the plane, with no three
on a line and no four on a circle, satisfies $h(n)/n\to\infty$.

[[problems/distance_problems/E0099/_index|E0099/]]: Asks whether, for all large
$n$, an $n$-point set in the plane with minimum distance $1$ and the smallest
possible diameter must contain three points forming an equilateral triangle of
side $1$.

[[problems/distance_problems/E0100/_index|E0100/]]: Asks whether $n$ points in
the plane whose pairwise distances are at least $1$, and whose distinct
distances differ by at least $1$, must have diameter $\gg n$.

[[problems/distance_problems/E0103/_index|E0103/]]: Asks whether the number of
incongruent $n$-point sets in the plane with minimum distance $1$ and the least
possible diameter tends to infinity.

[[problems/distance_problems/E0130/_index|E0130/]]: Asks how large the chromatic
and clique numbers can be for the graph joining points at integer distance in an
infinite plane set with no three points on a line and no four on a circle.

[[problems/distance_problems/E0132/_index|E0132/]]: Asks whether any $n\ge5$
points in the plane determine two distances that each occur between at most $n$
pairs, and whether the number of such distances tends to infinity with $n$.

[[problems/distance_problems/E0135/_index|E0135/]]: Asks whether $n$ points in
the plane, any four of which determine at least five distinct distances, must
determine $\gg n^2$ distinct distances.

[[problems/distance_problems/E0212/_index|E0212/]]: Asks whether the plane
contains a dense set of points all of whose pairwise distances are rational.

[[problems/distance_problems/E0213/_index|E0213/]]: Asks whether, for every
$n\ge4$, there are $n$ points in the plane, no three on a line and no four on a
circle, with all pairwise distances integers.

[[problems/distance_problems/E0214/_index|E0214/]]: Asks whether the complement
of any set in the plane with no two points at distance $1$ must contain the four
corners of a unit square.

[[problems/distance_problems/E0217/_index|E0217/]]: Asks for which $n$ there are
$n$ points in the plane, no three on a line and no four on a circle, that
determine $n-1$ distinct distances, the $i$th of which occurs $i$ times.

[[problems/distance_problems/E0223/_index|E0223/]]: Asks for estimates of the
largest number $f_d(n)$ of pairs at distance $1$ among $n$ points of diameter
$1$ in $\mathbb{R}^d$.

[[problems/distance_problems/E0232/_index|E0232/]]: Asks for estimates of the
largest upper density $m_1$ of a measurable set in the plane with no two points
at distance $1$, and whether $m_1\le1/4$.

[[problems/distance_problems/E0502/_index|E0502/]]: Asks for estimates of the
largest size $M_2(n)$ of a set in $\mathbb{R}^n$ with only two distinct pairwise
distances. It is settled to leading order: $M_2(n)=n^2/2+O(n)$.

[[problems/distance_problems/E0503/_index|E0503/]]: Asks for the largest size of
a set $A\subseteq\mathbb{R}^d$ in which every three points form an isosceles
triangle.

[[problems/distance_problems/E0604/_index|E0604/]]: Asks whether any $n$
distinct points in the plane must include a point with $\gg n^{1-o(1)}$ distinct
distances to the others.

[[problems/distance_problems/E0605/_index|E0605/]]: Asks whether $n$ points on a
sphere can have at least $f(n)n$ pairs at the same distance, for some
$f(n)\to\infty$.

[[problems/distance_problems/E0652/_index|E0652/]]: Asks whether the least
possible number of distinct distances from the $k$-th of $n$ planar points, in
units of $\sqrt{n}$, tends to infinity with $k$. Erdős's first guess, that it is
unbounded already at $k=3$, fails by a construction of Elekes.

[[problems/distance_problems/E0653/_index|E0653/]]: Asks whether the counts of
distinct distances from each of $n$ planar points to the others can take
$(1-o(1))n$ different values; yes, by an unrefereed Lean proof that
Conjectures.io kernel-checked and certified.

[[problems/distance_problems/E0654/_index|E0654/]]: Asks to estimate how many
distinct distances to the others some point must have, among any $n$ points in
the plane with no four on a circle.

[[problems/distance_problems/E0655/_index|E0655/]]: Asks whether $n$ points in
the plane determine at least $(1+c)n/2$ distinct distances when no circle
centered at one of them contains three others.

[[problems/distance_problems/E0657/_index|E0657/]]: Asks whether $n$ planar
points with no isosceles triangle must determine at least $f(n)n$ distinct
distances, for some $f(n)\to\infty$.

[[problems/distance_problems/E0659/_index|E0659/]]: Asks whether $n$ planar
points can have every four of them determine at least three distances while the
number of distinct distances is $\ll n/\sqrt{\log n}$.

[[problems/distance_problems/E0660/_index|E0660/]]: Asks whether the $n$
vertices of a convex polyhedron in $\mathbb{R}^3$ always determine at least
$(1-o(1))n/2$ distinct distances.

[[problems/distance_problems/E0661/_index|E0661/]]: Asks whether, for all large
$n$, two sets of $n$ planar points can have only $o(n/\sqrt{\log n})$ distinct
distances between the two sets.

[[problems/distance_problems/E0662/_index|E0662/]]: Asks whether $n$ points at
mutual distance at least $1$ have at most $f(t)$ distances at most $t$, where
$f(t)$ is the triangular lattice's count. As worded the question is garbled and
fails under every counting reading, and a disproof is claimed.

[[problems/distance_problems/E0668/_index|E0668/]]: Asks whether the number of
incongruent $n$-point planar sets maximizing the number of unit distances tends
to infinity, and whether it exceeds $1$ for every $n>3$.

[[problems/distance_problems/E0670/_index|E0670/]]: Asks whether $n$ points in
$\mathbb{R}^d$ whose pairwise distances all differ by at least $1$ must have
diameter at least $(1+o(1))n^2$.

[[problems/distance_problems/E0754/_index|E0754/]]: Asks whether $f(n)\le
n/2+O(1)$, where $f(n)$ is the largest number such that some $n$ points in
$\mathbb{R}^4$ have every point equidistant from at least $f(n)$ of the others.

[[problems/distance_problems/E0756/_index|E0756/]]: Asks whether a set of $n$
points in the plane can determine $\gg n$ distinct distances, each occurring for
more than $n$ pairs of points.

[[problems/distance_problems/E0953/_index|E0953/]]: Asks how large the measure
of a set in a disc of radius $r$ can be if no two of its points are at an
integer distance.

[[problems/distance_problems/E0956/_index|E0956/]]: Asks for the largest number
$h(n)$ of unit distances among $n$ disjoint translates of a compact convex set,
in particular whether $h(n)>n^{1+c}$ for some $c>0$.

[[problems/distance_problems/E0957/_index|E0957/]]: Asks whether the
multiplicities of the smallest and largest distances among $n$ points in the
plane have product at most $(9/8+o(1))n^2$.

[[problems/distance_problems/E0958/_index|E0958/]]: Asks whether $n$ planar
points with $n-1$ distances of multiplicities $n-1,\ldots,1$ must be equally
spaced on a line or a circle.

[[problems/distance_problems/E0959/_index|E0959/]]: Asks to estimate the largest
possible gap between the two highest distance multiplicities determined by a set
of $n$ points in the plane.

[[problems/distance_problems/E0982/_index|E0982/]]: Asks whether $n$ points in
convex position in the plane always include a vertex with at least $\lfloor
n/2\rfloor$ distinct distances to the other vertices.

[[problems/distance_problems/E1082/_index|E1082/]]: Asks whether $n$ points in
the plane with no three collinear always determine at least $\lfloor n/2\rfloor$
distinct distances, even as seen from a single point.

[[problems/distance_problems/E1083/_index|E1083/]]: Asks to estimate the least
number $f_d(n)$ of distinct distances determined by $n$ points in $\mathbb{R}^d$
for $d\ge3$, and whether $f_d(n)=n^{2/d-o(1)}$.

[[problems/distance_problems/E1084/_index|E1084/]]: Asks to estimate the largest
number of pairs at distance exactly $1$ among $n$ points in $\mathbb{R}^d$ that
are pairwise at distance at least $1$.

[[problems/distance_problems/E1085/_index|E1085/]]: Asks to estimate the largest
number of pairs at distance exactly $1$ among $n$ points in $\mathbb{R}^d$.

[[problems/distance_problems/E1086/_index|E1086/]]: Asks to estimate the largest
number of triangles of equal area whose vertices come from a set of $n$ points
in the plane.

[[problems/distance_problems/E1087/_index|E1087/]]: Asks to estimate the largest
number of four-point subsets with two pairs at equal distance among $n$ points
in the plane, and whether it is at most $n^{3+o(1)}$.

[[problems/distance_problems/E1089/_index|E1089/]]: Asks to estimate $g_d(n)$,
the least number such that any $g_d(n)$ points in $\mathbb{R}^d$ determine at
least $n$ distinct distances, and whether $\lim_{d\to\infty}g_d(n)/d^{n-1}$
exists.

[[problems/distance_problems/E1207/_index|E1207/]]: Asks to estimate $P_d(n)$,
the size of the largest subset with no isosceles triangle that any $n$ points in
$\mathbb{R}^d$ must contain, in particular whether $P_2(n)<n^{1-c}$ for some
$c>0$.

[[problems/distance_problems/E1208/_index|E1208/]]: Asks for an estimate of
$F_d(n)$, the largest number of points with all distances distinct that every
set of $n$ points in $\mathbb{R}^d$ must contain, for fixed $d\ge2$ as
$n\to\infty$.

***

Distinct, repeated and unit distances among finite point sets, diameters and
nearest-neighbor conditions, and distance problems for points in convex
position.

Site tags routed here: chromatic number, convex, distances, geometry, graph
theory, ramsey theory.
