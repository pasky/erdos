---
name: problems/graph_coloring
title: Graph Coloring
desc: |
  Chromatic number of graphs and hypergraphs, list and edge colorings,
  color-critical graphs, and the interaction of coloring with girth and
  cycles; colorings of the plane and of R^n are filed with discrete geometry.
created: 2026-09-04T09:17:27Z
updated: 2026-10-11T23:17:00Z
---

# Graph Coloring

[[problems/_index|..]]

[[problems/graph_coloring/E0019/_index|E0019/]]: Asks whether every
edge-disjoint union of $n$ copies of $K_n$ has chromatic number exactly $n$.

[[problems/graph_coloring/E0057/_index|E0057/]]: Asks whether the reciprocals of
the odd cycle lengths of a graph with infinite chromatic number must sum to
infinity.

[[problems/graph_coloring/E0058/_index|E0058/]]: Asks whether a graph whose odd
cycles have at most $k$ distinct lengths has chromatic number at most $2k+2$,
with equality only if it contains $K_{2k+2}$.

[[problems/graph_coloring/E0063/_index|E0063/]]: Asks whether every graph with
infinite chromatic number contains a cycle of length $2^n$ for infinitely many
$n$.

[[problems/graph_coloring/E0074/_index|E0074/]]: Asks whether, for every
$f(n)\to\infty$, some graph of infinite chromatic number has every $n$-vertex
subgraph made bipartite by deleting at most $f(n)$ edges.

[[problems/graph_coloring/E0075/_index|E0075/]]: Asks whether some graph with
$\aleph_1$ vertices and chromatic number $\aleph_1$ has, for every $\epsilon>0$
and all large $n$, an independent set of size $>n^{1-\epsilon}$ in each
$n$-vertex subgraph, and asks the same for size $\gg n$.

[[problems/graph_coloring/E0108/_index|E0108/]]: Asks whether, for every $r\ge
4$ and $k\ge 2$, large enough chromatic number forces a subgraph of girth $\ge
r$ and chromatic number $\ge k$; disproved at $r=5$ and $k=7$ by a Lean
counterexample family.

[[problems/graph_coloring/E0110/_index|E0110/]]: Asks whether one function
$F(n)$ bounds, for all large $n$, the order of a smallest subgraph of chromatic
number $n$ in every graph of chromatic number $\aleph_1$.

[[problems/graph_coloring/E0625/_index|E0625/]]: Asks whether
$\chi(G)-\zeta(G)\to\infty$ almost surely for the random graph $G(n,1/2)$, where
the cochromatic number $\zeta(G)$ is the fewest colors whose classes each induce
a complete or empty graph.

[[problems/graph_coloring/E0626/_index|E0626/]]: Asks whether, for $k\ge 4$, the
largest girth of an $n$-vertex graph with chromatic number $k$, divided by $\log
n$, tends to a limit.

[[problems/graph_coloring/E0627/_index|E0627/]]: Asks whether $f(n)/(n/(\log_2
n)^2)$ tends to a limit, where $f(n)$ is the largest ratio $\chi(G)/\omega(G)$
of chromatic number to clique number over graphs $G$ on $n$ vertices.

[[problems/graph_coloring/E0628/_index|E0628/]]: Asks whether a graph with
chromatic number $k$ and no $K_k$ must have two disjoint subgraphs of chromatic
numbers $\ge a$ and $\ge b$ whenever $a,b\ge 2$ and $a+b=k+1$.

[[problems/graph_coloring/E0629/_index|E0629/]]: Asks for the least number of
vertices $n(k)$ of a bipartite graph whose list chromatic number exceeds $k$;
open, with $n(2)=6$ and $n(3)=14$ known.

[[problems/graph_coloring/E0630/_index|E0630/]]: Asks whether every planar
bipartite graph has list chromatic number at most $3$. The list chromatic number
is the least list size per vertex that always permits a proper coloring from the
lists.

[[problems/graph_coloring/E0631/_index|E0631/]]: Asks whether every planar graph
has list chromatic number at most $5$, and whether $5$ is best possible. The
list chromatic number is the least list size per vertex that always allows a
proper coloring from the lists.

[[problems/graph_coloring/E0632/_index|E0632/]]: Asks whether every
$(a,b)$-choosable graph is $(am,bm)$-choosable for every integer $m\ge 1$. A
graph is $(a,b)$-choosable if, from any lists of $a$ colors, one can choose $b$
colors per vertex so that adjacent vertices get disjoint sets.

[[problems/graph_coloring/E0640/_index|E0640/]]: Asks whether, for each $k\ge
3$, large enough chromatic number forces an odd cycle whose vertices span a
subgraph of chromatic number at least $k$.

[[problems/graph_coloring/E0706/_index|E0706/]]: Asks for an estimate of $L(r)$,
the largest chromatic number of a graph on finitely many points in
$\mathbb{R}^2$ whose edges join pairs at one of $r$ prescribed distances, and
whether $L(r)\le r^{O(1)}$.

