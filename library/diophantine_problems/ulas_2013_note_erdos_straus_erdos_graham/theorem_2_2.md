---
name: diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_2_2
title: Ulas Theorem 2.2 — the solution sets for n = 1 and n = 2 are infinite
desc: >
  Infinitely many k = pq - 1, with p and q primes and 3p/2 < q < 2p, have
  k + 1 dividing C(2k+1, k), and k - 1 then solves the case n = 2, so
  Problem 389 has infinitely many solutions at its n = 2 and n = 3.
created: 2026-10-14T23:03:05Z
updated: 2026-10-14T23:03:05Z
---

***

**Source.** Published p. 586, Theorem 2.2; proof pp. 586–587.

**Statement.** With $S_n$ as on
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_2_1|Theorem 2.1]]:
(1) $S_1$ is infinite; (2) if $k\in S_1$, then $k-1\in S_2$, so $S_2$ is
infinite too. Here $k\in S_1$ means $(k+1)\mid\binom{2k+1}{k}$, and
$k\in S_2$ means $\binom{k+2}{2}\mid\binom{2k+2}{k}$.

**Proof sketch.** (1) Take a prime $p>5$ for which some prime $q$ satisfies
$3p/2<q<2p$; the print invokes a generalized Bertrand postulate, and every
large $p$ qualifies. Put $k=pq-1$. By Theorem 2.1 with $n=1$ it is enough
that $2s_r(pq)-s_r(2pq-1)-1\ge0$ for $r=p$ and $r=q$. In base $p$ the digits
of $pq$ are $1,q-p,0$ and those of $2pq-1$ are $3,2q-3p-1,p-1$, which are
digits because $3p/2<q<2p$ and $p>5$; in base $q$ the digits of $pq$ are
$p,0$ and those of $2pq-1$ are $1,2p-q-1,q-1$. Both expressions equal $0$, so
$k\in S_1$, and distinct $p$ give distinct $k$.

(2) Let $k\in S_1$; then $k\ge2$, since $2$ does not divide $\binom31$.
Multiplying $(k+1)\mid\binom{2k+1}{k}$ by $k$ and using
$k\binom{2k+1}{k}=(2k+1)\binom{2k}{k-1}$ gives
$k(k+1)\mid(2k+1)\binom{2k}{k-1}$. As $(2k+1)^2-4k(k+1)=1$, the factor
$2k+1$ is prime to $k(k+1)$, so $k(k+1)\mid\binom{2k}{k-1}$. A fortiori
$\binom{k+1}{2}\mid\binom{2(k-1)+2}{k-1}$, which says that $k-1\in S_2$.

**Source note.** The last line of the proof of (2) prints
$C(2(k-1)+1,k-1)$ where $C(2(k-1)+2,k-1)=\binom{2k}{k-1}$, the coefficient
the argument has reached, is meant.

**Dependencies.**
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_2_1|Theorem 2.1]]
for (1), and a prime in $(3p/2,2p)$ for infinitely many primes $p$.

**Read depth.** Claims checked: the statement was read clause by clause on
the page image, and the digit computations of the proof were followed.
Nothing here is independently reviewed.

**Bears on.** [[../wiki/problems/diophantine_problems/E0389/_index|#389]]:
the problem's $n=2$ and $n=3$ are the paper's $S_1$ and $S_2$, so each has
infinitely many solutions $k$; the least are $5$ and $4$, as
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/table_2|Table 2]]
reports. The paper also derives
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_3_2|Theorem 3.2]]
from (1).
