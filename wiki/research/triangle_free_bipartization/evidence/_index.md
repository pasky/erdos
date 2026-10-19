---
name: research/triangle_free_bipartization/evidence
title: Evidence for triangle-free bipartization
desc: Exact profile bounds, two-root switching traps and controls for hereditary and recursive comparisons, with bounded numerical discovery for the whole-band argument kept separate from evidence.
created: 2026-10-15T23:29:23Z
updated: 2026-10-17T22:11:11Z
---

# Evidence for triangle-free bipartization

[[research/triangle_free_bipartization/_index|..]]

***

`main.py` checks the finite profile calculations on
[[research/triangle_free_bipartization/profile_envelope_obstructions|the obstruction record]]
and the edge-cut, homomorphism and $C_{13}(1,5)$ examples on
[[research/triangle_free_bipartization/proof_sketch|the proof sketch]],
as well as the exact table and concentration constants for
[[research/triangle_free_bipartization/two_root_switching_traps|the two-root traps]].
Run it from the repository root:

```sh
uv run --no-sync python wiki/research/triangle_free_bipartization/evidence/main.py
```

The full run takes several minutes. `--quick` skips Higman–Sims and the
seven-root Clebsch clauses and takes about a minute. The program states
its clauses in its docstring and exits nonzero if any fails. Its dependency
on the prepared repository environment includes NumPy, SciPy and NetworkX.

**Two-root switching traps.** `util/switching_trap.py` builds the sixteen-part
template and fixed colouring, checks all $32768$ ordered root-part/switch
cases in bounded integer arithmetic, and verifies the strictly positive
minimum $49/65536$ in the $M/N^2$ gain convention at retention probability
$7/8$. It checks an attaining case, an improving two-root control at
retention probability one, and the three-root escape of gain
$-931/524288$. Rational comparisons verify the constants in the
probabilistic existence argument at $N=2^{32}$. This checks the finite
inputs to that argument; it does not generate a large random graph or
certify the original bipartization conjecture. A further exact sum checks
that the three-root gain weighted by squared common non-neighbour mass
has limiting monochromatic-density value $-164741871/2^{47}$; this is an
explicit order-seven row separating the trap from genuine maximum-cut states.
Run just these clauses with
`main.py --switching-only`; the full and quick modes also include them.

**Hereditary comparison controls.** `util/hereditary.py` checks the boundary
identity in the sketch and the inequality from the uniform source bound
$B=4/47$ for every vertex subset of $C_5$, $C_7$, Petersen and $C_{13}(1,5)$,
with maximum cuts found exhaustively. It rejects the false bound $B=7/100$
on $C_5$. A further rational calculation gives
$R_{4/47}=-1077/1540096$ for roots in parts $(2,3)$ and subset mask $41$
of the two-root switching trap, explicitly separating that trap by the
hereditary comparison. These integer controls check the formula on the stated finite
domain; the general argument still depends on the imported source bound.
Run them alone with `main.py --comparison-only`. Full and quick modes include
them as well. The same module checks every fractional selection with cell weights in
$\{0,1/2,1\}$ on $C_5$ and $C_7$, and the balanced monochromatic-degree
identity for the uniform mixtures of all optimal cuts of the four transitive
controls. A single maximum cut of $C_5$ is a negative control for that
pointwise identity. The module also checks every assignment of the vertices
of $C_5$ and $C_7$ to a recursive part or to independent coins of biases
$0,1/4,1/2,3/4,1$, and checks the induction row at $2/25$ on $C_5$.
For independent uniform optimal cuts of $C_5$, it checks the product of
monochromatic degrees and, on every ordered five-root tuple, the identity
between joint cut-pattern counts and the outer product of pattern counts.
Using the same cut twice is a negative control for independence.
These checks do not establish global optimality over vertex weights.
No contraction or induction certificate is checked by these controls.

**Exact graph and profile calculations.** Every graph is built from its
definition. The checker verifies triangle-freeness, edge counts and
vertex-transitivity by explicit automorphisms. For Higman–Sims it checks
the Golay hexads, $A^2+6A-16I=6J$, regularity, and an induced pentagon.
The smaller graphs' bipartization numbers come from all cuts and their
edge-cut values from all ordered four-tuples. The placement values $V_k$
scan every placement and every compatible cut. The four-root Clebsch
envelope scans every rule of every type. Exhibited rules give exact upper
bounds for the other envelopes.

