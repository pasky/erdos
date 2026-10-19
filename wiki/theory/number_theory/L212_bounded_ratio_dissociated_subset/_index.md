---
name: theory/number_theory/L212_bounded_ratio_dissociated_subset
title: Dissociation bounds from aspect ratio and coefficient imbalance
desc: A positive real set of ratio at most 2 has fewer than 3 times 2^d elements, and ratio at most 4/3 gives the sharp positive bound |P| < 2^d. A quantitative bound also uses the least possible nonzero coefficient sum of a relation.
id: L212
statement: |
  A set B of real numbers is dissociated if distinct finite subsets of B
  have distinct sums, the empty subset with sum 0 included. Let P be a
  nonempty finite set of positive real numbers, let n = |P|, and let
  d(P) be its largest dissociated-subset size. If max P <= 2 min P,
  then n < 3 * 2^d(P). In particular P contains a dissociated subset
  of size at least floor(log_2 n) - 1, with logarithm to base two.
  In addition, let q >= 1 be an integer and theta a rational number with
  0 < theta < q. If max P <= (1 + theta) min P, and every ternary
  relation sum(epsilon_x x) = 0 on P, with epsilon_x in {-1,0,1}, has
  sum(epsilon_x) either zero or of absolute value at least q, then
    n < (q + theta) / (2(q - theta)) * 2^d(P).
  In particular max P <= (4/3) min P implies n <= 2^d(P) - 1.
  No claim is made to resolve Problem 963 for arbitrary finite real sets.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T18:14:21Z
updated: 2026-10-15T22:09:18Z
---

# Dissociation bounds from aspect ratio and coefficient imbalance

[[theory/number_theory/_index|..]]

[[theory/number_theory/L212_bounded_ratio_dissociated_subset/_proof|_proof]]: A discrete Kraft deficiency estimate bounds a positive set in terms of its aspect ratio and the least possible nonzero coefficient sum of a relation. It gives the sharp positive bound at ratio 4/3 and the factor 3 at ratio 2.

***

## Statement

For a finite set $X\subset\mathbb R$ let $d(X)$ be the largest size of a
dissociated subset, a subset whose distinct subsets have distinct sums. If
$P$ is a nonempty finite set of positive reals with $\max P\le2\min P$ and
$n=|P|$, then

$$
n<3\,2^{d(P)},
\qquad\text{hence}\qquad
d(P)>\log_2 n-\log_2 3
\quad\text{and}\quad
d(P)\ge\lfloor\log_2n\rfloor-1.
$$

Every set of two distinct positive reals is dissociated, so $d(P)\ge2$
for $n\ge2$ independently of this bound.

There is also a bound that uses the possible coefficient sums of
relations. Let $q\ge1$ be an integer and $0<\theta<q$ a rational number.
Suppose $\max P\le(1+\theta)\min P$, and every ternary relation
$\sum_{x\in P}\varepsilon_xx=0$ has coefficient sum
$\sum_x\varepsilon_x$ either zero or of absolute value at least $q$.
Then

$$
|P|<\frac{q+\theta}{2(q-\theta)}\,2^{d(P)}.
$$

The relation hypothesis is automatic for $q=1$, and holds for $q=2$
on odd integer sets. Taking $q=1$ and $\theta=1/3$ proves
$|P|\le2^{d(P)}-1$ when $\max P\le\tfrac43\min P$. Thus the exact bound
asked in Problem 963 holds for real sets whose nonzero absolute values
lie within a factor of $4/3$: their symmetric reduction has
$|A|\le2|P|+1\le2^{d(A)+1}-1$. Sets with no nonzero element satisfy the
target directly.

## Significance

[[problems/number_theory/E0963/_index|Problem 963]] asks whether every
$n$-element real set has a dissociated subset of size
$\lfloor\log_2n\rfloor$. Its symmetric reduction replaces a set $A$ by the
positive set $P$ of absolute values of its nonzero elements, with
$d(P)=d(A)$ and $|A|\le2|P|+1$. For sets whose nonzero absolute values lie
within a factor two of each other this claim gives
$d(A)\ge\lfloor\log_2((|A|-1)/2)\rfloor-1$ when $|A|\ge3$, a constant
loss against the asked bound. The tier-2 bound of
[[theory/number_theory/L22_near_logarithmic_dissociated_subset/_index|L22, which loses $\log_2(\log_2n+1)$ for arbitrary real sets]],
is the comparison: in the bounded-ratio regime the loss here does not grow
with $n$. The general consequence, a loss of order
$\log_2\log_2\log_2 n$ for arbitrary sets, is
[[theory/number_theory/L213_triple_log_dissociated_subset/_index|L213, which applies this claim block by block]].

## Argument

The [proof](_proof.md), by Plasma AI, is author-recorded at tier 0. It has
no independent review and no formalization. An integer model reduces the
claim to positive integers. A pivot and companions at distinct difference
valuations are dissociated if their total distance from the pivot is
below $q$ times the pivot, under the stated relation hypothesis. The
truncated cost of $d$ companions is an integral over distance scales,
even at pivots with too
few levels. The Kraft equality and an integer deficiency inequality bound
its mean above by $1+2^d/n$ times the diameter. Failure of extraction
gives a lower mean in terms of $q$ times the minimum divided by the
diameter. Their comparison proves the quantitative bound. At $q=2$ and
ratio two it gives $n<3\,2^{d-1}$ for odd sets; summing valuation layers
proves the factor three. No computational premise is used.

The [[research/sharp_dissociated_subset/proof_sketch|editable proof sketch of the sharp-bound attack]]
places this claim in its route: the claim settles the bounded-ratio
regime up to the constant, and the remaining gaps toward the asked bound
are the combination of different dyadic scales and the last constant.

## Verification and remaining obligations

Read the proof page: its steps are the integer model, the pivot lemma,
the Kraft equality, the integer deficiency estimate, the upper and lower
averages of the same truncated cost, and the valuation-layer sum. No
mathematical gap is known in this statement. Independent review has not
been commissioned; the statement does not resolve Problem 963.
