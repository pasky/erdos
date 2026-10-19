---
name: research/erdos_644/indispensable_local_cores
desc: Near-three-quarter families for which retaining every local two-point cover requires exponentially many vertices.
tags: [proved, reductions, method-obstruction]
sources: []
created: 2026-09-22T22:54:42Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/indispensable_local_cores

***

This construction rules out a linear-size vertex restriction retaining the full
local property, even for families asymptotically attaining the three-quarter
lower bound. It is not an asymptotic counterexample to Problem 644, and does not
rule out a reduction restricted to a fixed positive excess above that
coefficient.

For every $m\ge1$ there is a $K$-uniform family with

$$
K=16m+1,\qquad P_7,\qquad \tau=12m=\tfrac34(K-1),
$$

such that every vertex subset retaining $P_7$ on all edge traces contains at
least $\binom{2m}{m}$ vertices. Here retaining $P_7$ means that every
at-most-seven original edges have a two-point transversal within the chosen
subset.

## Equality in the Fano threshold

We first use the following elementary fact. Seven $a$-subsets of a $7a/4$-point
ground set with no two-point transversal are the seven Fano caps with each point
replaced by $a/4$ points.

Every point has degree at most four: a point of degree at least five could be
combined with a point common to the remaining two edges, since $7a/4<2a$.
Counting forces every degree to be four. Let $M$ be the largest
pair-intersection size. The sum of the six pair intersections with any fixed row
is $3a$, so $M\ge a/2$.

For a maximizing pair $E_1,E_2$, a point outside their union has a missing
triple $\{1,2,r\}$. Thus $E_r$ avoids $E_1\cap E_2$, since otherwise two points
cover the rows. If two outside points have different missing thirds $r,s$, both
$E_r,E_s$ avoid $E_1\cap E_2$, giving

$$
|E_r\cap E_s|\ge2a-(7a/4-M)=M+a/4>M,
$$

a contradiction. All outside points therefore miss the same row $E_r$, and

$$
E_r\subseteq E_1\triangle E_2,
\qquad a\le2a-2M.
$$

Consequently $M=a/2$. The pair-intersection sums now force every pair
intersection to equal $a/2$.

Apply the same outside-point argument to any pair of row indices. It has a
unique missing third, and its outside class has size $a/4$. These missing
triples form the Steiner triple system on seven indices, namely the Fano plane.
Every point's spectrum is its complementary cap. In particular, each pair of
rows intersects in $a/2$ points, and the symmetric difference of the three rows
on any Fano line is empty.

## Construction

Put $a=16m$. Partition a $28m$-point set $\Omega$ into

$$
P_{12},P_{13},P_{23},R,X,Y
$$

of sizes $8m,7m,7m,2m,2m,2m$, respectively. Identify both $X$ and $Y$ with
$[2m]$. For each $S\in\binom{[2m]}m$, set

$$
\begin{aligned}
A_S&=P_{12}\cup P_{13}\cup X_S,\\
B_S&=P_{12}\cup P_{23}\cup Y_S,\\
C_S&=P_{13}\cup P_{23}\cup X_S\cup Y_S.
\end{aligned}
$$

These are $a$-sets and

$$
A_S\triangle B_T\triangle C_U=\varnothing
\quad\Longleftrightarrow\quad S=T=U.
\tag{1}
$$

Indeed, the restrictions to $X$ and $Y$ give $S=U$ and $T=U$.

Choose $D\subseteq\Omega$ with

$$
|D\cap P_{ij}|=4m,\qquad D\cap R=R,
\qquad D\cap(X\cup Y)=\varnothing.
$$

Thus $|D|=14m$, and all the displayed exceptional $a$-sets have even $D$-parity.

Include the following $(a+1)$-sets in $\mathcal H$:

- $E\cup\{p_E\}$ for every $a$-set $E\subseteq\Omega$ with odd $D$-parity, using
  a distinct private point $p_E$;
