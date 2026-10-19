[cut]

A list assignment gives every vertex a set of exactly
four colours; a graph is 4-choosable when every list assignment admits a
proper colouring that takes each vertex's colour from its list. Lists are
sets, and two vertices may carry the same list. Binomial coefficients
$\binom nk$ vanish unless $0\le k\le n$.

The palette-minimization and layer-counting method is that of
[[../library/graph_coloring/hanson_1996_choosability_bipartite_graphs/_index|Hanson, MacGillivray and Toft]],
Lemmas 1--3 and Theorem 1, pp. 184--187. Its required specializations are
derived below. The weighted count uses no unproved source premise.

## Reduction to complete bipartite graphs of order 26

Let $G$ be a bipartite graph with at most 26 vertices and $L$ a list
assignment on $G$ with no proper colouring. Add isolated vertices with
arbitrary four-element lists until there are 26 vertices, choose a
bipartition $(X,Y)$ of the enlarged graph, and add every edge between $X$
and $Y$. A proper colouring of the resulting complete bipartite graph
$K_{a,b}$, $a=|X|$, $b=|Y|$, $a+b=26$, restricts to a proper colouring of
$G$ from $L$, so the enlarged assignment has none either. It therefore
suffices to show that $K_{a,b}$ is 4-choosable whenever $a+b=26$, and the
statement for at most 26 vertices follows. Assume the contrary for a fixed
pair $(a,b)$. Empty sides give an edgeless graph, which is colourable, so
$a,b\ge1$. Swapping the sides preserves badness; choose their names so
that $a\le b$, hence $a\le13$.

**Subset criterion.** Write $A_1,\dots,A_a$ for the lists on $X$ (the left
lists), $B_1,\dots,B_b$ for the lists on $Y$ (the right lists), and $P$ for
the union of all lists. A proper colouring from the lists exists if and only
if some $T\subseteq P$ meets every $A_i$ and contains no $B_j$. Given a
colouring, let $T$ be the set of colours used on $X$: every $A_i$ meets $T$,
and since every vertex of $Y$ is adjacent to every vertex of $X$, each
vertex of $Y$ has a colour of its list outside $T$, so no $B_j$ lies inside
$T$. Conversely, given such a $T$, colour each left vertex from $A_i\cap T$
and each right vertex from $B_j\setminus T$; vertices on the same side are
not adjacent, and the two colour sets are disjoint. Call an assignment
**bad** when it has no proper colouring, that is, when for every
$T\subseteq P$ some left list is disjoint from $T$ or some right list lies
inside $T$. For a fixed $T$, call these two kinds of list the **events**
at $T$.

**Every pair of colours lies in a list.** Among bad assignments on this
$K_{a,b}$ choose one with $N=|P|$ least. Suppose colours $x\ne y$ lie in no
common list, and replace $y$ by $x$ in every list. Lists keep four
elements. If the new assignment had a proper colouring $c'$, define $c(v)=y$
when $c'(v)=x$ and the original list of $v$ contains $y$ (it then does not
contain $x$), and $c(v)=c'(v)$ otherwise. Then $c(v)$ lies in the original
list of $v$, and $c(u)=c(v)$ implies $c'(u)=c'(v)$, so $c$ is proper. The
new assignment is therefore bad with $N-1$ colours, which contradicts
minimality. Hence every pair of colours of $P$ lies in some list.

**The palette has exactly 17 colours.** Each list covers six pairs, so
$\binom N2\le 6\cdot26=156$ and $N\le18$. A colour lies in at least
$\lceil(N-1)/3\rceil$ lists, since each list containing it covers at most
three of its $N-1$ partners; summing over colours,
$104=4\cdot26\ge N\lceil(N-1)/3\rceil$, which fails at $N=18$
($18\cdot6=108$). If $N\le6$, split $P$ into two sets of at most three
colours and let $T$ be one of them: every four-element list meets both
parts, so no left list is disjoint from $T$ and no right list lies inside
$T$, and $T$ gives a colouring. For $N\ge7$ and $0\le l\le N$, a left list
is disjoint from $\binom{N-4}{l}$ of the $l$-subsets of $P$ and a right list
lies inside $\binom{N-4}{l-4}$ of them, and every $l$-subset carries an
event, so

