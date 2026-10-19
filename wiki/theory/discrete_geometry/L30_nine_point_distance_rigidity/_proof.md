---
name: theory/discrete_geometry/L30_nine_point_distance_rigidity/_proof
title: A nonsingular distance-equality minor
desc: The inverse function theorem and separated distance intervals turn an exact Jacobian minor into local similarity rigidity.
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

In the coordinates of
[[theory/discrete_geometry/L30_nine_point_distance_rigidity/_index|L30]],
squared length is $q(a,b)=a^2+ab+b^2$. The
[[theory/discrete_geometry/L30_nine_point_distance_rigidity/evidence/_index|exact checker]]
enumerates all 36 pairs. Their squared lengths and multiplicities are

$$
\begin{array}{c|rrrrrrrr}
q&1&3&4&7&12&13&19&21\\\hline
m_q&7&3&2&8&5&6&4&1.
\end{array}
$$

The only collinear triple is $(1,2,3)$, with indices starting at zero.
The only cocircular quadruples are $(0,2,3,4)$ and $(4,6,7,8)$; each
has no collinear triple, so each is a genuine circle.

In each distance class take its lexicographically first edge as a base,
and subtract its squared length from every other edge's. This gives 28
polynomial equations in 18 coordinates. The derivative of an edge with
difference $(a,b)$ is $(2a+b,a+2b)$ at its first endpoint and its negative
at the other endpoint.

Fix both coordinates of points 0 and 1. These points are distinct, and
there is a unique orientation-preserving similarity taking any nearby
ordered pair to this fixed pair. Thus this is a continuous local gauge for
the four similarity parameters. In the remaining coordinate order
$(a_2,b_2,\ldots,a_8,b_8)$, use the 14 equations with edge/base pairs

$$
\begin{split}
&(03,01),(24,01),(28,01),(48,01),(56,01),(67,01),\\
&(23,13),(57,13),(38,37),(07,02),(08,02),(17,02),\\
&(26,02),(27,02).
\end{split}
$$

Their exact square Jacobian has determinant $-1102248$. The complete
matrix is retained as an input to the checker, which recomputes it and
its determinant from the points. The inverse function theorem therefore
isolates the original gauged configuration among solutions of these
equations. In particular, a sufficiently close realization of the entire
distance partition is similar to it.

Choose disjoint open intervals about the eight original positive lengths.
By continuity, in a sufficiently small neighborhood each edge remains in
its original interval, and each interval still contains an edge. A
configuration there with at most eight distinct distances must have
exactly one distance in each interval. No original class can split, so
the entire distance partition is preserved. Apply the preceding local
uniqueness after the continuous gauge. Similarities preserve collinearity
and cocircularity, proving the final assertion.
