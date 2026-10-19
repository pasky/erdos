---
name: research/erdos_617/light_independent_set_obstruction
desc: Degree-balancing counterexamples and low-energy rounding; greedy succeeds below an approximately three-quarter energy-excess threshold.
tags: [graph-theory, proved, critical-graphs]
sources: []
created: 2026-09-22T06:08:00Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/light_independent_set_obstruction

***

**This is not a counterexample to Problem 617.** It disproves a proposed
auxiliary lemma: a connected independence-critical graph need not have
a maximum independent set whose average degree is at most the graph's
average degree. Independence-critical means that deleting any edge
increases the independence number.

The distinction matters for the [least-budget core](minimal_ratio_potential.md).
If such a core had a maximum independent set of degree sum at most
$a\overline d$, its total degree surplus would be less than $r-a$.
Sections 1--3 show that independence-criticality alone cannot supply that
assertion. The stronger construction in Sections 4--8 also has a
two-supported maximum independent set and the core's strict induced
minimal-ratio conditions. Both constructions fail the full hereditary
density caps and the least-color budget, so the assertion using those
additional hypotheses remains open.

## 1. An auxiliary four-clique graph

Fix an integer $p\ge7$, let $A=(\mathbb Z/p\mathbb Z)^6$, and put
$q=p^6$. Index its coordinate vectors by ordered pairs $ij$ of distinct
members of $\{1,2,3\}$, writing them $e_{ij}$. Put
$V_i=\{i\}\times A$. On $V_1\cup V_2\cup V_3$ define $F$ by making

$$
\{(i,x),(j,x),(j,x+e_{ij}),(j,x+2e_{ij})\}
\tag{1}
$$

a clique for every $i\ne j$ and $x\in A$, and adding no other edges.

Then $\omega(F[V_i])=3$: the internal edges change one incoming
coordinate by $\pm1$ or $\pm2$, so its components are Cartesian
products of two copies of $C_p^2$, each of clique number three.
Between $V_i,V_j$, adjacency is exactly

$$
y-x\in\{0,e_{ij},2e_{ij},-e_{ji},-2e_{ji}\}. \tag{2}
$$

An internal edge in $V_i$ changes a coordinate $e_{ki}$, and can
have a common neighbor in $V_j$ only when $j=k$, since differences
of the vectors in (2) use only $e_{ij},e_{ji}$. Thus a clique
meeting all three parts has at most three vertices.

A clique cannot have two vertices in each of two parts either.
Its internal differences would be nonzero multiples of $e_{ji}$
and $e_{ij}$ respectively. Its four cross adjacencies would require
four corners of a nondegenerate coordinate rectangle to lie in the
union of those two coordinate axes. Among two distinct coordinate
values on each axis, choose a nonzero value on each; their corner
does not lie on either axis. This is impossible. Therefore
$\omega(F)=4$, with equality supplied by (1). Also (1) shows that
every vertex outside $V_i$ is complete to some triangle in $V_i$.

## 2. Critical pruning preserves the required incidences

Take $\overline F$ on the three parts, adjoin independent vertices
$j_1,j_2,j_3$, and join $j_i$ precisely to $V\setminus V_i$.
Call this graph $G_0$. Its independence number is four. A set
avoiding the $j_i$ corresponds to a clique of $F$; a set containing
exactly $j_i$ has at most three further vertices, all in $V_i$;
a set containing two $j_i$ has no outside vertex.

Every edge $j_iv$, $v\notin V_i$, is independence-critical already
in $G_0$. Choose a triangle $T\subseteq V_i$ complete to $v$ in
$F$; after deleting $j_iv$, the set $\{j_i,v\}\cup T$ is independent.

Choose an inclusion-minimal spanning subgraph $H\subseteq G_0$
with $\alpha(H)=4$. Every edge $j_iv$ just described must survive,
so $H$ is connected, and each outside vertex still sees exactly
two of $j_1,j_2,j_3$. By construction $H$ is independence-critical.
Every possible choice of this minimal subgraph works below.

## 3. Blow up the three special vertices

Replace each $j_i$ by a clique of order $t\ge4q$, retaining all its
adjacencies, to obtain $H_t$. Clique blowups preserve independence
number and independence-criticality. For cross edges, lift the
original critical-edge witness. For an edge within a replacement
clique, replace its original vertex in a maximum independent set
by the two endpoints. Such a maximum independent set exists through
every vertex of $H$, by a critical witness for an incident edge.

