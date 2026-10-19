---
name: research/erdos_774/lemmas/prime_staircase_obstruction
title: Mandatory root configurations with almost full height-two kernel rank
desc: A staircase of linear-size prime-grid circuits has a connected integral height-two circuit basis of density tending to one, yet every signed sum has a mandatory coordinate and one-prime extensions have only full-fiber minimal ternary supports.
tags: [E0774, proved, algebra, obstruction]
sources: []
created: 2026-09-18T17:30:00Z
updated: 2026-09-18T18:37:35Z
---


# Mandatory root configurations with almost full height-two kernel rank

***

## Theorem and consequence for the live route

There are finite dissociated sets $C_t$ inside distinct odd-prime root
grids with the following properties:

1. Their integer relation lattices have bases consisting of primitive
   height-two circuits, with connected support-intersection graph and
   supports covering every column. Their column images are saturated in the
   standard ambient integer tensor lattices.
2. Writing $k_t=\dim\ker_{\mathbb Q}C_t$,
   $$
   \frac{k_t}{|C_t|}\longrightarrow1.
   $$
3. Every nonzero signed sum on $C_t$ has a **mandatory coordinate**:
   one column occurs in every representation with coefficients $0,\pm1$.
4. For a fresh odd prime $p$, a subset of $C_t\otimes S_p$ is
   dissociated if and only if it contains no full $p$-fiber. In particular
   $\chi_1(C_t\otimes S_p)=2$.

This disproves the proposed high-density short-relation descent criterion even
for actual cyclotomic units and at coefficient height **two**. It strengthens
the earlier [density $1/20$ pivot construction](prime_pivot_obstruction.md) and
replaces the nonintegral diagnostic in
[the arithmetic-unit discussion](unit_arithmetic_descent.md).

It does **not** give a finite coloring of the full prime-root family, or
exclude a mechanism coupling the actual classes of a coloring of that family.
Saturation is included, so that additional hypothesis does not rescue the
proposed rank-density descent. The main counterexample remains unproved.

## 1. A coefficient-two circuit of size linear in the largest prime

Let $p<q<r$ be distinct odd primes. Identify the labels of
$S_p\otimes S_q$ with edges of $K_{p,q}$, oriented from row
vertices $u_1,\ldots,u_p$ to column vertices $v_1,\ldots,v_q$.
Its rational relation space is the space of graph gradients
$t_u-t_v$: the row and column simplex relations span a space of
dimension $p+q-1$, exactly the kernel dimension.

A label set is independent exactly when deleting its edges leaves a connected
graph. Indeed a supported nonzero gradient exists precisely when a potential
can take different constant values on the components of the remaining graph.
Thus a bond (a minimal nonempty edge cut) is a circuit, with primitive cut
coefficients $\pm1$.

Put $a=(u_1,v_1)$, $b=(u_2,v_2)$, and take the two bonds
$$
O=\delta\{u_1,v_2\},\qquad
S=\delta\bigl((\{u_1,\ldots,u_p\}\setminus\{u_3\})
\cup(\{v_1,\ldots,v_q\}\setminus\{v_1,v_2\})\bigr).
$$
Both sides of each cut induce connected complete bipartite graphs (possibly
stars). Their sizes are
$$
|O|=p+q-2,\qquad |S|=2p+q-4.
$$
Choose the cut potentials equal to one on the displayed sides. The
coefficients at $a,b$ are $+1,-1$ for $O$, and $+1,+1$
for $S$.

Construct a subset of $(S_p\otimes S_q)\otimes S_r$ by layers:

- Layer zero: $O\setminus\{a\}$.
- Layer one: $S\setminus\{a,b\}$.
- Each of the remaining $r-2$ layers: $\{a,b\}$.

Every layer is independent. The cut relation on $O$ represents
$a+b$ on its zero layer with coefficient $2$ at $b$ and
coefficients $\pm1$ elsewhere. The cut relation on $S$ represents
$a+b$ on layer one with all coefficients $\pm1$. The remaining
layers use $a+b$ itself.

