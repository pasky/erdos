[cut]

# Countable Colorings from Linear Bipartization Budgets

[cut]

[cut]

The page keeps one editable proof sketch. Steps 1 to 3 below are [cut] arguments that reduce Problem 111 to a countable-coloring lemma, which
is equivalent to it. Step 4 lists equivalent coloring constructions that
the reduction does not supply; Step 5 records a [cut] candidate
proof of the lemma. The later sections
show that the lemma is sharp at both ends and record obstructions to specific
transversal and vector repairs. A hereditary vector-energy bound does give a
countable coloring, without a separability assumption, but the linear profile
alone does not give that bound. A finite partition before the vector repair is
an open alternative. Its known lower-bound mechanism needs a sharp gate, and
Proposition E shows that finite colorings forbidding monochromatic complete
bipartite subgraphs cannot replace the vectors. The
[[research/leads/linear_bipartization_countable_coloring/rooted_cut_measures|rooted extension measure]]
controls all abundantly realized finite patterns at once. It does not
identify a vertex's coordinate with the opposite of its derived trace sign;
correcting the measure layer by layer gives the candidate proof of Step 5.
A proposed negative route
through sparse ladder systems needs more than separated predecessor
intervals: the
[[research/leads/linear_bipartization_countable_coloring/sparse_ladder_profiles|Hadamard family]]
refutes a uniform linear bound from that finite condition alone.
A by-product, Proposition B,
reads off from Lambie-Hanson's construction a graph of chromatic number
$\aleph_1$ with $h_G(n)\le(n-1)g(n)$ for any prescribed nonnegative
integer-valued $g\to\infty$; this
confirms, in ZFC, Erdős's 1981 conjecture that some such graph has
$h_G(n)\ll n^{1+\varepsilon}$ for every $\varepsilon>0$, and shows that a
positive answer to Problem 111 could have no rate.

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
The same equivalence is stated in Section 2 of the Erdős Problem a Day report
on Problem 111 (<https://www.erdosproblemaday.com/report/111>, dated 26 July
2026, accessed 16 October 2026); the argument above does not rely on it.

### Step 4. The open step

Lemma CC is equivalent to the target, so the reduction relocates the
difficulty rather than reducing it. For a graph $G$ with
$\chi(G)\le\aleph_1$, each of the following is equivalent to
$\chi(G)\le\aleph_0$, and a proof of Lemma CC must construct one of them from
the linear count.

- **Locally finite repair layers.** Edge sets $R_0,R_1,\ldots$ such that $G$
  minus their union is bipartite, each graph $(V,R_i)$ has countable
  chromatic number, and every vertex meets edges of only finitely many $R_i$.
  Given them, color $v$ by its side in a 2-coloring of the bipartite
  remainder together with the finite list of pairs consisting of a layer
  index and its color in a fixed countable coloring of that layer, for the
  layers it meets; the palette is countable and the coloring is proper.
  Conversely, from a coloring $c:V\to\mathbb N$ take $R_i$ to be
  the edges whose smaller endpoint color is $i$; each $R_i$ is bipartite and a
  vertex of color $m$ meets only $R_0,\ldots,R_m$.
- **A recursion with finitely many changes.** Fix independent sets $I_\xi$
  ($\xi<\omega_1$) covering $V$ and put $V_\alpha=\bigcup_{\xi<\alpha}I_\xi$.
  Proper colorings $c_\alpha:V_\alpha\to\mathbb N$ in which every vertex
  changes color only finitely often as $\alpha$ increases, with $c_\lambda$ the
  pointwise limit at limit stages, have a proper limit coloring of $G$; the
  restrictions of a countable coloring are such a recursion. The obligation
  sits at successor stages: adding the independent set $I_\alpha$ may force
  recoloring of old vertices, and no vertex may be forced to change infinitely
  often.

### Step 5. A candidate proof of Lemma CC [cut]

The
[[research/leads/linear_bipartization_countable_coloring/layered_rooted_measures|layered measure note]]
gives an argument that every $C$-linear graph has countable chromatic
number, with no hypothesis on its chromatic number or cardinality. It
inducts on the number of vertices along a continuous chain of elementary
submodels. Along the chain it corrects the rooted extension measure layer
by layer until every vertex with infinite trace carries the opposite of
its countably determined trace sign, with expected trace defect at most
$C$. Proposition C's classes and countable coloring number across layers give the
coloring. The links it uses are Lemma F, the rooted measure, Proposition
C, standard measure theory and minimax, and the induction hypothesis; the
section "Layered correction of the rooted measure" below summarizes it.
[cut]

### How the steps compose

[cut] With Lemma CC they give the full
limit; [cut] If the candidate proof of Step 5 [cut], Steps 1 to 3 and Step 5
compose to the positive answer: $h_G(n)/n\to\infty$ for every graph with
$\chi(G)=\aleph_1$, of any cardinality. [cut] Step 5's local inputs are the rooted-measure
proposition, the elementary replication argument and the countable
Hilbert-space partition in Proposition C. The alternative coloring routes
and the profile constructions below are not its premises.

The partitioned vector replacement below gives a more concrete sufficient
lemma: select one binary vertex partition in every finite $C$-linear graph
so that its two induced graphs admit compatible unit-vector repairs with a
uniform energy coefficient. Compactness for the binary labels and Gram
matrices, followed by Proposition C, supplies the coherent countable coloring.
The unresolved finite step is to obtain those repairs. Requiring a single
repair on the whole finite graph is false, by Proposition D below.

A second, infinitary line uses no vectors. For graphs of size $\aleph_1$,
Lemma G below colors with countably many colors every vertex with few
earlier neighbours along an elementary chain. It also colors properly,
inside each class, the remaining vertices grouped by a finite set of
earlier neighbours. A countable coloring then needs only control of the
edges between different classes, and Lemma F restricts how such classes can
attach to earlier structure. This finite-root-class argument by itself
supplies neither that control nor the larger-cardinality case. Step 5 instead uses a rooted
probability measure with consistent marginals along the chain. Neither
(PV) nor the finite-root-class proposal is asserted to be equivalent to CC.

## What a linear budget can and cannot force

### Linear budgets allow chromatic number $\aleph_0$

**Proposition A [cut].** For every $C>0$ there is a countable
$C$-linear graph $U_C$ with $\chi(U_C)=\aleph_0$.

This conclusion is already attributed to Rödl's 1982 theorem in
[[problems/graph_coloring/E0074/claims/1982_12_01_rodl|the Problem 74 record]],
[cut] The following direct Borsuk-net argument supplies the needed
instance here; the conclusion is not claimed as new.

For $r\ge2$ and $0<\varepsilon\le1$, let $N\subseteq S^{r-1}\subseteq\mathbb
R^r$ be a maximal set of unit vectors at pairwise Euclidean distance at least
$\varepsilon/3$; it is finite. Join distinct $p,q\in N$ when
$|p+q|<\varepsilon$, and call the graph $N_{r,\varepsilon}$.

1. *$\chi(N_{r,\varepsilon})\ge r+1$.* By maximality every point of the
   sphere is within distance $\varepsilon/3$ of $N$. Given a coloring
   $c:N\to\{1,\ldots,r\}$, let $A_i$ be the union of the closed caps of
   radius $\varepsilon/3$ about the points of color $i$. These $r$ closed sets
   cover the sphere, so by the Lyusternik–Schnirelmann theorem some $A_i$
   contains a pair $x,-x$. Then there are $p,q$ of color $i$ with
   $|p+q|\le|p-x|+|x+q|\le2\varepsilon/3<\varepsilon$, and $p\ne q$ since
   $|2p|=2$. So $c$ is not proper.
2. *Every vertex has at most $7^r$ neighbours.* The neighbours of $p$ lie in
   the ball of radius $\varepsilon$ about $-p$; the balls of radius
   $\varepsilon/6$ about them are disjoint and lie in the ball of radius
   $7\varepsilon/6$ about $-p$.
