---
name: research/erdos_963/global_lift_gap
title: 'A normal empty lift that cannot be further projected'
desc: Greedy empty-lift iteration is false, one-step binary lifts are proved, and a cube-cover LP optimum need not have sufficiently small support.
tags: []
sources: []
created: 2026-09-19T02:53:02Z
updated: 2026-09-19T04:11:13Z
---


# A normal empty lift that cannot be further projected

***

The one-step construction in [[research/erdos_963/empty_lift_quotient|the
quotient note]] cannot be iterated with arbitrary valid choices. This remains
false even if normality and a unimodular star triangulation are maintained. The
obstruction below is not a counterexample to the target or to the existence of a
globally chosen lift in dimension $c(P)$.

## An exact obstruction

Take $P=\{3,7,8,9,12\}$. Then $c(P)=3$.
The triple $\{3,7,8\}$ is dissociated and hence coherent by the
established triple lemma. Three of the four-subsets are excluded by
$3+12=7+8$ or $3+9=12$. On $(3,7,8,9)$,

$$
\mathbf1=\tfrac13((0,0,0,3)+(1,0,3,0)+(2,3,0,0)).
$$

On $(7,8,9,12)$,

$$
\mathbf1=\tfrac14((0,0,0,3)+(0,0,4,0)+(0,3,0,1)+(4,1,0,0)).
$$

These are nontrivial decompositions within the respective total-sum
fibers, excluding the remaining four-subsets.

Label the heights $0,3,7,8,9,12$ by $O,A,B,C,D,E$, respectively, and
form

$$
Q=\operatorname{conv}(0,-e_1-e_2+2e_3,e_1,e_2,e_3,e_4)
\subset\mathbb Z^4.
$$

The height functional is $(7,8,9,12)$, and the unique affine relation is

$$
O+2D=A+B+C.                                               \tag{1}
$$

The three simplices omitting $A,B,C$ are unimodular and contain $O$,
by the proved one-step theorem. Thus $Q$ is empty, normal, and
unimodularly star-triangulated.

**Claim.** No height-preserving lattice projection to dimension three
retains all six vertices and emptiness.