Higman–Sims sums use weighted orbit representatives regenerated from two
stored stabilizer generators. The generated group has 887040 permutations;
its root-tuple weights total $100^6$. Canonical labeled types and their
numbers of labeled versions are checked to cover every placement. No
external identification of the automorphism group is required.

**Exact lower bound used by L240.** For each seven-root type,
`util/exactcut.py` branches on both colours of a chosen profile. It prunes
only after an integer Gram matrix and diagonally dominant residual give
a rational lower bound on every cut in the branch. The
[[theory/extremal_graph_theory/L240_seven_root_linear_band_obstruction/_proof|proof of L240]]
gives the algebra and the reduction from these weighted cut problems to
$U_7$. A numerical optimizer suggests factors and branching choices; the
inequality is valid for every proposed integer factor, and no numerical
optimality assertion is trusted. Explicit coefficient bounds exclude
integer overflow. Exhausted limits or failed proposals raise errors.
Small weighted controls are compared with exhaustive minima, deliberately
false targets are rejected, and a signed interaction matrix checks the
fixed-colour case.

This proves $U_7(W_{\rm HS})\ge81/1000$. The checker then verifies the
mixture's interior density $1/4$ and slack at least $1/1200$. A separate
exact threshold check proves $m_k(W_{\rm HS})>2/25$ for $k\le6$ without
asserting the optimum of every type.

**The in-band mixture.** The circulant $C_{13}(1,5)$ is built from its
connection set $\{1,5,8,12\}$; triangle-freeness, regularity and the
rotation automorphisms are checked, and all $2^{12}$ cuts are scanned for
$D_2=6$. Its $V_k$ and $m_k$ for $k\le4$ come from exhaustive scans of
placements and of every rule of every type. `util/mixtures.py` computes the
least unrooted four-root row of the mixture with the Clebsch graph exactly:
its support is checked against all 41 triangle-free labeled four-root
types, every deterministic rule is scanned in bounded integer arithmetic,
and for every assignment of the nonzero classes the best coin on the zero class is
found by minimizing its quadratic cost in exact integers. The minima at the
four stated weights are compared with stored rationals. A stored five-root
rule, a mask of profile sides, has its conditional density recomputed on
both graphs.

**Abelian Cayley graphs.** `util/cayley.py` lists every product of
cyclic groups of order $n\le24$, which covers every abelian group of each
order, and every symmetric sum-free connection set $S$ with $|S|/n$ in the
band; sum-freeness makes the Cayley graph triangle-free. All cuts are
scanned for $n\le16$; above that a seeded local search proposes a cut,
and its uncut edges are recounted exactly. The check is that every one of
the 5199 connection sets gives a graph with a cut of monochromatic density
at most $12/169$, that $12/169$ is attained, and that the scan contains
$C_{13}(1,5)$ and the Clebsch graph. The presentations may repeat isomorphic
graphs. Four of the connection sets occur at order four; all orders from
one through $24$ are included.

**Numerical optimum reports.** The stronger equality
$U_7(W_{\rm HS})=802719381387/9765625000000$, and the exact values reported
for $U_k,m_k$ at $k=5,6$, use HiGHS mixed-integer optimality reports on
integer input with zero relative gap. Each returned rule is re-evaluated
exactly, so its cost is a rigorous upper bound; its claimed optimality is
floating-point evidence. These stronger equalities are not premises of
L240 or of the separate exact thresholds. Likewise, the five-root
placement minimum of 406 uses numerical optimality for profile graphs
with more than eighteen classes. Every minimum with at most eighteen
classes is exhaustive.

**Retained inputs.** `assets/rules.json` holds Boolean rules as hexadecimal
profile masks, keyed by graph, root count and canonical type. Every needed
rule cost is recomputed from the graph. The rules are witnesses, not saved
verdicts. `assets/higman_sims_automorphisms.json` holds two stabilizer
generators and two permutations moving vertex 0. Their numbering follows
`util/envelopes.py`: 0 is infinity, 1–22 are points, and 23–99 are hexads.
The graph, group, profile tables and integer Gram bounds are regenerated;
no private cache or saved validity flag is read.