Thus $H_t$ is connected and independence-critical, with

$$
\alpha(H_t)=4,\qquad |H_t|=3(t+q).
$$

Every replacement vertex has degree $t-1+2q$, and every other
vertex has degree $2t+h(v)$, where $0\le h(v)\le3q-1$. Hence

$$
\overline d(H_t)
\le\frac{3t(t-1+2q)+3q(2t+3q-1)}{3(t+q)}
=t+3q-1. \tag{3}
$$

A maximum independent set consists either of four outside vertices,
or of one replacement vertex and three outside vertices. Consequently
every maximum independent set $I$ satisfies

$$
\sum_{v\in I}d(v)\ge\min\{8t,7t+2q-1\}
>4(t+3q-1)\ge4\overline d(H_t). \tag{4}
$$

The strict inequalities follow from $t\ge4q$. For example, at
$t=4q$ the graph has $15q$ vertices and every maximum independent
set has degree sum at least $30q-1>28q-4$.

This is a conceptual counterfamily to the auxiliary assertion, not
numerical evidence. It supplies no counterexample to the inherited
density conditions or to the original edge-coloring problem.

## 4. A stronger obstruction with two-support and induced ratio bounds

**Theorem.** For arbitrarily large integers $r$, there is a connected,
independence-critical, $K_r$-free graph $H$ such that

$$
|H|=9r+1,\qquad \alpha(H)=9,\qquad
|W|\le r\alpha(H[W])\quad(\varnothing\ne W\subsetneq V(H)),
\tag{5}
$$

and $H$ has a two-supported maximum independent set, but every maximum
independent set $J$ satisfies

$$
\sum_{v\in J}d_H(v)>9\overline d(H).
\tag{6}
$$

Here two-supported means that every outside vertex has one or two
neighbors in the indicated maximum independent set. In particular,
(5) also implies $\delta(H)\ge r$, by applying it outside a closed
neighborhood. The graphs below nevertheless violate both the least-color
edge budget and the full inherited density caps.

The construction uses clique blowups of a fixed graph of order 25.
First we give an exact integral example with weak induced ratio bounds,
then perturb its weights to obtain (5).

### A rank-preserving subdivision lemma

For a graph $L$, call a nonnegative vector $x$ rank-feasible when

$$
x(U)\le\alpha(L[U])\qquad(U\subseteq V(L)).
\tag{7}
$$

Replace an edge $uv$ by a path $u-p-q-v$, and retain the old weights.
Give $p,q$ weights $t,1-t$, where

$$
x_v\le t\le1-x_u.
\tag{8}
$$

Then the enlarged vector is rank-feasible in the enlarged graph.

To prove this, let $U$ be the old vertices of an induced set. If both
new vertices are included, a maximum independent set of $L[U]$ can be
augmented by one of them: it cannot contain both $u,v$. The new rank
is therefore at least $\alpha(L[U])+1$, as required. If neither is
included, removing the old edge cannot lower the rank. Suppose only
$p$ is included, and write $k=\alpha(L[U])$. If the new rank is at
least $k+1$, use $t\le1$. Otherwise $u\in U$ and
$\alpha(L[U\setminus\{u\}])=k-1$: an independent $k$-set avoiding
$u$ could be augmented by $p$. Consequently

$$
x(U)+t\le k-1+x_u+t\le k.
$$

The case with only $q$ is symmetric. This proves the lemma.

Odd subdivision increases the independence number by one. It also
preserves independence-criticality for connected critical graphs other
than $K_2$. For completeness, witnesses for untouched edges lift by
adjoining one new internal vertex. A critical witness for $uv$ lifts
after deleting either new end edge. For the new middle edge, use a
maximum independent set avoiding $u,v$, together with both new vertices.
Such a maximum set exists: choose an edge $uw$ with $w\ne v$ and
delete $u$ from its critical witness. A connected critical graph other
than $K_2$ has minimum degree at least two. Indeed, if $u$ is a leaf
at $v$ and $vw$ is another edge, a critical witness for $vw$, after
replacing $v$ by $u$, would already exceed the original independence
number.

## 5. The fixed critical graph and its exact weights

Let $F$ have vertices

$$
v_0,\ldots,v_4,\quad u_0,\ldots,u_4,\quad s,
$$

