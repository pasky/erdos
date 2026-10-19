---
name: research/erdos_132/generic_cluster_replacement
title: Generic balanced cluster replacement increases rarity
desc: |
  Replacing each point by an arbitrary fixed b-point cluster gains a rare
  distance outside finitely many scale parameters, including all small scales.
sources: []
research_state: closed
created: 2026-09-23T04:40:00Z
updated: 2026-09-24T22:12:56Z
---


# Generic balanced cluster replacement increases rarity

***

This excludes a class of counterexample constructions; it does not resolve
either unrestricted assertion of
[Problem 132](../../problems/distance_problems/E0132/_index.md). All multiplicities
count unordered pairs.

## The replacement theorem

Let $P\subset\mathbb R^2$ have $N\ge2$ points. For each $p\in P$, fix
a $b$-point set $S_p\subset\mathbb R^2$, where the same integer $b\ge2$
is used at every point. Put

$$A_t=\bigcup_{p\in P}(p+tS_p).$$

Outside a finite set of positive parameters $t$, the union has $n=Nb$
distinct points and

$$R(A_t)\ge R(P)+1. \tag{1}$$

If every $S_p$ is congruent to one set $S$, then

$$R(A_t)\ge R(P)+R(S). \tag{2}$$

In particular these conclusions hold for all sufficiently small positive
$t$, with the threshold depending on the base and the fixed shapes.
The shapes may have arbitrary different orientations; (1) does not
require them to be congruent, centrally symmetric, or convex.

### Proof

For a pair of different base points, write $v=q-p\ne0$ and $d=u-s$,
where $u\in S_q$, $s\in S_p$. Its squared distance is the polynomial

$$F_{v,d}(t)=|v|^2+2t\,v\cdot d+t^2|d|^2. \tag{3}$$

Internal squared distances have the form $t^2|s-u|^2$. Exclude all
positive roots of nonzero differences between these finitely many
polynomials, and all parameters causing a collision of distinct labeled
points. This excludes only finitely many parameters. At every remaining
parameter, equality of distances is exactly polynomial identity.
In particular, the constant term separates different base-distance
groups, and separates every cross-cluster class from every internal class.

Fix a rare base distance $r$, with $m_P(r)\le N$. Its entire group
contains exactly

$$b^2m_P(r)\le b^2N=bn \tag{4}$$

unordered cross-cluster pairs. For one base pair of this length,
$|S_q-S_p|\ge2b-1$. To verify this elementary sumset bound, choose a
linear functional injective on both sets, order their images, and use
the increasing chain of $2b-1$ sums obtained by first varying one
summand and then the other.

A fixed polynomial (3) prescribes both $v\cdot d$ and $|d|^2$.
A line intersects a circle in at most two points, so this single base
pair already produces at least $\lceil(2b-1)/2\rceil=b$ polynomial
classes. By (4), not all classes in its base-distance group can have
more than $n$ pairs. Thus each rare base distance supplies a distinct,
globally rare distance of $A_t$.

Finally let $D_* =\max_p\operatorname{diam}(S_p)>0$. Only clusters
attaining that diameter contribute internal pairs at distance $tD_*$.
The planar diameter bound gives at most $b$ pairs in each such cluster,
and hence at most $Nb=n$ in total. This class supplies the extra one
in (1). If all shapes are congruent, each rare distance $r$ of $S$
instead supplies an internal class with exactly $N m_S(r)\le Nb$
pairs, proving (2). This also permits reflections of the shapes.

## Consequence and exact limitation

A finite hierarchy assembled through balanced replacements at sufficiently
small scales gains at least one rare distance at each nontrivial stage.
This includes branch-dependent, nonstationary rhombus replacements,
without a common iterated-similarity system. It extends the mechanisms
excluded in [full_similarity_orbits](full_similarity_orbits.md), but
under a different, parameter-generic hypothesis.

To defeat this argument at a stage, a construction must choose an
exceptional parameter: two nonidentical squared-distance polynomials
must coincide, or labels must collide. Each such parameter satisfies
a polynomial of degree at most two over the coordinate field.

The excluded set depends on the base and on all shapes. Its smallest
positive element need not have a uniform lower bound as these vary.
Consequently large diameter-to-minimum-distance ratio alone does not
allow (1) to be applied to an arbitrary configuration. No reduction of
all planar sets to these generic hierarchies has been established.

The later [nonlinear collision theorem](nonlinear_cluster_limits.md)
removes the generic-parameter assumption for analytic balanced doubling
and tripling ($b=2,3$), even with varying branch shapes. The analogous
statement for arbitrary fixed $b$ remains unproved.

The author checked the unordered-pair budget, the sumset and line--circle
counts, and the treatment of exceptional parameters and congruent shapes; the
argument is author-recorded. No computation or external structural theorem
enters the proof beyond the classical planar diameter bound.