[[problems/graph_coloring/E0736/_index|E0736/]]: Asks whether, for every graph
$G$ of chromatic number $\aleph_1$ and every cardinal $m$, there is a graph of
chromatic number $m$ all of whose finite subgraphs occur in $G$.

[[problems/graph_coloring/E0737/_index|E0737/]]: Asks whether every graph of
chromatic number $\aleph_1$ has an edge that lies on a cycle of every
sufficiently large length.

[[problems/graph_coloring/E0738/_index|E0738/]]: Asks whether every
triangle-free graph of infinite chromatic number contains every tree as an
induced subgraph.

[[problems/graph_coloring/E0739/_index|E0739/]]: Asks whether a graph of
infinite chromatic number $\mathfrak{m}$ must have a subgraph of chromatic
number $\mathfrak{n}$ for every infinite cardinal $\mathfrak{n}<\mathfrak{m}$.

[[problems/graph_coloring/E0740/_index|E0740/]]: Asks whether a graph of
infinite chromatic number $\mathfrak{m}$ must contain a subgraph of the same
chromatic number with no odd cycle of length at most $r$; a claimed disproof is
pending.

[[problems/graph_coloring/E0744/_index|E0744/]]: Asks whether $f_k(n)\to\infty$,
where $f_k(n)$ is the fewest edges whose deletion makes bipartite some
$n$-vertex graph of chromatic number $k$ whose proper subgraphs all have smaller
chromatic number.

[[problems/graph_coloring/E0750/_index|E0750/]]: Asks whether, for every
$f(m)\to\infty$, some graph of infinite chromatic number has an independent set
of size at least $m/2-f(m)$ in every $m$-vertex subgraph.

[[problems/graph_coloring/E0751/_index|E0751/]]: Asks whether the smallest gap
between consecutive cycle lengths in a graph of chromatic number $4$ can be
arbitrarily large, and whether this can happen with large girth.

[[problems/graph_coloring/E0753/_index|E0753/]]: Asks whether some constant
$c>0$ makes the list chromatic numbers of every $n$-vertex graph and its
complement sum to more than $n^{1/2+c}$.

[[problems/graph_coloring/E0758/_index|E0758/]]: Asks for small values of
$z(n)$, the largest cochromatic number of an $n$-vertex graph, and in particular
whether $z(12)=4$. The cochromatic number is the fewest colors whose classes
each induce a complete or an empty graph.

[[problems/graph_coloring/E0759/_index|E0759/]]: Asks for the growth rate of the
largest cochromatic number of a graph embeddable on the orientable surface of
genus $n$. The cochromatic number is the fewest colors whose classes each induce
a complete or an empty graph.

[[problems/graph_coloring/E0760/_index|E0760/]]: Asks whether every graph with
chromatic number $m$ contains a subgraph $H$ with cochromatic number
$\zeta(H)\gg m/\log m$. The cochromatic number is the fewest colors such that
every color class induces a complete graph or an independent set.

[[problems/graph_coloring/E0761/_index|E0761/]]: Asks whether large chromatic
number forces large dichromatic number, and whether large cochromatic number
forces a subgraph of large dichromatic number. Cochromatic classes induce
complete or empty graphs, and dichromatic colorings avoid monochromatic oriented
cycles.

[[problems/graph_coloring/E0762/_index|E0762/]]: Asks whether a $K_5$-free graph
$G$ with cochromatic number $\zeta(G)\geq4$ has chromatic number
$\chi(G)\leq\zeta(G)+2$. Steiner answered no in 2024 with graphs of clique
number $4$, cochromatic number $4$ and chromatic number $7$.

[[problems/graph_coloring/E0780/_index|E0780/]]: Asks whether every $t$-coloring
of the edges of the complete $r$-uniform hypergraph on $n\geq kr+(t-1)(k-1)$
vertices has a color class with $k$ pairwise disjoint edges. Alon, Frankl and
Lovász proved it in 1986, and Lovász had proved the case $k=2$ in 1978.

[[problems/graph_coloring/E0797/_index|E0797/]]: Asks for an estimate of the
largest acyclic chromatic number $f(d)$ of a graph with maximum degree $d$
(proper colorings with no two-colored cycle), in particular whether
$f(d)=o(d^2)$. Alon, McDiarmid and Reed (1991) showed that $f(d)$ has order
$d^{4/3}$ up to a $(\log d)^{1/3}$ factor.

[[problems/graph_coloring/E0799/_index|E0799/]]: Asks whether almost every graph
on $n$ vertices has list chromatic number $o(n)$. Alon proved this in 1992 with
the bound $O(n\log\log n/\log n)$, and Alon, Krivelevich and Sudakov sharpened
it in 1999 to order $n/\log n$.

[[problems/graph_coloring/E0832/_index|E0832/]]: Asks whether, for $r\geq3$ and
large $k$, every $r$-uniform hypergraph with chromatic number $k$ has at least
$\binom{(r-1)(k-1)+1}{r}$ edges, with a defectively worded equality clause.
Alon's counterexamples disprove it, but the case $r=3$ is open.

