---
name: research/erdos_644/linear_relation_tests
desc: Every nontrivial linear seven-row relation excluding two-point covers is the Fano simplex code; these linear tests alone allow transversal-to-rank ratio one.
tags: [proved, boolean-functions, method-obstruction]
sources: []
created: 2026-09-23T05:00:08Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/linear_relation_tests

***

This page identifies the exact scope of linear seven-row tests. It does not
prove an upper bound for $P_7$, or for the weaker combination of $P_6$ and
Fano-freeness.

For a finite family $\mathcal H$ of nonempty sets, let

$$
f(x)=1\quad\Longleftrightarrow\quad
\operatorname{supp}(x)\text{ contains a member of }\mathcal H.
$$

Thus $f$ is monotone and $f(0)=0$. A relation $R\subseteq\mathbb F_2^7$ is a
valid seven-row test if no two of its words have supports whose union is $[7]$.
Property $P_7$ implies that applying $f$ to the seven rows of any matrix with
columns in $R$ cannot give $1^7$: otherwise choose an edge inside each positive
row. Their spectra are subsets of the original column supports and still admit
no two-point cover.

The exact formulation in [Boolean reductions](boolean_reductions.md) uses all
downward-closed relations with this property. The following theorem shows what
remains if one uses only linear relations, or their downward closures.

## Classification of linear relations

**Theorem.** Let $C\le\mathbb F_2^7$ be a linear subspace such that

$$
\operatorname{supp}(u)\cup\operatorname{supp}(v)\ne[7]
\qquad(u,v\in C).
\tag{1}
$$

Suppose that $C$ has full support: every coordinate is nonzero on some word of
$C$. Then, up to a permutation of coordinates, $C$ is the binary $[7,3,4]$
simplex code. Its seven nonzero supports are the seven Fano caps.

If $C$ does not have full support, its test imposes no restriction on a function
satisfying $f(0)=0$: a zero coordinate of $C$ produces an identically zero row
of every input matrix.

**Proof.** First every word of $C$ has weight at most four. A word $u$ of weight
seven violates (1) immediately. If its zero set $Z$ has size one or two, the
projection of $C$ onto $Z$ has full support and must avoid the all-ones word, by
(1). This is impossible: a full-support binary linear subspace on one or two
coordinates contains the all-ones word. This excludes weights six and five.

There is a word of weight four. Indeed, each coordinate equals one on half the
words of $C$, so the average weight over $C$ is $7/2$.

Fix a weight-four word $u$, with three-element zero set $Z$. The projection of
$C$ onto $Z$ has full support and avoids $111$. It must be the even-parity
plane. To check this, a full-support one-dimensional subspace contains $111$, as
does the full three-dimensional space. A two-dimensional subspace is the kernel
of a nonzero linear form. Avoiding $111$ requires that form to have odd weight;
weight one would give a zero coordinate, leaving only the weight-three parity
form. Consequently

$$
(1+u)\cdot v=0\quad(v\in C),
\qquad
u\cdot v\equiv |v|\pmod2.
\tag{2}
$$


Let $U$ consist of zero and all weight-four words of $C$. Two distinct
weight-four words have an even intersection by (2). Their supports, being
distinct four-subsets of a seven-set, intersect in exactly two points. Their sum
therefore also has weight four. Thus $U$ is a nonzero subspace.

If $v\in C$ has weight $r\in\{1,2,3\}$, write
$s=|\operatorname{supp}(u)\cap\operatorname{supp}(v)|$ for any nonzero $u\in U$.
Equation (2) gives $s\equiv r\pmod2$, while

$$
|u+v|=4+r-2s\le4.
$$

For each of $r=1,2,3$, these conditions force $s=r$. Hence

$$
\operatorname{supp}(v)\subseteq\operatorname{supp}(u)
\qquad(0\ne u\in U).
\tag{3}
$$

If $\dim U=1$, all words of $C$ are supported on its unique nonzero word,
contradicting full support. If $\dim U\ge2$, choose distinct nonzero $u,w\in U$.
The three supports of $u,w,u+w$ have empty common intersection. Equation (3)
then excludes every nonzero lower-weight word. Therefore $C=U$: all its nonzero
words have weight four.

