---
name: problems/integer_sequences/E0954
title: Problem 954
desc: |
  For the sequence with $a_0=0$, $a_1=1$ and each next term the least $n$ for
  which $a_i+a_j\le n$ has fewer than $n$ solutions, asks whether the number of
  solutions of $a_i+a_j\le x$ is $x+O(x^{1/4+o(1)})$.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 954

[[problems/integer_sequences/_index|..]]

***

**Statement.** Let $0=a_0<a_1<a_2<\cdots$ be the sequence of integers defined by
$a_0=0$ and $a_1=1$, and $a_{k+1}$ is the smallest integer $n$ for which the
number of solutions to $a_i+a_j \leq n$ (with $0\leq i\leq j\leq k$ and $j\geq
1$) is $<n$.

Is the number of solutions to $a_i+a_j \leq x$ equal to $x+O(x^{1/4+o(1)})$?

**Status.** Open.

**Source.** [erdosproblems.com/954](https://www.erdosproblems.com/954), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #954,
https://www.erdosproblems.com/954.

**Formalization.** None recorded.

## Current assessment

[[research/rosen_greedy_sequence/_index|Rosen greedy-sequence invariants]] gives
the complete author-recorded argument and its remaining gap. For every integer
n, R(n)>=n, with equality at each selected positive integer. If b(n) counts
unordered representations n=x+y with positive earlier selected x,y, then
H(n)=R(n)-n satisfies H(n)=max(0,H(n-1)+b(n)-1); n is selected exactly when
H(n-1)+b(n)=0. The source of b(n) is still the entire growing history. The exact
recurrence does not bound its state space or its excess at the target scale.
