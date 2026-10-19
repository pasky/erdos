---
name: diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_2_7
title: Ulas Theorem 2.7 — infinitely many non-solutions for every n
desc: >
  For every positive n, infinitely many k fail the Erdős–Straus divisibility:
  k = 2p^m - n, with p a prime above n and at least 5, violates the digit-sum
  criterion at p.
created: 2026-10-14T23:03:05Z
updated: 2026-10-14T23:03:05Z
---

***

**Source.** Published p. 589, Theorem 2.7, with its proof.

**Statement.** For every positive integer $n$, infinitely many positive
integers $k$ lie outside $S_n$, the set defined on
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_2_1|Theorem 2.1]];
that is, $(n+1)\cdots(n+k)$ does not divide $(n+k+1)\cdots(n+2k)$. The print
says that $\mathbb N\setminus S_n$ is infinite.

**Proof sketch.** Fix a prime $p\ge5$ with $p>n$ and an integer $m\ge2$, and
put $k=2p^m-n$, so that $k\ge1$ and $p$ divides $k+n=2p^m$. Then
$s_p(k+n)=2$, $s_p(n)=n$, and the base-$p$ expansion

$$
4p^m-n=3p^m+(p-1)(p^{m-1}+\cdots+p)+(p-n)
$$

gives $s_p(2k+n)=3+(m-1)(p-1)+p-n$. Hence
$2s_p(k+n)-s_p(2k+n)-s_p(n)=1-(m-1)(p-1)-p<0$, and Theorem 2.1 puts $k$
outside $S_n$. Each $m\ge2$ gives a different $k$.

**Source note.** The print evaluates the last expression as
$-1-(m-1)(p-1)-p$; it is $1-(m-1)(p-1)-p$, still negative. The print allows
any prime $p>n$, but the expansion needs $p\ge5$: for $p=3$ the leading digit
$3$ is not a base-$3$ digit, and for $p=2$ one has $s_2(2^{m+1})=1$.
Infinitely many primes remain, so the theorem is unaffected.

**Dependencies.**
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_2_1|Theorem 2.1]].

**Read depth.** Claims checked: the statement was read clause by clause on
the page image, and the proof was followed. Nothing here is independently
reviewed.

**Bears on.** [[../wiki/problems/diophantine_problems/E0389/_index|#389]]:
for each $n\ge2$ of the problem, infinitely many $k$ fail, so no such $n$ has
the divisibility for every large $k$. The problem asks for a single $k$, and
at its $n=1$ every $k$ works.
