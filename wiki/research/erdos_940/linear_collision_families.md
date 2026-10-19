---
name: research/erdos_940/linear_collision_families
title: Rank bounds for linear collision identities
desc: Nontrivial positive linear identities have fewer than r parameters, with a stronger bound when nonproportional terms survive.
tags: []
sources: []
created: 2026-09-22T03:46:38Z
updated: 2026-10-13T05:28:09Z
---


# Rank bounds for linear collision identities

***

## Status and scope

The theorem and its counting consequences below are proved and author-recorded.
They concern attempts to force gaps by removing redundant representations
through explicit linear identities. They do not bound all collisions, prove
positive density, or produce missing integers for $r\ge5$.

## The rank theorem

**Theorem.** Let $r\ge3$, let $a_i,b_i$ be positive rational numbers, and
suppose rational linear forms satisfy


$$
\sum_{i=1}^r a_iL_i(\mathbf t)^r
=\sum_{j=1}^r b_jM_j(\mathbf t)^r.
\tag{1}
$$


Assume there is a real parameter point at which all $2r$ linear forms are
positive. Unless the summands in (1) match pairwise as polynomial functions, the
combined linear forms span at most $r-1$ dimensions.

If combining all proportional forms leaves a nonzero relation, the stronger
bound is


$$
\operatorname{rank}\{L_i,M_j\}\le\left\lfloor\frac r2\right\rfloor+1.
\tag{2}
$$


### A separating-polynomial lemma

Let $T$ be a noncollinear set of at most $2r+1$ projective points over
$\mathbb Q$. There is a point $P\in T$ and a degree-$r$ homogeneous polynomial
vanishing at $T\setminus\{P\}$ but not at $P$.

At most one line can contain $r+2$ points of $T$, since two such lines would
have a union of at least $2r+3$ points. If such a line exists, choose $P$
outside it; otherwise choose any $P$. Each line through $P$ then contains at
most $r$ other points of $T$.

Group the other points by their lines through $P$, list each group
consecutively, and pad the list with dummy entries to length $2r$. Pair
positions $i$ and $i+r$ for $1\le i\le r$, then discard dummy entries. No pair
of genuine points belongs to the same group, since a group has length at most
$r$. For each pair choose a hyperplane through the two points but not through
$P$; for a singleton choose a hyperplane through it but not through $P$. Their
product vanishes at all other points and not at $P$. If its degree is less than
$r$, multiply by a suitable power of a linear form nonzero at $P$.

It follows that a relation among at most $2r+1$ distinct $r$th powers of linear
forms, all with nonzero coefficients, must have collinear projective support.
Apply the separating polynomial as a constant-coefficient differential operator
to the relation. Its value on the $r$th power of a linear form is $r!$ times its
evaluation at the coefficient vector; this would leave exactly one nonzero term.

### Proof of the theorem

Combine proportional forms in (1), choosing a common representative in each
class that is positive at the given parameter point. Every proportionality
factor is then positive. Consequently every canceled class contains at least
one original summand from each side and consumes at least two original forms.

Suppose a residual relation survives. Its projective support has at most $2r$
points, so the separating lemma puts these points on a line: the surviving forms
span two dimensions. There must be at least $r+2$ surviving classes. Indeed,
choose binary coordinates making all the projective points finite and expand
$(u+\alpha_i v)^r$; any at most $r+1$ of these powers are linearly independent
by the Vandermonde determinant.

If $c\ge r+2$ classes survive and $k$ classes cancel, then $c+2k\le2r$. The full
span has dimension at most $2+k$, proving (2).

If no residual survives, there are at most $r$ proportional classes. With
exactly $r$ classes, every class has exactly one original term from each side,
and the terms match pairwise. Otherwise there are at most $r-1$ classes and
hence rank at most $r-1$. This completes the proof.

## Uniform counting consequences

An $m$-dimensional linear subspace of $\mathbb R^{2r}$ contains at most
$(2B+1)^m$ integer points in $[-B,B]^{2r}$. Choose $m$ coordinate functions
whose restrictions form a basis of the dual of the subspace; their coordinate
projection is injective. The estimate is independent of the height of the
subspace.

For positive integral coefficients and target value at most $X=B^r$, every root
coordinate is at most $B$. Thus any one non-pairwise-matching family (1)
contributes $O_r(B^{r-1})$ collision pairs, uniformly in its coefficients and
linear parametrization. Any collection of $K(B)$ such families contributes at
most


$$
O_r(K(B)B^{r-1}).
\tag{3}
$$


If all the families have a nonzero residual after proportional terms are
combined, this improves to


$$
O_r\!\left(K(B)B^{\lfloor r/2\rfloor+1}\right).
\tag{4}
$$


In particular, fewer than order $B$ families cannot account for a positive
constant times $X=B^r$ collision pairs. For quintic families with a
nonproportional residual, (4) requires at least order $B^2$ families before
linear mass is possible. These are necessary thresholds, not sufficient
constructions; overlapping families can count the same pairs repeatedly.

The distinction between (3) and (4) matters. The positive quintic identity


$$
32u^5+32u^5+64v^5+w^5+z^5
=64u^5+32v^5+32v^5+w^5+z^5
$$


has rank four but every proportional class cancels. It is a split-and-merge
identity, so it does not contradict the rank-three bound for a surviving
nonproportional quintic relation.

No growing collection of families was constructed whose union has linear mass,
much less enough redundancy to force unrepresented targets. The theorem rules
out a fixed finite identity list as such a mechanism, and quantifies the growth
needed to revisit it.

For the cubic logarithmic-multiplicity problem, the subsequent
[input-plane estimate](primitive_cubic_fibers.md) removes all projected
planes of height at most $N^{1/2-\eta}$ with an $o(N^3)$ entropy contribution.
This does not control the generic higher-height planes or nonlinear
collision geometry.
