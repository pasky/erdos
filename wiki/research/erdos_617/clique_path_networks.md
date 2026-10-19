---
name: research/erdos_617/clique_path_networks
desc: Hereditary caps give fractional r-colorings of clique blowups of subdivisions, now allowing every root-edge path to have length at least two for r at least twelve.
tags: [graph-theory, proved, constructions, fractional-coloring]
sources: []
created: 2026-09-22T10:35:00Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/clique_path_networks

***

**Proved construction exclusion, not a resolution of Problem 617.**
The hereditary caps exclude a further family containing graphs with
claws, not just the line graphs already excluded in
[Line-graph obstruction](line_graph_obstruction.md).

Fix an integer $r\ge3$. Throughout,

$$
p_r(rq+b)=r\binom q2+qb\quad(0\le b<r),\qquad
D_r(n)=\binom n2-(r-1)p_r(n).
$$

A graph satisfies the caps if $e(H[W])\le D_r(|W|)$ for all $W$.
In fact the proofs below only use sets of order at most $2r-1$.

## 1. The class and the conclusion

Start with a loopless multigraph on a set of branch vertices, replace
every edge by an internally disjoint path of length at least three,
and replace every vertex of the resulting graph by a nonempty clique.
Two bags are completely joined exactly when their underlying vertices
are adjacent. Arbitrary positive, unequal bag orders are allowed.

**Theorem.** If the resulting graph $H$ satisfies the caps, then

$$
\boxed{\chi_f(H)\le r,\qquad |H|\le r\alpha(H).} \tag{1}
$$

There is no edge budget, order bound, or independence-number restriction.

More generally one may add edges between branch vertices provided those
direct branch edges form a disjoint union of cliques. The conclusion is
unchanged. Parallel subdivided paths are allowed, including paths whose
endpoints lie in the same direct branch clique. No other edges between
bags are allowed.

Here $\chi_f(H)\le r$ will be proved by constructing a probability
distribution on independent sets in which every vertex has probability
$1/r$ of being selected. Multiplying this distribution by $r$ gives a
fractional coloring of total weight $r$; taking expected cardinality gives
the second conclusion in (1).

In particular no color of an E617 counterexample can itself be one of
these graphs. If a color is a disjoint union of components in this class,
the same conclusion follows by summing the span inequalities.

## 2. Local consequences of the caps

There is no $K_{r+1}$, and an outsider has at most one neighbor in a
$K_r$: both assertions follow from
$D_r(r+1)=\binom r2+1$.
Consequently every bag has order at most $r$, every nonisolated branch
bag has order at most $r-1$, and every internal path bag has order at
most $r-2$.

For the last assertion, an internal bag of order $r-1$ together with
one vertex in a neighboring bag is a $K_r$. A vertex of its other
neighboring bag has $r-1\ge2$ neighbors in that clique, a contradiction.
The same argument shows that a branch bag of order $r-1$ has at most
one neighboring bag. If it is incident with a subdivided path, its
branch vertex therefore has multidegree one and no additional direct
branch neighbor.

Any adjacent pair of internal bags has total order at most $r-1$.
If its total were $r$, a vertex immediately before this pair would
force the first bag to have order at most one, and a vertex immediately
after it would force the second to have order at most one. This would
give $r\le2$.

For three consecutive bags of orders $a,b,c$, their only nonedges
are the $ac$ pairs between the first and third bags. Thus

$$
ac\ge(r-1)(a+b+c-r). \tag{2}
$$

If the right side is negative this is automatic; otherwise it follows
from the cap, since $p_r(n)\ge n-r$. The adjacent-pair clique bounds
also show that these triples have order at most $2r-1$.

Write $R=r-1$. A useful rearrangement of (2) is

$$
r-b-c\ge a-\frac{ac}{R}. \tag{3}
$$


## 3. Odd paths

Consider a path of length $2k+1$, with endpoint bag orders $a,f$ and
internal total $S$. Put $D=kr-S$.

For length three, write its bag orders as $(a,x,y,f)$ and
$\delta=r-x-y$. The internal-pair bound gives $\delta\ge1$.
Applying (2) at both ends and rearranging gives

$$
ax\le a+\delta(R-a),\qquad
fy\le f+\delta(R-f).
$$

Dividing by $a,f$ and using $x+y=r-\delta$ yields

$$
\delta\ge
\frac{(r-2)af}{R(a+f)-af}. \tag{4}
$$

The denominator is positive. If $a,f\le r-2$, then
$(R-a)(R-f)\ge1$, so (4) implies $\delta\ge af/r$.
If $a=R$ and $f\le r-2$, (4) gives
$\delta\ge f(r-2)/(r-1)>f-1$; integrality gives
$\delta\ge f\ge af/r$. The other case is symmetric.

