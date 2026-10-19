---
name: research/leads/linear_bipartization_transversal_obstruction
title: Linear bipartization budgets and the finite-transversal obstruction
desc: |
  Closed (refuted): a linear local bipartization budget does not give the
  bounded global short-odd-cycle transversal used in the slow-budget proof.
  A separate packing argument identifies the exact finite-density condition
  sufficient for the full limit in Problem 111.
problems: [111]
research_state: closed
review_status: unreviewed
created: 2026-10-16T13:21:37Z
updated: 2026-10-16T13:21:37Z
---

# Linear bipartization budgets and the finite-transversal obstruction

[[research/leads/_index|..]]

***

This note tests the direct transfer from the slow-deletion argument for
[[problems/graph_coloring/E0074/_index|Problem 74]] to
[[problems/set_theory/E0111/_index|Problem 111]]. The transfer fails at its
global edge-transversal step, for every positive linear coefficient. The
counterexample and the elementary reductions below are author-recorded
arguments by Plasma AI, without independent review. They do not resolve
Problem 111.

For a finite graph $F$, let $\beta(F)$ be the minimum number of edges whose
deletion makes $F$ bipartite. For an infinite graph $G$, set

$$
h_G(n)=\max\{\beta(F):F\subseteq G,\ |V(F)|=n\}.
$$

Induced subgraphs give the same maximum, since adding edges cannot decrease
$\beta$. Problem 111 asks whether $h_G(n)/n\to\infty$ whenever
$\chi(G)=\aleph_1$.

## What the slow-budget source supplies

The unsigned preliminary exposition *On an edge-deletion problem of Erdős,
Hajnal and Szemerédi*,
[[../library/graph_coloring/adamczewski_2026_erdos74/proposition_2_2|Proposition 2.2]],
uses the recurrence

$$
B(L,0)=0,\qquad B(L,d+1)=L(B(L,d)+1).
$$

Its hypothesis is $h_G(n)<d$ for every $n\le 2B(L,d)$. Its conclusion is
one set of fewer than $d$ edges meeting every odd closed walk of length at
most $L$ in the entire graph. The proof extracts a finite obstruction from
failure of such a transversal. The source's
[[../library/graph_coloring/adamczewski_2026_erdos74/lemma_5_1|Lemma 5.1]]
chooses a slowly growing function specifically to satisfy these thresholds.
The small endpoint sets then enter the distance-band coloring argument of
[[../library/graph_coloring/adamczewski_2026_erdos74/proposition_4_1|Proposition 4.1]].

For $L\ge1$, the recurrence gives $B(L,d)=L+\cdots+L^d\ge Ld$.
Consequently the sufficient numerical test $2CB(L,d)<d$, obtained by
substituting $h_G(n)\le Cn$, is already impossible when $2CL\ge1$.
This comparison alone only defeats that substitution. The following example
shows that improving the recurrence cannot establish the desired global
transversal from a linear budget alone.

## A counterexample to the proposed transfer

Fix $C>0$ and choose an odd integer $\ell\ge3$ with $1/\ell\le C$.
Let $G$ be the disjoint union of $\aleph_1$ copies of $C_\ell$. Then

$$
\chi(G)=3,\qquad h_G(n)=\left\lfloor\frac n\ell\right\rfloor\le Cn.
$$

Indeed, the only nonbipartite components of a finite subgraph are complete
copies of $C_\ell$, each requiring exactly one edge deletion. There are at
most $\lfloor n/\ell\rfloor$ such copies, and that number is attained by
packing whole cycles and padding with vertices from other components.

Every set meeting all odd closed walks of length at most $\ell$ must meet
each component cycle. It therefore has at least $\aleph_1$ edges. In
particular there is no finite, or even countable, global transversal.
The same example works for every $L\ge\ell$.
Finite unions of arbitrarily many copies also rule out any uniform finite
transversal bound depending only on $C$ and $L$.

This example is not a counterexample to Problem 111: its chromatic number is
three. It refutes the intermediate implication that the linear budget alone
supplies a bounded global transversal, which is the premise the direct port
would need. Any successful replacement must exploit additional chromatic
structure or permit distributed repairs. Replacing a finite transversal by
a countable one does not repair this particular implication.

