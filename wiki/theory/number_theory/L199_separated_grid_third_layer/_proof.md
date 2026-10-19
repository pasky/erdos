---
name: theory/number_theory/L199_separated_grid_third_layer/_proof
title: Separated rows cap the coincidences of every outer layer
desc: Outer-layer locations coincide only between adjacent rows, at most twice, and each missing following location forces a distinct preceding one into the block.
created: 2026-10-15T15:58:15Z
updated: 2026-10-15T15:58:15Z
---

***

Write $B=b_s$ for the largest column offset. Summing the separation
inequalities gives $a_{i'}-a_i>(i'-i)B$ whenever $i'>i$; in particular
$a_{i'}-a_i>2B$ whenever $i'\ge i+2$. For $(i,j)\in S$ the
multiples of $p_{ij}$ are

$$
M_{ij}(t)=z-a_i+tp_{ij}=z+tq+(t-1)a_i+tb_j\qquad(t\in\mathbb Z).
$$

Call $M_{ij}(t)$ the layer-$t$ location of the cell. The layer $0$
location $R_i=z-a_i$ depends only on the row and the layer $1$
location $C_j=z+q+b_j$ only on the column. Write $E_{ij}=M_{ij}(-1)$
and $D_{ij}=M_{ij}(2)=z+2q+a_i+2b_j$.

**Clusters.** Since all offsets are nonnegative and at most $a_r$ and
$B$, the layer locations of the cells of $S$ lie in

$$
\begin{aligned}
t=-1&:\ [z-q-2a_r-B,\ z-q], & t=0&:\ [z-a_r,\ z],\\
t=1&:\ [z+q,\ z+q+B], & t=2&:\ [z+2q,\ z+2q+a_r+2B],\\
t=3&:\ [z+3q,\ z+3q+2a_r+3B].
\end{aligned}
$$

These five intervals are pairwise disjoint because $2a_r+3B<q$.
Every layer $t\le-2$ lies at or below $z-2q$ and every layer $t\ge4$
at or above $z+4q$.

**Multiplicities.** (i) Layer $-1$ is injective on $S$: an equality
$2a_i+b_j=2a_{i'}+b_{j'}$ with $i<i'$ gives
$b_j-b_{j'}=2(a_{i'}-a_i)>2B$, impossible; with $i=i'$ it forces
$j=j'$. (ii) Each value of layer $2$ is taken by at most two cells: if
$a_i+2b_j=a_{i'}+2b_{j'}$ with $i<i'$, then
$a_{i'}-a_i=2(b_j-b_{j'})\le2B$, so $i'=i+1$; and within one row the
value determines the column. So the cells sharing a value lie in at most
two adjacent rows, one in each. (iii) The same holds for layer $3$: an
equality $2a_i+3b_j=2a_{i'}+3b_{j'}$ with $i'\ge i+2$ would give
$2(a_{i'}-a_i)=3(b_j-b_{j'})\le3B$, while $2(a_{i'}-a_i)>4B\ge3B$;
and within one row the value again determines the column.

In particular the set $T_S$ of layer $2$ offsets $a_i+2b_j$ has
$|T_S|\ge\lceil u/2\rceil$.

**Blocks retaining the row and column locations.** Let $J$ be a block of
$K$ consecutive integers containing every $R_i$ and $C_j$ of $S$. Fix
$(i,j)\in S$. The integers strictly between $E_{ij}=R_i-p_{ij}$ and
$D_{ij}=R_i+2p_{ij}$ number $3p_{ij}-1<3P\le K$, so $J$, which contains
$R_i$, also contains $E_{ij}$ or $D_{ij}$. Let $T_{\rm in}$ be the set of
$t\in T_S$ with $z+2q+t\in J$, and choose for each
$t\in T_S\setminus T_{\rm in}$ one cell with $a_i+2b_j=t$. Its layer $2$
location is not in $J$, so its layer $-1$ location is. Distinct values
$t$ give distinct cells and, by (i), distinct layer $-1$ locations.
By the cluster disjointness, $J$ therefore contains at least

$$
r_S+s_S+|T_{\rm in}|+|T_S\setminus T_{\rm in}|=r_S+s_S+|T_S|
$$

distinct multiples.

For $J_0=[z-q+1,z-q+K]$: it contains every $R_i$ because $a_r<q$;
every $C_j$ because $K\ge3P\ge3q$; and every $D_{ij}$ because
$P=q+\max_S(a_i+b_j)$ gives $K\ge3P\ge3q+a_i+2b_j$ for each cell of
$S$. It contains no $E_{ij}$, which is at most $z-q$, and no layer
$3$ location, which is at least $z+3q>z-q+K$ because $K<4q$. The
remaining layers are farther away. So the multiples in $J_0$ are exactly
the $r_S+s_S+|T_S|$ locations of layers $0$, $1$ and $2$.

**Blocks near $z$.** Let $J$ be a block of $K$ consecutive integers inside
$[z-2q+1,z+4q-1]$. It contains no location of a layer $t\le-2$ or
$t\ge4$. Each cell has at least three consecutive multiples in $J$,
since $K\ge3p_{ij}$, and three consecutive layers among
$-1,0,1,2,3$ include at least one of the outer layers $-1$, $2$ and $3$.
Let $n_t$ be the number of cells whose layer-$t$ location is in $J$,
for $t\in\{-1,2,3\}$; then $n_{-1}+n_2+n_3\ge u$. By (i) to (iii) these
locations take at least $\lceil n_t/2\rceil$ distinct values in each
outer layer, and the clusters are disjoint, so $J$ contains at least

$$
\lceil n_{-1}/2\rceil+\lceil n_2/2\rceil+\lceil n_3/2\rceil
\ \ge\ \lceil u/2\rceil
$$

distinct multiples. This proves the window bound.

Replacing $z$ by $z+n\prod_{(i,j)\in S}p_{ij}$ keeps the congruences
and translates every block statement, so the canonical block may be
taken to consist of positive integers.

**The sharp full-grid bound.** For $S=\{1,\ldots,r\}\times
\{1,\ldots,s\}$, only adjacent rows share third-layer values, and no
value belongs to three rows. Rows $i$ and $i+1$ share one value for
each pair of columns with
$b_j-b_{j'}=(a_{i+1}-a_i)/2=:d_i>B/2$.
No column participates in two of these pairs: a two-edge chain would
have span $2d_i>B$, and each column has at most one predecessor and one
successor at distance $d_i$. Thus the pairs form a matching and number
at most $\lfloor s/2\rfloor$. With $\mathcal B=\{b_1,\ldots,b_s\}$,
counting the overlaps gives

$$
|T_S|=rs-\sum_{i=1}^{r-1}
|(a_i+2\cdot\mathcal B)\cap(a_{i+1}+2\cdot\mathcal B)|
\ge rs-(r-1)\lfloor s/2\rfloor.
$$

Here $2\cdot\mathcal B$ is the dilate, not a two-fold sumset.
For an equality pattern take columns $b_j=j-1$ and rows
$a_i=2(i-1)\lceil s/2\rceil$. The row gap exceeds $s-1$ and adjacent
third-layer rows share exactly $s-\lceil s/2\rceil=\lfloor s/2\rfloor$
values. Fix $3\le\alpha<4$ and apply L202 to the cells $(-a_i,b_j)$.
Their differences $a_i+b_j$ are distinct. The proof of L202 supplies
integers $h,q$ with all $q+h(a_i+b_j)$ prime and
$(4-\alpha)q\ge16h\Omega+1$, where
$\Omega\ge\max(1,a_r,b_s)$. Consequently
$2ha_r+3hb_s<q$ and

$$
K=\lfloor\alpha\max_{i,j}(q+ha_i+hb_j)\rfloor
\le\alpha(q+2h\Omega)<4q.
$$

The scaled grid therefore meets all the hypotheses and preserves every
projection coincidence. Its canonical positive block has exactly
$r+s+rs-(r-1)\lfloor s/2\rfloor$ counted integers, which is the
core-retaining minimum already proved.
