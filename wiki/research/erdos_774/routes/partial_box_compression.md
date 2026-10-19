---
name: research/erdos_774/routes/partial_box_compression
title: Partial-box compression and the bounded-box limit
desc: Good monochromatic cells obey a quantitative compression bound; every fixed disjoint-box complexity has a uniform finite coloring, with 16 colors sufficient for two boxes.
tags: [E0774, proved, coloring, obstruction]
sources: []
created: 2026-09-18T01:42:00Z
updated: 2026-09-18T18:37:35Z
---


# Partial-box compression and the bounded-box limit

***

## Standing

The finite influence calculation in Section 4
below precisely limits one attempted route from approximate profiles to
actual good cells. It does not exclude optimized profile-dependent clustering.

This strengthens [profile compression](root_profile_compression.md) by allowing
only some product cells to be monochromatic. It then proves a limitation of that
mechanism: **every fixed bound on the number of disjoint constant-sign boxes
admits a uniform finite coloring**; 16 colors suffice for two boxes. The bound
is uniform over the distinct odd-prime tensors. This is not a coloring avoiding
all signed relations, and does not settle the
[main coloring obligation](../proof_sketch.md).

The proofs below are elementary, including the finite local lemma used in the
coloring construction. No computation is used.

## 1. Compression of good cells only

Let $f$ be a proper dissociated $q$-coloring of
$E=\bigotimes_i S_{p_i}$. Partition coordinate $[p_i]$ into nonempty
blocks $A_{i,1},\ldots,A_{i,m_i}$. Call a product cell **good** when
$f$ is constant on that whole box. Put