The sole remaining case is $a=f=R$. The two adjacent internal bags
then have orders one, and the branch-degree observation in Section 2
makes this an entire isolated component with bag orders
$(r-1,1,1,r-1)$. Its order is $2r$, its independence number is two,
and it is $r$-colorable: use colors $1,\ldots,r-1$ on the first bag,
color $r$ on the next bag, color $1$ on the third bag, and colors
$2,\ldots,r$ on the last bag. Such components can be handled separately.

For every odd path of length at least five, there is a stronger bound:

$$
\boxed{D\ge\min(a,f)+k-2.} \tag{5}
$$

Write the end triples as $(a,b,c)$ and $(d,e,f)$. The middle path
between $c,d$ has odd length $2h+1$, where $h=k-2\ge0$; write $T$
for its internal total. Matching all its bags in consecutive pairs,
and then matching only its internal bags, gives respectively

$$
c+d+T\le(h+1)R,\qquad T\le hR.
$$

All these pairs consist of internal bags of the original path.
Therefore

$$
hr-T\ge h+(c+d-R)_+.
$$

Using (3) at both ends now gives

$$
D\ge a+f-\frac{ac+fd}{R}+(c+d-R)_++h.
$$

Assume $a\le f$. Since the coefficient of $f$ is nonnegative,
replace $f$ by $a$ on the right. After subtracting $a+h$ the
result is

$$
a\left(1-\frac{c+d}{R}\right)+(c+d-R)_+\ge0,
$$

using $0\le a\le R$. This proves (5).

Thus, except for the explicitly removed isolated components, every
odd path satisfies $S+af/r\le kr$. For length at least five it
even satisfies $S+\min(a,f)\le kr$.

## 4. Even paths

For a path of length $2k\ge4$, let $T$ be the total of *all* its bag
orders and put $E=T-kr$. Then

$$
\boxed{E\le(a+f-r)_+.} \tag{6}
$$


For length four, write the orders as $(a,b,c,d,f)$. The two end
triple inequalities (2) give

$$
E\le\frac{c(a+f-R)}R.
$$

If $a+f\le R$, this is nonpositive. Otherwise $a+f-R$ is a positive
integer and $c\le R-1$, so integrality gives
$E\le a+f-R-1=a+f-r$.

For length six, write the orders as $(a,b,c,z,d,e,f)$. Applying (2)
to the three triples centered at $b,z,e$ gives

$$
E\le\frac{cd-(R-a)c-(R-f)d}{R}.
$$

The numerator is bilinear in $c,d\in[0,R-1]$. Its maximum on this
rectangle is

$$
\max\{0,(R-1)(a+f-r)\},
$$

as is seen at the four corners. This proves (6).

For length at least eight, write the end triples as $(a,b,c)$ and
$(d,e,f)$ and retain the even middle path from $c$ to $d$. Its corresponding
excess $E_{\rm mid}$ satisfies (6) by induction. Equation (3) at the
two ends gives

$$
E\le E_{\rm mid}-c-d+\frac{ac+fd}{R}.
$$

If $c+d\le r$, the right side is nonpositive. If $c+d>r$, it is
at most $-r+(ac+fd)/R\le a+f-r$. This proves (6) in every case.

## 5. Coupling independent sets on a path

The following elementary probability lemma accounts for the endpoint
dependencies, rather than treating them as independent without proof.
Let $L\ge1$ and let $p_0,\ldots,p_L\in[0,1]$ satisfy
$p_i+p_{i+1}\le1$.
Prescribe an endpoint joint probability $q$ satisfying the Fréchet bounds

$$
(p_0+p_L-1)_+\le q\le\min(p_0,p_L). \tag{7}
$$


If $L=2k+1$ is odd, a distribution on independent sets of the path
with these marginals and this joint probability exists exactly when

$$
\sum_{i=1}^{L-1}p_i+q\le k. \tag{8}
$$

If $L=2k$ is even, it exists exactly when

$$
\sum_{i=0}^L p_i-q\le k. \tag{9}
$$

Necessity follows by counting selected vertices in each of the four
endpoint states. Here is a self-contained sufficiency proof.

The stable-set polytope of an odd cycle of order $2s+1$ is described by
nonnegativity, the edge inequalities, and $\sum x_i\le s$.
To check integrality, consider a fractional extreme point. The tight edge
equations on fractional coordinates form paths, unless the whole cycle
is at $1/2$, which violates the sum bound. Each path has an alternating
perturbation parameter. Two parameters can be perturbed while preserving
the sum; one can also be perturbed if the sum bound is slack or its path
has even order. In the only remaining case there is one odd-order
fractional path and the sum bound is tight. Its sum is an integer plus
$t$ or $1-t$, whereas all other coordinates and the total sum are
integers, forcing $t$ to be integral. This is again a contradiction.
Thus every feasible point is a convex combination of independent-set
indicators.

