---
name: research/erdos_774/lemmas/fixed_base_defect
title: Exact eventual defect for a fixed simplex base
desc: The largest dissociated subset of B tensor S_p eventually has size p times r(B) minus one fixed integer; the changing-base coloring gap remains.
tags: [E0774, proved, tensor]
sources: []
created: 2026-09-18T16:44:29Z
updated: 2026-09-18T16:49:38Z
---


# Exact eventual defect for a fixed simplex base

***

## Theorem

Let $B$ be a finite nonempty set of nonzero rational vectors, and let
$a=r_{\rm diss}(B)$. There is an integer $d(B)$, with
$1\leq d(B)\leq a$, such that
$$
r_{\rm diss}(B\otimes S_p)=pa-d(B)
\quad\text{for every integer }p\geq(3^a+1)/2.
\tag{1}
$$
If $a\geq2$, then $d(B)\geq2$. Indexed simplexes of size two
are allowed when $a=1$; the application to odd prime factors uses $p\geq3$.

This is an exact fixed-base result, not a bound on the chromatic number of
the changing bases in [the main argument](../proof_sketch.md).

## Proof

Use the [signed-span layer criterion](../routes/tensor_coloring.md), and define
$$
d(B)=\min\left\{\sum_{i=1}^t(a-|C_i|):
t\geq1,\ C_i\subseteq B\text{ dissociated},\
\bigcap_{i=1}^t\Sigma(C_i)=\{0\}\right\}.
\tag{2}
$$
All costs are nonnegative integers; a single empty slice has cost $a$,
so the minimum exists and is at most $a$.

Choose a minimizing family and retain its first slice $C_1$. For each
pair $\{u,-u\}$ of nonzero elements of $\Sigma(C_1)$, retain
one slice whose signed span excludes $u$; it also excludes $-u$.
The retained intersection is still zero. There are at most
$$
1+\frac{|\Sigma(C_1)|-1}{2}\leq\frac{3^a+1}{2}
$$
retained slices. Discarding other slices cannot increase the cost, and the
definition of $d(B)$ prevents it from decreasing. Pad with maximum
dissociated subsets to obtain exactly $p$ slices. Each added slice has
zero cost and leaves the intersection zero. The layer criterion gives a
dissociated set of size $pa-d(B)$. Conversely, the slices of any
dissociated subset of $B\otimes S_p$ are an admissible family in
(2), proving the upper bound and (1).

Every maximum dissociated subset $C$ satisfies $B\subseteq\Sigma(C)$.
Indeed, adjoining $b\in B\setminus C$ produces a ternary relation,
necessarily with nonzero coefficient on $b$. Thus a zero-cost family
cannot have zero intersection, proving $d(B)\geq1$. A cost-one
family has just one deficient slice of size $a-1$, with all others
maximum. If $a\geq2$, any point of that deficient slice is a nonzero
element of every signed span. This excludes cost one.

## Source check and exact scope

After its digest, the reading copy of
[Ramsey–Graham, *Permutation and extension for planar quasi-independent subsets of the roots of unity*](../../../../library/analysis/ramsey_graham_2006_permutation_extension_planar_quasi_independent_subsets_roots_unity/_index.md),
the source this section compares against, was checked at Theorems 1.2.2 and
4.1.1 and the latter's proof. For odd squarefree $m$,
Theorem 1.2.2 gives, for primes $q>p$ with $p,q\nmid m$,
$$
\Psi(qm)\geq\Psi(pm)+(q-p)\Psi(m).
$$
Thus $p\Psi(m)-\Psi(pm)$ is already a nonincreasing nonnegative
integer and eventually stabilizes. The elementary proof above supplies an
explicit threshold and variational formula for its limiting value, and also
applies to nonprime simplex sizes.

The proof of the source's extension theorem uses only dissociation of each
new layer, although its statement asks for maximum-size new layers. Applied
color by color, or directly by the layer criterion, it shows
$$
\chi(B\otimes S_q)\leq\chi(B\otimes S_p)\qquad(q\geq p\geq3).
$$
Keep the old layers and add arbitrary properly colored base layers. Existing
signed-span intersections stay zero. This is replacement of a factor of a
**fixed** base; it is not monotonicity under adjoining a new prime factor.

Neither $d(B)$ nor the threshold in (1) is uniform as $B$ grows.
The theorem supplies no fixed coefficient height with infinite coloring
number. Its proof received an independent internal check; no computation or
external review is claimed.
