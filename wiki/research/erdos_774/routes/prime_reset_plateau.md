---
name: research/erdos_774/routes/prime_reset_plateau
title: The prime-grid reset and the three-color plateau
desc: Root-span coverage resets maximally at S3 times S5 times S7, whose separation threshold is 3 or 4; ordinary coloring stays exactly three through prime 19.
tags: [E0774, proved, tensor, obstruction]
sources: []
created: 2026-09-18T01:56:00Z
updated: 2026-09-18T01:56:00Z
---


# The prime-grid reset and the three-color plateau

***

## Standing

The maximal [root-coverage reset](tensor_holes.md) occurs inside the actual
distinct-prime family, already at its first proved jump. Thus restricting to
prime side sizes does not supply the missing restart. There is also an exact
three-color plateau and a sharper separation bound:

$$
\alpha_3(S_3\otimes S_5\otimes S_7)=2/3,
\qquad 3\leq\tau_3(S_3\otimes S_5\otimes S_7)\leq4.
$$

Neither statement proves the
[unbounded coloring obligation](../proof_sketch.md). All algebra below is
author-recorded; a separate reviewer checked it.

## 1. An exact root-closed partition at the prime jump

On $B=S_3\otimes S_5$, index rows by $r=0,1,2$, columns by
$j=0,\ldots,4$, and use $f(r,j)=r+j\pmod3$. Its classes are

$$
\begin{aligned}
C_0&=\{(0,0),(0,3),(1,2),(2,1),(2,4)\},\\
C_1&=\{(0,1),(0,4),(1,0),(1,3),(2,2)\},\\
C_2&=\{(0,2),(1,1),(1,4),(2,0),(2,3)\}.
\end{aligned}
$$

Each class is rationally independent and rational-root-closed:
$B\cap\operatorname{span}_{\mathbb Q}C_c=C_c$. Its complement graph
in $K_{3,5}$ is connected and bridgeless: suppressing the five degree-two
right vertices gives a triangle with edge multiplicities $(2,2,1)$.
The [proved cographic criterion](../evidence/tensor_layers/_index.md) applies.

In coordinates $(x_{11},x_{12},x_{13},x_{14},x_{21},x_{22},x_{23},x_{24})$,
the three spans have equations

$$
\begin{array}{ll}
C_0:&x_{21}=x_{13},\quad x_{22}=x_{12},\quad x_{24}=x_{13},\\
C_1:&x_{14}=x_{11},\quad x_{22}=0,\quad x_{23}=x_{13}-x_{11},\\
C_2:&x_{12}=0,\quad x_{23}=x_{21}-x_{11},\quad
 x_{24}=x_{14}+x_{21}-x_{11}.
\end{array}
$$

Each pair of spans has exactly the same intersection

$$
U=\{(a-b,0,a,a-b,a,0,b,a):a,b\in\mathbb Q\}.
$$

Let $T$ exchange columns $j=3,4$. On each row of four standard
coordinates it sends $(x_1,x_2,x_3,x_4)$ to
$(x_1-x_4,x_2-x_4,x_3-x_4,-x_4)$. Thus

$$
T(U)=\{(0,b-a,b,b-a,0,-a,b-a,-a):a,b\in\mathbb Q\},
\qquad U\cap T(U)=\{0\}.
$$

Coordinates $12$ and $22$ prove the last assertion immediately.

Use six layer types in $B\otimes S_m$: the three cyclic relabelings
of $f$, and the three cyclic relabelings of its $T$-image. For
$m\geq6$, fill additional layers by repetitions. For any fixed color,
deleting any single layer leaves at least two distinct original class types
and two distinct transformed types. The remaining rational-span intersection
is contained in $U\cap T(U)=0$.

The rational version of the [layer criterion](tensor_coloring.md) makes every
resulting color class $D_c$ independent. Moreover a root $b\otimes s_j$
can belong to $\operatorname{span}D_c$ only if there is a common sum
$u$ in all the other layer spans, with $u+b$ in layer $j$.
This forces $u=0$, and base root closure forces that root to have
color $c$. Therefore

$$
(B\otimes S_m)\cap\operatorname{span}_{\mathbb Q}D_c=D_c.
$$

At $m=7$, all three classes have 35 points and each root is omitted
from exactly the other two colors' signed spans. Hence $\alpha_3=2/3$,
the maximum allowed by its definition. The same witness works for arbitrary
nonnegative weights on roots. The existing exact bound
$\chi(B\otimes S_7)=3$ makes this a genuine postjump reset.

## 2. Rational thresholds and an ordinary plateau