**Discovery program.** `produce.py` is a discovery entry point, not
evidence, and `erdos evidence` does not run it. With `util/flaglp.py` it
builds the localized rooted rows of the proof sketch at order seven or
eight and searches for certificates by floating-point linear programming
with column generation; `--game` adds the mixture game over a fixed
library of genuine graphons. It writes nothing. Its printed thresholds
and game values are the floating-point outputs quoted on the sketch; they
certify neither a bound nor an obstruction. A certificate it found would
have to be recovered and checked in exact rational arithmetic before
any use. Run it from the repository root, for example:

```sh
uv run --no-sync python wiki/research/triangle_free_bipartization/evidence/produce.py --order 7 --interval 0.3 0.3125 --game
```

At order seven a run takes a few minutes; at order eight building the rows
takes a few minutes and each bisection step several more.

The sketch quotes the following runs. Each item gives the options after
`produce.py`, on the default interval $[0.3,0.3125]$ unless an interval is
named, and the reported value; solver versions may shift the last digits.

- With `--order 7 --game`: game value about $-1.4\cdot10^{-5}$ and
  reported threshold about $0.0913$.
- With `--order 7 --eigen-rounds 25 --bracket 0.08 0.0914 --steps 9`:
  about $0.0897$.
- With `--order 7 --start 0.088 --eigen-rounds 40 --bracket 0.08 0.0897`
  and `--steps 6`: about $0.0891$.
- With `--order 7 --products --bracket 0.0905 0.0914 --steps 5`: about
  $0.0913$.
- With `--order 7 --interval 0.3075 0.308 --bracket 0.08 0.0944`: about
  $0.0906$.
- With `--order 7 --interval 0.31 0.3197 --bracket 0.07 0.1 --steps 9`:
  about $0.0904$; with `--interval 0.2486 0.26` and the same bracket,
  about $0.0925$.
- With `--order 8 --bracket 0.08 0.096 --steps 7`: about $0.0891$.
- With `--order 8 --start 0.088 --eigen-rounds 10 --bracket 0.08 0.09`
  and `--steps 6`: about $0.0879$; a positive numerical margin appears
  after three rounds.
- With `--order 8 --start 0.084 --eigen-rounds 14`: eps at $0.084$ stays
  negative through the eighth round, rising from about $-8.5\cdot10^{-5}$
  to $-5.6\cdot10^{-5}$; the sketch quotes those rounds.

**Coloured discovery program.** `produce_coloured.py` is a second discovery
entry point, not evidence, and `erdos evidence` does not run it. With
`util/colouredflags.py` it builds the order-six relaxation of the proof
sketch's section on states coloured by a maximum cut: it enumerates the 1031
vertex-2-coloured triangle-free graphs of order six, forms vertex-stability,
switching, band and moment rows as averages over all orderings, and
maximizes the monochromatic density by a floating-point log-barrier method,
adding violated switching rows between solves. Pricing is exhaustive over
the recoloured cell sets on one to three roots and a seeded local search on
four. After each solve it prints the state's objective; with `--dual` it also
prints a dual bound, and `--bound` prints the objective and dual bound of a
state saved by `--save`. For the bound, a linear program chooses nonnegative multipliers $\lambda_i$ on the priced rows and
nonnegative weights on candidate matrices $Z$ for each block: the barrier's
inverse block matrix projected to positive semidefinite, $vv^{\mathsf T}$
for every eigenvector $v$ of the state's block matrix, and normalized sums
and differences of the eigenvectors of its five smallest eigenvalues. The
resulting
$\max_H\bigl(m(H)+\sum_i\lambda_i\,\mathrm{row}_i(H)+\sum\langle Z,F_b(H)\rangle\bigr)$
bounds the objective of every state satisfying the rows and blocks,
including rows not yet priced. This linear program takes a minute or more
and about 3 GiB with `--t4 --products`. `--t4` adds
four-rooted moment blocks and `--products` the products of $\sigma$ with
switching rows and with $\sigma$. It writes nothing unless `--save` names a
file, for example under the ignored `output/`, which then receives the state
and the added rows after each round, for `--bound` or exact recovery. Run it
from the repository root, for example:

