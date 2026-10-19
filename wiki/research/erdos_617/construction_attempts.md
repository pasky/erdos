---
name: research/erdos_617/construction_attempts
desc: Coordinate-edge counting excludes a class of strong-product templates; geometric constructions retain their stated barriers and unresolved independence conditions.
tags: [graph-theory, constructions, obstructions]
sources: []
created: 2026-09-21T23:52:12Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_617/construction_attempts

***

## Strong-product constructions cannot supply a large-parameter counterexample

**Proved exclusion of a specified construction class, not of arbitrary
colorings.** For each $i=1,\ldots,k$, take an $s_i$-coloring on $q_i$
vertices, where $s_i\ge2$ and every monochromatic clique has order at
most $s_i$. Put $r=\prod_i s_i$. Choose any $r^2+1$ vertices $S$ of the
Cartesian product of the seed vertex sets, and color pairs by tuples
$(c_1,\ldots,c_k)$ subject only to this rule: whenever the endpoints
differ in coordinate $i$, their seed edge has color $c_i$. Equal
coordinates impose no restriction. Arbitrary puncturing and arbitrary
legal choices on pairs with equal coordinates are allowed.

Suppose this produced a counterexample, with $r\ge12$. Critically prune the
colors as in [Critical-component reduction](critical_component_reduction.md);
the product restriction survives edge deletion. Let $C$ count all full $K_r$
components, and write

$$
e(r)=\left\lceil\frac{\sqrt{8r-7}-5}{2}\right\rceil.
$$

That note's bounds $g\ge e(r)$ and
$C\ge(r-1)e(r)-r+1+2g$ give

$$
C\ge(r+1)e(r)-r+1. \tag{P1}
$$


Every full monochromatic clique $Q$ in the product is an entire box.
Its coordinate projections are seed monochromatic cliques, and

$$
r=|Q|\le\prod_i|\pi_i(Q)|\le\prod_i s_i=r.
$$

Equality forces $|\pi_i(Q)|=s_i$ and $Q=\prod_i\pi_i(Q)$.
For each fixed coordinate $i$, the clique therefore contains exactly
$r(s_i-1)/2$ pairs differing only in that coordinate.

Distinct full components have disjoint edge sets, including across
colors. The whole set $S$ has at most $(r^2+1)(q_i-1)/2$ pairs of this
type. Consequently

$$
\boxed{C\le\left(r+\frac1r\right)
\min_i\frac{q_i-1}{s_i-1}.} \tag{P2}
$$

This is incompatible with (P1) whenever their numerical bounds cross.
For fixed seeds, it already excludes all sufficiently long products.

There is also a uniform conclusion for growing seeds. If $k\ge2$ and
$q_i\le s_i^2+1$ for every factor, some $s_i\le\sqrt r$, whence

$$
C\le(\sqrt r+2)(r+1/r).
$$

For $r\ge196$, put $t=\sqrt r\ge14$. Since
$8r-7\ge196r/25$,
$e(r)\ge7t/5-5/2$. The lower bound (P1) is strictly larger than
$r(7t/5-7/2)$. Its difference from the displayed upper bound is
therefore greater than

$$
r(2t/5-11/2)-(t+2)/r>0:
$$

the first term is at least $r/10$, whereas the subtracted term is at
most $1/14+2/196$. Thus **no such nontrivial product works for
$r\ge196$**. For pentagon seeds $s_i=2,q_i=5$, (P2) is
$C\le4(r+1/r)$; (P1) already contradicts it for $r=2^k\ge32$,
because $e(r)\ge6$.

The essential assumption is the seed clique cap $s_i$. Without it,
a full product-colored clique need not be a full box of these sizes.
This result is not a general obstruction to products with different
rules, nor an independence certificate for any surviving template.
No counterexample was obtained.

The separate [square-field semiregular
construction](semiregular_parabola_template.md) gives compatible
shifted-parabola full components and an explicit equivariant completion
mechanism. Its conditional light-anchor identity is exact, but its residual
independence requirement is unproved.

