---
name: research/erdos_774/lemmas/colored_line_preimages
title: A sharp dimension boundary for existential colored line lifting
desc: Common real spans yield simultaneous flat same-color lifts in two directions, but an explicit rationally independent twelve-line class in three directions has a flat point-supported image and no nonzero flat lift on that support.
tags: [E0774, proved, obstruction, coloring, lifting]
sources: []
created: 2026-09-18T20:06:38Z
updated: 2026-09-18T20:18:00Z
---


# A sharp dimension boundary for existential colored line lifting

***

## Standing and notation

For a family $S$ of axis-line indicators, write
$$
\Sigma_1(S)=\left\{\sum_{\ell\in S}a_\ell\ell:
                    a_\ell\in\{-1,0,1\}\right\}.
$$
For a point set $P$, $\mathbb R^P$ denotes the vectors supported
on $P$, extended by zero outside $P$. Line subsets below can be
**actual color classes**; no recoloring or replacement by their rational
rank is made.

The [quotient route](../routes/axis_line_quotient.md) needs a nonzero flat
point vector in several same-color sets $\Sigma_1(S_s)$ at once.
This page proves that real spans suffice for that **existential** question
in two directions, and disproves this replacement already in three
directions. The [unrestricted preimage theorem](axis_line_flat_preimages.md)
does not control the support of a preimage, so it is consistent with both
results. Neither result proves unbounded coloring of the line family.

## 1. Simultaneous existential lifting in two directions

Let $X,Y$ be finite nonempty sets. Write
$R_x=\mathbf1_{\{x\}\times Y}$ and
$C_y=\mathbf1_{X\times\{y\}}$.
Let $S_1,\ldots,S_k$ be arbitrary subsets of these row and column
lines, and let $P\subseteq X\times Y$.

**Theorem.** The following conditions are equivalent:
$$
\left(\bigcap_{s=1}^k\operatorname{span}_{\mathbb R}S_s\right)
\cap\mathbb R^P\ne\{0\},                                      \tag{1}
$$

$$
\left(\bigcap_{s=1}^k\Sigma_1(S_s)\right)
\cap\{-1,0,1\}^P\ne\{0\}.                                   \tag{2}
$$
Thus one nonzero common target can be chosen with height-one preimages
in **every specified actual line class**. The theorem does not promise
height-one preimages for a prescribed target in (1).

**Proof.** Only (1) implies (2) requires proof. A nonzero vector from
(1) can be written
$$
b(x,y)=u(x)-v(y).
$$
For each $s$, any other row-plus-column representation of the same
function differs by a scalar gauge. Consequently its coefficients on
the row and column lines can be written
$$
u(x)-\alpha_s,\qquad \alpha_s-v(y),                            \tag{3}
$$
respectively, for a real scalar $\alpha_s$. This follows by fixing
one $x$ and one $y$ in the identity between the two representations.

Build an undirected graph on the disjoint union of vertex sets
$X$, $Y$, and $[k]$. Insert edges

- $x\!\sim\!s$ whenever $R_x\notin S_s$;
- $y\!\sim\!s$ whenever $C_y\notin S_s$;
- $x\!\sim\!y$ whenever $(x,y)\notin P$.

Assign the real values $u(x),v(y),\alpha_s$ to these vertices.
Equations (3), the zero coefficients outside each $S_s$, and the
support condition on $b$ show that this assignment is constant on
every connected component. Because $b\ne0$, some $x,y$ belong
to different components. Let $K$ be the component containing this
$x$, and replace all vertex values by the indicator of $K$.
Denote the resulting values by $u',v',\alpha'_s$.

Now
$$
b'(x,y)=u'(x)-v'(y)
$$
is nonzero, has values in $\{-1,0,1\}$, and vanishes outside
$P$. For every $s$, its row and column coefficients
$$
u'(x)-\alpha'_s,\qquad \alpha'_s-v'(y)
$$
also lie in $\{-1,0,1\}$. The graph edges ensure that every
coefficient outside $S_s$ is zero. These are the required
simultaneous preimages. $\square$

The common point labeling is essential to this proof. Arbitrary
permutations of the points in different layers do not preserve its
equality-constraint graph; no twisted-layer version is claimed.

## 2. A prescribed target can fail even in two directions