```sh
uv run --no-sync python wiki/research/triangle_free_bipartization/evidence/produce_coloured.py --interval 0.3 0.3125 --validate
```

Building takes a few seconds and each round one to two minutes, about five
with `--t4 --products`. `--seconds` gives a positive time limit for each
barrier solve (default $180$ seconds), and `--lp-seconds` for each optional
dual LP (default $120$ seconds). `--limit` counts rows, not seconds. An
unfinished LP reports its status and returns the raw floating bound; an
unfinished barrier solve returns a possibly relaxed iterate, not an optimum.
`--validate` first computes the exact order-six states of the Petersen graph
and of $C_{13}(1,5)$, each coloured by a maximum cut found by scanning every
cut, and exits nonzero unless both satisfy every row and block to rounding
and a one-colour cut of the Petersen graph violates them. This checks the
implementation of the rows, not any bound. `--traps` instead scans every
cut of $C_5$, $C_7$, the Petersen graph, the Clebsch graph and $C_{13}(1,5)$
for vertex-stable cuts above $N^2/25$ without an improving two-root
switching, and runs switching descents from random cuts on seeded random
triangle-free Cayley graphs of band density; it takes seconds. The sketch
quotes these runs:

- With `--interval 0.3 0.3125 --validate --t4 --products --limit 500` and
  `--save`: validation passes; round 0 has objective $0.1200$, round 6
  objective $0.0841$, and at round 8, objective $0.0840$, pricing finds no
  violated row and the run stops. `--bound` on the state saved at round 0
  gives $0.1200$, and on the state saved at round 6 gives $0.0988$.
- With `--interval 0.2486 0.3197 --t4 --products --limit 500` and `--save`:
  round 2 has objective $0.0857$; `--bound` on its saved state gives
  $0.0990$.
- With `--traps`: no vertex-stable cut above $N^2/25$ of the five graphs
  lacks an improving two-root switching ($0$, $7$, $0$, $40$ and $78$ such
  cuts), and every descent on the 19 Cayley graphs, of orders $41$ to $128$,
  ends at most $0.79N^2/25$.

All of this is floating point. The dual bound holds whatever rows remain
unpriced, but only up to rounding. Feasibility checks cover only the rows
found so far, and an unfinished barrier iterate can retain a positive
relaxation. Its objective need not bound the optimum of those rows. The printed values certify neither a bound nor
an obstruction; a dual bound below $2/25$ would still need an exact
rational certificate.

**Weighted-extremal paired-cut discovery.** `produce_extremal.py`, with
`util/paired_flags.py` and `util/extremal_model.py`, implements the
sketch's finite weighted-extremal reduction. It enumerates $674$ four-colour
classes at order five or $6257$ at order six. The colour group consists of
the two independent global complements and exchange of the cuts; it is
not the full permutation group on four colours. Coefficients average all
vertex permutations and these eight colour transformations.

The rows include vertex stability, the extremal minimum-degree condition,
balance against flags coloured by the other cut, the equality $m=B$, band
conditions, fractional hereditary comparisons, stochastic switching and
recursive partial cuts. Ordinary moment and gain-weighted square blocks
are supplemented by cut-pattern matrices from two independent active cuts.
Copositive pricing uses grouped five-cycle Horn matrices and their
nonnegative diagonal congruences. Optional bounded integer search proposes
further matrices $J-2A_T$; every proposed $T$ is checked for triangles.
The weighted-Mantel argument in the sketch proves these matrices
copositive, without trusting numerical optimality. Their searches are
incomplete. `--affine-squares` adds all Boolean one-root hereditary-square
blocks at order five. At order six, scalar pricing keeps canonical root
types and, for zero roots, canonical four-colour multiplier flags: this is
a specified subset, not exhaustive pricing of the full rooted family.

