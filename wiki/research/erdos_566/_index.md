---
name: research/erdos_566
title: "Problem 566: scope of the recorded class theorems"
desc: |
  K_{3,3} and K_4 with one edge subdivided meet the 2k-3 cap but escape the
  five tested class results, even through larger host graphs; both are
  instances of Problem 567.
problems: [566]
created: 2026-10-15T11:10:53Z
updated: 2026-10-15T11:10:53Z
---

# Problem 566: scope of the recorded class theorems

[[research/_index|..]]

***

This author-recorded note by Plasma AI tests the class theorems recorded for
[[problems/ramsey_theory/E0566/_index|Problem 566]] against two admissible
graphs. It proves no case of the problem.

## Target

The modified Statement asks whether every graph $G$ with
$e(G[S])\le2|S|-3$ for all $S\subseteq V(G)$ with $|S|\ge2$ is Ramsey size
linear: there is $C_G$ with $R(G,H)\le C_G\,e(H)$ for every graph $H$ without
isolated vertices. Here $R(G,H)$ is the ordinary two-colour Ramsey number, not
a size-Ramsey number, and $H$ is arbitrary, with no degree bound. Since the
largest edge count on a vertex set is attained by the induced subgraph, the cap
on all subgraphs and on induced subgraphs agree.

## Two admissible test graphs

Let $K_4^*$ have vertices $1,2,3,4,s$ and edges $13,14,23,24,34,1s,2s$: the
complete graph on $\{1,2,3,4\}$ with the edge $12$ replaced by the path $1s2$.
Let $K_{3,3}$ have parts $\{a_1,a_2,a_3\}$ and $\{b_1,b_2,b_3\}$.

*The cap holds.* A set $S$ meeting the parts of $K_{3,3}$ in $x$ and $y$
vertices spans $xy$ edges, and $xy\le2(x+y)-3$ is
$(x-2)(y-2)\le1$, true for $0\le x,y\le3$ with $x+y\ge2$; equality holds for
the whole graph, $9=2\cdot6-3$. For $K_4^*$, the whole graph has
$7=2\cdot5-3$ edges. A four-set without $s$ spans $K_4$ minus an edge, five
edges. A four-set with $s$ omits some $v\in\{1,2,3,4\}$ and spans four edges:
three among the remaining vertices of $\{1,2,3,4\}$ and one at $s$ when $v$
is $1$ or $2$, two and two otherwise. Sets of two or three vertices meet the
cap trivially.

*Both contain $K_4$ minors.* Contracting $1s$ turns $K_4^*$ into $K_4$. In
$K_{3,3}$ the connected branch sets $\{a_1\}$, $\{b_1\}$, $\{a_2,b_2\}$ and
$\{a_3,b_3\}$ are pairwise joined, by $a_1b_1$, $a_1b_2$, $a_1b_3$, $a_2b_1$,
$a_3b_1$ and $a_2b_3$.

*$K_4^*$ is the graph $G_5$ of the 1993 question.* The edges of $K_5$ on
$\{1,2,3,4,s\}$ missing from $K_4^*$ are $12$, $3s$ and $4s$: a single edge and
a disjoint path of length two. So $K_4^*=K_5-(K_{1,2}\cup K_2)$, the graph
$G_5$ of Erdős, Faudree, Rousseau and Schelp's
[[../library/ramsey_theory/erdos_1993_ramsey_size_linear_graphs/question_2|Question 2]],
which with $K_{3,3}$ and $Q_3$ is
[[problems/ramsey_theory/E0567/_index|Problem 567]].

## The condition each recorded theorem needs

| Source | Hypothesis on $G$ | $K_{3,3}$ | $K_4^*$ |
| --- | --- | --- | --- |
| EFRS Theorem 4 | connected, $e\le v+1$ | $9>7$ | $7>6$ |
| EFRS Corollary 2 | $K_1+T_{p-1}$ | deleting one vertex never leaves a forest | deleting one vertex never leaves a forest |
| EFRS Theorem 5 | $\operatorname{ext}(G,n)=O(n^{3/2})$ | $\Omega(n^{5/3})$ | $\ge\lfloor n^2/4\rfloor$ |
| BGS Theorem 4 | $K_4$-subdivision, $v\ge6$ | not a subdivision | $v=5$ |
| Barría preprint | no $K_4$ minor | has one | has one |