## The limit does follow from a universal finite-density theorem

The following two assertions are equivalent, with both universal
quantifiers over graphs of chromatic number exactly $\aleph_1$:

1. $h_G(n)/n\to\infty$.
2. For every $C>0$, some finite $F\subseteq G$ satisfies
   $\beta(F)>C|V(F)|$.

The first assertion immediately implies the second. For the converse,
assume assertion 2 for every such graph. Fix $G$ and $K>0$. Removing
countably many vertices from $G$ leaves chromatic number $\aleph_1$:
otherwise a countable coloring of the remainder extends to one of $G$ by
assigning fresh colors to the removed vertices.

Recursively for $\xi<\omega_1$, apply assertion 2 with $C=2K$ to the
remainder after the earlier finite witnesses have been removed. This gives
pairwise vertex-disjoint $F_\xi$ with
$\beta(F_\xi)>2K|V(F_\xi)|$. There are only countably many finite graph
types. One type $F$, of order $v$ and defect $b>2Kv$, thus occurs
uncountably often. Packing $\lfloor n/v\rfloor$ copies yields

$$
h_G(n)\ge b\left\lfloor\frac n v\right\rfloor.
$$

For $n\ge2v$ the right side is greater than $Kn$. Cross edges do not
invalidate the bound: every bipartizing deletion set restricts to a
bipartizing deletion set on each copy. Since $K$ was arbitrary, assertion 1
follows.

The use of assertion 2 on every countable-deletion remainder is essential.
A single finite witness, or witnesses in $G$ alone without a replication
argument, does not supply the conclusion. The finite-density formulation
appears in Erdős, *On the combinatorial problems which I would most like
to see solved*, Part VII, p. 16 of the
[[../library/set_systems/erdos_1981_combinatorial_problems_which_i_would_most/_index|held source]].
The equivalence is also explicitly recorded in Section 2 of the
[Erdős Problem a Day report for 111](https://www.erdosproblemaday.com/report/111),
dated 26 July 2026 and accessed 16 October 2026; the argument is supplied
here rather than relying on that report's standing.

Thus excluding graphs with $\chi(G)=\aleph_1$ and $h_G(n)\le Cn$ for all
$n$, for every fixed $C$, would settle the full limit question. No separate
rate of growth or control of the sizes of the finite witnesses is needed.

## Consequence for further work

The direct transfer is closed by the counterexample above. Reopening it
requires a replacement for global bounded transversals, not a better
constant in $B$. One possible replacement would construct a countable
proper coloring from a linear profile bound, at least under the additional
hypothesis $\chi(G)\le\aleph_1$. That assertion remains unproved here.
Composed with the packing argument, it would answer Problem 111.

A discriminating test for such a replacement is whether it handles
uncountably many disjoint short odd cycles without demanding a countable
global hitting set, and still gives a coherent countable coloring. Merely
coloring each finite subgraph countably is vacuous. The finite-palette
compactness used at the end of the E74 proof does not provide compactness
for a countable palette: every finite subgraph of $K_{\aleph_1}$ is
countably colorable, while $K_{\aleph_1}$ is not. This last graph tests
only that compactness inference; it does not satisfy a linear profile bound.

The
[[research/methods/partitioned_vector_energy|partitioned vector-energy test]]
specifies a different finite repair proposal, with the partition chosen
before all subset constraints. Its zero-energy criterion excludes every
four-colorable graph as a counterexample to the binary proposal, while
its complete-join test prevents amplifying dense gadgets without checking
the linear hypothesis. Neither a uniform partition construction nor an
admissible divergent-energy family is supplied there.

The E74 transcription was read through its transversal and coloring chain;
only the transversal mechanism is used in this obstruction. The source
card distinguishes the prose three-color route from the formal project's
primary four-color route, whose proof was not rechecked here. A status
search on 16 October 2026 found no full E111 claim in the inspected catalog,
discussion, erdosproblems.ai, Palomar, or focused arXiv results. That
bounded search and the present author checks confer no acceptance or tier.
