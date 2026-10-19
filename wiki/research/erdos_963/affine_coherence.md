---
name: research/erdos_963/affine_coherence
title: 'Affine coherence and a universal coherent-support bound'
desc: A proved binary-tree extraction into affine integer-hull vertices, a congruence transfer lemma, and a near-logarithmic bound for coherent dimension.
tags: []
sources: []
created: 2026-09-19T02:53:02Z
updated: 2026-09-19T02:53:02Z
---


# Affine coherence and a universal coherent-support bound

***

These results do not prove the target. They strengthen the available
argument for the parameter $c(P)$ from
[[research/erdos_963/convex_fibers|the convex-fiber note]].

## Affine-coherent extraction

For an integer set $D=\{a_0,\ldots,a_h\}$, call $D$ affine-coherent if
$\mathbf1$ is a vertex of

$$
\operatorname{conv}\{u\in\mathbb Z_{\ge0}^{h+1}:
 \textstyle\sum u_i=h+1,\quad\sum a_i u_i=\sum a_i\}.
$$

This property is hereditary, by fixing the complementary coordinates
at one in any proposed convex decomposition.

**Lemma.** If the differences $a_i-a_0$, $1\le i\le h$, have
distinct $2$-adic valuations, then $D$ is affine-coherent.

In a convex decomposition of $\mathbf1$ into integer fiber points,
write $r=u-\mathbf1$ for each participating point. Then

$$
\sum_i r_i=0,\qquad
\sum_{i=1}^h(a_i-a_0)r_i=0,\qquad r_i\ge-1.
$$

Reduction modulo one power of two beyond the least difference
valuation makes the corresponding coefficient $r_i$ even. It is
therefore nonnegative. Its weighted average over the decomposition
is zero, so it vanishes at every participating point. Repeat with
the next valuation. All nonpivot coefficients vanish, and the degree
equation eliminates the pivot coefficient. The decomposition is trivial.

The binary residue tree used in [[research/erdos_963/proof_sketch|the proof
sketch]] has a path with at least $\lceil\log_2 m\rceil$ branching vertices when
it has $m$ leaves. Taking its pivot and one point in each sibling branch proves

$$
\boxed{c_{\rm aff}(P)\ge\lceil\log_2|P|\rceil+1.}             \tag{1}
$$

This is a statement about affine coherence, not ordinary dissociation.

## Transfer from a congruence class

**Lemma.** Suppose $D$ is a positive affine-coherent set contained
in $a+q\mathbb Z$, where $q\ge2$ and $\gcd(a,q)=1$. If
$|D|\le q+1$, then $D$ is coherent.

Write $k=|D|$. Any nonnegative integral representation of $\sum D$
using $D$ has total degree congruent to $k$ modulo $q$.
If $k\le q+1$, its only possible degrees below $k$ are zero or one.
Neither is possible when $k\ge2$, since $\sum D$ is positive and is
greater than every member of $D$. The singleton case is immediate.
Thus minimum degree exposes the degree-$k$ face of the full fiber.
Affine coherence makes $\mathbf1$ a vertex of that face, hence of
the full fiber.

Consequently, for a nonempty positive integer set $B$ in one unit
class modulo $q$,

$$
\boxed{c(B)\le q\quad\Longrightarrow\quad |B|\le2^{c(B)-1}.}  \tag{2}
$$

Otherwise (1) supplies an affine-coherent $(c(B)+1)$-subset,
and the transfer lemma makes it coherent.

## A universal bound

Let $P$ be a finite positive integer set and $C=c(P)\ge2$. Put

$$
q=2^{\lceil\log_2 C\rceil}.
$$

Order the occupied valuation layers increasingly as $P_1,\ldots,P_r$.
The established coherence extension across successive valuation layers
gives $r\le C$ and $c(P_i)\le C-i+1$.
Scale each layer to odd integers and split it among the $q/2$ odd
classes modulo $q$. Each nonempty class has coherent dimension at
most $C-i+1\le q$, so (2) gives

$$
|P_i|\le(q/2)2^{C-i}.
$$

Summation proves

$$
\boxed{|P|\le
2^{\lceil\log_2 C\rceil-1}(2^C-1).}                         \tag{3}
$$

For $C=1$, the separate exact bound is $|P|=1$.

For an arbitrary real set $A$ with $d=d(A)\ge2$, first use the
established positive integer reduction and then $c(P)\le d$.
The right side of (3) is increasing in $C$. Thus

$$
\boxed{|A|\le 2^{\lceil\log_2 d\rceil}(2^d-1)+1.}          \tag{4}
$$

Combined with the previously proved bound, this gives

$$
|A|\le
\min\{2^{d+\lfloor\log_2(d+1)\rfloor},
       2^{\lceil\log_2 d\rceil}(2^d-1)+1\}.                \tag{5}
$$

This improves the older bound slightly at some dimensions, but still
does not give $|A|<2^{d+1}$.

## Exact limitation

The transfer argument stops at size $q+1$: at larger sizes, degree
two or larger can occur below the affine fiber. No argument controlling
these alternatives across sibling branches of the binary tree has
been proved. A long affine-coherent chain alone cannot suffice, as the
block construction in the proof sketch already shows for dissociation.