with indices modulo five. Its edges are

$$
v_iv_{i+1},\qquad u_iv_{i-1},\ u_iv_{i+1},\qquad su_i.
\tag{9}
$$

Thus $F$ is the Mycielski graph of a five-cycle. It is triangle-free,
and every nonedge has a common neighbor. For two $u$-vertices use $s$;
for $s,v_i$ use $u_{i+1}$; the remaining cases follow directly from
the five-cycle. Hence $F$ is maximal triangle-free. Its complement
$G$ is connected and independence-critical with $\alpha(G)=2$.

The neighbors of $u_0$ in $G$ are

$$
v_0,v_2,v_3,u_1,u_2,u_3,u_4.
$$

Subdivide all seven of these edges twice, obtaining $Q$, so that

$$
|Q|=25,\qquad \alpha(Q)=9.
$$

It remains connected and independence-critical by the preceding lemma.
The maximum set $\{s,u_0\}$ of $G$ is two-supported. Extend it by
choosing, on each new path, the internal vertex farther from $u_0$.
This gives a two-supported maximum set of $Q$: an old neighbor of
$u_0$ has its support at $u_0$ replaced by the new anchor, while the
other internal vertex sees exactly $u_0$ and the new anchor.

In the order $(v_0,\ldots,v_4,u_0,\ldots,u_4,s)$, assign the old
vertices the integral weights

$$
w_{\rm old}=(146,199,146,146,199,146,117,91,91,117,602).
\tag{10}
$$

Their sum is 2000. For the following ordered edges $ab$, replace
$ab$ by $a-p-q-b$ and use the indicated weights:

| Ordered edge $ab$ | $w_p$ | $w_q$ |
|---|---:|---:|
| $v_0u_0$ | 616 | 384 |
| $v_2u_0$ | 537 | 463 |
| $v_3u_0$ | 537 | 463 |
| $u_0u_1$ | 117 | 883 |
| $u_0u_2$ | 91 | 909 |
| $u_0u_3$ | 91 | 909 |
| $u_0u_4$ | 117 | 883 |

The total weight on $Q$ is 9000. The normalized vector
$x=w/1000$ satisfies every rank inequality (7). On $G$, it suffices
to check cliques, because $\alpha(G)=2$ and the total weight is two.
A clique containing $s$ consists of $s$ and at most two $v$-vertices,
of total integral weight at most $602+398=1000$. A clique avoiding
$s$ has weight at most $562+398=960$: 562 is the total $u$-weight,
and 398 bounds the weight of its at most two $v$-vertices. Each
subdivision then satisfies (8), as is immediate from the table, so
the rank-preserving lemma applies successively.

## 6. Exact degree certificate

Put $M=I+A(Q)$ and $D=Mw$. The old vertices have closed weighted
degrees

$$
D_{\rm old}=(1838,1471,1838,1838,1471,1872,
1843,1816,1816,1843,1438).
\tag{11}
$$

The two new vertices on a subdivided edge $ab$ have closed weighted
degrees $1000+w_a$ and $1000+w_b$, respectively. Thus, in the order
of the table, their degree pairs are

$$
(1146,1146),\ (1146,1146),\ (1146,1146),\
(1146,1117),\ (1146,1091),\ (1146,1091),\ (1146,1117).
\tag{12}
$$

Direct summation gives

$$
w^{\mathsf T}Mw=11\,162\,060.
\tag{13}
$$


Here is a short exhaustive argument for the least closed weighted
degree sum of a maximum independent set, avoiding a search certificate.
Let $T$ be its old vertices, and let $b(T)$ count subdivided edges
with both endpoints in $T$. The seven paths contribute at most
$7-b(T)$ internal vertices. The old graph of $Q$ is $G$ with all
edges at $u_0$ removed, so $|T|\le3$ and

$$
|T|-b(T)=2.
$$

If $|T|=2$, then $b(T)=0$ and $T$ is an edge of $F$. If $|T|=3$,
then $T=\{u_0,a,b\}$, where $ab\in E(F)$ and $b(T)=1$.
Each case attains the bound on the number of internal vertices.

The baseline least internal cost, when no path is excluded by two
chosen endpoints, is

$$
3\cdot1146+2\cdot1117+2\cdot1091=7854.
$$

Selecting $u_1$ or $u_4$ forces an extra internal cost of 29;
selecting $u_2$ or $u_3$ forces an extra cost of 55. Incorporate
these charges into the adjusted old costs

