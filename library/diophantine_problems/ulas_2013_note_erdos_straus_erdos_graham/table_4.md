---
name: diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/table_4
title: Ulas Table 4 — least solutions of the Erdős–Graham divisibility for n up to 9
desc: >
  The least k > n with k(k-1)...(k-n) | C(2k, k) for n <= 9, from a search up
  to 2^30; the rows n = 2 to 9 are Problem 396's least witnesses for its
  k = 2 to 9, and the rows n = 0 and 1 are not least.
created: 2026-10-14T23:03:05Z
updated: 2026-10-14T23:03:05Z
---

***

**Source.** Published p. 593, Table 4; the search is described on pp. 592,
594 and 595.

**Statement.** Table 4, headed as the smallest element $z_n$ of $Z_n$ with
its factorization, with $Z_n$ the set defined on
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_3_1|Theorem 3.1]],
lists for $0\le n\le9$:

| Paper's $n$ (Problem 396's $k$) | $z_n$ as printed |
|---|---|
| $0$ | $2$ |
| $1$ | $210$ |
| $2$ | $2480$ |
| $3$ | $8178$ |
| $4$ | $45153$ |
| $5$ | $3648841$ |
| $6$ | $7979090$ |
| $7$ | $101130029$ |
| $8$ | $339949252$ |
| $9$ | $1019547844$ |

The search ran over $k\le2^{30}$ for $n\le9$ (p. 592) and drew the
candidates for $Z_n$ from the elements of $Z_{n-1}$ already found: p. 594
lists the 25 elements of $Z_7$ up to $2^{30}$, of which four lie in $Z_8$
($339949252$, $874906831$, $1019547843$ and $1019547844$), and reports one
element of $Z_9$. The introduction (p. 584) says the computation covers
$0\le n\le8$; Section 3, the table and the abstract cover $n\le9$.

**The rows $n=0$ and $n=1$.** Under the printed definition of $Z_n$ these
rows are not the least elements: $1\in Z_0$, since $1\mid\binom21$, and
$2\in Z_1$, since $2\cdot1\mid\binom42=6$, so $z_0=1$ and $z_1=2$. The
paper's own counts include these elements: Table 5 (p. 593) gives
$Z_0(2^2)=2$ and $Z_1(2^2)=1$, and p. 595 gives $Z_0(2)=2$ and $Z_1(2)=1$,
where $Z_n(x)=|Z_n\cap[1,x]|$.

**Comparison.** The rows $2\le n\le9$ are the terms $a(2)$ to $a(9)$ of the
OEIS entry A375077, the least $n$ with $n(n-1)\cdots(n-k)\mid\binom{2n}{n}$,
that the claim pages of
[[../wiki/problems/factorials_binomials/E0396/_index|Problem 396]] record and
credit to contributors from 2024 to 2026; the paper printed them in 2013. The
entry's $a(1)=2$ is the $z_1$ of the printed definition.

**Proof pointer.** A computer search (pp. 592 and 594): for each candidate
$k$ and each $j\le n$, the primes dividing $k-j$ are found and the
inequality of Theorem 3.1 is tested at each of them. The set $T'_j(k)$ that
p. 594 defines for this test is printed with the expression of Theorem 2.1,
$2s_p(k+n)-s_p(2k+n)-s_p(n)$; the test that Theorem 3.1 supports uses
$3s_p(k)-s_p(2k)-s_p(k-n-1)-(n+1)$.

**Dependencies.**
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_3_1|Theorem 3.1]].

**Read depth.** Claims checked: the table, the account of the search and the
counts used above were read on the page images. No entry was recomputed and
no search was rerun, so the minimality of the rows $2\le n\le9$ rests on the
paper's report, and on the separate searches that the claim pages of Problem
396 record. Nothing here is independently reviewed.

**Bears on.** [[../wiki/problems/factorials_binomials/E0396/_index|#396]]:
the table reports the least $n$ for each of the problem's $k$ from $2$ to
$9$, so each of these instances has an explicit witness, printed in 2013. The
instances $k=0$ and $k=1$ have the witnesses $n=1$ and $n=2$. The problem asks
about every $k$.