$$
a\binom{N-4}{l}+b\binom{N-4}{l-4}\ \ge\ \binom Nl .
$$

Adding this inequality at $l$ and at $N-l$, and using
$\binom{N-4}{N-l}=\binom{N-4}{l-4}$, gives

$$
26\left[\binom{N-4}{l}+\binom{N-4}{l-4}\right]\ \ge\ 2\binom Nl .
$$

At $l=\lfloor N/2\rfloor$ the quotient
$2\binom Nl\big/\big[\binom{N-4}{l}+\binom{N-4}{l-4}\big]$ equals
$70,70,42,42,33,33,143/5,143/5$ for $N=7,\dots,14$, each larger than 26,
so $N\ge15$.

For $N=16$ and $l=8$, $\binom{12}8=\binom{12}4=495$ and
$26\cdot495=12870=\binom{16}8$, so every 8-subset of $P$ carries exactly one
event. One side has two lists. Two left lists have a union of at most eight
colours, so at least eight colours avoid both and some 8-subset is disjoint
from both; two right lists lie inside a common 8-subset. Either way an
8-subset carries two events, a contradiction. For $N=15$ the inequality at
$l=7$ and $l=8$ reads $330a+165b\ge6435$ and $165a+330b\ge6435$, that is
$2a+b\ge39$ and $a+2b\ge39$; with $a+b=26$ this forces $a=b=13$ and
equality at $l=7$, so every 7-subset carries exactly one event. Two left
lists avoid at least seven common colours, hence a common 7-subset, a
contradiction. Therefore $N=17$.

**The 26 lists are distinct.** The distinct four-element sets among the
lists still cover every pair of the 17 colours, so each colour lies in at
least six of them, and their number $q$ satisfies $4q\ge17\cdot6=102$, that
is $q\ge26$. All 26 lists, left and right together, are therefore pairwise
distinct sets.

**Two disjoint left lists.** Take $T=A_1$. A right list inside $A_1$ would
equal $A_1$, which distinctness excludes, so some other left list is
disjoint from $A_1$; in particular $a\ge2$. Taking $T=P\setminus B_1$, a
left list disjoint from $T$ would equal $B_1$, so some right list lies
inside $T$; hence $b\ge2$. With the chosen side names this leaves
$2\le a\le13$. Relabel the colours
so that $P=\{0,\dots,16\}$, the two disjoint left lists are
$A_1=\{0,1,2,3\}$ and $A_2=\{4,5,6,7\}$, and $W=\{8,\dots,16\}$.

## The weighted count

Let $\mathcal S$ be the family of subsets $T\subseteq P$ meeting both $A_1$
and $A_2$; $A_1$ and $A_2$ have no event at such a $T$. Badness therefore
gives every $T\in\mathcal S$ an event among the other $24$ lists. For any
nonnegative weights $w(T)$ on $\mathcal S$ put

$$
Z=\sum_{T\in\mathcal S}w(T),\qquad
\ell(X)=\sum_{T\in\mathcal S,\ T\cap X=\varnothing}w(T),\qquad
r(X)=\sum_{T\in\mathcal S,\ T\supseteq X}w(T),
$$

for a four-subset $X$ of $P$. Since every $T\in\mathcal S$ carries an event
among the other lists,

$$
Z\ \le\ \sum_{T\in\mathcal S}w(T)\,\#\{\text{events at }T\}
\ =\ \sum_{i\ge3}\ell(A_i)+\sum_{j}r(B_j)
\ \le\ (a-2)\,\max_X\ell(X)+b\,\max_X r(X),
$$

where the indices are numbered so that $A_1,A_2$ are the fixed lists, and
both maxima run over all four-subsets $X\ne A_1,A_2$ of $P$; this uses only
that the other lists are four-subsets distinct from $A_1$ and $A_2$.

