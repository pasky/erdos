---
name: theory/ramsey_theory/L67_containment_pattern_levels/_proof
title: Nested bands and interior cells
desc: |
  Explicit nested leaf bands give every finite clique, while the last-child
  condition forces containment level one for an interior partition cell.
created: 2026-10-14T13:56:46Z
updated: 2026-10-14T13:56:46Z
---

***

We prove
[[theory/ramsey_theory/L67_containment_pattern_levels/_index|L67]], using
its definitions of $W_3$, $R_1$ and the pattern coloring. The pattern is

$$
A_3,B_3,A_1,B_3,A_2,B_3,A_1,B_3,A_3.                 \tag{1}
$$

## Cliques of arbitrary finite size

**Observation.** For every integer $n\ge2$, the coloring just defined has
a color-$1$ clique of size $n$. Its trees can have strictly increasing
root lengths.

Here is an explicit construction. Put $M=2n(n+2)$, and for
$1\le i\le n$ and $1\le k\le4$ put

$$
\ell_{ik}=(k-1)M+i,
\qquad r_{ik}=kM-(n+2)i.
$$

Represent a tree by an ordered tuple of its root children, each a tuple of
its label-$1$ children, each of those a tuple of leaf labels. Define

$$
T_i=\bigl\langle
 \langle\langle\ell_{i1},r_{i1}\rangle\rangle,
 \langle\langle\ell_{i2},r_{i2}\rangle\rangle,
 \langle\langle\ell_{i3}\rangle,\langle r_{i3}\rangle\rangle,
 \langle\langle\ell_{i4},r_{i4}\rangle\rangle,
 \langle\langle r_{i4}+1\rangle\rangle,\ldots,
 \langle\langle r_{i4}+i\rangle\rangle
\bigr\rangle.                                         \tag{2}
$$

All leaves increase from left to right, and every branch has height
three. Thus $T_i\in W_3$. It has $4+i$ root children, so
$T_1<\cdots<T_n$ in the required well-order.

Fix $i<j$. In each of the first three bands the order is

$$
\ell_{ik}<\ell_{jk}<r_{jk}<r_{ik}.
$$

The fourth band has the same nesting, with the extra leaves inside their
respective right-hand ends:

$$
\ell_{i4}<\ell_{j4}<r_{j4}<r_{j4}+1<\cdots<r_{j4}+j
<r_{i4}<r_{i4}+1<\cdots<r_{i4}+i.
$$

Indeed $r_{j4}+j<r_{i4}$ follows from
$(n+2)(j-i)-j\ge2$. Also
$\ell_{nk}<r_{nk}$, and every band ends before the next begins. These
inequalities show that all the trees' leaf sets are disjoint.

The five cells of $T_i$ relative to $T_j$ are

$$
\{\ell_{i1}\},\quad
\{r_{i1},\ell_{i2}\},\quad
\{r_{i2},\ell_{i3}\},\quad
\{r_{i3},\ell_{i4}\},\quad
\{r_{i4},r_{i4}+1,\ldots,r_{i4}+i\}.
$$

Their levels are $3,1,2,1,3$. For the second and fourth cells, the
largest leaf's label-$1$ ancestor contains its right partner outside the
cell. For the middle cell, the label-$1$ ancestor of $\ell_{i3}$ is a
singleton inside the cell, while its label-$2$ ancestor also contains
$r_{i3}$ outside the cell. The endpoint levels follow the rule.

The four cells of $T_j$ are its first three full root subtrees and the
union of its fourth root subtree with all its extra singleton subtrees.
The two interior cells have level $3$: each contains the full root
subtree of its largest leaf, but not the whole tree. The first and last
cells also have level $3$ by definition. Interleaving the two lists gives
exactly (1). Since this holds for every $i<j$, the trees in (2) form the
claimed clique.

## Degeneracy on good partitions

Let $D$ be a convex partition of $\operatorname{Seq}(T)$ for $T\in W_3$
such that the last child of every nonterminal node is outside $G(T,D)$.
We show that every interior cell has $R_1$ level $1$.

To see this, let $E$ be an interior cell and let $x$ be the leaf labeled
by $\max E$. Since $E$ is not the last cell, Definition 9 puts $x$ in
$X(T,D)$ and hence in $G(T,D)$. Let $y$ be its parent, of ordinal label
$1$. The assumed condition says that the last child of $y$ is not in $G(T,D)$,
so $x$ is not that last child. A later child of $y$ is a leaf with label
strictly larger than $\max E$. It lies outside $E$. Thus $y$ is the
lowest ancestor of $x$ whose leaf set is not contained in $E$, giving
$R_1(E)=1$. Good partitions satisfy the assumed condition by
Definition 11(3), so this conclusion applies to them.

In particular, the $A_2$ interior cell in (1) cannot occur when the
induced partition of $A$ is good. The pattern also requires interior
$B_3$ cells, which cannot occur when the induced partition of $B$ is
good. Restricting the candidate coloring to the paper's good pairs
therefore removes every occurrence of this pattern. It cannot supply the
required pattern realization on such pairs.
