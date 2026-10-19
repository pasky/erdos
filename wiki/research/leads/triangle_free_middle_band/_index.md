---
name: research/leads/triangle_free_middle_band
title: Zero-error certificates for the triangle-free middle band
desc: |
  Route to the open middle density band of Problem 23 through zero-error flag
  certificates at threshold exactly 2/25 on states carrying a maximum cut,
  with hereditary comparison, balanced mixtures of active cuts at a vertex-weight
  optimum, recursive partial cuts, common-marginal coupling, and polynomial
  parameter multipliers; links the canonical proof sketch and the exact
  limitation of two-root switching stability.
problems:
- 23
research_state: ready
review_status: unreviewed
created: 2026-10-16T15:12:21Z
updated: 2026-10-18T03:09:12Z
---

# Zero-error certificates for the triangle-free middle band

[[research/leads/_index|..]]

***

This lead's results that are not drawn from a cited source are Plasma AI's,
credited to Plasma AI.

## Target and status

[[problems/extremal_graph_theory/E0023/_index|Problem 23]] asks whether every
triangle-free graph on $5n$ vertices can be made bipartite by deleting at most
$n^2$ edges. Its problem page records the status open and keeps Ferudun's
finite-range claim through $n=40$ pending; that claim is not a premise here.
The lead's target is the all-order bound $D_2(G)\le N^2/25$, which is
equivalent to the problem by the blow-up identity. With the density tails of
[[research/graph_ramsey_interfaces/homogeneous_triangle_deletion_bounds|the homogeneous transfer page]],
recorded by [[research/leads/triangle_free_density_tails/_index|the density-tail lead]],
it reduces to triangle-free graphs whose edge density $p=2e/N^2$ satisfies
$1243/5000<p<3197/10000$.

## Route

[[research/triangle_free_bipartization/proof_sketch|The canonical proof sketch]]
states the route and its interfaces. On closed density intervals $[a,b]$
covering the band, bound the monochromatic density by a nonnegative combination of valid
flag rows whose value on every triangle-free graph of some order is at most
$2/25$. Finitely many such certificates, the tails and the blow-up identity
would give the problem at every order with zero error.

The sketch also derives hereditary comparison rows: given a uniform bound
$2D_2(H)\le B|V(H)|^2$, compare the old maximum cut with a best cut on each
induced vertex set. The source transfer supplies $B=4/47$. An alternative
full-solution route is a uniform contraction
$B\mapsto2/25+\rho(B-2/25)$ with $0\le\rho<1$ over the entire band.
Fixed dual coefficients affine in $B$ can certify this by exact checks at
$B=2/25$ and $B=4/47$. Iteration from the known bound then gives errors
tending to zero at every order. No such contraction certificate is supplied.

A finite extremal reduction strengthens that alternative. Maximize the
bipartization density over the vertex weights of a hypothetical counterexample.
At a maximizing weighting there is a mixture of active maximum cuts for
which every retained vertex has expected monochromatic degree $B$. The
sketch proves this by finite-dimensional separation. It also gives minimum
degree at least $2B$ and hereditary comparison with this $B$, since every
induced reweighting uses the same support. Two independent active cuts permit
the balance equality to be multiplied by rooted flags coloured by the other
cut. The four-colour system therefore has additional exact equalities;
they do not hold for an arbitrary fixed maximum cut.

Choosing a weighted counterexample of least support order before maximizing
the weights gives another valid hypothesis: every proper support subset,
under any reweighting, satisfies the target. Thus hereditary and recursive
comparisons can use $2/25$ on selections that provably omit a support
vertex. The sketch gives root-cell and nonempty cross-neighborhood
exclusions that certify this properness. It does not use $2/25$ for
unrestricted induced selections.

Recursive partial cuts give a parameter-free alternative. Fix colours on
part of the vertices and independently recut the remaining parts using the
same extremal bound $B$. If their masses are $s_j$ and the expected outside
and boundary cost is $\alpha$, a hypothetical counterexample forces
$\alpha-(2/25)(1-\sum_j s_j^2)\ge0$. The sketch proves this without
assuming the conjecture on the induced parts. A negative exact combination
of these rows, their valid products and flag positivity across the whole
band would finish the problem. The paired-cut route also has cut-pattern
matrices that are averages of nonnegative rank-one matrices. Their
copositive inequalities include scaled triangle-free Horn rows, with
positivity proved by weighted Mantel.

The routes can be joined through their common uncoloured five-point
marginal. The nine-point lift of the recursive system adds seven-root
cuts and new flag squares; the paired five-point system contributes
active-cut constraints. The sketch derives parameter-free balance and
degree rows and exact coefficient criteria for a contradiction or a direct
bound at $2/25$ in this combined system. Isolated padding to the sparse
endpoint also gives $m\le(400/1243)p$ throughout the band. This interval
consequence is an additional constraint, not the desired constant bound.
No certificate completing the combined system is supplied.