Here is one weighting that works for all these splits. Give each subset
$T$ weight $w_p$ according to its profile
$p=(|T\cap A_1|,|T\cap A_2|,|T\cap W|)$. The table includes the profile
with its first two entries interchanged, with the same weight; equal first
two entries describe only one profile. All unlisted profiles have weight
zero.

| Profile $p$, up to interchanging its first two entries | $w_p$ | Number of subsets, including the interchange |
| --- | --- | --- |
| $(1,1,6)$ | 7 | 1344 |
| $(1,2,5)$ | 3 | 6048 |
| $(1,2,6)$ | 1 | 4032 |
| $(1,3,4)$ | 8 | 4032 |
| $(2,3,3)$ | 4 | 4032 |
| $(3,3,2)$ | 6 | 576 |

Thus $Z=7(1344)+3(6048)+4032+8(4032)+4(4032)+6(576)=83424$.
For a four-subset $X$, put
$(x_1,x_2,x_3)=(|X\cap A_1|,|X\cap A_2|,|X\cap W|)$. Direct counting
gives

$$
\ell(X)=\sum_p w_p\binom{4-x_1}{t_1}\binom{4-x_2}{t_2}\binom{9-x_3}{t_3},
\qquad
r(X)=\sum_p w_p\binom{4-x_1}{t_1-x_1}\binom{4-x_2}{t_2-x_2}\binom{9-x_3}{t_3-x_3},
$$

where $p=(t_1,t_2,t_3)$ runs over the ten individual profiles specified by
the table. In the first formula, a subset disjoint from $X$ chooses its
elements from the complements of $X$ in the three parts; in the second,
it already contains the $x_i$ elements of $X$ in each part. The possible
types of $X\ne A_1,A_2$, up to interchanging the first two entries, are
exactly these eight:

| Type $(x_1,x_2,x_3)$ | $\ell(X)$ | $r(X)$ |
| --- | --- | --- |
| $(0,0,4)$ | 4304 | 2576 |
| $(1,0,3)$ | 4374 | 2618 |
| $(1,1,2)$ | 4347 | 2651 |
| $(2,0,2)$ | 4312 | 2400 |
| $(2,1,1)$ | 4284 | 2458 |
| $(2,2,0)$ | 4200 | 2208 |
| $(3,0,1)$ | 4200 | 2656 |
| $(3,1,0)$ | 4158 | 2664 |

Consequently $\max\ell=4374$ and $\max r=2664$. Since $a\le13$,

$$
(a-2)\max\ell+(26-a)\max r
=1710a+60516
\le82746
<83424=Z.
$$

This contradicts the weighted covering inequality. Thus no bad assignment
exists and every bipartite graph with at most 26 vertices is 4-choosable.

The [evidence entry point](evidence/main.py) recomputes the displayed
tables with integer binomial coefficients and, separately, computes all
event weights over all $2^{17}$ palette subsets and all 2378 admissible
four-subsets by subset- and superset-sum transforms. The latter uses no
profile-counting formula. The weights themselves are retained in
[`evidence/assets/compact_certificate.json`](evidence/assets/compact_certificate.json).
The table is small enough to check directly from the displayed formulas;
neither an exhaustive list-system search nor a solver verdict is a premise.
Controls apply the same transforms to two actual bad assignments with
smaller lists and confirm that their actual event weight is at least $Z$.

## How the weights arise

Minimizing $(a-2)\max\ell+b\max r$ over weightings of total weight 1 is a
linear program in the 160 profile weights. The
[discovery program](evidence/produce.py) produces separate weightings for
all ordered splits $2\le a\le24$, retained as auxiliary certificates in
`evidence/assets/certificates.json`. Scaling the weighting for $(13,13)$
so that its largest weight is 8 and rounding gives the compact table
above. The proof uses only this table and the two elementary counting
formulas, not optimization or floating-point correctness.

The uniform weighting of all 8-subsets of $P$ gives no
contradiction: for the split $(13,13)$ the 26 lists carry
$13\cdot1287+13\cdot715=26026$ events on the $24310$ such subsets. The
weighting has to concentrate on subsets meeting the two fixed lists, whose
own events vanish there.
