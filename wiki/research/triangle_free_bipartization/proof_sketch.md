---
name: research/triangle_free_bipartization/proof_sketch
title: Proof sketch for the middle-density band of Problem 23
desc: Editable sketch of the attack on the open middle-density band of Problem 23, separating the held tail results, author-recorded partial results, tested routes with their exact obstructions, and the remaining gap.
created: 2026-10-15T23:29:23Z
updated: 2026-10-17T22:11:11Z
---

# Proof sketch for the middle-density band of Problem 23

***

## Target

[[problems/extremal_graph_theory/E0023/_index|Problem 23]] asks whether
every triangle-free graph on $5n$ vertices can be made bipartite by deleting
at most $n^2$ edges. Write $D_2(G)$ for the fewest edges whose deletion makes
$G$ bipartite. The target of this sketch is the all-order statement that
every finite triangle-free graph $G$ on $N$ vertices satisfies

$$
D_2(G)\le\frac{N^2}{25}. \tag{T}
$$

On $N=5n$ it is the problem. Conversely the problem implies (T): apply it to
the blow-up $G[5]$, which is triangle-free on $5N$ vertices with
$D_2(G[5])=25D_2(G)$. Write $p=2e(G)/N^2$ for the edge density and
$d_{\rm mono}=2D_2(G)/N^2$; both are the values of the equal-weight step
graphon $W_G$, and (T) says $d_{\rm mono}(W_G)\le2/25$.

## Held links

- **Blow-up identity**, $D_2(G[t])=t^2D_2(G)$, proved on
  [[research/graph_ramsey_interfaces/homogeneous_triangle_deletion_bounds|the homogeneous transfer page]]
  (author-recorded) and also stated as Lemma 2.1 of Ferudun's preprint.
- **Density tails.** The same page transfers the large-order bounds of
  [[../library/extremal_graph_theory/balogh_2021_max_cuts_triangle_free_graphs/theorem_2|Balogh, Clemen and Lidický, Theorem 2]]
  to every order: (T) holds whenever $p\le1243/5000$ or $p\ge3197/10000$.
  The transfer is author-recorded; the theorem keeps the claims-checked
  reading standing of its source card.
- **What remains.** Given the tails, (T) is equivalent to the band statement:
  every triangle-free $G$ with $1243/5000<p<3197/10000$ has
  $d_{\rm mono}(W_G)\le2/25$. A family of valid bounds
  $d_{\rm mono}\le2/25+\delta_j$ on the band with $\delta_j\to0$ also
  suffices, since a fixed graph may then let $j\to\infty$; a single
  positive $\delta$ only extends a finite range by integer rounding.
