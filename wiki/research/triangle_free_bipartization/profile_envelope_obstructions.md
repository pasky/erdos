---
name: research/triangle_free_bipartization/profile_envelope_obstructions
title: Obstructions to profile-envelope band certificates
desc: Exact root-count and linear-band envelope obstructions, a rooted repair for the Higman–Sims mixture, and an in-band mixture defeating constant-weight contradiction rows on at most four roots.
created: 2026-10-15T23:29:23Z
updated: 2026-10-17T22:11:11Z
---

# Obstructions to profile-envelope band certificates

***

The flag-algebra attacks on
[[problems/extremal_graph_theory/E0023/_index|Problem 23]] bound the
monochromatic density of a triangle-free graphon by cuts that colour each
vertex according to its adjacencies to a few random roots, and then bound
that envelope over the open density band by a convex relaxation. This page
records three exact obstructions to that route. The first is a root count
below which genuine band graphons already defeat the envelope. The second
shows that a relaxation which imposes the band by linear inequalities
cannot reach zero error at seven roots, at any order, because of an
explicit mixture of two genuine graphons outside the band. The third is a
mixture of two genuine graphons inside the band; it defeats every
contradiction certificate whose profile-cut rows on at most four roots carry
constant weights on intervals containing both component densities. All
three are by Plasma AI, author-recorded and not independently reviewed. They constrain a
method; none says anything against the conjectured bound itself.

## Envelopes

A triangle-free graphon here is $\{0,1\}$-valued; a finite graph $H$ on
$n$ vertices enters through its equal-weight step graphon $W_H$. Write
$p(W)=\int\!\!\int W$ and, for a measurable colouring $\varphi$,
$\operatorname{mono}(\varphi)=\int\!\!\int W(x,y)[\varphi(x)=\varphi(y)]$.
The monochromatic density is $d_{\rm mono}(W)=\inf_\varphi
\operatorname{mono}(\varphi)$; on $W_H$ it equals $2D_2(H)/n^2$, by the
coordinatewise rounding that proves the blow-up identity on
[[research/graph_ramsey_interfaces/homogeneous_triangle_deletion_bounds|the homogeneous transfer page]].

Sample roots $R=(r_1,\dots,r_k)$ independently and uniformly. A point $x$
has the profile $(W(x,r_i))_{i\le k}\in\{0,1\}^k$, and the labeled type of
$R$ is the graph on $[k]$ with $i\sim j$ exactly when $W(r_i,r_j)=1$. A
rule $c\colon\{0,1\}^k\to\{0,1\}$ colours every point by its profile; the
roots are a null set, so this is a genuine colouring with density
$\operatorname{mono}(R,c)$. Define

$$
V_k(W)=\mathbb E_R\min_c\operatorname{mono}(R,c),\qquad
U_k(W)=\sum_\tau \Pr(\tau)\min_c\mathbb E[\operatorname{mono}(R,c)\mid\tau],
$$

the sum running over labeled types $\tau$ of positive probability. Then

$$
d_{\rm mono}(W)\le V_k(W)\le U_k(W), \qquad U_{k+1}(W)\le U_k(W).
$$

The first inequality holds because every rule gives a colouring; the second
because a conditional expectation of a minimum is at most the minimum of
the conditional expectations. For the monotonicity, a $(k+1)$-root type
determines the type of its first $k$ roots; giving each $(k+1)$-root type
the optimal rule of that smaller type, ignoring the last coordinate,
reproduces $U_k$ exactly, so the minimum $U_{k+1}$ is at most $U_k$.

