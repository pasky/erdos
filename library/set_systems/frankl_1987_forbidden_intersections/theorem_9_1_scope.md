---
name: set_systems/frankl_1987_forbidden_intersections/theorem_9_1_scope
title: Theorem 9.1 — a limitation of the printed metric claim
desc: >
  Records an explicit obstruction and the exact feasible-array consequence
  that remains valid.
created: 2026-09-05T14:25:21Z
updated: 2026-10-13T04:56:43Z
---
***

**Source.** Published p. 282, Theorem 9.1 and its preceding remark
(PDF).

The source defines $mS+b$ on the same points as $S\subseteq H(t,q)$
by replacing each distance between distinct points by $m d+b$. It then
asserts that if $m,b>\eta n$ and $mt+b<(1-\eta)n$, every sufficiently
dense subset of $H(n,q)$ contains an isometric copy. No proof is given
beyond the preceding positive-pattern discussion. With that literal
metric definition and those unrestricted hypotheses, the assertion has
the following obstruction; it is not certified in this compilation.

**Obstruction.** For every positive integer $u$, take

$$
q=2,\quad S=H(2,2),\quad n=100u,\quad
m=10u,\quad b=65u,\quad \eta=9/100.
$$

All the printed strict size inequalities hold, but $mS+b$ does not
embed even in the full binary cube $H(n,2)$.

**Proof.** Among the six unordered pairs of the four points of
$H(2,2)$, four have distance one and two have distance two. Their
transformed distances sum to

$$
4(10u+65u)+2(20u+65u)=470u.
$$

For any four binary words, a fixed coordinate splits the four words
into classes of sizes $a$ and $4-a$ and contributes $a(4-a)\le4$
to the sum of their six pairwise distances. Across $100u$ coordinates
the sum is therefore at most $400u$. The required sum is impossible.
The hypotheses hold because $10u,65u>9u$ and $20u+65u<91u$.
$\square$

**What the pattern theorem does prove.** Given a dense family in a
specified type class, and a compatible positive joint array for $r$
words with every cell at least a fixed positive proportion of $n$,
Theorem 1.16 realizes that entire array. The pairwise distances are
then obtained by summing the cells in which the corresponding two
letter indices differ. This is the precise feasible-array consequence
stated in the preceding source remark. The simple size conditions in
Theorem 9.1 do not by themselves establish such feasibility, as the
obstruction shows. This compilation-supplied observation is not an
author-issued erratum and does not affect Theorems 1.10 or 1.16.

**Dependencies.**
[[set_systems/frankl_1987_forbidden_intersections/theorem_1_16]].