$$
c=(1838,1471,1838,1838,1471,1872,
1872,1871,1871,1872,1438).
\tag{14}
$$

When both endpoints of a subdivided edge are chosen, subtract 1146
from this accounting. Therefore the exact minimum cost for a fixed
$T$ is

$$
C(T)=7854+\sum_{v\in T}c_v-1146b(T).
\tag{15}
$$

Every edge $ab$ of $F$ satisfies $c_a+c_b\ge3309$. This follows
immediately for the three edge types in (9): the minimum for a
$v$--$v$ edge is $1471+1838=3309$, for a $u$--$v$ edge it is at
least $1871+1471=3342$, and for an $s$--$u$ edge it is
$1438+1871=3309$. Consequently the minimum in (15) is

$$
\min_{J\text{ maximum in }Q}\sum_{v\in J}(Mw)_v=11\,163.
\tag{16}
$$

Equality is attained when $T=\{v_0,v_1\}$, for example. Sets with
three old vertices have cost at least
$7854+1872+3309-1146=11889$.

Replace every vertex $v$ of $Q$ by a clique of order $w_v$.
The resulting graph $H_0$ is connected and independence-critical,
has independence number nine, and retains the two-supported maximum
set. Clique blowups preserve criticality by lifting critical witnesses;
for an edge inside one bag, replace its original vertex in a maximum
set by the two endpoints. Every vertex of a connected critical graph
belongs to a maximum independent set.

Every induced set with support $U\subseteq V(Q)$ has independence
number $\alpha(Q[U])$ and order at most $w(U)$. Thus

$$
|W|\le1000\alpha(H_0[W])\qquad(W\subseteq V(H_0)).
$$

However, (13)--(16) give

$$
\min_{J\text{ maximum}}\sum_{v\in J}d_{H_0}(v)=11\,163-9=11\,154,
$$

whereas

$$
9\overline d(H_0)
=\frac{11\,162\,060-9000}{1000}
=11\,153.06.
\tag{17}
$$

This is an exact counterexample to degree balancing under two-support,
criticality, and the weak full induced-ratio condition.

## 7. Perturbing to the strict core ratio

For a vector $z\ge0$ with $z(V(Q))=9$, define

$$
g(z)=\min_{J\text{ maximum in }Q}
\mathbf1_J^{\mathsf T}Mz-z^{\mathsf T}Mz.
$$

This is continuous, and the preceding exact certificate gives

$$
g(x)=\frac{940}{10^6}>0,
\qquad x^{\mathsf T}Mx=11.16206>11.
\tag{18}
$$

Let $y$ be the average of the incidence vectors of all maximum
independent sets of $Q$. Then $y>0$, $y(V(Q))=9$, and

$$
y(U)<\alpha(Q[U])
\quad(\varnothing\ne U\subsetneq V(Q)).
\tag{19}
$$

For the strict inequality, choose a critical edge crossing the cut
$U,V(Q)\setminus U$. Its critical witness, after deleting either
endpoint, gives two maximum independent sets whose intersections
with $U$ have different sizes. At least one therefore has intersection
size smaller than $\alpha(Q[U])$. Positivity follows because every
vertex belongs to a maximum independent set.

Choose a sufficiently small positive rational $\varepsilon$, and put

$$
z=(1-\varepsilon)x+\varepsilon y.
$$

Then $z$ is positive and rational, has total weight nine, satisfies
all proper rank inequalities strictly, and retains
$g(z)>0$ and $z^{\mathsf T}Mz>11$. For arbitrarily large integers
$r$ clearing its denominators, all proper nonempty $U$ satisfy

$$
r z(U)\le r\alpha(Q[U])-2.
\tag{20}
$$

Make the clique-bag orders $r z_v$, and add one vertex to any one
bag. The resulting graph $H_r$ has order $9r+1$. An induced set
whose support $U$ is proper satisfies (5), by (20). A proper induced
set with full support has independence number nine and order at most
$9r$, so it also satisfies (5). Every clique has proper support of
rank one, and (20) makes its order at most $r-1$. Thus $H_r$ is
$K_r$-free. Criticality and two-support are preserved by the blowup.

For the degree inequality, let $m$ denote the integer bag-order
vector and put $z_r=9m/(9r+1)$. Then $z_r\to z$ and

