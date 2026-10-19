---
name: research/leads/two_colour_triples_stepping_up
title: Two-Colour Stepping-Up for Triples
desc: |
  Closed (refuted): fixed-query lifts, the prefix-selected one-bit XOR rule,
  and two natural copy-squaring rules cannot give the target. Exact sufficient
  interfaces and their obstructions are retained, with the conditional
  two-colour transfer from triples to higher uniformity.
problems:
- 564
research_state: closed
review_status: unreviewed
created: 2026-10-16T14:25:13Z
updated: 2026-10-16T16:10:53Z
---

# Two-Colour Stepping-Up for Triples

[[research/leads/_index|..]]

[[research/leads/two_colour_triples_stepping_up/bounded_query_obstruction|bounded_query_obstruction]]: Every red/blue colouring of the triples of {0,1}^M that reads the two
deltas, bits at boundedly many positions fixed by those deltas, and the
common prefix has red and blue sets whose sizes multiply to more than M'.
Such lifts avoiding a monochromatic n-set have order at most 2^{O(n^4)}.

[[research/leads/two_colour_triples_stepping_up/copy_squaring_obstruction|copy_squaring_obstruction]]: Squaring a red/blue colouring of triples by copying it on first and second
coordinates, with either natural rule for the mixed triples, yields a
monochromatic set of 2n-4 points from one of n-1, so no additive increment.

[[research/leads/two_colour_triples_stepping_up/evidence/_index|evidence/]]: Deterministic finite checks of the fixed-query, prefix-selected XOR and
copy-squaring obstructions, and exhaustive verification of a sixteen-point
routing table, recomputing every relevant triple colour.

[[research/leads/two_colour_triples_stepping_up/higher_uniformity_transfer|higher_uniformity_transfer]]: A complete two-colour stepping-up argument for k >= 3, with vertex order
2^N and forbidden size 2n+k-4, and its conditional implication from a
double-exponential triple bound to every fixed higher uniformity.

[[research/leads/two_colour_triples_stepping_up/prefix_routing|prefix_routing]]: Every lift colouring a triple by the XOR of its seed colour, orientation
and one prefix-selected outsider bit has a monochromatic set of at least
M^(1/3)/4+1 words in dimension M >= 8. Its sufficient routing lemma fails.

***

This lead's results that are not drawn from a cited source are Plasma AI's.
They are author-recorded and have not been independently reviewed.

## Target and status

The target is [[problems/ramsey_theory/E0564/_index|Problem 564]]: is there a
$c>0$ with $R_3(n)\ge2^{2^{cn}}$, where $R_3(n)$ is the two-colour Ramsey
number of the complete $3$-uniform hypergraph on $n$ vertices? The problem
page reads the bound for $n\ge3$, which agrees with the eventual reading up
to the value of $c$. A colouring of the triples of an $N$-set with no
monochromatic $n$-set shows $R_3(n)\ge N+1$.

**Closed outcome: the specified mechanisms are refuted.** The fixed-query
lift, the prefix-selected one-bit XOR lift, and two natural copy-squaring
rules cannot meet the target. This is a failure of these construction
families, not a negative answer to Problem 564 or a barrier to all
two-colour stepping-up. No viable construction or sufficient unproved
lemma with a surviving attack is supplied here. Every attempted mechanism
outputs two colours; higher colour counts are context only.

[[problems/ramsey_theory/E0562/_index|Problem 562]] asks the corresponding
question for every fixed uniformity $r\ge3$. Its two-colour consequence is
proved conditionally on the triple case below; the triple premise remains
open.

## Canonical proof sketch and interfaces

This is the sole sketch of the route. The construction interfaces and the
conditional higher-uniformity transfer are proved implications. The
obstructions invalidate the proposed mechanisms for supplying their
premises. Neither finite synthesis nor those implications prove the target.

### Squaring interface

Suppose a nonempty class of two-colour triple systems $(N,n)$ (a red/blue
colouring of the triples of an $N$-set with no monochromatic $n$-set), with
$N_0\ge2$ and $n_0\ge3$ for some member, is closed under an operation
sending $(N,n)$ to $(N^2,n+C)$ for a fixed integer $C\ge1$. Iterating gives
members $(N_0^{2^j},n_0+Cj)$. For $n\ge n_0$ take
$j=\lfloor(n-n_0)/C\rfloor$. Since $n_0+Cj\le n$,

$$
R_3(n)>N_0^{2^j}\ge2^{2^j},\qquad j\ge\frac{n-n_0-C}{C}.
$$

