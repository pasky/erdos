---
name: research/erdos_132/variational_reduction
title: A compact extremal reduction for a hypothetical counterexample
desc: |
  A minimal-distance-class counterexample would have a max-min realization
  without collisions or class mergers. The remaining equilibrium-stress
  obstruction is the absence of edgewise signs and possible abnormal multipliers.
sources: []
research_state: closed
created: 2026-09-22T21:50:03Z
updated: 2026-10-13T05:28:09Z
---


# A compact extremal reduction for a hypothetical counterexample

***

This is a conditional reduction for the first assertion of
[Problem 132](../../problems/distance_problems/E0132/_index.md), not a contradiction or
a construction.

## Equality-preserving mergers do not increase rarity

If an $n$-point realization preserves every original equality of pair
distances, its new distance partition is a coarsening of the old one.
A new rare class cannot contain an old rich class, because that old
class already has more than $n$ pairs. Different new rare classes
contain disjoint collections of old rare classes. Consequently

$$R(\text{new realization})\le R(\text{old realization}),$$

provided the new points remain distinct. This observation permits
mergers, but not splits. Arbitrary perturbation does not satisfy it.

The [affine-deformation criterion](affine_deformations.md), checked from
the independent input, identifies one family in which this restriction
is useful: a nonsimilarity affine map preserving every original equality
forces $R(A)\ge\lceil n/4\rceil$. Such a map exists exactly when the
equal-length difference constraints span at most one dimension of the
traceless symmetric $2\times2$ matrices. Equilateral triangles and
squares already prevent it. This supplies no general deformation or
sign-controlled stress for the reduction below.

## Maximizing the minimum distance

Assume an $n\ge5$ counterexample with $R=1$ exists. For this fixed $n$,
choose one with the fewest distinct distances, say $q$. Label its
pair classes $E_1,\ldots,E_q$ by increasing length. Each $E_k$ for
$k<q$ is rich, while $E_q$ is its sole rare class, the diameter.

Consider all realizations with variables $p_1,\ldots,p_n\in\mathbb R^2$
and squared lengths $t_1,\ldots,t_q$, subject to

$$p_1=0,\qquad |p_i-p_j|^2=t_k\quad(ij\in E_k),
\qquad0\le t_1\le\cdots\le t_q=1.$$

This is a nonempty compact set. All variables $t_k$ lie in $[0,1]$,
every $p_i$ lies in the closed unit disk about $p_1$, and all the
constraints are closed. Maximize $t_1$ on it. The maximum is positive,
because the original configuration after similarity normalization is
feasible. Thus no two points coincide at an optimizer.

No two nondiameter classes can merge there: the merged class remains
rich, and the result would still have $R=1$ but fewer than $q$
distinct distances. Nor can a rich class merge with $E_q$, since that
would give more than $n$ pairs at the diameter. Therefore the optimizer
still satisfies

$$0<t_1<\cdots<t_q=1.$$

A hypothetical counterexample can thus be taken to maximize its
minimum distance over its labeled equality pattern, without any
collision or merger obstruction.

## What the multiplier equations do and do not give

There is an explicit obstruction to extracting a real equilibrium stress
from a single rich class, even when that graph is connected and every
vertex is active. With $\omega=e^{i\pi/3}$, the five points


$$
\{0,1,\omega,-1,-\omega\}
$$


have six unit pairs: two equilateral triangles sharing only the origin.
Each noncentral vertex has two nonparallel incident unit edges. Its
equilibrium equation forces both incident stress coefficients to vanish,
so the whole unit framework has only the zero real stress. Thus
$m_A(1)=6>5$ is not a stress-existence criterion. The example is not a
counterexample to Problem 132: its other squared-distance multiplicities
are $3:2$ and $4:2$.

At this optimizer, the order inequalities are locally inactive. A
multiplier alternative for the equality constraints gives edge weights
$\omega_{ij}$ and $\lambda\ge0$, not all zero, with

$$\sum_{j\ne i}\omega_{ij}(p_i-p_j)=0,$$

$$\sum_{ij\in E_1}\omega_{ij}=\lambda,\qquad
  \sum_{ij\in E_k}\omega_{ij}=0\quad(1<k<q). \tag{1}$$

For completeness, use constraints $t_k-|p_i-p_j|^2=0$ and minimize
$-t_1$. If their gradients are linearly dependent, a nonzero dependence
gives these equations with $\lambda=0$. If they are independent, the
implicit-function theorem and stationarity on the equality manifold
give the ordinary multiplier equations with $\lambda=1$. The missing
equilibrium equation at fixed $p_1$ follows from cancellation of the
other edge forces.

Dotting equilibrium with the positions and summing gives
$\sum_{i<j}\omega_{ij}|p_i-p_j|^2=0$. Since $t_q=1$, (1) implies

$$\sum_{ij\in E_q}\omega_{ij}=-\lambda t_1.$$

These are class-total identities, not edgewise sign conditions.
They do not imply that any particular distance graph has a positive
or negative stress. The constraint system may also be redundant,
yielding only an abnormal multiplier with $\lambda=0$. No useful
normality or sign conclusion was obtained from $|E_k|>n$.

The reduction removes two technical difficulties of an extremal
realization argument. The remaining stress-sign issue is substantive;
the reduction alone proves neither requested assertion. Exploring
that issue is only a provisional direction, not an established next
step toward a solution.
