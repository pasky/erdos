---
name: graph_coloring/openai_2026_correspondence_coloring_graphs_forbidden_clique/theorem_1_1
title: "Theorem 1.1: K_r-free graphs of large maximum degree Delta have correspondence chromatic number at most ceil(C_r Delta/log Delta)"
desc: |
  The manuscript's main claim: for each fixed r at least 4, every K_r-free
  graph of maximum degree Delta at least Delta_r has correspondence, hence
  list and ordinary, chromatic number O_r(Delta/log Delta). Claims checked
  only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

Here a graph is finite, simple and undirected, and $\log$ is the natural
logarithm. To set up a correspondence assignment on $G$, attach to every
vertex $v$ a finite list $L(v)$, with different vertices receiving disjoint
lists, and to every edge $uv$ a matching $M_{uv}\subseteq L(u)\times L(v)$
whose pairs are declared forbidden; nothing ties the matchings of different
edges together around a cycle. The assignment is colorable when one entry
$c(v)\in L(v)$ can be chosen at each vertex so that no edge $uv$ has
$(c(u),c(v))\in M_{uv}$. Then $\chi_{\mathrm{DP}}(G)$, the correspondence or
DP-chromatic number, is the smallest integer $k$ for which every
correspondence assignment with lists of at least $k$ entries is colorable.
Ordinary and list coloring arise as special cases, and greedy coloring needs
at most $\Delta(G)+1$ entries per list, so
$\chi(G)\le\chi_{\mathrm{list}}(G)\le\chi_{\mathrm{DP}}(G)\le\Delta(G)+1$
(p. 2). A graph is $K_r$-free when it has no $r$ pairwise adjacent vertices.

**Theorem 1.1.** Fix an integer $r\ge4$. A constant $C_r>0$ and a degree
threshold $\Delta_r\ge3$, both determined by $r$ alone, exist such that each
$K_r$-free graph $G$ whose maximum degree $\Delta$ is at least $\Delta_r$ has

$$
\chi_{\mathrm{DP}}(G)\le\Bigl\lceil C_r\frac{\Delta}{\log\Delta}\Bigr\rceil.
$$

The bound therefore does not depend on the order of $G$, on the lengths of
the lists or on the choice of matchings, and the manuscript makes no attempt
to optimize $C_r$ or $\Delta_r$ (p. 2). By the chain above the same bound
holds for $\chi_{\mathrm{list}}(G)$ and $\chi(G)$. The proof sets
$C_r=100K/\gamma$ with $K=16(B+2)$, $\gamma=0.003$ and $B=B(r)$ the constant
of Lemma 2.1; no explicit value of $B$, $C_r$ or $\Delta_r$ is given. The case
$r=3$ is not part of the statement; the manuscript attributes the
triangle-free bound to Johansson for list coloring and to Bernshteyn for
correspondence coloring.

**Source.** OpenAI, *Correspondence coloring graphs with a forbidden clique*,
release folder
`preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026`;
TeX file `build/sections/introduction.tex`, label `thm:main` (lines 25--34),
PDF p. 2; the proof closes at the end of Section 5
(`build/sections/completion.tex` lines 9--68, PDF pp. 26--27). Read
2026-10-12. Provenance and attestations are on
[[graph_coloring/openai_2026_correspondence_coloring_graphs_forbidden_clique/_index|the card]].

**Read depth.** Claims checked: the statement, the definitions it rests on
(`introduction.tex` lines 3--21 and 179--188), and the statements of Lemma
2.1, Proposition 2.5, Lemma 3.1, Proposition 4.1 and Lemmas 4.2--4.4 were
read clause by clause in the TeX source. The proof (Sections 2--5, PDF
pp. 6--27) was read for its structure only, as summarized below; no step was
checked. Nothing here is independently reviewed.

## Proof pointer

The proof is a semi-random coloring procedure in the style of Johansson's
method, run on the list entries rather than on colors. Lists are cut to
exactly $k=\lceil C\Delta/\log\Delta\rceil$ entries and every entry starts
with weight $K/k$. The positive-weight entries form a graph $H$ whose edges
are the forbidden pairs; each entry has at most one neighbor in any list,
cliques of $H$ project to cliques of $G$, so $H$ is $K_r$-free. Each
uncolored vertex $v$ carries a potential $F_v$: an entropy term of its
weights relative to $K/k$, a penalty $\gamma\log\Delta$ times the lost total
weight, and the incident edge mass $D_v$ between its entries and those of its
neighbors (Section 4, p. 20).

