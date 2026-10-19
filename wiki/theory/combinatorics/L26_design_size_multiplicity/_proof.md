---
name: theory/combinatorics/L26_design_size_multiplicity/_proof
title: Incidence rank and the available sizes
desc: The incidence matrix gives m>=n, while a point outside a largest block bounds every block size in terms of the minimum.
created: 2026-10-14T12:38:34Z
updated: 2026-10-14T12:38:34Z
---

***

Let $r_x$ count the blocks through point $x$. One has $r_x\ge2$:
if only one block contained $x$, it would contain every other point to
cover every pair involving $x$, contrary to properness. For the
point-by-block incidence matrix $M$,

$$
MM^{\mathsf T}=J+\operatorname{diag}(r_x-1).
$$

The diagonal matrix is positive definite and $J$ is positive semidefinite,
so the matrix has rank $n$. Hence $m\ge n$.

Choose a largest block $B$, of size $b$, and a point $x\notin B$. The
unique blocks through the pairs $\{x,y\}$, $y\in B$, are distinct:
one block containing two such $y$ would share their pair with $B$. Any
two of these $b$ blocks meet only at $x$, again by pair uniqueness. Their
petals each have size at least $a-1$ and fit among the $n-1$ other points.
Therefore $b(a-1)\le n-1$.

If $w$ distinct block sizes occur and each is used at most $C\sqrt n$
times, then $n\le m\le C\sqrt n\,w$, giving
$w\ge\sqrt n/C$.

Finally all sizes lie in $[a,(n-1)/(a-1)]$. Since $b\ge a$, the
inequality also gives $a\le\sqrt n+O(1)$. Under
$a\ge(1-o(1))\sqrt n$, both endpoints of this interval are
$(1+o(1))\sqrt n$, and its length is $o(\sqrt n)$. It contains only
$o(\sqrt n)$ integers, contrary to the lower bound on $w$ for fixed
$C$. This proves precisely the claimed obstruction.