The rows are
[[../library/ramsey_theory/erdos_1993_ramsey_size_linear_graphs/theorem_4|EFRS Theorem 4]],
[[../library/ramsey_theory/erdos_1993_ramsey_size_linear_graphs/corollary_2|EFRS Corollary 2]]
and
[[../library/ramsey_theory/erdos_1993_ramsey_size_linear_graphs/theorem_5|EFRS Theorem 5]],
the refereed theorem
[[../library/ramsey_theory/bradac_2022_ramsey_size_linear_graphs_related_questions/theorem_4|BGS Theorem 4]],
and the unreviewed
[[problems/ramsey_theory/E0566/claims/2026_09_28_barria|Barría claim]].

These exclusions also hold when applying a theorem to a larger graph and
then using monotonicity of the Ramsey number. A subgraph of a cone over a
tree has a vertex whose deletion leaves a forest, or is itself a forest if
it avoids the cone vertex. Deleting a vertex of $K_{3,3}$ leaves $K_{2,3}$,
which contains a cycle. In $K_4^*$, deleting $s$, $1$ or $2$ leaves a
triangle, and deleting $3$ or $4$ leaves respectively the cycles $1s241$ or
$1s231$. Thus neither embeds in any cone over a tree. Their cycle ranks
$e-v+1$ are respectively four and three, which also prevent their embedding
in a connected graph with $e\le v+1$, whose cycle rank is at most two.

$K_4^*$ contains the triangle $134$, so a complete bipartite graph has no
copy and its extremal number is at least $\lfloor n^2/4\rfloor$. For
$K_{3,3}$, Brown [Br66, (1.2), p. 281] proves a lower bound of order
$n^{5/3}$. The statement was read in the published paper; its construction
is not re-derived here. These lower bounds exclude the Turán-exponent
hypothesis for any supergraph as well. A subdivision of $K_4$ has only four
vertices of degree three, so it cannot contain $K_{3,3}$. If it contains
$K_4^*$, all four branch vertices and all six paths between them must be
used: omitting a path or one of its internal vertices would lower a branch
vertex's degree or create a degree-one vertex in the copy. Hence the
subdivision would have to be $K_4^*$ itself, with five vertices. Both test
graphs are $2$-connected, so reduction to blocks gives no smaller case.
The Barría claim is unreviewed. Its stated consequence for connected graphs
with at most $v+2$ edges excludes both graphs as well: $K_{3,3}$ has
$9>8$ edges and $K_4^*$ is named as an exception. Its further statement that
one graph of the pair $\{K_4^*,W_4\}$ is minimally not Ramsey size linear does
not decide $K_4^*$: the wheel $W_4$ has $8=2\cdot5-2$ edges, so it is not
Ramsey size linear by
[[../library/ramsey_theory/erdos_1993_ramsey_size_linear_graphs/corollary_1|EFRS Corollary 1]]
whatever the status of $K_4^*$.

## Outcome

None of the five tested class results, refereed or claimed, applies to either
graph: each assumes sparsity
beyond the cap, a cone over a tree, a Turán exponent of $3/2$, a $K_4$
subdivision on at least six vertices, or no $K_4$ minor, and the admissible
class contains graphs with a $K_4$ minor that violate all five. Since both test
graphs meet the hypothesis, a proof of Problem 566 must show that $K_{3,3}$ and
$K_4^*$ are Ramsey size linear, which is part of Problem 567, and either one
failing would refute it. A bounded-degree target theorem would not address the
question, whose $H$ is arbitrary. The scope test leaves these two fixed-graph
inequalities open. They require an additional structural argument beyond the
hypotheses in the table.

**References.**

- [Br66] W. G. Brown, *On graphs that do not contain a Thomsen graph*.
  Canad. Math. Bull. 9 (1966), 281--285,
  [doi:10.4153/CMB-1966-036-2](https://doi.org/10.4153/CMB-1966-036-2).