[[problems/graph_coloring/E0833/_index|E0833/]]: Asks whether there is an
absolute constant $c>0$ such that, for all $r\geq2$, every $r$-uniform
hypergraph with chromatic number $3$ has a vertex in at least $(1+c)^r$ edges.
Erdős and Lovász proved this, and the page records an explicit constant that
works for every $r\geq2$.

[[problems/graph_coloring/E0836/_index|E0836/]]: Asks whether an intersecting
$r$-uniform hypergraph with chromatic number $3$ must have $O(r^2)$ vertices,
and whether two of its edges must meet in $\gg r$ vertices. The answer to the
first is no and the second is open; the page also corrects the site's gloss of
chromatic number $3$.

[[problems/graph_coloring/E0842/_index|E0842/]]: Asks whether $n$ disjoint
triangles joined by a Hamiltonian cycle on their $3n$ vertices always give a
$3$-colorable graph; proved by Fleischner and Stiebitz.

[[problems/graph_coloring/E0917/_index|E0917/]]: Asks whether the largest number
$f_k(n)$ of edges in a $k$-critical graph on $n$ vertices satisfies $f_k(n)\gg_k
n^2$, whether $f_6(n)\sim n^2/4$, and whether a proposed asymptotic holds for
$k\geq6$. The first is proved, the second is open, and the third fails when $k$
is not a multiple of $3$.

[[problems/graph_coloring/E0918/_index|E0918/]]: Asks whether some graph with
$\aleph_2$ vertices and chromatic number $\aleph_2$ has every subgraph on
$\aleph_1$ vertices countably colorable.

[[problems/graph_coloring/E0919/_index|E0919/]]: Asks whether some graph on the
ordinal $\omega_2^2$ has chromatic number $\aleph_2$ while every subgraph of
smaller type is countably colorable, and asks the same with chromatic number
$\aleph_1$.

[[problems/graph_coloring/E0920/_index|E0920/]]: Asks whether, for every
$k\geq4$, the largest chromatic number $f_k(n)$ of a $K_k$-free graph on $n$
vertices satisfies $f_k(n)\gg n^{1-1/(k-1)}/(\log n)^{c_k}$ for some constant
$c_k>0$.

[[problems/graph_coloring/E0921/_index|E0921/]]: Asks whether, for every
$k\geq4$, the largest $m$ such that some $k$-chromatic graph on $n$ vertices has
every odd cycle longer than $m$ is of order $n^{1/(k-2)}$.

[[problems/graph_coloring/E0922/_index|E0922/]]: Asks whether a graph in which
every subgraph on $n$ vertices has an independent set of size at least $(n-k)/2$
has chromatic number at most $k+2$.

[[problems/graph_coloring/E0923/_index|E0923/]]: Asks whether every graph whose
chromatic number is large enough in terms of $k$ contains a triangle-free
subgraph with chromatic number at least $k$.

[[problems/graph_coloring/E0944/_index|E0944/]]: Asks whether, for every
$k\geq4$ and $r\geq1$, some $k$-chromatic graph has every vertex critical but no
critical set of at most $r$ edges. A Lean proof certified by the bounty site
Conjectures.io in September 2026 settles it.

[[problems/graph_coloring/E1013/_index|E1013/]]: Asks for an asymptotic formula
for $h_3(k)$, the fewest vertices of a triangle-free graph with chromatic number
$k$, and for a proof that $h_3(k+1)/h_3(k)\to1$.

[[problems/graph_coloring/E1032/_index|E1032/]]: Asks whether, for arbitrarily
large $n$, some $4$-chromatic critical graph on $n$ vertices has minimum degree
$\gg n$. Such a graph has chromatic number $4$, and deleting any edge drops it
to $3$.

[[problems/graph_coloring/E1091/_index|E1091/]]: Asks whether every $K_4$-free
graph with chromatic number $4$ contains an odd cycle with at least two
diagonals; solved. Erdős first asked for one diagonal, which Larson proved in 1979.

[[problems/graph_coloring/E1092/_index|E1092/]]: Asks whether $f_r(n)\gg_r n$,
in particular for $r=2$, where $f_r$ is the largest function such that a graph
whose every $m$-vertex subgraph is an $r$-colorable graph plus at most $f_r(m)$
edges has chromatic number at most $r+1$.

[[problems/graph_coloring/E1104/_index|E1104/]]: Asks for an estimate of the
largest chromatic number of a triangle-free graph on $n$ vertices.

[[problems/graph_coloring/E1156/_index|E1156/]]: Asks whether the chromatic
number of a random graph on $n$ vertices, each edge present independently with
probability $1/2$, is almost surely concentrated on boundedly many values, and
whether it is within a slowly growing $\omega(n)$ of any given $f(n)$ with
probability below $1/2$.

***

Chromatic number of graphs and hypergraphs, list and edge colorings,
color-critical graphs, and the interaction of coloring with girth and cycles;
colorings of the plane and of R^n are filed with discrete geometry.

Site tags routed here: chromatic number, combinatorics, cycles, graph theory,
hypergraphs.
