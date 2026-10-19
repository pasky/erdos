# Frozen mathematical extraction

[cut]

## Target and conventions

All graphs are simple. For a finite graph $F$, $\beta(F)$ is the least number
of edges whose deletion leaves $F$ bipartite. Deleting vertices or edges never
increases $\beta$. For an infinite graph $G$ and $n\ge1$,

$$
h_G(n)=\max\{\beta(F):F\subseteq G,\ |V(F)|=n\},
$$

which is the least bound in the statement of Problem 111; the maximum exists
because $\beta(F)\le\binom n2$. Problem 111 asks whether $h_G(n)/n\to\infty$
for every graph $G$ with $\chi(G)=\aleph_1$. The vertex set of $G$ may have
any cardinality. A positive answer needs the whole limit for every such $G$,
not an unbounded subsequence or a positive linear coefficient. A negative
answer needs one graph of chromatic number exactly $\aleph_1$ for which the
limit fails. Graphs of finite or countable chromatic number are not instances
of the problem.

For $C\ge0$, call a graph $G$ **$C$-linear** if $\beta(F)\le C|V(F)|$ for
every finite subgraph $F$ of $G$. A $C$-linear graph has $h_G(n)\le Cn$ for
every $n$.

## The editable proof sketch

### Step 1. Countable deletion [cut]

If $\chi(G)=\aleph_1$ and $S\subseteq V(G)$ is countable, then
$\chi(G-S)=\aleph_1$. Indeed $\chi(G-S)\le\aleph_1$, and a coloring of $G-S$
by natural numbers would extend to $G$ by giving the points of $S$ distinct
new colors, so $\chi(G)\le\aleph_0$.

### Step 2. Packing [cut]

Let $K>0$. Suppose $G$ contains infinitely many pairwise vertex-disjoint
copies of one finite graph $F_0$ with $v$ vertices and $\beta(F_0)=b>2Kv$.
Then

$$
h_G(n)\ge b\left\lfloor\frac nv\right\rfloor>Kn\qquad(n\ge2v).
$$

Take $q=\lfloor n/v\rfloor$ of the copies and $n-qv$ further vertices, and let
$H$ be the subgraph they induce. If $H-D$ is bipartite, then $D$ restricted to
each copy bipartizes that copy, so $D$ has at least $b$ edges in each of the
$q$ copies, whatever edges run between copies. Thus $\beta(H)\ge qb$, and
$qb\ge(b/v)(n-v)>2K(n-v)\ge Kn$ for $n\ge2v$. A family of $\aleph_1$ pairwise
vertex-disjoint finite subgraphs $F$ with $\beta(F)>2K|V(F)|$ meets the
hypothesis, since there are only countably many isomorphism types of finite
graphs.

### Step 3. Equivalence with the countable-coloring lemma [cut]

**Lemma CC [cut].** For every $C\ge0$, every $C$-linear graph $G$ with
$\chi(G)\le\aleph_1$ satisfies $\chi(G)\le\aleph_0$.

**Claim.** Problem 111 has a positive answer if and only if Lemma CC holds.
Moreover, if $G$ has $\chi(G)=\aleph_1$ and $h_G(n)\le Kn$ for infinitely
many $n$, then some countable $S\subseteq V(G)$ makes $G-S$ a $2K$-linear
graph with $\chi(G-S)=\aleph_1$.

*Lemma CC gives the limit.* Let $\chi(G)=\aleph_1$ and $K>0$. Recursively for
$\xi<\omega_1$, the union $S_\xi$ of the vertex sets already chosen is
countable, so $\chi(G-S_\xi)=\aleph_1$ by Step 1, and by Lemma CC the graph
$G-S_\xi$ is not $2K$-linear: choose a finite $F_\xi\subseteq G-S_\xi$ with
$\beta(F_\xi)>2K|V(F_\xi)|$. Step 2 gives $h_G(n)>Kn$ for all large $n$. As
$K$ was arbitrary, $h_G(n)/n\to\infty$.

*A failure of the limit gives a linear remainder.* Let $\chi(G)=\aleph_1$ and
$h_G(n)\le Kn$ for infinitely many $n$. Take a maximal family of pairwise
vertex-disjoint finite subgraphs $F$ with $\beta(F)>2K|V(F)|$. If it were
uncountable, Step 2 would give $h_G(n)>Kn$ for every large $n$. So its vertex
union $S$ is countable. By maximality every finite subgraph of $G-S$ has
$\beta(F)\le2K|V(F)|$, and $\chi(G-S)=\aleph_1$ by Step 1. A $C$-linear graph
of chromatic number $\aleph_1$ conversely has $h_G(n)\le Cn$ for every $n$,
so Lemma CC fails exactly when Problem 111 has a negative answer.