`--minimal-support` adds the sketch's proper-support comparisons at $2/25$.
Their hypothesis is a weighted counterexample with the fewest support
vertices, maximized over its weights. The selected set must omit either a
named root's whole profile cell or its cross-neighborhood in one active
cut. Vertex stability and positive minimum degree guarantee that the latter
is nonempty. These are zero-derivative rows in the parameter $B$. The
implementation checks the exclusions in each control recipe and evaluates
the proposed rows on both cycle controls; the proof of the minimality
reduction remains the argument in the sketch. Arbitrary induced selections
do not qualify for these target-constant rows.

At degree $d$, the LP seeks nonnegative Bernstein coefficients for the
inequality multipliers and a factor $\rho<1$ satisfying $(C_d)$.
Eigenvectors propose rank-one square rows; they do not supply exact
positive semidefinite certificates. Each LP checks an explicit feasible
$\rho=1$ baseline and has a positive `--seconds` limit; `--rounds` bounds
the number of iterations. An incomplete solve stops without a mathematical
verdict. Unmodified coefficients are re-evaluated before a numerical
candidate is reported. No exact reconstruction is implemented.

```sh
uv run --no-sync python wiki/research/triangle_free_bipartization/evidence/produce_extremal.py --validate-only
uv run --no-sync python wiki/research/triangle_free_bipartization/evidence/produce_extremal.py --degree 2 --rounds 24 --seconds 90
```

Validation uses independent uniform optimal-cut pairs on $C_5$, with
$B=2/25$, and $C_7$, with $B=2/49$. The latter lies inside the density
band and checks every base row and block there. For an odd cycle on $n$
vertices, the weighted bipartization density is twice the least adjacent
weight product, at most $2/n^2$ by the arithmetic-geometric mean inequality;
so these are genuine weighted-extremal controls. A pentagon plus an isolate
and a dependent pair of pentagon cuts must fail the balance equalities.
These controls test the implementation in floating arithmetic, not the
full target. The degree-two order-five command above completed fourteen
LPs at $\rho$ numerically equal to one before local pricing found no new
direction. This gives no bound, no exact feasible state and no obstruction
to the full family.

**Recursive induction discovery.** `produce_recursive.py` implements
$(I_r)$ on the $107$ uncoloured triangle-free graphs of order seven or the
$410$ of order eight. Each profile cell receives a fixed colour, a coin
of bias $1/4,1/2,3/4$, or one of `--parts` independently recut parts.
The root families use $k=\ell-2,\ell-3,\ell-4$ roots at order $\ell$,
with the fixed nonnegative multipliers and moment blocks of `util/flaglp.py`.
The search adds full profile-mass square directions localized by an
induction row or by $d(r_i)-4/25$. `--products` prices products from a
finite list of induction and degree factors on the same roots; the list
and the coordinate searches are incomplete. Pentagon boundary controls
are checked for each generated row whose hypotheses apply to it.
`--mip-seconds` optionally adds bounded mixed-integer pricing of
deterministic binary cuts on the largest root family. It imposes all four
XOR inequalities, so signed pair weights are allowed. Any proposed side
assignment is rebuilt as a cut row and checked before use; a solver time
limit supplies no optimality or exhaustive-pricing assertion. This option
does not exhaust recursive or randomized rules.
`--ternary-seconds` additionally proposes a fixed outside cut with one
recursive part, on at most `--ternary-types` root types of largest mass
in the current numerical state. Binary variables select the two outside
colours; product variables enforce their quadratic costs. The proposed
ternary assignment is rebuilt as a valid row regardless of the optimizer's
status. These positive per-type limits do not make pricing exhaustive.
`--full-localizers`, implemented by `util/recursive_flags.py`, adds degree
surplus times every one-rooted flag on $\ell-1$ vertices. It also adds
degree-localized square blocks on $s$ roots and $m$-vertex flags with
$2m-s\in\{\ell-2,\ell-1\}$ and $m-s\le3$, for each root whose degree
is used. Its additional recursive matrices use $\ell-6$ roots, two cut
endpoints and two disjoint two-vertex flag extensions. Every assignment
from the declared finite cell-label set is enumerated for those matrices;
each iteration adds only selected negative square directions. These are
the specified larger flag bases, not a claim to include every possible
localizer. Pentagon matrices must be positive to rounding, and the empty
graph must violate a degree row. No completion of the full band follows
from these implementation controls.