Put $d=\dim C$. Counting incidences between coordinates and words gives

$$
4(2^d-1)=7\cdot2^{d-1},
$$

and hence $d=3$.

Choose an identification $C\cong\mathbb F_2^3$. Each of the seven coordinate
functions is a nonzero linear form. Let $m_a$ be the multiplicity of the form
$x\mapsto a\cdot x$, where $0\ne a\in\mathbb F_2^3$. Fix $a$ and sum the weights
of the four codewords indexed by $x$ with $a\cdot x=1$. The form $a$ contributes
$4m_a$, and every other nonzero form contributes twice its multiplicity. Since
these four words each have weight four,

$$
16=4m_a+2(7-m_a),
$$

so $m_a=1$. Thus the coordinates are exactly the seven nonzero linear forms.
Each nonzero word has support

$$
\{a\ne0:a\cdot x=1\},
$$

the complement of a Fano line. $\square$

## Fano tests and binary subspaces

For $f(0)=0$, passing the simplex-code test is equivalent to the winning set

$$
W=\{x\in\mathbb F_2^V:f(x)=1\}
$$

containing no set $L\setminus\{0\}$ for a three-dimensional linear subspace
$L\le\mathbb F_2^V$.

Indeed, the seven rows of a matrix whose columns lie in the simplex code are the
images of the seven nonzero vectors of $\mathbb F_2^3$ under one linear map. If
all seven rows win, none is zero, so this map is injective and its image is such
an $L$. Conversely, enumerate the nonzero vectors of any three-dimensional $L$
through a linear isomorphism from $\mathbb F_2^3$. Each coordinate column is
either zero or a simplex-code word, producing a failed test.

Call this condition **Fano-free**. It is necessary for $P_7$, not equivalent to
$P_7$. For monotone $f$, replacing the simplex relation by its downward closure
gives the same test: a failed matrix with smaller columns can be enlarged to
simplex-code columns, and its rows remain positive.

## Linear tests alone permit ratio one

For every integer $m\ge3$, put $k=2m$ and take disjoint blocks $X,Y$, each of
size $3m-1$. Define

$$
\mathcal H=\binom X{2m}\ \cup\ \binom Y{2m}.
\tag{4}
$$

Each complete component has transversal number

$$
(3m-1)-2m+1=m.
$$

Since the blocks are disjoint,

$$
\operatorname{rank}(\mathcal H)=k,
\qquad \tau(\mathcal H)=2m=k.
\tag{5}
$$


Nevertheless, its monotone winning set is Fano-free. Any three edges in one
component have common intersection of size at least

$$
3(2m)-2(3m-1)=2.
$$

The winning set of either component therefore contains no linear triangle
$x,y,x+y$: those three supports have empty common intersection, so they cannot
contain three edges of that component.

If all seven nonzero vectors of a three-dimensional subspace won (4), color each
vector by a component in which it wins. Every two-coloring of the Fano plane has
a monochromatic line. For completeness, a line-free set has at most four points;
if it has four, its complement is a line. To see this, three points of a
line-free set form a basis of $\mathbb F_2^3$, and the only possible fourth
point is their sum. Its complementary three points form a line. The
monochromatic line in the supposed coloring would give a linear triangle in one
component's winning set, a contradiction.

The family (4) fails even $P_5$. Partition $3m-3$ points of $X$ into three
disjoint $(m-1)$-sets $D_1,D_2,D_3$, leaving two points. Choose an $(m-1)$-set
$D_4$ containing those two points; this is possible for $m\ge3$. The four edges
$X\setminus D_i$ have empty common intersection, and hence require at least two
covering points in $X$. Adjoining any edge from the $Y$ component requires a
third point.

## Exact scope

The classification and construction show that linear seven-row relation tests
alone cannot imply a $3k/4+o(k)$ transversal bound: they all hold for (4), whose
ratio is one. The same holds if all such linear relations are replaced by their
downward closures.

This is not a $P_7$ counterexample. It does not refute a bound using
Fano-freeness together with $P_6$, since (4) fails $P_5$. The full
promise-relation formulation includes nonlinear relations and retains
constraints absent from the linear tests.
