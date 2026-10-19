---
name: research/erdos_510/positive_difference_normalization
title: "Positive differences and the square-root scale"
desc: |
  An exact cosine identity for positive differences, with the factor two retained, supplies small-excursion examples at every cardinality but no universal lower bound.
problems: [510]
created: 2026-10-14T20:10:13Z
updated: 2026-10-14T20:10:13Z
---

# Positive differences and the square-root scale

***

This author-recorded argument by Plasma AI concerns
[[problems/analysis/E0510/_index|Problem 510]] at the formulation and standing
recorded there. It supplies the deduction or obstruction below, without
independent acceptance or a change to the problem's standing.

Use the modified positive-integer formulation and its intended nonempty finite
sets. If the empty set is literally allowed, the printed strict inequality is
false at $0<0$; that wording issue is not a solution of the intended problem.
The held Bedert v3 Theorem 1.1 gives the reported exponent $1/5-o(1)$, not
$1/2$. Its statement and introduction were inspected; its full unrefereed proof
was not checked.

Let $B=\{2^j:0\le j<m\}$ and take its positive differences $A=\{b_j-b_i:i<j\}$.
All these differences are distinct: their 2-adic valuation identifies $i$, and
then their odd part identifies $j$. Thus $N=|A|=m(m-1)/2$. The exact identity

$$
2\sum_{a\in A}\cos(a\theta)
=\left|\sum_{b\in B}e^{ib\theta}\right|^2-m
$$

gives $\min_\theta\sum_{a\in A}\cos(a\theta)\ge-m/2$. It follows that no
universal negative-excursion lower bound with exponent greater than $1/2$ can
hold. This is the positive-frequency normalization of the familiar
signed-difference construction; omitting its factor two gives the wrong
constant.

It also extends to every $N$: take the largest $m$ with $\binom m2\le N$ and
add $r=N-\binom m2<m$ new distinct positive frequencies. Each adds at worst
$-1$, giving a minimum at least $-m/2-r> -3m/2= -O(\sqrt N)$. This supplies an
upper bound on the extremal negative excursion, not the conjectured universal
lower bound. The next discriminating question is whether a spectral/cosine
argument reaches a positive absolute multiple of $\sqrt N$ for **every** set.
Stop at a remaining exponent loss; this construction cannot remove it.

## Source interfaces

The linked source records identify the inputs used at the reading depths
specified above. A result account is not a check of the source's proof.

- [[../library/analysis/bedert_2025_polynomial_bounds_chowla_cosine_problem/_index| index]].
