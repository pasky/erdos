---
name: research/erdos_644/minimum_transversal_exchanges
desc: Critical near-three-quarter families with a disconnected minimum-cover exchange graph, a non-submodular replacement function, and an exact linear reconfiguration barrier.
tags: [proved, method-obstruction, transversals]
sources: []
created: 2026-09-23T00:04:55Z
updated: 2026-10-13T05:28:09Z
---


# research/erdos_644/minimum_transversal_exchanges

***

This investigates a different upper-bound route: organize the family around a
minimum transversal and use exchanges to replace its points. The exact residual
identities below suggest a Hall-type argument, but the subsequent construction
shows that neither submodularity nor local accessibility follows, even after
passing to a transversal-critical family at the conjectured three-quarter scale.

Write $P_7$ for the condition that every subfamily of at most seven edges has a
transversal of size at most two. All families here are finite. Neither assertion
of Problem 644 is resolved.

## The proposed exchange reduction

Let $T$ be a minimum transversal of a family $\mathcal H$, with $|T|=t$. For
$S\subseteq T$, put

$$
\mathcal H_S=\{E\in\mathcal H:E\cap T\subseteq S\}.
$$

Then

$$
\tau(\mathcal H_S)=|S|.
\tag{1}
$$

Indeed, $S$ covers this subfamily, since every edge meets $T$. If a smaller set
$Y$ covered it, $(T\setminus S)\cup Y$ would cover all of $\mathcal H$ with
fewer than $t$ points. In particular, whenever $Y\subseteq V\setminus T$ has
$|Y|<|S|$, an edge satisfies

$$
\varnothing\ne E\cap T\subseteq S,
\qquad E\cap Y=\varnothing.
$$


One possible replacement function is

$$
r_T(Y)=\max\{|S|:S\subseteq T,\ (T\setminus S)\cup Y
\text{ covers }\mathcal H\},\qquad Y\subseteq V\setminus T.
\tag{2}
$$

It is monotone and satisfies $r_T(Y)\le|Y|$, by minimality of $T$. A
matroid-rank or exchange interpretation would be useful, as would a way of
walking to a better minimum transversal through small exchanges. Both assertions
fail in the strong form tested below.

## A critical construction at the three-quarter scale

For every integer $m\ge2$, there is a family $\mathcal H$ with

$$
K=4m+1,\qquad \tau(\mathcal H)=3m,\qquad P_7,
$$

which is $\tau$-critical and has the following properties. Its
minimum-transversal graph under one-for-one exchanges has exactly two
components, one an isolated vertex $T$. Its replacement function (2) violates
submodularity by $3m$. Finally, any path from $T$ to another minimum
transversal, adding or deleting one vertex at each step and remaining a
transversal throughout, must reach size at least $6m-2$; this bound is attained.

Thus the required temporary excess over the minimum size is exactly $3m-2$,
linear in the rank. These statements do not disprove the conjectured transversal
bound: the ratio is $3m/(4m+1)\to3/4$.

### Definition

Put

$$
p=3m,\qquad a=4m,\qquad n=7m-1=a+p-1.
$$

Take an $n$-point core $X$, labeled by residues in $\mathbb Z_p$. Each residue
has two core representatives; give an additional representative to $m-1$
distinct residues. Thus every residue occurs two or three times. Write $\ell(x)$
for the label of $x$.

For $E\in\binom Xa$, define

$$
c(E)=\sum_{x\in E}\ell(x)\pmod p.
$$

Take disjoint tag vertices $T=\{z_c:c\in\mathbb Z_p\}$, and put

$$
\mathcal H=\{E\cup\{z_{c(E)}\}:E\in\tbinom Xa\}.
\tag{3}
$$

No primality assumption is made on $p$.

### The local property

The complete $a$-uniform family on $X$ has $P_7$. In seven core edges the total
incidence count is

$$
7a=28m>4n=28m-4,
$$

so some core point belongs to at least five of them. Any two core edges
intersect because $2a>n$, and a second point therefore meets the at most two
remaining edges. The same core points cover the tagged edges. There are more
than seven edges, so smaller subfamilies inherit the property as well.

### All colors survive many core deletions