This is at least $2^{2^{n/(2C)}}$ for $n\ge2(n_0+C)$. Smaller $n\ge3$
are covered by shrinking $c$, since $R_3(n)\ge3$. If the operation applies
to every system, its forcing-number form is

$$
R_3(n+C)\ge(R_3(n)-1)^2+1,
$$

which is weaker than $R_3(n+C)\ge R_3(n)^2$ but sufficient. An admissible
class, its invariant and such an operation remain unknown here. Both
natural operations tested below fail even on a specially chosen seed
class, since their monochromatic sizes grow by at least $a\mapsto2a-2$.

### Finite lifting interface

For $t\ge4$, a red/blue colouring $\varphi$ of the pairs of
$M=\lfloor2^{t/4}\rfloor$ labels with no monochromatic $t$-set exists,
since

$$
\binom Mt2^{1-\binom t2}\le2^{1-t^2/4+t/2}/t!<1.
$$

For fixed integers $C\ge1,D\ge0,t_0\ge4$, it would suffice to produce,
for each $t\ge t_0$, one such seed and a red/blue colouring of the
triples of $\{0,1\}^M$ with no monochromatic $(Ct+D)$-set. A lift of
every such seed would be stronger than needed. For $t\ge8$,
$M\ge2^{t/8}$; putting $t=\lfloor(n-D)/C\rfloor$ yields

$$
R_3(n)>2^{2^{n/(16C)}}
$$

for all sufficiently large $n$. The interpolation and all off-by-one
conventions are detailed on the
[[research/leads/two_colour_triples_stepping_up/prefix_routing|prefix-routing page]].

That page specifies a finite attempt exactly: XOR the graph seed colour,
the orientation of the two deltas, and one outsider bit at a position
selected by their common prefix and delta pair. Its sufficient assertion
is **false within this family**, since every routing table has cliques
of polynomial size in $M$. The page retains the necessary-and-sufficient
constraint system for every possible monochromatic tree, including
repeated labels, arbitrary compatible prefixes and free off-path bits.
A sixteen-point example is real finite data but gives no asymptotic escape.

### Transfer to Problem 562

The
[[research/leads/two_colour_triples_stepping_up/higher_uniformity_transfer|complete two-colour transfer argument]]
sends an $N$-vertex $k$-uniform example avoiding $n$ points to a $2^N$-vertex
$(k+1)$-uniform example avoiding $2n+k-4$ points, for every $n\ge k\ge3$.
Its forcing form is

$$
R_{k+1}(2n+k-4)\ge2^{R_k(n)-1}+1.
$$

Iterating from triples gives forbidden size $2^{r-3}n-r+3$ and a tower of
height $r$, using two colours at every transfer. Combining with the known
upper bound gives the full conclusion of Problem 562, conditionally on a
triple solution. The transfer proof is author-recorded; the classical
upper bound is used at the literature standing stated on that page.
This does not establish the missing triple premise.

## Obstructions and exact scope

- [[research/leads/two_colour_triples_stepping_up/bounded_query_obstruction|Fixed-query obstruction]]:
  a two-colour rule on $\{0,1\}^M$ reads the two deltas, the bits at at
  most $w$ additional positions fixed by that delta pair, and any function
  of the common prefix above the upper delta. It has red and blue sets
  whose sizes multiply to more than $M'$, where $M'=M$ for $w=0$ and
  $M'$ is of order $\sqrt{M/w}$ otherwise. Avoiding a monochromatic
  $n$-set requires $M\le n^2-2n$ for $w=0$, and
  $M<(27w/4)n^4$ for $w\ge1$. For fixed $w$, the cube has at most
  single-exponential order in a polynomial of $n$. This includes mergers
  of the four stepping-up colours and all 256 tables that also read the
  outsider bit. The prefix can affect the output, but the query positions
  must be fixed by the delta pair.
- [[research/leads/two_colour_triples_stepping_up/prefix_routing|Prefix-selected one-bit XOR obstruction]]:
  for the specified rule, query positions may depend on the entire prefix.
  For every seed and every routing table, each colour has a set of at least
  $M^{1/3}/4+1$ words when $M\ge8$. Avoiding an $n$-set therefore requires
  $M\le64(n-2)^3$. Random selection of the active delta labels proves
  this for deterministic, arbitrarily biased routing tables. It is a
  separate argument from the fixed-query theorem, and does not cover
  every prefix-dependent output rule. XORing $w$ selected outsider bits
  instead gives the bound $M\le64w(n-2)^3$, so any fixed number also fails.
