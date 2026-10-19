---
name: research/erdos_132/minkowski_sum_layers
title: Convex layers of bounded-factor Minkowski sums
desc: |
  Support directions control full digit sums; a convex-sumset incidence
  theorem also gives polynomial rarity for their dense selected subsets.
sources: []
research_state: closed
created: 2026-09-22T22:45:00Z
updated: 2026-10-14T00:26:52Z
---


# Convex layers of bounded-factor Minkowski sums

***

This rules out a proposed counterexample mechanism; it does not solve
[Problem 132](../../problems/distance_problems/E0132/_index.md). Multiplicities are
unordered.

## The layer bound

Let

$$A=B_1+\cdots+B_d\subset\mathbb R^2,\qquad 1\le |B_i|\le b.$$

Write $C_k(A)$ for the union of the first $k$ convex-hull vertex
layers, with the usual degenerate final layers. Then

$$
|C_k(A)|\le
bd\sum_{j=0}^{3(k-1)}\binom dj b^j
\le bd(1+bd)^{3(k-1)}, \tag{1}
$$

where $\binom dj=0$ for $j>d$.

Fix a representation $x=\sum_i x_i$, $x_i\in B_i$.
For an index subset $J$, call the selection on $J$ bad if
$\sum_{i\in J}x_i$ is not a vertex of
$\operatorname{conv}(\sum_{i\in J}B_i)$.

A selected sum is a vertex precisely when there is a vector $u$ with

$$u\cdot(x_i-y)>0\quad
\text{for every }i\text{ and }y\in B_i\setminus\{x_i\}.$$

Indeed, this says that the selected point is the unique maximizer of
$u$ in every summand. Conversely, a uniquely exposed sum cannot have
a nonmaximal summand or a tied alternative in a summand.
Failure of these strict inequalities is equivalent, by strict
separation, to zero lying in the convex hull of the finite set of
nonzero vectors $x_i-y$. Planar Carathéodory then supplies a witness
using at most three vectors, hence at most three factors. Therefore
every bad selection contains a bad index subset of size at most three.

If a representation has $t$ disjoint bad index subsets, its point has
layer depth at least $t+1$. Induct on $t$. On one bad subset, express
its selected sum as a nontrivial convex combination of distinct other
partial sums. After adding the unchanged complementary summands, the
resulting points still have $t-1$ disjoint bad subsets. By induction
they survive the first $t-1$ layer deletions. Their convex combination
therefore cannot have been removed earlier and is not a vertex at
layer $t$. This proves the claim.

For a point in $C_k(A)$, take a maximal family of disjoint bad subsets
of size at most three. Its union $J$ has at most $3(k-1)$ indices.
The complementary selection is a vertex selection: otherwise it
would contain another small bad subset, contradicting maximality.

For each possible $J$, there are at most $b^{|J|}$ choices of its
selected sum. The complementary Minkowski sum has at most $bd$
vertices, since planar polygon edge-direction lists merge under
Minkowski addition. The same bound covers point and segment summands;
an empty complementary sum has one vertex. Counting these possibilities
proves the first inequality in (1). For the second, bound
$\binom dj\le d^j/j!$ and compare with the binomial expansion of
$(1+bd)^{3(k-1)}$.

## Consequence for rare distances

Let $r_k$ be the $k$-th largest distinct distance, when it exists.
The checked [rank–layer bound](layers_and_obstructions.md) gives

$$
m_A(r_k)\le4^{k-1}|C_k(A)|
\le bd\,[4(1+bd)^3]^{k-1}. \tag{2}
$$

For fixed $b$, suppose a sequence of such sumsets has
$|A|/d^M\to\infty$ for every fixed $M$. Then each fixed right-hand
side in (2) is eventually at most $|A|$, so

$$R(A)\longrightarrow\infty.$$

The required fixed ranks eventually exist: two distinct anchor
points locate the other points among at most two intersections for
each pair of pinned distance values, giving $|A|\le2q(A)^2+2$.
For exponentially large sumsets with fixed $b$, (2) gives the
quantitative lower bound $\Omega(\log|A|/\log(d+1))$.

For example, put $\omega=(1+i\sqrt3)/2$ and

$$
A_d=\sum_{j=0}^{d-1}(\sqrt3)^j\{0,1,\omega,1+\omega\}.
$$

This set has $4^d$ points. In each of the two real coordinate
directions $1,\omega$, a digit sum in base $\sqrt3$ splits into its
even and odd powers, yielding $p+\sqrt3\,q$ with distinct base-three
digit expansions for $p,q$. Thus the two independent binary digit
choices give exactly $4^d$ distinct planar points.