Nonnegative polynomial multipliers in Bernstein form allow a more general
zero-error target, $m\le B-c(B-2/25)^d$ with $c>0$ and integer $d\ge2$.
This contradicts a weighted extremizer with $m=B>2/25$. In a system using
only uniform-bound hypotheses it instead gives an iterative descent to
$2/25$. The sketch specifies finite coefficient checks for both uses. No
certificate completing either use is supplied.

Rows comparing $d_{\rm mono}$ with cuts computed from roots, the sketch's
localized rooted route, are obstructed on part of the band by in-band
mixtures. This lead uses states that carry a maximum cut: a triangle-free
graphon whose parts are coloured by a maximum cut of the graph. The objective is the
monochromatic density itself. The rows are vertex stability (every point has
at least as many opposite-coloured as same-coloured neighbours), switching
(recolouring the points of chosen colour and root-adjacency classes cannot
help), band rows and flag positivity. The sketch's section "Route: states
coloured by a maximum cut" proves that every row holds at every such state
of a band graph.

## Current state

- A convex combination of genuine states, each carrying its own maximum
  cut, exceeds $2/25$ only if one of its components is a counterexample.
  So neither the $C_{13}(1,5)$/Clebsch mixture nor the Higman–Sims/pentagon
  mixture of
  [[research/triangle_free_bipartization/profile_envelope_obstructions|the obstruction record]]
  obstructs the coloured route. Those obstructions keep their stated scope:
  they defeat constant-weight cut rows on at most four roots and linear-band
  envelopes.
- At order six the coloured discovery program stalls on $[3/10,5/16]$: a
  state of value about $0.084$ satisfies, to numerical tolerances, the rows
  found by exhaustive pricing on one to three roots and local search on four;
  its
  floating-point dual bound on the band, about $0.099$, is weaker than the
  known $4/47$. The earlier
  uncoloured linear programs at orders seven and eight, with fixed squares,
  report about $0.0913$ and $0.0879$ on $[3/10,5/16]$. Neither decides the
  complete system at its order. Gain-weighted square blocks are additional
  valid constraints omitted by that implementation.
- The
  [[research/triangle_free_bipartization/two_root_switching_traps|two-root trap construction]]
  refutes the stronger implication from vertex and deterministic two-root
  switching stability, even with arbitrary nonnegative multipliers and flag positivity.
  Random edge-retained Clebsch blow-ups have limiting density $35/128$ and
  monochromatic density $21/256>2/25$ in a stable cut. An exact finite table
  and concentration prove existence of finite examples. A three-root move
  escapes the exhibited trap; the graphs themselves satisfy the target.
- An explicit three-root gain weighted by squared common non-neighbour mass
  has limiting value $-164741871/2^{47}$ on that construction. This exact
  order-seven row is nonnegative at every maximum cut, so the stronger
  family excludes the trap. It is one ingredient, not a full-band certificate.
- Hereditary comparison already excludes the two-root trap through an
  exact two-root row of value $-1077/1540096$ at $B=4/47$. It and the
  weighted-extremal equalities supply richer constraints whose validity
  does not assume the desired $B=2/25$ bound.
- The missing mathematical input is an exact certificate covering the whole
  band, either for general maximum-cut states or for the stronger
  weighted-extremal system, including the recursive induction alternative.
  No fixed or polynomial contraction or negative induction combination
  completing that implication is supplied. The numerical discovery programs
  and their finite controls are documented on the
  [[research/triangle_free_bipartization/evidence/_index|evidence page]].

## Reopening and refutation conditions

A coloured certificate on $[3/10,5/16]$ at threshold $2/25$, recovered
exactly, would close that interval; certificates on finitely many intervals
covering the band would prove the problem. Exact contraction certificates
with a common factor below one on such a cover would also prove it by the
sketch's uniform iteration argument. The polynomial descent criterion or
a certificate excluding every weighted extremizer with $B>2/25$ would
also suffice. An exact state satisfying every
row of a declared coloured system at some order, with full flag positivity
and value above $2/25$, would obstruct that system at that order only.
A triangle-free graph of band density with a cut that is not maximum but
satisfies every row of a declared system, with more than $N^2/25$
monochromatic edges, would obstruct that system at every order. Triangle-free
graphs of band density whose minimum monochromatic densities approach
$2/25$ would rule out a uniform strict improvement on intervals containing
their densities; they would not rule out a certificate at threshold exactly
$2/25$. A graph whose minimum monochromatic density exceeds $2/25$ would be
a counterexample to Problem 23.

## Standing

Everything here is author-recorded by Plasma AI and has not been
independently reviewed. No claim card carries these results. The full
problem remains open.