Assume $|Y|\ge2$, choose $y_0\in Y$, and put
$$
S=\{R_x:x\in X\}\cup\{C_{y_0}\}.
$$
These lines are rationally independent: evaluation at an unselected
column first forces all row coefficients to vanish, and evaluation at
the selected column then forces its coefficient to vanish.

Consider the flat target
$$
b(x,y)=\begin{cases}1,&y=y_0,\\-1,&y\ne y_0.\end{cases}
$$
Its unique preimage supported on $S$ is
$$
b=2C_{y_0}-\sum_{x\in X}R_x.                                 \tag{4}
$$
It therefore has no height-one preimage on this rationally independent
actual color class. The full line family does have a flat preimage,
namely $C_{y_0}-\sum_{y\ne y_0}C_y$.

This does not contradict Section 1: another nonzero target supported
on the same point set can have a flat preimage on $S$.

## 3. A three-direction obstruction even to existential lifting

Work on $\{0,1,2\}^3$. Write $A_{yz}$, $B_{xz}$, and
$C_{xy}$ for the full lines in the first, second, and third
directions. Let $S$ consist of the following twelve lines, and
define the integer coefficient vector $a$ by the table:

| Lines | Coefficient in $a$ |
|---|---:|
| $A_{00},A_{02},A_{11}$ | $-1$ |
| $A_{01}$ | $-2$ |
| $B_{01},B_{10},B_{11},B_{12},B_{21}$ | $+1$ |
| $C_{00},C_{20}$ | $+1$ |
| $C_{12}$ | $-1$ |

Its point image $b=A_Sa$ is flat. Its nonzero coordinates are
$$
\begin{array}{c|rrrrr}
\text{point}&(0,2,1)&(1,0,1)&(1,1,0)&(1,1,2)&(2,2,1)\\\hline
b&1&-1&1&1&1.
\end{array}                                                    \tag{5}
$$
Put $P=\operatorname{supp}b$. The same point vector also has the
unrestricted flat preimage
$$
b=A_{21}+C_{11}-B_{11},                                       \tag{6}
$$
whose first two lines are not in $S$.

The exact colored conclusion is
$$
\operatorname{span}_{\mathbb R}(S)\cap\mathbb R^P
       =\mathbb R b\ne\{0\},\qquad
\boxed{\Sigma_1(S)\cap\mathbb R^P=\{0\}.}                    \tag{7}
$$
Moreover $S$ is rationally independent. Thus the obstruction is
present even in a color class with no rational dependence at all.

### 3.1 Symbolic elimination certificate

Give an arbitrary coefficient vector on these twelve lines the names
$$
\begin{array}{c|cccccccccccc}
\text{line}&A_{00}&A_{01}&A_{02}&A_{11}&B_{01}&B_{10}&B_{11}&B_{12}
&B_{21}&C_{00}&C_{12}&C_{20}\\\hline
\text{coefficient}&u_0&u_1&u_2&v&p&q_0&q_1&q_2&r&s&t&w.
\end{array}
$$
Suppose its point image vanishes outside $P$. The following
evaluations all occur outside $P$:
$$
\begin{array}{c|l}
\text{point or points}&\text{forced equation or consequence}\\\hline
(0,0,0),(0,0,2)&u_0=u_2=-s\\
(0,1,1)&v=-p\\
(0,0,1)&u_1=-p-s\\
(1,0,0),(1,0,2)&q_0=q_2=s\\
(1,1,1)&q_1=p\\
(1,2,0)&t=-s\\
(1,2,1)&p=s\\
(2,0,0)&w=s\\
(2,1,1)&r=p=s.
\end{array}                                                    \tag{8}
$$
Hence the coefficient vector is exactly $s a$. Conversely (5)
checks that every such multiple has image supported on $P$.
This proves the first equality in (7). It also proves rational
independence of $S$: if the whole image is zero, its value at
$(0,2,1)$, namely $s$, forces every coefficient to vanish.

If all twelve coefficients are in $\{-1,0,1\}$, then the
coefficient at $C_{00}$ gives $s\in\{-1,0,1\}$, while the
coefficient at $A_{01}$ is $-2s$. The latter can have height
at most one only when $s=0$. This proves the boxed statement.
No rank computation is needed for this certificate.

### 3.2 Actual-color interpretation and scope