- $A_S\cup\{v_S\}$, $B_S\cup\{v_S\}$, and $C_S\cup\{v_S\}$ for every $S$, with
  all $v_S$ distinct and outside $\Omega$.

## The local property

Take seven edges and inspect their core traces. If two core points cover the
traces, they cover the edges. Otherwise the equality fact above applies.

Two exceptional traces of the same type cannot occur, because their intersection
is at least $14m$, greater than the required $a/2=8m$. Thus at most three traces
are exceptional.

On each Fano line the three traces have empty symmetric difference, so the
number of odd-parity traces on the line is zero or two. If $w$ is the total
number of odd rows, counting over the seven lines gives $3w\le14$, hence
$w\le4$. At most three rows are exceptional and even, so $w\ge4$. There are
exactly four odd rows and three exceptional rows. The three even rows form a
Fano line: otherwise every line would have exactly two odd rows, contradicting
$3w=12<14$.

The three exceptional rows have different types. Equation (1) shows that they
have one common label $S$, so $v_S$ covers them. A core point in the Fano class
complementary to their line covers the other four rows. This proves $P_7$.

The family has more than seven distinct edges, so the same property for smaller
subfamilies follows by extending them to seven edges.

## Indispensability of the added vertices

Fix $S$. The pair atoms

$$
U_{12}=A_S\cap B_S,\qquad
U_{13}=A_S\cap C_S,\qquad
U_{23}=B_S\cap C_S
$$

are disjoint, each of size $8m$ with $4m$ points of $D$. Their complement $W$ in
$\Omega$ has size $4m$ with $2m$ points of $D$.

Split each atom into two $4m$-point halves, both of odd $D$-parity. One can put
respectively $1$ and $4m-1$ of its $D$-points in the two halves. Form four new
core rows by adjoining to $W$ one half of each atom, with half-index triples

$$
000,\quad011,\quad101,\quad110.
$$

Each row has size $16m$ and odd $D$-parity, and thus occurs among the privately
padded base edges.

Together with $A_S,B_S,C_S$, these are the seven Fano caps on seven classes of
size $4m$. Hence no two core points cover them. Each core point meets four
witness edges. Apart from $v_S$, every outside point meets at most one witness
edge. Therefore no two points avoiding $v_S$ cover these seven edges. Every
$P_7$-preserving vertex restriction must retain $v_S$.

This holds for all $\binom{2m}{m}$ choices of $S$.

## The transversal number

Suppose a transversal uses $r$ core points and $q$ outside points, with
$r+q\le12m-1$. The remaining core set $Z$ has size

$$
|Z|\ge16m+q+1.
$$

Both $D$ and its complement have size $14m<16m$. The feasible $D$-counts of
$a$-subsets of $Z$ form an integer interval of length at least one, so $Z$
contains an odd-parity $a$-set $E$. It meets both parity classes. For every
$z\in Z\setminus E$, replace an element of $E$ of the same parity by $z$.
Together with $E$, this gives at least

$$
|Z|-a+1\ge q+2
$$

distinct odd $a$-sets avoiding the chosen core points. Their padded edges can be
covered outside the core only by their distinct private points. The $q$ selected
outside points cannot cover them all. Thus $\tau(\mathcal H)\ge12m$.

For the reverse inequality, choose an even-parity $a$-set $F$ containing a point
of $R$; for example choose $8m$ points from each parity class, including that
point. It is neither an odd base trace nor an exceptional trace, since the
latter avoid $R$. All core traces have size $a$, so $\Omega\setminus F$ meets
every edge. Its size is $12m$.

## Remaining scope

Unlike the padding examples in
[Structural reductions](structural_reductions.md), the new points here cannot
all be discarded while retaining the full local property. An argument allowed to
delete a subfamily of small transversal number is not excluded: the exceptional
edges in this construction themselves have a two-point transversal, obtained by
taking one point in $P_{12}$ and one in $P_{13}$. The construction also leaves
open any core theorem assuming a fixed linear excess $\tau>(3/4+\varepsilon)K$.