The common-sum intersection is exactly $\mathbb Q(a+b)$. To see this,
the reference layers restrict it to $\operatorname{span}\{a,b\}$,
whose intersection with $\operatorname{span}(S\setminus\{a,b\})$
is that line: any relation on $S$ is a multiple of its cut relation.
The zero layer contains the line by its displayed representation. Since
each layer is independent, coefficients are uniquely determined by the
common sum. The simplex layer criterion now proves that the entire set
is a circuit with one primitive coefficient of magnitude two and all other
coefficients of magnitude one.

Its cardinality and rank are
$$
n(p,q,r)=3p+2q+2r-13,\qquad d(p,q,r)=n(p,q,r)-1\le7r. \tag{1}
$$
Realize the tensor columns faithfully by roots via the coprime cyclotomic
field identification. Denote this circuit by $B\cup\{w\}$, with
$|B|=d$, and reverse its signs if necessary to write
$$
2w=\sum_{b\in B}\epsilon_b b,\qquad\epsilon_b\in\{\pm1\}. \tag{2}
$$
Then $B$ is a rational basis. For any $b_0\in B$, the set
$$
T=(B\setminus\{b_0\})\cup\{w\}
$$
is an integer basis of $M=\mathbb Z(B\cup\{w\})$: equation (2)
solves for $b_0$ integrally. The sublattice $L=\mathbb ZB$ has
index two in $M$, since $w$ has exact order two modulo $L$.

The image $M$ is saturated in the standard ambient integer lattice.
Indeed the graph-gradient, bond, and common-span arguments above work over
every field, including characteristic two. The reference columns $a,b$
remain independent; the common intersection is still the nonzero line
$\operatorname{span}(a+b)$. Thus the full circuit matrix has nullity one
modulo every prime, with the displayed relation (whose coefficient two
may reduce to zero). Removing a coefficient-$\pm1$ column leaves a
rank-$d$ matrix over every such field. All its Smith invariant factors
are therefore one, proving saturation of $\mathbb ZT=M$.
The index-two sublattice $L$ itself is not saturated.

## 2. The staircase of column lattices

Choose such circuits $B_i\cup\{w_i\}$ on mutually disjoint prime
triples, and choose corresponding bases $T_i$, lattices $L_i,M_i$,
and ranks $d_i$. Fix $t$ and put $R=\prod_{i=1}^t d_i$.

Start with all $R$ columns in $B_1\cdots B_t$. For stage $j$,
adjoin all columns
$$
T_1\cdots T_{j-1}\,\{w_j\}\,B_{j+1}\cdots B_t. \tag{3}
$$
Call the resulting set $C_t$. Products are injective because conductors
are disjoint. The stages and the original base are disjoint: stage $j$
has rightmost distinguished coordinate $w_j$, whereas the original base
has no distinguished coordinates. Thus
$$
|C_t|=R+\sum_{j=1}^t\frac R{d_j},\qquad
\operatorname{rank}_{\mathbb Q}C_t=R. \tag{4}
$$

Before stage $j$, the generated lattice is
$$
M_1\otimes\cdots\otimes M_{j-1}\otimes
L_j\otimes\cdots\otimes L_t.
$$
After that stage it is the same tensor with $L_j$ replaced by $M_j$.
The quotient is
$$
(\mathbb Z/2\mathbb Z)^{R/d_j}, \tag{5}
$$
and the newly adjoined columns (3) are exactly a basis of this quotient.
Consequently **each** new column has exact order two modulo all preceding
columns, even after any earlier additions within its own stage.

Moreover, twice each new column is a signed sum of earlier actual columns:
use (2) in its $j$-th factor. All required products
$T_1\cdots T_{j-1}B_j\cdots B_t$ already occur. For a direct check,
classify each such tuple by its rightmost $w_i$; if there is none it is
in the initial base, and otherwise it appeared at stage $i<j$.

At the end, $\mathbb ZC_t=\bigotimes_iM_i$. Each $M_i$ is a direct
summand of its ambient integer tensor lattice by the preceding saturation
argument. Tensoring those direct summands shows that the image of $C_t$
is saturated too.

## 3. An integral height-two circuit basis and mandatory coordinates