## Semiregular cyclic template with r vertex orbits

**Unresolved template, not a construction or computational result.**
No functions meeting the independence requirements were found or
tested.

For odd $r$, use vertices

$$
\{\infty\}\cup([r]\times\mathbb Z/r\mathbb Z)
$$

and colors $\mathbb Z/r\mathbb Z$. Set
$c(\infty,(a,x))=x$. For old vertices prescribe

$$
c((a,x),(b,y))=\frac{x+y}{2}+f_{ab}(y-x), \tag{C1}
$$

where division by two is in $\mathbb Z/r\mathbb Z$ and

$$
f_{ba}(-d)=f_{ab}(d).
$$

For $a=b$, only $d\ne0$ is needed and the condition says
$f_{aa}(-d)=f_{aa}(d)$. Thus (C1) is a well-defined undirected
edge coloring. Translating every second coordinate by $t$ fixes
$\infty$ and adds $t$ to every color.

This action has $r$ old vertex orbits, rather than one. The
[one-point transitivity exclusion](symmetry_obstructions.md)
does not apply merely from this stated symmetry. Additional
symmetry of particular functions could, of course, make it apply.

All color graphs are isomorphic. Every old-edge orbit has length
$r$: a translation stabilizing an unordered same-row edge could
only swap its endpoints, which would require $2t=0$; oddness
forces $t=0$. Distinct-row endpoints cannot be swapped by this
action. Colors run once through the palette on each orbit.
Consequently each color has

$$
\frac{r-1}{2}\text{ edges in each row},\qquad
r\text{ edges between each pair of rows},\qquad
1\text{ edge from }\infty\text{ to each row}.
$$

Its total size is exactly $r(r^2+1)/2$. On any $k$ whole rows
its edge count is $(rk^2-k)/2$, and adjoining $\infty$ makes
this $(rk^2+k)/2$.

These exact symmetry and edge counts supply no independence bound.
Whether any choices of the functions have $\alpha(G_c)\le r$
for every color remains unproved; whether the template itself
can be excluded also remains unproved. It must not be described
as a counterexample or as an established promising construction.

## Nonabelian one-point template (excluded for large r)

**Superseded.** The [one-point transitivity theorem](symmetry_obstructions.md)
excludes this entire template for $r\ge100$, without prescribing the function
below. Its description identifies exactly which construction family that theorem
eliminates.

A further construction attempt used an odd-order nonabelian group $B$,
$|B|=r$, with vertices $(B\times B)\cup\{\infty\}$ and colors $B$.
Color $\infty(g,h)$ by $gh^{-1}$. For
$f:B^2\setminus\{(1,1)\}\to B$ satisfying

$$
f(I,J)=I f(I^{-1},J^{-1})J^{-1},
$$

color $\{(g,h),(gI,hJ)\}$ by $g f(I,J)h^{-1}$.
The displayed identity makes the color independent of the ordering of
the two endpoints. Left multiplication by $(a,b)$ sends colors by
$c\mapsto acb^{-1}$, so all color graphs are isomorphic.

In color $1$, an old vertex $(g,h)$, with $d=g^{-1}h$, has degree

$$
|f^{-1}(d)|+\mathbf1_{d=1}.
$$

Thus unequal fibers can supply the degree irregularity absent from
regular constructions. No function $f$ with independence number at most
$r$ was obtained. A choice making all these degrees $r$ is excluded by
the existing Brooks argument; irregular choices are not excluded by
that argument. This is a well-defined template, not a counterexample
or an independence certificate.

No counterexample was constructed. The arguments below exclude specified
families, not all colorings. No isolated-parameter random or exhaustive
search was performed.

The separate [partial-net obstruction](partial_net_obstruction.md)
records an infinite incidence model considered during the color-coupling
approach. It satisfies the partial-resolution conditions but fails the
private-row capacity constraint. It rules out a proposed inference from
incidence alone, not the original coloring assertion.

Throughout, a putative counterexample has color graphs with
$\alpha(G_i)\le r$. In particular, each color has clique number at most
$r$, and every $(r+1)$-set has at least $r-1$ edges outside any specified
color.