The use of Lemma CC on every countable-deletion remainder matters: one
finite witness in $G$, or witnesses that cannot be replicated disjointly,
give no lower bound on the limit. No control of the size of the witnesses
as $C$ varies is needed. The finite-density form of the question, that every
$C$ admits a finite $F$ with $\beta(F)>C|V(F)|$, is the form asked in Part VII
of
[[../library/set_systems/erdos_1981_combinatorial_problems_which_i_would_most/_index|Erdős's 1981 survey]].
[cut]


[cut]

### Barely superlinear budgets allow chromatic number $\aleph_1$

**Proposition B [cut].** For every nondecreasing unbounded
$g:\mathbb N\to\mathbb N$ there is a graph $G$ with $|V(G)|=2^{\aleph_1}$,
$\chi(G)=\aleph_1$ and

$$
h_G(n)\le(n-1)\,g(n)\qquad(n\ge1).
$$

Under $\diamondsuit$ there is such a graph with $|V(G)|=\aleph_1$, a
Hajnal–Máté graph.

Put $f(k)=\max(\{0\}\cup\{m\ge1:g(m)\le k\})$, which is finite because $g$ is
nondecreasing and unbounded. For this $f$, the proof of
[[../library/graph_coloring/lambiehanson_2020_growth_rate_chromatic_numbers_finite_subgraphs/theorem_a|Lambie-Hanson's Theorem A]]
builds a graph $G$ with $|V(G)|=2^{\aleph_1}$ and $\chi(G)=\aleph_1$ whose
edges carry labels in $\mathbb N$ such that, by its Claim 4.1 (p. 7):

- for each $k$, the edges labelled $k$ form a forest, because every vertex has
  at most one lower neighbour with a given label;
- for each $k$, the edges labelled at least $k$ form a graph with no odd cycle
  of length at most $f(k)$, because they map homomorphically into a Specker
  graph of large odd girth.

Let $F\subseteq G$ have $n$ vertices and put $k=g(n)$, so $n\le f(k)$. Every
cycle in $F$ has length at most $n$, so the edges of $F$ labelled at least
$k$ form a bipartite graph. The edges of $F$ with labels below $k$ form $k$
forests on $n$ vertices, at most $k(n-1)$ edges, and deleting them leaves $F$
bipartite. Hence $\beta(F)\le(n-1)g(n)$. Under $\diamondsuit$ the graph of
[[../library/graph_coloring/lambiehanson_2020_growth_rate_chromatic_numbers_finite_subgraphs/theorem_b|Theorem B]]
has the same two properties, whose verification the paper says is as for
Theorem A.

Consequences: [cut]

- **Erdős's 1981 conjecture on the upper bound holds.** After the passage
  posing the finite-density question, Part VII of
  [[../library/set_systems/erdos_1981_combinatorial_problems_which_i_would_most/_index|Erdős's 1981 survey]]
  states the belief that for every $\varepsilon>0$ some graph of chromatic
  number $\aleph_1$ has every $m$-vertex subgraph bipartite after fewer than
  $m^{1+\varepsilon}$ edge deletions. [cut] Proposition B with
  $g(m)=\lfloor m^\varepsilon\rfloor$ gives
  $h_G(m)\le(m-1)\lfloor m^\varepsilon\rfloor<m^{1+\varepsilon}$ for every
  $m\ge1$, the 1981 wording, and with $g(n)=\lceil\log_2(n+1)\rceil$ one graph
  has $h_G(n)\ll n^{1+\varepsilon}$ for every $\varepsilon>0$ at once. This
  is a ZFC statement about graphs of size $2^{\aleph_1}$, and of size
  $\aleph_1$ under $\diamondsuit$. It answers neither the limit question nor
  whether $h_G(n)/n$ is unbounded for these graphs. [cut]
- **No uniform rate.** For every $r(n)\to\infty$ there is a graph of
  chromatic number $\aleph_1$ with $h_G(n)<n\,r(n)$ for all large $n$: apply
  Proposition B to $g(n)=\max(1,\min_{m\ge n}\lfloor r(m)\rfloor)$. If
  Problem 111 has a positive answer, the divergence of $h_G(n)/n$ has no rate
  common to all graphs of chromatic number $\aleph_1$.
- **Lemma CC is sharp at the linear scale.** With $C|V(F)|$ replaced by
  $|V(F)|\,g(|V(F)|)$ for any integer-valued $g\to\infty$, the lemma is
  false: apply Proposition B to the nondecreasing minorant
  $\min_{m\ge n}g(m)$. A proof must
  use that $\beta(F)/|V(F)|$ is bounded, not only that $h_G$ is subquadratic
  or $n^{1+o(1)}$.
- **Blow-ups are not obligatory.** For a finite graph $H$ let $H[s]$ replace
  each vertex by $s$ independent copies and each edge by $K_{s,s}$. If $H$
  contains an odd cycle $C_\ell$, then $\beta(H[s])\ge s^2$: the $s^\ell$
  cycles of $C_\ell[s]$ that take one vertex from each class each get weight
  $s^{2-\ell}$, every edge lies on exactly $s^{\ell-2}$ of them, and a
  bipartizing edge set meets every odd cycle. With
  $g(n)=\lceil\log_2(n+1)\rceil$, the graph of Proposition B contains $H[s]$
  only if $s^2\le s|V(H)|\,g(s|V(H)|)$, which fails for large $s$. So one
  graph of chromatic number $\aleph_1$ contains $H[s]$ for only finitely many
  positive integers $s$, for each non-bipartite $H$. Obligatory blow-ups
  would have proved Problem 111
  through Steps 1 to 3, since $\beta(H[s])/|V(H[s])|\ge s/|V(H)|$ and every
  countable-deletion remainder again has chromatic number $\aleph_1$.
- **Every scale keeps chromatic number $\aleph_1$.** In the graph of
  Proposition B the edges labelled below $k$ form $k$ forests, of chromatic
  number at most $2^k$ together, so by taking products of colorings the edges
  labelled at least $k$ still form a graph of chromatic number $\aleph_1$.
  The bipartite behaviour of small subgraphs is a finite-scale effect only.

[cut]