Order the initial base first, then the new columns stage by stage. Equation
(5) has this consequence:

> In every nonzero integer relation, the coefficient at the greatest used
> column is even.

The greatest column cannot lie in the initial independent base. At a newly
added column, its coefficient must annihilate its exact order-two coset
modulo the preceding lattice, and therefore is even.

For every newly added column take its relation $2\,\mathrm{new}$
minus the signed old sum described above. These relations have height two
and are an **integer** kernel basis. They are independent by their triangular
last-column structure. Given any integer relation, its last coefficient is
even, so subtract an integer multiple of the corresponding displayed
relation to eliminate it; induction ends at the independent initial base.

Each basis relation is also a primitive rational circuit: its support is
a fixed nonzero pure tensor times the factor circuit $B_j\cup\{w_j\}$.
The supports cover every column. Their intersection graph is connected.
After stage one, its components are indexed by $B_2\cdots B_t$.
Inductively for $j\ge2$, after stage $j-1$, components are indexed by
the untouched
suffix in $B_j\cdots B_t$. A stage-$j$ circuit meets the components
for every $b_j\in B_j$, joining them for each later suffix; its other
circuits attach through old points. At the last stage only one component
remains.

The even-last-coefficient property forbids any ternary relation, so $C_t$
is dissociated. If two signed representations of the same nonzero value
had different greatest used columns, their difference would have last
coefficient $\pm1$, impossible. Thus every representation has the same
greatest used column, which is mandatory.

The pivot block of this integer kernel basis is **triangular**, not $2I$:
earlier pivot entries can be odd. Hence the construction does not contradict
the half-density ceiling for the older diagonal-pivot invariant, or any of
the binary-code bounds.

## 4. Density tends to one

Use consecutive disjoint triples of odd primes. Their largest primes $r_i$
have divergent reciprocal sum. Indeed convergence of that every-third-prime
subseries would imply convergence of the entire prime reciprocal series:
the next block's three terms sum to at most $3/r_i$. The divergence of
the prime reciprocal series also follows directly from Euler's finite
products and divergence of the harmonic series.

By (1), $s_t=\sum_{i\le t}1/d_i\ge\frac17\sum_{i\le t}1/r_i\to\infty$.
Equations (4) and the kernel basis give
$$
k_t=Rs_t,\qquad
\frac{k_t}{|C_t|}=\frac{s_t}{1+s_t}\longrightarrow1. \tag{6}
$$
Thus the span of the height-two relations is the full kernel and occupies
an arbitrarily large proportion of the column count, despite mandatory
coordinates.

## 5. The next prime still has only fiber obstructions

A ternary relation on a subset of $C_t\otimes S_p$ has a common
signed layer sum $u$. If $u=0$, every layer relation is trivial by
base dissociation. If $u\ne0$, its mandatory base column occurs in
every layer, giving a full $p$-fiber in the support. Conversely a full
fiber is itself a ternary simplex relation.

Therefore precisely the fiber-proper subsets are dissociated. Splitting
every fiber into two nonempty colors proves $\chi_1(C_t\otimes S_p)=2$.
In particular, no height-two rank-density threshold strictly below one can
guarantee a fiber-free relation in a one-prime extension, even for actual
root configurations with a connected primitive circuit basis.

## 6. A staircase is finitely colorable at every fixed height

The selected staircase cannot supply infinite fixed-height coloring:
for $t\ge1$ and every finite $h$,
$$
\chi_h(C_t)\le\left\lceil\log_2(h+1)\right\rceil. \tag{7}
$$
In particular $\chi_1(C_t)=1$ and
$\chi_2(C_t)=\chi_3(C_t)=2$.

To prove this, change signs of the leaves in each rational basis so that
$w_i=\frac12\sum_b e_{i,b}$. Individual column sign changes preserve
every coefficient-height coloring number. Order product-basis rows
lexicographically, with the distinguished deleted leaf $b_{0,i}$
largest in each factor. A column with $k$ pivot coordinates has leading
row obtained by replacing those pivots by distinguished leaves, with
leading coefficient $2^{-k}$.