$$
N=\prod_i m_i,\quad d=\prod_i(m_i-1),\quad R=d/N,\quad
L=\sum_i\frac{\log(m_i-1)}{m_i},\quad
\alpha=\frac{\#\{\text{good cells}\}}N.
$$

For $m_i\geq2$ and $\alpha>0$,

$$
\frac\alpha q<4R\left(1+\frac{2L}{\log2}\right). \tag{1}
$$

If some $m_i=1$, then $\alpha=0$, since any good cell would
contain a monochromatic full simplex fiber.

### Proof

The block sums $w_{i,a}=\sum_{x\in A_{i,a}}s_{i,x}$ form a linear
copy of $S_{m_i}$. A rational relation between these sums expands to a
simplex relation constant on each block; the only such relations have the
same coefficient on every block. A signed relation among same-colored good
indexed cells expands over disjoint original boxes and retains every
coefficient in $\{-1,0,1\}$. Thus the good cells have a proper partial
coloring of the indexed compressed tensor. Nongood cells are not colored.

For any dissociated indexed subset $D$ of the compressed tensor, randomly
choose one distinguished simplex column in each coordinate and use all the
other columns as the integer basis. Every fixed tensor column has expected
logarithmic $\ell_1$-norm $L$. Some basis therefore makes the average
logarithmic norm over $D$ at most $L$, and at least $|D|/2$ columns
have norm at most $e^{2L}$. If $L=0$, all columns have norm one.

Let $s\geq|D|/2$ denote this subcollection's size. Its distinct subset
sums fit in coordinate intervals whose total width is at most $s e^{2L}$.
Counting integer points and applying arithmetic--geometric mean gives

$$
2^s\leq\left(1+\frac{s e^{2L}}d\right)^d.
$$

The elementary bound used in
[the small-column argument](tensor_schedule_constraints.md),
$2^t\leq1+Mt\Rightarrow t<2\log_2(2M)$ for $M\geq1$, gives
$|D|<4d(1+2L/\log2)$. A largest color class of good cells has size at
least $\alpha N/q$, proving (1).

For all odd primes through $P\geq e^5$, put
$D_P=\sum_{p\leq P,\ p\text{ odd}}(1/m_p-1/p)$. The estimates already
proved in [profile compression](root_profile_compression.md) give

$$
\frac\alpha q<24(D_P+2)e^{-D_P}\leq48e^{-D_P/2},
\qquad D_P<2\log(48q/\alpha). \tag{2}
$$

When all $m_i=2$, the sharper exact conclusion is
$\#\{\text{good cells}\}\leq q$: every compressed indexed column is
one of two opposite values, so any two labels of the same color would be
dependent with coefficients of magnitude one.

## 2. A uniform coloring avoiding every two-box relation

A product box means a nonempty set $\prod_i A_i$ in a finite tensor
grid. Consider relations whose coefficient function is constant $+1$ or
$-1$ on each of at most two disjoint such boxes, and zero elsewhere.
There is a 16-coloring of each odd-prime grid with no monochromatic relation
of this form. The same holds on the infinite finite-support odd-prime grid.

### Primitive edges

Fix a nonempty finite set $I$ of prime coordinates and fix every other
coordinate. Choose nonempty proper $A_p\subset[p]$, $p\in I$, and set

$$
B=\prod_{p\in I}A_p,\qquad B^*=\prod_{p\in I}A_p^c,
\qquad h=B\cup B^*.
$$

The two boxes are disjoint, and their vector sums differ by the sign
$(-1)^{|I|}$. Thus $h$ supports a signed relation. Its size $s_h$
satisfies

$$
s_h=\prod_{p\in I}a_p+\prod_{p\in I}(p-a_p)
\geq2+\sum_{p\in I}(p-2)\geq3. \tag{3}
$$

Here $\prod_j b_j\geq1+\sum_j(b_j-1)$ for positive integers $b_j$.
The case $|I|=1$ is a full prime fiber.

### Local-lemma estimate

Color each vertex independently with 16 colors. Let $H_h$ be the event
that a primitive edge $h$ is monochromatic, so
$\mathbb P(H_h)=16^{1-s_h}$, and put $x_h=4^{-s_h}$.
For a fixed vertex $v$, orient any incident edge so that $v\in B$.
For fixed $I$ there are at most $\prod_{p\in I}2^{p-1}$ choices of
the sets $A_p$ containing $v_p$. This may count an edge repeatedly,
which only enlarges the bound. By (3),

$$
\begin{aligned}
\sum_{h\ni v}x_h
&\leq\frac1{16}
 \left(\prod_{p\text{ in the grid}}(1+2^{3-p})-1\right)\\
&\leq\frac1{16}\left(\exp\sum_{p\text{ odd}}2^{3-p}-1\right)
<\frac3{16}. \tag{4}
\end{aligned}
$$

Indeed $\sum_{p\text{ odd}}2^{3-p}\leq\sum_{j\geq0}4^{-j}=4/3 <\log4$. For
example $\log2>2/3$ follows by integrating the strictly convex function $1/x$
over $[1,2]$.

Use intersecting supports as the event dependency graph. Disjoint supports
give independence from the entire corresponding event sigma-algebra. Since
$x_h\leq1/64$, $\log(1-x_h)\geq-2x_h$. Therefore

$$
\prod_{g\sim h}(1-x_g)>
\exp(-3s_h/8).
$$

For $s\geq3$,

$$
\log\frac{4^{-s}e^{-3s/8}}{16^{1-s}}
=(s-2)\log4-3s/8>0,
$$

because the left expression increases with $s$, and at $s=3$ it is
$\log4-9/8>0$. Hence

$$
\mathbb P(H_h)<x_h\prod_{g\sim h}(1-x_g). \tag{5}
$$

For completeness, the finite asymmetric local lemma in precisely this form
has a short induction proof. For every event $H_i$ and collection $S$
of other events, induction on $|S|$ proves
$\mathbb P(H_i\mid\bigcap_{j\in S}H_j^c)\leq x_i$. Separate $S$
into neighbors $D$ and nonneighbors $J$. The numerator is at most
$\mathbb P(H_i\mid\bigcap_{j\in J}H_j^c)=\mathbb P(H_i)$, while
successive conditional complementary probabilities bound the denominator
below by $\prod_{j\in D}(1-x_j)$. Each conditioning collection for
this denominator is smaller than $S$. If $D$ is empty, independence
applies directly. Equation (5) gives the claimed inductive bound and all
conditioning events have positive probability. Multiplying the resulting
complementary conditional probabilities shows that avoiding all events has
positive probability.

We thus obtain the desired finite coloring. A diagonal subsequence on nested
prime prefixes stabilizes each vertex's color and avoids every primitive edge
globally, since every edge has finite support.

### Why primitive edges cover all two-box relations

The sum of a product box is the tensor product of its coordinate sums. It is
zero precisely when a coordinate side is the full simplex; such a box contains
a full monochromatic prime fiber if it is monochromatic.

Otherwise all coordinate sums are nonzero. If two box sums agree up to sign,
uniqueness of nonzero pure tensors makes their coordinate sums proportional.
For nonempty proper simplex subsets $A,C$, the condition
$w(A)=\lambda w(C)$, $\lambda\ne0$, says that
$1_A-\lambda1_C$ is constant. Inspecting the membership patterns shows
that either $A=C,\lambda=1$, or $C=A^c,\lambda=-1$. Thus every
coordinate side is either identical or complementary. At least one coordinate
is complementary for distinct disjoint boxes. Fix a symbol in every identical
side; the remaining two subboxes form a primitive edge. The constructed
coloring therefore excludes the original monochromatic relation as well.

## 3. Every fixed disjoint-box complexity is finitely colorable

Fix $M\geq1$. An $M$-box relation is a nonzero ternary relation
whose coefficient function is constant $+1$ or $-1$ on each of at
most $M$ pairwise disjoint product boxes. There is a coloring avoiding
all such monochromatic relations on the entire finite-support odd-prime grid
with at most

$$
Q_M=2^{2M+4}\prod_{\substack{p<2M+4\\p\text{ odd prime}}}p
\tag{6}
$$

colors. For $M=2$, the separate two-box proof improves this general palette
bound to 16 colors.

### Slicing a relation to full projections

If a relation's projection onto coordinate $p$ is a proper subset
$A\subsetneq[p]$, write it as $\sum_{a\in A}s_{p,a}\otimes u_a=0$.
The proper simplex subset is independent, so every $u_a=0$. Choose
any occupied slice. Its formal relation is nonzero and still consists of at
most $M$ disjoint constant-sign boxes: a slice either deletes a box or
fixes its $p$-coordinate, and distinct surviving boxes stay disjoint.
Remove that fixed coordinate and repeat as necessary. The process ends at
a nontrivial relation having full projection on every remaining coordinate.
At least one coordinate remains, since a nonzero zero-dimensional tensor
cannot have a nontrivial one-point signed relation.

### Counting an enlarged tail hypergraph

Put $P_0=2M+4$. In the tail $p\geq P_0$, include as edges
**all** disjoint unions of $r\leq M$ product boxes which have full
projection in every coordinate of some nonempty finite varying set $I$,
with other coordinates fixed. Such an edge need not itself support a relation.
If its side sizes are $a_{j,p}$ and its cardinality is $m$, then

$$
\begin{aligned}
m=\sum_{j=1}^r\prod_{p\in I}a_{j,p}
&\geq r+\sum_{p\in I}\left(\sum_j a_{j,p}-r\right)\\
&\geq r+\sum_{p\in I}(p-r)
\geq\tfrac12\sum_{p\in I}p.
\end{aligned}\tag{7}
$$

Full projection also gives $m\geq\max_{p\in I}p\geq P_0$.
For a vertex $v$ and fixed $I$, the outside context is forced;
there are at most $M2^{M\sum_{p\in I}p}$ ordered box presentations
of incident edges. This bound ignores all disjointness, incidence, and
full-projection restrictions and therefore overcounts safely.

Set $x=2^{-2M-2}$ and give edge $h$ charge $x^{|h|}$.
Equation (7) bounds the incident charge by

$$
\begin{aligned}
C:=\sup_v\sum_{h\ni v}x^{|h|}
&\leq M\left(\prod_{p\geq P_0}(1+2^{-p})-1\right)\\
&\leq M\left(e^{2^{1-P_0}}-1\right)
\leq2M2^{1-P_0}=M2^{-2M-2}\leq\tfrac1{16}.
\end{aligned}\tag{8}
$$

Here the prime sum was bounded by all integers at least $P_0$, and
$e^t-1\leq2t$ for $0\leq t\leq1$ suffices.

Independently color a finite tail grid with $q=2^{2M+4}=4/x$ colors.
A monochromatic edge of size $m$ has probability $q^{1-m}$.
As in Section 2, its neighbor charge product is at least
$e^{-2mC}\geq e^{-m/2}$. Moreover

$$
\log\frac{x^m e^{-m/2}}{q^{1-m}}
=m(\log4-1/2)-P_0\log2
\geq P_0(\log2-1/2)>0.
$$

The proved finite local lemma therefore supplies a coloring avoiding every
enlarged edge. Diagonal compactness gives one such coloring on the whole tail.

Finally color a full tuple by its tail color together with its complete tuple
of small-prime symbols $p<P_0$, using the palette in (6). Any
monochromatic $M$-box relation would be fixed on these small coordinates.
Slicing its tail relation as above gives a nontrivial monochromatic enlarged
edge, a contradiction.

## 4. A finite approximate-profile certificate and its limit

Let $f:\prod_{i=1}^k[p_i]\to[q]$, and define the full-profile influence
$$
I_i=\Pr[f(X)\ne f(X^{(i)})],
$$
where $X$ is uniform and $X^{(i)}_i$ is a uniformly chosen
**different** symbol, with all other coordinates unchanged.
This is not single-coordinate mutual information.

In coordinate $i$, prescribe positive block sizes summing to $p_i$,
with $m_i\ge2$ blocks, and randomly permute the symbols into those blocks.
Put $b_i=p_i/m_i$. Some choices of the partitions have good-cell
fraction
$$
\alpha\ge1-W,\qquad
W=\sum_i(b_i-1)\left(\prod_{j<i}b_j\right)I_i. \tag{9}
$$
Here cells, not original vertices, receive equal weight.

For a proof choose a compressed cell uniformly. If its side sizes are
$s_i$, a rooted Cartesian spanning tree has
$(s_i-1)\prod_{j<i}s_j$ edges of type $i$: vary coordinate $i$
from its first symbol, allow all earlier coordinates, and fix all later
coordinates at their first symbols. Each such edge under the random
coordinate permutations has disagreement probability $I_i$.
A nonmonochromatic cell has a disagreeing tree edge. Average the union
bound, using independence of the chosen block indices and
$\mathbb E s_i=b_i$, to obtain (9).

If every full prime fiber is nonmonochromatic, then
$$
I_i\ge\frac2{p_i}.
$$
Indeed a nonconstant fiber has at least $2(p_i-1)$ ordered disagreeing
pairs, out of $p_i(p_i-1)$. Hence, with
$D=\sum_i(1/m_i-1/p_i)$,
$$
W\ge2\sum_i\frac{b_i-1}{p_i}=2D. \tag{10}
$$
The **displayed** lower-bound certificate $1-W>0$ therefore requires
$D<1/2$.

In the odd-prime-prefix regime of Section 1, where its stated cutoff
hypothesis holds, contradiction via the $48$-constant deficit bound
would require
$\alpha>48q e^{-D/2}$.
For $D<1/2$ the right side exceeds one. Thus (9) cannot supply the
required good-cell fraction for that criterion.

This is a limitation of this random-label merging and tree union-bound
certificate only. It is not a theorem about optimized profile-dependent
clusterings, all first-moment arguments, or the entire signed relation
system. The finite inequality, its averaging convention, and this exact
scope received independent internal review. No experiment was run.

## Exact remaining requirement

No claim here colors all signed relations: $M$ is fixed before the coloring, and
$Q_M$ grows with $M$. Thus a successful box-based proof of unbounded chromatic
number must use unbounded disjoint-box complexity. In particular, binary block
compression cannot on its own prove unbounded chromatic number: the displayed
existence theorem supplies a fixed-palette coloring under which every binary
product partition has at most one good cell per color. A successful further use
of (1)--(2) needs additional information from the full signed relation system,
not a Ramsey assertion contradicted by this coloring. Both finite-coloring
proofs received independent internal audits of slicing, incidence counting, the
local lemma, and compactness.