For a finite transitive indexed vector configuration of $N$ columns and
rank $d$, averaging a basis over the transitive group gives
$\operatorname{rank}F\geq d|F|/N$ for every subfamily $F$.
Rado--Horn therefore proves

$$
\chi_{\mathbb Q\text{-ind}}(E)=\lceil N/d\rceil.
$$

The precise indexed-list statement was checked in
[Lewko, Theorem 4.1](../../../../library/analysis/lewko_2026_sidon_decomposition_problem_abelian_groups_bounded_torsion/_index.md),
after its digest. Its necessity follows just by summing color-class ranks. For
$q>N/d$, the rational separation threshold (independent layers, zero
intersection of their rational spans) is consequently

$$
\tau_q^{\mathbb Q}(E)=
\left\lceil\frac q{q-N/d}\right\rceil.
$$

Indeed $E\otimes S_p$ has density $Np/[d(p-1)]$; it has a rational
$q$-coloring exactly when this is at most $q$, which rearranges to
the displayed inequality. The rational layer criterion identifies this with
the stated separation parameter. Indexed size-two simplexes are allowed in
this rational statement.

For $Y=S_3\otimes S_5\otimes S_7$, $N/d=35/16$, so
$\tau_3^{\mathbb Q}(Y)=\lceil48/13\rceil=4$. Rational separation
is also ordinary signed separation. The already proved lower bound
$\chi(Y)=3\Rightarrow\tau_3(Y)\geq3$ gives $3\leq\tau_3(Y)\leq4$.

Every full odd-prime prefix ending between 7 and 19 inclusive has ordinary
dissociated chromatic number exactly three: it contains $Y$, while its
rational density is below three.

| Last prime | Rational density $N/d$ |
|---|---:|
| 7 | $35/16$ |
| 11 | $77/32$ |
| 13 | $1001/384$ |
| 17 | $17017/6144$ |
| 19 | $323323/110592$ |
| 23 | $676039/221184>3$ |

At 23 only $3\leq\chi_{\rm diss}\leq4$ follows here. A rational
chromatic jump does not prove an ordinary one.

## 3. Cyclic fiber colorings have a nonzero common signed sum

There is an algebraic reason that cyclic relabelings of the entire reset
partition do not witness $\tau_3(Y)=3$.

Let $T\ne\varnothing$ be a finite vector set with $\sum_{t\in T}t=0$,
partition it as $A_0\sqcup A_1\sqcup A_2$, and put
$\sigma_a=\sum_{t\in A_a}t$. For $S_3=\{s_0,s_1,s_2\}$, define

$$
D_c=\bigcup_{a=0}^2 s_{a+c}\otimes A_a\quad(c=0,1,2),
$$

with indices modulo three. If these indexed classes are dissociated, then
not all $\sigma_a$ vanish: a nonempty group with sum zero would already
give a monochromatic signed relation. The nonzero vector
$u=s_1\otimes\sigma_0-s_0\otimes\sigma_2$ satisfies

$$
\begin{aligned}
u&=-s_1\otimes\sigma_1+s_2\otimes\sigma_2\in\Sigma(D_0),\\
u&= s_1\otimes\sigma_0-s_0\otimes\sigma_2\in\Sigma(D_1),\\
u&=-s_2\otimes\sigma_0+s_0\otimes\sigma_1\in\Sigma(D_2).
\end{aligned}
$$

The identities use $s_0+s_1+s_2=0$ and $\sigma_0+\sigma_1+\sigma_2=0$.
If $u=0$, independence of $s_0,s_1$ forces all three $\sigma_a=0$,
a contradiction. All coefficients expand as $\pm1$ on disjoint groups.

The reset partition is of this form on its $S_3$-fibers, with
$T=S_5\otimes S_7$. Three cyclic relabelings of any such partition
cannot have zero common signed spans. This does not exclude three unrelated
witness colorings, or arbitrary fiber permutations.

## Finite discovery and the stopped test

The reset discovery checked at most the 120 permutations of the five base
columns and stopped at permutation 2, using exact rational arithmetic. The
displayed coordinate proof supersedes that search.

A separate [fixed common-span checker](../evidence/prime_reset_span/_index.md)
constructs only the displayed seven-layer partition and its $96\times105$
equality matrix. It reported class sizes $(35,35,35)$, rank 83 and
nullity 22. Its declared gate allowed ternary enumeration only at nullity at
most 12, so **no ternary enumeration ran**. The algebraic cyclic-sum lemma
above supersedes that unsuccessful route; no zero-intersection conclusion is
drawn from the stopped computation.