```sh
uv run --no-sync python wiki/research/triangle_free_bipartization/evidence/produce_recursive.py --order 7 --parts 3 --products --rounds 100 --seconds 30
```

The LP normalizes nonnegative weights on induction rows and products and
maximizes a margin whose positivity would make every graph coefficient
negative. The displayed margin is not a bipartization bound. The command
above ends with margin about $-0.0006143$, not a certificate. By default
unused positive-slack columns are discarded and may be rediscovered;
`--keep-inactive` retains them. `--interval` selects a closed density
interval; closing one interval would still require certificates covering
the rest of the band. Every LP has a positive time limit, and no unfinished
solve or locally stationary state is called feasible for the complete
system.

**Nine-point lifting.** `produce_lifted.py` and `util/lifted_flags.py` implement
the sketch's deletion lift and seven-root rows $(J_7)$. They generate the
nine-vertex triangle-free universe by every independent-neighborhood
extension of the eight-vertex universe, with exact isomorphism checks for
duplicate classes. The deletion matrix records the nine eight-vertex
subgraphs of every resulting class. Seven-root coefficients count all
embeddings of each canonical labeled root type and both endpoint orders;
integer mass and edge identities check coverage. This avoids constructing
the complete nine-vertex labeling table. Proposed binary rules have integer
coefficient numerators with denominator $25\cdot9!$.

The new full square basis uses one root and five-vertex flags.
`--three-root-squares` adds three-rooted six-vertex flags. Sampling the
complementary extension sets gives exactly their nine-point coefficients.
Pentagon occupancies count all $5^9$ ordered samples, check the deletion
identity, test new square matrices, and check each proposed seven-root row
in integer arithmetic. These are generation controls, not a full-target
certificate. The program also separates the original order-eight rows on
the projected numerical state.

`--localized-squares` adds nine-point matrices on one-rooted four-vertex
flags, weighted by a one-root recursive comparison or either band
surplus. The recursive rules enumerate the five stated outside coin
biases and two recut labels on the two adjacency cells. All $5040$
root, endpoint-pair and complementary extension choices are counted;
integer mass and edge identities check their coverage. Recursive
coefficient numerators have denominator $200\cdot5040$, and band
numerators have denominator $10000\cdot5040$. Pentagon controls test
recursive and lower-band matrices as positive semidefinite. The pentagon
is outside the upper band, so that control instead checks the reversed
sign of its upper-band matrix. These controls do not assert positivity
on arbitrary numerical states.

`--pentagon-recursion` enumerates all $3^{11}$ assignments of the eleven
pentagon-neighborhood profiles to two fixed colours and one recut part.
It does this for every induced pentagon subset of every seven-root type;
the other two roots act as a nonnegative multiplier. The sketch proves
$(J_{5\mid7})$ from recursive induction. The least value on this finite
grid is computed in floating arithmetic, and each proposed row is rebuilt
with integer numerator and denominator $50\cdot9!$. Its value must agree
with the enumerated quadratic expression, and its integer pentagon control
must be nonnegative. This exhausts the stated three-label grid only;
absence of a numerical violation is no exact feasibility certificate.

```sh
uv run --no-sync python wiki/research/triangle_free_bipartization/evidence/produce_lifted.py --three-root-squares --localized-squares --rounds 36 --seconds 60
```

`--seed-eight` can import a saved whole-band order-eight discovery directory
from `produce_recursive.py`; it is optional, and its floating rows remain
subject to exact reconstruction if a candidate appears. Neither a saved
margin nor a seed file supplies evidence. `--seed-nine` similarly reuses
active rows and a numerical state saved by this nine-point program; all
coefficient tables and generation controls are rebuilt. The whole-band LP seeks a strictly
negative combination of valid rows; cut and square pricing remain incomplete.

These discovery programs write nothing unless `--save` names a directory. Their
saved rows, multipliers and recipes are numerical recovery ingredients,
not cached success flags. None is an evidence entry point, and none
is run by `erdos evidence`. An exact full-band certificate remains missing.