A round (Proposition 4.1) activates each entry independently with
probability $\tau w_z$, $\tau=\Delta^{-0.1}$; a vertex with an activated
entry that has no activated neighbor in $H$ takes one such entry as its
color, and entries left untouched receive a compensating multiplier that
cancels, to first order, the mean weight lost to activations and multiplier
operations. The correlated deletion of two adjacent entries by a common
neighbor's activation costs, at entry $i$, a term proportional to its
triangle mass $t_i$. The local weight adjustment of Lemma 2.1 supplies
random multiplier and drop operations, run with their own flags in the same
round, whose first-order effect offsets $t_i$ up to
$Bd_i$ at every entry, each operation touching at most $P_0=\Delta^{o(1)}$
entries of any one list. Lemma 4.2 bounds the expected rise of $F_v$ by
$\tau(B+1)D_v$; coloring neighbors removes about $\tau(K/8)D_v$ of edge mass,
which wins since $K/8>B+1$. Concentration comes from a read-$k$ style
inequality whose participation parameter is that per-list bound (Lemma 4.3),
from concentrating each matching sum separately, and from a collision bound
through large matchings of colliding activations (Lemma 4.4); the Lovász
local lemma makes all local events hold at once, and trimming restores the
weight window $[\Delta^{-3},\Delta^{-0.99}]$ and $s_i\le20\log\Delta$. After
$\lceil2\tau^{-1}\log\Delta\rceil$ rounds each remaining degree is at most
about $\Delta^{0.96}$ while each list keeps at least $(K/2)\Delta^{0.99}$
positive-weight entries, so a greedy pass completes the coloring
(Section 5).

Lemma 2.1 is proved by duality (Sections 2--3): testing against nonnegative
prices reduces it to a priced triangle bound; triangles at vertices whose
support price dominates are paid by drop operations; the rest are grouped by
the dyadic level of their median price and reweighted. A sparse-multiplier
construction (Lemma 2.2, the Ajtai--Erdős--Komlós--Szemerédi neighborhood
recursion) turns the price condition into a bound on edge mass between
nearby sets (Lemma 2.3), which survives vertex splitting (Corollary 2.4).
Lemma 3.1 splits vertices along labels drawn from lazy walks inside
neighborhoods, coupled by shared rejection sampling, keeping most triangle
mass while cutting neighborhood weights from $e^\ell$ to $e^{\sqrt\ell}$; an
entropy bound on those walks (Lemma 3.2) drives it. Iterating
$\ell\mapsto\sqrt\ell$ leaves bounded neighborhood weights, where triangles
are directly bounded by edges, proving Proposition 2.5. The manuscript says
these structural steps adapt the companion independence manuscript's
Sections 2--5, with the added bound on entries per list.

## Dependencies

External inputs, taken at statement level; none was checked here. The
manuscript says it proves every ingredient it needs, and cites the following
as precedents for arguments it writes out. The companion manuscript *A
logarithmic independence bound for clique-free graphs*, filed at
[[extremal_graph_theory/openai_2026_logarithmic_independence_bound_clique_free_graphs/_index|the independence card]]:
its Sections 2--5 for the multipliers, walks and splitting, its
Lemmas 2.2--2.3 for the mean-one multipliers and the cross estimate, and its
Sections 3--5 for the triangle estimate. The clique-free neighborhood
recursion of Ajtai, Erdős, Komlós and Szemerédi (Section 3 of their 1981
paper); the entropy increments controlling walk distributions of Benjamini,
Duminil-Copin, Kozma and Yadin (their Section 2, Theorem 8); the coupling
disagreement bound of Angel and Spinka (their Theorem 2), with a finite-state
proof in the text. The read-$k$ concentration setting of Gavinsky, Lovett,
Saks and Srinivasan, from which Lemma 4.3 is derived in the text through
Finner's generalized Hölder inequality and Hoeffding's exponential-moment
bound; the Lovász local lemma of Erdős and Lovász (1975), whose symmetric
form is proved in the text. Johansson's method as presented by Bansal, Gupta
and Guruganesh (Sections 2 and 6--8 of their extended version) is cited for
the entropy, edge-energy and compensated-weight features of the rounds.

## Bears on

The manuscript names no Erdős problem; the row is an input inferred on this
page, not stated in the manuscript and not verified here.

- [[../wiki/problems/extremal_graph_theory/E0620/_index|Problem 620]]: input.
  At $r=4$ the theorem would supply the independence step of the
  neighborhood argument the page records (written out on
  [[extremal_graph_theory/shearer_1995_independence_number_sparse_graphs/corollary_1|Shearer's Corollary 1 page]]):
  a $K_4$-free graph of maximum degree below $D=\sqrt{n\log n}$ has
  $\chi\le\max\{\Delta_4,\lceil C_4D/\log D\rceil\}$, so a color class of size
  $\gg\sqrt{n\log n}$, while a vertex of degree at least $D$ has a
  triangle-free neighborhood; hence $f(n)\gg\sqrt{n\log n}$. The page already
  derives that bound from Corollary 2 of Joret, Micek, Reed and Smid,
  subject to the gap claim recorded on Problem 610; the companion's accepted
  independence bound gives it as well. Nothing here bears on the open upper
  bound. Unverified.
