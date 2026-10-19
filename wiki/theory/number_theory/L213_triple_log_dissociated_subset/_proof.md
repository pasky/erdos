---
name: theory/number_theory/L213_triple_log_dissociated_subset/_proof
title: Dyadic blocks, doubling chains and a weighted pigeonhole
desc: The bounded-ratio bound L212 in each dyadic block of the absolute values, a doubling chain from alternate blocks above the chosen one, and a weighted choice of that block.
created: 2026-10-15T18:14:21Z
updated: 2026-10-15T18:14:21Z
---

# Dyadic blocks, doubling chains and a weighted pigeonhole

***

This proves
[[theory/number_theory/L213_triple_log_dissociated_subset/_index|L213]].
Write $d(X)$ for the largest size of a dissociated subset of a finite set
$X$ of reals.

## Step 1: symmetric reduction and blocks

Let $P=\{|x|:x\in A,\ x\ne0\}$ and $N=|P|$. Changing individual signs
preserves dissociation by reversing the corresponding ternary coefficients,
and a dissociated set contains neither
$0$ nor two opposite elements, so $d(P)=d(A)$; also $N\ge(n-1)/2\ge2$ for
$n\ge5$. Let $m=\min P$ and, for integers $k\ge0$,

$$
P_k=P\cap[2^km,2^{k+1}m).
$$

These blocks partition $P$, and each satisfies $\max P_k<2\min P_k$. Let
$k_1<\cdots<k_B$ be the indices of the nonempty blocks and $n_i=|P_{k_i}|$,
so $\sum_in_i=N$.

## Step 2: one block and a doubling chain

Fix $i$. By
[[theory/number_theory/L212_bounded_ratio_dissociated_subset/_index|L212]]
and $d\ge1$, the block $P_{k_i}$ has a dissociated subset $D_i$ of size

$$
\tau_i=\max\bigl(1,\lfloor\log_2n_i-\log_2 3\rfloor+1\bigr)
>\log_2n_i-\log_2 3 .
$$

Since $\tau_i\le\max(1,\log_2N-\log_2 3+1)\le\log_2N$, we have
$\lceil\log_2\tau_i\rceil\le\lambda:=\lceil\log_2\log_2N\rceil$.

**Doubling chains.** If $D\subseteq P$ is dissociated and
$z_1<\cdots<z_r$ in $P\setminus D$ satisfy $z_1>\sum D$ and
$z_{j+1}>2z_j$, then $D\cup\{z_1,\ldots,z_r\}$ is dissociated. Indeed, by
induction $\sum D+\sum_{j<t}z_j<z_t$ for every $t$. In a ternary relation
on the union, let $t$ be the largest index with a nonzero coefficient on
$z_t$; then $z_t$ is at most the sum of all the other elements, which is
impossible. So no $z_j$ occurs, and the relation lies in $D$, where it is
trivial.

List in increasing order the nonempty blocks with index at least
$k_i+1+\lceil\log_2\tau_i\rceil$, as $\kappa_1<\kappa_2<\cdots$, and take
one element $z_j$ from block $\kappa_{2j-1}$ for each $j$. Every element
of $D_i$ is below $2^{k_i+1}m$, so
$\sum D_i<\tau_i2^{k_i+1}m\le2^{\kappa_1}m\le z_1$, and
$z_{j+1}\ge2^{\kappa_{2j+1}}m\ge2^{\kappa_{2j-1}+2}m>2z_j$. Among the
$B-i$ nonempty blocks after $k_i$, at most $\lceil\log_2\tau_i\rceil\le\lambda$
have an index in $(k_i,k_i+\lceil\log_2\tau_i\rceil]$, so the chain has at
least $\tfrac12(B-i-\lambda)_+$ elements. Hence, for every $i$,

$$
d(P)\ \ge\ \log_2n_i-\log_2 3+\tfrac12(B-i-\lambda)_+ .
\tag{1}
$$

## Step 3: weighted pigeonhole

Put $w_i=2^{-(B-i-\lambda)_+/2}$. At most $\lambda+1$ indices have
$B-i-\lambda\le0$, and the other indices give distinct exponents
$t=B-i-\lambda\ge1$, so

$$
W=\sum_{i=1}^Bw_i\le\lambda+1+\sum_{t\ge1}2^{-t/2}=\lambda+2+\sqrt2 .
$$

If $n_i<Nw_i/W$ held for every $i$, summing would give $N<N$. So some $i$
has $\log_2n_i\ge\log_2N-\log_2W-\tfrac12(B-i-\lambda)_+$, and (1) gives

$$
d(A)=d(P)\ \ge\ \log_2N-\log_2(\lambda+2+\sqrt2)-\log_2 3 .
$$

Finally $\log_2N\ge\log_2(n-1)-1$ and
$\lambda\le\lceil\log_2\log_2n\rceil$, which is the displayed bound of the
statement.

## Step 4: the simplified form

Let $n\ge2^{16}$ and $y=\log_2\log_2n\ge4$. Since $\sqrt2<3/2$,
we have $\lceil y\rceil+2+\sqrt2<y+9/2\le(9/4)y$.
Since $n\ge16$ also gives $n-1\ge15n/16$, this yields

$$
d(A)>\log_2n-\log_2y-\log_2(72/5)
>\log_2n-\log_2\log_2\log_2n-4 .
\qquad\square
$$

## Scope

The argument uses one block's dissociated subset and single elements from
other blocks. It never combines dissociated subsets from two blocks within
a factor of order $\log_2n$ of each other, and that is the whole source of
the $\log_2\log_2\log_2n$ loss: a set spread with equal counts over about
$\log_2\log_2n$ consecutive dyadic blocks is the case it handles worst.