The complex-scale version with $\sqrt3$ replaced by $1+\omega$ has
at least $3^d$ points: the digits $0,1,\omega$ are distinct modulo
$1+\omega$ in $\mathbb Z[\omega]$, whose quotient is $\mathbb F_3$.
Successive reduction modulo the base proves uniqueness of these
three-digit expansions. In both cases (2) forces
$R(A_d)=\Omega(d/\log(d+1))$.

These conclusions allow all distance-class mergers caused by the
algebraic scales. They do not assume generic directions or a rational
Euclidean coordinate field.

## Cartesian products

There is a stronger elementary bound for an arbitrary product
$A=S\times T$, independent of the spacing of the real sets $S,T$.
After deleting $h$ points, each quadrant order has at most $h+1$
maximal surviving points. For the northeast order, list them with
increasing first coordinate; their second coordinates strictly
decrease. For each consecutive pair
$(x_i,y_i),(x_{i+1},y_{i+1})$, the product point
$(x_{i+1},y_i)$ dominates both and must have been deleted. These
witnesses are distinct.

Every hull vertex maximizes some generic linear functional and is
therefore maximal in one of the four quadrant orders. The next hull
has at most $4(h+1)$ vertices. If $h_k$ counts the points in the first
$k$ layers, then

$$h_0=0,\qquad h_k\le5h_{k-1}+4,\qquad h_k\le5^k-1.$$

Consequently $m_A(r_k)<20^k$ whenever rank $k$ exists, and
$R(A)=\Omega(\log |A|)$ for Cartesian products.

## Selected subsets: a convex-sumset incidence bound

There is a separate argument tolerating arbitrary deletions in a dense
regime. Let $A\subseteq P+Q$, where $n=|A|\ge2$, $p=|P|$, $q=|Q|$, and both
factors are nonempty. Theorem 1 of Eisenbrand--Pach--Rothvoß--Sopher, [*Convexly
independent subsets of the Minkowski sum of planar point
sets*](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v15i1n8/pdf/)
(2008), bounds every convexly independent subset of $P+Q$ by

$$H=C\bigl(p^{2/3}q^{2/3}+p+q\bigr), \tag{3}$$

for an absolute constant $C\ge1$. The theorem and its incidence proof
were read in the full paper, pp. 2--3. No generic-position or
unique-representation assumption is imposed.

Every convex-vertex layer of $A$ is such a subset, including degenerate
final layers after enlarging $C$. The
[angular rank bound](layers_and_obstructions.md) therefore yields

$$m_A(r_j)\le2j|C_j(A)|\le2j^2H.$$

Consequently

$$R(A)\ge\max\left\{1,
 \left\lfloor\sqrt{\frac{n}{2H}}\right\rfloor\right\}. \tag{4}$$

For rank existence, if there are $t$ layers, then $t\ge n/H$.
The rank--depth lemma applied to a deepest point and any distinct
point gives $q(A)\ge t$. If the floor in (4) is positive, then
$n/H\ge2$ and this floor is at most $n/H$. Thus every rank used
exists. The additional lower bound one is the diameter theorem.

Now let $A$ be any subset of $B_1+\cdots+B_d$, with
$1\le |B_i|\le b$, and write $N=\prod_i|B_i|$ for the formal
product size, not the actual number of sums. Split the factors at
the first prefix product $\alpha\ge\sqrt N$ and put $\beta=N/\alpha$.
Then $\alpha\le b\sqrt N$, $\beta\le\sqrt N$. Empty factor groups
are interpreted as the singleton sumset $\{0\}$. The resulting
sumsets $P,Q$ have $p\le\alpha$, $q\le\beta$, and $pq\le N$.
Hence (3) gives $H\le C_bN^{2/3}$, with $C_b=C(b+2)$, and

$$R(A)\ge\max\left\{1,
 \left\lfloor\sqrt{\frac{|A|}{2C_bN^{2/3}}}\right\rfloor\right\}. \tag{5}$$

In particular, for fixed $b,c>0$, $|A|\ge cN$ implies
$R(A)=\Omega_{b,c}(|A|^{1/6})$. More generally, (5) forces growth
whenever $|A|/N^{2/3}\to\infty$. Collisions and arbitrary deletions
are permitted, provided the stated density condition survives.

The author checked the factor split, rank existence, and the exact
scope of the cited theorem; the argument is author-recorded.

## Exact scope

The support-direction argument (1)--(2) applies to the full Minkowski
sum, and the Cartesian-product argument applies to full products.
They do not themselves survive arbitrary deletions. The separate
incidence bound (3)--(5) handles selected subsets at the densities
just stated, not every sparse selection or nonproduct window.
No bounded-rarity counterexample was found, and no reduction of
arbitrary planar sets to the displayed sumsets was proved.