$$
\min_{J\text{ maximum in }H_r}\sum_{v\in J}d_{H_r}(v)
-9\overline d(H_r)
=\frac{9r+1}{9}\,g(z_r)>0
$$

for all sufficiently large admissible $r$. This proves the theorem.

## 8. Why the construction does not satisfy the density caps

The strict perturbation was chosen with $z^{\mathsf T}Mz>11$.
Consequently

$$
2e(H_r)=r^2z^{\mathsf T}Mz+O(r)>11r^2
$$

for all sufficiently large $r$. The least-budget core bound when $a=9$ is
$2e\le10r^2-8r$, so it fails for all sufficiently large $r$.
The full inherited cap already fails on the whole graph: at order
$9r+1$ it would give

$$
2e(H_r)\le2D_r(9r+1)=9r^2+63r+18.
$$

Thus even criticality, two-support, minimum degree $r$, exclusion of
$K_r$, and the strict proper-subgraph ratio condition do not suffice
for a light maximum independent set. Any surviving version must use
additional information, such as the least-color edge budget or the
full hereditary density caps. This obstruction does not combine or
exclude the two actual cores of Problem 617.

## 9. The budget alone does not give the weaker light-set bound

**Checked counterexample to a weaker auxiliary assertion, not to E617.**
The desired bridge in the budgeted core is a maximum independent set
of degree sum at most $a(r-1)+r+1$. Even this weaker bound does not
follow from independence-criticality and the edge budget alone.

Let

$$
H=2K_{88}\ \dot\cup\ C_{11}^{\,2}[K_{20}],
\qquad r=79,\quad a=5.
$$

Here $C_{11}^{\,2}$ joins vertices at cyclic distance one or two, and
$[K_{20}]$ replaces every vertex by a clique of order twenty.
An independent set in $C_{11}^{\,2}$ has cyclic gaps at least three,
so its independence number is three, attained by vertices $0,3,6$.
Consequently

$$
|H|=176+220=396=5\cdot79+1,\qquad \alpha(H)=5.
$$

Vertices in the two clique components have degree $87$, while vertices
in the blowup have degree $5\cdot20-1=99$. Thus

$$
2e(H)=176\cdot87+220\cdot99=37092
\le37130=5\cdot79\cdot78+79\cdot80.
$$

Every maximum independent set uses one vertex from each clique and
three from the blowup. Its degree sum is therefore

$$
2\cdot87+3\cdot99=471>470=5(79-1)+79+1.
$$


The graph is independence-critical. Deleting a distance-two edge of
$C_{11}^{\,2}$ permits four vertices with cyclic gaps $2,3,3,3$;
deleting a distance-one edge permits gaps $1,3,3,4$. In each case the
deleted edge is the sole adjacency among the four vertices. Every vertex
belongs to a maximum independent set by cyclic symmetry. Critical
witnesses lift through the clique blowup; an internal bag edge is
handled by using its two endpoints instead of its base vertex in a
maximum independent set. Disjoint clique components preserve criticality.

This graph is disconnected and violates the inherited clique cap,
since $88>79$. It therefore leaves the actual capped-core light-set
question open. Its normalized quadratic energy, for
$x=(5/396)\mathbf1$, is

$$
x^{\mathsf T}(I+A_H)x
=\frac{25\cdot37488}{396^2}<6=a+1.
$$

Thus a Motzkin--Straus argument based only on this low-energy threshold
cannot prove the bridge. The rank conditions or hereditary caps must
enter; here $x$ is not rank-feasible, since its weight on a $K_{88}$
is $440/396>1$. No argument with the full core hypotheses was completed.
This is an explicit auxiliary
counterexample, not an isolated positive case or a search for an E617
counterexample.

## 10. An unresolved rank-feasible low-energy rounding route

The latest attempt at the missing light-set bound has the following
precise form. It is **unproved**, even with independence-criticality.
Let $\alpha(G)=a$, $M=I+A_G$, and suppose $x\ge0$ satisfies

$$
x(V)=a,\qquad x(U)\le\alpha(G[U])\quad(U\subseteq V).
$$

The candidate implication is

$$
x^{\mathsf T}Mx<a+1
\quad\Longrightarrow\quad
\min_{\substack{I\text{ independent}\\|I|=a}}
\mathbf1_I^{\mathsf T}Mx\le a+1. \tag{21}
$$