For odd $L$, add one vertex adjacent to both endpoints, forming an odd
cycle, and give it marginal $1-p_0-p_L+q$. Conditions (7)--(8) make
the vector feasible in the cycle polytope. The induced path distribution
has an endpoint joint $q'\ge q$, because the added vertex can occur only
when both endpoints are absent. On the original path there is also a
distribution with joint $(p_0+p_L-1)_+$: choose $U$ uniformly in $[0,1]$,
select even-indexed $i$ when $U\le p_i$, and odd-indexed $i$ when
$U>1-p_i$. Mixing these two distributions gives joint exactly $q$.

For even $L$, close the path with a new path of length three, whose
two internal marginals have sum $1-q$, the first at most $1-p_0$
and the second at most $1-p_L$. Such choices exist by (7). The resulting
odd-cycle vector is feasible by (9). Its endpoint joint $q'\le q$,
since selecting both endpoints excludes both new vertices. The threshold
distribution just described now has joint $\min(p_0,p_L)$, because
the two endpoints have the same parity. Mixing again gives $q$.

## 6. The global fractional coloring

Remove the isolated exceptional length-three components from Section 3.
In each direct branch clique independently, select a branch bag $v$ with
probability $w_v/r$, selecting none with the remaining probability.
These are valid probabilities because the joined branch bags constitute
a clique of order at most $r$. For no direct branch edges this simply
selects the branch bags independently.

An endpoint pair in different branch cliques has joint probability
$af/r^2$; one in the same branch clique has joint zero. Put $p_i=w_i/r$
on every subdivided path. Adjacent marginals sum to at most one.
For length three, Section 3 proves (8) for joint $af/r^2$, hence also
for zero. For longer odd paths, (5) proves (8) for *every* joint allowed
by (7). For even paths, (6) proves (9) for every allowed joint.

Apply the coupling lemma separately on each path. Conditional on the
already sampled endpoint states, sample its interior according to the
corresponding conditional distribution. Events of zero endpoint
probability need no choice. Interior paths have no edges between them,
so all the selected bags together form an independent set of the bag
graph, and every bag has marginal $w_v/r$.

Choose one uniformly random vertex from each selected bag. Every vertex
then has marginal $1/r$. This proves (1), including the direct-branch
extension.

There is a useful local form. Start with a distribution on independent
sets of the remaining graph in which every vertex has marginal exactly
$1/r$. Any clique path of length at least four, whose internal bags have
no neighbors outside their own and adjacent bags, can be inserted without
changing this outside distribution. The endpoint joint may be arbitrary.
The endpoint bags need only be disjoint cliques; their outside neighborhoods
need not be homogeneous, and edges between the endpoint cliques are allowed.

Every graph with $\chi_f\le r$ admits the required exact-marginal
normalization: divide fractional-color weights by $r$, pad with the
empty independent set, and independently thin the selected vertices to
reduce each marginal to $1/r$. This normalization can change the initial
distribution. A length-three path is not asserted to have the universal
extension property.

## Scope and the remaining structural gap

The initial odd-subdivision span proof and the enlarged fractional proof
were separately audited. The arguments use only the cap, elementary
probability, and the odd-cycle polytope proof above; no external
classification theorem or finite computation is invoked.

The class contains, for example, positive clique blowups of the graph
obtained by replacing each edge of $K_4$ by a path of length three.
Those graphs can have claws, so this is not a restatement of the
line-graph exclusion. The construction also permits an unbounded root
and unbounded residual independence number.

No surviving least-color core has been proved to admit this decomposition.
Its private-clique support description does **not** imply that exception
vertices can be organized into the internally disjoint paths used here.
Deleting a strip can leave a smaller graph with fractional chromatic
number above $r$ even when every proper induced set has Hall ratio at
most $r$. Thus rank minimality cannot be silently replaced by fractional
coloring minimality. This theorem excludes a parameterized construction
mechanism; it does not prove any new unrestricted E617 case.

## 7. Allowing paths of length two

**Theorem.** Let $r\ge12$. Start with a loopless multigraph, replace
every edge by an internally disjoint path of length at least two, and
replace every vertex by a nonempty clique, with complete joins exactly
between consecutive bags. If the resulting graph $G$ satisfies the
hereditary caps, then

$$
\boxed{\chi_f(G)\le r,\qquad |G|\le r\alpha(G).} \tag{10}
$$

