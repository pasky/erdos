---
name: research/rosen_greedy_sequence
title: Rosen greedy-sequence invariants
desc: |
  The exact surplus recurrence and indefinite existence of Rosen’s greedy sequence, with the unresolved excursion bound stated explicitly.
tags: []
sources: []
problems: [954]
created: 2026-10-14T20:10:13Z
updated: 2026-10-14T20:10:13Z
---

# Rosen greedy-sequence invariants

[[research/_index|..]]

***

This note concerns [[problems/integer_sequences/E0954/_index|Problem 954]] and
preserves the exact scope of its remaining question.

These author-recorded arguments and source-fit limitations are by Plasma AI.
They do not confer independent verification or resolve the remaining
erdosproblems.com question.

Preserve the pair convention:
$a_0=0$, positive $a_1,a_2,\ldots$, $i\le j$, $j\ge1$.
Let $R(n)$ count such unordered pairs of sum at most integer $n$
in the full sequence, $H(n)=R(n)-n$, $H(0)=0$.
Let $b(n)$ count unordered pairs of positive earlier selected terms
whose sum is exactly $n$. Then
$$
 H(n)=\max\{0,H(n-1)+b(n)-1\},                      \tag{1}
$$
and $n$ is selected exactly when $H(n-1)+b(n)=0$.

Before deciding $n$, terms greater than $n$ are irrelevant. Assuming $R(n-1)\ge
n-1$, the old count at $n$ is $R(n-1)+b(n)\ge n-1$, deficient exactly when equal
to $n-1$. Adjoining $n$ then adds only the pair $(0,n)$, making the count $n$.
Otherwise $n$ is not selected and the count is already at least $n$. This
increasing scan is exactly the least-deficit greedy rule. The base case selects
1 because $b(1)=0$. Induction proves (1), $H(n)\ge0$, and $R(a_k)=a_k$. For real
$x$, replacing $x$ by $\lfloor x\rfloor$ changes the comparison with $x$ by less
than 1.

After $k$ positive terms, the finite prefix has
$k+k(k+1)/2=k(k+3)/2$ allowable pairs in total.
One more than that total is certainly deficient, whereas the invariant
excludes a deficit at or before the last selected term. Consequently
the next term always exists and
$$
 a_{k+1}\le k(k+3)/2+1,\qquad a_k\le k(k+1)/2.
$$
This proves indefinite existence, not the requested surplus bound.

The [erdosproblems.com commentary](https://www.erdosproblems.com/954) was read to identify
Rosen's sequence and the elementary lower count as already known. Equation (1)
still depends on the entire pair-arrival history through $b(n)$. Nonnegativity
and resets do not prove $H(n)=O(n^{1/4+o(1)})$ or bounded memory.

The unresolved obligation is to bound the convolution-driven excess H(n) at
exponent 1/4+o(1), or supply a genuinely closed bounded state invariant. A
useful test is to try an explicit deterministic bound on b(n) or on its interval
sums using the equality R(a_k)=a_k; reject any argument treating H alone as
Markov. Stop at a growing pending-sum table, empirical cycles, or an unproved
finite state-space bound.
