---
name: problems/additive_bases/E0345
title: Problem 345
desc: |
  Asks whether infinitely many $k$ make the completeness threshold of the $k$th
  powers larger than that of the $(k+1)$th powers, $T(n^k)>T(n^{k+1})$.
tags:
- Number theory
- Complete sequences
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 345

[[problems/additive_bases/_index|..]]

***

**Statement.** Let $A\subseteq \mathbb{N}$ be a complete sequence, and define
the threshold of completeness $T(A)$ to be the least integer $m$ such that all
$n\geq m$ are in

$$
P(A) = \left\{\sum_{n\in B}n : B\subseteq A\textrm{ finite }\right\}
$$

(the existence of $T(A)$ is guaranteed by completeness).

Is it true that there are infinitely many $k$ such that $T(n^k)>T(n^{k+1})$?

**Status.** Open.

**Source.** [erdosproblems.com/345](https://www.erdosproblems.com/345), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #345,
https://www.erdosproblems.com/345.

**References.**

- [ErGr80] Erdős, P. and Graham, R., Old and new problems and results in
  combinatorial number theory. Monographies de L'Enseignement Mathematique
  (1980).

**Formalization.** None recorded.

## Current assessment

The successive-exponent comparison remains unresolved. The powers-of-two
congruence mechanism in the
[[../library/number_theory/erdos_1980_old_new_problems_results_combinatorial_number_theory/_index|Erdős–Graham completeness discussion]]
has the following explicit author-recorded consequence by Plasma AI. Write
$T(k)=T(\{1^k,2^k,\ldots\})$. For $t\ge2$, put $k=2^t$ and $q=4k$.
Every odd integer $b$ has $b^k\equiv1\pmod q$: start with
$b^2\equiv1\pmod8$ and square successively. Every even $b$ has
$b^k\equiv0\pmod q$, since $2^t\ge t+2$.

A sum of distinct $k$th powers congruent to $-1\pmod q$ must therefore
contain at least $q-1$ odd powers. Its size is at least
$S_k=\sum_{j=1}^{q-1}(2j-1)^k$. The positive integer $S_k-q$ has the same
residue and is smaller, so it is not representable. Consequently

$$
T(2^t)\ge
\sum_{j=1}^{2^{t+2}-1}(2j-1)^{2^t}-2^{t+2}+1\qquad(t\ge2).
$$

No threshold search is needed for this deduction. To establish infinitely many
drops by this route one still needs an upper bound for $T(2^t+1)$ below this
lower bound along infinitely many $t$. Neither the formula nor finitely many
exact thresholds provides that comparison. The account is a partial deduction
from the held congruence idea, without independent review or a new complete
literature search.