Parallel root edges and unequal bag sizes are permitted. Unlike the
length-at-least-three theorem, this extension does **not** permit direct
edges between branch bags. A correlated distribution on the branch bags
replaces their independent selection.

### Minimum degree and a common correlation parameter

First assume $\delta(G)\ge r$. Put $R=r-1$, let $M$ be the largest
bag order, and set $d=r-M$. The clique cap gives $M\le r$.
A largest bag has at least $d+1$ common neighbors outside itself.
Together they form an $(r+1)$-set whose nonedges all lie among those
$d+1$ neighbors. Hence

$$
d(d+1)\ge2R.
$$

For $r\ge12$, this forces $d\ge5$, and therefore

$$
R\le d(d+1)/2\le(d-1)^2.
$$

Define

$$
\theta=\frac{M}{Rd}.
$$

Then $0<\theta<1$ and

$$
\theta\le\frac{d-2}{r+d-2}. \tag{11}
$$

After cross multiplication, the latter inequality is exactly
$r((d-1)^2-R)\ge0$.

Since branch bags are pairwise anticomplete, use the following mixture.
With probability $1-\theta$, select them independently with probabilities
$w/r$, where $w$ is the bag order. With probability $\theta$, choose
a common uniform $U\in[0,1]$ and select every branch bag with
$U\le w/r$. Each branch bag still has marginal $w/r$. Endpoint
bags of orders $a\le f\le M$ have joint selection probability

$$
j=\frac{af+\theta a(r-f)}{r^2}. \tag{12}
$$

We check that this single distribution can be extended along every path.

### Length two and length three

For a path with bag orders $(a,b,f)$, put $E=a+b+f-r$.
Its only nonedges are the $af$ endpoint pairs, so its cap and
$p_r(n)\ge n-r$ give $E\le af/R$. Since

$$
\theta=\frac{M}{R(r-M)}\ge\frac{f}{R(r-f)},
$$

equation (12) gives

$$
rj\ge\frac{af+af/R}{r}=af/R\ge E.
$$

This is precisely the even-path coupling requirement (9).

For a length-three path $(a,x,y,f)$, put $\delta=r-x-y$.
The end-triple caps, as in Section 3, give

$$
\delta\ge\frac{(r-2)af}{R(a+f)-af}.
$$

The coupling requirement is $rj\le\delta$. To check it for
arbitrary unequal endpoints, set $A=R-a$, $B=R-f$. Then
$A\ge B\ge d-1$, and the preceding bound implies

$$
\frac{r\delta-af}{a(r-f)}
\ge\frac{f(AB-1)}{(B+1)(R^2-AB)}
\ge\frac{B-1}{R+B}
\ge\frac{d-2}{r+d-2}
\ge\theta.
$$

For the second inequality, $(z-1)/(R^2-z)$ increases with $z$,
so replace $A$ by $B$, then use $f=R-B$. The third follows
by monotonicity in $B$. This proves the required upper bound for $j$.

Paths of length at least four extend every feasible endpoint joint,
by Sections 3--5. Sample all branch states first, then sample each
path interior conditional on its two endpoint states. The interiors
have no cross edges, so the samples combine into independent bags
with marginal $w/r$. Choosing one uniform vertex from each selected
bag gives each vertex marginal exactly $1/r$. This proves (10)
when the minimum degree is at least $r$.

### Removing the minimum-degree assumption

If $G-v$ already has an independent-set distribution with marginals
$1/r$ and $d_G(v)\le r-1$, then the event that no neighbor of $v$
is selected has probability at least $1-d_G(v)/r\ge1/r$.
Add $v$ on a randomized subevent of probability exactly $1/r$.
This preserves all existing marginals and gives the required marginal
at $v$.

Repeatedly delete vertices of degree at most $r-1$. In the remaining
induced graph the bags may have smaller orders or disappear. A nonempty
bag with quotient degree zero or one cannot remain: it and its sole
neighboring bag, if any, form a clique of order at most $r$, making
its vertices' degree at most $r-1$.

Thus a surviving original internal bag retains both its neighboring
bags. Propagating along its original path forces the whole path and
both branch bags to survive. The nonempty remainder is still a clique
blowup of a root subgraph with every path of length at least two.
Apply the minimum-degree construction to it, then restore deleted
vertices in reverse order by the preceding extension argument. If the
remainder is empty, start with the empty-set distribution.

This proves the fractional conclusion itself, not merely the unweighted
span inequality. It does not replace induced-ratio minimality by
fractional minimality. No least-color budget or independence restriction
is used in this theorem, and no general E617 core is known to have
the required subdivision structure.

The correlation bounds, arbitrary-endpoint coupling, preservation of
the class under taking the $r$-core, and reverse low-degree extension
were checked by the author and are author-recorded.