Color the twelve lines in $S$ with one actual color $c$, and
give every other old line its own fresh color. This is a proper
dissociated coloring because $S$ is rationally independent. Give
the points of $P$ color $c$. The monochromatic flat quotient
relation (5) belongs to the span of the correct old color, but there
is **no** nonzero flat old-color sum supported on $P$.

The same obstruction persists with any number of identical untwisted
old layers: use $S$ as color $c$ in every layer and give exactly
the new transversals labeled by $P$ color $c$. A ternary
relation in color $c$ would require a nonzero vector in the boxed
intersection, so it cannot exist. All other columns may receive
separate fresh colors. This is an explicit failure of replacing the
required common same-color signed sums by their real spans.

This finite example does not show that all possible colored lifting
or covering arguments fail. It shows that span membership alone is
insufficient, even for flat point targets, rationally independent
classes, and only three old directions.

### 3.3 Finite discovery record

The witness was discovered in a bounded $[3]^3$ calculation with
Python's standard pseudorandom seed $774009$, using exact SymPy
linear algebra. The submitted program had a hard maximum of 2,000
trials. Each trial selected nine of the 27 quotient point columns;
only a one-dimensional nullspace with primitive coefficients in
$\{-1,0,1\}$ was retained. For each such candidate, at most 20
random spanning trees of the nine-vertex complete tripartite graph
were checked. The finite bounds were present in the submitted command;
the preliminary message called the calculation bounded but did not
separately list these numerical bounds.

The program stopped on zero-based trial 10, the fifth retained flat
candidate, when a gauged line preimage had height two. This first
preimage used fifteen lines. The twelve-line vector above was then
simplified by hand, and a single exact check confirmed that its full
line matrix has rank 12, its restriction to $P^c$ has rank 11,
and its image is (5). Equations (5) and (8) replace those computations
by a complete symbolic proof. No four-or-more-direction feasibility
experiment was performed or repeated.

## 4. A sparse-support reset for arbitrary successive twists

There is also a limited positive actual-color statement extending the
[compatible-twist reset](../routes/transversal_gadgets.md). It does
not provide a reusable chromatic amplifier.

Let $F$ be a configuration on $n$ rows admitting a proper
$q$-coloring. Form a $d$-layer twisted pure-transversal extension
$Y$, where $d\ge2$, and then a $D$-layer twisted
pure-transversal extension $Z$ of $Y$. Both stages may use
arbitrary row bijections. If
$$
nd<d^D,                                                       \tag{9}
$$
then $Z$ admits a proper $(q+1)$-coloring.

Indeed, for each $r\in[d]$, color $Y$ as follows: retain old
color 1 only in its $r$-th layer; replace old color 1 by color
$q+1$ in all other layers; leave the other old colors unchanged;
give all first-stage transversals color $q+1$. This is proper:
restriction of a color-$q+1$ relation to layer $r$ forces every
new transversal coefficient to vanish. Its distinguished color-1
class is supported on the $r$-th old layer, a set $U_r$ of
size $n$. The $U_r$ partition the $nd$ rows of $Y$.

Let $T_s$ be the row twist for the $s$-th layer of $Z$.
Independently choose $r_s\in[d]$ uniformly. Every row label of
$Y$ belongs to
$\bigcap_{s=1}^D T_s^{-1}U_{r_s}$ with probability $d^{-D}$.
Its expected size is $nd/d^D<1$. Some deterministic choice has
empty intersection. Use the corresponding witness coloring in each
layer of $Z$, and give all newest transversals color 1. Restriction
of a color-1 relation to the layers forces its transversal coefficient
vector to be supported on that empty intersection. All remaining
relations lie in already proper old layers. This proves the claim.

More exactly, this support-only construction works whenever the
profile map
$$
y\longmapsto
\bigl(r(T_1y),\ldots,r(T_Dy)\bigr)\in[d]^D,
\quad r(z)\text{ defined by }z\in U_{r(z)},
$$
is not surjective; (9) is a sufficient cardinality condition. When
$nd=d^D$, arbitrary twists can realize all profiles, so this
particular empty-support argument has no unconditional extension.
This does not prove that the resulting configuration requires more
colors. The argument also does not restore a sparse distinguished
class after its second extension, so it is not an indefinitely
repeatable reset with a fixed palette.