For a fixed leading row $L$, let $Z$ be the positions where $L$
uses the distinguished leaf. The staircase columns with leading row $L$
have pivot sets exactly the initial segments of $Z$. Indeed before the
last pivot, membership in the $T$-prefix forbids an un-replaced
distinguished leaf; after it, the $B$-suffix forbids any pivot. Thus
there is at most one column per pivot count $k$ at each leading row.

Choose $m=\lceil\log_2(h+1)\rceil$, so $2^m>h$, and color by
pivot count modulo $m$. In a monochromatic height-$h$ relation,
take the greatest participating leading row and, among its columns, the
largest participating pivot count $K$. Its row equation, multiplied by
$2^K$, makes the coefficient of that column divisible by $2^m$,
because every other participating count differs by a positive multiple of
$m$. That coefficient is nonzero and of magnitude at most $h<2^m$,
a contradiction. This proves (7). A displayed height-two circuit supplies
the lower bound two for $h=2,3$.

The union of staircases over **all factor orderings** is the full product
of the factor circuits: put all pivot positions before all distinguished-leaf
positions to include a given tuple. But the subfamily using only pivots and
distinguished leaves is rationally independent, as a tensor of independent
pairs. Incompatible orderings or same-leading-row collisions alone therefore
do not force a relation. Any use of their union must also control the neutral
leaves and their full expansions. No such actual-color argument was proved.

## 7. Parity cores and the limitation of separate lattice indices

Put $R_2=\mathbb Z_{(2)}$, the rationals with odd denominator.
A finite configuration $C$ has an ordering in which every nonzero
integer relation has even greatest coefficient if and only if every
nonempty $S\subset C$ has an $x$ satisfying
$$
x\notin\operatorname{span}_{R_2}(S\setminus\{x\}). \tag{8}
$$
An odd coefficient at $x$ in an integer relation is equivalent to an
$R_2$-expression of $x$ using the other columns, by clearing odd
denominators. Thus an $R_2$-essential point can be removed and placed
last, proving one direction inductively. In the other direction, the last
point of any subset satisfies (8).

The repeated deletion of essential points has a unique terminal redundant
core. Unions of subsets in which every point is generated by the other
points over $R_2$ are again redundant. An essential point cannot belong
to any such subset, so every deletion order leaves exactly their union.
This is a criterion for the **stronger parity-filtration property**, not
an equivalence with dissociation or with mandatory coordinates.

If every rank-dependent addition in a filtration has exact order two
modulo the preceding lattice, its rank-increasing columns form a rational
basis $B$ and
$$
[\mathbb ZC:\mathbb ZB]=2^{|C|-\operatorname{rank}_{\mathbb Q}C}. \tag{9}
$$
Every dependent addition multiplies the index by two; a rank-increasing
addition extends both lattices by the same independent cyclic factor.
For different color classes these indices need not combine into an index
of the full-grid lattice.

One exact full-grid fact explains why. For
$E=\bigotimes_{i=1}^kS_{p_i}$, deleting fewer than $2^k$ columns
still leaves the whole standard integer lattice generated; the threshold
is sharp. Over every field, the row code of a single simplex is the
length-$p_i$ zero-sum code, of minimum support two. The tensor row code
has minimum support $2^k$: in a nonzero tensor-code array a nonzero
column forces at least the first code's minimum number of nonzero rows,
each of at least the second code's minimum weight, and induction applies.
Pure tensors of weight-two words attain the bound.
Deleting fewer columns therefore preserves full rank over $\mathbb Q$
and over every prime field. Smith normal form implies integer generation.
Deleting the support of a minimum-weight rational row word shows sharpness.

Thus a column essential within one class can be regenerated using other
classes. No simultaneous-color contradiction was derived from (8), (9),
or the deletion robustness.

The small circuits, quotient-basis argument, integer kernel elimination,
mandatory property, saturation, and density limit are author-recorded; two
separate reviewers checked them. The theorem is algebraic; no exploratory
finite probe is an input. A separate reviewer also checked the pivot-depth
coloring; the core and row-code claims have the direct proofs above and
establish no new chromatic lower bound.