**Lemma.** If $R\subseteq X$ and $|R|\le p-3$, then the $a$-subsets of
$X\setminus R$ have all $p$ colors.

**Proof.** Set $r=|R|$, $U=X\setminus R$, and $d=p-1-r\ge2$, so $|U|=a+d$. Let
$D\subseteq\mathbb Z_p$ be the labels still represented in $U$. Erasing a label
requires at least two deletions, hence

$$
|D|\ge p-\lfloor r/2\rfloor,
\qquad 2|D|-p\ge3.
$$

For every $s\in\mathbb Z_p$,

$$
|D\cap(s-D)|\ge2|D|-p\ge3.
$$

The congruence $2u=s$ has at most two solutions in the cyclic group
$\mathbb Z_p$. Thus this intersection contains some $u$ with $u\ne s-u$, giving
two distinct labels in $D$ whose sum is $s$.

Choose a set $W\subseteq U$ with one point of each label in $D$. Since
$|W|\le p\le a$, choose a fixed set $F\subseteq U\setminus W$ of size $d-2$. As
two distinct points of $W$ vary, the sums of the $d$-sets consisting of $F$ and
those two points range over all residues. Their complements in $U$ are $a$-sets
with all colors. $\square$

Consequently, any transversal using at most $p-3$ core points must contain
**every** tag.

### Transversal number and all minimum transversals

The minimum transversals are exactly

$$
T;\qquad
C\in\tbinom Xp;\qquad
(X\setminus E)\cup\{z_{c(E)}\}quad(E\in\tbinom Xa).
\tag{4}
$$

In particular, $\tau(\mathcal H)=p$.

To check this, consider a transversal of size at most $p$, and write $R$ for its
core part and $r=|R|$. If $r\le p-3$, the lemma forces all $p$ tags, so the only
possibility is $T$.

If $r=p-2$, the remaining core $U$ has size $a+1$. Its $a$-subsets are obtained
by deleting one point, so their colors form

$$
\sum_{x\in U}\ell(x)-\{\ell(x):x\in U\}.
$$

This set has at least $p-\lfloor(p-2)/2\rfloor>2$ elements. At most two selected
tags cannot cover all these edges, excluding this case.

If $r=p-1$, exactly one core $a$-set $E=X\setminus R$ avoids $R$. Its tag is
necessary and sufficient, giving the third class in (4). If $r=p$, there is no
room for tags, and every such core set is a transversal because its core
complement has size $a-1$. This proves (4) and excludes every smaller
transversal.

For a tagged edge based on $E$, the core set $X\setminus E$ has size $p-1$,
misses this edge, and meets every other edge: distinct core edges have the same
size $a$. Deleting that edge therefore lowers the transversal number from $p$ to
$p-1$. Thus $\mathcal H$ is $\tau$-critical.

## Disconnected exchanges and failure of submodularity

Join two minimum transversals when one is obtained from the other by replacing
one vertex. By (4), every minimum transversal other than $T$ contains at least
$p-1$ core points. Reaching any of them directly from $T$ requires at least
$p-1$ simultaneous replacements; in particular $T$ is isolated.

All the core $p$-sets form a connected Johnson graph. Every mixed minimum
transversal $(X\setminus E)\cup\{z_{c(E)}\}$ is adjacent to a core $p$-set, by
replacing its tag by any point of $E$. These account for all other minimum
transversals, so there are exactly two components.

Criticality does supply cliques of minimum covers: for an edge $A$ and a
critical $(p-1)$-cover $C_A$ disjoint from it, the sets $C_A\cup\{v\}$,
$v\in A$, are minimum transversals. Here all the cliques supplied by
$C_A=X\setminus E$ lie in the large component. They do not reach the isolated
minimum transversal.

The replacement function (2) is also far from submodular. The lemma gives
$r_T(Y)=0$ for $|Y|\le p-3$. Take any core $p$-set $B$ and partition it into two
parts $B_1,B_2$ with sizes $\lfloor p/2\rfloor,\lceil p/2\rceil$. Since $p\ge6$,
both sizes are at most $p-3$. Hence

$$
r_T(B_1)+r_T(B_2)=0,
\qquad
r_T(B_1\cup B_2)+r_T(B_1\cap B_2)=p.
$$