Neither the rank-feasible counterexample in Sections 4--8, whose
energy exceeds $a+2$, nor the low-energy example in Section 9, which
fails rank feasibility, decides (21).

There is a useful exact reformulation. Since
$\alpha(G-N[v])\le a-1$, rank feasibility gives

$$
(Mx)_v=x(N[v])\ge1.
$$

Thus $y=Mx-\mathbf1\ge0$ and
$x^{\mathsf T}Mx=a+x\cdot y$. The missing conclusion is a maximum
independent set of $y$-weight at most one, assuming $x\cdot y<1$.

**Proved extension fact.** Every independent $J$ with $y(J)<1$ extends
to a maximum independent set. Otherwise
$\alpha(G-N[J])\le a-|J|-1$, and rank feasibility would give

$$
x(N[J])\ge |J|+1.
$$

On the other hand,

$$
x(N[J])\le\sum_{v\in J}(Mx)_v=|J|+y(J)<|J|+1,
$$

a contradiction. In particular any maximal independent set of
$y$-weight less than one is maximum. An arbitrary extension need not
preserve the weight bound. A rounding argument producing such a
low-weight **maximal** set has not been obtained.

For the [least-budget minimal-ratio core](minimal_ratio_potential.md),
put $n=ar+1$ and $x=(a/n)\mathbf1$. Proper-induced minimality makes
$x$ rank-feasible, while the budget gives

$$
x^{\mathsf T}Mx
\le\frac{a^2((a+1)r^2+r+1)}{(ar+1)^2}<a+1.
$$

For the strict inequality, the difference after multiplying by
$(ar+1)^2$ is $a(a+2)r-a^2+a+1>0$. If (21) held, integrality for $a\ge2$
would yield

$$
\sum_{v\in I}d(v)
\le\left\lfloor\frac{(a+1)(ar+1)}a-a\right\rfloor
=a(r-1)+r+1.
$$

This is the desired weaker light-set bound, but would still **not**
solve E617. The resulting $I$ need not be two-supported or the
intersection with a foreign full clique. No argument controls
outsiders with three or more anchor neighbors. Conversely the
[common component-balancing weights](cross_color_cores.md) have exact
residue masses and a coupled energy bound, but only clique feasibility,
not the full rank feasibility required in (21).

The attempted weighted rounding and component averaging have therefore
not combined the two surviving reductions. Computation on selected
templates supplied no proof and is not used as evidence for (21).

## 11. A squared-slack bound for the degree-minimal maximum set

**Proved.** Let $\alpha(G)=a$, $M=I+A_G$, and $x\ge0$ with
$x(V)=a$. Set

$$
y=Mx-\mathbf1,\qquad e=x\cdot y=x^{\mathsf T}Mx-a.
$$

If $e<1$, every independent set maximizing the weight
$w=\mathbf1-y$ has cardinality $a$, and any such maximizer $J$
satisfies

$$
\boxed{\sum_{j\in J}y_j^2\le e.} \tag{22}
$$

This statement does not require rank feasibility or $y\ge0$.

For every vertex $v$, exchange the vertices of $J\cap N[v]$
for $v$ (the exchange does nothing when $v\in J$). Optimality
gives

$$
w_v\le\sum_{j\in J\cap N[v]}w_j.
$$

Multiplication by $x_v\ge0$ and summation yield

$$
a-e=x\cdot w
\le\sum_{j\in J}w_j(Mx)_j
=|J|-\sum_{j\in J}y_j^2.
$$

Therefore

$$
e\ge a-|J|+\sum_{j\in J}y_j^2.
$$

Since $|J|\le a$ is integral and $e<1$, this proves (22).

For the least-budget minimal-ratio core, use
$x=(a/(ar+1))\mathbf1$. Among maximum independent sets,
maximizing $w$ is exactly minimizing the degree sum. Thus the
degree-sum-minimal maximum independent set has squared slack
at most the energy excess, which is strictly below one.
The original-degree greedy argument in
[Minimal core structure](minimal_core_structure.md) only produced
some maximum independent set; it did not establish this conclusion
for the degree-sum-minimizer.

The remaining issue is still the linear cost $y(J)\le1$.
Cauchy--Schwarz applied to (22) gives only
$y(J)\le\sqrt{ae}$ when $y\ge0$, not the required bound.
No inference from a squared-slack bound to (21) is warranted.

