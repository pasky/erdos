---
name: diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_3_1
title: Ulas Theorem 3.1 — the digit-sum criterion for the Erdős–Graham divisibility
desc: >
  For integers n >= 0 and k > n, k(k-1)...(k-n) divides C(2k, k) exactly when
  every prime p dividing that product has 3s_p(k) - s_p(2k) - s_p(k-n-1) >=
  n + 1, where s_p is the base-p digit sum.
created: 2026-10-14T23:03:05Z
updated: 2026-10-14T23:03:05Z
---

***

**Source.** Published p. 592, Theorem 3.1, with its proof.

**Setting.** For an integer $n\ge0$, $Z_n$ is the set of integers $k>n$ with

$$
k(k-1)\cdots(k-n)\mid\binom{2k}{k},
$$

and $z_n$ is its least element when it is nonempty (p. 592); a positive
$k\le n$ makes the product $0$. Since the product for $n+1$ contains the one
for $n$, $Z_{n+1}\subset Z_n$. For a prime $p$, $s_p(m)$ is the sum of the
base-$p$ digits of $m$.

**Statement.** Let $n\ge0$ and $k>n$ be integers. Then $k\in Z_n$ if and only
if every prime $p$ dividing $k(k-1)\cdots(k-n)$ satisfies

$$
3s_p(k)-s_p(2k)-s_p(k-n-1)\ge n+1.
$$

The print words this, as it does Theorem 2.1, as "there exists an integer
$k>n$ such that" the divisibility holds "if and only if" the inequality
holds, with $k$ free in the second condition; the proof and the search method
of p. 594 treat it as the criterion above for each given $k>n$.

**Proof sketch.** Since $k(k-1)\cdots(k-n)=k!/(k-n-1)!$, the divisibility is
equivalent to $k!^3\mid(2k)!\,(k-n-1)!$, which holds at every prime not
dividing the product. At a prime $p$ dividing it, Legendre's formula gives

$$
\nu_p((2k)!)+\nu_p((k-n-1)!)-3\nu_p(k!)
=\frac{3s_p(k)-s_p(2k)-s_p(k-n-1)-(n+1)}{p-1},
$$

so the condition at $p$ is the displayed inequality. Put through Kummer's
theorem, it says that the number of carries when $k$ is added to itself in
base $p$, which is $\nu_p\binom{2k}{k}$, is at least
$\nu_p(k(k-1)\cdots(k-n))$.

**Source note.** The first line of the proof prints $(n-k-1)!$ where
$(k-n-1)!$ is meant, twice.

**Dependencies.** Legendre's formula for $\nu_p(m!)$ (p. 585).

**Read depth.** Claims checked: the statement was read clause by clause on
the page image, and the proof was followed. Nothing here is independently
reviewed.

**Bears on.** [[../wiki/problems/factorials_binomials/E0396/_index|#396]]:
the problem's $k$ and $n$ are the paper's $n$ and $k$, so the paper's $Z_k$ is
the set of solutions of the problem at $k$. The criterion is the digit-sum
form of the check through Kummer's theorem that the problem page describes,
and it drives the search behind
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/table_4|Table 4]].