- [[research/leads/two_colour_triples_stepping_up/copy_squaring_obstruction|Copy-squaring obstruction]]:
  copy a two-colour triple colouring on blocks and on positions, using
  either the positions rule or the outsider-block rule for mixed triples.
  A monochromatic $a$-set produces one of $2a-2$ points. Iteration makes
  the monochromatic sizes grow exponentially while the proposed forbidden
  size $n_0+Cj$ grows linearly. Neither rule can supply the squaring
  interface, even on a selected nontrivial class of seeds. The two
  configurations, fat and thin blocks and two fat blocks, identify what
  a different mixed rule must control.

All dimensional bounds here bound the orders of colourings in these
families. They are not upper bounds on $R_3(n)$.

## Known constructions and their scope

- The two-colour lower bound $2^{cn^2}$ and the conjecture are statements
  16.4 and p. 140 of [EHR65] on the
  [[../library/ramsey_theory/erdos_1965_partition_relations_cardinal_numbers/_index|library card]],
  printed without proof. The problem page records the known upper bound
  and its status-search scope.
- The three-colour bound $r_3(n,n,n)\ge2^{n^{c\log n}}$ of
  [[../library/ramsey_theory/conlon_2008_hypergraph_ramsey_numbers/theorem_1_1|Conlon, Fox and Sudakov, Theorem 1.1]]
  merges two of the four stepping-up colours and keeps three. With two
  colours the fixed-query obstruction applies to every such merger.
- [[../library/ramsey_theory/bai_2026_new_tower_type_lower_bounds_hypergraph/theorem_1_2|Bai et al., Theorem 1.2]]
  gives two-colour tower bounds for $r_k(k+1,k+1)$, $k\ge6$, from a proper
  three-colouring of a shift graph and a finite two-colouring of pairs of
  twelve states that excludes certain bonds. It colours $k$-sets through
  two windows of $k/2$ vertices and cannot be specialized to $k=3$.
- The [[../library/ramsey_theory/openai_2026_ten_advances_mathematics_theoretical_computer_science/chapter_9/_index|recursive colourings of chapter 9]]
  concern multicolour graph Ramsey numbers of triangles. Their growing
  edge palette supplies no two-colour triple construction.

## Failure account and reopening conditions

The failed step is the construction of a two-colour lift with forbidden
size linear in the graph parameter, or a squaring operation with bounded
additive increase. The required premise is false in each specified family,
by the obstruction that names it. The generic interfaces remain valid
conditional implications. Their premises are unknown for broader families;
no composition of the finite witnesses with those implications supplies them.

Two additional variants have only narrower author analysis:

- **Interval parities.** Adding the parity of the pair's bits strictly
  between the deltas appears to fail. Allocate an extra position for each
  tree edge, outside the labels and query sets, and make the parity of the
  pair's common bits from each node up to the root zero. The interval
  parity then acts as the side bit. This is an unwritten proof proposal,
  not an additional established obstruction or a premise used above.
- **Blow-ups of a fixed four-colour merger.** If positions inside vertex
  blocks merely select which merger to use, one point per block at a common
  position sees a fixed merger. The fixed-query obstruction applies to
  that subconfiguration. No broader blow-up theorem is asserted.

Reopening needs a specified rule outside the hypotheses of these
obstructions, a large subset of the cube that excludes their displayed
trees, or a mixed squaring rule with an invariant controlling both known
configurations. Merely choosing a more complicated prefix selector in the
one-bit XOR family cannot work. No such replacement is constructed here.

The next discriminating test for any proposed replacement is whether its
exact triple rule defeats the sparse distinct-label trees on the
prefix-routing page and the repeated-label trees on the fixed-query page,
or, for squaring, both explicit mixed configurations. Surviving these
necessary tests would still leave the parameter-uniform proof. More small
examples in the refuted families cannot close that gap.

## Evidence

[evidence/main.py](evidence/main.py) rebuilds explicit monochromatic sets
for all three obstruction families from actual binary words or pairs and
recomputes every triple colour. It also exhaustively checks the retained
sixteen-point routing table and its prefix-independent control. Run it
from the repository root with
`uv run --no-sync python wiki/research/leads/two_colour_triples_stepping_up/evidence/main.py`.
It takes about a second and exits nonzero on a failed check. The optional
finite synthesis program has no independently checked UNSAT certificate.
The universal obstructions rest on the written arguments, not the finite
checks. No independent review or verification tier is claimed.