### Independence two does satisfy the stronger rounding bound

For $a=2$ and $x(V)=2$, one has

$$
\min_{I\text{ maximum independent}}\mathbf1_I^{\mathsf T}Mx
\le x^{\mathsf T}Mx
\qquad\text{whenever }x^{\mathsf T}Mx<3. \tag{23}
$$

This does not need rank feasibility. Let $F=\overline G$,
$d=A_Fx$, and $s=x\cdot d=4-x^{\mathsf T}Mx>1$.
Average $d_u+d_v$ over edges $uv$ with weights $x_ux_v$.
Their total weight is $s/2$, and the weighted sum is
$\sum_vx_vd_v^2\ge s^2/2$. Some edge of positive weight
therefore satisfies $d_u+d_v\ge s$. Since
$Mx=2\mathbf1-d$, its endpoints form a maximum independent
set of $G$ with cost at most $4-s=x^{\mathsf T}Mx$, proving
(23).

Neither result addresses the unbounded independence range of the
surviving cores. The exchange argument and weighted-edge averaging
were checked by the author and are author-recorded; no computation is
needed for them.

## 12. Greedy rounding at a stronger partial threshold

**Proved.** Let $\alpha(G)=a\ge2$, $x\ge0$, $x(V)=a$, and

$$
y=(I+A_G)x-\mathbf1\ge0,\qquad e=x\cdot y.
$$

If

$$
\boxed{e\le\frac{3a+1}{4a},} \tag{24}
$$

then minimum-original-$y$ greedy produces a maximum independent set
$I$ with $y(I)\le1$. Strict inequality in (24) gives $y(I)<1$.
Rank feasibility is needed only to establish $y\ge0$, not elsewhere
in this argument. If $a=1$, the graph is complete and $y=0$.

At each step choose a vertex of minimum original $y$ among the
remaining vertices and delete its closed neighborhood in the remaining
graph. Write the chosen costs as $0\le q_1\le\cdots\le q_k$, and
let $b_i$ be the $x$-mass deleted at step $i$. Then

$$
\sum_i b_i=a,\qquad 0\le b_i\le1+q_i,\qquad
e\ge\sum_i b_iq_i\ge\sum_i b_i^2-a\ge a^2/k-a.
$$

Since $k\le a$ and (24) implies $e<1$, necessarily $k=a$.

Put $p=\sum_{i<a}q_i$. Minimize $\sum_i c_iq_i$ subject to
$0\le c_i\le1+q_i$ and $\sum_i c_i=a$. Filling the earliest
coordinates first is optimal. If $p\ge1$, this optimum can be
supported on at most $a-1$ coordinates. For that optimum,

$$
e\ge\sum_i c_iq_i\ge\sum_i c_i^2-a
\ge a^2/(a-1)-a>1,
$$

a contradiction. Thus $p<1$, so an earliest-fill optimum has
$c_i=1+q_i$ for $i<a$ and $c_a=1-p$. Therefore

$$
e\ge p+\frac{p^2}{a-1}+(1-p)q_a. \tag{25}
$$


If $s=p+q_a\ge1$, monotonicity of the greedy costs gives

$$
q_a\ge\max\{1-p,p/(a-1)\}.
$$

For $p\le(a-1)/a$, (25) yields

$$
e\ge1-p+\frac a{a-1}p^2\ge\frac{3a+1}{4a}.
$$

For larger $p$, it yields $e\ge ap/(a-1)\ge1$. If $s>1$ in
the first range, the first inequality is strict because $1-p>0$.
These observations prove both versions of the claim. Zero $x$-weights
and arbitrary greedy ties cause no difficulty.

The argument was checked by the author and is author-recorded. It is a
uniform rounding
theorem, but the actual core budget only guarantees $e<1$, with its
upper bound tending to one. Thus (24) does **not** prove the proposed
full-threshold implication (21).

## 13. A fractional assignment supplied by the rank inequalities

There is another exact consequence of rank feasibility. Fix any maximum
independent set $J$. Every vertex has nonempty support
$S(v)=N[v]\cap J$. For $T\subseteq J$, put

$$
U_T=\{v:S(v)\subseteq T\}.
$$

An independent set in $U_T$ of order greater than $|T|$ could replace
$T$ in $J$, so $\alpha(G[U_T])\le|T|$. Consequently

$$
x(U_T)\le|T|.
$$