The submodular inequality fails by $p=\Theta(K)$, despite criticality, $P_7$,
and (1).

## An exact reconfiguration barrier

Consider paths of transversals starting at $T$, with each step adding or
deleting one point. Before the first tag is deleted, the current transversal
contains all $p$ tags. Immediately after that deletion its core part must have
size at least $p-2$, by the lemma. That core part was already present before the
deletion. Thus every path reaching any other minimum transversal passes through
a set of size at least

$$
2p-2.
\tag{5}
$$


This is sharp. Choose a residue with exactly two core representatives, and a set
$R\subseteq X$ of size $p-2$ containing both of them. Such a residue exists,
since only $m-1$ of the $p$ residues have a third representative. The set
$U=X\setminus R$ has size $a+1$ and lacks that residue. The colors of its
$a$-subsets consequently omit some color $c$, by the displayed palette formula
above.

Starting from $T$, add the points of $R$ one at a time, and then delete $z_c$.
This remains a transversal. Add one further core point $w\notin R$. Now the only
core edge avoiding the selected core points is

$$
E'=X\setminus(R\cup\{w\}).
$$

Its color $c'$ differs from $c$, since $E'\subseteq U$ and color $c$ was
absent there. Delete every tag except $z_{c'}$. This ends at the mixed minimum
transversal $(R\cup\{w\})\cup\{z_{c'}\}$. Every intermediate set is a
transversal and has size at most $2p-2$. This proves the exact threshold (5).

More generally, suppose each step adds at most $q$ points and deletes at most
$q$ points, and every intermediate transversal has size at most $p+s$. Before
the first step dropping a tag, there are at most $s$ core points; afterwards
there must be at least $p-2$. Therefore

$$
s+q\ge p-2
$$

is necessary to leave tag containment. Sublinear slack together with
sublinear-size exchanges cannot escape.

Even the singleton-trace layer remains large throughout the accessible region.
For a transversal $C=T\cup R$, with $R\subseteq X$ and $|R|=r\le p-1$, the edges
meeting $C$ in exactly one point are precisely the tagged edges whose cores
avoid $R$. Their transversal number is exactly $p-r$: it is at least
$\tau(\mathcal H)-r$, and any $p-r$ remaining core points cover all remaining
core $a$-sets. Thus $o(K)$ local slack does not make that layer have sublinear
transversal number.

## A global choice is still different from an exchange walk

This construction does not obstruct choosing a better minimum transversal
globally. In fact, maximizing

$$
\Phi(C)=\sum_{A\in\mathcal H}|A\cap C|
$$

among minimum transversals selects exactly the all-core $p$-sets in (4).

To check this, put $M=\binom na$. Every core vertex has degree $(a/n)M$. A tag
has degree at most $(3/p)M$: each $(a-1)$-set has at most three extensions to a
core edge of a prescribed color, so

$$
a\deg(z_c)\le3\binom n{a-1}=\frac{3a}{p}M.
$$

For $m\ge2$, $3/p=1/m<a/n$. The classification (4) therefore proves the claim.
For an all-core minimum transversal $C$, its singleton-trace edges all contain
the common $(a-1)$-set $X\setminus C$, so that layer has transversal number one.

There is a small general observation in the same direction. In a $\tau$-critical
family containing two distinct intersecting edges $A,B$, a minimum transversal
meeting every edge exactly once cannot maximize $\Phi$. Take a critical
$(t-1)$-cover $C_A$ disjoint from $A$, and $v\in A\cap B$. The minimum
transversal $C_A\cup\{v\}$ meets every edge and meets $B$ at least twice, giving
potential at least $|\mathcal H|+1$ rather than $|\mathcal H|$. A
potential-maximizing minimum transversal therefore has a proper singleton-trace
subfamily, whose transversal number is at most $t-1$ by criticality. This only
saves one point.

What remains unproved is any substantial improvement for such a globally
selected transversal—for example, a sublinear bound on the singleton-trace layer
in the relevant linear-transversal regime. Even that would need a further
argument to control the other trace layers. The exchange identities alone,
submodularity, and small local reconfiguration do not provide the required upper
bound.
