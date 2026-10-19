---
name: diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_3_4
title: Ulas Theorem 3.4 — infinitely many non-solutions for every n
desc: >
  For every n >= 0, infinitely many k fail k(k-1)...(k-n) | C(2k, k): each
  power of 2 that is at least 4 and exceeds n + 1 violates the digit-sum
  criterion at 2.
created: 2026-10-14T23:03:05Z
updated: 2026-10-14T23:03:05Z
---

***

**Source.** Published p. 593, Theorem 3.4; proof p. 594.

**Statement.** For every integer $n\ge0$, infinitely many positive integers
$k$ lie outside $Z_n$, the set defined on
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_3_1|Theorem 3.1]];
the print says that $\mathbb N_+\setminus Z_n$ is infinite. At $n=0$:
infinitely many $k$ do not divide $\binom{2k}{k}$.

**Proof sketch.** Take $k=2^m$ with $m\ge2$ and $2^m>n+1$. The prime $2$
divides $k$, and $3s_2(k)-s_2(2k)-s_2(k-n-1)=2-s_2(2^m-n-1)$. This is less
than $n+1$: for $n=0$ because $s_2(2^m-1)=m\ge2$, and for $n\ge1$ because
$s_2(2^m-n-1)\ge1$. So Theorem 3.1 puts $2^m$ outside $Z_n$. The print also
treats each base $p\ge3$ with $k=p^m$, which the conclusion does not need.

**Dependencies.**
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_3_1|Theorem 3.1]].

**Read depth.** Claims checked: the statement was read clause by clause on
the page image, and the proof was followed. Nothing here is independently
reviewed.

**Bears on.** [[../wiki/problems/factorials_binomials/E0396/_index|#396]]:
for each $k$ of the problem, infinitely many $n$ fail, so no $k$ has the
divisibility for every large $n$; the problem asks for a single $n$.
