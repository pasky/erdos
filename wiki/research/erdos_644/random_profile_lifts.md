---
name: research/erdos_644/random_profile_lifts
desc: Convex profiles of a fixed local-two-cover seed have uniformly exponentially few bad random lifted tuples; the resulting alteration criterion still loses at the Fano entropy threshold.
tags: [proved, conditional, amplification, limitations]
sources: []
created: 2026-09-23T05:27:00Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/random_profile_lifts

***

This gives a probabilistic counterpart to
[Convex profile amplification](convex_profile_amplification.md). It does not
provide an unrestricted amplifier or prove convergence of $f(k,r)/k$.

## Uniform exponential bound

Let $\mathcal H$ be a finite nonempty $P_r$ family of nonempty sets on $n$
points, where $r\ge3$, and put

$$
P=\operatorname{conv}\{\mathbf1_E:E\in\mathcal H\}.
$$

Replace each point by a block of $L$ points. For prescribed profiles
$p^{(1)},\ldots,p^{(r)}\in P$ with integral $Lp^{(j)}$, independently realize
each row by uniformly choosing $Lp^{(j)}_v$ points in block $v$, independently
between blocks. With $\delta=1/(n+1)$,

$$
\Pr(\text{the rows have no two-cover})
\le2(L+1)^{r-1}(1-\delta^{r-1})^L.
\tag{1}
$$


Caratheodory's theorem expresses each profile using at most $n+1$ seed edges.
Some edge $E_j$ has coefficient at least $\delta$, so $p^{(j)}_v\ge\delta$ on
$E_j$. A seed two-cover partitions the rows into two nonempty groups of sizes at
most $r-1$, with a designated point common to each group's seed edges. If one
seed point covers every row, split the rows into groups of sizes $r-1$ and one
using the same designated block.

For $s$ independent uniform subsets of an $L$-point block, of integral densities
$p_i\ge\delta$, the probability of empty common intersection is at most

$$
(L+1)^s(1-\textstyle\prod_i p_i)^L
\le (L+1)^s(1-\delta^s)^L.
$$

Indeed, first use independent Bernoulli subsets. Their intersection is empty
with probability $(1-\prod_i p_i)^L$. Conditioning each cardinality on its
integral mean gives the uniform model. That cardinality is a mode of its
binomial distribution, and has probability at least $1/(L+1)$. Dividing by the
conditioning probability proves the bound. Apply this to the two designated
groups and take a union bound to prove (1). The same proof handles any number of
rows from two through $r$.

## A sufficient alteration inequality

Suppose, more generally, that $e^{o(L)}$ allowed profiles on $nL$ points satisfy
the following uniform estimates, for constants $s>0$, $B\ge0$, and $I>0$:

- every point set of size at most $sL$ is avoided by a random realization of
  some profile with probability at least $e^{-(B+o(1))L}$;
- independently sampled realizations of any prescribed $r$ profiles form a bad
  tuple with probability at most $e^{-(I-o(1))L}$.

If

$$
I>rB,
\tag{2}
$$

there are $P_r$ lifted families with transversal number greater than
$\lfloor sL\rfloor$ for all sufficiently large $L$.

Choose $B<\alpha<(I-B)/(r-1)$ and sample $\lceil e^{\alpha L}\rceil$ rows per
profile. For each candidate transversal, its designated profile supplies at
least $e^{(\alpha-B-o(1))L}$ avoiding rows, simultaneously for all candidates:
Chernoff's inequality gives a doubly exponential failure estimate, which beats
their number $2^{nL}$. Meanwhile the expected number of bad $r$-tuples of
distinct sample positions is at most $e^{(r\alpha-I+o(1))L}$. Markov's
inequality, with any sufficiently small fixed exponential slack, bounds their
number by less than the preceding avoidance count. Delete every sampled row
participating in a bad tuple. The strict inequality $r\alpha-I<\alpha-B$ ensures
that each candidate transversal still misses a row. A smaller bad subfamily
among the remaining rows would extend to a bad $r$-tuple, since the surviving
transversal number tends to infinity. Removing duplicate rows is harmless.

## Why this is not yet an amplifier

The positive rate in (1) need not satisfy (2) at the desired transversal scale.
At the ideal homogeneous Fano boundary $p=4/7$, deleting $3L/7$ points in each
of $n$ blocks gives avoidance exponent

$$
B=n h(4/7),\qquad h(u)=-u\log u-(1-u)\log(1-u).
$$

For $7\mid L$, balanced assignments of the seven Fano caps in every block give
bad tuples with exponent

$$
I\le n\bigl(7h(4/7)-\log7\bigr)<7B.
$$

This calculation concerns the limiting homogeneous model, not a claim that a
particular fixed $P_7$ seed contains that exact boundary profile. It shows why
uniform exponential rarity alone does not recover the boundary coefficient by
this alteration argument. It is consistent with the separate
[Bernoulli thinning obstruction](random_thinning_obstruction.md), and does not
exclude more structured sampling or deletion methods.
