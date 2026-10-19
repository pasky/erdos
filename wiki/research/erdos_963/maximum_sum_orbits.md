---
name: research/erdos_963/maximum_sum_orbits
title: 'An antichain and charging argument for maximum-sum orbit matching'
desc: Orbit Hall holds with at most three omission coordinates; an odd seventeen-set shows that single-exchange sum optimality cannot replace maximum cardinality.
tags: []
sources: []
created: 2026-09-19T01:40:00Z
updated: 2026-09-19T04:11:13Z
---


# An antichain and charging argument for maximum-sum orbit matching

***

Let $O$ be a positive odd integer set, and choose $D=\{d_1,\ldots,d_d\}$ of
maximum dissociated cardinality and, among these choices, maximum sum. This note
proves a limited case of the complement-orbit Hall condition in
[[research/erdos_963/proof_sketch|the proof sketch]], not its general form.

## Maximum-sum optimality

If $a\in O\setminus D$ and $a>d_i$, then $a$ has a ternary
representation on $D$ omitting coordinate $i$. Otherwise
$(D\setminus\{d_i\})\cup\{a\}$ would be dissociated and have larger
sum. A dependence on that replacement must use $a$, hence gives the
claimed representation.

Call a color exclusively full-support if all its ternary representations
on $D$ have full support. Such a representation is unique: subtracting
two full sign vectors and dividing by two would contradict dissociation.
The color is not a basis element, and the preceding observation gives

$$
a<\min D.                                                   \tag{1}
$$

The two complementary sign vertices defining its orbit therefore satisfy

$$
\left|\sum_i\sigma_i d_i\right|<\min D.
$$

Vertices in this strip form an antipodal antichain under the coordinate
order $-1<1$. Indeed, two distinct comparable vertices have signed sums
differing by at least $2\min D$, exceeding the width of the strip.

## Hall with at most three omission coordinates

**Proposition.** Suppose $d\ge5$ is odd. Let $C\subset O$, and suppose
the union of zero coordinates over **all** ternary representations
of colors in $C$ has size at most three. Then

$$
|N(C)|\ge |C|,                                               \tag{2}
$$

where $N(C)$ is the union of their complement-orbit neighborhoods.

Pad that coordinate set to a set $I$ of size three. Identify the
complement orbits of subset-sum vertices with the folded sign cube,
where $\sigma$ and $-\sigma$ are identified. Fixing outside signs up
to global reversal partitions this space into eight-vertex coordinate
$I$-cubes $Q$.

Oddness forces a represented odd value to have odd support. Since $d$
is odd, its zero-set has even cardinality. Thus a nonfull representation
has exactly two zero coordinates, both in $I$, and gives a square face
of a cube $Q$ in its orbit neighborhood.

Put $K_Q=N(C)\cap Q$. Let $s_Q$ count exclusively full-support colors
whose orbit lies in $Q$, and let $t_Q$ count distinct colors having a
square representation in $Q$. The strip antichain gives $s_Q\le3$:
an antichain in a three-cube has size at most three. In any square it
has size at most two. These elementary bounds follow, for example, by
partitioning the three-cube into three chains and the square into two.
A square determines at most one positive color, so distinct counted
colors can be assigned distinct square faces.

Consequently

$$
s_Q+t_Q\le |K_Q|                                           \tag{3}
$$

except possibly when $s_Q=3,t_Q=6,K_Q=Q$, when its left side exceeds
the right side by one. Here are all cases. If $t_Q=0$, the assertion
is immediate. If $1\le t_Q\le2$, a contained square has at most two
exclusively full-support vertices, so $s_Q\le |K_Q|-2$. Three
distinct faces cover at least seven vertices, while four or five cover
all eight. Six faces leave only the stated possible unit excess.

Call a cube with that excess bad. Choose its outside signs so that
its center

$$
b_Q=\sum_{j\notin I}\sigma_j d_j
$$

