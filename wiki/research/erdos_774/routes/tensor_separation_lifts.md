---
name: research/erdos_774/routes/tensor_separation_lifts
title: Finite and coefficient-bounded separation lifts
desc: Exact constructions bound separation thresholds after large tensor factors, identifying coefficient doubling and a coarse fixed-base saturation bound.
tags: [E0774, proved, tensor, reduction]
sources: []
created: 2026-09-18T00:44:00Z
updated: 2026-09-18T00:44:00Z
---


# Finite and coefficient-bounded separation lifts

***

These proved upper bounds complement the necessary lower bounds from
[root coverage](tensor_holes.md). They do not settle the unbounded-coloring
obligation for the [prime tensors](prime_tensor_extraction.md).

## Coefficient-sensitive threshold

For an integer $h\geq1$, put
$\Sigma_h(C)=\{\sum_{b\in C}n_bb: n_b\in\mathbb Z,\ |n_b|\leq h\}$.
Define $\tau_{q,h}(B)$ by the same proper $q$-colorings as
$\tau_q$, but requiring zero intersections of their colorwise
$\Sigma_h$ sets. Properness still means ordinary full dissociation,
not $h$-degree independence. Thus $\tau_{q,1}=\tau_q$.

If $t=\tau_{q,2h}(B)<\infty$, then for every integer $s\geq1$,

$$
p\geq t\left\lceil\frac{t+s-1}{s}\right\rceil
\quad\Longrightarrow\quad
\tau_{q,h}(B\otimes S_p)\leq t+s. \tag{1}
$$

In particular $p\geq2t$ gives the bound $2t-1$, by taking
$s=t-1$, and $p\geq t^2$ gives the bound $t+1$.
For a nonempty base a finite threshold has $t\geq2$, so these are valid
simplex sizes.

### Proof

Fix $t$ base witness colorings. Use $t+s$ rows, which will be
colorings of the new tensor, and distinguish row zero. Partition the other
rows into groups of size at most $s$. For every group $G$ and every
witness type $i$, make one layer: assign type $i$ to row zero and
all rows in $G$, and assign the other rows so every other witness type
occurs. There are at least $t-1$ such rows, so this is possible. Fill
any extra layers by repetition.

Every row encounters all witness types, making its colorwise layer
intersections zero and hence giving a proper tensor coloring. Every layer
also contains every type among its rows.

Fix a color and a vector $y$ in all rowwise $\Sigma_h$ sets. Choose
its layer sums $u_{a,j}$ in row $a$. Comparing its representation
with row zero shows $u_{a,j}-u_{0,j}=z_a$, independent of $j$.
On the layers associated with the group containing $a$, both rows have
the same base class of type $i$. Thus
$z_a\in\Sigma_{2h}(C_i)$ for every type $i$, and $z_a=0$.
Now every layer has a common sum belonging to all types' $\Sigma_h$,
so that sum is zero and $y=0$. This proves (1).

The coefficient doubling is a real hypothesis of this proof: ordinary
$\tau_q(B)$ does not provide the needed intersections of difference
sets. No fixed-degree extraction statement fills this gap.

## A coarse saturation bound for a fixed base

There is also an ordinary-threshold bound without a higher-coefficient
assumption, though it is extremely large. Let $t=\tau_q(B)<\infty$,
$d=|\Sigma(B)-\Sigma(B)|$, and $r=d(t-1)+1$. Let $M$ be the
number of surjections $[r]\to[t]$. Then

$$
m\geq M\quad\Longrightarrow\quad
\tau_q(B\otimes S_m)\leq r. \tag{2}
$$

Construct $r$ colorings using as layers all surjections into a fixed
$t$-witness family; repeat layers for larger $m$. Every row contains
all witness types and is therefore proper.

For a vector common to a fixed color's signed spans, compare all layer
representations to a reference row. Their differences are row shifts
$z_a$, each in the finite set $\Sigma(B)-\Sigma(B)$. At least
$t$ shifts coincide. If some row has a different shift, choose a
surjection layer assigning all $t$ types to the equal-shift rows. Their
common layer value is forced to zero. Assign to the exceptional row a type
whose signed span excludes the nonzero shift difference; one exists by the
witness property. This is a contradiction. Hence all shifts are equal;
surjectivity of each layer then makes every layer sum zero. This proves (2).

Thus for any fixed base with finite $\tau_q$, sending a single new side
size to infinity does not make its subsequent threshold unbounded. The bound
depends strongly on the base; it does not rule out growth along changing bases.
