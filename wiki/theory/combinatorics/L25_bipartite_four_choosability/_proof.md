---
name: theory/combinatorics/L25_bipartite_four_choosability/_proof
title: A minimal palette and two counting inequalities
desc: All possible palette sizes for a bad four-list assignment on at most 25 vertices are excluded by exact counting.
created: 2026-10-14T12:38:34Z
updated: 2026-10-14T12:38:34Z
---

***

Complete any fixed bipartition to $K_{a,c}$; an uncolorable assignment
stays uncolorable after adding edges. Suppose such an assignment exists
with $v=a+c\le25$, and among bad four-list assignments on this complete
bipartite graph choose one minimizing its palette size $N$.

Every pair of palette colors occurs together in some list. Otherwise
identify a pair that never cooccurs. No list shrinks, and any proper coloring
from the merged lists lifts to the original lists: the preimage at each
vertex is unique, and distinct merged colors have distinct original colors.
This contradicts palette minimality. Pair counting and then counting
cooccurrences with each fixed color give

$$
\binom N2\le6v,\qquad
4v\ge N\left\lceil\frac{N-1}{3}\right\rceil. \tag{1}
$$

For a palette subset $T$ of size $\ell$, one can color using $T$ on
the left and its complement on the right if every left list meets $T$
and no right list is contained in $T$. A bad assignment therefore covers
every such $T$ by a left list it misses or a right list it contains.
Counting, with out-of-range binomial coefficients equal to zero, yields

$$
a\binom{N-4}{\ell}+c\binom{N-4}{\ell-4}\ge\binom N\ell.
$$

Add the inequality with $N-\ell$ in place of $\ell$ to obtain

$$
v\left(\binom{N-4}{\ell}+\binom{N-4}{\ell-4}\right)
\ge2\binom N\ell. \tag{2}
$$

These arguments are the palette-merging and covering method of
[[../library/graph_coloring/hanson_1996_choosability_bipartite_graphs/_index|Hanson–MacGillivray–Toft]],
Lemmas 1–3 and Theorem 1, pp. 184–187. The required specializations have
been proved above rather than left as an uninspected source premise.

If $N\le6$, partition the palette into two parts of size at most three.
Every four-list meets both, giving a coloring with separate palettes on
the two sides. Thus $N\ge7$. Inequality (1) and $v\le25$ give
$N\le17$. In (2) put $\ell=\lfloor N/2\rfloor$. Division by its
positive coefficient gives:

| $N$ | 7, 8 | 9, 10 | 11, 12 | 13, 14 | 15, 16 | 17 |
| --- | --- | --- | --- | --- | --- | --- |
| lower bound on $v$ | 70 | 42 | 33 | $143/5$ | 26 | $170/7$ |

All $N\le16$ are excluded. At $N=17$, the incidence inequality in
(1) gives $4v\ge17\cdot6=102$, so $v\ge26$ too. This contradiction
proves the claim. The
[[research/finite_graph_coloring_obstructions/evidence/_index|exact arithmetic checker]]
recomputes this table and the incidence bounds; the counting argument is
what makes those finite palette cases exhaustive.