is positive. It is nonzero by dissociation. Distinct cubes have
distinct positive centers: equality, after subtracting their sign
vectors and dividing by two, would be a ternary relation on $D$.

Choose $i\in I$ with largest $d_i$. In a bad cube the six square
colors are distinct, and one of them is

$$
a_Q=b_Q+d_i>d_i.
$$

The only square there representing $a_Q$ fixes coordinate $i$.
Maximum-sum optimality supplies another representation omitting $i$.
Its zero-set has size two, so its square fixes a different coordinate
$j\in I$. It lies in a cube $Q'$ with center satisfying

$$
b_{Q'}\ge a_Q-d_j>b_Q,
$$

because $d_i>d_j$. In particular $Q'\ne Q$. Thus $a_Q$ is counted
in at least two of the numbers $t_Q$.

Different bad cubes give different colors $a_Q$, since $i$ was fixed
globally and their centers are distinct. Every exclusively full-support
color is counted once in $\sum s_Q$, and every other color at least
once in $\sum t_Q$. The distinct duplicate colors just obtained show
that

$$
\sum_Q(s_Q+t_Q)\ge |C|+\#\{\text{bad cubes}\}.
$$

Summing (3), with its allowed unit excess in each bad cube, proves (2).

## Single-exchange sum optimality is not sufficient

The local optimality condition at the start of this note cannot
replace maximum **cardinality**. There is an explicit positive odd
example with a dissociated five-set $D$, all other elements below
$\min D$, and seventeen ambient elements.

Put $M=1001$, $B=\{0,1,3,7,15\}$, and

$$
\begin{split}
T=\{&-18,-14,-12,-11,-10,-8,-7,-6,-5,-4,-3,-2,\\
&0,1,3,7,15\},
\qquad O=M+2T,\quad D=M+2B.
\end{split}
$$

The set $D$ is dissociated. In a ternary relation on it, the
$M$-coefficient must vanish since the total perturbation has
absolute value at most $2\sum B=52<M$. Writing the members of
$B$ as $2^i-1$, $0\le i\le4$, the remaining relation reduces
to a ternary relation among $1,2,4,8,16$, which is impossible.

Every element of $O\setminus D$ is ternarily represented on $D$.
The ten offsets other than $-18,-10$ are the distinct values

$$
b_i+b_j-b_k,\qquad 0\le i<j<k\le4,
\quad (b_0,\ldots,b_4)=(0,1,3,7,15).
$$

The other two representations come from

$$
-18=0+1+3-7-15,\qquad -10=0+1+7-3-15.
$$

Each representation has coefficient sum one, so it transfers
directly to $M+2T$. Consequently $D$ is inclusion-maximal.
Every outside element is below every member of $D$, so no
single cardinality-preserving exchange can increase its sum.
Indeed, $D$ is the unique largest-sum five-subset of $O$.
Nevertheless $|O|=17>2^{|D|-1}$.

This is not a counterexample to the odd bound: $d(O)\ge6$. The established
[[research/erdos_963/affine_coherence|binary-tree extraction]] gives an
affine-coherent, hence affinely dissociated, six-subset of the seventeen
integers. All entries are odd and in $[965,1031]$. An unbalanced relation of
even support at most six would have at least four terms against at most two, or
at least three against one, impossible in that interval. Thus the extracted set
is ordinarily dissociated. The example rules out a proof relying only on ternary
spanning and single-exchange sum optimality.

## Remaining gap

For four or more omission coordinates, local families of even-dimensional
faces can have larger excess. No general replacement for the distinct
upward duplicate-color charges has been proved. A multi-element exchange
can create coefficients of absolute value two on $D$, which dissociation
does not exclude.

In particular, for $C=O$ the canonical representations of basis colors omit
$d-1$ coordinates, and their union includes every coordinate. The proposition
therefore does not prove the cardinality bound on $O$. Nor does the
[[research/erdos_963/orbit_matching_obstruction|arbitrary-maximum obstruction]]
settle the maximum-sum version.

## A four-omission result when at most three colors are small

There is a further proved case. Let $d\ge5$ be odd, let $I$ be
a four-coordinate set containing every zero in every representation
of every color in $C$, and put $m=\max_{i\in I}d_i$. If at
most three colors of $C$ are at most $m$, then $|N(C)|\ge|C|$.

Here is the counting argument. Put $H=\{a\in C:a>m\}$ and
use only its nonfull representations, with neighborhood $N_0(H)$.
Maximum-sum exchange supplies such a representation omitting each
prescribed coordinate of $I$. Partition the folded cube into
four-cubes $Q$ with positive outside center $b$. Local nonfull
representations have form $a=\pm b+\varepsilon_i d_i+
\varepsilon_jd_j$ (a square face), or $a=b$ (the whole cube).
Write $K_Q=N_0(H)\cap Q$, $k_Q=|K_Q|$, $t_Q$ for the number
of colors occurring nonfully in $Q$, and $h_Q$ for those whose
nonfull representations occur only there. Then

$$
2|H|\le\sum_Q(t_Q+h_Q).
\tag{3}
$$


A trapped noncentral color must have local pair supports with
empty intersection. Otherwise exchange supplies a representation
omitting their common coordinate in a different cube. An
empty-intersection pair family contains disjoint pairs or a triangle.
Disjoint pairs must have opposite outside signs, and give
$2a=\sum_{i\in I}\varepsilon_i d_i$. If the four weights are
$p<q<r<s=m$ and have total $T_I$, the condition $a>m$ leaves
only $a=T_I/2$ or $a=T_I/2-p$.

For a triangle of pair supports, a negative-center representation
must be $a=-b+x+y$, and there is at most one such pair by
dissociation. The other two are

$$
a=b+\sigma z+\tau x=b-\sigma z+\upsilon y.
$$

The opposite signs at $z$ follow from dissociation. Both
$\tau,\upsilon$ equal one: for instance $\tau=-1$ would give
$2a=y+\sigma z\le y+z<2a$. Adding the two equations gives
$a=3b$. Thus at most three noncentral colors are trapped in a
cube. Each needs at least seven vertices (disjoint pair supports
give faces meeting in one vertex; triangle supports include
disjoint faces).

If the center color occurs, $b>m$, so no high color can have a
negative-center representation. Noncentral local pair supports
then have a common coordinate: disjoint supports would give a
ternary relation, while a triangle would force opposite signs
at every common coordinate and its three represented values to
sum to zero. Hence $h_Q\le1$ and $k_Q=16$ in this case.

For a vertex set $K$ in the four-cube with $k\ge5$ vertices,
the number $f(K)$ of contained square faces satisfies
$f(K)\le2k-8$. Coordinate down-compression does not decrease
that count. For a proper downset with $r,p,q$ vertices of
weights one, two, three, respectively,

$$
k=1+r+p+q,\qquad f=p+3q.
$$

If $q=0$, then $r\ge3$ and $f\le k-4$; if $q=1$, then
$k\ge8,r\ge3$ and $f\le k-2$; if $q\ge2$, then
$r=4,k\ge12,q\le4$ and $f=k-5+2q\le k+3\le2k-8$.
For the full cube $f=24$, and for $k=4$ there is at most one
square.

A square determines at most one positive color. Without a center
color, these bounds give $t_Q+h_Q\le2k_Q-5$; for $k_Q=4$
use $t_Q\le1,h_Q=0$. With a center color,
$t_Q+h_Q\le24+1+1\le32-5$. If $H$ is nonempty, (3) now
gives $|N_0(H)|\ge|H|+3$, accommodating the at most three
remaining low colors. If $H$ is empty, at most three colors are
present; singleton neighborhoods are distinct and every other
neighborhood has at least four vertices, so the conclusion still
holds.

This proof does not handle four or more low colors. It uses only
single-exchange sum optimality; the central low-color obstruction
and the unrestricted maximum-cardinality augmentation gap remain.