- **Pending, not a premise.**
  [[../library/extremal_graph_theory/ferudun_2026_erdos_max_cut_small_multiples/_index|Ferudun's unrefereed preprint]]
  reports $\delta\approx4.8558\cdot10^{-5}$ and hence (T) for $N=5n$ with
  $n\le40$. Its certificate is not accepted here, and
  [[research/triangle_free_bipartization/profile_envelope_obstructions|the obstruction record]]
  identifies what its eight-root and rooted-Horn rows must accomplish for
  the reported value to stand.

## Partial results

These three results are by Plasma AI and author-recorded. They settle (T)
for restricted classes or constrain a counterexample; none covers the band.

**Edge-cut criterion.** For an edge $uv$ of a triangle-free $G$, the
neighbourhoods $N(u)$ and $N(v)$ are disjoint independent sets. Put $N(u)$
on one side, $N(v)$ on the other and every other vertex on a uniformly random
side. Each edge with an end outside $N(u)\cup N(v)$ is uncut with probability
$1/2$, and every other edge runs between $N(u)$ and $N(v)$ and is cut, so
$D_2(G)\le(e-e(N(u),N(v)))/2$. Summed over edges,
$\sum_{uv}e(N(u),N(v))=\hom(C_4,G)/2$, so the best edge gives

$$
d_{\rm mono}\le\frac p2-\frac{t(C_4)}p=\frac{d(2K_2)+d(P_4)}{6p},
$$

where $t(C_4)$ is the homomorphism density and $d(F)$ the induced density
of $F$ among four independent uniform vertices. The second form uses that
in a triangle-free graph the only four-vertex graphs with a perfect matching
are $2K_2$, $P_4$ and $C_4$, with one, one and two perfect matchings, and
that only $C_4$ contains a four-cycle; hence $p^2=(d(2K_2)+d(P_4)+2d(C_4))/3$
and $t(C_4)=d(C_4)/3$. So (T) holds for every triangle-free $G$ with

$$
d(2K_2)+d(P_4)\le\frac{12}{25}\,p ,
$$

with equality for the balanced $C_5$ blow-up, which has no induced $2K_2$
and $d(P_4)=24/125$. The cut is the classical edge cut used by Erdős,
Faudree, Pach and Spencer and by Balogh, Clemen and Lidický; the
induced-density form is a routine rewriting. Inside the band it fails on
$C_7$, Petersen and Clebsch, whose edge-cut values are $4/49$, $1/10$ and
$27/256$.

**Homomorphism transfer.** Suppose $H$ carries a probability distribution
on its cuts under which every edge of $H$ is uncut with probability at most
$q$. If $\phi\colon G\to H$ is a homomorphism, pulling the cuts back along
$\phi$ leaves each edge of $G$ uncut with probability at most $q$, so
$D_2(G)\le q\,e(G)$. In the Clebsch graph, the even subsets of $[5]$ with
$X\sim Y$ when $|X\triangle Y|=4$, the coordinate cut $j$ leaves uncut
exactly the eight edges with $X\triangle Y=[5]\setminus\{j\}$; the uniform
distribution on the five coordinate cuts gives $q=1/5$. Hence every
triangle-free $G$ with a homomorphism to the Clebsch graph has
$D_2(G)\le e(G)/5$, which is at most $N^2/25$ when $p\le2/5$. When
$p\ge2/5$, the cut of $N(v)$ against the rest, averaged over $v$, gives
$d_{\rm mono}\le p-2p^2\le2/25$ for any triangle-free graph. So (T) holds
for every graph with a homomorphism to the Clebsch graph. The class
contains the three band graphs that defeat the low-root envelopes: $C_7$,
the Petersen graph (the non-neighbours of a vertex of the Clebsch graph)
and the Clebsch graph itself. Each has an optimal cut that is a
pulled-back coordinate cut, which few roots cannot see. The class also contains the
Grötzsch graph, while the Chvátal graph and the Andrásfai graph on eleven vertices,
both above the band, have no homomorphism to it; the evidence checks these
five cases. The circulant $C_{13}(1,5)$ of the Gap section lies inside
the band and has no homomorphism to the Clebsch graph either, since
$D_2=6>e/5$; so the hard band graphs are not confined to this class. The
transfer is an instance of the standard principle that bipartite density is
monotone under homomorphisms into edge-transitive targets; no novelty is
claimed.

**A vertex-minimal counterexample.** Let $G$ violate (T) with $N$ as small as
possible, and with as many edges as possible among such graphs. Then:

1. $G$ is maximal triangle-free, since adding an edge does not decrease
   $D_2$.
2. $G$ is connected, since $D_2$ adds over components and
   $\sum N_i^2\le N^2$.
3. Every vertex has degree above $(4N-2)/25$: deleting $x$ gives
   $D_2(G)\le D_2(G-x)+\lfloor\deg x/2\rfloor$ and
   $D_2(G-x)\le(N-1)^2/25$.
4. $1243/5000<p<3197/10000$, by the density tails.
5. $d(2K_2)+d(P_4)>(12/25)p$, by the edge-cut criterion.
6. $G$ has no homomorphism to the Clebsch graph, by the transfer.

## Route tried: profile envelopes and convex relaxations

The flag-algebra attacks in the literature colour each vertex by its
adjacencies to $k$ random roots, average over the induced type of the
roots, and bound the resulting envelope $U_k\ge d_{\rm mono}$ over the band
by a convex relaxation.
[[research/triangle_free_bipartization/profile_envelope_obstructions|The obstruction record]]
proves two obstructions to this route.

- **Root count.** The envelope exceeds $2/25$ on genuine band graphons for
  $k\le5$: on $C_7$ at one root, on the Petersen graph up to three and on
  the Clebsch graph up to five roots. No relaxation of any order, with any
  constraints valid throughout the band, proves $U_k\le2/25$ on the band
  for $k\le5$. From six roots
  on all three are below $2/25$ ($C_7$ from two, Petersen from four); the
  Clebsch value at seven roots is at most $0.0706$.
- **Linear band.** A convex relaxation containing every triangle-free
  graphon state contains the density-vector mixture of the Higman–Sims
  graphon and the balanced pentagon with weights $5/6$ and $1/6$. Its
  density is $1/4$, strictly inside the band.
  [[theory/extremal_graph_theory/L240_seven_root_linear_band_obstruction/_index|L240]]
  proves $U_7(W_{\rm HS})\ge81/1000$ by exact integer-Gram branch bounds.
  Consequently every such relaxation imposing the band only linearly has
  seven-root envelope slack at least $1/1200$, at every order. This is
  author-recorded tier 0, with no numerical optimality premise. It
  obstructs this envelope, not the bipartization conjecture.

The infeasibility form instead assumes $d_{\rm mono}\ge t>2/25$ and
refutes the per-type inequalities this forces. It needs only one good rule
per graphon rather than a good average, so it excludes the Clebsch graphon
from four roots on. The unrooted version under a linear band still admits
the Higman–Sims mixture through six roots. Exact integer-Gram bounds
prove $m_k>2/25$ for $k\le6$; the stronger numerical optimum reports
are separate and are not needed for that obstruction.

Rooted constraints give a distinct repair. Let $a(r)$ be a root's degree
density and let $m(r)$ be the monochromatic density of the neighbourhood
cut. A graphon with $d_{\rm mono}\ge t$ satisfies

$$
\int\left(a(r)-\frac{11}{50}\right)^2(m(r)-t)\,dr\ge0.
$$

This is an order-five rooted inequality. It vanishes on the regular
Higman–Sims component and is negative on the balanced pentagon for every
$t>2/25$, so it excludes their mixture. The obstruction record gives the
exact calculation. Thus localizing the band is one remedy, not a necessary
condition for every rooted argument.

Two materially different continuations remain: use at least six roots
with band-localized constraints, or combine cuts with rooted multipliers in
the contradiction formulation, the route of the next section. A linear band
is dominated: the localized row $(p-\mathrm{LO})(\mathrm{HI}-p)\ge0$ only
adds a constraint, so a linear-band certificate is also a localized one. No
continuation is shown to prove the universal band inequality.

A related convergence question is provisional. For a fixed twin-free
finite graph $H$, $U_k(W_H)$ decreases to $d_{\rm mono}(W_H)$: with
probability tending to one every part contains a root; the labeled type
then identifies the parts up to an automorphism of $H$, and equal part
weights let a type-specific rule realize an optimal cut. For arbitrary
graphons, including the general weighted-step case, no proof of the needed
pointwise convergence is supplied here. A compactness route additionally
needs continuous envelopes on the compact domain of $[0,1]$-valued
triangle-free graphons, extending the $\{0,1\}$-valued profile definition,
with the same monotonicity and pointwise limit. Under those hypotheses,
a strictly sub-$2/25$ maximum of $d_{\rm mono}$ in the closed band would
be witnessed by $\sup U_k<2/25$ at some finite $k$: the increasing open
sets $\{U_k<2/25\}$ cover the compact band. These hypotheses are not
established here. This gives no certificate, and a numerical plateau in a
relaxation decides neither the convergence premise nor the strict inequality.

## Route tried: localized rooted certificates

[[research/leads/triangle_free_middle_band/_index|The middle-band lead]]
tracks this route and its blocking input. Fix rationals $a<b$, and let
$H(a,b)$ be the hypothesis that $W$ is a triangle-free $\{0,1\}$-valued
graphon with $a\le p(W)\le b$ and $d_{\rm mono}(W)\ge2/25$. Each row
below is a linear functional of induced densities that is nonnegative
under $H(a,b)$.

- **Cut rows.** For $k$ independent uniform roots $R$, a labeled type
  $\tau$ and a rule $c$ on profiles, the profile colouring has
  $\operatorname{mono}(R,c)\ge d_{\rm mono}$. Hence
  $\int f(R)[\tau(R)=\tau](\operatorname{mono}(R,c)-2/25)\,dR\ge0$ for
  every nonnegative multiplier $f$: profile-class sizes and their
  products, squares of rational combinations of rooted densities such as
  $(a(r_i)-c)^2$, and the band factors $p-a$ and $b-p$. A rule may also
  send the points of a class to a side with a fixed probability.
- **Band rows.** $p-a\ge0$, $b-p\ge0$ and $(p-a)(b-p)\ge0$, where $p^2$ is
  the density of two disjoint edges, and their products with squares.
- **Squares.** $\llbracket F^2\rrbracket_\sigma\ge0$ for fixed rational
  combinations $F$ of $\sigma$-flags.

Only the case $W=W_G$ of a finite graph is needed. There each profile class
is a union of parts, so a randomized rule puts a fixed fraction of each part
on each side. The rounding argument of the blow-up identity shows that every
such fractional placement has monochromatic density at least
$2D_2(G)/N^2=d_{\rm mono}(W_G)$, so the randomized rows are valid at
$W_G$.

A *certificate on $[a,b]$* is a nonnegative combination of rows whose
coefficient on every triangle-free graph of some order $\ell$ is negative.
At $W_G$ the combination is an average of these coefficients weighted by
induced densities, hence negative, while each row is nonnegative under
$H(a,b)$. So every triangle-free $G$ with $a\le p\le b$ has
$d_{\rm mono}(W_G)<2/25$. Finitely many certificates whose intervals cover
the closed band, with the tails and the blow-up identity, would prove (T)
for every $G$ with zero error; no limit of errors is needed. Such a
certificate can exist only if the supremum of $d_{\rm mono}(W_G)$ over
triangle-free graphs $G$ with density in $[a,b]$ is below $2/25$: at graphs
whose values approach $2/25$, every cut row is at least a vanishing
negative amount and every other row is nonnegative, so the combination
cannot stay below a fixed $-\varepsilon$. Balanced $C_5$ blow-ups attain
$2/25$ at $p=2/5$, outside the band; the retained band examples stay below
$0.0711$.

The tests below concern $I_1=[3/10,5/16]$, which contains the Petersen,
$C_{13}(1,5)$ and Clebsch graphons.

- **Exact.**
  [[research/triangle_free_bipartization/profile_envelope_obstructions|The obstruction record]]
  proves that cut rows with constant weights on at most four roots fail on
  every interval containing $[4/13,5/16]$, whatever universal or
  band-localized constraints are added. Its witness mixes the
  $C_{13}(1,5)$ and Clebsch graphons. A certificate there therefore needs
  non-constant multipliers or at least five roots; one exhibited five-root
  rule excludes that witness.
- **Linear programs.** At order $\ell\in\{7,8\}$ the discovery program
  uses cut rows on $\ell-2$ roots with multiplier $1$, on $\ell-3$ roots
  times class sizes, and on $\ell-4$ roots times class sizes, the band
  factors $p-a$ and $b-p$, degree squares $(a(r_i)-c)^2$ for six values
  of $c$, and squares of combinations of class sizes. A rule is
  deterministic at the largest root count. At the smaller root counts it
  can also put the zero class on a side with probability $1/4$, $1/2$ or
  $3/4$. The other rows are the band rows and fixed squares: the
  squares of sums and differences of two flags in every flag block of
  order $\ell-1$ or $\ell$ with at most 26 flags, and band-localized
  squares of order $\ell-3$ or $\ell-2$. Cut rows enter by column
  generation over all 107, respectively 410, triangle-free graphs of that
  order. Pricing is exhaustive for types with at most 17 profile classes
  and a local search above that. Squares of class-size combinations are
  proposed only for rules encountered by the search. Thus the thresholds
  below are those found numerically, not proved optima of these row families.
- **Their thresholds.** On $I_1$ the reported threshold is about
  $0.0913$ at order seven and about $0.0891$ at order eight. Squares of
  eigenvectors of the moment matrices at the dual states help little at
  order seven: 25 rounds generated at $t=2/25$ give about $0.0897$, and 40
  rounds generated at $t=0.088$ give about $0.0891$. Yet the dual state at
  $0.088$ then has least moment eigenvalue only about $-3\cdot10^{-7}$,
  while every cut row found by the pricing keeps a positive margin. At order
  eight they help more: three rounds generated at $t=0.088$, with 824
  squares, give about $0.0879$. Eight rounds generated at $t=0.084$, with
  1440 squares, still leave the program infeasible there, its margin
  closing only from $-8.5\cdot10^{-5}$ to $-5.6\cdot10^{-5}$. Products of
  two three-root cut rows on the
  same roots, valid under the hypothesis, leave the order-seven value at
  about $0.0913$. At order seven the program reports about $0.0904$
  on $[0.31,0.3197]$, beside the dense tail, about $0.0925$ on
  $[0.2486,0.26]$, beside the sparse tail, and about $0.0906$ on the narrow
  interval $[0.3075,0.3080]$, so narrowing the interval does not close the
  gap. Every one of these thresholds exceeds $2/25$ by between about
  $0.008$ and $0.013$.
- **Diagnosis.** In the same floating-point setting, every mixture of
  eleven genuine graphons with density in $I_1$ violates some order-seven
  row at $2/25$. The eleven are $C_{13}(1,5)$, Clebsch, Petersen, two
  $C_5$ blow-ups with an added isolated part, and two reweightings of each
  of the first three. The dual states are not such mixtures: at orders
  seven and eight their flag moment matrices have negative eigenvalues. So
  fixed squares do not enforce full flag positivity on these vectors.
  This identifies missing constraints, but does not prove that positivity
  is the only missing ingredient: some cut pricing is non-exhaustive, and
  the library of genuine graphons is finite. Whether full positivity closes
  $I_1$ at these orders is not decided here. The nearly positive order-seven
  vector is a recovery candidate, not an obstruction. An exactly positive
  semidefinite state satisfying every declared cut row at a threshold above
  $2/25$ would obstruct that finite system. No such state is retained.

The linear programs are discovery runs in floating point, reproduced by
the discovery program described on
[[research/triangle_free_bipartization/evidence/_index|the evidence page]].
Their outputs certify nothing: a positive outcome would have to be
recovered as an exact rational certificate and checked in rational
arithmetic. These finite searches yield neither a zero-error certificate
nor a family of valid errors tending to zero. They do not exclude further
cut rules, other fixed rational squares or full flag positivity.

The failed proof step is the contradiction to $H(a,b)$. For constant-weight
rows on at most four roots, the exact in-band mixture proves that no such
contradiction exists on intervals containing $[4/13,5/16]$, even after
adding every convex constraint valid on all band graphons. For the richer
rooted system the needed contradiction is unknown, not refuted. Thus the
exact obstruction and the numerical failures compose with the sketch as
limitations on a proof method; neither composes with the density tails to
give (T).

## Route: states coloured by a maximum cut

This route keeps the cut inside the state instead of reconstructing it from
roots. Its objective is $d_{\rm mono}$ itself, so there is no envelope to
pay for, and it is the route of the
[[research/leads/triangle_free_middle_band/_index|middle-band lead]]. Everything in this section is by Plasma AI and author-recorded.
The flag computations of the two held sources, the local cuts of Balogh,
Clemen and Lidický and Ferudun's per-root envelopes, colour points by their
adjacencies to roots only; this comparison with two sources does not
establish novelty.

**The coloured state.** Let $G$ be triangle-free on $N$ vertices and let
$\chi$ be a maximum cut, a colouring of $V(G)$ with $D_2(G)$ monochromatic
edges. Colour each part of $W_G$ by $\chi$. A measurable colouring of
$W_G$ puts a fraction $t_i$ of part $i$ on colour $1$, and its monochromatic
density

$$
\frac2{N^2}\sum_{ij\in E(G)}\bigl(t_it_j+(1-t_i)(1-t_j)\bigr)
$$

is affine in each $t_i$, since no edge lies inside a part. So a vertex of
$[0,1]^N$, a cut of $G$, does at least as well, and the part-constant
colouring $\chi$ is optimal among all measurable colourings of $W_G$. Sample
$\ell$ independent uniform points; with their colours they induce a
vertex-2-coloured triangle-free graph, since two points of one part are
non-adjacent and share a colour. Let $\phi_\ell(H)$ be the probability of
each coloured graph $H$ of order $\ell$, up to colour-preserving
isomorphism. The objective is

$$
m(\phi)=\Pr[x_1\sim x_2,\ \chi(x_1)=\chi(x_2)]=\frac{2D_2(G)}{N^2}
=d_{\rm mono}(W_G).
$$

**Rows valid at every such state.** Each is a linear functional of
$\phi_\ell$, written as an expectation over independent points.

*Vertex stability.* For a point $x$ put
$\sigma(x)=\int W(x,y)\bigl(1-2[\chi(x)=\chi(y)]\bigr)\,dy$, the density
of opposite-coloured minus same-coloured neighbours. Recolouring the part of
$x$ changes the monochromatic density by $2\sigma(x)/N$, so $\sigma(x)\ge0$
at every point. Hence $\mathbb E_x[\sigma(x)F(x)]\ge0$ for every
one-rooted coloured flag $F$, and $\sigma$ times the square of any
combination of one-rooted flags is nonnegative too.

*Switching.* For roots $r=(r_1,\dots,r_k)$, the cell $c_r(x)$ of a point is
its colour together with its adjacencies to $r_1,\dots,r_k$. For a set $S$
of cells, write $s_r(x)=1$ if $c_r(x)\in S$ and $0$ otherwise. Recolouring
every point with $s_r(x)=1$ gives another measurable colouring, so the
change of monochromatic density

$$
\Delta_S(r)=\mathbb E_{x,y}\Bigl[W(x,y)\bigl(1-2[\chi(x)=\chi(y)]\bigr)
\,\bigl|s_r(x)-s_r(y)\bigr|\Bigr]
$$

is nonnegative for every $r$. Hence $\mathbb E_r[\Delta_S(r)F(r)]\ge0$ for
every $k$-rooted coloured flag $F$. Choosing the resulting colour independently
of the old colour recovers a profile recolouring of the previous route;
general switchings keep or flip the existing colours separately in each
profile class. A switching inside one
colour class is implied by vertex stability, since its change is
$2\int_T\sigma+2\iint_{T\times T}W\ge0$ for the recoloured set $T$.
Products of two of these pointwise nonnegative quantities, such as
$\sigma(r_1)\Delta_S(r)$, are valid rows as well.

Fractional switching probabilities give further valid rows. Put
$J(x,y)=W(x,y)(1-2[\chi(x)=\chi(y)])$ and independently flip a vertex in
cell $c$ with probability $q_c\in[0,1]$. The expected change is

$$
\mathbb E_{x,y}J(x,y)
\bigl(q_{c_r(x)}+q_{c_r(y)}-2q_{c_r(x)}q_{c_r(y)}\bigr)\ge0.
$$

For finite graphs this follows by averaging actual cuts; for their weighted
blow-ups it follows by splitting independent twin classes. Boolean $q$
recovers the deterministic switching row. Searching only Boolean switches
does not exhaust this family.

*Gain-weighted squares.* Let $f_c(r)$ be the mass of the cell $c$ of the
root tuple, and let $\tau$ specify its coloured induced type. Pointwise
nonnegativity also gives

$$
K_{\tau,S}=\mathbb E_r[1_\tau(r)\Delta_S(r)
                 f(r)f(r)^{\mathsf T}]\succeq0.
$$

Indeed its quadratic form is the expectation of $\Delta_S$ times a square.
This uses $k+4$ sampled points: the $k$ roots, two edge endpoints and two
independent cell samples. It is available for two roots at order six and
three at order seven. Ordinary flag positivity and entrywise nonnegativity
of the gains do not by themselves supply this conditional positivity.

*Band and positivity.* The band rows of the previous section and the flag
moment matrices of every coloured type, including those localized by
$\sigma$, $p-a$ and $b-p$.

*Hereditary comparison.* Suppose the uniform all-order bound
$2D_2(H)\le B|V(H)|^2$ is available for every triangle-free $H$.
The [[research/graph_ramsey_interfaces/homogeneous_triangle_deletion_bounds|homogeneous transfer]]
supplies $B=4/47$ from Balogh, Clemen and Lidický's Theorem 2, at the
source standing recorded there. Let $\chi$ be a maximum cut of $G$, and
let $U\subseteq V(G)$. Recolour $U$ by a maximum cut of $G[U]$, choosing
its two orientations with equal probability. Write $M_U$ for the old
monochromatic edges inside $U$, $M_\partial$ for those across its boundary,
and $e_\partial$ for all boundary edges. Optimality gives

$$
M_U+M_\partial\le D_2(G[U])+e_\partial/2.
$$

If $C_U$ is the number of old bichromatic edges inside $U$ and
$\sigma_v$ is the unnormalised vertex slack, then
$2C_U-\sum_{v\in U}\sigma_v
=2M_U+2M_\partial-e_\partial$. Consequently

$$
\sum_{v\in U}\sigma_v-2C_U+B|U|^2\ge0. \tag{H}
$$

For a union $U(r)$ of coloured profile cells, put $s_r=1_{U(r)}$ and
$J(x,y)=W(x,y)(1-2[\chi(x)=\chi(y)])$. Dividing (H) by $N^2$ gives the
pointwise rooted row

$$
R_B(r)=\mathbb E_{x,y}\left[
\frac{s_r(x)+s_r(y)}2J(x,y)
+\bigl(B-W(x,y)[\chi(x)\ne\chi(y)]\bigr)s_r(x)s_r(y)
\right]\ge0.
$$

It uses $k+2$ points for $k$ roots. Nonnegative rooted multipliers and
gain-weighted square blocks apply to $R_B$ as well. For $U=V(G)$ it reduces
to $B-d_{\rm mono}\ge0$; proper subsets compare the old cut with a best cut
inside an induced graph, going beyond deterministic profile switching.
For the step graphon of $G$ a profile union is a union of whole vertex
parts, so the finite proof applies exactly and introduces no sampling error.
These rows depend on the uniform bound $B$ just stated. The desired
$B=2/25$ cannot be substituted without a separate argument establishing it.
Hereditary comparison is strictly stronger than two-root switching stability
in the needed sense: the
[[research/triangle_free_bipartization/two_root_switching_traps|two-root trap page]]
exhibits root parts $(2,3)$ and subset mask $41$ for which $R_{4/47}$ has
limiting value $-1077/1540096$, despite stability under every deterministic
two-root switch. The finite exact calculation is retained in the evidence.

**Certificate.** Suppose nonnegative multipliers $\lambda_i$ on such rows,
positive semidefinite matrices $Z_b$ on the moment blocks $M_b$, and a
constant $\mu\le2/25$ satisfy
$m(H)+\sum_i\lambda_i\,\mathrm{row}_i(H)+\sum_b\langle Z_b,M_b(H)\rangle
\le\mu$ for every coloured triangle-free graph $H$ of order $\ell$.
Averaging over $H$ with weights $\phi_\ell(H)$, every added term is
nonnegative, so $d_{\rm mono}(W_G)\le\mu$ for every triangle-free $G$ with
$a\le p\le b$, that is $D_2(G)\le N^2/25$. Finitely many intervals
covering the band, with the tails, would prove (T). The bound is the
objective itself: no strict margin, error term or envelope enters.

**An alternative full-solution interface: uniform contraction.** Hereditary
comparison also permits a route through a sequence of uniform errors, if
one can prove the following additional certificate. Put $b_0=2/25$ and
$B_0=4/47$. On each of finitely many intervals covering the open band,
seek fixed nonnegative multipliers and positive semidefinite dual matrices
whose coefficient on every coloured graph $H$ is an affine function
$g_H(B)$ of the hereditary parameter $B$. It suffices to find
$0\le\rho<1$ such that

$$
g_H(b_0)\le b_0,\qquad
g_H(B_0)\le b_0+\rho(B_0-b_0) \quad\text{for every }H. \tag{C}
$$

The coefficients include the objective, as in the preceding certificate.
Their affineness makes the two endpoint checks imply
$g_H(B)\le b_0+\rho(B-b_0)$ for every $B\in[b_0,B_0]$.
The matrices and multipliers are fixed on each interval; the same $\rho$
may be taken as the largest of its finitely many interval values.

To see why this would finish the problem, assume the uniform all-order bound
$m\le B$ is available. It validates the hereditary rows at that $B$.
The certificate gives $m\le b_0+\rho(B-b_0)$ throughout the band, and the
source tails give $m\le b_0$ outside it. Starting with the available
$B_0$, induction therefore gives, for every finite triangle-free graph,

$$
m\le B_j=b_0+\rho^j(B_0-b_0)\qquad(j\ge0).
$$

Letting $j$ tend to infinity proves $m\le b_0$ at every order. Checking
(C) at $b_0$ is an algebraic endpoint check, not an assumption that the
conjecture already holds. Each invocation of the hereditary comparison uses
the preceding established bound $B_j$. This route has zero limiting error;
one isolated positive-error certificate would not suffice. No certificate
satisfying (C) with $\rho<1$ is presently supplied, on one interval or on
the full band. Establishing such a certificate, with all positivity
hypotheses and endpoint inequalities exact, is the missing step of this
alternative argument.

**A finite extremal reduction with additional equalities.** There is a
stronger sufficient system for the full target. It uses a mixture of maximum
cuts of one weighted graph at an optimum over vertex weights. It does not
assert these extra equalities for an arbitrary maximum cut.

Let $F$ be a finite triangle-free support and let $w_i\ge0$,
$\sum_iw_i=1$. For a colouring $\chi$, put

$$
m_\chi(w)=\sum_{i,j}w_iw_j A_{ij}[\chi_i=\chi_j],\qquad
m_F(w)=\min_\chi m_\chi(w).
$$

This is the monochromatic density of its weighted blow-up. It is continuous,
so it attains a maximum $B$ on the weight simplex. If any graph violates
(T), its support has such a maximum with $B>2/25$. Remove the zero-weight
vertices of a maximizing $w$. Rational weights are represented by integer
blow-ups with possibly unequal part sizes. A minimum cut can be chosen
constant on each independent twin class: with the other classes fixed,
its cost is linear in that class's two colour masses, so moving all its
mass to an endpoint cannot increase the cost. Applying the source's
all-order bounds to these blow-ups and then taking rational approximations
extends them to real weights. Thus $B\le4/47$ and this weighted graph has
density in the closed interval
$[1243/5000,3197/10000]$. Indeed a density strictly outside that interval,
together with $B>2/25$, would persist under close rational approximation
and contradict the source tails. A finite closed-interval cover of the
open band covers its closure as well.

There is a probability distribution $\lambda$ on the cuts active at $w$
(those with $m_\chi(w)=B$) such that, for every retained vertex $i$,

$$
\mathbb E_{\chi\sim\lambda} u_\chi(i)=B,
\qquad
u_\chi(i):=\sum_j A_{ij}w_j[\chi_i=\chi_j]. \tag{E}
$$

Here is a finite proof. Every vector $u_\chi$ for an active cut satisfies
$w\cdot u_\chi=B$. If $B\mathbf1$ were outside their convex hull, let $z$
be its nearest point in that compact hull and set $h=z-B\mathbf1$.
The closest-point inequality gives
$h\cdot(u_\chi-B\mathbf1)\ge\|h\|^2>0$ for every active cut. The direction
$d=h-(\sum_i h_i)w$ has $\sum_i d_i=0$ and
$d\cdot u_\chi=h\cdot(u_\chi-B\mathbf1)>0$. Since all retained weights are
positive, $w+\varepsilon d$ stays in the simplex for small positive
$\varepsilon$. The derivative of each active $m_\chi$ is
$2d\cdot u_\chi>0$; the finitely many inactive cuts have a positive gap at
$w$ and remain above $B$ for small enough $\varepsilon$. This increases
$m_F$, a contradiction. Thus $B\mathbf1$ lies in the hull, giving (E).
The distribution may also be averaged with its colour complement.

Vertex stability says $u_\chi(i)\le d(i)/2$ for each active cut. Averaging
in (E) therefore gives the additional pointwise condition $d(i)\ge2B$.
It may be multiplied by nonnegative coloured rooted flags, since the degree
bound concerns the underlying graph and holds for every active colouring.

For any rooted function $f(i)$ depending only on the uncoloured weighted
graph, (E) gives the exact equality

$$
\mathbb E_{\chi,i,j}
 [W(i,j)[\chi_i=\chi_j]f(i)]-B\mathbb E_i f(i)=0. \tag{E_f}
$$

In particular $f$ can be any uncoloured rooted flag density. A rooted flag
on $\ell-1$ points, with an additional endpoint $j$, gives a row on
$\ell$ points, affine in $B$. Both signs of the row may be used. A
colour-dependent multiplier is not justified by (E), and cannot be inserted
in this equality without a further argument.

Every active cut is a genuine maximum cut at $w$, so all ordinary
optimality rows and moment blocks remain valid after averaging over
$\lambda$. The hereditary comparison (H) is valid with this same $B$ as
well: every normalized induced reweighting has the support $F$ and hence
has monochromatic density at most the defining maximum $B$. This use of
$B$ does not assume a uniform bound for all triangle-free supports.

The comparison also holds for fractional selection of the profile cells.
For $0\le q_i\le1$, split vertex $i$ into two independent twins of weights
$q_iw_i$ and $(1-q_i)w_i$. A maximum cut may be chosen constant on each
original twin class, since its cost is linear in that class's two colour
masses when the other classes are fixed. Thus the old maximum cut remains
optimal on the split graph. Select the first twin of each vertex and apply
the same recolouring argument as for (H). In the formula for $R_B$, replace
$s_r$ by $q_r\in[0,1]$; its validity is unchanged. The same conclusion holds
for the earlier uniform-bound version of (H), after extending that bound to
weighted graphs by rational approximation. Searching only Boolean profile
unions does not exhaust these valid fractional rows.

**Proper-support comparison at the target constant.** The counterexample
reduction can be strengthened further. Among all finite weighted
triangle-free graphs with $m_F(w)>b_0=2/25$, choose a support $F$ of least
order, and then maximize $m_F$ over its weight simplex. The resulting
maximum $B>b_0$ has no zero-weight vertex: deleting such a vertex would
give a smaller weighted counterexample. Every proper subset of the
support, with *any* normalized nonnegative weights, satisfies the target
$m\le b_0$, by the choice of $F$. This is a conditional minimality
argument, not an assumption that the target holds on arbitrary induced
sets of an arbitrary graph.

For this extremizer, whenever a selection $q_i\in[0,1]$ vanishes on at
least one support vertex, its normalized selected support is proper.
The hereditary comparison is therefore valid at $b_0$ itself:

$$
R_{b_0}(q)=\mathbb E_{x,y}\!\left[
 \tfrac12(q_x+q_y)W_{xy}(1-2[\chi_x=\chi_y])
 +(b_0-W_{xy}[\chi_x\ne\chi_y])q_xq_y
\right]\ge0. \tag{P}
$$

Zero selected mass makes the row zero. Otherwise the proof is the same
recolouring argument as (H), with the justified bound on the smaller
support. Splitting twins for a fractional selection does not alter this
reason: its selected weights are still represented on that proper subset
of the original $F$.

There are two useful ways for a rooted profile rule to certify properness.
It can assign selection zero to the cell containing a named sampled root;
this omits that root's positive-weight support vertex. Alternatively it can
assign zero to all cells adjacent to that root and opposite to it in one
of the active cuts. Vertex stability gives that cross-neighborhood mass
at least $d(r)/2\ge B>0$, so it too omits a nonempty support subset.
Both justifications survive repeated root samples. Root cells are computed
from the actual root colours and root adjacencies, including zero adjacency
to the root itself. An arbitrary cell cannot be declared nonempty.

The same properness condition gives a stronger partial-cut comparison:
if the recursively treated part $U$ is proper, its bound in the following
construction may be $b_0$, giving

$$
\alpha(z,1_U)+b_0s^2-m\ge0. \tag{P'}
$$

Here every forced excluded cell is assigned an outside colour. This is a
$B$-independent inequality on a state carrying the old cut; at the
extremizer $m=B$. For several recursive parts, each must separately have
proper support before replacing all their bounds by $b_0$.
The paired-cut program's `--minimal-support` option uses (P) and (P')
with root-cell or either cut's cross-neighborhood exclusions. These rows
may enter (C) or $(C_d)$ without a derivative in $B$. They require the
least-support reduction, and are not asserted for a general weighted
extremum of a prescribed support. No certificate follows from minimality
alone.

Consequently a certificate of the endpoint form (C), augmented by
$(E_f)$ and the equality $m=B$, with $\rho<1$ throughout the band, would
also prove (T). Applied to a hypothetical weighted counterexample above,
it gives $B\le2/25+\rho(B-2/25)$, contradicting $B>2/25$. This is a finite
reduction and needs neither an extremal graphon nor a compactness theorem.
The missing object is still an exact full-band certificate; the reduction
and the equalities alone supply none. They are author-recorded arguments.

**Recursive partial cuts.** The same extremal parameter permits a comparison
that also changes the cut outside the recursively treated set. Partition
the weighted vertex space into $A_-$, $A_+$ and $U$. Fix the two outside
parts on opposite sides, use an optimal cut of the subgraph on $U$, and
choose its global orientation uniformly. Put $u=1_U$, let $z$ be $-1$
on $A_-$, $1$ on $A_+$ and $0$ on $U$, and write $s=\int u$.
The resulting expected monochromatic density is at most

$$
\alpha(z,u)+Bs^2,\qquad
\alpha(z,u)=\frac12\iint W(x,y)
 \bigl(1+z(x)z(y)-u(x)u(y)\bigr)\,dx\,dy.
$$

Indeed the integrand counts fixed outside edges with their actual colours,
counts edges from $U$ to its complement with probability $1/2$, and
leaves internal $U$ edges to its optimal cut. The normalized induced
reweighting has monochromatic density at most $B$. Since the original
weighted graph has $m=B$, every such partial cut therefore satisfies

$$
\alpha(z,u)-B(1-s^2)\ge0.
$$

For a hypothetical counterexample $B>b_0=2/25$, this implies the
parameter-free induction row

$$
\alpha(z,u)-b_0(1-s^2)
 \ge (B-b_0)(1-s^2)\ge0. \tag{I}
$$

The term at $U=V$ is identically zero. No claim that $b_0$ already bounds
the induced subgraph is used: the bound on that subgraph is $B$, and the
last inequality follows from $B>b_0$. A direct vertex-minimal
counterexample argument gives the same necessary row for deterministic
finite partitions, using the target on every proper induced subgraph.

For a rooted profile rule, assigning each cell one of the labels $-1,0,1$
gives a row on $k+2$ sample points. Nonnegative rooted multipliers and
positive semidefinite blocks localized by (I) are valid. An exact negative
coefficient combination on a finite cover of the whole band would refute
every hypothetical counterexample and prove (T); it would have zero final
error. This does not require the two-cut system. In a state carrying a
maximum cut $\chi$, another valid affine row is

$$
\mathbb E\!\left[
 \tfrac12 W_{xy}(1-2[\chi_x=\chi_y])
 +\tfrac12W_{xy}z_xz_y
 +(B-\tfrac12W_{xy})u_xu_y\right]\ge0.
$$

It compares the same partial construction with the old cut, and can enter
the parameter certificates (C) or $(C_d)$. A fractional assignment of
profile mass is justified by splitting independent twins before applying
the construction. Paired-cut discovery uses deterministic ternary
assignments for this family. Uncoloured induction discovery also permits
several recursive parts and outside coins of biases $1/4,1/2,3/4$.
Neither search exhausts all fractional assignments.

There may also be several recursive parts $U_1,\ldots,U_r$, whose optimal
cuts receive independent random orientations. Replace $u_xu_y$ by
$\sum_j1_{U_j}(x)1_{U_j}(y)$ in $\alpha$ and replace $s^2$ by
$\sum_j s_j^2$, where $s_j$ is the mass of $U_j$. The same argument gives

$$
\alpha-b_0\left(1-\sum_j s_j^2\right)
\ge (B-b_0)\left(1-\sum_j s_j^2\right)\ge0. \tag{I_r}
$$

In particular, with no fixed outside vertices and two recursive parts,
every subset $U$ satisfies the expansion condition
$\int_{U\times U^c}W\ge2B\,s(1-s)$, and hence the same condition with
$B$ replaced by $b_0$. Products of two induction rows on the same roots,
or of an induction row with a rooted degree surplus $d(r_i)-2b_0$, are
nonnegative at a hypothetical weighted counterexample. These rows have
their stated extremal hypothesis; they are not inequalities for every
triangle-free graph.

**Lifting to additional roots.** A valid order-eight coefficient row $r$
has the order-nine lift

$$
(Lr)(H)=\frac19\sum_{v\in V(H)}r(H-v).
$$

Its value on the induced density vector of any weighted graph is exactly
the old value: delete a uniformly chosen slot from nine independent samples.
Thus nonnegativity, localizing hypotheses and the density convention are
preserved without an error term. This permits larger systems without
discarding the recursive-induction rows already constructed.

One genuinely additional row specifies a labeled seven-root type $\tau$
and a binary profile rule $c:\{0,1\}^7\to\{0,1\}$. Under the hypothetical
counterexample, every such cut has monochromatic density at least
$B>b_0$, so

$$
\mathbb E_r\!\left[1_\tau(r)
 \left(\mathbb E_{x,y}W_{xy}[c(p_r(x))=c(p_r(y))]-b_0\right)\right]
\ge0. \tag{J_7}
$$

Its coefficient on a nine-vertex graph is the average over its $9!$
labelings, using seven root slots and the remaining two endpoint slots.
For each seven-element subset, only isomorphisms from $\tau$ to that
induced subgraph contribute. Enumerating those embeddings and both
endpoint orders gives the same coefficient without storing all labelings.
The program retains integer numerators with denominator $25\cdot9!$.
Repeated underlying vertices in the independent sample cause no exception:
they yield an ordinary triangle-free graph on the nine labeled slots,
which remains in the coefficient universe.

A recursive alternative uses a labeled seven-root type $\tau$ containing
an induced pentagon on a specified five-element root set $T$. A vertex's
neighborhood in that pentagon is independent, so it has eleven possible
profiles: the empty set, five singletons and five independent pairs. Assign
each profile to fixed colour $0$, fixed colour $1$, or one recut part $U$.
Let $z_T(x)$ be $-1,1,0$ respectively, and let $u_T(x)=1$ exactly on $U$.
The pointwise recursive inequality $(I_r)$ gives

$$
\mathbb E_r1_\tau(r)\,\mathbb E_{x,y}\left[
 \frac{W_{xy}}2
   (1+z_T(x)z_T(y)-u_T(x)u_T(y))
 -b_0(1-u_T(x)u_T(y))\right]\ge0. \tag{J_{5\mid7}}
$$

The extra two roots specify a nonnegative multiplier of the five-root
comparison. Their adjacencies impose no additional assumption: the inner
comparison is nonnegative for every actual five-root tuple. All
$3^{11}$ assignments form a finite family, and every induced pentagon
subset of each seven-root type may be used. Multiplying the displayed
integrand by $50$ gives the integer
$25W_{xy}(1+z_T(x)z_T(y)-u_T(x)u_T(y))
-4(1-u_T(x)u_T(y))$. Thus the existing seven-root embedding table gives
integer coefficient numerators with denominator $50\cdot9!$. This
family includes one independently recut part and deterministic outside
colours; it does not exhaust recursive assignments or richer multipliers.

The new ordinary flag-square bases have one root and five-vertex flags,
or three roots and six-vertex flags. Their two extension sets are disjoint
as sets of sample slots, so they use nine slots and give positive
semidefinite matrices by conditional independence given the roots.
Further nine-point matrices multiply squares of linear combinations of
one-rooted four-vertex flags by a one-root recursive comparison $(I_r)$,
or by either band surplus $p-p_0$ and $p_1-p$. There is one root, three
extension slots for each flag factor, and two slots for the comparison.
Conditioning on the root leaves a nonnegative comparison times a square.
For the recursive comparison, the two root-adjacency cells may each have
outside colour bias in $\{0,1/4,1/2,3/4,1\}$ or belong to one of two
independently recut parts. This finite grid does not exhaust fractional
part assignments. The two endpoints can be unordered because each
comparison is symmetric in them. Averaging over the root, endpoint pair
and first three-element extension set therefore uses
$9\binom82\binom63=5040$ choices; the other extension set is their
complement. Integer incidence counts give the coefficients exactly before
conversion to floating arithmetic for discovery.
The nine-vertex universe is generated exhaustively by extending each
eight-vertex triangle-free graph with every independent neighborhood;
exact isomorphism tests remove duplicates. The discovery program
`produce_lifted.py` combines these squares and $(J_7)$ with lifted
order-eight rows, with $(J_{5\mid7})$ as an optional additional family.
Its cut and square pricing is incomplete. A negative
exact coefficient combination throughout the whole band would finish the
same counterexample argument; no such combination is supplied here.

**Two active cuts.** The weighted-extremal reduction permits another
strengthening. Draw $\chi$ and $\psi$ independently from the balanced
active-cut distribution $\lambda$, conditional on the same weighted graph.
Use the four vertex colours $(\chi_i,\psi_i)$. For any rooted function
$f(i,\psi)$ depending on the graph and on the second cut, but not on the
first cut, conditional independence and (E) give

$$
\mathbb E_{\chi,\psi,i,j}
 [W(i,j)[\chi_i=\chi_j]f(i,\psi)]
 -B\mathbb E_{\psi,i}f(i,\psi)=0. \tag{E_2}
$$

The corresponding equality with the cuts exchanged also holds. Thus the
uncoloured flags in $(E_f)$ can be replaced by flags coloured by the other
cut in this four-colour system. Arbitrary multipliers depending on both
cuts are still not justified for $(E_2)$.

Both cuts have monochromatic density exactly $B$ individually. Consequently
$(m_\chi-B)F=(m_\psi-B)F=0$ for every flag function $F$ of the two-cut
state; these give further sampled equalities. Each cut separately satisfies
vertex stability, switching and hereditary comparison. Its profile cells
may now use both cut colours, so even a switching without roots can use the
four intersections of the two cuts. Ordinary and gain-weighted flag
positivity remain valid under the average over the cut pair. The state is
invariant under independently complementing the two cuts and exchanging
them, a group of eight colour transformations. Arbitrary permutations of
the four colours need not preserve the meaning of the two cuts and are not
allowed as symmetries.

A coefficient certificate valid for all these states, with the endpoint
and positivity checks of (C), would again exclude every hypothetical
weighted counterexample with $B>2/25$. This specifies a richer full-target
system; no such exact certificate is supplied here.

Independence of the cuts also gives a second family of positive semidefinite
matrices, distinct from vertex-sampling flag positivity. Fix a sampled
vertex tuple $r=(r_1,\ldots,r_\ell)$ and write $q_\alpha(r)$ for the
probability that an active cut drawn from $\lambda$ has colour pattern
$\alpha$ on this tuple. For any uncoloured induced type $\tau$,

$$
C_\tau[\alpha,\beta]
=\mathbb E_r[1_\tau(r)q_\alpha(r)q_\beta(r)]\succeq0. \tag{CP}
$$

The entries are linear functionals of the four-colour state on just
$\ell$ vertices: the two patterns are supplied by the two independent
cuts on the same vertices. The matrix is an average of nonnegative
rank-one matrices. Global complementation permits patterns to be grouped
into complementary pairs, using a basis of size $2^{\ell-1}$. For every
copositive matrix $A$ on this basis, meaning $x^{\mathsf T}Ax\ge0$ for
all vectors $x\ge0$, the stronger scalar inequality
$\langle A,C_\tau\rangle\ge0$ also holds. No unverified copositivity
hypothesis may be used in such a row.

One copositive family has an elementary exact warrant. Let $T$ be any
triangle-free graph on the cut patterns. Then $A=J-2A_T$ is copositive.
To prove this, for nonnegative
weights $x$ of total mass $s$, the quadratic form is
$s^2-4\sum_{ij\in E(T)}x_ix_j$. The weighted edge sum of any triangle-free
support is at most $s^2/4$: if two nonadjacent vertices have positive
weight, transferring their combined weight to one of them can only increase
or preserve the edge sum, because it is affine in that transfer. Repeating
leaves a clique, of size at most two, whose edge product is at most
$s^2/4$. This proves copositivity without a numerical test. With five single
patterns and $T=C_5$ this is the five-cycle Horn matrix. Partitioning the
patterns into five groups and joining consecutive groups also gives a
triangle-free $T$. Finding a profitable grouping by local search does not
certify that all such groupings, or all copositive matrices, have been
tested. A bounded search over all triangle-free graphs on the pattern
basis can propose further rows: each returned graph must be checked for
triangles, but its validity requires no numerical optimality claim.
Nonnegative diagonal congruences are valid as well: for $a_i\ge0$,
$\operatorname{diag}(a)(J-2A_T)\operatorname{diag}(a)$ is copositive
by applying the same proof to weights $a_ix_i$. Optimizing these weights
does not add an unproved positivity assumption. A search restricted to
unit weights does not exhaust this scaled family.

**Joining the systems through a common marginal.** The uncoloured and
paired-cut routes may be combined without enumerating every coloured graph
on nine vertices. At the same hypothetical least-support weighted
extremizer, let $Y$ be its uncoloured nine-point density vector and $Z$ its
five-point vector carrying two independent active cuts. Let $\pi$ average
the $\binom95=126$ five-point subgraphs of a nine-point graph, and let
$\kappa$ forget both cut colours. These rational linear maps satisfy

$$
\pi Y=\kappa Z. \tag{M}
$$

Both sides are the ordinary five-point density vector of the underlying
weighted graph. Thus the separate relaxations cannot choose unrelated
uncoloured marginals.

Some weighted-extremal constraints can also be made independent of the
unknown parameter $B$. If $F_\psi(0,1,2)$ is any three-point rooted flag
function using only the other cut $\psi$, then

$$
\mathbb E\!\left[
 \bigl(W_{03}[\chi_0=\chi_3]-W_{34}[\chi_3=\chi_4]\bigr)
 F_\psi(0,1,2)\right]=0. \tag{E_0}
$$

For the first term, average (E) in $\chi$ with the independently chosen
$\psi$ fixed. For the second, integrate sample slots $3,4$ first; every
active $\chi$ has monochromatic density $B$. Both terms therefore equal
$B\mathbb E F_\psi$. Similarly, for every nonnegative three-point flag
$F_{\chi,\psi}(0,1,2)$, even one using both cuts,

$$
\mathbb E\!\left[
 \bigl(W_{03}-2W_{34}[\chi_3=\chi_4]\bigr)
 F_{\chi,\psi}(0,1,2)\right]\ge0, \tag{D_0}
$$

because integration of slots $3,4$ gives $d(0)-2B\ge0$.
This pointwise inequality also gives a matrix condition. For any linear
combination $f$ of one-rooted two-point flags using both cuts,

$$
\mathbb E\!\left[
 (W_{03}-2W_{34}[\chi_3=\chi_4])f(0,1)f(0,2)
\right]\ge0. \tag{D_{0,\mathrm{sq}}}
$$

After integrating slots $3,4$ and the two independent flag extensions,
the integrand is $(d(0)-2B)(\mathbb E_1f(0,1))^2$. Thus the full matrix
on this flag basis is positive semidefinite. The same construction works
with the scalar multipliers $B-b_0$, $B_0-B$, and the nonnegative padding
surplus $(400/1243)p-B$ proved below. Their five-point realizations use
the disjoint edge on slots $3,4$. These are additional localized square
conditions, rather than consequences asserted from entrywise flag
inequalities alone. The combined program also retains the one-root
hereditary square blocks at the uniform source bound $B_0$.
The remaining balance rows with nonnegative larger flags give interval
consequences: if $L=BF$ in expectation and $F\ge0$, retain
$L-b_0F\ge0$ and $B_0F-L\ge0$. The scalar degree rows retain
$d-2b_0\ge0$. These use $b_0<B\le B_0$; they do not set $B=b_0$.
The source-bound hereditary comparisons use $B_0$, and the target-bound
proper-support comparisons keep their explicit exclusions.

One additional interval consequence follows from isolated padding. Put
$p_0=1243/5000$. For any weighted graph with $p\ge p_0$, scale all its
vertex weights by $t=\sqrt{q/p}$, where $0<q<p_0$, and give the remaining
mass to an isolated vertex. Both $p$ and $m$ scale by $t^2$. Rational
approximation stays inside the sparse range, so the source bound gives
$m\le b_0p/q$. Taking $q\uparrow p_0$ yields

$$
m\le\frac{b_0}{p_0}p=\frac{400}{1243}p. \tag{IP}
$$

This applies throughout the hypothetical counterexample band. For an
active cut its monochromatic density is $B$, so multiplying
$(400/1243)p-B\ge0$ by a nonnegative flag on disjoint sample slots
gives another valid row. The program uses three-point flags carrying both
cuts and a separate edge pair. This use retains the condition $p\ge p_0$.

The two components admit a stronger direct comparison as well. Choose a
binary profile cut rule for every canonical seven-root type. Given seven
random roots, identify their type, choose a uniformly random isomorphism
to its canonical representative, and use that representative's rule on
the whole graph. This is a distribution of actual cuts. If $C$ is its
nine-point monochromatic-cost vector and $c_m$ the paired objective, then

$$
C\cdot Y-c_m\cdot Z\ge0. \tag{GC}
$$

Indeed every output cut costs at least the optimum $B=c_m\cdot Z$.
This uses the actual optimum rather than replacing it by $b_0$. In the
seven-root embedding table, a canonical type $\tau$ receives multiplicity
$7!/|\operatorname{Aut}(\tau)|$. Multiplying its embedding counts by
this integer, summing the costs of all type-specific rules, and dividing
by $9!$ gives $C$. The same multiplicities make the total sampling mass
exactly one on every nine-vertex graph. Random canonicalization makes the
construction valid even when a rule is not invariant under the type's
automorphisms. Each comparison has one shared nonnegative multiplier on
its two components; they are not asserted separately nonnegative.

There is a finite formulation that avoids listing every combination of
type-specific rules. Let $C_{\tau,r}$ be the cost vector of rule $r$ on
the canonical event $\tau$, and put
$h_\tau=7!/|\operatorname{Aut}(\tau)|$. Nonnegative coefficients with

$$
\sum_r\mu_{\tau,r}=\gamma h_\tau\quad\text{for every }\tau,
\qquad \gamma\ge0
$$

give the valid joint row
$\sum_{\tau,r}\mu_{\tau,r}C_{\tau,r}\cdot Y-\gamma c_m\cdot Z\ge0$.
Each rule's cost on its canonical event is at least $B\Pr(\tau)$,
and $\sum_\tau h_\tau\Pr(\tau)=1$. Equivalently, when $\gamma>0$,
choose a rule independently for each type with probabilities
$\mu_{\tau,r}/(\gamma h_\tau)$ and average (GC). This formulation
allows every combination from a finite per-type rule pool. The retained
coupled program instead prices individual complete algorithms; it does
not optimize this entire pool formulation. `produce_envelope.py` solves
the finite pool formulation on its saved numerical row ingredients,
rebuilding the cut costs in integers. It does not price rules outside
that pool or certify the other numerical ingredients.

Here is a finite full-solution interface for the combined system. Choose
nonnegative multipliers for valid uncoloured rows $r_i$ and paired rows
$s_j$, and any real vector $v$ on the five-point marginal classes. Put

$$
a=\sum_i\alpha_i r_i+\pi^{\mathsf T}v,\qquad
c=\sum_j\beta_j s_j-\kappa^{\mathsf T}v.
$$

If exact coefficient checks give
$\max_H a(H)+\max_K c(K)<0$, then normalization of $Y,Z$ makes
$a\cdot Y+c\cdot Z<0$, while (M) and row nonnegativity make it
nonnegative. This excludes every hypothetical counterexample in the whole
band with zero error. Square rows must retain their actual positive
semidefinite or rank-one justification, and every proper-support and
independence hypothesis remains in force.

An alternative certificate permits equality at the target. Let $c_m$ be
the paired monochromatic-density coefficient vector, and replace $c$ by

$$
c=c_m+\sum_j\beta_j s_j-\kappa^{\mathsf T}v.
$$

Then $a\cdot Y+c\cdot Z\ge B$. Consequently the exact bound
$\max_H a(H)+\max_K c(K)\le b_0$ already contradicts $B>b_0$.
This objective requires no normalization of the nonnegative multipliers.
Comparisons (GC) may be added with multipliers $\gamma_j\ge0$: add
$\sum_j\gamma_j C_j$ to $a$ and subtract
$(\sum_j\gamma_j)c_m$ from $c$. Their joint expectation is nonnegative,
so both coefficient criteria remain valid with these shared multipliers.
`produce_coupled.py` searches this direct-bound interface by default;
its separate contradiction mode normalizes the row multipliers and seeks
a strictly negative coefficient sum. Both include $(E_0)$, $(D_0)$ and
the stated interval consequences. The projection has fourteen
classes; one identity is redundant because both vectors have total mass
one. No exact combined certificate is supplied. A numerical feasible state
of this relaxation need not have a common underlying graph or higher
coloured extension.

The failed step in this combined argument is the construction of exact
multipliers meeting either coefficient criterion. The retained discovery
procedures do not supply them: they price only selected square directions
and bounded cut proposals, and their numerical states are not verified
feasible states of the complete declared families. The missing implication
is therefore **unknown here**. A richer common marginal or additional
justified conditional rows could change it; the finite searches establish
no impossibility for those alternatives.

**Polynomial multipliers and vanishing errors.** The fixed-multiplier
condition (C) is sufficient but need not be the only usable parameter
certificate. Write $\delta=B_0-b_0$, $t=(B-b_0)/\delta$ and
$R_i(t)=(1-t)R_i^-+tR_i^+$ for an affine row. At an integer degree $d\ge2$,
choose its multiplier in Bernstein form

$$
\lambda_i(t)=\sum_{j=0}^{d-1}\lambda_{ij}
 {d-1\choose j}t^j(1-t)^{d-1-j},\qquad \lambda_{ij}\ge0.
$$

Positive semidefinite matrix multipliers may use the same form with
positive semidefinite coefficient matrices. Equality multipliers are free.
For a graph $H$, include the objective $m(H)$ in each degree-$d$
Bernstein coefficient of the resulting expression. The scalar-row
contribution to coefficient $j$ is

$$
\frac{d-j}{d}\sum_i\lambda_{ij}R_i^-(H)
+\frac{j}{d}\sum_i\lambda_{i,j-1}R_i^+(H),
$$

where a term with an index outside $0,\ldots,d-1$ is omitted. The analogous
formula applies to an affine matrix row. If these graph coefficients are
at most $b_0+\delta j/d$ for $j<d$, and at most $b_0+\rho\delta$ for
$j=d$, with $0\le\rho<1$, nonnegativity of the Bernstein basis gives

$$
m\le B-(1-\rho)\frac{(B-b_0)^d}{\delta^{d-1}}. \tag{C_d}
$$

For the weighted-extremal system, $m=B>b_0$ would contradict $(C_d)$
immediately. For a uniform-bound version of the hereditary system, iteration
of the right-hand side decreases $B$ to $b_0$: it stays in $[b_0,B_0]$,
and its only possible limiting fixed point there is $b_0$. Either version
would prove the full target with zero limiting error. All coefficients and
positivity conditions must be exact on every interval of a finite cover of
the density band. No certificate of this form is supplied; failure of a
fixed-multiplier search is not a failure of all polynomial multipliers.

**The recorded mixtures do not obstruct this route.** Let
$\psi=\sum_j\lambda_j\phi^{(j)}$ be a finite convex combination of order-$\ell$
states of triangle-free graphs $G_j$, each coloured by a maximum cut, with
any densities. Every vertex-stability and switching row, every flag moment
matrix and the matrices localized by $\sigma$ are nonnegative at each
$\phi^{(j)}$, hence at $\psi$; the band rows are imposed on $\psi$ itself.
Its value is $m(\psi)=\sum_j\lambda_j\,d_{\rm mono}(W_{G_j})$. By the
density tails, $d_{\rm mono}(W_{G_j})\le2/25$ whenever $p(G_j)$ lies outside
the band. Hence such a mixture, feasible or not, has value above $2/25$
only if one of its components is itself a counterexample to (T). In
particular the $C_{13}(1,5)$/Clebsch mixture, with each component carrying
its own maximum cut, has value
$\frac{12}{169}\lambda+\frac1{16}(1-\lambda)<2/25$, and the
Higman–Sims/pentagon mixture has value at most $2/25$, since the
Higman–Sims graphon has $p=11/50$, inside the sparse tail. The mechanism of
both obstructions, one rule per root type serving every component of a
mixture, is absent: each component brings its own cut. This is an exact
statement about mixtures of genuine states only.

**What can still obstruct it.** At a fixed order the system can fail in two
ways short of a counterexample. A vector may satisfy the finitely many
positivity conditions of that order without being a mixture of genuine
states. Or a genuine graph may carry a cut that is not maximum but
satisfies every included row: a trap. Traps need many twin classes. If $G$
has $s$ classes of vertices with equal neighbourhoods and a colouring of
$W_G$ is stable under every switching on $s$ roots, it is optimal: with one
root in each class, distinct classes have distinct profiles, the cells are
the colour classes inside twin classes, and an optimal colouring constant
on each twin class is reached by recolouring a union of cells.

The stronger sufficient condition that every cut in the band stable under
vertex flips and deterministic two-root switching has at most $N^2/25$
monochromatic edges is false. The
[[research/triangle_free_bipartization/two_root_switching_traps|two-root trap construction]]
retains each edge of a balanced Clebsch blow-up independently with probability
$7/8$ and uses a fixed cut with twelve monochromatic template edges. The
limiting densities are $p=35/128$ and $d_{\rm mono}=21/256>2/25$.
An exact table for all deterministic two-root switchings has a strictly
positive margin; concentration gives finite graphs stable under those
switchings and all vertex flips, still above the target. Every graph in the construction
satisfies (T) by another cut, and the proof exhibits an improving
three-root switching. Thus even arbitrary nonnegative multipliers and flag
positivity cannot complete a system whose only optimality assumptions are
vertex and deterministic two-root stability. This does not obstruct the
route using genuine maximum cuts and richer switching. The universal three-root
implication remains unproved here. The same construction is excluded by
one explicit order-seven row: a three-root switching gain weighted by the
square of the common non-neighbour mass. The trap page checks its negative
limiting value $-164741871/2^{47}$ in the monochromatic-density convention.
Thus this stronger family escapes the exact two-root obstruction, without
yet supplying the missing full-band inequality.

The earlier finite tests by `produce_coloured.py --traps` concern different
graphs. On $C_5$, $C_7$, Petersen, Clebsch and $C_{13}(1,5)$
every vertex-stable cut above $N^2/25$ (none, $7$, none, $40$ and $78$ of
them) has a strictly improving two-root switching. Descents from random cuts
on random band Cayley graphs of orders $41$ to $128$ all ended at or below
$0.79N^2/25$. These are finite samples; they prove nothing about other
graphs.

**Order six.** The discovery program `produce_coloured.py` builds this
system at order six on the 1031 coloured triangle-free graphs of that order.
It has vertex rows times every one-rooted flag on four further points,
switching rows on one to four roots times every rooted flag on the remaining
points, band rows, and moment blocks for root types of sizes zero to three,
with localizing blocks for $\sigma$, $p-a$ and $b-p$; optionally it adds
four-rooted moment blocks and the products $\sigma(r_1)\Delta_S(r)F(r)$
and $\sigma(r_1)\sigma(r_2)F(r_1,r_2)$. It maximizes $m$ by a log-barrier
method, adding violated switching rows between solves; pricing is
exhaustive on at most three roots and a local search on four. Exact states
of the Petersen graph and $C_{13}(1,5)$ with maximum cuts satisfy every row
and block, and a one-colour cut violates them; this checks the
implementation, not the bound.

Each round solves the system with the rows found so far. Once switching
rows on several roots are present the barrier method stalls short of
convergence, so two numbers are read for each round. The state found is
checked against the rows priced so far only to numerical tolerances; its value bounds nothing about the
complete system. A dual certificate gives a floating-point upper bound for the
complete order-six system, whatever rows remain unpriced: nonnegative
multipliers on the priced rows and nonnegative weights on rank-one matrices
$vv^{\mathsf T}$ for the blocks, with $v$ ranging over the eigenvectors of
the state's moment matrices and normalized sums and differences of those of
the five smallest eigenvalues, the weights chosen by a linear program.
Before any switching row on two or more roots is priced, state and bound
agree at $0.1200$ on $I_1=[3/10,5/16]$. With the optional rows, after six
rounds on $I_1$ the state has value $0.0841$ and the bound is $0.0988$;
after two rounds on the whole band they are $0.0857$ and $0.0990$. On $I_1$
pricing finds no violated row after eight rounds, at a state of value
$0.0840$; a second solver variant, run on the rows of round six, reaches
the same value as the first. The final state satisfies, to rounding, every row and block of the
system, with switching rows on one to three roots and their products priced
exhaustively; only the four-root pricing is a local search. This suggests a
possible obstruction near $0.084$ to the particular implemented system on
$I_1$, but does not prove one. An obstruction would need an exact feasible
state and exhaustive four-root pricing. These floating-point bounds are weaker than the bound
$d_{\rm mono}\le4/47\approx0.0851$, which the
[[research/graph_ramsey_interfaces/homogeneous_triangle_deletion_bounds|homogeneous transfer]]
of Balogh, Clemen and Lidický's $D_2\le N^2/23.5$ gives at every order;
order six, as solved here, improves on nothing known. For
comparison, the uncoloured fixed-square programs report thresholds of about
$0.0913$ at order seven and $0.0879$ at order eight.

The failed step is again the certificate: none is known at any order. The
state near $0.084$ is not an established optimum: the solver stalled,
four-root pricing is incomplete, and this implementation omits the
gain-weighted squares above. It therefore does not settle the strengthened
order-six system. Whether a richer order-six, seven or eight system reaches
$2/25$ is unknown. The exact two-root trap obstructs only systems whose
optimality assumptions stop at two roots.

## Gap

The band inequality itself is open: no argument here proves
$d_{\rm mono}\le2/25$, or a vanishing family of errors, for every
triangle-free graphon with $1243/5000<p<3197/10000$. No counterexample is
supplied here either. The largest value among the retained band examples is
$d_{\rm mono}=12/169\approx0.0710$, for the circulant $C_{13}(1,5)$ on
$\mathbb Z/13$ with connection set $\{1,5,8,12\}$, at $p=4/13$; it lies
$38/4225\approx0.0090$ below $2/25$. The evidence scans all its cuts. Its
ratio $D_2/e=3/13$ exceeds the ratio $1/5$ of every Clebsch-colourable
graph. The evidence also checks that every triangle-free Cayley graph on
an abelian group of order at most $24$ with band density has
$d_{\rm mono}\le12/169$, so $C_{13}(1,5)$ is the largest in that class.
The Clebsch graphon has $d_{\rm mono}=1/16$ at
$p=5/16$, the Petersen graphon $3/50$ at $p=3/10$, and the balanced $C_5$
blow-up with isolated vertices added has $d_{\rm mono}=p/5$ at every band
density, which is $3197/50000\approx0.0639$ at the top. A disjoint union
does slightly better there: the $C_5$ blow-up with weight $1-\alpha$
beside the Higman–Sims graphon with weight $\alpha$ has
$p=\frac{11}{50}\alpha^2+\frac25(1-\alpha)^2$ and
$d_{\rm mono}\ge\frac7{100}\alpha^2+\frac2{25}(1-\alpha)^2$. This lower
bound approaches about $0.0643$ as the density approaches $3197/10000$
from inside the band along the small-$\alpha$ branch, the largest value
retained near the top of the band. The transfer gives
$d_{\rm mono}\le p/5$ for every
graph with a homomorphism to the Clebsch graph, but $p/5$ is not a general
bound, even inside the band: the same union has $d_{\rm mono}>p/5$ for
every $\alpha$ with $0<\alpha<1$.

A finite witness to that stronger bound's failure is the disjoint union
$H\cup C_5[140]$, where $H$ is the 100-vertex Higman–Sims graph. It has
$N=800$, $e=99100$, and $p=991/3200$ inside the band. The spectral lower
bound $D_2(H)\ge350$ and the exact pentagon blow-up identity give
$D_2\ge19950>e/5=19820$. This is not a counterexample to (T), whose
upper target here is $25600$.

## Next tests

- **A common-marginal certificate.** Seek an exact combined bound at
  $2/25$ for the monochromatic-density objective, or a negative exact
  contradiction bound in the system (M), including the parameter-free
  identities $(E_0)$ and $(D_0)$, the padding consequence (IP), and
  justified proper-support comparisons.
  This directly joins seven-root cuts and nine-point positivity with
  active-cut information. A next test is a six-point paired-cut extension
  with parameter-free balance and proper-support comparisons, coupled to
  the uncoloured six-point marginal. The balanced finite seven-root pool
  has been tested numerically without a certificate; repeating that pool
  adds no new implication. The displayed criterion covers the whole band;
  a nonpositive numerical search margin does not decide it.
- **Recursive induction on the whole band.** Seek an exact negative
  coefficient combination of $(I_r)$, its justified products, degree
  localizers and flag positivity. The search may use several recursive
  parts and stochastic colours outside them. The retained order-seven
  and order-eight programs have not produced such a certificate. Lifting
  to nine points permits $(J_7)$ and the additional full flag squares. A
  narrow interval is a diagnostic for whether localization removes the
  remaining slack; it is not the target. Any successful interval must
  compose with finitely many others and the source tails, with zero
  final error. Local pricing is not an exhaustive feasibility test.
- **A strict parameter certificate.** For the paired-cut system, find
  $\rho<1$ in (C) or $(C_d)$, including balance equalities,
  hereditary and recursive comparisons, proper-support comparisons (P)
  and (P') under their minimality hypothesis, and the cut-pattern positivity
  conditions actually justified above. Exact coefficient and positivity
  checks must cover every sampled coloured graph and every interval in
  the proposed cover. A numerical value $\rho=1$ supplies no progress
  toward the target and does not obstruct all nonconstant multipliers,
  larger roots or stronger cut-pattern conditions.
- **A construction or structural replacement.** A genuine weighted
  triangle-free graph with minimum monochromatic density above $2/25$
  would give finite counterexamples by rational approximation and
  blow-up. Conversely, a structural theorem reducing every hypothetical
  weighted extremizer to a class with a proved good cut would replace
  the certificate step. The expected-monochromatic-degree identity,
  the expansion condition and the failure of two-root stability specify
  necessary interfaces; they do not yet provide that theorem.

The missing step in these proof chains is an exact whole-band
implication. Its status is **unknown here**, not refuted by a floating
relaxation state. The stronger implication from vertex and two-root
deterministic switching stability alone is **false**, with the finite
construction above. Reopening that restricted argument requires an additional
hypothesis the construction violates; increasing the number of its
otherwise valid square or multiplier rows cannot repair it.

A further sufficient condition from the preprint's Section 7 is
$\Gamma=\sum_{uv\in M}(\operatorname{dist}_B(u,v)+1)^2\le N^2$ for a
maximum-cut graph $B$ with uncut edges $M$. If $G$ is connected, $B$ is
connected: otherwise flipping one $B$-component turns every edge from it
to another component from uncut to cut, contradicting maximality. Each
uncut edge has even $B$-distance at least four, since distance two would
form a triangle. Hence $25D_2\le\Gamma$. Proving the proposed bound for
each connected component of order $N_i$ would give
$D_2\le\sum_iN_i^2/25\le N^2/25$.

The proposed $\Gamma$ bound remains unproved. For the balanced blow-up
$C_{2k+1}[t]$, $k\ge2$, a maximum cut leaving one consecutive pair of
parts uncut has $t^2$ uncut edges, each at distance $2k$ in $B$, and
$\Gamma=t^2(2k+1)^2=N^2$. Failure of this stronger condition would not
by itself refute (T).