## Basic barriers

**Regular color graphs cannot suffice.** If every $G_i$ is regular, with
degree $d_i$, then $d_i\le r-1$ gives an independent $(r+1)$-set by greedy
coloring. If $d_i=r$, Brooks's theorem gives an $r$-coloring of $G_i$,
since a $K_{r+1}$ is forbidden and $r\ge3$; again there is an independent
$(r+1)$-set. Thus every $d_i\ge r+1$, contradicting
$\sum_i d_i=r^2$. This excludes difference-colorings in which translations
preserve every color separately.

The later [symmetry obstruction](symmetry_obstructions.md) excludes
all vertex-transitive constructions even if the action permutes
colors. It also excludes abelian-equivariant one-point extensions of every
order $r\ge101$, without prescribing old affine-direction edges.

**Even one full clique resolution is impossible.** The stronger argument
in [packing tools](packing_tools.md) proves that no color can contain
$r$ disjoint $K_r$'s, for any $r\ge3$. The target-color lower bound is
$(2r-1)\binom r2+r$; the final $r$ counts the edges from the remaining
vertex to the blocks. Together with the other-color bounds, the excess
over the total edge budget is $(r-1)(r-2)/2$. Therefore extending the
standard affine example requires changing edges in **every** original
singleton-direction class.

The checked [affine edit-distance argument](affine_edit_obstruction.md)
now requires more than

$$
\frac{(r-1)r^2}{16\sqrt r+1}
=\left(\frac1{16}-o(1)\right)r^{5/2}
$$

old-edge recolorings. It counts defective original rows and uses
matching-transversal rigidity and the hereditary span theorem.
The older bounds $2(r-1)^2$, or $(r-1)(2r-1)$ for $r\ge5$,
remain useful for small parameters.
This is only a restriction on extensions of that particular construction.

**Small incident palettes cannot suffice.** The coupled greedy
decomposition in [Palette and cut bounds](palette_and_cut_bounds.md)
shows that every vertex sees more than $4r/5$ colors. Its later
global defect bound is stronger: at most $\lfloor(r-1)/4\rfloor$
vertex--color incidences are missing in the entire coloring.
That note also bounds the number of absent colors across disjoint sets;
a balanced bipartition of the entire vertex set uses at least
$r-1$ colors. These conditions exclude specified sparse-palette
templates, not arbitrary asymmetric colorings.

**Two-direction incidence constructions are too rigid.** A color formed
by the union of two parallel-class clique systems on a retained point set
is the line graph of a bipartite incidence graph. If its independence
number is at most $r$, König's theorem covers its vertices by at most
$r$ underlying lines. Each line contains at most $r$ retained points,
because it is a monochromatic clique. Hence the retained set has size at
most $r^2$. Uneven point deletions do not avoid this obstruction.

The [line-graph obstruction](line_graph_obstruction.md) extends this
barrier: a least color cannot be the line graph of any loopless
multigraph, even with unrestricted multiplicities and a nonbipartite
root. The proof uses Tutte--Berge, inherited density on an odd matching
obstruction, concentration on heavy pairs, and a final three-vertex
energy inequality. No reduction of arbitrary colors to line graphs is
known.

**The pentagon does not automatically multiply.** The strong square of
$C_5$ has an independent five-set, for example
$\{(i,2i):i\in\mathbb Z/5\mathbb Z\}$, rather than the desired bound
$2\cdot2=4$. Product color classes also overlap on pairs for which one
coordinate agrees. Removing those overlaps destroys the clique bags on
which the naive independence calculation depends. Lexicographic products
retain two colors rather than producing the required growing palette.

A sparse clique-blowup substitute is also invalid: take two disjoint
$K_r$'s, distinguish one vertex in each, join the distinguished vertices,
and add a vertex adjacent to all other vertices of the two cliques. Its
independence number is two, but it contains a $K_{r+1}-e$, violating the
local color cap. The stronger [two-row obstruction](two_row_structure.md)
excludes any $(2r+1)$-vertex target subgraph of independence two for
$r\ge4$.