These are the weighted Hall inequalities for assigning the vertex
masses $x_v$ to their neighboring anchors. More explicitly, every
vertex subfamily $R$ is contained in $U_{\cup_{v\in R}S(v)}$, so
its total mass is at most the number of its available anchors.
Finite capacitated Hall, or max-flow/min-cut, therefore gives numbers

$$
f_{v,j}\ge0,\quad f_{v,j}=0\ (j\notin S(v)),\quad
\sum_j f_{v,j}=x_v,\quad \sum_v f_{v,j}=1\ (j\in J).
$$

The last equalities follow because total mass and total anchor capacity
both equal $a$. Thus $e$ is the sum of the transported average
$y$-costs. No inequality comparing those costs with $y(J)$ has been
proved. In particular the supports define a transversal-matroid
assignment problem, but independent sets of the original graph are
not being claimed to be matroid independent sets.

### Why marginal-preserving repair is too strong

A concrete obstruction rules out converting every such rank-feasible
vector into a distribution on maximum independent sets with unchanged
marginals. Take a five-cycle and add a universal hub, and assign
$x_v=1/3$ at all six vertices. The graph has independence number two
and clique number three. This vector is rank-feasible: sets of size at
most three have weight at most one, while larger sets have weight at
most two and are not cliques. Its slack is $1/3$ at each rim vertex
and one at the hub, so

$$
x\cdot y=5/9+1/3=8/9<1.
$$

Every maximum independent set avoids the hub. No distribution on such
sets can therefore have hub marginal $x_{\rm hub}=1/3$. This does
**not** refute (21): every maximum independent pair has slack weight
$2/3$.

The attempted local repair of greedy selection has a separate gap.
Rank feasibility makes a deleted bucket of mass greater than one
contain an independent pair, but the pair can meet many other anchor
neighborhoods. It need not replace just the bucket representative and
the last costly greedy vertex. The extension lemma controls the final
cardinality, not the cost of the additional vertices. No repair with
controlled cost or controlled change of marginals was obtained.

## 14. A rank-preserving operation that adds a chosen cost

**Proved identity, not a proof or disproof of the rounding conjecture.**
Let $x$ be rank-feasible, with $x(V(G))=\alpha(G)=a$,
$y=(I+A_G)x-\mathbf1$, and $e=x\cdot y$.
Fix $v\in V(G)$. Add adjacent vertices $p,q$, make $p$ adjacent to
$v$ and no other old vertex, and give $q$ no old neighbors. Assign
masses $x_p=t$, $x_q=1-t$, where $0\le t\le1-x_v$.

The new independence number and total mass are both $a+1$, and the
new vector is rank-feasible. For induced sets containing both new
vertices, add $q$ to a maximum old independent set; for those containing
only $q$ the verification is equally immediate. Suppose only $p$ is
included, and the old induced independence is $k$. If adding $p$ does
not increase it, every old maximum independent set contains $v$.
The old set with $v$ removed has independence $k-1$, so its old weight
is at most $k-1+x_v$. Adding $t\le1-x_v$ proves the remaining rank
inequality.

The old slack changes only at $v$, by $y'_v=y_v+t$, while
$y'_p=x_v$ and $y'_q=0$. Therefore the new energy excess and the
least slack of a maximum independent set are exactly

$$
e'=e+2t x_v,\qquad
\min_{J\text{ maximum}}y'(J)
=\min_{I\text{ maximum in }G}
\bigl(y(I)+t\mathbf1_{\{v\in I\}}\bigr). \tag{26}
$$

Every maximum set using $p$ can replace it by $q$ without increasing
its cost, which proves the second identity.

Repeated attachments realize additive nonnegative costs $t_v$ on old
vertices at total excess cost $2\sum_v x_vt_v$, splitting increments
to meet $t\le1-x_v$. Positive increments at vertices with $x_v=1$
are not allowed. Thus a counterexample to the full-threshold rounding
claim would follow from a rank-feasible instance and such costs with

$$
\min_{I\text{ maximum}}(y+t)(I)>1,\qquad e+2x\cdot t<1.
$$

No such instance was established. Bounded tests using the existing
Mycielski-subdivision family found no counterexample; they are not a
proof of this implication or a certificate for all vectors.
The complementary near-Turan reformulation likewise remained open.
The established squared-slack and stronger-threshold greedy results
have not been extended to the full condition $e<1$.
