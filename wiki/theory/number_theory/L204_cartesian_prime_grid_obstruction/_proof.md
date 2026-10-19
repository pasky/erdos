---
name: theory/number_theory/L204_cartesian_prime_grid_obstruction/_proof
title: Minimal sumset growth and a median cut through the grid
desc: Doubling a uniquely represented sum embeds it in a two-fold sumset, and a median rectangle forces many preceding or following multiples into every block retaining the core.
created: 2026-10-15T16:33:51Z
updated: 2026-10-15T16:33:51Z
---

***

For a set $C$, write $2\cdot C=\{2c:c\in C\}$. This is a dilate,
whereas $C+C$ allows two independently chosen elements.

**A minimal-growth lemma.** Let $A$ and $V$ be nonempty finite sets in
an abelian group. Choose a nonempty $X\subseteq V$ minimizing
$\kappa=|X+A|/|X|$ over nonempty subsets of $V$. Then for every finite
set $C$,

$$
|X+A+C|\le\kappa|X+C|.
$$

Here is the additive proof of Petridis's Proposition 2.1. Order
$C=\{c_1,\ldots,c_t\}$ and let
$X_i=\{x\in X:x+c_i\notin X+\{c_1,\ldots,c_{i-1}\}\}$.
The new elements at step $i$ in $X+C$ are exactly $X_i+c_i$.
In $X+A+C$, all elements of $(X\setminus X_i)+A+c_i$ have already
appeared. Thus the number of new elements there is at most

$$
|X+A|-|(X\setminus X_i)+A|
\le\kappa|X|-\kappa|X\setminus X_i|
=\kappa|X_i|.
$$

The inequality uses minimality, with an empty complement contributing
zero. Summing over $i$ proves the lemma. Taking $C=A$ gives
$|X+A+A|\le\kappa^2|X|$.

**A third-projection inequality.** Suppose $A+B$ has unique
representations, and put $t=|A+2\cdot B|$. Apply the lemma with
$V=2\cdot B$ and the summand set $A$. Then
$\kappa\le t/s$. For its nonempty $X\subseteq2\cdot B$, the sums
$2a+x$ are all distinct as $(a,x)$ varies: writing $x=2b$, equality
reduces to $a+b=a'+b'$. Hence

$$
r|X|=|2\cdot A+X|\le|A+A+X|
\le\kappa^2|X|\le(t/s)^2|X|.
$$

Canceling $|X|$ gives $t\ge s\sqrt r$. Interchanging $A$ and $B$
proves $|2\cdot A+B|\ge r\sqrt s$. These inequalities hold for any
nonempty subrectangle as well.

**The multiple layers.** In the stated prime grid, the multiples of
$p_{ij}$ are

$$
M_{ij}(t)=z-a_i+t(q+a_i+b_j).
$$

The row and column locations are $R_i=M_{ij}(0)=z-a_i$ and
$C_j=M_{ij}(1)=z+q+b_j$. Write

$$
E_{ij}=M_{ij}(-1)=z-q-2a_i-b_j,\qquad
D_{ij}=M_{ij}(2)=z+2q+a_i+2b_j.
$$

The preceding locations, the row locations, the column locations and
the following locations lie respectively in

$$
\begin{aligned}
&[z-q-2a_r-b_s,z-q], &&[z-a_r,z],\\
&[z+q,z+q+b_s], &&[z+2q,z+2q+a_r+2b_s].
\end{aligned}
$$

These intervals are pairwise disjoint under $2a_r+3b_s<q$.
If $J$ contains the row and column locations and has at least $3P$
integers, then for each cell it contains $E_{ij}$ or $D_{ij}$.
Otherwise, since it contains $R_i$, it would lie strictly between
$E_{ij}$ and $D_{ij}$, an interval containing only $3p_{ij}-1<3P$
integers.

**A median rectangle.** Put $i_0=\lceil r/2\rceil$,
$j_0=\lceil s/2\rceil$, and let $U$ be the right endpoint of $J$.
If $U\ge D_{i_0j_0}$, all $D_{ij}$ with $i\le i_0$, $j\le j_0$
belong to $J$. They lie after the core and at or before $U$. The
third-projection inequality on this lower-left rectangle gives at least

$$
j_0\sqrt{i_0}\ge\frac{s\sqrt r}{2\sqrt2}
$$

distinct following locations. If $U<D_{i_0j_0}$, every $D_{ij}$ with
$i\ge i_0$, $j\ge j_0$ is outside $J$, so every corresponding
$E_{ij}$ belongs to $J$. The other inequality on this upper-right
rectangle gives at least

$$
(r-i_0+1)\sqrt{s-j_0+1}\ge\frac{r\sqrt s}{2\sqrt2}
$$

distinct preceding locations. In either case these locations are
disjoint from the $r+s$ core locations. This proves the stated count.

For the power bound, write $m=\max(r,s)$, $n=\min(r,s)$ and $u=mn$.
Then $\min(s\sqrt r,r\sqrt s)=n\sqrt m=u/\sqrt m$. With
$c=1/(2\sqrt2)$ the count is at least $m+cu/\sqrt m$. The minimum of
this expression over positive real $m$ is
$3(cu/2)^{2/3}=3u^{2/3}/2^{5/3}$.

Replacing $z$ by $z+v\prod_{i,j}p_{ij}$ for a sufficiently large
integer $v$ makes any fixed block positive and preserves its count.