**Common-marginal discovery.** `produce_coupled.py` joins the nine-point
uncoloured state to the paired-cut five-point state through the fourteen
uncoloured five-point classes. The former projection counts all $126$
five-element subsets, and the latter forgets both colours. Pentagon
controls check that the two marginals agree. Parameter-free balance rows
use three-point flags coloured only by the other cut; parameter-free
degree rows may use both cuts. The sketch proves their different
hypotheses. Interval consequences of $2/25<B\le4/47$ retain the correct
inequality directions, and proper-support rows still require their root
or cross-neighborhood exclusions. An isolate control must fail the
parameter-free balance identity.

Additional five-point matrices multiply one-rooted two-point flag squares
by $d(0)-2B$, $B-2/25$, $4/47-B$, and $(400/1243)p-B$. A disjoint
monochromatic edge realizes $B$, so no unknown parameter is replaced by
the target. The sketch proves the pointwise or scalar positivity used by
each matrix. Source-bound one-root hereditary square blocks are retained
as well. Pentagon controls check the additional matrices before solving.

The default LP adds the monochromatic-density objective to the coloured
coefficients and minimizes the sum of the two coefficient maxima, with
nonnegative row multipliers and free marginal-equality multipliers. An
exact upper bound of $2/25$ would exclude a counterexample across the
whole band. The optional `--mode contradiction` instead normalizes all
nonnegative multipliers and seeks a strictly negative sum. Isolated
padding to the sparse endpoint also supplies $B\le(400/1243)p$ on the
counterexample band, multiplied by disjoint three-point flags; the sketch
derives its scope. Both objectives require exact reconstruction and all
positivity checks. Unused priced columns can be discarded and rediscovered;
this weakens discovery only. Optional `--seed-coupled` restores selected
floating rows and the separation state from an earlier output, after
checking its declared universe; it accepts no verdict.
`--seed-all` retains every saved priced row instead of only rows with
positive saved multiplier. Saved zero multipliers need not make their
inequalities dispensable during discovery.
`--coloured-pool` controls the retained slack-column pool, while base rows
and rows with positive dual weight are kept. `--localized-squares` includes
the stated nine-point recursive/band matrices in the uncoloured component.
`--pentagon-recursion` also includes $(J_{5\mid7})$ there.
`--global-cuts` links complete seven-root cut algorithms directly to the
paired optimum. One rule is chosen for each canonical root type; the
integer multiplicity $7!/|\operatorname{Aut}(\tau)|$ makes the total
sampling mass one. The resulting integer cost numerator has denominator
$9!$ and is checked against the pentagon minimum in integer arithmetic.
The shared inequality is $C\cdot Y-c_m\cdot Z\ge0$, so its two
coefficient components have the same nonnegative multiplier. Saved
global-cut rows and their complete rule recipes remain discovery
ingredients, subject to exact reconstruction with the rest of a candidate.
The bounded LP uses the interior-point method by default, with dual simplex
available through `--method highs-ds`; neither status is accepted unless
the solve completes and its unmodified coefficient bounds are evaluated.
Numerical margins, incomplete pricing and time limits certify nothing.
This is also a discovery program, not an evidence entry point.

```sh
uv run --no-sync python wiki/research/triangle_free_bipartization/evidence/produce_coupled.py --rounds 20 --seconds 60
```

**Balanced per-type cut pool.** `produce_envelope.py --seed <directory>`
reads floating row ingredients saved by `produce_coupled.py`. It collects
the saved seven-root rules and every rule in the complete algorithms,
rebuilds their costs in integers, and permits independent mixtures within
each root type. With the type multiplicity absorbed into each cost row,
the multiplier sums are equal to one shared $\gamma$ on every type; the
paired component has coefficient $-\gamma c_m$. This implements the
balanced formulation of (GC) in the sketch. Missing types receive the
valid all-one-colour rule. An integer pentagon control checks the least
cost over all combinations of the finite pool.

The LP has a finite `--seconds` limit. Its numerical output is recomputed
after nonnegative weights and equal type totals are restored. An exact
certificate would still require exact recovery of the saved uncoloured
and paired rows, their positivity factors, all multipliers, the balance
equalities, and every coefficient bound. Cached row files and a completed
numerical solve supply no such warrant. This is a discovery program, not
an evidence entry point, and a failure in this pool obstructs no larger
rule family.