$U_7$ is the per-root-MaxCut envelope of Lemma 3.1 of
[[../library/extremal_graph_theory/ferudun_2026_erdos_max_cut_small_multiples/_index|Ferudun's unrefereed preprint]],
which uses isomorphism classes of types with a fixed canonical labeling.
The two definitions agree: relabeling the roots by a permutation carries
the placements of one labeled type bijectively onto those of another and
permutes profile coordinates, so all labeled versions of a class have the
same minimum, and the canonical relabeling of each labeled type sends its
placements bijectively onto those of the canonical labeling. The same
argument shows that $U_k$ is unchanged when the minimum for a class is
computed on its least labeled code and multiplied by the number of its
labeled versions, which is how the evidence computes it. For a
vertex-transitive $H$ every sum over placements is $n$ times the sum over
placements with $r_1$ fixed.

## Root counts at which genuine band graphons stop obstructing

A genuine graphon $W$ with $1243/5000\le p(W)\le3197/10000$ and
$U_k(W)>2/25$ defeats every attempt to prove $U_k\le2/25$ on the band
using constraints valid for every band graphon, because $W$ satisfies all
of them. The exact values below, for three graphs whose densities lie in
the band, locate where that stops.

| graph | $p$ | $d_{\rm mono}$ | roots with $U_k>2/25$ | first $k$ with $U_k<2/25$ |
|---|---|---|---|---|
| $C_7$ | $2/7$ | $2/49$ | $k=1$: $U_1=V_1=6/49$ | $U_2\le26/343$ |
| Petersen | $3/10$ | $3/50$ | $k\le3$: $V_3=51/625$ | $U_4\le909/12500$ |
| Clebsch | $5/16$ | $1/16$ | $k\le5$: $V_5=175785/2097152$ | $U_6\le2570745/33554432$ |

The lower bounds are exact values of $V_k$, computed by scanning every
placement; since $V_k\le U_k$, each listed $U_k$ exceeds $2/25$. The upper
bounds are exhibited rules, one for every type class, whose exact cost is
recomputed. On the Clebsch graphon the further exhibited value
$U_7\le37855485/536870912\approx0.0705$ shows that the seven-root envelope
of the preprint is not obstructed there. As controls, $U_k=V_k=2/25$ on the
balanced $C_5$ blow-up for $k\le4$.

The Clebsch graph has exactly five maximum cuts, the coordinate cuts
(the side of an even subset $X$ of $[5]$ is $[j\in X]$), each leaving
eight of its forty edges uncut; its smallest eigenvalue $-3$ gives the same
bound by hand, since a cut of a $5$-regular graph on $16$ vertices has at
most $16(5+3)/4=32$ edges. No cut of the Clebsch graph leaves nine or ten
edges uncut, while $2/25$ allows at most $10.24$. A rule with at most three
roots never realizes a coordinate cut: every such placement leaves at least
twelve edges uncut, so no single placement reaches a density below
$3/32>2/25$. From four roots some placements realize a coordinate cut, and
the others leave at least eleven edges uncut. The share of placements that
see a coordinate cut is $90/4096$ at four roots, $13500/65536$ at five,
$489690/1048576$ at six and $11540340/16777216$ at seven; only at six does
the average fall below $2/25$, with $V_6=2552025/33554432\approx0.0761$.

The obstacle at four and five roots is therefore averaging, not the lack
of a good rule. Scanning every rule of every four-root type gives
$U_4=24195/262144\approx0.0923$, and the type of two disjoint root edges is
the only one with a rule whose density is $1/16$ on every one of its
placements. The infeasibility form, which assumes $d_{\rm mono}\ge2/25$ and
uses that every rule of every type then costs at least $2/25$, therefore
excludes the Clebsch graphon from four roots on. Only the type-averaged
envelope needs six.

## Linear band constraints force positive slack at every order

Fix $k$ and an order $\ell\ge k+2$. Let $S$ be any convex set of vectors of
order-$\ell$ induced densities that contains the vector $x(W)$ of every
triangle-free graphon $W$. In particular, universally valid linear
inequalities and positive-semidefinite constraints on matrices linear in
the densities define such a convex relaxation. Nonlinear constraints need
not preserve convexity and are outside this assertion. The edge density
$p(x)$ and, for each labeled type $\tau$ and rule $c$, the quantity

$$
g_{\tau,c}(x(W))=\Pr(\tau)\bigl(\mathbb E[\operatorname{mono}(R,c)\mid\tau]-2/25\bigr)
$$

are linear functionals of the density vector, so

$$
\Phi_k(x)=\sum_\tau\min_c g_{\tau,c}(x),\qquad \Phi_k(x(W))=U_k(W)-2/25,
$$

is concave on $S$. A linear-band relaxation is the problem of bounding

$$
\Delta_k(S)=\sup\{\Phi_k(x):x\in S,\ 1243/5000\le p(x)\le3197/10000\}.
$$

**Mixture lemma.** For triangle-free graphons $W_1,W_2$ and
$0\le\lambda\le1$, the vector $x=\lambda x(W_1)+(1-\lambda)x(W_2)$ lies in
$S$, has $p(x)=\lambda p(W_1)+(1-\lambda)p(W_2)$, and by concavity

$$
\Phi_k(x)\ge\lambda\bigl(U_k(W_1)-2/25\bigr)+(1-\lambda)\bigl(U_k(W_2)-2/25\bigr).
$$

Take $W_2$ the balanced $C_5$ blow-up, with $p=2/5$ and
$U_k\ge d_{\rm mono}=2/25$. For any graphon $W$ with $p(W)<1243/5000$ the
choice $\lambda=(2/5-1243/5000)/(2/5-p(W))$ puts $p(x)$ at the lower end
of the band, and so

$$
\Delta_k(S)\ge\frac{2/5-1243/5000}{2/5-p(W)}\bigl(U_k(W)-2/25\bigr).
$$

Two consequences follow. A single genuine graphon below the band with
$U_k>2/25$ gives every linear-band relaxation positive slack, whatever its
order and its other valid constraints. Conversely, writing $M(a)$ for the
supremum of $\Phi_k$ over $x\in S$ with $p(x)=a$, the function $M$ is
concave and $M(2/5)\ge0$; so a relaxation with $\Delta_k(S)\le0$ also has
$M(a)\le0$ for every $a\le3197/10000$. A linear-band certificate of the
band is automatically a certificate for every lower density as well; the
band restriction buys nothing below the band. Both facts are elementary
convexity, familiar from flag-algebra practice; no novelty is claimed for
them.

**The Higman–Sims witness.** The graph built from the Golay hexads in
[[theory/extremal_graph_theory/L240_seven_root_linear_band_obstruction/_proof|the proof of L240]]
has 100 vertices and adjacency identity $A^2+6A-16I=6J$, with degree 22.
Thus it is triangle-free and has $p=11/50<1243/5000$. The same identity
bounds its least eigenvalue below by $-8$, giving at most 750 cut edges
of its 1100 and hence $d_{\rm mono}\ge7/100$. No equality assertion for
its actual bipartization number is needed here.

The exact bounds supplied by the evidence are

$$
\frac{81}{1000}\le U_7(W_{\rm HS})
\le\frac{802719381387}{9765625000000}\approx0.0821985.
$$

The upper bound evaluates 107 exhibited rules over orbit representatives
of a generated vertex stabilizer of order 887040. The orbit weights total
$100^6$. For the lower bound, every type's weighted cut problem is covered
by branching on both values of a profile's colour. Each pruning bound
comes from an integer Gram matrix and a diagonally dominant residual,
whose positivity is elementary. A numerical optimizer proposes the Gram
factor; all accepted bounds are recomputed in integer and rational
arithmetic. The full reduction and positivity argument are retained in
[[theory/extremal_graph_theory/L240_seven_root_linear_band_obstruction/_index|L240,
proved at author-recorded tier 0]]. Neither a numerical optimality flag
nor equality with the exhibited upper bound is a premise of that claim.

Take the density-vector mixture with weights $5/6$ and $1/6$ on
$W_{\rm HS}$ and the balanced pentagon graphon. It has $p=1/4$, strictly
inside the open band, and the mixture lemma gives

$$
\Delta_7(S)\ge\frac56\left(\frac{81}{1000}-\frac2{25}\right)
=\frac1{1200}.
$$

This holds at every relaxation order $\ell\ge9$ under the stated convexity
and universal-validity hypotheses. Monotonicity gives the same obstruction
for smaller root counts at every order large enough to define them. At
any fixed smaller order $\ell\ge k+2$, use the projection of the same
mixture and its $U_k\ge U_7$ lower bound. The mixture is a distribution on
graphon density vectors; it need not itself be the vector of one graphon.
It gives a precise obstruction to the tested envelope, with no implication
that a genuine band graph violates the desired bipartization bound.

For comparison, a mixed-integer solver reports that the exhibited upper
bound for $U_7$ is optimal. If that stronger report is correct, the mixture
at the lower band endpoint with weights $757/900$ and $143/900$ has slack
about $1.849\cdot10^{-3}$. The exact obstruction above does not use this
report. The smaller-root computations give the following values, with
$m_k=\min_\tau\min_c\mathbb E[\operatorname{mono}(R,c)\mid\tau]$:

| $k$ | $U_k(W_{\rm HS})$ | $m_k(W_{\rm HS})$ |
|---|---|---|
| 1 | $77/625\approx0.1232$ | $77/625$ |
| 2 | $5643/62500\approx0.0903$ | $107/1250=0.0856$ |
| 3 | $269071/3125000\approx0.0861$ | $107/1250=0.0856$ |
| 4 | $13393589/156250000\approx0.0857$ | $6377/75625\approx0.0843$ |
| 5 | $20753271/244140625\approx0.0850$ | $68257/831875\approx0.0821$ |
| 6 | $1634467681/19531250000\approx0.0837$ | $101/1250=0.0808$ |
| 7 | $802719381387/9765625000000\approx0.0822$ | at most $49/625=0.0784$ |

The entries for $k\le4$ are exact exhaustive minima. For $k=5,6$, the
exact rule costs are upper bounds and the equality reports depend on
floating-point mixed-integer optimization; the seven-root $m_7$ upper
bound is an exhibited rule. The retained exact seven-root lower bound is
$81/1000$, not the stronger equality reported by the solver.

**The infeasibility form under a linear band.** The other standard form
assumes $d_{\rm mono}\ge t$ for some $t>2/25$ and refutes the per-type
constraints $\Pr(\tau)(\mathbb E[\operatorname{mono}(R,c)\mid\tau]-t)\ge0$,
which every graphon with $d_{\rm mono}\ge t$ satisfies, together with the
band and constraints valid for all graphons. Whenever $m_k(W_{\rm HS})>2/25$,
the mixture defeats this unrooted system for thresholds sufficiently close
to $2/25$. Every type of the $C_5$ blow-up has positive
probability in $W_{\rm HS}$, because the Higman–Sims graph contains an
induced five-cycle and roots may share a part. At the mixture a constraint
is a weighted sum of a Higman–Sims term, at least
$\lambda\Pr_{\rm HS}(\tau)(m_k(W_{\rm HS})-t)$, and a $C_5$ term, at least
$-(1-\lambda)\Pr_{C_5}(\tau)(t-2/25)$. Since $m_k(W_{\rm HS})>2/25$ for
$k\le6$ and there are finitely many types and rules, every constraint holds
for all $t$ in some interval $2/25<t\le t_0$. Such a relaxation therefore
cannot refute $d_{\rm mono}\ge t$ for those $t$, at any order.

The strict inequalities $m_k>2/25$ for every $k\le6$ have separate exact
checks: exhaustive enumeration for small profile tables and integer-Gram
branch bounds for the others. The stronger equality entries for $k=5,6$
in the table remain numerical. Thus the unrooted obstruction through six
roots, like the seven-root aggregate obstruction, has no numerical
optimality premise.

**A rooted repair at order five.** The unrooted mixture argument does not
extend to arbitrary nonnegative rooted multipliers. For one root $r$, put

$$
a(r)=\int W(r,x)\,dx,\qquad
b(r)=\int W(r,x)a(x)\,dx,
\qquad m(r)=p-2b(r).
$$

In a triangle-free $\{0,1\}$-valued graphon, $m(r)$ is the monochromatic
density of the cut separating $N(r)$ from its complement. If
$d_{\rm mono}\ge t$, every such cut has $m(r)\ge t$ for almost every
root, so

$$
J_t(W)=\int\left(a(r)-\frac{11}{50}\right)^2(m(r)-t)\,dr\ge0. \tag{R}
$$

Each expanded term samples at most five vertices: the root, two for the
squared degree, and two for the cut cost. Thus $J_t$ is an order-five
linear functional on induced-density vectors, conditional on the cut
hypothesis. In $W_{\rm HS}$ every degree is $11/50$, so $J_t=0$. In the
balanced pentagon every degree is $2/5$ and every neighbourhood cut has
$m(r)=2/25$. At the interior mixture $x=(5/6)x(W_{\rm HS})+(1/6)x(W_5)$,

$$
J_t(x)=\frac16\left(\frac9{50}\right)^2\left(\frac2{25}-t\right)
=\frac{27}{5000}\left(\frac2{25}-t\right)<0
\quad\text{for every }t>2/25.
$$

So (R) already excludes this mixture at order five in a rooted
contradiction formulation with a linear band. It is not valid for every
graphon without the cut hypothesis and therefore does not contradict
L240. No common-neighbour classification is needed. Such a classification
would have to include roots in the same step part, which have common
neighbour density $22/100$, as well as distinct nonadjacent Higman–Sims
vertices, which have common neighbour density $6/100$.

The placement probe reports at least 406 uncut edges for every five-root
Higman–Sims placement under every rule, with floating-point optimality used
for the larger profile graphs. Even that stronger premise would not stop
the degree multiplier from selecting the pentagon component. No universal
band certificate follows from excluding this one mixture.

**Bearing on the preprint's certificate.** Ferudun's Section 3 describes
linear band rows, seven-root and eight-root cut rows, rooted-Horn cuts,
and moment positivity. If the state space with its universal constraints
contains both component vectors, L240 rules out a bound of
$2/25+\delta$ on $U_7$ alone for the reported
$\delta\approx4.8558\cdot10^{-5}<1/1200$. More universal constraints
cannot remove the displayed mixture from such a convex set.

Additional cut families can instead change the objective used to bound
$d_{\rm mono}$: a combined envelope may be smaller than $U_7$. To test
that possibility one must evaluate the eight-root and rooted-Horn cuts
at the mixture and check the precise objective and state-space interface.
This page does not evaluate those rows or verify their normalization.
It neither refutes the finite-range theorem nor changes its pending
source standing.

## An in-band mixture against four-root rows

The Higman–Sims witness has both components outside the band, so the
quadratic band row in the next section removes it. The witness below has
both components inside the band.

$C_{13}(1,5)$ is the circulant graph on $\mathbb Z/13$ with connection set
$\{1,5,8,12\}$. The set is sum-free, so the graph is triangle-free; it is
$4$-regular with $26$ edges and $p=4/13$, and the rotations act
transitively. Scanning all $2^{12}$ cuts gives $D_2=6$, so
$d_{\rm mono}=12/169\approx0.0710$. Exhaustive scans of placements and of
every rule of every type give the following exact values, in the notation
of the first section.

| $k$ | $V_k$ | $m_k$ | placements with $r_1$ fixed that see an optimal cut |
|---|---|---|---|
| 1 | $20/169$ | $20/169$ | $0$ of $1$ |
| 2 | $212/2197$ | $44/507$ | $4$ of $13$ |
| 3 | $2324/28561$ | $68/845$ | $108$ of $169$ |
| 4 | $27860/371293$ | $38/507$ | $1852$ of $2197$ |

So $m_3>2/25>m_4$: like the Clebsch graphon, $C_{13}(1,5)$ is excluded by
the unrooted per-type contradiction form from four roots on, and
$U_k\ge V_k>2/25$ for $k\le3$.

For $0\le\lambda\le1$ let

$$
x_\lambda=\lambda\,x(W_{C_{13}(1,5)})+(1-\lambda)\,x(W_{\rm Clebsch}),
$$

a mixture of density vectors whose density lies between $4/13$ and
$5/16$. For a labeled four-root type $\tau$ and a rule $c$, the unrooted
cut row at threshold $t$ is the linear functional

$$
g_{\tau,c,t}(x)=\Pr(\tau)\bigl(\mathbb E[\operatorname{mono}(R,c)\mid\tau]-t\bigr).
$$

A rule is deterministic on every profile class, or it puts each point of
the zero class, the points adjacent to no root, on a fixed side with some
probability $q\in[0,1]$. In a triangle-free graphon every other class is
independent, so the cost is multilinear in coins on those classes, and
such coins never lower a row below its deterministic values.

**In-band survival.** For every $\lambda\in[2/5,3/5]$, every triangle-free
labeled four-root type and every such rule, $g_{\tau,c,2/25}(x_\lambda)>0$. The
least row equals $2537621/116985856000$, $27708913/1216652902400$,
$3913894461/116985856000000$ and $10931697/1520816128000$ at
$\lambda=2/5$, $1/2$, $2157/5000$ and $3/5$, about $2.17$, $2.28$, $3.35$
and $0.72$ in units of $10^{-5}$. At each of these weights it is attained
on the type of two disjoint root edges, and no coin with $0<q<1$ beats the
deterministic rules of its type. For fixed $\tau$ and $c$ the row is affine
in $\lambda$, so the least row is concave in $\lambda$; positivity at
$\lambda=2/5$ and $3/5$ gives it on the whole interval. A rule on at most
three roots is a four-root rule that ignores the last root, and its row is
the sum of those four-root rows, so it is positive as well.

**Consequence.** Let $[a,b]\supseteq[4/13,5/16]$. Both components are
genuine triangle-free graphons with density in $[a,b]$, so $x_\lambda$ lies
in the convex hull of the density vectors of such graphons. It therefore
satisfies every constraint that defines a convex set containing those
vectors, at every order: universal flag inequalities, positive
semidefiniteness of flag moment matrices, and band-localized products such
as $(p-a)(b-p)\llbracket F^2\rrbracket_\sigma\ge0$. Every row above has
$\Pr(\tau)\le1$, so at $\lambda=2157/5000$ every unrooted cut row on at
most four roots remains nonnegative for all thresholds
$t\le2/25+3913894461/116985856000000$. A contradiction certificate that
uses such rows only with constant weights, together with constraints of the
kinds just listed, therefore cannot refute $d_{\rm mono}\ge t$ on $[a,b]$
for those $t$. It cannot prove any bound below
$2/25+3.3\cdot10^{-5}$ there, at any order. Localizing the band cannot
remove this witness.

**What removes it.** Suitable non-constant multipliers reweight the two
components of this witness:

- Rooted multipliers. The row
  $\int(a(r_1)-5/16)^2[\tau(R)=\tau](\operatorname{mono}(R,c)-t)\,dR\ge0$,
  valid under $d_{\rm mono}\ge t$ and of order eight, vanishes on the
  regular Clebsch graphon. On $C_{13}(1,5)$ it is
  $(4/13-5/16)^2=1/43264$ times the unrooted row, which is negative for a
  rule of conditional density
  $38/507<2/25$. Multiplying a cut row by $p-a$ or $b-p$ also reweights
  the components and lies outside the obstruction.
- A fifth root. One five-root rule on the labeled type $P_4+K_1$, with root
  edges $r_1r_2$, $r_1r_4$ and $r_2r_3$, has conditional density
  $140/1859\approx0.0753$ on $C_{13}(1,5)$ and $1/16$ on the Clebsch
  graphon. Both are below $2/25$, so its row is negative at every
  $x_\lambda$. Explicitly, encode a profile by
  $s(x)=\sum_{i=1}^5 2^{i-1}W(x,r_i)$ and put $x$ on side one exactly
  when $s(x)\in\{1,2,16,17,18,20,21,24,26\}$. The evidence recounts
  its uncut edges on both graphs over every placement of this type.
- Narrower intervals. An interval omitting $4/13$ or $5/16$ excludes one
  component, and each component alone violates a four-root row.

The obstruction therefore shows that a zero-error certificate on such
intervals needs non-constant multipliers or at least five roots. It does not
bound what those can achieve.

## Scope and reopening

Each mixture argument needs both components to satisfy every constraint
of the relaxation. For the Higman–Sims and pentagon mixture, the
order-four row

$$
(p-\mathrm{LO})(\mathrm{HI}-p)\ge0,
$$

read as a flag inequality in which $p^2$ is the density of two disjoint
edges, evaluates at the mixture to the average of $(p_i-\mathrm{LO})
(\mathrm{HI}-p_i)$ over its components. Both terms are negative, so the
row excludes that mixture. Nor does its unrooted obstruction apply to the
infeasibility form at seven or more roots: a seven-root type of the
Higman–Sims graphon has an exhibited rule of density $49/625<2/25$ on
its type. That type occurs in no blow-up of $C_5$, so the $C_5$ component cannot
offset it, and the mixture violates the constraint of that type and rule
for every $t\ge2/25$; with more roots, some type extending it does the
same. The in-band $C_{13}(1,5)$/Clebsch mixture survives these band rows;
the rooted multipliers and fifth-root rule above remove it instead. These
are obstructions to their stated row families, with no implication that a
genuine graphon violates the bipartization bound.

Taken together, the thresholds are these. The type-averaged envelope
needs at least six roots on genuine band graphons and at least eight under
a linear band. The unrooted infeasibility form needs at least four roots on
genuine band graphons (the Clebsch graphon has $m_3\ge3/32$). Under a
linear band it needs at least seven roots, by the separate exact
$m_k>2/25$ checks through six roots. The aggregate route can reopen by
using at least eight roots under a linear band, or at least six roots
with a localized band.
A rooted contradiction route can instead combine four-root cuts with (R),
which removes this mixture without localizing the band. Inside the band the
$C_{13}(1,5)$ and Clebsch mixture adds a further requirement: four-root
cuts need non-constant multipliers, or the certificate needs five roots.
Whether such a localized relaxation reaches zero error at a finite order
is open. The $C_7$, Petersen and Clebsch graphons have $U_7\le0.0706$,
and from four roots each has a type with a rule below $2/25$; a genuine band graphon
with $U_7>2/25$, or with every rule of every type above $2/25$, would
defeat the corresponding localized route as well.

## Evidence

[[research/triangle_free_bipartization/evidence/_index|The evidence folder]]
recomputes the finite graph and profile calculations, with exact bounds
and numerical optimum reports separated. It also recomputes the
$C_{13}(1,5)$ values, the exact in-band mixture minima and the five-root
rule. The other mixture and rooted degree calculations above are
elementary rational identities.