The external input is Howe's theorem that every empty three-dimensional lattice
polytope has width one. The original passage was checked in [Scarf, *Integral
Polyhedra in Three Space*, preprint, printed p. 7, Theorems
1.3–1.4](https://cowles.yale.edu/sites/default/files/2022-08/d0632.pdf).
Definition 1.1 on printed p. 3 uses “integral polyhedron” precisely for a
polytope whose only lattice points are its vertices.

Suppose the projection exists. Use an integral width-one functional
$f$ with values zero and one on the projected vertices, normalized by
$f(O)=0$. Relation (1) gives

$$
2f(D)=f(A)+f(B)+f(C).
$$

If $f(D)=0$, five vertices occupy one lattice plane. An empty lattice
polygon has at most four vertices, by parity, so this is impossible.
Hence $f(D)=1$ and exactly one of $A,B,C$, denoted $L$, has $f=0$.
Write its height as $a$, and the heights of the other two, $U,V$, as
$b,c$.

If $f(E)=1$, the four upper vertices form an empty lattice
quadrilateral, hence a unimodular parallelogram. Their heights would
have equal complementary pair sums. None of

$$
\{7,8,9,12\},\quad\{3,8,9,12\},\quad\{3,7,9,12\}
$$

does. Therefore $f(E)=0$.

Both layers now consist of empty triangles, hence unimodular
triangles in the plane lattice. Thus $x=U-D$ and $y=V-D$ form a
basis of $\ker f$ in that lattice. Relation (1) says $L=-x-y$.
Write $E=\alpha x+\beta y$, with integers $\alpha,\beta$.
Unimodularity of the lower triangle gives $\alpha-\beta=\pm1$.
Since $b+c-18=-a$, applying the height functional yields

$$
12\equiv\pm(c-9)\pmod a.
$$

For $(a,b,c)=(3,7,8),(7,3,8),(8,3,7)$ this requires, respectively,

$$
0\equiv\pm1\pmod3,\quad5\equiv\pm1\pmod7,\quad
4\equiv\pm2\pmod8,
$$

all impossible. The claim follows.

The planar facts used here are elementary: an empty triangle has
area $1/2$ and an empty quadrilateral area $1$, by Pick's theorem.
Triangulation of the latter into two unimodular triangles forces
it to be a unimodular parallelogram.

## A different first quotient succeeds

The six cube vertices

$$
0,\ (1,0,0),\ (1,1,0),\ (1,0,1),\ (0,1,1),\ (1,1,1)
$$

have the required heights under $(3,4,5)$. Their convex hull is empty:
every lattice point in the unit cube is a cube vertex, and a missing
cube vertex cannot lie in the convex hull of the others.
This lift has the compatible relations

$$
A+E=B+C,\qquad E=A+D,
$$

and the star tetrahedra $OABE,OACE,OBDE,OCDE$ are unimodular.

In particular, a lift which is minimal under further projections
need not have minimum possible dimension. A global proof must permit
replacing previously imposed relations, not merely adding relations.

## The one-step lift can always be binary

There is a useful strengthening of the proved one-step construction.
If a positive integer $n$-set is noncoherent, it is contained in the
subset-sum set of $n-1$ external integers, which need not be positive
or belong to the original set.

Use the relation $r$ chosen in the one-step theorem. Its negative
entries are $-1$ on a set $J$ of size $m$. Its positive entries $k_i$
satisfy $1\le k_i\le m-1$: their sum is at most $m$, and equality
with only one positive entry was excluded when selecting the affine
relation. Zero coordinates can be handled by unit rows.

For each positive coordinate $i$ and each $K\subset J$ of size $k_i$,
the Boolean row

$$
e_i+\mathbf1_K
$$

is orthogonal to $r$. These rows generate the full integer lattice
$r^\perp\cap\mathbb Z^n$. Their differences generate the zero-sum
lattice on $J$, and subtracting the appropriate chosen row for
each positive coordinate reduces any lattice vector to that
zero-sum lattice.

More precisely, fix one such row with negative support $K_0$.
Swapping one element of $K_0$ with one of $J\setminus K_0$ produces
row differences along the edges of the connected complete bipartite
graph on these parts. Choose a spanning tree. The original row,
the $m-1$ swapped rows, one row for each remaining positive coordinate,
and the zero-coordinate unit rows form a Boolean integer basis of
$r^\perp\cap\mathbb Z^n$.

The weight vector lies in this lattice and hence is an integer linear
combination of those $n-1$ Boolean rows. Reading the matrix by columns
gives the asserted binary lift and external subset-sum generators.
This does not iterate automatically: the external generators are
not a subset of the original configuration.

## A separate sufficient cubical statement

For a positive odd integer vector $p=(p_1,\ldots,p_n)$, let $h(p)$
be the least dimension of a subspace of $\mathbb R^n$ containing $p$
and spanned by vertices of $\{\pm1\}^n$. Equivalently, it is the least
number of external generators whose full signed sums cover all $p_i$.
The unproved assertion

$$
h(p)\le d(\{p_1,\ldots,p_n\})                               \tag{2}
$$

would imply the strong odd bound: $k$ generators have at most
$2^{k-1}$ distinct positive full signed sums.

Every even-support ternary relation has a hyperplane spanned by cube
vertices. After changing coordinate signs, its support equation is
the sum of an even number of coordinates equal to zero; the balanced
sign vectors span that hyperplane. Thus one constraint can always
be imposed. Intersections need not remain cube-spanned.

For an explicit example, the subspace

$$
U=\{(a,b,c,a+b+c,a+b-c,a-b+c,a-b-c):a,b,c\in\mathbb R\}
$$

is the intersection of four such even-support ternary hyperplanes.
It admits all-odd integer vectors. Nevertheless
$U\cap\{\pm1\}^7$ is empty: the first three coordinates would force
$a,b,c\in\{\pm1\}$, and one of the last four coordinates would then
equal $3$ or $-3$.

An equivalent formulation of (2) is this unproved subspace assertion.
Let $U\subseteq\mathbb R^n$ be rational, admit an all-odd integer
point, and have no coordinate identically zero or equal up to sign
to another. Let $d_U$ be the maximum size of a coordinate set
supporting no nonzero ternary vector in $U^\perp$. Then some
cube-spanned $W\supseteq U$ has dimension at most $d_U$.

For the equivalence, the odd lattice points of $U$ are Zariski dense.
There are only finitely many ternary hyperplanes and cube-spanned
subspaces. Choose an odd point avoiding all proper intersections
with these spaces, and change its coordinate signs to make it
positive. Its ternary relations are precisely those in $U^\perp$,
and every cube-spanned space containing it contains $U$.
The converse applies the subspace assertion to the intrinsic lift
defined by the actual ternary relations.

Neither this global cubical statement nor the globally minimum
empty-lift statement has been proved. They are sufficient stronger
routes, not established reformulations of the original target.

### An exact test for a one-dimensional cube-spanned extension

Let $U\subset\mathbb R^n$ have dimension $r<n$, and write
$\pi:\mathbb R^n\to\mathbb R^n/U$. Group the cube vertices whose
images under $\pi$ are nonzero according to the projective line
spanned by that image. To every group adjoin all cube vertices
already in $U$.

Then $U$ is contained in a cube-spanned space of dimension at most
$r+1$ if and only if one of these groups spans dimension $r+1$.

Indeed, every group lies in $\pi^{-1}(\ell)$ for one line $\ell$,
a space of dimension $r+1$. If its span has that dimension, its
intersection with $U$ has dimension $r$ and equals $U$.
Conversely, a cube-spanned $(r+1)$-space containing $U$ projects
onto one line, so its spanning cube vertices belong to that group.
If $U$ itself is cube-spanned, adjoin any cube vertex outside $U$
to obtain such an $(r+1)$-space.

This is a finite criterion, not a general existence theorem.
The conditions defining $d_U$ have not been shown to force a group
of the required rank. Bounded checks supplied no counterexample,
but are not used in any proof. In particular, this test does not
justify an induction through successive extensions.

The subsequent [[research/erdos_963/cube_two_relations|two-relation theorem]]
proves a cube-spanned codimension-two extension when two minimal even ternary
supports differ by more than one exchange. The remaining case reduces to an odd
uniform core with one full-support-deletion relation per coordinate. Three-row
replacements cannot resolve that core. The new
[[research/erdos_963/large_uniform_cores|large-core theorem]] proves that dense or
one-large-class four-row constructions always succeed for $q\ge761$.
The uniform-core gap remains at odd sizes $7\le q\le759$, and the
general global extension is still unproved.

## Noncoherence gives an integral full-sign cover in one fewer dimension

If a positive odd integer $n$-set $P$ is noncoherent, then it is
covered by full signed sums of $n-1$ external **integer** weights.
This extends the one-ternary-relation construction to a noncoherent
set that may itself be dissociated.

Take the relation $r$ supplied by the one-step quotient theorem.
Its negative entries are $-1$ on $J$, with $|J|=m$; its positive
entries are $k_i$ on $I$, with $K=\sum k_i\le m$ and $k_i<m$.
Write $Z$ for its zero coordinates. Oddness gives $K\equiv m\pmod2$.
We show that the rank-$(n-1)$ lattice

$$
H=\{x\in\mathbb Z^n:r\cdot x=0,\quad
x_1\equiv\cdots\equiv x_n\pmod2\}
$$

has a basis consisting of sign vectors.

Choose signs $\varepsilon_i$ on $I$ with
$|\sum k_i\varepsilon_i|<m$: use all plus signs if $K<m$,
and flip one if $K=m$. They extend to a sign solution $v$ of
$r\cdot v=0$ with both signs occurring on $J$. Fix an anchor
$i_0\in I$. Use $v$, its swaps along a spanning tree of the
complete bipartite graph between the two sign classes on $J$,
one sign solution, keeping the $Z$-signs fixed, with just the
$i$-th $I$-sign changed for each
$i\in I\setminus\{i_0\}$, and one zero-coordinate flip for
each $z\in Z$. The $I$-flip solutions exist because every
signed sum of the $k_i$ has magnitude at most $m$ and parity $m$.
There are $1+(m-1)+(|I|-1)+|Z|=n-1$ rows.

For integral generation, let $x\in H$. The anchor prescribes the
total row coefficient $S=\varepsilon_{i_0}x_{i_0}$. At each
nonanchor $I$-coordinate assign its flip-row coefficient
$(S-\varepsilon_i x_i)/2$, and similarly at zero coordinates.
Choose the coefficient of $v$ to make the total $S$. The residual
is even, supported on $J$, and has coordinate sum zero. Differences
between tree-swap rows and $v$ generate twice the zero-sum lattice
on $J$, so they eliminate that residual. Thus the rows generate
$H$ and form a basis. The odd weight vector belongs to $H$,
giving the asserted integer full-sign cover.

For example, the established noncoherent dissociated set
$\{7,15,17,27,33\}$ consists of the total $33$ of the four
weights $13,9,8,3$, and the four values obtained by changing
one sign. Hence its full-sign covering dimension is four, while
its dissociation dimension is five. This construction still does
not iterate: the external weights are not a subset of $P$.

## A large-quotient case of the global extension

Suppose $\dim U=r$ and $d_U=r+1$. In the maximum-volume basis coordinates of
[[research/erdos_963/corank_one|the corank-one argument]], the nonintegral
columns occupy one signed residue class $\{g,-g\}$ modulo $\mathbb Z^r$. If its
order $q$ is greater than $r+2$, then $U$ has a cube-spanned extension of
dimension $r+1$.

Orient the nonintegral columns to residue $g$ and append a
coordinate $t$ which is one on them and zero on integral columns.
The lifted rank is $r+1$, since $t$ vanishes on the chosen basis
but not on every column. Every old ternary relation supported on
at most $r+2$ columns has nonintegral coefficient sum $s$ with
$sg=0$ and $|s|\le r+2<q$. Thus $s=0$ and that relation
survives the lift. Every $(r+2)$-set was dependent and remains
so; the lifted dissociation dimension is exactly its rank $r+1$.
The original odd functional survives as well.

For completeness, a rank-$k$, dissociation-$k$ configuration with
an odd functional has a cube-spanned row space. In maximum-volume
basis coordinates its matrix $A$ is totally unimodular, as in
the full-rank argument. If the odd point is $p=A^{\mathsf T}y$,
the bounded full-dimensional polytope

$$
(-1-p)/2\le A^{\mathsf T}z\le(1-p)/2
$$

has integral vertices by total unimodularity. Their images
$p+2A^{\mathsf T}z$ are sign-cube vertices and affinely span
the row space. Apply this to the lifted configuration.

Small quotient orders remain unresolved. This is a sufficient
special case of the global cover, not a reduction of its general
case to the full-rank case.

## The natural linear-programming relaxation does not control support

Let $E$ be the matrix whose columns are all vertices of
$\{\pm1\}^n$. The full-sign covering parameter has the exact
formulation

$$
h(p)=\min\{|\operatorname{supp}a|:Ea=p,\ a\ge0\}.         \tag{3}
$$

A representation on a cube basis can have its coefficients made
nonnegative by reversing the corresponding cube vectors. Conversely,
every representation spans a cube-generated space. A support-minimal
representation uses independent columns: a nonzero dependence permits
moving its positive coefficients until one first reaches zero,
contradicting minimality.

The convex relaxation that minimizes $\sum a_i$ instead has value
exactly $\|p\|_\infty$. The lower bound follows from
$\|Ea\|_\infty\le\sum a_i$. Equality follows because
$p/\|p\|_\infty$ belongs to the convex hull of the sign cube.
Equivalently, its dual is

$$
\max\{y\cdot p:\|y\|_1\le1\}.
$$

Thus the objective value alone gives no dissociation-sensitive bound.

Even choosing an optimal extreme point need not produce at most
$d(p)$ atoms. For $p=(1,3,5,7)$ put

$$
\begin{split}
v_0&=(1,1,1,1),&v_1&=(-1,1,1,1),\\
v_2&=(-1,-1,1,1),&v_3&=(-1,-1,-1,1).
\end{split}
$$

Then $p=4v_0+v_1+v_2+v_3$, of coefficient sum $7$, so this
four-atom representation is optimal. Its columns are independent:
successive differences give $2e_1,2e_2,2e_3$, and the fourth
coordinate of every column is one. Independence of the supported
columns makes the coefficient vector an extreme point of
$\{a\ge0:Ea=p\}$.

Nevertheless $d(p)=3$, since $1+7=3+5$ and every three distinct
positive odd integers are dissociated. Also $h(p)=3$: generators
$1,2,4$ give all four positive values as full signed sums, while
two generators can give at most two distinct positive full signed
sums. This example does **not** refute $h(p)\le d(p)$ or the
existence of a suitable sparse LP optimum. It rules out using an
arbitrary optimal extreme point as the missing support certificate.

## Dense full-sign covers must be integral

Suppose $n$ distinct positive odd integers are covered by full
signed sums of $k$ real generators $a_1,\ldots,a_k$, with
$n>2^{k-2}$. Then every $a_j$ is an integer, and
$\sum_j a_j$ is odd.

At least $2n>2^{k-1}$ sign-cube vertices evaluate into the odd
set $P\cup(-P)$. For each coordinate $j$, the cube's
coordinate-$j$ edges partition its vertices into $2^{k-1}$
pairs. Some edge therefore has both endpoints in that evaluation
set. Its values differ by $2a_j$, an even integer. Hence
$a_j\in\mathbb Z$. All full signed sums now have the parity
of $\sum_j a_j$, which must be odd.

In particular, if an odd cardinality counterexample has covering
dimension $h(P)=d(P)+1$, its minimal cover is necessarily
integral. This does not reduce the number of generators, and no
global replacement argument was obtained from integrality.

## A tree cover of the odd ternary cube

For completeness, a structured potential obstruction has a small
external cover. All odd-support vectors of $\{-1,0,1\}^r$ are
full signed sums of $2r-2$ vector generators when $r$ is even,
or $2r-1$ when $r$ is odd.

Choose a tree on the $r$ coordinates. For each edge $ij$ use
$(e_i+e_j)/2$ and $(e_i-e_j)/2$. Their two signed contributions
can sum to either $\pm e_i$ or $\pm e_j$. Orient each edge
toward the coordinate which receives its contribution. An orientation
with prescribed indegree parities exists precisely when their total
parity is the number of edges: reversing edges changes the parity
vector by their incidence vectors, which span the even-weight
binary subspace for a tree.

When $r$ is even, $r-1$ is odd. Prescribe odd indegree exactly
at the desired nonzero coordinates. At each vertex independently,
the incoming signs can sum to its desired value $0,1$, or $-1$.
When $r$ is odd, add one generator $e_i$ at a fixed root and
toggle the prescribed root parity; the incoming contributions
together with that generator are handled in the same way.

This supplies a cover, not a lower bound on dissociation and not
a counterexample to $h\le d$. In particular the rank-four odd
ternary cube has a six-generator cover; it cannot supply a
purported example requiring seven generators.