## A checked independent-transversal input

Glock and Sudakov, *An average degree condition for independent transversals*,
J. Combin. Theory Ser. B **154** (2022), 370--391,
[Theorem 1.2, printed p. 372](https://people.math.ethz.ch/~sudakovb/transversals-average-degree.pdf),
states the following. For every $\varepsilon>0$ there is $\gamma>0$ such that a
graph partitioned into parts $V_j$ has an independent transversal provided


$$
|V_j|\ge(1+\varepsilon)D,\qquad
\frac{1}{|V_j|}\sum_{v\in V_j}d(v)\le D,
$$


and the maximum degree between any two distinct parts is at most
$\gamma D$. The theorem statement and its definition of local degree
were checked in the primary paper. Its proof was not independently
reproved. The deductions here use this stated theorem, not an unstated
average-degree variant.

### Deficiency counting

Suppose a target graph of independence number at most $r$ has its vertices
partitioned into $q>r$ cliques, each of size at least $m$. Let $J$ consist
only of target edges between distinct parts. Assume its local degree is
at most $\gamma m/(1+\varepsilon)$.

As long as more than $r$ parts remain, their cross graph has no independent
transversal. Apply the preceding theorem with $D=m/(1+\varepsilon)$.
Some part then has average cross degree greater than $D$. Deleting that
whole part removes more than $m^2/(1+\varepsilon)$ cross edges. Part sizes
and the local-degree bound persist. Repeating until $r$ parts remain
proves


$$
e(J)>\frac{(q-r)m^2}{1+\varepsilon}. \tag{1}
$$


Thus a construction must pay for the entire independence deficiency
$q-r$, not merely for destroying one full transversal. An analogous
application after fixing an independent set $I$ uses the surviving lists
$C_j\setminus N(I)$ and deficiency $q-r+|I|$, provided those lists still
meet the size and local-degree hypotheses.

## A subfield lift of the pentagon

The following was a parameterized candidate, not a completed coloring.
Let $t$ be a prime power, and put


$$
q=t^2,\qquad r=t(t-1),\qquad m=(t-1)^2.
$$


In the affine plane over $\mathbb F_q$, retain


$$
S=\bigl((\mathbb F_q\setminus\mathbb F_t)
\times(\mathbb F_q\setminus\mathbb F_t)\bigr)\cup\{(0,0)\}.
$$


Then $|S|=r^2+1=qm+1$. Prescribe each edge whose slope lies in
$\mathbb F_q\setminus\mathbb F_t$ to receive its slope color. There are
exactly $r$ such colors. Leave the $t+1$ subfield directions, including
the vertical direction, available for arbitrary coloring.

For a prescribed slope $c\notin\mathbb F_t$, every affine line
$y=cx+b$ has exactly $m$ points in the retained grid: its $t$ points with
$x\in\mathbb F_t$ and its $t$ points with $y\in\mathbb F_t$ intersect
in exactly one point. The line through the origin gains the extra point.
Consequently every prescribed color is initially


$$
K_{m+1}\ \sqcup\ (q-1)K_m.
$$


Its independence number must be reduced from $q=r+t$ to $r$. Unlike the
original affine example, this retains no full $r$-block resolution and
its deficient region grows with the parameter. For $t=2$, the prescribed
edges can be completed to the exceptional two-color pentagon.

The available edges have cross local degree at most $t+1$ between any
two prescribed clique blocks: each reserved-direction line through a
vertex meets a prescribed-slope line at most once.

### Exact edge accounting and rejection

Each prescribed color contains
$q\binom m2+m=r^2(m-1)/2+m$ edges. Subtracting the $r$ prescribed
color classes from $\binom{r^2+1}{2}$, and using
$r-m+1=t$ and $r-2m=-(t-1)(t-2)$, gives


$$
2E_{\rm free}=r^3t-r(t-1)(t-2),
\qquad
\frac{E_{\rm free}}r
=\frac{tr^2-(t-1)(t-2)}2. \tag{2}
$$


If a completion existed, apply (1) to each prescribed color, with its
$q$ blocks and the added edges. Fix $\varepsilon=1/4$. Since
$(t+1)/m\to0$, the checked transversal theorem applies for all
sufficiently large $t$. Every color would need more than


$$
\frac{t m^2}{1+\varepsilon}
$$


added edges. But $m/r=(t-1)/t\to1$, so this required amount is
asymptotic to $\tfrac45tr^2$, while the average available amount in (2)
is asymptotic to $\tfrac12tr^2$. Summing over colors is impossible.

This rejects the subfield candidate for all sufficiently large $t$.
No explicit cutoff is claimed, and no remaining finite values were
searched or certified. The failure does not exclude constructions that
also recolor the prescribed edges or that have large cross local degree;
those changes remove the hypotheses used in the deficiency count.

## Fixed-independence component substitutions

The hereditary span theorem gives a further uniform obstruction. If all
components of even one color have independence number at most $a$, where
$r\ge64a^2$, then each component $C$ has
$|C|\le r\alpha(C)$. For independence one this is the clique cap;
otherwise apply [Hereditary span](hereditary_span_bound.md) to a subset
of order $r\alpha(C)+1$ if necessary. Summing over components gives

$$
r^2+1\le r\sum_C\alpha(C)=r\alpha(G)\le r^2,
$$

a contradiction. Thus fixed-independence component gadgets, including
nonuniformly distributed pentagon gadgets, cannot supply a family of
counterexamples as $r\to\infty$. This does not exclude connected
constructions whose independence grows with $r$.

A proposed stronger statement about deleting a bounded number of
vertices to make a color perfect was **not established**. Its attempted
proof removed many full $K_r$'s using a greedy extension at total size
$r+1$, whereas that lemma only guarantees extension through size $r$.
No such bounded-surgery obstruction is being claimed here.

## Two reserved directions in the next affine order

**Proved rejection for $r\ge4096$.** Let $q=r+1$ be a prime power.
In the affine plane of order $q$, retain any $r^2+1=q^2-2q+2$
points. Prescribe $r=q-1$ directions as distinct colors, retaining
every edge within their lines in its prescribed color. Complete the
coloring using only the remaining two directions' edges.
No such completion is a counterexample when $r\ge4096$.

This was a distinct candidate from the subfield lift. The initial
independence bound in each color is $r+1$, only one too large,
and the available edge count is asymptotic to $r^2$ per color.
The earlier one-step transversal deficiency estimate did not
reject it. The total-edge lemma in [Packing tools](packing_tools.md)
does, without an external asymptotic transversal theorem.

Suppose a completion were a counterexample. For each prescribed
color its $r+1$ parallel-line blocks have size at most $r$, by the
monochromatic clique cap. They are all nonempty, since $r$ blocks
of size at most $r$ cannot cover $r^2+1$ points. Their deficits
from $r$ sum to

$$
r(r+1)-(r^2+1)=r-1.
$$

Consequently all but the smallest block have size at least
$(r+1)/2$: the second-largest deficit is at most $(r-1)/2$.

Before point deletion the two reserved directions have
$2q\binom q2=rq^2$ edges in total. Thus some color receives at
most $q^2=(r+1)^2$ cross edges. Between two of its prescribed
parallel-line blocks, these edges have local degree at most two,
since each of the two reserved-direction lines through a vertex
meets another prescribed line at most once.

Fix any vertex in the smallest prescribed block of this color.
Its nonneighbor lists in the other $r$ blocks have size at least
$m=(r-3)/2$, and their cross graph still has local degree at most
two and at most $(r+1)^2$ edges. For $r\ge4096$,

$$
(r-3)^3>2048(r+1)^2,
\qquad (r+1)^2<\frac{m^3}{256}.
$$

For example, divide the first inequality by $(r+1)^2$:
the function $(r-3)^3/(r+1)^2$ is increasing for $r>3$,
and at $r=4096$ it exceeds $2048$.
The total-edge transversal lemma produces independent representatives
of these $r$ lists. Together with the fixed vertex they contradict
the required independence bound.

This handles arbitrary, possibly very uneven, point deletions and
arbitrary assignments of reserved edges. It does not exclude
constructions that also recolor the prescribed-direction edges.
No remaining finite parameter was searched.

## Extending the affine plane of order r minus one

**Proved rejection for $q=r-1\ge2940$.** Start with any affine plane
of order $q$, coloring its $q^2$ points by the $q+1=r$ direction
classes. Adjoin $2q+2$ arbitrary vertices, retaining every old edge
color. No choice of new edges yields an E617 counterexample in the
stated range. If $q$ is even, $q\ge261$ suffices (so even prime-power
orders $q\ge512$ are excluded). This is a different construction
family from the earlier one-point and reserved-direction extensions.

Let $B$ be the $m=2q+2$ new vertices. For color $i$, put
$e_i=e(G_i[B])$, $\omega_i=\omega(G_i[B])$, and
$S_i=e_i(B,V_{\rm old})$. Exact totals are

$$
\sum_i e_i=(q+1)(2q+1),\qquad
\sum_i S_i=2(q+1)q^2. \tag{3}
$$

For an old color-$i$ line $L$, put $A_w=N_i(w)\cap L$ and
$a_w=|A_w|$. The cap on $L\cup\{u,v\}$ gives

$$
a_u+a_v+\mathbf1_{\{uv\in E(G_i)\}}\le q+1. \tag{4}
$$

Thus at most one new vertex has $a_w>(q+1)/2$. Remove these heavy
vertices over all $q$ lines of direction $i$. The remaining set
$B_i$ has size $n_i\ge q+2$, with $h_i=m-n_i\le q$ removed.

For each such line define a graph $F_L$ on $B_i$ by
$uv\in E(F_L)$ exactly when $A_u\cup A_v=L$. Every non-color-$i$
pair in $B_i$ belongs to some $F_L$: otherwise it can be augmented
by one old common nonneighbor from each of the $q$ direction lines,
giving an independent $q+2=r+1$-set. Put $c=\lfloor q/2\rfloor$.
Every nonisolated vertex of $F_L$ has at least $c$ color-$i$ neighbors
in $L$, since all retained $a_w\le\lfloor(q+1)/2\rfloor$.

Each $F_L$ is 3-colorable. For odd $q=2k+1$, choose a $k$-subset
of each complement $L\setminus A_w$. Adjacent vertices receive
disjoint subsets. Such subsets have a proper 3-coloring: fix two
elements; use the first if present, the second if only that is
present, and the third color when neither is present. Two sets of
the third type lie in a $(2k-1)$-set and cannot be disjoint. For even
$q=2k$, every nonisolated complement has size $k$ and adjacent
complements are complementary $k$-sets, giving a bipartite graph.

Let $b=3$, or $b=2$ for even $q$. Independently select one of $b$
color classes in each $F_L$, leaving its isolated vertices unrestricted.
If $t_w$ counts the line graphs in which $w$ is nonisolated, it
survives with probability $b^{-t_w}$. All survivors form a color-$i$
clique, so AM--GM gives

$$
\sum_{w\in B_i} b^{-t_w}\le\omega_i,
\qquad
\sum_{w\in B_i}t_w\ge n_i\log_b(n_i/\omega_i).
$$

Every removed heavy vertex costs at least $c$ star edges, and every
remaining active line incidence costs at least $c$ more. These charges
are disjoint, hence

$$
S_i\ge c\left[h_i+n_i\log_b(n_i/\omega_i)\right]. \tag{5}
$$

Write $M=\sum_i n_i$ and $\Omega=\sum_i\omega_i$. From
$\omega_i(\omega_i-1)\le2e_i$ and Cauchy--Schwarz,

$$
\Omega\le rW,\qquad W=\frac{1+\sqrt{16q+9}}2.
$$

The log-sum inequality in (5) gives

$$
\frac{\sum_i S_i}{c}\ge rm-M+M\log_b(M/\Omega).
$$

Since $M\ge r(q+2)$, the expression is increasing in $M$ throughout
this range whenever $\log_b((q+2)/W)\ge1$. Substituting the lower
bound for $M$ and using (3) yields

$$
2q^2\ge c\left[q+(q+2)\log_b
\frac{2(q+2)}{1+\sqrt{16q+9}}\right]. \tag{6}
$$

For $q\ge2940$, the logarithm's argument exceeds $27$, equivalently
$q^2-2939q-1508>0$. With $b=3$, the right side of (6) then exceeds
$c(4q+6)>2q^2$, a contradiction. For even $q\ge261$, the argument
exceeds $8$, equivalently $q^2-260q-140>0$, and $b=2$ gives the same
contradiction. The covering, coloring, and incidence steps and the
threshold arithmetic were separately checked.

This does not exclude constructions that recolor old direction edges.
No remaining finite parameter was searched.

## Uniform rejection of nearby larger affine orders

**Proved.** Let an affine plane have order $q=r+s$, where $s\ge1$.
Retain any $r^2+1$ of its points. Prescribe $r$ directions in distinct
colors, keeping every retained pair in one of these directions in its
prescribed color. Assign the pairs in the remaining $s+1$ directions
arbitrarily. This cannot be an E617 counterexample if

$$
\boxed{r\ge1024(s+1)^2.} \tag{7}
$$

The plane need not be Desarguesian. This extends the earlier
two-reserved-direction obstruction uniformly to a growing gap $q-r$;
it is still a restriction on a construction family, not a positive
case of the unrestricted problem.

Put $d=s+1$. The $d$ unprescribed directions contain at most
$dq^2(q-1)/2$ pairs before point deletion. Hence some prescribed
color receives at most

$$
E\le\frac{dq^2(q-1)}{2r}<\frac{dq^3}{2r}
$$

added edges. Its prescribed parallel lines give $q$ clique blocks,
including empty blocks. Between two distinct blocks, the added graph
has local degree at most $d$: each unprescribed line through a point
meets the other prescribed line in at most one point.

Suppose that the completed coloring is a counterexample. Each block
then has order at most $r$, and its block deficits from $r$ sum to
$qr-(r^2+1)=rs-1$. Call blocks of order less than $r/2$ small,
and write $k$ for their number. Their deficits give $k<2s$, so
$k\le2s-1$. If $k<s$, there are at least $r+1$ large blocks;
we will find a transversal of any $r+1$ of them.

If $k\ge s$, put $\ell=k-s$. The union of the small blocks
has at least

$$
r^2+1-(q-k)r=r\ell+1
$$

vertices. Within this union the selected color has maximum degree
plus one less than or equal to

$$
r/2+(k-1)d\le r/2+2(s-1)d\le r.
$$

The last inequality follows from (7). Greedy selection therefore
gives $t=\ell+1\le s$ independent vertices. They lie in distinct
small blocks, automatically handling any empty blocks. There are
$q-k=r-\ell$ large blocks. In each, remove the neighbors of these
$t$ vertices; its remaining list has order at least

$$
r/2-td\ge r/2-sd\ge m:=7r/16.
$$


In both cases the lists under consideration have order at least $m$,
cross local degree at most $d$, and at most $E$ cross edges. Since
$s/r\le1/16$, one has $q\le17r/16$, and

$$
E<\frac{4913}{8192}dr^2
<\frac{5488}{8192}dr^2
\le\frac{343r^3}{524288d}
=\frac{m^3}{128d}.
$$

Also $m\ge8$. The [total-edge transversal lemma](packing_tools.md)
supplies independent representatives. In the first case there are
$r+1$ of them; in the second they combine with the small-block set
to give $(r-\ell)+(\ell+1)=r+1$ independent vertices, a contradiction.

The deficit count, small-block degree bound, empty-line cases, and
constants were checked by the author and are author-recorded. No
search over isolated values
of $r$ or unverified computational input is used.
