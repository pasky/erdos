---
name: theory/number_theory/L35_divisor_prefix_compression/_proof
title: Exact reduction from integers to distinct-part partitions
desc: Taking the least common multiple preserves a divisor prefix, making exhaustive minimization finite for each target sum.
created: 2026-10-14T18:42:37Z
updated: 2026-10-14T18:42:37Z
---

***

Suppose the divisors of $n$ greater than $1$ begin
$d_1<\cdots<d_k$, with sum $N$. Put $L=\operatorname{lcm}(d_1,\ldots,d_k)$.
Then $L\mid n$, so $L\le n$. Every $d_i$ divides $L$. Conversely,
if $2\le e\le d_k$ divides $L$, it divides $n$ and hence is one
of the $d_i$, since these are the entire prefix through $d_k$.
Thus $L$ has precisely the same divisor prefix.

Every original witness therefore gives a partition $P$ of $N$ into
distinct integers at least $2$ such that the divisors of
$\operatorname{lcm}(P)$ up to $\max(P)$ are exactly $P$, and gives
such a witness of size no larger than the original integer. Conversely,
any partition passing this test realizes its sum as a divisor prefix
of $\operatorname{lcm}(P)$. Taking minima proves the formula, including
the convention that an empty family means no witness exists. Every
part is at most $N$, so each candidate least common multiple divides
$\operatorname{lcm}(1,\ldots,N)$; there are finitely many partitions.

The [checker](evidence/main.py) enumerates all increasing distinct-part
partitions of each $N$ in $[2,64]$. It verifies partition validity,
uniqueness and counts against a separate subset-sum dynamic program,
tests the exact divisor-prefix predicate, and minimizes the candidate
least common multiples. The [retained table](evidence/assets/values.json)
contains every minimum and one corresponding prefix. A separate divisor
sieve for $n\le10000$ crosschecks all the attained minima; completeness
over all $n$ comes from the reduction, not from this sieve bound.

There are 83,691 tested partitions. Only $N=4$ has no valid prefix.
The largest minimum is $f(58)=265$, with prefix $(5,53)$, whose least
common multiple is $265$. The boundary values are
$f(2)=2$, $f(3)=3$, $f(5)=5$ and $f(6)=4$.
These exact finite conclusions are the whole computational scope.
