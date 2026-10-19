---
name: diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_3_2
title: Ulas Theorem 3.2 — infinitely many k divide the central binomial coefficient
desc: >
  Every k in S_1 gives k + 1 dividing C(2k+2, k+1), so infinitely many k
  divide C(2k, k); Corollary 3.3 restates this as k dividing the Catalan
  number C_k for infinitely many k.
created: 2026-10-14T23:03:05Z
updated: 2026-10-14T23:03:05Z
---

***

**Source.** Published p. 592, Theorem 3.2, with its proof; Corollary 3.3 on
p. 593.

**Statement.** $S_1+1\subset Z_0$, with $S_1$ as on
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_2_1|Theorem 2.1]]
and $Z_0$ as on
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_3_1|Theorem 3.1]]:
if $(k+1)\mid\binom{2k+1}{k}$, then $(k+1)\mid\binom{2k+2}{k+1}$. In
particular $Z_0$, the set of positive $k$ with $k\mid\binom{2k}{k}$, is
infinite.

**Corollary 3.3** (p. 593). With $C_k=\binom{2k}{k}/(k+1)$ the $k$th Catalan
number, $C_k\equiv0\pmod k$ for infinitely many $k$.

**Proof sketch.** Since $\binom{2k+2}{k+1}=2\binom{2k+1}{k}$, the number $k+1$
divides the former whenever it divides the latter, and
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_2_2|Theorem 2.2]]
(1) makes $S_1$, and hence $Z_0$, infinite. The paper states the corollary
without a separate proof. It follows because $\binom{2k}{k}=(k+1)C_k$ and $k$
is prime to $k+1$, so $k\mid\binom{2k}{k}$ exactly when $k\mid C_k$.

**Dependencies.**
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_2_2|Theorem 2.2]]
(1).

**Read depth.** Claims checked: the theorem and the corollary were read
clause by clause on the page images, and the proof was followed. Nothing here
is independently reviewed.

**Connections.** A remark after the statement of Theorem 3 in
[[factorials_binomials/pomerance_2015_divisors_middle_binomial_coefficient/_index|Pomerance's 2015 paper]]
cites this theorem and
[[diophantine_problems/ulas_2013_note_erdos_straus_erdos_graham/theorem_3_4|Theorem 3.4]]
for the infinitude of the $n$ with $n\mid\binom{2n}{n}$ and of the $n$ with
$n\nmid\binom{2n}{n}$.

**Bears on.** [[../wiki/problems/factorials_binomials/E0396/_index|#396]]:
the problem's instance $k=0$ asks for some $n$ with $n\mid\binom{2n}{n}$.
The solution $n=1$ already answers it; this theorem gives infinitely many
solutions, as does
[[factorials_binomials/pomerance_2015_divisors_middle_binomial_coefficient/theorem_3|Pomerance's Theorem 3]]
at $k=0$.