3. *$\beta(F)\le\frac\varepsilon4 7^r|V(F)|$ for every subgraph $F$.* If
   $|p+q|<\varepsilon$, the angle between $p$ and $q$ is $\pi-\varphi$ with
   $\sin(\varphi/2)=|p+q|/2<\varepsilon/2$, so $\varphi<\pi\varepsilon/2$. A
   uniformly random hyperplane through the origin leaves two unit vectors at
   angle $\theta$ on the same side with probability $1-\theta/\pi$, here
   below $\varepsilon/2$. Coloring each vertex by its side therefore leaves at
   most $\frac\varepsilon2|E(F)|\le\frac\varepsilon4 7^r|V(F)|$
   monochromatic edges in expectation, and some hyperplane does at least as
   well.

Take $\varepsilon_r=\min(1,4C\cdot7^{-r})$ and let $U_C$ be the disjoint union
of the graphs $N_{r,\varepsilon_r}$ for $r\ge2$. Since $\beta$ adds over
components, $U_C$ is $C$-linear; it is countable, and its finite components
have chromatic numbers at least $r+1$ for every $r$, so
$\chi(U_C)=\aleph_0$.

So a linear budget, with any constant, bounds no finite chromatic number:
Lemma CC cannot conclude a finite bound, and any argument that would produce a
finite coloring proves something false. This includes finite-palette
compactness as used at the end of the
[[problems/graph_coloring/E0074/claims/2026_09_03_adamczewski|Problem 74 disproof]],
whose budgets grow slowly, and the bounded transversals discussed below.

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

Consequences [cut]:

