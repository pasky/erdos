---
name: research/erdos_774/lemmas/chain_circuit_box_complexity
title: Chain circuits with unbounded box complexity and one finite coloring
desc: Explicit ternary rational circuits in prime grids need k disjoint product boxes yet admit one 30-color proper coloring; unbounded box complexity alone forces nothing.
tags: [E0774, proved, obstruction]
sources: []
created: 2026-09-24T23:30:00Z
updated: 2026-09-24T23:30:00Z
---

# Chain circuits with unbounded box complexity and one finite coloring

***

This finite algebraic observation complements the
[bounded-box theorem](../routes/partial_box_compression.md), which proves
that every fixed number of disjoint constant-sign product boxes is finitely
colorable. It shows that relations whose box complexity grows without
bound can still all be split by one finite palette. It is not another
candidate counterexample.

## The chain family

Fix distinct odd primes $p_1,\ldots,p_k$, $k\geq2$, and choose
$\alpha_j\in\mu_{p_j}\setminus\{1\}$. In the product grid, put

$$
\begin{aligned}
B_1&=(\mu_{p_1}\setminus\{\alpha_1\})\times\{1\}^{k-1},\\
B_j&=\{\alpha_1\}\times\cdots\times\{\alpha_{j-1}\}
\times(\mu_{p_j}\setminus\{1,\alpha_j\})\times\{1\}^{k-j}
&& (1<j<k),\\
B_k&=\{\alpha_1\}\times\cdots\times\{\alpha_{k-1}\}
\times(\mu_{p_k}\setminus\{1\}).
\end{aligned}
$$

Give $B_j$ coefficient sign $(-1)^{j-1}$. Their disjoint union supports a
ternary rational circuit of size

$$
|B_1\cup\cdots\cup B_k|=2+\sum_{j=1}^k(p_j-2).
\tag{1}
$$

For a direct proof, start with the full $p_1$-cycle. Replace its selected
term $v$ by $-v\sum_{a\in\mu_p\setminus\{1\}}a$ at a fresh prime, and
repeat, selecting the term with the next prescribed $\alpha_j$. This
produces exactly the displayed boxes and signs. It preserves being a
rational circuit: in a relation on the new support, each nonidentity
new-prime layer contains one scalar multiple of $v$. Equal layer sums force
all their coefficients to agree. The identity layer and their common value
then give precisely a relation on the old circuit. The new kernel has
dimension one, and every displayed coefficient is nonzero. Formula (1)
follows by counting the boxes.

## Exactly k boxes are needed

The exact minimum number of product boxes whose union is precisely this
support is $k$, even without requiring constant signs or disjointness. A
box contained in the support cannot meet both $B_j$ and $B_l$, $j<l$: take
the first-departure coordinate from a point of $B_j$ and the nonidentity
$l$-coordinate from a point of $B_l$. The resulting point would also be in
the product box, but its first departure at $j$ is followed by a
nonidentity coordinate and it belongs to none of the $B_i$. Thus at least
one separate box is needed for each $B_j$; the displayed partition attains
that number.

## One finite coloring splits every chain

Nevertheless all these chains admit one finite coloring. Record the
complete symbols in prime coordinates 3 and 5 (when present), and color the
remaining coordinates by the parity of membership in fixed almost-equal
binary parts. Choose each counted part to exclude the default symbol $1$,
so this parity sum is finite on every finite-support tuple. This uses at
most $3\cdot5\cdot2=30$ colors on the finite-support grid. If a chain has
an active small-prime coordinate, its full projection onto that coordinate
already prevents monochromaticity. Otherwise all active primes are at least
7. Its first box contains $p_1-1$ points in one prime fiber, more than
either binary part, so parity splits that box.

Thus (1) coexists with unbounded box complexity and a bounded palette. No
claim that all bounded-excess relations have this form, or have a bounded
coloring, follows. A general bounded-conductor-excess argument, which would
need a singleton-layer or recursive alternative, is not established and is
not imported as a theorem; the elementary chain construction above is
proved directly, without the Conway–Jones reduced-conductor theorem. This
page is author-recorded.
