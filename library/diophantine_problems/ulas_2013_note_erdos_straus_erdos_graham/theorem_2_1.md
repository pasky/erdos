---
name: diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_2_1
title: Ulas Theorem 2.1 — the digit-sum criterion for the Erdős–Straus divisibility
desc: >
  For positive n and k, (n+1)...(n+k) divides (n+k+1)...(n+2k) exactly when
  every prime p dividing (k+1)...(k+n) has 2s_p(k+n) - s_p(2k+n) - s_p(n) >= 0,
  where s_p is the base-p digit sum.
created: 2026-10-14T23:03:05Z
updated: 2026-10-14T23:03:05Z
---

***

**Source.** Published p. 585, Theorem 2.1; proof p. 586.

**Setting.** For a positive integer $n$, $S_n$ is the set of positive
integers $k$ with

$$
(n+1)(n+2)\cdots(n+k)\mid(n+k+1)(n+k+2)\cdots(n+2k),
$$

and $k_n$ is its least element when it is nonempty. The two products are
$k!\binom{n+k}{n}$ and $k!\binom{2k+n}{k}$, so $k\in S_n$ exactly when
$\binom{n+k}{n}\mid\binom{2k+n}{k}$ (p. 585). For a prime $p$, $s_p(m)$ is the
sum of the base-$p$ digits of $m$.

**Statement.** Let $n$ and $k$ be positive integers. Then $k\in S_n$ if and
only if every prime $p$ dividing $(k+1)(k+2)\cdots(k+n)$ satisfies

$$
2s_p(k+n)-s_p(2k+n)-s_p(n)\ge0.
$$

The print words this as "there exists an integer $k>n$ such that" the
divisibility holds "if and only if" the inequality holds for every prime
dividing $\prod_{i=1}^n(k+i)$, which leaves $k$ free in the second condition.
The proof establishes the criterion above for each given $k$, without using
$k>n$, and the paper applies it that way on p. 589, in the proof of Theorem
2.7 and in its search method.

**Proof sketch.** Multiplying both sides by $n!$, the divisibility
$\binom{n+k}{n}\mid\binom{2k+n}{k}$ becomes
$(k+1)\cdots(k+n)\mid n!\binom{2k+n}{k}$, which holds at every prime not
dividing the left side. At a prime $p$ dividing it, write both $p$-adic
valuations through factorials and apply Legendre's formula
$\nu_p(m!)=(m-s_p(m))/(p-1)$; the comparison reduces to the displayed
inequality. Its left side is $p-1$ times
$\nu_p\binom{2k+n}{k}-\nu_p\binom{n+k}{n}$.

**Dependencies.** Legendre's formula for $\nu_p(m!)$, which the paper cites
from Legendre's *Théorie des nombres* (p. 585).

**Read depth.** Claims checked: the statement was read clause by clause on
the page image, and the proof was followed. Nothing here is independently
reviewed.

**Bears on.** [[../wiki/problems/diophantine_problems/E0389/_index|#389]]:
$S_n$ is the set of $k$ answering the problem at $n+1$, and this criterion is
the test behind the searches of
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/table_2|Table 2]].
