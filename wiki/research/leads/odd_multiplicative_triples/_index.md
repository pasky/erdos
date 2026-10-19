---
name: research/leads/odd_multiplicative_triples
title: Three consecutive ones for odd-order multiplicative functions
desc: |
  Toward the odd-k triple question of Problem 436: an exact realization
  bridge, a sieve proof for weakly pretentious functions, and an unresolved
  relative three-point correlation estimate with scoped statistical models.
problems:
- 436
research_state: ready
review_status: unreviewed
created: 2026-10-16T15:00:01Z
updated: 2026-10-17T04:21:01Z
---

# Three consecutive ones for odd-order multiplicative functions

[[research/leads/_index|..]]

[[research/leads/odd_multiplicative_triples/proof_sketch|proof_sketch]]: An end-to-end sketch for the odd-k triple question: realization and sieve
arguments, the unresolved aggregate cofactor estimate, scoped tests of
statistical and finite-sums mechanisms, and a conditional spectral route
for every odd order using an explicit quotient by the bounded-distance core.

***

This lead's results that are not drawn from a cited source are Plasma AI's,
credited to Plasma AI.

## Target

The target is the second question of
[[problems/integer_sequences/E0436/_index|Problem 436]]: whether
$\Lambda(k,3)$ is finite for every odd $k$. The lead works with the equivalent
statement T(k): every completely multiplicative function from the positive
integers into the $k$th roots of unity takes the value $1$ at three
consecutive integers. The problem's growth question is outside this lead. The
problem page records the status search and the accepted partial results: the
pair theorem of Hildebrand and the value $\Lambda(3,3)=23532$.

## Standing

The [canonical proof sketch](proof_sketch.md) is author-recorded and
unreviewed. No claim card has been made and the full target is unresolved.
Its supported parts are:

- $\Lambda(k,3)=\sup_fN(f)$ for odd $k$, where $N(f)$ is the first start of
  three consecutive ones. The argument proves independence of the prescribed
  prime values, applies Chebotarev, and uses compactness to pass from
  existence for each function to a bound for each fixed $k$.
- Every $\mu_3$-valued completely multiplicative function has
  $N(f)\le23532$, from the accepted cubic result and the realization bridge.
- If $f$ weakly pretends to a Dirichlet character, its triples of ones have
  positive upper natural and logarithmic densities. Section 4 derives the
  needed multiform probability approximation from the fundamental sieve
  lemma, with its summed errors. Bounded pretentious distance gives positive
  lower densities.
- Product-based logarithmic correlation cancellation reduces the other
  cases to monochromatic triples, with a relative condition for composite
  $k$. The cited correlation theorem is used at the statement standing of its
  quotation in the held source; its primary proof was not read.
- The three-point logarithmically averaged Elliott conjecture would imply
  the full assertion for every odd $k$. The exact aggregate estimate needed
  by that conditional argument is stated in Section 10.
- The spectral hypothesis (QSP) in Section 12 would also imply the full
  assertion for every odd $k$. It concerns an explicit quotient of $f$ by a
  pointwise root of its bounded-distance core. This quotient need not be
  multiplicative, but it is invariant under multiplication by $k$th powers.
  If one of its logarithmic Furstenberg systems has no nonzero rational
  eigenvalue, polynomial recurrence transfers to consecutive triples and
  composes with the core's positive lower density on the same scales. The
  spectral assertion is unproved. A simpler multiplicative factorization
  covers squarefree orders conditionally on (SP); its required Dirichlet
  root can fail, as an order-nine example shows.

The remaining gap is positive mass for the relative diagonal of three
consecutive values. Pairwise uniformity does not fill it. A digit-twisted
stationary process with odd $k\ge7$ satisfies all the specific rotation,
pair, dilation and correlation-isotypy identities tested in the sketch but
has no monochromatic consecutive triple. This limits those identities, and
is not a counterexample multiplicative function. Its colour process has the
rational eigenvalue $1/3$. Section 12 shows that a process with a Haar
position and the conditional self-similarity identities can avoid
monochromatic consecutive triples only if its colour process has a nonzero
rational eigenvalue. For $k=5$, the sketch proves
that an independent linear-phase construction with arc colours cannot have
this behavior if it obeys the conditional identities at $2$ and $5$; more
general processes remain outside that argument.

The cofactor route remains open (sketch Section 11). Its exact weighted
aggregate has a total-variation error summed over all characters, and its
common-scale cancellation would compose with the positive bounded-distance
core on the same selected population. Independence of the cofactor term
from the entire small-prime vector is a stronger sufficient assertion, not
the required estimate. The digit-twisted process defeats deductions from
the label law and listed stationary identities alone; its formal cofactors
are not values of one multiplicative function.

Other proposed mechanisms have narrower obstructions. Every polynomial family
of consecutive values given by products of affine forms, in any number of
parameters, depends on one affine form and so is a local pattern; the
digit-twisted process gives probability zero, for odd $k\ge7$, to all families
with two factors per value, and for odd $k\ge9$ to all with three. Hildebrand's
special-set method for pairs cannot yield triples from first moments, since
one colour class of an even-order function avoids every scaled consecutive
triple in any finite set. The finite-sums strengthening of the pair theorem
also leaves a selection problem: explicitly constructed completely
multiplicative functions, both at bounded distance from $1$ and in Case C,
admit a homogeneous finite-sums sequence for which every normalized
predecessor has any prescribed nontrivial odd-order value (Proposition F).
These functions have a triple of ones elsewhere; the examples refute the
proposed universal reflection constraint, not an argument using a global
absence of triples.

## Next investigation

The quantitative analytic test is (AC) of Section 10, or the selected
population version (CF) of Section 11. A proof must control the actual joint
cofactor expectations in their weighted sum, with the summed error and one
common sequence of scales. No assertion of independence from every label is
needed. A one-sided estimate beating the negative of the positive core would
already suffice for existence; its threshold is stated in Section 11.

The qualitative alternative is (QSP) of Section 12, for the actual quotient
$u_f$ defined there. A proof of its spectral assertion would cover every odd
order without assuming a Dirichlet root of the core. The quotient has
uniform one-point marginals on residue classes, but this does not imply the
process independence used in transferring recurrence and combining it with
the core. The spectral input remains unproved. With trivial bounded-distance
subgroup, $u_f=f$ and the hypothesis specializes to (SP); a weaker condition
at one recurrence step can then suffice. The related spectral question for
the Liouville function remains open in the cited source.

The function equal to a fixed primitive $k$th root at every prime remains a
necessary test of any proposed full route: it requires three consecutive
integers whose numbers of prime factors, counted with multiplicity, are all
divisible by $k$, for every odd $k$. The finite-sums alternative would need a
method for selecting a favorable sequence, since arbitrary homogeneous
refinements can have nontrivial predecessor colours. Local Fourier uniformity
or additional polynomial identities are possible inputs, but no necessity
or sufficient arithmetic consequence of those proposed additions is proved
here. Further model tests alone would not settle the target.
