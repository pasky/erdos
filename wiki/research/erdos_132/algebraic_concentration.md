---
name: research/erdos_132/algebraic_concentration
title: A positive collinear or bounded-degree algebraic fraction forces rarity
desc: |
  A translated-hyperbola argument gives linear rarity from a positive
  collinear fraction, completing the bounded-degree algebraic-curve criterion.
sources: []
research_state: closed
created: 2026-09-22T23:15:00Z
updated: 2026-09-24T22:12:56Z
---


# A positive collinear or bounded-degree algebraic fraction forces rarity

***

These results do not resolve either unrestricted assertion of
[Problem 132](../../problems/distance_problems/E0132/_index.md). All multiplicities
count unordered pairs. Write $q(A)$ for the number of distinct positive
distances.

## A positive fraction on one line

**Theorem.** Fix $0<c\le1$. For all sufficiently large $n$, if an
$n$-point planar set $A$ has at least $cn$ points on one line, then

$$R(A)\ge\left\lfloor c^2n/64\right\rfloor.$$

The proof first shows that $q(A)\le n$ forces $A$ onto fewer than
$8/c$ parallel lines. This is a line version of the existing
[circle-incidence argument](circle_incidence.md).

### Uniform hyperbola overlap

Let $U,V$ be translates of an $m$-element real set $B$, and put
$d=|B-B|$. For any $h\ne0$,

$$
E:=\#\{(x,y)\in U\times V:y^2-x^2=h\}
\le C\left(\frac{d^{4/3}}{m^{2/3}}+\frac{d^2}{m^2}+1\right). \tag{1}
$$

For each $(u,v)\in U\times V$, use the curve

$$\Gamma_{u,v}:\quad (Y+v)^2-(X+u)^2=h.$$

The curves are irreducible conics, and their linear coefficients
determine their translation parameters. Two distinct curves meet in
at most two points: their equations subtract to a nonzero line,
which cannot be a component of a nondegenerate hyperbola. Dually,
the parameter equations for curves through two distinct points are
two distinct translates of the same hyperbola, so at most two curves
pass through two points.

The two-degrees-of-freedom crossing-lemma argument therefore gives

$$I(P,\Gamma)\le C\bigl(|P|^{2/3}|\Gamma|^{2/3}+|P|+|\Gamma|\bigr),$$

with an absolute constant, uniform in $h\ne0$. One can use the
elementary proof in [circle_incidence](circle_incidence.md): here
each curve has just two simple branches, pairwise intersections
and edge multiplicities are at most two, and there are no singular
or coincident components.

Take $P=(B-B)\times(B-B)$ and the $m^2$ displayed curves. Each
solution $(x,y)$ counted by $E$, and each parameter pair $(u,v)$,
give the incidence $(x-u,y-v)\in\Gamma_{u,v}$. These $Em^2$
incidences are distinct. Substituting $|P|=d^2$, $|\Gamma|=m^2$
and dividing by $m^2$ proves (1).

### Pinned spectra and parallel lines

If $q(A)>n$, fewer than $n/2$ classes are rich by the pair budget,
and hence $R(A)>n/2$. Assume $q=q(A)\le n$.

Normalize the anchor line to the $x$-axis and let $B$ be its $m\ge cn$
point coordinates. Then

$$d=|B-B|\le2q+1\le3n.$$

For $p=(a,b)\in A$, set

$$S_p=\{(x-a)^2+b^2:x\in B\}.$$

This pinned squared-distance spectrum has at least $m/2$ elements
and is contained in the global squared-distance set with zero
adjoined, of cardinality $q+1$.

If $p'=(a',b')$ and $|b|\ne|b'|$, a common value satisfies

$$ (y-a')^2-(x-a)^2=b^2-b'^2\ne0.$$

Apply (1) to $U=B-a$, $V=B-a'$. It follows that

$$|S_p\cap S_{p'}|=O_c(n^{2/3}). \tag{2}$$

Suppose $L=\lceil4/c\rceil$ distinct absolute heights occur.
Choose one point at each height. Inclusion-exclusion and (2) give

$$
q+1\ge\left|\bigcup_{j=1}^L S_{p_j}\right|
\ge Lm/2-O_c(n^{2/3})
\ge2n-O_c(n^{2/3}),
$$

contradicting $q+1\le n+1$ for sufficiently large $n$.
Thus fewer than $L$ absolute heights occur. Since height zero
occurs, all points lie on at most $k\le2L-3<8/c$ parallel lines.
The proved [parallel-line rank bound](line_covers.md) gives

$$R(A)\ge\lfloor n/k^2\rfloor\ge\lfloor c^2n/64\rfloor.$$

This includes $k=1$, for which every distance is rare and at least
$n-1$ occur. The height-zero degeneracy in (2) is not used: each
absolute height contributes at most two covering lines.

## A positive fraction on a bounded-degree curve

**Corollary.** Fix $c>0$ and an integer $d\ge1$. If a real algebraic
curve of degree at most $d$ contains at least $cn$ points of $A$,
then

$$R(A)=\Omega_{c,d}(n). \tag{3}$$

Factor a defining polynomial over $\mathbb R$. There are at most
$d$ nonconstant irreducible factors, so one component contains
at least $cn/d$ points. For a line component use the theorem above;
for a circle use [circle_incidence](circle_incidence.md).
For any other component, Theorem 1.1 of Pach--de Zeeuw gives
$q(A)\ge c_d(cn/d)^{4/3}$. Since there are fewer than $n/2$ rich
classes, this implies (3), in fact a superlinear lower bound in
this last case.

The exact source input is J. Pach and F. de Zeeuw, *Distinct
distances on algebraic curves in the plane*, Theorem 1.1,
[arXiv:1308.0177v4, PDF p. 2](https://arxiv.org/pdf/1308.0177).
Its statement was checked in the full paper: the constant depends
only on the degree, and the excluded components are lines and circles.
Thus the curve may vary with $n$ while its degree stays bounded.

In particular, a bounded-rarity sequence has $o(n)$ points on every
fixed-degree algebraic curve, uniformly over curves of that degree.
The existing layer reduction still puts a positive fraction of its
points in finitely many outer convex layers. No argument here forces
one of those layers onto a bounded-degree curve.

## Checks

The author checked the hyperbola degeneracies, incidence replication,
inclusion-exclusion, and unordered-pair rank bound; the argument is
author-recorded. Neither this criterion nor the curve
theorem supplies the missing unrestricted structure theorem.
