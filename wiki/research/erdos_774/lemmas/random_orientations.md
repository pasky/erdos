---
name: research/erdos_774/lemmas/random_orientations
title: Independent orientations collapse planted labels
desc: An exact probability bound shows why a dense planted relation family needs correlated signs to admit distinct labels.
tags: [E0774, proved, probabilistic]
sources: []
created: 2026-09-17T23:53:25Z
updated: 2026-09-17T23:53:25Z
---


# Independent orientations collapse planted labels

***

## Theorem — proved

Fix arbitrary supports $E_1,\ldots,E_m\subseteq[n]$, each of size
$k\geq3$. Independently on every support choose uniformly exactly $h$
positive and $k-h$ negative signs, where $1\leq h<k$. Let $V$ be
the rational span of these signed rows. Set

$$
\rho=\frac1{\max(h,k-h)+1}\leq\frac13.
$$

Then

$$
\mathbb P(e_i-e_j\notin V\text{ for all }i\ne j)
\leq\sum_{r=0}^{n-1}\binom mr\rho^{m-r}. \tag{1}
$$

At $m=3n$, the right side is at most $n(e/3)^n$, which tends to zero.
The same estimate with $\rho=1/3$ permits different support sizes and
numbers of positive signs, provided every size is at least three and both
signs occur.

### Proof

Fix a subspace $W$ containing no coordinate difference. On one support,
the $h$-sets of positive positions whose signed row lies in $W$ cannot
differ by swapping one element: subtracting their rows would put
$2(e_i-e_j)$ in $W$. Their $(h-1)$-subsets are therefore disjoint
between different members, giving relative density at most
$1/(k-h+1)$. Counting $(h+1)$-supersets instead gives density at most
$1/(h+1)$. Thus a fresh row belongs to $W$ with probability at most
$\rho$.

If the final span avoids coordinate differences, its rank is $r<n$. Choose
$r$ sampled rows forming a basis. Conditional on any specified candidate
basis whose span has the required avoidance, the other $m-r$ rows all
belong to that span with probability at most $\rho^{m-r}$. Summing over
candidate bases and ranks proves (1). For $m=3n$, bound each of the $n$
terms by $\binom{3n}{n}3^{-2n}\leq(e/3)^n$.

## Consequence for construction

Any realization satisfying all planted relations has equal labels at indices
$i,j$ if $e_i-e_j\in V$. Thus independently orienting $3n$ or more
relations is typically incompatible with distinct labels, including for
balanced orientations. A nonzero quotient alone does not guarantee a usable
configuration.

This does **not** exclude rare conditioning or correlated orientations. Those
are the remaining possibilities for this planting mechanism, and their full
signed closure must still satisfy uniform extraction.