- **Erdős's 1981 conjecture on the upper bound holds.** After the passage
  posing the finite-density question, Part VII of
  [[../library/set_systems/erdos_1981_combinatorial_problems_which_i_would_most/_index|Erdős's 1981 survey]]
  states the belief that for every $\varepsilon>0$ some graph of chromatic
  number $\aleph_1$ has every $m$-vertex subgraph bipartite after fewer than
  $m^{1+\varepsilon}$ edge deletions; the remarks on
  [erdosproblems.com/111](https://www.erdosproblems.com/111) (accessed
  2026-10-16) record it as Erdős's conjecture that the
  Erdős–Hajnal–Szemerédi bound $h_G(n)\ll n^{3/2}$ can be improved to
  $\ll n^{1+\varepsilon}$ for every $\varepsilon>0$. Proposition B with
  $g(m)=\lfloor m^\varepsilon\rfloor$ gives
  $h_G(m)\le(m-1)\lfloor m^\varepsilon\rfloor<m^{1+\varepsilon}$ for every
  $m\ge1$, the 1981 wording, and with $g(n)=\lceil\log_2(n+1)\rceil$ one graph
  has $h_G(n)\ll n^{1+\varepsilon}$ for every $\varepsilon>0$ at once. This
  is a ZFC statement about graphs of size $2^{\aleph_1}$, and of size
  $\aleph_1$ under $\diamondsuit$. It answers neither the limit question nor
  whether $h_G(n)/n$ is unbounded for these graphs. The Erdős Problem a Day
  report cited above claims that the ordered 2-shift witness of Erdős,
  Hajnal and Szemerédi has profile of order $n^{3/2}$; that argument and
  its computation are not used here. Proposition B uses a different graph.
- **No uniform rate.** For every $r(n)\to\infty$ there is a graph of
  chromatic number $\aleph_1$ with $h_G(n)<n\,r(n)$ for all large $n$: apply
  Proposition B to $g(n)=\max(1,\min_{m\ge n}\lfloor r(m)\rfloor)$. If
  Problem 111 has a positive answer, the divergence of $h_G(n)/n$ has no rate
  common to all graphs of chromatic number $\aleph_1$.
- **Lemma CC is sharp at the linear scale.** With $C|V(F)|$ replaced by
  $|V(F)|\,g(|V(F)|)$ for any nonnegative integer-valued $g\to\infty$, the lemma is
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

Propositions A and B place Problem 111 exactly at the linear scale: linear
budgets allow countable chromatic number, and every superlinear budget of the
form $n\,g(n)$, with $g$ nonnegative, integer-valued and tending to infinity,
allows chromatic number $\aleph_1$.

## The transversal step and its distributed replacement

The slow-budget proof of Problem 74 starts from
[[../library/graph_coloring/adamczewski_2026_erdos74/proposition_2_2|Proposition 2.2]]
of the preliminary exposition: if $h_G(n)<d$ for every $n\le2B(L,d)$, where
$B(L,0)=0$ and $B(L,d+1)=L(B(L,d)+1)$, then one set of fewer than $d$ edges
meets every odd closed walk of length at most $L$ in the whole graph. Its
coloring chain,
[[../library/graph_coloring/adamczewski_2026_erdos74/proposition_4_1|Proposition 4.1]],
uses the finite endpoint sets of these transversals to bound component
diameters and to find a free four-level band, and finite-palette compactness
ends the proof. The source card distinguishes this preliminary three-color
prose route from the primary four-color formal route; only the prose
mechanism is described here.

**No global transversal.** Let $\ell\ge3$ be odd with $1/\ell\le C$ and let
$G$ be the disjoint union of $\aleph_1$ copies of $C_\ell$. A finite subgraph
needs one deletion for each whole copy it contains and none otherwise, so
$h_G(n)=\lfloor n/\ell\rfloor$ and $G$ is $C$-linear, with $\chi(G)=3$. Every
edge set meeting all odd cycles of length at most $\ell$ meets every copy and
so has $\aleph_1$ edges. A linear budget therefore gives no finite, or even
countable, global transversal.

**The distributed replacement.** The natural repair lets transversals spread
over uncountably many places. *Candidate R:* for every $C$ and odd $L$ there
is $d(C,L)$ such that every $C$-linear graph has an edge set $T_L$ meeting
every odd cycle of length at most $L$, of arboricity at most $d(C,L)$ (every
finite subgraph of $(V,T_L)$ on $m$ vertices has at most $d(C,L)(m-1)$
edges). Combined with a coloring step, it was meant to give a countable
coloring. Two different limitations must be distinguished.

1. *With $d$ independent of $L$, candidate R is false.* Enlarge $d$ to a
   positive integer if necessary. Take a nonprincipal
   ultrafilter on the odd $L$ and let $T$ contain the edges lying in
   ultrafilter-many $T_L$. A finite edge set meets $T$ as it meets
   ultrafilter-many $T_L$, so every finite subgraph of $(V,T)$ has arboricity
   at most $d$, and every odd cycle meets $T$. Thus $G-T$ is bipartite and,
   since a graph of arboricity at most $d$ has every finite subgraph with a
   vertex of degree below $2d$, the de Bruijn–Erdős theorem gives
   $\chi(V,T)\le2d$ and $\chi(G)\le4d$. The graph $U_C$ of Proposition A is
   $C$-linear with $\chi(U_C)=\aleph_0$, a contradiction.
2. *With $d$ growing in $L$, the transversals are not enough.* In the graph of
   Proposition B the edges labelled below $k$, for any $k$ with $f(k)\ge L$,
   form such a $T_L$: nested in $L$, a union of $k$ forests, with $G-T_L$ free
   of odd cycles of length at most $L$. Yet $\chi(G)=\aleph_1$. Whether
   candidate R holds for $C$-linear graphs is not decided here; what fails is
   the passage from such transversal families to a countable coloring.

The uniform-in-$L$ version is refuted. The growing-in-$L$ version needs an
additional use of the linear bound: the graph witnessing insufficiency of
the transversal families is not asserted to be $C$-linear. Neither argument
obstructs all uses of distributed transversals in Lemma CC. To finish, one
could supply locally finite repair layers, every vertex meeting only finitely
many of them, which by Step 4 is equivalent to the whole conclusion; the graph
of Proposition B has no such layers.

## Coherence tests

Three small examples constrain any invariant for the recursion of Step 4.

- **Precoloring extension fails at zero defect.** In the countable star, the
  leaves colored $0,1,2,\ldots$ form a proper coloring of an independent set
  that does not extend to the centre within $\mathbb N$. An invariant must
  restrict boundary colorings, reserve colors, or allow controlled
  recoloring.
- **A 2-coloring cannot keep defects locally countable.** The graph
  $K_{1,\aleph_1,\aleph_1}$ has apex $z$ and parts $A,B$, with $\chi=3$ and
  $h(n)=\lfloor(n-1)/2\rfloor$; it is $\frac12$-linear. Suppose a 2-coloring
  gave every vertex only countably many neighbours of its own color. One
  part, say $A$, has uncountably many vertices of some color $i$; then $B$
  has no vertex of color $i$, so $B$ is uncountable of color $1-i$ and $A$ has
  no vertex of color $1-i$. The apex then has uncountably many neighbours of
  its own color whichever color it takes. Ordered defects do survive: with
  $A$ colored $0$, $B$ and the apex colored $1$, and the apex first in a
  well-order, every vertex has at most one earlier neighbour of its own
  color.
- **Ordered defects fail outside the linear class.** In
  $K_{\aleph_1,\aleph_1,\aleph_1}$ every 2-coloring makes some two parts
  share a color on uncountable sets $W_1,W_2$. In any well-order, whichever
  of $W_1,W_2$ meets the first $\omega$ elements of $W_1\cup W_2$
  infinitely often gives the first later element of the other set
  infinitely many earlier neighbours of its own color. This graph is not
  $C$-linear for any $C$: the triangles $\{a_i,b_j,c_{i+j\bmod m}\}$ of
  $K_{m,m,m}$ are $m^2$ edge-disjoint odd cycles on $3m$ vertices.

These examples suggest a structural form of Lemma CC that compactness does not
give.

**Uniform root replacement S [cut].** For every $C$ there is $n_0$ such
that every $C$-linear graph of chromatic number at most $\aleph_1$ has a
2-coloring in which no $n_0$ vertices of one color have uncountably many
common neighbours of that color.

This replacement would imply Lemma CC. If the monochromatic edges of a
2-coloring contain no $K_{n_0,\aleph_1}$, then by
[[../library/set_theory/erdos_1966_chromatic_number_graphs_set_systems/corollary_5_6|Erdős and Hajnal's Corollary 5.6]]
they form a graph of countable colouring number, hence of countable chromatic
number by
[[../library/set_theory/erdos_1966_chromatic_number_graphs_set_systems/theorem_3_1|their Theorem 3.1]],
and the product with the 2-coloring is a countable coloring of $G$.
Nevertheless no choice of $n_0(C)$ makes S true.

**Distributed root obstruction [cut].** For every $C>0$ and
integer $n\ge1$ there is a $C$-linear graph of chromatic number three such
that every 2-coloring contains a monochromatic $K_{n,\aleph_1}$.

Set $k=2n-1$ and choose an odd integer $\ell\ge3$ with $k/(2\ell)\le C$.
Take the cyclic sequence of independent parts

$$
P_0,A_0,B_0,P_1,A_1,B_1,\ldots,
P_{\ell-1},A_{\ell-1},B_{\ell-1},
$$

with $|P_i|=k$ and $|A_i|=|B_i|=\aleph_1$, and put all edges between
successive parts and no others. It maps to the odd cycle $C_{3\ell}$ and
contains that cycle, so its chromatic number is three.

For a finite induced subgraph let $b$ be the minimum product of its sizes
in two successive parts. Deleting the $b$ edges at that interface leaves
a bipartite graph. Every $A_i$ and $B_i$ is adjacent to a part of size at
most $k$, so its intersection with the finite subgraph has size at least
$b/k$. There are $2\ell$ such parts. Thus

$$
\beta(F)\le b\le\frac{k}{2\ell}|V(F)|\le C|V(F)|.
$$

This includes $b=0$, and monotonicity handles noninduced subgraphs.
Suppose a 2-coloring contains no monochromatic $K_{n,\aleph_1}$. In each
$A_i,B_i$ select a color present uncountably often. The selected colors of
$A_i$ and $B_i$ must differ. The selected colors of $B_{i-1}$ and $A_i$
must agree: otherwise at least $n$ of the $2n-1$ vertices of $P_i$ match
one of these two colors and give the forbidden complete bipartite graph.
The selected color consequently flips once for each of the $\ell$ blocks
around the cycle, impossible when $\ell$ is odd. This proves the
obstruction. It defeats a uniform bound on monochromatic finite roots,
not Lemma CC: color every $P_i$ with color 2, every $A_i$ with color 0 and
every $B_i$ with color 1 to get an explicit proper three-coloring. A replacement
using this criterion must permit more than two initial colors or abandon
the uniform root bound.

**Root replacement with $q$ colors ([cut] for $q\ge3$).** For every $C$
there are $q$ and $n_0$ such that every $C$-linear graph of chromatic
number at most $\aleph_1$ has a $q$-coloring with no color class
containing $K_{n_0,\aleph_1}$. Exactly as for S, Corollary 5.6 and
Theorem 3.1 then color each class with countably many colors, so this
would imply Lemma CC. The obstruction above uses only two colors. For
graphs obtained from a finite template by replacing its vertices with
independent sets, each finite or of size $\aleph_1$, linearity forces
the template's edges among the uncountable sets to form a bipartite
graph, and three colors then suffice: two on those sets and the third
on the finite ones, which the condition does not restrict among
themselves. The infinite statement is not compact, however, and its
finite strengthening fails.

**Proposition E [cut].** For every $C>0$ and all integers
$q,n\ge1$ there is a finite $C$-linear graph in which every
$q$-coloring has a color class containing $K_{n,n}$.

Put $m=q(n-1)+1$, let $0<\varepsilon\le1$ be fixed below and
$\rho=\varepsilon/4$. Let $N_0$ be a maximal $(\rho/2)$-separated subset
of the sphere $S^q\subseteq\mathbb R^{q+1}$, and let $N$ consist of $m$
distinct points within distance $\rho/2$ of each point of $N_0$, all
$m|N_0|$ points distinct. By maximality every point of $S^q$ lies within
$\rho/2$ of $N_0$, so every closed cap of radius $\rho$ contains at least
$m$ points of $N$. Join distinct $p,p'\in N$ when $|p+p'|<\varepsilon$.
A neighbour of $p$ lies within $\rho/2$ of a point of $N_0$ at distance
less than $9\rho/2$ from $-p$; such points of $N_0$ have disjoint balls
of radius $\rho/4$ inside a ball of radius $19\rho/4$, so there are at
most $19^{q+1}$ of them and every vertex has at most $m\,19^{q+1}$
neighbours. The random-hyperplane argument of Proposition A gives
$\beta(F)\le(\varepsilon/4)\,m\,19^{q+1}|V(F)|$ for every subgraph $F$,
so $\varepsilon=\min(1,4C/(m\,19^{q+1}))$ makes the graph $C$-linear.

Given a $q$-coloring, let $F_i$ be the set of $x\in S^q$ whose closed cap
of radius $\rho$ contains at least $n$ points of color $i$. Each cap
holds at least $m$ points, so the $F_i$ cover $S^q$. Each $F_i$ is
closed: if caps about $x_k\to x$ all contain one fixed set of $n$ points
of color $i$, so does the closed cap about $x$, and there are finitely
many such sets. By the Lyusternik–Schnirelmann theorem some $F_i$
contains a pair $x,-x$. Take $n$ points $A$ of color $i$ within $\rho$
of $x$ and $n$ points $B$ of color $i$ within $\rho$ of $-x$. For
$a\in A$ and $b\in B$, $|a+b|\le2\rho<\varepsilon$, and $a\ne b$ since
$|a-b|\ge2-2\rho$. So $A\cup B$ spans $K_{n,n}$ inside color class
$i$. $\square$

Hence no compactness argument from finite colorings avoiding
monochromatic complete bipartite subgraphs of bounded size can prove
the $q$-color root replacement or Lemma CC. A finite input must permit
the Borsuk-type structures of Proposition A, as the vector inputs below
do: those graphs have small hereditary vector energy without any
partition.

### A geometric certificate and a finite replacement lemma

Call unit vectors $x_v$ ($v\in V(G)$) in a real Hilbert space a **near-antipodal
representation with constant $D$** if

$$
\sum_{uv\in E(F)}\bigl(1+\langle x_u,x_v\rangle\bigr)\le D\,|V(F)|
$$

for every finite subgraph $F$. A 2-coloring with sign vectors $\pm e$ gives
twice its number of monochromatic edges on the left. A random 2-coloring,
a probability measure on $\{0,1\}^{V(G)}$ with expected number of
monochromatic edges at most $C'|V(F)|$ in every finite $F$, gives one with
$D=2C'$ through $x_v=2X_v-1$ in $L^2$ of the measure.

**Proposition C [cut].** A graph with a near-antipodal
representation with a finite constant $D$ has countable chromatic number.
The Hilbert space need not be separable, and no hypothesis on $|V(G)|$ or
$\chi(G)$ is needed.

*Proof.* Choose an orthonormal basis $(e_i)_{i\in I}$ and well-order $I$.
For rational $0<b<a$, let $X_{a,b}$ be the set of unit vectors $x$ for which

$$
S_a(x)=\{i:|\langle x,e_i\rangle|\ge a\}
$$

is nonempty and every coordinate outside $S_a(x)$ has magnitude at most $b$.
This support is finite. Every unit vector belongs to some $X_{a,b}$: choose
a positive coordinate magnitude $m$. Only finitely many coordinate magnitudes
exceed $m/2$, so choose rationals $m/2<b<a<m$ such that $[b,a]$ contains none
of those finitely many magnitudes. Then $S_a(x)$ is nonempty and every
coordinate outside it has magnitude below $b$. Assign each vector the first
suitable rational pair in a fixed enumeration. Within its assigned class,
also record the sign of its coordinate at the least member of $S_a(x)$.

Suppose two vectors $x,y$ receive the same pair and sign. If
$S_a(x)\ne S_a(y)$, a coordinate in their symmetric difference gives
$\|x+y\|\ge a-b$. If their supports agree, their least support coordinate
has the same sign and magnitude at least $a$, so $\|x+y\|\ge2a$. In either
case,

$$
1+\langle x,y\rangle=\tfrac12\|x+y\|^2
   \ge\tfrac12(a-b)^2=:\eta_{a,b}>0.
$$

Thus every finite subgraph on $W$ inside one of these countably many classes
has at most $(D/\eta_{a,b})|W|$ edges. Repeatedly removing a vertex of degree
at most $\lfloor2D/\eta_{a,b}\rfloor$ shows that every such finite graph has
a coloring with $\lfloor2D/\eta_{a,b}\rfloor+1$ colors. Fixed finite-palette
de Bruijn--Erdős compactness colors the whole class with that palette. Use
disjoint palettes for the countably many classes. This gives a proper
countable coloring of $G$. $\square$

The density hypothesis is essential to this argument. A fixed upper bound on
$\|x_u+x_v\|$ for edges alone does not suffice: the $m$-shift graph has
vectors $x_A=m^{-1/2}\sum_{j<m}(-1)^je_{a_j}$ for
$A=\{a_0<\cdots<a_{m-1}\}$, with $\|x_A+x_B\|=\sqrt{2/m}$ on shift edges.
Such graphs can have uncountable chromatic number. This example is not a
counterexample to Proposition C: it does not supply the hereditary energy
bound. Indeed the edge energy is exactly $1/m$, and an uncountably chromatic
graph cannot have bounded finite edge density.

**Single vector replacement [cut].** For every $C\ge0$, there is
a finite $D(C)$ such that every finite $C$-linear graph $H$ admits unit vectors
$(x_v)_{v\in V(H)}$ satisfying

$$
\sum_{uv\in E(H[U])}(1+\langle x_u,x_v\rangle)\le D(C)|U|
\qquad(U\subseteq V(H)).
$$

This would be a sufficient replacement for the failed transversal step. Its
failure is finite compatibility, not the passage to an infinite graph. For its
full implication, take the compact product of the intervals $[-1,1]$ for
the entries of a symmetric Gram matrix indexed by $V(G)$. Impose diagonal
entries $1$, positive semidefiniteness on every finite principal submatrix,
and the displayed inequality for every finite vertex set. Any finitely many
constraints concern one finite induced graph, so the replacement lemma
satisfies them simultaneously. Compactness gives a positive semidefinite
kernel. Its usual inner-product construction, followed by completion,
realizes it by unit vectors in a Hilbert space. Proposition C gives a
countable coloring. Steps 1 to 3 then give the entire limit in Problem 111.
There is no further separability or countable-palette compactness step.

The proposed input is entirely finite, but is stronger than the separate
inequalities $\beta(H[U])\le C|U|$: it requires one compatible family of
vectors for all $U$. A sufficient, possibly stronger, version asks for one
probability distribution on 2-colorings with expected monochromatic-edge
count at most $A(C)|U|$ for every $U$. It yields the vector version with
$D(C)=2A(C)$ by using the random signs as unit vectors in $L^2$. The converse
does not follow from Gram-matrix compactness: a positive semidefinite
correlation matrix need not be the correlation matrix of random signs.

**Exact finite minimax test.** The random-cut version is equivalent to the
following weighted inequality, for every finite $C$-linear $H$ and every
choice of nonnegative real vertex weights $a_v$:

$$
\min_{c:V(H)\to\{0,1\}}
 \sum_{uv\in E(H)}\min(a_u,a_v)\,\mathbf1_{c(u)=c(v)}
 \le A(C)\sum_v a_v. \tag{RC}
$$

For the vector version, replace the indicator by
$1+\langle x_u,x_v\rangle$, minimize over unit vectors, and replace $A(C)$
by $D(C)$; call this inequality (VC). Here is why nested weights suffice.
Finite-dimensional minimax for the convex hull of cut vectors, or for the
compact convex set of Gram matrices, says that simultaneous feasibility is
equivalent to every nonnegative linear combination of the subset constraints.
For such a combination with coefficients $\lambda_U$, set
$a_v=\sum_{U\ni v}\lambda_U$. The resulting edge weight
$w_{uv}=\sum_{U\supseteq\{u,v\}}\lambda_U$ is at most
$\min(a_u,a_v)$, and the total vertex budget is $\sum_v a_v$. Since all
edge costs are nonnegative, the latter weights dominate the dual constraint.
Conversely,

$$
\min(a_u,a_v)=\int_0^\infty
 \mathbf1_{u,v\in U_t}\,dt,\qquad U_t=\{v:a_v\ge t\},
$$

so these are themselves nonnegative combinations of a nested chain of subset
constraints. This proves the equivalence. Choosing a different optimum cut
at every threshold $t$ is not a proof of (RC), because the minimum in (RC)
uses one cut.

**The unchanged cut constant fails [cut].** Let $t\ge1$ be an
integer. Take vertices $p,q,z,a_1,\ldots,a_t,b_1,\ldots,b_t$ and edges
$pq$, $pa_i$, $a_i z$, $zb_i$, $b_iq$. Removing $pq$ makes the graph
bipartite; every odd cycle has length at least five, and a 5-cycle is
present. Consequently its maximum hereditary ratio $\beta(F)/|V(F)|$ is
exactly $1/5$.

In (RC), give $p,q$ weight $t$ and all other vertices weight $1$. The edge
$pq$ has weight $t$ and all other edges have weight $1$. If $p,q$ get the
same color, the cost is at least $t$. If they get different colors, $z$
agrees with one of them, and each of the $t$ length-two paths joining it to
the other has a monochromatic edge. The minimum weighted cost is therefore
$t$, while $\sum_v a_v=4t+1$. Any uniform random-cut coefficient for
$C=1/5$ must be at least $1/4$, by letting $t$ increase. In particular
$A(C)=C$ is false, already for $t=2$, which gives $2/9>1/5$ on seven
vertices. This refutes the constant-preserving cut implication only. It does
not refute (RC) with slack, the vector version (VC), or Lemma CC.

For comparison, one deterministic 2-coloring good for all subsets with a
uniform coefficient would force a finite chromatic bound: its monochromatic
edges would have bounded finite density, hence a finite coloring, and a
product with the two sides would color $H$. Proposition A rules this out
uniformly in the graph. The random and vector replacements avoid that
incorrect deterministic strengthening.

### An obstruction to every uniform single-representation coefficient

**Proposition D [cut].** For every $C>0$ and every finite $D\ge0$,
there is a finite $C$-linear graph of chromatic number three that has no
near-antipodal representation with constant $D$. Thus neither (VC) nor (RC)
has a coefficient depending only on $C$.

*Construction.* Let $k\ge1$, let $\ell\ge5$ be odd, and let
$t\ge\ell^2 k$ be an integer. Replace the vertices of $C_\ell$ by independent
parts $V_0,\ldots,V_{\ell-1}$, with all edges between consecutive parts
(indices modulo $\ell$), where

$$
|V_0|=|V_1|=k,\qquad |V_i|=t\quad(2\le i<\ell).
$$

Call this graph $B(k,\ell,t)$. It maps to $C_\ell$ and contains an odd
cycle, so its chromatic number is exactly three.

*Hereditary deletion bound.* For an induced subgraph put
$n_i=|U\cap V_i|$ and $b=\min_i n_i n_{i+1}$. If any $n_i=0$, the subgraph
is bipartite. Otherwise deleting the $b$ edges between a minimizing pair of
parts makes it bipartite. Moreover

$$
\prod_i n_i^2=\prod_i(n_i n_{i+1})\ge b^\ell,
\qquad \sum_i n_i\ge\ell\sqrt b,
\qquad b\le n_0n_1\le k^2.
$$

Consequently

$$
\frac{\beta(B[U])}{|U|}\le\frac{b}{\sum_i n_i}
 \le\frac{\sqrt b}{\ell}\le\frac{k}{\ell}.
$$

The same bound holds for noninduced subgraphs by monotonicity. Choose
$\ell\ge k/C$ to make $B$ $C$-linear.

*Incompatibility of the vector constraints.* Suppose unit vectors satisfy
the hereditary energy bound with coefficient $D$, and let $m_i$ be their
average over $V_i$. Then $\|m_i\|\le1$. The constraint on
$V_i\cup V_{i+1}$, using completeness of its bipartite edges, gives

$$
1+\langle m_i,m_{i+1}\rangle
 \le D\left(\frac1{|V_i|}+\frac1{|V_{i+1}|}\right).
$$

Since $\|m_i+m_{i+1}\|^2\le2(1+\langle m_i,m_{i+1}\rangle)$, the three
edges of the part cycle incident with $V_0$ or $V_1$ each give
$\|m_i+m_{i+1}\|\le2\sqrt{D/k}$. The other $\ell-3$ edges each give
$\|m_i+m_{i+1}\|\le2\sqrt{D/t}$. Because $\ell$ is odd,

$$
2m_0=\sum_{i=0}^{\ell-1}(-1)^i(m_i+m_{i+1}),\qquad m_\ell=m_0.
$$

Therefore

$$
\|m_0\|\le\sqrt D\left(\frac3{\sqrt k}
                     +\frac{\ell-3}{\sqrt t}\right)
 \le4\sqrt{D/k}.
$$

On the other hand the constraint on $V_0\cup V_1$ gives
$\langle m_0,m_1\rangle\le-1+2D/k$, hence
$\|m_0\|\ge1-2D/k$ whenever $D<k/2$. If $D\le k/25$, these inequalities
would give simultaneously $\|m_0\|\ge23/25$ and $\|m_0\|\le4/5$,
which is impossible. Every such representation thus has $D>k/25$.
Choosing $k>25D$ completes the counterexample. A cut distribution with
coefficient $A$ would give vectors with coefficient $2A$, so no uniform
random-cut coefficient exists either. $\square$

This obstruction is about compatible repairs, not about chromatic number:
every member is three-colorable. Its mechanism is explicit. Dense complete
bipartite pairs force the average vectors to be almost antipodal. The long
cycle makes each separate deletion problem cheap per vertex, but the averages
cannot close around an odd cycle when all these constraints are imposed
together. The hypothesis missing from the refuted replacement is not
separability; it must permit a preliminary partition or use further chromatic
structure.

### A partitioned replacement and the maximum-cut test

**Binary partitioned vector lemma [cut].** For every $C\ge0$ there is a
finite $D(C)$ such that every finite $C$-linear graph $H$ has a vertex
partition $V(H)=A\cup B$ and unit vectors satisfying

$$
\sum_{\substack{uv\in E(H[U])\\
                 u,v\in A\ \mathrm{or}\ u,v\in B}}
 (1+\langle x_u,x_v\rangle)\le D(C)|U|
 \qquad(U\subseteq V(H)). \tag{PV}
$$

This is a sufficient condition for Lemma CC, not a proved reformulation.
One may also ask for any fixed finite number of parts depending on $C$.
For the binary version, use the compact space of binary labels together with
Gram entries. The conditions in (PV) are closed because only finitely many
labels enter each inequality. Finite satisfiability follows from the lemma
on the induced graph containing the finitely many constrained vertices.
The resulting two global classes each satisfy Proposition C, and their
countable colorings combine. Steps 1 to 3 give the full E111 limit. The only
unproved link in this route is the finite statement (PV).

The [cut]
[[research/methods/partitioned_vector_energy|finite-energy tests]]
express (PV) as a uniform bound on $D_2(H)$ and its weighted formulation
with quantifier order $\min_c\max_a\min_X$. They also show
$D_q(H)=0$ exactly when $\chi(H)\le2q$, and give bounds for bounded
exceptional sets and sphere representations. Complete joins of dense
gadgets can violate the fixed-$C$ hypothesis before testing (PV).
These tests constrain a candidate obstruction; they supply neither a
uniform bound nor a family refuting it.

This change directly handles Proposition D. Two labels alternating around
the part cycle can leave only the edges between $V_0,V_1$ within a class.
Those edges form $K_{k,k}$, which admits exactly antipodal vectors and energy
zero. More generally every four-colorable graph satisfies (PV) with $D=0$:
group its four independent classes into two pairs and use opposite vectors
within each pair. Hence the finite three-color obstruction to (VC) is not an
obstruction to (PV).

A tempting sufficient test for (PV) takes a maximum cut of $H$ and writes
$R$ for its monochromatic-edge graph. Cut optimality supplies the switching
inequalities

$$
|E(R)\cap\partial S|
 \le|(E(H)\setminus E(R))\cap\partial S|
\qquad(S\subseteq V(H)),
$$

where $\partial S$ means the edges with exactly one endpoint in $S$.
Nevertheless even choosing among all maximum cuts does not guarantee a
uniform vector bound for $R$.

**Maximum-cut obstruction [cut].** Take any graph $R$ of
Proposition D with $k/\ell\le1$. For each edge $uv$ of $R$, add two new
vertices, each adjacent to $u$ and $v$, and add no other edges. Call the
result $H$. It is $1$-linear: for any induced subgraph, write $U$ for its
old vertices and $W$ for its new ones. Bipartize $R[U]$ with at most $|U|$
deletions; each new vertex has at most two neighbors and can be colored
with at most one additional monochromatic edge. Hence
$\beta(H[U\cup W])\le|U|+|W|$. Also $H$ is three-colorable: properly
3-color $R$ and give each new vertex the third color not used by the
endpoints of its associated edge.

Each edge of $R$ and its two new vertices form a five-edge subgraph. If the
old endpoints have the same color in a cut, at most four of these edges
cross, and four are attainable. If the endpoints differ, at most three
cross. The five-edge sets partition $E(H)$, and coloring every old vertex
on one side and every new vertex on the other attains $4|E(R)|$ crossing
edges. Therefore every maximum cut attains four in each subgraph: all old
edges are monochromatic and every new edge crosses. Its residual graph is
exactly $R$, together with isolated new vertices. Proposition D makes the
required hereditary energy coefficient arbitrarily large, despite the fixed
linear coefficient $1$ for $H$.

Thus total optimality and all its switching inequalities do not supply the
needed coherent repair. This does not refute (PV): these particular $H$ are
three-colorable and satisfy (PV) with zero energy under another partition.
The remaining test must choose the partition for its hereditary repair
properties, allowing it to sacrifice the total size of the cut.

**A combinatorial sufficient form.** Testing the dual certificate of the
finite method with sign vectors shows that (PV) with $D=2A$ follows from
the following statement, the partitioned form of (RC): there is a
labeling $c$ with $q$ labels such that for every choice of vertex
weights $a_v\ge0$ some 2-coloring $\sigma$, which may depend on $a$,
satisfies

$$
\sum_{\substack{uv\in E(H)\\ c(u)=c(v),\ \sigma(u)=\sigma(v)}}
 \min(a_u,a_v)\le A\sum_v a_v. \tag{WB}
$$

Equivalently, by the same minimax, one probability distribution on
2-colorings, chosen after $c$, has at most $A|U|$ expected edges inside
$U$ that are monochromatic for both $c$ and the random coloring, for
every $U$. Both the vector and this form must respect the lower bound
and the gate constraints recorded in the
[[research/methods/partitioned_vector_energy|finite method]]: an odd
cycle of complete bipartite pieces inside one part forces energy, and
in a linear blow-up such a cycle needs, once its smallest part is large
compared with $C$, two consecutive parts of comparatively small size.

**Weighting edges by their 4-cycles also fails [cut].** In the
same construction attach $T$ new degree-two vertices to each edge of $R$,
where $R$ is triangle-free and $T(T-1)$ exceeds the largest original
4-cycle count $w_e$ of any edge of $R$. The graph is still $1$-linear and
three-colorable by the preceding argument. Each new edge lies on exactly
$T-1$ 4-cycles; the count through an old edge remains $w_e$. A new 4-cycle
through an old edge would require a triangle in $R$.

After optimizing the new vertices, the weighted cut contribution at an
old edge $e$ is $2T(T-1)$ when its endpoints have the same color, and
$T(T-1)+w_e$ when they differ. The first is strictly larger. The edge
groups partition all edges and the simultaneous first choice is feasible,
so every cut maximizing these 4-cycle weights leaves all of $R$
monochromatic. Requiring constancy on non-adjacent twins does not help.
Thus this weighted rule has the same unbounded hereditary-energy defect;
it does not supply the partition in (PV).

### Local coherence conditional on a random-cut representation

A random 2-coloring $\mu$ with at most $C'|V(F)|$ expected monochromatic
edges in every finite $F$ also has the following local property
[cut]. This paragraph assumes the stronger random-cut input;
the vector input alone does not supply it. Let $M$ be a
countable elementary submodel containing $G$ and $x\notin M$ a vertex whose
trace $N(x)\cap M=\{d_1,d_2,\ldots\}$ is infinite. Each
$A_N=\{d_1,\ldots,d_N\}$ has uncountably many common neighbours, so for any
$t$ of them every 2-coloring has at least $tZ_N$ monochromatic edges, where
$Z_N$ is the size of the smaller color class of $A_N$. Hence
$t\,\mathbb E_\mu Z_N\le C'(N+t)$ for every $t$, so
$\mathbb E_\mu Z_N\le C'$, and by monotone convergence almost surely all but
finitely many $d_i$ share one color. The same count over $N$ common
neighbours $x_1,\ldots,x_N$ of $A_N$ shows that on average they take the
majority color of the trace with probability $O(C'/N)$. These almost-sure
assertions alone do not select one 2-coloring good at every vertex at once.
Proposition C does obtain a countable proper coloring from the assumed
measure, by a different argument; its construction does not require that
simultaneous selection.

### Replication over an elementary submodel

The following tool restricts how a linear graph can sit over a countable
elementary submodel; it needs no random-cut input.

**Lemma F [cut].** Let $M\prec H(\theta)$ be countable with
$G\in M$, let $F\subseteq V(G)$ be finite and put $R=F\cap M$. For every
$j\ge1$ there are pairwise disjoint sets $F_1,\ldots,F_j\subseteq
V(G)\setminus R$ and bijections $F\to R\cup F_i$ that fix $R$ pointwise
and preserve adjacency and non-adjacency. Consequently, if $G$ is
$C$-linear, then so is the graph obtained from $j$ copies of $G[F]$ by
identifying them along $R$, with no edges between different copies outside
$R$.

*Proof.* For a finite $D\in M$, the statement that some injective map on
$F\setminus R$ into $V(G)\setminus(R\cup D)$ extends the identity of $R$ to
an isomorphism of induced subgraphs has parameters in $M$: $G$, $R$, $D$
and the finite adjacency pattern of $F$ over $R$. It holds in $H(\theta)$,
witnessed by the inclusion of $F\setminus R$, which misses $M\supseteq D$.
By elementarity it has a witness in $M$. Taking $D=R\cup F_1\cup\cdots\cup
F_{i-1}$, a finite subset of $M$, gives $F_i$. The amalgam is isomorphic
to a spanning subgraph of $G[R\cup F_1\cup\cdots\cup F_j]$, and deleting
edges does not increase $\beta$. $\square$

**Corollary (gates do not follow their arms).** Let $G$ be $C$-linear, let
$\ell\ge3$ be odd, and let $V_0,\ldots,V_{\ell-1}$ be pairwise disjoint
finite sets with every vertex of $V_i$ adjacent to every vertex of
$V_{i+1}$ (indices modulo $\ell$), $|V_0|=|V_1|=k>4C$ and $|V_i|\ge\ell k$
for $2\le i\le\ell-1$. Then no countable $M\prec H(\theta)$ with $G\in M$
contains $V_2\cup\cdots\cup V_{\ell-1}$ and misses $V_0\cup V_1$.

*Proof.* Shrink each $V_i$ with $i\ge2$ to $\ell k$ vertices and apply
Lemma F with $j=\ell^2$ to $F=V_0\cup\cdots\cup V_{\ell-1}$, so that the
gate $V_0\cup V_1$ is copied $j$ times over the arms. Give each odd cycle
through one copy of the gate and one vertex of each arm part the weight
$(\ell k)^{-(\ell-2)}$. Every edge then carries weight at most one: an edge
of a gate copy lies on $(\ell k)^{\ell-2}$ such cycles, an edge between two
arm parts on $jk^2(\ell k)^{\ell-4}$, and an edge from a gate copy to an arm
part on $k(\ell k)^{\ell-3}$. The total weight is $jk^2$, so the amalgam has
$\beta\ge jk^2=\ell^2k^2$ on $2\ell^2k+(\ell-2)\ell k<3\ell^2k$ vertices,
a ratio above $k/3>C$, contrary to Lemma F. $\square$

One such cycle is itself $C$-linear when $\ell\ge k/C$, by the
two-adjacent-parts bound of the
[[research/methods/partitioned_vector_energy|finite method]]. So the
corollary is a genuine restriction. In a continuous chain of countable
elementary submodels covering a $C$-linear graph of size $\aleph_1$, a
large cheap gate is never added entirely after the large parts it closes
into an odd cycle. This is the orientation that a coherent transfinite coloring needs:
later vertices cannot make an earlier rigid bipartition inconsistent
through a cheap gate. Lemma F applies to every finite configuration, not
only to gated cycles. Turning it into a countable coloring, for instance
into the root replacement with $q$ colors above or into the infinite form
of (PV), is open.

**Lemma G [cut].** If $G$ is $C$-linear and $A\subseteq V(G)$
is finite with $|A|=n>3C$, then the common neighbourhood $N^*(A)$ induces
a graph containing no $K_{n,n}$. Hence $G[N^*(A)]$ has countable coloring
number and countable chromatic number.

*Proof.* $A$ is disjoint from $N^*(A)$, since no vertex is adjacent to
itself. If $S_1,S_2\subseteq N^*(A)$ span $K_{n,n}$, then $A\cup S_1\cup
S_2$ contains $K_{n,n,n}$. Indexing the three parts by $\mathbb Z_n$, the
$n^2$ triangles $(a_i,b_j,c_{i+j})$ are edge-disjoint, so $\beta\ge n^2$ on
$3n$ vertices, a ratio $n/3>C$. Therefore $G[N^*(A)]$ contains no
$K_{n,\aleph_1}$, and
[[../library/set_theory/erdos_1966_chromatic_number_graphs_set_systems/corollary_5_6|Corollary 5.6]]
with
[[../library/set_theory/erdos_1966_chromatic_number_graphs_set_systems/theorem_3_1|Theorem 3.1]]
gives the rest. $\square$

For a $C$-linear graph of size $\aleph_1$, choose a continuous chain
$(M_\alpha)_{\alpha<\omega_1}$ of countable elementary submodels whose union
contains $V(G)$, and put $n=\lfloor3C\rfloor+1$. Color the countable initial
layer $V(G)\cap M_0$ separately. For the remaining vertices, call
$v\in M_{\alpha+1}\setminus M_\alpha$ low if fewer than $n$ of its
neighbours lie in $M_\alpha$, and high otherwise. Ordering the vertices by
layers, and each countable layer in
type $\omega$, gives every low vertex finitely many earlier low neighbours,
so the low vertices induce a graph of countable coloring number. Every high
vertex lies in $N^*(A)$ for an $n$-set $A$ of earlier neighbours. If
countably many such sets $A$ cover the high vertices in this way, coloring
each high vertex through the first covering set and Lemma G gives a
countable coloring of $G$. A disjoint union of $\aleph_1$ copies of
$K_{n,\aleph_1}$ shows that countably many sets need not suffice even for
bipartite graphs. Since vertices sharing a set are colored properly by
Lemma G, the open step is to control the edges between high vertices
assigned different sets.

The unfiltered quotient of these root classes cannot be required to have
countable chromatic number. For each $i<\omega_1$ take an independent
$n$-set $A_i$. For each $i<j$ and each $\xi<\omega_1$ add a private edge
$x_{ij\xi}y_{ij\xi}$, join $x_{ij\xi}$ to all of $A_i$, and join
$y_{ij\xi}$ to all of $A_j$. There are no other edges. Deleting the
matching of private edges bipartizes every finite subgraph at a cost of
at most half its number of endpoint vertices. The graph is $1/2$-linear
and three-colorable, but the quotient on the classes $N^*(A_i)$ is the
complete graph on $\omega_1$. Even over a countable model containing both
root sets, paired endpoints can be chosen outside the model, so their
traces there are exactly those roots. This rules out raw quotient
adjacency as the closing input. It does not rule out a refinement that
first disposes of edges within model layers.

### A simultaneous rooted extension measure

The
[[research/leads/linear_bipartization_countable_coloring/rooted_cut_measures|rooted measure argument]]
combines Lemma F with finite minimax and compactness. For every $C$-linear
graph there is one measure on vertex signs satisfying
$\mathbb E e_P\le C|S_P|$ for every abundantly realized rooted pattern
$P$, where $e_P$ is its minimum extension cost after the root signs are
chosen. For any fixed countable elementary model, the infinite traces then
give majority signs $s_x$ with

$$
 \mathbb E\left[\sum_{x\in A}b_x+
       \sum_{xy\in E(G[A])}\mathbf1_{s_x=s_y}\right]\le C|A|
$$

for every finite set $A$ of outside vertices having infinite traces;
$b_x$ counts the minority signs on the trace. This is a genuine
hereditary energy bound on that outside set and includes its boundary
cost. Its gap is exact: the extension minimizers are not the coordinate
signs of the measure. For nested countable models and a vertex outside both,
its derived signs do agree almost surely once its smaller trace is
infinite, since the larger trace has only finitely many minority signs.
The missing relation is at the step when the vertex becomes a coordinate
in the next model. The unmodified measure supplies neither that relation
nor a global hereditary representation or fixed partition for (PV).

### Layered correction of the rooted measure: a candidate proof of Lemma CC

The
[[research/leads/linear_bipartization_countable_coloring/layered_rooted_measures|layered measure note]]
records a [cut] candidate proof that every $C$-linear graph,
of any cardinality and with no hypothesis on its chromatic number, has
countable chromatic number. With Steps 1 to 3 this would prove the full
limit in Problem 111. [cut]

The argument runs along a continuous chain $(N_\xi)$ of elementary
submodels, each smaller than the graph, and inducts on the number of
vertices. Each vertex outside $N_0$ has a layer and a trace, its
neighbours in the model preceding its layer. Write $J(\nu,\xi)$ for the
rooted measure's inequality $\mathbb E_\nu e_P\le C|S_P|$ for all
patterns over $N_\xi$, with $\nu$ a measure on the signs of $N_\xi$. The
rooted measure gives $J$ at $N_0$. At a successor step, every vertex of the
new layer with infinite trace receives the opposite of its countably
determined trace sign, and the finite-trace vertices of the layer are
chosen by a coupling. $J$ at the next model survives. The proof replicates
the pattern's new vertices over the next model, keeps the layer's
infinite-trace roots rigid through long stretches of their traces, which
lie in the earlier model, and applies $J$ there, minimax and compactness.
Limits are projective limits, including chains of length
$\operatorname{cf}\kappa$ when the vertex cardinality $\kappa$ is singular.
In the final measure every infinite-trace
vertex $v$ satisfies $\sum_{u\in T_v}\nu(\sigma_u=\sigma_v)\le C$. This
is a finite trace-star energy for the unit vectors $\sigma_v$ in
$L^2(\nu)$. Proposition C's classes then reduce the coloring to countable
coloring number across layers and the induction inside layers.

This replaces the compatibility gap of the rooted measure: coordinates
are corrected to the derived signs one layer at a time, and the rooted
property is maintained rather than exchanged. The note also shows that a
uniform energy bound at every vertex, finite-trace vertices included,
fails for every chain in a bouquet of Proposition D petals sharing one
gate part. The candidate argument imposes no trace-energy constraint at
finite-trace vertices. It bypasses (PV), whose finite quantifiers [cut] are unchanged.

## Next discriminating tests

**The full candidate.** The complete route claimed by Step 5 is the
layered measure argument. Its decisive point is Lemma S: a fixed old law
must admit an extension with all the infinite-trace coordinates prescribed
and all rooted inequalities at the next model satisfied simultaneously.
The proof first lets trace-star lengths tend to infinity at fixed copy
multiplicity, then lets that multiplicity tend to infinity, before finite
convex separation and compactness. [cut] The tests below concern alternative
routes; no bound in (PV) is a premise of Step 5.

**1. The partitioned finite inequality.** Decide (PV), first with two
parts. Its positive resolution supplies the missing finite input in the
complete implication to E111 above. Equivalently, after choosing the two
parts, prove the vector weighted inequality (VC) for each induced part with
a coefficient uniform in the finite $C$-linear graph. The order of choices
is essential: one partition must work for every choice of vertex weights;
the vectors may depend on the weights in this minimax formulation. Neither
a single global representation nor selecting a maximum cut can supply it,
by the explicit families above. A useful falsification target is a family
with fixed $C$ for which every binary partition has one induced part whose
minimum hereditary energy coefficient diverges. Such a family would close
only this two-part replacement; it would not disprove E111. A proof should
instead show how to separate interacting finite high-density repair regions
with one partition, using the linear profile to control the remaining
vector energy. Allowing a fixed finite number of parts depending on $C$
still suffices for E111.

The finite method's gate constraints sharpen both directions. An
obstruction through odd cycles of dense pieces must force, in every
labeling, such a cycle inside one part with a gate of two consecutive
small pieces and much larger pieces elsewhere. Labelings by size band
defeat it unless gated cycles link the bands into a graph of chromatic
number above $q$, and labelings properly 2-coloring the large pieces
defeat it unless the large pieces force monochromatic long paths, as
Borsuk-type graphs do. Forcing of the latter kind is topological and
spreads parity changes over many steps, while the energy bound (8) of
the method needs a sharp gate. The two sphere designs examined there
fail for this reason, with the scope stated on that page. A positive
proof would have to produce a partition that separates gates from the
large pieces they close up. Both the ordinary and 4-cycle-weighted maximum
cut rules fail at this task. The next discriminating test is to decide (WB), or (PV), for
blow-ups of odd cycles and Borsuk graphs with arbitrary part sizes,
where both the gate constraint and the topological forcing are present.
Proposition E shows that colorings avoiding monochromatic complete
bipartite subgraphs cannot replace the vectors in such a finite input.
The rooted extension measure offers another precise interface: obtain
compatible derived signs across the model filtration, with a hereditary
energy bound, or use their incompatibility to choose the finite partition
before any vertex weights. Its expected-minimum inequality alone does
neither. The layered measure note proposes to close CC directly by
correcting coordinates layer by layer. This bypasses the finite test;
even a valid proof of CC there would not by itself settle (PV) or (WB).

**2. The profile of Lambie-Hanson graphs.** This decides whether the method
of Proposition B can give a negative answer. In an $n$-vertex subgraph of the
graph of Proposition B, the edges labelled at least $g(n)$ are bipartite and
each smaller label $j$ adds a forest. A linear profile needs the defects
caused by these forests to be summable over $j$. Inside one branch of the
construction the label of an edge is the branch value at its lower endpoint,
so the vertices split into classes by label and each vertex has at most one
earlier neighbour in each class. The whole graph on any full branch is
countably colorable: each class of branch value $j$ induces a subgraph of the
label-$j$ forest, and the countably many bipartitions combine. Thus
restricting to one branch cannot itself provide an uncountably chromatic
counterexample. Finite patterns within a branch could still test the density.
The positive-profile test is exact: for every $M$, find a finite graph $F$
with $\beta(F)>M|V(F)|$ and prove it occurs after every countable deletion.
The pattern must satisfy all of the construction's label restrictions. In
particular, every edge labelled at least $j$ maps, through the $j$-th block
of the ladders, into a Specker graph; the pattern needs these homomorphisms
for all its labels at once. The club-guessing ladders must then realize the
pattern, including the least-neighbour selection, whereas Lemma 3.4 supplies
only the pair-of-levels input used in the chromatic-number proof. Neither
the compatible homomorphisms nor this realization step is proved here.
High-girth graphs far from bipartite are possible finite candidates, not
subgraphs established by the paper. Conversely, a structural restriction
would give a negative answer only after proving a uniform linear bound for
every finite subgraph of the full construction. The separate per-label
forest bounds do not give that uniform estimate.

*Forcing with finite conditions.* Komjáth and Shelah, *Finite subgraphs of
uncountably chromatic graphs* (J. Graph Theory 49 (2005); [cut] arXiv:math/0212064v1), force an uncountably chromatic
graph on $\omega_1$ from a club-guessing sequence. Conditions are finite
labelled graphs subject to stipulations on short odd cycles. Their chain
condition joins two isomorphic conditions over a common initial segment, and
their chromatic argument joins a condition to an interleaved isomorphic copy
over an initial segment and adds one edge between a vertex and its copy. A
consistent negative answer to Problem 111 along these lines needs a
hereditary class of finite structures, closed under both operations and
under the density extensions, all of whose graphs are $C$-linear. Three
constraints on such a class are recorded here [cut].

- Every finite subgraph of the generic graph lies in a condition. By
  compactness and Proposition C, the class must therefore contain graphs
  defeating (PV) for every number of parts. A uniform finite property such
  as (RC), (WB) or a vector-energy bound on every condition passes to the
  generic graph by compactness and forces countable chromatic number, so it
  cannot be the stipulation.
- Plain $C$-linearity is not preserved by joining copies over a common part.
  Take Proposition D's graph $B(k,\ell,t)$ and join $j$ copies over the arms
  $V_2\cup\cdots\cup V_{\ell-1}$, so that the gate $V_0\cup V_1$ is copied
  $j$ times. Keep all $j$ gates and $\lceil\sqrt jk\rceil$ vertices of each
  arm part, possible when $t\ge\sqrt jk$. Weighting each odd cycle that
  passes through one gate and one vertex of each arm part by the reciprocal
  of the product of the arm counts loads every edge by at most one and has
  total weight at least $jk^2$. So this subgraph has $\beta\ge jk^2$ on
  $2jk+(\ell-2)\lceil\sqrt jk\rceil\le3jk+\ell$ vertices, and for
  $j\ge\ell^2$ the ratio exceeds $k/4$. Choose $k>4C$ and $\ell\ge k/C$,
  so that one copy is $C$-linear, and double the gates repeatedly. Some
  doubling then joins two isomorphic $C$-linear graphs over the arms and
  is not $C$-linear. With the arms below the gates in the well-order,
  uncountably many copies of that last $C$-linear stage over the same arms
  would be pairwise incompatible, if they met the other stipulations. A
  suitable class must keep large gates from being copied above the arms
  they close.
- The added edge joins a vertex to its own copy, so every coloring that
  agrees on the two copies leaves it monochromatic. In the Komjáth–Shelah
  graph, as in Lambie-Hanson's, the edges of each label form a forest and
  are paid for one forest per label, the source of bounds of the form
  $(n-1)g(n)$ as in Proposition B. A linear class must
  instead make these edges bichromatic in good colorings, by coloring the
  copies differently across a small cut.

No class meeting these constraints is known here; it would supply exactly
the finite graphs that test 1 asks for.

*Sparse ladders.* Soukup's Theorem 5.5 gives a different uncountably
chromatic graph in ZFC. Its finite subgraphs have separated predecessor
intervals, but the
[[research/leads/linear_bipartization_countable_coloring/sparse_ladder_profiles|Hadamard construction]]
shows that this condition permits unbounded $\beta(F)/|F|$, already on
three-colorable graphs. The missing input is a stronger restriction on
the actual finite realizations of the chosen ladder system, together
with an all-subgraph profile bound. No such restriction is proved here;
the generic interval-separation implication is false.
The [[research/leads/linear_bipartization_countable_coloring/recursive_probe_cuts|recursive probe calculation]]
retains an exact cut-potential recurrence for a narrower finite family.
Its checked whole-graph values through level eight give neither a bound
for all induced subgraphs nor an uncountably chromatic construction with
that finite age.

**3. The independence-ratio connection.** A $C$-linear graph has an
independent set of at least $|V(F)|/(8C+2)$ vertices in every finite subgraph
$F$: the larger side $S$ of a 2-coloring with at most $C|V(F)|$
monochromatic edges has average degree at most $4C$ inside, and the
Caro–Wei bound applies. Hence a negative answer to Problem 111 by a graph of
size $\aleph_1$ would, through the remainder of Step 3, answer the linear
question of [[problems/graph_coloring/E0075/_index|Problem 75]] positively;
that question is
[[../library/graph_coloring/erdos_1982_almost_bipartite_large_chromatic_graphs/problem_2|Problem 2 of Erdős, Hajnal and Szemerédi]].
Contrapositively, a negative answer to that question would prove the limit
of Problem 111 for every graph of size and chromatic number $\aleph_1$.

## Sources and reading

- [[../library/graph_coloring/lambiehanson_2020_growth_rate_chromatic_numbers_finite_subgraphs/_index|Lambie-Hanson 2020]]:
  arXiv:1902.08177v2, the edition identified by the source card. Section 4
  (the construction, Claims 4.1 and 4.2 and the chromatic-number
  argument), Lemma 3.4 [cut], and
  Section 5 for the $\diamondsuit$ version; Shelah's club-guessing theorem and
  the Erdős–Hajnal odd-girth bound for Specker graphs are used as the paper
  cites them. Proposition B consumes only Claim 4.1 and $\chi(G)=\aleph_1$.
  The shift-graph chromatic bound in the geometric certificate is the
  paper's Theorem 1.1(1), which it recalls from Erdős and Hajnal without
  proof.
- [[../library/set_theory/erdos_1966_chromatic_number_graphs_set_systems/_index|Erdős–Hajnal 1966]]:
  Corollary 5.6 and Theorem 3.1 [cut].
- [[../library/set_theory/soukup_2015_trees_ladders_graphs/_index|Soukup 2015]]:
  arXiv:1409.2922v1. [cut] The finite-profile probe uses
  the sparse-system conclusion from the proof of Theorem 5.5, with its
  source dependence and limits stated on that probe's page[cut].
- [[../library/graph_coloring/adamczewski_2026_erdos74/_index|The Problem 74 preliminary exposition]]:
  Propositions 2.2 and 4.1 and Lemma 5.1 [cut]; only the mechanism is used, as a target for replacement.
- [[../library/graph_coloring/erdos_1982_almost_bipartite_large_chromatic_graphs/_index|Erdős, Hajnal and Szemerédi 1982]]:
  [cut] Theorems 1 and 3, Lemma 2.1, the p. 121
  remarks and Problem 2 [cut].
- P. Komjáth and S. Shelah, *Finite subgraphs of uncountably chromatic
  graphs*, J. Graph Theory 49 (2005), no. 1, 28–38: arXiv:math/0212064v1, [cut] The introduction and Section 2 (the conditions,
  Lemmas 1–5, Theorem 1 and the statement of Theorem 2) [cut]. Only the structure of the two joins
  is used, as a design target; no result of the paper is a premise here.
- The Lyusternik–Schnirelmann theorem, the random-hyperplane separation
  probability, the de Bruijn–Erdős theorem and the Caro–Wei bound are
  standard results used as stated[cut].
