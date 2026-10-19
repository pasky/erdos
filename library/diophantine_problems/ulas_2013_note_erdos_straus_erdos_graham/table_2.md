---
name: diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/table_2
title: Ulas Table 2 — least solutions of the Erdős–Straus divisibility for n up to 20
desc: >
  The least k with (n+1)...(n+k) | (n+k+1)...(n+2k) for n <= 16, and a
  solution not checked to be least for 17 <= n <= 20: witnesses for Problem
  389 at each n from 2 to 21.
created: 2026-10-14T23:03:05Z
updated: 2026-10-14T23:03:05Z
---

***

**Source.** Published p. 590, Table 2 and the paragraph before it; the search
method is on p. 589.

**Statement.** Table 2, headed as the smallest element of $S_n$ with its
factorization, lists a value $k_n$ for each $1\le n\le20$, with $S_n$ the set
defined on
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_2_1|Theorem 2.1]].
For $n\le16$ the paper reports $k_n$ as the least element of $S_n$, computed
with the criterion of Theorem 2.1; for $n=17$ a search over $k\le10^8$ found
no element (p. 590). The rows $17\le n\le20$ carry an asterisk: the paper
found these elements of $S_n$ through Conjecture 3.8 (p. 595), expects them to
be the least, and did not check that. Row $n$ answers Problem 389 at $n+1$:

| Paper's $n$ | Problem 389's $n$ | $k$ |
|---|---|---|
| $1$ | $2$ | $5$ |
| $2$ | $3$ | $4$ |
| $3$ | $4$ | $207$ |
| $4$ | $5$ | $206$ |
| $5$ | $6$ | $2475$ |
| $6$ | $7$ | $984$ |
| $7$ | $8$ | $8171$ |
| $8$ | $9$ | $8170$ |
| $9$ | $10$ | $45144$ |
| $10$ | $11$ | $45143$ |
| $11$ | $12$ | $3648830$ |
| $12$ | $13$ | $3648829$ |
| $13$ | $14$ | $7979077$ |
| $14$ | $15$ | $7979076$ |
| $15$ | $16$ | $58068862$ |
| $16$ | $17$ | $58068861$ |
| $17$ | $18$ | $339949235^*$ |
| $18$ | $19$ | $339949234^*$ |
| $19$ | $20$ | $1019547825^*$ |
| $20$ | $21$ | $1019547824^*$ |

The starred values for $n=17$ and $n=19$ are $z_8-17$ and $z_9-19$ for the
values $z_8$ and $z_9$ of
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/table_4|Table 4]],
and those for $n=18$ and $n=20$ are one less, the pattern of Conjecture 2.11
($k_{2n-1}-1\in S_{2n}$). The abstract (p. 583) states the outcome as a
positive answer to Question 1.1 for each $n\le20$.

**Proof pointer.** A computer search (p. 589): for each candidate $k$ and
each $j\le n$, the primes dividing $k+j$ are found, and the inequality of
Theorem 2.1 is tested at each of them.

**Dependencies.**
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_2_1|Theorem 2.1]];
for the starred rows, Table 4 and Conjecture 3.8 as the means of finding them.

**Read depth.** Claims checked: the table and the account of the search were
read on the page images. No entry was recomputed and no search was rerun, so
the minimality for $n\le16$ and the membership of the starred values rest on
the paper's report. Nothing here is independently reviewed.

**Bears on.** [[../wiki/problems/diophantine_problems/E0389/_index|#389]]:
the table reports a witness $k$ for each of the problem's $n$ from $2$ to
$21$, the least one for $n\le17$; at the problem's $n=1$ every $k$ works.
These are instances only: the problem asks about every $n$.
