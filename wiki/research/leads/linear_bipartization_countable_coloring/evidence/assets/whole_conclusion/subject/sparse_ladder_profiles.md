[cut]

# Sparse ladder orders do not bound bipartization linearly

[[research/leads/linear_bipartization_countable_coloring/_index|The canonical proof sketch]]
records the target and the remaining countable-coloring gap. [cut] They rule out one proposed
finite sufficient condition for a negative answer; they do not determine
the profile of the source's particular graph.

## Source interface and the proposed implication

The proof of
[[../library/set_theory/soukup_2015_trees_ladders_graphs/theorem_5_5|Soukup's Theorem 5.5]]
constructs a sparse ladder system on $T(S)$ whose graph has chromatic
number $\aleph_1$. The version used is arXiv:1409.2922v1, Definitions 3.1
and 5.2, Lemma 5.4, Theorem 5.5, Claim 5.5.1 and Observation 5.6. Here one
may choose $S\subseteq\omega_1$ stationary and costationary. The graph has
size continuum; the theorem's conclusion is not restricted to one branch.

For $r<s$ in one ladder $C_t$, sparsity says that no decreasing graph path
from $s$ reaches a vertex $w$ with $\max(w)\le\max(r)$. This is the
non-strict inequality in the printed Definition 5.2, p. 15. [cut] The existence theorem remains an external input.

For a finite ordered graph on $1,\ldots,n$, orient every edge downwards and
let $r(v)$ be the least vertex reachable from $v$, allowing the path of
length zero. Consider the condition

$$
 u<w<v,\quad uv,wv\in E
 \quad\Longrightarrow\quad u<r(w). \tag{SO}
$$

Thus the intervals $[r(u),u]$ of the lower neighbors of any vertex are
pairwise disjoint. Every finite subgraph of a sparse ladder graph satisfies
(SO), by ordering its vertices by $\max(t)$ and resolving equal values
arbitrarily. Any decreasing path in the finite graph is a monotone path in
the source graph. Sparsity therefore gives a strict inequality between the
corresponding maximum ordinals, irrespective of how ties were resolved.

Condition (SO) is hereditary: deleting edges or vertices only shrinks
reachable sets and increases their minima in the inherited order. It also
gives a path decomposition whose bags induce forests. Use the intervals
$[r(v),v]$ for the bags. Every edge has its endpoints together at its lower
endpoint. At any point of the order a vertex has at most one lower neighbor
whose interval contains that point. The induced bag graph is consequently
a forest.

A uniform bound $\beta(F)\le C|F|$ for all finite graphs satisfying (SO)
would compose with Soukup's theorem to give a negative answer to Problem
111. The proposition below refutes this finite bound. In particular,
neither (SO) nor the existence of the displayed forest-bag decomposition
provides it.

## A family with unbounded cost per vertex

**Proposition.** For every power of two $t\ge2$ there is an ordered graph
$J_t$ satisfying (SO), with chromatic number at most three, such that

$$
 |V(J_t)|=3t^2,
 \qquad
 \beta(J_t)\ge\frac{t^2}{2}(t-\sqrt t).
 \tag{1}
$$

**Construction.** Put $M=t^2$. Take $t$ disjoint copies of $K_{t,t}$,
with sides $A_i,B_i$, and $M$ independent vertices $z_j$. Choose $t$
distinct nonconstant columns of a Sylvester Hadamard matrix of order $M$;
write the resulting matrix as $H=(h_{ji})$. Each column has $M/2$ entries
of each sign and $H^{\mathsf T}H=MI_t$.
Explicitly, for $t=2^r$ take rows indexed by $j\in\mathbb F_2^{2r}$,
distinct nonzero column labels $a_i$, and $h_{ji}=(-1)^{j\cdot a_i}$.
Every nonzero binary character sums to zero, proving both properties.

For each $i$, the vertex $z_j$ has one neighbor in $A_i$ if $h_{ji}=1$,
and one in $B_i$ if $h_{ji}=-1$. Distribute these choices evenly within
each side. This is possible because $M/2$ is divisible by $t$.
Every old vertex then has exactly $t/2$ neighbors among the $z_j$.

Order the blocks consecutively, with $A_i$ before $B_i$, and put all
$z_j$ last. An $A_i$ vertex has no lower neighbors. The lower-neighbor
intervals of a $B_i$ vertex are the singleton vertices of $A_i$. Each
$z_j$ has one neighbor per block, whose reachable interval stays in that
block. This verifies (SO). Coloring all $A_i$, all $B_i$, and all $z_j$
with three separate colors verifies the chromatic upper bound.

**Rounding a cut.** In an arbitrary two-coloring, choose for each block
the closer of its two proper bipartitions. If $x_i$ vertices of $A_i$ and
$y_i$ vertices of $B_i$ differ from that bipartition, then
$d_i=x_i+y_i\le t$. The block's monochromatic-edge count is

$$
 x_i(t-y_i)+y_i(t-x_i)
 =td_i-2x_iy_i
 \ge td_i-d_i^2/2
 \ge td_i/2.
$$

Change those $d_i$ colors to make the block proper, leaving the apex
colors fixed. At most $(t/2)d_i$ incident apex edges become monochromatic,
while all the block's monochromatic edges disappear. Doing this in every
block cannot increase the total cost. It follows that an optimal cut may
be chosen proper on every block.

Encode such a choice by $s\in\{-1,1\}^t$, giving every vertex of $A_i$
sign $s_i$ and every vertex of $B_i$ sign $-s_i$. The signs of the $t$
neighbors of $z_j$ sum to $(Hs)_j$. Its minimum contribution is
$(t-|(Hs)_j|)/2$. Hence, in fact,

$$
 \beta(J_t)=\frac{Mt-\max_{s\in\{-1,1\}^t}\|Hs\|_1}{2}.
 \tag{2}
$$

Orthogonality and Cauchy--Schwarz give
$\|Hs\|_1\le\sqrt M\|Hs\|_2=M\sqrt t$. This proves (1), and
$\beta(J_t)/|J_t|\ge(t-\sqrt t)/6\to\infty$.

## Evidence and failure scope

The exact-integer checker [evidence/main.py](evidence/main.py) regenerates
$J_t$ for $t=2,4,16,64$. It checks simplicity, the order condition, the
three-coloring, all column inner products, balanced apex incidence, and the
rounding inequality for every possible pair of block error counts. It
enumerates all graph cuts at $t=2$ and all block phases at $t=2,4$ to
cross-check (2). For $t=16$ and $64$, the lower bounds in (1) are respectively
$1536$ on $768$ vertices and $114688$ on $12288$ vertices. These are certified
lower bounds, not asserted exact optima.

The checker uses Python integers and the repository evidence harness, with
no numerical solver or external data. [cut]
The expected runtime is below a minute on one core; `--quick` omits $t=64$.
The general conclusion follows from the displayed proof, not from finite
coverage. [cut]

The failed step is precisely the implication from (SO) to a uniform linear
profile. Its proposed input is false. Neither one-dimensional reachability
nor forest bags account for incompatible bipartition choices of the dense
blocks. A route using Soukup's construction must impose and prove a further
restriction on its actual finite realizations that excludes this mechanism,
then prove the profile bound for all of them. No such restriction is
established here. The three-colorable graphs $J_t$ are not counterexamples
to Problem 111, and their existence does not show that every sparse ladder
construction realizes them.
