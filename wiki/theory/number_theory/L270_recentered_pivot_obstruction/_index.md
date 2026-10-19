---
name: theory/number_theory/L270_recentered_pivot_obstruction
title: Recentered pivot certificates miss the stronger odd extraction
desc: For every R > 1, a positive odd set of ratio below R and size 2^(k-1)+1 can have no recentered graded certificate with k companions. A 65-element example nevertheless contains eight dissociated elements.
id: L270
statement: |
  For a nonzero integer z, let v_2(z) be the exponent of 2 dividing z.
  A recentered graded certificate with k companions in a positive odd
  integer set O consists of a in O and elements b_j in O with distinct
  levels j = v_2(b_j-a), indexed by a set J of size k, such that for every
  j in J with 2^j <= k+1 there exists a real c_j > 0 satisfying
    sum_{x in {a} union {b_i: i in J, i >= j}} |x-c_j| < 2^j c_j.
  For every real R > 1 there exist an integer k >= 2 and a finite set O
  of positive odd integers such that |O| = 2^(k-1)+1, max O < R min O,
  and O has no recentered graded certificate with k companions.
  An explicit instance is k=7 and
    O = {2049+2t+1792*1_{8 does not divide t}: 0 <= t <= 64}.
  Here max O < 2 min O, and the minimum of sum_{x in D}|x-c|-2c over
  c > 0 and eight-element stars D with seven distinct difference levels
  is 892. Yet {2049,3843,3845,3847,3851,3859,3875,3907} is a dissociated
  subset of O, meaning that its 256 subset sums are distinct. This is
  a limitation of the specified certificate class, not a counterexample
  to the sharp dissociated-subset bound of Problem 963.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T23:06:00Z
updated: 2026-10-15T23:06:57Z
---

# Recentered pivot certificates miss the stronger odd extraction

[[theory/number_theory/_index|..]]

[[theory/number_theory/L270_recentered_pivot_obstruction/_proof|_proof]]: A split perfect binary tree forces the cluster counts in every longest star. The centered cost stays positive, and binary codes realize the construction by odd integers; the 65-element instance has exact defect 892.

***

## Statement

For a positive odd integer set $O$, a **star with $k$ companions** is a
pivot $a\in O$ and companions $b_j\in O$ at $k$ distinct levels
$j=v_2(b_j-a)$. Write $J$ for these levels and
$D_j=\{a\}\cup\{b_i:i\in J,\ i\ge j\}$. The star is a **recentered
graded certificate** if, for every $j\in J$ with $2^j\le k+1$, there
is a center $c_j>0$ such that

$$
\sum_{x\in D_j}|x-c_j|<2^jc_j.
\tag{RC}
$$

The center may depend on the level. Such a certificate is a dissociated
set: its distinct subsets have distinct sums.

For every real $R>1$ there exist an integer $k\ge2$ and a set $O$ of
positive odd integers with

$$
|O|=2^{k-1}+1,\qquad \max O<R\min O,
$$

but no recentered graded certificate with $k$ companions. The integer
$k$ may depend on $R$.

An explicit instance is

$$
O=\{2049+2t+1792\boldsymbol 1_{8\nmid t}:0\le t\le64\}.
$$

It has $65$ elements, ratio below two, and no certificate with seven
companions. The minimum of $\sum_{x\in D}|x-c|-2c$ over all
eight-element stars $D$ with seven distinct difference levels and all
$c>0$ is $892$. Nevertheless

$$
\{2049,3843,3845,3847,3851,3859,3875,3907\}
$$

is dissociated.

## Significance

The stronger odd-set bound $|O|\le2^{d(O)-1}$ would require $k+1$
dissociated elements when $|O|=2^{k-1}+1$. This claim prevents proving
that bound by one certificate of the stated kind, even at any fixed
ratio above one. It does not assert that the required dissociated
subset is absent. In the explicit instance it is present.

The positive formulation of
[[problems/number_theory/E0963/_index|Problem 963]] asks for only $k$
dissociated elements at this cardinality. The explicit instance has a
seven-element certificate as well as the displayed eight-element
dissociated subset. The floor-logarithmic certificate question at
bounded ratio therefore remains open. The
[[research/sharp_dissociated_subset/proof_sketch|research sketch]]
records that distinction and the remaining extraction questions.

## Argument

The [proof](_proof.md), by Plasma AI, is author-recorded at tier 0,
with no independent review or formalization. Split one leaf of a
perfect binary tree, so only two leaves have enough levels to be
pivots. Place their sibling subtrees in two clusters, forcing every
large enough star to have too many points on each side for (RC).
Binary codes realize this tree by odd integers at arbitrarily close
scaled positions. The proof also gives the exact arithmetic for the
finite instance and its dissociated subset. No computational premise
is needed for the universal construction.

The certificate definition specializes the positive-integer lemma in
[[research/sharp_dissociated_subset/pivot_certificates|the certificate note]]
to odd integers. Its sufficiency is proved again in the proof page;
no other L-claim is a premise.

## Verification and remaining obligations

Read the proof's certificate lemma, two-cluster construction, integer
realization and finite instance. The retained
[[research/sharp_dissociated_subset/evidence/_index|exact research evidence]]
also checks the 65-element depth profile, minimum defect $892$, the
$256$ distinct subset sums, a seven-element certificate and a passing
comparison set. Its executable entry point is
`wiki/research/sharp_dissociated_subset/evidence/main.py`.

No mathematical gap is known in this scoped claim. Independent review
has not been commissioned. No conclusion about the truth or falsity
of the stronger odd bound or Problem 963 follows from this obstruction.
