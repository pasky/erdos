---
name: theory/discrete_geometry/L143_split_class_rarity/_proof
title: Extreme anchors and absolute displacements
desc: Unsplit classes have fixed absolute displacements, so long ones have maximum degree two; anchor distances outside split circles give the rare classes.
created: 2026-10-15T11:12:05Z
updated: 2026-10-15T11:12:05Z
---

***

Use the definitions in
[[theory/discrete_geometry/L143_split_class_rarity/_index|L143]] and write
$\kappa=\kappa(A)$. Fix $S$ with exactly $\kappa$ split classes and
orthonormal coordinates in which $S=\lambda\operatorname{diag}(1,-1)$,
$\lambda\ne0$. Then $d^{\mathsf T}Sd=\lambda(d_x^2-d_y^2)$. In a class that is
not $S$-split, $d_x^2-d_y^2$ and $d_x^2+d_y^2$ are both constant, so all its
pairs have the same absolute displacements, say $(a,b)$.

If all points lie on one vertical line, every displacement is vertical. Each
class is then a union of vertical paths with at most $n-1$ pairs, and the
distances from the lowest point give $R(A)\ge n-1$, which implies the claim.
Otherwise let the abscissae fill $[m,M]$ with $W=M-m>0$, let $c$ points lie on
the middle line $x=(m+M)/2$, and choose $p_L,p_R\in A$ with abscissae $m$ and
$M$.

An unsplit class with $a>W/2$ has at most $n$ pairs. A neighbor of $v$ in it
lies at $v+(\pm a,\pm b)$, and the abscissae $x_v+a$ and $x_v-a$ cannot both
lie in $[m,M]$ because they differ by $2a>W$. So $v$ has neighbors in one
column only, at most two of them, and a graph of maximum degree two on $n$
vertices has at most $n$ edges. An unsplit class with $a=0$ consists of
vertical pairs of one length. On each vertical line every point has at most one
neighbor above and one below, so the class is a union of paths and has at most
$n-1$ pairs.

For each point $z$ strictly right of the middle line, consider the class of
$|z-p_L|$; for each point strictly left, the class of $|z-p_R|$. These pairs
have $|d_x|>W/2$. If such a class is unsplit, it is rare by the preceding
paragraph. If it is split, $z$ lies on one of at most $\kappa$ circles about
$p_L$, or about $p_R$, with split radii, so at most $2\kappa M(A)$ of the
$n-c$ off-middle points meet a split class. An unsplit class with absolute
displacements $(a,b)$ is reached from $p_L$ only by $p_L+(a,\pm b)$ and from
$p_R$ only by $p_R+(-a,\pm b)$, so by at most four of these points. This gives
at least $(n-c-2\kappa M(A))/4$ rare classes, all with $a>W/2$.

If $c\ge2$, let $z_0$ be the lowest middle point. The $c-1$ vectors from $z_0$
to the other middle points are vertical with distinct lengths, and each split
length is attained by only one of them. Their unsplit classes have $a=0$ and
are rare, which gives at least $c-1-\kappa$ further rare classes. They differ
from the classes of the previous paragraph, whose common $a$ is positive.
Therefore

$$
R(A)\ge\max\Bigl\{0,\frac{n-c-2\kappa M(A)}{4}\Bigr\}+\max\{0,c-1-\kappa\}.
$$

For $c=0$ this implies the claim. For $c\ge1$ the right side is at least
$(n+3c-4-2\kappa M(A)-4\kappa)/4\ge(n-1-2\kappa(M(A)+2))/4$. $\square$

The argument uses only the classes met from the two extreme anchors, so the
same count holds with $2\kappa M(A)$ replaced by the number of off-middle
points whose anchor class is $S$-split, for any one $S$.
