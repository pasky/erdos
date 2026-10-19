---
name: research/erdos_864
title: The one-exception Sidon problem
desc: "Current bounds, reductions, and construction routes for the one-exception Sidon problem."
tags: []
sources: []
created: 2026-09-23T01:53:50Z
updated: 2026-10-19T04:19:07Z
---

# The one-exception Sidon problem

[[research/_index|..]]

[[research/erdos_864/core_completion|core_completion]]: Reflection completion, outer-sector symmetrization, the marked-Sidon formulation of one-sided outsiders, and residue-fiber bounds for unary obstructions.

[[research/erdos_864/established_bounds|established_bounds]]: Leading bounds, a vector-kernel refinement of the upper secondary term, difference structure, and Fourier stability; the target remains unresolved.

[[research/erdos_864/obstructions|obstructions]]: Explicit failed reductions and algebraic construction obstructions; none is a counterexample to the target.

[[research/erdos_864/second_order_construction|second_order_construction]]: An endpoint-compression construction giving a positive N-to-the-one-quarter term above the reflected lower bound along an unbounded sequence.

[[research/erdos_864/source_notes/_index|source_notes/]]: Paper summaries and source comparisons used in the research on Problem 864.

[[research/erdos_864/symmetric_reformulations|symmetric_reformulations]]: Positive-half characterization, modular constructions, and the relation to four-independent sets and Lee packings.

***

This folder's notes that cite no source are author-recorded research, not
claims.

Only the notes linked on this page are retained here; the notes and
computations named without links below are not part of this repository, so
their results are recorded here without proofs.

Let $M(N)$ be the largest size of $A\subseteq\{1,\ldots,N\}$ for
which at most one integer has two or more unordered representations
$a+b$, including diagonal pairs. The target is

$$
 M(N)\le\left(\frac2{\sqrt3}+o(1)\right)\sqrt N.
$$

The bounds proved here remain

$$
 \left(\frac2{\sqrt3}+o(1)\right)\sqrt N
 \le M(N)
 \le\sqrt{2N}+O(N^{1/4}).
$$

Conditional on the feasible kernel certificate asserted in Lemma 4.1 of
Hou--Zhao (arXiv:2607.01169v3), which is not checked here, the upper bound
sharpens to $\sqrt{2N}+2^{1/4}\gamma_0N^{1/4}+O(1)$ with
$\gamma_0=0.9434925907\ldots$, as the
[established bounds](established_bounds.md) derive. The leading constant is
undetermined.

The best upper bound that follows from published results is
$(1.863\ldots+o(1))\sqrt N$, from Pikhurko's theorem on quasi-Sidon sets, as
the [established bounds](established_bounds.md) page shows.

## Main reading path

1. [Established bounds](established_bounds.md) contains the reflected
   construction and the difference-reflection argument for the upper bound.
   [Endpoint compression](second_order_construction.md) improves the lower
   bound by a positive multiple of $N^{1/4}$ along an unbounded sequence.
2. [Symmetric reformulations](symmetric_reformulations.md) identifies the
   central subproblem: for ordinary Sidon $B\subset[1,L]$ satisfying
   $B\cap3B=\varnothing$, prove $|B|^2\le(2/3+o(1))L$.
   The same page explains cyclic constructions and the Lee-packing connection.
3. [Core completion](core_completion.md) treats asymmetry. Reflection closure
   has a four-term criterion; a lossless reduction is available when that
   criterion holds. Outer-sector symmetrization loses only outsiders in the
   central third of a centered enclosing interval. When all outsiders have
   one sign, the problem becomes the marked-Sidon condition

   $$
   B\subset E,\qquad E\text{ Sidon},\qquad E\cap(E+E+B)=\varnothing,
   $$

   with objective $|E|+|B|$ and span $\max E+\max B$.
4. [Obstructions](obstructions.md) records the scope of the principal
   reductions. In particular, ordinary Sidon estimates do not bound the
   enlarged class, and a fixed continuum or fourth-moment model does not
   retain all of the required arithmetic compatibility.

## Construction mechanisms

### Elliptic toric quotients

Elliptic toric quotients give explicit
candidates in cyclic groups of order approximately $p^2/m$. A rational
point $T$ of order $m$ supplies a function with divisor $m(T)-m(O)$;
its values and elliptic point sums determine the quotient pair collisions.
The order-four and order-six Tate families have explicit functions and
chord identities. For order six, a thinning larger than

$$
 \left(\frac{2}{\sqrt{18}}+\varepsilon\right)p
$$

would improve the target. The remaining task is a sufficiently large
selection avoiding the competing chord pairs. A half-selection defined
by an elliptic group character cannot supply it; nonhomomorphic character
filters are a more specific possibility.

### Twisted Frobenius and complementary pair supports

Twisted Frobenius constructions develop the growing-exponent Sidon-space
candidate beyond the exponent-three thinning theorem.
For $q=3^{2h+1}$ and $\tau=3^{h+1}$, the identity $\tau^2(x)=x^3$
turns the collision equations into a bounded-degree surface with a
nonstandard Frobenius condition. The remaining algebraic issue is the
behavior of its quadratic covers and their rational fixed points.
A characteristic-two complementary-support criterion is also formulated
by an explicit trace equation.

### Integer carries and Frobenius orbits

Integer carry lifts distinguish integer
uniqueness from uniqueness modulo a doubled group. The modular six-point
obstruction permits the integer defect pattern $(1,1,2)$.
For trace-zero Singer sets, all modular zero triples are Frobenius orbits.
There are three lift choices making each full orbit sum to zero in the
integers; a correlated choice admits a uniform positive-magnitude profile.
The four-term relations between different orbits still have to be controlled.

Asymmetric endpoint compression permits
retaining one sign of a generator. A linear triple-system model saves deletions,
but a square-root-density integer realization is missing.
Order-two centers,
binary phase lifts, and the
Singer profile inequalities give
complementary criteria for these lift constructions.

## Global upper-bound mechanisms

The triple-center matrices have the common
rank-one generating identity

$$
 \sum_x H_xz^x=F(z)v(z)v(z)^{\mathsf T}.
$$

Their individual spectra and fixed limiting moments do not force the
desired constant. Mixed center moments
retain operator correlations between different centers.

The
nonbacktracking formulation
retains cycles of every length at once. For each triple-block graph, its
antisymmetric nonbacktracking fixed space has dimension

$$
 \dim\mathcal C_x=E_x-V_x+c_x.
$$

A useful new estimate would control these dimensions jointly through the
translated kernels and integer span. Separate local bounds, or bounds
for every fixed cycle length, do not give this aggregate estimate.
The clique-hypergraph formulation
provides a second global encoding, with zero-centroid blocks and
restricted short cycles.

## Supporting results and other construction criteria

Three-fiber completion excludes nonempty
outsider completions of the specified Bose, characteristic-three Singer,
and Ruzsa reflected cores: they have at most
$23q/12+O(q^{3/4})$ points, below the reflected $2q$.
Geometrically separated copies obey the
proposed bound. These hypotheses do not hold for arbitrary interval sets.

The index-five norm torus,
elliptic hexagonal candidates, and
graph Bose encodings retain explicit collision
criteria for other constructions. Their supporting algebraic arguments, the
Eisenstein and Lee formulations, finite certificates, earlier models and
bounded computational tests are not part of this repository; the tests were
not asymptotic constructions or upper bounds.
